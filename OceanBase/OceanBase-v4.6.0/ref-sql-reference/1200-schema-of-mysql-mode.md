---
title: SCHEMA
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687353.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SCHEMA

## 声明

```sql
SCHEMA()
```

## 说明

返回当前 Schema 名称。此函数是 `DATABASE()` 的同义词。

## 示例

如下示例为查询当前的 Schema 名称。

```sql
obclient> SELECT SCHEMA();
+----------+
| SCHEMA() |
+----------+
| test     |
+----------+
1 row in set
```
