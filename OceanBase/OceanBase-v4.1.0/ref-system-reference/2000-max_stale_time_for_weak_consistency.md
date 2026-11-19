---
title: max_stale_time_for_weak_consistency
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700964.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# max_stale_time_for_weak_consistency

max_stale_time_for_weak_consistency 用于设置弱一致性读允许读到多旧的数据。

|        属性        |    描述     |
|------------------|-----------|
| 参数类型             | 时间类型      |
| 默认值              | 5s        |
| 取值范围             | \[5s, +∞) |
| 是否重启 OBServer 节点生效 | 否         |
