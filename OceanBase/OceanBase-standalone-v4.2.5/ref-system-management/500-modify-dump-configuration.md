---
title: "修改转储配置"
book: "系统管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150252.html"
tags:
  - oceanbase
  - standalone
  - ref-system-management
---

# 修改转储配置

#### 说明

在 V4.3.x 版本中，从 V4.3.0 版本开始，还支持通过租户级隐藏配置项 `_memstore_limit_percentage` 来配置租户 MemStore 占租户总内存的百分比，除了生效范围不同，其功能及默认值与集群级配置项 `memstore_limit_percentage` 均相同。在配置这两个配置项时，需要注意以下事项：

- 如果仅配置了 `_memstore_limit_percentage` 或 `memstore_limit_percentage` 中某一个配置项的值（非默认值），则以配置的值（非默认值）为准。
- 如果同时配置了租户级隐藏配置项 `_memstore_limit_percentage`（非默认值）和集群级配置项 `memstore_limit_percentage` （非默认值）的值，则以 `_memstore_limit_percentage`配置的值为准。
- 如果两者均未配置，或均配置为默认值时，系统将采用以下自适应策略：
  - 内存为 8G （真实 Memory）及以下规格的租户，其租户 Memstore 的配置比例为 40%。
  - 内存为 8G 以上规格的租户，其租户 Memstore 的配置比例为 50%。

#### 注意

集群级配置项需要在 `sys` 租户下设置。
