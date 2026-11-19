---
title: CURRENT_TIME
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702908.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# CURRENT_TIME

## 声明

```javascript
CURRENT_TIME([scale])
```

## 说明

返回当前时间，不含日期部分。

`scale` 表示微秒部分精度，有效值为 `0` 到 `6` 的整数，默认值为 `0`。

## 示例

```javascript
obclient> SELECT CURRENT_TIME(6);
+-----------------+
| CURRENT_TIME(6) |
+-----------------+
| 11:11:45.215311 |
+-----------------+
1 row in set 
```
