---
title: "V$SUBSCR_REGISTRATION_STATS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3086.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SUBSCR_REGISTRATION_STATS` displays information for diagnosability of notifications.

| Column | Datatype | Description |
| --- | --- | --- |
| `REG_ID` | `NUMBER` | Registration identifier |
| `NUM_NTFNS` | `NUMBER` | Number of notifications |
| `NUM_GROUPING_NTFNS` | `NUMBER` | Number of grouping notifications |
| `NUM_NTFNS_CURRENT_GROUP` | `NUMBER` | Number of events received in the current group |
| `LAST_NTFN_START_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when the last notification was started |
| `LAST_NTFN_SENT_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when the last notification was sent |
| `TOTAL_EMON_LATENCY` | `NUMBER` | Total EMON latency (time taken by the EMON slave to process notifications) |
| `EMON#` | `NUMBER` | Active EMON slave serving the registration |
| `ALL_EMON_SERVERS` | `RAW(2000)` | EMON slaves that served the registration |
| `TOTAL_PAYLOAD_BYTES_SENT` | `NUMBER` | Total payload bytes sent |
| `NUM_RETRIES` | `NUMBER` | Number of retries in sending notifications |
| `TOTAL_PLSQL_EXEC_TIME` | `NUMBER` | Total PL/SQL callback execution time (relevant only for PL/SQL notifications) |
| `LAST_ERR` | `VARCHAR2(90)` | Last error message |
| `LAST_ERR_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time of the last error |
| `LAST_UPDATE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time of the last update |
| `NUM_PENDING_NTFNS` | `NUMBER` | Number of notifications pending to be sent |
| `TOTAL_PENDING_NTFN_BYTES` <sup>Foot 1</sup> | `NUMBER` | Total number of bytes for notifications pending to be sent |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).