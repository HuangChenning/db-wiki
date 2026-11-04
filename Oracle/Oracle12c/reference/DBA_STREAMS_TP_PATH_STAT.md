---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_STREAMS_TP_PATH_STAT.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_STREAMS_TP_PATH_STAT` displays temporary performance statistics about each stream path that exists in the Oracle Streams topology.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PATH_ID` | `NUMBER` |  | ID of the stream path |
| `STATISTIC_TIME` | `DATE` |  | Time that the statistic was taken |
| `STATISTIC_NAME` | `VARCHAR2(64)` |  | Name of the statistic |
| `STATISTIC_VALUE` | `NUMBER` |  | Value of the statistic |
| `STATISTIC_UNIT` | `VARCHAR2(64)` |  | Unit of the statistic |
| `ADVISOR_RUN_ID` | `NUMBER` |  | Logical number (1-based) of the Advisor run |
| `ADVISOR_RUN_TIME` | `DATE` |  | Time that the Advisor was run |