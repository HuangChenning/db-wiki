---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_DLM_MISC.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.399 DBA\_HIST\_DLM\_MISC

`DBA_HIST_DLM_MISC` displays miscellaneous Oracle Real Application Clusters (Oracle RAC) statistics.

This view contains snapshots of `V$DLM_MISC`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `STATISTIC#` | `NUMBER` |  | Statistic number |
| `NAME` | `VARCHAR2(38)` |  | Statistic name |
| `VALUE` | `NUMBER` |  | Statistic value |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |