---
title: ob_sql_audit_percentage
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186419.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ob_sql_audit_percentage

`ob_sql_audit_percentage` 用于设置 SQL Audit 内存上限占当前租户内存的百分比。

| **属性**  |  **描述**   |
|---------|-----------|
| 参数类型    | int       |
| 默认值     | 3         |
| 取值范围    | \[0, 80\] |
| 生效范围    | Global    |
| 是否参与序列化 | 是         |
