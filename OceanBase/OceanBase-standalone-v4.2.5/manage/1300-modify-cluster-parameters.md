---
title: "修改集群配置项"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701880.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 修改集群配置项

#### 注意

系统租户（即 `sys` 租户），可以查看和设置集群级配置项，用户租户只能查看集群级配置项，无法设置集群级配置项。

#### 说明

OceanBase 数据库从 V4.2.1 版本开始，`TENANT = all_user` 与 `TENANT = all`语义相同，在需要生效范围为所有用户租户时，推荐使用 `TENANT = all_user`，后续 `TENANT = all` 将废弃不再使用。
