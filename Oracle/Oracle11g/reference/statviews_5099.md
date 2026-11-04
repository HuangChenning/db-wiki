---
title: DBA_WORKLOAD_USER_MAP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5099.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_WORKLOAD_USER_MAP` contains all the mappings ever done until they are removed at some point.

The mappings are stored in a table made public through this view.

To remove old mappings, execute this statement:

```
SQL> delete * from DBA_WORKLOAD_USER_MAP;
```

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REPLAY_ID` | `NUMBER` |  | This is a foreign key to the `ID` column in the `DBA_WORKLOAD_REPLAYS` view |
| `SCHEDULE_CAP_ID` | `NUMBER` |  | The ID of a capture in the schedule |
| `CAPTURE_USER` | `VARCHAR2(4000)` | `NOT NULL` | The user name during the time of the workload capture |
| `REPLAY_USER` | `VARCHAR2(4000)` |  | The user name to which the captured user should be remapped during replay. If the `REPLAY_USER` is null, the `CAPTURE_USER` is used during replay. In other words, the original user is used. |

Note:

This view is available starting with Oracle Database 11g Release 2 (11.2.0.4).

See Also:

["DBA\_WORKLOAD\_REPLAYS"](statviews_5096.md)