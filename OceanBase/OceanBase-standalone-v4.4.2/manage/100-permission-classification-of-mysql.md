---
title: "MySQL 模式下的权限分类"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078044.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# MySQL 模式下的权限分类

#### 说明

支持通过 `GRANT`、`REVOKE` 语句为用户授予、撤销该权限，但授予权限后，该权限不会生效。

#### 说明

支持通过 `GRANT`、`REVOKE` 语句为用户授予、撤销该权限，但授予权限后，该权限不会生效。

#### 说明

对于 OceanBase 数据库 V4.4.x 版本，从 V4.4.1 版本开始引入 `CREATE LOCATION` 权限。

#### 注意

如果要查询 Catalog 数据，则需要单独授予 `SELECT ON CATALOG` 权限。
