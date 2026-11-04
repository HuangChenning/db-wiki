---
title: "管理WAL日志文件"
book: "管理员指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeTwo7.html"
tags:
  - highgo
  - highgo-v9
  - safety-administrator-guide
---

## 数据库监控

数据库管理员常常会疑惑，”系统正在做什么？”这一章会深入讨论这个问题。

一些工具可以用来监控数据库活动并且分析性能。这一章的大部分都致力于描述瀚高数据库的统计收集器，但是我们也不能忽视常规的Unix监控程序，如ps、top、iostat和vmstat。另外一旦我们发现了一个性能差的查询，可能需要瀚高数据库的EXPLAIN命令来进行进一步的调查。

## 标准Unix工具

在大部分Unix平台上，瀚高数据库会修改由ps报告的命令标题，这样个体服务器进程可以被标识。一个显示样例是

$ ps auxww | grep ^postgres

postgres 15551 0.0 0.1 57536 7132 pts/0 S 18:02 0:00 postgres -i

postgres 15554 0.0 0.0 57536 1184? Ss 18:02 0:00 postgres:

background writer

postgres 15555 0.0 0.0 57536 916? Ss 18:02 0:00 postgres:

checkpointer

postgres 15556 0.0 0.0 57536 916? Ss 18:02 0:00 postgres:

walwriter

postgres 15557 0.0 0.0 58504 2244? Ss 18:02 0:00 postgres:

autovacuum launcher

postgres 15558 0.0 0.0 17512 1068? Ss 18:02 0:00 postgres:

stats collector

postgres 15582 0.0 0.0 58772 3080? Ss 18:04 0:00 postgres: joe

runbug 127.0.0.1 idle

postgres 15606 0.0 0.0 58772 3052? Ss 18:07 0:00 postgres: tgl

regression \[local\] SELECT waiting

postgres 15610 0.0 0.0 58772 3056? Ss 18:07 0:00 postgres: tgl

regression \[local\] idle in transaction

（ps的调用方式随不同的平台而变，但是显示的细节都差不多。这个例子来自于一个最近的Linux系统）。列在这里的第一个进程是主服务器进程。显示的命令参数是当数据库启动时使用的那些。接下来的五个进程是由主进程自动启动的后台工作者进程（如果你已经设置系统为不启动统计收集器，”统计收集器”进程将不会出现；同样”自动清理发动”进程也可以被禁用）。剩余的每一个进程都是一个处理一个客户端连接的服务器进程。每个这种进程都会把它的命令行显示设置为这种形式postgres: user database host activity在该客户端连接的生命期中，用户、数据库以及（客户端）主机项保持不变，但是活动指示器会改变。活动可以是闲置（即等待一个客户端命令）、在事务中闲置（在一个BEGIN块里等待客户端）或者一个命令类型名，例如SELECT。还有如果服务器进程正在等待一个其它会话持有的锁，等待中会被追加到上述信息中。在上面的例子中，我们可以推断：

进程15606正在等待进程15610完成其事务并且因此释放一些锁（进程 15610必定是阻塞者，因为没有其他活动会话。在更复杂的情况中，可能需要查看pg\_locks系统视图来决定谁阻塞了谁）。

如果配置了cluster\_name，则集簇的名字 也将会显示在ps的输出中：

$ psql -c 'SHOW cluster\_name'

cluster\_name

\--------------

server1

(1 row)

$ ps aux|grep server1

postgres 27093 0.0 0.0 30096 2752? Ss 11:34 0:00 postgres:

server1: background writer

...

如果你已经关闭了update\_process\_title，那么活动指示器将不会被更新，进程标题仅在新进程被启动的时候设置一次。在某些平台上这样做可以为每个命令节省资源，但在其它平台上却不明显。

Solaris需要特别的处理。你必需使用/usr/ucb/ps而不是/bin/ps。你还必需使用两个w标志，而不是一个。另外你对postgres命令的最初调用必须用一个比服务器进程提供的短的ps状态显示。如果你没有满足全部三个要求，每个服务器进程的ps输出将是原始的postgres命令行。

## 统计收集器

瀚高数据库的统计收集器是一个支持收集和报告服务器活动信息的子系统。 目前这个收集器可以对表和索引的访问计数，可以按磁盘块和记录行来进行计数。它还跟踪每个表中的总行数、每个表的清理和分析动作的信息。它也统计调用用户定义函数的次数以及在每次调用中花费的总时间。

瀚高数据库也支持报告有关系统正在干什么的动态信息，例如当前正在被其他服务器进程执行的命令以及系统中存在哪些其他连接。这个功能是独立于收集器进程存在的。

### 统计收集配置

因为统计收集给查询执行增加了一些负荷，系统可以被配置为收集或不收集信息。这由配置参数控制，它们通常在postgresql.conf中设置。

参数track\_activities允许监控当前被任意服务器进程执行的命令。

参数track\_counts控制是否收集关于表和索引访问的统计信息。

参数track\_functions启用对用户定义函数使用的跟踪。

参数track\_io\_timing启用对块读写次数的监控。

参数 track\_wal\_io\_timing 启用WAL写时间的监控。

通常这些参数被设置在postgresql.conf中，这样它们会应用于所有服务器进程，但是可以在单个会话中使用SET命令打开或关闭它们（为了阻止普通用户对管理员隐藏他们的活动，只有超级用户被允许使用SET来改变这些参数）。

统计收集器通过临时文件将收集到的信息传送给其他瀚高数据库进程。这些文件被存储在名字由stats\_temp\_directory参数指定的目录中，默认是pg\_stat\_tmp。为了得到更好的性能，stats\_temp\_directory可以被指向一个基于RAM的文件系统来降低物理I/O需求。当服务器被干净地关闭时，一份统计数据的永久拷贝被存储在pg\_stat子目录中，这样在服务器重启后统计信息能被保持。当在服务器启动时执行恢复时（例如立即关闭、服务器崩溃以及时间点恢复之后），所有统计计数器会被重置。

### 查看统计信息

表 8.1中列出了一些预定义视图可以用来显示系统的当前状态。表8.2中列出了另一些视图可以显示统计收集的结果。你也可以使用底层统计函数（在第8.2.22讨论）来建立自定义的视图。

在使用统计信息监控收集到的数据时，必须了解这些信息并非是实时更新的。每个独立的服务器进程只在进入闲置状态之前才向收集器传送新的统计计数；因此正在进行的查询或事务并不影响显示出来的总数。同样，收集器本身也最多每PGSTAT\_STAT\_INTERVAL毫秒（缺省为500ms）发送一次新的报告。因此显示的信息总是落后于实际活动。但是由track\_activities收集的当前查询信息总是最新的。

另一个重点是当一个服务器进程被要求显示任何这些统计信息时，它首先取得收集器进程最近发出的报告并且接着为所有统计视图和函数使用这个快照，直到它的当前事务的结尾。因此只要你继续当前事务，统计数据将会一直显示静态信息。当任何关于会话的查询的信息在一个事务中第一次被请求时，这样的信息将被收集。并且在整个事务期间将显示相同的信息。这是一种特性而非缺陷，因为它允许你在该统计信息上执行多个查询并且关联结果而不用担心那些数字会在你不知情的情况下改变。但是如果你希望用每个查询都看到新结果，要确保在任何事务块之外做那些查询。或者可以调用pg\_stat\_clear\_snapshot()，那将丢弃当前事务的统计快照（如果有）。下一次对统计性信息的使用将导致获取一个新的快照。

一个事务也可以在视图pg\_stat\_xact\_all\_tables、pg\_stat\_xact\_sys\_tables、pg\_stat\_xact\_user\_tables和pg\_stat\_xact\_user看到它自己的统计信息（还没有被传送给收集器）。这些数字并不像上面所述的那样行动，相反它们在事务期间持续被更新。

表8.1中显示的动态统计视图中的一些信息是有安全限制的。普通用户只能看到关于他们自己的会话的所有信息（属于他们是成员的角色的会话）。在关于其他会话的行中，许多列将为空。但是请注意，一个会话的存在和它的一般属性，例如会话用户和数据库，对所有用户都是可见的。超级用户和内置角色pg\_read\_all\_stats的成员可以看到所有会话的所有信息。

表 8.1. 动态统计视图

| 视图名称 | 描述 |
| --- | --- |
| pg\_stat\_activity | 每个服务器进程一行，显示与那个进程的当前活动相关的信息，例如状态和当前查询。详见pg\_stat\_activity 。 |
| pg\_stat\_replication | 每一个 WAL 发送进程一行，显示有关到该发送进程连接的后备服务器的复制的统计信息。详见pg\_stat\_replication。 |
| pg\_stat\_wal\_receiver | 只有一行，显示来自 WAL 接收器所连接服务器的有关该接收器的统计信息。详见pg\_stat\_wal\_receiver。 |
| pg\_stat\_subscription | 每个订阅至少一行，显示有关该订阅的工作者的信息。详见 pg\_stat\_subscription。 |
| pg\_stat\_ssl | 每个连接（常规的或者复制）一行，显示在这个连接上使用的SSL的信息。详见pg\_stat\_ssl。 |
| pg\_stat\_gssapi | 每个连接（常规和复制）有一行，显示关于GSSAPI验证和加密的信息。详情请参阅 pg\_stat\_gssapi。 |
| pg\_stat\_progress\_analyze | 每个运行ANALYZE的后端(包括自动清理工作者进程)的行，显示当前进度。参见第8.4.1节。 |
| pg\_stat\_progress\_create\_index | 每个后台运行CREATE INDEX或REINDEX的后端都有一行，显示当前的进度。参见第8.4.2节。 |
| pg\_stat\_progress\_vacuum | 每个运行着VACUUM的后端（包括autovacuum 工作者进程）一行，显示当前的进度。详见第8.4.3节。 |

---

表8.2已收集统计信息的视图

| **视图名称** | **描述** |
| --- | --- |
| pg\_stat\_archiver | 仅一行，显示WAL归档器进程活动的统计信息。详情请参阅pg\_stat\_archiver。 |
| pg\_stat\_bgwriter | 仅一行，显示后台写入程序进程活动的统计信息。详情请参阅pg\_stat\_bgwriter。 |
| pg\_stat\_wal | 仅一行，显示WAL活动的统计信息。详情请参阅pg\_stat\_wal。 |
| pg\_stat\_database | 每个数据库一行，显示数据库范围的统计信息。详情请参阅pg\_stat\_database。 |
| pg\_stat\_database\_conflicts | 每个数据库一行，显示与在备用服务器上的恢复冲突取消查询的数据库范围的统计信息。详情请参阅pg\_stat\_database\_conflicts。 |
| pg\_stat\_all\_tables | 当前数据库中每个表一行，显示有关访问该特定表的统计信息。详情请参阅pg\_stat\_all\_tables。 |
| pg\_stat\_sys\_tables | 与pg\_stat\_all\_tables相同，只是只显示系统表。 |
| pg\_stat\_user\_tables | 与pg\_stat\_all\_tables相同，只是只显示用户表。 |
| pg\_stat\_xact\_all\_tables | 类似于pg\_stat\_all\_tables，但仅计算当前事务中已执行的操作（尚未包含在pg\_stat\_all\_tables及相关视图中）。此视图中不包含有关活跃行数和死元组数以及清理和分析操作的列。 |
| pg\_stat\_xact\_sys\_tables | 与pg\_stat\_xact\_all\_tables相同，只是只显示系统表。 |
| pg\_stat\_xact\_user\_tables | 与pg\_stat\_xact\_all\_tables相同，只是只显示用户表。 |
| pg\_stat\_all\_indexes | 当前数据库中每个索引一行，显示有关访问该特定索引的统计信息。详情请参阅pg\_stat\_all\_indexes。 |
| pg\_stat\_sys\_indexes | 与pg\_stat\_all\_indexes相同，只是只显示系统表上的索引。 |
| pg\_stat\_user\_indexes | 与pg\_stat\_all\_indexes相同，只是只显示用户表上的索引。 |
| pg\_statio\_all\_tables | 当前数据库中每个表一行，显示有关该特定表的I/O统计信息。详情请参阅pg\_statio\_all\_tables。 |
| pg\_statio\_sys\_tables | 与pg\_statio\_all\_tables相同，只是只显示系统表。 |
| pg\_statio\_user\_tables | 与pg\_statio\_all\_tables相同，只是只显示用户表。 |
| pg\_statio\_all\_indexes | 当前数据库中每个索引一行，显示有关该特定索引的I/O统计信息。详情请参阅pg\_statio\_all\_indexes。 |
| pg\_statio\_sys\_indexes | 与pg\_statio\_all\_indexes相同，只是只显示系统表上的索引。 |
| pg\_statio\_user\_indexes | 与pg\_statio\_all\_indexes相同，只是只显示用户表上的索引。 |
| pg\_statio\_all\_sequences | 当前数据库中每个序列一行，显示有关该特定序列的I/O统计信息。详情请参阅pg\_statio\_all\_sequences。 |
| pg\_statio\_sys\_sequences | 与pg\_statio\_all\_sequences相同，只是只显示系统序列。 (当前，未定义系统序列，因此此视图始终为空。) |
| pg\_statio\_user\_sequences | 与pg\_statio\_all\_sequences相同，只是只显示用户序列。 |
| pg\_stat\_user\_functions | 每个跟踪函数一行，显示有关该函数执行的统计信息。详情请参阅pg\_stat\_user\_functions。 |
| pg\_stat\_xact\_user\_functions | 类似于pg\_stat\_user\_functions，但仅计算当前事务中的调用（尚未包含在pg\_stat\_user\_functions中）。 |
| pg\_stat\_slru | 每个SLRU一行，显示操作的统计信息。详情请参阅pg\_stat\_slru。 |
| pg\_stat\_replication\_slots | 每个复制插槽一行，显示有关复制插槽使用情况的统计信息。详情请参阅pg\_stat\_replication\_slots。 |
| pg\_stat\_progress\_cluster | 每个运行着CLUSTER或VACUUM FULL的后端一行，显示当前进度。参见第8.4.4节。 |
| pg\_stat\_progress\_basebackup | 每一个WAL发送者进程的行显示一个基础备份，显示当前进度。参见第8.4.5节。 |
| pg\_stat\_progress\_copy | 对每个后端运行COPY的行,显示当前进度。参见第2.4.6节。 |

每个索引的统计信息特别有用，可以确定哪些索引正在使用以及它们的效果如何。

pg\_statio\_视图主要用于确定缓冲区缓存的效果。当实际磁盘读取的数量远远小于缓冲区命中的数量时，缓存会满足大部分读取请求而不需要调用内核。然而，这些统计数据并不能完全说明问题：由于瀚高数据库处理磁盘I/O的方式，未在瀚高数据库缓冲区缓存中的数据可能仍然驻留在内核的I/O缓存中，因此仍然可以在不需要物理读取的情况下获取。有兴趣获取有关瀚高数据库I/O行为更详细信息的用户建议使用瀚高数据库统计收集器结合操作系统工具，这些工具允许查看内核对I/O的处理方式。

### pg\_stat\_activity

pg\_stat\_activity视图将每个服务器进程显示为一行，显示与该进程当前活动相关的信息。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| datid | oid | 这个后端连接到的数据库的OID |
| datname | name | 这个后端连接到的数据库的名称 |
| pid | datname | name |
| usesysid | oid | 登录到这个后端的用户的OID |
| usename | name | 登录到这个后端的用户的名称 |
| application\_name | text | 连接到这个后端的应用的名称 |
| client\_addr | inet | 连接到这个后端的客户端的IP 地址。如果这个域为空，它表示客户端通过服务器机器上的一个 Unix 套接字连接或者这是一个内部进程（如 自动清理）。 |
| client\_hostname | text | 已连接的客户端的主机名，由client\_addr的反向DNS查找报告。这个域将只对IP连接非空，并且只有log\_hostname被启用时才会非空。 |
| client\_port | integer | 客户端用以和这个后端通信的TCP端口号，如果使用Unix 套接字则为-1 |
| backend\_start | timestamp with time zone | 这个进程被启动的时间。对客户端后端来说就是客户端连接到服务器的时间。 |
| xact\_start | timestamp with time zone | 这个进程的当前事务被启动的时间，如果没有活动事务则为空。如果当前查询是它的第一个事务，这一列等于query\_start。 |
| query\_start | timestamp with time zone | 当前活动查询被开始的时间，如果state不是active，这个域为上一个查询被开始的时间 |
| state\_change | timestamp with time zone | state上一次被改变的时间 |
| wait\_event\_type | text | 后端正在等待的事件类型，如果不存在则为NULL。可能的值有： LWLock：后端正在等待一个轻量级锁。每一个这样的锁保护着共享内存中的一个特殊数据结构。wait\_event将含有一个标识该轻量级锁目的的名称（一些锁具有特定的名称，其他是一组具有类似目的的锁中的一部分）。Lock：后端正在等待一个重量级锁。重量级锁，也称为锁管理器锁或者简单锁，主要保护SQL可见的对象，例如表。不过它们也被用于确保特定内部操作的互斥，例如关系扩展。wait\_event将标识等待的锁的类型。BufferPin：服务器进程正在等待访问一个数据缓冲区，而此时没有其他进程正在检查该缓冲区。如果另一个进程持有一个最终从要访问的缓冲区中读取数据的打开的游标，缓冲区pin等待可能会被拖延。Activity：服务器进程处于闲置状态。这被用于在其主处理循环中等待活动的系统进程。wait\_event将标识特定的等待点。 Extension：服务器进程正在一个扩展模块中等待活动。这一个分类被用于要跟踪自定义等待点的模块。Client：服务器进程正在一个套接字上等待来自用户应用的某种活动，并且该服务器预期某种与其内部处理无关的事情发生。wait\_event将标识特定的等待点。IPC：服务器进程正在等待来自服务器中另一个进程的某种活动。wait\_event将标识特定的等待点。 Timeout：服务器进程正在等待一次超时发生。wait\_event将标识特定的等待点。 IO：服务器进程正在等待一次IO完成。wait\_event将标识特定的等待点。 |
| wait\_event | text | 如果后端当前正在等待，则是等待事件的名称，否则为NULL。详见表12.4。 |
| state | text | 这个后端的当前总体状态。可能的值是： active：后端正在执行一个查询。 idle：后端正在等待一个新的客户端命令。 idle in transaction：后端在一个事务中，但是当前没有正在执行一个查询。 idle in transaction (aborted)：这个状态与idle in transaction相似，不过在该事务中的一个语句导致了一个错误。 fastpath function call：后端正在执行一个fast- path函数。 disabled：如果在这个后端中track\_activities被禁用，则报告这个状态。 |
| backend\_xid | xid | 这个后端的顶层事务标识符（如果存在）。 |
| backend\_xmin | xid | 当前后端的xmin范围。 |
| query | text | 这个后端最近查询的文本。如果state为active，这个域显示当前正在执行的查询。在所有其他状态下，它显示上一个被执行的查询。默认情况下，查询文本会被截断至1024个字符，这个值可以通过参数track\_activity\_query\_size更改。 |
| backend\_type | text | 当前后端的类型。可能的类型是 autovacuum launcher, autovacuum worker, logical replication launcher, logical replication worker,parallel worker, background writer, client backend,checkpointer, startup,walreceiver, walsender以及walwriter。除此以外，由扩展注册的后台Worker可能有额外的类型。 |

---

| **等待时间类型** | **等待事件名称** | **描述** |
| --- | --- | --- |
| LWLock | ShmemIndexLock | 正等待在共享内存中查找或者分配空间 |
| OidGenLock | 正等待分配或者赋予一个OID |  |
| XidGeLock | 正等待分配或者赋予一个事务 ID。 |  |
| ProcArrayLock | 正等待在事务结尾得到一个快照或者清除事务 ID |  |
| SInvalReadLock | 正等待从共享无效消息队列中检索或者移除消息 |  |
| SInvalWriteLock | 正等待在共享无效消息队列中增加一个消息 |  |
| WALBufMappingLock | 正等待在 WAL 缓冲区中替换一个页面 |  |
| WALWriteLock | 正等待 WAL 缓冲区被写入到磁盘 |  |
| ControlFileLock | 正等待读取或者更新控制文件或创建一个新的WAL 文件。 |  |
| CheckpointLock | 正等待执行检查点 |  |
| CLogControlLock | 正等待读取或者更新事务状态 |  |
| SubtransControlLock | 正等待读取或者更新子事务信息 |  |
| MultiXactGenLock | 正等待读取或者更新共享多事务状态 |  |
| MultiXactOffsetControlLock | 正等待读取或者更新多事务偏移映射 |  |
| MultiXactMemberControlLock | 正等待读取或者更新多事务成员映射 |  |
| RelCacheInitLock | 正等待读取或者写入关系缓冲区初始化文件 |  |
| CheckpointerCommLock | 正等待管理 fsync 请求 |  |
| TwoPhaseStateLock | 正等待读取或者更新预备事务的状态 |  |
| TablespaceCreateLock | 正等待创建或者删除表空间 |  |
| BtreeVacuumLock | 正等待读取或者更新一个 B- 树索引的 vacuum 相关的信息。 |  |
| AddinShmemInitLock | 正等待管理共享内存中的空间分配 |  |
| AutovacuumLock | 自动清理工作者或者启动器正等待更新或者读取自动清理工作者的当前状态 |  |
| AutovacuumScheduleLock | 正等待确认选中进行清理的表仍需要清理 |  |
| SyncScanLock | 正等待为同步扫描得到一个表上扫描的开始位置 |  |
| RelationMappingLock | 正等待更新用来存储目录到文件节点映射的关系映射文件。 |  |
| AsyncCtlLock | 正等待读取或者更新共享通知状态 |  |
| AsyncQueueLock | 正等待读取或者更新通知消息 |  |
| SerializableXactHashLock | 正等待检索或者存储有关可序列化事务的信息 |  |
| SerializableFinishedListLock | 正等待访问已结束可序列化事务的列表 |  |
| SerializablePredicateLockListLock | 正等待在由可序列化事务持有的所列表上执行一个操作。 |  |
| OldSerXidLock | 正等待读取或者记录冲突的可序列化事务 |  |
| SyncRepLock | 正等待读取或者更新有关同步复制的信息 |  |
| BackgroundWorkerLock | 正等待读取或者更新后台工作者状态 |  |
| DynamicSharedMemoryControlLock | 正等待读取或者更新动态共享内存状态 |  |
| AutoFileLock | 正等待更新postgresql.auto.conf文件。 |  |
| ReplicationSlotAllocationLock | 正等待分配或者释放一个复制槽。 |  |
| ReplicationSlotControlLock | 正等待读取或者更新复制槽状态 |  |
| CommitTsControlLock | 正等待读取或者更新事务提交时间戳 |  |
| CommitTsLock | 正等待读取或者更新事务时间戳的最新设置值 |  |
| ReplicationOriginLock | 正等待设置、删除或者使用复制源头 |  |
| MultiXactTruncationLock | 正等待读取或者阶段多事务信息 |  |
| OldSnapshotTimeMapLock | 正等待读取或者更新旧的快照控制信息 |  |
| LogicalRepWorkerLock | 正等待逻辑复制工作者上的动作完成 |  |
| CLogTruncationLock | 等待执行txid\_status或更新可用的最新事务id |  |
| clog | 正在等地clog (事务状态)缓冲区上的I/O |  |
| commit\_timestamp | 正等待提交时间戳缓冲区上的 I/O |  |
| subtrans | 正等待子事务缓冲区上的 I/ O。 |  |
| multixact\_offset | 正等待多事务偏移缓冲区上的 I/O。 |  |
| multixact\_member | 正等待多事务成员缓冲区上的 I/O |  |
| async | 正等待 async（通知）缓冲区上的 I/O |  |
| oldserxid | 正等待 oldserxid 缓冲区上的 I/O |  |
| wal\_insert | 正等待把 WAL 插入到一个内存缓冲区 |  |
| buffer\_content | 正等待读取或者写入内存中的一个数据页 |  |
| buffer\_io | 正等待一个数据页面上的 I/ O |  |
| replication\_origin | 正等待读取或者更新复制进度 |  |
| replication\_slot\_io | 正等待一个复制槽上的 I/O |  |
| proc | 正等待读取或者更新fast- path 锁信息 |  |
| buffer\_mapping | 正等待把一个数据块与缓冲池中的一个缓冲区关联。 |  |
| lock\_manager | 正等待增加或者检查用于后端的锁，或者正等待加入或者退出一个锁定组（并行查询使用） |  |
| predicate\_lock\_manager | 正等待增加或者检查谓词锁信息 |  |
| serializable\_xact | 等待在并行查询中对一个可序列化事务执行操作 |  |
| parallel\_query\_dsa | 正等待并行查询动态共享内存分配锁 |  |
| tbm | 正等待TBM共享迭代器锁 |  |
| parallel\_append | 在Parallel Append计划执行期间等待选择下一个子计划。 |  |
| parallel\_hash\_join | 在Parallel Hash计划执行期间等待分配或交换一块内存 或者更新计数器 |  |
| Lock | relation | 正等待获得一个关系上的锁 |
| extend | 正等待扩展一个关系 |  |
| page | 正等待获得一个关系上的页面的锁 |  |
| tuple | 正等待获得一个元组上的锁 |  |
| transactionid | 正等待一个事务结束 |  |
| virtualxid | 正等待获得一个虚拟xid 锁 |  |
| speculative token | 正等待获取一个 speculative insertion lock |  |
| object | 正等待获得一个非关系数据库对象上的锁 |  |
| userlock | 正等待获得一个用户锁 |  |
| advisory | 正等待获得一个咨询用户锁 |  |
| BufferPin | BufferPin | 正等待在一个缓冲区上加pin |
| Activity | ArchiverMain | 正在归档进程的主循环中等待 |
| AutoVacuumMain | 正在autovacuum启动器进程的主循环中等待 |  |
| BgWriterHibernate | 正在后台写入器进程中等待，休眠中 |  |
| BgWriterMain | 正在后台写入器进程的后台工作者的主循环中等待 |  |
| CheckpointerMain | 正在检查点进程的主循环中等待 |  |
| LogicalApplyMain | 正在逻辑应用进程的主循环中等待 |  |
| LogicalLauncherMain | 正在逻辑启动器进程的主循环中等待 |  |
| PgStatMain | 正在统计收集器进程的主循环中等待 |  |
| RecoveryWalAll | 在恢复时等待来自于任意类型来源（本地、归档或流） 的WAL |  |
| RecoveryWalStream | 在恢复时等待来自于一个流的WAL |  |
| SysLoggerMain | 正在系统日志进程的主循环中等待 |  |
| WalReceiverMain | 正在WAL接收器进程的主循环中等待 |  |
| WalSenderMain | 正在WAL发送器进程的主循环中等待 |  |
| WalWriterMain | 正在WAL写入器进程的主循环中等待 |  |
| Client | ClientRead | 正等待从客户端读取数据 |
| ClientWrite | 正等待向客户端写入数据 |  |
| LibPQWalReceiverConnect | 正在WAL接收器中等待建立与远程服务器的连接 |  |
| LibPQWalReceiverReceive | 正在WAL接收器中等待从远程服务器接收数据 |  |
| SSLOpenServer | 正在尝试连接期间等待SSL |  |
| WalReceiverWaitStart | 正等待startup进程发送流复制的初始数据 |  |
| WalSenderWaitForWAL | 正在WAL发送器进程中等待WAL被刷写 |  |
| WalSenderWriteData | 在WAL发送器进程中处理来自WAL接收器的回复时等待任意活动 |  |
| Extension | Extension | 正在一个扩展中等待 |
| IPC | BgWorkerShutdown | 正等待后台工作者关闭 |
| BgWorkerStartup | 正等待后台工作者启动 |  |
| BtreePage | 正等待继续并行B-树扫描所需的页号变得可用 |  |
| CheckpointDone | 等待检查点完成 |  |
| CheckpointStart | 等待检查点开始 |  |
| ClogGroupUpdate | 正等待组领袖在事务结束时更新事务状态 |  |
| ExecuteGather | 在执行Gather节点时等待来自子进程的活动 |  |
| Hash/Batch/Allocating | 正等待一个选出的Parallel Hash参与者分配哈希表 |  |
| Hash/Batch/Electing | 正在选出一个Parallel Hash 参与者来分配一个哈希表 |  |
| Hash/Batch/Loading | 正等待其他Parallel Hash参与者完成装载哈希表 |  |
| Hash/Build/Allocating | 正等待一个选出的Parallel Hash参与者分配初始哈希表 |  |
| Hash/Build/Electing | 正在选出一个Parallel Hash 参与者以分配初始哈希表 |  |
| Hash/Build/HashingInner | 正等待其他Parallel Hash参与者完成对内关系的哈希操作。 |  |
| Hash/Build/HashingOuter | 正等待其他Parallel Hash参与者完成对外关系的哈希操作 |  |
| Hash/GrowBatches/ Allocating | 正等待一个选出的Parallel Hash参与者分配更多批次 |  |
| Hash/GrowBatches/Deciding | 正在选出一个Parallel Hash 参与者决定未来的批次增长。 |  |
| Hash/GrowBatches/Electing | 正在选出一个Parallel Hash 参与者分配更多批次 |  |
| Hash/GrowBatches/ Finishing | 正 在 等 待 一 个 选 出 的 Parallel Hash参与者决定未来的批次增长 |  |
| Hash/GrowBatches/ Repartitioning | 正等待其他Parallel Hash参与者完成重新分区 |  |
| Hash/GrowBuckets/ Allocating | 正等待一个选出的Parallel Hash参与者完成更多桶的分配 |  |
| Hash/GrowBuckets/Electing | 正在选出一个Parallel Hash 参与者分配更多桶 |  |
| Hash/GrowBuckets/ Reinserting | 正等待其他Parallel Hash参与者完成将元组插入到新桶 的操作 |  |
| LogicalSyncData | 正等待逻辑复制的远程服务器发送用于初始表同步的数据 |  |
| LogicalSyncStateChange | 正等待逻辑复制的远程服务器发送用于初始表同步的数据 |  |
| LogicalSyncStateChange | 正等待逻辑复制的远程服务器更改状态 |  |
| MessageQueueInternal | 正等待其他进程被挂接到共享消息队列 |  |
| MessageQueuePutMessage | 正等待把一个协议消息写到一个共享消息队列 |  |
| MessageQueueReceive | 正等待从一个共享消息队列接收字节 |  |
| MessageQueueSend | 正等待向一个共享消息队列中发送字节 |  |
| ParallelBitmapScan | 正等待并行位图扫描被初始化 |  |
| ParallelCreateIndexScan | 正等待并行CREATE INDEX工作者完成堆扫描 |  |
| ParallelFinish | 正等待并行工作者完成计算 |  |
| ProcArrayGroupUpdate | 正等待组领袖在事务结束时清除事务ID |  |
| Promote | 等待备用节点升级 |  |
| ReplicationOriginDrop | 正等待一个复制源头变得不活跃以便被删除 |  |
| ReplicationSlotDrop | 正等待一个复制槽变得不活跃以便被删除 |  |
| SafeSnapshot | 正等待一个用于READ ONLY DEFERRABLE事务的快照 |  |
| SyncRep | 正在同步复制期间等待来自远程服务器的确认 |  |
| Timeout | BaseBackupThrottle | 当有限流活动时在基础备份期间等待 |
| PgSleep | 正在调用pg\_sleep的进程中等待 |  |
| RecoveryApplyDelay | 在恢复时等待应用WAL，因为它被延迟了 |  |
| IO | BufFileRead | 正等待从一个缓存的文件中读取 |
| BufFileWrite | 正等待向一个缓存的文件中写入 |  |
| ControlFileRead | 正等待从控制文件中读取 |  |
| ControlFileSync | 正等待控制文件到达稳定存储 |  |
| ControlFileSyncUpdate | 正等待对控制文件的更新到达稳定存储 |  |
| ControlFileWrite | 正等待一个对控制文件的写入 |  |
| ControlFileWriteUpdate | 正等待一个写操作更新控制文件 |  |
| CopyFileRead | 正在文件拷贝操作期间等待一个读操作 |  |
| CopyFileWrite | 正在文件拷贝操作期间等待一个写操作 |  |
| DataFileExtend | 正等待一个关系数据文件被扩充 |  |
| DataFileFlush | 正等待一个关系数据文件到达稳定存储 |  |
| DataFileImmediateSync | 正等待一个关系数据文件的立即同步到达稳定存储 |  |
| DataFilePrefetch | 正等待从一个关系数据文件中的一次异步预取 |  |
| DataFileRead | 正等待一次对一个关系数据文件的读操作 |  |
| DataFileSync | 正等待对一个关系数据文件的更改到达稳定存储 |  |
| DataFileTruncate | 正等待一个关系数据文件被截断 |  |
| DataFileWrite | 正等待一次对一个关系数据文件的写操作 |  |
| DSMFillZeroWrite | 等待向一个动态共享内存备份文件中写零字节 |  |
| LockFileAddToDataDirRead | 在向数据目录锁文件中增加一行时等待一个读操作 |  |
| LockFileAddToDataDirSync | 在向数据目录锁文件中增加一行时等待数据到达稳定存储 |  |
| LockFileAddToDataDirWrite | 在向数据目录锁文件中增加一行时等待一个写操作 |  |
| LockFileCreateRead | 在创建数据目录锁文件期间等待读取 |  |
| LockFileCreateSync | 在创建数据目录锁文件期间等待数据到达稳定存储 |  |
| LockFileCreateWrite | 在创建数据目录锁文件期间等待一个写操作 |  |
| LockFileReCheckDataDirRead | 在重新检查数据目录锁文件的过程中等待一个读操作 |  |
| LogicalRewriteCheckpointSync | 在一个检查点期间等待逻辑重写映射到达稳定存储 |  |
| LogicalRewriteMappingSync | 在一次逻辑重写期间等待映射数据到达稳定存储 |  |
| LogicalRewriteMappingWrite | 在一次逻辑重写期间等待对映射数据的写操作 |  |
| LogicalRewriteSync | 正等待逻辑重写映射到达稳定存储 |  |
| LogicalRewriteWrite | 正等待对逻辑重写映射的写操作 |  |
| RelationMapRead | 正等待对关系映射文件的读操作 |  |
| RelationMapSync | 正等待关系映射文件到达稳定存储 |  |
| RelationMapWrite | 正等待对关系映射文件的写操作 |  |
| ReorderBufferRead | 在重排序缓冲区管理期间等待一个读操作 |  |
| ReorderBufferWrite | 在重排序缓冲区管理期间等待一个写操作 |  |
| ReorderLogicalMappingRead | 在重排序缓冲区管理期间等待对一个逻辑映射的读操作 |  |
| ReplicationSlotRead | 正等待对一个复制槽控制文件的读操作 |  |
| ReplicationSlotRestoreSync | 在把一个复制槽控制文件恢复到内存的过程中等待它到达稳定存储 |  |
| ReplicationSlotSync | 正等待一个复制槽控制文件到达稳定存储 |  |
| ReplicationSlotWrite | 正等待对一个复制槽控制文件的写操作 |  |
| SLRUFlushSync | 在检查点或者数据库关闭期间等待SLRU数据到达稳定存储 |  |
| SLRURead | 正等待对一个SLRU页面的读操作 |  |
| SLRUSync | 正等待SLRU数据在一个页面写之后到达稳定存储 |  |
| SLRUWrite | 正等待一个SLRU页面上的写操作 |  |
| SnapbuildRead | 正等待一个序列化历史目录快照的读操作 |  |
| SnapbuildSync | 正等待一个序列化历史目录快照到达稳定存储 |  |
| SnapbuildWrite | 正等待一个序列化历史目录快照的写操作 |  |
| TimelineHistoryFileSync | 正等待一个通过流复制接收到的时间线历史文件到达稳定存储 |  |
| TimelineHistoryFileWrite | 正等待一个通过流复制接收到的时间线历史文件的读操作 |  |
| TimelineHistoryRead | 正等待一个时间线历史文件上的读操作 |  |
| TimelineHistorySync | 正等待一个新创建的时间线历史文件达到稳定存储 |  |
| TimelineHistoryWrite | 正等待一个新创建的时间线历史文件上的写操作 |  |
| TwophaseFileRead | 正等待一个两阶段状态文件的读操作 |  |
| TwophaseFileSync | 正等待一个两阶段状态文件到达稳定存储。 |  |
| TwophaseFileWrite | 正等待一个两阶段状态文件的写操作 |  |
| WALBootstrapSync | 在自举期间等待WAL到达稳定存储 |  |
| WALBootstrapWrite | 在自举期间等待一个WAL页面的写操作 |  |
| WALCopyRead | 在通过拷贝一个已有WAL段创建一个新的WAL段时等待一个读操作 |  |
| WALCopySync | 正等待一个通过拷贝已有WAL 段创建的新WAL段到达稳定存储 |  |
| WALCopyWrite | 在通过拷贝一个已有WAL段创建一个新的WAL段时等待一个写操作 |  |
| WALInitSync | 正等待一个新初始化的WAL文件到达稳定存储 |  |
| WALInitWrite | 在初始化一个新的WAL文件期间等待一个写操作 |  |
| WALRead | 正等待一次对一个WAL文件的读操作 |  |
| WALSenderTimelineHistoryRead | 在walsender的时间线命令期间等待对一个时间线历史文件的读操作 |  |
| WALSync | 等待WAL文件到达持久的存储空间 |  |
| WALSyncMethodAssign | 在指派WAL同步方法时等待数据到达稳定存储 |  |
| WALWrite | 正等待一次对一个WAL文件的写操作 |  |

表8.4 等待事件类型

| 等待事件类型 | 描述 |
| --- | --- |
| Activity | 服务器进程处于空闲状态。此事件类型表示进程正在等待其主处理循环中的活动。wait\_event将标识特定的等待点；请参阅表8.5。 |
| BufferPin | 服务器进程正在等待对数据缓冲区的排他访问。如果另一个进程持有最后从所讨论的缓冲区读取数据的打开游标，则缓冲区锁定等待可能会延长。请参阅表8.6。 |
| Client | 服务器进程正在等待与用户应用程序连接的套接字上的活动。因此服务器期望发生的事情与其内部进程无关。wait\_event将标识特定的等待点；请参阅表8.7。. |
| Extension | 服务器进程正在等待由扩展模块定义的某种条件。请参阅表8.8。. |
| IO | 服务器进程正在等待I/O操作完成。wait\_event将标识特定的等待点；请参阅表8.9。. |
| IPC | 服务器进程正在等待与另一个服务器进程的某种交互。wait\_event将标识特定的等待点；请参阅表8.10。. |
| Lock | 服务器进程正在等待重量级锁。重量级锁，也称为锁管理器锁或简称锁，主要用于保护SQL可见对象，如表。但是，它们也用于确保某些内部操作的互斥，例如关系扩展。wait\_event将标识所等待的锁的类型；请参阅表8.11。 |
| LWLock | 服务器进程正在等待轻量级锁。大多数此类锁用于保护共享内存中的特定数据结构。wait\_event将包含一个标识轻量级锁目的的名称。（某些锁具有特定名称；其他锁是一组锁的一部分，每个锁都具有类似的目的。）请参阅表8.12。 |
| Timeout | 服务器进程正在等待超时到期。wait\_event将标识特定的等待点；请参阅表8.13。 |

表8.5 活动的等待事件类型

| 等待事件类型 | 描述 |
| --- | --- |
| ArchiverMain | 归档进程主循环中等待。 |
| AutoVacuumMain | 自动清理启动器进程主循环中等待。 |
| BgWriterHibernate | 后台写入进程中等待，正在休眠。 |
| BgWriterMain | 后台写入进程主循环中等待。 |
| CheckpointerMain | 检查点进程主循环中等待。 |
| LogicalApplyMain | 逻辑复制应用进程主循环中等待。 |
| LogicalLauncherMain | 逻辑复制启动器进程主循环中等待。 |
| PgStatMain | 统计收集器进程主循环中等待。 |
| RecoveryWalStream | 启动过程中等待WAL到达的主循环中等待，正在流式恢复。 |
| SysLoggerMain | 系统日志记录器进程主循环中等待。 |
| WalReceiverMain | WAL接收器进程主循环中等待。 |
| WalSenderMain | WAL发送器进程主循环中等待。 |
| WalWriterMain | WAL写入器进程主循环中等待。 |

表8.6. BufferPin等待事件类型

| 等待事件类型 | 描述 |
| --- | --- |
| BufferPin | 等待在缓冲区上获取排他锁。 |

表8.7. Client等待事件类型

| 等待事件类型 | 描述 |
| --- | --- |
| ClientRead | 等待从客户端读取数据。 |
| ClientWrite | 等待向客户端写入数据。 |
| GSSOpenServer | 在建立GSSAPI会话时等待从客户端读取数据。 |
| LibPQWalReceiverConnect | 在WAL接收器中等待建立与远程服务器的连接。 |
| LibPQWalReceiverReceive | 在WAL接收器中等待从远程服务器接收数据。 |
| SSLOpenServer | 在尝试连接时等待SSL。 |
| WalSenderWaitForWAL | 在WAL发送器进程中等待WAL被刷新。 |
| WalSenderWriteData | 在WAL发送器进程中处理来自WAL接收器的回复时等待任何活动。 |

表8.8. Extension等待事件类型

| 等待事件类型 | 描述 |
| --- | --- |
| Extension | 等待一个插件 |

表8.9. IO等待事件类型

| 等待事件类型 | 描述 |
| --- | --- |
| BaseBackupRead | 等待从文件读取基础备份 |
| BufFileRead | 等待从缓冲文件中读取数据 |
| BufFileWrite | 等待向缓冲文件中写入数据 |
| BufFileTruncate | 等待对缓冲文件进行截断 |
| ControlFileRead | 等待从pg\_control文件中读取数据 |
| ControlFileSync | 等待pg\_control文件达到持久存储 |
| ControlFileSyncUpdate | 等待对pg\_control文件的更新达到持久存储 |
| ControlFileWrite | 等待向pg\_control文件中写入数据 |
| ControlFileWriteUpdate | 等待写入更新到pg\_control文件 |
| CopyFileRead | 等待在文件复制操作期间进行读取 |
| CopyFileWrite | 等待在文件复制操作期间进行写入 |
| DSMFillZeroWrite | 等待将动态共享内存备份文件填充为零 |
| DataFileExtend | 等待扩展关系数据文件 |
| DataFileFlush | 等待关系数据文件达到持久存储 |
| DataFileImmediateSync | 等待关系数据文件立即同步到持久存储 |
| DataFilePrefetch | 等待对关系数据文件的异步预取 |
| DataFileRead | 等待从关系数据文件中读取数据 |
| DataFileSync | 等待对关系数据文件的更改达到持久存储 |
| DataFileTruncate | 等待对关系数据文件进行截断 |
| DataFileWrite | 等待向关系数据文件中写入数据 |
| LockFileAddToDataDirRead | 等待在将行添加到数据目录锁文件时进行读取 |
| LockFileAddToDataDirSync | 等待在向数据目录锁文件添加行时将数据达到持久存储 |
| LockFileAddToDataDirWrite | 等待在将行添加到数据目录锁文件时进行写入 |
| LockFileCreateRead | 等待在创建数据目录锁文件时进行读取 |
| LockFileCreateSync | 等待在创建数据目录锁文件时将数据达到持久存储 |
| LockFileCreateWrite | 等待在创建数据目录锁文件时进行写入 |
| LockFileReCheckDataDirRead | 等待在重新检查数据目录锁文件时进行读取 |
| LogicalRewriteCheckpointSync | 等待在检查点期间逻辑重写映射达到持久存储 |
| LogicalRewriteMappingSync | 等待在逻辑重写期间映射数据达到持久存储 |
| LogicalRewriteMappingWrite | 等待在逻辑重写期间写入映射数据 |
| LogicalRewriteSync | 等待逻辑重写映射达到持久存储 |
| LogicalRewriteTruncate | 等待在逻辑重写期间截断映射数据 |
| LogicalRewriteWrite | 等待写入逻辑重写映射数据 |
| RelationMapRead | 等待读取关系映射文件 |
| RelationMapSync | 等待关系映射文件达到持久存储 |
| RelationMapWrite | 等待向关系映射文件中写入数据 |
| ReorderBufferRead | 等待在重新排序缓冲区管理期间进行读取 |
| ReorderBufferWrite | 等待在重新排序缓冲区管理期间进行写入 |
| ReorderLogicalMappingRead | 等待在重新排序缓冲区管理期间读取逻辑映射 |
| ReplicationSlotRead | 等待从复制插槽控制文件中读取数据 |
| ReplicationSlotRestoreSync | 等待在将复制插槽控制文件恢复到内存时将数据达到持久存储 |
| ReplicationSlotSync | 等待复制插槽控制文件达到持久存储 |
| ReplicationSlotWrite | 等待向复制插槽控制文件中写入数据 |
| SLRUFlushSync | 等待在检查点或数据库关闭期间SLRU数据达到持久存储 |
| SLRURead | 等待读取SLRU页面 |
| SLRUSync | 等待SLRU数据在页面写入后达到持久存储 |
| SLRUWrite | 等待写入SLRU页面 |
| SnapbuildRead | 等待读取序列化历史目录快照 |
| SnapbuildSync | 等待序列化历史目录快照达到持久存储 |
| SnapbuildWrite | 等待写入序列化历史目录快照 |
| TimelineHistoryFileSync | 等待通过流复制接收到的时间线历史文件达到持久存储 |
| TimelineHistoryFileWrite | 等待写入通过流复制接收到的时间线历史文件 |
| TimelineHistoryRead | 等待读取时间线历史文件 |
| TimelineHistorySync | 等待新创建的时间线历史文件达到持久存储 |
| TimelineHistoryWrite | 等待写入新创建的时间线历史文件 |
| TwophaseFileRead | 等待读取两阶段状态文件 |
| TwophaseFileSync | 等待两阶段状态文件达到持久存储 |
| TwophaseFileWrite | 等待写入两阶段状态文件 |
| WALBootstrapSync | 等待在引导过程中WAL达到持久存储 |
| WALBootstrapWrite | 等待在引导过程中写入WAL页 |
| WALCopyRead | 等待在复制现有WAL段创建新WAL段时进行读取 |
| WALCopySync | 等待通过复制现有WAL段创建新WAL段时将新WAL段达到持久存储 |
| WALCopyWrite | 等待在复制现有WAL段创建新WAL段时进行写入 |
| WALInitSync | 等待新初始化的WAL文件达到持久存储 |
| WALInitWrite | 等待在初始化新WAL文件时进行写入 |
| WALRead | 等待从WAL文件读取数据 |
| WALSenderTimelineHistoryRead | 等待在walsender时间线命令期间从时间线历史文件中读取数据 |
| WALSync | 等待WAL文件达到持久存储 |
| WALSyncMethodAssign | 等待在分配新的WAL同步方法时将数据达到持久存储 |
| WALWrite | 等待向WAL文件写入数据 |
| LogicalChangesRead | 等待从逻辑变更文件中读取数据 |
| LogicalChangesWrite | 等待向逻辑变更文件中写入数据 |
| LogicalSubxactRead | 等待从逻辑子事务文件中读取数据 |
| LogicalSubxactWrite | 等待向逻辑子事务文件中写入数据 |

表8.10. IPC等待事件类型

| 等待事件类型 | 描述 |
| --- | --- |
| AppendReady | 等待子计划节点准备就绪以继续追加计划节点的执行。 |
| BackendTermination | 等待另一个后端终止。 |
| BackupWaitWalArchive | 等待成功归档用于备份的WAL文件。 |
| BgWorkerShutdown | 等待后台工作进程关闭。 |
| BgWorkerStartup | 等待后台工作进程启动。 |
| BtreePage | 等待需要的页码以继续并行B树扫描。 |
| BufferIO | 等待缓冲区I/O操作完成。 |
| CheckpointDone | 等待检查点完成。 |
| CheckpointStart | 等待检查点开始。 |
| ExecuteGather | 在执行Gather计划节点时等待子进程的活动。 |
| HashBatchAllocate | 等待选举的并行哈希参与者分配哈希表。 |
| HashBatchElect | 等待选举并行哈希参与者以分配哈希表。 |
| HashBatchLoad | 等待其他并行哈希参与者完成加载哈希表。 |
| HashBuildAllocate | 等待选举的并行哈希参与者分配初始哈希表。 |
| HashBuildElect | 等待选举并行哈希参与者以分配初始哈希表。 |
| HashBuildHashInner | 等待其他并行哈希参与者完成对内部关系的哈希处理。 |
| HashBuildHashOuter | 等待其他并行哈希参与者完成对外部关系的分区处理。 |
| HashGrowBatchesAllocate | 等待选举的并行哈希参与者分配更多批次。 |
| HashGrowBatchesDecide | 等待选举并行哈希参与者决定未来批次的增长。 |
| HashGrowBatchesElect | 等待选举并行哈希参与者以分配更多批次。 |
| HashGrowBatchesFinish | 等待选举的并行哈希参与者决定未来批次的增长。 |
| HashGrowBatchesRepartition | 等待其他并行哈希参与者完成重新分区。 |
| HashGrowBucketsAllocate | 等待选举的并行哈希参与者完成分配更多桶。 |
| HashGrowBucketsElect | 等待选举并行哈希参与者以分配更多桶。 |
| HashGrowBucketsReinsert | 等待其他并行哈希参与者完成将元组重新插入新桶中。 |
| LogicalSyncData | 等待逻辑复制远程服务器发送数据以进行初始表同步。 |
| LogicalSyncStateChange | 等待逻辑复制远程服务器更改状态。 |
| MessageQueueInternal | 等待其他进程连接到共享消息队列。 |
| MessageQueuePutMessage | 等待向共享消息队列写入协议消息。 |
| MessageQueueReceive | 等待从共享消息队列接收字节。 |
| MessageQueueSend | 等待向共享消息队列发送字节。 |
| ParallelBitmapScan | 等待并行位图扫描初始化。 |
| ParallelCreateIndexScan | 等待并行CREATE INDEX工作者完成堆扫描。 |
| ParallelFinish | 等待并行工作者完成计算。 |
| ProcArrayGroupUpdate | 等待组领导在并行操作结束时清除事务ID。 |
| ProcSignalBarrier | 等待所有后端处理栅栏事件。 |
| Promote | 等待备机升级。 |
| RecoveryConflictSnapshot | 等待清理回滚时的恢复冲突解析。 |
| RecoveryConflictTablespace | 等待删除表空间时的恢复冲突解析。 |
| RecoveryPause | 等待恢复恢复。 |
| ReplicationOriginDrop | 等待复制源变得非活跃以便删除。 |
| ReplicationSlotDrop | 等待复制插槽变得非活跃以便删除。 |
| SafeSnapshot | 等待为READ ONLY DEFERRABLE事务获取有效快照。 |
| SyncRep | 等待同步复制期间远程服务器的确认。 |
| WalReceiverExit | 等待WAL接收器退出。 |
| WalReceiverWaitStart | 等待启动过程发送流复制的初始数据。 |
| XactGroupUpdate | 等待组领导在并行操作结束时更新事务状态。 |

表8.11. 锁等待事件类型

| 等待事件类型 | 描述 |
| --- | --- |
| advisory | 等待获取一个咨询用户锁。 |
| extend | 等待扩展一个关系。 |
| frozenid | 等待更新pg\_database.datfrozenxid和pg\_database.datminmxid。 |
| object | 等待在非关系数据库对象上获取锁。 |
| page | 等待在关系的页面上获取锁。 |
| relation | 等待在关系上获取锁。 |
| spectoken | 等待获取一个投机性插入锁。 |
| transactionid | 等待事务完成。 |
| tuple | 等待在元组上获取锁。 |
| userlock | 等待获取用户锁。 |
| virtualxid | 等待获取一个虚拟事务ID锁。 |

表8.12. LWLock等待事件类型

| 等待事件类型 | 描述 |
| --- | --- |
| AddinShmemInit | 等待管理扩展在共享内存中的空间分配。 |
| AutoFile | 等待更新postgresql.auto.conf文件。 |
| Autovacuum | 等待读取或更新自动清理工作者的当前状态。 |
| AutovacuumSchedule | 等待确保选定用于自动清理的表仍需要清理。 |
| BackgroundWorker | 等待读取或更新后台工作者状态。 |
| BtreeVacuum | 等待读取或更新与B-tree索引相关的清理信息。 |
| BufferContent | 等待访问内存中的数据页。 |
| BufferMapping | 等待将数据块与缓冲区池中的缓冲区关联。 |
| CheckpointerComm | 等待管理fsync请求。 |
| CommitTs | 等待读取或更新事务提交时间戳的最后设置值。 |
| CommitTsBuffer | 等待在提交时间戳SLRU缓冲区上进行I/O。 |
| CommitTsSLRU | 等待访问提交时间戳SLRU缓存。 |
| ControlFile | 等待读取或更新pg\_control文件或创建新的WAL文件。 |
| DynamicSharedMemoryControl | 等待读取或更新动态共享内存分配信息。 |
| LockFastPath | 等待读取或更新进程的快速路径锁信息。 |
| LockManager | 等待读取或更新“重量级”锁的信息。 |
| LogicalRepWorker | 等待读取或更新逻辑复制工作者的状态。 |
| MultiXactGen | 等待读取或更新共享多重事务状态。 |
| MultiXactMemberBuffer | 等待在多重事务成员SLRU缓冲区上进行I/O。 |
| MultiXactMemberSLRU | 等待访问多重事务成员SLRU缓存。 |
| MultiXactOffsetBuffer | 等待在多重事务偏移SLRU缓冲区上进行I/O。 |
| MultiXactOffsetSLRU | 等待访问多重事务偏移SLRU缓存。 |
| MultiXactTruncation | 等待读取或截断多重事务信息。 |
| NotifyBuffer | 等待在NOTIFY消息SLRU缓冲区上进行I/O。 |
| NotifyQueue | 等待读取或更新NOTIFY消息。 |
| NotifyQueueTail | 等待更新NOTIFY消息存储的限制。 |
| NotifySLRU | 等待访问NOTIFY消息SLRU缓存。 |
| OidGen | 等待分配新的OID。 |
| OldSnapshotTimeMap | 等待读取或更新旧快照控制信息。 |
| ParallelAppend | 等待在执行并行附加计划节点期间选择下一个子计划。 |
| ParallelHashJoin | 等待在执行并行哈希连接计划节点期间同步工作者。 |
| ParallelQueryDSA | 等待并行查询动态共享内存分配。 |
| PerSessionDSA | 等待并行查询动态共享内存分配。 |
| PerSessionRecordType | 等待访问并行查询有关复合类型的信息。 |
| PerSessionRecordTypmod | 等待访问并行查询有关标识匿名记录类型的类型修改器的信息。 |
| PerXactPredicateList | 等待在并行查询期间由当前串行化事务持有的谓词锁列表。 |
| PredicateLockManager | 等待访问序列化事务使用的谓词锁信息。 |
| ProcArray | 等待访问共享的每个进程数据结构（通常是为了获取快照或报告会话的事务ID）。 |
| RelationMapping | 等待读取或更新pg\_filenode.map文件（用于跟踪某些系统目录的文件节点分配）。 |
| RelCacheInit | 等待读取或更新pg\_internal.init关系缓存初始化文件。 |
| ReplicationOrigin | 等待创建、删除或使用复制起点。 |
| ReplicationOriginState | 等待读取或更新一个复制起点的进度。 |
| ReplicationSlotAllocation | 等待分配或释放复制槽。 |
| ReplicationSlotControl | 等待读取或更新复制槽状态。 |
| ReplicationSlotIO | 等待在复制槽上进行I/O。 |
| SerialBuffer | 等待在可串行化事务冲突SLRU缓冲区上进行I/O。 |
| SerializableFinishedList | 等待访问已完成的可串行化事务列表。 |
| SerializablePredicateList | 等待访问可串行化事务持有的谓词锁列表。 |
| SerializableXactHash | 等待读取或更新关于可串行化事务的信息。 |
| SerialSLRU | 等待访问可串行化事务冲突SLRU缓存。 |
| SharedTidBitmap | 等待在并行位图索引扫描期间访问共享的TID位图。 |
| SharedTupleStore | 等待在并行查询期间访问共享的元组存储。 |
| ShmemIndex | 等待在共享内存中找到或分配空间。 |
| SInvalRead | 等待从共享的目录失效队列检索消息。 |
| SInvalWrite | 等待将消息添加到共享的目录失效队列。 |
| SubtransBuffer | 等待在子事务SLRU缓冲区上进行I/O。 |
| SubtransSLRU | 等待访问子事务SLRU缓存。 |
| SyncRep | 等待读取或更新关于同步复制状态的信息。 |
| SyncScan | 等待选择同步表扫描的起始位置。 |
| TablespaceCreate | 等待创建或删除表空间。 |
| TwoPhaseState | 等待读取或更新预备事务的状态。 |
| WALBufMapping | 等待替换WAL缓冲区中的页面。 |
| WALInsert | 等待将WAL数据插入内存缓冲区。 |
| WALWrite | 等待将WAL缓冲区写入磁盘。 |
| WrapLimitsVacuum | 等待更新事务ID和多重事务消耗的限制。 |
| XactBuffer | 等待在事务状态SLRU缓冲区上进行I/O。 |
| XactSLRU | 等待访问事务状态SLRU缓存。 |
| XactTruncation | 等待执行pg\_xact\_status或更新可用于其的最旧事务ID。 |
| XidGen | 等待分配新的事务ID。 |

表8.13. Timeout等待事件类型

| 等待事件类型 | 描述 |
| --- | --- |
| BaseBackupThrottle | 在限制活动时进行基础备份时等待。 |
| CheckpointWriteDelay | 在执行检查点时写入之间的等待。 |
| PgSleep | 由于调用pg\_sleep或类似函数而等待。 |
| RecoveryApplyDelay | 由于延迟设置而在恢复期间等待应用WAL。 |
| RecoveryRetrieveRetryInterval | 在恢复期间等待时，当WAL数据从任何源（pg\_wal、存档或流）都不可用时。 |
| RegisterSyncRequest | 在向检查点发送同步请求时等待，因为请求队列已满。 |
| VacuumDelay | 在基于成本的清理延迟点等待。 |

这是一个查看等待事件的示例：

SELECT pid, wait\_event\_type, wait\_event FROM pg\_stat\_activity WHERE wait\_event is NOT NULL;

pid | wait\_event\_type | wait\_event

——+—————–+————

2540 | Lock | relation

6644 | LWLock | ProcArray

(2 rows)

### pg\_stat\_replication

pg\_stat\_replication 视图将包含每个WAL发送进程的一行，显示关于复制到该发送进程连接的备用服务器的统计信息。仅列出直接连接的备用服务器；没有关于下游备用服务器的信息可用。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| pid | integer | 一个 WAL 发送进程的进程 ID |
| usesysid | oid | 登录到这个 WAL 发送进程的用户的 OID |
| usename | name | 登录到这个 WAL 发送进程的用户的名称 |
| application\_name | text | 连接到这个 WAL 发送进程的应用的名称 |
| client\_addr | inet | 连接到这个WAL发送进程的客户端的IP地址。如果这个域为空，它表示该客户端通过服务器机器上的一个Unix 套接字连接 |
| client\_hostname | text | 连接上的客户端的主机名，由一次对client\_addr的逆向DNS查找报告。这个域将只对IP连接非空，并且只有在log\_hostname被启用时非空 |
| client\_port | integer | 客户端用来与这个WAL发送进程通讯的TCP端口号， 如果使用Unix套接字则为-1 |
| backend\_start | timestamp with time zone | 这个进程开始的时间，即客户端是何时连接到这个WAL 发送进程的 |
| backend\_xmin | xid | 由 hot\_standby\_feedback报告的这个后备机的xmin水平线。 |
| state | text | 当前的 WAL 发送进程状态。可能的值是： startup：这个WAL发送器正在启动。 catchup：这个WAL发送器连接的后备机正在追赶主服务器。 streaming：这个WAL发送器在它连接的后备服务器追上主服务器之后用流传送更改。 backup：这个WAL发送器正在发送一个备份。 stopping：这个WAL发送器正在停止 |
| sent\_lsn | pg\_lsn | 在这个连接上发送的最后一个预写式日志的位置 |
| write\_lsn | pg\_lsn | 被这个后备服务器写入到磁盘的最后一个预写式日志的位置 |
| flush\_lsn | pg\_lsn | 被这个后备服务器刷入到磁盘的最后一个预写式日志的位置 |
| replay\_lsn | pg\_lsn | 被重放到这个后备服务器上的数据库中的最后一个预写式日志的位置 |
| write\_lag | interval | 在本地刷写近期的WAL与接收到后备服务器已经写入它（但还没有刷写或者应用） 的通知之间流逝的时间。如果这台服务器被配置为一个同步后备，这可以用来计量在提交时synchronous\_commit的级别remote\_write所导致的延迟。 |
| flush\_lag | interval | 在本地刷写近期的WAL与接收到后备服务器已经写入并且刷写它（但还没有应用）的通知之间流逝的时间。如果这台服务器被配置为一个同步后备，这可以用来计量在提交时synchronous\_commit的级别on所导致的延迟。 |
| replay\_lag | interval | 在本地刷写近期的WAL与接收到后备服务器已经写入它、刷写它并且应用它的通知之间流逝的时间。如果这台服务器被配置为一个同步后备，这可以用来计量在提交时synchronous\_commit的级别remote\_apply所导致的延迟。 |
| sync\_priority | integer | 在基于优先的同步复制中， 这台后备服务器被选为同步后备的优先级。在基于规定数量的同步复制中，这个值没有效果 |
| sync\_state | text | 这一台后备服务器的同步状态。 可能的值是：• async：这台后备服务器是异步的。• potential：这台后备服务器现在是异步的，但可能在当前的同步后备失效时变成同步的。• sync：这台后备服务器是同步的。quorum：这台后备服务器被当做规定数量后备服务器的候选。 |
| reply\_time | 带时区的时间戳 | 从备用服务器收到的最后一条回复信息的发送时间 |

pg\_stat\_replication 视图中报告的延迟时间是对最近WAL被写入、刷新和重放的时间以及发送者了解这一过程所需的时间的测量。这些时间代表了如果远程服务器被配置为同步备用服务器，则每个同步提交级别引入的提交延迟（或将引入的延迟）。对于异步备用服务器，replay\_lag列近似表示最近的事务在查询中可见之前的延迟。如果备用服务器已完全赶上发送服务器，并且没有更多的 WAL活动，则最近测量的延迟时间将在短时间内继续显示，然后显示为NULL。

延迟时间对于物理复制是自动工作的。逻辑解码插件可以选择性地发出跟踪消息；如果它们没有这样做，跟踪机制将简单地显示NULL延迟。

### pg\_stat\_replication\_slots

pg\_stat\_replication\_slots 视图将包含每个逻辑复制插槽的一行，显示关于其使用情况的统计信息。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| slot\_name | text | 复制插槽的唯一、集群范围内的标识符 |
| spill\_txns | bigint | 一旦逻辑解码器用于解码WAL中的更改的内存超出了 logical\_decoding\_work\_mem，将会将事务溢出到磁盘的数量递增。该计数器对于顶级事务和子事务都会递增。 |
| spill\_count | bigint | 事务在解码来自WAL的更改时被溢出到磁盘的次数。每次事务溢出时，该计数器都会递增，同一个事务可能会被多次溢出。 |
| spill\_bytes | bigint | 在为此插槽执行WAL更改解码时溢出到磁盘的解码事务数据量。此计数器和其他溢出计数器可用于衡量逻辑解码期间发生的I/O 操作，并允许调整 logical\_decoding\_work\_mem。 |
| stream\_txns | bigint | 一旦逻辑解码器用于解码WAL中的更改的内存超出了 logical\_decoding\_work\_mem，即插槽的流式事务数量。流式只适用于顶级事务（子事务不能独立流式），因此对于子事务不会递增该计数器。 |
| stream\_count | Bigint | 在解码来自WAL的更改时，流式进行中的事务被发送到解码输出插件的次数。每次事务被流式处理时，该计数器都会递增，同一个事务可能会被多次流式处理。 |
| stream\_bytes | bigint | 在解码来自WAL的更改时，解码输出插件将进行中的事务流式处理的事务数据量。此计数器和此插槽的其他流式计数器可用于调整 logical\_decoding\_work\_mem。 |
| total\_txns | bigint | 为此插槽发送到解码输出插件的解码事务总数。仅计、数顶级事务，并且不会为子事务递增。请注意，这包括被流式处理和溢出的事务。 |
| total\_bytes | bigint | 在解码来自WAL的更改时，为将事务发送到解码输出插件解码的事务数据量。请注意，这包括流式处理溢出的数据。 |
| stats\_reset | timestamp with time zone | 上次重置统计信息的时间 |

### pg\_stat\_wal\_receiver

pg\_stat\_wal\_receiver事务只包含一行，它显示了从 WAL 接收器所连接的服务器得到的有关该接收器的统计信息。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| pid | integer | WAL接收器进程的进程ID |
| status | text | WAL接收器进程的活动状态 |
| receive\_start\_lsn | pg\_lsn | WAL接收器启动时使用的第一个预写式日志位置 |
| receive\_start\_tli | integer | WAL接收器启动时使用的第一个时间线编号 |
| received\_lsn | pg\_lsn | 已经接收到并且已经被杀入磁盘的最后一个预写式日志的位置，这个域的初始值是WAL 接收器启动时使用的第一个日志位置 |
| received\_tli | integer | 已经接收到并且已经被杀入 磁盘的最后一个预写式日志 的时间线编号，这个域的初 始值是WAL接收器启动时使用的第一个日志所在的时间 线编号 |
| last\_msg\_send\_time | timestamp with time zone | 从源头WAL发送器接收到的最后一个消息的发送时间 |
| last\_msg\_receipt\_time | timestamp with time zone | 从源头WAL发送器接收到的最后一个消息的接收时间 |
| latest\_end\_lsn | pg\_lsn | 报告给源头WAL发送器的最后一个预写式日志位置 |
| latest\_end\_time | timestamp with time zone | 报告给源头WAL发送器最后一个事务日志位置的时间 |
| slot\_name | text | 这个WAL接收器使用的复制槽的名称 |
| sender\_host | text | 这WAL接收器连接到的瀚高数据库实例的主机。这可以是一个主机名、一个IP地址，如果连接是通过Unix 套接字则是一个目录路径（为目录的情况可以被辨别出来，因为路径将总是一个绝对路径并且以/开头） |
| sender\_host | integer | 这个WAL接收器连接到的瀚高数据库实例的端口号 |
| conninfo | text | 这个WAL接收器使用的连接串，安全相关的域会被隐去。 |

### pg\_stat\_subscription

每一个订阅都在pg\_stat\_subscription视图中有一行，处理被订阅表的初始数据拷贝操作的工作者还会有额外的行。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| subid | oid | 订阅的OID |
| subname | text | 订阅的名称 |
| pid | integer | 订阅工作者进程的进程ID |
| relid | Oid | 工作者正在同步的关系的OID，对于主应用工作者为空 |
| received\_lsn | pg\_lsn | 接收到的最后一个预写式日志位置，这个字段的初始值是0 |
| last\_msg\_send\_time | timestamp with time zone | 从源头WAL发送器接收到的最后一个消息的发送时间 |
| last\_msg\_receipt\_time | timestamp with time zone | 从源头WAL发送器接收到的最后一个消息的接收时间 |
| latest\_end\_lsn | pg\_lsn | 最后一个报告给源头WAL发送器的预写式日志位置 |
| latest\_end\_time | timestamp with time zone | 报告给源头WAL发送器的最后一个预写式日志位置的时间 |

### pg\_stat\_ssl

pg\_stat\_ssl 视图将包含每个后端或WAL发送进程的一行，显示关于此连接上SSL使用情况的统计信息。可以通过pid列将其与pg\_stat\_activity或 pg\_stat\_replication连接以获取有关连接的更多详细信息。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| pid | integer | 一个后端或者WAL发送进程的进程 ID |
| ssl | boolean | 如果在这个连接上使用了 SSL 则为真 |
| version | text | 在用的 SSL 版本，如果这个连接上没有使用SSL则为NULL |
| cipher | text | 在用的SSL密码的名称， 如果这个连接上没有使用 SSL 则为 NULL |
| bits | integer | 使用的加密算法中的位数， 如果这个连接上没有使用 SSL 则为 NULL |
| compression | boolean | 如果使用了SSL 压缩则为真，否则为假，如果这个连接上没有使用SSL则为 NULL |
| client\_dn | text | 来自所使用的客户端证书的 识别名（DN）域,如果没有提供客户端证书或者这个连 接上没有使用SSL则为NULL。如果DN域长度超过NAMEDATALEN（标准编译中是 64 个字符），则它会被截断。 |
| client\_serial | numeric | 客户端证书的序列号，如果 没有提供客户端证书，或者 在此连接上不使用SSL，则为NULL。证书序列号和证书发行者的组合可以唯一地识别 一个证书（除非发行者错误 地重复使用序列号） |
| issuer\_dn | text | 客户端证书的发行者的DN， 如果没有提供客户端证书， 或者如果这个连接上没有使用SSL，则为NULL。这个字段被截断，就像client\_dn一 样。 |

### pg\_stat\_gssapi

pg\_stat\_gssapi视图将包含每一个后端一个行，显示该连接上的GSSAPI使用情况。它可以加入到pg\_stat\_activity或pg\_stat\_replication上的pid列，获取更多关于连接的详细信息。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| pid | integer | 后台的进程 ID |
| gss\_authenticated | boolean | 如果此连接使用了GSSAPI认证，则为True。 |
| principal | text | 如果没有使用GSSAPI来验证此连接，则为NULL。如果principal长于 NAMEDATALEN（标准构建中为 64 个字符），则该字段被截断。 |
| encrypted | boolean | 如果此连接上使用了GSSAPI 加密，则为True |

### pg\_stat\_archiver

pg\_stat\_archiver视图将总是一个单一的行，该行包含着有关集簇的归档进程的数据。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| failed\_count | bigint | 已被成功归档的WAL文件数量 |
| last\_archived\_wal | text | 最后一个被成功归档的WAL文件名称 |
| last\_archived\_time | timestamp with time zone | 最后一次成功归档操作的时间 |
| failed\_count | bigint | 失败的归档WAL文件尝试的数量 |
| last\_failed\_wal | text | 最后一次失败的归档操作的WAL文件名称 |
| last\_failed\_time | timestamp with time zone | 最后一次失败的归档操作的时间 |
| stats\_reset | timestamp with time zone | 上次重置统计信息的时间 |

### pg\_stat\_bgwriter

pg\_stat\_bgwriter视图将总是只有单独的一行，它包含集簇的全局数据。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| checkpoints\_timed | bigint | 已经被执行的计划中检查点的数量 |
| checkpoints\_req | bigint | 已经被执行的请求检查点的数量 |
| checkpoint\_write\_time | double precision | 在文件被写入磁盘的检查点处理部分花费的总时间，以毫秒计 |
| checkpoint\_sync\_time | double precision | 在文件被同步到磁盘中的检查点处理部分花费的总时间，以毫秒计 |
| buffers\_checkpoint | bigint | 在检查点期间被写的缓冲区数目 |
| buffers\_clean | bigint | 被后台写进程写的缓冲区数目 |
| maxwritten\_clean | bigint | 后台写进程由于已经写了太多缓冲区而停止清洁扫描的次数 |
| buffers\_backend | bigint | 被一个后端直接写的缓冲区数量 |
| buffers\_backend\_fsync | bigint | 一个后端不得不自己执 行fsync调用的次数（通常即 使后端自己进行写操作，后台写进程也会处理这些） |
| buffers\_alloc | bigint | 被分配的缓冲区数量 |
| stats\_reset | timestamp with time zone | 上次重置统计信息的时间 |

### pg\_stat\_wal

pg\_stat\_wal视图始终只包含一行数据，其中包含有关集群WAL活动的数据。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| wal\_records | bigint | 生成的WAL记录总数 |
| wal\_fpi | bigint | 生成的WAL全页总数 |
| wal\_bytes | numeric | 生成的WAL总量，以字节为单位 |
| wal\_buffers\_full | bigint | 由于WAL缓冲区变满而将 WAL数据写入磁盘的次数 |
| wal\_write | bigint | 通过XLogWrite请求将 WAL 缓冲区写入磁盘的次数 |
| wal\_sync | bigint | 通过issue\_xlog\_fsync请求将WAL 文件同步到磁盘的次数（如果 fsync 打开，并且wal\_sync\_method是 fdatasync、fsync或 fsync\_writethrough，则为零）。 |
| wal\_write\_time | double precision | 通过 XLogWrite 请求将 WAL 缓冲区写入磁盘的总时间，以毫秒为单位（如果启用了 track\_wal\_io\_timing，则为零）。当 wal\_sync\_method 为 open\_datasync 或 open\_sync 时，此时间包括同步时间。 |
| wal\_sync\_time | double precision | 通过 issue\_xlog\_fsync 请求将 WAL 文件同步到磁盘的总时间，以毫秒为单位（如果启用了 track\_wal\_io\_timing、fsync 打开，并且 wal\_sync\_method 为 fdatasync、fsync 或 fsync\_writethrough，则为零）。 |
| stats\_reset | timestamp with time zone | 上次重置统计信息的时间 |

### pg\_stat\_database

pg\_stat\_database视图将为集簇中的每一个数据库包含有一行，再加上一个共享对象，显示出全数据库的统计信息。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| datid | oid | 一个数据库的OID，或属于共享关系的对象为0。 |
| datname | name | 此数据库的名称，或共享对象的NULL。 |
| numbackends | integer | 当前连接到这个数据库的后端数量，或者NULL为共享对象。这是此视图中唯一返回反映当前状态的值的列；所有其他列都返回上次重置后的累积值。 |
| xact\_commit | bigint | 在这个数据库中已经被提交的事务的数量 |
| xact\_rollback | bigint | 在这个数据库中已经被回滚的事务的数量 |
| blks\_read | bigint | 在这个数据库中被读取的磁盘块的数量 |
| blks\_hit | bigint | 磁盘块被发现已经在缓冲区中的次数，这样不需要一次读取（这只包括数据库缓冲区中的命中，而不包括在操作系统文件系统缓冲区中的命中） |
| tup\_returned | bigint | 在这个数据库中被查询返回的行数 |
| tup\_fetched | bigint | 在这个数据库中被查询取出的行数 |
| tup\_inserted | bigint | 在这个数据库中被查询插入的行数 |
| tup\_updated | bigint | 在这个数据库中被查询更新的行数 |
| tup\_deleted | bigint | 在这个数据库中被查询删除的行数 |
| conflicts | bigint | 由于与恢复冲突而在这个数据库中被取消的查询的数目（冲突只发生在后备服务器上，详见pg\_stat\_database\_conflicts）。 |
| temp\_files | bigint | 在这个数据库中被查询创建 的临时文件的数量。所有临时文件都被统计，不管为什么创建这些临时文件（如排 序或哈希），并且不管log\_temp\_files设置。 |
| temp\_bytes | bigint | 在这个数据库中被查询写到临时文件中的数据总量。所有临时文件都被统计，不管为什么创建这些临时文件 （如排序或哈希），并且不管log\_temp\_files设置。 |
| deadlocks | bigint | 在这个数据库中被检测到的死锁数 |
| checksum\_failures | bigint | 在此数据库（或共享对象上）检测到的数据页校验和失败的次数，如果没有启用数据校验和，则为NULL。 |
| checksum\_last\_failure | timestamp with time zone | 在此数据库（或共享对象上）检测到最后一个数据页校验和失败的时间，如果没有启用数据校验和，则为 NULL。 |
| blk\_read\_time | double precision | 在这个数据库中后端花费在读取数据文件块的时间，以毫秒计 |
| blk\_write\_time | double precision | 在这个数据库中后端花费在写数据文件块的时间，以毫秒计 |
| stats\_reset | timestamp with time zone | 上次重置统计信息的时间 |

### pg\_stat\_database\_conflicts

pg\_stat\_database\_conflicts视图为每一个 数据库包含一行，用来显示数据库范围内由于与后备服务器上的恢复过程冲突而被取消的查询的统计信息。 这个视图将只包含后备服务器上的信息，因为冲突会不发生在主服务器上。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| datid | oid | 一个数据库的 OID |
| datname | name | 这个数据库的名称 |
| confl\_tablespace | bigint | 这个数据库中由于表空间被删掉而取消的查询数量 |
| confl\_lock | bigint | 这个数据库中由于锁超时而 取消的查询数量 |
| confl\_snapshot | bigint | 这个数据库中由于旧快照而取消的查询数量 |
| confl\_bufferpin | bigint | 这个数据库中由于被占用的缓冲区而取消的查询数量 |
| confl\_deadlock | bigint | 这个数据库中由于死锁而取消的查询数量 |

### pg\_stat\_all\_tables

pg\_stat\_all\_tables视图将为当前数据库中的每一个表（包括TOAST表）包含一行，该行显示与对该表的访问相关的统计信息。pg\_stat\_user\_tables和pg\_stat\_sys\_tables视图包含相同的信息，分别只显示用户表和系统表。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| relid | oid | 一个表的 OID |
| schemaname | name | 这个表所在的模式的名称 |
| relname | name | 这个表的名称 |
| seq\_scan | bigint | 在这个表上发起的顺序扫描的次数 |
| seq\_tup\_read | bigint | 被顺序扫描取得的活着的行的数量 |
| idx\_scan | bigint | 在这个表上发起的索引扫描的次数 |
| idx\_tup\_fetch | bigint | 被索引扫描取得的活着的行的数量 |
| n\_tup\_ins | bigint | 被插入的行数 |
| n\_tup\_upd | bigint | 被更新的行数（包括 HOT 更新的行） |
| n\_tup\_del | bigint | 被删除的行数 |
| n\_tup\_hot\_upd | bigint | 被更新的HOT行数（即不要求独立索引更新的行更新） |
| n\_live\_tup | bigint | 活着的行的估计数量 |
| n\_dead\_tup | bigint | 死亡行的估计数量 |
| n\_mod\_since\_analyze | bigint | 从这个表最后一次被分析后备修改的行的估计数量 |
| last\_vacuum | timestamp with time zone | 上次这个表被手动清理的时间（不统计VACUUM FULL） |
| last\_autovacuum | timestamp with time zone | 上次这个表被自动清理守护进程清理的时间 |
| last\_analyze | timestamp with time zone | 上次这个表被手动分析的时间 |
| last\_autoanalyze | timestamp with time zone | 上次这个表被自动清理守护进程分析的时间 |
| vacuum\_count | bigint | 这个表已被手工清理的次数（不统计VACUUM FULL） |
| autovacuum\_count | bigint | 这个表已被自动清理守护进程清理的次数 |
| analyze\_count | bigint | 这个表已被手工分析的次数 |
| autoanalyze\_count | bigint | 这个表已被自动清理守护进程分析的次数 |

### pg\_stat\_all\_indexes

pg\_stat\_all\_indexes视图将为当前数据库中的每个索引包含一行，该行显示关于对该索引访问的统计信息。pg\_stat\_user\_indexes和pg\_stat\_sys\_ indexes视图包含相同的信息，分别显示用户索引和系统索引。

索引可以被简单索引扫描、“位图”索引扫描以及优化器使用。在一次位图扫描中，多个索引的输出可以被通过AND或OR规则组合，因此当使用一次位图扫描时难以将取得的个体堆行与特定的索引关联起来。因此，一次位图扫描会增加它使用的索引的pg\_stat\_all\_indexes.idx\_tup\_read计数，并且为每个表增 加pg\_stat\_all\_tables.idx\_tup\_fetch计数，但是它不影响pg\_stat\_all\_indexes.idx\_tup\_fetch。如果所提供的常量值不在优化器统计信息记录的范围之内，优化器也会访问索引来检查，因为优化器统计信息可能已经旧了。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| relid | oid | 这个索引的基表的 OID |
| indexrelid | oid | 这个索引的OID |
| schemaname | name | 这个索引所在的模式的名称 |
| relname | name | 这个索引的基表的名称 |
| indexrelname | name | 这个索引的名称 |
| idx\_scan | bigint | 在这个索引上发起的索引扫 描次数 |
| idx\_tup\_read | bigint | 在这个索引上由扫描返回的索引项数量 |
| idx\_tup\_fetch | bigint | 被使用这个索引的简单索引扫描取得的活着的表行数量 |

### pg\_statio\_all\_tables

pg\_statio\_all\_tables 视图将包含当前数据库中每个表的一行（包括 TOAST 表），显示关于该特定表的I/O统计信息。pg\_statio\_user\_tables和 pg\_statio\_sys\_tables视图包含相同的信息，只显示用户表和系统表的统计信息。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| relid | oid | 一个表的 OID |
| schemaname | name | 这个表所在的模式的名称 |
| relname | name | 这个表的名称 |
| heap\_blks\_read | bigint | 从这个表读取的磁盘块数量 |
| heap\_blks\_hit | bigint | 在这个表中的缓冲区命中数 量 |
| idx\_blks\_read | bigint | 从这个表上所有索引中读取 的磁盘块数 |
| idx\_blks\_hit | bigint | 在这个表上的所有索引中的 缓冲区命中数量 |
| toast\_blks\_read | bigint | 从这个表的 TOAST 表（如果 有）读取的磁盘块数 |
| toast\_blks\_hit | bigint | 在这个表的 TOAST 表（如果 有）中的缓冲区命中数量 |
| tidx\_blks\_read | bigint | 从这个表的 TOAST 表索引 （如果有）中读取的磁盘块数 |
| tidx\_blks\_hit | bigint | 在这个表的 TOAST 表索引 （如果有）中的缓冲区命中 数量 |

### pg\_statio\_all\_indexes

pg\_statio\_all\_indexes视图将包含当前数据库中每个索引的一行，显示关于该特定索引的 I/O 统计信息。pg\_statio\_user\_indexes和pg\_statio\_sys\_indexes视图包含相同的信息，只显示用户索引和系统索引的统计信息。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| relid | oid | 这个索引的基表的 OID |
| indexrelid | oid | 这个索引的 OID |
| schemaname | name | 这个索引所在的模式的名称 |
| relname | name | 这个索引的基表的名称 |
| indexrelname | name | 这个索引的名称 |
| idx\_blks\_read | bigint | 从这个索引读取的磁盘块数 |
| idx\_blks\_hit | bigint | 在这个索引中的缓冲区命中数量 |

### pg\_statio\_all\_sequences

pg\_statio\_all\_sequences视图将为当前数据库中的每个序列包含一行，该行显示在指定序列上有关I/O的统计信息。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| relid | oid | 一个序列的 OID |
| schemaname | name | 这个序列所在的模式的名称 |
| relname | name | 这个序列的名称 |
| blks\_read | bigint | 从这个序列中读取的磁盘块数 |
| blks\_hit | bigint | 在这个序列中的缓冲区命中数量 |

### pg\_stat\_user\_functions

pg\_stat\_user\_functions视图将为每一个被追踪的函数包含一行，该行显示有关该函数执行的统计信息。track\_functions参数控制到底哪些函数被跟踪。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| funcid | oid | 一个函数的OID |
| schemaname | name | 这个函数所在的模式的名称 |
| funcname | name | 这个函数的名称 |
| calls | bigint | 这个函数已经被调用的次数 |
| total\_time | double precision | 在这个函数以及它所调用的其他函数中花费的总时间，以毫秒计 |
| self\_time | double precision | 在这个函数本身花费的总时间，不包括被它调用的其他函数，以毫秒计 |

### pg\_stat\_slru

通过SLRU（简单的最近未使用）缓存访问某些磁盘信息。pg\_stat\_slru视图将包含每个被跟踪的SLRU缓存的一行，显示关于对缓存页面的访问统计信息。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| name | Text | SLRU名称 |
| blks\_zeroed | bigint | 初始化期间被置零的块数 |
| blks\_hit | bigint | 在SLRU中找到磁盘块的次数，因此不需要读取（仅包括SLRU中的命中，不包括操作系统的文件系统缓存） |
| blks\_read | bigint | 读取该SLRU的磁盘块数 |
| blks\_written | bigint | 为该SLRU写入的磁盘块数 |
| blks\_exists | bigint | 为该SLRU检查存在的块数 |
| flushes | bigint | 为该SLRU刷新脏数据的次数 |
| truncates | bigint | 该SLRU的截断次数 |
| stats\_reset | bigint | 上次重置统计数据的时间 |

### Statistics Functions

其他查看统计信息的方法是直接使用查询，这些查询使用上述标准视图用到的底层统计信息访问函数。如要了解如函数名等细节，可参考标准视图的定义（例如，在psql中你可以发出\\d+ pg\_stat\_activity）。针对每一个数据库统计信息的访问函数把一个数据库 OID 作为参数来标识要报告哪个数据库。而针对每个表和每个索引的函数要求表或索引 OID。针对每个函数统计信息的函数用一个函数 OID。注意只有在当前数据库中的表、索引和函数才能被这些函数看到。

| **函数** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_backend\_pid() | integer | 处理当前会话的服务器进程 的进程 ID |
| pg\_stat\_get\_activity(integer) | setof record | 返回具有指定PID的后端相关的一个记录，或者在指 定NULL的情况下为系统中每 一个活动后端返回一个记录。被返回的域是pg\_stat\_activity视图中 的那些域的一个子集。 |
| pg\_stat\_get\_snapshot\_timestamp() | timestamp with time zone | 返回当前统计信息快照的时间戳 |
| pg\_stat\_get\_xact\_blocks\_fetched (oid) | bigint | 在当前事务中，返回对表或索引的块读取请求的数量。这个数字减去 pg\_stat\_get\_xact\_blocks\_hit就是内核read()调用的数量；由于内核级别的缓冲，实际物理读取的数量通常较低。 |
| pg\_stat\_get\_xact\_blocks\_hit (oid) | bigint | 返回当前事务中表或索引的块读取请求数量，这些请求在缓存中找到（不会触发内核的read()调用）。 |
| pg\_stat\_clear\_snapshot() | void | 把用于当前数据库的所有统计计数器重置为零（默认要求超级用户权限，但这个函数的EXECUTE可以被授予给其他人）。 |
| pg\_stat\_reset () | void | 重置当前数据库的所有统计计数器为零。此函数默认仅限超级用户使用，但可以授予其他用户执行权限以运行该函数。 |
| pg\_stat\_reset\_shared(text) | void | 把某些集簇范围的统计计数器重置为零，具体哪些取决于参数（默认要求超级用户权限，但这个函数的 EXECUTE 可以被授予给其他人）。 调用pg\_stat\_reset\_shared(‘bgwriter’)把pg\_stat\_bgwriter 视图中显示的所有计数器清零。调 用pg\_stat\_reset\_shared(‘archiver’) 将会把pg\_stat\_archiver视图中展示的所有计数器清零 |
| pg\_stat\_reset\_single\_table\_counters(oid) | void | 把当前数据库中用于单个表或索引的统计数据重置为零 （默认要求超级用户权限，但这个函数的 EXECUTE 可以被授予给其他人） |
| pg\_stat\_reset\_single\_function\_counters(oid) | void | 把当前数据库中用于单个函数的统计信息重置为零（默认要求超级用户权限，但这个函数的 EXECUTE 可以被授予给其他人） |
| pg\_stat\_reset\_slru ( text ) | void | 将单个SLRU缓存或集群中所有SLRU的统计信息重置为零。如果参数为NULL，则将重置所有SLRU缓存的pg\_stat\_slru视图中显示的所有计数器。参数可以是CommitTs、MultiXactMember、MultiXactOffset、Notify、Serial、Subtrans或Xact之一，以仅重置该条目的计数器。如果参数是其他（或者确实是任何未识别的名称），那么将重置所有其他SLRU缓存的计数器，例如扩展定义的缓存。此函数默认仅限超级用户使用，但可以授予其他用户执行权限以运行该函数。 |
| pg\_stat\_reset\_replication\_slot (text) | void | 重置由参数定义的复制槽的统计信息。如果参数为NULL，则重置所有复制槽的统计信息。此函数默认仅限超级用户使用，但可以授予其他用户执行权限以运行该函数。 |

pg\_stat\_get\_activity是pg\_stat\_activity视图的底层函数，它返回一个行集合，其中包含有关每个后端进程所有可用的信息。有时只获得该信息的一个子集可能会更方便。在那些情况中，可以使用一组更老的针对每个后端的统计访问函数。这些访问函数使用一个后端ID号，范围从1到当前活动后端数目。函数pg\_stat\_get\_backend\_idset提供了一种方便的方法为每个活动后端产生一行来调用这些函数。例如，要显示PID以及所有后端当前的查询：

SELECT pg\_stat\_get\_backend\_pid(s.backendid) AS pid,

pg\_stat\_get\_backend\_activity(s.backendid) AS query

FROM (SELECT pg\_stat\_get\_backend\_idset() AS backendid) AS s;

| **函数** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_stat\_get\_backend\_idset() | setof integer | 当前活动后端ID号的集合（从1到活动后端数目） |
| pg\_stat\_get\_backend\_activity | (integer) | 这个后端最近查询的文本 |
| pg\_stat\_get\_backend\_activity\_start(integer) | timestamp with time zone | 最近查询被开始的时间 |
| pg\_stat\_get\_backend\_client\_addr(integer) | inet | 该客户端连接到这个后端的 IP 地址 |
| pg\_stat\_get\_backend\_client\_port(integer) | integer | 该客户端用来通信的 TCP 端口号 |
| pg\_stat\_get\_backend\_dbid(integer) | oid | 这个后端连接到的数据库的OID |
| pg\_stat\_get\_backend\_pid(integer) | integer | 这个后端的进程ID |
| pg\_stat\_get\_backend\_start(integer) | timestamp with time zone | 这个进程被开始的时间 |
| pg\_stat\_get\_backend\_userid(integer) | oid | 登录到这个后端的用户的 OID |
| pg\_stat\_get\_backend\_wait\_event\_type(integer) | text | 如果后端正在等待，则是等待事件类型的名称，否则为NULL。 |
| pg\_stat\_get\_backend\_wait\_event(integer) | text | 如果后端正在等待，则是等待事件的名称，否则为NULL。 |
| pg\_stat\_get\_backend\_xact\_start(integer) | timestamp with time zone | 当前事务被开始的时间 |

## 锁统计信息

监控数据库活动的另外一个有用的工具是pg\_locks系统表。这样就允许数据库管理员查看在锁管理器里面未解决的锁的信息。例如，这个功能可以被用于：

• 查看当前所有未解决的锁、在一个特定数据库中的关系上所有的锁、在一个特定关系上所有的锁，或者由一个特定瀚高数据库会话持有的所有的锁。

• 判断当前数据库中带有最多未授予锁的关系（它很可能是数据库客户端的竞争源）。

• 判断锁竞争给数据库总体性能带来的影响，以及锁竞争随着整个数据库流量的变化范围。

## 进度报告

瀚高数据库具有在命令执行过程中报告某些命令进度的能力。目前，仅支持进度报告的命令包括ANALYZE、CLUSTER、CREATE INDEX、VACUUM、COPY和BASE\_BACKUP（即pg\_basebackup用于进行基本备份的复制命令）。这在将来可能会扩展。

### ANALYZE 进度报告

当ANALYZE正在运行时，pg\_stat\_progress\_analyze视图将包含当前正在运行该命令的每个后端的一行。

下面的表描述了将报告的信息，并提供了关于如何解释它的信息。

| **列名** | **类型** | **描述** |
| --- | --- | --- |
| pid | Integer | 后端进程ID |
| datid | oid | 后端进程连接的数据库OID |
| datname | name | 后端进程连接的数据库名 |
| relid | oid | 分析表的OID |
| phase | text | 当前处理阶段。 |
| sample\_blks\_total | bigint | 将被采样的堆块的总数。 |
| sample\_blks\_scanned | bigint | 已扫描的堆块数量。 |
| ext\_stats\_total | bigint | 扩展统计数量。 |
| ext\_stats\_computed | bigint | 计算的扩展统计数量。此计数器仅在计算扩展统计时递增。 |
| child\_tables\_total | bigint | 子表数量。 |
| child\_tables\_done | bigint | 已扫描的子表数量。此计数器仅在获取继承样本行阶段时递增。 |
| current\_child\_table\_relid | oid | 当前正在扫描的子表的OID。当阶段正在获取继承样本行时，此字段有效。 |

表 分析阶段

| **阶段** | **描述** |
| --- | --- |
| initializing | 命令正在准备开始扫描堆。这个阶段预计会非常短暂。 |
| acquiring sample rows | 命令当前正在扫描由 relid 给出的表以获取样本行。 |
| acquiring inherited sample rows | 命令当前正在扫描子表以获取样本行。列 child\_tables\_total、child\_tables\_done 和 current\_child\_table\_relid 包含此阶段的进度信息。 |
| computing statistics | 命令正在根据在表扫描期间获取的样本行计算统计信息。 |
| computing extended statistics | 命令正在根据在表扫描期间获取的样本行计算扩展统计信息。 |
| finalizing analyze | 命令正在更新pg\_class。当此阶段完成时，ANALYZE 将结束。 |

当在分区表上运行ANALYZE时，它的所有分区也会被递归分析。在这种情况下，首先为父表报告ANALYZE进度，收集其继承统计信息，然后为每个分区报告进度。

### CREATE INDEX进度报告

每当CREATE INDEX或REINDEX运行时，pg\_stat\_progress\_create\_index视图将包含当前正在创建索引的每个后端的一条记录。

下面的表格描述了将被报告的信息，并提供了如何解释这些信息。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| pid | integer | 后端进程ID. |
| datid | oid | 该后端连接的数据库OID。 |
| datname | name | 与此后端连接的数据库的名称。 |
| relid | oid | 创建索引所依据的表OID。 |
| index\_relid | oid | 被创建或重新索引的索引的OID。在非当前的CREATE INDEX中，这个值为0。 |
| command | text | 正在运行的命令：CREATE INDEX, CREATE INDEX CONCURRENTLY, REINDEX, 或 REINDEX CONCURRENTLY. |
| phase | text | 索引创建的当前处理阶段。 |
| lockers\_total | bigint | 在适用的情况下，需要等待的储物柜总数。 |
| lockers\_done | bigint | 已经等待的储物柜数量。 |
| current\_locker\_pid | bigint | 目前正在等待的储物柜的进程ID。 |
| blocks\_total | bigint | 本阶段要处理的区块总数。 |
| blocks\_done | bigint | 当前阶段已经处理的区块数量。 |
| tuples\_total | bigint | 当前阶段要处理的元组数。 |
| tuples\_done | bigint | 在当前阶段已经处理的元组数量。 |
| partitions\_total | bigint | 在分区表上创建索引时，该列被设置为要在其上创建索引的分区总数。 |

表 创建索引阶段

| **阶段** | **描述** |
| --- | --- |
| initializing | CREATE INDEX或REINDEX正在准备创建索引。这个阶段预计会非常短暂。 |
| waiting for writers before build | CREATE INDEX CONCURRENTLY或REINDEX CONCURRENTLY正在等待有可能看到表的写锁的事务完成。当不在并发模式时，这个阶段会被跳过。lockers\_total、 lockers\_done和current\_locker\_pid列包含了这个阶段的 进度信息。 |
| building index | 索引是由访问方法专用代码建立的。 在这一 阶段，支持进度报告的访问方法填写自己的 进度数据，子阶段在这一栏中表示。 通常情 况下，blocks\_total和blocks\_done将包含进度数据，也可能包含tuples\_total和tuples\_done。 |
| waiting for writers before validation | CREATE INDEX CONCURRENTLY或REINDEX CONCURRENTLY正在等待有可能写入表的事务完成写锁的事务。当不在并发模式时，这个阶段会被跳过。lockers\_total、lockers\_done 和 current\_locker\_pid 列包含了这个阶段的进度信息。 |
| index validation: scanning index | CREATE INDEX CONCURRENTLY正在扫描索引，搜索需要验证的图元组。如果不是在并发模式下，这个阶段会被跳过。列blocks\_total（设置为索引的总大小）和blocks\_done包含了这个阶段的进度信息。 |
| index validation: sorting tuples | CREATE INDEX CONCURRENTLY正在对索引扫描阶段的输出进行排序。 |
| index validation: scanning table | CREATE INDEX CONCURRENTLY正在扫描表，以 验证前两个阶段收集的索引图元。当不在并发模式时，这个阶段被跳过。blocks\_total列（设置为表的总大小） 和blocks\_done列包含这个阶段的进度信息。 |
| waiting for old snapshots | CREATE INDEX CONCURRENTLY或REINDEX CONCURRENTLY正在等待可能看到表的事务释放快照。 当不处于并发模式时，这个阶段会被跳过。lockers\_total、lockers\_done和current\_locker\_pid 列包含了这个阶段的进度信息。 |
| waiting for readers before marking dead | REINDEX CONCURRENTLY等待表上有读锁的事务完成后，再将旧索引标记为死索引。当不在并发模式时，这个阶段被跳过。lockers\_total、lockers\_done和current\_locker\_pid 列包含了这个阶段的进 度信息。 |
| waiting for readers before dropping | REINDEX CONCURRENTLY等待表上有读锁的事务完成后，再丢弃旧索引。当不在并发模式时，这个阶段被跳过。列lockers\_total、lockers\_done和current\_locker\_pid包含了这个阶段的进度信息。 |

### VACUUM进度报告

只要VACUUM正在运行，每一个当前正在清理的后端（包括autovacuum工作者进程）在pg\_stat\_progress\_vacuum视图中都会有一行。

下面的表描述了将被报告的信息并且提供了如何解释它们的信息。VACUUM FULL命令的进度是通过pg\_stat\_progress\_cluster报告的，因为VACUUM FULL和CLUSTER都是重写表，而普通的VACUUM只是原地修改表。

| **列** | **类型** | **描述** |
| --- | --- | --- |
| pid | integer | 后端的进程ID。 |
| datid | oid | 这个后端连接的数据库的OID。 |
| datname | name | 这个后端连接的数据库的名 称。 |
| relid | oid | 被vacuum的表的OID。 |
| phase | text | vacuum的当前处理阶段。 |
| heap\_blks\_total | bigint | 该表中堆块的总数。这个数 字在扫描开始时报告，之后 增加的块将不会（并且不需 要）被这个VACUUM访问。 |
| heap\_blks\_scanned | bigint | 被扫描的堆块数量。由于可 见性映射被用来优化扫描， 一些块将被跳过而不做检查，被跳过的块会被包括在这个总数中，因此当清理完成时这个数字最终将会等于heap\_blks\_total。仅当处于扫描堆阶段时这个计数器才会前进。 |
| heap\_blks\_vacuumed | bigint | 被清理的堆块数量。除非表 没有索引，这个计数器仅在 处于清理堆阶段时才会前进。不包含死亡元组的块会被跳过，因此这个计数器可 能有时会向前跳跃一个比较 大的增量。 |
| index\_vacuum\_count | bigint | 已完成的索引清理周期数。 |
| max\_dead\_tuples | bigint | 在需要执行一个索引清理周 期之前我们可以存储的死亡 元组数，取决于maintenance\_work\_mem。 |
| num\_dead\_tuples | bigint | 从上一个索引清理周期以来 收集的死亡元组数。 |

表 VACUUM阶段

| **阶段** | **描述** |
| --- | --- |
| initializing | VACUUM正在准备开始扫描堆。这个阶段应该很简短。 |
| scanning heap | VACUUM正在扫描堆。如果需要，它将会对每个页面进行修建以及碎片整理，并且可能会 执行冻结动作。heap\_blks\_scanned列可以用来监控扫描的进度。 |
| vacuuming indexes | VACUUM当前正在清理索引。如果一个表拥有索引，那么每次清理时这个阶段会在堆扫描 完成后至少发生一次。如果maintenance\_work\_mem不足以存放找到的 死亡元组，则每次清理时会多次清理索引。 |
| vacuuming heap | VACUUM当前正在清理堆。清理堆与扫描堆不是同一个概念，清理堆发生在每一次清理索 引的实例之后。如果heap\_blks\_scanned小 于heap\_blks\_total，系统将在这个阶段完成之后回去扫描堆；否则，系统将在这个阶段完成后开始清理索引。 |
| cleaning up indexes | VACUUM当前正在清除索引。这个阶段发生在堆被完全扫描并且对堆和索引的所有清理都已经完成以后。 |
| truncating heap | VACUUM正在截断堆，以便把关系尾部的空页面返还给操作系统。这个阶段发生在清除完 索引之后。 |
| performing final cleanup | VACUUM在执行最终的清除。在这个阶段中，VACUUM将清理空闲空间映射、更新pg\_class中的统计信息并且将统计信息报告给统计收集器。当这个阶段完成时，VACUUM也就结束了。 |

### CLUSTER进度报告

每当CLUSTER或VACUUM FULL正在运行时，pg\_stat\_progress\_cluster视图将包含当前正在运行任一命令的每个后端的一行。

下面的表描述了将报告的信息，并提供了关于如何解释它的信息。

表 pg\_stat\_progress\_cluster 视图

| **列** | **类型** | **描述** |
| --- | --- | --- |
| pid | integer | 后台的进程ID。 |
| datid | oid | 该后端连接的数据库的OID。 |
| datname | name | 与此后端连接的数据库的名 称。 |
| relid | oid | 被聚类的表的OID。 |
| command | text | 正在运行的命令。CLUSTER或VACUUM FULL。 |
| phase | text | 当前处理阶段。 |
| cluster\_index\_relid | oid | 如果正在使用索引对表进行 扫描，这就是正在使用的索 引的OID；否则为0。 |
| heap\_tuples\_scanned | bigint | 扫描的堆元组数. 这个计数器 只有在阶段为 seq scanning heap, index scanning heap or writing new heap时才会前进。 |
| heap\_tuples\_written | bigint | 写入的堆元组的数量。这 个计数器只有在阶段为 seq scanning heap, index scanning heap or writing new heap时才会前进。 |
| heap\_blks\_total | bigint | 表中的堆块总数。这个数字 是在seq扫描堆的开始时报告的。 |
| heap\_blks\_scanned | bigint | 扫描的堆块数量。这个计数 器只有在阶段为seq扫描堆时才会前进。 |
| index\_rebuild\_count | bigint | 重建的索引数。该计数器仅 在重建索引阶段时才会前进。 |

表 CLUSTER 和 VACUUM FULL 阶段

| **阶段** | **描述** |
| --- | --- |
| initializing | 该命令准备开始扫描堆栈。这个阶段预计会 非常短暂。 |
| seq scanning heap | 该命令目前采用顺序扫描的方式对表进行扫 描。 |
| index scanning heap | CLUSTER目前正在使用索引扫描表。 |
| sorting tuples | CLUSTER目前正在对元组进行排序。 |
| writing new heap | CLUSTER目前正在编写新的堆。 |
| swapping relation files | 目前，该命令正在将新建立的文件调换到位。 |
| rebuilding index | 该命令目前正在重建一个索引。 |
| performing final cleanup | 该命令正在执行最后的清理工作。当此阶段 完成后，CLUSTER或VACUUM FULL将结束。 |

### Base Backup进度报告

每当应用程序像pg\_basebackup正在进行基本备份时，pg\_stat\_progress\_basebackup视图将包含当前正在运行BASE\_BACKUP复制命令并流式传输备份的每个WAL发送进程的一行。

下面的表描述了将报告的信息，并提供了关于如何解释它的信息。

表 pg\_stat\_progress\_basebackup视图

| **列** | **类型** | **描述** |
| --- | --- | --- |
| pid | Integer | WAL Sender的进程ID。 |
| phase | text | 当前处理阶段。 |
| backup\_total | bigint | 将被流式传输的数据总量。这是在开始流式传输数据库文件阶段估计和报告的。请注意，这只是一个近似值，因为在流式传输数据库文件阶段期间数据库可能会发生更改，并且WAL日志可能会在稍后包含在备份中。一旦流式传输的数据量超过估计的总大小，此值就会与 backup\_streamed 相同。如果在pg\_basebackup中禁用了估算（即指定了–no-estimate-size选项），则此值为NULL。 |
| backup\_streamed | bigint | 已流式传输的数据量。此计数器仅在阶段为流式传输数据库文件或传输wal文件时递增。 |
| tablespaces\_total | bigint | 将被流式传输的表空间总数。 |
| tablespaces\_streamed | bigint | 已流式传输的表空间数量。此计数器仅在阶段为流式传输数据库文件时递增。 |

表 Base Backup阶段

| **阶段** | **描述** |
| --- | --- |
| Initializing | WAL发送进程正在准备开始备份。这个阶段预计会非常短暂。 |
| waiting for checkpoint to finish | WAL发送进程当前正在执行pg\_start\_backup以准备进行基本备份，并等待开始备份检查点完成。 |
| estimating backup size | WAL发送进程当前正在估算将作为基本备份流式传输的数据库文件的总量。 |
| streaming database files | WAL发送进程当前正在作为基本备份流式传输数据库文件。 |
| waiting for wal archiving to finish | WAL发送进程当前正在执行pg\_stop\_backup以完成备份，并等待成功归档用于基本备份的所有WAL文件。如果在pg\_basebackup中指定了–wal-method=none或–wal-method=stream，则当此阶段完成时备份将结束。 |
| transferring wal files | WAL发送进程当前正在传输备份期间生成的所有WAL日志。如果在pg\_basebackup中指定了–wal-method=fetch，则此阶段将在等待wal归档完成阶段之后发生。备份将在此阶段完成时结束。 |

### COPY进度报告

每当COPY正在运行时，pg\_stat\_progress\_copy视图将包含当前正在运行COPY命令的每个后端的一行。

下表描述了将被报告的信息，并提供了解释的信息。

表 pg\_stat\_progress\_copy 视图

| **列** | **类型** | **描述** |
| --- | --- | --- |
| pid | Integer | 后端进程ID。 |
| datid | oid | 连接到此后端的数据库的OID。 |
| datname | name | 连接到此后端的数据库的名称。 |
| relid | oid | 执行COPY命令的表的OID。如果从SELECT查询中复制，则设置为0。 |
| command | text | 正在运行的命令：COPY FROM或COPY TO。 |
| type | text | 数据读取或写入的IO类型：FILE、PROGRAM、PIPE（用于COPY FROM STDIN和COPY TO STDOUT），或者CALLBACK（例如，在逻辑复制中的初始表同步期间使用）。 |
| bytes\_processed |  | COPY命令已处理的字节数。 |
| bytes\_total |  | COPY FROM命令的源文件大小（以字节为单位）。如果不可用，则设置为0。 |
| tuples\_processed |  | COPY命令已处理的元组数。 |
| tuples\_excluded |  | 由COPY命令的WHERE子句排除的未处理元组数。 |