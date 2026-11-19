---
title: "删除数据"
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077460.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 删除数据

#### 说明

当前登录租户所属的租户模式可以由 `sys` 租户通过查询 `oceanbase.DBA_OB_TENANTS` 视图进行确认。

#### 说明

除了 `DELETE` 语句外，`REPLACE INTO` 语句也可能会删除数据，`REPLACE INTO` 语句相关的操作及示例请参见 [替换数据](400-replace-data-of-mysql-mode-in-develop.md)。
