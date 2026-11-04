---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-AQ_IPC_ACTIVE_MSGS.html
tags:
  - oracle
  - 19c
  - reference
---

## 7.18 V$AQ\_IPC\_ACTIVE\_MSGS

`V$AQ_IPC_ACTIVE_MSGS` displays the information related to active IPC messages being processed by AQ background processes.

| Column | Datatype | Description |
| --- | --- | --- |
| `PROCESS_NAME` | `VARCHAR2(48)` | Worker process name |
| `PROCESS_ID` | `NUMBER` | Oracle process ID for this worker |
| `SLAVE_STATE` | `NUMBER` | Worker status:  - `3`: Picked task - `4`: Running - `7`: Idle |
| `SLAVEOBJ_STATE` | `NUMBER` | Worker object status:  - `0`: Invalid - `1`: Valid |
| `SEQUENCE_NUMBER` | `NUMBER` | Message sequence number |
| `MSG_CLASS_NAME` | `VARCHAR2(30)` | Message class name |
| `MSG_FLAGS` | `NUMBER` | Message flags:  - `1`: This message needs ack - `2`: Short - `4`: Long - `8`: Priority - `10`: Special ack |
| `MSG_SUBMT_TIME` | `NUMBER` | Time this message was added into the IPC primary's list (in seconds) |
| `MSG_PICKD_TIME` | `NUMBER` | Time this message was picked by worker or primary for processing (in seconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |