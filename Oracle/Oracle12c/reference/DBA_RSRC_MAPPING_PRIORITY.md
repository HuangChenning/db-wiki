---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_RSRC_MAPPING_PRIORITY.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_RSRC_MAPPING_PRIORITY` displays information about all consumer group mapping attribute priorities.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ATTRIBUTE` | `VARCHAR2(128)` |  | Session attribute |
| `PRIORITY` | `NUMBER` |  | Priority (`1` is the highest) |
| `STATUS` | `VARCHAR2(128)` |  | Indicates whether the consumer group is part of the pending area (`PENDING`) or not (NULL) |