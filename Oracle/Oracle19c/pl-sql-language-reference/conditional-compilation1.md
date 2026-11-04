---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/conditional-compilation1.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Conditional Compilation

Conditional compilation lets you customize the functionality of a PL/SQL application without removing source text.

For example, you can:

- Use new features with the latest database release and disable them when running the application in an older database release.
- Activate debugging or tracing statements in the development environment and hide them when running the application at a production site.

Topics

### How Conditional Compilation Works

Conditional compilation uses selection directives, which are similar to `IF` statements, to select source text for compilation.

The condition in a selection directive usually includes an inquiry directive. Error directives raise user-defined errors. All conditional compilation directives are built from preprocessor control tokens and PL/SQL text.

Topics

See Also:

" [Static Expressions](expressions.md) "

#### Preprocessor Control Tokens

A preprocessor control token identifies code that is processed before the PL/SQL unit is compiled.

Syntax

```
$plsql_identifier
```

There cannot be space between `$` and `plsql_identifier`.

The character `$` can also appear inside `plsql_identifier`, but it has no special meaning there.

These preprocessor control tokens are reserved:

- `$IF`
- `$THEN`
- `$ELSE`
- `$ELSIF`
- `$ERROR`

For information about `plsql_identifier`, see " [Identifiers](lexical-units.md) ".

#### Selection Directives

A selection directive selects source text to compile.

Syntax

```
$IF boolean_static_expression $THEN
   text
[ $ELSIF boolean_static_expression $THEN
   text
]...
[ $ELSE
   text
$END
]
```

For the syntax of `boolean_static_expression`, see " [BOOLEAN Static Expressions](expressions.md) ". The `text` can be anything, but typically, it is either a statement (see " [statement::=](block.md) ") or an error directive (explained in " Error Directives ").

The selection directive evaluates the `BOOLEAN` static expressions in the order that they appear until either one expression has the value `TRUE` or the list of expressions is exhausted. If one expression has the value `TRUE`, its text is compiled, the remaining expressions are not evaluated, and their text is not analyzed. If no expression has the value `TRUE`, then if `$ELSE` is present, its text is compiled; otherwise, no text is compiled.

For examples of selection directives, see " Conditional Compilation Examples ".

See Also:

" [Conditional Selection Statements](conditional-selection-statements.md) " for information about the `IF` statement, which has the same logic as the selection directive

#### Error Directives

An error directive produces a user-defined error message during compilation.

Syntax

```
$ERROR varchar2_static_expression $END
```

It produces this compile-time error message, where `string` is the value of `varchar2_static_expression`:

```
PLS-00179: $ERROR: string
```

For the syntax of `varchar2_static_expression`, see " [VARCHAR2 Static Expressions](expressions.md) ".

For an example of an error directive, see Example 2-58.

#### Inquiry Directives

An inquiry directive provides information about the compilation environment.

Syntax

```
$$name
```

For information about `name`, which is an unquoted PL/SQL identifier, see " [Identifiers](lexical-units.md) ".

An inquiry directive typically appears in the `boolean_static_expression` of a selection directive, but it can appear anywhere that a variable or literal of its type can appear. Moreover, it can appear where regular PL/SQL allows only a literal (not a variable)—for example, to specify the size of a `VARCHAR2` variable.

Topics

##### Predefined Inquiry Directives

The predefined inquiry directives are:

- `$$PLSQL_LINE`
	A `PLS_INTEGER` literal whose value is the number of the source line on which the directive appears in the current PL/SQL unit. An example of `$$PLSQL_LINE` in a selection directive is:
	```
	$IF $$PLSQL_LINE = 32 $THEN ...
	```
- `$$PLSQL_UNIT`
	A `VARCHAR2` literal that contains the name of the current PL/SQL unit. If the current PL/SQL unit is an anonymous block, then `$$PLSQL_UNIT` contains a `NULL` value.
- `$$PLSQL_UNIT_OWNER`
	A `VARCHAR2` literal that contains the name of the owner of the current PL/SQL unit. If the current PL/SQL unit is an anonymous block, then `$$PLSQL_UNIT_OWNER` contains a `NULL` value.
- `$$PLSQL_UNIT_TYPE`
	A `VARCHAR2` literal that contains the type of the current PL/SQL unit— `ANONYMOUS` `BLOCK`, `FUNCTION`, `PACKAGE`, `PACKAGE` `BODY`, `PROCEDURE`, `TRIGGER`, `TYPE`, or `TYPE` `BODY`. Inside an anonymous block or non-DML trigger, `$$PLSQL_UNIT_TYPE` has the value `ANONYMOUS BLOCK`.
- `$$` `plsql_compilation_parameter`
	The name `plsql_compilation_parameter` is a PL/SQL compilation parameter (for example, `PLSCOPE_SETTINGS`). For descriptions of these parameters, see [Table 1-2](architecture-pl-sql.md).

Because a selection directive needs a `BOOLEAN` static expression, you cannot use `$$PLSQL_UNIT`, `$$PLSQL_UNIT_OWNER`, or `$$PLSQL_UNIT_TYPE` in a `VARCHAR2` comparison such as:

```
$IF $$PLSQL_UNIT = 'AWARD_BONUS' $THEN ...
$IF $$PLSQL_UNIT_OWNER IS HR $THEN ...
$IF $$PLSQL_UNIT_TYPE IS FUNCTION $THEN ...
```

However, you can compare the preceding directives to `NULL`. For example:

```
$IF $$PLSQL_UNIT IS NULL $THEN ...
$IF $$PLSQL_UNIT_OWNER IS NOT NULL $THEN ...
$IF $$PLSQL_UNIT_TYPE IS NULL $THEN ...
```

Example 2-55 Predefined Inquiry Directives

In this example, a SQL\*Plus script, uses several predefined inquiry directives as `PLS_INTEGER` and `VARCHAR2` literals to show how their values are assigned.

```
SQL> CREATE OR REPLACE PROCEDURE p
  2  AUTHID DEFINER IS
  3    i PLS_INTEGER;
  4  BEGIN
  5    DBMS_OUTPUT.PUT_LINE('Inside p');
  6    i := $$PLSQL_LINE;
  7    DBMS_OUTPUT.PUT_LINE('i = ' || i);
  8    DBMS_OUTPUT.PUT_LINE('$$PLSQL_LINE = ' || $$PLSQL_LINE);
  9    DBMS_OUTPUT.PUT_LINE('$$PLSQL_UNIT = ' || $$PLSQL_UNIT);
 10    DBMS_OUTPUT.PUT_LINE('$$PLSQL_UNIT_OWNER = ' || $$PLSQL_UNIT_OWNER);
 11    DBMS_OUTPUT.PUT_LINE('$$PLSQL_UNIT_TYPE = ' || $$PLSQL_UNIT_TYPE);
 12  END;
 13  /
 
Procedure created.
 
SQL> BEGIN
  2    p;
  3    DBMS_OUTPUT.PUT_LINE('Outside p');
  4    DBMS_OUTPUT.PUT_LINE('$$PLSQL_LINE = ' || $$PLSQL_LINE);
  5    DBMS_OUTPUT.PUT_LINE('$$PLSQL_UNIT = ' || $$PLSQL_UNIT);
  6    DBMS_OUTPUT.PUT_LINE('$$PLSQL_UNIT_OWNER = ' || $$PLSQL_UNIT_OWNER);
  7    DBMS_OUTPUT.PUT_LINE('$$PLSQL_UNIT_TYPE = ' || $$PLSQL_UNIT_TYPE);
  8  END;
  9  /
```

Result:

```
Inside p
i = 6
$$PLSQL_LINE = 8
$$PLSQL_UNIT = P
$$PLSQL_UNIT_OWNER = HR
$$PLSQL_UNIT_TYPE = PROCEDURE
Outside p
$$PLSQL_LINE = 4
$$PLSQL_UNIT =
$$PLSQL_UNIT_OWNER =
$$PLSQL_UNIT_TYPE = ANONYMOUS BLOCK
 
PL/SQL procedure successfully completed.
```

Example 2-56 Displaying Values of PL/SQL Compilation Parameters

This example displays the current values of PL/SQL the compilation parameters.

Note:

In the SQL\*Plus environment, you can display the current values of initialization parameters, including the PL/SQL compilation parameters, with the command `SHOW` `PARAMETERS`. For more information about the `SHOW` command and its `PARAMETERS` option, see [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQPUG123).

```
BEGIN
  DBMS_OUTPUT.PUT_LINE('$$PLSCOPE_SETTINGS = '     || $$PLSCOPE_SETTINGS);
  DBMS_OUTPUT.PUT_LINE('$$PLSQL_CCFLAGS = '        || $$PLSQL_CCFLAGS);
  DBMS_OUTPUT.PUT_LINE('$$PLSQL_CODE_TYPE = '      || $$PLSQL_CODE_TYPE);
  DBMS_OUTPUT.PUT_LINE('$$PLSQL_OPTIMIZE_LEVEL = ' || $$PLSQL_OPTIMIZE_LEVEL);
  DBMS_OUTPUT.PUT_LINE('$$PLSQL_WARNINGS = '       || $$PLSQL_WARNINGS);
  DBMS_OUTPUT.PUT_LINE('$$NLS_LENGTH_SEMANTICS = ' || $$NLS_LENGTH_SEMANTICS);
END;
/
```

Result:

```
$$PLSCOPE_SETTINGS = IDENTIFIERS:NONE
$$PLSQL_CCFLAGS =
$$PLSQL_CODE_TYPE = INTERPRETED
$$PLSQL_OPTIMIZE_LEVEL = 2
$$PLSQL_WARNINGS = ENABLE:ALL
$$NLS_LENGTH_SEMANTICS = BYTE
```

##### Assigning Values to Inquiry Directives

You can assign values to inquiry directives with the `PLSQL_CCFLAGS` compilation parameter.

For example:

```
ALTER SESSION SET PLSQL_CCFLAGS = 
  'name1:value1, name2:value2, ... namen:valuen'
```

Each `value` must be either a `BOOLEAN` literal (`TRUE`, `FALSE`, or `NULL`) or `PLS_INTEGER` literal. The data type of `value` determines the data type of `name`.

The same `name` can appear multiple times, with values of the same or different data types. Later assignments override earlier assignments. For example, this command sets the value of `$$flag` to 5 and its data type to `PLS_INTEGER`:

```
ALTER SESSION SET PLSQL_CCFLAGS = 'flag:TRUE, flag:5'
```

Oracle recommends against using `PLSQL_CCFLAGS` to assign values to predefined inquiry directives, including compilation parameters. To assign values to compilation parameters, Oracle recommends using the `ALTER` `SESSION` statement.

For more information about the `ALTER` `SESSION` statement, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF00901).

Note:

The compile-time value of `PLSQL_CCFLAGS` is stored with the metadata of stored PL/SQL units, which means that you can reuse the value when you explicitly recompile the units. For more information, see " [PL/SQL Units and Compilation Parameters](architecture-pl-sql.md) ".

For more information about `PLSQL_CCFLAGS`, see [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=REFRN10261).

Example 2-57 PLSQL\_CCFLAGS Assigns Value to Itself

This example uses `PLSQL_CCFLAGS` to assign a value to the user-defined inquiry directive `$$Some_Flag` and (though not recommended) to itself. Because later assignments override earlier assignments, the resulting value of `$$Some_Flag` is 2 and the resulting value of `PLSQL_CCFLAGS` is the value that it assigns to itself (99), not the value that the `ALTER` `SESSION` statement assigns to it (`'Some_Flag:1, Some_Flag:2, PLSQL_CCFlags:99'`).

```
ALTER SESSION SET
PLSQL_CCFlags = 'Some_Flag:1, Some_Flag:2, PLSQL_CCFlags:99'
/
BEGIN
  DBMS_OUTPUT.PUT_LINE($$Some_Flag);
  DBMS_OUTPUT.PUT_LINE($$PLSQL_CCFlags);
END;
/
```

Result:

```
2
99
```

##### Unresolvable Inquiry Directives

If the source text is not wrapped, PL/SQL issues a warning if the value of an inquiry directive cannot be determined.

If an inquiry directive (`$$` `name`) cannot be resolved, and the source text is not wrapped, then PL/SQL issues the warning `PLW-6003` and substitutes `NULL` for the value of the unresolved inquiry directive. If the source text is wrapped, the warning message is disabled, so that the unresolved inquiry directive is not revealed.

For information about wrapping PL/SQL source text, see [PL/SQL Source Text Wrapping](plsql-source-text-wrapping.md).

#### DBMS\_DB\_VERSION Package

The `DBMS_DB_VERSION` package specifies the Oracle version numbers and other information useful for simple conditional compilation selections based on Oracle versions.

The `DBMS_DB_VERSION` package provides these static constants:

- The `PLS_INTEGER` constant `VERSION` identifies the current Oracle Database version.
- The `PLS_INTEGER` constant `RELEASE` identifies the current Oracle Database release number.
- Each `BOOLEAN` constant of the form `VER_LE_` `v` has the value `TRUE` if the database version is less than or equal to `v`; otherwise, it has the value `FALSE`.
- Each `BOOLEAN` constant of the form `VER_LE_` `v_r` has the value `TRUE` if the database version is less than or equal to `v` and release is less than or equal to `r`; otherwise, it has the value `FALSE`.

For more information about the `DBMS_DB_VERSION` package, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS223).

### Conditional Compilation Examples

Examples of conditional compilation using selection and user-defined inquiry directives.

Example 2-58 Code for Checking Database Version

This example generates an error message if the database version and release is less than Oracle Database 10g release 2; otherwise, it displays a message saying that the version and release are supported and uses a `COMMIT` statement that became available at Oracle Database 10g release 2.

```
BEGIN
  $IF DBMS_DB_VERSION.VER_LE_10_1 $THEN  -- selection directive begins
    $ERROR 'unsupported database release' $END  -- error directive
  $ELSE
    DBMS_OUTPUT.PUT_LINE (
      'Release ' || DBMS_DB_VERSION.VERSION || '.' ||
      DBMS_DB_VERSION.RELEASE || ' is supported.'
    );
  -- This COMMIT syntax is newly supported in 10.2:
  COMMIT WRITE IMMEDIATE NOWAIT;
  $END  -- selection directive ends
END;
/
```

Result:

```
Release 12.1 is supported.
```

Example 2-59 Compiling Different Code for Different Database Versions

This example sets the values of the user-defined inquiry directives `$$my_debug` and `$$my_tracing` and then uses conditional compilation:

- In the specification of package `my_pkg`, to determine the base type of the subtype `my_real` (`BINARY_DOUBLE` is available only for Oracle Database versions 10g and later.)
- In the body of package `my_pkg`, to compute the values of `my_pi` and `my_e` differently for different database versions
- In the procedure `circle_area`, to compile some code only if the inquiry directive `$$my_debug` has the value `TRUE`.
```
ALTER SESSION SET PLSQL_CCFLAGS = 'my_debug:FALSE, my_tracing:FALSE';
 
CREATE OR REPLACE PACKAGE my_pkg AUTHID DEFINER AS
  SUBTYPE my_real IS
    $IF DBMS_DB_VERSION.VERSION < 10 $THEN
      NUMBER;
    $ELSE
      BINARY_DOUBLE;
    $END
  
  my_pi my_real;
  my_e  my_real;
END my_pkg;
/
 
CREATE OR REPLACE PACKAGE BODY my_pkg AS
BEGIN
  $IF DBMS_DB_VERSION.VERSION < 10 $THEN
    my_pi := 3.14159265358979323846264338327950288420;
    my_e  := 2.71828182845904523536028747135266249775;
  $ELSE
    my_pi := 3.14159265358979323846264338327950288420d;
    my_e  := 2.71828182845904523536028747135266249775d;
  $END
END my_pkg;
/
 
CREATE OR REPLACE PROCEDURE circle_area(radius my_pkg.my_real) AUTHID DEFINER IS
  my_area       my_pkg.my_real;
  my_data_type  VARCHAR2(30);
BEGIN
  my_area := my_pkg.my_pi * (radius**2);
  
  DBMS_OUTPUT.PUT_LINE
    ('Radius: ' || TO_CHAR(radius) || ' Area: ' || TO_CHAR(my_area));
  
  $IF $$my_debug $THEN
    SELECT DATA_TYPE INTO my_data_type
    FROM USER_ARGUMENTS
    WHERE OBJECT_NAME = 'CIRCLE_AREA'
    AND ARGUMENT_NAME = 'RADIUS';
 
    DBMS_OUTPUT.PUT_LINE
      ('Data type of the RADIUS argument is: ' || my_data_type);
  $END
END;
/

CALL DBMS_PREPROCESSOR.PRINT_POST_PROCESSED_SOURCE
 ('PACKAGE', 'HR', 'MY_PKG');
```

Result:

```
PACKAGE my_pkg AUTHID DEFINER AS
SUBTYPE my_real IS
BINARY_DOUBLE;
my_pi my_real;
my_e my_real;
END my_pkg;
 
Call completed.
```

### Retrieving and Printing Post-Processed Source Text

The `DBMS_PREPROCESSOR` package provides subprograms that retrieve and print the source text of a PL/SQL unit in its post-processed form.

For information about the `DBMS_PREPROCESSOR` package, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS222).

Example 2-60 Displaying Post-Processed Source Textsource text

This example invokes the procedure `DBMS_PREPROCESSOR`.`PRINT_POST_PROCESSED_SOURCE` to print the post-processed form of `my_pkg` (from " Example 2-59 "). Lines of code in " Example 2-59 " that are not included in the post-processed text appear as blank lines.

```
CALL DBMS_PREPROCESSOR.PRINT_POST_PROCESSED_SOURCE (
  'PACKAGE', 'HR', 'MY_PKG'
);
```

Result:

```
PACKAGE my_pkg AUTHID DEFINERs AS
SUBTYPE my_real IS
BINARY_DOUBLE;
my_pi my_real;
my_e my_real;
END my_pkg;
```

### Conditional Compilation Directive Restrictions

Conditional compilation directives are subject to these semantic restrictions.

A conditional compilation directive cannot appear in the specification of a schema-level user-defined type (created with the " [CREATE TYPE Statement](CREATE-TYPE-statement.md) "). This type specification specifies the attribute structure of the type, which determines the attribute structure of dependent types and the column structure of dependent tables.

Caution:

Using a conditional compilation directive to change the attribute structure of a type can cause dependent objects to "go out of sync" or dependent tables to become inaccessible. Oracle recommends that you change the attribute structure of a type only with the " [ALTER TYPE Statement](ALTER-TYPE-statement.md) ". The `ALTER` `TYPE` statement propagates changes to dependent objects.

If a conditional compilation directive is used in a schema-level type specification, the compiler raises the error `PLS-00180: preprocessor directives are not supported in this context.`

As all conditional compiler constructs are processed by the PL/SQL preprocessor, the SQL Parser imposes the following restrictions on the location of the first conditional compilation directive in a stored PL/SQL unit or anonymous block:

- In a package specification, a package body, a type body, a schema-level function and in a schema-level procedure, at least one nonwhitespace PL/SQL token must appear after the identifier of the unit name before a conditional compilation directive is valid.
	Note:
	- The PL/SQL comments, "--" or "/\*", are counted as whitespace tokens.
	- If the token is invalid in PL/SQL, then a PLS-00103 error is issued. But if a conditional compilation directive is used in violation of this rule, then an ORA error is produced.
	Example 2-61 and Example 2-62, show that the first conditional compilation directive appears after the first PL/SQL token that follows the identifier of the unit being defined.
- In a trigger or an anonymous block, the first conditional compilation directive cannot appear before the keyword `DECLARE` or `BEGIN`, whichever comes first.

The SQL parser also imposes this restriction: If an anonymous block uses a placeholder, the placeholder cannot appear in a conditional compilation directive. For example:

```
BEGIN
  :n := 1; -- valid use of placeholder
  $IF ... $THEN
    :n := 1; -- invalid use of placeholder
$END
```

Example 2-61 Using Conditional Compilation Directive in the Definition of a Package Specification

This example shows the placement of the first conditional compilation directive after an `AUTHID` clause, but before the keyword `IS`, in the definition of the package specification.

```
CREATE OR REPLACE PACKAGE cc_pkg
AUTHID DEFINER
$IF $$XFLAG $THEN ACCESSIBLE BY(p1_pkg) $END
IS
    i NUMBER := 10;
    trace CONSTANT BOOLEAN := TRUE;
END cc_pkg;
```

Result:

```
Package created.
```

Example 2-62 Using Conditional Compilation Directive in the Formal Parameter List of a Subprogram

This example shows the placement of the first conditional compilation directive after the left parenthesis, in the formal parameter list of a PL/SQL procedure definition.

```
CREATE OR REPLACE PROCEDURE my_proc (
  $IF $$xxx $THEN i IN PLS_INTEGER $ELSE i IN INTEGER $END
) IS 
BEGIN 
      NULL; 
END my_proc;
```

Result:

```
Procedure created.
```