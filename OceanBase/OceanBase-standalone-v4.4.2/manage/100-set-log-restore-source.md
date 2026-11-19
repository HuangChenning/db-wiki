---
title: "设置日志恢复源"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078026.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 设置日志恢复源

#### 注意

当归档介质为对象存储（例如：阿里云 OSS、Azure Blob、AWS S3 以及兼容 S3 协议的对象存储）时，物理备库运行过程中，如果主租户或源端的备租户更改了备份介质的密钥信息，则需要参考以下操作重新设置日志恢复源。

#### 说明

对于 V4.4.2 版本，OceanBase 数据库从 V4.4.2 BP2 版本开始支持延迟备库功能。有关延迟备库的详细操作及注意事项，参见 [配置备库延迟](300-configure-a-delayed-standby-tenant.md)。

#### 注意

OceanBase 数据库的用户名和权限信息是在主备租户之间进行同步，备租户自身不允许创建用户和授予权限。因此，如果当前备租户的源端是另外一个备租户，则需要在对应的主租户上创建访问视图专用用户并授予权限。

#### 说明

如果您当前登录的是 `sys` 租户，需要通过查询 `CDB_OB_ACCESS_POINT` 视图来获取访问入口信息。

#### 说明

对于 V4.4.2 版本，OceanBase 数据库从 V4.4.2 BP2 版本开始支持延迟备库功能。有关延迟备库的详细操作及注意事项，参见 [配置备库延迟](300-configure-a-delayed-standby-tenant.md)。
