---
title: DBA_ADVISOR_EXECUTION_TYPES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3017.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_EXECUTION_TYPES` displays possible execution action for a given advisor. Only advisors that support multiple executions of their tasks have entries in this view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ADVISOR_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the advisor |
| `EXECUTION_TYPE` | `VARCHAR2(30)` | `NOT NULL` | Execution type supported by the advisor |
| `EXECUTION_DESCRIPTION` | `VARCHAR2(4000)` |  | Optional description of the execution type |