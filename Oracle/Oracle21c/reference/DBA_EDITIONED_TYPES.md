---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_EDITIONED_TYPES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.297 DBA\_EDITIONED\_TYPES

`DBA_EDITIONED_TYPES` lists all types that are editioned by default for every user in the database.

Related View

`USER_EDITIONED_TYPES` lists the types that are editioned by default for the current user. This view does not display the `SCHEMA` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Schema in which the object types is editionable |
| `OBJECT_TYPE` | `VARCHAR2(23)` |  | Object type that is editionable |

See Also:

" [USER\_EDITIONED\_TYPES](USER_EDITIONED_TYPES.md) "