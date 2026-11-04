---
title: "V$SQLCOMMAND"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3066.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQLCOMMAND` displays the mapping between SQL opcodes and names.

| Column | Datatype | Description |
| --- | --- | --- |
| `COMMAND_TYPE` | `NUMBER` | SQL command number |
| `COMMAND_NAME` | `VARCHAR2(64)` | SQL command name |