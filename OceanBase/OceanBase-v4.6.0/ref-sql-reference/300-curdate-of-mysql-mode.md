---
title: CURDATE
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687967.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# CURDATE

## 声明

```javascript
CURDATE()
```

## 说明

返回当前日期，不含时间部分。

## 示例

```javascript
obclient> SELECT CURDATE();
+------------+
| CURDATE()  |
+------------+
| 2018-05-05 |
+------------+
1 row in set
```
