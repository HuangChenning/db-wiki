---
title: ALL_APPLY_EXECUTE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1011.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_APPLY_EXECUTE` displays information about the apply execute actions for the rules visible to the current user.

Related View

`DBA_APPLY_EXECUTE` displays information about the apply execute actions for all rules in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rule |
| `EXECUTE_EVENT` | `VARCHAR2(2)` |  | Indicates whether the event satisfying the rule is executed |

See Also:

["DBA\_APPLY\_EXECUTE"](statviews_3054.md)