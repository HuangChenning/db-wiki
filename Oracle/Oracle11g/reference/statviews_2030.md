---
title: ALL_SCHEDULER_CHAIN_RULES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2030.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_CHAIN_RULES` displays information about the rules for the chains accessible to the current user (that is, those chains that the user has `ALTER` or `EXECUTE` privileges for).

Related Views

- `DBA_SCHEDULER_CHAIN_RULES` displays information about the rules for all chains in the database.
- `USER_SCHEDULER_CHAIN_RULES` displays information about the rules for the chains owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the Scheduler chain that the rule is in |
| `CHAIN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the Scheduler chain that the rule is in |
| `RULE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(30)` |  | Name of the rule |
| `CONDITION` | `VARCHAR2(4000)` |  | Boolean condition triggering the rule |
| `ACTION` | `VARCHAR2(4000)` |  | Action to be performed when the rule is triggered |
| `COMMENTS` | `VARCHAR2(4000)` |  | User-specified comments about the rule |

See Also:

- ["DBA\_SCHEDULER\_CHAIN\_RULES"](statviews_4234.md)
- ["USER\_SCHEDULER\_CHAIN\_RULES"](statviews_5422.md)