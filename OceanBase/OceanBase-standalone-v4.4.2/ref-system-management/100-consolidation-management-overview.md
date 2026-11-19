---
title: "合并管理概述"
book: "系统管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077799.html"
tags:
  - oceanbase
  - standalone
  - ref-system-management
---

# 合并管理概述

#### 说明

更高的压缩率将更节约磁盘空间，但是也意味着性能的牺牲。例如，通常 ZSTD 比 LZ4 节省更多的空间，但是 ZSTD 合并的时间更长，同时需要 IO 查询的 RT 也更大。
