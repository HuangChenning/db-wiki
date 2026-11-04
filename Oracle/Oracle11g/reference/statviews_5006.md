---
title: DBA_STREAMS_KEEP_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5006.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_STREAMS_KEEP_COLUMNS` displays information about declarative rule-based transformations that keep a list of columns in a row logical change record (LCR).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_OWNER` | `VARCHAR2(30)` |  | Owner of the rule which has an associated transformation |
| `RULE_NAME` | `VARCHAR2(30)` |  | Name of the rule which has an associated transformation |
| `SCHEMA_NAME` | `VARCHAR2(30)` |  | Schema of the column to be kept |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Table of the column to be kept |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Column to keep |
| `VALUE_TYPE` | `VARCHAR2(3)` |  | Indicates whether to keep the old (`OLD`), new (`NEW`), or both (`*`) value of the LCR |
| `PRECEDENCE` | `NUMBER` |  | `0` (the execution order relative to other transformations on the same `STEP_NUMBER`; the smaller number will be executed first) |
| `STEP_NUMBER` | `NUMBER` |  | Order in which this transformation should be executed |