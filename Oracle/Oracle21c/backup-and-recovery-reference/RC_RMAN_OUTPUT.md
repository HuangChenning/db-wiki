---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_RMAN_OUTPUT.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

`RC_RMAN_OUTPUT` corresponds to the control file view `V$RMAN_OUTPUT`. This view is primarily for internal use by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `RSR_KEY` | `NUMBER` | Unique key for the row in `RC_RMAN_STATUS` corresponding to the job that created this output. |
| `SESSION_KEY` | `NUMBER` | Session identifier. Use in joins with `RC_RMAN_OUTPUT` and `RC_RMAN_BACKUP_JOB_DETAILS`. |
| `RECID` | `NUMBER` | Contains the value displayed in `V$RMAN_OUTPUT.RECID` for this database. |
| `STAMP` | `NUMBER` | Stamp (used for ordering) of when the row for this line out output was added. |
| `OUTPUT` | `VARCHAR2(130)` | RMAN output text. |