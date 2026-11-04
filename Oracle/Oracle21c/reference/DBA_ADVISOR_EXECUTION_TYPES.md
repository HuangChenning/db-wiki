---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_EXECUTION_TYPES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.26 DBA\_ADVISOR\_EXECUTION\_TYPES

`DBA_ADVISOR_EXECUTION_TYPES` displays possible execution action for a given advisor.

Only advisors that support multiple executions of their tasks have entries in this view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ADVISOR_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the advisor |
| `EXECUTION_TYPE` | `VARCHAR2(128)` | `NOT NULL` | Execution type supported by the advisor |
| `EXECUTION_DESCRIPTION` | `VARCHAR2(4000)` |  | Optional description of the execution type |