---
title: "管理序列"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150380.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 管理序列

#### 说明

在分布式系统中使用 Sequence 时，如果您使用了 `CACHE` + `NOORDER` 选项，那么连接到不同机器时获得的序列不是有序递增的，但是可以保证唯一。
