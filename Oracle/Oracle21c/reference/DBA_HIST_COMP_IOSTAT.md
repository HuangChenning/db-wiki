---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_COMP_IOSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.387 DBA\_HIST\_COMP\_IOSTAT

`DBA_HIST_COMP_IOSTAT` displays information about I/O statistics aggregated on the component level.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `COMPONENT` | `VARCHAR2(64)` | `NOT NULL` | Component name |
| `FILE_TYPE` | `VARCHAR2(64)` | `NOT NULL` | File type |
| `IO_TYPE` | `CHAR(5)` | `NOT NULL` | The type of I/O performed |
| `OPERATION` | `CHAR(5)` | `NOT NULL` | Operation name |
| `BYTES` | `NUMBER` | `NOT NULL` | Number of bytes |
| `IO_COUNT` | `NUMBER` | `NOT NULL` | Number of I/Os that were performed |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |