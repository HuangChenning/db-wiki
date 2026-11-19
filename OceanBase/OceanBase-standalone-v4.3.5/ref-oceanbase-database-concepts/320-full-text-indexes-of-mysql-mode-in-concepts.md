---
title: "全文索引"
book: "系统原理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578317.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 全文索引

#### 说明

用 ngram2 分词器时，需注意其内存占用较高，比如设置 `min_ngram_size` 和 `max_ngram_size` 参数范围较大时，会生成大量词元组合，可能导致资源消耗过大。
