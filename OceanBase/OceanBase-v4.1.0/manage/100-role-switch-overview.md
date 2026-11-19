---
title: "角色切换概述"
book: "管理数据库"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001698983.html"
tags:
  - oceanbase
  - distributed
  - manage
---

# 角色切换概述

OceanBase 集群的租户角色包括两种：主租户（PRIMARY）和备租户（STANDBY）。您可以通过 Switchover 和 Failover 操作动态改变租户角色。

* Switchover

  允许主租户与其中一个备租户交换角色，保证数据无损。

* Failover

  主租户不可用的情况下，可以将一个备租户切换为主租户。
