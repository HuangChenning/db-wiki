---
title: ALL_EVALUATION_CONTEXTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1090.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_EVALUATION_CONTEXTS` describes the rule evaluation contexts accessible to the current user.

Related Views

- `DBA_EVALUATION_CONTEXTS` describes all rule evaluation contexts in the database.
- `USER_EVALUATION_CONTEXTS` describes the rule evaluation contexts owned by the current user. This view does not display the `EVALUATION_CONTEXT_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `EVALUATION_CONTEXT_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the evaluation context |
| `EVALUATION_CONTEXT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the evaluation context |
| `EVALUATION_FUNCTION` | `VARCHAR2(4000)` |  | Evaluation function associated with the evaluation context, if any |
| `EVALUATION_CONTEXT_COMMENT` | `VARCHAR2(4000)` |  | Comment specified with the evaluation context, if any |

See Also:

- ["DBA\_EVALUATION\_CONTEXTS"](statviews_3174.md)
- ["USER\_EVALUATION\_CONTEXTS"](statviews_5300.md)