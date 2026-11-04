---
title: "V$DATAFILE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1100.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DATAFILE` displays datafile information from the control file.

See Also:

["V$DATAFILE\_HEADER"](dynviews_1102.md), which displays information from datafile headers

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | File identification number |
| `CREATION_CHANGE#` | `NUMBER` | Change number at which the datafile was created |
| `CREATION_TIME` | `DATE` | Timestamp of the datafile creation |
| `TS#` | `NUMBER` | Tablespace number |
| `RFILE#` | `NUMBER` | Tablespace relative datafile number |
| `STATUS` | `VARCHAR2(7)` | Type of file (system or user) and its status. Values: `OFFLINE`, `ONLINE`, `SYSTEM`, `RECOVER`, `SYSOFF` (an offline file from the `SYSTEM` tablespace) |
| `ENABLED` | `VARCHAR2(10)` | Describes how accessible the file is from SQL: - `DISABLED` - No SQL access allowed - `READ ONLY` - No SQL updates allowed - `READ WRITE` - Full access allowed - `UNKNOWN` - should not occur unless the control file is corrupted |
| `CHECKPOINT_CHANGE#` | `NUMBER` | SCN at last checkpoint |
| `CHECKPOINT_TIME` | `DATE` | Timestamp of the checkpoint# |
| `UNRECOVERABLE_CHANGE#` | `NUMBER` | Last unrecoverable change number made to this datafile. If the database is in `ARCHIVELOG` mode, then this column is updated when an unrecoverable operation completes. If the database is not in `ARCHIVELOG` mode, this column does not get updated. |
| `UNRECOVERABLE_TIME` | `DATE` | Timestamp of the last unrecoverable change. This column is updated only if the database is in `ARCHIVELOG` mode. |
| `LAST_CHANGE#` | `NUMBER` | Last change number made to this datafile (null if the datafile is being changed) |
| `LAST_TIME` | `DATE` | Timestamp of the last change |
| `OFFLINE_CHANGE#` | `NUMBER` | Offline change number of the last offline range. This column is updated only when the datafile is brought online. |
| `ONLINE_CHANGE#` | `NUMBER` | Online change number of the last offline range |
| `ONLINE_TIME` | `DATE` | Online timestamp of the last offline range |
| `BYTES` | `NUMBER` | Current datafile size (in bytes); `0` if inaccessible |
| `BLOCKS` | `NUMBER` | Current datafile size (in blocks); 0 if inaccessible |
| `CREATE_BYTES` | `NUMBER` | Size when created (in bytes) |
| `BLOCK_SIZE` | `NUMBER` | Block size of the datafile |
| `NAME` | `VARCHAR2(513)` | Name of the datafile |
| `PLUGGED_IN` | `NUMBER` | Describes whether the tablespace is plugged in. The value is `1` if the tablespace is plugged in and has not been made read/write, `0` if not. |
| `BLOCK1_OFFSET` | `NUMBER` | Offset from the beginning of the file to where the Oracle generic information begins. The exact length of the file can be computed as follows: `BYTES + BLOCK1_OFFSET`. |
| `AUX_NAME` | `VARCHAR2(513)` | Auxiliary name that has been set for this file via `CONFIGURE AUXNAME` |
| `FIRST_NONLOGGED_SCN` | `NUMBER` | First nonlogged SCN (check in standby database) |
| `FIRST_NONLOGGED_TIME` | `DATE` | First nonlogged time (check in standby database) |
| `FOREIGN_DBID` | `NUMBER` | Foreign DBID from which this data file came from. The value is 0 if this file is not a foreign database file. |
| `FOREIGN_CREATION_CHANGE#` | `NUMBER` | Creation SCN of a foreign datafile. The value is 0 if this file is not a foreign database file. |
| `FOREIGN_CREATION_TIME` | `DATE` | Creation time of a foreign datafile. The value is 0 if this file is not a foreign database file. |
| `PLUGGED_READONLY` | `VARCHAR2(3)` | `YES` if this is a transported read-only foreign file; otherwise `NO`. |
| `PLUGIN_CHANGE#` | `NUMBER` | SCN at which the foreign datafile was transported into the database. The value is 0 if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_CHANGE#` | `NUMBER` | The SCN of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is 0 if this file is not a foreign database file. |
| `PLUGIN_RESETLOGS_TIME` | `DATE` | The time of the `RESETLOGS` operation for the incarnation into which this foreign file was transported. The value is 0 if this file is not a foreign database file. |