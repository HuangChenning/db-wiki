---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-SQL_OPTIMIZER_ENV.html
tags:
  - oracle
  - 12c
  - reference
---

`V$SQL_OPTIMIZER_ENV` displays the contents of the optimizer environment used to build the execution plan of a SQL cursor. This view can be joined with `V$SQLAREA` on (`HASH_VALUE`, `ADDRESS`) and with `V$SQL` on (`HASH_VALUE`, `CHILD_ADDRESS`).

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Address of the parent cursor |
| `HASH_VALUE` | `NUMBER` | Hash value of the parent cursor in the library cache. The hash value is the fixed index for the view and should be used when querying `V$SQL_OPTIMIZER_ENV` to avoid scanning the entire library cache. |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier |
| `CHILD_ADDRESS` | `RAW(4 \| 8)` | Address of the child cursor |
| `CHILD_NUMBER` | `NUMBER` | Child cursor number |
| `ID` | `NUMBER` | Unique identifier of the parameter in the optimizer environment |
| `NAME` | `VARCHAR2(40)` | Name of the parameter |
| `ISDEFAULT` | `VARCHAR2(3)` | Indicates whether the parameter is set to the default value (`YES`) or not (`NO`) |
| `VALUE` | `VARCHAR2(25)` | Value of the parameter |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |