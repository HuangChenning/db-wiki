---
title: DBA_STREAMS_RENAME_TABLE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5012.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_STREAMS_RENAME_TABLE` displays information about declarative rule-based transformations that rename a table in a row logical change record (LCR).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_OWNER` | `VARCHAR2(30)` |  | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(30)` |  | Name of the rule |
| `FROM_SCHEMA_NAME` | `VARCHAR2(30)` |  | Schema to be renamed |
| `TO_SCHEMA_NAME` | `VARCHAR2(30)` |  | New schema name |
| `FROM_TABLE_NAME` | `VARCHAR2(30)` |  | Table to be renamed |
| `TO_TABLE_NAME` | `VARCHAR2(30)` |  | New table name |
| `PRECEDENCE` | `NUMBER` |  | `4` (the execution order relative to other transformations on the same `STEP_NUMBER`; the smaller number will be executed first) |
| `STEP_NUMBER` | `NUMBER` |  | Order in which this transformation should be executed |