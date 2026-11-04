---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-IOSTAT_CONSUMER_GROUP.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.17 V$IOSTAT\_CONSUMER\_GROUP

`V$IOSTAT_CONSUMER_GROUP` displays disk I/O statistics for consumer groups.

If the resource manager is enabled, then I/O statistics for all consumer groups that are part of the currently enabled resource plan are captured.

| Column | Datatype | Description |
| --- | --- | --- |
| `CONSUMER_GROUP_ID` | `NUMBER` | Consumer group ID |
| `SMALL_READ_MEGABYTES` | `NUMBER` | Number of single block megabytes read |
| `SMALL_WRITE_MEGABYTES` | `NUMBER` | Number of single block megabytes written |
| `LARGE_READ_MEGABYTES` | `NUMBER` | Number of multiblock megabytes read |
| `LARGE_WRITE_MEGABYTES` | `NUMBER` | Number of multiblock megabytes written |
| `SMALL_READ_REQS` | `NUMBER` | Number of single block read requests |
| `SMALL_WRITE_REQS` | `NUMBER` | Number of single block write requests |
| `LARGE_READ_REQS` | `NUMBER` | Number of multiblock read requests |
| `LARGE_WRITE_REQS` | `NUMBER` | Number of multiblock write requests |
| `NUMBER_OF_WAITS` | `NUMBER` | Number of I/O waits by consumer group |
| `WAIT_TIME` | `NUMBER` | Total wait time (in milliseconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |