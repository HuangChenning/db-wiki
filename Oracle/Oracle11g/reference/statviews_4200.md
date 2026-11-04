---
title: DBA_RECOVERABLE_SCRIPT_PARAMS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4200.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_RECOVERABLE_SCRIPT_PARAMS` provides details about recoverable operation parameters.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCRIPT_ID` | `RAW(16)` |  | Unique ID of the operation |
| `PARAMETER` | `VARCHAR2(30)` |  | Name of the parameter |
| `PARAM_INDEX` | `NUMBER` |  | Index for multi-valued parameter |
| `VALUE` | `VARCHAR2(4000)` |  | Value of the parameter |