---
title: YEAR
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504747.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# YEAR

## 声明

```sql
YEAR(date)
```

## 说明

返回 `date` 值的年份信息。

## 示例

```sql
obclient> SELECT YEAR('1987-01-01');
+--------------------+
| YEAR('1987-01-01') |
+--------------------+
|               1987 |
+--------------------+
1 row in set
```
