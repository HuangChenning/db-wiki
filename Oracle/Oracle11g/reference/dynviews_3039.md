---
title: "V$SHARED_SERVER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3039.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SHARED_SERVER` displays information on the shared server processes.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(4)` | Name of the server |
| `PADDR` | `RAW(4 \| 8)` | Server's process address |
| `STATUS` | `VARCHAR2(16)` | Server status:  `EXEC` - Executing SQL  `WAIT` (ENQ) - Waiting for a lock  `WAIT` (SEND) - Waiting to send data to user  `WAIT` (COMMON) - Idle; waiting for a user request  `WAIT` (RESET) - Waiting for a circuit to reset after a break  `QUIT` - Terminating |
| `MESSAGES` | `NUMBER` | Number of messages processed |
| `BYTES` | `NUMBER` | Total number of bytes in all messages |
| `BREAKS` | `NUMBER` | Number of breaks |
| `CIRCUIT` | `RAW(4 \| 8)` | Address of the circuit currently being serviced |
| `IDLE` | `NUMBER` | Total idle time (in hundredths of a second) |
| `BUSY` | `NUMBER` | Total busy time (in hundredths of a second) |
| `IN_NET` | `NUMBER` | Total incoming network wait time (in hundredths of a second) |
| `OUT_NET` | `NUMBER` | Total outgoing network wait time (in hundredths of a second) |
| `REQUESTS` | `NUMBER` | Total number of requests taken from the common queue in this server's lifetime |