---
title: DISABLE_OPT_TRACE
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503811.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# DISABLE_OPT_TRACE

`DISABLE_OPT_TRACE` 过程用于关闭当前 Session 的优化器全链路追踪功能。

  <main id="notice">
  <h4>功能适用性</h4>
  <p>社区版自 V4.2.5 版本支持该功能。</p>
  </main>
  
## 语法

```sql
DBMS_XPLAN.DISABLE_OPT_TRACE;
```

## 示例

关闭当前 Session 的优化器追踪功能。

```shell
obclient> CALL DBMS_XPLAN.DISABLE_OPT_TRACE();
Query OK, 0 rows affected 
```
