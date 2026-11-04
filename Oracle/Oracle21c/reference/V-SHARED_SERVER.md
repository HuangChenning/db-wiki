---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SHARED_SERVER.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.41 V$SHARED\_SERVER

`V$SHARED_SERVER` displays information on the shared server processes.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(4)` | Name of the server |
| `PADDR` | `RAW(4 \| 8)` | Server's process address |
| `STATUS` | `VARCHAR2(16)` | Server status:  - `EXEC` - Executing SQL - `WAIT (ENQ)` - Waiting for a lock - `WAIT (SEND)` - Waiting to send data to user - `WAIT (COMMON)` - Idle; waiting for a user request - `WAIT (RECEIVE)` - Waiting for records to be shown in the client application - `WAIT (RESET)` - Waiting for a circuit to reset after a break - `QUIT` - Terminating |
| `MESSAGES` | `NUMBER` | Number of messages processed |
| `BYTES` | `NUMBER` | Total number of bytes in all messages |
| `BREAKS` | `NUMBER` | Number of breaks |
| `CIRCUIT` | `RAW(4 \| 8)` | Address of the circuit currently being serviced |
| `IDLE` | `NUMBER` | Total idle time (in hundredths of a second) |
| `BUSY` | `NUMBER` | Total busy time (in hundredths of a second) |
| `IN_NET` | `NUMBER` | Total incoming network wait time (in hundredths of a second) |
| `OUT_NET` | `NUMBER` | Total outgoing network wait time (in hundredths of a second) |
| `REQUESTS` | `NUMBER` | Total number of requests taken from the common queue in this server's lifetime |
| `BOUND_TIME` | `NUMBER` | Time that a circuit and shared server have been bound (in centiseconds) |
| `BOUND_REASON` | `VARCHAR2(32)` | Provides a reason (a short explanation) for why a shared server and circuit could not be unbound.  This column is empty when a circuit is not bound to a server.  When the server starts serving a circuit, `BOUND_REASON` is empty and remains empty unless the server tries unsuccessfully to unbind the circuit (after it finishes serving the current request).  When this column is not empty, it will be cleared once the server and circuit are unbound (that is, once the resources preventing the session migration to another shared server are released). |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |