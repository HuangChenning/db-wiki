---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_CURRENT_BLOCK_SERVER.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.394 DBA\_HIST\_CURRENT\_BLOCK\_SERVER

`DBA_HIST_CURRENT_BLOCK_SERVER` displays historical statistics on the Global Cache Service processes (LMS) used in cache fusion.

This view contains snapshots of `V$CURRENT_BLOCK_SERVER`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `PIN0` | `NUMBER` |  | Pins taking less than 100 microseconds |
| `PIN1` | `NUMBER` |  | Pins taking 100 microseconds to 1 millisecond |
| `PIN10` | `NUMBER` |  | Pins taking 1 to 10 milliseconds |
| `PIN100` | `NUMBER` |  | Pins taking 10 to 100 milliseconds |
| `PIN1000` | `NUMBER` |  | Pins taking 100 to 1000 milliseconds |
| `PIN10000` | `NUMBER` |  | Pins taking 1000 to 10000 milliseconds |
| `FLUSH0` | `NUMBER` |  | Flushes taking less than 100 microseconds |
| `FLUSH1` | `NUMBER` |  | Flushes taking 100 microseconds to 1 millisecond |
| `FLUSH10` | `NUMBER` |  | Flushes taking 1 to 10 milliseconds |
| `FLUSH100` | `NUMBER` |  | Flushes taking 10 to 100 milliseconds |
| `FLUSH1000` | `NUMBER` |  | Flushes taking 100 to 1000 milliseconds |
| `FLUSH10000` | `NUMBER` |  | Flushes taking 1000 to 10000 milliseconds |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |