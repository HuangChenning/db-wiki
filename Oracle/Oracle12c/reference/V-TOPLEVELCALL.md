---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-TOPLEVELCALL.html
tags:
  - oracle
  - 12c
  - reference
---

`V$TOPLEVELCALL` displays the mapping between Oracle top level calls and names.

| Column | Datatype | Description |
| --- | --- | --- |
| `TOP_LEVEL_CALL#` | `NUMBER` | Oracle top level call number |
| `TOP_LEVEL_CALL_NAME` | `VARCHAR2(64)` | Oracle top level call name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |