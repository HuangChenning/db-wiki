---
title: "SYSSTAT 监控项"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077614.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# SYSSTAT 监控项

#### 说明

MemTable 上校验成功依旧可能失败在 SSTable 上。

#### 说明

不包含 SSTable 上的校验。

#### 注意

监控项不带 `background` 的指标是不包括 background 的部分。例如，`idle wait time` 只记录前台 Session 相关的时间，不包含 `background database idle wait time` 相关内容，这两个监控项的统计值是互斥的。
