---
title: SQRT
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002018173.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SQRT

## 声明

```sql
SQRT(X)
```

## 说明

返回 `X` 的平方根。

## 示例

```sql
obclient> SELECT SQRT(4);
+---------+
| SQRT(4) |
+---------+
|       2 |
+---------+
1 row in set

obclient> SELECT SQRT(5);
+------------------+
| SQRT(5)          |
+------------------+
| 2.23606797749979 |
+------------------+
1 row in set

obclient> SELECT SQRT(-16);
+-----------+
| SQRT(-16) |
+-----------+
|      NULL |
+-----------+
1 row in set
```
