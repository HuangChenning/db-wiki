---
title: ob_enable_sql_audit
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186386.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ob_enable_sql_audit

ob_enable_sql_audit 用于控制当前租户是否开启 SQL Audit 功能。

| **属性**  |                                                      **描述**                                                      |
|---------|------------------------------------------------------------------------------------------------------------------|
| 参数类型    | bool                          |
| 默认值     | true                          |
| 取值范围    | <li> true：表示开启   <li> false：表示关闭    |
| 生效范围    | GLOBAL                        |
| 是否参与序列化 | 是                             |

enable_sql_audit 为 false 时，全部的租户均不会开启 sql audit 功能。
