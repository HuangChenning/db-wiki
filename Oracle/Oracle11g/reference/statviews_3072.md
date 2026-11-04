---
title: DBA_AUDIT_MGMT_CLEAN_EVENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3072.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_AUDIT_MGMT_CLEAN_EVENTS` displays information about the history of audit trail cleanup or purge events. Periodically, you should delete the contents of this view so that it will not grow too large.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `AUDIT_TRAIL` | `VARCHAR2(28)` |  | Audit trail that was cleaned at the time of the event: |
| `RAC_INSTANCE` | `NUMBER` | `NOT NULL` | Instance number indicating the Oracle RAC instance that was cleaned up at the time of the event; `0` implies not applicable |
| `CLEANUP_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Timestamp when the cleanup event completed |
| `DELETE_COUNT` | `NUMBER` |  | Number of audit records or audit files that were deleted at the time of the event |
| `WAS_FORCED` | `VARCHAR2(3)` |  | Indicates whether a forced cleanup occurred (`YES`) or not (`NO`); forced cleanup bypasses the last archive timestamp set |