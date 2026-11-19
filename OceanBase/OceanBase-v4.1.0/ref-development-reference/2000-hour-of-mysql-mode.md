---
title: HOUR
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702923.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# HOUR

## 声明

```sql
HOUR(time)
```

## 说明

返回时间类型 `time` 的小时部分的数值。

## 示例

```sql
obclient> SELECT HOUR('10:05:03');
+------------------+
| HOUR('10:05:03') |
+------------------+
|               10 |
+------------------+
1 row in set 

obclient> SELECT HOUR('272:59:59');
+-------------------+
| HOUR('272:59:59') |
+-------------------+
|               272 |
+-------------------+
1 row in set 
```
