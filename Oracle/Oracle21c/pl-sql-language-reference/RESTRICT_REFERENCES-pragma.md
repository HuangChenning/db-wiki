---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/RESTRICT_REFERENCES-pragma.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

The `RESTRICT_REFERENCES` pragma asserts that a user-defined subprogram does not read or write database tables or package variables.

Note:

The `RESTRICT_REFERENCES` pragma is deprecated. Oracle recommends using `DETERMINISTIC` and `PARALLEL_ENABLE` instead of `RESTRICT_REFERENCES`.

Subprograms that read or write database tables or package variables are difficult to optimize, because any invocation of the subprogram might produce different results or encounter errors. If a statement in a user-defined subprogram violates an assertion made by `RESTRICT_REFERENCES`, then the PL/SQL compiler issues an error message when it parses that statement, unless you specify `TRUST`.

Typically, this pragma is specified for functions. If a function invokes procedures, then specify this pragma for those procedures also.

Restrictions on RESTRICT\_REFERENCES Pragma

- This pragma can appear only in a package specification or ADT specification.
- Only one `RESTRICT_REFERENCES` pragma can reference a given subprogram.

Topics

- Syntax
- Semantics

Syntax

restrict\_references\_pragma::=

![restrict_references_pragma](img/restrict_references_pragma.gif)

> ```
> PRAGMA RESTRICT_REFERENCES
>  ( { subprogram | method | DEFAULT } ,
>      { RNDS | WNDS | RNPS | WNPS | TRUST }
>        [, { RNDS | WNDS | RNPS | WNPS | TRUST } ]... ) ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

subprogram

Name of a user-defined subprogram, typically a function. If `subprogram` is overloaded, the pragma applies only to the most recent subprogram declaration.

method

Name of a `MEMBER` subprogram. See " [CREATE TYPE Statement](CREATE-TYPE-statement.md) "for more information.

DEFAULT

Applies the pragma to all subprograms in the package specification or ADT specification (including the system-defined constructor for ADTs).

If you also declare the pragma for an individual subprogram, it overrides the `DEFAULT` pragma for that subprogram.

RNDS

Asserts that the subprogram reads no database state (does not query database tables).

WNDS

Asserts that the subprogram writes no database state (does not modify tables).

RNPS

Asserts that the subprogram reads no package state (does not reference the values of package variables)

Restriction on RNPS

You cannot specify `RNPS` if the subprogram invokes the `SQLCODE` or `SQLERRM` function.

WNPS

Asserts that the subprogram writes no package state (does not change the values of package variables).

Restriction on WNPS

You cannot specify `WNPS` if the subprogram invokes the `SQLCODE` or `SQLERRM` function.

TRUST

Asserts that the subprogram can be trusted not to violate the other specified assertions and prevents the PL/SQL compiler from checking the subprogram body for violations. Skipping these checks can improve performance.

If your PL/SQL subprogram invokes a C or Java subprogram, then you must specify `TRUST` for either the PL/SQL subprogram or the C or Java subprogram, because the PL/SQL compiler cannot check a C or Java subprogram for violations at run time.

Note:

To invoke a subprogram from a parallelized DML statement, you must specify all four constraints— `RNDS`, `WNDS`, `RNPS`, and `WNPS`. No constraint implies another.

See Also:

[Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=ADFNS388) for information about using `PRAGMA` `RESTRICT_REFERENCES` in existing applications