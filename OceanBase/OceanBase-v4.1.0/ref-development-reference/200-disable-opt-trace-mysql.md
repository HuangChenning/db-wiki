---
title: DISABLE_OPT_TRACE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702494.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# DISABLE_OPT_TRACE

`DISABLE_OPT_TRACE` 过程用于关闭当前 Session 的优化器全链路追踪功能。

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
