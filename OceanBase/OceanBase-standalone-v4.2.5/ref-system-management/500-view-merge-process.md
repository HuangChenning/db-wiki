---
title: "查看合并过程"
book: "系统管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150259.html"
tags:
  - oceanbase
  - standalone
  - ref-system-management
---

# 查看合并过程

发起合并后，您可以通过视图来查看合并过程。

合并的过程可以通过内部表进行查看，通常合并的时间是取决于两次合并之间的数据变化量。两次合并之间的数据变化大，合并的时间会更长。同时，合并的线程数、合并时的集群压力等都影响合并的时间长短。

## 系统租户查看所有租户的合并过程

系统租户可以通过查询 `oceanbase.CDB_OB_ZONE_MAJOR_COMPACTION` 和 `oceanbase.CDB_OB_MAJOR_COMPACTION` 视图来观察所有租户的合并信息。

1.  使用 `root` 用户登录集群的 `sys` 租户。

2.  执行以下语句，查看合并进度。

    - 查看所有租户各个 Zone 的合并过程。

      ``` sql
      obclient> SELECT * FROM oceanbase.CDB_OB_ZONE_MAJOR_COMPACTION\G
      *************************** 1. row ***************************
               TENANT_ID: 1
                    ZONE: zone1
           BROADCAST_SCN: 1748250509971336000
                LAST_SCN: 1748250509971336000
        LAST_FINISH_TIME: 2025-05-26 17:10:43.710085
              START_TIME: 2025-05-26 17:08:30.003479
                  STATUS: IDLE
      *************************** 2. row ***************************
               TENANT_ID: 1001
                    ZONE: zone1
           BROADCAST_SCN: 1
                LAST_SCN: 1
        LAST_FINISH_TIME: 2025-05-26 17:15:43.514588
              START_TIME: 2025-05-26 17:05:30.121122
                  STATUS: IDLE
      *************************** 3. row ***************************
               TENANT_ID: 1002
                    ZONE: zone1
           BROADCAST_SCN: 1748250673911253000
                LAST_SCN: 1748250673911253000
        LAST_FINISH_TIME: 2025-05-26 17:16:26.906812
              START_TIME: 2025-05-26 17:11:13.949242
                  STATUS: IDLE
      3 rows in set
      ```

      在执行结果中观察 `status` 列，部分字段说明如下表所示。

      [TABLE]

    - 查看所有租户的合并全局信息。

      ``` sql
      obclient> SELECT * FROM oceanbase.CDB_OB_MAJOR_COMPACTION\G
      *************************** 1. row ***************************
                 TENANT_ID: 1
                FROZEN_SCN: 1748250509971336000
               FROZEN_TIME: 2025-05-26 17:08:29.971336
      GLOBAL_BROADCAST_SCN: 1748250509971336000
                  LAST_SCN: 1748250509971336000
          LAST_FINISH_TIME: 2025-05-26 17:10:43.739933
                START_TIME: 2025-05-26 17:08:29.993232
                    STATUS: IDLE
                  IS_ERROR: NO
              IS_SUSPENDED: NO
                      INFO:
      *************************** 2. row ***************************
                 TENANT_ID: 1001
                FROZEN_SCN: 1
               FROZEN_TIME: 1970-01-01 08:00:00.000000
      GLOBAL_BROADCAST_SCN: 1
                  LAST_SCN: 1
          LAST_FINISH_TIME: 2025-05-26 17:15:43.514588
                START_TIME: 2025-05-26 17:05:30.121122
                    STATUS: IDLE
                  IS_ERROR: NO
              IS_SUSPENDED: NO
                      INFO:
      *************************** 3. row ***************************
                 TENANT_ID: 1002
                FROZEN_SCN: 1748250673911253000
               FROZEN_TIME: 2025-05-26 17:11:13.911253
      GLOBAL_BROADCAST_SCN: 1748250673911253000
                  LAST_SCN: 1748250673911253000
          LAST_FINISH_TIME: 2025-05-26 17:16:26.930780
                START_TIME: 2025-05-26 17:11:13.937381
                    STATUS: IDLE
                  IS_ERROR: NO
              IS_SUSPENDED: NO
                      INFO:
      3 rows in set
      ```

      在执行结果中观察 `status` 列，部分参数的说明如下表所示。

      [TABLE]

## 用户租户查看本租户的合并过程

用户租户可以通过查询 `DBA_OB_ZONE_MAJOR_COMPACTION` 和 `DBA_OB_MAJOR_COMPACTION` 来观察本租户的合并过程。

1.  用户租户的租户管理员登录到数据库。

2.  执行以下语句，查看合并进度。

    - 查看本租户各个 Zone 的合并过程。

      MySQL 模式：

      ``` sql
      obclient> SELECT * FROM oceanbase.DBA_OB_ZONE_MAJOR_COMPACTION\G
      *************************** 1. row ***************************
                  ZONE: zone1
         BROADCAST_SCN: 1748250673911253000
              LAST_SCN: 1748250673911253000
      LAST_FINISH_TIME: 2025-05-26 17:16:26.906812
            START_TIME: 2025-05-26 17:11:13.949242
                STATUS: IDLE
      1 row in set
      ```

      Oracle 模式：

      ``` sql
      obclient> SELECT * FROM sys.DBA_OB_ZONE_MAJOR_COMPACTION\G
      ```

      在执行结果中观察 `status` 列，部分参数的说明如下表所示。

      [TABLE]

    - 查看本租户的合并全局信息。

      MySQL 模式：

      ``` sql
      obclient> SELECT * FROM oceanbase.DBA_OB_MAJOR_COMPACTION\G
      ```

      返回结果如下：

      ```
      *************************** 1. row ***************************
                FROZEN_SCN: 1748250673911253000
               FROZEN_TIME: 2025-05-26 17:11:13.911253
      GLOBAL_BROADCAST_SCN: 1748250673911253000
                  LAST_SCN: 1748250673911253000
          LAST_FINISH_TIME: 2025-05-26 17:16:26.930780
                START_TIME: 2025-05-26 17:11:13.937381
                    STATUS: IDLE
                  IS_ERROR: NO
              IS_SUSPENDED: NO
                      INFO:
      1 row in set
      ```

      在执行结果中观察 `status` 列，部分参数的说明如下表所示。

      [TABLE]

      Oracle 模式：

      ``` sql
      obclient> SELECT * FROM sys.DBA_OB_MAJOR_COMPACTION\G
      ```

      返回结果如下：

      ```
      *************************** 1. row ***************************
                FROZEN_SCN: 1748252298651465000
      GLOBAL_BROADCAST_SCN: 1748252298651465000
                  LAST_SCN: 1748252298651465000
          LAST_FINISH_TIME: 1748252461252613
                START_TIME: 1748252298672195
                    STATUS: IDLE
                  IS_ERROR: NO
              IS_SUSPENDED: NO
                      INFO: NULL
      1 row in set
      ```

      在执行结果中观察 `status` 列，部分参数的说明如下表所示。

      [TABLE]
