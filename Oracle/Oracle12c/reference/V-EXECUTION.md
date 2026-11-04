---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-EXECUTION.html
tags:
  - oracle
  - 12c
  - reference
---

| Column | Datatype | Description |
| --- | --- | --- |
| `PID` | `NUMBER` | Session ID |
| `DEPTH` | `NUMBER` | The depth |
| `FUNCTION` | `VARCHAR2(10)` | Session serial number |
| `TYPE` | `VARCHAR2(7)` | Name of the `OBJECT_NODE` in plan table |
| `NVALS` | `NUMBER` | Elapsed time for `OBJECT_NODE` |
| `VAL1` | `NUMBER` | The value for number 1 |
| `VAL2` | `NUMBER` | The value for number 2 |
| `SEQH` | `NUMBER` | A sequence |
| `SEQL` | `NUMBER` | A sequence |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |