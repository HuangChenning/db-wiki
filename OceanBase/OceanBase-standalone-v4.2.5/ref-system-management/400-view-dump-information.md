---
title: "查看转储信息"
book: "系统管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150251.html"
tags:
  - oceanbase
  - standalone
  - ref-system-management
---

# 查看转储信息

触发转储后，您可以通过视图查看转储进度和转储历史。

## 查看转储进度

1.  使用 `root` 用户登录集群的 `sys` 租户。

2.  查看转储进度，可以查看转储未完成的数据量及预期完成时间等信息。

    `GV$OB_TABLET_COMPACTION_PROGRESS` 视图用于展示 Tablet 级别 Compaction 任务的进度信息，且仅展示正在运行的任务，任务结束后就不再展示。具体查询语句如下：

    ```
    obclient> SELECT * FROM oceanbase.GV$OB_TABLET_COMPACTION_PROGRESS WHERE TYPE='MINI_MERGE'\G
    *************************** 1. row ***************************
                          SVR_IP: xx.xx.xx.xx
                        SVR_PORT: 2401
                       TENANT_ID: 1002
                            TYPE: MINI_MERGE
                           LS_ID: 1001
                       TABLET_ID: 1152921504606847235
                  COMPACTION_SCN: 1680514780195130031
                         TASK_ID: YXXXXXXXXXXXX-XXXXXXXXXXXXXXXX-0-0
                          STATUS: NODE_RUNNING
                       DATA_SIZE: 31890729
            UNFINISHED_DATA_SIZE: 3351030
    PROGRESSIVE_COMPACTION_ROUND: 1
                     CREATE_TIME: 2025-05-26 10:32:06.278506
                      START_TIME: 2025-05-26 10:34:06.953999
           ESTIMATED_FINISH_TIME: 2025-05-26 16:32:06.969930
    1 row in set
    ```

    查询结果中的部分字段说明如下：

    - `TYPE`：表示 Compaction 任务的类型。

      - `MDS_TABLE_MERGE`：将系统的元数据按照 SSTable 的格式持久化到磁盘里。
      - `MAJOR_MERGE`：租户级合并
      - `MEDIUM_MERGE`：分区级合并
      - `MINI_MERGE`：Mini Compaction，将 MemTable 转变成 Mini SSTable。
      - `MINOR_MERGE`：Minor Compaction，多个 Mini SSTable 合成一个新的 Mini SSTable 或者多个 Mini SSTable 与一个 Minor SSTable 合成一个新的 Minor SSTable。
      - `META_MAJOR_MERGE`：一种特殊的 Compaction 类型，是将某个指定时间点之前的数据合成一个 Meta Major SSTable，其数据格式与 Major SSTable 一样，不包含多版本数据和未提交事务数据。

    - `STATUS`：表示任务状态。任务正在运行中时，该字段值为 `NODE_RUNNING`。

    - `DATA_SIZE`：表示需要转储的总数据量。

    - `UNFINISHED_DATA_SIZE`：表示转储未完成的数据量。

    - `ESTIMATED_FINISH_TIME`：表示预计完成时间。

    有关 `GV$OB_TABLET_COMPACTION_PROGRESS` 视图中字段的详细介绍，请参见 [GV\$OB_TABLET_COMPACTION_PROGRESS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501522)。

    根据查询结果，对于未出现在该视图中的 Tablet 或长时间未完成的 Tablet，可以进一步查看诊断视图 `GV$OB_COMPACTION_DIAGNOSE_INFO`，确认是否有异常情况出现。

    有关 `GV$OB_COMPACTION_DIAGNOSE_INFO` 视图中字段的详细介绍，请参见 [GV\$OB_COMPACTION_DIAGNOSE_INFO](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501517)。

## 查看转储历史

1.  使用 `root` 用户登录集群的 `sys` 租户。

2.  查看转储历史。

    `GV$OB_TABLET_COMPACTION_HISTORY` 视图用于展示 Tablet 级别 Compaction 的历史信息。具体查询语句如下：

    ```
    obclient [oceanbase]> SELECT * FROM oceanbase.GV$OB_TABLET_COMPACTION_HISTORY WHERE TYPE='MINI_MERGE' AND TABLET_ID=200001\G
    *************************** 1. row ***************************
                                   SVR_IP: XXX.XXX.XXX.XXX
                                 SVR_PORT: 2882
                                TENANT_ID: 1
                                    LS_ID: 1
                                TABLET_ID: 200001
                                     TYPE: MINI_MERGE
                           COMPACTION_SCN: 1748248321461094000
                               START_TIME: 2025-05-26 16:32:06.599339
                              FINISH_TIME: 2025-05-26 16:32:06.600478
                                  TASK_ID: YXXXXXXXXXXXX-XXXXXXXXXXXXXXXX-0-0
                              OCCUPY_SIZE: 705
                        MACRO_BLOCK_COUNT: 1
            MULTIPLEXED_MACRO_BLOCK_COUNT: 0
             NEW_MICRO_COUNT_IN_NEW_MACRO: 1
     MULTIPLEXED_MICRO_COUNT_IN_NEW_MACRO: 0
                          TOTAL_ROW_COUNT: 3
                    INCREMENTAL_ROW_COUNT: 3
                        COMPRESSION_RATIO: 0.57
                      NEW_FLUSH_DATA_RATE: 653
             PROGRESSIVE_COMPACTION_ROUND: 0
               PROGRESSIVE_COMPACTION_NUM: 0
                          PARALLEL_DEGREE: 1
                            PARALLEL_INFO: -
                        PARTICIPANT_TABLE: table_cnt=1,start_scn=1,end_scn=1748248321461094000;
                            MACRO_ID_LIST: 483
                                 COMMENTS: extra_info="time_guard=total=4.65ms;";
    1 row in set
    ```

    有关 `GV$OB_TABLET_COMPACTION_HISTORY` 视图中字段的详细介绍，请参见 [GV\$OB_TABLET_COMPACTION_HISTORY](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501615)。
