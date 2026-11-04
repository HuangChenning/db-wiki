---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_OBJ_AUDIT_OPTS.html
tags:
  - oracle
  - 12c
  - reference
---

`USER_OBJ_AUDIT_OPTS` describes auditing options on all objects owned by the current user. Its columns (except for `OWNER`) are the same as those in `DBA_OBJ_AUDIT_OPTS`.

Note:

This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from `UNIFIED_AUDIT_TRAIL`.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

See Also:

" [DBA\_OBJ\_AUDIT\_OPTS](DBA_OBJ_AUDIT_OPTS.md) "