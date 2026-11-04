---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_USAGE.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.52 DBA\_ADVISOR\_USAGE

`DBA_ADVISOR_USAGE` displays the usage information for each type of advisor in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ADVISOR_ID` | `NUMBER` | `NOT NULL` | Type of the advisor |
| `ADVISOR_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the advisor |
| `LAST_EXEC_TIME` | `DATE` | `NOT NULL` | Date of the last execution |
| `NUM_EXECS` | `NUMBER` | `NOT NULL` | Cumulative number of executions |
| `NUM_DB_REPORTS` | `NUMBER` | `NOT NULL` | Cumulative number of reports |
| `FIRST_REPORT_TIME` | `DATE` |  | Time of the first report |
| `LAST_REPORT_TIME` | `DATE` |  | Time of the last report |