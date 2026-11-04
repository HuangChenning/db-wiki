---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/pls_integer-and-binary_integer-data-types.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## PLS\_INTEGER and BINARY\_INTEGER Data Types

The PL/SQL data types `PLS_INTEGER` and `BINARY_INTEGER` are identical.

For simplicity, this document uses `PLS_INTEGER` to mean both `PLS_INTEGER` and `BINARY_INTEGER`.

The `PLS_INTEGER` data type stores signed integers in the range -2,147,483,648 through 2,147,483,647, represented in 32 bits.

The `PLS_INTEGER` data type has these advantages over the `NUMBER` data type and `NUMBER` subtypes:

- `PLS_INTEGER` values require less storage.
- `PLS_INTEGER` operations use hardware arithmetic, so they are faster than `NUMBER` operations, which use library arithmetic.

For efficiency, use `PLS_INTEGER` values for all calculations in its range.

Topics

### Preventing PLS\_INTEGER Overflow

A calculation with two `PLS_INTEGER` values that overflows the `PLS_INTEGER` range raises an overflow exception.

For calculations outside the `PLS_INTEGER` range, use `INTEGER`, a predefined subtype of the `NUMBER` data type.

Example 3-4 PLS\_INTEGER Calculation Raises Overflow Exception

This example shows that a calculation with two `PLS_INTEGER` values that overflows the `PLS_INTEGER` range raises an overflow exception, even if you assign the result to a `NUMBER` data type.

```
DECLARE
  p1 PLS_INTEGER := 2147483647;
  p2 PLS_INTEGER := 1;
  n NUMBER;
BEGIN
  n := p1 + p2;
END;
/
```

Result:

```
DECLARE
*
ERROR at line 1:
ORA-01426: numeric overflow
ORA-06512: at line 6
```

Example 3-5 Preventing Example 3-4 Overflow

This example shows the correct use of the `INTEGER` predefined subtype for calculations outside the `PLS_INTEGER` range.

```
DECLARE
  p1 PLS_INTEGER := 2147483647;
  p2 INTEGER := 1;
  n NUMBER;
BEGIN
  n := p1 + p2;
END;
/
```

Result:

```
PL/SQL procedure successfully completed.
```

### Predefined PLS\_INTEGER Subtypes

This summary lists the predefined subtypes of the `PLS_INTEGER` data type and describes the data they store.

Table 3-3 Predefined Subtypes of PLS\_INTEGER Data Type

| Data Type | Data Description |
| --- | --- |
| `NATURAL` | Nonnegative `PLS_INTEGER` value |
| `NATURALN` | Nonnegative `PLS_INTEGER` value with `NOT NULL` constraint |
| `POSITIVE` | Positive `PLS_INTEGER` value |
| `POSITIVEN` | Positive `PLS_INTEGER` value with `NOT NULL` constraint |
| `SIGNTYPE` | `PLS_INTEGER` value -1, 0, or 1 (useful for programming tri-state logic) |
| `SIMPLE_INTEGER` | `PLS_INTEGER` value with `NOT` `NULL` constraint. |

`PLS_INTEGER` and its subtypes can be implicitly converted to these data types:

- `CHAR`
- `VARCHAR2`
- `NUMBER`
- `LONG`

All of the preceding data types except `LONG`, and all `PLS_INTEGER` subtypes, can be implicitly converted to `PLS_INTEGER`.

A `PLS_INTEGER` value can be implicitly converted to a `PLS_INTEGER` subtype only if the value does not violate a constraint of the subtype.

See Also:

- " [NOT NULL Constraint](declarations.md) "for information about the `NOT` `NULL` constraint
- " SIMPLE\_INTEGER Subtype of PLS\_INTEGER " for more information about `SIMPLE_INTEGER`

Example 3-6 Violating Constraint of SIMPLE\_INTEGER Subtype

This example shows that casting the `PLS_INTEGER` value `NULL` to the `SIMPLE_INTEGER` subtype raises an exception.

```
DECLARE
  a SIMPLE_INTEGER := 1;
  b PLS_INTEGER := NULL;
BEGIN
  a := b;
END;
/
```

Result:

```
DECLARE
*
ERROR at line 1:
ORA-06502: PL/SQL: numeric or value error
ORA-06512: at line 5
```

### SIMPLE\_INTEGER Subtype of PLS\_INTEGER

`SIMPLE_INTEGER` is a predefined subtype of the `PLS_INTEGER` data type.

`SIMPLE_INTEGER` has the same range as `PLS_INTEGER` and has a `NOT` `NULL` constraint. It differs significantly from `PLS_INTEGER` in its overflow semantics.

If you know that a variable will never have the value `NULL` or need overflow checking, declare it as `SIMPLE_INTEGER` rather than `PLS_INTEGER`. Without the overhead of checking for nullness and overflow, `SIMPLE_INTEGER` performs significantly better than `PLS_INTEGER`.

Topics

#### SIMPLE\_INTEGER Overflow Semantics

If and only if all operands in an expression have the data type `SIMPLE_INTEGER`, PL/SQL uses two's complement arithmetic and ignores overflows.

Because overflows are ignored, values can wrap from positive to negative or from negative to positive; for example:

2 <sup>30</sup> + 2 <sup>30</sup> = 0x40000000 + 0x40000000 = 0x80000000 = -2 <sup>31</sup>

\-2 <sup>31</sup> + -2 <sup>31</sup> = 0x80000000 + 0x80000000 = 0x00000000 = 0

For example, this block runs without errors:

```
DECLARE
  n SIMPLE_INTEGER := 2147483645;
BEGIN
  FOR j IN 1..4 LOOP
    n := n + 1;
    DBMS_OUTPUT.PUT_LINE(TO_CHAR(n, 'S9999999999'));
  END LOOP;
  FOR j IN 1..4 LOOP
   n := n - 1;
   DBMS_OUTPUT.PUT_LINE(TO_CHAR(n, 'S9999999999'));
  END LOOP;
END;
/
```

Result:

```
+2147483646
+2147483647
-2147483648
-2147483647
-2147483648
+2147483647
+2147483646
+2147483645

PL/SQL procedure successfully completed.
```

#### Expressions with Both SIMPLE\_INTEGER and Other Operands

If an expression has both `SIMPLE_INTEGER` and other operands, PL/SQL implicitly converts the `SIMPLE_INTEGER` values to `PLS_INTEGER` `NOT` `NULL`.

The PL/SQL compiler issues a warning when `SIMPLE_INTEGER` and other values are mixed in a way that might negatively impact performance by inhibiting some optimizations.

#### Integer Literals in SIMPLE\_INTEGER Range

Integer literals in the `SIMPLE_INTEGER` range have the data type `SIMPLE_INTEGER`.

However, to ensure backward compatibility, when all operands in an arithmetic expression are integer literals, PL/SQL treats the integer literals as if they were cast to `PLS_INTEGER`.