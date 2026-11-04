---
title: DBA_WORKLOAD_CONNECTION_MAP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5092.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_WORKLOAD_CONNECTION_MAP` displays the connection mapping information for workload replay. Each row defines one connection mapping for a particular workload replay.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REPLAY_ID` | `NUMBER` | `NOT NULL` | ID of the replay (corresponds to `DBA_WORKLOAD_REPLAYS.ID`) |
| `CONN_ID` | `NUMBER` | `NOT NULL` | Key (ID) of the connection mapping table |
| `SCHEDULE_CAP_ID` <sup>Foot 1</sup> | `NUMBER` |  | Schedule capture ID (corresponds to `DBA_WORKLOAD_SCHEDULE_CAPTURES.SCHEDULE_CAP_ID`) |
| `CAPTURE_CONN` | `VARCHAR2(4000)` | `NOT NULL` | Connection string that was used during capture |
| `REPLAY_CONN` | `VARCHAR2(4000)` |  | Connection string that should be used during replay |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.4)