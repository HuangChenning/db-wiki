---
title: TIME
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002018242.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# TIME

## 声明

```javascript
TIME(datetime)
```

## 说明

以 `TIME` 类型返回 `datetime` 的时间信息。

## 示例

```javascript
obclient> SELECT TIME('2003-12-31 01:02:03');
+-----------------------------+
| TIME('2003-12-31 01:02:03') |
+-----------------------------+
| 01:02:03.000000             |
+-----------------------------+
1 row in set
```
