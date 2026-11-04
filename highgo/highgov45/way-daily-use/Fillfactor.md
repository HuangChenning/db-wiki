---
title: "25、如何查看并修改表或索引的Fillfactor值"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/Fillfactor.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## 如何查看并修改表或索引的Fillfactor值

## 1、什么是Fillfactor

FillFactor意为填充因子，用于设置数据要占用page空间的比例。一个表的填充因子(fillfactor)是一个介于 10 和 100 之间的百分数。100(完全填充)是默认值。。

## 2、Fillfactor参数的作用

设置填充因子的主要作用是为新数据预留一定的空间，当有新数据时，可以插入到预留的空间里，从而避免分页的发生。

## 3、设置Fillfactor参数的利弊

如果指定了较小的填充因子，INSERT 操作仅按照填充因子指定的百分率填充表页。每个页上的剩余空间将用于在该页上更新行，这就使得 UPDATE 有机会在同一页上放置同一条记录的新版本，这比把新版本放置在其它页上更有效。对于一个从不更新的表将填充因子设为 100 是最佳选择，但是对于频繁更新的表，较小的填充因子则更加有效。

总结为一句话：fillfactor会降低insert的性能,但是update和delete性能将有提升。

## 4、Fillfactor参数查询修改示例

```
highgo=# SELECT
pc.relname AS ObjectName,pc.reloptions AS ObjectOptions
FROM pg_class AS pc INNER JOIN pg_namespace AS pns
ON pns.oid = pc.relnamespace
WHERE pns.nspname = 'public'
AND pc.relname = 'test';                                   -----查询现在的填充因子

 objectname | objectoptions 
------------+---------------
 test       | 
(1 row)
highgo=#
highgo=# ALTER TABLE test set ( fillfactor = 50);          -----修改填充因子数值
ALTER TABLE
highgo=# SELECT
pc.relname AS ObjectName,pc.reloptions AS ObjectOptions
FROM pg_class AS pc INNER JOIN pg_namespace AS pns
ON pns.oid = pc.relnamespace
WHERE pns.nspname = 'public'
AND pc.relname = 'test';  -----查询修改后的填充因子数值

 objectname |  objectoptions  
------------+-----------------
 test       | {fillfactor=50}
(1 row)
highgo=#
```