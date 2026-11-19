---
title: "设置日志恢复源"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702226.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 设置日志恢复源

#### 注意

OceanBase 数据库的用户名和权限信息是在主备租户之间进行同步，备租户自身不允许创建用户和授予权限。因此，如果当前备租户的源端是另外一个备租户，则需要在对应的主租户上创建访问视图专用用户并授予权限。

#### 说明

如果您当前登录的是 `sys` 租户，需要通过查询 `CDB_OB_ACCESS_POINT` 视图来获取访问入口信息。
