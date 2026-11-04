---
title: SQL92_SECURITY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams249.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Range of values | `true \| false` |

The SQL standard specifies that security administrators should be able to require that users have `SELECT` privilege on a table when executing an `UPDATE` or `DELETE` statement that references table column values in a `WHERE` or `SET` clause. `SQL92_SECURITY` specifies whether users must have been granted the `SELECT` object privilege in order to execute such `UPDATE` or `DELETE` statements.

Values:

- `true`
	The user must have `SELECT` privilege on a column in order to reference it in the `WHERE` clause of a `DELETE` or `UPDATE` statement, on the right hand side of an assignment in the `SET` clause of an `UPDATE` statement.
- `false`
	A user with `DELETE` privilege on the target table of a `DELETE` statement may reference any column of that target table in the `WHERE` clause. A user with `UPDATE` privilege on the target table of an `UPDATE` statement may reference any column of that target in the `WHERE` clause or on the right hand side of any assignment in the `SET` clause of the `UPDATE` statement.