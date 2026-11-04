---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RECOVERY_FILE_STATUS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.159 V$RECOVERY\_FILE\_STATUS

This view contains useful information only for the Oracle process doing the recovery. When Recovery Manager directs a server process to perform recovery, only Recovery Manager can view the relevant information in this view. `V$RECOVERY_FILE_STATUS` will be empty to all other Oracle users.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILENUM` | `NUMBER` | Number of the file being recovered |
| `FILENAME` | `VARCHAR2(513)` | Filename of the datafile being recovered |
| `STATUS` | `VARCHAR2(13)` | Status of the recovery:  - `IN RECOVERY` - `CURRENT` - `NOT RECOVERED` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=BRADV90026)