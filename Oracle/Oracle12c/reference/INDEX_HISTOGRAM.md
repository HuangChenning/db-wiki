---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/INDEX_HISTOGRAM.html
tags:
  - oracle
  - 12c
  - reference
---

`INDEX_HISTOGRAM` contains information from the `ANALYZE INDEX ... VALIDATE STRUCTURE` statement.

Note:

The `ANALYZE INDEX ... VALIDATE STRUCTURE OFFLINE` statement must be used to collect statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REPEAT_COUNT` | `NUMBER` |  | Number of times that one or more index keys is repeated in the table |
| `KEYS_WITH_REPEAT_COUNT` | `NUMBER` |  | Number of index keys that are repeated that many times |