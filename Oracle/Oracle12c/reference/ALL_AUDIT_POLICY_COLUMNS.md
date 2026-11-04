---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_AUDIT_POLICY_COLUMNS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_AUDIT_POLICY_COLUMNS` describes the fine-grained auditing policy columns on the tables and views accessible to the current user.

Note:

This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from `UNIFIED_AUDIT_TRAIL`.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

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