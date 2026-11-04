---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/TABLE_EXPORT_OBJECTS.html
tags:
  - oracle
  - 12c
  - reference
---

`TABLE_EXPORT_OBJECTS` lists simple path names for some of the object types belonging to a Data Pump schema export, which is invoked using the `TABLES` parameter on the `expdp` command.

Users of the Data Pump Export and Import utilities can query this view to determine valid values for the `EXCLUDE` and `INCLUDE` parameters.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_PATH` | `VARCHAR2(200)` | `NOT NULL` | Simple path name for the object type |