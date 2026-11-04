---
title: SQL Language Quick Reference
book: SQL Language Quick Reference
doc_id: F31302-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlqr/SQL-Conditions.html
tags:
  - oracle
  - 21c
  - sql-language-quick-reference
---

This chapter presents the syntax for combining one or more expressions and logical (Boolean) operators to specify a condition.

This chapter includes the following section:

- Syntax for SQL Condition Types

### Syntax for SQL Condition Types

A condition specifies a combination of one or more expressions and logical (Boolean) operators and returns a value of `TRUE`, `FALSE`, or unknown.

Conditions have several forms. The sections that follow show the syntax for each form of condition. Refer to [Subclauses](Subclauses.md) for the syntax of the subclauses.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF005) for detailed information about SQL conditions

[BETWEEN condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52164)

```
expr1 [ NOT ] BETWEEN expr2 AND expr3
```

[Compound conditions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52162)

```
{ (condition)
| NOT condition
| condition { AND | OR } condition
}
```

[EQUALS\_PATH condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52156)

```
EQUALS_PATH
    (column, path_string [, correlation_integer ])
```

[EXISTS condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52167)

```
EXISTS (subquery)
```

[Floating-point conditions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52113)

```
expr IS [ NOT ] { NAN | INFINITE }
```

[Group comparison conditions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52110)

```
{ expr
     { = | != | ^= | <> | > | < | >= | <= }
     { ANY | SOME | ALL }
     ({ expression_list | subquery })
| ( expr [, expr ]... )
  { = | != | ^= | <> }
  { ANY | SOME | ALL }
  ({ expression_list
     [, expression_list ]...
   | subquery
   }
  )
}
```

where `!=`, ` ^=`, and `<>` test for inequality

[IN condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52169)

```
{ expr [ NOT ] IN ({ expression_list | subquery })
| ( expr [, expr ]... )
    [ NOT ] IN ({ expression_list [, expression_list ]...
                | subquery
                }
               )
}
```

[IS A SET condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52129)

```
nested_table IS [ NOT ] A SET
```

[IS ANY condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52122)

```
[ dimension_column IS ] ANY
```

[IS EMPTY condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52132)

```
nested_table IS [ NOT ] EMPTY
```

[IS JSON condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56661)

```
expr IS [ NOT ] JSON [ FORMAT JSON ] [ STRICT | LAX ]
[ { WITH | WITHOUT } UNIQUE KEYS ]
```

[IS OF type condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52174)

```
expr IS [ NOT ] OF [ TYPE ]
   ([ ONLY ] [ schema. ] type
      [, [ ONLY ] [ schema. ] type ]...
   )
```

[IS PRESENT condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52125)

```
cell_reference IS PRESENT
```

[JSON\_EQUAL condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF-GUID-579717DA-62E8-406D-8513-36A69929BF0B)

```
JSON_EQUAL ( (expr), (expr) )
```

[JSON\_EXISTS condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56664)

```
JSON_EXISTS( expr [ FORMAT JSON ], JSON_basic_path_expression
  [ JSON_passing_clause ] [ JSON_exists_on_error_clause ] [ JSON_exists_on_empty_clause ] )
```

[JSON\_TEXTCONTAINS condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF56963)

```
JSON_TEXTCONTAINS( column, JSON_basic_path_expression, string )
```

[LIKE condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52142)

```
char1 [ NOT ] { LIKE | LIKEC | LIKE2 | LIKE4 }
  char2 [ ESCAPE esc_char ]
```

[Logical conditions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52116)

```
{ NOT | AND | OR }
```

[MEMBER condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52135)

```
expr [ NOT ] MEMBER [ OF ] nested_table
```

[Null conditions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52152)

```
expr IS [ NOT ] NULL
```

[REGEXP\_LIKE condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00501)

```
REGEXP_LIKE(source_char, pattern
            [, match_param ]
           )
```

[Simple comparison conditions](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52107)

```
{ expr 
  { = | != | ^= | <> | > | < | >= | <= }
  expr
| (expr [, expr ]...)
  { = | != | ^= | <> }
  ( expression_list | subquery )
}
```

where `!=`, ` ^=`, and `<>` test for inequality

[SUBMULTISET condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52138)

```
nested_table1
[ NOT ] SUBMULTISET [ OF ]
nested_table2
```

[UNDER\_PATH condition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF52159)

```
UNDER_PATH (column [, levels ], path_string
             [, correlation_integer ]
           )
```