---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_HIST_SNAPSHOT_DETAILS.html
tags:
  - oracle
  - 19c
  - reference
---

## 5.59 DBA\_HIST\_SNAPSHOT\_DETAILS

`DBA_HIST_SNAPSHOT_DETAILS` displays table details for snapshots in the Workload Repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `TABLE_ID` | `NUMBER` | `NOT NULL` | Dictionary object ID of the table |
| `TABLE_NAME` | `VARCHAR2(64)` |  | Name of the table |
| `BEGIN_TIME` | `TIMESTAMP(3)` |  | Time at the beginning of the snapshot interval for the table |
| `END_TIME` | `TIMESTAMP(3)` |  | Time at the end of the snapshot interval for the table; the actual time the snapshot was taken |
| `ELAPSED` | `INTERVAL DAY(9) TO SECOND(3)` |  | Amount of time to perform the snapshot for the table |
| `STEP_ID` | `NUMBER` | `NOT NULL` | For internal use only |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 19c, Release Update 19.28.