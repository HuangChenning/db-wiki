---
title: DELETE Statement Extension
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/delete_statement.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The PL/SQL extension to the `where_clause` of the SQL `DELETE` statement lets you specify a `CURRENT` `OF` clause, which restricts the `DELETE` statement to the current row of the specified cursor. For information about the `CURRENT` `OF` clause, see ["UPDATE Statement Extensions"](update_statement.md).

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8005.htm#SQLRF01505) for the syntax of the SQL `DELETE` statement