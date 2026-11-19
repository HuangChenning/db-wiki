---
title: CURDATE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702906.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
