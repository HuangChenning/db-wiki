---
title: ALL_TAB_STATS_HISTORY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2115.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TAB_STATS_HISTORY` provides a history of table statistics modifications for all tables accessible to the current user.

Related Views

- `DBA_TAB_STATS_HISTORY` provides a history of table statistics modifications for all tables in the database.
- `USER_TAB_STATS_HISTORY` provides a history of table statistics modifications for all tables owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table |
| `PARTITION_NAME` | `VARCHAR2(30)` |  | Name of the partition |
| `SUBPARTITION_NAME` | `VARCHAR2(30)` |  | Name of the subpartition |
| `STATS_UPDATE_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time at which the statistics were updated |

See Also:

- ["DBA\_TAB\_STATS\_HISTORY"](statviews_5054.md)
- ["USER\_TAB\_STATS\_HISTORY"](statviews_5488.md)