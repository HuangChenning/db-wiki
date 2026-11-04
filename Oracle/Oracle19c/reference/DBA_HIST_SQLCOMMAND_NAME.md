---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_HIST_SQLCOMMAND_NAME.html
tags:
  - oracle
  - 19c
  - reference
---

## 5.65 DBA\_HIST\_SQLCOMMAND\_NAME

`DBA_HIST_SQLCOMMAND_NAME` displays the mapping between SQL opcodes and names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `COMMAND_TYPE` | `NUMBER` | `NOT NULL` | SQL command number |
| `COMMAND_NAME` | `VARCHAR2(64)` |  | SQL command name |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |