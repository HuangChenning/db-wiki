---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DATAFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.157 V$DATAFILE

`V$DATAFILE` displays datafile information from the control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | Absolute file number |
| `CREATION_CHANGE#` | `NUMBER` | Change number at which the data file was created |
| `CREATION_TIME` | `DATE` | Timestamp of the data file creation |
| `TS#` | `NUMBER` | Tablespace number |
| `RFILE#` | `NUMBER` | Tablespace relative data file number |
| `STATUS` | `VARCHAR2(7)` | Type of file (system or user) and its status. Values: `OFFLINE`, `ONLINE`, `SYSTEM`, `RECOVER`, `SYSOFF` (an offline file from the `SYSTEM` tablespace) |
| `ENABLED` | `VARCHAR2(10)` | Describes how accessible the file is from SQL:  - `DISABLED` - No SQL access allowed. The tablespace might be offline. - `READ ONLY` - No SQL updates allowed - `READ WRITE` - Full access allowed - `UNKNOWN` - Unknown whether SQL updates would be allowed or not |
| `CHECKPOINT_CHANGE#` | `NUMBER` | SCN at last checkpoint |
| `CHECKPOINT_TIME` | `DATE` | Timestamp of the checkpoint# |
| `UNRECOVERABLE_CHANGE#` | `NUMBER` | Last unrecoverable change number made to this data file. If the database is in `ARCHIVELOG` mode, then this column is updated when an unrecoverable operation completes. If the database is not in `ARCHIVELOG` mode, this column does not get updated. |
| `UNRECOVERABLE_TIME` | `DATE` | Timestamp of the last unrecoverable change. This column is updated only if the database is in `ARCHIVELOG` mode. |
| `LAST_CHANGE#` | `NUMBER` | Last change number made to this data file (null if the data file is being changed) |
| `LAST_TIME` | `DATE` | Timestamp of the last change |
| `OFFLINE_CHANGE#` | `NUMBER` | Offline change number of the last offline range. This column is updated only when the data file is brought online. |
| `ONLINE_CHANGE#` | `NUMBER` | Online change number of the last offline range |
| `ONLINE_TIME` | `DATE` | Online timestamp of the last offline range |
| `BYTES` | `NUMBER` | Current data file size (in bytes); `0` if inaccessible |
| `BLOCKS` | `NUMBER` | Current data file size (in blocks); 0 if inaccessible |
| `CREATE_BYTES` | `NUMBER` | Size when created (in bytes) |
| `BLOCK_SIZE` | `NUMBER` | Block size of the data file |
| `NAME` | `VARCHAR2(513)` | Name of the data file |
| `PLUGGED_IN` | `NUMBER` | Describes whether the tablespace is plugged in. The value is `1` if the tablespace is plugged in and has not been made read/write, `0` if not. |
| `BLOCK1_OFFSET` | `NUMBER` | Offset from the beginning of the file to where the Oracle generic information begins. The exact length of the file can be computed as follows: `BYTES + BLOCK1_OFFSET`. |
| `AUX_NAME` | `VARCHAR2(513)` | Auxiliary name that has been set for this file via `CONFIGURE AUXNAME` |
| `FIRST_NONLOGGED_SCN` | `NUMBER` | First nonlogged SCN (check in standby database) |
| `FIRST_NONLOGGED_TIME` | `DATE` | First nonlogged time (check in standby database) |
| `FOREIGN_DBID` | `NUMBER` | Foreign DBID from which this data file came from. The value is 0 if this file is not a foreign database file. |
| `FOREIGN_CREATION_CHANGE#` | `NUMBER` | Creation SCN of a foreign data file. The value is 0 if this file is not a foreign database file. |
| `FOREIGN_CREATION_TIME` | `DATE` | Creation time of a foreign data file. The value is 0 if this file is not a foreign database file. |
| `PLUGGED_READONLY` | `VARCHAR2(3)` | `YES` if this is a transported read-only foreign file; otherwise `NO`. |
| `PLUGIN_CHANGE#` | `NUMBER` | SCN at which the foreign data file was transported into the database. The value is 0 if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is 0 if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_TIME` | `DATE` | The time of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is 0 if this file is not a foreign database file. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |