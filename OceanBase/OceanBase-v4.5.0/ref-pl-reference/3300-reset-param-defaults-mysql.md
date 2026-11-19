---
title: RESET_PARAM_DEFAULTS
book: "PL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479853.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
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
