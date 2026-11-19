---
title: RESET_GLOBAL_PREF_DEFAULTS
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699702.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
