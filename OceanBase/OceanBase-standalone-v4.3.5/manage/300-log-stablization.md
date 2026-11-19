---
title: "日志稳定性"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577420.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 日志稳定性

#### 注意

出于稳定性考虑建议开启异步日志。但是开启异步日志后，在 OBServer 异常退出的情况下，会有最后一小段日志没来得及刷盘而丢失，所以在测试环境中建议关闭异步日志。

#### 注意

虽然有异步日志打印方案，但依然会有 CPU 损耗。某些极致性能场景下（例如大促活动）可以将日志级别设置为 ERROR 以减少日志量。
