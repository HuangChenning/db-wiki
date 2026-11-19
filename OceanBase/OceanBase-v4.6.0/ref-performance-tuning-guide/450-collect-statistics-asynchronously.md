---
title: "异步统计信息收集"
book: "性能调优"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000007059165.html"
tags:
  - oceanbase
  - distributed
  - ref-performance-tuning-guide
---

# 异步统计信息收集

#### 说明

满足上述条件表示表或分区进入异步收集候选范围，不代表统计信息会立即完成收集。异步统计信息收集的默认判断阈值为 2；自动统计信息收集通过 `STALE_PERCENT` 控制统计信息过期阈值，其默认值为 10（即 10%）。
