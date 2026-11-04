---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_COPY_CORRUPTION.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists corrupt block ranges in data file copies. It corresponds to the `V$COPY_CORRUPTION` view.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `RECID` | `NUMBER` | The record identifier from `V$COPY_CORRUPTION`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The stamp from `V$COPY_CORRUPTION`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `CDF_KEY` | `NUMBER` | The primary key of the data file copy in the recovery catalog. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. Use this column to join with `RC_DATAFILE_COPY`. |
| `COPY_RECID` | `NUMBER` | The `RECID` from `RC_DATAFILE_COPY`. This value is propagated from the control file. |
| `COPY_STAMP` | `NUMBER` | The `STAMP` from `RC_DATAFILE_COPY`. This value is propagated from the control file. |
| `FILE#` | `NUMBER` | The absolute file number of the data file. |
| `CREATION_CHANGE#` | `NUMBER` | The creation SCN of this data file. Because file numbers can be reused, `FILE#` and `CREATION_CHANGE#` are both required to uniquely identify a specified file over the life of the database. |
| `BLOCK#` | `NUMBER` | The block number of the first corrupted block in the file. |
| `BLOCKS` | `NUMBER` | The number of corrupted blocks found beginning with `BLOCK#`. |
| `CORRUPTION_CHANGE#` | `NUMBER` | For media corrupt blocks, this value is zero. For logically corrupt blocks, this value is the lowest SCN in the blocks in this corrupt range. |
| `MARKED_CORRUPT` | `VARCHAR2(3)` | `YES` if this corruption was not previously detected by the database server or `NO` if it was known by the database server. |
| `CORRUPTION_TYPE` | `VARCHAR2(9)` | Same as `RC_DATABASE_BLOCK_CORRUPTION.CORRUPTION_TYPE`. |