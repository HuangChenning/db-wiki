---
title: DBA_HIST_CURRENT_BLOCK_SERVER
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3214.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_CURRENT_BLOCK_SERVER` displays historical statistics on the Global Cache Service processes (lMS) used in cache fusion. This view contains snapshots of `V$CURRENT_BLOCK_SERVER`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `PIN1` | `NUMBER` |  | Pins taking less than 1 millisecond |
| `PIN10` | `NUMBER` |  | Pins taking 1 to 10 milliseconds |
| `PIN100` | `NUMBER` |  | Pins taking 10 to 100 milliseconds |
| `PIN1000` | `NUMBER` |  | Pins taking 100 to 1000 milliseconds |
| `PIN10000` | `NUMBER` |  | Pins taking 1000 to 10000 milliseconds |
| `FLUSH1` | `NUMBER` |  | Flushes taking less than 1 millisecond |
| `FLUSH10` | `NUMBER` |  | Flushes taking 1 to 10 milliseconds |
| `FLUSH100` | `NUMBER` |  | Flushes taking 10 to 100 milliseconds |
| `FLUSH1000` | `NUMBER` |  | Flushes taking 100 to 1000 milliseconds |
| `FLUSH10000` | `NUMBER` |  | Flushes taking 1000 to 10000 milliseconds |
| `WRITE1` | `NUMBER` |  | Writes taking less than 1 millisecond |
| `WRITE10` | `NUMBER` |  | Writes taking 1 to 10 milliseconds |
| `WRITE100` | `NUMBER` |  | Writes taking 10 to 100 milliseconds |
| `WRITE1000` | `NUMBER` |  | Writes taking 100 to 1000 milliseconds |
| `WRITE10000` | `NUMBER` |  | Writes taking 1000 to 10000 milliseconds |