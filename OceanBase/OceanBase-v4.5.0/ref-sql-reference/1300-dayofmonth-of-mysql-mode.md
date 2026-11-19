---
title: DAYOFMONTH
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004481301.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# DAYOFMONTH

## 声明

```sql
DAYOFMONTH(date)
```

## 说明

返回日期或时间日期 `date` 在一个月中的位置。

## 示例

```sql
obclient> SELECT DAYOFMONTH('2008-12-31');
+--------------------------+
| DAYOFMONTH('2008-12-31') |
+--------------------------+
|                       31 |
+--------------------------+
```
