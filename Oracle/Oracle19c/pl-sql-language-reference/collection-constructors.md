---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/collection-constructors.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Collection Constructors

A collection constructor (constructor) is a system-defined function with the same name as a collection type, which returns a collection of that type.

Note:

This topic applies only to varrays and nested tables. In this topic, collection means varray or nested table. Associative arrays use qualified expressions and aggregates (see [Qualified Expressions Overview](qualified-expressions-overview.md)).

The syntax of a constructor invocation is:

```
collection_type ( [ value [, value ]... ] )
```

If the parameter list is empty, the constructor returns an empty collection. Otherwise, the constructor returns a collection that contains the specified values. For semantic details, see " [collection\_constructor](expression.md) ".

You can assign the returned collection to a collection variable (of the same type) in the variable declaration and in the executable part of a block.

Example 5-7 Initializing Collection (Varray) Variable to Empty

This example invokes a constructor twice: to initialize the varray variable `team` to empty in its declaration, and to give it new values in the executable part of the block. The procedure `print_team` shows the initial and final values of `team`. To determine when `team` is empty, `print_team` uses the collection method `COUNT`, described in " [Collection Methods](collection-methods.md) ". (For an example of a procedure that prints a varray that might be null, see [Example 5-26](collection-methods.md).)

Live SQL:

You can view and run this example on Oracle Live SQL at [Initializing Collection (Varray) Variable to Empty](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/composites58.html)

```
DECLARE
  TYPE Foursome IS VARRAY(4) OF VARCHAR2(15);
  team Foursome := Foursome();  -- initialize to empty
 
  PROCEDURE print_team (heading VARCHAR2)
  IS
  BEGIN
    DBMS_OUTPUT.PUT_LINE(heading);
 
    IF team.COUNT = 0 THEN
      DBMS_OUTPUT.PUT_LINE('Empty');
    ELSE 
      FOR i IN 1..4 LOOP
        DBMS_OUTPUT.PUT_LINE(i || '.' || team(i));
      END LOOP;
    END IF;
 
    DBMS_OUTPUT.PUT_LINE('---'); 
  END;
 
BEGIN
  print_team('Team:');
  team := Foursome('John', 'Mary', 'Alberto', 'Juanita');
  print_team('Team:');
END;
/
```

Result:

```
Team:
Empty
---
Team:
1.John
2.Mary
3.Alberto
4.Juanita
---
```