---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DISPATCHER.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.185 V$DISPATCHER

`V$DISPATCHER` displays information about the dispatcher processes.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(4)` | Name of the dispatcher process |
| `NETWORK` | `VARCHAR2(1024)` | Network address of the dispatcher |
| `PADDR` | `RAW(4 \| 8)` | Process address |
| `STATUS` | `VARCHAR2(16)` | Status of the dispatcher:  - `WAIT` - Idle - `SEND` - Sending a message - `RECEIVE` - Receiving a message - `CONNECT` - Establishing a connection - `DISCONNECT` - Handling a disconnect request - `BREAK` - Handling a break - `TERMINATE` - In the process of terminating - `ACCEPT` - Accepting connections (no further information available) - `REFUSE` - Rejecting connections (no further information available) |
| `ACCEPT` | `VARCHAR2(3)` | Indicates whether the dispatcher is accepting new connections (`YES`) or not (`NO`) |
| `MESSAGES` | `NUMBER` | Number of messages processed by the dispatcher |
| `BYTES` | `NUMBER` | Size (in bytes) of messages processed by the dispatcher |
| `BREAKS` | `NUMBER` | Number of breaks occurring in the connection |
| `OWNED` | `NUMBER` | Number of circuits owned by the dispatcher |
| `CREATED` | `NUMBER` | Number of circuits created by the dispatcher |
| `IDLE` | `NUMBER` | Total idle time for the dispatcher (in hundredths of a second) |
| `BUSY` | `NUMBER` | Total busy time for the dispatcher (in hundredths of a second) |
| `CPU` | `NUMBER` | Total CPU time for the dispatcher (in millionths of a second) |
| `LISTENER` | `NUMBER` | Most recent Oracle error number the dispatcher received from the listener |
| `CONF_INDX` | `NUMBER` | Zero-based index of the `DISPATCHERS` configuration used by the dispatcher |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |