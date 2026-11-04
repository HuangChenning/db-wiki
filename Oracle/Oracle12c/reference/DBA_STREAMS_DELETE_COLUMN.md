---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_STREAMS_DELETE_COLUMN.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_STREAMS_DELETE_COLUMN` displays information about declarative rule-based transformations that delete a column from a row logical change record (LCR).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_OWNER` | `VARCHAR2(128)` |  | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(128)` |  | Name of the rule |
| `SCHEMA_NAME` | `VARCHAR2(128)` |  | Schema of the column to be deleted |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Table of the column to be deleted |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column to delete |
| `VALUE_TYPE` | `VARCHAR2(3)` |  | Indicates whether to modify the old (`OLD`), new (`NEW`), or both (`*`) values of the LCR |
| `PRECEDENCE` | `NUMBER` |  | `1` (the execution order relative to other transformations on the same `STEP_NUMBER`; the smaller number will be executed first) |
| `STEP_NUMBER` | `NUMBER` |  | Order in which this transformation should be executed |