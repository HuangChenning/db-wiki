---
title: DBA_ADVISOR_USAGE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3043.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_USAGE` displays the usage information for each type of advisor in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ADVISOR_ID` | `NUMBER` | `NOT NULL` | Type of the advisor |
| `LAST_EXEC_TIME` | `DATE` | `NOT NULL` | Date of the last execution |
| `NUM_EXECS` | `NUMBER` | `NOT NULL` | Cumulative number of executions |