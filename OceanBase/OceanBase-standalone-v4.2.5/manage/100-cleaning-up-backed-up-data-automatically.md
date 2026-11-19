---
title: "自动清理过期备份"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701923.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 自动清理过期备份

#### 注意

`enable_worm=true` 参数适用于开启了合规保留策略（WORM）的场景。对于 V4.2.5 版本，OceanBase 数据库从 V4.2.5 BP7 版本开始支持将配置了 WORM 策略的阿里云 OSS Bucket 作为备份或归档路径。

#### 说明

自动清理任务由后台系统每小时定时触发，因此清理策略设置完成后，可能需要等待一段时间（不超过一小时）才能查询到相对应的清理任务。

#### 注意

当前仅支持设置租户级清理策略，不支持设置集群级清理策略，每条命令只能为一个租户设置一个清理策略。

#### 说明

自动清理任务由后台系统每小时定时触发，因此清理策略设置完成后，可能需要等待一段时间（不超过一小时）才能查询到相对应的清理任务。
