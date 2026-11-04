---
title: "V$FAST_START_SERVERS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1134.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$FAST_START_SERVERS` provides information about all the recovery slaves performing parallel transaction recovery.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATE` | `VARCHAR2(11)` | State of the server (`IDLE` or `RECOVERING`) |
| `UNDOBLOCKSDONE` | `NUMBER` | Number of undo blocks done so far |
| `PID` | `NUMBER` | Process ID |
| `XID` | `RAW(8)` | Transaction ID |

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm)