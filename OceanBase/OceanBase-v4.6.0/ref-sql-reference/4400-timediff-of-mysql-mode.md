---
title: TIMEDIFF
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687925.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# TIMEDIFF

## 声明

```javascript
TIMEDIFF(date1, date2)
```

## 说明

以 `TIME` 类型返回两个日期时间的时间间隔。

## 示例

```javascript
obclient> SELECT
     TIMEDIFF('2015-06-06 12:12:12', '2014-06-05 11:11:11'),
     TIMEDIFF('2015-06-06 12:12:12', '2015-06-05 11:11:11')
     \G
*************************** 1. row ***************************
TIMEDIFF('2015-06-06 12:12:12', '2014-06-05 11:11:11'): 838:59:59
TIMEDIFF('2015-06-06 12:12:12', '2015-06-05 11:11:11'): 25:01:01
1 row in set
```
