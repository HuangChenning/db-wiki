---
title: WEEKDAY
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504725.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# WEEKDAY

## 声明

```sql
WEEKDAY(date)
```

## 说明

返回日期或日期时间类型 `date` 在一周中的位置。

## 示例

```sql
obclient> SELECT WEEKDAY('2021-07-16 00:00:00');
+--------------------------------+
| WEEKDAY('2020-07-16 00:00:00') |
+--------------------------------+
|                              5 |
+--------------------------------+
1 row in set
```
