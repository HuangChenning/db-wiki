---
title: "查看物理恢复进度"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701919.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 查看物理恢复进度

数据恢复过程中，可以通过视图查看物理恢复进度。

## 操作步骤

1.  使用 `root` 用户登录待恢复租户所在集群的 `sys` 租户。

2.  执行以下语句，查看恢复进度。

    ``` sql
    obclient [oceanbase]> SELECT * FROM oceanbase.CDB_OB_RESTORE_PROGRESS\G
    ```

    查询结果的示例如下：

    ```
    *************************** 1. row ***************************
               TENANT_ID: 1
                  JOB_ID: 2
     RESTORE_TENANT_NAME: mysql
       RESTORE_TENANT_ID: 1012
      BACKUP_TENANT_NAME: test
        BACKUP_TENANT_ID: 1002
     BACKUP_CLUSTER_NAME: standalone
             BACKUP_DEST: file:///data/nfs/backup//archive,file:///data/nfs/backup/data
          RESTORE_OPTION: pool_list=restore_pool&concurrency=50
             RESTORE_SCN: 1743136998483902000
     RESTORE_SCN_DISPLAY: 2025-03-28 12:43:18.483902
                  STATUS: WAIT_TENANT_RESTORE_FINISH
         START_TIMESTAMP: 2025-03-28 12:45:18.821075
         BACKUP_SET_LIST: file:///data/nfs/backup/data/backup_set_1_full
       BACKUP_PIECE_LIST: file:///data/nfs/backup/archive/piece_d1001r1p1,file:///data/nfs/backup/archive/piece_d1001r2p2
             RECOVER_SCN: NULL
     RECOVER_SCN_DISPLAY: NULL
        RECOVER_PROGRESS: NULL
            TABLET_COUNT: NULL
     FINISH_TABLET_COUNT: NULL
        RESTORE_PROGRESS: NULL
             TOTAL_BYTES: NULL
     TOTAL_BYTES_DISPLAY: NULL
            FINISH_BYTES: NULL
    FINISH_BYTES_DISPLAY: NULL
             DESCRIPTION:
    *************************** 2. row ***************************
               TENANT_ID: 1012
                  JOB_ID: 2
     RESTORE_TENANT_NAME: mysql
       RESTORE_TENANT_ID: 1012
      BACKUP_TENANT_NAME: test
        BACKUP_TENANT_ID: 1002
     BACKUP_CLUSTER_NAME: standalone
             BACKUP_DEST: file:///data/nfs/backup//archive,file:///data/nfs/backup/data
          RESTORE_OPTION: pool_list=restore_pool&concurrency=50
             RESTORE_SCN: 1743136998483902000
     RESTORE_SCN_DISPLAY: 2025-03-28 12:43:18.483902
                  STATUS: RESTORING
         START_TIMESTAMP: 2025-03-28 12:45:18.821075
         BACKUP_SET_LIST: file:///data/nfs/backup/data/backup_set_1_full
       BACKUP_PIECE_LIST: file:///data/nfs/backup/archive/piece_d1001r1p1,file:///data/nfs/backup/archive/piece_d1001r2p2
             RECOVER_SCN: 1743132903785125999
     RECOVER_SCN_DISPLAY: 2025-03-28 11:35:03.785125
        RECOVER_PROGRESS: 0.00
            TABLET_COUNT: 0
     FINISH_TABLET_COUNT: 0
        RESTORE_PROGRESS: NULL
             TOTAL_BYTES: 24971047
     TOTAL_BYTES_DISPLAY: 23.81MB
            FINISH_BYTES: 0
    FINISH_BYTES_DISPLAY: 0.00MB
             DESCRIPTION:
    2 rows in set
    ```

    该视图记录了恢复时用户输入的相关参数，以及恢复的进度等信息。

    一次租户恢复对应两条任务记录: `sys` 租户的任务记录和被恢复租户的任务记录。 `sys` 租户的任务记录主要记录被恢复租户的恢复相关信息，不会记录恢复进度信息，被恢复租户的任务记录主要记录其自身的恢复进度信息。

    在恢复期间，主要关注恢复进度视图中的 `status` 字段：

    - 系统租户：

      - `CREATE_TENANT`: 创建租户，此阶段系统租户创建被恢复租户。 租户创建完成, 状态变更为 `WAIT_TENANT_RESTORE_FINISH`；创建失败，则变更为 `RESTORE_FAIL`。

      - `WAIT_TENANT_RESTORE_FINISH`: 等待被恢复租户的恢复结束。租户恢复完成, 状态变更为 `RESTORE_SUCCESS`； 恢复失败，则变更为 `RESTORE_FAIL`。

      - `RESTORE_SUCCESS`: 恢复租户成功。

      - `RESTORE_FAIL`: 恢复租户失败。

    - 被恢复租户：

      - `RESTORING`: 租户数据恢复中。恢复完成，状态会变更为 `RESTORE_SUCCESS`；如果恢复失败，状态会变更为 `RESTORE_FAIL`。

      - `RESTORE_SUCCESS`: 恢复成功。

      - `RESTORE_FAIL`: 恢复失败。

    更多关于 `CDB_OB_RESTORE_PROGRESS` 视图的介绍，请参见 [恢复视图](900-views-of-the-restore.md)。

    待恢复完成后，可以查看恢复结果，具体操作请参见 [查看恢复结果](500-view-the-restore-history.md)。
