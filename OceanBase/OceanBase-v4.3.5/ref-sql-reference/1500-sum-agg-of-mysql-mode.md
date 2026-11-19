---
title: SUM
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002017697.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SUM

## 声明

```sql
SUM([DISTINCT | ALL] expr)
```

## 说明

返回 `expr` 的总数。如果集合中无任何行，则返回 `NULL`。`DISTINCT` 关键字可用于求得 `expr` 不同值的总和。

如果找不到匹配的行，该函数也会返回 `NULL`。

## 示例

```javascript
obclient> SELECT * FROM oceanbasetest;
+------+------+------+
| id   | ip   | ip2  |
+------+------+------+
|    1 |    4 | NULL |
|    3 |    3 | NULL |
|    4 |    3 | NULL |
+------+------+------+
3 rows in set

obclient> SELECT SUM(ip2),SUM(ip),SUM(DISTINCT(ip)) FROM oceanbasetest;
+----------+---------+-------------------+
| sum(ip2) | sum(ip) | sum(distinct(ip)) |
+----------+---------+-------------------+
|     NULL |      10 |                 7 |
+----------+---------+-------------------+
1 row in set
```
