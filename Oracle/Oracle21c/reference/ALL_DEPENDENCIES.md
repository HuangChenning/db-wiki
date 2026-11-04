---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_DEPENDENCIES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.165 ALL\_DEPENDENCIES

`ALL_DEPENDENCIES` describes dependencies between procedures, packages, functions, package bodies, and triggers accessible to the current user, including dependencies on views created without any database links. This view does not display the `SCHEMAID` column.

Related Views

- `DBA_DEPENDENCIES` describes all dependencies between objects in the database. This view does not display the `SCHEMAID` column.
- `USER_DEPENDENCIES` describes dependencies between objects in the current user's schema. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `TYPE` | `VARCHAR2(18)` |  | Type of the object |
| `REFERENCED_OWNER` | `VARCHAR2(128)` |  | Owner of the referenced object (remote owner if remote object) |
| `REFERENCED_NAME` | `VARCHAR2(128)` |  | Name of the referenced object |
| `REFERENCED_TYPE` | `VARCHAR2(18)` |  | Type of the referenced object |
| `REFERENCED_LINK_NAME` | `VARCHAR2(128)` |  | Name of the link to the parent object (if remote) |
| `DEPENDENCY_TYPE` | `VARCHAR2(4)` |  | Indicates whether the dependency is a `REF` dependency (`REF`) or not (`HARD`) |

See Also:

- " [DBA\_DEPENDENCIES](DBA_DEPENDENCIES.md) "
- " [USER\_DEPENDENCIES](USER_DEPENDENCIES.md) "