---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_APP_ERRORS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_APP_ERRORS` displays errors raised when an application PDB synchronizes with an application in the application root.

This view displays errors raised during the last synchronization for each application.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APP_NAME` | `VARCHAR2(128)` |  | Name of the application whose statement was captured |
| `APP_STATEMENT` | `CLOB` |  | Application statement |
| `ERRORNUM` | `NUMBER` |  | Error number for the statement |
| `ERRORMSG` | `VARCHAR2(4000)` |  | Error message for the statement |
| `SYNC_TIME` | `DATE ` | `NOT NULL` | Sync time for the statement |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).