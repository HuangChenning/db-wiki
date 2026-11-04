---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_STREAMS_TP_COMPONENT_STAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.14 DBA\_STREAMS\_TP\_COMPONENT\_STAT

`DBA_STREAMS_TP_COMPONENT_STAT` displays temporary performance statistics and session statistics about each Replication component.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPONENT_ID` | `NUMBER` | `NOT NULL` | ID of the Replication component |
| `COMPONENT_NAME` | `VARCHAR2(4000)` |  | Name of the Replication component |
| `COMPONENT_DB` | `VARCHAR2(128)` |  | Database where the Replication component resides |
| `COMPONENT_TYPE` | `VARCHAR2(20)` |  | Type of the Replication component:  - `CAPTURE` - `PROPAGATION SENDER` - `PROPAGATION RECEIVER` - `APPLY` - `QUEUE` |
| `SUB_COMPONENT_TYPE` | `VARCHAR2(27)` |  | Type of the Replication subcomponent:  - `LOGMINER READER` - `LOGMINER PREPARER` - `LOGMINER BUILDER` - `CAPTURE SESSION` - `PROPAGATION SENDER+RECEIVER` - `APPLY READER` - `APPLY COORDINATOR` - `APPLY SERVER` |
| `SESSION_ID` | `NUMBER` |  | ID of the Replication session for the Replication component |
| `SESSION_SERIAL#` | `NUMBER` |  | Serial number of the Replication session for the Replication component |
| `STATISTIC_TIME` | `DATE` |  | Time that the statistic was taken |
| `STATISTIC_NAME` | `VARCHAR2(64)` |  | Name of the statistic |
| `STATISTIC_VALUE` | `VARCHAR2(4000)` |  | Value of the statistic |
| `STATISTIC_UNIT` | `VARCHAR2(64)` |  | Unit of the statistic |
| `ADVISOR_RUN_ID` | `NUMBER` |  | Logical number (1-based) of the Advisor run |
| `ADVISOR_RUN_TIME` | `DATE` |  | Time that the Advisor was run |