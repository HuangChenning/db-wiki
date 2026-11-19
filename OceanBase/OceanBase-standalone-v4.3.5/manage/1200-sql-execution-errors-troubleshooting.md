---
title: "SQL 执行报错问题排查"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577375.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# SQL 执行报错问题排查

#### 注意

必须在执行完报错 SQL 后，第一时间执行以下语句；否则，查询出来的不是报错 SQL 的 `trace_id`。
