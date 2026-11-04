---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/AUDIT_ACTIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.173 AUDIT\_ACTIONS

`AUDIT_ACTIONS` describes audit trail action type codes. This table can be used to map action type numbers to action type names.

Note:

The mapping explained in this view is valid for audit trail records from the following views only, and such audit records are generated only when unified auditing is not enabled:

- `DBA_AUDIT_TRAIL`
- `DBA_COMMON_AUDIT_TRAIL`
- `DBA_FGA_AUDIT_TRAIL`
- `USER_AUDIT_TRAIL`
- `V$XML_AUDIT_TRAIL`

Note:

This view is relevant when using traditional auditing. Traditional auditing is deprecated in Oracle Database 21c. Oracle recommends that you instead use unified auditing, which enables selective and more effective auditing inside Oracle Database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ACTION` | `NUMBER` | `NOT NULL` | Numeric audit trail action type code. |
| `NAME` | `VARCHAR2(28)` | `NOT NULL` | Name of the type of audit trail action |