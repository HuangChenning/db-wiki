---
title: "DMDPC配置"
book: "DM8 分布计算集群"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dpc-dispose.html
tags:
  - dameng
  - dm8
  - dpc
---

## 6.1 相关参数

### 6.1.1 DM.INI

DM.INI 是 DM 数据库实例的配置文件，通过配置该文件可以设置 DM 数据库服务器的各种功能和性能选项。

#### 6.1.1.1 DMDPC 相关的参数

DM.INI 中的配置项多达数百个，涉及 DM 数据库运行各个方面的设置，这里我们只介绍与 DMDPC 相关的几个配置项，读者若对其他配置项感兴趣可以参看《DM8 系统管理员手册》的相关章节。

表6.1 DM.INI DMDPC相关配置项

| **参数** | **说明** | **属性** | **缺省值** |
| --- | --- | --- | --- |
| INSTANCE\_NAME | 实例名称。推荐以角色开头，例如：SP\_1，BP\_2 | 静态 | DMSERVER |
| PORT\_NUM | 数据库服务器监听端口，SP/BP 本地设置的 PORT\_NUM 如果和自身在 MP 上注册的不一致，按照在 MP 上实际注册的为准，启动时会自动覆盖 | 静态 | 5236 |
| AP\_PORT\_NUM | 分布式环境下协同工作的监听端口，SP/BP 本地设置的 AP\_PORT\_NUM 如果和自身在 MP 上注册的 AP\_PORT\_NUM 不一致，按照在 MP 上实际注册的为准，启动时会自动覆盖 | 静态 | 0 |
| DPC\_OPT\_FLAG | 执行计划优化策略。取值 1、2、4、8、16、32、64、128、256、512、1024、2048、4096、8192、16384、32768、65536、131072、262144、524288、1048576、2097152 或上述任意取值的和。   1：表示忽略 UNIONALL，将分支的内容直接发给 UNIONALL 之上的 ERECV；   2：表示根据 HSCN 的使用情况，对 HTAB 的分布信息调整，可以减少 HSCN 之后的数据分发量；   4：表示在通讯符之前将 afun 转换成两个，可以减少通讯量；   8： 表示按照实际执行的 BP 个数调整子任务并行度；   16：根据利用统计信息最大、最小值计算相同表不同别名的选择率。例如 t1.c1 + 10 > t1.c1 ==> t1.c1 < max(t1.c1) +10；   32：同时开启 SP、MP 和 BP 节点的计划缓存的功能，减少事务密集型应用中计划发送带来的耗时。可通过 V$SQL\_PLAN 查询到 BP 端缓存的不完整计划，其 RET\_CMD 字段为 0。非 32 的情况下，只有 SP 具有计划缓存功能；   64：多列 primary key 用于连接时的行数估算调整优化；   128：根据估算的行数对连接、分组等使用到的哈希表大小进行缩放优化；   256：哈希连接时，如果连接左边数据来自广播，启用共享哈希表优化减少哈希表构造开销；   512：huge 表考虑 hfsek 与 hfscn+slct 的代价；   1024：计划只从几个子任务开始，而不是所有的叶子节点；   2048：DISTINCT 尝试下放至集合运算的左右侧的子任务先做；   4096：afun/sagr+sort+dis 的 sort 下放到 dis 下面，变成 afun/sagr+dis（归并信息）+sort。sort 放到 dis 下面后，每一路可先做排序，如果子任务并行度比 sagr/afun 的并行度大时能较快的完成排序；   8192：esend 发送时对 link\_id 进行优化。优化后，消息可以多条链路同时发生，而非一条链路串行；   16384：表示 DMDPC 环境下支持变量跨层引用；   32768：支持 L\_FULL 优化。具体为支持 LEFT JOIN 操作符左边使用全部数据，右边使用部分数据的情况；   65536：表示开启子任务为空连接提前终止的优化。若某个子任务的结果为空，上层有连接操作且可以推断出连接的结果也为空时，那直接终止此连接以及此连接的所有子任务。这个过程是可以向上传递的，直到某个子任务结果不为空或者无法推断为空为止；   131072：表示当某任务的子任务都在同一个站点上时，那么系统会优先让这个任务也在此站点做。因为数据在同站点不同线程内传输，相比不同站点会减小数据传输时间；   262144：表示将 GROUP BY 最大值下放到 HTAB；   524288：表示 SP、BS 节点考虑将接收到的简单 SQL（非分区表查询、包含分区列等值条件过滤的查询、行分区表的值插入等）转发给对应的 BP 节点处理以提升性能；此优化还需要设置 USE\_PLN\_POOL 非 0 开启计划重用，并与 DPC\_OPT\_FLAG 取值 32 一起使用；   1048576：当哈希连接的 KEY 包含有大量 NULL 值时，是否启用空值的分发优化。开启后，连接 KEY 包含 NULL 值的记录会根据语义选择自动丢弃或随机选择目标线程；   2097152：两层 GROUP 且中间是 DIS 时，如果下层 HAGR 有冲突，直接将冲突的输出 | 动态，会话级 | 65407 |
| ALTER\_MODE\_STATUS | 在多副本系统中使用。 是否允许手工修改服务器的模式、状态和 OGUID。1：允许；0：不允许。建议设置为 0 | 动态，系统级 | 1 |
| DPC\_2PC | DMDPC 系统是否采用两阶段提交策略及是否使用优化方案。 0：关闭两阶段提交，没有故障的情况下直接提交效率更高，但是出现故障就无法保证事务一致性了； 1：启用两阶段提交； 2 或 3：启用两阶段提交，启用 trxid 缓存，启用 snap\_seq 缓存方案优化； 4 或 5：启用两阶段提交，启用 trxid 缓存，启用 snap\_seq 本地优化； 6 或 7：启用两阶段提交，启用 trxid 缓存，启用 snap\_seq 缓存，启用 snap\_seq 本地优化 | 手动 | 1 |
| SWITCH\_CONN | JDBC 客户端是否进行连接切换，执行过程中发现计划只和一个 BP 相关时，客户端是否切换到该 BP 执行。 0：否；1：是。 此参数需要和 JDBC 驱动/dm\_svc.conf 配合使用，只用于 BS 模式 | 动态，系统级 | 0 |
| TRC\_LOG | TRACE 日志开关。需和 TRC\_LOG\_MODULE 配合使用。 0：表示关闭； 非 0：为功能组合值，组合规则为： switch\_mod *4 + asyn\_flag* 2 + 1。其中，<switch\_mode> 日志文件切换方式： 0 不切换；1 按文件记录行数，满 10000 行切换；2 按文件大小进行切换，满 128M 切换； 3 按时间间隔进行切换，每小时切换。 <asyn\_flag> 日志文件是否采用异步方式：0 否，采用同步方式； 1 是，采用异步方式 。 TRACE 日志位于安装目录下的/log 中，名称为 dmtrc\_instname.log（不含切换方式）或 dmtrc\_instname\_日期时间.log（含有切换方式） | 动态，系统级 | 0 |
| TRC\_LOG\_MODULE | 当打开 TRC\_LOG 开关时，用于配置 TRACE 日志中记录的内容。该参数为字符类型，最大长度 128。 书写格式为：TRC\_LOG\_MODULE=服务器记录项,DMDPC 记录项。 服务器记录项和 DMDPC 记录项设置方法相同。缺省表示不记录该模块中的任何内容。 具体记录项和代号： 内存 MEM (0)、任务线程 TSK (1) 、站点信息 SITE (2) 、事务 TRX (3) 、通信消息 MSG (4) 、 会话 SESS (5) 、计划 PLN\_GEN (6) 、HUGE 文件系统 HFS (7)、LOCK 相关(8)、快速装载服务器端模块 BLDR(9)、字典 DICT(10)、错误堆栈 ESTK(11) 、用户自定义向日志写入内容(12)、0 ~~12 全部记录(ALL)。多个记录项之间使用冒号(:)分割。 例如： 1）记录 0~~ 12 项所有的信息，需设置 trc\_log\_module = ALL 2）只服务器模块记录 HFS 和 TRX，DMDPC 模块不记录，需设置 trc\_log\_module= 3:7, 3）只 DMDPC 模块记录 MSG，服务器模块不记录，需设置 trc\_log\_module=,4 4）若服务器记录 HFS 和 TRX，DMDPC 记录 MSG，需设置 trc\_log\_module=3:7,4 | 动态，系统级 | ALL |
| DPC\_LOG\_INTERVAL | MP 定时通知各节点生成相同时间点日志的时间间隔。取值范围 0~1440（24 小时）。以分钟为单位。0 表示关闭定时通知功能。 此参数打开后，可支持使用归档恢复到指定时间点功能，在对系统性能有要求的情况下，可以调大或关闭此参数值 | 动态，系统级 | 0 |
| SQC\_GI\_NUM\_PER\_TAB | 每个表拆分的扫描单元个数。取值范围 1~1024。 扫描表对象时，每个表可以被拆分成多个单元以提升并行性能。参数值表示拆分的单元个数，每个单元可以独立用于工作线程的扫描任务。例如：需要扫描一个子表且子表数据量较大，为充分利用工作线程资源，可以调大此参数以使用分区内并行 | 动态，会话级 | 1 |
| HP\_TAB\_COUNT\_PER\_BP | 创建一级、二级哈希分区时，如果分区数指定为 DEFAULT 而不是具体数值，系统会根据本参数值决定每个 BP RAFT 上创建的哈希子表个数。 取值范围 1~1024 | 动态，会话级 | 1 |
| DPC\_SYNC\_STEP | 打开 DMDPC 限流（MPP\_MOTION\_SYNC 非 0）时使用。 表示检查接收端数据堆积的步长，即每发送 DPC\_SYNC\_STEP 次 BDTA 后检查一次是否堆积。取值范围 1~5000 | 动态，会话级 | 16 |
| DPC\_SYNC\_TOTAL | 打开 DMDPC 限流（MPP\_MOTION\_SYNC 非 0）时使用。XBOX 上所有来源路数（并行线程数）的总限流资源数。取值范围 0~10000。0 表示不限总资源数 | 动态，会话级 | 0 |
| XBOX\_DUMP\_THRESHOLD | XBOX 邮件内存阈值，超过该值则保存到文件中。取值范围 0~409600。单位 MB。 和 XBOX\_DUMP\_PATH 一起设置才生效 | 动态，系统级 | 0 |
| XBOX\_DUMP\_PATH | XBOX 邮件保存到临时文件的目录。 和 XBOX\_DUMP\_THRESHOLD 一起设置才生效 | 手动 | 空串 |
| XBOX\_SPACE\_LIMIT | 配置了 XBOX\_DUMP\_THRESHOLD 和 XBOX\_DUMP\_PATH 时有效。 表示单个 XBOX 的空间限制。取值范围 0 ~ 409600。单位 MB。0 表示不限制。 XBOX\_SPACE\_LIMIT 和 XBOXS\_SPACE\_LIMIT 可分别单独配置，也可同时配置，同时配置时须保证 XBOXS\_SPACE\_LIMIT > XBOX\_SPACE\_LIMIT | 动态，系统级 | 0 |
| XBOXS\_SPACE\_LIMIT | 配置了 XBOX\_DUMP\_THRESHOLD 和 XBOX\_DUMP\_PATH 时有效。 表示系统所有 XBOX 的总空间限制。取值范围 0 ~ 1000000。单位 MB。0 表示不限制 | 动态，系统级 | 0 |
| XBOX\_MEMORY\_TARGET | XBOX 系统内存在扩充到此大小以上后，空闲时收缩回此指定大小，单位 MB。取值范围 1024~262144 | 动态，系统级 | 1024 |
| STMT\_XBOX\_REUSE | DMDPC 会话的语句是否重用 box\_id。 0：否，每个语句都请求分配一个 box\_id； 1：是 | 动态，会话级 | 1 |
| XBOX\_SHORT\_MSG\_SIZE | 在配置了 XBOX\_DUMP\_THRESHOLD 后，即使内存达到阈值的情况下，小于此长度的短消息也不会保存到文件，防止大量的文件读写。 取值范围 0~32768。单位 BYTE | 动态，系统级 | 1024 |
| DPC\_TRX\_TIMEOUT | 用于 DMdpc 中，表示事务等待超时时间。取值范围 0~604800。单位秒 | 动态，会话级 | 10 |
| DPC\_GUP\_SESS\_TIMEOUT | 用于 DMdpc 中，表示 sP 升级时事务、会话超时断开时间。取值范围 60~600。单位秒 | 动态，会话级 | 180 |
| DPC\_TABLESPACE\_BALANCE | 当在 DPC 下创建分区表，子表个数少于所选择的表空间个数时，是否启用随机选择起始表空间以使得表空间负载均衡。0：不启用；1：启用，表示从已有子表所使用的表空间中挑选；2：启用，在新增子表时同时考虑从所有表空间中挑选 | 动态，系统级 | 1 |
| DPC\_DCT\_REFRESH\_POLICY | MP 广播实例字典信息优化开关。 0：表示关闭，MP 会定时广播实例字典信息； 1：表示打开，MP 只会在每次修改实例字典信息时进行广播 | 动态，系统级 | 1 |
| ENET\_SESS\_CHECK\_INTERVAL | 当 BP/SP 处于 MP 无效服务状态时，BP/SP 断开会话连接的时间间隔阈值。如果 BP/SP 处于 MP 无效服务状态的时间超过该阈值，则会主动断开所有会话连接。取值范围 0~4294967294，单位 S。0 表示关闭 | 动态，系统级 | 10 |
| STHD\_FLAG | 是否启用 ESESS/SESS 线程池。取值范围 0~3。0：表示关闭；1：表示打开 ESESS 线程池；2：表示打开 SESS 线程池；3：表示同时打开 ESESS 和 SESS 线程池 | 静态 | 0 |
| STHD\_THREAD\_NUM | 每个 ESESS 线程池初始化的线程数量。取值范围 1~10000 | 静态 | 8 |
| STHD\_GRP\_NUM | 初始化的 ESESS 线程池数量。取值范围 1~64。当打开 SESS 线程池（即 STHD\_FLAG=2 或 3）时，该参数强制等于 WORKER\_THREADS 的值 | 静态 | 8 |
| RLOG\_RAFT\_NEED\_WAIT | 主库是否进行日志包发送等待控制，仅 RAFT 主库生效。 0：主库不进行日志包发送控制；1：任意备库存在日志堆积时，根据 RLOG\_RAFT\_WAIT\_TIME 暂缓日志包发送；2：存在日志堆积的备库个数超过备库总数的半数时，根据 RLOG\_RAFT\_WAIT\_TIME 暂缓日志包发送；3：任意归档状态有效的备库存在日志堆积，根据 RLOG\_RAFT\_WAIT\_TIME 暂缓日志包发送；4：存在日志堆积的归档状态有效的备库个数超过备库总数的半数时，根据 RLOG\_RAFT\_WAIT\_TIME 暂缓日志包发送 | 动态， 系统级 | 3 |
| RLOG\_RAFT\_WAIT\_TIME | 备库出现堆积后，RAFT 主库延迟发送等待时间，取值范围 0~3600000，单位 MS。仅 RAFT 主库生效 | 动态， 系统级 | 1000 |
| SHADOW\_CHECK\_INTERVAL | 用于设置清理影子库的本地归档文件的时间间隔，取值范围 0~3600，单位 S。如果设为 0，则关闭自动清理功能。此参数仅对影子库有用 | 动态，系统级 | 60 |
| GROUP\_OPT\_FLAG | 分组项优化参数开关。GROUP\_OPT\_FLAG=4 须和 INI 参数 PARALLEL\_POLICY（非 0）搭配使用。   0：不优化；   1：非 MYSQL 兼容模式下（即 COMPATIBLE\_MODE 不等于 4），支持查询项不是 GROUP BY 表达式；   2：外层分组项下放到内层派生表中提前分组优化；   4：表示对于多级分区，并行下允许尝试不生成多个 agr 操作符；   8：进行哈希分组时，依赖分组项列中的核心项分组列来分组；   16：位图索引覆盖简单分组查询中的所有列时，允许使用位图索引对查询进行优化；   32：进行哈希分组时，对 TOP 查询进行优化，提前返回指定数量的分组；   64：DMDPC 下，对无分组项且含有 DISTINCT 集函数的查询，允许对集函数参数先进行一次分发处理；   128：尽量使用 SAGR+SORT 计划实现 group； 256：使用新的计算方法计算数据 DISTINCT 值，新计算方法：(i \* j)/max(((i - j) \* j/i),1)，假设其中 i > j， i、j 为每列 DISTINCT 个数；   512：SAGR 中的 count(DISTINCT)尽量使用优化模式计算；   1024：使用 COST\_CPU\_CALC\_HAGR、COST\_CPU\_CALC\_AAGR 代替 COST\_CPU\_CALC\_ORDER 计算操作符#HAGR、#AAGR 的代价；   2048：list 分区只有一个值 hagr 变 aagr，只在 dpc 环境有效；   4096：在进行分组时根据 blank\_pad\_mode 和 space\_compare\_mode 判断是否忽略后缀空格；   8192：对一级 RANGE 分区的分区首列没有分组时求 MIN/MAX，优化分区裁剪，目前优化暂不支持并行；   16384：对分区表使用 FAGR2 求 count(\*)时，不加载字典对象，使用读取系统表直接加载所有叶子表需要的信息优化方式，提升性能；   32768：有分组项和集函数有非分区列的 distinct 也支持两层分组，只在 dpc 环境有效。   支持使用上述有效值的组合值，如 3 表示同时进行 1 和 2 的优化 | 动态，会话级 | 8252 |
| STAT\_CACHE\_FLAG | SP 是否缓存表行数。 0：不缓存； 1：SP 缓存表行数，而不是每次都向 MP 请求表行数，从本地缓存中获取表行数以降低 MP 的性能瓶颈。和 STAT\_CACHE\_CAPACITY 搭配使用 | 静态 | 1 |
| STAT\_CACHE\_CAPACITY | 当 STAT\_CACHE\_FLAG=1 时使用。sp 缓存表行数的缓存容量。取值范围 100~100000000，单位缓存表的个数 | 动态，系统级 | 1000 |
| TSMV\_RAFIL\_SIZE | 指定表空间迁移的临时归档文件的最大空间。取值范围 2~1024。单位 Mb | 静态 | 64 |
| TSMV\_FILE\_COPY\_PLL | 表空间迁移时物理文件拷贝并行度。取值范围 1~128 | 动态，系统级 | 1 |
| TSMV\_WAIT\_TIMEOUT | 表空间迁移上锁等待时间。取值范围 0~12000，单位 S | 动态，系统级 | 120 |
| TSMV\_SEND\_BUF\_SIZE | 表空间迁移发送文件缓冲区大小。单位 MB，取值范围 1~64。值越小，迁移越慢，但迁移中对并发业务影响越小；值越大迁移速度越快，但迁移中对并发业务影响越大，可结合实际情况设置 | 动态，系统级 | 4 |
| MAX\_ESESSIONS | 指定分支 ESESSION 个数上限，取值范围 0~650000，0 表示无限制。ESESSION 为 SP 和其他节点之间的内部会话，SP 上的 ESESSION 为主 ESESSION，其他节点上的 ESESSION 为分支 ESESSION | 动态，系统级 | 100000 |
| DPC\_PROXY\_TIMEOUT | 允许 MP 代理处理故障 SP 事务的最小故障时间，取值范围 0~4294967294，单位秒。因为存在任务调度时间和节点故障判定时间，SP 故障后至少需要 5-10 秒才会被 MP 代理 | 动态，系统级 | 600 |
| DPC\_CONN\_POLICY | 设置 DMDPC 系统链路的管理策略，按位取值，10 进制取值如下：0：无特殊策略；1：DPC AP 监听端口如果长时间没有监听到连接，则重建监听端口；2：阻塞模式的链接对于 EINPROGRESS 错误进行检查并重试 | 动态，系统级 | 0 |
| DPC\_CHECK\_MP\_INI | 是否检查并修改 MP.INI。   0：不检查；1：检查并修改。   对于数据库迁移场景，将 MP 库物理拷贝或备份还原到另一台机器后，IP 信息会发生改变，MP 启动前需要将此参数配置为 0，避免 MP 使用字典信息中的旧 IP 信息去刷新 MP.INI。正常启动后，用户可以通过 SP\_MODIFY\_DPC\_INSTANCE 来更新 IP 等信息, 修改完成后再将该参数改回 1 | 静态 | 1 |
| SFUN\_PUSH\_DOWN\_FLAG | 是否将集函数下放到 UNIONALL 的各个分支。0：否；1：是，要求外层是简单查询 | 动态，会话级 | 1 |

> **注意**
> 
> DMDPC环境下不允许修改TS\_MAX\_ID和TS\_FIL\_MAX\_ID参数。

#### 6.1.1.2 自动覆盖不一致的参数

部分 DM.INI 参数，当 SP/BP 本地设置的 DM.INI 参数值和自身在 MP 上注册的参数值不一致时，按照在 MP 上实际注册值为准，系统启动时会将 SP/BP 本地的参数自动覆盖掉。如果 MP 为多副本架构，则以 MP 主节点为准。

会被覆盖的 DM.INI 参数为：一是包括和 DMDPC 相关的 PORT\_NUM、AP\_PORT\_NUM、DPC\_SYNC\_STEP、DPC\_SYNC\_TOTAL、STMT\_XBOX\_REUSE、DPC\_2PC；以及二是 DM 数据库通用的参数，目前有以下这些： PARALLEL\_POLICY、USE\_NEW\_HASH、COMPRESS\_MODE、LIST\_TABLE、LIST\_TABLE\_BRANCH、LIST\_TABLE\_NON\_BRANCH、COMPATIBLE\_MODE、COUNT\_64BIT、BLANK\_PAD\_MODE、ALTER\_TABLE\_OPT、DECIMAL\_FIX\_STORAGE、ENABLE\_HUGE\_SECIND、PK\_WITH\_CLUSTER、DATETIME\_FMT\_MODE、SLCT\_ERR\_PROCESS\_FLAG、FORCE\_CERTIFICATE\_ENCRYPTION、CAST\_VARCHAR\_MODE、SPACE\_COMPARE\_MODE、JSON\_MODE、JSON\_OPTION、MPP\_MOTION\_SYNC、BDTA\_SIZE、USE\_PLN\_POOL、MAX\_SESSION\_STATEMENT、MAX\_EP\_SITES、HUGE\_ENABLE\_DEL\_UPD、ENABLE\_INJECT\_HINT（只会同步 MP、SP 和 BS。BP 不支持该参数，永远为 0）、ENABLE\_FLASHBACK、UNDO\_RETENTION、ALLOWED\_CLIENT\_VERSIONS、SELECT\_LOCK\_MODE、ENABLE\_CS\_CVT、HFI\_HP\_MODE、NUMBER\_MODE、VIEW\_ACCESS\_MODE、TRUNC\_CHECK\_MODE、PL\_SQL\_STRIP、CAST\_CLOB\_MODE、WM\_CONCAT\_LOB、CALC\_AS\_DECIMAL、ORA\_REVERSE\_MODE、USE\_JSON\_DATATYPE、DEC\_CAST\_FORMAT 等。

当试图修改上述参数的内存值时，DM 服务器会拒绝并报错。

#### 6.1.1.3 从主库同步参数

在主备环境中，当备库 DM.INI 参数与主库不一致时，可在备库执行 INT SF\_SYNC\_INI( LEVEL  
INT)函数来同步主库上的 DM.INI 参数。LEVEL 为同步级别，取值 0 和 1。0 表示同步所属环境下必须同步的参数；1 表示同步所有可以同步的参数。

例 在备库上执行 SF\_SYNC\_INI 函数，备库同步主库上所有可以同步的 INI 参数。

```
SELECT SF_SYNC_INI (1);
```

SF\_SYNC\_INI 函数的详细用法请参考《DM8 SQL 语言使用手册》。

### 6.1.2 DMINIT 工具

通过 DMINIT 工具指定初始化参数。 和 DMDPC 集群搭建相关的参数如下表 6.2 所示。

使用 DMINIT 工具初始化时，如果同一个 INI 参数在 DM.INI 和 DMINIT 中分别指定了不同的值，那么以 DMINIT 工具中指定的为准。

表6.2 DMINIT工具配置参数

| **参数** | **说明** | **缺省值** |
| --- | --- | --- |
| PATH | 初始数据库存放的路径 | 无。不指定时会提示输入 |
| INSTANCE\_NAME | 实例名 | DMSERVER |
| PORT\_NUM | 数据库服务器监听端口号，取值范围 1024~65534 | 5236 |
| AP\_PORT\_NUM | 分布式环境下协同工作的监听端口号，手动配置的取值范围 1024~65534 | 0 |
| DPC\_MODE | 指定 DMDPC 集群中的实例角色。   0：无；1/MP：MP；2/BP：BP；3/SP：SP。 使用 DMINIT 搭建环境时，DPC\_MODE 参数值既可以使用数字 0/1/2/3，也可以使用 MP/BP/SP 字符串代替，二者作用等价 | 0 |

只要 DMINIT 初始化库时，指定了 DPC\_MODE 参数值，那么在 DMServer 启动时，启动参数 DPC\_MODE 值必须和 DMINIT 保持一致。否则，可能导致服务器起不来。DPC\_MODE 在 DMINIT 和 DMServer 中的取值对应关系如表 6.3 所示。

表 6.3 DMINIT 和 DMServer 中 DPC\_MODE 参数值对应关系

| **DMINIT 的 DPC\_MODE** | **DMServer 的 DPC\_MODE** |
| --- | --- |
| 0 | 0 |
| 1 或 MP | 1 或 MP |
| 2 或 BP | 2 或 BP |
| 4 或 BS |  |
| 3 或 SP | 3 或 SP |

### 6.1.3 MP.INI

DMDPC 集群中除 MP 自身外，SP、BP 都存在和 MP 通讯的可能，因此在 SP、BP 和 MP 初始化的 PATH 相同目录下需要用 MP.INI 来写明 MP 的 IP 地址和端口号。同一集群中 SP、BP 的 MP.INI 内容完全一致。

表6.4 MP.INI中的参数

| **参数名** | **说明** |
| --- | --- |
| MP\_HOST | mp 实例的 IP 地址 |
| MP\_PORT | mp 实例的监听端口号 |
| MP\_RECONN\_TIMEOUT | 连接 MP 失败时，尝试重连的超时时间。在设定的时间段内，如果与 MP 连接断开，会不断的尝试连接 MP。单位为秒。取值范围 0~4294967294，缺省为 4294967294‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬ |

例 一个完整的 MP.INI 文件内容如下：

```
mp_host = 223.254.30.136
mp_port = 9000 #与MP、BP和SP上的ap_port_num不冲突的端口号
```

### 6.1.4 DMARCH.INI

DMARCH.INI 是 DM 数据库实例的归档配置文件，用于配置数据库本地归档和 RAFT 归档。这里仅对多副本系统相关配置项进行介绍。若读者对其他配置项感兴趣，可参考《DM8 系统管理员手册》的相关章节。

表6.5 DMARCH.INI多副本相关配置项

<table><tbody><tr><td><b>项目</b></td><td><b>项目意义</b></td><td><b>字段</b></td><td><b>字段意义</b></td></tr><tr><td rowspan="9">全局配置项</td><td rowspan="9"></td><td>XMAL_HB_INTERVAL</td><td>节点间通信检测间隔。单位s，取值范围1~600。该参数仅在多副本集群中使用，多副本各实例需配置相同</td></tr><tr><td>RAFT_HB_interval</td><td>主库广播心跳消息的间隔时间。单位ms，取值范围5~1800。该参数仅在多副本集群中使用，多副本各实例需配置相同</td></tr><tr><td>RAFT_VOTE_INTERVAL</td><td>选举超时时间。单位MS，取值范围10~3600000。这个配置值需要保证至少是RAFT_HB_interval的2倍大小，确保在选举超时时间内能够收到主库的心跳消息，避免误判主库故障发起无效选举。建议各实例配置为不同的值，以便能够快速选举出主库，配置的值越小，被选举为主库的优先级越高。该参数仅在多副本集群中使用，并且仅在开启选举开关的实例上有效</td></tr><tr><td>XMAL_IP</td><td>当前副本XMAL通信IP。DMDPC环境下无需在DMARCH.INI文件中配置此项</td></tr><tr><td>XMAL_PORT</td><td>当前副本XMAL通信端口。DMDPC环境下无需在DMARCH.INI文件中配置此项</td></tr><tr><td>RAFT_SELF_ID</td><td>多副本节点编号，用于标识多副本RAFT组中不同的节点。取值范围0~31</td></tr><tr><td>RAFT_LEARNER</td><td>用于标识自己是否为LEARNER角色。1：是，0：否。 参数缺省为0，非learner节点可不配置此参数</td></tr><tr><td>RAFT_SELF_ID</td><td>多副本节点编号，用于标识多副本RAFT组中不同的节点。取值范围0~31</td></tr><tr><td>RAFT_PKG_INTERVAL</td><td>专用于多副本环境中，设置备库接收主库日志包的超时时间。当备库超过该时间还未接收到主库日志包，则备库主动断开与主库连接。单位S，取值范围60~36000。缺省为不配置该参数。可选参数</td></tr><tr><td rowspan="5">[ARCHIVE_RAFT1]</td><td rowspan="5">RAFT归档</td><td>ARCH_TYPE</td><td>归档类型。ARCH_TYPE支持配置为RAFT和LEARNER。其中LEARNER归档仅在动态增删节点时使用</td></tr><tr><td>ARCH_DEST</td><td>归档目标实例名</td></tr><tr><td>ARCH_DEST_IP</td><td>归档目标XMAL通信IP。DMDPC环境下无需在DMARCH.INI文件中配置此项</td></tr><tr><td>ARCH_DEST_PORT</td><td>归档目标XMAL通信端口。DMDPC环境下无需在DMARCH.INI文件中配置此项</td></tr><tr><td>ARCH_DEST_ID</td><td>归档目标多副本节点编号，用于标识多副本RAFT组中不同的节点。取值范围0~31</td></tr><tr><td rowspan="6">[ARCHIVE_LOCAL1]</td><td rowspan="6">本地归档配置</td><td>ARCH_TYPE</td><td>归档类型</td></tr><tr><td>ARCH_DEST</td><td>归档路径</td></tr><tr><td>ARCH_FILE_SIZE</td><td>单个归档文件大小，单位MB，取值范围64~2048，缺省为1024MB，即1G</td></tr><tr><td>ARCH_SPACE_LIMIT</td><td>归档文件空间限制，单位MB，取值范围1024~4294967294，缺省为0，表示无空间限制</td></tr><tr><td>ARCH_FILE_SIZE</td><td>归档合并刷盘缓存大小，单位MB，取值范围0~128，缺省为0，表示不使用归档合并刷盘</td></tr><tr><td>ARCH_HANG_FLAG</td><td>本地归档写入失败时系统是否挂起。取值0或1。0不挂起；1挂起。缺省为1。第一路本地归档系统内固定设为1，设0实际也不起作用</td></tr></tbody></table>

**说明：**

1. ARCH\_TYPE 表示 Redo 日志归档类型，多副本系统中需要使用到 RAFT 归档和本地归档，配置 RAFT 归档时，必须配置至少一个本地归档；
2. XMAL\_PORT 是多副本用于选举和消息通信的专用端口号。为了防止端口通信冲突，XMAL\_PORT 配置项必须不同于 dm.ini 中 PORT\_NUM 配置；
3. 由于多副本系统总的节点个数必须为奇数，因此 RAFT 归档目标个数要配置为偶数个（除去本机后剩余的节点个数），也就是最少要配置 2 个，最多允许配置 8 个；
4. 可以通过 RAFT\_VOTE\_INTERVAL 设置选举优先级，RAFT\_VOTE\_INTERVAL 配置值越小的节点实例，被选举为新主库的优先级越高。

### 6.1.5 DMServer 启动参数

DMServer 指定启动参数，表示实例以何种模式工作，相关参数如下表 6.6 所示。

表6.6 DMServer启动参数

| **参数** | **说明** | **缺省值** |
| --- | --- | --- |
| PATH | 数据库 dm.ini 存放的路径 | dm.ini 绝对路径或者 dmserver 程序当前目录的 dm.ini |
| DPC\_MODE | 实例运行模式 | 指定 DPC 中的实例角色，0：无角色，缺省为 0、1：MP、2：BP、3：SP、4：BS，取值 1/2/3/4 时也可以分别用 MP/BP/SP/BS 代替。其中 BS 模式表示直连 BP 模式，详见 3.1 基本概念 中的 BS 模式说明。DMServer 启动时，DPC\_MODE 在 DMINIT 和 DMServer 中的取值须按照对应关系正确对应，对应关系请参考 DMINIT 工具介绍 |

## 6.2 配置方法

本节对 DMDPC 进行配置的多种过程进行详细介绍。

### 6.2.1 SP\_CREATE\_DPC\_BP\_GROUP

**定义：**

```
SP_CREATE_DPC_BP_GROUP(
    GROUP_NAME         VARCHAR(128),
    DESC                VARCHAR(256)
)
```

**功能说明：**

向 MP 注册一个新的 BP 组。

**参数说明：**

GROUP\_NAME：待注册 BP 组名称；

DESC：描述信息。

**举例说明：**

注册名字为 BG\_1 的 BP 组，描述信息为“bp group1”。

```
SP_CREATE_DPC_BP_GROUP('BG_1', 'bp group1');
```

### 6.2.2 SP\_DROP\_DPC\_BP\_GROUP

**定义：**

```
SP_DROP_DPC_BP_GROUP(
    NAME VARCHAR(128)
)
```

**功能说明：**

删除一个 BP 组。

**参数说明：**

NAME：待移除 BP 组名称，必须是已经注册过的 BP 组。

**举例说明：**

删除名字为 BG\_1 的 BP 组。

```
SP_DROP_DPC_BP_GROUP('BG_1');
```

### 6.2.3 SP\_CREATE\_DPC\_SP\_GROUP

**定义：**

```
SP_CREATE_DPC_SP_GROUP(
    GROUP_NAME         VARCHAR(128),
    DESC                VARCHAR(256)
)
```

**功能说明：**

向 MP 注册一个新的 SP 组。

**参数说明：**

GROUP\_NAME：待注册 SP 组名称；

DESC：描述信息。

**举例说明：**

注册名字为 SPG\_1 的 SP 组，描述信息为“sp group1”。

```
SP_CREATE_DPC_SP_GROUP('SPG_1', 'sp group1');
```

### 6.2.4 SP\_DROP\_DPC\_SP\_GROUP

**定义：**

```
SP_DROP_DPC_SP_GROUP(
    NAME varchar(128)
)
```

**功能说明：**

删除一个 SP 组。

**参数说明：**

NAME：待移除 SP 组名称，必须是已经注册过的 SP 组。

**举例说明：**

删除名字为 SPG\_1 的 SP 组。

```
SP_DROP_DPC_SP_GROUP('SPG_1');
```

### 6.2.5 SP\_CREATE\_DPC\_RAFT

**定义：**

```
SP_CREATE_DPC_RAFT（
    DPC_MODE         VARCHAR(8),
    RAFT_NAME         VARCHAR(128)
）
```

**功能说明：**

向 MP 注册一个新的 RAFT 组。

**参数说明：**

DPC\_MODE：待注册 RAFT 组类型，取值只能为 BP 或者 SP。一个 SP 类型的 RAFT 组中最多只能加入一个 SP 节点；

RAFT\_NAME：待注册 RAFT 组名称。

**举例说明：**

注册名字为 RAFT\_1 的 BP RAFT 组，隶属于 BG\_1。

```
SP_CREATE_DPC_RAFT('BP', 'RAFT_1');
```

### 6.2.6 SP\_DROP\_DPC\_BP\_RAFT/SP\_DROP\_DPC\_RAFT

**定义：**

```
SP_DROP_DPC_BP_RAFT(
    NAME    VARCHAR(128)
)
```

或

```
SP_DROP_DPC_RAFT(
    NAME    VARCHAR(128)
)
```

**功能说明：**

删除一个 RAFT 组。

**参数说明：**

NAME：待删除 RAFT 组名称。

**举例说明：**

删除名字为 RAFT\_1 的 RAFT 组。

```
SP_DROP_DPC_BP_RAFT('RAFT_1');
或
SP_DROP_DPC_RAFT('RAFT_1');
```

### 6.2.7 SP\_CREATE\_DPC\_INSTANCE

SP\_CREATE\_DPC\_INSTANCE 过程有两个。

**1.内外网地址相同情景**

**定义：**

```
SP_CREATE_DPC_INSTANCE (
    RAFT_NAME         VARCHAR(128),
    NAME           VARCHAR(128),
    DPC_MODE     VARCHAR(8),
    AP_PORT       INT,
    INST_PORT     INT,
    IP_ADDR        VARCHAR(256),
    SYS MODE       VARCHAR(32),
    STATUS         INT,
    DESC            VARCHAR(256) 
）
```

**功能说明：**

注册一个 BP/SP/MP 实例。

**参数说明：**

RAFT\_NAME：RAFT 名称，和 SP\_CREATE\_DPC\_RAFT 中保持一致。如果是 MP，该值可写成'MP\_RAFT'，也可缺省为空串''或 NULL，因为 MP 多副本系统只有一个 RAFT 组，所以 RAFT 组名固定为 MP\_RAFT，缺省值也为 MP\_RAFT。如果 BP 或 SP，则该值不能缺省；

NAME：待注册的实例名称，和 DM.INI 中 INSTANCE\_NAME 保持一致；

DPC\_MODE：注册的实例类型，取值：BP、SP 或 MP。需要和 RAFT\_NAME 所属类型一致；

AP\_PORT： AP\_PORT 端口号，和 DM.INI 中 AP\_PORT\_NUM 保持对应。和 DPC\_INSTANCE 表中 XMAL\_PORT 值对应。SP/BP 本地设置的 AP\_PORT\_NUM 如果和自身在 MP 上注册的 AP\_PORT\_NUM 不一致，按照在 MP 上实际注册的为准，启动时会自动覆盖；

INST\_PORT： 实例端口号，和 DM.INI 中 PORT\_NUM 保持对应。和 DPC\_INSTANCE 表中 INST\_PORT 值对应。SP/BP 本地设置的 PORT\_NUM 如果和自身在 MP 上注册的 PORT\_NUM 不一致，按照在 MP 上实际注册的为准，启动时会自动覆盖；

IP\_ADDR： IP 地址；

SYS\_MODE： 主备模式，取值有 NORMAL，PRIMARY，STANDBY；

STATUS： 实例状态，1：有效；0：无效；2：表示 SP 为正常退出状态，可动态删除此 SP 实例；

DESC： 描述信息。

**举例说明：**

在 RAFT\_1 组注册一个新的 BP 节点 BP\_1。

```
SP_CREATE_DPC_INSTANCE('RAFT_1', 'BP_1', 'BP', 1822, 5238, '192.168.1.76',
'NORMAL', 1, 'BP instance');
```

**2.内外网地址不同或相同的情景**

**定义：**

```
SP_CREATE_DPC_INSTANCE (
    RAFT_NAME         VARCHAR(128),
    NAME           VARCHAR(128),
    DPC_MODE     VARCHAR(8),
    AP_PORT       INT,
    INST_PORT     INT,
    IP_INTER      VARCHAR(256),
    IP_EXTER      VARCHAR(256),
    SYS MODE       VARCHAR(32),
    STATUS         INT,
    DESC            VARCHAR(256) 
）
```

**功能说明：**

注册一个 BP/SP/MP 实例。

**参数说明：**

RAFT\_NAME：RAFT 名称，和 SP\_CREATE\_DPC\_RAFT 中保持一致。如果是 MP，该值可写成'MP\_RAFT'，也可缺省为空串''或 NULL，因为 MP 多副本系统只有一个 RAFT 组，所以 RAFT 组名固定为 MP\_RAFT，缺省值也为 MP\_RAFT。如果 BP 或 SP，则该值不能缺省。

NAME： 待注册的实例名称，和 DM.INI 中 INSTANCE\_NAME 保持一致；

DPC\_MODE： 注册的实例类型，取值：BP、SP 或 MP。需要和 RAFT\_NAME 所属类型一致；

AP\_PORT：AP\_PORT 端口号，和 DM.INI 中 AP\_PORT\_NUM 保持对应。和 DPC\_INSTANCE 表中 XMAL\_PORT 值对应。SP/BP 本地设置的 AP\_PORT\_NUM 如果和自身在 MP 上注册的 AP\_PORT\_NUM 不一致，按照在 MP 上实际注册的为准，启动时会自动覆盖；

INST\_PORT： 实例端口号，和 DM.INI 中 PORT\_NUM 保持对应。和 DPC\_INSTANCE 表中 INST\_PORT 值对应。SP/BP 本地设置的 PORT\_NUM 如果和自身在 MP 上注册的 PORT\_NUM 不一致，按照在 MP 上实际注册的为准，启动时会自动覆盖；

IP\_INTER： 实例的内网 IP 地址；

IP\_EXTER： 实例的外网 IP 地址；可传空串，表示内外网地址相同；

SYS\_MODE： 主备模式，取值有 NORMAL，PRIMARY，STANDBY；

STATUS： 实例状态，1：有效；0：无效；2：表示 SP 为正常退出状态，可动态删除此 SP 实例；

DESC： 描述信息。

**举例说明：**

在 RAFT\_1 组注册一个新的 BP 节点 BP\_1。

```
SP_CREATE_DPC_INSTANCE('RAFT_1', 'BP_1', 'BP', 1822, 5238, '192.168.1.76',
'192.168.1.77', 'NORMAL', 1, 'BP instance');
```

### 6.2.8 SP\_DROP\_DPC\_INSTANCE

**定义：**

```
SP_DROP_DPC_INSTANCE (
    NAME VARCHAR(128)
)
```

**功能说明：**

移除多副本中的一个 BP/SP/MP 实例。只剩最后一个实例则不能删除。

**参数说明：**

NAME：待移除实例名称，必须是已经注册过的实例名。

**举例说明：**

移除名字为 BP\_1 的 BP 服务器。

```
SP_DROP_DPC_INSTANCE('BP_1');
```

### 6.2.9 SP\_MODIFY\_DPC\_INSTANCE

**定义：**

```
SP_MODIFY_DPC_INSTANCE (
    NAME           VARCHAR(128),
    IP_INTER      VARCHAR(256),
    IP_EXTER      VARCHAR(256),
    AP_PORT       INT,
    INST_PORT     INT
)
```

或

```
SP_MODIFY_DPC_INSTANCE (
    NAME           VARCHAR(128),
    ATTR            VARCHAR(128),
    VALUE            VARCHAR(512)
)
```

**功能说明：**

修改注册在 MP 上的实例信息。修改成功后需要重启全部环境来应用新参数。

SP/BP 本地设置的 AP\_PORT\_NUM/PORT\_NUM 如果和自身在 MP 上注册的 AP\_PORT\_NUM/PORT\_NUM 不一致，按照在 MP 上实际注册的为准，启动时会自动覆盖。

**参数说明：**

NAME： 待修改的实例名称，非空；

IP\_INTER： 修改为新的内网 IP 地址，可为空串，表示不修改；

IP\_EXTER： 修改为新的外网 IP 地址，可为空串，表示不修改；

AP\_PORT： AP\_PORT 端口号，和 DM.INI 中 AP\_PORT\_NUM 保持对应。和 DPC\_INSTANCE 表中 XMAL\_PORT 值对应。可为空串，表示不修改。SP/BP 本地设置的 AP\_PORT\_NUM 如果和自身在 MP 上注册的 AP\_PORT\_NUM 不一致，按照在 MP 上实际注册的为准，启动时会自动覆盖；

INST\_PORT： 实例端口号，和 DM.INI 中 PORT\_NUM 保持对应。和 DPC\_INSTANCE 表中 INST\_PORT 值对应。可为空串，表示不修改。SP/BP 本地设置的 PORT\_NUM 如果和自身在 MP 上注册的 PORT\_NUM 不一致，按照在 MP 上实际注册的为准，启动时会自动覆盖；

ATTR： 属性，不可为空串，目前 ATTR 参数仅支持使用'CFG\_PORT'，用于设置 MP 的 CFG\_PORT 参数；

VALUE： 属性值，不可为空串。

**举例说明：**

修改 BP\_1 实例的 IP 地址、ap 端口号和实例端口号。可同时修改多个字段，也可以只修改部分字段值，不需要修改的字段传入空串''值即可，要求必须修改至少一个字段。

```
SP_MODIFY_DPC_INSTANCE('BP_1', '192.168.1.76', '192.168.100.77', 2822, 5338);
```

### 6.2.10 SP\_BP\_GROUP\_ADD\_RAFT

**定义：**

```
SP_BP_GROUP_ADD_RAFT（
    BP_GROUP_NAME    VARCHAR(128),
    RAFT_NAME         VARCHAR(128)
）
```

**功能说明：**

向 BP 组中添加一个 RAFT 组。

**参数说明：**

BP\_GROUP\_NAME：指定添加 RAFT 组的 BP 组名；

RAFT\_NAME：待添加的 RAFT 组名。

**举例说明：**

向 BP 组 BG\_1 中添加一个名为 RAFT\_1 的 RAFT 组。

```
SP_BP_GROUP_ADD_RAFT('BG_1', 'RAFT_1');
```

### 6.2.11 SP\_BP\_GROUP\_DEL\_RAFT

**定义：**

```
SP_BP_GROUP_DEL_RAFT（
    BP_GROUP_NAME    VARCHAR(128),
    RAFT_NAME         VARCHAR(128)
）
```

**功能说明：**

从 BP 组中删除一个 RAFT 组。

**参数说明：**

BP\_GROUP\_NAME：指定删除的 BP 组名；

RAFT\_NAME：待删除的 RAFT 组名。

**举例说明：**

从 BP 组 BG\_1 中删除名为 RAFT\_1 的 RAFT 组。

```
SP_BP_GROUP_DEL_RAFT('BG_1', 'RAFT_1');
```

### 6.2.12 SP\_SP\_GROUP\_ADD\_RAFT

**定义：**

```
SP_SP_GROUP_ADD_RAFT（
    SP_GROUP_NAME    VARCHAR(128),
    RAFT_NAME         VARCHAR(128)
）
```

**功能说明：**

向 SP 组中添加一个 RAFT 组。

**参数说明：**

SP\_GROUP\_NAME：指定添加 RAFT 组的 SP 组名；

RAFT\_NAME\*\*：\*\*待添加的 RAFT 组名。

**举例说明：**

向 SP 组 SPG\_1 中添加一个名为 SP\_RAFT\_1 的 RAFT 组。

```
SP_SP_GROUP_ADD_RAFT('SPG_1', 'SP_RAFT_1');
```

如果传入的参数 sp\_group\_name 并不是 SP 组或者 raft\_name 不是 SP RAFT 对象，系统会因指定的对象不存在而报错。

### 6.2.13 SP\_SP\_GROUP\_DEL\_RAFT

**定义：**

```
SP_SP_GROUP_DEL_RAFT（
    SP_GROUP_NAME    VARCHAR(128),
    RAFT_NAME         VARCHAR(128)
）
```

**功能说明：**

从 SP 组中删除一个 SP RAFT。

**参数说明：**

SP\_GROUP\_NAME：指定删除的 SP 组名；

RAFT\_NAME：待删除的 RAFT 组名。

**举例说明：**

从 SP 组 SPG\_1 中删除名为 SP\_RAFT\_1 的 RAFT 组。

```
SP_SP_GROUP_DEL_RAFT('SPG_1', 'SP_RAFT_1');
```

### 6.2.14 SP\_SET\_DPC\_NET\_CONF

**定义：**

```
SP_SET_DPC_NET_CONF(
    PARA_NAME         varchar(128),
    PARA_VALUE    varchar(128)
);
```

**功能说明：**

修改注册在 MP 上的通信参数。

**参数说明：**

PARA\_NAME: 待修改的参数名称，非空；

PARA\_VALUE: 修改为新的参数值，非空。

**举例说明：**

修改 MP 与 BP，MP 与 SP 通信时使用的参数信息，调用时同步修改系统表 SYS.DPC\_NET\_CONF，除了 CENTER\_COMPRESS\_LEVEL 修改后立即生效外，其他参数修改成功后需要重启全部环境来应用新参数。目前支持修改的参数为 TIMEOUT（通信超时，单位为秒）、XLNK\_NUM（链路数）、MONITOR\_XLNK\_TIME（监控链路消息收发用时，单位为微秒）、CRC\_CHECK（消息的 CRC 检验）、COMPRESS\_LEVEL（消息压缩级别）、CENTER\_COMPRESS\_LEVEL（数据中心间通信的压缩等级描述串）。

```
SP_SET_DPC_NET_CONF('TIMEOUT', '1000');
```

为了增加网络传输效率和减少带宽利用，对 XLNK 消息统一增加 COMPRESS\_LEVEL 参数，配置在 DPC\_NET\_CONF 系统表中。修改成功后需要重启全部节点才能生效。登录 SP 或者 MP 执行系统过程设置 XLNK 消息压缩等级。

```
SP_SET_DPC_NET_CONF('COMPRESS_LEVEL',10);
```

为了支持各数据中心间通信使用不同压缩等级，增加 CENTER\_COMPRESS\_LEVEL 参数，配置在 DPC\_NET\_CONF 系统表中。修改成功后自动广播到其他 dpc 节点，保证各节点保存的配置串一致，可通过在 SP 执行 GV$DPC\_CENTER\_COMPRESS\_LEVEL 查询各节点的配置串。

```
SP_SET_DPC_NET_CONF('CENTER_COMPRESS_LEVEL','(1,5,3):10/(1,2):10/(2,5):10');
```

### 6.2.15 SP\_TS\_GROUP\_CREATE

**定义：**

```
SP_TS_GROUP_CREATE(
    NAME        VARCHAR(128),
    DESC        VARCHAR(256)
)
```

**功能说明：**

创建表空间组。

**参数说明：**

NAME：表空间组名称。

DESC：表空间描述。

**举例说明：**

```
SP_TS_GROUP_CREATE('TSG_1', 'tablespace group1');
```

### 6.2.16 SP\_TS\_GROUP\_DROP

**定义：**

```
SP_TS_GROUP_DROP(
    GROUP_NAME VARCHAR(128)
)
```

**功能说明：**

删除表空间组。

**参数说明：**

NAME：表空间组名称。

**举例说明：**

```
SP_TS_GROUP_DROP('TSG_1');
```

### 6.2.17 SP\_TS\_GROUP\_ADD\_TS

**定义：**

```
SP_TS_GROUP_ADD_TS(
    GROUP_NAME    VARCHAR(128),
    TS_NAME        VARCHAR(128)
)
```

**功能说明：**

表空间组添加表空间。

**参数说明：**

GROUP\_NAME：表空间组名称；

TS\_NAME：表空间名称。

**举例说明：**

```
SP_TS_GROUP_ADD_TS('TSG_1', 'TS1');
```

### 6.2.18 SP\_TS\_GROUP\_REMOVE\_TS

**定义：**

```
SP_TS_GROUP_REMOVE_TS(
    GROUP_NAME    VARCHAR(128),
    TS_NAME        VARCHAR(128)
)
```

**功能说明：**

表空间组移除表空间。

**参数说明：**

GROUP\_NAME：表空间组名称；

TS\_NAME：表空间名称。

**举例说明：**

```
SP_TS_GROUP_REMOVE_TS('TSG_1', 'TS1');
```

### 6.2.19 SP\_RENAME\_DPC\_INSTANCE

**定义：**

```
SP_RENAME_DPC_INSTANCE(
    OLD_NAME       VARCHAR(128),
    NEW_NAME       VARCHAR(128)
)
```

**功能说明：**

重命名实例。

**参数说明：**

OLD\_NAME：旧实例名；

NEW\_NAME：新实例名。

**举例说明：**

```
SP_RENAME_DPC_INSTANCE('BP1_A', 'BP_INSTANCE_A');
```

### 6.2.20 SP\_ALTER\_DPC\_INSTANCE

**定义：**

```
SP_ALTER_DPC_INSTANCE(
    NAME            VARCHAR(128),
    SYS_MODE        VARCHAR(32),
    SYS_STATUS    INT,
    STATUS         INT   
)
```

**功能说明：**

修改实例的系统模式、系统状态、实例状态信息。

**参数说明：**

NAME：实例名；

SYS\_MODE：系统模式；

SYS\_STATUS：系统状态；

STATUS：实例状态。

**举例说明：**

```
SP_ALTER_DPC_INSTANCE('BP1','STANDBY',4,1);
```

### 6.2.21 SP\_DPC\_MOVE\_TS\_OFFLINE

**定义：**

```
SP_DPC_MOVE_TS_OFFLINE(
    TS_NAME        VARCHAR(128),
    RAFT_NAME        VARCHAR(128)
);
```

**功能说明：**

脱机方式表空间迁移时，MP 上手动修改系统表信息。只在脱机表空间迁移过程中使用。

**参数说明：**

TS\_NAME：迁移的表空间名称；

RAFT\_NAME：目标 RAFT 名。

**举例说明：**

将表空间 TS\_1 迁移到 RAFT\_1 上。

```
SP_DPC_MOVE_TS_OFFLINE('TS_1', 'RAFT_1');
```

### 6.2.22 SP\_SET\_DPC\_INST\_AUX

**定义：**

```
SP_SET_DPC_INST_AUX(
     INST_NAME   VARCHAR(128),
      AUX_FLAG        INT
);
```

**功能说明：**

设置 SP 实例是否作为辅助计算节点。缺省为是。

**参数说明：**

INST\_NAME：SP 节点的实例名；

AUX\_FLAG：是否作为辅助计算节点。1 是；0 否。

**举例说明：**

取消 SP\_1 实例作为辅助计算节点。

```
SP_SET_DPC_INST_AUX('SP_1', 0);
```

### 6.2.23 SP\_ADD\_RAFT\_LEARNER

**定义：**

```
SP_ADD_RAFT_LEARNER(
    DEST VARCHAR,
    DEST_IP VARCHAR,
    DEST_PORT INT,
    DEST_ID INT
);
```

**功能说明：**

增加 LEARNER 节点。需在当前多副本集群的主节点上执行。

**参数说明：**

DEST：LEARNER 节点实例名；

DEST\_IP：LEARNER 节点 IP 地址；

DEST\_PORT：LEARNER 节点通信 PORT；

DEST\_ID：LEARNER 节点编号。

**返回值：**

无

**举例说明：**

增加多副本集群的 LEARNER 节点 BP\_04。

```
SP_ADD_RAFT_LEARNER('BP_04', '192.168.1.68', 10010 , 3);
```

### 6.2.24 SP\_DELETE\_RAFT\_LEARNER

**定义：**

```
SP_DELETE_RAFT_LEARNER(
    DEST VARCHAR
)
```

**功能说明：**

删除 LEARNER 节点。需在当前多副本集群的主节点上执行。

使用细则如下：

1. 每次执行只允许删除 1 个节点；
2. 只允许在 LEARNER 主节点上执行，其他节点不允许执行；
3. 仅多数 RAFT 节点正常的情况下，才允许执行；
4. DMDPC 下的删除 LEARNER 的顺序为，先执行 SP\_DELETE\_RAFT\_LEARNER 从 RAFT 组中删除，再使用 SP\_DROP\_DPC\_INSTANCE 从系统表中删除节点；
5. 和 SP\_ADD\_RAFT\_LEARNER 策略一样，此函数仅会删除 RAFT 节点上的 LEARNER 归档配置，对于 LEARNER 节点上的配置则仍然是以手工方式进行修改。

**参数说明：**

DEST：LEARNER 节点实例名，对应 ARCH\_DEST 字段。

**返回值：**

无

**举例说明：**

删除多副本集群的 LEARNER 节点 BP\_04。

```
SP_DELETE_RAFT_LEARNER('BP_04');
```

### 6.2.25 SP\_ALTER\_RAFT\_NODE

**定义：**

```
SP_ALTER_RAFT_NODE(
    NEW_NODE VARCHAR
)
```

**功能说明：**

执行多副本集群成员变更。将当前多副本集群变更为仅含有 NEW\_NODE 节点的集群。不管是增加、删除还是替换，都可以使用这个系统函数来完成。

需在当前多副本集群的主节点上执行。

**参数说明：**

NEW\_NODE：指定新配置的所有节点实例名字符串。可以是一个或多个实例名，多个实例名之间用“/”符号分隔，目前最多支持 9 个节点。

**返回值：**

无

**举例说明：**

将当前多副本集群变更为仅含有 BP\_01、BP\_02、BP\_03、BP\_04、BP\_05 节点的集群。

```
SP_ALTER_RAFT_NODE('BP_01/BP_02/BP_03/BP_04/BP_05');
```

### 6.2.26 SP\_ADD\_RAFT\_NODE

```
SP_ADD_RAFT_NODE(
    NEW_NODE VARCHAR
)
```

**功能说明：**

增加多副本集群节点。如果集群变更还包含删除或替换节点，则不建议使用这个系统函数。

需在当前多副本集群的主节点上执行。

**参数说明：**

NEW\_NODE：指定新增的所有节点实例名。实例名之间用“/”符号分隔。加入新增节点后，新集群的节点总数最多支持 9 个节点。

**返回值：**

无

**举例说明：**

增加多副本集群的节点 BP\_04、BP\_05。

```
SP_ADD_RAFT_NODE('BP_04/BP_05');
```

### 6.2.27 SP\_DELETE\_RAFT\_NODE

```
SP_DELETE_RAFT_NODE(
    DELETE_NODE VARCHAR
)
```

**功能说明：**

删除多副本集群节点。如果集群变更还包含增加或替换节点，则不建议使用这个系统函数。

需在当前多副本集群的主节点上执行。

**参数说明：**

DELETE\_NODE：指定要删除的所有节点实例名。各实例名以“/”符号分隔。

**返回值：**

无

**举例说明：**

删除多副本集群的节点 BP\_04、BP\_05。

```
SP_DELETE_RAFT_NODE('BP_04/BP_05');
```

### 6.2.28 SP\_REPLACE\_RAFT\_NODE

**定义：**

```
SP_REPLACE_RAFT_NODE(
    OLD_NODE VARCHAR,
    NEW_NODE VARCHAR
)
```

**功能说明：**

替换多副本集群的节点。即同时包含新增和删除节点的情况下，使用该系统函数来完成。

需在当前多副本集群的主节点上执行。

**参数说明：**

OLD\_NODE：指定要删除的所有节点实例名。各实例名先“/”符号分隔，OLD\_NODE 必须是旧配置下的多副本节点；

NEW\_NODE：指定要增加的所有节点实例名。各实例名以“/”符号分隔，NEW\_NODE 必须是 learner 节点。

**返回值：**

无

**举例说明：**

例 1 将 BP\_02/BP\_03 替换为 BP\_04/BP\_05。

```
SP_REPLACE_RAFT_NODE('BP_02/BP_03', 'BP_04/BP_05');
```

例 2 将 BP\_02/BP\_03 替换为 BP\_04/BP\_05，再新增 BP\_06/BP\_07。

```
SP_REPLACE_RAFT_NODE('BP_02/BP_03', 'BP_04/BP_05/BP_06/BP_07');
```

### 6.2.29 SP\_DPC\_DUMP\_INST

**定义：**

```
SP_DPC_DUMP_INST (
    FILE_PATH            VARCHAR(256)
)
```

**功能说明：**

将 dpc\_instance 的配置以追加的形式，转储到文本文件，以便于在 MP 故障时查看。文件路径不存在时报错。在 MP/BP/BS/SP 均能执行。

**参数说明：**

FILE\_PATH：导出的文本文件路径。

**举例说明：**

```
SP_DPC_DUMP_INST('S:\DPC\C\dpc_instance.md');
```

### 6.2.30 SP\_SET\_SP\_UPGRADE

**定义：**

```
SP_SET_SP_UPGRADE(
    INST_NAME         VARCHAR(128)
)
```

**功能说明：**

将一个正常状态的 SP 标记为升级状态。非正常状态的 SP 无效。

只能在 SP 上运行；BP 和 MP 上无法运行。只能升级 SP。

**参数说明：**

INST\_NAME：待升级的 SP 的实例名称。

**返回值：**

无

**举例说明：**

```
SP_SET_SP_UPGRADE('SP2');
```

### 6.2.31 SP\_RESET\_SP\_UPGRADE

**定义：**

```
SP_RESET_SP_UPGRADE(
    INST_NAME         VARCHAR(128)
)
```

**功能说明：**

将一个升级状态的 SP 恢复正常；非升级状态的 SP 无效。

只能在 SP 或 MP 上运行；BP 上无法运行。只能恢复 SP。

**参数说明：**

INST\_NAME：待恢复的 SP 的实例名称。

**返回值：**

无

**举例说明：**

```
SP_RESET_SP_UPGRADE('SP2');
```

### 6.2.32 SP\_DPC\_REBALANCE\_SESSION

**定义：**

```
SP_DPC_REBALANCE_SESSION(
    BALANCE_FLAG     INT
)
```

**功能说明：**

收集当前 SP 可见的所有 SP 的会话数，并产生或清空所有节点各自的平衡方案。

**参数说明：**

BALANCE\_FLAG：取 1 表示产生节点各自的平衡方案；取 0 表示清空各个节点的方案；不论取 0 还是取 1，都会收集可见的所有 SP 的会话数。

**返回值：**

无

**举例说明：**

```
SP_DPC_REBALANCE_SESSION(1);
```

### 6.2.33 SP\_RAFT\_SUSPEND\_THREAD

**定义：**

```
SP_RAFT_SUSPEND_THREAD()
```

**功能说明：**

多副本环境中，主库挂起除当前会话外的所有工作线程。直连主库执行。

此过程执行成功之后会强制将当前会话设置为只读属性，后续不允许再通过当前会话来执行非只读操作。

**举例说明：**

主库挂起自己的工作线程。

```
SP_RAFT_SUSPEND_THREAD();
```

### 6.2.34 SP\_RAFT\_SWITCHOVER

**定义：**

```
SP_RAFT_SWITCHOVER()
```

**功能说明：**

多副本环境中，将备库手动切换为主库。直连备库执行。raft 影子节点不支持通过 SP\_RAFT\_SWITCHOVER()过程切换为主节点。

**举例说明：**

备库手动切换为主库流程：

1.连接主库执行挂起

```
SP_RAFT_SUSPEND_THREAD();
```

2.连接备库执行手动切换

```
SP_RAFT_SWITCHOVER();
```

### 6.2.35 SP\_RAFT\_RESUME\_THREAD

**定义：**

```
SP_RAFT_RESUME_THREAD(
    INST_NAME   VARCHAR(128)
)
```

**功能说明：**

多副本环境中，唤醒指定多副本组内的节点的工作线程，直连任意一个备库执行。

**参数说明：**

INST\_NAME：待唤醒的实例名称。

**举例说明：**

唤醒 BP01 的工作线程。

```
SP_RAFT_RESUME_THREAD('BP01');
```

### 6.2.36 SP\_TS\_DROP\_INVALID

**定义：**

```
SP_TS_DROP_INVALID()
```

**功能说明：**

删除本地节点有，但是 MP 中没有注册的表空间。

只能在 BP 或 BS 节点执行该系统函数。

**参数说明：**

无。

**举例说明：**

```
SP_TS_DROP_INVALID;
```

### 6.2.37 SP\_CLEAR\_TAB\_ROWCNT\_CACHE

**定义：**

```
SP_CLEAR_TAB_ROWCNT_CACHE (
RAFT_ID INT,
TAB_ID INT
)
```

**功能说明：**

清除所有或指定 SP/BS 节点上的全部或部分表行数缓存。

虽站点号指定为其他类型的节点也能成功执行，并不报错，但因其他类型节点不存在表行数缓存，执行该过程没有实际意义。

**参数说明：**

RAFT\_ID：SP/BS 站点号。

TAB\_ID：表 ID。

如果表 ID 和 SP/BS 站点号都为 NULL，就清除所有 SP/BS 站点上的全部表行数缓存；提供表 ID，但是 SP/BS 站点号为 NULL，就清除所有 SP/BS 站点上的指定表 ID 的缓存；如果表 ID 为 NULL，提供 SP/BS 站点号，就清除指定 SP/BS 站点上的所有表行数缓存。

**举例说明：**

清理所有 SP/BS 站点上的全部表行数缓存：

```
SP_CLEAR_TAB_ROWCNT_CACHE(NULL,NULL);
```

### 6.2.38 SP\_GET\_ALL\_TS\_BY\_TSGROUP

**定义：**

```
SP_GET_ALL_TS_BY_TSGROUP (
TGNAME VARCHAR(128)
)
```

**功能说明：**

显示表空间组内的所有表空间信息。显示的列信息和系统表 DPC\_INSTANCE 相同。该存储过程在单机环境下无效。

**参数说明：**

TGNAME：表空间组名。

**举例说明：**

显示表空间组 TSG\_1 内的所有表空间信息：

```
SP_GET_ALL_TS_BY_TSGROUP('TSG_1');
```

### 6.2.39 SP\_SET\_RAFT\_ASYNC\_INTERVAL

**定义：**

```
SP_SET_RAFT_ASYNC_INTERVAL(
ARCH_DEST VARCHAR,
ASYNC_INTERVAL INT
)
```

**功能说明：**

重置一个 RAFT 备库或 LEARNER 备库的异步恢复时间间隔。

仅在多副本环境主库上执行有效。

对于 BS 主库，需要以 LOCAL 方式登录执行。

**参数说明：**

ARCH\_DEST：待重置异步恢复时间间隔的节点实例名。

ASYNC\_INTERVAL： 异步恢复时间间隔，单位：S(秒)，取值范围 3~86400。

**返回值：**

无

**举例说明：**

在主库上执行，设置 RAFT 备库 BP\_2 的异步恢复时间间隔为 30s。

```
SP_SET_RAFT_ASYNC_INTERVAL('BP_2', 30);
```

### 6.2.40 SP\_GET\_RAFT\_ASYNC\_INTERVAL

**定义：**

```
SP_GET_RAFT_ASYNC_INTERVAL(

ARCH_DEST    VARCHAR

)
```

**功能说明：**

获取一个 RAFT 备库或 LEARNER 备库的异步恢复时间间隔。

仅在多副本环境主库上执行有效。

对于 BS 主库，需要以 LOCAL 方式登录执行。

**参数说明：**

ARCH\_DEST：待重置异步恢复时间间隔的节点实例名。

**返回值：**

异步恢复时间间隔。

**举例说明：**

在主库上执行，获取 RAFT 备库 BP\_2 的异步恢复时间间隔。

```
SP_GET_RAFT_ASYNC_INTERVAL('BP_2');
```

### 6.2.41 SP\_SET\_RAFT\_ELECT

**定义：**

```
SP_SET_RAFT_ELECT(

ELECT_FLAG       dmbool

)
```

**功能说明：**

设置当前 RAFT 库节点的选举开关。关闭选举开关的节点不会进行超时检测，不会主动发起选举，但收到其他节点的投票请求后，如果对方符合条件，可以正常投出选票。打开选举开关的节点检测超时后可以正常发起选举和投出选票。

选举开关默认情况下均为打开状态。SP\_SET\_RAFT\_ELECT 仅修改内存值，节点重启后失效。对于 BS 主库节点需要 LOCAL 方式登录执行。

**参数说明：**

ELECT\_FLAG：设置选举开关，0：关闭选举开关；1：打开选举开关。

**返回值：**

无

**举例说明：**

关闭当前 RAFT 库节点的选举开关。

```
SP_SET_RAFT_ELECT(0);
```

### 6.2.42 SF\_GET\_RAFT\_ELECT

**定义：**

```
SF_GET_RAFT_ELECT()
```

**功能说明：**

获取当前 RAFT 库节点的选举开关。对于 BS 主库节点需要 LOCAL 方式登录执行。

**参数说明：**

无

**返回值：**

0：选举开关为关闭状态；1：选举开关为打开状态。

**举例说明：**

获取当前 RAFT 库节点的选举开关。

```
SELECT SF_GET_RAFT_ELECT();
```

### 6.2.43 SF\_CLEAR\_DICT\_CACHE

**定义：**

INT

SF\_CLEAR\_DICT\_CACHE(

RAFT\_ID INT

)

或

INT

SF\_CLEAR\_DICT\_CACHE(

RAFT\_ID INT,

OBJID INT,

CASCADE INT,

TYPE VARCHAR(128),

SUBTYPE VARCHAR(128)

)

**功能说明：**

广播到指定节点，如果不指定对象 ID，清理该节点的所有字典缓存，否则清理指定 ID 的字典缓存。

**参数说明：**

RAFT\_ID：广播的目标节点号。

OBJID：对象 ID。

CASCADE：是否级联删除。

TYPE：类型，对应 SYSOBJECTS 的 TYPE$。

SUBTYPE：子类型，对应 SYSOBJECTS 的 SUBTYPE$。

**返回值：**

清理的字典个数。

**举例说明：**

例 1 清理目标节点号为 1 的所有字典信息。

```
SELECT SF_CLEAR_DICT_CACHE(1);
```

例 2 清理目标节点号为 1，对象 ID 为 1024 的字典缓存。

```
SELECT SF_CLEAR_DICT_CACHE(1,1024,1,'SCHOBJ','UTAB');
```

### 6.2.44 SP\_DELETE\_RAFT\_NODE\_FOR\_SINGLE

**定义：**

SP\_DELETE\_RAFT\_NODE\_FOR\_SINGLE(

DEST VARCHAR

);

**功能说明**

删除 RAFT 节点。需在单副本节点上执行,仅会修改内存值。

注意:本函数仅用于对单副本集群升级成多副本时，用户执行 SP\_ADD\_RAFT\_NODE\_FOR\_SINGLE 后，发现加错节点需要删除时使用,若要在多副本集群增加节点需要使用正常的节点变更步骤,具体可见 5.10 动态增删节点。

**参数说明**

DEST：RAFT 节点实例名，对应 ARCH\_DEST 字段。

**返回值**

无。

**举例说明**

例 1 向单副本集群删除一个 RAFT 节点 BP\_04。

```
SP_DELETE_RAFT_NODE_FOR_SINGLE('BP_04');
```