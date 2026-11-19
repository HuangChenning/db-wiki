---
title: "手动触发合并"
book: "系统管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077796.html"
tags:
  - oceanbase
  - standalone
  - ref-system-management
---

# 手动触发合并

#### 说明

OceanBase 数据库从 V4.2.1 版本开始，`TENANT = all_user` 与 `TENANT = all`语义相同，在需要生效范围为所有用户租户时，推荐使用 `TENANT = all_user`，后续 `TENANT = all` 将废弃不再使用。

#### 注意

分区级合并命令与租户级合并以及自适应调度策略发起的合并均存在互斥关系，命令执行成功并不代表分区合并发起成功。您可以根据视图 `GV$OB_MERGE_INFO` 查看指定分区中 `ACTION='MEDIUM_MERGE'` 的合并信息，或者根据视图 `GV$OB_TABLET_COMPACTION_HISTORY` 查看指定分区中 `TYPE='MEDIUM_MERGE'` 的合并信息来确认合并是否成功发起。有关查看合并信息的详细操作，请参见 [查看合并信息](500-view-merge-process.md)。

#### 注意

分区级合并命令与租户级合并以及自适应调度策略发起的合并均存在互斥关系，命令执行成功并不代表分区合并发起成功。用户租户可以根据视图 `GV$OB_TABLET_COMPACTION_HISTORY` 查看指定分区中 `TYPE='MEDIUM_MERGE'` 的合并信息来确认合并是否成功发起。有关查看合并信息的详细操作，请参见 [查看合并信息](500-view-merge-process.md)。
