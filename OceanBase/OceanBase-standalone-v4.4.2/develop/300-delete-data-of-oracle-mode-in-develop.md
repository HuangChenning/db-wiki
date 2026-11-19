---
title: "删除数据"
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077472.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 删除数据

#### 说明

当前登录租户所属的租户模式可以由 `sys` 租户通过查询 `oceanbase.DBA_OB_TENANTS` 视图进行确认。

#### 说明

如果表记录数多达几百万以上，会形成大事务，可能会有性能问题。建议带上 `WHERE` 条件分批删除，或者使用 `TRUNCATE TABLE` 语句。
