---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/CREATE-TYPE-BODY-statement.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

The `CREATE` `TYPE` `BODY` defines or implements the member methods defined in the type specification that was created with the ` CREATE` `TYPE` statement.

For each method specified in a type specification for which you did not specify the `call_spec`, you must specify a corresponding method body in the type body.

Topics

Prerequisites

Every member declaration in the `CREATE` `TYPE` specification for an ADT must have a corresponding construct in the `CREATE` `TYPE` or `CREATE` `TYPE` `BODY` statement.

To create or replace a type body in your schema, you must have the `CREATE` `TYPE` or the `CREATE` `ANY` `TYPE` system privilege. To create a type in another user's schema, you must have the `CREATE` `ANY` `TYPE` system privilege. To replace a type in another user's schema, you must have the `DROP` `ANY` `TYPE` system privilege.

Syntax

create\_type\_body::=

![create_type_body](img/create_type_body.gif)

> ```
> CREATE [ OR REPLACE ] [ EDITIONABLE | NONEDITIONABLE ]
>    TYPE BODY plsql_type_body_source
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


plsql\_type\_body\_source::=

![plsql_type_body_source](img/plsql_type_body_source.gif)

> ```
> [ schema. ] type_name  [ sharing_clause ] 
> { IS | AS }
>    { subprog_decl_in_type
>    | map_order_func_declaration
>    }
>      [, { subprog_decl_in_type
>         | map_order_func_declaration
>         }
>      ]...
> END;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


([sharing\_clause::=](SHARING-clause.md), map\_order\_func\_declaration::=, subprog\_decl\_in\_type::=)

subprog\_decl\_in\_type::=

![subprog_decl_in_type](img/subprog_decl_in_type.gif)

> ```
> { proc_decl_in_type | func_decl_in_type | constructor_declaration }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


proc\_decl\_in\_type::=

![proc_decl_in_type](img/proc_decl_in_type.gif)

> ```
> PROCEDURE name [ ( parameter_declaration [, parameter_declaration ]... ) ]
>    { IS | AS } { [ declare_section ] body | call_spec }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


([body::=](block.md), [call\_spec::=](call-specification.md), [declare\_section::=](block.md), [parameter\_declaration::=](formal-parameter-declaration.md))

func\_decl\_in\_type::=

![func_decl_in_type](img/func_decl_in_type.gif)

> ```
> FUNCTION name [ ( parameter_declaration [, parameter_declaration ]... ) ]
>    RETURN datatype
>   [ { invoker_rights_clause
>     | accessible_by_clause
>     | DETERMINISTIC
>     | parallel_enable_clause
>     | result_cache_clause
>     }... [ PIPELINED ] 
>    { IS | AS } { [ declare_section ] body | call_spec }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


([body::=](block.md), [invoker\_rights\_clause::=](invokers_rights_clause.md), [accessible\_by\_clause::=](ACCESSIBLE-BY-clause.md), [deterministic\_clause::=](DETERMINISTIC-clause.md), [call\_spec::=](call-specification.md), [declare\_section::=](block.md), [parameter\_declaration::=](formal-parameter-declaration.md), [parallel\_enable\_clause::=](PARALLEL_ENABLE-clause.md), [result\_cache\_clause::=](RESULT_CACHE-clause.md), [pipelined\_clause::=](PIPELINED-clause.md))

constructor\_declaration::=

![constructor_declaration](img/constructor_declaration.gif)

> ```
> [ FINAL ]
> [ INSTANTIABLE ]
> CONSTRUCTOR FUNCTION datatype
> [ [ SELF IN OUT datatype, ]
>   parameter datatype [, parameter datatype ]...
> ]
> RETURN SELF AS RESULT
> { IS | AS } { [ declare_section ] body | call_spec }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


([call\_spec::=](call-specification.md))

map\_order\_func\_declaration::=

![map_order_func_declaration](img/map_order_func_declaration.gif)

> ```
> { MAP | ORDER ] MEMBER func_decl_in_type
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

create\_type\_body

OR REPLACE

Re-creates the type body if it exists, and recompiles it.

Users who were granted privileges on the type body before it was redefined can still access the type body without being regranted the privileges.

You can use this clause to add member subprogram definitions to specifications added with the `ALTER` `TYPE`... `REPLACE` statement.

\[ EDITIONABLE | NONEDITIONABLE \]

If you do not specify this property, then the type body inherits `EDITIONABLE` or `NONEDITIONABLE` from the type specification. If you do specify this property, then it must match that of the type specification.

plsql\_type\_body\_source

schema

Name of the schema containing the type body. Default: your schema.

type\_name

Name of an ADT.

subprog\_decl\_in\_type

The type of function or procedure subprogram associated with the type specification.

You must define a corresponding method name and optional parameter list in the type specification for each procedure or function declaration. For functions, you also must specify a return type.

map\_order\_func\_declaration

You can declare either one `MAP` method or one `ORDER` method, regardless of how many `MEMBER` or `STATIC` methods you declare. If you declare either a `MAP` or `ORDER` method, then you can compare object instances in SQL.

If you do not declare either method, then you can compare object instances only for equality or inequality. Instances of the same type definition are equal only if each pair of their corresponding attributes is equal.

MAP MEMBER

Declares or implements a `MAP` member function that returns the relative position of a given instance in the ordering of all instances of the object. A `MAP` method is called implicitly and specifies an ordering of object instances by mapping them to values of a predefined scalar type. PL/SQL uses the ordering to evaluate Boolean expressions and to perform comparisons.

If the argument to the `MAP` method is null, then the `MAP` method returns null and the method is not invoked.

An type body can contain only one `MAP` method, which must be a function. The `MAP` function can have no arguments other than the implicit `SELF` argument.

ORDER MEMBER

Specifies an `ORDER` member function that takes an instance of an object as an explicit argument and the implicit `SELF` argument and returns either a negative integer, zero, or a positive integer, indicating that the implicit `SELF` argument is less than, equal to, or greater than the explicit argument, respectively.

If either argument to the `ORDER` method is null, then the `ORDER` method returns null and the method is not invoked.

When instances of the same ADT definition are compared in an `ORDER` `BY` clause, the database invokes the `ORDER` `MEMBER` `func_decl_in_type`.

An object specification can contain only one `ORDER` method, which must be a function having the return type `NUMBER`.

proc\_decl\_in\_type

A procedure subprogram declaration.

constructor\_declaration

A user-defined constructor subprogram declaration. The `RETURN` clause of a constructor function must be `RETURN` `SELF` `AS` `RESULT`. This setting indicates that the most specific type of the value returned by the constructor function is the most specific type of the `SELF` argument that was passed in to the constructor function.

See Also:

- " [CREATE TYPE Statement](CREATE-TYPE-statement.md) " for a list of restrictions on user-defined functions
- " [Overloaded Subprograms](plsql-subprograms.md) " for information about overloading subprogram names
- [Oracle Database Object-Relational Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=ADOBJ006) for information about and examples of user-defined constructors

declare\_section

Declares items that are local to the procedure or function.

body

Procedure or function statements.

func\_decl\_in\_type

A function subprogram declaration.

Examples

Several examples of creating type bodies appear in the [Examples](CREATE-TYPE-statement.md) section of " [CREATE TYPE Statement](CREATE-TYPE-statement.md) ". For an example of re-creating a type body, see " [Example 15-7](ALTER-TYPE-statement.md) ".