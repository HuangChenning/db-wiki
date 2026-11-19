---
title: "通过 OBClient 连接 OceanBase 租户"
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077435.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 通过 OBClient 连接 OceanBase 租户

#### 注意

普通租户通过直连方式连接时，需要确保该租户的资源分布在该 OBServer 节点上，如果该租户的资源未分布在该 OBServer 节点上，则无法通过直连该 OBServer 节点连接到该租户。

#### 注意

在使用直连方式连接 OceanBase 数据库时，连接参数 `-u` 后应填写正确的 `用户名@租户名`，不要指定集群名。如果在 `-u` 中包含了集群名，会导致连接报错。

#### 说明

出于安全考虑，建议不在命令行直接输入密码，尤其是在脚本或历史记录可见的环境下，可以省略此选项并在提示时输入密码。

#### 说明

Hint 是特殊的注释，不受 `-c` 影响。
