---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-CODE_CLAUSE.html
tags:
  - oracle
  - 12c
  - reference
---

`V$CODE_CLAUSE` contains the supported clause names and parameter names for the Oracle Data Vault `ALTER SYSTEM` and `ALTER SESSION` commands.

| Column | Datatype | Description |
| --- | --- | --- |
| `CODE_ID#` | `NUMBER` | The OCT code ID:  - `42`: For `ALTER SESSION` - `49`: For `ALTER SYSTEM` |
| `CLAUSE_ID#` | `NUMBER` | Clause ID |
| `CLAUSE_NAME` | `VARCHAR2(100)` | The clause name that is supported by the Oracle Data Vault command rule (for example, `SET` or `ADVICE`) |
| `PARAMETER_NAME` | `VARCHAR2(100)` | The parameter name that is supported by the Oracle Data Vault command rule. For example, for `ALTER SYSTEM SET EVENTS`, `EVENTS` is the parameter. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).