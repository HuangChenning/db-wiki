---
title: RC_TEMPFILE
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews055.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

This view lists information about all temp files registered in the recovery catalog. It corresponds to the `V$TEMPFILE` view. A temp file is shown as dropped if its tablespace is dropped.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the target database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
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