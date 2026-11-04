---
title: "2、HGDB如何提升批量导入数据的速度"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HGDB_speed.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## HGDB如何提升批量导入数据的速度

## 1、文档用途

本文档用于提供几个提升瀚高数据库批量导入数据速度的方向，需要根据实际情况具体分析及选择。

## 2、详细信息

### （1）关闭自动提交

在批量插入数据时，如果每条数据都被自动提交，当中途出现系统故障时，不仅不能保障本次批量插入的数据一致性，而且由于有多次提交操作的发生，整个插入效率也会受到很大的打击。解决方法是，关闭系统的自动提交(SET AUTOCOMMIT = OFF)，并且在插入开始之前，显式的执行 BEGIN TRANSACTION 命令，在全部插入操作完成之后再执行 COMMIT 命令提交所有的插入操作。

### （2）使用 COPY 命令

使用 COPY 在一条命令里装载所有记录，而不是一系列的 INSERT 命令。COPY 命令是为装载数量巨大的数据行优化过的，它不像 INSERT 命令那样灵活，但是在装载大量数据时，系统开销也要少很多。

注：因为 COPY 是单条命令，因此在填充表的时候就没有必要关闭自动提交了。

### （2）删除索引

如果你正在装载一个新创建的表，最快的方法是创建表，用 COPY 批量装载，然后创建表需要的任何索引。因为在已存在数据的表上创建索引比维护逐行增加要快。当然在缺少索引期间，其它有关该表的查询操作的性能将会受到一定的影响，唯一性约束也有可能遭到破坏。

### （4）删除外键约束

和索引一样，”批量地”检查外键约束比一行行检查更加高效。因此，我们可以先删除外键约束，装载数据，然后再重建约束。

### （5）临时增大 MAINTENANCE\_WORK\_MEM

在装载大量数据时，临时增大 maintenance\_work\_mem 系统变量的值可以改进性能。这个系统参数可以提高CREATE INDEX 命令和 ALTER TABLE ADD FOREIGN KEY 命令的执行效率，但是它不会对 COPY 操作本身产生多大的影响。

### （6）临时增大 CHECKPOINT\_SEGMENTS

临时增大 checkpoint\_segments 系统变量的值也可以提高大量数据装载的效率。这是因为在向 PostgreSQL 装载大量数据时，将会导致检查点操作(由系统变量 checkpoint\_timeout 声明)比平时更加频繁的发生。在每次检查点发生时，所有的脏数据都必须 flush 到磁盘上。通过提高 checkpoint\_segments 变量的值，可以有效的减少检查点的数目。

### （7）设置为 UNLOGGED 表

PostgreSQL 的 unlogged table 是不记录 xlog 的，因此批量导入的时候 unlogged 表速度比 logged 表性能要快上一倍。但是， unlogged 表不是异常安全的：数据库崩溃或者异常关闭后， unlogged 表中的数据会被自动删减；另外， unlogged 表中的数据也不会备份到从服务器。任何 unlogged 表上创建的索引也是 unlogged 的。对于批量数据导入，我们可以临时设置表为 unlogged(ALTER TABLE tb SET UNLOGGED)，之后再将表重新设置为 logged(ALTER TABLE tb SET LOGGED)。

### （8）事后运行 VACUUM ANALYZE

在增加或者更新了大量数据之后，应该立即运行 VACUUM ANALYZE 命令，这样可以保证规划器得到基于该表的最新数据统计。换句话说，如果没有统计数据或者统计数据太过陈旧，那么规划器很可能会选择一个较差的查询规划，从而导致查询效率过于低下。