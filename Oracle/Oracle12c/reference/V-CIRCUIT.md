---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-CIRCUIT.html
tags:
  - oracle
  - 12c
  - reference
---

`V$CIRCUIT` contains information about virtual circuits, which are user connections to the database through dispatchers and servers.

| Column | Datatype | Description |
| --- | --- | --- |
| `CIRCUIT` | `RAW(4 \| 8)` | Circuit address |
| `DISPATCHER` | `RAW(4 \| 8)` | Current dispatcher process address |
| `SERVER` | `RAW(4 \| 8)` | Current server process address |
| `WAITER` | `RAW(4 \| 8)` | Address of the server process that is waiting for the (currently busy) circuit to become available |
| `SADDR` | `RAW(4 \| 8)` | Address of the session bound to the circuit |
| `STATUS` | `VARCHAR2(16)` | Status of the circuit:  - `BREAK` - currently interrupted - `EOF` - about to be removed - `OUTBOUND` - an outward link to a remote database - `NORMAL` - normal circuit into the local database |
| `QUEUE` | `VARCHAR2(16)` | Queue the circuit is currently on:  - `COMMON` - on the common queue, waiting to be picked up by a server process - `DISPATCHER` - waiting for the dispatcher - `SERVER` - currently being serviced - `NONE` - idle circuit |
| `MESSAGE0` | `NUMBER` | Size in bytes of the messages in the first message buffer |
| `MESSAGE1` | `NUMBER` | Size in bytes of the messages in the second message buffer |
| `MESSAGE2` | `NUMBER` | Size in bytes of the messages in the third message buffer |
| `MESSAGE3` | `NUMBER` | Size in bytes of the messages in the fourth message buffer |
| `MESSAGES` | `NUMBER` | Total number of messages that have gone through this circuit |
| `BYTES` | `NUMBER` | Total number of bytes that have gone through this circuit |
| `BREAKS` | `NUMBER` | Total number of breaks (interruptions) for this circuit |
| `PRESENTATION` | `VARCHAR2(257)` | Presentation protocol used by the client and server |
| `PCIRCUIT` | `RAW(4 \| 8)` | Address of the parent circuit |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |