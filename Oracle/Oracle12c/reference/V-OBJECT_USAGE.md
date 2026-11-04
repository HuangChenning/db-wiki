---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-OBJECT_USAGE.html
tags:
  - oracle
  - 12c
  - reference
---

`V$OBJECT_USAGE` displays statistics about index usage gathered from the database for the indexes owned by the current user. You can use this view to monitor index usage. All indexes that have been used at least once can be monitored and displayed in this view.

Note:

The `V$OBJECT_USAGE` view is deprecated in Oracle Database 12c Release 1 (12.1) and maintained for backward compatibility. Support for this view may be removed in a future release. Oracle recommends that you use the `USER_OBJECT_USAGE` view instead of the `V$OBJECT_USAGE` view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INDEX_NAME` | `VARCHAR2` | `NOT NULL` | Index name in sys.obj$.name |
| `TABLE_NAME` | `VARCHAR2` | `NOT NULL` | Table name in sys.obj$.name |
| `MONITORING` | `VARCHAR2` |  | `YES` \| `NO` |
| `USED` | `VARCHAR2` |  | `YES` \| `NO` |
| `START_MONITORING` | `VARCHAR2` |  | Start monitoring time in `sys.object_stats.start_monitoring` |
| `END_MONITORING` | `VARCHAR2` |  | End monitoring time in ` sys.object_stats.end_monitoring` |

See Also:

- " [USER\_OBJECT\_USAGE](USER_OBJECT_USAGE.md) "
- " [DBA\_OBJECT\_USAGE](DBA_OBJECT_USAGE.md) "