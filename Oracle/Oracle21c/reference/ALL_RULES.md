---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_RULES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.35 ALL\_RULES

`ALL_RULES` describes the rules accessible to the current user.

Related Views

- `DBA_RULES` describes all rules in the database.
- `USER_RULES` describes the rules owned by the current user. This view does not display the `RULE_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the rule |
| `RULE_CONDITION` | `CLOB` |  | Expressions and operators that constitute the rule condition |
| `RULE_EVALUATION_CONTEXT_OWNER` | `VARCHAR2(128)` |  | Owner of the evaluation context associated with the rule, if any |
| `RULE_EVALUATION_CONTEXT_NAME` | `VARCHAR2(128)` |  | Name of the evaluation context associated with the rule, if any |
| `RULE_ACTION_CONTEXT` | `RE$NV_LIST` |  | Action context associated with the rule, if any |
| `RULE_COMMENT` | `VARCHAR2(4000)` |  | Comment specified with the rule, if any |

See Also:

- " [DBA\_RULES](DBA_RULES.md) "
- " [USER\_RULES](USER_RULES.md) "