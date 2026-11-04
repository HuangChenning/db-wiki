---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_IDENTIFIERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.228 ALL\_IDENTIFIERS

`ALL_IDENTIFIERS` displays information about the identifiers in the stored objects accessible to the current user.

Related Views

- `DBA_IDENTIFIERS` displays information about the identifiers in all stored objects in the database.
- `USER_IDENTIFIERS` displays information about the identifiers in the stored objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the identifier |
| `NAME` | `VARCHAR2(128)` |  | Name of the identifier |
| `SIGNATURE` | `VARCHAR2(32)` |  | Signature of the identifier |
| `TYPE` | `VARCHAR2(18)` |  | Type of the identifier.  For SQL identifiers, the types include:  - `TABLE` - `VIEW` - `SEQUENCE` - `ALIAS` - `COLUMN` - `MATERIALIZED VIEW` - `OPERATOR`  For PL/SQL identifiers, the types include:  - `FUNCTION` - `PROCEDURE` - `PACKAGE` |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object where the identifier action occurred |
| `OBJECT_TYPE` | `VARCHAR2(13)` |  | Type of the object where the identifier action occurred |
| `USAGE` | `VARCHAR2(11)` |  | Type of the identifier usage:  - `DECLARATION` - `DEFINITION` - `CALL` - `REFERENCE` - `ASSIGNMENT` |
| `USAGE_ID` | `NUMBER` |  | Unique key for the identifier usage within the object |
| `LINE` | `NUMBER` |  | Line number of the identifier action |
| `COL` | `NUMBER` |  | Column number of the identifier action |
| `USAGE_CONTEXT_ID` | `NUMBER` |  | Context `USAGE_ID` of the identifier usage |
| `CHARACTER_SET` | `VARCHAR2(10)` |  | Contains the value of the `character set` clause when it is used in a variable identifier declaration. These are the possible values when the character set is derived from another variable identifier: - `CHAR_CS` - `NCHAR_CS` - `IDENTIFIER` |
| `ATTRIBUTE` | `VARCHAR2(7)` |  | Column contains the attribute value when `%attribute` is used in a variable declaration. Possible values: - `ROWTYPE` - `TYPE` - `CHARSET` |
| `CHAR_USED` | `VARCHAR2(4)` |  | Contains the type of the length constraint when it is used in a string length constraint declaration. Possible values: - `CHAR` - `BYTE` |
| `LENGTH` | `NUMBER` |  | Contains the numeric length constraint value for a string length constraint declaration |
| `PRECISION` | `NUMBER` |  | Contains the numeric precision when it is used in a variable declaration |
| `PRECISION2` | `NUMBER` |  | Contains the numeric second precision value (for instance, interval types) used in a variable declaration |
| `SCALE` | `NUMBER` |  | Contains the numeric scale value used in a variable declaration. |
| `LOWER_RANGE` | `NUMBER` |  | Contains the numeric lower range value used by a variable declaration with a range constraint |
| `UPPER_RANGE` | `NUMBER` |  | Contains the numeric upper range value used by a variable declaration with a range constraint |
| `NULL_CONSTRAINT` | `VARCHAR2(8)` |  | This column is set when a `NULL` constraint is used by a variable declaration. Possible values: - `NULL` - `NOT NULL` |
| `SQL_BUILTIN` | `VARCHAR2(3)` |  | Is set to `YES` when an identifier is a SQL builtin used in a SQL statement issued from PL/SQL. Otherwise, this column is set to `NO`. |
| `IMPLICIT` | `VARCHAR2(3)` |  | Indicates whether the identifier is an implicit identifier that does not appear in the source (`YES`) or not (`NO`) |
| `DECLARED_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object in which this identifier was declared |
| `DECLARED_OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object in which this identifier was declared |
| `DECLARED_OBJECT_TYPE` | `VARCHAR2(12)` |  | Type of the object in which this identifier was declared |
| `ORIGIN_CON_ID` | `VARCHAR2(256)` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root) |

See Also:

- " [DBA\_IDENTIFIERS](DBA_IDENTIFIERS.md) "
- " [USER\_IDENTIFIERS](USER_IDENTIFIERS.md) "