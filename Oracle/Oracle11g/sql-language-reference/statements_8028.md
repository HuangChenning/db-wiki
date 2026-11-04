---
title: DROP RESTORE POINT
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8028.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `DROP` `RESTORE` `POINT` statement to remove a normal restore point or a guaranteed restore point from the database.

- You need not drop normal restore points. The database automatically drops the oldest restore points when necessary, as described in the semantics for [restore\_point](statements_6011.md). However, you can drop a normal restore point if you want to reuse the name.
- Guaranteed restore points are not dropped automatically. Therefore, if you want to remove a guaranteed restore point from the database, then you must do so explicitly using this statement.

See Also:

[CREATE RESTORE POINT](statements_6011.md), [FLASHBACK DATABASE](statements_9011.md), and [FLASHBACK TABLE](statements_9012.md) for information on creating and using restore points

Prerequisites

To drop a normal restore point, you must have either the `SELECT` `ANY` `DICTIONARY` or the `FLASHBACK` `ANY` `TABLE` system privilege. To drop a guaranteed restore point, you must have the `SYSDBA` system privilege.

Semantics

restore\_point Specify the name of the restore point you want to drop.

Examples

Dropping a Restore Point: Example The following example drops the `good_data` restore point, which was created in ["Creating and Using a Restore Point: Example"](statements_6011.md):

```
DROP RESTORE POINT good_data;
```