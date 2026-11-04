---
title: Formal Parameter Declaration
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/parameter_declaration.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

A formal parameter declaration can appear in the following:

- ["Function Declaration and Definition"](function.md)
- ["Procedure Declaration and Definition"](procedure.md)
- ["CREATE FUNCTION Statement"](create_function.md)
- ["CREATE PROCEDURE Statement"](create_procedure.md)

Topics

Semantics

parameter

Name of the formal parameter that you are declaring, which you can reference in the executable part of the subprogram.

IN, OUT, IN OUT

Mode that determines the behavior of the parameter, explained in ["Subprogram Parameter Modes"](subprograms.md). Default: `IN`.

Note:

Avoid using `OUT` and `IN` `OUT` for function parameters. The purpose of a function is to take zero or more parameters and return a single value. Functions must be free from side effects, which change the values of variables not local to the subprogram.

NOCOPY

Requests that the compiler pass the corresponding actual parameter by reference instead of value (for the difference, see ["Subprogram Parameter Passing Methods"](subprograms.md)). Each time the subprogram is invoked, the optimizer decides, silently, whether to obey or disregard `NOCOPY`.

Caution:

`NOCOPY` increases the likelihood of aliasing. For details, see ["Subprogram Parameter Aliasing with Parameters Passed by Reference"](subprograms.md).

The compiler ignores `NOCOPY` in these cases:

- The actual parameter must be implicitly converted to the data type of the formal parameter.
- The actual parameter is the element of a collection.
- The actual parameter is a scalar variable with the `NOT` `NULL` constraint.
- The actual parameter is a scalar numeric variable with a range, size, scale, or precision constraint.
- The actual and formal parameters are records, one or both was declared with `%ROWTYPE` or `%TYPE`, and constraints on corresponding fields differ.
- The actual and formal parameters are records, the actual parameter was declared (implicitly) as the index of a cursor `FOR` `LOOP` statement, and constraints on corresponding fields differ.
- The subprogram is invoked through a database link or as an external subprogram.

Note:

The preceding list might change in a subsequent release.

datatype

Data type of the formal parameter that you are declaring. The data type can be a constrained subtype, but cannot include a constraint (for example, `NUMBER` (`2`) or `VARCHAR2` (`20`).

If `datatype` is a constrained subtype, the corresponding actual parameter inherits the `NOT` `NULL` constraint of the subtype (if it has one), but not the size (see [Example 8-10](subprograms.md)).

Caution:

The data type `REF` `CURSOR` increases the likelihood of subprogram parameter aliasing, which can have unintended results. For more information, see ["Subprogram Parameter Aliasing with Cursor Variable Parameters"](subprograms.md).

expression

Default value of the formal parameter that you are declaring. The data type of `expression` must be compatible with `datatype`.

If a subprogram invocation does not specify an actual parameter for the formal parameter, then that invocation evaluates `expression` and assigns its value to the formal parameter.

If a subprogram invocation does specify an actual parameter for the formal parameter, then that invocation assigns the value of the actual parameter to the formal parameter and does not evaluate `expression`.

Examples

- [Example 2-26, "Assigning Value to Variable as IN OUT Subprogram Parameter"](fundamentals.md)
- [Example 8-9, "Formal Parameters and Actual Parameters"](subprograms.md)
- [Example 8-14, "Parameter Values Before, During, and After Procedure Invocation"](subprograms.md)
- [Example 8-15, "OUT and IN OUT Parameter Values After Unhandled Exception"](subprograms.md)
- [Example 8-16, "OUT Formal Parameter of Record Type with Non-NULL Default Value"](subprograms.md)
- [Example 8-20, "Procedure with Default Parameter Values"](subprograms.md)
- [Example 8-21, "Function Provides Default Parameter Value"](subprograms.md)
- [Example 8-22, "Adding Subprogram Parameter Without Changing Existing Invocations"](subprograms.md)