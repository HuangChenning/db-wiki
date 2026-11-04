---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_HANG_MANAGER_PARAMETERS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_HANG_MANAGER_PARAMETERS` shows the available user tunable Hang Manager parameters and their values.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(40)` | `NOT NULL` | String representation of the parameter names |
| `CURRENT_VALUE` | `VARCHAR2(20)` |  | String representation of the parameter values |
| `CURRENT_TIME` | `DATE` |  | Time when the current value was set |
| `PREVIOUS_VALUE` | `VARCHAR2(20)` |  | String representation of the parameter value from the previous update |
| `PREVIOUS_TIME` | `DATE` |  | Time when the previous value was set |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).