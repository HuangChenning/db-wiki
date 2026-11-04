---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_UNIFIED_AUDIT_ACTIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.134 ALL\_UNIFIED\_AUDIT\_ACTIONS

The actions described in this view are valid for audit trail records from the `UNIFIED_AUDIT_TRAIL` view. Such records are generated only when unified auditing is enabled.

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TYPE` | `NUMBER` | `NOT NULL` | Numeric component type for system wide actions |
| `COMPONENT` | `VARCHAR2(64)` | `NOT NULL` | Name of component for system wide actions |
| `ACTION` | `NUMBER` | `NOT NULL` | Numeric auditable action code for system wide actions  Note: The action code values have changed from Oracle Database release 12.2 to the current release. If your applications have queries that include the `ACTION` column, and if these queries were written in release 12.2, then be aware that the output may be different if you are running these queries in the current release. |
| `NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of auditable action |

See Also:

" [UNIFIED\_AUDIT\_TRAIL](UNIFIED_AUDIT_TRAIL.md) "