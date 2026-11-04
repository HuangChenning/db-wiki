---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CAPTURE_PARAMETERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.119 ALL\_CAPTURE\_PARAMETERS

`ALL_CAPTURE_PARAMETERS` displays information about the parameters for the capture processes that enqueue the captured changes into queues accessible to the current user.

Related View

`DBA_CAPTURE_PARAMETERS` displays information about the parameters for all capture processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the capture process |
| `PARAMETER` | `VARCHAR2(128)` | `NOT NULL` | Name of the parameter |
| `VALUE` | `VARCHAR2(4000)` |  | Parameter value |
| `SET_BY_USER` | `VARCHAR2(3)` |  | Indicates whether the parameter value was set by the user (`YES`) or was not set by the user (`NO`). If `NO`, then the parameter is set to its default value. If `YES`, then the parameter may or may not be set to its default value. |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | Global name of the container for which the capture parameter is defined |

See Also:

" [DBA\_CAPTURE\_PARAMETERS](DBA_CAPTURE_PARAMETERS.md) "