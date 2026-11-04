---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AW_ALLOCATE_OP.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.77 V$AW\_ALLOCATE\_OP

`V$AW_ALLOCATE_OP` displays the allocation operators available in analytic workspaces. You can use this view in an application to provide a list of choices.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(14)` | Keyword for the allocation operator |
| `LONGNAME` | `VARCHAR2(30)` | Descriptive name for the operator |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |