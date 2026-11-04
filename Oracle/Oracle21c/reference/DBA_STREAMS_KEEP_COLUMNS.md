---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_STREAMS_KEEP_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.4 DBA\_STREAMS\_KEEP\_COLUMNS

`DBA_STREAMS_KEEP_COLUMNS` displays information about declarative rule-based transformations that keep a list of columns in a row logical change record (LCR).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_OWNER` | `VARCHAR2(128)` |  | Owner of the rule which has an associated transformation |
| `RULE_NAME` | `VARCHAR2(128)` |  | Name of the rule which has an associated transformation |
| `SCHEMA_NAME` | `VARCHAR2(128)` |  | Schema of the column to be kept |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Table of the column to be kept |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Column to keep |
| `VALUE_TYPE` | `VARCHAR2(3)` |  | Indicates whether to keep the old (`OLD`), new (`NEW`), or both (`*`) value of the LCR |
| `PRECEDENCE` | `NUMBER` |  | `0` (the execution order relative to other transformations on the same `STEP_NUMBER`; the smaller number will be executed first) |
| `STEP_NUMBER` | `NUMBER` |  | Order in which this transformation should be executed |