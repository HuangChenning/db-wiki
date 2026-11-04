---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TAB_STATS_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.120 ALL\_TAB\_STATS\_HISTORY

`ALL_TAB_STATS_HISTORY` provides a history of table statistics modifications for all tables accessible to the current user.

Related Views

- `DBA_TAB_STATS_HISTORY` provides a history of table statistics modifications for all tables in the database.
- `USER_TAB_STATS_HISTORY` provides a history of table statistics modifications for all tables owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the object |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table |
| `PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the partition |
| `SUBPARTITION_NAME` | `VARCHAR2(128)` |  | Name of the subpartition |
| `STATS_UPDATE_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time at which the statistics were updated |

See Also:

- " [DBA\_TAB\_STATS\_HISTORY](DBA_TAB_STATS_HISTORY.md) "
- " [USER\_TAB\_STATS\_HISTORY](USER_TAB_STATS_HISTORY.md) "