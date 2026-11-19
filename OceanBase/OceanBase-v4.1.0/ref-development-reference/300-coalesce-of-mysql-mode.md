---
title: COALESCE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702729.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
