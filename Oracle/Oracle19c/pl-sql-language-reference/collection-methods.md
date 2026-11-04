---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/collection-methods.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Collection Methods

A collection method is a PL/SQL subprogram—either a function that returns information about a collection or a procedure that operates on a collection. Collection methods make collections easier to use and your applications easier to maintain.

Table 5-2 summarizes the collection methods.

Note:

With a null collection, `EXISTS` is the only collection method that does not raise the predefined exception `COLLECTION_IS_NULL`.

Table 5-2 Collection Methods

| Method | Type | Description |
| --- | --- | --- |
| `DELETE` | Procedure | Deletes elements from collection. |
| `TRIM` | Procedure | Deletes elements from end of varray or nested table. |
| `EXTEND` | Procedure | Adds elements to end of varray or nested table. |
| `EXISTS` | Function | Returns `TRUE` if and only if specified element of varray or nested table exists. |
| `FIRST` | Function | Returns first index in collection. |
| `LAST` | Function | Returns last index in collection. |
| `COUNT` | Function | Returns number of elements in collection. |
| `LIMIT` | Function | Returns maximum number of elements that collection can have. |
| `PRIOR` | Function | Returns index that precedes specified index. |
| `NEXT` | Function | Returns index that succeeds specified index. |

The basic syntax of a collection method invocation is:

```
collection_name.method
```

For detailed syntax, see " [Collection Method Invocation](collection-method.md) ".

A collection method invocation can appear anywhere that an invocation of a PL/SQL subprogram of its type (function or procedure) can appear, except in a SQL statement. (For general information about PL/SQL subprograms, see [PL/SQL Subprograms](plsql-subprograms.md).)

In a subprogram, a collection parameter assumes the properties of the argument bound to it. You can apply collection methods to such parameters. For varray parameters, the value of `LIMIT` is always derived from the parameter type definition, regardless of the parameter mode.

Topics

### DELETE Collection Method

`DELETE` is a procedure that deletes elements from a collection.

This method has these forms:

- `DELETE` deletes all elements from a collection of any type.
	This operation immediately frees the memory allocated to the deleted elements.
- From an associative array or nested table (but not a varray):
	- `DELETE(``n``)` deletes the element whose index is n, if that element exists; otherwise, it does nothing.
		- `DELETE(``m,n``)` deletes all elements whose indexes are in the range m..n, if both m and n exist and m <= n; otherwise, it does nothing.
	For these two forms of `DELETE`, PL/SQL keeps placeholders for the deleted elements. Therefore, the deleted elements are included in the internal size of the collection, and you can restore a deleted element by assigning a valid value to it.

Example 5-19 DELETE Method with Nested Table

This example declares a nested table variable, initializing it with six elements; deletes and then restores the second element; deletes a range of elements and then restores one of them; and then deletes all elements. The restored elements occupy the same memory as the corresponding deleted elements. The procedure `print_nt` prints the nested table variable after initialization and after each `DELETE` operation. The type `nt_type` and procedure `print_nt` are defined in [Example 5-6](nested-tables.md).

```
DECLARE
  nt nt_type := nt_type(11, 22, 33, 44, 55, 66);
BEGIN
  print_nt(nt);
 
  nt.DELETE(2);     -- Delete second element
  print_nt(nt);
 
  nt(2) := 2222;    -- Restore second element
  print_nt(nt);
 
  nt.DELETE(2, 4);  -- Delete range of elements
  print_nt(nt);
 
  nt(3) := 3333;    -- Restore third element
  print_nt(nt);
 
  nt.DELETE;        -- Delete all elements
  print_nt(nt);
END;
/
```

Result:

```
nt.(1) = 11
nt.(2) = 22
nt.(3) = 33
nt.(4) = 44
nt.(5) = 55
nt.(6) = 66
---
nt.(1) = 11
nt.(3) = 33
nt.(4) = 44
nt.(5) = 55
nt.(6) = 66
---
nt.(1) = 11
nt.(2) = 2222
nt.(3) = 33
nt.(4) = 44
nt.(5) = 55
nt.(6) = 66
---
nt.(1) = 11
nt.(5) = 55
nt.(6) = 66
---
nt.(1) = 11
nt.(3) = 3333
nt.(5) = 55
nt.(6) = 66
---
nt is empty
---
```

Example 5-20 DELETE Method with Associative Array Indexed by String

This example populates an associative array indexed by string and deletes all elements, which frees the memory allocated to them. Next, the example replaces the deleted elements—that is, adds new elements that have the same indexes as the deleted elements. The new replacement elements do not occupy the same memory as the corresponding deleted elements. Finally, the example deletes one element and then a range of elements. The procedure `print_aa_str` shows the effects of the operations.

```
DECLARE
  TYPE aa_type_str IS TABLE OF INTEGER INDEX BY VARCHAR2(10);
  aa_str  aa_type_str;
 
  PROCEDURE print_aa_str IS
    i  VARCHAR2(10);
  BEGIN
    i := aa_str.FIRST;
 
    IF i IS NULL THEN
      DBMS_OUTPUT.PUT_LINE('aa_str is empty');
    ELSE
      WHILE i IS NOT NULL LOOP
        DBMS_OUTPUT.PUT('aa_str.(' || i || ') = ');
        DBMS_OUTPUT.PUT_LINE(NVL(TO_CHAR(aa_str(i)), 'NULL'));
        i := aa_str.NEXT(i);
      END LOOP;
    END IF;
 
    DBMS_OUTPUT.PUT_LINE('---');
  END print_aa_str;
 
BEGIN
  aa_str('M') := 13;
  aa_str('Z') := 26;
  aa_str('C') := 3;
  print_aa_str;
 
  aa_str.DELETE;  -- Delete all elements
  print_aa_str;
 
  aa_str('M') := 13;   -- Replace deleted element with same value
  aa_str('Z') := 260;  -- Replace deleted element with new value
  aa_str('C') := 30;   -- Replace deleted element with new value
  aa_str('W') := 23;   -- Add new element
  aa_str('J') := 10;   -- Add new element
  aa_str('N') := 14;   -- Add new element
  aa_str('P') := 16;   -- Add new element
  aa_str('W') := 23;   -- Add new element
  aa_str('J') := 10;   -- Add new element
  print_aa_str;
 
  aa_str.DELETE('C');      -- Delete one element
  print_aa_str;
 
  aa_str.DELETE('N','W');  -- Delete range of elements
  print_aa_str;
 
  aa_str.DELETE('Z','M');  -- Does nothing
  print_aa_str;
END;
/
```

Result:

```
aa_str.(C) = 3
aa_str.(M) = 13
aa_str.(Z) = 26
---
aa_str is empty
---
aa_str.(C) = 30
aa_str.(J) = 10
aa_str.(M) = 13
aa_str.(N) = 14
aa_str.(P) = 16
aa_str.(W) = 23
aa_str.(Z) = 260
---
aa_str.(J) = 10
aa_str.(M) = 13
aa_str.(N) = 14
aa_str.(P) = 16
aa_str.(W) = 23
aa_str.(Z) = 260
---
aa_str.(J) = 10
aa_str.(M) = 13
aa_str.(Z) = 260
---
aa_str.(J) = 10
aa_str.(M) = 13
aa_str.(Z) = 260
---
```

### TRIM Collection Method

`TRIM` is a procedure that deletes elements from the end of a varray or nested table.

This method has these forms:

- `TRIM` removes one element from the end of the collection, if the collection has at least one element; otherwise, it raises the predefined exception `SUBSCRIPT_BEYOND_COUNT`.
- `TRIM(``n``)` removes n elements from the end of the collection, if there are at least n elements at the end; otherwise, it raises the predefined exception `SUBSCRIPT_BEYOND_COUNT`.

`TRIM` operates on the internal size of a collection. That is, if `DELETE` deletes an element but keeps a placeholder for it, then `TRIM` considers the element to exist. Therefore, `TRIM` can delete a deleted element.

PL/SQL does not keep placeholders for trimmed elements. Therefore, trimmed elements are not included in the internal size of the collection, and you cannot restore a trimmed element by assigning a valid value to it.

Caution:

Do not depend on interaction between `TRIM` and `DELETE`. Treat nested tables like either fixed-size arrays (and use only `DELETE`) or stacks (and use only `TRIM` and `EXTEND`).

Example 5-21 TRIM Method with Nested Table

This example declares a nested table variable, initializing it with six elements; trims the last element; deletes the fourth element; and then trims the last two elements—one of which is the deleted fourth element. The procedure `print_nt` prints the nested table variable after initialization and after the `TRIM` and `DELETE` operations. The type `nt_type` and procedure `print_nt` are defined in [Example 5-6](nested-tables.md).

```
DECLARE
  nt nt_type := nt_type(11, 22, 33, 44, 55, 66);
BEGIN
  print_nt(nt);

  nt.TRIM;       -- Trim last element
  print_nt(nt);

  nt.DELETE(4);  -- Delete fourth element
  print_nt(nt);

  nt.TRIM(2);    -- Trim last two elements
  print_nt(nt);
END;
/
```

Result:

```
nt.(1) = 11
nt.(2) = 22
nt.(3) = 33
nt.(4) = 44
nt.(5) = 55
nt.(6) = 66
---
nt.(1) = 11
nt.(2) = 22
nt.(3) = 33
nt.(4) = 44
nt.(5) = 55
---
nt.(1) = 11
nt.(2) = 22
nt.(3) = 33
nt.(5) = 55
---
nt.(1) = 11
nt.(2) = 22
nt.(3) = 33
---
```

### EXTEND Collection Method

`EXTEND` is a procedure that adds elements to the end of a varray or nested table.

The collection can be empty, but not null. (To make a collection empty or add elements to a null collection, use a constructor. For more information, see " [Collection Constructors](collection-constructors.md) ".)

The `EXTEND` method has these forms:

- `EXTEND` appends one null element to the collection.
- `EXTEND(``n``)` appends n null elements to the collection.
- `EXTEND(``n`,`i``)` appends n copies of the ith element to the collection.
	Note:
	`EXTEND(``n`,`i``)` is the only form that you can use for a collection whose elements have the `NOT` `NULL` constraint.

`EXTEND` operates on the internal size of a collection. That is, if `DELETE` deletes an element but keeps a placeholder for it, then `EXTEND` considers the element to exist.

Example 5-22 EXTEND Method with Nested Table

This example declares a nested table variable, initializing it with three elements; appends two copies of the first element; deletes the fifth (last) element; and then appends one null element. Because `EXTEND` considers the deleted fifth element to exist, the appended null element is the sixth element. The procedure `print_nt` prints the nested table variable after initialization and after the `EXTEND` and `DELETE` operations. The type `nt_type` and procedure `print_nt` are defined in [Example 5-6](nested-tables.md).

```
DECLARE
  nt nt_type := nt_type(11, 22, 33);
BEGIN
  print_nt(nt);
 
  nt.EXTEND(2,1);  -- Append two copies of first element
  print_nt(nt);
 
  nt.DELETE(5);    -- Delete fifth element
  print_nt(nt);
 
  nt.EXTEND;       -- Append one null element
  print_nt(nt);
END;
/
```

Result:

```
nt.(1) = 11
nt.(2) = 22
nt.(3) = 33
---
nt.(1) = 11
nt.(2) = 22
nt.(3) = 33
nt.(4) = 11
nt.(5) = 11
---
nt.(1) = 11
nt.(2) = 22
nt.(3) = 33
nt.(4) = 11
---
nt.(1) = 11
nt.(2) = 22
nt.(3) = 33
nt.(4) = 11
nt.(6) = NULL
---
```

### EXISTS Collection Method

`EXISTS` is a function that tells you whether the specified element of a varray or nested table exists.

`EXISTS(``n``)` returns `TRUE` if the nth element of the collection exists and `FALSE` otherwise. If n is out of range, `EXISTS` returns `FALSE` instead of raising the predefined exception `SUBSCRIPT_OUTSIDE_LIMIT`.

For a deleted element, `EXISTS(``n``)` returns `FALSE`, even if `DELETE` kept a placeholder for it.

Example 5-23 EXISTS Method with Nested Table

This example initializes a nested table with four elements, deletes the second element, and prints either the value or status of elements 1 through 6.

```
DECLARE
  TYPE NumList IS TABLE OF INTEGER;
  n NumList := NumList(1,3,5,7);
BEGIN
  n.DELETE(2); -- Delete second element
 
  FOR i IN 1..6 LOOP
    IF n.EXISTS(i) THEN
      DBMS_OUTPUT.PUT_LINE('n(' || i || ') = ' || n(i));
    ELSE
      DBMS_OUTPUT.PUT_LINE('n(' || i || ') does not exist');
    END IF;
  END LOOP;
END;
/
```

Result:

```
n(1) = 1
n(2) does not exist
n(3) = 5
n(4) = 7
n(5) does not exist
n(6) does not exist
```

### FIRST and LAST Collection Methods

`FIRST` and `LAST` are functions.

If the collection has at least one element, `FIRST` and `LAST` return the indexes of the first and last elements, respectively (ignoring deleted elements, even if `DELETE` kept placeholders for them). If the collection has only one element, `FIRST` and `LAST` return the same index. If the collection is empty, `FIRST` and `LAST` return `NULL`.

Topics

- FIRST and LAST Methods for Associative Array
- FIRST and LAST Methods for Varray
- FIRST and LAST Methods for Nested Table

#### FIRST and LAST Methods for Associative Array

For an associative array indexed by `PLS_INTEGER`, the first and last elements are those with the smallest and largest indexes, respectively. For an associative array indexed by string, the first and last elements are those with the lowest and highest key values, respectively.

Key values are in sorted order (for more information, see " [NLS Parameter Values Affect Associative Arrays Indexed by String](associative-arrays.md) ").

Example 5-24 FIRST and LAST Values for Associative Array Indexed by PLS\_INTEGER

This example shows the values of `FIRST` and `LAST` for an associative array indexed by `PLS_INTEGER`, deletes the first and last elements, and shows the values of `FIRST` and `LAST` again.

```
DECLARE
  TYPE aa_type_int IS TABLE OF INTEGER INDEX BY PLS_INTEGER;
  aa_int  aa_type_int;
 
  PROCEDURE print_first_and_last IS
  BEGIN
    DBMS_OUTPUT.PUT_LINE('FIRST = ' || aa_int.FIRST);
    DBMS_OUTPUT.PUT_LINE('LAST = ' || aa_int.LAST);
  END print_first_and_last;
 
BEGIN
  aa_int(1) := 3;
  aa_int(2) := 6;
  aa_int(3) := 9;
  aa_int(4) := 12;
 
  DBMS_OUTPUT.PUT_LINE('Before deletions:');
  print_first_and_last;
 
  aa_int.DELETE(1);
  aa_int.DELETE(4);
 
  DBMS_OUTPUT.PUT_LINE('After deletions:');
  print_first_and_last;
END;
/
```

Result:

```
Before deletions:
FIRST = 1
LAST = 4
After deletions:
FIRST = 2
LAST = 3
```

Example 5-25 FIRST and LAST Values for Associative Array Indexed by String

This example shows the values of `FIRST` and `LAST` for an associative array indexed by string, deletes the first and last elements, and shows the values of `FIRST` and `LAST` again.

```
DECLARE
  TYPE aa_type_str IS TABLE OF INTEGER INDEX BY VARCHAR2(10);
  aa_str  aa_type_str;
 
  PROCEDURE print_first_and_last IS
  BEGIN
    DBMS_OUTPUT.PUT_LINE('FIRST = ' || aa_str.FIRST);
    DBMS_OUTPUT.PUT_LINE('LAST = ' || aa_str.LAST);
  END print_first_and_last;
 
BEGIN
  aa_str('Z') := 26;
  aa_str('A') := 1;
  aa_str('K') := 11;
  aa_str('R') := 18;
 
  DBMS_OUTPUT.PUT_LINE('Before deletions:');
  print_first_and_last;
 
  aa_str.DELETE('A');
  aa_str.DELETE('Z');
 
  DBMS_OUTPUT.PUT_LINE('After deletions:');
  print_first_and_last;
END;
/
```

Result:

```
Before deletions:
FIRST = A
LAST = Z
After deletions:
FIRST = K
LAST = R
```

#### FIRST and LAST Methods for Varray

For a varray that is not empty, `FIRST` always returns 1. For every varray, `LAST` always equals `COUNT`.

Example 5-26 Printing Varray with FIRST and LAST in FOR LOOP

This example prints the varray `team` using a `FOR` `LOOP` statement with the bounds `team`.`FIRST` and `team`.`LAST`. Because a varray is always dense, `team(i)` inside the loop always exists.

```
DECLARE
  TYPE team_type IS VARRAY(4) OF VARCHAR2(15);
  team team_type;
 
  PROCEDURE print_team (heading VARCHAR2)
  IS
  BEGIN
    DBMS_OUTPUT.PUT_LINE(heading);
 
    IF team IS NULL THEN
      DBMS_OUTPUT.PUT_LINE('Does not exist');
    ELSIF team.FIRST IS NULL THEN
      DBMS_OUTPUT.PUT_LINE('Has no members');
    ELSE
      FOR i IN team.FIRST..team.LAST LOOP
        DBMS_OUTPUT.PUT_LINE(i || '. ' || team(i));
      END LOOP;
    END IF;
 
    DBMS_OUTPUT.PUT_LINE('---'); 
  END;
  
BEGIN 
  print_team('Team Status:');
 
  team := team_type();  -- Team is funded, but nobody is on it.
  print_team('Team Status:');
 
  team := team_type('John', 'Mary');  -- Put 2 members on team.
  print_team('Initial Team:');
 
  team := team_type('Arun', 'Amitha', 'Allan', 'Mae');  -- Change team.
  print_team('New Team:');
END;
/
```

Result:

```
Team Status:
Does not exist
---
Team Status:
Has no members
---
Initial Team:
1. John
2. Mary
---
New Team:
1. Arun
2. Amitha
3. Allan
4. Mae
---
```

#### FIRST and LAST Methods for Nested Table

For a nested table, `LAST` equals `COUNT` unless you delete elements from its middle, in which case `LAST` is larger than `COUNT`.

Example 5-27 Printing Nested Table with FIRST and LAST in FOR LOOP

This example prints the nested table `team` using a `FOR` `LOOP` statement with the bounds `team`.`FIRST` and `team`.`LAST`. Because a nested table can be sparse, the `FOR` `LOOP` statement prints `team(i)` only if `team`.`EXISTS(i)` is `TRUE`.

```
DECLARE
  TYPE team_type IS TABLE OF VARCHAR2(15);
  team team_type;
 
  PROCEDURE print_team (heading VARCHAR2) IS
  BEGIN
    DBMS_OUTPUT.PUT_LINE(heading);
 
    IF team IS NULL THEN
      DBMS_OUTPUT.PUT_LINE('Does not exist');
    ELSIF team.FIRST IS NULL THEN
      DBMS_OUTPUT.PUT_LINE('Has no members');
    ELSE
      FOR i IN team.FIRST..team.LAST LOOP
        DBMS_OUTPUT.PUT(i || '. ');
        IF team.EXISTS(i) THEN
          DBMS_OUTPUT.PUT_LINE(team(i));
        ELSE
          DBMS_OUTPUT.PUT_LINE('(to be hired)');
        END IF;
      END LOOP;
    END IF;
 
    DBMS_OUTPUT.PUT_LINE('---'); 
  END;
  
BEGIN 
  print_team('Team Status:');
 
  team := team_type();  -- Team is funded, but nobody is on it.
  print_team('Team Status:');
 
  team := team_type('Arun', 'Amitha', 'Allan', 'Mae');  -- Add members.
  print_team('Initial Team:');
 
  team.DELETE(2,3);  -- Remove 2nd and 3rd members.
  print_team('Current Team:');
END;
/
```

Result:

```
Team Status:
Does not exist
---
Team Status:
Has no members
---
Initial Team:
1. Arun
2. Amitha
3. Allan
4. Mae
---
Current Team:
1. Arun
2. (to be hired)
3. (to be hired)
4. Mae
---
```

### COUNT Collection Method

`COUNT` is a function that returns the number of elements in the collection (ignoring deleted elements, even if `DELETE` kept placeholders for them).

Topics

- COUNT Method for Varray
- COUNT Method for Nested Table

#### COUNT Method for Varray

For a varray, `COUNT` always equals `LAST`. If you increase or decrease the size of a varray (with the `EXTEND` or `TRIM` method), the value of `COUNT` changes.

Example 5-28 COUNT and LAST Values for Varray

This example shows the values of `COUNT` and `LAST` for a varray after initialization with four elements, after `EXTEND(3)`, and after `TRIM(5)`.

```
DECLARE
  TYPE NumList IS VARRAY(10) OF INTEGER;
  n NumList := NumList(1,3,5,7);
 
  PROCEDURE print_count_and_last IS
  BEGIN
    DBMS_OUTPUT.PUT('n.COUNT = ' || n.COUNT || ', ');
    DBMS_OUTPUT.PUT_LINE('n.LAST = ' || n.LAST);
  END  print_count_and_last;
 
BEGIN
  print_count_and_last;
 
  n.EXTEND(3);
  print_count_and_last;
 
  n.TRIM(5);
  print_count_and_last;
END;
/
```

Result:

```
n.COUNT = 4, n.LAST = 4
n.COUNT = 7, n.LAST = 7
n.COUNT = 2, n.LAST = 2
```

#### COUNT Method for Nested Table

For a nested table, `COUNT` equals `LAST` unless you delete elements from the middle of the nested table, in which case `COUNT` is smaller than `LAST`.

Example 5-29 COUNT and LAST Values for Nested Table

This example shows the values of `COUNT` and `LAST` for a nested table after initialization with four elements, after deleting the third element, and after adding two null elements to the end. Finally, the example prints the status of elements 1 through 8.

```
DECLARE
  TYPE NumList IS TABLE OF INTEGER;
  n NumList := NumList(1,3,5,7);
 
  PROCEDURE print_count_and_last IS
  BEGIN
    DBMS_OUTPUT.PUT('n.COUNT = ' || n.COUNT || ', ');
    DBMS_OUTPUT.PUT_LINE('n.LAST = ' || n.LAST);
  END  print_count_and_last;
 
BEGIN
  print_count_and_last;
 
  n.DELETE(3);  -- Delete third element
  print_count_and_last;
 
  n.EXTEND(2);  -- Add two null elements to end
  print_count_and_last;
 
  FOR i IN 1..8 LOOP
    IF n.EXISTS(i) THEN
      IF n(i) IS NOT NULL THEN
        DBMS_OUTPUT.PUT_LINE('n(' || i || ') = ' || n(i));
      ELSE
        DBMS_OUTPUT.PUT_LINE('n(' || i || ') = NULL');
      END IF;
    ELSE
      DBMS_OUTPUT.PUT_LINE('n(' || i || ') does not exist');
    END IF;
  END LOOP;
END;
/
```

Result:

```
n.COUNT = 4, n.LAST = 4
n.COUNT = 3, n.LAST = 4
n.COUNT = 5, n.LAST = 6
n(1) = 1
n(2) = 3
n(3) does not exist
n(4) = 7
n(5) = NULL
n(6) = NULL
n(7) does not exist
n(8) does not exist
```

### LIMIT Collection Method

`LIMIT` is a function that returns the maximum number of elements that the collection can have. If the collection has no maximum number of elements, `LIMIT` returns `NULL`. Only a varray has a maximum size.

Example 5-30 LIMIT and COUNT Values for Different Collection Types

This example prints the values of `LIMIT` and `COUNT` for an associative array with four elements, a varray with two elements, and a nested table with three elements.

```
DECLARE
  TYPE aa_type IS TABLE OF INTEGER INDEX BY PLS_INTEGER;
  aa aa_type;                          -- associative array
 
  TYPE va_type IS VARRAY(4) OF INTEGER;
  va  va_type := va_type(2,4);   -- varray
 
  TYPE nt_type IS TABLE OF INTEGER;
  nt  nt_type := nt_type(1,3,5);  -- nested table
 
BEGIN
  aa(1):=3; aa(2):=6; aa(3):=9; aa(4):= 12;
 
  DBMS_OUTPUT.PUT('aa.COUNT = ');
  DBMS_OUTPUT.PUT_LINE(NVL(TO_CHAR(aa.COUNT), 'NULL'));
 
  DBMS_OUTPUT.PUT('aa.LIMIT = ');
  DBMS_OUTPUT.PUT_LINE(NVL(TO_CHAR(aa.LIMIT), 'NULL'));
 
  DBMS_OUTPUT.PUT('va.COUNT = ');
  DBMS_OUTPUT.PUT_LINE(NVL(TO_CHAR(va.COUNT), 'NULL'));
 
  DBMS_OUTPUT.PUT('va.LIMIT = ');
  DBMS_OUTPUT.PUT_LINE(NVL(TO_CHAR(va.LIMIT), 'NULL'));
 
  DBMS_OUTPUT.PUT('nt.COUNT = ');
  DBMS_OUTPUT.PUT_LINE(NVL(TO_CHAR(nt.COUNT), 'NULL'));
 
  DBMS_OUTPUT.PUT('nt.LIMIT = ');
  DBMS_OUTPUT.PUT_LINE(NVL(TO_CHAR(nt.LIMIT), 'NULL'));
END;
/
```

Result:

```
aa.COUNT = 4
aa.LIMIT = NULL
va.COUNT = 2
va.LIMIT = 4
nt.COUNT = 3
nt.LIMIT = NULL
```

### PRIOR and NEXT Collection Methods

`PRIOR` and `NEXT` are functions that let you move backward and forward in the collection (ignoring deleted elements, even if `DELETE` kept placeholders for them). These methods are useful for traversing sparse collections.

Given an index:

- `PRIOR` returns the index of the preceding existing element of the collection, if one exists. Otherwise, `PRIOR` returns `NULL`.
	For any collection `c`, `c.PRIOR(c.FIRST)` returns `NULL`.
- `NEXT` returns the index of the succeeding existing element of the collection, if one exists. Otherwise, `NEXT` returns `NULL`.
	For any collection `c`, `c.NEXT(c.LAST)` returns `NULL`.

The given index need not exist. However, if the collection `c` is a varray, and the index exceeds `c.LIMIT`, then:

- `c.PRIOR(``index``)` returns `c.LAST`.
- `c.NEXT(``index``)` returns `NULL`.

For example:

```
DECLARE
  TYPE Arr_Type IS VARRAY(10) OF NUMBER;
  v_Numbers Arr_Type := Arr_Type();
BEGIN
  v_Numbers.EXTEND(4);
 
  v_Numbers (1) := 10;
  v_Numbers (2) := 20;
  v_Numbers (3) := 30;
  v_Numbers (4) := 40;
 
  DBMS_OUTPUT.PUT_LINE(NVL(v_Numbers.prior (3400), -1));
  DBMS_OUTPUT.PUT_LINE(NVL(v_Numbers.next (3400), -1));
END;
/
```

Result:

```
4
-1
```

For an associative array indexed by string, the prior and next indexes are determined by key values, which are in sorted order (for more information, see " [NLS Parameter Values Affect Associative Arrays Indexed by String](associative-arrays.md) "). [Example 5-1](associative-arrays.md) uses `FIRST`, `NEXT`, and a `WHILE` `LOOP` statement to print the elements of an associative array.

Example 5-31 PRIOR and NEXT Methods

This example initializes a nested table with six elements, deletes the fourth element, and then shows the values of `PRIOR` and `NEXT` for elements 1 through 7. Elements 4 and 7 do not exist. Element 2 exists, despite its null value.

```
DECLARE
  TYPE nt_type IS TABLE OF NUMBER;
  nt nt_type := nt_type(18, NULL, 36, 45, 54, 63);
 
BEGIN
  nt.DELETE(4);
  DBMS_OUTPUT.PUT_LINE('nt(4) was deleted.');
 
  FOR i IN 1..7 LOOP
    DBMS_OUTPUT.PUT('nt.PRIOR(' || i || ') = ');
    DBMS_OUTPUT.PUT_LINE(NVL(TO_CHAR(nt.PRIOR(i)), 'NULL'));

    DBMS_OUTPUT.PUT('nt.NEXT(' || i || ')  = ');
    DBMS_OUTPUT.PUT_LINE(NVL(TO_CHAR(nt.NEXT(i)), 'NULL'));
  END LOOP;
END;
/
```

Result:

```
nt(4) was deleted.
nt.PRIOR(1) = NULL
nt.NEXT(1)  = 2
nt.PRIOR(2) = 1
nt.NEXT(2)  = 3
nt.PRIOR(3) = 2
nt.NEXT(3)  = 5
nt.PRIOR(4) = 3
nt.NEXT(4)  = 5
nt.PRIOR(5) = 3
nt.NEXT(5)  = 6
nt.PRIOR(6) = 5
nt.NEXT(6)  = NULL
nt.PRIOR(7) = 6
nt.NEXT(7)  = NULL
```

Example 5-32 Printing Elements of Sparse Nested Table

This example prints the elements of a sparse nested table from first to last, using `FIRST` and `NEXT`, and from last to first, using `LAST` and `PRIOR`.

```
DECLARE
  TYPE NumList IS TABLE OF NUMBER;
  n NumList := NumList(1, 2, NULL, NULL, 5, NULL, 7, 8, 9, NULL);
  idx INTEGER;
 
BEGIN
  DBMS_OUTPUT.PUT_LINE('First to last:');
  idx := n.FIRST;
  WHILE idx IS NOT NULL LOOP
    DBMS_OUTPUT.PUT('n(' || idx || ') = ');
    DBMS_OUTPUT.PUT_LINE(NVL(TO_CHAR(n(idx)), 'NULL'));
    idx := n.NEXT(idx);
  END LOOP;
    
  DBMS_OUTPUT.PUT_LINE('--------------');
 
  DBMS_OUTPUT.PUT_LINE('Last to first:');
  idx := n.LAST;
  WHILE idx IS NOT NULL LOOP
    DBMS_OUTPUT.PUT('n(' || idx || ') = ');
    DBMS_OUTPUT.PUT_LINE(NVL(TO_CHAR(n(idx)), 'NULL'));
    idx := n.PRIOR(idx);
  END LOOP;
END;
/
```

Result:

```
First to last:
n(1) = 1
n(2) = 2
n(3) = NULL
n(4) = NULL
n(5) = 5
n(6) = NULL
n(7) = 7
n(8) = 8
n(9) = 9
n(10) = NULL
--------------
Last to first:
n(10) = NULL
n(9) = 9
n(8) = 8
n(7) = 7
n(6) = NULL
n(5) = 5
n(4) = NULL
n(3) = NULL
n(2) = 2
n(1) = 1
```