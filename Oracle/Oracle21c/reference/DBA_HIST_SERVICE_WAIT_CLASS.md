---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SERVICE_WAIT_CLASS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.48 DBA\_HIST\_SERVICE\_WAIT\_CLASS

`DBA_HIST_SERVICE_WAIT_CLASS` displays the history of wait class information for services as tracked by the Workload Repository.

This view contains information from `V$SERVICE_WAIT_CLASS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `SERVICE_NAME_HASH` | `NUMBER` | `NOT NULL` | Hash of the service name |
| `SERVICE_NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the service |
| `WAIT_CLASS_ID` | `NUMBER` | `NOT NULL` | Identifier for the class of the wait event |
| `WAIT_CLASS` | `VARCHAR2(64)` |  | Name for the class of the wait event |
| `TOTAL_WAITS` | `NUMBER` |  | Total number of waits for this event |
| `TIME_WAITED` | `NUMBER` |  | Total amount of time waited for this event (in hundredths of a second) |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SERVICE\_WAIT\_CLASS](V-SERVICE_WAIT_CLASS.md) "