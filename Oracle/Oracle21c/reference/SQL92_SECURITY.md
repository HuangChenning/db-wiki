---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SQL92_SECURITY.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.348 SQL92\_SECURITY

`SQL92_SECURITY` specifies whether users must have been granted the `SELECT` privilege on a table in order to specify certain clauses in a `DELETE`, `INSERT`, or `UPDATE` statement.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `TRUE` |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Range of values | `TRUE \| FALSE` |
| Basic | No |

The SQL standard specifies that security administrators should be able to require that users have the `SELECT` privilege on a table when executing a `DELETE`, `INSERT`, or `UPDATE` statement that references table column values in a `RETURNING`, `SET`, or `WHERE` clause.

Values

- `TRUE`
	A user must have the `SELECT` privilege on the target table in order to reference its columns in:
	- The `WHERE` clause of a `DELETE` or `UPDATE` statement
		- The right hand side of an assignment in the `SET` clause of an `UPDATE` statement
		- The `RETURNING` clause of a `DELETE`, `INSERT`, or `UPDATE` statement
- `FALSE`
	- A user with the `DELETE` privilege on the target table of a `DELETE` statement may reference any column of that target table in the `WHERE` clause of the `DELETE` statement.
		- A user with the `UPDATE` privilege on the target table of an `UPDATE` statement may reference any column of that target table in the `WHERE` clause or on the right hand side of any assignment in the `SET` clause of the `UPDATE` statement.
		- A user with the `READ` or `SELECT` privilege on the target table of a `DELETE`, `INSERT`, or `UPDATE` statement may reference any column of that target table in the `RETURNING` clause.