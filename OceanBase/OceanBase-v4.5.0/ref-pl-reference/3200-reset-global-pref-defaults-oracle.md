---
title: RESET_GLOBAL_PREF_DEFAULTS
book: "PL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480207.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# RESET_GLOBAL_PREF_DEFAULTS

`RESET_GLOBAL_PREF_DEFAULTS` 过程用于将全局 Prefs 设置为默认值。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版暂不支持。</p>
  </main>

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
