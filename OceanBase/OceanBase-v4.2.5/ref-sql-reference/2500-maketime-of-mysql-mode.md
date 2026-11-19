---
title: MAKETIME
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504694.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# MAKETIME

## 声明

```sql
MAKETIME(hour,minute,second)
```

## 说明

返回由 `hour:minute:second` 指定的时间值，其中 `second` 可以有小数部分。

## 示例

```sql
obclient> SELECT MAKETIME(12,15,30);
+--------------------+
| MAKETIME(12,15,30) |
+--------------------+
| 12:15:30.000000    |
+--------------------+
1 row in set
```
