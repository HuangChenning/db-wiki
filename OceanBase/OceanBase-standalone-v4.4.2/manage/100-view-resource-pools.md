---
title: "查看资源池"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077591.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 查看资源池

资源池创建成功后，您可以查看集群中的资源池以及各资源池的分布情况。

## 操作步骤

1.  使用 `root` 用户登录集群的 `sys` 租户。

2.  执行以下语句，查看集群中的资源池信息。

    ``` sql
    obclient [oceanbase]> SELECT * FROM oceanbase.DBA_OB_RESOURCE_POOLS\G
    *************************** 1. row ***************************
    RESOURCE_POOL_ID: 1
                NAME: sys_pool
           TENANT_ID: 1
         CREATE_TIME: 2026-04-27 15:27:50.328370
         MODIFY_TIME: 2026-04-27 15:27:50.328370
          UNIT_COUNT: 1
      UNIT_CONFIG_ID: 1
           ZONE_LIST: zone1
        REPLICA_TYPE: FULL
    *************************** 2. row ***************************
    RESOURCE_POOL_ID: 1001
                NAME: test_pool
           TENANT_ID: 1002
         CREATE_TIME: 2026-04-27 15:28:07.623621
         MODIFY_TIME: 2026-04-27 15:28:07.642679
          UNIT_COUNT: 1
      UNIT_CONFIG_ID: 1001
           ZONE_LIST: zone1
        REPLICA_TYPE: FULL
    *************************** 3. row ***************************
    RESOURCE_POOL_ID: 1002
                NAME: mq_pool_01
           TENANT_ID: 1004
         CREATE_TIME: 2026-04-27 15:31:40.027348
         MODIFY_TIME: 2026-04-27 15:32:31.466142
          UNIT_COUNT: 1
      UNIT_CONFIG_ID: 1002
           ZONE_LIST: zone1
        REPLICA_TYPE: FULL
    *************************** 4. row ***************************
    RESOURCE_POOL_ID: 1005
                NAME: mq_pool_02
           TENANT_ID: NULL
         CREATE_TIME: 2026-04-28 14:14:45.843252
         MODIFY_TIME: 2026-04-28 14:15:59.766659
          UNIT_COUNT: 1
      UNIT_CONFIG_ID: 1004
           ZONE_LIST: zone1
        REPLICA_TYPE: FULL
    4 rows in set
    ```

    其中：

    - `RESOURCE_POOL_ID`：资源池 ID，每个资源池对应一个资源池 ID。

    - `TENANT_ID`：该资源池归属的租户 ID，每个租户对应一个租户 ID，`sys` 租户的租户 ID 为 `1`，当前租户详细信息的查看方法，请参见 [查看租户和资源信息](400-view-tenant-information.md)。

      如果查询结果中 `TENANT_ID` 为 `NULL`，则表示当前资源池未绑定租户，您可以将该资源池分配给租户，将资源池分配给租户的详细操作请参见 [将资源池分配给租户](200-assign-a-resource-pool-to-a-tenant.md)。

    - `UNIT_COUNT`：资源池中资源单元的个数。

    - `UNIT_CONFIG_ID`：资源池对应的资源单元规格 ID。一个资源单元对应一个资源单元规格 ID。

      资源单元对应的资源单元规格（即资源单元配置）的查看方法，请参见 [查看资源单元配置](100-view-resource-unit-configuration.md)。

    - `ZONE_LIST`：表示资源池的 Zone 列表，展示该资源池的资源在哪些 Zone 中被使用。对于 OceanBase 集中式数据库，只有一个 Zone。
