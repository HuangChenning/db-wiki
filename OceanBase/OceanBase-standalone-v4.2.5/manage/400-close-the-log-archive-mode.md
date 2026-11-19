---
title: "关闭归档模式"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701934.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 关闭归档模式

#### 注意

为防止归档任务状态卡在 STOPPING 状态无法关闭，当归档介质不可用时也能够正常关闭归档任务。相应地，日志消费模块也能够在强关归档的场景下正确消费日志。

#### 说明

同时指定多个租户时，租户名之间使用英文逗号 (\`,\`) 分隔。
