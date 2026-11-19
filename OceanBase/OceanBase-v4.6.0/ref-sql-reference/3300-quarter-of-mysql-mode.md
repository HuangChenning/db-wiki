---
title: QUARTER
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687934.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# QUARTER

## 声明

```sql
QUARTER(date)
```

## 说明

返回指定日期的季度值，取值范围为 \[1,4\]。

## 示例

```sql
obclient> SELECT QUARTER(NOW()), NOW();
+----------------+---------------------+
| QUARTER(NOW()) | NOW()               |
+----------------+---------------------+
|              3 | 2021-07-12 19:45:01 |
+----------------+---------------------+
1 row in set
```
