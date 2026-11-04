---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTOTASK_WINDOW_CLIENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.203 DBA\_AUTOTASK\_WINDOW\_CLIENTS

`DBA_AUTOTASK_WINDOW_CLIENTS` displays the windows that belong to `MAINTENANCE_WINDOW_GROUP`, along with the Enabled or Disabled status for the window for each maintenance task.

`DBA_AUTOTASK_WINDOW_CLIENTS` is primarily used by Enterprise Manager.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WINDOW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the maintenance window |
| `WINDOW_NEXT_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Next scheduled window open time unless the window is disabled |
| `WINDOW_ACTIVE` | `VARCHAR2(5)` |  | Indicates whether the window is currently active (open) (`TRUE`) or not (`FALSE`) |
| `AUTOTASK_STATUS` | `VARCHAR2(8)` |  | Status of the automated maintenance task subsystem:  - `ENABLED` - `DISABLED` |
| `OPTIMIZER_STATS` | `VARCHAR2(8)` |  | Status of optimizer statistics gathering:  - `ENABLED` - `DISABLED` |
| `SEGMENT_ADVISOR` | `VARCHAR2(8)` |  | Status of Segment Advisor:  - `ENABLED` - `DISABLED` |
| `SQL_TUNE_ADVISOR` | `VARCHAR2(8)` |  | Status of SQL Tuning Advisor:  - `ENABLED` - `DISABLED` |