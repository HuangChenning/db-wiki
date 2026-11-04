---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-SHARED_SERVER.html
tags:
  - oracle
  - 12c
  - reference
---

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |