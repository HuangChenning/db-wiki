---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_IDENTIFIERS.html
tags:
  - oracle
  - 12c
  - reference
---

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
| `ORIGIN_CON_ID` | `VARCHAR2(256)` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root) |

See Also:

- " [DBA\_IDENTIFIERS](DBA_IDENTIFIERS.md) "
- " [USER\_IDENTIFIERS](USER_IDENTIFIERS.md) "