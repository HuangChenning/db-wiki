---
title: DATEDIFF
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687926.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# DATEDIFF

## 声明

```javascript
DATEDIFF(date1, date2)
```

## 说明

返回 `date1` 和 `date2` 之间的天数。

计算中只用到参数的日期部分，忽略时间部分。

## 示例

```javascript
obclient> SELECT DATEDIFF('2015-06-19','1994-12-17');
+-------------------------------------+
| DATEDIFF('2015-06-19','1994-12-17') |
+-------------------------------------+
|                                7489 |
+-------------------------------------+
1 row in set
```
