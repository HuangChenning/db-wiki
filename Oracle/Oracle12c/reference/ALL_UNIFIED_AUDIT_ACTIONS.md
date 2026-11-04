---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_UNIFIED_AUDIT_ACTIONS.html
tags:
  - oracle
  - 12c
  - reference
---

The actions described in this view are valid for audit trail records from the `UNIFIED_AUDIT_TRAIL` view. Such records are generated only when unified auditing is enabled.

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG006) for more information about unified auditing.
- [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TYPE` | `NUMBER` | `NOT NULL` | Numeric component type for system wide actions |
| `COMPONENT` | `VARCHAR2(64)` | `NOT NULL` | Name of component for system wide actions |
| `ACTION` | `NUMBER` | `NOT NULL` | Numeric auditable action code for system wide actions |
| `NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of auditable action |

See Also:

" [UNIFIED\_AUDIT\_TRAIL](UNIFIED_AUDIT_TRAIL.md) "