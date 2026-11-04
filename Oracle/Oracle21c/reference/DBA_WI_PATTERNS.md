---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WI_PATTERNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.112 DBA\_WI\_PATTERNS

Each row in `DBA_WI_PATTERNS` represents a pattern that has been identified by Workload Intelligence as significant in the workload associated with the given job. Such a pattern consists of one or more templates.

These templates that comprise the given pattern are described in the related view `DBA_WI_PATTERN_ITEMS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOB_ID` | `NUMBER` | `NOT NULL` | The identifier of the job in the workload of which the current pattern has been found |
| `PATTERN_ID` | `NUMBER` | `NOT NULL` | The identifier of the current pattern |
| `LENGTH` | `NUMBER` | `NOT NULL` | The length of the pattern, that is, the number of items (templates) it consists of |
| `NUMBER_OF_EXECUTIONS` | `NUMBER` | `NOT NULL` | The number of times the current pattern has been executed in the given workload |
| `DB_TIME` | `NUMBER` | `NOT NULL` | The total time consumed in the database server by all the executions of the current pattern in the given workload |

See Also:

" [DBA\_WI\_PATTERN\_ITEMS](DBA_WI_PATTERN_ITEMS.md) "