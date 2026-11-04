---
title: "23、再谈mvcc与vacuum"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/again_mvcc.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 再谈mvcc与vacuum

## 1 、简介

在pg的各种技术讨论和日常运维中，vacuum永远是主要的话题之一。 pg数据库管理运维过程中，经常会调整以下的vacuum参数，以优化数据库的性能

```
alter system set autovacuum = on;
alter system set log_autovacuum_min_duration = -1;
alter system set autovacuum_max_workers = 6;
alter system set autovacuum_naptime=60;
alter system set autovacuum_vacuum_scale_factor=0.2;
```

并发操作。即数据库中可以同时运行多个事务。这也是数据库区别于一般存储软件（Excel）的功能特点。并发控制是在并发运行中维护事务一致性和隔离性的一种机制。

注：事务的ACID特性不在本文讨论

有三种主要的并发控制技术，即 Multi-version Concurrency Control (MVCC), Strict Two-Phase Locking (S2PL) 和 Optimistic Concurrency Control (OCC)，每种技术都有很多变体。 PostgreSQL使用称为 快照隔离 Snapshot Isolation (SI) 的MVCC变体。

在MVCC中，每个写操作都会创建新版本的数据项，同时保留旧版本。当事务读取数据项时，系统会选择其中一个版本来确保单个事务的隔离。MVCC的主要优势在于”读不会阻塞写，而写也从不阻塞读“，相反，例如，基于S2PL的系统当有写操作时必须阻塞读，因为写操作获得了独占锁。

为了实现SI，一些RDBMS(例如Oracle)使用回滚段(rollback segments)。当写入新的数据项时，旧的数据项被写入回滚段，随后新项被覆盖到数据区域。PostgreSQL使用更简单的方法。一个新的数据项被直接插入相关表页。读取数据时，PostgreSQL通过\*\*可见性检查规则(visibility check rules)\*\*来选择适当版本的数据项以响应单个事务。

以上介绍了mvcc的概念，要了解vacuum，还需要进一步了解mvcc机制及其产生的影响。

## 2、事务ID（txid）

每当事务开始时，由事务管理器分配一个唯一标识符 事务id(txid)。PostgreSQL的txid是一个32位无符号整数，约为42亿。如果在事务开始后调用内部函数 txid\_current()，则返回当前的txid，如下所示。

```
testdb=# BEGIN;
BEGIN
test=> SELECT txid_current();
 txid_current
      592
(1 row)
```

PostgreSQL保留以下三个特殊的 txid：

· 0 表示 Invalid txid，无效txid。

· 1 表示 Bootstrap txid, 它仅用于数据库集群的初始化。

· 2 表示 Frozen txid, 用来描述冻结状态。

所以数据库系统的第一个正常的事务ID是从3开始的，然后不停递增，达到4字节整数的最大值后，再从3开始。事务ID为0、1、2的始终保留。

txid可以相互比较。例如，从txid 100的角度看，大于100的txid表示“将来的”，并且它们在txid 100中不可见; 小于100的txid表示”过去的”并且可见

事例

| … | 97 | 98 | 99 | **100** | 101 | 102 | … |
| --- | --- | --- | --- | --- | --- | --- | --- |

可以将txid看作一个时间轴、事务99小于100，是“过去的”，其操作对100可见；事务101大于100，是“将来的”，其操作对100不可见

由于txid空间在实际系统中是不够的，PostgreSQL将txid空间视为一个圆。之前的21亿txid是“过去的”，之后的21亿txid是“将来的”

tps是1000，21亿可以使用多长时间

2100000000 ÷ ( 24 × 3600 × 1000 ) = ？

## 3、tuple结构

HeapTupleHeaderData

HeapTupleHeaderData

| **t\_xmin** | **t\_xmax** | **t\_cid** | **t\_ctid** | t\_infomask2 | t\_infomask | t\_hoff | null\_bitmap | **user\_data** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

虽然 \[HeapTupleHeaderData\]结构包含7个元素，但本文中只涉及其中4个元素。

· t\_xmin 记录插入此元组的事务ID txid。

· t\_xmax 记录删除或更新此元组的事务ID txid。如果这个元组没有被删除或更新，t\_xmax被设置为0，这意味着INVALID。

· t\_cid 记录命令ID(command id，cid)，从0开始递增，表示当前事务中执行此命令之前执行了多少个SQL命令。例如，假定我们在单个事务中执行三个INSERT命令：BEGIN; INSERT; INSERT; INSERT; COMMIT;。如果第一个命令插入这个元组，则t\_cid被设置为0，如果第二个命令插入该元组，则t\_cid被设置为1，依此类推。

· t\_ctid 记录指向自身或新元组的元组标识符(tuple identifier，tid)。当这个元组更新时，这个元组的t\_ctid指向新的元组; 否则，t\_ctid指向自己。

## 4、dead tuple

```
Inserting, Deleting and Updating tuple与dead tuple
```

### 1.Insert事例

begin;  
insert into test\_con values (1,’A’);  
commit;

page结构：

block 0

| Header\_data | — | — | — |
| --- | --- | --- | --- |
| — | — | — | line\_pointer |
|  | freespace |  |  |
|  |  | freespace |  |
|  |  |  | heap\_tuple\_1 |

|  | t\_xmin | t\_xmax | t\_cid | t\_ctid | user\_data |
| --- | --- | --- | --- | --- | --- |
| tuple\_1 | 594 | 0 | 0 | (0,1) | ‘A’ |

t\_xmin设置为594，表示这条数据是由事务594插入的 t\_xmax设置为0，保留事务id，无效的。表示这行数据没有被update或delete t\_cid设置为0，表示这行数据是事务594插入的第一行数据 t\_ctid设置为（0，1），指向自己，没有新版本产生

注：page结构不在本文讨论，参考体系结构-物理结构

PostgreSQL提供了一个扩展pageinspect，用于显示page页的内容。

```
CREATE EXTENSION pageinspect;
create table test_con(id int,name text);
insert into test_con values (1,'A');

test=# SELECT lp as tuple, t_xmin, t_xmax, t_field3 as t_cid, t_ctid  FROM heap_page_items(get_raw_page('test.test_con', 0));
 tuple | t_xmin | t_xmax | t_cid | t_ctid
-------+--------+--------+-------+--------
     1 |    594 |      0 |     0 | (0,1)
(1 row)
```

### 2.delete事例

block 0

| Header\_data | — | — | — |
| --- | --- | --- | --- |
| — | — | line\_pointer |  |
|  | freespace |  |  |
|  |  | freespace |  |
|  |  |  | heap\_tuple\_1 |

|  | t\_xmin | t\_xmax | t\_cid | t\_ctid | user\_data |
| --- | --- | --- | --- | --- | --- |
| tuple\_1 | 594 | 595 | 0 | (0,1) |  |

t\_xmax设置为595，表示这行数据被事务595update或delete 如果事务操作commited，那么这行数据tuple\_1就不再需要了，会被标记为dead tuple。

可以通过扩展 pageinspect ，查看page的内容

```
test=# SELECT lp as tuple, t_xmin, t_xmax, t_field3 as t_cid, t_ctid  FROM heap_page_items(get_raw_page('test.test_con', 0));
 tuple | t_xmin | t_xmax | t_cid | t_ctid
-------+--------+--------+-------+--------
     1 |    594 |    595 |     0 | (0,1)
(1 row)
```

### 3.update事例

```
test=> insert into test_con values (1,'A');
INSERT 0 1
test=> update test_con set name='B' where id=1;                                                              UPDATE 1
test=> update test_con set name='C' where id=1;                                                             UPDATE 1
test=>
```

block 0

| Header\_data | — | — | — |
| --- | --- | --- | --- |
| — | — | line\_pointer | — |
|  | freespace |  |  |
|  |  | freespace |  |
|  | tuple\_3 | tuple\_2 | heap\_tuple\_1 |

|  | t\_xin | t\_xmax | t\_cid | t\_ctid | user\_data |
| --- | --- | --- | --- | --- | --- |
| tuple\_1 | 599 | 600 | 0 | (0,2) | ‘A’ |
| tuple\_2 | 600 | 601 | 0 | (0,3) | ‘B’ |
| tuple\_3 | 601 | 0 | 0 | (0,3) | ‘C’ |

tuple\_1 t\_xmax设置为600，被事务600修改 t\_ctid设置为（0，2），不再指向自己，指向第二个版本tuple\_2 tuple\_2 t\_xmax设置为601，被事务601修改 t\_ctid设置为（0，3），不再指向自己，指向第三个版本tuple\_3 tuple\_3 t\_xmax设置为0，没有被修改过 t\_ctid设置为（0，3），指向自己

如果事务操作committed，那么数据tuple\_1和tuple\_2就不再需要了，会被标记为dead tuple。

可以通过扩展 pageinspect ，查看page的内容

```
test=# SELECT lp as tuple, t_xmin, t_xmax, t_field3 as t_cid, t_ctid  FROM heap_page_items(get_raw_page('test.test_con', 0));
 tuple | t_xmin | t_xmax | t_cid | t_ctid
-------+--------+--------+-------+--------
     1 |    599 |    600 |     0 | (0,2)
     2 |    600 |    601 |     0 | (0,3)
     3 |    601 |      0 |     0 | (0,3)
(3 rows)
test=#
```

产生这么多的dead tuple怎么办？死数据导致数据膨胀问题

## 5 、事务回卷问题

在这里，我们描述事务ID回卷问题。

假定 txid 100 插入元组 Tuple\_1，即 Tuple\_1 的 t\_xmin 为 100。服务器运行了很长时间，Tuple\_1 没有被修改。当前 txid 为21亿+100，并执行 SELECT 命令。此时，Tuple\_1 可见，因为 txid 100 是过去。然后，执行相同的SELECT 命令; 此时，目前的 txid 为21亿+101。然而，Tuple\_1 不再可见，因为 txid 100 在未来(如下图)。这是PostgreSQL中所谓的 事务回卷问题 transaction wraparound problem。

事务id回卷问题，非常严重，如果没有处理措施，等于数据丢失。

也就是说，在事务时间轴上，相差21亿就会出现事务回卷问题。

为了解决这个问题，PostgreSQL引入了一个名为 frozen txid 的概念，并实现了 冻结 FREEZE 的过程。

在PostgreSQL中，定义了一个 frozen txid，它是一个特殊的保留 txid 2，它总是比所有其他 txid 更早。换句话说，frozen txid 总是不活动和可见的。

冻结处理由 vacuum 调用。将Tuple\_1和Tuple\_2的t\_xmin都被重写为2。

清理的速度要比使用的速度开！

## 6 、mvcc维护

通过以上的mvcc机制，可知，其一方面提高了并发，另一方面也会造成各种影响。所以需要通过引入vacuum机制解决此问题

PostgreSQL的并发控制机制需要以下过程维护。

1. ```
	删除dead tuple和指向对应的dead tuple的索引元组。
	```
2. ```
	删除clog不必要的部分。
	```
3. ```
	冻结旧txid。
	```
4. ```
	更新FSM、VM和统计信息。
	```

## 7、 vacuum概述

vacuum处理是一个维护过程，有助于PostgreSQL的持续运行。它的两个主要任务是 清理 dead tuples 和 冻结事务ID

为了清理 dead tuple，vacuum提供了两种模式，即 Concurrent VACUUM 和 Full VACUUM。Concurrent VACUUM(通常简称为VACUUM)为表文件的每个页清理 dead tuple，其他事务可以在此过程运行时读取表。相比之下，Full VACUUM 清理 dead tuple 并且整理文件的 live tuple 碎片，而其他事务无法在 Full VACUUM 运行时访问表。

vacuum处理有如下内容：

· Visibility Map

· Freeze processing

· Removing unnecessary clog files

· Autovacuum daemon

· Full VACUUM

## 8、 Concurrent VACUUM

vacuum处理对指定的表或数据库中的所有表执行以下操作

· (1) 从指定的表中获取每个表。

· (2) 获取表的ShareUpdateExclusiveLock锁。该锁允许从其他事务中读取。

· (3) 扫描所有页以获取所有dead tuple，并在必要时冻结dead tuple。

·

· (4) 删除指向相应dead tuple的索引元组(如果存在的话)。

· (5) 为表的每个页执行以下处理，步骤(6)和(7)。

· (6) 删除dead tuple并重新分配页中的live tuple。

· (7) 更新目标表的相应FSM和VM。

·

· (8) 如果最后一页没有任何元组，则截断最后一页。

· (9) 更新与vacuum处理的表相关的统计数据和系统目录。

· (10) 更新与vacuum处理相关的统计数据和系统目录。

· (11) 如果可能，删除不必要的文件和clog。

1.该块执行冻结处理并删除指向dead tuple的索引元组。 首先，PostgreSQL扫描一个目标表来建立一个dead tuple列表，并尽可能冻结旧的元组。该列表存储在本地缓存的 \[maintenance\_work\_mem\]中。

扫描后，PostgreSQL通过引用dead tuple列表来删除索引元组。

当maintenance\_work\_mem满了并且扫描不完整时，PostgreSQL进行下一个任务，即步骤(4)到(7); 然后返回步骤(3)并继续进行剩余扫描。

2.清理dead tuple，并逐页更新FSM和VM。

假设该表包含三个page页。我们专注于第0页(即第一页)。这个页有三个元组。Tuple\_2是一个dead tuple。在这种情况下，PostgreSQL清理Tuple\_2并重新排序剩余的元组以整理碎片，然后更新此页面的FSM和VM。PostgreSQL继续这个过程直到最后一页。

请注意，不必要的行指针不会被删除，它们将在未来重用。因为如果删除行指针，则必须更新关联索引的所有索引元组。

由于vacuum处理涉及扫描整个表，所以这是一个昂贵的过程。在8.4版本(2009)中，引入了\*\*可见性映射 Visibility Map (VM)\*\*以提高清理dead tuple的效率。

3.更新与vacuum处理的表相关的统计数据和系统目录。 而且，如果最后一页没有元组，它将从表文件中截断。

## 9、 vacuum冻结处理

冻结处理有两种模式，根据特定条件在任一模式下执行。为了方便，这些模式被称为 lazy 模式 和 eager 模式。

1.Lazy 模式 Concurrent VACUUM在内部通常被称为“lazy vacuum”。这里讨论的是冻结处理的lazy模式

启动冻结处理时，PostgreSQL计算FreezeLimittxid并冻结t\_xmin小于FreezeLimittxid的元组。

freezeLimit txid定义如下：

freezeLimit\_txid =(OldestXmin-vacuum\_freeze\_min\_age)

OldestXmin是当前正在运行的事务中最老的txid。例如，如果执行VACUUM命令时有三个事务(txids 100,101和102)正在运行，则OldestXmin为100.如果不存在其他事务，则OldestXmin是执行此VACUUM命令的txid。这里，\[vacuum\_freeze\_min\_age\] 是一个配置参数(默认50,000,000)。

在这里，Table\_1由三个页组成，每个页有三个元组。当执行VACUUM命令时，当前的txid是50,002,500，并且没有其他事务。在这种情况下，OldestXmin是5,002,500;因此，freezeLimit txid是2500.冻结处理执行如下。

图片略

· 0th page 由于所有t\_xmin值都小于freezeLimit txid，因此三个元组被冻结。另外，在这个vacuum过程中，由于Tuple\_1是dead tuple，所以被清理。

· 1st page: 通过引用VM来跳过此页。???

· 2nd page: Tuple\_7和Tuple\_8被冻结; Tuple\_7被清理。

但是看上面的参数，很明显不能绝对保证这个约束，为了解决这个问题，PostgreSQL 引入了autovacuum\_freeze\_max\_age 参数。 autovacuum\_freeze\_max\_age 表示如果当前最新的tXID 减去元组的t\_xmin 大于等于autovacuum\_freeze\_max\_age，则元组对应的表会强制进行autovacuum，即使PostgreSQL已经关闭了autovacuum。默认值为2亿 也就是说，在事务时间轴上，相差超过50,000,000就会被执行冻结，超过2亿，强制执行冻结这也就避免了事务回卷，同时也保证事务清理的速度快于事务使用速度。 1/10

2.Eager 模式 eager模式弥补了lazy模式的缺陷。它扫描所有页以检查表中的所有元组，更新相关的系统目录，并在可能的情况下删除不必要的文件和clog页。

当满足以下条件时执行eager模式。

pg\_database.datfrozenxid <(OldestXmin-vacuum\_freeze\_table\_age)

在上面的条件中，pg\_database.datfrozenxid表示\[pg\_database\]系统目录的列，并保存每个数据库的最早的冻结txid。\[Vacuum\_freeze\_table\_age\]是一个配置参数(默认值为150,000,000)。

在下面的事例中，Tuple\_1和Tuple\_7都已被清理。Tuple\_10和Tuple\_11已经被插入第二页。当执行VACUUM命令时，当前txid是150,002,000，并且没有其他事务。因此，OldestXmin是150,002,000，freezeLimit txid是100,002,000。在这种情况下，由于’1821（假设当前数据库的datfrozenxid都是1821） < (150002000 - 150000000)’，因此满足上述条件。因此，在eager模式中冻结处理如下执行。

图片略

· 0th page 即使所有元组都已被冻结，Tuple\_2和Tuple\_3也被检查。

· 1st page: 此页中的三个元组已冻结，也会被检查，因为所有t\_xmin值都小于freezeLimit txid。请注意，在lazy模式此页会跳过。

· 2nd page: Tuple\_10已被冻结。Tuple\_11没有。

冻结每个表后，目标表的pg\_class.relfrozenxid被更新。 在完成vacuum处理之前，必要时更新pg\_database.datfrozenxid。每个pg\_database.datfrozenxid列在相应的数据库中保存最小pg\_class.relfrozenxid。

查看每个表的pg\_class.relfrozenxid

```
SELECT n.nspname as "Schema", c.relname as "Name", c.relfrozenxid
            FROM pg_catalog.pg_class c
            LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
            WHERE c.relkind IN ('r','')
                  AND n.nspname <> 'information_schema' AND n.nspname !~ '^pg_toast'
                  AND pg_catalog.pg_table_is_visible(c.oid)
                  ORDER BY c.relfrozenxid::text::bigint DESC;
```

查看数据库的pg\_database.datfrozenxid

```
SELECT datname, datfrozenxid FROM pg_database;
```

freeze 操作会消耗大量的IO/cpu，对于不经常更新的表，可以合理地增大autovacuum\_freeze\_max\_age和vacuum\_freeze\_min\_age的差值。

## 10、 autovacuum

autovacuum守护进程已经使vacuum处理自动化; 因此，PostgreSQL的操作变得非常简单。 autovacuum守护进程定期调用几个autovacuum\_worker进程。默认情况下，它每1分钟唤醒一次(由\[autovacuum\_naptime\]定义，并调用三个worker由\[autovacuum\_max\_workers\]定义

触发条件

```
vacuum threshold = vacuum base threshold + vacuum scale factor * number of tuples
```

必要时调整以上参数

```
select   schemaname,   relname from pg_stat_all_tables where   n_live_tup>0   and n_dead_tup*1.0/n_live_tup>0.2   and schemaname not in ('pg_toast','pg_catalog')   and n_live_tup>100000;

vacuum(verbose,analyze) tf_f_announcement;
```

## 11、 Full VACUUM

虽然Concurrent VACUUM至关重要，但这还不够。例如，即使删除了许多dead tuple，它也不能减小表的大小。

vacuum会使dead tuple空间可重用，，而不是申请新的空间继续膨胀。（不会降低高水位线），dead tuple被清理; 但是，表大小并未减少。这既浪费磁盘空间，也会对数据库性能产生负面影响。 当对表执行VACUUM FULL命令时，

图片略

1. ```
	PostgreSQL首先获取表的AccessExclusiveLock锁并创建一个大小为8 KB的新表文件。AccessExclusiveLock锁不允许访问。
	```
2. ```
	将live tuple复制到新表中
	```
3. ```
	删除旧文件，重建索引，并更新统计信息，FSM和VM
	```

什么时候做VACUUM FULL？ 不幸的是，当执行’VACUUM FULL’时没有最佳时机。但是，扩展\[pg\_freespacemap\]可能会给你很好的建议。

```
testdb=# CREATE EXTENSION pg_freespacemap;
CREATE EXTENSION

testdb=# SELECT count(*) as "number of pages",
       pg_size_pretty(cast(avg(avail) as bigint)) as "Av. freespace size",
       round(100 * avg(avail)/8192 ,2) as "Av. freespace ratio"
       FROM pg_freespace('accounts');
 number of pages | Av. freespace size | Av. freespace ratio 
-----------------+--------------------+---------------------
            1640 | 99 bytes           |                1.21
(1 row)
```

在执行VACUUM FULL之后，会发现表文件已被压缩。