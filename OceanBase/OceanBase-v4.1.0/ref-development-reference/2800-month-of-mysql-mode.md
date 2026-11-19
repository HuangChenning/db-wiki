---
title: MONTH
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701600.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
