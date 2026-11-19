---
title: ob_plan_cache_percentage
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186405.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ob_plan_cache_percentage

ob_plan_cache_percentage 用于设置计划缓存可使用内存占租户内存的百分比。

| **属性**  |   **描述**   |
|---------|------------|
| 参数类型    | int        |
| 默认值     | 5          |
| 取值范围    | \[0, 100\] |
| 生效范围    | GLOBAL     |
| 是否参与序列化 | 是          |

计划缓存最多可使用内存（内存上限绝对值）= 租户内存上限 \* ob_plan_cache_percentage/100。
