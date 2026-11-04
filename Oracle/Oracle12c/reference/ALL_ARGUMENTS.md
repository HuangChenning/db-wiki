---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_ARGUMENTS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_ARGUMENTS` lists the arguments of the functions and procedures that are accessible to the current user.

Note:

Starting with Oracle Database 12c release 1 (12.1.0.2), this view omits procedures with no arguments. Prior to Oracle Database 12c release 1 (12.1.0.2), a procedure with no arguments was presented as a single row in this view.

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
| `ARGUMENT_NAME` | `VARCHAR2(128)` |  | If the argument is a scalar type, then the argument name is the name of the argument. A null argument name is used to denote a function return. If the function return or argument is a composite type, this view will have one row for each attribute of the composite type. Attributes are recursively expanded if they are composite.  The meanings of `ARGUMENT_NAME`, `POSITION`, `SEQUENCE`, and `DATA_LEVEL` are interdependent. Together, as a tuple, they represent a node of a flattened tree.  `ARGUMENT_NAME` can refer to any of the following:  - Return type, if `ARGUMENT_NAME` is null and `DATA_LEVEL` = 0 - The argument that appears in the argument list if `ARGUMENT_NAME` is not null and `DATA_LEVEL` = 0 - Attribute name of the composite type if `ARGUMENT_NAME` is not null and `DATA_LEVEL` > 0; - A collection element type if `ARGUMENT_NAME` is null and `DATA_LEVEL` > 0; |
| `POSITION` | `NUMBER` | `NOT NULL ` | If `DATA_LEVEL` is zero, then this column holds the position of this item in the argument list, or zero for a function return value.If `DATA_LEVEL` is greater than zero, then this column holds the position of this item with respect to its siblings at the same `DATA_LEVEL`. So, for a referenced record field, this is the index of the field within the record. For a referenced collection element, this is 1 (because collection elements do not have siblings.) |
| `SEQUENCE` | `NUMBER` | `NOT NULL ` | Defines the sequential order of the argument and its attributes. Argument sequence starts from 1. Return type and its recursively expanded (preorder tree walk) attributes will come first, and each argument with its recursively expanded (preorder tree walk) attributes will follow. |
| `DATA_LEVEL` | `NUMBER` | `NOT NULL ` | Nesting depth of the argument for composite types |
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
| `PLS_TYPE` | `VARCHAR2(128)` |  | For numeric arguments, the name of the PL/SQL type of the argument. Null otherwise. |
| `CHAR_LENGTH` | `NUMBER` |  | Character limit for string datatypes |
| `CHAR_USED` | `VARCHAR2(1)` |  | Indicates whether the byte limit (`B`) or char limit (`C`) is official for the string |
| `ORIGIN_CON_ID` | `VARCHAR2(256)` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root) |

Note:

To list the procedure names in a package, use the `ALL_PROCEDURES` view.

See Also:

- " [DBA\_ARGUMENTS](DBA_ARGUMENTS.md) "
- " [USER\_ARGUMENTS](USER_ARGUMENTS.md) "
- " [ALL\_PROCEDURES](ALL_PROCEDURES.md) " for information about the functions and procedures that are accessible to the current user