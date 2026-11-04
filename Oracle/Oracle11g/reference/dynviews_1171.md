---
title: "V$HANG_SESSION_INFO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1171.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$HANG_SESSION_INFO` displays information about sessions involved in hangs described by `V$HANG_INFO`. Each row with the same `HANG_ID` describes a session that is in the hang wait chain described by the row with the same `HANG_ID` in `V$HANG_INFO`. This session is blocked by the victim or final blocker of that hang.

| Column | Datatype | Description |
| --- | --- | --- |
| `HANG_ID` | `NUMBER` | A number identifying the hang including this session. This column can be used to join `V$HANG_INFO` with `V$HANG_SESSION_INFO`. |
| `INSTANCE` | `NUMBER` | Instance number of instance on which this session resides |
| `SID` | `NUMBER` | Oracle session ID of this session |
| `SERIAL#` | `NUMBER` | Oracle session serial number of this session |
| `OSPID` | `VARCHAR2(25)` | Operating system process ID of this session |
| `FATAL_BACKGROUND` | `VARCHAR2(1)` | `Y` - Session is a critical background process  `N` - Session is not a critical background process |
| `ROOT` | `VARCHAR2(1)` | `Y` - This session is the victim or final blocker of the hang  `N` - This session is not the victim or final blocker of the hang |
| `WAIT_EVENT_TEXT` | `VARCHAR2(64)` | Resource or event for which this session is waiting; set to `not in a wait` if the session is not waiting on a resource |

See Also:

- ["V$HANG\_INFO"](dynviews_1170.md)
- ["V$HANG\_STATISTICS"](dynviews_1172.md)