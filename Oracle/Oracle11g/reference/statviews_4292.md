---
title: DBA_SSCR_RESTORE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4292.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SSCR_RESTORE` displays session state restore statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DB_NAME` | `VARCHAR2(4000)` |  | Database name of restored session |
| `INST_NAME` | `VARCHAR2(4000)` |  | Instance name of restored session |
| `INST_ID` | `NUMBER` |  | Instance ID of restored session |
| `SESSION_ID` | `NUMBER` |  | Session ID of restored session |
| `SESSION_SERIAL#` | `NUMBER` |  | Session serial number of restored session |
| `USER_NAME` | `VARCHAR2(30)` | `NOT NULL` | User name of restored session |
| `SCHEMA_NAME` | `VARCHAR2(30)` | `NOT NULL` | Schema name of restored session |
| `SEQUENCE#` | `NUMBER` |  | Sequence number of restore operation |
| `RESTORE_MODE` | `VARCHAR2(7)` |  | Mode of restore operation |
| `RESTORE_SCOPE` | `VARCHAR2(7)` |  | Scope of restore operation |
| `RESTORE_FORMAT` | `VARCHAR2(9)` |  | Format of restore files |
| `RESTORE_DIR` | `VARCHAR2(30)` |  | Directory object of restore files |
| `RESTORE_LOCATOR` | `RAW(64)` |  | Locator of master restore file |
| `RESTORE_TIME` | `TIMESTAMP(6)` |  | Timestamp of restore operation |