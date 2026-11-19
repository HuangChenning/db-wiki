---
title: DISABLE_OPT_TRACE
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286801.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
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
