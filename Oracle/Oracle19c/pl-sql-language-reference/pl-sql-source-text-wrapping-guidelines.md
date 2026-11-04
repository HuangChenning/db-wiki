---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/pl-sql-source-text-wrapping-guidelines.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## PL/SQL Source Text Wrapping Guidelines

- Wrap only the body of a package or type, not the specification.
	Leaving the specification unwrapped allows other developers to see the information needed to use the package or type (see [Example A-5](wrapping-pl-sql-source-text-dbms_ddl-subprograms.md)). Wrapping the body prevents them from seeing the package or type implementation.
- Wrap files only after you have finished editing them.
	You cannot edit wrapped files. If a wrapped file needs changes, you must edit the original unwrapped file and then wrap it.
- Before distributing a wrapped file, view it in a text editor and ensure that all important parts are wrapped.