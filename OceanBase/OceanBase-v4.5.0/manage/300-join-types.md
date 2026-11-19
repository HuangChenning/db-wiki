---
title: "联接类型"
book: "管理数据库"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479283.html"
tags:
  - oceanbase
  - distributed
  - manage
---

# 联接类型

每种联接类型支持的联接算法如下表所示。

|联接类型	|支持的联接算法|
|---|---|
|INNER JOIN	|Nested Loops Join、Hash Join、Merge Join|
|LEFT JOIN|	Nested Loops Join、Hash Join、Merge Join|
|RIGHT JOIN	|Hash Join、Merge Join|
|FULL JOIN	|Hash Join、Merge Join|
|LEFT SEMI JOIN	|Nested Loops Join、Hash Join、Merge Join|
|RIGHT SEMI JOIN	|Hash Join、Merge Join|
|LEFT ANTI JOIN	|Nested Loops Join、Hash Join、Merge Join|
|RIGHT ANTI JOIN	|Hash Join、Merge Join|
