---
title: "物理恢复相关视图介绍"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577563.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 物理恢复相关视图介绍

OceanBase 数据库支持通过各视图查看恢复的进度与结果。

## CDB_OB_RESTORE_PROGRESS

[CDB_OB_RESTORE_PROGRESS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002014725) 用于展示各租户恢复的进度。

## DBA_OB_RESTORE_PROGRESS

`DBA_OB_RESTORE_PROGRESS` 用于展示正在进行的恢复任务。

- 系统租户请参见 [DBA_OB_RESTORE_PROGRESS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002014690) 。

- Oracle 租户请参见 [DBA_OB_RESTORE_PROGRESS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002014372) 。

- MySQL 租户请参见 [DBA_OB_RESTORE_PROGRESS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015296) 。

## CDB_OB_RESTORE_HISTORY

[CDB_OB_RESTORE_HISTORY](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002014803) 用于展示各租户的恢复结果。

## DBA_OB_RESTORE_HISTORY

`DBA_OB_RESTORE_HISTORY` 用于展示已完成的恢复任务。

- 系统租户请参见 [DBA_OB_RESTORE_HISTORY](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002014622)。

- Oracle 租户请参见 [DBA_OB_RESTORE_HISTORY](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002014319)。

- MySQL 租户请参见 [DBA_OB_RESTORE_HISTORY](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015262)。

## DBA_OB_TENANTS

`DBA_OB_TENANTS` 用于展示租户的基本信息，其中有 `RESTORE_DATA_MODE` 列为物理恢复相关信息。

- 系统租户请参见 [DBA_OB_TENANTS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002014776)。

- Oracle 租户请参见 [DBA_OB_TENANTS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002014377)。

- MySQL 租户请参见 [DBA_OB_TENANTS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015192)。
