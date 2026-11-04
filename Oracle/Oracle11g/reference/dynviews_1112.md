---
title: "V$DEAD_CLEANUP"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1112.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DEAD_CLEANUP` shows the dead processes and killed sessions present in the instance and their cleanup status.

| Column | Datatype | Description |
| --- | --- | --- |
| `TYPE` | `VARCHAR2(64)` | Indicates whether a row contains a `DEAD PROCESS` or `KILLED SESSION` |
| `PADDR` | `RAW(8)` | Process pointer. Can be joined with `V$PROCESS`. - For a killed session that has not been moved, this is the current owner of the session. - For a killed session that has been moved but has not been acked, this is the owner of the session at the time of the kill (the one that still needs to provide an ack). - For a killed session that has been moved and acked, this will be `NULL`. - There can be multiple rows for the same process if it owns multiple killed sessions. |
| `SADDR` | `RAW(8)` | Session pointer. Can be joined with `V$SESSION`. If a dead process has multiple user sessions, this is the current user session. If it owns other killed processes, there will be multiple rows for this dead process. |
| `STATE` | `VARCHAR2(64)` | Cleanup state: - `UNSAFE TO ATTEMPT` - Occurs for a killed session that has not been moved, so no cleanup can occur on it yet - `CLEANUP PENDING` - Occurs for a dead process / killed session that can be cleaned up, but PMON has not yet made an attempt - `RESOURCES FREED` - Occurs for a dead process / killed session where all children have been freed, but the process / killed session itself is not yet freed - `RESOURCES FREED - PENDING ACK` - Occurs for a killed session where all children have been freed, but the session itself cannot be freed until the owner has acked it - `PARTIAL CLEANUP` - Occurs if some of the children have been cleaned up |
| `DEAD_TIME` | `NUMBER` | Time since the process was marked dead or the session was marked killed (in seconds) |
| `CLEANUP_ATTEMPTS` | `NUMBER` | Number of times PMON has attempted cleanup |
| `LAST_ATTEMPT` | `NUMBER` | How long ago the last cleanup attempt occurred (in seconds) |
| `CLEANUP_TIME` | `NUMBER` | Total amount of time PMON has spent on cleanup of the process/session (in seconds) |
| `NUM_BLOCKED` | `NUMBER` | Number of sessions blocked on cleanup of this session |

Note:

This view is available starting with Oracle Database 11g Release 2 (11.2.0.4).