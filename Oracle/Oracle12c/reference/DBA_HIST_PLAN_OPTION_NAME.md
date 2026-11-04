---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_HIST_PLAN_OPTION_NAME.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_HIST_PLAN_OPTION_NAME` displays historical information about SQL plan option names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database identifier |
| `OPTION_ID` | `NUMBER` | `NOT NULL` | Plan option identifier |
| `OPTION_NAME` | `VARCHAR2(64)` |  | Plan option name. This value also appears in the `SQL_PLAN_OPTIONS` column of the `DBA_HIST_ACTIVE_SESS_HISTORY` view. |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |