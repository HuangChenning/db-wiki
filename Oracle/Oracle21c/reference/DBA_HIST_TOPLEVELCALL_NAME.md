---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_TOPLEVELCALL_NAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.82 DBA\_HIST\_TOPLEVELCALL\_NAME

`DBA_HIST_TOPLEVELCALL_NAME` displays the mapping between Oracle top level calls and names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `TOP_LEVEL_CALL#` | `NUMBER` | `NOT NULL` | Oracle top level call number |
| `TOP_LEVEL_CALL_NAME` | `VARCHAR2(64)` |  | Oracle top level call name |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |