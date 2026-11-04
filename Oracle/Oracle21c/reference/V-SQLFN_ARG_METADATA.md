---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQLFN_ARG_METADATA.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.74 V$SQLFN\_ARG\_METADATA

There is one row for each argument of every function found in `V$SQLFN_METADATA`. There are no rows for functions that do not have any arguments.

| Column | Datatype | Description |
| --- | --- | --- |
| `FUNC_ID` | `NUMBER` | Internal function identification number. This column can be used to join with the `V$SQLFN_METADATA` view. |
| `ARGNUM` | `NUMBER` | Argument number |
| `DATATYPE` | `VARCHAR2(8)` | Data type of the argument. The value is NULL if this argument is not used. Otherwise, it can take values of any Oracle data type, family data type, or EXPR data type. |
| `DESCR` | `VARCHAR2(128)` | This column is reserved for future use. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SQLFN\_METADATA](V-SQLFN_METADATA.md) "