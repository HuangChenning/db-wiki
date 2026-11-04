---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/SQL92_SECURITY.html
tags:
  - oracle
  - 12c
  - reference
---

`SQL92_SECURITY` specifies whether users must have been granted the `SELECT` privilege on a table to execute an `UPDATE` or `DELETE` statement that references table column values in a `WHERE` or `SET` clause.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |

The SQL standard specifies that security administrators should be able to require that users have `SELECT` privilege on a table when executing an `UPDATE` or `DELETE` statement that references table column values in a `WHERE` or `SET` clause.

Values

- `true`
	The user must have `SELECT` privilege on a column to reference it in the `WHERE` clause of a `DELETE` or `UPDATE` statement, on the right hand side of an assignment in the `SET` clause of an `UPDATE` statement.
- `false`
	A user with `DELETE` privilege on the target table of a `DELETE` statement may reference any column of that target table in the `WHERE` clause. A user with `UPDATE` privilege on the target table of an `UPDATE` statement may reference any column of that target in the `WHERE` clause or on the right hand side of any assignment in the `SET` clause of the `UPDATE` statement.