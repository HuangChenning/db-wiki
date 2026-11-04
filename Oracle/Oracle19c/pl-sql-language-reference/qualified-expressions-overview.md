---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/qualified-expressions-overview.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Qualified Expressions Overview

Qualified expressions improve program clarity and developer productivity by providing the ability to declare and define a complex value in a compact form where the value is needed.

A qualified expression combines expression elements to create values of a `RECORD` type or associative array type.

Qualified expressions use an explicit type indication to provide the type of the qualified item. This explicit indication is known as a `typemark`.

The syntax for qualified expressions is:

qualified\_expression::= typemark ( aggregate )

aggregate::= \[ positional\_choice\_list \] \[explicit\_choice\_list\]

positional\_choice\_list::= (expr )+

explicit\_choice\_list::= named\_choice\_list | indexed\_choice\_list

named\_choice\_list::= identifier => expr \[,\]+

indexed\_choice\_list::= expr => expr \[,\] +

See [qualified\_expression::=](expression.md) for more information about the syntax and semantics.

Example 5-8 Assigning Values to RECORD Type Variables Using Qualified Expressions

This example shows the declaration, initialization, and definition of RECORD type variables. Type rec\_t is defined and partially initialized in package pkg. Variable v\_rec1 is declared with that type and assigned initial values using the positional notation. Variable v\_rec2 is declared with that type as well and assigned initial values using the named association syntax. Variable v\_rec3 is assigned the NULL values. The procedure print\_rec displays the values of the local variable v\_rec1, followed by the procedure parameter pi\_rec variable values. If no parameter is passed to the procedure, it displays the initial values set in the procedure definition.

Live SQL:

You can view and run this example on Oracle Live SQL at [18c Assigning Values to RECORD Type Variables Using Qualified Expressions](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/rec-agg.html)

```
CREATE PACKAGE pkg IS
  TYPE rec_t IS RECORD
   (year PLS_INTEGER := 2,
    name VARCHAR2 (100) );
END;
```
```
DECLARE
  v_rec1 pkg.rec_t := pkg.rec_t(1847,'ONE EIGHT FOUR SEVEN');
  v_rec2 pkg.rec_t := pkg.rec_t(year => 1, name => 'ONE');
  v_rec3 pkg.rec_t := pkg.rec_t(NULL,NULL);

PROCEDURE print_rec ( pi_rec pkg.rec_t := pkg.rec_t(1847+1,  'a'||'b')) IS
  v_rec1 pkg.rec_t := pkg.rec_t(2847,'TWO EIGHT FOUR SEVEN');
BEGIN
  DBMS_OUTPUT.PUT_LINE(NVL(v_rec1.year,0) ||' ' ||NVL(v_rec1.name,'N/A'));
  DBMS_OUTPUT.PUT_LINE(NVL(pi_rec.year,0) ||' ' ||NVL(pi_rec.name,'N/A'));
END;
BEGIN
  print_rec(v_rec1);
  print_rec(v_rec2);
  print_rec(v_rec3);
  print_rec();
END;
```
```
2847 TWO EIGHT FOUR SEVEN
1847 ONE EIGHT FOUR SEVEN
2847 TWO EIGHT FOUR SEVEN
1 ONE
2847 TWO EIGHT FOUR SEVEN
0 N/A
2847 TWO EIGHT FOUR SEVEN
1848 ab
```

Example 5-9 Assigning Values to Associative Array Type Variables Using Qualified Expressions

This example uses a function to display the values of a table of `BOOLEAN`.

Live SQL:

You can view and run this example on Oracle Live SQL at [18c Assigning Values to RECORD Type Variables Using Qualified Expressions](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/aa-agg.html)

```
CREATE FUNCTION print_bool (v IN BOOLEAN)
  RETURN VARCHAR2
IS
  v_rtn VARCHAR2(10);
BEGIN
  CASE v
  WHEN TRUE THEN
    v_rtn := 'TRUE';
  WHEN FALSE THEN
    v_rtn := 'FALSE';
  ELSE
    v_rtn := 'NULL';
  END CASE;
  RETURN v_rtn;
END print_bool;
```

The variable v\_aa1 is initialized using index key-value pairs.

```
DECLARE
  TYPE t_aa IS TABLE OF BOOLEAN INDEX BY PLS_INTEGER;
  v_aa1 t_aa := t_aa(1=>FALSE,
                     2=>TRUE,
                     3=>NULL);
BEGIN
  DBMS_OUTPUT.PUT_LINE(print_bool(v_aa1(1)));
  DBMS_OUTPUT.PUT_LINE(print_bool(v_aa1(2)));
  DBMS_OUTPUT.PUT_LINE(print_bool(v_aa1(3)));
END;
```
```
FALSE
TRUE
NULL
```