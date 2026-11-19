---
title: "物化视图资源隔离"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578246.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 物化视图资源隔离

OceanBase 数据库从 V4.3.5 BP2 版本开始支持 `DBMS_RESOURCE_MANAGER` 为物化视图的增量刷新、MLOG Purge 提供资源隔离的能力，可以限定物化视图能使用的资源上限。

## 示例

1.  创建资源计划 `mview_task`。

    ``` sql
    CALL DBMS_RESOURCE_MANAGER.CREATE_PLAN('mview_task','该资源计划用于物化视图处理');
    ```

    更多关于创建资源计划的信息，参见 [CREATE_PLAN](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002016413)。

2.  创建定义资源用户组 `mview_group`。

    ``` sql
    CALL DBMS_RESOURCE_MANAGER.CREATE_CONSUMER_GROUP('mview_group','物化视图处理组');
    ```

    更多关于创建定义资源用户组的信息，参见 [CREATE_CONSUMER_GROUP](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002016410)。

3.  创建资源计划，限制 CPU 资源使用比例上限 5%。

    ``` sql
    CALL DBMS_RESOURCE_MANAGER.CREATE_PLAN_DIRECTIVE(
        PLAN => 'mview_task',
        GROUP_OR_SUBPLAN => 'mview_group',
        UTILIZATION_LIMIT => 5
        );
    ```

    更多关于创建资源计划指令的信息，参见 [CREATE_PLAN_DIRECTIVE](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002016409)。

4.  绑定资源计划到 `FUNCTION`。

    ``` sql
    CALL DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING(
        ATTRIBUTE => 'FUNCTION',
        VALUE => 'MVIEW',
        CONSUMER_GROUP => 'mview_group'
        );
    ```

    更多关于将会话映射到资源组的条目信息，参见 [SET_CONSUMER_GROUP_MAPPING](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002016415)。

5.  激活资源管理计划 `mview_task`。

    ``` sql
    SET GLOBAL resource_manager_plan = 'mview_task';
    ```

    更多关于激活资源管理计划的信息，参见 [resource_manager_plan](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015919)。

6.  修改 CPU 资源使用上限为 30%。

    ``` sql
    CALL DBMS_RESOURCE_MANAGER.UPDATE_PLAN_DIRECTIVE(
        PLAN => 'mview_task',
        GROUP_OR_SUBPLAN => 'mview_group',
        NEW_UTILIZATION_LIMIT => 30
        );
    ```

    更多关于更新资源计划的信息，参见 [UPDATE_PLAN_DIRECTIVE](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002016411)。

## 相关文档

- [物化视图日志](200-materialized-views-log-of-oracle-mode.md)
- [刷新物化视图](400-refresh-materialized-views-of-oracle-mode.md)
- [DBMS_RESOURCE_MANAGER 概述](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002016408)
