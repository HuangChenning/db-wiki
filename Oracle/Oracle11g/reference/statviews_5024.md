---
title: DBA_STREAMS_TP_PATH_BOTTLENECK
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5024.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_STREAMS_TP_PATH_BOTTLENECK` displays temporary information about Oracle Streams components that might be slowing down the flow of messages in a stream path.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PATH_ID` | `NUMBER` |  | ID of the stream path |
| `COMPONENT_ID` | `NUMBER` |  | ID of the bottleneck component |
| `COMPONENT_NAME` | `VARCHAR2(4000)` |  | Name of the bottleneck component |
| `COMPONENT_DB` | `VARCHAR2(128)` |  | Database where the bottleneck component resides |
| `COMPONENT_TYPE` | `VARCHAR2(20)` |  | Type of the bottleneck component: - `CAPTURE` - `PROPAGATION SENDER` - `PROPAGATION RECEIVER` - `APPLY` - `QUEUE` |
| `TOP_SESSION_ID` | `NUMBER` |  | ID of the top session for the bottleneck component |
| `TOP_SESSION_SERIAL#` | `NUMBER` |  | Serial number of the top session for the bottleneck component |
| `ACTION_NAME` | `VARCHAR2(32)` |  | Action name for the bottleneck process |
| `BOTTLENECK_IDENTIFIED` | `VARCHAR2(30)` |  | Indicates whether the bottleneck was identified (`YES`) or not (`NO`) |
| `ADVISOR_RUN_ID` | `NUMBER` |  | Logical number (1-based) of the Advisor run |
| `ADVISOR_RUN_TIME` | `DATE` |  | Time that the Advisor was run |
| `ADVISOR_RUN_REASON` | `VARCHAR2(4000)` |  | Reason for the bottleneck analysis result.: - NULL - Bottleneck is identified - `PRE-11.1 DATABASE EXISTS` - A pre-release 11.1 database exists in the stream path - `DIAGNOSTIC PACK REQUIRED` - A database in the stream path does not have the diagnostic package installed - `NO BOTTLENECK IDENTIFIED` |