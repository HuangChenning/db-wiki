---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/package-state.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Package State

The values of the variables, constants, and cursors that a package declares (in either its specification or body) comprise its **package state**.

If a PL/SQL package declares at least one variable, constant, or cursor, then the package is stateful; otherwise, it is stateless.

Each session that references a package item has its own instantiation of that package. If the package is stateful, the instantiation includes its state.

The package state persists for the life of a session, except in these situations:

- The package is `SERIALLY_REUSABLE`.
- The package body is recompiled.
	If the body of an instantiated, stateful package is recompiled (either explicitly, with the " [ALTER PACKAGE Statement](ALTER-PACKAGE-statement.md) ", or implicitly), the next invocation of a subprogram in the package causes Oracle Database to discard the existing package state and raise the exception ORA-04068.
	After PL/SQL raises the exception, a reference to the package causes Oracle Database to re-instantiate the package, which re-initializes it. Therefore, previous changes to the package state are lost.
- Any of the session's instantiated packages are invalidated and revalidated.
	All of a session's package instantiations (including package states) can be lost if any of the session's instantiated packages are invalidated and revalidated.

Oracle Database treats a package as stateless if its state is constant for the life of a session (or longer). This is the case for a package whose items are all compile-time constants.

A compile-time constant is a constant whose value the PL/SQL compiler can determine at compilation time. A constant whose initial value is a literal is always a compile-time constant. A constant whose initial value is not a literal, but which the optimizer reduces to a literal, is also a compile-time constant. Whether the PL/SQL optimizer can reduce a nonliteral expression to a literal depends on optimization level. Therefore, a package that is stateless when compiled at one optimization level might be stateful when compiled at a different optimization level.

Starting with Oracle Database 19c, Release Update 19.23, the initialization parameter `SESSION_EXIT_ON_PACKAGE_STATE_ERROR` allows you to specify behavior in the event package state is invalidated. When a stateful PL/SQL package undergoes modification, the sessions that have an active instantiation of the package receive the following error when they attempt to run it:

```
ORA-04068: existing state of package has been discarded
```

When `SESSION_EXIT_ON_PACKAGE_STATE_ERROR` is set to `TRUE`, the session immediately exits instead of just raising ORA-04068. This can be advantageous because many applications are better equipped to handle a session being discarded, simplifying recovery.

See Also:

- " [SERIALLY\_REUSABLE Packages](serially_reusable-packages.md) "
- " [Package Instantiation and Initialization](package-instantiation-and-initialization.md) " for information about initialization
- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADFNS99967) for information about invalidation and revalidation of schema objects
- " [PL/SQL Optimizer](pl-sql-optimizer.md) " for information about the optimizer
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=REFRN-GUID-6493B7C8-B048-4069-8A68-37CD0F1D0221) for more information about `SESSION_EXIT_ON_PACKAGE_STATE_ERROR`