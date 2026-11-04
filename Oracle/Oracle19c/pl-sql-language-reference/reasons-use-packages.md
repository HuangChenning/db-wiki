---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/reasons-use-packages.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Reasons to Use Packages

Packages support the development and maintenance of reliable, reusable code with the following features:

- Modularity
	Packages let you encapsulate logically related types, variables, constants, subprograms, cursors, and exceptions in named PL/SQL modules. You can make each package easy to understand, and make the interfaces between packages simple, clear, and well defined. This practice aids application development.
- Easier Application Design
	When designing an application, all you need initially is the interface information in the package specifications. You can code and compile specifications without their bodies. Next, you can compile standalone subprograms that reference the packages. You need not fully define the package bodies until you are ready to complete the application.
- Hidden Implementation Details
	Packages let you share your interface information in the package specification, and hide the implementation details in the package body. Hiding the implementation details in the body has these advantages:
	- You can change the implementation details without affecting the application interface.
		- Application users cannot develop code that depends on implementation details that you might want to change.
- Added Functionality
	Package public variables and cursors can persist for the life of a session. They can be shared by all subprograms that run in the environment. They let you maintain data across transactions without storing it in the database. (For the situations in which package public variables and cursors do not persist for the life of a session, see " [Package State](package-state.md) ".)
- Better Performance
	The first time you invoke a package subprogram, Oracle Database loads the whole package into memory. Subsequent invocations of other subprograms in same the package require no disk I/O.
	Packages prevent cascading dependencies and unnecessary recompiling. For example, if you change the body of a package function, Oracle Database does not recompile other subprograms that invoke the function, because these subprograms depend only on the parameters and return value that are declared in the specification.
- Easier to Grant Roles
	You can grant roles on the package, instead of granting roles on each object in the package.

Note:

You cannot reference host variables from inside a package.