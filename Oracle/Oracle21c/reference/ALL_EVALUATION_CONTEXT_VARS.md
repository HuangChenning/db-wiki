---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_EVALUATION_CONTEXT_VARS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.186 ALL\_EVALUATION\_CONTEXT\_VARS

`ALL_EVALUATION_CONTEXT_VARS` describes the variables in the rule evaluation contexts accessible to the current user.

Related Views

- `DBA_EVALUATION_CONTEXT_VARS` describes the variables in all rule evaluation contexts in the database.
- `USER_EVALUATION_CONTEXT_VARS` describes the variables in the rule evaluation contexts owned by the current user. This view does not display the `EVALUATION_CONTEXT_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `EVALUATION_CONTEXT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the evaluation context |
| `EVALUATION_CONTEXT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the evaluation context |
| `VARIABLE_NAME` | `VARCHAR2(128)` |  | Name of a variable in the evaluation context |
| `VARIABLE_TYPE` | `VARCHAR2(4000)` |  | Datatype of the variable |
| `VARIABLE_VALUE_FUNCTION` | `VARCHAR2(4000)` |  | Function used to retrieve the value of the variable; NULL for variables that are not implicit |
| `VARIABLE_METHOD_FUNCTION` | `VARCHAR2(228)` |  | Function used to retrieve the result of method invocation on the variable. Such a function can speed up evaluation, if there are many simple rules that invoke the method on the variable. |

See Also:

- " [DBA\_EVALUATION\_CONTEXT\_VARS](DBA_EVALUATION_CONTEXT_VARS.md) "
- " [USER\_EVALUATION\_CONTEXT\_VARS](USER_EVALUATION_CONTEXT_VARS.md) "