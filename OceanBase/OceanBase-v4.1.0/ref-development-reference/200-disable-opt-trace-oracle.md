---
title: DISABLE_OPT_TRACE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699755.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# DISABLE_OPT_TRACE

`DISABLE_OPT_TRACE` 过程用于关闭当前 Session 的优化器全链路追踪功能。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
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
