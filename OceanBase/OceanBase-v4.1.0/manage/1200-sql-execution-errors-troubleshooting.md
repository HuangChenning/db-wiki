---
title: "SQL 执行报错问题排查"
book: "管理数据库"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000003008252.html"
tags:
  - oceanbase
  - distributed
  - manage
---

# SQL 执行报错问题排查

#### 注意

必须在执行完报错 SQL 后，第一时间执行以下语句；否则，查询出来的不是报错 SQL 的 `trace_id`。
