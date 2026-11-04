---
title: "V$LATCHHOLDER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2019.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LATCHHOLDER` displays information about the current latch holders.

| Column | Datatype | Description |
| --- | --- | --- |
| `PID` | `NUMBER` | Identifier of the process holding the latch |
| `SID` | `NUMBER` | Identifier of the session that owns the latch |
| `LADDR` | `RAW(4 \| 8)` | Latch address |
| `NAME` | `VARCHAR2(64)` | Name of the latch being held |
| `GETS` | `NUMBER` | Number of times that the latch was obtained in either wait mode or no-wait mode |