---
title: CURTIME
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702910.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# CURTIME

## 声明

```javascript
CURTIME(scale)
```

## 说明

返回当前时间，不含日期部分。该函数是 `CURRENT_TIME()` 的别名。

`scale` 表示微秒部分精度，有效值为 `0` 到 `6` 的整数，默认值为 `0`。

## 示例

```sql
obclient> SELECT CURTIME(0);
+------------+
| CURTIME(0) |
+------------+
| 16:17:11   |
+------------+
1 row in set 
```
