---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/STMT_AUDIT_OPTION_MAP.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.247 STMT\_AUDIT\_OPTION\_MAP

`STMT_AUDIT_OPTION_MAP` describes auditing option type codes. This table can be used to map auditing option type numbers to type names.

Note:

This view is populated in any Oracle Database where auditing is enabled, regardless of whether pre-Oracle Database 12c auditing or unified auditing is enabled for the database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

Note:

The mapping explained in this view is valid for audit configuration from the `DBA_STMT_AUDIT_OPTS` view only, and such audit configurations can be made when unified auditing is not enabled.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OPTION#` | `NUMBER` | `NOT NULL` | Numeric auditing option type code |
| `NAME` | `VARCHAR2(40)` | `NOT NULL` | Name of the type of auditing option |
| `PROPERTY` | `NUMBER` | `NOT NULL` | Property flag of the auditing option |

See Also:

" [DBA\_STMT\_AUDIT\_OPTS](DBA_STMT_AUDIT_OPTS.md) "