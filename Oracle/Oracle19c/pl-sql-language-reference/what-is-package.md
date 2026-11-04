---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/what-is-package.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## What is a Package?

A package is a schema object that groups logically related PL/SQL types, variables, constants, subprograms, cursors, and exceptions. A package is compiled and stored in the database, where many applications can share its contents.

A package always has a specification, which declares the public items that can be referenced from outside the package.

If the public items include cursors or subprograms, then the package must also have a body. The body must define queries for public cursors and code for public subprograms. The body can also declare and define private items that cannot be referenced from outside the package, but are necessary for the internal workings of the package. Finally, the body can have an initialization part, whose statements initialize variables and do other one-time setup steps, and an exception-handling part. You can change the body without changing the specification or the references to the public items; therefore, you can think of the package body as a black box.

In either the package specification or package body, you can map a package subprogram to an external Java or C subprogram by using a call specification, which maps the external subprogram name, parameter types, and return type to their SQL counterparts.

The `AUTHID` clause of the package specification determines whether the subprograms and cursors in the package run with the privileges of their definer (the default) or invoker, and whether their unqualified references to schema objects are resolved in the schema of the definer or invoker.

The `ACCESSIBLE` `BY` clause of the package specification lets you specify a white list of PL/SQL units that can access the package. You use this clause in situations like these:

- You implement a PL/SQL application as several packages—one package that provides the application programming interface (API) and helper packages to do the work. You want clients to have access to the API, but not to the helper packages. Therefore, you omit the `ACCESSIBLE` `BY` clause from the API package specification and include it in each helper package specification, where you specify that only the API package can access the helper package.
- You create a utility package to provide services to some, but not all, PL/SQL units in the same schema. To restrict use of the package to the intended units, you list them in the `ACCESSIBLE` `BY` clause in the package specification.

See Also:

- " [Package Specification](package-specification.md) " for more information about the package specification
- " [Package Body](package-body.md) " for more information about the package body
- " [Function Declaration and Definition](function-declaration-and-definition.md) "
- " [Procedure Declaration and Definition](procedure-declaration-and-definition.md) "
- " [Invoker's Rights and Definer's Rights (AUTHID Property)](invokers-rights-and-definers-rights-authid-property.md) "