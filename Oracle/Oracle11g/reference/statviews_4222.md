---
title: DBA_RSRC_CATEGORIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4222.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_RSRC_CATEGORIES` displays all resource consumer group categories.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(30)` |  | Name of the consumer group category |
| `COMMENTS` | `VARCHAR2(2000)` |  | Text comment on the consumer group category |
| `STATUS` | `VARCHAR2(30)` |  | Indicates whether the consumer group category is part of the pending area (`PENDING`) or not (NULL) |
| `MANDATORY` | `VARCHAR2(3)` |  | Indicates whether the consumer group category is mandatory (`YES`) or not (`NO`) |