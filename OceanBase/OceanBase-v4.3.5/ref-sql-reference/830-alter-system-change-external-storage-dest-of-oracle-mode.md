---
title: ALTER/CHANGE/MODIFY EXTERNAL_STORAGE_DEST
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004971501.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# ALTER/CHANGE/MODIFY EXTERNAL_STORAGE_DEST

#### 说明

I/O 限流参数设置建议：

- 对于高并发、带宽敏感的多租户环境，可以为不同的备份路径设置不同的 `max_iops` 或 `max_bandwidth` 参数值，用于隔离备份对线上业务带宽和 IOPS 的影响。
- 建议结合实际网络带宽和对象存储的限速策略，先从较低值开始，逐步调整。例如，先从设置为 `max_iops=500&max_bandwidth=100mb` 开始观察，再根据备份耗时与业务峰值进行微调。
