---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_STREAMS_TP_COMPONENT.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.12 DBA\_STREAMS\_TP\_COMPONENT

`DBA_STREAMS_TP_COMPONENT` displays information about each Replication component at each database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPONENT_ID` | `NUMBER` | `NOT NULL` | ID of the Replication component |
| `COMPONENT_NAME` | `VARCHAR2(4000)` |  | Name of the Replication component |
| `COMPONENT_DB` | `VARCHAR2(128)` |  | Database where the Replication component resides |
| `COMPONENT_TYPE` | `VARCHAR2(20)` |  | Type of the Replication component:  - `CAPTURE` - `PROPAGATION SENDER` - `PROPAGATION RECEIVER` - `APPLY` - `QUEUE` |
| `COMPONENT_CHANGED_TIME` | `DATE` |  | Time that the Replication component was last changed |