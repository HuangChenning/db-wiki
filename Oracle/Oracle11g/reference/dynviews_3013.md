---
title: "V$SES_OPTIMIZER_ENV"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3013.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SES_OPTIMIZER_ENV` displays the contents of the optimizer environment used by each session. When a new session is first created, it automatically inherits its optimizer environment from the optimizer environment defined at the instance level by `V$SYS_OPTIMIZER_ENV`. The value of certain parameters can be dynamically modified by issuing an `ALTER SESSION` statement.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier. This column can be used to join with `V$SESSION` on the `SID` column. |
| `ID` | `NUMBER` | Unique identifier of the parameter in the optimizer environment |
| `NAME` | `VARCHAR2(40)` | Name of the parameter |
| `SQL_FEATURE` | `VARCHAR2(64)` | Associated feature control ID |
| `ISDEFAULT` | `VARCHAR2(3)` | Indicates whether the parameter is set to the default value (`YES`) or not (`NO`) |
| `VALUE` | `VARCHAR2(25)` | Value of the parameter for the session |

See Also:

["V$SYS\_OPTIMIZER\_ENV"](dynviews_3087.md)