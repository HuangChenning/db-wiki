---
title: "删除资源管理计划"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702234.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 删除资源管理计划

您可以调用 `DBMS_RESOURCE_MANAGER` 系统包中的 `DELETE_PLAN` 子程序删除未在使用的资源管理计划。

## 前提条件

请确认待删除的资源管理计划已存在。

## 注意事项

删除资源管理计划会级联删除与该资源管理计划相关的资源管理计划内容。

## 操作步骤

1.  租户管理员登录集群的 MySQL 租户。

2.  调用 `DBMS_RESOURCE_MANAGER` 系统包中的 `DELETE_PLAN` 子程序删除资源管理计划。

    ``` sql
    obclient [test]> CALL DBMS_RESOURCE_MANAGER.DELETE_PLAN(
    PLAN => 'daytime' 
    );
    ```

    其中，`PLAN` 用于指定待删除的资源管理计划。

3.  执行成功后，可以查看 `oceanbase.DBA_RSRC_PLANS` 视图进行确认。

    ``` sql
    +---------+------+----------+-----------------------------------+
    | PLAN_ID | PLAN | SUB_PLAN | COMMENTS                          |
    +---------+------+----------+-----------------------------------+
    |    NULL | DAY  | NULL     | 该资源计划用于事务处理              |
    +---------+------+----------+-----------------------------------+
    1 row in set
    ```

    有关 `oceanbase.DBA_RSRC_PLANS` 视图的详细介绍请参见 [oceanbase.DBA_RSRC_PLANS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501748)。

## 相关文档

[DELETE_PLAN](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503557)
