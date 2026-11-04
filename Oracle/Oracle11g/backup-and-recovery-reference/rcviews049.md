---
title: RC_RMAN_OUTPUT
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews049.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

`RC_RMAN_OUTPUT` corresponds to the control file view `V$RMAN_OUTPUT`.

This view is primarily for internal use by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `RSR_KEY` | `NUMBER` | Unique key for the row in `RC_RMAN_STATUS` corresponding to the job that created this output. |
| `SESSION_KEY` | `NUMBER` | Session identifier. Use in joins with `RC_RMAN_OUTPUT` and `RC_RMAN_BACKUP_JOB_DETAILS`. |
| `RECID` | `NUMBER` | Contains the value displayed in `V$RMAN_OUTPUT.RECID` for this database. |
| `STAMP` | `NUMBER` | Stamp (used for ordering) of when the row for this line out output was added. |
| `OUTPUT` | `VARCHAR2(130)` | RMAN output text. |