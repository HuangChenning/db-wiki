---
title: "为新创建的表设置透明加密"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702008.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 为新创建的表设置透明加密

#### 注意

- 如果主租户有对应的备租户，建议您先设置备租户的 `tde_method`，再设置主租户的 `tde_method`。
- 配置项 `tde_method` 一旦设置就不能再修改，并且在存在备租户的场景下，需要在备租户中也设置相同的值。

#### 说明

仅当租户上所有 OBServer 节点上的配置项 `tde_method` 的值均为 `internal`，该语句才能执行成功。
