---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_STREAMS_ADD_COLUMN.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.1 DBA\_STREAMS\_ADD\_COLUMN

`DBA_STREAMS_ADD_COLUMN` displays information about declarative rule-based transformations that add a column to a row logical change record (LCR).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_OWNER` | `VARCHAR2(128)` |  | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(128)` |  | Name of the rule |
| `SCHEMA_NAME` | `VARCHAR2(128)` |  | Schema of the column to be added |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Table of the column to be added |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column to be added |
| `COLUMN_VALUE` | `ANYDATA` |  | Value of the column to be added |
| `COLUMN_TYPE` | `VARCHAR2(4000)` |  | Type of the column to be added |
| `COLUMN_FUNCTION` | `VARCHAR2(128)` |  | Name of the default function used to add a column |
| `VALUE_TYPE` | `VARCHAR2(3)` |  | Indicates whether to modify the old (`OLD`), new (`NEW`), or both (`*`) values of the LCR |
| `PRECEDENCE` | `NUMBER` |  | `3` (the execution order relative to other transformations on the same `STEP_NUMBER`; the smaller number will be executed first) |
| `STEP_NUMBER` | `NUMBER` |  | Order in which this transformation should be executed |