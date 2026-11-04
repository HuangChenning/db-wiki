---
title: ALL_POLICY_CONTEXTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2011.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_POLICY_CONTEXTS` describes the driving contexts defined for the synonyms, tables, and views accessible to the current user.

Related Views

- `DBA_POLICY_CONTEXTS` describes all driving contexts in the database.
- `USER_POLICY_CONTEXTS` describes the driving contexts defined for the synonyms, tables, and views owned by the current user. This view does not display the `OBJECT_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the synonym, table, or view |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the synonym, table, or view |
| `NAMESPACE` | `VARCHAR2(30)` | `NOT NULL` | Namespace of the driving context |
| `ATTRIBUTE` | `VARCHAR2(30)` | `NOT NULL` | Attribute of the driving context |

See Also:

- ["DBA\_POLICY\_CONTEXTS"](statviews_4183.md)
- ["USER\_POLICY\_CONTEXTS"](statviews_5398.md)