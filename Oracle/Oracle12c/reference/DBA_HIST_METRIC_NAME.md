---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_HIST_METRIC_NAME.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_HIST_METRIC_NAME` describes attributes of the set of RDBMS metrics.

This view contains a snapshot of `V$METRICNAME`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `GROUP_ID` | `NUMBER` | `NOT NULL` | Metric Group ID |
| `GROUP_NAME` | `VARCHAR2(64)` |  | Metric group name |
| `METRIC_ID` | `NUMBER` | `NOT NULL` | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` | `NOT NULL` | Metric name |
| `METRIC_UNIT` | `VARCHAR2(64)` | `NOT NULL` | Unit of measurement |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$METRICNAME](V-METRICNAME.md) "