---
title: ALL_SCHEDULER_WINDOW_LOG
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2057.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_WINDOW_LOG` displays log information for the Scheduler windows accessible to the current user.

Related View

`DBA_SCHEDULER_WINDOW_LOG` displays log information for all Scheduler windows in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `LOG_ID` | `NUMBER` | `NOT NULL` | Unique identifier of the log entry |
| `LOG_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Date of the log entry |
| `WINDOW_NAME` | `VARCHAR2(65)` |  | Name of the Scheduler window |
| `OPERATION` | `VARCHAR2(30)` |  | Operation corresponding to the log entry |
| `STATUS` | `VARCHAR2(30)` |  | Status of the operation, if applicable |
| `USER_NAME` | `VARCHAR2(30)` |  | Name of the user who performed the operation, if applicable |
| `CLIENT_ID` | `VARCHAR2(64)` |  | Client identifier of the user who performed the operation, if applicable |
| `GLOBAL_UID` | `VARCHAR2(32)` |  | Global user identifier of the user who performed the operation, if applicable |
| `ADDITIONAL_INFO` | `CLOB` |  | Additional information on the entry, if applicable |

See Also:

["DBA\_SCHEDULER\_WINDOW\_LOG"](statviews_4262.md)