---
title: Cursor Variable Declaration
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/cursor_variable.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

A cursor variable is like an explicit cursor that is not limited to one query.

To create a cursor variable, either declare a variable of the predefined type `SYS_REFCURSOR` or define a `REF` `CURSOR` type and then declare a variable of that type.

Restrictions on Cursor Variables

- You cannot declare a cursor variable in a package specification.
	That is, a package cannot have a public cursor variable (a cursor variable that can be referenced from outside the package).
- You cannot store the value of a cursor variable in a collection or database column.
- You cannot use comparison operators to test cursor variables for equality, inequality, or nullity.
- Using a cursor variable in a server-to-server remote procedure call (RPC) causes an error. However, you can use a cursor variable in a server-to-server RPC if the remote database is a non-Oracle database accessed through a Procedural Gateway.
- You cannot use LOB parameters in a server-to-server RPC.

Topics

- Syntax
- Semantics
- Examples
- Related Topics

Semantics

ref\_cursor\_type\_definition

type

Name of the `REF` `CURSOR` type that you are defining.

RETURN

Specifies the data type of the value that the cursor variable returns.

Specify `RETURN` to define a strong `REF` `CURSOR` type. Omit `RETURN` to define a weak `REF` `CURSOR` type. For information about strong and weak `REF` `CURSOR` types, see ["Creating Cursor Variables"](static.md).

db\_table\_or\_view

Name of a database table or view, which must be accessible when the declaration is elaborated.

cursor

Name of a previously declared explicit cursor.

cursor\_variable

Name of a previously declared cursor variable.

record

Name of a user-defined record.

record\_type

Name of a user-defined type that was defined with the data type specifier `RECORD`.

ref\_cursor\_type

Name of a user-defined type that was defined with the data type specifier `REF` `CURSOR`.

cursor\_variable\_declaration

cursor\_variable

Name of the cursor variable that you are declaring.

type

Type of the cursor variable that you are declaring—either `SYS_REFCURSOR` or the name of the `REF` `CURSOR` type that you defined previously.

`SYS_REFCURSOR` is a weak type. For information about strong and weak `REF` `CURSOR` types, see ["Creating Cursor Variables"](static.md).

Examples

- [Example 6-24, "Cursor Variable Declarations"](static.md)
- [Example 6-25, "Cursor Variable with User-Defined Return Type"](static.md)
- [Example 6-28, "Variable in Cursor Variable Query—No Result Set Change"](static.md)
- [Example 6-29, "Variable in Cursor Variable Query—Result Set Change"](static.md)
- [Example 6-30, "Procedure to Open Cursor Variable for One Query"](static.md)
- [Example 6-31, "Opening Cursor Variable for Chosen Query (Same Return Type)"](static.md)
- [Example 6-32, "Opening Cursor Variable for Chosen Query (Different Return Types)"](static.md)
- [Example 6-33, "Cursor Variable as Host Variable in Pro\*C Client Program"](static.md)

Related Topics

In this chapter:

- ["CLOSE Statement"](close_statement.md)
- ["Named Cursor Attribute"](cursor_attribute.md)
- ["Explicit Cursor Declaration and Definition"](explicit_cursor.md)
- ["FETCH Statement"](fetch_statement.md)
- ["OPEN FOR Statement"](openfor_statement.md)
- ["%ROWTYPE Attribute"](rowtype_attribute.md)
- ["%TYPE Attribute"](type_attribute.md)

In other chapters:

- ["Cursor Variables"](static.md)
- ["Passing CURSOR Expressions to Pipelined Table Functions"](tuning.md)