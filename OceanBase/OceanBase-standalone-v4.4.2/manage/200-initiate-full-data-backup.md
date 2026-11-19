---
title: "发起全量数据备份"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077228.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 发起全量数据备份

#### 说明

该密码为备份后的备份集的密码。如果设置了该选项，在使用该备份集进行恢复时，需要输入该密码，且该密码不能被删除。

#### 说明

设置备份密码后，在未发起数据备份前，您可以通过断开会话再重新连接数据库的方式取消本次设置。

#### 说明

OceanBase 数据库从 V4.2.1 版本开始，`TENANT = all_user` 与 `TENANT = all`语义相同，在需要生效范围为所有用户租户时，推荐使用 `TENANT = all_user`，后续 `TENANT = all` 将废弃不再使用。

#### 说明

同时指定多个租户时，租户名之间使用英文逗号 (\`,\`) 分隔。
