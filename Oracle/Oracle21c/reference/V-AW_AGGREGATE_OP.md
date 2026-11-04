---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AW_AGGREGATE_OP.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.76 V$AW\_AGGREGATE\_OP

`V$AW_AGGREGATE_OP` displays the aggregation operators available in analytic workspaces. You can use this view in an application to provide a list of choices.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(14)` | Keyword for the aggregation operator |
| `LONGNAME` | `VARCHAR2(30)` | Descriptive name for the operator |
| `DEFAULT_WEIGHT` | `NUMBER` | Default weight factor for weighted operators |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |