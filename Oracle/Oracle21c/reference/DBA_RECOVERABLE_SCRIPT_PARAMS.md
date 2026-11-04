---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_RECOVERABLE_SCRIPT_PARAMS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.269 DBA\_RECOVERABLE\_SCRIPT\_PARAMS

`DBA_RECOVERABLE_SCRIPT_PARAMS` provides details about recoverable operation parameters.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCRIPT_ID` | `RAW(16)` |  | Unique ID of the operation |
| `PARAMETER` | `VARCHAR2(128)` |  | Name of the parameter |
| `PARAM_INDEX` | `NUMBER` |  | Index for multi-valued parameter |
| `VALUE` | `VARCHAR2(4000)` |  | Value of the parameter |