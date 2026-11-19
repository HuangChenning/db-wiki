---
title: nls_length_semantics
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183523.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# nls_length_semantics

`nls_length_semantics` 表示 char、varchar2 类型 的 length 语义。

|  **属性**  |                                                   **描述**                                                   |
|----------|------------------------------------------------------------------------------------------------------------|
| 参数类型     | varchar                 |
| 默认值      | BYTE                    |
| 取值范围     | <li> BYTE   <li> CHAR         |
| 生效范围     | <li> Global   <li> Session    |
| 是否参与序列化  | 是                       |
| 是否影响计划生成 | 是                       |
