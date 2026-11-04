---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUDIT_MGMT_CLEAN_EVENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.168 DBA\_AUDIT\_MGMT\_CLEAN\_EVENTS

`DBA_AUDIT_MGMT_CLEAN_EVENTS` displays information about the history of audit trail cleanup or purge events.

Periodically, you should delete the contents of this view so that it will not grow too large.

Note:

This view is intended for use with traditional auditing (pre-Oracle Database 12c auditing) only, not for unified auditing.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `AUDIT_TRAIL` | `VARCHAR2(28)` |  | Audit trail that was cleaned at the time of the event:  - `STANDARD AUDIT TRAIL` - `FGA AUDIT TRAIL` - `STANDARD AND FGA AUDIT TRAIL` - `OS AUDIT TRAIL` - `XML AUDIT TRAIL` - `OS AND XML AUDIT TRAIL` - `ALL AUDIT TRAILS` |
| `RAC_INSTANCE` | `NUMBER` | `NOT NULL` | Instance number indicating the Oracle RAC instance that was cleaned up at the time of the event; `0` implies not applicable |
| `CLEANUP_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Timestamp when the cleanup event completed |
| `DELETE_COUNT` | `NUMBER` |  | Number of audit records or audit files that were deleted at the time of the event |
| `WAS_FORCED` | `VARCHAR2(3)` |  | Indicates whether a forced cleanup occurred (`YES`) or not (`NO`); forced cleanup bypasses the last archive timestamp set |

Note:

In a read-only database, including an Oracle Active Data Guard physical standby database, this view is not populated. Instead, a summary of cleanup events is written to the respective database instance's alert log file.