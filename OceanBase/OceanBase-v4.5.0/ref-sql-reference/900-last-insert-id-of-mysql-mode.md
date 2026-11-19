---
title: LAST_INSERT_ID
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480739.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
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
|                0 |
+------------------+
1 row in set
```
