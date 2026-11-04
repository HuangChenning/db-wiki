---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SSCR_RESTORE.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.394 DBA\_SSCR\_RESTORE

`DBA_SSCR_RESTORE` displays session state restore statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DB_NAME` | `VARCHAR2(4000)` |  | Database name of restored session |
| `INST_NAME` | `VARCHAR2(4000)` |  | Instance name of restored session |
| `INST_ID` | `NUMBER` |  | Instance ID of restored session |
| `SESSION_ID` | `NUMBER` |  | Session ID of restored session |
| `SESSION_SERIAL#` | `NUMBER` |  | Session serial number of restored session |
| `USER_NAME` | `VARCHAR2(128)` | `NOT NULL` | User name of restored session |
| `SCHEMA_NAME` | `VARCHAR2(128)` | `NOT NULL` | Schema name of restored session |
| `SEQUENCE#` | `NUMBER` |  | Sequence number of restore operation |
| `RESTORE_MODE` | `VARCHAR2(7)` |  | Mode of restore operation |
| `RESTORE_SCOPE` | `VARCHAR2(7)` |  | Scope of restore operation |
| `RESTORE_FORMAT` | `VARCHAR2(9)` |  | Format of restore files |
| `RESTORE_DIR` | `VARCHAR2(128)` |  | Directory object of restore files |
| `RESTORE_LOCATOR` | `RAW(64)` |  | Locator of primary restore file |
| `RESTORE_TIME` | `TIMESTAMP(6)` |  | Timestamp of restore operation |