---
title: DBA_AUTOTASK_WINDOW_CLIENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3091.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_AUTOTASK_WINDOW_CLIENTS` displays the windows that belong to `MAINTENANCE_WINDOW_GROUP`, along with the Enabled or Disabled status for the window for each maintenance task. Primarily used by Enterprise Manager.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WINDOW_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the maintenance window |
| `WINDOW_NEXT_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Next scheduled window open time unless the window is disabled |
| `WINDOW_ACTIVE` | `VARCHAR2(5)` |  | Indicates whether the window is currently active (open) (`TRUE`) or not (`FALSE`) |
| `AUTOTASK_STATUS` | `VARCHAR2(8)` |  | Status of the automated maintenance task subsystem: |
| `OPTIMIZER_STATS` | `VARCHAR2(8)` |  | Status of optimizer statistics gathering: |
| `SEGMENT_ADVISOR` | `VARCHAR2(8)` |  | Status of Segment Advisor: |
| `SQL_TUNE_ADVISOR` | `VARCHAR2(8)` |  | Status of SQL Tuning Advisor: |
| `HEALTH_MONITOR` | `VARCHAR2(8)` |  | Status of Health Monitor: |