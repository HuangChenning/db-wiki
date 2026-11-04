---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_STREAMS_TP_COMPONENT_STAT.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_STREAMS_TP_COMPONENT_STAT` displays temporary performance statistics and session statistics about each Oracle Streams component.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPONENT_ID` | `NUMBER` | `NOT NULL` | ID of the Streams component |
| `COMPONENT_NAME` | `VARCHAR2(4000)` |  | Name of the Streams component |
| `COMPONENT_DB` | `VARCHAR2(128)` |  | Database where the Streams component resides |
| `COMPONENT_TYPE` | `VARCHAR2(20)` |  | Type of the Streams component:  - `CAPTURE` - `PROPAGATION SENDER` - `PROPAGATION RECEIVER` - `APPLY` - `QUEUE` |
| `SUB_COMPONENT_TYPE` | `VARCHAR2(27)` |  | Type of the Streams subcomponent:  - `LOGMINER READER` - `LOGMINER PREPARER` - `LOGMINER BUILDER` - `CAPTURE SESSION` - `PROPAGATION SENDER+RECEIVER` - `APPLY READER` - `APPLY COORDINATOR` - `APPLY SERVER` |
| `SESSION_ID` | `NUMBER` |  | ID of the Streams session for the Streams component |
| `SESSION_SERIAL#` | `NUMBER` |  | Serial number of the Streams session for the Streams component |
| `STATISTIC_TIME` | `DATE` |  | Time that the statistic was taken |
| `STATISTIC_NAME` | `VARCHAR2(64)` |  | Name of the statistic |
| `STATISTIC_VALUE` | `VARCHAR2(4000)` |  | Value of the statistic |
| `STATISTIC_UNIT` | `VARCHAR2(64)` |  | Unit of the statistic |
| `ADVISOR_RUN_ID` | `NUMBER` |  | Logical number (1-based) of the Advisor run |
| `ADVISOR_RUN_TIME` | `DATE` |  | Time that the Advisor was run |