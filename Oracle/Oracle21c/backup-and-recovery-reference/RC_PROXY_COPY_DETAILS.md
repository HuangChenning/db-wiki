---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_PROXY_COPY_DETAILS.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

`RC_PROXY_COPY_DETAILS` contains detailed information about proxy copy backups for databases registered in the recovery catalog.

This view is primarily intended to be used internally by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `SESSION_KEY` | `NUMBER` | Session identifier. Use in joins with `RC_RMAN_OUTPUT` and `RC_RMAN_BACKUP_JOB_DETAILS`. |
| `SESSION_RECID` | `NUMBER` | With `SESSION_STAMP`, uniquely identifies output for this proxy copy operation from `RC_RMAN_OUTPUT`. |
| `SESSION_STAMP` | `NUMBER` | With `SESSION_RECID`, uniquely identifies output for this proxy copy operation from `RC_RMAN_OUTPUT`. |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `RSR_KEY` | `NUMBER` | Unique key for the row in `RC_RMAN_STATUS` corresponding to the job that created this proxy copy. |
| `COPY_KEY` | `NUMBER` | Unique identifier for this proxy copy. |
| `FILE#` | `NUMBER` | The absolute file number of the data file that is proxy copied. |
| `HANDLE` | `VARCHAR2(1024)` | The proxy copy handle identifies the copy for purposes of restore operations. |