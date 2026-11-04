---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_DATAFILE.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view lists information about all data files registered in the recovery catalog. It corresponds to the `V$DATAFILE` view.

A data file is shown as dropped if its tablespace was dropped.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - 0: Rows containing data that pertain to the entire multitenant container database (CDB) - 1: Rows containing data that pertains only to the root - n: Where n is the applicable container ID for the rows containing data |
| `PDB_NAME` | `VARCHAR2(31)` | Name of the pluggable database (PDB) in the recovery catalog. |
| `PDB_KEY` | `NUMBER` | The primary key for this PDB in the recovery catalog. |
| `PDBINC_KEY` | `NUMBER` | The primary key for the incarnation of the PDB. |
| `TS#` | `NUMBER` | The number of the tablespace to which the data file belongs. The `TS#` may exist multiple times in the same incarnation if the tablespace is dropped and re-created. |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | The tablespace name. The name may exist multiple times in the same incarnation if the tablespace is dropped and re-created. |
| `FILE#` | `NUMBER` | The absolute file number of the data file. The same data file number may exist multiple times in the same incarnation if the data file is dropped and re-created. |
| `CREATION_CHANGE#` | `NUMBER` | The SCN at data file creation. |
| `CREATION_TIME` | `DATE` | The time of data file creation. |
| `DROP_CHANGE#` | `NUMBER` | The SCN recorded when the data file was dropped. If a new data file with the same file number is discovered, then the `DROP_CHANGE#` is set to `CREATION_CHANGE#` for the data file; otherwise the value is set to `RC_CHECKPOINT.CKP_SCN`. |
| `DROP_TIME` | `DATE` | The time when the data file was dropped. If a new data file with the same file number is discovered, then the `DROP_TIME` is set to `CREATION_TIME` for the data file; otherwise the value is set to `RC_CHECKPOINT.CKP_TIME`. |
| `BYTES` | `NUMBER` | The size of the data file in bytes. |
| `BLOCKS` | `NUMBER` | The size of the data file in blocks. |
| `BLOCK_SIZE` | `NUMBER` | The size of the data blocks in bytes. |
| `NAME` | `VARCHAR2(1024)` | The data file name. |
| `STOP_CHANGE#` | `NUMBER` | For offline or read-only data files, the SCN value such that no changes in the redo stream at an equal or greater SCN apply to this file. |
| `STOP_TIME` | `DATE` | For offline normal or read-only data files, the time beyond which there are no changes in the redo stream that apply to this data file. |
| `READ_ONLY` | `NUMBER` | `1` if the file is read-only; otherwise `0`. |
| `RFILE#` | `NUMBER` | The relative file number of this data file within its tablespace. |
| `INCLUDED_IN_DATABASE_BACKUP` | `VARCHAR2(3)` | Indicates whether this tablespace is included in whole database backups: `YES` or `NO`. The `NO` value occurs only if `CONFIGURE EXCLUDE` was run on the tablespace that owns this data file. |
| `AUX_NAME` | `VARCHAR2(1024)` | Indicates the auxiliary name for the data file as set by `CONFIGURE` `AUXNAME`. |
| `ENCRYPT_IN_BACKUP` | `VARCHAR2(3)` | `YES` if this data file has been configured to be transparently encrypted when backed up; otherwise `NULL`. |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with this file. Each database in a Data Guard environment has a unique `SITE_KEY` value. You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |
| `DB_UNIQUE_NAME` | `VARCHAR2(512)` | The `DB_UNIQUE_NAME` of the database incarnation to which this record belongs. All databases in a Data Guard environment share the same DBID but different `DB_UNIQUE_NAME` values. The value in this column is null when the database name is not known for a specific file. For example, rows for databases managed by versions of RMAN before Oracle Database 11g are null. |
| `FOREIGN_DBID` | `NUMBER` | Foreign DBID from which this data file came from. The value is `0` if this file is not a foreign database file. |
| `FOREIGN_CREATION_CHANGE#` | `NUMBER` | Creation SCN of a foreign data file. The value is `0` if this file is not a foreign database file. |
| `FOREIGN_CREATION_TIME` | `DATE` | Creation time of a foreign data file. The value is `0` if this file is not a foreign database file. |
| `PLUGGED_READONLY` | `VARCHAR2(3)` | `YES` if this is a transported read-only foreign file; otherwise `NO`. |
| `PLUGIN_CHANGE#` | `NUMBER` | SCN at which the foreign data file was transported into the database. The value is `0` if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is `0` if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_TIME` | `DATE` | The time of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is `0` if this file is not a foreign database file. |
| `CREATION_THREAD` | `NUMBER` | The thread number of the data file describe by this row. |
| `CREATION_SIZE` | `NUMBER` | The size of the data file at the time of creation. |