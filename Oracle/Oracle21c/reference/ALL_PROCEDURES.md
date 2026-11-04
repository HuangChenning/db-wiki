---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_PROCEDURES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.17 ALL\_PROCEDURES

`ALL_PROCEDURES` lists all functions and procedures that are accessible to the current user, along with associated properties. For example, `ALL_PROCEDURES` indicates whether or not a function is pipelined, parallel enabled or an aggregate function. If a function is pipelined or an aggregate function, the associated implementation type (if any) is also identified.

Related Views

- `DBA_PROCEDURES` lists all functions and procedures available in the database, along with associated properties.
- `USER_PROCEDURES` lists all functions and procedures owned by the current user, along with associated properties. It does not contain the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the procedure |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the object: top-level function, procedure, or package name |
| `PROCEDURE_NAME` | `VARCHAR2(128)` |  | Name of the procedure |
| `OBJECT_ID` | `NUMBER` |  | Object number of the object |
| `SUBPROGRAM_ID` | `NUMBER` |  | Unique subprogram identifier |
| `OVERLOAD` | `VARCHAR2(40)` |  | Overload unique identifier |
| `OBJECT_TYPE` | `VARCHAR2(13)` |  | The typename of the object |
| `AGGREGATE` | `VARCHAR2(3)` |  | Indicates whether the procedure is an aggregate function (`YES`) or not (`NO`) |
| `PIPELINED` | `VARCHAR2(3)` |  | Indicates whether the procedure is a pipelined table function (`YES`) or not (`NO`) |
| `IMPLTYPEOWNER` | `VARCHAR2(128)` |  | Owner of the implementation type, if any |
| `IMPLTYPENAME` | `VARCHAR2(128)` |  | Name of the implementation type, if any |
| `PARALLEL` | `VARCHAR2(3)` |  | Indicates whether the procedure or function is parallel-enabled (`YES`) or not (`NO`) |
| `INTERFACE` | `VARCHAR2(3)` |  | `YES`, if the procedure/function is a table function implemented using the ODCI interface; otherwise `NO` |
| `DETERMINISTIC` | `VARCHAR2(3)` |  | `YES`, if the procedure/function is declared to be deterministic; otherwise `NO` |
| `AUTHID` | `VARCHAR2(12)` |  | Indicates whether the procedure/function is declared to execute as `DEFINER` or `CURRENT_USER` (invoker) |
| `RESULT_CACHE` | `VARCHAR2(3)` |  | Indicates whether the function is result–cached (`YES`) or not (`NO`) |
| `ORIGIN_CON_ID` | `VARCHAR2(256)` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root) |
| `POLYMORPHIC` | `VARCHAR2(5)` |  | The type of polymorphic table function:  - `ROW` - `TABLE` - `LEAF` - `NULL` |
| `SQL_MACRO` <sup>Foot 1</sup> | `VARCHAR2(6)` |  | Indicates whether the procedure is a SQL macro. Possible values:  - `SCALAR`: The procedure is a SQL macro for a scalar expression - `TABLE`: The procedure is a SQL macro for a table expression - `NULL`: The procedure is not a SQL macro |
| `BLOCKCHAIN` <sup>Foot 1</sup> | `VARCHAR2(3)` |  | For internal use only |
| `BLOCKCHAIN_MANDATORY_VOTES` <sup>Foot 1</sup> | `VARCHAR2(4000)` |  | For internal use only |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.

See Also:

- " [DBA\_PROCEDURES](DBA_PROCEDURES.md) "
- " [USER\_PROCEDURES](USER_PROCEDURES.md) "
- " [ALL\_ARGUMENTS](ALL_ARGUMENTS.md) " for information about the arguments of the functions and procedures that are accessible to the current user