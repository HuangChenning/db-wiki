---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ARGUMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.80 ALL\_ARGUMENTS

`ALL_ARGUMENTS` lists the arguments of the functions and procedures that are accessible to the current user.

Note:

The following changes have been made to this view:

- Starting with Oracle Database 12c release 1 (12.1.0.2), this view omits procedures with no arguments. Prior to Oracle Database 12c release 1 (12.1.0.2), a procedure with no arguments was presented as a single row in this view.
- Starting with Oracle Database 18c, this view displays only one row for an argument that is a composite type. Prior to Oracle Database 18c, this view displayed multiple rows for composite types.
	To obtain information about composite type arguments, use the value of the `TYPE_NAME` column in this view to query the `ALL_PLSQL_TYPES`, `ALL_PLSQL_TYPE_ATTRS`, and `ALL_PLSQL_COLL_TYPES` views, which fully describe composite types.

See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD-GUID-543498D6-3799-4217-9BE3-4BB8630FC32D) for more information about these changes.

Related Views

- `DBA_ARGUMENTS` lists the arguments of the functions and procedures that are available in the database.
- `USER_ARGUMENTS` lists the arguments of the functions and procedures that are owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL ` | Owner of the object |
| `OBJECT_NAME ` | `VARCHAR2(128)` |  | Name of the procedure or function |
| `PACKAGE_NAME` | `VARCHAR2(128)` |  | Name of the package |
| `OBJECT_ID ` | `NUMBER` | `NOT NULL ` | Object number of the object |
| `OVERLOAD` | `VARCHAR2(40)` |  | Indicates the `n` th overloading ordered by its appearance in the source; otherwise, it is NULL. |
| `SUBPROGRAM_ID` | `NUMBER` |  | Unique subprogram identifier |
| `ARGUMENT_NAME` | `VARCHAR2(128)` |  | Name of the argument  A null argument name is used to denote a function return. |
| `POSITION` | `NUMBER` | `NOT NULL ` | This column holds the position of this item in the argument list, or `0` for a function return value. |
| `SEQUENCE` | `NUMBER` | `NOT NULL ` | Defines the sequential order of the argument. Argument sequence starts from 1. Return type comes first, and each argument will follow. |
| `DATA_LEVEL` | `NUMBER` | `NOT NULL ` | Nesting depth of the argument for composite types  Note: Starting with Oracle Database 18c, the value of this column is always `0`, because this view displays only one row for each argument. This view no longer displays multiple rows for composite type arguments. |
| `DATA_TYPE` | `VARCHAR2(30)` |  | Datatype of the argument |
| `DEFAULTED` | `VARCHAR2(1)` |  | Specifies whether or not the argument is defaulted |
| `DEFAULT_VALUE` | `LONG` |  | Reserved for future use |
| `DEFAULT_LENGTH` | `NUMBER` |  | Reserved for future use |
| `IN_OUT` | `VARCHAR2(9)` |  | Direction of the argument:  - `IN` - `OUT` - `IN/OUT` |
| `DATA_LENGTH` | `NUMBER` |  | Length of the column (in bytes) |
| `DATA_PRECISION` | `NUMBER` |  | Length in decimal digits (`NUMBER`) or binary digits (`FLOAT`) |
| `DATA_SCALE` | `NUMBER` |  | Digits to the right of the decimal point in a number |
| `RADIX ` | `NUMBER` |  | Argument radix for a number |
| `CHARACTER_SET_NAME` | `VARCHAR2(44)` |  | Character set name for the argument |
| `TYPE_OWNER` | `VARCHAR2(128)` |  | Owner of the type of the argument |
| `TYPE_NAME` | `VARCHAR2(128)` |  | Name of the type of the argument. If the type is a package local type (that is, it is declared in a package specification), then this column displays the name of the package. |
| `TYPE_SUBNAME` | `VARCHAR2(128)` |  | Relevant only for package local types. Displays the name of the type declared in the package identified in the `TYPE_NAME` column. |
| `TYPE_LINK` | `VARCHAR2(128)` |  | Relevant only for package local types when the package identified in the `TYPE_NAME` column is a remote package. This column displays the database link used to refer to the remote package. |
| `TYPE_OBJECT_TYPE` | `VARCHAR2(7)` |  | Displays the type of the type described by the `TYPE_OWNER`, `TYPE_NAME`, and `TYPE_SUBNAME` columns. Possible values are:  - `TABLE` - `VIEW` - `PACKAGE` - `TYPE` |
| `PLS_TYPE` | `VARCHAR2(128)` |  | For numeric arguments, the name of the PL/SQL type of the argument. Null otherwise. |
| `CHAR_LENGTH` | `NUMBER` |  | Character limit for string datatypes |
| `CHAR_USED` | `VARCHAR2(1)` |  | Indicates whether the byte limit (`B`) or char limit (`C`) is official for the string |
| `ORIGIN_CON_ID` | `VARCHAR2(256)` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root) |

Note:

To list the procedure names in a package, use the `ALL_PROCEDURES` view.