---
title: JSON_VALID
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005688043.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# JSON_VALID

## 描述

该函数用于判断输入值是否为有效的 JSON，如果是有效的 JSON 返回 1，否则返回 0。

## 语法

```sql
JSON_VALID(val)
```

## 说明

参数 `val` 为输入值。如果参数为 `NULL`，则返回 `NULL`。

## 示例

```sql
obclient> SELECT JSON_VALID('{"a": 1}');
+------------------------+
| JSON_VALID('{"a": 1}') |
+------------------------+
|                      1 |
+------------------------+
1 row in set

obclient> SELECT JSON_VALID('oceanbase'), JSON_VALID('"oceanbase"');
+-------------------------+---------------------------+
| JSON_VALID('oceanbase') | JSON_VALID('"oceanbase"') |
+-------------------------+---------------------------+
|                       0 |                         1 |
+-------------------------+---------------------------+
1 row in set
```
