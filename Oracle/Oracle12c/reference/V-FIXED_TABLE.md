---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-FIXED_TABLE.html
tags:
  - oracle
  - 12c
  - reference
---

`V$FIXED_TABLE` displays all dynamic performance tables, views, and derived tables in the database.

Some `V$` tables (for example, `V$ROLLNAME`) refer to real tables and are therefore not listed.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(128)` | Name of the object |
| `OBJECT_ID` | `NUMBER` | Identifier of the fixed object |
| `TYPE` | `VARCHAR2(5)` | Object type (`TABLE` \| `VIEW`) |
| `TABLE_NUM` | `NUMBER` | Number that identifies the dynamic performance table if it is of type `TABLE` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |