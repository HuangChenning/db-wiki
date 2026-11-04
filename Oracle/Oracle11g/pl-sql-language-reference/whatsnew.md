---
title: "What's New in PL/SQL?"
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/whatsnew.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

This topic briefly describes the new PL/SQL features that this book documents and provides links to more information.

Topics

## PL/SQL Feature for Oracle Database 11g Release 2 (11.2.0.2)

Package Treated as Stateless if State is Constant for Life of Session

Before Release 11.2.0.2, if a session recompiled the body of a stateful package, and then another session that had instantiated that package referenced it, the latter session got the severely disruptive error ORA-04068 (”existing state of packages … has been discarded”). Therefore, "hot patching" packages was likely to disrupt their users.

As of Release 11.2.0.2, Oracle Database treats a package as stateless if its state is constant for the life of a session (or longer). This is the case for a package whose items are all compile-time constants. Therefore, "hot patching" packages (especially noneditioned packages) is much less likely to disrupt sessions that are using them.

For more information, see ["Package State"](packages.md).

## PL/SQL Features for Oracle Database 11g Release 2

The PL/SQL features for Oracle Database 11g Release 2 are:

- DBMS\_PARALLEL\_EXECUTE Package
- FORCE Option in CREATE TYPE Statement
- Crossedition Triggers
- ALTER TYPE Statement Restrictions for Editioned ADTs
- RESET option for ALTER TYPE Statement
- Automatic Detection of Data Sources of Result-Cached Function
- Result Caches in Oracle RAC Environment Are No Longer Private

DBMS\_PARALLEL\_EXECUTE Package

The `DBMS_PARALLEL_EXECUTE` package lets you incrementally update the data in a large table in parallel, in two high-level steps:

1. Group sets of rows in the table into smaller chunks.
2. Apply the desired `UPDATE` statement to the chunks in parallel, committing each time you have finished processing a chunk.

Oracle recommends this technique whenever you are updating a lot of data. It improves performance, reduces rollback space consumption, and reduces the number of row locks held.

For more information, see ["Updating Large Tables in Parallel"](tuning.md).

FORCE Option in CREATE TYPE Statement

Before Oracle Database 11g Release 2, if a `CREATE` `OR` `REPLACE` `TYPE` statement specified an existing type that had either type dependents or table dependents, the statement failed with error ORA-02303.

As of Oracle Database 11g Release 2, if you specify `FORCE` in this situation, the statement fails only if the existing type has table dependents, not if it has type dependents. For more information, see ["CREATE TYPE Statement"](create_type.md).

Crossedition Triggers

Crossedition triggers are intended to fire when database manipulation language (DML) statements change database tables while an online application that uses the tables is being patched or upgraded with edition-based redefinition. The body of a crossedition trigger is designed to handle these changes so that they can be appropriately applied after the changes to the application code are completed.

For more information, see ["CREATE TRIGGER Statement"](create_trigger.md).

See Also:

[Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_editions.htm#ADFNS020) for information about edition-based redefinition in general and crossedition triggers in particular, including the relationship between crossedition triggers and editions

ALTER TYPE Statement Restrictions for Editioned ADTs

If you use edition-based redefinition to patch or upgrade an application, you use editioned objects. If any of your editioned objects are Abstract Data Types (ADTs), see ["Restriction on type"](alter_type.md).

See Also:

[Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_editions.htm#ADFNS020) for information about edition-based redefinition in general and editioned objects in particular

RESET option for ALTER TYPE Statement

The `RESET` option of the `ALTER` `TYPE` statement resets the version of a type to 1, so that it is no longer considered to be evolved. `RESET` is intended for evolved ADTs that are preventing their owners from being editions-enabled. For more information, see ["ALTER TYPE Statement"](alter_type.md).

See Also:

[Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_editions.htm#ADFNS99878) for information about enabling editions for users

Automatic Detection of Data Sources of Result-Cached Function

Before Oracle Database 11g Release 2, you had to specify any data sources on which a result-cached function depended.

As of Oracle Database 11g Release 2, Oracle Database automatically detects all data sources that are queried while a result-cached function is running. For more information, see ["PL/SQL Function Result Cache"](subprograms.md).

Result Caches in Oracle RAC Environment Are No Longer Private

Before Oracle Database 11g Release 2, each database instance in an Oracle RAC environment had a private function result cache, available only to sessions on that instance. If a required result was missing from the private cache of the local instance, the body of the function ran to compute the result, which was then added to the local cache. The result was not retrieved from the private cache of another instance.

As of Oracle Database 11g Release 2, each database instance manages its own local result cache, but the local result cache is no longer private—sessions attached to remote database instances can access its contents. If a required result is missing from the result cache of the local instance, the result might be retrieved from the local cache of another instance, instead of being locally computed. For more information, see ["Result Caches in Oracle RAC Environment"](subprograms.md).

## PL/SQL Features for Oracle Database 11g Release 1

The PL/SQL features for Oracle Database 11g Release 1 are:

- Enhancements to Regular Expression SQL Functions
- SIMPLE\_INTEGER, SIMPLE\_FLOAT, and SIMPLE\_DOUBLE Data Types
- CONTINUE Statement
- Sequences in PL/SQL Expressions
- Dynamic SQL Enhancements
- Named and Mixed Notation in PL/SQL Subprogram Invocations
- PL/SQL Function Result Cache
- Compound DML Triggers
- More Control Over Triggers
- Automatic Subprogram Inlining
- PL/Scope
- PL/SQL Hierarchical Profiler
- PL/SQL Native Compiler Generates Native Code Directly

Enhancements to Regular Expression SQL Functions

The regular expression SQL functions `REGEXP_INSTR` and `REGEXP_SUBSTR` have increased functionality. A new regular expression SQL function, `REGEXP_COUNT`, returns the number of times a pattern appears in a string. These functions act the same in SQL and PL/SQL.

See Also:

- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_regexp.htm#ADFNS9999) for information about the implementation of regular expressions
- Oracle Database SQL Language Reference for detailed descriptions of the [`REGEXP_INSTR`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions148.htm#SQLRF06300), [`REGEXP_SUBSTR`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions150.htm#SQLRF06303), and [`REGEXP_COUNT`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions147.htm#SQLRF20014) functions

SIMPLE\_INTEGER, SIMPLE\_FLOAT, and SIMPLE\_DOUBLE Data Types

The `SIMPLE_INTEGER`, `SIMPLE_FLOAT`, and `SIMPLE_DOUBLE` data types are predefined subtypes of `PLS_INTEGER`, `BINARY_FLOAT`, and `BINARY_DOUBLE`, respectively. Each subtype has the same range as its base type and has a `NOT` `NULL` constraint.

`SIMPLE_INTEGER` differs significantly from `PLS_INTEGER` in its overflow semantics, but `SIMPLE_FLOAT` and `SIMPLE_DOUBLE` are identical to their base types, except for their `NOT` `NULL` constraint.

You can use `SIMPLE_INTEGER` when the value will never be `NULL` and overflow checking is unnecessary. You can use `SIMPLE_FLOAT` and `SIMPLE_DOUBLE` when the value will never be `NULL`. Without the overhead of checking for nullness and overflow, these subtypes provide significantly better performance than their base types when `PLSQL_CODE_TYPE='NATIVE'`, because arithmetic operations on `SIMPLE_INTEGER` values are done directly in the hardware. When `PLSQL_CODE_TYPE='INTERPRETED'`, the performance improvement is smaller.

For more information, see:

- ["SIMPLE\_INTEGER Subtype of PLS\_INTEGER"](datatypes.md)
- ["Additional PL/SQL Constants for BINARY\_FLOAT and BINARY\_DOUBLE"](datatypes.md)
- ["Use Data Types that Use Hardware Arithmetic"](tuning.md)

CONTINUE Statement

The `CONTINUE` statement exits the current iteration of a loop and transfers control to the next iteration (in contrast with the `EXIT` statement, which exits a loop and transfers control to the end of the loop). The `CONTINUE` statement has two forms: the unconditional `CONTINUE` and the conditional `CONTINUE` `WHEN`.

For more information, see:

- ["LOOP Statements"](controlstatements.md)
- ["CONTINUE Statement"](continue_statement.md)

Sequences in PL/SQL Expressions

The pseudocolumns `CURRVAL` and `NEXTVAL` make writing PL/SQL source text easier for you and improve runtime performance and scalability. You can use `sequence_name`.`CURRVAL` and `sequence_name`.`NEXTVAL` wherever you can use a `NUMBER` expression.

For more information, see ["CURRVAL and NEXTVAL in PL/SQL"](static.md).

Dynamic SQL Enhancements

Both native dynamic SQL and the `DBMS_SQL` package have been enhanced.

Native dynamic SQL now supports a dynamic SQL statement larger than 32 KB by allowing it to be a `CLOB` —see ["EXECUTE IMMEDIATE Statement"](executeimmediate_statement.md) and ["OPEN FOR Statement"](openfor_statement.md).

In the `DBMS_SQL` package:

- All data types that native dynamic SQL supports are supported.
- The `DBMS_SQL.PARSE` function accepts a `CLOB` argument, allowing dynamic SQL statements larger than 32 KB.
- The new ["DBMS\_SQL.TO\_REFCURSOR Function"](dynamic.md) lets you switch from the `DBMS_SQL` package to native dynamic SQL.
- The new ["DBMS\_SQL.TO\_CURSOR\_NUMBER Function"](dynamic.md) lets you switch from native dynamic SQL to the `DBMS_SQL` package.

Named and Mixed Notation in PL/SQL Subprogram Invocations

Before Oracle Database 11g Release 1, a SQL statement that invoked a PL/SQL subprogram had to specify the actual parameters in positional notation. As of Oracle Database 11g Release 1, named and mixed notation are also allowed. This improves usability when a SQL statement invokes a PL/SQL subprogram that has many defaulted parameters, and few of the actual parameters must differ from their default values.

For an example, see the `SELECT` statements in [Example 8-24](subprograms.md).

PL/SQL Function Result Cache

A function result cache can save significant space and time. Each time a result-cached function is invoked with different parameter values, those parameters and their result are stored in the cache. Subsequently, when the same function is invoked with the same parameter values, the result is retrieved from the cache, instead of being recomputed.

Before Oracle Database 11g Release 1, if you wanted your PL/SQL application to cache the results of a function, you had to design and code the cache and cache-management subprograms. If multiple sessions ran your application, each session had to have its own copy of the cache and cache-management subprograms. Sometimes each session had to perform the same expensive computations.

As of Oracle Database 11g Release 1, PL/SQL provides a function result cache. To use it, use the `RESULT_CACHE` clause in each PL/SQL function whose results you want cached. Because the function result cache resides in a shared global area (SGA), it is available to any session that runs your application.

After you convert your application to PL/SQL function result caching, it uses more SGA, but significantly less total system memory.

For more information, see:

- ["PL/SQL Function Result Cache"](subprograms.md)
- ["Function Declaration and Definition"](function.md)

Compound DML Triggers

A compound DML trigger created on a table or editioning view can fire at multiple timing points. Each timing point section has its own executable part and optional exception-handling part, but all of these parts can access a common PL/SQL state. The common state arises when the triggering statement starts and disappears when the triggering statement completes, even when the triggering statement causes an error.

Before Oracle Database 11g Release 1, application developers modeled the common state with an ancillary package. This approach was both cumbersome to program and subject to memory leak when the triggering statement caused an error and the after-statement trigger did not fire. Compound triggers help program an approach where you want the actions you implement for the various timing points to share common data.

For more information, see ["Compound DML Triggers"](triggers.md).

More Control Over Triggers

The SQL statement `CREATE` `TRIGGER` now supports `ENABLE`, `DISABLE`, and `FOLLOWS` clauses that give you more control over triggers. The `DISABLE` clause lets you create a trigger in the disabled state, so that you can ensure that your code compiles successfully before you enable the trigger. The `ENABLE` clause explicitly specifies the default state. The `FOLLOWS` clause lets you control the firing order of triggers that are defined on the same table and have the same timing point.

For more information, see:

- ["Order in Which Triggers Fire"](triggers.md)
- ["Trigger Enabling and Disabling"](triggers.md)

Automatic Subprogram Inlining

Subprogram inlining replaces a subprogram invocation (to a subprogram in the same PL/SQL unit) with a copy of the invoked subprogram, which almost always improves program performance.

You can use `PRAGMA INLINE` to specify that individual subprogram invocations are, or are not, to be inlined. You can also turn on automatic inlining—that is, ask the compiler to search for inlining opportunities—by setting the compilation parameter `PLSQL_OPTIMIZE_LEVEL` to 3 (the default is 2).

In the rare cases when automatic inlining does not improve program performance, you can use the PL/SQL hierarchical profiler to identify subprograms for which you want to turn off inlining.

For more information, see:

- ["Subprogram Inlining"](tuning.md)
- ["INLINE Pragma"](inline_pragma.md)

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams198.htm#REFRN10255) for information about the compilation parameter `PLSQL_OPTIMIZE_LEVEL`

PL/Scope

PL/Scope is a compiler-driven tool that collects and organizes data about user-defined identifiers from PL/SQL source text. Because PL/Scope is a compiler-driven tool, you use it through interactive development environments (such as SQL Developer and JDeveloper), rather than directly.

PL/Scope enables the development of powerful and effective PL/Scope source text browsers that increase PL/SQL developer productivity by minimizing time spent browsing and understanding source text.

For more information, see ["Collecting Data About User-Defined Identifiers"](tuning.md).

See Also:

[Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_plscope.htm#ADFNS022)

PL/SQL Hierarchical Profiler

The PL/SQL hierarchical profiler reports the dynamic execution profile of your PL/SQL program, organized by subprogram invocations. It accounts for SQL and PL/SQL execution times separately. Each subprogram-level summary in the dynamic execution profile includes information such as number of invocations to the subprogram, time spent in the subprogram itself, time spent in the subprogram's subtree (that is, in its descendent subprograms), and detailed parent-children information.

You can browse the generated HTML reports in any browser. The browser's navigational capabilities, combined with well chosen links, provide a powerful way to analyze performance of large applications, improve application performance, and lower development costs.

For more information, see ["Profiling and Tracing PL/SQL Programs"](tuning.md).

See Also:

[Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_profiler.htm#ADFNS023)

PL/SQL Native Compiler Generates Native Code Directly

The PL/SQL native compiler now generates native code directly, instead of translating PL/SQL code to C code and having the C compiler generate the native code. An individual developer can now compile PL/SQL units for native execution without any set-up on the part of the DBA. Execution speed of natively compiled PL/SQL programs improves, in some cases by an order of magnitude.

For more information, see ["Compiling PL/SQL Units for Native Execution"](tuning.md).