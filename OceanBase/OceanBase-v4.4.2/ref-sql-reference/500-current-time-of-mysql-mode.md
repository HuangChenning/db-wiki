---
title: CURRENT_TIME
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288213.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
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
