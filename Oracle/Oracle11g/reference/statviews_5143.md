---
title: INDEX_HISTOGRAM
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5143.htm
tags:
  - oracle
  - 11g
  - reference
---

`INDEX_HISTOGRAM` contains information from the `ANALYZE INDEX ... VALIDATE STRUCTURE` statement.

Note:

The `ANALYZE INDEX ... VALIDATE STRUCTURE OFFLINE` statement must be used in order to collect statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REPEAT_COUNT` | `NUMBER` |  | Number of times that one or more index keys is repeated in the table |
| `KEYS_WITH_REPEAT_COUNT` | `NUMBER` |  | Number of index keys that are repeated that many times |