---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_STREAMS_TP_COMPONENT_LINK.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.13 DBA\_STREAMS\_TP\_COMPONENT\_LINK

`DBA_STREAMS_TP_COMPONENT_LINK` displays information about how messages flow between Replication components.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SOURCE_COMPONENT_ID` | `NUMBER` | `NOT NULL` | ID of the source Replication component |
| `SOURCE_COMPONENT_NAME` | `VARCHAR2(4000)` |  | Name of the source Replication component |
| `SOURCE_COMPONENT_DB` | `VARCHAR2(128)` |  | Database where the source Replication component resides |
| `SOURCE_COMPONENT_TYPE` | `VARCHAR2(20)` |  | Type of the source Replication component:  - `CAPTURE` - `PROPAGATION SENDER` - `PROPAGATION RECEIVER` - `APPLY` - `QUEUE` |
| `DESTINATION_COMPONENT_ID` | `NUMBER` | `NOT NULL` | ID of the destination Replication component |
| `DESTINATION_COMPONENT_NAME` | `VARCHAR2(4000)` |  | Name of the destination Replication component |
| `DESTINATION_COMPONENT_DB` | `VARCHAR2(128)` |  | Database where the destination Replication component resides |
| `DESTINATION_COMPONENT_TYPE` | `VARCHAR2(20)` |  | Type of the destination Replication component:  - `CAPTURE` - `PROPAGATION SENDER` - `PROPAGATION RECEIVER` - `APPLY` - `QUEUE` |
| `PATH_ID` | `NUMBER` | `NOT NULL` | ID of the stream path |
| `POSITION` | `NUMBER` |  | Position of the link within the stream path |