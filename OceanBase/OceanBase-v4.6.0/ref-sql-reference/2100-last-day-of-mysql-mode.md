---
title: LAST_DAY
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687914.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# LAST_DAY

## 声明

```sql
LAST_DAY(date)
```

## 说明

返回 `date` 当月最后一天的日期值。

## 示例

```sql
obclient> SELECT LAST_DAY('2004-02-05');
+------------------------+
| LAST_DAY('2004-02-05') |
+------------------------+
| 2004-02-29             |
+------------------------+
1 row in set

obclient> SELECT LAST_DAY('2004-01-01 01:01:01');
+---------------------------------+
| LAST_DAY('2004-01-01 01:01:01') |
+---------------------------------+
| 2004-01-31                      |
+---------------------------------+
1 row in set
```
