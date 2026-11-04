---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.48 V$LOGFILE

`V$LOGFILE` contains information about redo log files.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP#` | `NUMBER` | Redo log group identifier number |
| `STATUS` | `VARCHAR2(7)` | Status of the log member:  - `INVALID` - File is inaccessible - `STALE` - File's contents are incomplete - `DELETED` - File is no longer used - null - File is in use |
| `TYPE` | `VARCHAR2(7)` | Type of the logfile:  - `ONLINE` - `STANDBY` |
| `MEMBER` | `VARCHAR2(513)` | Redo log member name |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | Indicates whether the file was created in the fast recovery area (`YES`) or not (`NO`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |