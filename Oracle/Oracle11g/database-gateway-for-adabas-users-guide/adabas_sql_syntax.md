---
title: Supported SQL Syntax and Functions
book: "Database Gateway for Adabas User's Guide"
doc_id: E12074-01
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/adabas_sql_syntax.htm
tags:
  - oracle
  - 11g
  - database-gateway-for-adabas-users-guide
---

## B Supported SQL Syntax and Functions

This appendix contains the following sections:

- Supported SQL Statements
- Oracle Functions

See Also:

Oracle Database SQL Reference for detailed descriptions of keywords, parameters, and options and the Adabas documentation for details of executing SQL statements in a transaction.

## Supported SQL Statements

With a few exceptions, the gateway provides full support for Oracle `DELETE`, `INSERT`, `SELECT`, and `UPDATE` statements.

The gateway does not support Oracle data definition language (DDL) statements. No form of the Oracle `ALTER`, `CREATE`, `DROP`, `GRANT`, or `TRUNCATE` statements can be used. Instead, for `ALTER`, `CREATE`, `DROP`, and `GRANT` statements, use the pass-through feature of the gateway if you need to use DDL statements against the Adabas database.

Note:

`TRUNCATE` cannot be used in a pass-through statement.

### DELETE

The `DELETE` statement is fully supported. However, only Oracle functions supported by Adabas can be used.

See Also:

Functions Supported by Adabas for a list of supported functions.

### INSERT

The `INSERT` statement is fully supported. However, only Oracle functions supported by Adabas can be used.

See Also:

Functions Supported by Adabas for a list of supported functions.

### SELECT

The `SELECT` statement is fully supported, with these exceptions:

- CONNECT BY condition
- NOWAIT
- START WITH condition
- WHERE CURRENT OF

### UPDATE

The `UPDATE` statement is fully supported. However, only Oracle functions supported by Adabas can be used. Also, you cannot have SQL statements in the subquery that refer to the same table name in the outer query. Subqueries are not supported in the SET clause.

See Also:

Functions Supported by Adabas for a list of supported functions.

## Oracle Functions

All functions are evaluated by the Adabas database after the gateway has converted them to Adabas SQL.

### Functions Not Supported by Adabas

Oracle SQL functions with no equivalent function in Adabas are not supported in `DELETE`, `INSERT`, or `UPDATE` statements, but are evaluated by the Oracle Database if the statement is a `SELECT` statement. That is, the Oracle Database performs post-processing of `SELECT` statements sent to the gateway.

If an unsupported function is used in a `DELETE`, `INSERT`, or `UPDATE`, statement, the following Oracle error occurs:

```
ORA-02070: database db_link_name does not support function in this context
```

### Functions Supported by Adabas

The gateway translates the following Oracle Database functions in SQL statements to their equivalent Adabas functions:

- Arithmetic Operators
- Comparison Operators
- Group Functions
- String Functions
- Other Functions

#### Arithmetic Operators

The following table specifies the arithmetic operators.

| Oracle | Adabas |
| --- | --- |
| + | + |
| \- | \- |
| \* | \* |
| / | / |

#### Comparison Operators

The following table specifies the comparison operators.

| Oracle | Adabas |
| --- | --- |
| \= | \= |
| \> | \> |
| < | < |
| \>= | \>= |
| <= | <= |
| <>,!=, ^= | <>,!= |
| IS NOT NULL | IS NOT NULL |
| IS NULL | IS NULL |

#### Group Functions

The following table specifies the group functions.

| Oracle | Adabas |
| --- | --- |
| AVG | AVG |
| COUNT | COUNT |
| MAX | MAX |
| MIN | MIN |
| SUM | SUM |

#### String Functions

The following table specifies the string functions.

| Oracle | Adabas |
| --- | --- |
| \|\| | \+ (expression1 + expression2) |
| ASCII | ASCII |
| CHR | CHAR |
| INSTR | CHARINDEX |
| LENGTH | CHAR\_LENGTH |
| LOWER | LOWER |
| SUBSTR (second argument cannot be a negative number) | SUBSTRING |
| UPPER | UPPER |

#### Other Functions

The following table specifies other functions.

| Oracle | Adabas |
| --- | --- |
| ABS | ABS |
| CEIL | CEILING |
| COS | COS |
| EXP | EXP |
| FLOOR | FLOOR |
| LN | LOG |
| LOG | LOG10 |
| MOD | % |
| NVL | IS NULL |
| POWER | POWER |
| ROUND | ROUND |
| SIN | SIN |
| SQRT | SQRT |
| TAN | TAN |