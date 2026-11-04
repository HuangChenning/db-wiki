---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/differences-pl-sql-and-sql-name-resolution-rules.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Differences Between PL/SQL and SQL Name Resolution Rules

PL/SQL and SQL name resolution rules are very similar. However:

- PL/SQL rules are less permissive than SQL rules.
	Because most SQL rules are context-sensitive, they recognize as legal more situations than PL/SQL rules do.
- PL/SQL and SQL resolve qualified names differently.
	For example, when resolving the table name `HR`.`JOBS`:
	- PL/SQL searches first for packages, types, tables, and views named `HR` in the current schema, then for public synonyms, and finally for objects named `JOBS` in the `HR` schema.
		- SQL searches first for objects named `JOBS` in the `HR` schema, and then for packages, types, tables, and views named `HR` in the current schema.

To avoid problems caused by the few differences between PL/SQL and SQL name resolution rules, follow the recommendations in " [Avoiding Inner Capture in SELECT and DML Statements](avoiding-inner-capture-select-and-dml-statements.md) ".

Note:

When the PL/SQL compiler processes a static SQL statement, it sends that statement to the SQL subsystem, which uses SQL rules to resolve names in the statement. For details, see " [Resolution of Names in Static SQL Statements](resolution-names-static-sql-statements.md) ".