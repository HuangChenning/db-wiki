---
title: CURRENT_INSTANCE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702546.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# CURRENT_INSTANCE

CURRENT_INSTANCE 
=====================================

`CURRENT_INSTANCE` 函数用于返回当前连接的实例编号。当连接的实例关闭时，返回 `NULL`。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

语法 
-----------------------

```sql
DBMS_UTILITY.CURRENT_INSTANCE
RETURN NUMBER;
```
