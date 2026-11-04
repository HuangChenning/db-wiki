---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-FIXED_VIEW_DEFINITION.html
tags:
  - oracle
  - 12c
  - reference
---

`V$FIXED_VIEW_DEFINITION` contains the definitions of all the fixed views (views beginning with `V$`).

Use this table with caution. Oracle tries to keep the behavior of fixed views the same from release to release, but the definitions of the fixed views can change without notice. Use these definitions to optimize your queries by using indexed columns of the dynamic performance tables.

| Column | Datatype | Description |
| --- | --- | --- |
| `VIEW_NAME` | `VARCHAR2(128)` | Name of the fixed view |
| `VIEW_DEFINITION` | `VARCHAR2(4000)` | Definition of the fixed view |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |