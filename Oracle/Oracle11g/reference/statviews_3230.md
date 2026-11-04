---
title: DBA_HIST_INTERCONNECT_PINGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3230.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_INTERCONNECT_PINGS` displays information about measured latency of interconnect messages (round-trip) from instance to instance. In Oracle Database 11g, the `PING` process assesses the latencies associated with communications for each pair of instances.

Every few seconds, the process in one instance (`INSTANCE_NUMBER` value) sends two messages to each instance (`TARGET_INSTANCE` value). One message has a size of 500 bytes and the other has a size of 8 KB. The message is received by the `PING` process on the target instance and is immediately acknowledged. The time for the round-trip is measured and collected.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `TARGET_INSTANCE` | `NUMBER` | `NOT NULL` | Target instance number |
| `CNT_500B` | `NUMBER` |  | Number of pings of size 500 bytes from `INSTANCE_NUMBER` to `TARGET_INSTANCE` since the startup of the source instance (`INSTANCE_NUMBER`) |
| `WAIT_500B` | `NUMBER` |  | Sum of round-trip times for messages of size 500 bytes from `INSTANCE_NUMBER` to `TARGET_INSTANCE` since the startup of the source instance (`INSTANCE_NUMBER`). Dividing by `CNT_500B` gives the average latency. |
| `WAITSQ_500B` | `NUMBER` |  | Sum of squares (divided by 1000) of round-trip times for messages of size 500 bytes from `INSTANCE_NUMBER` to `TARGET_INSTANCE` since the startup of the source instance (`INSTANCE_NUMBER`). When used with `CNT_500B` and `WAIT_500B`, the standard deviation of the latency can be calculated. |
| `CNT_8K` | `NUMBER` |  | Number of pings of size 8 KB from `INSTANCE_NUMBER` to `TARGET_INSTANCE` since the startup of the source instance (`INSTANCE_NUMBER`) |
| `WAIT_8K` | `NUMBER` |  | Sum of round-trip times for messages of size 8 KB from `INSTANCE_NUMBER` to `TARGET_INSTANCE` since the startup of the source instance (`INSTANCE_NUMBER`). Dividing by `CNT_8K` gives the average latency. |
| `WAITSQ_8K` | `NUMBER` |  | Sum of squares (divided by 1000) of round-trip times for messages of size 8 KB from `INSTANCE_NUMBER` to `TARGET_INSTANCE` since the startup of the source instance (`INSTANCE_NUMBER`). When used with `CNT_8K` and `WAIT_8K`, the standard deviation of the latency can be calculated. |