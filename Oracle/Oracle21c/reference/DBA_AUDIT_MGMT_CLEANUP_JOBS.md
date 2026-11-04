---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUDIT_MGMT_CLEANUP_JOBS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.169 DBA\_AUDIT\_MGMT\_CLEANUP\_JOBS

`DBA_AUDIT_MGMT_CLEANUP_JOBS` displays information about the configured audit trail purge jobs.

Note:

This view is populated in any Oracle Database where auditing is enabled, regardless of whether pre-Oracle Database 12c auditing or unified auditing is enabled for the database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOB_NAME` | `VARCHAR2(100)` | `NOT NULL` | Name of the audit trail purge job |
| `JOB_STATUS` | `VARCHAR2(8)` |  | Current status of the audit trail purge job (`ENABLED`) or (`DISABLED`) |
| `AUDIT_TRAIL` | `VARCHAR2(28)` |  | Audit trail for which the audit trail purge job is configured:  - `STANDARD AUDIT TRAIL` - `FGA AUDIT TRAIL` - `STANDARD AND FGA AUDIT TRAIL` - `OS AUDIT TRAIL` - `XML AUDIT TRAIL` - `OS AND XML AUDIT TRAIL` - `ALL AUDIT TRAILS` - `UNIFIED AUDIT TRAIL` |
| `JOB_FREQUENCY` | `VARCHAR2(100)` |  | Frequency at which the audit trail purge job runs |
| `USE_LAST_ARCHIVE_TIMESTAMP` | `VARCHAR2(3)` |  | Indicates whether the audit trail purge job invocation uses the last archive timestamp. The last archive timestamp is shown in the `LAST_ARCHIVE_TS` column of the `DBA_AUDIT_MGMT_LAST_ARCH_TS` view. Possible values:  - `YES` - Indicates that the audit trail purge job invocation uses the last archive timestamp - `NO` - Indicates that the audit trail purge job invocation does not use the last archive timestamp |
| `JOB_CONTAINER` | `VARCHAR2(7)` |  | In a CDB, indicates whether audit trail purge job will be performed only in the current container or in all the containers. Possible values:  - `CURRENT` - Indicates that audit trail purge job will be performed only in the current container - `ALL` - Indicates that audit trail purge job will be performed in all the containers  In a non-CDB, the value in this column is always `CURRENT`. |

See Also:

" [DBA\_AUDIT\_MGMT\_LAST\_ARCH\_TS](DBA_AUDIT_MGMT_LAST_ARCH_TS.md) "