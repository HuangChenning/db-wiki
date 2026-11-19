---
title: DELETE_PLAN
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503557.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# DELETE_PLAN

`DELETE_PLAN` 过程用于删除指定的计划以及它所引用的所有计划指令。

## 语法 

```sql
DBMS_RESOURCE_MANAGER.DELETE_PLAN (
    plan IN VARCHAR2);
```

## 参数说明 

`plan` 用于指定要删除的资源计划的名称。

## 示例 

```sql
obclient> CALL DBMS_RESOURCE_MANAGER.DELETE_PLAN('NIGHT');
Query OK, 0 rows affected
```
