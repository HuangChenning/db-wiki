---
title: "创建空备租户"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702066.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 创建空备租户

#### 注意

OceanBase 数据库的用户名和权限信息是在主备租户之间进行同步，备租户自身不允许创建用户和授予权限。因此，如果当前备租户的源端是另外一个备租户，则需要在对应的主租户上创建访问视图专用用户并授予权限。
