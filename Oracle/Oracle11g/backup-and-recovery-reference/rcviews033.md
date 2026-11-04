---
title: RC_OFFLINE_RANGE
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews033.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

This view lists the offline ranges for data files. It corresponds to the `V$OFFLINE_RANGE` view.

An offline range is created for a data file when its tablespace is first altered to be offline normal or read-only, and then subsequently altered to be online or read/write. No offline range is created if the data file itself is altered to be offline or if the tablespace is altered to be offline immediate.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `RECID` | `NUMBER` | The record identifier for the offline range from `V$OFFLINE_RANGE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The stamp for the offline range from `V$OFFLINE_RANGE`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `FILE#` | `NUMBER` | The absolute file number of the data file. |
| `CREATION_CHANGE#` | `NUMBER` | The SCN at data file creation. |
| `OFFLINE_CHANGE#` | `NUMBER` | The SCN taken when the data file was taken offline. |
| `ONLINE_CHANGE#` | `NUMBER` | The online checkpoint SCN. |
| `ONLINE_TIME` | `DATE` | The online checkpoint time. |
| `CF_CREATE_TIME` | `DATE` | The time of control file creation. |