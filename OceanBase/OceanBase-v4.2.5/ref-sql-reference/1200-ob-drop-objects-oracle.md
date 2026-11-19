---
title: OB_DROP_OBJECTS
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503932.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# OB_DROP_OBJECTS

用于在用户 <code>schema</code> 下删除数据统计表。

<main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

## 语法

```SQL
PROCEDURE OB_DROP_OBJECTS;
```

## 示例

```shell
obclient> call dbms_profiler.ob_drop_objects();
Query OK, 0 rows affected (0.06 sec)
```
