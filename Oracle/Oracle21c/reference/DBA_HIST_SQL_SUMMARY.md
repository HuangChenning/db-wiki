---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SQL_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.61 DBA\_HIST\_SQL\_SUMMARY

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `TOTAL_SQL` | `NUMBER` | `NOT NULL` | Total number of SQLs |
| `TOTAL_SQL_MEM` | `NUMBER` | `NOT NULL` | Total sharable memory in bytes for SQLs |
| `SINGLE_USE_SQL` | `NUMBER` | `NOT NULL` | Total number of single execution SQLs |
| `SINGLE_USE_SQL_MEM` | `NUMBER` | `NOT NULL` | Total sharable memory in bytes for single execution SQLs |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |