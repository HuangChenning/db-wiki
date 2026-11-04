---
title: DBA_LOGSTDBY_SKIP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4126.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_LOGSTDBY_SKIP` displays the skip rules that are used by SQL Apply. This view is for logical standby databases only.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ERROR` | `VARCHAR2(1)` |  | Indicates how the skip rule was created: |
| `STATEMENT_OPT` | `VARCHAR2(30)` |  | Specifies the type of statement that should be skipped |
| `OWNER` | `VARCHAR2(30)` |  | Name of the schema under which the skip option should be used |
| `NAME` | `VARCHAR2(65)` |  | Name of the table that is being skipped |
| `USE_LIKE` | `VARCHAR2(1)` |  | Indicates whether the statement should use a SQL wildcard search when matching names (`Y`) or not (`N`) |
| `ESC` | `VARCHAR2(1)` |  | Escape character used when performing wildcard matches |
| `PROC` | `VARCHAR2(98)` |  | Name of a stored procedure that will be executed when processing the skip option |