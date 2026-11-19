---
title: MONTH
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002018210.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# MONTH

## 声明

```javascript
MONTH(date)
```

## 说明

返回 `date` 的月份信息。

## 示例

```javascript
obclient> SELECT MONTH('2008-02-03');
+---------------------+
| MONTH('2008-02-03') |
+---------------------+
|                   2 |
+---------------------+
1 row in set
```
