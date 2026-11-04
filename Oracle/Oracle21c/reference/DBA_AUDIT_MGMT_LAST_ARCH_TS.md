---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUDIT_MGMT_LAST_ARCH_TS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.171 DBA\_AUDIT\_MGMT\_LAST\_ARCH\_TS

`DBA_AUDIT_MGMT_LAST_ARCH_TS` displays information about the last archive timestamps set for audit trail cleanup or purges.

Note:

This view is populated in any Oracle Database where auditing is enabled, regardless of whether pre-Oracle Database 12c auditing or unified auditing is enabled for the database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `AUDIT_TRAIL` | `VARCHAR2(20)` |  | Audit trail for which the last archive timestamp applies:  - `STANDARD AUDIT TRAIL` - `FGA AUDIT TRAIL` - `OS AUDIT TRAIL` - `XML AUDIT TRAIL` - `UNIFIED AUDIT TRAIL` |
| `RAC_INSTANCE` | `NUMBER` | `NOT NULL` | Oracle RAC instance number for which the last archive timestamp applies; `0` implies not applicable |
| `LAST_ARCHIVE_TS` | `TIMESTAMP(6) WITH TIME ZONE` |  | Timestamp of the last audit record or audit file that has been archived |
| `DATABASE_ID` | `NUMBER` | `NOT NULL` | Database ID of the audit records to clean up |
| `CONTAINER_GUID` | `VARCHAR2(33)` | `NOT NULL` | GUID of the container of the audit records to clean up |

Note:

In a read-only database, including an Oracle Active Data Guard physical standby database, this view is not populated when `DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP` is invoked. In such a case, use `DBMS_AUDIT_MGMT.GET_LAST_ARCHIVE_TIMESTAMP` to check for the timestamp, if it was configured for the database instance.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS65409) for more information about `DBMS_AUDIT_MGMT` subprograms