---
title: ALL_RULES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2029.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_RULES` describes the rules accessible to the current user.

Related Views

- `DBA_RULES` describes all rules in the database.
- `USER_RULES` describes the rules owned by the current user. This view does not display the `RULE_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rule |
| `RULE_CONDITION` | `CLOB` |  | Expressions and operators that constitute the rule condition |
| `RULE_EVALUATION_CONTEXT_OWNER` | `VARCHAR2(30)` |  | Owner of the evaluation context associated with the rule, if any |
| `RULE_EVALUATION_CONTEXT_NAME` | `VARCHAR2(30)` |  | Name of the evaluation context associated with the rule, if any |
| `RULE_ACTION_CONTEXT` | `RE$NV_LIST` |  | Action context associated with the rule, if any |
| `RULE_COMMENT` | `VARCHAR2(4000)` |  | Comment specified with the rule, if any |

See Also:

- ["DBA\_RULES"](statviews_4233.md)
- ["USER\_RULES"](statviews_5421.md)