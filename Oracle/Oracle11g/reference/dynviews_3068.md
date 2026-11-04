---
title: "V$SQLFN_METADATA"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3068.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQLFN_METADATA` contains metadata about operators and built-in functions. Note that this view does not contain information about arguments because the number of arguments will be different for various functions. Information about arguments is contained in `V$SQLFN_ARG_METADATA`, which can be joined with `V$SQLFN_METADATA` to get information about any function and its arguments.

| Column | Datatype | Description |
| --- | --- | --- |
| `FUNC_ID` | `NUMBER` | Internal function identification number |
| `NAME` | `VARCHAR2(30)` | Name of the built-in function |
| `MINARGS` | `NUMBER` | Minimum number of arguments for the function |
| `MAXARGS` | `NUMBER` | Maximum number of arguments for the function |
| `DATATYPE` | `VARCHAR2(8)` | Return datatype, which can take any Oracle datatype values, datatype family values, or ARG\[n\] datatypes |
| `VERSION` | `VARCHAR2(12)` | Minimum version of the database that has this function |
| `ANALYTIC` | `VARCHAR2(3)` | Indicates whether the function is an analytic function (`YES`) or not (`NO`) |
| `AGGREGATE` | `VARCHAR2(3)` | Indicates whether the function is an aggregate function (`YES`) or not (`NO`) |
| `OFFLOADABLE` | `VARCHAR2(3)` | Indicates whether execution of the function can be offloaded to the Oracle Exadata Storage Server (`YES`) or not (`NO`)  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `DISP_TYPE` | `VARCHAR2(13)` | Function display type: |
| `USAGE` | `VARCHAR2(30)` | A text explanation of how to use this function. The text is based on the syntax diagram for the function in the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm). |
| `DESCR` | `VARCHAR2(4000)` | Description of the function |