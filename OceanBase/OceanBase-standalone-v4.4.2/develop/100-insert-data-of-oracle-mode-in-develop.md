---
title: "插入数据"
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077468.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 插入数据

#### 说明

当前登录租户所属的租户模式可以由 `sys` 租户通过查询 `oceanbase.DBA_OB_TENANTS` 视图进行确认。

#### 说明

在使用 `INSERT` 语句插入数据时，如果表上有唯一性约束，则在插入相同的记录时，系统会报错，您可以通过 `MERGE INTO` 语句来更新表记录，避免唯一性约束的冲突。
