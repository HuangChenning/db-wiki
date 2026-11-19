---
title: COALESCE
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480696.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# COALESCE

## 声明

```sql
COALESCE(expr, expr, expr,...)
```

## 说明

依次参考各参数表达式，遇到非 `NULL` 值即停止并返回该值。如果所有的表达式都是空值，最终将返回一个空值。

所有表达式必须是相同类型，或者可以隐性转换为相同的类型。

## 示例

```sql
obclient> SELECT COALESCE(NULL,NULL,3,4,5), COALESCE(NULL,NULL,NULL);
+---------------------------+--------------------------+
| COALESCE(NULL,NULL,3,4,5) | COALESCE(NULL,NULL,NULL) |
+---------------------------+--------------------------+
|                         3 |                     NULL |
+---------------------------+--------------------------+
1 row in set
```
