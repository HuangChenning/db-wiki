---
title: AWS DMS
book: "生态集成"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005724641.html"
tags:
  - oceanbase
  - distributed
  - ecological-integration
---

# AWS DMS

#### 注意

连接租户的用户需要拥有该数据库的 `CREATE`、`INSERT`、`DROP` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

#### 注意

OceanBase 到 MySQL 的增量迁移必须通过 ODP 连接，不能直接连接 OBServer。
