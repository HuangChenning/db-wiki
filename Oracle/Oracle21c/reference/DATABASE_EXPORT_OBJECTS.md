---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DATABASE_EXPORT_OBJECTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.186 DATABASE\_EXPORT\_OBJECTS

`DATABASE_EXPORT_OBJECTS` lists simple path names for some of the object types belonging to a full Data Pump export, which is invoked using the `FULL=Y` parameter on the `expdp` command.

Users of the Data Pump Export and Import utilities can query this view to determine valid values for the `EXCLUDE` and `INCLUDE` parameters.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_PATH` | `VARCHAR2(200)` | `NOT NULL` | Simple path name for the object type |