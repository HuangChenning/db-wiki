---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_AUDIT_STATEMENT.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_AUDIT_STATEMENT` displays audit trail entries for the `GRANT`, `REVOKE`, `AUDIT`, `NOAUDIT`, and `ALTER SYSTEM` statements issued by the current user.

Its columns are the same as those in " [DBA\_AUDIT\_STATEMENT](DBA_AUDIT_STATEMENT.md) ".

Note:

This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from `UNIFIED_AUDIT_TRAIL`.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=UPGRD52810) for more information about migrating to unified auditing.