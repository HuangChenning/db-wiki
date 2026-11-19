---
title: "连接类型"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702213.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 连接类型

每种连接类型支持的连接算法如下表所示。

| 连接类型        | 支持的连接算法                           |
|-----------------|------------------------------------------|
| INNER JOIN      | Nested Loops Join、Hash Join、Merge Join |
| LEFT JOIN       | Nested Loops Join、Hash Join、Merge Join |
| RIGHT JOIN      | Hash Join、Merge Join                    |
| FULL JOIN       | Hash Join、Merge Join                    |
| LEFT SEMI JOIN  | Nested Loops Join、Hash Join、Merge Join |
| RIGHT SEMI JOIN | Hash Join、Merge Join                    |
| LEFT ANTI JOIN  | Nested Loops Join、Hash Join、Merge Join |
| RIGHT ANTI JOIN | Hash Join、Merge Join                    |
