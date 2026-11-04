---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/AUDIT_UNIFIED_CONTEXTS.html
tags:
  - oracle
  - 12c
  - reference
---

`AUDIT_UNIFIED_CONTEXTS` describes the application context's attributes, which are configured to be captured in the audit trail.

Note:

This view is populated only in an Oracle Database where unified auditing is enabled.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(128)` |  | Application context namespace |
| `ATTRIBUTE` | `VARCHAR2(128)` |  | Application context attribute |
| `USER_NAME` | `VARCHAR2(128)` |  | Username of database user for whom the application context's attribute is confiured to be captured in the audit trail |