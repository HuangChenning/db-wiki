---
title: "转储和合并"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701869.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 转储和合并

#### 说明

- `memstore_limit_percentage` 用于设置租户使用 MemStore 的内存占其总可用内存的百分比，默认值是 0，取值范围是\[0, 100)。有关该配置项的详细信息，参见 [memstore_limit_percentage](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502223)。
- `freeze_trigger_percentage` 用于设置触发全局冻结的租户使用内存阈值，默认值是 20，取值范围是 (0, 100)。有关该配置项的详细信息，参见 [freeze_trigger_percentage](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502037)。

#### 说明

`major_compact_trigger` 用于设置多少次转储并触发一次全局合并。取值范围为 \[0, 65535\]。有关该配置项的详细信息，参见 [major_compact_trigger](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502059)。
