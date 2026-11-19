---
title: "清理备份相关视图介绍"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701925.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 清理备份相关视图介绍

## CDB_OB_BACKUP_DELETE_JOBS

系统租户可通过该视图查看所有租户正在执行的备份清理任务的进展。

[TABLE]

## DBA_OB_BACKUP_DELETE_JOBS

用户租户可通过该视图查看所在租户正在执行的备份清理任务的进展。

[TABLE]

## CDB_OB_BACKUP_DELETE_JOB_HISTORY

系统租户可通过该视图查看所有租户已结束的备份清理任务的历史信息。

[TABLE]

## DBA_OB_BACKUP_DELETE_JOB_HISTORY

用户租户可通过该视图查看所在租户已结束的备份清理任务的历史信息。

[TABLE]

## CDB_OB_BACKUP_DELETE_TASKS

系统租户可通过该视图查看所有租户正在执行的`backup_set/backup_piece`备份清理任务的进展。

[TABLE]

## DBA_OB_BACKUP_DELETE_TASKS

用户租户可通过该视图查看所在租户正在执行的 `backup_set/backup_piece` 备份清理任务的进展。

[TABLE]

## CDB_OB_BACKUP_DELETE_TASK_HISTORY

系统租户可通过该视图查看所有租户已执行完成的 `backup_set/backup_piece` 备份清理任务历史信息。

[TABLE]

## DBA_OB_BACKUP_DELETE_TASK_HISTORY

用户租户可通过该视图查看所在租户已执行完成的 `backup_set/backup_piece` 备份清理任务的历史信息。

[TABLE]

## CDB_OB_BACKUP_DELETE_POLICY

系统租户可通过该视图查看所有租户正在生效的备份清理策略信息。

| 字段            | 描述           |
|-----------------|----------------|
| TENANT_ID       | 租户 ID        |
| POLICY_NAME     | 清理策略名     |
| RECOVERY_WINDOW | 可恢复时间窗口 |

## DBA_OB_BACKUP_DELETE_POLICY

用户租户可通过该视图查看正在生效的备份清理策略信息。

- MySQL 模式

  | 字段            | 描述                         |
  |-----------------|------------------------------|
  | POLICY_NAME     | 清理策略名                   |
  | RECOVERY_WINDOW | 可恢复时间窗口，默认值为 `0` |

- Oracle 模式

  | 字段            | 描述                         |
  |-----------------|------------------------------|
  | POLICY_NAME     | 清理策略名                   |
  | RECOVERY_WINDOW | 可恢复时间窗口，默认值为 `0` |
