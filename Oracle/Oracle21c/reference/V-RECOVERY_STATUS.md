---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RECOVERY_STATUS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.163 V$RECOVERY\_STATUS

This view contains useful information only for the Oracle process doing the recovery. When Recovery Manager directs a server process to perform recovery, only Recovery Manager can view the relevant information in this view. `V$RECOVERY_STATUS` will be empty to all other Oracle users.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECOVERY_CHECKPOINT` | `DATE` | Point in time to which the recovery has occurred. If no logs have been applied, this is the point in time the recovery starts. |
| `THREAD` | `NUMBER` | Number of the redo thread currently being processed |
| `SEQUENCE_NEEDED` | `NUMBER` | Log sequence number of the log needed by the recovery process. The value is `0` if no log is needed. |
| `SCN_NEEDED` | `VARCHAR2(16)` | Low SCN of the log needed by recovery. The value is `0` if unknown or no log is needed. |
| `TIME_NEEDED` | `DATE` | Time when the log was created. The value is midnight on 1/1/88 if the time is unknown or if no log is needed. |
| `PREVIOUS_LOG_NAME` | `VARCHAR2(513)` | Filename of the log |
| `PREVIOUS_LOG_STATUS` | `VARCHAR2(13)` | Status of the previous log. Contains one of the following values: `RELEASE; WRONG NAME; MISSING NAME; UNNEEDED NAME; NONE` |
| `REASON` | `VARCHAR2(13)` | Reason recovery is returning control to the user (`NEED LOG\|LOG REUSED\|THREAD DISABLED`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=BRADV90026)