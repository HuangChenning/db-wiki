---
title: ALL_PROCEDURES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2013.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_PROCEDURES` lists all functions and procedures that are accessible to the current user, along with associated properties. For example, `ALL_PROCEDURES` indicates whether or not a function is pipelined, parallel enabled or an aggregate function. If a function is pipelined or an aggregate function, the associated implementation type (if any) is also identified.

Related Views

- `DBA_PROCEDURES` lists all functions and procedures, along with associated properties.
- `USER_PROCEDURES` lists all functions and procedures owned by the current user, along with associated properties. It does not contain the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the procedure |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object: top-level function, procedure, or package name |
| `PROCEDURE_NAME` | `VARCHAR2(30)` |  | Name of the procedure |
| `OBJECT_ID` | `NUMBER` |  | Object number of the object |
| `SUBPROGRAM_ID` | `NUMBER` |  | Unique subprogram identifier |
| `OVERLOAD` | `VARCHAR2(40)` |  | Overload unique identifier |
| `OBJECT_TYPE` | `VARCHAR2(19)` |  | The typename of the object |
| `AGGREGATE` | `VARCHAR2(3)` |  | Indicates whether the procedure is an aggregate function (`YES`) or not (`NO`) |
| `PIPELINED` | `VARCHAR2(3)` |  | Indicates whether the procedure is a pipelined table function (`YES`) or not (`NO`) |
| `IMPLTYPEOWNER` | `VARCHAR2(30)` |  | Owner of the implementation type, if any |
| `IMPLTYPENAME` | `VARCHAR2(30)` |  | Name of the implementation type, if any |
| `PARALLEL` | `VARCHAR2(3)` |  | Indicates whether the procedure or function is parallel-enabled (`YES`) or not (`NO`) |
| `INTERFACE` | `VARCHAR2(3)` |  | `YES`, if the procedure/function is a table function implemented using the ODCI interface; otherwise `NO` |
| `DETERMINISTIC` | `VARCHAR2(3)` |  | `YES`, if the procedure/function is declared to be deterministic; otherwise `NO` |
| `AUTHID` | `VARCHAR2(12)` |  | Indicates whether the procedure/function is declared to execute as `DEFINER` or `CURRENT_USER` (invoker) |

See Also:

- ["DBA\_PROCEDURES"](statviews_4186.md)
- ["USER\_PROCEDURES"](statviews_5400.md)
- ["ALL\_ARGUMENTS"](statviews_1016.md) for information about the arguments of the functions and procedures that are accessible to the current user