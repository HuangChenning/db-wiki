---
title: RESET_PARAM_DEFAULTS
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503563.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# RESET_PARAM_DEFAULTS

`RESET_PARAM_DEFAULTS` 过程将所有参数的默认值重置为数据库推荐的值。

## 语法 

```sql
DBMS_STATS.RESET_PARAM_DEFAULTS;
```

## 示例 

```sql
obclient> CALL DBMS_STATS.RESET_PARAM_DEFAULTS;
Query OK, 0 rows affected
```
