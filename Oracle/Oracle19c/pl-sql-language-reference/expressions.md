---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/expressions.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Expressions

An expression is a combination of one or more values, operators, and SQL functions that evaluates to a value.

An expression always returns a single value. The simplest expressions, in order of increasing complexity, are:

1. A single constant or variable (for example, `a`)
2. A unary operator and its single operand (for example, `-a`)
3. A binary operator and its two operands (for example, `a+b`)

An operand can be a variable, constant, literal, operator, function invocation, or placeholder—or another expression. Therefore, expressions can be arbitrarily complex. For expression syntax, see [Expression](expression.md).

The data types of the operands determine the data type of the expression. Every time the expression is evaluated, a single value of that data type results. The data type of that result is the data type of the expression.

### Concatenation Operator

The concatenation operator (`||`) appends one string operand to another.

The concatenation operator ignores null operands.

For more information about the syntax of the concatenation operator, see " [character\_expression::=](expression.md) ".

Example 2-28 Concatenation Operator

```
DECLARE
  x VARCHAR2(4) := 'suit';
  y VARCHAR2(4) := 'case';
BEGIN
  DBMS_OUTPUT.PUT_LINE (x || y);
END;
/
```

Result:

```
suitcase
```

Example 2-29 Concatenation Operator with NULL Operands

The concatenation operator ignores null operands, as this example shows.

```
BEGIN
  DBMS_OUTPUT.PUT_LINE ('apple' || NULL || NULL || 'sauce');
END;
/
```

Result:

```
applesauce
```

### Operator Precedence

An operation is either a unary operator and its single operand or a binary operator and its two operands. The operations in an expression are evaluated in order of operator precedence.

Table 2-3 shows operator precedence from highest to lowest. Operators with equal precedence are evaluated in no particular order.

Table 2-3 Operator Precedence

| Operator | Operation |
| --- | --- |
| `**` | exponentiation |
| `+`, `-` | identity, negation |
| `*`, `/` | multiplication, division |
| `+`, `-`, `\|\|` | addition, subtraction, concatenation |
| `=`, `<`, `>`, `<=`, `>=`, `<>`, `!=`, `~=`, ` ^=`, `IS` `NULL`, `LIKE`, `BETWEEN`, `IN` | comparison |
| `NOT` | negation |
| `AND` | conjunction |
| `OR` | inclusion |

To control the order of evaluation, enclose operations in parentheses, as in Example 2-30.

When parentheses are nested, the most deeply nested operations are evaluated first.

You can also use parentheses to improve readability where the parentheses do not affect evaluation order.

Example 2-30 Controlling Evaluation Order with Parentheses

```
DECLARE
  a INTEGER := 1+2**2;
  b INTEGER := (1+2)**2;
BEGIN
  DBMS_OUTPUT.PUT_LINE('a = ' || TO_CHAR(a));
  DBMS_OUTPUT.PUT_LINE('b = ' || TO_CHAR(b));
END;
/
```

Result:

```
a = 5
b = 9
```

Example 2-31 Expression with Nested Parentheses

In this example, the operations (1+2) and (3+4) are evaluated first, producing the values 3 and 7, respectively. Next, the operation 3\*7 is evaluated, producing the result 21. Finally, the operation 21/7 is evaluated, producing the final value 3.

```
DECLARE
  a INTEGER := ((1+2)*(3+4))/7;
BEGIN
  DBMS_OUTPUT.PUT_LINE('a = ' || TO_CHAR(a));
END;
/
```

Result:

```
a = 3
```

Example 2-32 Improving Readability with Parentheses

In this example, the parentheses do not affect the evaluation order. They only improve readability.

```
DECLARE
  a INTEGER := 2**2*3**2;
  b INTEGER := (2**2)*(3**2);
BEGIN
  DBMS_OUTPUT.PUT_LINE('a = ' || TO_CHAR(a));
  DBMS_OUTPUT.PUT_LINE('b = ' || TO_CHAR(b));
END;
/
```

Result:

```
a = 36
b = 36
```

Example 2-33 Operator Precedence

This example shows the effect of operator precedence and parentheses in several more complex expressions.

```
DECLARE
  salary      NUMBER := 60000;
  commission  NUMBER := 0.10;
BEGIN
  -- Division has higher precedence than addition:
  
  DBMS_OUTPUT.PUT_LINE('5 + 12 / 4 = ' || TO_CHAR(5 + 12 / 4));
  DBMS_OUTPUT.PUT_LINE('12 / 4 + 5 = ' || TO_CHAR(12 / 4 + 5));
  
 -- Parentheses override default operator precedence:
 
  DBMS_OUTPUT.PUT_LINE('8 + 6 / 2 = ' || TO_CHAR(8 + 6 / 2));
  DBMS_OUTPUT.PUT_LINE('(8 + 6) / 2 = ' || TO_CHAR((8 + 6) / 2));
 
  -- Most deeply nested operation is evaluated first:
 
  DBMS_OUTPUT.PUT_LINE('100 + (20 / 5 + (7 - 3)) = '
                      || TO_CHAR(100 + (20 / 5 + (7 - 3))));
 
  -- Parentheses, even when unnecessary, improve readability:
 
  DBMS_OUTPUT.PUT_LINE('(salary * 0.05) + (commission * 0.25) = '
    || TO_CHAR((salary * 0.05) + (commission * 0.25))
  );
 
  DBMS_OUTPUT.PUT_LINE('salary * 0.05 + commission * 0.25 = '
    || TO_CHAR(salary * 0.05 + commission * 0.25)
  );
END;
/
```

Result:

```
5 + 12 / 4 = 8
12 / 4 + 5 = 8
8 + 6 / 2 = 11
(8 + 6) / 2 = 7
100 + (20 / 5 + (7 - 3)) = 108
(salary * 0.05) + (commission * 0.25) = 3000.025
salary * 0.05 + commission * 0.25 = 3000.025
```

### Logical Operators

The logical operators `AND`, `OR`, and `NOT` follow a tri-state logic.

`AND` and `OR` are binary operators; `NOT` is a unary operator.

Table 2-4 Logical Truth Table

| x | y | x AND y | x OR y | NOT x |
| --- | --- | --- | --- | --- |
| `TRUE` | `TRUE` | `TRUE` | `TRUE` | `FALSE` |
| `TRUE` | `FALSE` | `FALSE` | `TRUE` | `FALSE` |
| `TRUE` | `NULL` | `NULL` | `TRUE` | `FALSE` |
| `FALSE` | `TRUE` | `FALSE` | `TRUE` | `TRUE` |
| `FALSE` | `FALSE` | `FALSE` | `FALSE` | `TRUE` |
| `FALSE` | `NULL` | `FALSE` | `NULL` | `TRUE` |
| `NULL` | `TRUE` | `NULL` | `TRUE` | `NULL` |
| `NULL` | `FALSE` | `FALSE` | `NULL` | `NULL` |
| `NULL` | `NULL` | `NULL` | `NULL` | `NULL` |

`AND` returns `TRUE` if and only if both operands are `TRUE`.

`OR` returns `TRUE` if either operand is `TRUE`.

`NOT` returns the opposite of its operand, unless the operand is `NULL`. `NOT` `NULL` returns `NULL`, because `NULL` is an indeterminate value.

Example 2-34 Procedure Prints BOOLEAN Variable

This example creates a procedure, `print_boolean`, that prints the value of a `BOOLEAN` variable. The procedure uses the " [IS \[NOT\] NULL Operator](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/expressions.html#GUID-D02FA4D0-0074-4227-9624-F01E3D219BAB "The IS NULL operator returns the BOOLEAN value TRUE if its operand is NULL or FALSE if it is not NULL. The IS NOT NULL operator does the opposite.") ". Several examples in this chapter invoke `print_boolean`.

```
CREATE OR REPLACE PROCEDURE print_boolean (
  b_name   VARCHAR2,
  b_value  BOOLEAN
) AUTHID DEFINER IS
BEGIN
  IF b_value IS NULL THEN
    DBMS_OUTPUT.PUT_LINE (b_name || ' = NULL');
  ELSIF b_value = TRUE THEN
    DBMS_OUTPUT.PUT_LINE (b_name || ' = TRUE');
  ELSE
    DBMS_OUTPUT.PUT_LINE (b_name || ' = FALSE');
  END IF;
END;
/
```

Example 2-35 AND Operator

As Table 2-4 and this example show, `AND` returns `TRUE` if and only if both operands are `TRUE`.

```
DECLARE
  PROCEDURE print_x_and_y (
    x  BOOLEAN,
    y  BOOLEAN
  ) IS
  BEGIN
   print_boolean ('x', x);
   print_boolean ('y', y);
   print_boolean ('x AND y', x AND y);
 END print_x_and_y;
 
BEGIN
 print_x_and_y (FALSE, FALSE);
 print_x_and_y (TRUE, FALSE);
 print_x_and_y (FALSE, TRUE);
 print_x_and_y (TRUE, TRUE);
 
 print_x_and_y (TRUE, NULL);
 print_x_and_y (FALSE, NULL);
 print_x_and_y (NULL, TRUE);
 print_x_and_y (NULL, FALSE);
END;
/
```

Result:

```
x = FALSE
y = FALSE
x AND y = FALSE
x = TRUE
y = FALSE
x AND y = FALSE
x = FALSE
y = TRUE
x AND y = FALSE
x = TRUE
y = TRUE
x AND y = TRUE
x = TRUE
y = NULL
x AND y = NULL
x = FALSE
y = NULL
x AND y = FALSE
x = NULL
y = TRUE
x AND y = NULL
x = NULL
y = FALSE
x AND y = FALSE
```

Example 2-36 OR Operator

As Table 2-4 and this example show, `OR` returns `TRUE` if either operand is `TRUE`. (This example invokes the `print_boolean` procedure from Example 2-34.)

```
DECLARE
  PROCEDURE print_x_or_y (
    x  BOOLEAN,
    y  BOOLEAN
  ) IS
  BEGIN
    print_boolean ('x', x);
    print_boolean ('y', y);
    print_boolean ('x OR y', x OR y);
  END print_x_or_y;
 
BEGIN
  print_x_or_y (FALSE, FALSE);
  print_x_or_y (TRUE, FALSE);
  print_x_or_y (FALSE, TRUE);
  print_x_or_y (TRUE, TRUE);
 
  print_x_or_y (TRUE, NULL);
  print_x_or_y (FALSE, NULL);
  print_x_or_y (NULL, TRUE);
  print_x_or_y (NULL, FALSE);
END;
/
```

Result:

```
x = FALSE
y = FALSE
x OR y = FALSE
x = TRUE
y = FALSE
x OR y = TRUE
x = FALSE
y = TRUE
x OR y = TRUE
x = TRUE
y = TRUE
x OR y = TRUE
x = TRUE
y = NULL
x OR y = TRUE
x = FALSE
y = NULL
x OR y = NULL
x = NULL
y = TRUE
x OR y = TRUE
x = NULL
y = FALSE
x OR y = NULL
```

Example 2-37 NOT Operator

As Table 2-4 and this example show, `NOT` returns the opposite of its operand, unless the operand is `NULL`. `NOT` `NULL` returns `NULL`, because `NULL` is an indeterminate value. (This example invokes the `print_boolean` procedure from Example 2-34.)

```
DECLARE
  PROCEDURE print_not_x (
    x  BOOLEAN
  ) IS
  BEGIN
    print_boolean ('x', x);
    print_boolean ('NOT x', NOT x);
  END print_not_x;
 
BEGIN
  print_not_x (TRUE);
  print_not_x (FALSE);
  print_not_x (NULL);
END;
/
```

Result:

```
x = TRUE
NOT x = FALSE
x = FALSE
NOT x = TRUE
x = NULL
NOT x = NULL
```

Example 2-38 NULL Value in Unequal Comparison

In this example, you might expect the sequence of statements to run because `x` and `y` seem unequal. But, `NULL` values are indeterminate. Whether `x` equals `y` is unknown. Therefore, the `IF` condition yields `NULL` and the sequence of statements is bypassed.

```
DECLARE
  x NUMBER := 5;
  y NUMBER := NULL;
BEGIN
  IF x != y THEN  -- yields NULL, not TRUE
    DBMS_OUTPUT.PUT_LINE('x != y');  -- not run
  ELSIF x = y THEN -- also yields NULL
    DBMS_OUTPUT.PUT_LINE('x = y');
  ELSE
    DBMS_OUTPUT.PUT_LINE
      ('Can''t tell if x and y are equal or not.');
  END IF;
END;
/
```

Result:

```
Can't tell if x and y are equal or not.
```

Example 2-39 NULL Value in Equal Comparison

In this example, you might expect the sequence of statements to run because `a` and `b` seem equal. But, again, that is unknown, so the `IF` condition yields `NULL` and the sequence of statements is bypassed.

```
DECLARE
  a NUMBER := NULL;
  b NUMBER := NULL;
BEGIN
  IF a = b THEN  -- yields NULL, not TRUE
    DBMS_OUTPUT.PUT_LINE('a = b');  -- not run
  ELSIF a != b THEN  -- yields NULL, not TRUE
    DBMS_OUTPUT.PUT_LINE('a != b');  -- not run
  ELSE
    DBMS_OUTPUT.PUT_LINE('Can''t tell if two NULLs are equal');
  END IF;
END;
/
```

Result:

```
Can't tell if two NULLs are equal
```

Example 2-40 NOT NULL Equals NULL

In this example, the two `IF` statements appear to be equivalent. However, if either `x` or `y` is `NULL`, then the first `IF` statement assigns the value of `y` to `high` and the second `IF` statement assigns the value of `x` to `high`.

```
DECLARE
  x    INTEGER := 2;
  Y    INTEGER := 5;
  high INTEGER;
BEGIN
  IF (x > y)       -- If x or y is NULL, then (x > y) is NULL
    THEN high := x;  -- run if (x > y) is TRUE
    ELSE high := y;  -- run if (x > y) is FALSE or NULL
  END IF;
  
  IF NOT (x > y)   -- If x or y is NULL, then NOT (x > y) is NULL
    THEN high := y;  -- run if NOT (x > y) is TRUE
    ELSE high := x;  -- run if NOT (x > y) is FALSE or NULL
  END IF;
END;
/
```

Example 2-41 Changing Evaluation Order of Logical Operators

This example invokes the `print_boolean` procedure from Example 2-34 three times. The third and first invocation are logically equivalent—the parentheses in the third invocation only improve readability. The parentheses in the second invocation change the order of operation.

```
DECLARE
  x  BOOLEAN := FALSE;
  y  BOOLEAN := FALSE;
  
BEGIN
  print_boolean ('NOT x AND y', NOT x AND y);
  print_boolean ('NOT (x AND y)', NOT (x AND y));
  print_boolean ('(NOT x) AND y', (NOT x) AND y);
END;
/
```

Result:

```
NOT x AND y = FALSE
NOT (x AND y) = TRUE
(NOT x) AND y = FALSE
```

### Short-Circuit Evaluation

When evaluating a logical expression, PL/SQL uses short-circuit evaluation. That is, PL/SQL stops evaluating the expression as soon as it can determine the result.

Therefore, you can write expressions that might otherwise cause errors.

In Example 2-42, short-circuit evaluation prevents the `OR` expression from causing a divide-by-zero error. When the value of `on_hand` is zero, the value of the left operand is `TRUE`, so PL/SQL does not evaluate the right operand. If PL/SQL evaluated both operands before applying the `OR` operator, the right operand would cause a division by zero error.

Example 2-42 Short-Circuit Evaluation

```
DECLARE
  on_hand  INTEGER := 0;
  on_order INTEGER := 100;
BEGIN
  -- Does not cause divide-by-zero error;
  -- evaluation stops after first expression
  
  IF (on_hand = 0) OR ((on_order / on_hand) < 5) THEN
    DBMS_OUTPUT.PUT_LINE('On hand quantity is zero.');
  END IF;
END;
/
```

Result:

```
On hand quantity is zero.
```

### Comparison Operators

Comparison operators compare one expression to another. The result is always either `TRUE`, `FALSE`, or `NULL`.

If the value of one expression is `NULL`, then the result of the comparison is also `NULL`.

The comparison operators are:

- [IS \[NOT\] NULL Operator](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/expressions.html#GUID-D02FA4D0-0074-4227-9624-F01E3D219BAB "The IS NULL operator returns the BOOLEAN value TRUE if its operand is NULL or FALSE if it is not NULL. The IS NOT NULL operator does the opposite.")
- Relational Operators
- LIKE Operator
- BETWEEN Operator
- IN Operator

Note:

Character comparisons are affected by NLS parameter settings, which can change at runtime. Therefore, character comparisons are evaluated at runtime, and the same character comparison can have different values at different times. For information about NLS parameters that affect character comparisons, see [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=NLSPG005).

Note:

Using `CLOB` values with comparison operators can create temporary LOB values. Ensure that your temporary tablespace is large enough to handle them.

#### IS \[NOT\] NULL Operator

The `IS` `NULL` operator returns the `BOOLEAN` value `TRUE` if its operand is `NULL` or `FALSE` if it is not `NULL`. The `IS` `NOT` `NULL` operator does the opposite.

Comparisons involving `NULL` values always yield `NULL`.

To test whether a value is `NULL`, use `IF` `value` `IS` `NULL`, as in these examples:

- [Example 2-14](declarations.md), "Variable Initialized to NULL by Default"
- Example 2-34, "Procedure Prints BOOLEAN Variable"
- Example 2-53, "Searched CASE Expression with WHEN... IS NULL"

#### Relational Operators

This table summarizes the relational operators.

Table 2-5 Relational Operators

| Operator | Meaning |
| --- | --- |
| `=` | equal to |
| `<>`, `!=`, `~=`, ` ^=` | not equal to |
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |

Topics

##### Arithmetic Comparisons

One number is greater than another if it represents a larger quantity.

Real numbers are stored as approximate values, so Oracle recommends comparing them for equality or inequality.

Example 2-43 Relational Operators in Expressions

This example invokes the `print_boolean` procedure from Example 2-35 to print the values of expressions that use relational operators to compare arithmetic values.

```
BEGIN
  print_boolean ('(2 + 2 =  4)', 2 + 2 = 4);
  
  print_boolean ('(2 + 2 <> 4)', 2 + 2 <> 4);
  print_boolean ('(2 + 2 != 4)', 2 + 2 != 4);
  print_boolean ('(2 + 2 ~= 4)', 2 + 2 ~= 4);
  print_boolean ('(2 + 2 ^= 4)', 2 + 2  ^= 4);
  
  print_boolean ('(1 < 2)', 1 < 2);
 
  print_boolean ('(1 > 2)', 1 > 2);
 
  print_boolean ('(1 <= 2)', 1 <= 2);
 
  print_boolean ('(1 >= 1)', 1 >= 1);
END;
/
```

Result:

```
(2 + 2 =  4) = TRUE
(2 + 2 <> 4) = FALSE
(2 + 2 != 4) = FALSE
(2 + 2 ~= 4) = FALSE
(2 + 2 ^= 4) = FALSE
(1 < 2) = TRUE
(1 > 2) = FALSE
(1 <= 2) = TRUE
(1 >= 1) = TRUE
```

##### BOOLEAN Comparisons

By definition, `TRUE` is greater than `FALSE`. Any comparison with `NULL` returns `NULL`.

##### Character Comparisons

By default, one character is greater than another if its binary value is larger.

For example, this expression is true:

```
'y' > 'r'
```

Strings are compared character by character. For example, this expression is true:

```
'Kathy' > 'Kathryn'
```

If you set the initialization parameter `NLS_COMP=ANSI`, string comparisons use the collating sequence identified by the `NLS_SORT` initialization parameter.

A collating sequence is an internal ordering of the character set in which a range of numeric codes represents the individual characters. One character value is greater than another if its internal numeric value is larger. Each language might have different rules about where such characters occur in the collating sequence. For example, an accented letter might be sorted differently depending on the database character set, even though the binary value is the same in each case.

By changing the value of the `NLS_SORT` parameter, you can perform comparisons that are case-insensitive and accent-insensitive.

A case-insensitive comparison treats corresponding uppercase and lowercase letters as the same letter. For example, these expressions are true:

```
'a' = 'A'
'Alpha' = 'ALPHA'
```

To make comparisons case-insensitive, append `_CI` to the value of the `NLS_SORT` parameter (for example, `BINARY_CI` or `XGERMAN_CI`).

An accent-insensitive comparison is case-insensitive, and also treats letters that differ only in accents or punctuation characters as the same letter. For example, these expressions are true:

```
'Cooperate' = 'Co-Operate'
'Co-Operate' = 'coöperate'
```

To make comparisons both case-insensitive and accent-insensitive, append `_AI` to the value of the `NLS_SORT` parameter (for example, `BINARY_AI` or `FRENCH_M_AI`).

Semantic differences between the `CHAR` and `VARCHAR2` data types affect character comparisons.

For more information, see " [Value Comparisons](sql-data-types.md) ".

##### Date Comparisons

One date is greater than another if it is more recent.

For example, this expression is true:

```
'01-JAN-91' > '31-DEC-90'
```

#### LIKE Operator

The `LIKE` operator compares a character, string, or `CLOB` value to a pattern and returns `TRUE` if the value matches the pattern and `FALSE` if it does not.

Case is significant.

The pattern can include the two wildcard characters underscore (`_`) and percent sign (%).

Underscore matches exactly one character.

Percent sign (`%`) matches zero or more characters.

To search for the percent sign or underscore, define an escape character and put it before the percent sign or underscore.

Example 2-44 LIKE Operator in Expression

The string `'Johnson'` matches the pattern `'J%s_n'` but not `'J%S_N'`, as this example shows.

```
DECLARE
  PROCEDURE compare (
    value   VARCHAR2,
    pattern VARCHAR2
  ) IS
  BEGIN
    IF value LIKE pattern THEN
      DBMS_OUTPUT.PUT_LINE ('TRUE');
    ELSE
      DBMS_OUTPUT.PUT_LINE ('FALSE');
    END IF;
  END;
BEGIN
  compare('Johnson', 'J%s_n');
  compare('Johnson', 'J%S_N');
END;
/
```

Result:

```
TRUE
FALSE
```

Example 2-45 Escape Character in Pattern

This example uses the backslash as the escape character, so that the percent sign in the string does not act as a wildcard.

```
DECLARE
  PROCEDURE half_off (sale_sign VARCHAR2) IS
  BEGIN
    IF sale_sign LIKE '50\% off!' ESCAPE '\' THEN
      DBMS_OUTPUT.PUT_LINE ('TRUE');
    ELSE
      DBMS_OUTPUT.PUT_LINE ('FALSE');
    END IF;
  END;
BEGIN
  half_off('Going out of business!');
  half_off('50% off!');
END;
/
```

Result:

```
FALSE
TRUE
```

#### BETWEEN Operator

The `BETWEEN` operator tests whether a value lies in a specified range.

The value of the expression `x BETWEEN a AND b` is defined to be the same as the value of the expression `(x>=a) AND (x<=b)`. The expression `x` will only be evaluated once.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF52164) for more information about `BETWEEN`

Example 2-46 BETWEEN Operator in Expressions

This example invokes the `print_boolean` procedure from Example 2-34 to print the values of expressions that include the `BETWEEN` operator.

```
BEGIN
  print_boolean ('2 BETWEEN 1 AND 3', 2 BETWEEN 1 AND 3);
  print_boolean ('2 BETWEEN 2 AND 3', 2 BETWEEN 2 AND 3);
  print_boolean ('2 BETWEEN 1 AND 2', 2 BETWEEN 1 AND 2);
  print_boolean ('2 BETWEEN 3 AND 4', 2 BETWEEN 3 AND 4);
END;
/
```

Result:

```
2 BETWEEN 1 AND 3 = TRUE
2 BETWEEN 2 AND 3 = TRUE
2 BETWEEN 1 AND 2 = TRUE
2 BETWEEN 3 AND 4 = FALSE
```

#### IN Operator

The `IN` operator tests set membership.

`x` `IN` `(``set``)` returns `TRUE` only if `x` equals a member of `set`.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF52169) for more information about `IN`

Example 2-47 IN Operator in Expressions

This example invokes the `print_boolean` procedure from Example 2-34 to print the values of expressions that include the `IN` operator.

```
DECLARE
  letter VARCHAR2(1) := 'm';
BEGIN
  print_boolean (
    'letter IN (''a'', ''b'', ''c'')',
    letter IN ('a', 'b', 'c')
  );
  print_boolean (
    'letter IN (''z'', ''m'', ''y'', ''p'')',
    letter IN ('z', 'm', 'y', 'p')
  );
END;
/
```

Result:

```
letter IN ('a', 'b', 'c') = FALSE
letter IN ('z', 'm', 'y', 'p') = TRUE
```

Example 2-48 IN Operator with Sets with NULL Values

This example shows what happens when `set` includes a `NULL` value. This invokes the `print_boolean` procedure from Example 2-34.

```
DECLARE
  a INTEGER; -- Initialized to NULL by default
  b INTEGER := 10;
  c INTEGER := 100;
BEGIN
  print_boolean ('100 IN (a, b, c)', 100 IN (a, b, c));
  print_boolean ('100 NOT IN (a, b, c)', 100 NOT IN (a, b, c));
  
  print_boolean ('100 IN (a, b)', 100 IN (a, b));
  print_boolean ('100 NOT IN (a, b)', 100 NOT IN (a, b));
 
  print_boolean ('a IN (a, b)', a IN (a, b));
  print_boolean ('a NOT IN (a, b)', a NOT IN (a, b));
END;
/
```

Result:

```
100 IN (a, b, c) = TRUE
100 NOT IN (a, b, c) = FALSE
100 IN (a, b) = NULL
100 NOT IN (a, b) = NULL
a IN (a, b) = NULL
a NOT IN (a, b) = NULL
```

### BOOLEAN Expressions

A `BOOLEAN` expression is an expression that returns a `BOOLEAN` value— `TRUE`, `FALSE`, or `NULL`.

The simplest `BOOLEAN` expression is a `BOOLEAN` literal, constant, or variable. The following are also `BOOLEAN` expressions:

```
NOT boolean_expression
boolean_expression relational_operator boolean_expression
boolean_expression { AND | OR } boolean_expression
```

For a list of relational operators, see Table 2-5. For the complete syntax of a `BOOLEAN` expression, see " [boolean\_expression::=](expression.md) ".

Typically, you use `BOOLEAN` expressions as conditions in control statements (explained in [PL/SQL Control Statements](plsql-control-statements.md)) and in `WHERE` clauses of DML statements.

You can use a `BOOLEAN` variable itself as a condition; you need not compare it to the value `TRUE` or `FALSE`.

Example 2-49 Equivalent BOOLEAN Expressions

In this example, the conditions in the loops are equivalent.

```
DECLARE
  done BOOLEAN;
BEGIN
  -- These WHILE loops are equivalent
  
  done := FALSE;
  WHILE done = FALSE
    LOOP
      done := TRUE;
    END LOOP;
 
  done := FALSE;
  WHILE NOT (done = TRUE)
    LOOP
      done := TRUE;
    END LOOP;
 
  done := FALSE;
  WHILE NOT done
    LOOP
      done := TRUE;
    END LOOP;
END;
/
```

### CASE Expressions

Topics

- Simple CASE Expression
- Searched CASE Expression

#### Simple CASE Expression

For this explanation, assume that a simple `CASE` expression has this syntax:

```
CASE selector
WHEN selector_value_1 THEN result_1
WHEN selector_value_2 THEN result_2
...
WHEN selector_value_n THEN result_n
[ ELSE
  else_result ]
END
```

The `selector` is an expression (typically a single variable). Each `selector_value` and each `result` can be either a literal or an expression. At least one `result` must not be the literal `NULL`.

The simple `CASE` expression returns the first `result` for which `selector_value` matches `selector`. Remaining expressions are not evaluated. If no `selector_value` matches `selector`, the `CASE` expression returns `else_result` if it exists and `NULL` otherwise.

See Also:

" [simple\_case\_expression::=](expression.md) " for the complete syntax

Example 2-50 Simple CASE Expression

This example assigns the value of a simple `CASE` expression to the variable `appraisal`. The `selector` is `grade`.

```
DECLARE
  grade CHAR(1) := 'B';
  appraisal VARCHAR2(20);
BEGIN
  appraisal :=
    CASE grade
      WHEN 'A' THEN 'Excellent'
      WHEN 'B' THEN 'Very Good'
      WHEN 'C' THEN 'Good'
      WHEN 'D' THEN 'Fair'
      WHEN 'F' THEN 'Poor'
      ELSE 'No such grade'
    END;
    DBMS_OUTPUT.PUT_LINE ('Grade ' || grade || ' is ' || appraisal);
END;
/
```

Result:

```
Grade B is Very Good
```

Example 2-51 Simple CASE Expression with WHEN NULL

If `selector` has the value `NULL`, it cannot be matched by `WHEN` `NULL`, as this example shows.

Instead, use a searched `CASE` expression with `WHEN` `boolean_expression` `IS` `NULL`, as in Example 2-53.

```
DECLARE
  grade CHAR(1); -- NULL by default
  appraisal VARCHAR2(20);
BEGIN
  appraisal :=
  CASE grade
    WHEN NULL THEN 'No grade assigned'
    WHEN 'A' THEN 'Excellent'
    WHEN 'B' THEN 'Very Good'
    WHEN 'C' THEN 'Good'
    WHEN 'D' THEN 'Fair'
    WHEN 'F' THEN 'Poor'
    ELSE 'No such grade'
  END;
  DBMS_OUTPUT.PUT_LINE ('Grade ' || grade || ' is ' || appraisal);
END;
/
```

Result:

```
Grade  is No such grade
```

#### Searched CASE Expression

For this explanation, assume that a searched `CASE` expression has this syntax:

```
CASE
WHEN boolean_expression_1 THEN result_1
WHEN boolean_expression_2 THEN result_2
...
WHEN boolean_expression_n THEN result_n
[ ELSE
  else_result ]
END]
```

The searched `CASE` expression returns the first `result` for which `boolean_expression` is `TRUE`. Remaining expressions are not evaluated. If no `boolean_expression` is `TRUE`, the `CASE` expression returns `else_result` if it exists and `NULL` otherwise.

See Also:

" [searched\_case\_expression::=](expression.md) " for the complete syntax

Example 2-52 Searched CASE Expression

This example assigns the value of a searched `CASE` expression to the variable `appraisal`.

```
DECLARE
  grade      CHAR(1) := 'B';
  appraisal  VARCHAR2(120);
  id         NUMBER  := 8429862;
  attendance NUMBER := 150;
  min_days   CONSTANT NUMBER := 200;
  
  FUNCTION attends_this_school (id NUMBER)
    RETURN BOOLEAN IS
  BEGIN
    RETURN TRUE;
  END;
BEGIN
  appraisal :=
  CASE
    WHEN attends_this_school(id) = FALSE
      THEN 'Student not enrolled'
    WHEN grade = 'F' OR attendance < min_days
      THEN 'Poor (poor performance or bad attendance)'
    WHEN grade = 'A' THEN 'Excellent'
    WHEN grade = 'B' THEN 'Very Good'
    WHEN grade = 'C' THEN 'Good'
    WHEN grade = 'D' THEN 'Fair'
    ELSE 'No such grade'
  END;
  DBMS_OUTPUT.PUT_LINE
    ('Result for student ' || id || ' is ' || appraisal);
END;
/
```

Result:

```
Result for student 8429862 is Poor (poor performance or bad attendance)
```

Example 2-53 Searched CASE Expression with WHEN... IS NULL

This example uses a searched `CASE` expression to solve the problem in Example 2-51.

```
DECLARE
  grade CHAR(1); -- NULL by default
  appraisal VARCHAR2(20);
BEGIN
  appraisal :=
    CASE
      WHEN grade IS NULL THEN 'No grade assigned'
      WHEN grade = 'A' THEN 'Excellent'
      WHEN grade = 'B' THEN 'Very Good'
      WHEN grade = 'C' THEN 'Good'
      WHEN grade = 'D' THEN 'Fair'
      WHEN grade = 'F' THEN 'Poor'
      ELSE 'No such grade'
    END;
    DBMS_OUTPUT.PUT_LINE ('Grade ' || grade || ' is ' || appraisal);
END;
/
```

Result:

```
Grade  is No grade assigned
```

### SQL Functions in PL/SQL Expressions

In PL/SQL expressions, you can use all SQL functions except:

- Aggregate functions (such as `AVG` and `COUNT`)
- Analytic functions (such as `LAG` and `RATIO_TO_REPORT`)
- Data mining functions (such as `CLUSTER_ID` and `FEATURE_VALUE`)
- Encoding and decoding functions (such as `DECODE` and `DUMP`)
- Model functions (such as `ITERATION_NUMBER` and `PREVIOUS`)
- Object reference functions (such as `REF` and `VALUE`)
- XML functions
- These conversion functions:
	- `BIN_TO_NUM`
- These JSON SQL operators:
	- `JSON_ARRAYAGG`
		- `JSON_EQUAL`
		- `JSON_OBJECTAGG`
		- `JSON_TABLE`
		- `JSON_TEXTCONTAINS`
- These collation SQL operators and functions:
	- `COLLATE`
		- `COLLATION`
		- `NLS_COLLATION_ID`
		- `NLS_COLLATION_NAME`
- These miscellaneous functions:
	- `CUBE_TABLE`
		- `DATAOBJ_TO_PARTITION`
		- `LNNVL`
		- `NVL2`
		- `SYS_CONNECT_BY_PATH`
		- `SYS_TYPEID`
		- `WIDTH_BUCKET`

PL/SQL supports an overload of `BITAND` for which the arguments and result are `BINARY_INTEGER`.

When used in a PL/SQL expression, the `RAWTOHEX` function accepts an argument of data type `RAW` and returns a `VARCHAR2` value with the hexadecimal representation of bytes that comprise the value of the argument. Arguments of types other than `RAW` can be specified only if they can be implicitly converted to `RAW`. This conversion is possible for `CHAR`, `VARCHAR2`, and `LONG` values that are valid arguments of the `HEXTORAW` function, and for `LONG` `RAW` and `BLOB` values of up to 16380 bytes.

### Static Expressions

A static expression is an expression whose value can be determined at compile time—that is, it does not include character comparisons, variables, or function invocations. Static expressions are the only expressions that can appear in conditional compilation directives.

Definition of Static Expression

- An expression is static if it is the NULL literal.
- An expression is static if it is a character, numeric, or boolean literal.
- An expression is static if it is a reference to a static constant.
- An expression is static if it is a reference to a conditional compilation variable begun with $$.
- An expression is static if it is an operator is allowed in static expressions, if all of its operands are static, and if the operator does not raise an exception when it is evaluated on those operands.

Table 2-6 Operators Allowed in Static Expressions

<table><thead><tr align="left"><th align="left" width="20%">Operators</th><th align="left" width="20%">Operators Category</th></tr></thead><tbody><tr align="left"><td align="left" width="20%" headers="d19391e4462 ">()</td><td align="left" width="20%" headers="d19391e4470 d19391e4465 "><p>Expression delimiter</p></td></tr><tr align="left"><td rowspan="1" colspan="1" align="left" headers="d19391e4462 "><p>**</p></td><td rowspan="1" colspan="1" align="left" headers="d19391e4476 d19391e4465 "><p>exponentiation</p></td></tr><tr align="left"><td rowspan="1" colspan="1" align="left" headers="d19391e4462 "><p>*, /,+, -</p></td><td rowspan="1" colspan="1" align="left" headers="d19391e4483 d19391e4465 "><p>Arithmetic operators for multiplication, division, addition or positive, subtraction or negative</p></td></tr><tr align="left"><td rowspan="1" colspan="1" align="left" headers="d19391e4462 "><p>=,!=, <, <=, >=, > IS [NOT] NULL</p></td><td rowspan="1" colspan="1" align="left" headers="d19391e4490 d19391e4465 "><p>Comparison operators</p></td></tr><tr align="left"><td align="left" width="20%" headers="d19391e4462 "><p>NOT</p></td><td align="left" width="20%" headers="d19391e4497 d19391e4465 "><p>Logical operator</p></td></tr><tr align="left"><td align="left" width="20%" headers="d19391e4462 "><p>[NOT] LIKE, [NOT] LIKE2, [NOT] LIKE4, [NOT] LIKEC</p></td><td align="left" width="20%" headers="d19391e4504 d19391e4465 "><p>Pattern matching operators</p></td></tr><tr align="left"><td rowspan="1" colspan="1" align="left" headers="d19391e4462 "><p>XOR</p></td><td rowspan="1" colspan="1" align="left" headers="d19391e4511 d19391e4465 "><p>Binary operator</p></td></tr></tbody></table>

This list shows functions allowed in static expressions.

- ABS
- ACOS
- ASCII
- ASCIISTR
- ASIN
- ATAN
- ATAN2
- BITAND
- CEIL
- CHR
- COMPOSE
- CONVERT
- COS
- COSH
- DECOMPOSE
- EXP
- FLOOR
- HEXTORAW
- INSTR
- INSTRB
- INSTRC
- INSTR2
- INSTR4
- IS \[NOT\] INFINITE
- IS \[NOT\] NAN
- LENGTH
- LENGTH2
- LENGTH4
- LENGTHB
- LENGTHC
- LN
- LOG
- LOWER
- LPAD
- LTRIM
- MOD
- NVL
- POWER
- RAWTOHEX
- REM
- REMAINDER
- REPLACE
- ROUND
- RPAD
- RTRIM
- SIGN
- SIN
- SINH
- SQRT
- SUBSTR
- SUBSTR2
- SUBSTR4
- SUBSTRB
- SUBSTRC
- TAN
- TANH
- TO\_BINARY\_DOUBLE
- TO\_BINARY\_FLOAT
- TO\_CHAR
- TO\_NUMBER
- TRIM
- TRUNC
- UPPER

Static expressions can be used in the following subtype declarations:

- Length of string types (`VARCHAR2, NCHAR, CHAR, NVARCHAR2, RAW`, and the ANSI equivalents)
- Scale and precision of `NUMBER` types and subtypes such as `FLOAT`
- Interval type precision (year, month,second)
- Time and Timestamp precision
- `VARRAY` bounds
- Bounds of ranges in type declarations

In each case, the resulting type of the static expression must be the same as the declared item subtype and must be in the correct range for the context.

#### PLS\_INTEGER Static Expressions

`PLS_INTEGER` static expressions are:

- `PLS_INTEGER` literals
	For information about literals, see " [Literals](lexical-units.md) ".
- `PLS_INTEGER` static constants
	For information about static constants, see " Static Constants ".
- `NULL`

See Also:

" [PLS\_INTEGER and BINARY\_INTEGER Data Types](pls_integer-and-binary_integer-data-types.md) " for information about the `PLS_INTEGER` data type

#### BOOLEAN Static Expressions

`BOOLEAN` static expressions are:

- `BOOLEAN` literals (`TRUE`, `FALSE`, or `NULL`)
- `BOOLEAN` static constants
	For information about static constants, see " Static Constants ".
- Where `x` and `y` are `PLS_INTEGER` static expressions:
	- `x` `>` `y`
		- `x` `<` `y`
		- `x` `>=` `y`
		- `x` `<=` `y`
		- `x` `=` `y`
		- `x` `<>` `y`
	For information about `PLS_INTEGER` static expressions, see " PLS\_INTEGER Static Expressions ".
- Where `x` and `y` are `BOOLEAN` expressions:
	- `NOT` `y`
		- `x` `AND` `y`
		- `x` `OR` `y`
		- `x` `>` `y`
		- `x` `>=` `y`
		- `x` `=` `y`
		- `x` `<=` `y`
		- `x` `<>` `y`
	For information about `BOOLEAN` expressions, see " BOOLEAN Expressions ".
- Where `x` is a static expression:
	- `x` `IS` `NULL`
		- `x` `IS` `NOT` `NULL`
	For information about static expressions, see " Static Expressions ".

See Also:

" [BOOLEAN Data Type](boolean-data-type.md) " for information about the `BOOLEAN` data type

#### VARCHAR2 Static Expressions

`VARCHAR2` static expressions are:

- String literal with maximum size of 32,767 bytes
	For information about literals, see " [Literals](lexical-units.md) ".
- `NULL`
- `TO_CHAR(x)`, where `x` is a `PLS_INTEGER` static expression
	For information about the `TO_CHAR` function, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF06128).
- `TO_CHAR(x`, `f`, `n)` where `x` is a `PLS_INTEGER` static expression and `f` and `n` are `VARCHAR2` static expressions
	For information about the `TO_CHAR` function, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF06130).
- `x` `||` `y` where `x` and `y` are `VARCHAR2` or `PLS_INTEGER` static expressions
	For information about `PLS_INTEGER` static expressions, see " PLS\_INTEGER Static Expressions ".

See Also:

" [CHAR and VARCHAR2 Variables](sql-data-types.md) " for information about the `VARCHAR2` data type

#### Static Constants

A static constant is declared in a package specification with this syntax:

```
constant_name CONSTANT data_type := static_expression;
```

The type of `static_expression` must be the same as `data_type` (either `BOOLEAN` or `PLS_INTEGER`).

The static constant must always be referenced as `package_name`.`constant_name`, even in the body of the `package_name` package.

If you use `constant_name` in the `BOOLEAN` expression in a conditional compilation directive in a PL/SQL unit, then the PL/SQL unit depends on the package `package_name`. If you alter the package specification, the dependent PL/SQL unit might become invalid and need recompilation (for information about the invalidation of dependent objects, see [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADFNS99992)).

If you use a package with static constants to control conditional compilation in multiple PL/SQL units, Oracle recommends that you create only the package specification, and dedicate it exclusively to controlling conditional compilation. This practice minimizes invalidations caused by altering the package specification.

To control conditional compilation in a single PL/SQL unit, you can set flags in the `PLSQL_CCFLAGS` compilation parameter. For information about this parameter, see " [Assigning Values to Inquiry Directives](conditional-compilation1.md) " and [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=REFRN10261).

Example 2-54 Static Constants

In this example, the package `my_debug` defines the static constants `debug` and `trace` to control debugging and tracing in multiple PL/SQL units. The procedure `my_proc1` uses only `debug`, and the procedure `my_proc2` uses only `trace`, but both procedures depend on the package. However, the recompiled code might not be different. For example, if you only change the value of `debug` to `FALSE` and then recompile the two procedures, the compiled code for `my_proc1` changes, but the compiled code for `my_proc2` does not.

```
CREATE PACKAGE my_debug IS
  debug CONSTANT BOOLEAN := TRUE;
  trace CONSTANT BOOLEAN := TRUE;
END my_debug;
/
 
CREATE PROCEDURE my_proc1 AUTHID DEFINER IS
BEGIN
  $IF my_debug.debug $THEN
    DBMS_OUTPUT.put_line('Debugging ON');
  $ELSE
    DBMS_OUTPUT.put_line('Debugging OFF');
  $END
END my_proc1;
/
 
CREATE PROCEDURE my_proc2 AUTHID DEFINER IS
BEGIN
  $IF my_debug.trace $THEN
    DBMS_OUTPUT.put_line('Tracing ON');
  $ELSE
    DBMS_OUTPUT.put_line('Tracing OFF');
  $END
END my_proc2;
/
```