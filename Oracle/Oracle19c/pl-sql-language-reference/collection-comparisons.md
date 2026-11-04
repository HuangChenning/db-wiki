---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/collection-comparisons.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Collection Comparisons

To determine if one collection variable is less than another (for example), you must define what less than means in that context and write a function that returns `TRUE` or `FALSE`.

You cannot compare associative array variables to the value `NULL` or to each other.

Except for Comparing Nested Tables for Equality and Inequality, you cannot natively compare two collection variables with relational operators. This restriction also applies to implicit comparisons. For example, a collection variable cannot appear in a `DISTINCT`, `GROUP` `BY`, or `ORDER` `BY` clause.

Topics

See Also:

- [Table 2-5](expressions.md)
- [PL/SQL Subprograms](plsql-subprograms.md) for information about writing functions

### Comparing Varray and Nested Table Variables to NULL

Use the `IS[NOT] NULL` operator when comparing to the NULL value.

You can compare varray and nested table variables to the value `NULL` with the " [IS \[NOT\] NULL Operator](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/expressions.html#GUID-D02FA4D0-0074-4227-9624-F01E3D219BAB "The IS NULL operator returns the BOOLEAN value TRUE if its operand is NULL or FALSE if it is not NULL. The IS NOT NULL operator does the opposite.") ", but not with the relational operators equal (`=`) and not equal (`<>`, `!=`, `~=`, or ` ^=`).

Example 5-16 Comparing Varray and Nested Table Variables to NULL

This example compares a varray variable and a nested table variable to `NULL` correctly.

```
DECLARE  
  TYPE Foursome IS VARRAY(4) OF VARCHAR2(15);  -- VARRAY type
  team Foursome;                               -- varray variable
  
  TYPE Roster IS TABLE OF VARCHAR2(15);        -- nested table type
  names Roster := Roster('Adams', 'Patel');    -- nested table variable
  
BEGIN
  IF team IS NULL THEN
    DBMS_OUTPUT.PUT_LINE('team IS NULL');
  ELSE
    DBMS_OUTPUT.PUT_LINE('team IS NOT NULL');
  END IF;
 
  IF names IS NOT NULL THEN
    DBMS_OUTPUT.PUT_LINE('names IS NOT NULL');
  ELSE
    DBMS_OUTPUT.PUT_LINE('names IS NULL');
  END IF;
END;
/
```

Result:

```
team IS NULL
names IS NOT NULL
```

### Comparing Nested Tables for Equality and Inequality

Two nested table variables are equal if and only if they have the same set of elements (in any order).

If two nested table variables have the same nested table type, and that nested table type does not have elements of a record type, then you can compare the two variables for equality or inequality with the relational operators equal (`=`) and not equal (`<>`, `!=`, `~=`, ` ^=`).

See Also:

" [Record Comparisons](record-comparisons.md) "

Example 5-17 Comparing Nested Tables for Equality and Inequality

This example compares nested table variables for equality and inequality with relational operators.

Live SQL:

You can view and run this example on Oracle Live SQL at [Comparing Nested Tables for Equality and Inequality](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/lnplscomposites95.html)

```
DECLARE
  TYPE dnames_tab IS TABLE OF VARCHAR2(30); -- element type is not record type

  dept_names1 dnames_tab :=
    dnames_tab('Shipping','Sales','Finance','Payroll');

  dept_names2 dnames_tab :=
    dnames_tab('Sales','Finance','Shipping','Payroll');

  dept_names3 dnames_tab :=
    dnames_tab('Sales','Finance','Payroll');

BEGIN
  IF dept_names1 = dept_names2 THEN
    DBMS_OUTPUT.PUT_LINE('dept_names1 = dept_names2');
  END IF;

  IF dept_names2 != dept_names3 THEN
    DBMS_OUTPUT.PUT_LINE('dept_names2 != dept_names3');
  END IF;
END;
/
```

Result:

```
dept_names1 = dept_names2
dept_names2 != dept_names3
```

### Comparing Nested Tables with SQL Multiset Conditions

You can compare nested table variables, and test some of their properties, with SQL multiset conditions.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF52128) for more information about multiset conditions
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF06305) for details about `CARDINALITY` syntax
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF06308) for details about `SET` syntax

Example 5-18 Comparing Nested Tables with SQL Multiset Conditions

This example uses the SQL multiset conditions and two SQL functions that take nested table variable arguments, `CARDINALITY` and `SET`.

Live SQL:

You can view and run this example on Oracle Live SQL at [Comparing Nested Tables with SQL Multiset Conditions](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/tdlnplscomposites24.html)

```
DECLARE
  TYPE nested_typ IS TABLE OF NUMBER;
  nt1 nested_typ := nested_typ(1,2,3);
  nt2 nested_typ := nested_typ(3,2,1);
  nt3 nested_typ := nested_typ(2,3,1,3);
  nt4 nested_typ := nested_typ(1,2,4);
 
  PROCEDURE testify (
    truth BOOLEAN := NULL,
    quantity NUMBER := NULL
  ) IS
  BEGIN
    IF truth IS NOT NULL THEN
      DBMS_OUTPUT.PUT_LINE (
        CASE truth
           WHEN TRUE THEN 'True'
           WHEN FALSE THEN 'False'
        END
      );
    END IF;
    IF quantity IS NOT NULL THEN
        DBMS_OUTPUT.PUT_LINE(quantity);
    END IF;
  END;
BEGIN
  testify(truth => (nt1 IN (nt2,nt3,nt4)));        -- condition
  testify(truth => (nt1 SUBMULTISET OF nt3));      -- condition
  testify(truth => (nt1 NOT SUBMULTISET OF nt4));  -- condition
  testify(truth => (4 MEMBER OF nt1));             -- condition
  testify(truth => (nt3 IS A SET));                -- condition
  testify(truth => (nt3 IS NOT A SET));            -- condition
  testify(truth => (nt1 IS EMPTY));                -- condition
  testify(quantity => (CARDINALITY(nt3)));         -- function
  testify(quantity => (CARDINALITY(SET(nt3))));    -- 2 functions
END;
/
```

Result:

```
True
True
True
False
False
True
False
4
3
```