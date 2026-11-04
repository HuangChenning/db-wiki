---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_AUDIT_POLICY_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.112 ALL\_AUDIT\_POLICY\_COLUMNS

`ALL_AUDIT_POLICY_COLUMNS` describes the fine-grained auditing policy columns on the tables and views accessible to the current user.

Related Views

- `DBA_AUDIT_POLICY_COLUMNS` describes all fine-grained auditing policy columns in the database.
- `USER_AUDIT_POLICY_COLUMNS` describes the fine-grained auditing policy columns on the tables and views owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_SCHEMA` | `VARCHAR2(128)` |  | Owner of the table or view |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the table or view |
| `POLICY_NAME` | `VARCHAR2(128)` |  | Name of the policy |
| `POLICY_COLUMN` | `VARCHAR2(128)` |  | Relevant column of the policy |

See Also:

- " [DBA\_AUDIT\_POLICY\_COLUMNS](DBA_AUDIT_POLICY_COLUMNS.md) "
- " [USER\_AUDIT\_POLICY\_COLUMNS](USER_AUDIT_POLICY_COLUMNS.md) "