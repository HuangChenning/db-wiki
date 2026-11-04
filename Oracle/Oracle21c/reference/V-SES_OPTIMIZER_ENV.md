---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SES_OPTIMIZER_ENV.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.14 V$SES\_OPTIMIZER\_ENV

When a new session is first created, it automatically inherits its optimizer environment from the optimizer environment defined at the instance level by `V$SYS_OPTIMIZER_ENV`. The value of certain parameters can be dynamically modified by issuing an `ALTER SESSION` statement.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier. This column can be used to join with `V$SESSION` on the `SID` column. |
| `ID` | `NUMBER` | Unique identifier of the parameter in the optimizer environment |
| `NAME` | `VARCHAR2(40)` | Name of the parameter |
| `SQL_FEATURE` | `VARCHAR2(64)` | Associated feature control ID |
| `ISDEFAULT` | `VARCHAR2(3)` | Indicates whether the parameter is set to the default value (`YES`) or not (`NO`) |
| `VALUE` | `VARCHAR2(25)` | Value of the parameter for the session |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$SYS\_OPTIMIZER\_ENV](V-SYS_OPTIMIZER_ENV.md) "