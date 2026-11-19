---
title: "大对象存储性能最佳实践"
book: "性能调优"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000002081521.html"
tags:
  - oceanbase
  - best-practices
  - performance-tuning
---

# 大对象存储性能最佳实践

#### 注意

处理 LOB 和 JSON 字段开销较大的问题已在 V4.2.x 的 V4.2.2、V4.3.x 的 V4.3.1 以及之后的版本进行了优化。详见下文“升级到合适的 OceanBase 版本”小节。

#### 注意

修改 `ob_default_lob_inrow_threshold` 变量的值，不会影响已经创建表的行内存储阈值，只会影响新创建且没有指定行内阈值的表。
