---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_HIST_SNAP_ERROR.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_HIST_SNAP_ERROR` displays information about the snapshot error information in the Workload Repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table in which the error occurred |
| `ERROR_NUMBER` | `NUMBER` | `NOT NULL` | Error number for the error encountered |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |