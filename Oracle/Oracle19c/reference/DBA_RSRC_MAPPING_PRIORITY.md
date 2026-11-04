---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_RSRC_MAPPING_PRIORITY.html
tags:
  - oracle
  - 19c
  - reference
---

## 5.307 DBA\_RSRC\_MAPPING\_PRIORITY

`DBA_RSRC_MAPPING_PRIORITY` displays information about all consumer group mapping attribute priorities.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ATTRIBUTE` | `VARCHAR2(128)` |  | Session attribute |
| `PRIORITY` | `NUMBER` |  | Priority (`1` is the highest) |
| `STATUS` | `VARCHAR2(128)` |  | Indicates whether the consumer group is part of the pending area (`PENDING`) or not (NULL) |