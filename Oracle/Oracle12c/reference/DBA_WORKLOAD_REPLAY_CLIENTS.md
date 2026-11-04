---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_WORKLOAD_REPLAY_CLIENTS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_WORKLOAD_REPLAY_CLIENTS` displays all workload replay clients and their assigned instances.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `WRC_ID` | `NUMBER(38)` | `NOT NULL` | The identifier of a workload replay client |
| `SCHEDULE_CAP_ID` | `NUMBER(38)` | `NOT NULL` | A unique identifier for a workload capture added to a replay schedule. `0` for a non-consolidated replay |
| `INSTANCE_NUMBER` | `NUMBER(38)` | `NOT NULL` | The instance that the replay client connects to |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).