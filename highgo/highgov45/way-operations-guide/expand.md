---
title: "10、如何处理表或索引的膨胀"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/expand.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 如何处理表或索引的膨胀

首先说明：

vacuum命令一般不会减小table的大小，vacuum的作用是释放dead tuple占用的空间，释放出来的空间可以被本表上的其他事务重用。

## 1、缓解膨胀：

可以从数据库参数层面进行优化：

配置较为积极的数据库参数，目的是让autovacuum操作尽快尽早进行，以便dead tuple占用的空间被尽早释放，进而可被本表上的其他事物重用。

```
autovacuum_naptime=15ms
autovacuum_vacuum_threshold=25
autovacuum_analyze_threshold=10
autovacuum_vacuum_scale_factor=0.01
autovacuum_analyze_scale_factor=0.05
```

## 2、解决膨胀的方法之一：vacuum full

postgresql 的 vacuum full 需要 access exclusive lock，获得这个锁后，针对该表的所有操作均无法执行，包括 select。因此，本方法的适用场景是业务停机状态下。

vacuum full需要额外的磁盘空间，因为vacuum full的过程是建立新表的过程。

vacuum full的过程，会改变table的pg\_relation\_filepath，会改变index的pg\_relation\_filepath

vacuum full的过程，不会改变table的oid,不会改变index的oid

**注意：使用vacuum full会造成锁表，禁止在业务运行高峰期时使用**

## 3、解决膨胀的方法之二：使用pg\_repack extension。

截止目前，pg\_repack的最新版本是1.4.5，支持的PostgreSQL版本是9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 10, 11, 12

pg\_repack可以单独编译安装，编译安装的前提:

要求服务器操作系统上有gcc、zlib、zlib-devel、readline-devel 操作系统包

pg\_repack安装之后，在bin目录下形成pg\_repack命令。

pg\_repack的运行不会使用独占锁，pg\_repack运行时对target table持有ACCESS SHARE LOCK

pg\_repack的使用前提：

1.超级用户运行

2.表必须有primary key，或者至少一个unique key,且组成unique key的列是非空列。

3.需要足够的空余磁盘空间，假设表和索引是1GB，那么至少需要2GB的空余磁盘空间。

警告：不带任何参数的pg\_repack会直接repack，不要pg-repack不带参数直接敲回车！！！

pg\_repack的使用限制：

1.不能对temp table使用

2.不能对GiST index使用

3.在pg\_repack运行过程中，不能执行DDL语句（除了vacuum、analyze）

4.pg\_repack是服务器端的程序，因此必须在服务器端安装pg\_repack

pg\_repack的过程，会改变table的pg\_relation\_filepath，会改变index的pg\_relation\_filepath

pg\_repack的过程，不会改变table的oid,不会改变index的oid

pg\_repack执行的细粒度

1.针对某个schema

2.针对某个table及其索引

3.针对某个index

4.针对某个表上的所有索引