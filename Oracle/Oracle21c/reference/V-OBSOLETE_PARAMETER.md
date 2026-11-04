---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-OBSOLETE_PARAMETER.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.98 V$OBSOLETE\_PARAMETER

If any row of the view contains `TRUE` in the `ISSPECIFIED` column, then you should examine why.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(64)` | Name of the parameter |
| `ISSPECIFIED` | `VARCHAR2(5)` | Indicates whether the parameter was specified in the parameter file (`TRUE`) or not (`FALSE`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |