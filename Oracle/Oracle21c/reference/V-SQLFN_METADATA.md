---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQLFN_METADATA.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.75 V$SQLFN\_METADATA

Note that this view does not contain information about arguments because the number of arguments will be different for various functions. Information about arguments is contained in `V$SQLFN_ARG_METADATA`, which can be joined with `V$SQLFN_METADATA` to get information about any function and its arguments.

| Column | Datatype | Description |
| --- | --- | --- |
| `FUNC_ID` | `NUMBER` | Internal function identification number |
| `NAME` | `VARCHAR2(128)` | Name of the built-in function |
| `MINARGS` | `NUMBER` | Minimum number of arguments for the function |
| `MAXARGS` | `NUMBER` | Maximum number of arguments for the function |
| `DATATYPE` | `VARCHAR2(8)` | Return data type, which can take any Oracle data type values, data type family values, or ARG\[n\] data types |
| `VERSION` | `VARCHAR2(12)` | Minimum version of the database that has this function |
| `ANALYTIC` | `VARCHAR2(3)` | Indicates whether the function is an analytic function (`YES`) or not (`NO`) |
| `AGGREGATE` | `VARCHAR2(3)` | Indicates whether the function is an aggregate function (`YES`) or not (`NO`) |
| `OFFLOADABLE` | `VARCHAR2(3)` | Indicates whether execution of the function can be offloaded to the Oracle Exadata Storage Server (`YES`) or not (`NO`)  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `DISP_TYPE` | `VARCHAR2(13)` | Function display type:  - NORMAL - ARITHMETIC - PARENTHESIS - REL-OP - CASELIKE - NOPARENTHESIS |
| `USAGE` | `VARCHAR2(128)` | A text explanation of how to use this function. The text is based on the syntax diagram for the function in the [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF006). |
| `DESCR` | `VARCHAR2(4000)` | Description of the function |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SQLFN\_ARG\_METADATA](V-SQLFN_ARG_METADATA.md) "