---
title: DELETE_CONSUMER_GROUP
book: "PL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005686444.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# DELETE_CONSUMER_GROUP

`DELETE_CONSUMER_GROUP` 过程用于删除资源使用组。

## 语法

```sql
DBMS_RESOURCE_MANAGER.DELETE_CONSUMER_GROUP (
    consumer_group IN VARCHAR2);
```

## 参数说明

`consumer_group` 用于指定待删除的使用组名称。

## 示例

```sql
obclient> CALL DBMS_RESOURCE_MANAGER.DELETE_CONSUMER_GROUP ('group1');
Query OK, 0 rows affected
```
