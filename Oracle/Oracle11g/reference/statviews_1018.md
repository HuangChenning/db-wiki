---
title: ALL_ASSOCIATIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1018.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_ASSOCIATIONS` describes user-defined statistics associated with objects accessible to the current user.

Related Views

- `DBA_ASSOCIATIONS` describes all user-defined statistics in the database.
- `USER_ASSOCIATIONS` describes user-defined statistics associated with objects owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object for which the association is being defined |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object for which the association is being defined |
| `COLUMN_NAME` | `VARCHAR2(30)` |  | Column name in the object for which the association is being defined |
| `OBJECT_TYPE` | `VARCHAR2(9)` |  | Kind of object with which statistics are being associated: column, type, package or function, indextype, or domain index. |
| `STATSTYPE_SCHEMA` | `VARCHAR2(30)` |  | Owner of the statistics type |
| `STATSTYPE_NAME` | `VARCHAR2(30)` |  | Name of statistics type that contains the cost, selectivity or statistics functions |
| `DEF_SELECTIVITY` | `NUMBER` |  | Default selectivity of the object, if any |
| `DEF_CPU_COST` | `NUMBER` |  | Default CPU cost of the object, if any |
| `DEF_IO_COST` | `NUMBER` |  | Default I/O cost of the object, if any |
| `DEF_NET_COST` | `NUMBER` |  | Default networking cost of the object, if any |
| `INTERFACE_VERSION` | `NUMBER` |  | Identifies the version number of the `ODCIStats` interface. Value is `1` for statistics type implementing Oracle8i 8.1; `0` for types implementing Oracle9i 9.0.0. |
| `MAINTENANCE_TYPE` | `VARCHAR2(14)` |  | Specifies whether the object is system-managed or user-managed |

See Also:

- ["DBA\_ASSOCIATIONS"](statviews_3069.md)
- ["USER\_ASSOCIATIONS"](statviews_5230.md)