---
title: "设置强同步的下游"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077523.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 设置强同步的下游

#### 说明

MySQL 模式的管理员用户为 `root` 用户，Oracle 模式的管理员用户为 `SYS` 用户。

#### 说明

设置后，如果备租户因负载均衡或容灾场景，导致设置的 `ip_list` 信息发生了变化，主租户会秒级探测备租户上系统日志流的位置变化并自动更新，不需要用户再手动修改 `ip_list` 信息。
