---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SHARED_SERVER_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.56 DBA\_HIST\_SHARED\_SERVER\_SUMMARY

`DBA_HIST_SHARED_SERVER_SUMMARY` displays historical information for shared servers.

This includes information about shared server activity, the servers, common queues, and dispatcher queues. This view obtains information from `V$SHARED_SERVER`, `V$DISPATCHER`, `V$CIRCUIT`, and `V$QUEUE`, and is aggregated over all servers, dispatchers, queues, and circuits.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `NUM_SAMPLES` | `NUMBER` |  | Total number of samples |
| `SAMPLE_TIME` | `NUMBER` |  | Last sample timestamp |
| `SAMPLED_TOTAL_CONN` | `NUMBER` |  | Cumulative sum of total number of connections over all samples. To determine the average number of connections between two snapshots, divide the difference in `SAMPLED_TOTAL_CONN` by the difference in `NUM_SAMPLES`. |
| `SAMPLED_ACTIVE_CONN` | `NUMBER` |  | Cumulative sum of active number of connections over all samples. To determine the average number of active connections between two snapshots, divide the difference in `SAMPLED_ACTIVE_CONN` by the difference in `NUM_SAMPLES`. |
| `SAMPLED_TOTAL_SRV` | `NUMBER` |  | Cumulative sum of total number of servers over all samples. To determine the average number of servers between two snapshots, divide the difference in `SAMPLED_TOTAL_SRV` by the difference in `NUM_SAMPLES`. |
| `SAMPLED_ACTIVE_SRV` | `NUMBER` |  | Cumulative sum of active number of servers over all samples. To determine the average number of active servers between two snapshots, divide the difference in `SAMPLED_ACTIVE_SRV` by the difference in `NUM_SAMPLES`. |
| `SAMPLED_TOTAL_DISP` | `NUMBER` |  | Cumulative sum of total number of dispatchers over all samples. To determine the average number of dispatchers between two snapshots, divide the difference in `SAMPLED_TOTAL_DISP` by the difference in `NUM_SAMPLES`. |
| `SAMPLED_ACTIVE_DISP` | `NUMBER` |  | Cumulative sum of active number of dispatchers over all samples. To determine the average number of active dispatchers between two snapshots, divide the difference in `SAMPLED_ACTIVE_DISP` by the difference in `NUM_SAMPLES`. |
| `SRV_BUSY` | `NUMBER` |  | Total shared server busy time (in hundredths of a second) |
| `SRV_IDLE` | `NUMBER` |  | Total shared server idle time (in hundredths of a second) |
| `SRV_IN_NET` | `NUMBER` |  | Total shared server incoming network wait time (in hundredths of a second). This includes waits for receives and resets. This time is also included in `SRV_BUSY`. |
| `SRV_OUT_NET` | `NUMBER` |  | Total shared server outgoing network wait time (in hundredths of a second). This includes waits for sends and outbound connection requests. This time is also included in `SRV_BUSY`. |
| `SRV_MESSAGES` | `NUMBER` |  | Number of messages processed |
| `SRV_BYTES` | `NUMBER` |  | Total number of bytes in all messages |
| `CQ_WAIT` | `NUMBER` |  | Total time that all items in the common queue have waited (in hundredths of a second) |
| `CQ_TOTALQ` | `NUMBER` |  | Total number of items that have ever been in the common queue |
| `DQ_TOTALQ` | `NUMBER` |  | Total number of items that have ever been in a dispatcher queue |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |