---
title: ALL_RULE_SETS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2028.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_RULE_SETS` describes the rule sets accessible to the current user.

Related Views

- `DBA_RULE_SETS` describes all rule sets in the database.
- `USER_RULE_SETS` describes the rule sets owned by the current user. This view does not display the `RULE_SET_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_SET_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the rule set |
| `RULE_SET_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rule set |
| `RULE_SET_EVAL_CONTEXT_OWNER` | `VARCHAR2(30)` |  | Owner of the evaluation context associated with the rule set, if any |
| `RULE_SET_EVAL_CONTEXT_NAME` | `VARCHAR2(30)` |  | Name of the evaluation context associated with the rule set, if any |
| `RULE_SET_COMMENT` | `VARCHAR2(4000)` |  | Comment specified with the rule set, if any |

See Also:

- ["DBA\_RULE\_SETS"](statviews_4232.md)
- ["USER\_RULE\_SETS"](statviews_5420.md)