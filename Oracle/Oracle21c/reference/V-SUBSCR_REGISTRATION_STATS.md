---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SUBSCR_REGISTRATION_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.91 V$SUBSCR\_REGISTRATION\_STATS

`V$SUBSCR_REGISTRATION_STATS` displays information for diagnosability of notifications.

| Column | Datatype | Description |
| --- | --- | --- |
| `REG_ID` | `NUMBER` | Registration identifier |
| `NUM_NTFNS` | `NUMBER` | Number of notifications |
| `NUM_GROUPING_NTFNS` | `NUMBER` | Number of grouping notifications |
| `NUM_NTFNS_CURRENT_GROUP` | `NUMBER` | Number of events received in the current group |
| `LAST_NTFN_START_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when the last notification was started |
| `LAST_NTFN_SENT_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when the last notification was sent |
| `TOTAL_EMON_LATENCY` | `NUMBER` | Total EMON latency (time taken by the EMON worker to process notifications) |
| `EMON#` | `NUMBER` | Active EMON worker serving the registration |
| `ALL_EMON_SERVERS` | `RAW(2000)` | EMON workers that served the registration |
| `TOTAL_PAYLOAD_BYTES_SENT` | `NUMBER` | Total payload bytes sent |
| `SHARD_ID` | `NUMBER` | Shard number for current registration used for Key Based Messaging |
| `NUM_RETRIES` | `NUMBER` | Number of retries in sending notifications |
| `TOTAL_PLSQL_EXEC_TIME` | `NUMBER` | Total PL/SQL callback execution time (relevant only for PL/SQL notifications) |
| `LAST_ERR` | `VARCHAR2(90)` | Last error message |
| `LAST_ERR_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time of the last error |
| `LAST_UPDATE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time of the last update |
| `NUM_PENDING_NTFNS` | `NUMBER` | Number of notifications pending to be sent |
| `TOTAL_PENDING_NTFN_BYTES` | `NUMBER` | Total number of bytes for notifications pending to be sent |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |