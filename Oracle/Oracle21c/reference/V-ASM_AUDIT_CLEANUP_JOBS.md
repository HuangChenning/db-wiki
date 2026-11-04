---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_AUDIT_CLEANUP_JOBS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.51 V$ASM\_AUDIT\_CLEANUP\_JOBS

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_AUDIT_CLEANUP_JOBS` displays information about the configured audit trail purge jobs.

In a database instance, `V$ASM_AUDIT_CLEANUP_JOBS` displays no rows.

| Column | Datatype | Description |
| --- | --- | --- |
| `JOB_NAME` | `VARCHAR2(64)` | Name of the audit trail purge job |
| `JOB_STATUS` | `VARCHAR2(64)` | Current status of the audit trail purge job (`ENABLED`) or (`DISABLED`) |
| `AUDIT_TRAIL` | `VARCHAR2(64)` | Audit trail for which the audit trail purge job is configured: `OS AUDIT TRAIL` and `UNIFIED AUDIT TRAIL` |
| `JOB_FREQUENCY` | `NUMBER` | Frequency at which the audit trail purge job runs |
| `USE_TIMESTAMP` | `VARCHAR2(64)` | Indicates whether the audit trail purge job is configured to use the last archive timestamp (`TRUE`) or not (`FALSE`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |