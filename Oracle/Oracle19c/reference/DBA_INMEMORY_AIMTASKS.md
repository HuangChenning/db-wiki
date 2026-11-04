---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_INMEMORY_AIMTASKS.html
tags:
  - oracle
  - 19c
  - reference
---

## 5.120 DBA\_INMEMORY\_AIMTASKS

`DBA_INMEMORY_AIMTASKS` displays information about Automatic In-Memory management tasks.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER` |  | Number that uniquely identifies a specific automatic IM column store management task |
| `CREATION_TIME` | `TIMESTAMP(6)` |  | Creation time of the task |
| `STATE` | `VARCHAR2(7)` |  | State of the task |

See Also:

[Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=INMEM-GUID-B2473D1F-AEAF-4802-9E28-85B3D823093C) for more information about configuring the Automatic In-Memory feature