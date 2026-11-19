---
title: "MySQL 事务控制"
book: "系统原理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078407.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# MySQL 事务控制

#### 说明

- `ob_trx_timeout` 用于设置事务超时时间，单位为微秒。

- `ob_trx_idle_timeout` 用于设置事务空闲超时时间，即事务中两条语句之间的执行间隔超过该值时超时，单位为微秒。
