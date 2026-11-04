---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_APPLY_REPERROR_HANDLERS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_APPLY_REPERROR_HANDLERS` provides details about apply reperror handlers on objects visible to the user.

Related View

`DBA_APPLY_REPERROR_HANDLERS` provides details about apply reperror handlers.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APPLY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the apply process |
| `OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `SOURCE_OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Source database owner of the source object |
| `SOURCE_OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Source database name of the object |
| `ERROR_NUMBER` | `NUMBER` | `NOT NULL` | Error number for the handler |
| `METHOD` | `VARCHAR2(18)` |  | Error handling method:  - `ABEND` - `RECORD` - `IGNORE` - `RETRY` - `RETRY_TRANSACTION` - `RECORD_TRANSACTION` |
| `MAX_RETRIES` | `NUMBER` |  | Maximum number of times to retry for the method `RETRY` and `RETRY_TRANSACTION` |
| `DELAY_CSECS` | `NUMBER` |  | Number of centiseconds to wait between retries for `RETRY` and `RETRY_TRANSACTION` |
| `SET_BY` | `VARCHAR2(10)` |  | Entity that set up the handler:  - `USER` - `GOLDENGATE` |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

" [DBA\_APPLY\_REPERROR\_HANDLERS](DBA_APPLY_REPERROR_HANDLERS.md) "