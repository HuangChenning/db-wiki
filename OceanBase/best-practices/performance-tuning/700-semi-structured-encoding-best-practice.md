---
title: "半结构化存储性能最佳实践"
book: "性能调优"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000003029301.html"
tags:
  - oceanbase
  - best-practices
  - performance-tuning
---

# 半结构化存储性能最佳实践

#### 注意

如果启用半结构化编码功能，请务必保证集群配置项 [micro_block_merge_verify_level](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000003381833) 为默认配置 `2` ，切勿关闭微块合并校验。

#### 注意

此功能从 V4.3.5 BP2 开始支持。
