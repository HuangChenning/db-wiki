---
title: "V$LATCHNAME"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2020.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LATCHNAME` displays information about decoded latch names for the latches shown in `V$LATCH`. The rows of `V$LATCHNAME` have a one-to-one correspondence to the rows of `V$LATCH`.

| Column | Datatype | Description |
| --- | --- | --- |
| `LATCH#` | `NUMBER` | Latch number |
| `NAME` | `VARCHAR2(64)` | Latch name |
| `HASH` | `NUMBER` | Latch hash |

See Also:

["V$LATCH"](dynviews_2015.md)