---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_REPLICATION_TBL_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.31 DBA\_HIST\_REPLICATION\_TBL\_STATS

`DBA_HIST_REPLICATION_TBL_STATS` displays replication table statistics for Oracle GoldenGate and XStream sessions. This view is intended for use with Automatic Workload Repository (AWR).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `APPLY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the apply process |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `SESSION_MODULE` | `VARCHAR2(64)` | `NOT NULL` | Session module. Valid values:  - XStream - GoldenGate |
| `TOTAL_INSERTS` | `NUMBER` |  | Number of insert operations on this table processed by this apply server |
| `TOTAL_UPDATES` | `NUMBER` |  | Number of update operations on this table processed by this apply server |
| `TOTAL_DELETES` | `NUMBER` |  | Number of delete operations on this table processed by this apply server |
| `CDR_SUCCESSFUL` | `NUMBER` |  | Number of successfully resolved conflicts |
| `CDR_FAILED` | `NUMBER` |  | Number of conflicts that could not be resolved due to an error during resolution |
| `REPERR_CNT` | `NUMBER` |  | The total number of errors for the replication operation |
| `HANDLE_COLLISIONS` | `NUMBER` |  | Number of collisions on this table handled by this apply server |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |