---
title: ALL_AUDIT_POLICY_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1021.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_AUDIT_POLICY_COLUMNS` describes the fine-grained auditing policy columns on the tables and views accessible to the current user.

Related Views

- `DBA_AUDIT_POLICY_COLUMNS` describes all fine-grained auditing policy columns in the database.
- `USER_AUDIT_POLICY_COLUMNS` describes the fine-grained auditing policy columns on the tables and views owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_SCHEMA` | `VARCHAR2(30)` |  | Owner of the table or view |
| `OBJECT_NAME` | `VARCHAR2(30)` |  | Name of the table or view |
| `POLICY_NAME` | `VARCHAR2(30)` |  | Name of the policy |
| `POLICY_COLUMN` | `VARCHAR2(30)` |  | Relevant column of the policy |

See Also:

- ["DBA\_AUDIT\_POLICY\_COLUMNS"](statviews_3078.md)
- ["USER\_AUDIT\_POLICY\_COLUMNS"](statviews_5234.md)