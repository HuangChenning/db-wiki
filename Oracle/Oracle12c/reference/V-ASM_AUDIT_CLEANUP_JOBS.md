---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-ASM_AUDIT_CLEANUP_JOBS.html
tags:
  - oracle
  - 12c
  - reference
---

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_AUDIT_CLEANUP_JOBS` displays information about the configured audit trail purge jobs.

In a database instance, `V$ASM_AUDIT_CLEANUP_JOBS` displays no rows.

| Column | Datatype | Description |
| --- | --- | --- |
| `JOB_NAME` | `VARCHAR2(64)` | Name of the audit trail purge job |
| `JOB_STATUS` | `VARCHAR2(64)` | Current status of the audit trail purge job (`ENABLED`) or (`DISABLED`) |
| `AUDIT_TRAIL` | `VARCHAR2(64)` | Audit trail for which the audit trail purge job is configured: `OS AUDIT TRAIL` and `UNIFIED AUDIT TRAIL` |
| `JOB_FREQUENCY` | `NUMBER` | Frequency at which the audit trail purge job runs |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |