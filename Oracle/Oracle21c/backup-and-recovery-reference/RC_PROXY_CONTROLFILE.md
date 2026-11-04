---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_PROXY_CONTROLFILE.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view contains descriptions of control file backups that were taken using the proxy copy functionality. It corresponds to the `V$PROXY_DATAFILE` view.

In a proxy copy, the media manager takes over the operations of backing up and restoring data. Each row represents a backup of one control file.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `XCF_KEY` | `NUMBER` | The proxy copy primary key in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `RECID` | `NUMBER` | The proxy copy record identifier from `V$PROXY_DATAFILE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The proxy copy stamp from `V$PROXY_DATAFILE`.`RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `TAG` | `VARCHAR2(32)` | The tag for the proxy copy. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The `RESETLOGS` SCN of the database incarnation to which this data file belongs. |
| `RESETLOGS_TIME` | `DATE` | The `RESETLOGS` time stamp of the database incarnation to which this data file belongs. |
| `CHECKPOINT_CHANGE#` | `NUMBER` | Data file checkpoint SCN when this copy was made. |
| `CHECKPOINT_TIME` | `DATE` | Data file checkpoint time when this copy was made. |
| `CREATION_TIME` | `DATE` | The control file creation time. |
| `BLOCK_SIZE` | `NUMBER` | The block size for the copy in bytes. |
| `BLOCKS` | `NUMBER` | The number of blocks in the copy. |
| `MIN_OFFR_RECID` | `NUMBER` | Internal use only. |
| `OLDEST_OFFLINE_RANGE` | `NUMBER` | Internal use only. |
| `DEVICE_TYPE` | `VARCHAR2(255)` | The type of sequential media device. |
| `HANDLE` | `VARCHAR2(1024)` | The name or "handle" for the proxy copy. RMAN passes this value to the operating system-dependent layer that identifies the file. |