---
title: "28、如何查看SQL的执行计划"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/sql_plan.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## 如何查看SQL的执行计划

## 一、explain命令详解

### 1、语法

```
EXPLAIN [ ( option [, ...] ) ] statement
EXPLAIN [ ANALYZE ] [ VERBOSE ] statemen
```

### 2、选项说明

option可以有以下选项

analyze：执行语句并显示真正的运行时间和其它统计信息，会真正执行SQL语句；

verbose：显示额外的信息,尤其是计划树中每个节点的字段列表,schema识别表和函数名称。总是打印统计数据中显示的每个触发器的名字；

costs：包括每个计划节点的启动成本预估和总成本的消耗，也包括行数和行宽度的预估；

buffers：使用信息，特别包括共享块命中、读、脏和写的次数，本地块命中、读、脏和写，临时块读和写的次数；

timing：在输出中包含实际启动时间和每个节点花费的时间，重复读系统块在某些系统上会显著的减缓查询的速度，只在ANALYZE也启用的时候使用；

format：声明输出格式，可以为TEXT、XML、JSON 或 YAML，默认 text；

## 二、explain输出详解

### 1、计划解读

```
a=> explain analyze select * from pgbench_accounts ;
QUERY PLAN
Seq Scan on pgbench_accounts  (cost=0.00..2688.00 rows=100000 width=97) (actual time=0.267..34.302 rows=100000 loops=1)
Planning Time: 0.165 ms
Execution Time: 46.280 ms
cost=0.00..2688.00，0.00代表启动成本；2688.00代表返回所有数据的成本；rows=100000表示返回多少行；width=97，表示每行平均宽度(以字节计算)；actual time=0.267..34.302，实际花费的时间；loops=1，循环的次数；
Planning Time，生成执行计划的时间；
Execution Time，执行执行计划的时间。
```

### 2、输出参数详细说明

cost：第一个数字表示启动的成本，也就是返回第一行需要多少cost值；第二个数字表示返回所有的数据的成本。默认cost值如下

顺序扫描一个数据块，cost值定为1

随机扫描一个数据块，cost值定为4

处理一个数据行的 CPU，cost为0.01

处理一个索引行的 CPU，cost为0.005

每个操作符的CPU代价为0.0025

rows：表示会返回多少行

width：表示每行平均宽度为多少字节

buffers

shared hit：表示在共享内存中直接读到 多少个块，

read：表示从磁盘读了多少块

written：写磁盘多少块

执行计划含义  
Seq Scan：全表扫描

Index Scan：索引扫描

Bitmap Heap Scan：位图扫描

Filter：条件过滤

Nestloop Join：嵌套循环连接，是在两个表做连接时，内表被外表驱动，外表返回的每一行都要在内表中检索找到与它匹配的行，因此整个查询返回的结果集不能太大，要把返回子集较小的表作为外表，而且在内表的连接字段上要有索引，否则会很慢。执行过程：

确定一个驱动表（outer table），另一个表为inner table

驱动表中的每一行与inner 表中的相应记录 JOIN 类似一个嵌套的循环

Hash Join：使用两个表中较小的表，并利用连接键在内存中建立散列表，然后扫描较大的表并探测散列表，找出与散列表匹配的行。适用于较小的表可以完全放入内存中的情况。如果表很大，不能完全放入内存，优化器会将它分割成若干不同的分区，把不能放入内存的部分写入磁盘的临时段。

Merge Join：如果源数据上有索引，或者结果已经被排过序，在执行排序合并连接时就不需要排序了，Merge Join 的性能会优于散列连接。

### 3、解读原则

①从下往上读  
②从右至左读  
③开启时间消耗是输出开始前的时间例如排序的时间  
④消耗包括磁盘检索页，cpu时间  
⑤注意，每一步的cost包括上一步的

⑥重要的是，explain 不是真正的执行一次查询 只是得到查询执行的计划和估计的花费

### 4、其他举例说明

## 下面是一个hash，hash join例子：=# EXPLAIN SELECT relname, nspname FROM pg\_class JOIN pg\_namespace ON (pg\_class.relnamespace=pg\_namespace.oid);QUERY PLAN

```
Hash Join (cost=1.06..10.71 rows=186 width=128)
  Hash Cond: ("outer".relnamespace = "inner".oid)
     -> Seq Scan on pg_class (cost=0.00..6.86 rows=186 width=68)
     -> Hash (cost=1.05..1.05 rows=5 width=68)
        -> Seq Scan on pg_namespace (cost=0.00..1.05 rows=5 width=68)
两个表间INNER JOIN和LEFT OUTER JOIN 连接的时候，这个运算是很常用的。这个运算是先把外表中关联条件部分做一个哈希表，然后去和内部表关联。
首先在表pg_namespace上做了一次顺序扫描，之后进行hash运算形成一个hash表，之后再pg_class表上进行顺序扫描，再进行hash join操作，hash join操作的条件为"outer".relnamespace = "inner".oid。
```