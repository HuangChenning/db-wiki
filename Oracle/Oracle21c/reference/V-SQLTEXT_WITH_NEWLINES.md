---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQLTEXT_WITH_NEWLINES.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.79 V$SQLTEXT\_WITH\_NEWLINES

`V$SQLTEXT_WITH_NEWLINES` is identical to the `V$SQLTEXT` view except that, to improve legibility, `V$SQLTEXT_WITH_NEWLINES` does not replace newlines and tabs in the SQL statement with spaces.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Used with `HASH_VALUE` to uniquely identify a cached cursor |
| `HASH_VALUE` | `NUMBER` | Used with `ADDRESS` to uniquely identify a cached cursor |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of a cached cursor |
| `COMMAND_TYPE` | `NUMBER` | Code for the type of SQL statement (`SELECT`, `INSERT`, and so on) |
| `PIECE` | `NUMBER` | Number used to order the pieces of SQL text |
| `SQL_TEXT` | `VARCHAR2(64)` | A column containing one piece of the SQL text |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SQLTEXT](V-SQLTEXT.md) "