---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_INMEMORY_AIMTASKDETAILS.html
tags:
  - oracle
  - 19c
  - reference
---

## 5.119 DBA\_INMEMORY\_AIMTASKDETAILS

`DBA_INMEMORY_AIMTASKDETAILS` displays details for an Automatic In-Memory management task.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER` |  | Number that uniquely identifies a specific automatic IM column store management task |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Owner of the object subject to automatic IM column store management task action |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the object subject to automatic IM column store management task action |
| `SUBOBJECT_NAME` | `VARCHAR2(128)` |  | Name of the subobject subject to automatic IM column store management task action |
| `ACTION` | `VARCHAR2(16)` |  | Action taken on the object |
| `STATE` | `VARCHAR2(10)` |  | Status of the action on the object |

See Also:

[Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=INMEM-GUID-B2473D1F-AEAF-4802-9E28-85B3D823093C) for more information about configuring the Automatic In-Memory feature