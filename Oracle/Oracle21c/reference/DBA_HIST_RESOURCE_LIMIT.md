---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_RESOURCE_LIMIT.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.37 DBA\_HIST\_RESOURCE\_LIMIT

`DBA_HIST_RESOURCE_LIMIT` displays historical information about global resource use for some of the system resource.

This view contains snapshots of `V$RESOURCE_LIMIT`.

If time is of interest, join this view with `DBA_HIST_SNAPSHOT.END_INTERVAL_TIME`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `RESOURCE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the resource |
| `CURRENT_UTILIZATION` | `NUMBER` |  | Number of (resources, locks, or processes) currently being used |
| `MAX_UTILIZATION` | `NUMBER` |  | Maximum consumption of the resource since the last instance start up |
| `INITIAL_ALLOCATION` | `VARCHAR2(10)` |  | Initial allocation. This will be equal to the value specified for the resource in the initialization parameter file (`UNLIMITED` for infinite allocation). |
| `LIMIT_VALUE` | `VARCHAR2(10)` |  | Unlimited for resources and locks. This can be greater than the initial allocation value (`UNLIMITED` for infinite limit). |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |