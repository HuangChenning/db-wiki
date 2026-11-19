---
title: "监控项"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577867.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 监控项

#### 注意

监控项不带 `background` 的指标是不包括 background 的部分。例如，`idle wait time` 只记录前台 Session 相关的时间，不包含 `background database idle wait time` 相关内容，这两个监控项的统计值是互斥的。
