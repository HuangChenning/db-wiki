---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_APP_ERRORS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.105 DBA\_APP\_ERRORS

`DBA_APP_ERRORS` displays errors raised when an application PDB synchronizes with an application in the application root.

This view displays errors raised during the last synchronization for each application.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APP_NAME` | `VARCHAR2(128)` |  | Name of the application whose statement was captured |
| `APP_STATEMENT` | `CLOB` |  | Application statement |
| `ERRORNUM` | `NUMBER` |  | Error number for the statement |
| `ERRORMSG` | `VARCHAR2(4000)` |  | Error message for the statement |
| `SYNC_TIME` | `DATE ` | `NOT NULL` | Sync time for the statement |
| `SYSTEM_IGNORABLE` | `VARCHAR2(1)` |  | Indicates whether the error is a system-ignorable error (`Y`) or not (`N`) |
| `USER_IGNORABLE` | `VARCHAR2(1)` |  | Indicates whether the error is a user-ignorable error (`Y`) or not (`N`) |