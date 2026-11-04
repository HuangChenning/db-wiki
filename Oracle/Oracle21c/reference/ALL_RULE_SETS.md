---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_RULE_SETS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.34 ALL\_RULE\_SETS

`ALL_RULE_SETS` describes the rule sets accessible to the current user.

Related Views

- `DBA_RULE_SETS` describes all rule sets in the database.
- `USER_RULE_SETS` describes the rule sets owned by the current user. This view does not display the `RULE_SET_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_SET_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the rule set |
| `RULE_SET_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the rule set |
| `RULE_SET_EVAL_CONTEXT_OWNER` | `VARCHAR2(128)` |  | Owner of the evaluation context associated with the rule set, if any |
| `RULE_SET_EVAL_CONTEXT_NAME` | `VARCHAR2(128)` |  | Name of the evaluation context associated with the rule set, if any |
| `RULE_SET_COMMENT` | `VARCHAR2(4000)` |  | Comment specified with the rule set, if any |

See Also:

- " [DBA\_RULE\_SETS](DBA_RULE_SETS.md) "
- " [USER\_RULE\_SETS](USER_RULE_SETS.md) "