---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_APPLY_HANDLE_COLLISIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.71 ALL\_APPLY\_HANDLE\_COLLISIONS

`ALL_APPLY_HANDLE_COLLISIONS` provides details about apply handlers for collisions on objects visible to the user at the table level.

Related View

`DBA_APPLY_HANDLE_COLLISIONS` provides details about apply handlers for collisions at the table level.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APPLY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the apply process |
| `OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the target object |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the target object |
| `SOURCE_OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Source database owner of the object |
| `SOURCE_OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Source database name of the object |
| `ENABLED` | `VARCHAR2(1)` | `NOT NULL` | State of the collision handlers: `Y` for enabled, `N` for disabled |
| `SET_BY` | `VARCHAR2(10)` |  | Entity that set up the handler:  - `USER` - `GOLDENGATE` |

See Also:

" [DBA\_APPLY\_HANDLE\_COLLISIONS](DBA_APPLY_HANDLE_COLLISIONS.md) "