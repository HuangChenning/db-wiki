---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AQ_IPC_PENDING_MSGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.22 V$AQ\_IPC\_PENDING\_MSGS

`V$AQ_IPC_PENDING_MSGS` displays information about pending messages, present in the local primary context.

| Column | Datatype | Description |
| --- | --- | --- |
| `SEQUENCE_NUMBER` | `NUMBER` | Message sequence number |
| `MSG_CLASS_NAME` | `VARCHAR2(30)` | Message class name |
| `MSG_FLAGS` | `NUMBER` | Message flags:  - `1`: This message needs ack - `2`: Short - `4`: Long - `8`: Priority - `10`: Special ack |
| `MSG_SUBMT_TIME` | `NUMBER` | Time this message was added into the IPC primary's list (in seconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |