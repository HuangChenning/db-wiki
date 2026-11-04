---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_WORKLOAD_USER_MAP.html
tags:
  - oracle
  - 12c
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

See Also:

" [DBA\_WORKLOAD\_REPLAYS](DBA_WORKLOAD_REPLAYS.md) "