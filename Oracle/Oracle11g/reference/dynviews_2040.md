---
title: "V$LOGMNR_PARAMETERS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2040.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LOGMNR_PARAMETERS` contains log information.

| Column | Datatype | Description |
| --- | --- | --- |
| `START_DATE` | `DATE` | Date to start the search |
| `REQUIRED_START_DATE` | `DATE` | Required date to start the search if DDL tracking is enabled |
| `END_DATE` | `DATE` | Date to end the search |
| `START_SCN` | `NUMBER` | System change number to start the search |
| `REQUIRED_START_SCN` | `NUMBER` | Required system change number to start the search if DDL tracking is enabled |
| `END_SCN` | `NUMBER` | System change number to end the search |
| `OPTIONS` | `NUMBER` | Options specified for the current LogMiner session |
| `INFO` | `VARCHAR2(32)` | This column is always null. |
| `STATUS` | `NUMBER` | This column is always `0`. |