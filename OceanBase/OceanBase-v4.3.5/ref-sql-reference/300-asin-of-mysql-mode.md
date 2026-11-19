---
title: ASIN
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002018150.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# ASIN

## 声明

```sql
ASIN(X)
```

## 说明

返回 `X` 的反正弦值，即正弦为 `X` 的值。如果 `X` 的取值不在 `[-1,1]` 区间内，该函数返回 `NULL`。

## 示例

```sql
obclient> SELECT ASIN(-10), ASIN(0), ASIN(10), ASIN(-0.5), ASIN(0.5);
+-----------+---------+----------+---------------------+--------------------+
| ASIN(-10) | ASIN(0) | ASIN(10) | ASIN(-0.5)          | ASIN(0.5)          |
+-----------+---------+----------+---------------------+--------------------+
|      NULL |       0 |     NULL | -0.5235987755982989 | 0.5235987755982989 |
+-----------+---------+----------+---------------------+--------------------+
1 row in set
```
