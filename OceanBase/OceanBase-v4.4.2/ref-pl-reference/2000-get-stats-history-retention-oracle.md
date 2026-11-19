---
title: GET_STATS_HISTORY_RETENTION
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005287097.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# GET_STATS_HISTORY_RETENTION

`GET_STATS_HISTORY_RETENTION` 函数用于获取当前历史统计信息的保留间隔时间。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

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
