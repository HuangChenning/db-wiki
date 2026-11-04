---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/TS_PITR_OBJECTS_TO_BE_DROPPED.html
tags:
  - oracle
  - 12c
  - reference
---

`TS_PITR_OBJECTS_TO_BE_DROPPED` lists all objects lost as a result of performing tablespace point-in-time recovery.

This view applies only to the tablespace point-in-time recovery feature.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | The owner of the object |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | The name of the object that will be lost as a result of undergoing tablespace point-in-time recovery |
| `CREATION_TIME` | `DATE` | `NOT NULL` | Creation timestamp of the object |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing the object |

See Also:

[Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=BRADV009) for more information about tablespace point-in-time recovery