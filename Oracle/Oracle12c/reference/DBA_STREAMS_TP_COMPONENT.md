---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_STREAMS_TP_COMPONENT.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_STREAMS_TP_COMPONENT` displays information about each Oracle Streams component at each database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPONENT_ID` | `NUMBER` | `NOT NULL` | ID of the Streams component |
| `COMPONENT_NAME` | `VARCHAR2(4000)` |  | Name of the Streams component |
| `COMPONENT_DB` | `VARCHAR2(128)` |  | Database where the Streams component resides |
| `COMPONENT_TYPE` | `VARCHAR2(20)` |  | Type of the Streams component:  - `CAPTURE` - `PROPAGATION SENDER` - `PROPAGATION RECEIVER` - `APPLY` - `QUEUE` |
| `COMPONENT_CHANGED_TIME` | `DATE` |  | Time that the Streams component was last changed |