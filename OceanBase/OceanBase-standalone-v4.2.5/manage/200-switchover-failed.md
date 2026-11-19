---
title: "Switchover 或 Failover 相关问题"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701877.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# Switchover 或 Failover 相关问题

#### 说明

对于基于日志归档的物理备库场景，不会出现以上报错，需要您参考以下步骤自行检查归档源所在的租户是否已经切换为备租户，否则可能会出现双主租户或者本次 Switchover 操作一直无法完成日志同步的问题。

#### 注意

报错信息 `original error code: -4012` 中的 ` -4012`，仅代表其中一种可能出现的错误码，该报错还有可能显示为其它错误码。

#### 说明

执行 `SWITCHOVER TO STANDBY VERIFY` 命令时，系统仅检查备租户与恢复源的系统日志流是否同步；执行 `SWITCHOVER TO STANDBY`命令时，系统会检查备租户与恢复源的所有日志流是否同步。
