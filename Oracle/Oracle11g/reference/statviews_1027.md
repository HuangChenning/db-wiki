---
title: ALL_CAPTURE_PARAMETERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1027.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CAPTURE_PARAMETERS` displays information about the parameters for the capture processes that enqueue the captured changes into queues accessible to the current user.

Related View

`DBA_CAPTURE_PARAMETERS` displays information about the parameters for all capture processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the capture process |
| `PARAMETER` | `VARCHAR2(128)` | `NOT NULL` | Name of the parameter |
| `VALUE` | `VARCHAR2(4000)` |  | Parameter value |
| `SET_BY_USER` | `VARCHAR2(3)` |  | Indicates whether the parameter value was set by the user (`YES`) or was not set by the user (`NO`). If `NO`, then the parameter is set to its default value. If `YES`, then the parameter may or may not be set to its default value. |

See Also:

["DBA\_CAPTURE\_PARAMETERS"](statviews_3099.md)