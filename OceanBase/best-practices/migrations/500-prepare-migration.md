---
title: "OMS 海量数据迁移策略"
book: "数据迁移和导入"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000001489659.html"
tags:
  - oceanbase
  - best-practices
  - migrations
---

# OMS 海量数据迁移策略

#### 注意

旁路导入如果表中有数据，需要将数据清空之后再开始导入。即使旁路导入报错中断，如果要恢复迁移，还是需要重新清空表。
