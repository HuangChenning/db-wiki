---
title: RESET_GLOBAL_PREF_DEFAULTS
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503591.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# RESET_GLOBAL_PREF_DEFAULTS

`RESET_GLOBAL_PREF_DEFAULTS` 过程用于将全局 Prefs 设置为默认值。

## 语法 

```sql
DBMS_STATS.RESET_GLOBAL_PREF_DEFAULTS;
```



## 示例 

还原全局级别的所有 Prefs 默认值。

```sql
obclient> CALL DBMS_STATS.RESET_GLOBAL_PREF_DEFAULTS();
Query OK, 0 rows affected
```
