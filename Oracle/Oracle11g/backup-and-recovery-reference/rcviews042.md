---
title: RC_REDO_THREAD
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews042.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

This view lists data about all redo threads for all incarnations of the database since the last catalog resynchronization. This view corresponds to `V$THREAD`.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `THREAD#` | `NUMBER` | The redo thread number for the database incarnation. |
| `STATUS` | `VARCHAR2(1)` | The status of the redo thread: `D` (disabled), `E` (enabled), or `O` (open). |
| `SEQUENCE#` | `NUMBER` | The last allocated log sequence number. |
| `ENABLE_CHANGE#` | `NUMBER` | The SCN at which this thread was enabled. |
| `ENABLE_TIME` | `DATE` | The time at which this thread was enabled. |
| `DISABLE_CHANGE#` | `NUMBER` | The most recent SCN at which this thread was disabled. If the thread is still disabled, then no redo at or beyond this SCN exists for this thread. If the thread is now enabled, then no redo exists between the `DISABLE_CHANGE#` and the `ENABLE_CHANGE#` for this thread. |
| `DISABLE_TIME` | `DATE` | The most recent time at which this thread was disabled. |