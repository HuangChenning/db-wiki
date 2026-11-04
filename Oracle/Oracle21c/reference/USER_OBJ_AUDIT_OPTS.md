---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_OBJ_AUDIT_OPTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.586 USER\_OBJ\_AUDIT\_OPTS

`USER_OBJ_AUDIT_OPTS` describes auditing options on all objects owned by the current user. Its columns (except for `OWNER`) are the same as those in `DBA_OBJ_AUDIT_OPTS`.

Note:

This view is relevant when using traditional auditing. Traditional auditing is deprecated in Oracle Database 21c. Oracle recommends that you instead use unified auditing, which enables selective and more effective auditing inside Oracle Database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from `UNIFIED_AUDIT_TRAIL`.

See Also:

" [DBA\_OBJ\_AUDIT\_OPTS](DBA_OBJ_AUDIT_OPTS.md) "