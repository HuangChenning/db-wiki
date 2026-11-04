---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_RECOVERABLE_SCRIPT_PARAMS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_RECOVERABLE_SCRIPT_PARAMS` provides details about recoverable operation parameters.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCRIPT_ID` | `RAW(16)` |  | Unique ID of the operation |
| `PARAMETER` | `VARCHAR2(128)` |  | Name of the parameter |
| `PARAM_INDEX` | `NUMBER` |  | Index for multi-valued parameter |
| `VALUE` | `VARCHAR2(4000)` |  | Value of the parameter |