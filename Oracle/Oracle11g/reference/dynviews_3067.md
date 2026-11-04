---
title: "V$SQLFN_ARG_METADATA"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3067.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQLFN_ARG_METADATA` contains metadata about function arguments. There is one row for each argument of every function found in `V$SQLFN_METADATA`. There are no rows for functions that do not have any arguments.

| Column | Datatype | Description |
| --- | --- | --- |
| `FUNC_ID` | `NUMBER` | Internal function identification number. This column can be used to join with the `V$SQLFN_METADATA` view. |
| `ARGNUM` | `NUMBER` | Argument number |
| `DATATYPE` | `VARCHAR2(8)` | Datatype of the argument. The value is NULL if this argument is not used. Otherwise, it can take values of any Oracle datatype, family datatype, or EXPR datatype. |
| `DESCR` | `VARCHAR2(30)` | This column is reserved for future use. |