---
title: DBA_RSRC_MAPPING_PRIORITY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4228.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_RSRC_MAPPING_PRIORITY` displays information about all consumer group mapping attribute priorities.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ATTRIBUTE` | `VARCHAR2(30)` |  | Session attribute |
| `PRIORITY` | `NUMBER` |  | Priority (`1` is the highest) |
| `STATUS` | `VARCHAR2(30)` |  | Indicates whether the consumer group is part of the pending area (`PENDING`) or not (NULL) |