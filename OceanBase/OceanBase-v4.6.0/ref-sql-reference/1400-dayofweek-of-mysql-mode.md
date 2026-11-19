---
title: DAYOFWEEK
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687972.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# DAYOFWEEK

## 声明

```sql
DAYOFWEEK(date)
```

## 说明

返回日期或时间日期 `date` 在一周中的位置，从周日开始计算。

## 示例

```sql
obclient> SELECT DAYOFWEEK('2021-07-15');
+-------------------------+
| DAYOFWEEK('2021-07-15') |
+-------------------------+
|                       5 |
+-------------------------+
1 row in set
```
