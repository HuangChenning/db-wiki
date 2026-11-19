---
title: DELETE_PLAN
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503706.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# DELETE_PLAN

`DELETE_PLAN` 过程用于删除指定的计划以及它所引用的所有计划指令。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

## 语法 

```sql
DBMS_RESOURCE_MANAGER.DELETE_PLAN (
    plan IN VARCHAR2);
```

## 参数说明 

`plan` 用于指定要删除的资源计划的名称。

## 示例 

```shell
obclient> BEGIN
  DBMS_RESOURCE_MANAGER.DELETE_PLAN('NIGHT');
END ;
```
