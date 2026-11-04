---
title: SQL Language Quick Reference
book: SQL Language Quick Reference
doc_id: F31302-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlqr/SQL-Expressions.html
tags:
  - oracle
  - 21c
  - sql-language-quick-reference
---

This chapter presents the syntax for combining values, operators, and functions into expressions.

This chapter includes the following section:

- Syntax for SQL Expression Types

### Syntax for SQL Expression Types

An expression is a combination of one or more values, operators, and SQL functions that evaluate to a value. An expression generally assumes the data type of its components.

Expressions have several forms. The sections that follow show the syntax for each form of expression. Refer to [Subclauses](Subclauses.md) for the syntax of the subclauses.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF004) for detailed information about SQL expressions

[Calculated Measure Expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-2E9CCE5B-D490-414F-A111-7741EBB1B933)

```
{    av_meas_expression
   | av_simple_expression
   | single_row_function_expression
   | case_expression
   | compound_expression
   | datetime_expression
   | interval_expression
}
```

[CASE expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF20037)

```
CASE { simple_case_expression
     | searched_case_expression
     }
     [ else_clause ]
     END
```

[Column expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF20043)

A column expression can be a simple expression, compound expression, function expression, or expression list, containing only columns of the subject table, constants, and deterministic functions.

[Compound expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52070)

```
{ (expr)
| { + | - | PRIOR } expr
| expr { * | / | + | - | || } expr
| expr COLLATE collation_name
}

Note: The double vertical bars are part of the syntax
      (indicating concatenation) rather than BNF notation.
```

[CURSOR expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52077)

```
CURSOR (subquery)
```

[Datetime expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00401)

```
expr AT
   { LOCAL
   | TIME ZONE { ' [ + | - ] hh:mi'
               | DBTIMEZONE
               | 'time_zone_name'
               | expr
               }
   }
```

[Function expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52082)

You can use any built-in SQL function or user-defined function as an expression.

[Interval expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52084)

```
( expr1 - expr2 )
   { DAY [ (leading_field_precision) ] TO
     SECOND [ (fractional_second_precision) ]
   | YEAR [ (leading_field_precision) ] TO
     MONTH
   }
```

[JSON object access expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF57024)

```
table_alias.JSON_column [.JSON_object_key [ array_step ]... ]...
```

[Model expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52086)

```
{ measure_column [ { condition | expr } [, { condition | expr } ]... ]
| aggregate_function 
     { [ { condition | expr } [, { condition | expr } ]... ]
     | [ single_column_for_loop [, single_column_for_loop ]... ]
     | [ multi_column_for_loop ]
     }
| analytic_function
}

Note: The outside square brackets shown in boldface type are part of
      the syntax. In this case, they do not represent optionality.
```

[Object access expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52088)

```
{ table_alias.column.
| object_table_alias.
| (expr).
}
{ attribute [.attribute ]...
  [.method ([ argument [, argument ]... ]) ]
| method ([ argument [, argument ]... ])
}
```

[Placeholder expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52091)

```
:host_variable
   [ [ INDICATOR ]
     :indicator_variable
   ]
```

[Scalar subquery expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52093)

A scalar subquery expression is a subquery that returns exactly one column value from one row.

[Simple expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52068)

```
{ [ query_name.
  | [schema.] { table. | view. | materialized view. }
  | t_alias.
  ] { column | ROWID }
| ROWNUM
| string
| number
| sequence. { CURRVAL | NEXTVAL }
| NULL
}
```

[Type constructor expressions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52094)

```
[ NEW ] [ schema. ]type_name
   ([ expr [, expr ]... ])
```