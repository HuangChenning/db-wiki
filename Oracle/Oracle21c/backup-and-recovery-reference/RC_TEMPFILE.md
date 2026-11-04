---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_TEMPFILE.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists information about all temp files registered in the recovery catalog.

It corresponds to the `V$TEMPFILE` view. A temp file is shown as dropped if its tablespace is dropped.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `CON_ID` | `NUMBER` | The ID of the current container:  - 0: Rows containing data that pertain to the entire multitenant container database (CDB) - 1: Rows containing data that pertains only to the root - n: Where n is the applicable container ID for the rows containing data |
| `PDB_NAME` | `VARCHAR2(30)` | The name of the pluggable database (PDB) in the recovery catalog. |
| `PDB_KEY` | `NUMBER` | The primary key for the PDB in the recovery catalog. |
| `TS#` | `NUMBER` | The tablespace ID in the target database. The `TS#` may exist multiple times in the same incarnation if the tablespace is dropped and re-created. |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | The tablespace name. The name may exist multiple times in the same incarnation if the tablespace is dropped and re-created. |
| `FILE#` | `NUMBER` | The absolute file number of the temp file. The same temp file number may exist in the same incarnation of the temp file is dropped and re-created. |
| `CREATION_CHANGE#` | `NUMBER` | The SCN when the temp file is created. |
| `CREATION_TIME` | `DATE` | The time when the temp file is created. |
| `DROP_CHANGE#` | `NUMBER` | The SCN recorded when the temp file was dropped. If a new temp file with the same `FILE#` is discovered, then the `DROP_CHANGE#` is set to `CREATION_CHANGE#` for the temp file; otherwise, the value is set to `RC_CHECKPOINT`.`CKP_SCN`. |
| `DROP_TIME` | `DATE` | The time when the temp file was dropped. If a new temp file with the same `FILE#` is discovered, then the `DROP_TIME` is set to `CREATION_TIME` for the temp file; otherwise the value is `RC_CHECKPOINT`.`CKP_TIME`. |
| `BYTES` | `NUMBER` | The size of the temp file in bytes. |
| `BLOCKS` | `NUMBER` | Size of the file in blocks. |
| `BLOCK_SIZE` | `NUMBER` | The block size of the temp file in bytes. |
| `NAME` | `VARCHAR2(1024)` | The temp file name. |
| `RFILE#` | `NUMBER` | The relative file number of this temp file within the tablespace. |
| `AUTOEXTEND` | `VARCHAR2(3)` | `ON` if the temp file is autoextensible. Otherwise `OFF`. |
| `MAXSIZE` | `NUMBER` | Maximum file size in blocks to which the file can be extended. Valid only when `AUTOEXTEND` is `ON`. Always `0` when `AUTOEXTEND` is `OFF`. |
| `NEXTSIZE` | `NUMBER` | Amount of incremental size for file extensible in blocks. Valid only when `AUTOEXTEND` is `ON`. Always `0` when `AUTOEXTEND` is `OFF`. |
| `BIGFILE` | `VARCHAR2(3)` | `YES` if the tablespace is a bigfile tablespace; otherwise, `NO`. |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with this file. Each database in a Data Guard environment has a unique `SITE_KEY` value. You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |
| `TABLESPACE_CREATION_CHANGE#` | `NUMBER` | SCN at which this tablespace was created. |
| `TABLESPACE_CREATION_TIME` | `DATE` | Timestamp at which this tablespace was created. |
| `TABLESPACE_DROP_CHANGE#` | `NUMBER` | SCN at which this tablespace was dropped. |
| `TABLESPACE_DROP_TIME` | `DATE` | Timestamp at which the tablespace was dropped. |
| `DB_UNIQUE_NAME` | `VARCHAR2(512)` | The `DB_UNIQUE_NAME` of the database incarnation to which this record belongs. All databases in a Data Guard environment share the same DBID but different `DB_UNIQUE_NAME` values. The value in this column is null when the database name is not known for a specific file. For example, rows for databases managed by versions of RMAN before Oracle Database 11g are null. |