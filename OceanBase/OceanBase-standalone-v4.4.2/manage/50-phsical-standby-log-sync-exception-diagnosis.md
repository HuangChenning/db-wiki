---
title: "物理备库日志同步与回放异常诊断"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006547425.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 物理备库日志同步与回放异常诊断

#### 注意

由于日志传输服务仅在强同步模式下工作，仅当主租户为强同步模式时，才可以通过该方式查看主租户日志的传输状态。异步同步模式下，由备租户向主租户拉取日志。

#### 注意

由于日志传输服务仅在强同步模式下工作，仅当主租户为强同步模式时，才可以通过以下方式查看主租户日志的传输状态。异步同步模式下，由备租户向主租户拉取日志。
