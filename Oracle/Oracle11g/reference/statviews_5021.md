---
title: DBA_STREAMS_TP_COMPONENT_LINK
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5021.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_STREAMS_TP_COMPONENT_LINK` displays information about how messages flow between Oracle Streams components.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SOURCE_COMPONENT_ID` | `NUMBER` | `NOT NULL` | ID of the source Streams component |
| `SOURCE_COMPONENT_NAME` | `VARCHAR2(4000)` |  | Name of the source Streams component |
| `SOURCE_COMPONENT_DB` | `VARCHAR2(128)` |  | Database where the source Streams component resides |
| `SOURCE_COMPONENT_TYPE` | `VARCHAR2(20)` |  | Type of the source Streams component: - `CAPTURE` - `PROPAGATION SENDER` - `PROPAGATION RECEIVER` - `APPLY` - `QUEUE` |
| `DESTINATION_COMPONENT_ID` | `NUMBER` | `NOT NULL` | ID of the destination Streams component |
| `DESTINATION_COMPONENT_NAME` | `VARCHAR2(4000)` |  | Name of the destination Streams component |
| `DESTINATION_COMPONENT_DB` | `VARCHAR2(128)` |  | Database where the destination Streams component resides |
| `DESTINATION_COMPONENT_TYPE` | `VARCHAR2(20)` |  | Type of the destination Streams component: - `CAPTURE` - `PROPAGATION SENDER` - `PROPAGATION RECEIVER` - `APPLY` - `QUEUE` |
| `PATH_ID` | `NUMBER` | `NOT NULL` | ID of the stream path |
| `POSITION` | `NUMBER` |  | Position of the link within the stream path |