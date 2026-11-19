---
title: "恢复租户"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077276.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 恢复租户

为防止恶意或误操作导致的数据不可恢复性丢失，OceanBase 数据库提供了回收站功能，从而支持租户级的数据的快速恢复功能。本文介绍如何恢复回收站中的租户。

OceanBase 数据库可以通过 `FLASHBACK TENANT` 语句恢复回收站中的租户。

## 使用限制

由于当前仅 `sys` 租户可以删除租户，故 MySQL 模式和 Oracle 模式的租户被删除后，只能进入 `sys` 租户的回收站中。也只有 `sys` 租户可以执行恢复租户的操作。

## 操作步骤

1.  使用 root 用户登录到集群的 sys 租户。

    ```
    obclient -h172.30.xx.xx -P2881 -uroot@sys -p**** -A
    ```

2.  进入 `oceanbase` 数据库。

    ```
    obclient(root@sys)[(none)]> USE oceanbase;
    ```

3.  通过 `SHOW RECYCLEBIN` 语句，查看当前系统租户回收站中的对象。

    ```
    obclient(root@sys)[oceanbase]> SHOW RECYCLEBIN;
    ```

    返回结果如下：

    ```
    +-------------------------------------+---------------+--------+----------------------------+
    | OBJECT_NAME                         | ORIGINAL_NAME | TYPE   | CREATETIME                 |
    +-------------------------------------+---------------+--------+----------------------------+
    | __recycle_$_100017_1673367572701376 | mq_t1         | TENANT | 2023-01-11 00:23:36.317242 |
    +-------------------------------------+---------------+--------+----------------------------+
    1 row in set
    ```

    回收站相关参数的详细说明，参见 [recyclebin](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285654)。

4.  通过 `FLASHBACK TENANT` 语句，恢复回收站中的租户。

    以恢复租户 `mq_t1` 为例：

    ```
    obclient(root@sys)[oceanbase]> FLASHBACK TENANT mq_t1 TO BEFORE DROP;
    ```

    `FLASHBACK TENANT` 语句的详细说明，参见 [FLASHBACK](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286439)。

5.  查看 `DBA_OB_TENANTS` 视图和回收站确认执行结果。

    ```
    obclient(root@sys)[oceanbase]> SHOW RECYCLEBIN;
    Empty set
    ```

    查询结果为空，再查看 `DBA_OB_TENANTS` 视图，确认租户已恢复。

    ```
    obclient(root@sys)[oceanbase]> SELECT TENANT_ID, TENANT_NAME, TENANT_TYPE, CREATE_TIME, MODIFY_TIME, PRIMARY_ZONE, LOCALITY, COMPATIBILITY_MODE, STATUS FROM DBA_OB_TENANTS WHERE TENANT_NAME = 'mq_t1';
    ```

    返回结果如下：

    ```
    +-----------+-------------+-------------+----------------------------+----------------------------+--------------+---------------+--------------------+--------+
    | TENANT_ID | TENANT_NAME | TENANT_TYPE | CREATE_TIME                | MODIFY_TIME                | PRIMARY_ZONE | LOCALITY      | COMPATIBILITY_MODE | STATUS |
    +-----------+-------------+-------------+----------------------------+----------------------------+--------------+---------------+--------------------+--------+
    |      1004 | mq_t1       | USER        | 2026-04-27 15:32:31.464025 | 2026-04-27 15:32:34.088969 | zone1        | FULL{1}@zone1 | MYSQL              | NORMAL |
    +-----------+-------------+-------------+----------------------------+----------------------------+--------------+---------------+--------------------+--------+
    1 row in set
    ```

## 相关文档

删除租户和回收站相关的更多信息，参见：

- [删除租户](1200-delete-tenant.md)

- [回收站](100-recyclebin-overview.md)。

- [恢复回收站对象](400-restore-the-recyclebin-objects.md)
