---
title: "V$OBJECT_USAGE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2079.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$OBJECT_USAGE` displays statistics about index usage gathered from the database for the indexes owned by the current user. You can use this view to monitor index usage. All indexes that have been used at least once can be monitored and displayed in this view.

| Column | Datatype | Description |
| --- | --- | --- |
| `INDEX_NAME` | `VARCHAR2(30)` | Index name in sys.obj$.name |
| `TABLE_NAME` | `VARCHAR2(30)` | Table name in sys.obj$.name |
| `MONITORING` | `VARCHAR2(3)` | `YES` \| `NO` |
| `USED` | `VARCHAR2(3)` | `YES` \| `NO` |
| `START_MONITORING` | `VARCHAR2(19)` | Start monitoring time in `sys.object_stats.start_monitoring` |
| `END_MONITORING` | `VARCHAR2(19)` | End monitoring time in `sys.object_stats.end_monitoring` |

Note:

To view the information in the `V$OBJECT_USAGE` view, you must be connected as the user owner of the objects you want to monitor, otherwise you might not find the monitoring information you are looking for.