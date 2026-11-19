---
title: "备份到指定目录"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000007124952.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 备份到指定目录

#### 说明

对于 V4.4.2 版本，从 V4.4.2 BP3 版本开始支持该功能。

#### 说明

OceanBase 数据库从 V4.2.1 版本开始，`TENANT = all_user` 与 `TENANT = all`语义相同，在需要生效范围为所有用户租户时，推荐使用 `TENANT = all_user`，后续 `TENANT = all` 将废弃不再使用。

#### 说明

系统租户通过 \`TO\` 语法仅支持指定 1 个租户，不支持同时对多个租户发起备份，也不支持省略 \`TENANT\` 子句。
