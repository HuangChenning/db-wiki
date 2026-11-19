---
title: "自动清理过期备份"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077573.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 自动清理过期备份

#### 注意

`enable_worm=true` 参数适用于开启了合规保留策略（WORM）的场景。

#### 注意

当前仅支持设置租户级清理策略，不支持设置集群级清理策略，每条命令只能为一个租户设置一个清理策略。

#### 说明

自动清理任务由后台系统每小时定时触发，因此清理策略设置完成后，可能需要等待一段时间（不超过一小时）才能查询到相对应的清理任务。

#### 说明

MySQL 租户的管理员用户为 `root` 用户，Oracle 租户的管理员用户为 `SYS` 用户。

#### 说明

自动清理任务由后台系统每小时定时触发，因此清理策略设置完成后，可能需要等待一段时间（不超过一小时）才能查询到相对应的清理任务。
