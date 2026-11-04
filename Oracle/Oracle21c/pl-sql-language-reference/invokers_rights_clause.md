---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/invokers_rights_clause.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

Specifies the `AUTHID` property of a stored PL/SQL subprogram. The `AUTHID` property affects the name resolution and privilege checking of SQL statements that the unit issues at run time.

Syntax

Semantics

invoker\_rights\_clause

When it appears in the package declaration, it specifies the `AUTHID` property of functions and procedures in the package, and of the explicit cursors declared in the package specification.

When it appears in a standalone function declaration, it specifies the `AUTHID` property of the function.

When it appears in a standalone procedure declaration, it specifies the `AUTHID` property of the procedure.

The invoker\_rights\_clause can appear only once in a subprogram declaration.

When it appears in an ADT, it specifies the `AUTHID` property of the member functions and procedures of the ADT.

Restrictions on invoker\_rights\_clause

The following restrictions apply for types:

- This clause is valid only for ADTs, not for a nested table or `VARRAY` type.
- You can specify this clause for clarity if you are creating a subtype. However, a subtype inherits the `AUTHID` property of its supertype, so you cannot specify a different value than was specified for the supertype.
- If the supertype was created with `AUTHID` `DEFINER`, then you must create the subtype in the same schema as the supertype.
- You cannot specify the `AUTHID` property of SQL macros. They behave like IR units.