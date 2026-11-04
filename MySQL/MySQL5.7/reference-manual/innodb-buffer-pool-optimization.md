---
title: "8.10.1 InnoDB Buffer Pool Optimization"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/innodb-buffer-pool-optimization.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 8.10.1 InnoDB Buffer Pool Optimization

[`InnoDB`](innodb-storage-engine.md) maintains a storage area called the [buffer pool](glossary.md) for caching data and indexes in memory. Knowing how the `InnoDB` buffer pool works, and taking advantage of it to keep frequently accessed data in memory, is an important aspect of MySQL tuning.

For an explanation of the inner workings of the `InnoDB` buffer pool, an overview of its LRU replacement algorithm, and general configuration information, see [Section 14.5.1, “Buffer Pool”](innodb-buffer-pool.md).

For additional `InnoDB` buffer pool configuration and tuning information, see these sections:

- [Section 14.8.3.4, “Configuring InnoDB Buffer Pool Prefetching (Read-Ahead)”](innodb-performance-read_ahead.md)
- [Section 14.8.3.5, “Configuring Buffer Pool Flushing”](innodb-buffer-pool-flushing.md)
- [Section 14.8.3.3, “Making the Buffer Pool Scan Resistant”](innodb-performance-midpoint_insertion.md)
- [Section 14.8.3.2, “Configuring Multiple Buffer Pool Instances”](innodb-multiple-buffer-pools.md)
- [Section 14.8.3.6, “Saving and Restoring the Buffer Pool State”](innodb-preload-buffer-pool.md)
- [Section 14.8.3.1, “Configuring InnoDB Buffer Pool Size”](innodb-buffer-pool-resize.md)