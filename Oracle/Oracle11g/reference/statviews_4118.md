---
title: DBA_LOGMNR_PURGED_LOG
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4118.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_LOGMNR_PURGED_LOG` displays archived redo log files that have been applied to the logical standby database and can be deleted because they are no longer needed. FIles in this view are refreshed as a result of executing either of the following PL/SQL procedures:

- `DBMS_LOGSTDBY.PURGE_SESSION` (for Oracle Data Guard SQL Apply)
- `DBMS_CAPTURE.SET_FIRST_SCN` (for Oracle Streams)

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_NAME` | `VARCHAR2(513)` |  | Fully qualified names of the archived redo log files that are no longer needed by SQL Apply and can be deleted from the operating system |