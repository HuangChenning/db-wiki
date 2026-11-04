---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_APPLY_PARAMETERS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_APPLY_PARAMETERS` displays information about the parameters for the apply processes that dequeue events from queues accessible to the current user.

Related View

`DBA_APPLY_PARAMETERS` displays information about the parameters for all apply processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APPLY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the apply process |
| `PARAMETER` | `VARCHAR2(128)` | `NOT NULL` | Name of the parameter |
| `VALUE` | `VARCHAR2(4000)` |  | Parameter value |
| `SET_BY_USER` | `VARCHAR2(3)` |  | Indicates whether the parameter value was set by the user (`YES`) or was not set by the user (`NO`). If `NO` for a parameter, then the parameter is set to its default value. If `YES` for a parameter, then the parameter may or may not be set to its default value. |

See Also:

" [DBA\_APPLY\_PARAMETERS](DBA_APPLY_PARAMETERS.md) "