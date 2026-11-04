---
title: ALL_RULE_SET_RULES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2027.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_RULE_SET_RULES` describes the rules in the rule sets accessible to the current user.

Related Views

- `DBA_RULE_SET_RULES` describes the rules in all rule sets in the database.
- `USER_RULE_SET_RULES` describes the rules in the rule sets owned by the current user. This view does not display the `RULE_SET_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_SET_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the rule set |
| `RULE_SET_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rule set |
| `RULE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rule |
| `RULE_SET_RULE_ENABLED` | `VARCHAR2(8)` |  | Indicates whether the rule is enabled in the rule set (`ENABLED`) or not (`DISABLED`) |
| `RULE_SET_RULE_EVAL_CTX_OWNER` | `VARCHAR2(30)` |  | Owner of the evaluation context specified when the rule was added to the rule set, if any |
| `RULE_SET_RULE_EVAL_CTX_NAME` | `VARCHAR2(30)` |  | Name of the evaluation context specified when the rule was added to the rule set, if any |
| `RULE_SET_RULE_COMMENT` | `VARCHAR2(4000)` |  | Comment specified when the rule was added to the rule set, if any |

See Also:

- ["DBA\_RULE\_SET\_RULES"](statviews_4231.md)
- ["USER\_RULE\_SET\_RULES"](statviews_5419.md)