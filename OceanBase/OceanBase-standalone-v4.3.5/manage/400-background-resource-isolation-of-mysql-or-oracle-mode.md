---
title: "后台任务的资源隔离配置案例"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577840.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 后台任务的资源隔离配置案例

#### 说明

由于后台任务 `CLOG_HIGH` 会直接影响业务请求的延迟，对 I/O 请求的要求应尽量得到满足，因此将资源组 `CLOG_HIGH_GROUP` 中的 `MIN_IOPS` 配置为 40；同时该任务对 CPU 的要求不高，故将 `CPU_WEIGHT` 配置为 30。
