---
title: "V$SPPARAMETER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3042.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SPPARAMETER` displays information about the contents of the server parameter file. If a server parameter file was not used to start the instance, then each row of the view will contain `FALSE` in the `ISSPECIFIED` column.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `VARCHAR2(80)` | SID for which the parameter is defined |
| `NAME` | `VARCHAR2(80)` | Name of the parameter |
| `TYPE` | `VARCHAR2(11)` | Parameter type |
| `VALUE` | `VARCHAR2(255)` | Parameter value (null if a server parameter file was not used to start the instance) |
| `DISPLAY_VALUE` | `VARCHAR2(255)` | Parameter value in a user-friendly format. For example, if the `VALUE` column shows the value `262144` for a big integer parameter, then the `DISPLAY_VALUE` column will show the value `256K`. |
| `ISSPECIFIED` | `VARCHAR2(6)` | Indicates whether the parameter was specified in the server parameter file (`TRUE`) or not (`FALSE`) |
| `ORDINAL` | `NUMBER` | Position (ordinal number) of the parameter value (`0` if a server parameter file was not used to start the instance). Useful only for parameters whose values are lists of strings. |
| `UPDATE_COMMENT` | `VARCHAR2(255)` | Comments associated with the most recent update (null if a server parameter file was not used to start the instance) |