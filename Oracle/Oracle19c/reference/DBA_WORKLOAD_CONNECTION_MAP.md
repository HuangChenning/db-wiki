---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_WORKLOAD_CONNECTION_MAP.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.118 DBA\_WORKLOAD\_CONNECTION\_MAP

`DBA_WORKLOAD_CONNECTION_MAP` displays the connection mapping information for workload replay. Each row defines one connection mapping for a particular workload replay.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REPLAY_ID` | `NUMBER` | `NOT NULL` | ID of the replay (corresponds to `DBA_WORKLOAD_REPLAYS.ID`) |
| `CONN_ID` | `NUMBER` | `NOT NULL` | Key (ID) of the connection mapping table |
| `SCHEDULE_CAP_ID` | `NUMBER` |  | Schedule capture ID (corresponds to `DBA_WORKLOAD_SCHEDULE_CAPTURES.SCHEDULE_CAP_ID`) |
| `CAPTURE_CONN` | `VARCHAR2(4000)` | `NOT NULL` | Connection string that was used during capture |
| `REPLAY_CONN` | `VARCHAR2(4000)` |  | Connection string that should be used during replay |