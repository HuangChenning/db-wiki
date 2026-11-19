---
title: explicit_defaults_for_timestamp
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186434.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# explicit_defaults_for_timestamp

explicit_defaults_for_timestamp 用于指定 timestamp 数据类型在处理默认值和空值时是否启用非标准行为。

|  **属性**  |                                                   **描述**                                                   |
|----------|------------------------------------------------------------------------------------------------------------|
| 参数类型     | bool                    |
| 默认值      | ON                      |
| 取值范围     | <li> OFF：不启用   <li> ON：启用     |
| 生效范围     | <li> GLOBAL   <li> SESSION    |
| 是否参与序列化  | 是                       |
| 是否影响计划生成 | 是                       |
