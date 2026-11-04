---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_WI_PATTERN_ITEMS.html
tags:
  - oracle
  - 12c
  - reference
---

Each row in `DBA_WI_PATTERN_ITEMS` represents a template that participates in a significant pattern that has been found by the given Workload Intelligence job.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOB_ID` | `NUMBER` | `NOT NULL` | The identifier of the job in the workload of which the current pattern has been found |
| `PATTERN_ID` | `NUMBER` | `NOT NULL` | The identifier of the pattern to which the current item (template) belongs |
| `SEQUENCE_NUMBER` | `NUMBER` | `NOT NULL` | Number that indicates the position of the current item in the given pattern |
| `TEMPLATE_ID` | `NUMBER` | `NOT NULL` | The identifier of the template that participates in the given position of the current pattern |
| `IS_FIRST_IN_LOOP` | `CHAR(1)` | `NOT NULL` | A flag that indicates whether or not the current item marks the beginning of a loop in the given pattern. The possible values are `Y` and `N`. |
| `IS_LAST_IN_LOOP` | `CHAR(1)` | `NOT NULL` | A flag that indicates whether or not the current item marks the end of a loop in the given pattern. The possible values are `Y` and `N`. |