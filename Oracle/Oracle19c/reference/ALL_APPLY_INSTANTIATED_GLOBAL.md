---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_APPLY_INSTANTIATED_GLOBAL.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.64 ALL\_APPLY\_INSTANTIATED\_GLOBAL

`ALL_APPLY_INSTANTIATED_GLOBAL` displays information for the current user about databases for which an instantiation SCN has been set.

Related View

`DBA_APPLY_INSTANTIATED_GLOBAL` displays information about databases for which an instantiation SCN has been set.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SOURCE_DATABASE` | `VARCHAR2(128)` | `NOT NULL` | Name of the database that was instantiated |
| `INSTANTIATION_SCN` | `NUMBER` |  | Instantiation SCN for the database. Only changes committed after this SCN are applied by an apply process. |
| `APPLY_DATABASE_LINK` | `VARCHAR2(128)` |  | Database link to which changes are applied. If null, then changes are applied to the local database. |
| `SOURCE_ROOT_NAME` | `VARCHAR2(128)` |  | The global name of the source root database |

See Also:

" [DBA\_APPLY\_INSTANTIATED\_GLOBAL](DBA_APPLY_INSTANTIATED_GLOBAL.md) "