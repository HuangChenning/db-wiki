---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ROLLING_EVENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.297 DBA\_ROLLING\_EVENTS

`DBA_ROLLING_EVENTS` lists all the events reported from the `DBMS_ROLLING` PL/SQL package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `EVENTID` | `NUMBER` |  | Event identifier which identifies event order |
| `EVENT_TIME` | `TIMESTAMP(6)` |  | Time associated with the event |
| `TYPE` | `VARCHAR2(7)` |  | Type of event: `INFO`, `NOTICE`, `WARNING`, or `ERROR` |
| `MESSAGE` | `VARCHAR2(256)` |  | Text describing the event details |
| `STATUS` | `NUMBER` |  | Status code associated with an event |
| `INSTID` | `NUMBER` |  | Instruction ID associated with an event |
| `REVISION` | `NUMBER` |  | Plan revision number associated with an event |

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB5214) for more information about rolling operations.
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS73534) for more information about the `DBMS_ROLLING` package