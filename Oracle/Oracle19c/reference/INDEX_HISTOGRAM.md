---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/INDEX_HISTOGRAM.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.204 INDEX\_HISTOGRAM

`INDEX_HISTOGRAM` contains information from the `ANALYZE INDEX ... VALIDATE STRUCTURE` statement.

Note:

The `ANALYZE INDEX ... VALIDATE STRUCTURE OFFLINE` statement must be used to collect statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REPEAT_COUNT` | `NUMBER` |  | Number of times that one or more index keys is repeated in the table |
| `KEYS_WITH_REPEAT_COUNT` | `NUMBER` |  | Number of index keys that are repeated that many times |