---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-SQLTEXT.html
tags:
  - oracle
  - 12c
  - reference
---

`V$SQLTEXT` displays the text of SQL statements belonging to shared SQL cursors in the SGA.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Used with `HASH_VALUE` to uniquely identify a cached cursor |
| `HASH_VALUE` | `NUMBER` | Used with `ADDRESS` to uniquely identify a cached cursor |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of a cached cursor |
| `COMMAND_TYPE` | `NUMBER` | Code for the type of SQL statement (`SELECT`, `INSERT`, and so on) |
| `PIECE` | `NUMBER` | Number used to order the pieces of SQL text |
| `SQL_TEXT` | `VARCHAR2(64)` | A column containing one piece of the SQL text |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |