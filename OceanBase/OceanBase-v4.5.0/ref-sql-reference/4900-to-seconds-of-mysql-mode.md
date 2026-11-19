---
title: TO_SECONDS
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004481357.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# TO_SECONDS

## 声明

```sql
TO_SECONDS(expr)
```

## 说明

返回时间或日期时间表达式 `expr` 自公元零年起的秒数。如果 `expr` 为 `NULL`，则返回 `NULL`。

## 示例

```sql
obclient> SELECT TO_SECONDS(950501);
+--------------------+
| TO_SECONDS(950501) |
+--------------------+
|        62966505600 |
+--------------------+
1 row in set

obclient> SELECT TO_SECONDS('2021-07-15');
+--------------------------+
| TO_SECONDS('2021-07-15') |
+--------------------------+
|              63793526400 |
+--------------------------+
1 row in set
```
