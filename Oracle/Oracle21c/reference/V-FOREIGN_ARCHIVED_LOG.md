---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FOREIGN_ARCHIVED_LOG.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.240 V$FOREIGN\_ARCHIVED\_LOG

`V$FOREIGN_ARCHIVED_LOG` can be queried on a logical standby database to find out the list of foreign archived logs received by a database.

No rows are returned for this view on a physical standby database.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Archived log record ID |
| `STAMP` | `NUMBER` | Archived log record stamp |
| `NAME` | `VARCHAR2(513)` | Archived log file name. If set to NULL, either the log file was cleared before it was archived or an RMAN `BACKUP` command with the `delete input` option was executed to back up archivelog all (`RMAN> backup archivelog all delete input;`). |
| `DEST_ID` | `NUMBER` | Original destination from which the archive log was generated. The value is 0 if the destination identifier is not available |
| `THREAD#` | `NUMBER` | Redo thread number |
| `SEQUENCE#` | `NUMBER` | Redo log sequence number |
| `RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs change number of the database when the log was written |
| `RESETLOGS_TIME` | `DATE` | Resetlogs time of the database when the log was written |
| `RESETLOGS_ID` | `NUMBER` | Resetlogs identifier associated with the archived redo log |
| `FIRST_CHANGE#` | `NUMBER` | First change number in the archived log |
| `FIRST_TIME` | `DATE` | Timestamp of the first change |
| `NEXT_CHANGE#` | `NUMBER` | First change in the next log |
| `NEXT_TIME` | `DATE` | Timestamp of the next change |
| `BLOCKS` | `NUMBER` | Size of the archived log (in blocks) |
| `BLOCK_SIZE` | `NUMBER` | Redo log block size. This is the logical block size of the archived log, which is the same as the logical block size of the online log from which the archived log was copied. The online log logical block size is a platform-specific value that is not adjustable by the user. |
| `CREATOR` | `VARCHAR2(7)` | Creator of the archive log:  ARCH - Archiver process  FGRD - Foreground process  RMAN - Recovery Manager  SRMN - RMAN at standby  LGWR - Logwriter process |
| `REGISTRAR` | `VARCHAR2(7)` | Registrar of the entry:  RFS - Remote File Server process  ARCH - Archiver process  FGRD - Foreground process  RMAN - Recovery Manager  SRMN - RMAN at standby  LGWR - Logwriter process |
| `ARCHIVED` | `VARCHAR2(3)` | Indicates whether the online redo log was archived (`YES`) or whether RMAN only inspected the log and created a record for future application of redo logs during recovery (`NO`). |
| `APPLIED` | `VARCHAR2(3)` | Indicates whether the archivelog has been applied to its corresponding standby database (`YES`) or not (`NO`). The value is always `NO` for local destinations.  This column is meaningful at the standby site for the `ARCHIVED_LOG` entries with `REGISTRAR='RFS'` (which means this log is shipped from the primary to the standby database). If `REGISTRAR='RFS' ` and `APPLIED` is `NO`, then the log has arrived at the standby but has not yet been applied. If `REGISTRAR='RFS'` and `APPLIED` is `YES`, the log has arrived and been applied at the standby database.  You can use this field to identify archivelogs that can be backed up and removed from disk. |
| `DELETED` | `VARCHAR2(3)` | Indicates whether an RMAN `DELETE` command has physically deleted the archived log file from disk, as well as logically removing it from the control file of the target database and from the recovery catalog (`YES`) or not (`NO`) |
| `STATUS` | `VARCHAR2(1)` | Status of the archived log:  A - Available  D - Deleted  U - Unavailable  X - Expired |
| `COMPLETION_TIME` | `DATE` | Time when the archiving completed |
| `DICTIONARY_BEGIN` | `VARCHAR2(3)` | Indicates whether the log contains the start of a LogMiner dictionary (`YES`) or not (`NO`) |
| `DICTIONARY_END` | `VARCHAR2(3)` | Indicates whether the log contains the end of a LogMiner dictionary (`YES`) or not (`NO`) |
| `END_OF_REDO` | `VARCHAR2(3)` | Indicates whether the archived redo log contains the end of all redo information from the primary database () or not () |
| `ARCHIVAL_THREAD#` | `NUMBER` | Redo thread number of the instance that performed the archival operation. This column differs from the `THREAD#` column only when a closed thread is archived by another instance. |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | Indicates whether the file was created in the fast recovery area (`YES`) or not (`NO`) |
| `COMPRESSED` | `VARCHAR2(3)` | Reserved for internal use |
| `FAL` | `VARCHAR2(3)` | Indicates whether the archive log was generated as the result of a FAL request (`YES`) or not (`NO`) |
| `END_OF_REDO_TYPE` | `VARCHAR2(10)` | Possible values are as follows:  SWITCHOVER - Shows archived redo log files that are produced at the end of a switchover  TERMINAL - Shows archived redo log files produced after a failover  RESETLOGS - Shows online redo log files archived on the primary database after an `ALTER DATABASE OPEN RESETLOGS` statement is issued  ACTIVATION - Shows any log files archived on a physical standby database after an `ALTER DATABASE ACTIVATE STANDBY DATABASE` statement is issued  "empty string" - Any empty string implies that the log is just a normal archival and was not archived due to any of the other events |
| `SOURCE_DBID` | `NUMBER` | Database ID of the source database that generated this archived log |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |