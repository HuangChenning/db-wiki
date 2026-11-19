---
title: LAST_INSERT_ID
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702764.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# LAST_INSERT_ID

## 声明

```sql
LAST_INSERT_ID()
```

## 说明

返回本 Session 最后一次插入的自增字段值。

特别地，如果最近一条 `INSERT` 插入多条记录，`LAST_INSERT_ID()` 返回第一条记录的自增字段值。

## 示例

```sql
obclient> CREATE TABLE t1(c1 INT,c2 INT AUTO_INCREMENT);
obclient> SELECT LAST_INSERT_ID();
+------------------+
| LAST_INSERT_ID() |
+------------------+
|                5 |
+------------------+
1 row in set 
```
