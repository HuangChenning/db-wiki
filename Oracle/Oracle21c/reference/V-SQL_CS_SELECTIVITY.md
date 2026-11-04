---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_CS_SELECTIVITY.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.51 V$SQL\_CS\_SELECTIVITY

A valid range consists of a low and high value for each predicate containing binds. Each predicate's selectivity (with the current bind value) must fall between the corresponding low and high values in order for the child cursor to be shared.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Address of the handle to the parent for this cursor |
| `HASH_VALUE` | `NUMBER` | Hash value of the parent statement in the library cache |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the parent cursor in the library cache |
| `CHILD_NUMBER` | `NUMBER` | Number of the child cursor |
| `PREDICATE` | `VARCHAR2(40)` | Predicate whose selectivity must fall between low and high values |
| `RANGE_ID` | `NUMBER` | Identifier for the range used to match up the low and high values for multiple predicates |
| `LOW` | `VARCHAR2(10)` | Lower bound for allowable selectivity |
| `HIGH` | `VARCHAR2(10)` | Upper bound for allowable selectivity |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |