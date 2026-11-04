---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_PROCESS_WAITTIME.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.29 DBA\_HIST\_PROCESS\_WAITTIME

`DBA_HIST_PROCESS_WAITTIME` displays CPU and wait time by process types.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `PROCESS_TYPE` | `VARCHAR2(5)` | `NOT NULL` | Process type |
| `DESCRIPTION` | `VARCHAR2(64)` | `NOT NULL` | Process description |
| `WAIT_CLASS_TYPE` | `VARCHAR2(64)` | `NOT NULL` | Type of wait class |
| `VALUE` | `NUMBER` |  | Wait time or CPU used time in milliseconds |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the process |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |