---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WI_PATTERN_ITEMS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.111 DBA\_WI\_PATTERN\_ITEMS

Each row in `DBA_WI_PATTERN_ITEMS` represents a template that participates in a significant pattern that has been found by the given Workload Intelligence job.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOB_ID` | `NUMBER` | `NOT NULL` | The identifier of the job in the workload of which the current pattern has been found |
| `PATTERN_ID` | `NUMBER` | `NOT NULL` | The identifier of the pattern to which the current item (template) belongs |
| `SEQUENCE_NUMBER` | `NUMBER` | `NOT NULL` | Number that indicates the position of the current item in the given pattern |
| `TEMPLATE_ID` | `NUMBER` | `NOT NULL` | The identifier of the template that participates in the given position of the current pattern |
| `IS_FIRST_IN_LOOP` | `CHAR(1)` | `NOT NULL` | A flag that indicates whether or not the current item marks the beginning of a loop in the given pattern. The possible values are `Y` and `N`. |
| `IS_LAST_IN_LOOP` | `CHAR(1)` | `NOT NULL` | A flag that indicates whether or not the current item marks the end of a loop in the given pattern. The possible values are `Y` and `N`. |