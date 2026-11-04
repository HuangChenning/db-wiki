---
title: "V$GES_ENQUEUE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1159.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$GES_ENQUEUE` describes all locks currently known to lock manager. This is an Oracle Real Application Clusters view.

See Also:

["V$GES\_BLOCKING\_ENQUEUE"](dynviews_1156.md) for a description of all such locks that are currently blocking or being blocked

| Column | Datatype | Description |
| --- | --- | --- |
| `HANDLE` | `RAW(4 \| 8)` | Lock pointer |
| `GRANT_LEVEL` | `VARCHAR2(9)` | Granted level of the lock |
| `REQUEST_LEVEL` | `VARCHAR2(9)` | Requested level of the lock |
| `RESOURCE_NAME1` | `VARCHAR2(30)` | Resource name for the lock |
| `RESOURCE_NAME2` | `VARCHAR2(30)` | Resource name for the lock |
| `PID` | `NUMBER` | Process identifier which holds the lock |
| `TRANSACTION_ID0` | `NUMBER` | Lower 4 bytes of the transaction identifier to which the lock belongs |
| `TRANSACTION_ID1` | `NUMBER` | Upper 4 bytes of the transaction identifier to which the lock belongs |
| `GROUP_ID` | `NUMBER` | Group identifier for the lock |
| `OPEN_OPT_DEADLOCK` | `NUMBER` | `1` if `DEADLOCK` open option is set, otherwise `0` |
| `OPEN_OPT_PERSISTENT` | `NUMBER` | `1` if `PERSISTENT` open option is set, otherwise `0` |
| `OPEN_OPT_PROCESS_OWNED` | `NUMBER` | `1` if `PROCESS_OWNED` open option is set, otherwise `0` |
| `OPEN_OPT_NO_XID` | `NUMBER` | `1` if `NO_XID` open option is set, otherwise `0` |
| `CONVERT_OPT_GETVALUE` | `NUMBER` | `1` if `GETVALUE` convert option is set, otherwise `0` |
| `CONVERT_OPT_PUTVALUE` | `NUMBER` | `1` if `PUTVALUE` convert option is set, otherwise `0` |
| `CONVERT_OPT_NOVALUE` | `NUMBER` | `1` if `NOVALUE` convert option is set, otherwise `0` |
| `CONVERT_OPT_DUBVALUE` | `NUMBER` | `1` if `DUBVALUE` convert option is set, otherwise `0` |
| `CONVERT_OPT_NOQUEUE` | `NUMBER` | `1` if `NOQUEUE` convert option is set, otherwise `0` |
| `CONVERT_OPT_EXPRESS` | `NUMBER` | `1` if `EXPRESS` convert option is set, otherwise `0` |
| `CONVERT_OPT_NODEADLOCKWAIT` | `NUMBER` | `1` if `NODEADLOCKWAIT` convert option is set, otherwise `0` |
| `CONVERT_OPT_NODEADLOCKBLOCK` | `NUMBER` | `1` if `NODEADLOCKBLOCK` convert option is set, otherwise `0` |
| `WHICH_QUEUE` | `NUMBER` | Which queue the lock is currently located. `0` for `NULL` queue; `1` for `GRANTED` queue; `2` for `CONVERT` queue. |
| `STATE` | `VARCHAR2(64)` | State of the lock as the owner sees it |
| `AST_EVENT0` | `NUMBER` | Last AST event |
| `OWNER_NODE` | `NUMBER` | Node identifier |
| `BLOCKED` | `NUMBER` | `1` if this lock request is blocked by others, otherwise `0` |
| `BLOCKER` | `NUMBER` | `1` if this lock is blocking others, otherwise `0` |