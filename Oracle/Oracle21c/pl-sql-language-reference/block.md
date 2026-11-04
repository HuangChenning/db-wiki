---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/block.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

The block, which groups related declarations and statements, is the basic unit of a PL/SQL source program.

It has an optional declarative part, a required executable part, and an optional exception-handling part. Declarations are local to the block and cease to exist when the block completes execution. Blocks can be nested.

An anonymous block is an executable statement.

Topics

Syntax

plsql\_block::=

![plsql_block](img/plsql_block.gif)

> ```
> [ << label >> ]... [ DECLARE declare_section ] body
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


(body::=)

declare\_section::=

![declare_section](img/declare_section.gif)

> ```
> { item_list_1 [ item_list_2 ] | item_list_2 }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


(item\_list\_2::=)

item\_list\_1::=

![item_list_1](img/item_list_1.gif)

> ```
> { type_definition
> | cursor_declaration
> | item_declaration
> | function_declaration
> | procedure_declaration
> }
>  ...
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


([cursor\_declaration::=](explicit-cursor-declaration-and-definition.md), [function\_declaration::=](function-declaration-and-definition.md), item\_declaration::=, [procedure\_declaration::=](procedure-declaration-and-definition.md), type\_definition::=)

item\_list\_2::=

![item_list_2](img/item_list_2.gif)

> ```
> { cursor_declaration
> | cursor_definition
> | function_declaration
> | function_definition
> | procedure_declaration
> | procedure_definition
> }
>  ...
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


([cursor\_declaration::=](explicit-cursor-declaration-and-definition.md), [cursor\_definition::=](explicit-cursor-declaration-and-definition.md), [function\_declaration::=](function-declaration-and-definition.md), [function\_definition::=](function-declaration-and-definition.md), [procedure\_declaration::=](procedure-declaration-and-definition.md), [procedure\_definition::=](procedure-declaration-and-definition.md))

type\_definition::=

![type_definition](img/type_definition.gif)

> ```
> { collection_type_definition
> | record_type_definition
> | ref_cursor_type_definition
> | subtype_definition
> }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


([collection\_type\_definition::=](collection-variable.md), [record\_type\_definition::=](record-variable-declaration.md), [ref\_cursor\_type\_definition::=](cursor-variable-declaration.md), subtype\_definition::=)

subtype\_definition::=

![subtype_definition](img/subtype_definition.gif)

> ```
> SUBTYPE subtype IS base_type [ constraint | CHARACTER SET character_set ]
>   [ NOT NULL ]
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


constraint::=

![constraint](img/constraint.gif)

> ```
> { precision [, scale ] | RANGE low_value .. high_value }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


item\_declaration::=

![item_declaration](img/item_declaration.gif)

> ```
> { collection_variable_decl
> | constant_declaration
> | cursor_variable_declaration
> | exception_declaration
> | record_variable_declaration
> | variable_declaration
> }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


([collection\_variable\_decl::=](collection-variable.md), [constant\_declaration::=](constant-declaration.md), [cursor\_declaration::=](explicit-cursor-declaration-and-definition.md), [cursor\_variable\_declaration::=](cursor-variable-declaration.md), [exception\_declaration::=](exception-declaration.md), [record\_variable\_declaration::=](record-variable-declaration.md), [variable\_declaration::=](scalar-variable-declaration.md))

body::=

![body](img/body.gif)

> ```
> BEGIN statement ...
>   [ EXCEPTION exception_handler [ exception_handler ]... ] END [ name ] ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


([exception\_handler::=](exception-handler.md))

statement::=

![statement](img/statement.gif)

> ```
> [ << label >> [ << label >> ] ...]
>   { assignment_statement
>   | basic_loop_statement
>   | case_statement
>   | close_statement
>   | continue_statement
>   | cursor_for_loop_statement
>   | execute_immediate_statement
>   | exit_statement
>   | fetch_statement
>   | for_loop_statement
>   | forall_statement
>   | goto_statement
>   | if_statement
>   | null_statement
>   | open_statement
>   | open_for_statement
>   | pipe_row_statement
>   | plsql_block
>   | raise_statement
>   | return_statement
>   | select_into_statement
>   | sql_statement
>   | while_loop_statement
>   }
> ```


(plsql\_block::=, procedure\_call::=, sql\_statement::=)

procedure\_call::=

![procedure_call](img/procedure_call.gif)

> ```
> procedure [ ( [ parameter [, parameter ]... ] ) ] ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


sql\_statement::=

![sql_statement](img/sql_statement.gif)

> ```
> { commit_statement
> | collection_method_call
> | delete_statement
> | insert_statement
> | lock_table_statement
> | merge_statement
> | rollback_statement
> | savepoint_statement
> | set_transaction_statement
> | update_statement
> }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

plsql\_block

label

Undeclared identifier, unique for the block.

DECLARE

Starts the declarative part of the block.

declare\_section

Contains local declarations, which exist only in the block and its sub-blocks and are not visible to enclosing blocks.

Restrictions on declare\_section

- A `declare_section` in `create_package`, `create_package_body`, or `compound_trigger_block` cannot include `PRAGMA` `AUTONOMOUS_TRANSACTION`.
- A `declare_section` in `trigger_body` or `tps_body` cannot declare variables of the data type `LONG` or `LONG` `RAW`.

See Also:

- " [CREATE PACKAGE Statement](CREATE-PACKAGE-statement.md) " for more information about `create_package`
- " [CREATE PACKAGE BODY Statement](CREATE-PACKAGE-BODY-statement.md) " for more information about `create_package_body`
- " [CREATE TRIGGER Statement](CREATE-TRIGGER-statement.md) " for more information about `compound_trigger_block`, `trigger_body`, and `tps_body`

subtype\_definition

Static expressions can be used in subtype declarations. See [Static Expressions](plsql-language-fundamentals.md) for more information.

subtype

Name of the user-defined subtype that you are defining.

base\_type

Base type of the subtype that you are defining. `base_type` can be any scalar or user-defined PL/SQL datatype specifier such as `CHAR`, `DATE`, or `RECORD`.

CHARACTER SET character\_set

Specifies the character set for a subtype of a character data type.

Restriction on CHARACTER SET character\_set

Do not specify this clause if `base_type` is not a character data type.

NOT NULL

Imposes the `NOT` `NULL` constraint on data items declared with this subtype. For information about this constraint, see " [NOT NULL Constraint](plsql-language-fundamentals.md) ".

constraint

Specifies a constraint for a subtype of a numeric data type.

Restriction on constraint

Do not specify `constraint` if `base_type` is not a numeric data type.

precision

Specifies the precision for a constrained subtype of a numeric data type.

Restriction on precision

Do not specify `precision` if `base_type` cannot specify precision.

scale

Specifies the scale for a constrained subtype of a numeric data type.

Restriction on scale

Do not specify `scale` if `base_type` cannot specify scale.

RANGE low\_value.. high\_value

Specifies the range for a constrained subtype of a numeric data type. The `low_value` and `high_value` must be numeric literals.

Restriction on RANGE high\_value.. low\_value

Specify this clause only if `base_type` is `PLS_INTEGER` or a subtype of `PLS_INTEGER` (either predefined or user-defined). (For a summary of the predefined subtypes of `PLS_INTEGER`, see [Table 4-3](plsql-data-types.md). For information about user-defined subtypes with ranges, see " [Constrained Subtypes](plsql-data-types.md) ".)

body

BEGIN

Starts the executable part of the block, which contains executable statements.

EXCEPTION

Starts the exception-handling part of the block. When PL/SQL raises an exception, normal execution of the block stops and control transfers to the appropriate `exception_handler`. After the exception handler completes, execution resumes with the statement following the block. For more information about exception-handling, see [PL/SQL Error Handling](plsql-error-handling.md).

exception\_handler

See " [Exception Handler](exception-handler.md) ".

END

Ends the block.

name

The name of the block to which `END` applies—a label, function name, procedure name, or package name.

statement

label

Undeclared identifier, unique for the statement.

assignment\_statement

See " [Assignment Statement](assignment-statement.md) ".

basic\_loop\_statement

See " [Basic LOOP Statement](basic-LOOP-statement.md) ".

case\_statement

See " [CASE Statement](CASE-statement.md) ".

close\_statement

See " [CLOSE Statement](CLOSE-statement.md) ".

collection\_method\_call

Invocation of one of these collection methods, which are procedures:

- `DELETE`
- `EXTEND`
- `TRIM`

For syntax, see " [Collection Method Invocation](collection-method.md) ".

continue\_statement

See " [CONTINUE Statement](CONTINUE-statement.md) ".

cursor\_for\_loop\_statement

See " [Cursor FOR LOOP Statement](cursor-FOR-LOOP-statement.md) ".

execute\_immediate\_statement

See " [EXECUTE IMMEDIATE Statement](EXECUTE-IMMEDIATE-statement.md) ".

exit\_statement

See " [EXIT Statement](EXIT-statement.md) ".

fetch\_statement

See " [FETCH Statement](FETCH-statement.md) ".

for\_loop\_statement

See " [FOR LOOP Statement](FOR-LOOP-statement.md) ".

forall\_statement

See " [FORALL Statement](FORALL-statement.md) ".

goto\_statement

See " [GOTO Statement](GOTO-statement.md) ".

if\_statement

See " [IF Statement](IF-statement.md) ".

null\_statement

See " [NULL Statement](NULL-statement.md) ".

open\_statement

See " [OPEN Statement](OPEN-statement.md) ".

open\_for\_statement

See " [OPEN FOR Statement](OPEN-FOR-statement.md) ".

pipe\_row\_statement

See " [PIPE ROW Statement](PIPE-ROW-statement.md) ".

Restriction on pipe\_row\_statement

This statement can appear only in the body of a pipelined table function; otherwise, PL/SQL raises an exception.

raise\_statement

See " [RAISE Statement](RAISE-statement.md) ".

return\_statement

See " [RETURN Statement](RETURN-statement.md) ".

select\_into\_statement

See " [SELECT INTO Statement](SELECT-INTO-statement.md) ".

while\_loop\_statement

See " [WHILE LOOP Statement](WHILE-LOOP-statement.md) ".

procedure\_call

procedure

Name of the procedure that you are invoking.

parameter \[, parameter \]...

List of actual parameters for the procedure that you are invoking. The data type of each actual parameter must be compatible with the data type of the corresponding formal parameter. The mode of the formal parameter determines what the actual parameter can be:

| Formal Parameter Mode | Actual Parameter |
| --- | --- |
| `IN` | Constant, initialized variable, literal, or expression |
| `OUT` | Variable whose data type is not defined as `NOT` `NULL` |
| `IN` `OUT` | Variable (typically, it is a string buffer or numeric accumulator) |

If the procedure specifies a default value for a parameter, you can omit that parameter from the parameter list. If the procedure has no parameters, or specifies a default value for every parameter, you can either omit the parameter list or specify an empty parameter list.

See Also:

" [Positional, Named, and Mixed Notation for Actual Parameters](plsql-subprograms.md) "

sql\_statement

commit\_statement

SQL `COMMIT` statement. For syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF01110).

delete\_statement

SQL `DELETE` statement. For syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF01505). See also " [DELETE Statement Extension](DELETE-statement-extension.md) ".

insert\_statement

SQL `INSERT` statement. For syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF01505). See also " [INSERT Statement Extension](INSERT-statement-extension.md) ".

lock\_table\_statement

SQL `LOCK` `TABLE` statement. For syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF01605).

merge\_statement

SQL `MERGE` statement. For syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF01606).

rollback\_statement

SQL `ROLLBACK` statement. For syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF01610).

savepoint\_statement

SQL `SAVEPOINT` statement. For syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF01701).

set\_transaction\_statement

SQL `SET` `TRANSACTION` statement. For syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF01705).

update\_statement

SQL `UPDATE` statement. For syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=SQLRF01708). See also " [UPDATE Statement Extensions](UPDATE-statement-extensions.md) ".

Examples