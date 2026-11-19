---
title: "日志解读"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077039.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 日志解读

#### 说明

每一台 OBServer 上允许的最大的 Scheduler CTX 数量为 10 万，Participant CTX 数量为 70 万。

#### 说明

RPC 传输慢很可能与网络延迟、时钟偏差以及系统负载和 RPC 线程的繁忙有关。
