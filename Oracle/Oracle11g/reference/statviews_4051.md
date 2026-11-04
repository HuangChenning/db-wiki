---
title: DBA_HIST_SQLCOMMAND_NAME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4051.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SQLCOMMAND_NAME` displays the mapping between SQL opcodes and names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `COMMAND_TYPE` | `NUMBER` | `NOT NULL` | SQL command number |
| `COMMAND_NAME` | `VARCHAR2(64)` |  | SQL command name |