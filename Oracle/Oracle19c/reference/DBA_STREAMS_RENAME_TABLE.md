---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_STREAMS_RENAME_TABLE.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.9 DBA\_STREAMS\_RENAME\_TABLE

`DBA_STREAMS_RENAME_TABLE` displays information about declarative rule-based transformations that rename a table in a row logical change record (LCR).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_OWNER` | `VARCHAR2(128)` |  | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(128)` |  | Name of the rule |
| `FROM_SCHEMA_NAME` | `VARCHAR2(128)` |  | Schema to be renamed |
| `TO_SCHEMA_NAME` | `VARCHAR2(128)` |  | New schema name |
| `FROM_TABLE_NAME` | `VARCHAR2(128)` |  | Table to be renamed |
| `TO_TABLE_NAME` | `VARCHAR2(128)` |  | New table name |
| `PRECEDENCE` | `NUMBER` |  | `4` (the execution order relative to other transformations on the same `STEP_NUMBER`; the smaller number will be executed first) |
| `STEP_NUMBER` | `NUMBER` |  | Order in which this transformation should be executed |