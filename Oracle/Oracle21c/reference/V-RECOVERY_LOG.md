---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RECOVERY_LOG.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.160 V$RECOVERY\_LOG

`V$RECOVERY_LOG` lists information about archived logs that are needed to complete media recovery. This information is derived from the log history view, `V$LOG_HISTORY`.

`V$RECOVERY_LOG` contains useful information only for the Oracle process doing the recovery. When Recovery Manager directs a server process to perform recovery, only Recovery Manager can view the relevant information in this view. `V$RECOVERY_LOG` will be empty to all other Oracle users.

| Column | Datatype | Description |
| --- | --- | --- |
| `THREAD#` | `NUMBER` | Thread number of the archived log |
| `SEQUENCE#` | `NUMBER` | Sequence number of the archived log |
| `TIME` | `DATE` | Time of the first entry (lowest SCN) in the log |
| `ARCHIVE_NAME` | `VARCHAR2(513)` | Name of the file when archived, using the naming convention specified by the `LOG_ARCHIVE_FORMAT` initialization parameter  See Also: " [LOG\_ARCHIVE\_FORMAT](LOG_ARCHIVE_FORMAT.md) " |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$LOG\_HISTORY](V-LOG_HISTORY.md) " and [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=BRADV90032)