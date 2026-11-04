---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_OBJECT_USAGE.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_OBJECT_USAGE` displays statistics about index usage gathered from the database for all the indexes in the database.

You can use this view to monitor index usage. All indexes that have been used at least once can be monitored and displayed in this view.

Related View

- `USER_OBJECT_USAGE` displays statistics about index usage gathered from the database for the indexes owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Index owner |
| `INDEX_NAME` | `VARCHAR2(128)` | `NOT NULL` | Index name in sys.obj$.name |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Table name in sys.obj$.name |
| `MONITORING` | `VARCHAR2(3)` |  | Indicates whether the monitoring feature is turned on. Possible values:  - `YES` - `NO` |
| `USED` | `VARCHAR2(3)` |  | Indicates whether the index has been accessed. Possible values:  - `YES` - `NO` |
| `START_MONITORING` | `VARCHAR2(19)` |  | Start monitoring time in `sys.object_stats.start_monitoring` |
| `END_MONITORING` | `VARCHAR2(19)` |  | End monitoring time in ` sys.object_stats.end_monitoring` |

See Also:

" [USER\_OBJECT\_USAGE](USER_OBJECT_USAGE.md) "