---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SYSMETRIC_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.72 DBA\_HIST\_SYSMETRIC\_HISTORY

`DBA_HIST_SYSMETRIC_HISTORY` externalizes all available history of the system metric values for the entire set of data kept in the database.

This view contains snapshots of `V$SYSMETRIC_HISTORY`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `BEGIN_TIME` | `DATE` | `NOT NULL` | Begin time of the interval |
| `END_TIME` | `DATE` | `NOT NULL` | End time of the interval |
| `INTSIZE` | `NUMBER` | `NOT NULL` | Interval size (in hundredths of a second) |
| `GROUP_ID` | `NUMBER` | `NOT NULL` | Group ID |
| `METRIC_ID` | `NUMBER` | `NOT NULL` | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` | `NOT NULL` | Metric name |
| `VALUE` | `NUMBER` | `NOT NULL` | Metric Value |
| `METRIC_UNIT` | `VARCHAR2(64)` | `NOT NULL` | Unit of measurement |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |