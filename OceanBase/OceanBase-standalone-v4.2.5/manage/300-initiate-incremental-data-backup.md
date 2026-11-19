---
title: "发起增量数据备份"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701943.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 发起增量数据备份

#### 说明

OceanBase 数据库从 V4.2.1 版本开始，`TENANT = all_user` 与 `TENANT = all`语义相同，在需要生效范围为所有用户租户时，推荐使用 `TENANT = all_user`，后续 `TENANT = all` 将废弃不再使用。

#### 说明

同时指定多个租户时，租户名之间使用英文逗号 (\`,\`) 分隔。
