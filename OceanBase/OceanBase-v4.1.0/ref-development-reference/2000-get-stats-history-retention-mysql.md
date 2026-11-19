---
title: GET_STATS_HISTORY_RETENTION
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701266.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# GET_STATS_HISTORY_RETENTION

`GET_STATS_HISTORY_RETENTION` 函数用于获取当前历史统计信息的保留间隔时间。

## 语法 

```sql
DBMS_STATS.GET_STATS_HISTORY_RETENTION
  RETURN NUMBER;
```

## 示例 

获取当前历史统计信息的保留间隔时间。

```sql
obclient> SELECT DBMS_STATS.GET_STATS_HISTORY_RETENTION() FROM DUAL;
+------------------------------------------+
| DBMS_STATS.GET_STATS_HISTORY_RETENTION() |
+------------------------------------------+
|                                       15 |
+------------------------------------------+
1 row in set
```
