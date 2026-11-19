---
title: GET_STATS_HISTORY_AVAILABILITY
book: "PL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002016359.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# GET_STATS_HISTORY_AVAILABILITY

`GET_STATS_HISTORY_AVAILABILITY` 函数用于获取当前可用的最早历史统计信息时间，无法恢复指定时间早于这个时间的历史统计信息。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

## 语法 

```sql
DBMS_STATS.GET_STATS_HISTORY_AVAILABILITY
  RETURN TIMESTAMP WITH TIMEZONE;
```

## 示例 

获取当前可用的最早历史统计信息时间。

```sql
obclient> SELECT DBMS_STATS.GET_STATS_HISTORY_AVAILABILITY() FROM DUAL;
+---------------------------------------------+
| DBMS_STATS.GET_STATS_HISTORY_AVAILABILITY() |
+---------------------------------------------+
| 2022-12-06 22:00:01.007146                  |
+---------------------------------------------+
1 row in set
```
