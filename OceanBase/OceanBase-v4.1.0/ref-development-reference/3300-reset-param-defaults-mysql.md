---
title: RESET_PARAM_DEFAULTS
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699703.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
