---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AQ_NOTIFICATION_CLIENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.30 V$AQ\_NOTIFICATION\_CLIENTS

`V$AQ_NOTIFICATION_CLIENTS` displays performance statistics for secure OCI client connections.

| Column | Datatype | Description |
| --- | --- | --- |
| `CLIENT_ID` | `VARCHAR2(29)` | Internally generated client ID for secure notification clients |
| `EMON_ID` | `NUMBER` | Emon ID serving the client |
| `NOTIFICATION_STATE` | `NUMBER` | Notification state:  - `ACTIVE` – Sending notification - `WAIT_FOR_ACK` – Waiting for client acknowledgment - `INACTIVE` - Idle connection |
| `NUM_MESSAGE_SENT` | `NUMBER` | Number of messages sent on the connection |
| `NUM_BYTES_SENT` | `NUMBER` | Number of bytes sent on the connection |
| `NUM_MESSAGE_RECEIVED` | `NUMBER` | Number of messages successfully received by the client |
| `LAST_SEND_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when the last message was sent on the connection |
| `LAST_RECEIVE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when the last message was received over the connection |
| `CONNECT_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time at which the client connected |
| `DISCONNECT_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time at which the client disconnected |
| `LAST_ERROR` | `NUMBER` | The last error that occurred on the client connection |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Database Advanced Queueing