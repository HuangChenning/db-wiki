---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_HANG_MANAGER_PARAMETERS.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.324 DBA\_HANG\_MANAGER\_PARAMETERS

`DBA_HANG_MANAGER_PARAMETERS` shows the available user tunable Hang Manager parameters and their values.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(40)` | `NOT NULL` | String representation of the parameter names |
| `CURRENT_VALUE` | `VARCHAR2(20)` |  | String representation of the parameter values |
| `CURRENT_TIME` | `DATE` |  | Time when the current value was set |
| `PREVIOUS_VALUE` | `VARCHAR2(20)` |  | String representation of the parameter value from the previous update |
| `PREVIOUS_TIME` | `DATE` |  | Time when the previous value was set |