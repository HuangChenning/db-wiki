---
title: "V$HANG_INFO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1170.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$HANG_INFO` displays information about hangs found on the cluster. A hang can be an open wait chain or closed wait chain (cycle or deadlock). A wait chain is a series of sessions that are blocking one another. Each row represents a hang and describes how severe the hang is. This view also includes the victim or final blocker of the hang.

| Column | Datatype | Description |
| --- | --- | --- |
| `HANG_ID` | `NUMBER` | A number identifying the hang |
| `HANG_CHAIN_SESSIONS` | `NUMBER` | Indicates how many sessions are in the main wait chain of the hang |
| `TOTAL_HUNG_SESSIONS` | `NUMBER` | Indicates how many total sessions are affected by the hang, including the main wait chain and any wait chains branching off of the main wait chain |
| `HANG_TYPE` | `VARCHAR2(18)` | Is set to `Hang` if this is an open wait chain, or `Deadlock` if this is a cycle or closed wait chain? |
| `HANG_CREATE_TIME` | `VARCHAR2(20)` | Date and time that the hang was detected |
| `HANG_RESOLVE_TIME` | `VARCHAR2(20)` | Time that the hang may be automatically resolved |
| `IGNORED_HANG` | `VARCHAR2(1)` | `Y` - The hang was ignored and will not be automatically resolved at this time  `N` - The hang has not yet been verified |
| `RESOLUTION_ATTEMPTED` | `VARCHAR2(1)` | `Y` - An attempt was made to resolve the hang  `N` - No attempt was made to resolve the hang |
| `GLOBAL_HANG` | `VARCHAR2(1)` | `Y` - The hang spans multiple nodes in the cluster  `N` - All of the sessions in the hang reside on a single instance |
| `ESCALATED_HANG` | `VARCHAR2(1)` | `Y` - An attempt was made to resolve the hang but was unsuccessful, and the hang is becoming more severe. Another resolution attempt will be made.  `N` - The first resolution attempt was successful and it was not necessary to escalate the hang to a higher resolution level. |
| `RESOLUTION_STATUS` | `VARCHAR2(46)` | Contains the reason why the hang was resolved or ignored |
| `VICTIM_INSTANCE` | `NUMBER` | Instance number of the instance on which the victim or final blocker session resides |
| `VICTIM_SESSION_ID` | `NUMBER` | Victim or final blocker's Oracle session ID |
| `VICTIM_SERIAL#` | `NUMBER` | Victim or final blocker's Oracle session serial number |
| `VICTIM_OSPID` | `VARCHAR2(25)` | Victim or final blocker's operating system process ID |
| `FATAL_BACKGROUND` | `VARCHAR2(1)` | `Y` - Victim or final blocker is a critical background process  `N` - Victim or final blocker is not a critical background process |
| `WAIT_EVENT_TEXT` | `VARCHAR2(64)` | Resource or event for which the victim or final blocker is waiting; set to `not in a wait` if the session is not waiting on a resource |

See Also:

- ["V$HANG\_SESSION\_INFO"](dynviews_1171.md)
- ["V$HANG\_STATISTICS"](dynviews_1172.md)