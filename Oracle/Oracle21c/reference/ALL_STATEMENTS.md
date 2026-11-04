---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_STATEMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.87 ALL\_STATEMENTS

`ALL_STATEMENTS` describes all SQL statements in stored PL/SQL objects accessible to the user.

Related Views

- `DBA_STATEMENTS` describes SQL statements in stored PL/SQL objects accessible to `SYS`.
- `USER_STATEMENTS` describes SQL statements in stored PL/SQL objects accessible to the user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the statement |
| `SIGNATURE` | `VARCHAR2(32)` |  | Signature of the statement. Every statement type has a unique PL/Scope signature that identifies that instance of th statement. |
| `TYPE` | `VARCHAR2(17)` |  | Type of the statement. Statement types correspond to statements that can be used in PL/SQL to execute or otherwise interact with SQL:  - `SELECT` - `UPDATE` - `INSERT` - `DELETE` - `MERGE` - `CLOSE` - `FETCH` - `OPEN` - `SAVEPOINT` - `COMMIT` - `SET_TRANSACTION` - `ROLLBACK` - `LOCK_TABLE` - `EXECUTE_IMMEDIATE` |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object where the statement usage occurred |
| `OBJECT_TYPE` | `VARCHAR2(12)` |  | Type of the object where the statement usage occurred |
| `USAGE_ID` | `NUMBER` |  | Unique key for a statement usage within the object |
| `LINE` | `NUMBER` |  | Line number of the statement usage |
| `COL` | `NUMBER` |  | Column number of the statement usage |
| `USAGE_CONTEXT_ID` | `NUMBER` |  | Context USAGE\_ID of an statement usage |
| `SQL_ID` | `VARCHAR2(13)` |  | SQL ID of the SQL statement. The value of this column is null for statements that do not have a SQL ID. |
| `HAS_HINT` | `VARCHAR2(3)` |  | `YES` if the SQL statement contains a hint, `NO` otherwise.  If a hint appears inside of a subquery, then `HAS_HINT` will be `YES` for the containing statement or statements of the subquery as well as for the subquery itself. |
| `HAS_INTO_BULK` | `VARCHAR2(3)` |  | Indicates whether the statement contains a `BULK_COLLECT` clause (`YES`) or not (`NO`) |
| `HAS_INTO_RETURNING` | `VARCHAR2(3)` |  | Indicates whether the statement contains a `RETURNING_INTO` clause (`YES`) or not (`NO`) |
| `HAS_INTO_RECORD` | `VARCHAR2(3)` |  | Indicates whether the statement returns results into a PL/SQL record (`YES`) or not (`NO`) |
| `HAS_CURRENT_OF` | `VARCHAR2(3)` |  | Indicates whether the statement contains a `HAS_CURRENT_OF` clause (`YES`) or not (`NO`) |
| `HAS_FOR_UPDATE` | `VARCHAR2(3)` |  | Indicates whether the statement contains a `HAS_FOR_UPDATE` clause (`YES`) or not (`NO`) |
| `HAS_IN_BINDS` | `VARCHAR2(3)` |  | Indicates whether the statement contains an `IN_BINDS` clause (`YES`) or not (`NO`) |
| `TEXT` | `VARCHAR2(4000)` |  | The normalized form of the statement, when the statement has a normalized form. These are typically the same statements that have a SQL ID.  The column value is null when the statement does not have a normalized form. |
| `FULL_TEXT` | `CLOB` |  | Clob text of the SQL statement |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root) |

See Also:

- " [DBA\_STATEMENTS](DBA_STATEMENTS.md) "
- " [USER\_STATEMENTS](USER_STATEMENTS.md) "