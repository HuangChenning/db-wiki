---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_SSCR_CAPTURE.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_SSCR_CAPTURE` displays session state capture statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DB_NAME` | `VARCHAR2(4000)` |  | Database name of captured session |
| `INST_NAME` | `VARCHAR2(4000)` |  | Instance name of captured session |
| `INST_ID` | `NUMBER` |  | Instance ID of captured session |
| `SESSION_ID` | `NUMBER` |  | Session ID of captured session |
| `SESSION_SERIAL#` | `NUMBER` |  | Session serial number of captured session |
| `USER_NAME` | `VARCHAR2(128)` | `NOT NULL` | User name of captured session |
| `SCHEMA_NAME` | `VARCHAR2(128)` | `NOT NULL` | Schema name of captured session |
| `SEQUENCE#` | `NUMBER` |  | Sequence number of captured session |
| `CAPTURE_MODE` | `VARCHAR2(7)` |  | Mode of capture operation |
| `CAPTURE_SCOPE` | `VARCHAR2(7)` |  | Scope of capture operation |
| `CAPTURE_FORMAT` | `VARCHAR2(9)` |  | Format of capture files |
| `CAPTURE_DIR` | `VARCHAR2(128)` |  | Directory object of capture files |
| `CAPTURE_LOCATOR` | `RAW(64)` |  | Locator of master capture file |
| `CAPTURE_TIME` | `TIMESTAMP(6)` |  | Timestamp of capture operation |