---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/reasons-use-subprograms.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Reasons to Use Subprograms

Subprograms support the development and maintenance of reliable, reusable code with the following features:

- Modularity
	Subprograms let you break a program into manageable, well-defined modules.
- Easier Application Design
	When designing an application, you can defer the implementation details of the subprograms until you have tested the main program, and then refine them one step at a time. (To define a subprogram without implementation details, use the `NULL` statement, as in [Example 4-35](sequential-control-statements.md).)
- Maintainability
	You can change the implementation details of a subprogram without changing its invokers.
- Packageability
	Subprograms can be grouped into packages, whose advantages are explained in " [Reasons to Use Packages](reasons-use-packages.md) ".
- Reusability
	Any number of applications, in many different environments, can use the same package subprogram or standalone subprogram.
- Better Performance
	Each subprogram is compiled and stored in executable form, which can be invoked repeatedly. Because stored subprograms run in the database server, a single invocation over the network can start a large job. This division of work reduces network traffic and improves response times. Stored subprograms are cached and shared among users, which lowers memory requirements and invocation overhead.

Subprograms are an important component of other maintainability features, such as packages (explained in [PL/SQL Packages](plsql-packages.md)) and Abstract Data Types (explained in " [Abstract Data Types](main-features-pl-sql.md) ").