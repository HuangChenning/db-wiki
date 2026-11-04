---
title: DBA_AUDIT_MGMT_CLEANUP_JOBS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3073.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_AUDIT_MGMT_CLEANUP_JOBS` displays information about the configured audit trail purge jobs.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOB_NAME` | `VARCHAR2(100)` | `NOT NULL` | Name of the audit trail purge job |
| `JOB_STATUS` | `VARCHAR2(8)` |  | Current status of the audit trail purge job (`ENABLED`) or (`DISABLED`) |
| `AUDIT_TRAIL` | `VARCHAR2(28)` |  | Audit trail for which the audit trail purge job is configured: |
| `JOB_FREQUENCY` | `VARCHAR2(100)` |  | Frequency at which the audit trail purge job runs |