---
title: "查看数据备份结果"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701945.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 查看数据备份结果

数据备份执行完成后，您可以通过视图查看备份任务历史。

## 系统租户查看数据备份任务历史

1.  使用 `root` 用户登录集群的 `sys` 租户。

2.  查看数据备份历史。

    - 查看 JOB 级任务历史

      租户发起一次备份即对应一条 JOB 任务记录。

      ``` sql
      obclient [oceanbase]> SELECT * FROM oceanbase.CDB_OB_BACKUP_JOB_HISTORY\G
      ```

      查询结果如下：

      ```
      *************************** 1. row ***************************
                TENANT_ID: 1002
                   JOB_ID: 1
              INCARNATION: 1
            BACKUP_SET_ID: 1
      INITIATOR_TENANT_ID: 1002
         INITIATOR_JOB_ID: 0
       EXECUTOR_TENANT_ID: 1002
          PLUS_ARCHIVELOG: OFF
              BACKUP_TYPE: FULL
                JOB_LEVEL: USER_TENANT
          ENCRYPTION_MODE: NONE
                   PASSWD:
          START_TIMESTAMP: 2025-03-28 11:34:28.032635
            END_TIMESTAMP: 2025-03-28 11:36:47.269458
                   STATUS: COMPLETED
                   RESULT: 0
                  COMMENT:
              DESCRIPTION:
                     PATH: file:///data/nfs/backup/data
      *************************** 2. row ***************************
                TENANT_ID: 1008
                   JOB_ID: 1
              INCARNATION: 1
            BACKUP_SET_ID: 1
      INITIATOR_TENANT_ID: 1008
         INITIATOR_JOB_ID: 0
       EXECUTOR_TENANT_ID: 1008
          PLUS_ARCHIVELOG: OFF
              BACKUP_TYPE: FULL
                JOB_LEVEL: USER_TENANT
          ENCRYPTION_MODE: NONE
                   PASSWD:
          START_TIMESTAMP: 2025-03-27 21:19:48.280892
            END_TIMESTAMP: 2025-03-27 21:21:29.334126
                   STATUS: COMPLETED
                   RESULT: 0
                  COMMENT:
              DESCRIPTION:
                     PATH: file:///data/nfs/backup/data
      2 rows in set
      ```

    - 查看 Task 级任务历史

      一个 Task 对应一个备份集的任务。

      ``` sql
      obclient [oceanbase]> SELECT * FROM oceanbase.CDB_OB_BACKUP_TASK_HISTORY\G
      ```

      查询结果如下：

      ```
      *************************** 1. row ***************************
                     TENANT_ID: 1002
                       TASK_ID: 1
                        JOB_ID: 1
                   INCARNATION: 1
                 BACKUP_SET_ID: 1
               START_TIMESTAMP: 2025-03-28 11:34:28.032635
                 END_TIMESTAMP: 2025-03-28 11:36:47.243439
                        STATUS: COMPLETED
                     START_SCN: 1743132890184347000
                       END_SCN: 1743133007208983000
             USER_LS_START_SCN: 1743132900046938000
               ENCRYPTION_MODE: NONE
                        PASSWD:
                   INPUT_BYTES: 177249726
                  OUTPUT_BYTES: 24971047
             OUTPUT_RATE_BYTES: 179375.7832
              EXTRA_META_BYTES: 0
                  TABLET_COUNT: 678
           FINISH_TABLET_COUNT: 678
             MACRO_BLOCK_COUNT: 84
      FINISH_MACRO_BLOCK_COUNT: 84
                    FILE_COUNT: 0
                  META_TURN_ID: 1
                  DATA_TURN_ID: 0
                        RESULT: 0
                       COMMENT:
                          PATH: file:///data/nfs/backup/data
                 MINOR_TURN_ID: 1
                 MAJOR_TURN_ID: 1
      *************************** 2. row ***************************
                     TENANT_ID: 1008
                       TASK_ID: 1
                        JOB_ID: 1
                   INCARNATION: 1
                 BACKUP_SET_ID: 1
               START_TIMESTAMP: 2025-03-27 21:19:48.280892
                 END_TIMESTAMP: 2025-03-27 21:21:29.308480
                        STATUS: COMPLETED
                     START_SCN: 1743081606572222000
                       END_SCN: 1743081689271339000
             USER_LS_START_SCN: 1743081614467223000
               ENCRYPTION_MODE: NONE
                        PASSWD:
                   INPUT_BYTES: 271611097
                  OUTPUT_BYTES: 23088778
             OUTPUT_RATE_BYTES: 228539.3372
              EXTRA_META_BYTES: 0
                  TABLET_COUNT: 667
           FINISH_TABLET_COUNT: 667
             MACRO_BLOCK_COUNT: 129
      FINISH_MACRO_BLOCK_COUNT: 129
                    FILE_COUNT: 0
                  META_TURN_ID: 1
                  DATA_TURN_ID: 0
                        RESULT: 0
                       COMMENT:
                          PATH: file:///data/nfs/backup/data
                MINOR_TURN_ID: 1
                MAJOR_TURN_ID: 1
      2 rows in set
      ```

      `oceanbase.CDB_OB_BACKUP_JOB_HISTORY` 视图中的各字段基本与 `oceanbase.CDB_OB_BACKUP_JOBS` 视图相对应，`oceanbase.CDB_OB_BACKUP_TASK_HISTORY` 各字段基本与 `oceanbase.CDB_OB_BACKUP_TASKS` 相对应。其中，`COMMENT` 用于记录任务失败时的相关错误信息。

    更多 `CDB_OB_BACKUP_JOB_HISTORY` 和 `CDB_OB_BACKUP_TASK_HISTORY` 视图的说明，请参见 [CDB_OB_BACKUP_JOB_HISTORY](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501296) 和 [CDB_OB_BACKUP_TASK_HISTORY](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501107)。

3.  查看对应的备份集信息。

    ``` sql
    obclient [oceanbase]> SELECT * FROM oceanbase.CDB_OB_BACKUP_SET_FILES WHERE TENANT_ID = 1002 AND BACKUP_SET_ID = 1\G
    ```

    查询结果如下：

    ```
    *************************** 1. row ***************************
                    TENANT_ID: 1002
                BACKUP_SET_ID: 1
                      DEST_ID: 1001
                  INCARNATION: 1
                  BACKUP_TYPE: FULL
      PREV_FULL_BACKUP_SET_ID: 0
       PREV_INC_BACKUP_SET_ID: 0
              START_TIMESTAMP: 2025-03-28 11:34:28.032635
                END_TIMESTAMP: 2025-03-28 11:36:47.243439
                       STATUS: SUCCESS
                  FILE_STATUS: AVAILABLE
             ELAPSED_SECONDES: 139
              PLUS_ARCHIVELOG: OFF
             START_REPLAY_SCN: 1743132761189584000
     START_REPLAY_SCN_DISPLAY: 2025-03-28 11:32:41.189584
              MIN_RESTORE_SCN: 1743133007208983000
      MIN_RESTORE_SCN_DISPLAY: 2025-03-28 11:36:47.208983000
                  INPUT_BYTES: 177249726
                 OUTPUT_BYTES: 24971047
            OUTPUT_RATE_BYTES: 179375.7832
             EXTRA_META_BYTES: 0
                 TABLET_COUNT: 678
          FINISH_TABLET_COUNT: 678
            MACRO_BLOCK_COUNT: 84
     FINISH_MACRO_BLOCK_COUNT: 84
                   FILE_COUNT: 0
                 META_TURN_ID: 1
                 DATA_TURN_ID: 0
                       RESULT: 0
                      COMMENT:
              ENCRYPTION_MODE: NONE
                       PASSWD:
            TENANT_COMPATIBLE: 4.2.5.3
            BACKUP_COMPATIBLE: 3
                         PATH: file:///data/nfs/backup/data
              CLUSTER_VERSION: 4.2.5.3
               CONSISTENT_SCN: 1743132910463917000
                MINOR_TURN_ID: 1
                MAJOR_TURN_ID: 1
     1 row in set
    ```

    更多 `CDB_OB_BACKUP_SET_FILES` 视图的说明，请参见 [CDB_OB_BACKUP_SET_FILES](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501280)。

## 用户租户查看数据备份任务历史

1.  租户管理员登录到数据库。

2.  查看数据备份历史。

    - 查看 JOB 级任务历史

      租户发起一次备份即对应一条 JOB 任务记录。

      MySQL 模式

      Oracle 模式

      MySQL 模式下的查询示例如下：

      ``` sql
      obclient [oceanbase]> SELECT * FROM oceanbase.DBA_OB_BACKUP_JOB_HISTORY\G
      ```

      Oracle 模式下的查询示例如下：

      ``` sql
      obclient [SYS]> SELECT * FROM SYS.DBA_OB_BACKUP_TASK_HISTORY\G
      ```

    - 查看 Task 级任务历史

      一个 Task 对应一个备份集的任务。

      MySQL 模式

      Oracle 模式

      MySQL 模式下的查询示例如下：

      ``` sql
      obclient [oceanbase]> SELECT * FROM oceanbase.DBA_OB_BACKUP_TASK_HISTORY\G
      ```

      Oracle 模式下的查询示例如下：

      ``` sql
      obclient [SYS]> SELECT * FROM SYS.DBA_OB_BACKUP_TASK_HISTORY\G
      ```

3.  查看对应的备份集信息。

    MySQL 模式

    Oracle 模式

    MySQL 模式下的查询示例如下：

    ``` sql
    obclient [oceanbase]> SELECT * FROM oceanbase.DBA_OB_BACKUP_SET_FILES WHERE BACKUP_SET_ID = 1 \G
    ```

    Oracle 模式下的查询示例如下：

    ``` sql
    obclient [SYS]> SELECT * FROM SYS.DBA_OB_BACKUP_SET_FILES WHERE BACKUP_SET_ID = 1 \G
    ```
