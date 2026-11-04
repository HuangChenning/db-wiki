---
title: DBA_AUDIT_MGMT_LAST_ARCH_TS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3075.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_AUDIT_MGMT_LAST_ARCH_TS` displays information about the last archive timestamps set for audit trail cleanup or purges.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `AUDIT_TRAIL` | `VARCHAR2(20)` |  | Audit trail for which the last archive timestamp applies: |
| `RAC_INSTANCE` | `NUMBER` | `NOT NULL` | Oracle RAC instance number for which the last archive timestamp applies; `0` implies not applicable |
| `LAST_ARCHIVE_TS` | `TIMESTAMP(6) WITH TIME ZONE` |  | Timestamp of the last audit record or audit file that has been archived |