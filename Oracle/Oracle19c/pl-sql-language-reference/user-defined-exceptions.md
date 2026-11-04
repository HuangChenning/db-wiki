---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/user-defined-exceptions.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## User-Defined Exceptions

You can declare your own exceptions in the declarative part of any PL/SQL anonymous block, subprogram, or package.

An exception name declaration has this syntax:

```
exception_name EXCEPTION;
```

For semantic information, see " [Exception Declaration](exception-declaration.md) ".

You must raise a user-defined exception explicitly. For details, see " [Raising Exceptions Explicitly](raising-exceptions-explicitly.md) ".