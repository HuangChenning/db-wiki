---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_RSRC_MAPPING_PRIORITY.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.310 DBA\_RSRC\_MAPPING\_PRIORITY

`DBA_RSRC_MAPPING_PRIORITY` displays information about all consumer group mapping attribute priorities.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ATTRIBUTE` | `VARCHAR2(128)` |  | Session attribute |
| `PRIORITY` | `NUMBER` |  | Priority (`1` is the highest) |
| `STATUS` | `VARCHAR2(128)` |  | Indicates whether the consumer group is part of the pending area (`PENDING`) or not (NULL) |