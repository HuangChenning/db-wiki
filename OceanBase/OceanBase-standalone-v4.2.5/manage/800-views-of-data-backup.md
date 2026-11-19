---
title: "数据备份相关视图介绍"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701939.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 数据备份相关视图介绍

OceanBase 数据库支持通过各视图查看备份的进度与结果。

## CDB_OB_BACKUP_JOBS

`oceanbase.CDB_OB_BACKUP_JOBS` 用于展示各租户 Job 级数据备份的进度。

[TABLE]

## CDB_OB_BACKUP_JOB_HISTORY

`oceanbase.CDB_OB_BACKUP_JOB_HISTORY` 用于展示各租户 Job 级数据备份的历史信息。

[TABLE]

## CDB_OB_BACKUP_TASKS

`oceanbase.CDB_OB_BACKUP_TASKS` 用于展示各租户 Task 级数据备份任务的进度。

[TABLE]

## CDB_OB_BACKUP_TASK_HISTORY

`oceanbase.CDB_OB_BACKUP_TASK_HISTORY` 用于展示各租户 Task 级数据备份任务的历史信息。

[TABLE]

## CDB_OB_BACKUP_SET_FILES

`oceanbase.CDB_OB_BACKUP_SET_FILES` 用于展示各租户备份集信息。

[TABLE]
