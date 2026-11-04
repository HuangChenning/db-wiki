---
title: ALL_POLICY_GROUPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2012.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_POLICY_GROUPS` describes the policy groups defined for the synonyms, tables, and views accessible to the current user.

Related Views

- `DBA_POLICY_GROUPS` describes all policy groups in the database.
- `USER_POLICY_GROUPS` describes the policy groups defined for the synonyms, tables, and views owned by the current user. This view does not display the `OBJECT_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the synonym, table, or view |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the synonym, table, or view |
| `POLICY_GROUP` | `VARCHAR2(30)` | `NOT NULL` | Name of the policy group |

See Also:

- ["DBA\_POLICY\_GROUPS"](statviews_4184.md)
- ["USER\_POLICY\_GROUPS"](statviews_5399.md)