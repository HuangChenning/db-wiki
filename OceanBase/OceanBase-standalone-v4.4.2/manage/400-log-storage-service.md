---
title: "日志存储服务"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077172.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 日志存储服务

#### 注意

RAW_WRITE 是日志流工作模式的默认值，因此在主租户上，对于某些正在执行负载均衡任务的场景，其日志流副本的 `ACCESS_MODE` 也会是 `RAW_WRITE`。
