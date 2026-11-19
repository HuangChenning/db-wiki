---
title: ob_enable_aggregation_pushdown
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186376.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ob_enable_aggregation_pushdown

ob_enable_aggregation_pushdown 用于设置是否允许聚合操作下压。

|  **属性**  |                                                   **描述**                                                   |
|----------|------------------------------------------------------------------------------------------------------------|
| 参数类型     | bool                    |
| 默认值      | 1                       |
| 取值范围     | <li> 0：不允许   <li> 1：允许        |
| 生效范围     | <li> GLOBAL   <li> SESSION    |
| 是否参与序列化  | 是                       |
| 是否影响计划生成 | 是                       |
