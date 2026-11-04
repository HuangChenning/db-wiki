---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-RESULT_CACHE_DEPENDENCY.html
tags:
  - oracle
  - 12c
  - reference
---

`V$RESULT_CACHE_DEPENDENCY` displays the depends-on relationship between cached results and dependencies.

| Column | Datatype | Description |
| --- | --- | --- |
| `RESULT_ID` | `NUMBER` | Cached result |
| `DEPEND_ID` | `NUMBER` | Dependency object |
| `OBJECT_NO` | `NUMBER` | Dictionary object number of the dependency object |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |