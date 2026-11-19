---
title: "创建表"
book: "应用开发"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701951.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 创建表

#### 说明

当前登录租户所属的租户模式可以由 `sys` 租户通过查询 `oceanbase.DBA_OB_TENANTS` 视图进行确认。

#### 注意

对于 Hash 分区，如果是通过指定分区数的方式（例如，`SUBPARTITIONS 5`）进行二次分区，则在创建模板化二级分区表时，不需要指定 `SUBPARTITION TEMPLATE` 关键字。
