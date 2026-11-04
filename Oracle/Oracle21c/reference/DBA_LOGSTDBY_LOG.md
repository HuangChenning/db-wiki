---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_LOGSTDBY_LOG.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.162 DBA\_LOGSTDBY\_LOG

`DBA_LOGSTDBY_LOG` displays information about the logs registered for a logical standby database.

This view is for logical standby databases only.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `THREAD#` | `NUMBER` | `NOT NULL` | Thread ID of the archive log. The THREAD number is `1` for a single instance. For Real Application Clusters, this column will contain different numbers. |
| `RESETLOGS_CHANGE#` | `NUMBER` | `NOT NULL` | Start SCN of the branch |
| `RESETLOGS_ID` | `NUMBER` | `NOT NULL` | Resetlogs identifier (a numeric form of the timestamp of the branch) |
| `SEQUENCE#` | `NUMBER` | `NOT NULL` | Sequence number of the archive log file |
| `FIRST_CHANGE#` | `NUMBER` | `NOT NULL` | System change number (SCN) of the current archive log |
| `NEXT_CHANGE#` | `NUMBER` |  | SCN of the next archive log |
| `FIRST_TIME` | `DATE` |  | Date of the current archive log |
| `NEXT_TIME` | `DATE` |  | Date of the next archive log |
| `FILE_NAME` | `VARCHAR2(513)` |  | Name of the archive log |
| `TIMESTAMP` | `DATE` |  | Time when the archive log was registered |
| `DICT_BEGIN` | `VARCHAR2(3)` |  | Indicates whether the beginning of the dictionary build is in this archive log (`YES`) or not (`NO`) |
| `DICT_END` | `VARCHAR2(3)` |  | Indicates whether the end of the dictionary build is in this archive log (`YES`) or not (`NO`) |
| `APPLIED` | `VARCHAR2(8)` |  | Indicates primarily whether a given foreign archived log has been applied fully by SQL Apply:  - `YES` - SQL Apply has fully applied the foreign archived log and no longer needs it - `CURRENT` - SQL Apply is currently applying changes contained in the foreign archived log - `NO` - SQL Apply has not started applying any changes contained in the foreign archived log - `FETCHING` - SQL Apply encountered a corruption while reading redo records from this foreign archived log, and is currently using the automatic gap resolution to refetch a new copy of the log from the primary database - `CORRUPT` - SQL Apply encountered a corruption while reading redo records from this foreign archived log, and refetching a new copy of the archived log did not resolve the problem. SQL Apply will not refetch a new copy of this archived log automatically, and will require user intervention to manually register a new copy of the foreign archived log. |
| `BLOCKS` | `NUMBER` |  | Number of blocks in the log |
| `BLOCK_SIZE` | `NUMBER` |  | Size of each block in the log |

Note:

The SCN values in this view correlate to the SCN values shown in the `DBA_LOGSTDBY_PROGRESS` view.

Note:

In a CDB, this view shows data only when queried in the root.