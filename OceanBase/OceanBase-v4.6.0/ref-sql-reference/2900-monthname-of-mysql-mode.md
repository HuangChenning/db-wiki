---
title: MONTHNAME
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687941.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# MONTHNAME

## 声明

```sql
MONTHNAME(date)
```

## 说明

返回指定日期 `date` 的月份全称。

## 示例

```sql
obclient> SELECT MONTHNAME('2008-02-03');
+-------------------------+
| MONTHNAME('2008-02-03') |
+-------------------------+
| February                |
+-------------------------+
1 row in set
```
