---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_EVALUATION_CONTEXTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.187 ALL\_EVALUATION\_CONTEXTS

`ALL_EVALUATION_CONTEXTS` describes the rule evaluation contexts accessible to the current user.

Related Views

- `DBA_EVALUATION_CONTEXTS` describes all rule evaluation contexts in the database.
- `USER_EVALUATION_CONTEXTS` describes the rule evaluation contexts owned by the current user. This view does not display the `EVALUATION_CONTEXT_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `EVALUATION_CONTEXT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the evaluation context |
| `EVALUATION_CONTEXT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the evaluation context |
| `EVALUATION_FUNCTION` | `VARCHAR2(4000)` |  | Evaluation function associated with the evaluation context, if any |
| `EVALUATION_CONTEXT_COMMENT` | `VARCHAR2(4000)` |  | Comment specified with the evaluation context, if any |

See Also:

- " [DBA\_EVALUATION\_CONTEXTS](DBA_EVALUATION_CONTEXTS.md) "
- " [USER\_EVALUATION\_CONTEXTS](USER_EVALUATION_CONTEXTS.md) "