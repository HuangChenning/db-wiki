---
title: MONTHNAME
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701601.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
