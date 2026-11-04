---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_REPLICATION_TXN_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.32 DBA\_HIST\_REPLICATION\_TXN\_STATS

`DBA_HIST_REPLICATION_TXN_STATS` displays replication transaction statistics for Oracle GoldenGate and XStream sessions.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Object name |
| `SESSION_TYPE` | `VARCHAR2(64)` | `NOT NULL` | Type of session |
| `SESSION_MODULE` | `VARCHAR2(64)` | `NOT NULL` | Session module. Valid values:  - XStream - GoldenGate |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | Database where the transaction originated |
| `SOURCE_TXN_ID` | `VARCHAR2(128)` | `NOT NULL` | Original transaction ID at the source database |
| `FIRST_LCR_TIME` | `DATE` |  | Time of the first LCR (message in an error transaction) |
| `TOTAL_LCRS_COUNT` | `NUMBER` |  | Total number of LCRs for this replication transaction |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |