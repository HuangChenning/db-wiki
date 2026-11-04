---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/multidimensional-collections.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Multidimensional Collections

Although a collection has only one dimension, you can model a multidimensional collection with a collection whose elements are collections.

Example 5-13 Two-Dimensional Varray (Varray of Varrays)

In this example, `nva` is a two-dimensional varray—a varray of varrays of integers.

Live SQL:

You can view and run this example on Oracle Live SQL at [Two-Dimensional Varray (Varray of Varrays)](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/composites25.html)

```
DECLARE
  TYPE t1 IS VARRAY(10) OF INTEGER;  -- varray of integer
  va t1 := t1(2,3,5);

  TYPE nt1 IS VARRAY(10) OF t1;      -- varray of varray of integer
  nva nt1 := nt1(va, t1(55,6,73), t1(2,4), va);

  i INTEGER;
  va1 t1;
BEGIN
  i := nva(2)(3);
  DBMS_OUTPUT.PUT_LINE('i = ' || i);

  nva.EXTEND;
  nva(5) := t1(56, 32);          -- replace inner varray elements
  nva(4) := t1(45,43,67,43345);  -- replace an inner integer element
  nva(4)(4) := 1;                -- replace 43345 with 1

  nva(4).EXTEND;    -- add element to 4th varray element
  nva(4)(5) := 89;  -- store integer 89 there
END;
/
```

Result:

```
i = 73
```

Example 5-14 Nested Tables of Nested Tables and Varrays of Integers

In this example, `ntb1` is a nested table of nested tables of strings, and `ntb2` is a nested table of varrays of integers.

Live SQL:

You can view and run this example on Oracle Live SQL at [Nested Tables of Nested Tables and Varrays of Integers](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/composites26.html)

```
DECLARE
  TYPE tb1 IS TABLE OF VARCHAR2(20);  -- nested table of strings
  vtb1 tb1 := tb1('one', 'three');

  TYPE ntb1 IS TABLE OF tb1; -- nested table of nested tables of strings
  vntb1 ntb1 := ntb1(vtb1);

  TYPE tv1 IS VARRAY(10) OF INTEGER;  -- varray of integers
  TYPE ntb2 IS TABLE OF tv1;          -- nested table of varrays of integers
  vntb2 ntb2 := ntb2(tv1(3,5), tv1(5,7,3));

BEGIN
  vntb1.EXTEND;
  vntb1(2) := vntb1(1);
  vntb1.DELETE(1);     -- delete first element of vntb1
  vntb1(2).DELETE(1);  -- delete first string from second table in nested table
END;
/
```

Example 5-15 Nested Tables of Associative Arrays and Varrays of Strings

In this example, `aa1` is an associative array of associative arrays, and `ntb2` is a nested table of varrays of strings.

Live SQL:

You can view and run this example on Oracle Live SQL at [Nested Tables of Associative Arrays and Varrays of Strings](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/composites27.html)

```
DECLARE
  TYPE tb1 IS TABLE OF INTEGER INDEX BY PLS_INTEGER;  -- associative arrays
  v4 tb1;
  v5 tb1;

  TYPE aa1 IS TABLE OF tb1 INDEX BY PLS_INTEGER;  -- associative array of
  v2 aa1;                                         --  associative arrays

  TYPE va1 IS VARRAY(10) OF VARCHAR2(20);  -- varray of strings
  v1 va1 := va1('hello', 'world');

  TYPE ntb2 IS TABLE OF va1 INDEX BY PLS_INTEGER;  -- associative array of varrays
  v3 ntb2;

BEGIN
  v4(1)   := 34;     -- populate associative array
  v4(2)   := 46456;
  v4(456) := 343;

  v2(23) := v4;  -- populate associative array of associative arrays

  v3(34) := va1(33, 456, 656, 343);  -- populate associative array varrays

  v2(35) := v5;      -- assign empty associative array to v2(35)
  v2(35)(2) := 78;
END;
/
```