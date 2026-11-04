---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_RULE_SET_RULES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.33 ALL\_RULE\_SET\_RULES

`ALL_RULE_SET_RULES` describes the rules in the rule sets accessible to the current user.

Related Views

- `DBA_RULE_SET_RULES` describes the rules in all rule sets in the database.
- `USER_RULE_SET_RULES` describes the rules in the rule sets owned by the current user. This view does not display the `RULE_SET_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_SET_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the rule set |
| `RULE_SET_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the rule set |
| `RULE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the rule |
| `RULE_SET_RULE_ENABLED` | `VARCHAR2(8)` |  | Indicates whether the rule is enabled in the rule set (`ENABLED`) or not (`DISABLED`) |
| `RULE_SET_RULE_EVAL_CTX_OWNER` | `VARCHAR2(128)` |  | Owner of the evaluation context specified when the rule was added to the rule set, if any |
| `RULE_SET_RULE_EVAL_CTX_NAME` | `VARCHAR2(128)` |  | Name of the evaluation context specified when the rule was added to the rule set, if any |
| `RULE_SET_RULE_COMMENT` | `VARCHAR2(4000)` |  | Comment specified when the rule was added to the rule set, if any |

See Also:

- " [DBA\_RULE\_SET\_RULES](DBA_RULE_SET_RULES.md) "
- " [USER\_RULE\_SET\_RULES](USER_RULE_SET_RULES.md) "