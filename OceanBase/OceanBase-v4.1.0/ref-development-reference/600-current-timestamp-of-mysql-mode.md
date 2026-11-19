---
title: CURRENT_TIMESTAMP
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702909.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# CURRENT_TIMESTAMP

## 声明

```javascript
CURRENT_TIMESTAMP([scale])
```

## 说明

返回当前时区的日期时间。

`scale` 表示微秒部分精度，有效值为 `0` 到 `6` 的整数，默认值为 `0`。

## 示例

```javascript
obclient> SELECT CURRENT_TIMESTAMP(6);
+-----+
| CURRENT_TIMESTAMP(6)       |
+-----+
| 2018-05-05 11:35:39.177764 |
+-----+
1 row in set 
```
