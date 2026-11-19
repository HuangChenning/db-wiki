---
title: USEC_TO_TIME
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701623.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# USEC_TO_TIME

## 声明

```javascript
USEC_TO_TIME(usec)
```

## 说明

将 `usec` 值转换为 `TIMESTAMP` 类型值。

`usec` 表示距离 `1970-01-01 00:00:00.000000` 的微秒数，并考虑时区信息。

## 示例

```javascript
obclient> SELECT USEC_TO_TIME(1);
+----------------------------+
| USEC_TO_TIME(1)            |
+----------------------------+
| 1970-01-01 08:00:00.000001 |
+----------------------------+
1 row in set 
```
