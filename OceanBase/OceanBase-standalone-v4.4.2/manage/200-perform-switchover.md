---
title: Switchover
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077524.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# Switchover

#### 注意

在进行 Switchover 操作时，要求必须先将主租户切换为备租户，再将备租户切换为主租户。如果先将备租户切换为主租户，可能会由于出现双主租户的问题，从而导致 `ALTER SYSTEM SWITCHOVER TO PRIMARY` 命令执行失败。

#### 注意

在进行 Switchover 时，要求必须首先将主租户切换为备租户，否则可能会出现双主租户或者备租户无法完成日志同步的问题。同时，由于在基于日志归档的物理备库场景中，备租户无法感知原主租户的状态，故如果先将备租户切换为主租户，在执行 `ALTER SYSTEM SWITCHOVER TO PRIMARY` 命令时，系统也不会报错。

#### 注意

在配置归档目的端时，不同租户需要使用的不同的归档路径。

#### 注意

在执行备切主前，需要确保 `SYNCHRONIZED` 字段显示为 `YES`，否则，执行备切主操作后，可能会导致 Switchover 后新主租户的数据不完整。

#### 注意

备切主命令开始执行前，系统会检查备租户是否已同步到恢复源端的所有日志，故备切主命令的执行时间取决于备租户与主租户的同步进度。
