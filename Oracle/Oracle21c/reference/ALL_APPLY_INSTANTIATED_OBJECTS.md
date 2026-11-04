---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_APPLY_INSTANTIATED_OBJECTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.73 ALL\_APPLY\_INSTANTIATED\_OBJECTS

`ALL_APPLY_INSTANTIATED_OBJECTS` displays information about objects accessible to the current user for which an instantiation SCN has been set.

Related View

`DBA_APPLY_INSTANTIATED_OBJECTS` displays information about objects for which an instantiation SCN has been set.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SOURCE_DATABASE` | `VARCHAR2(128)` | `NOT NULL` | Name of the database where the object originated |
| `SOURCE_OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object at the source database |
| `SOURCE_OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object at the source database |
| `SOURCE_OBJECT_TYPE` | `VARCHAR2(11)` |  | Type of the object at the source database |
| `INSTANTIATION_SCN` | `NUMBER` |  | Instantiation SCN for the object. Only changes committed after this SCN are applied by an apply process. |
| `IGNORE_SCN` | `NUMBER` |  | SCN below which the instantiation SCN cannot be set. This value corresponds to the SCN value at the source database at the time when the object was prepared for instantiation. |
| `APPLY_DATABASE_LINK` | `VARCHAR2(128)` |  | Database link to which changes are applied. If null, then changes are applied to the local database. |
| `SOURCE_ROOT_NAME` | `VARCHAR2(128)` |  | The global name of the source root database |

See Also:

" [DBA\_APPLY\_INSTANTIATED\_OBJECTS](DBA_APPLY_INSTANTIATED_OBJECTS.md) "