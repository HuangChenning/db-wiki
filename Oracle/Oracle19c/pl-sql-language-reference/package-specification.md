---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/package-specification.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Package Specification

A package specification declares public items. The scope of a public item is the schema of the package. A public item is visible everywhere in the schema. To reference a public item that is in scope but not visible, qualify it with the package name. (For information about scope, visibility, and qualification, see " [Scope and Visibility of Identifiers](scope-and-visibility-identifiers.md) ".)

Each public item declaration has all information needed to use the item. For example, suppose that a package specification declares the function `factorial` this way:

```
FUNCTION factorial (n INTEGER) RETURN INTEGER; -- returns n!
```

The declaration shows that `factorial` needs one argument of type `INTEGER` and returns a value of type `INTEGER`, which is invokers must know to invoke `factorial`. Invokers need not know how `factorial` is implemented (for example, whether it is iterative or recursive).

Note:

To restrict the use of your package to specified PL/SQL units, include the `ACCESSIBLE` `BY` clause in the package specification.

Topics

- Appropriate Public Items
- Creating Package Specifications

### Appropriate Public Items

Appropriate public items are:

- Types, variables, constants, subprograms, cursors, and exceptions used by multiple subprograms
	A type defined in a package specification is either a PL/SQL user-defined subtype (described in " [User-Defined PL/SQL Subtypes](user-defined-pl-sql-subtypes.md) ") or a PL/SQL composite type (described in [PL/SQL Collections and Records](plsql-collections-and-records.md)).
	Note:
	A PL/SQL composite type defined in a package specification is incompatible with an identically defined local or standalone type (see [Example 5-33](collection-types-defined-package-specifications.md), [Example 5-34](collection-types-defined-package-specifications.md), and [Example 5-39](record-variables.md)).
- Associative array types of standalone subprogram parameters
	You cannot declare an associative array type at schema level. Therefore, to pass an associative array variable as a parameter to a standalone subprogram, you must declare the type of that variable in a package specification. Doing so makes the type available to both the invoked subprogram (which declares a formal parameter of that type) and to the invoking subprogram or anonymous block (which declares a variable of that type). See Example 10-2.
- Variables that must remain available between subprogram invocations in the same session
- Subprograms that read and write public variables ("get" and "set" subprograms)
	Provide these subprograms to discourage package users from reading and writing public variables directly.
- Subprograms that invoke each other
	You need not worry about compilation order for package subprograms, as you must for standalone subprograms that invoke each other.
- Overloaded subprograms
	Overloaded subprograms are variations of the same subprogram. That is, they have the same name but different formal parameters. For more information about them, see " [Overloaded Subprograms](overloaded-subprograms.md) ".

Note:

You cannot reference remote package public variables, even indirectly. For example, if a subprogram refers to a package public variable, you cannot invoke the subprogram through a database link.

### Creating Package Specifications

To create a package specification, use the " [CREATE PACKAGE Statement](CREATE-PACKAGE-statement.md) ".

Because the package specifications in Example 10-1 and Example 10-2 do not declare cursors or subprograms, the packages `trans_data` and `aa_pkg` do not need bodies.

Example 10-1 Simple Package Specification

In this example, the specification for the package `trans_data` declares two public types and three public variables.

```
CREATE OR REPLACE PACKAGE trans_data AUTHID DEFINER AS
  TYPE TimeRec IS RECORD (
    minutes SMALLINT,
    hours   SMALLINT);
  TYPE TransRec IS RECORD (
    category VARCHAR2(10),
    account  INT,
    amount   REAL,
    time_of  TimeRec);
  minimum_balance     CONSTANT REAL := 10.00;
  number_processed    INT;
  insufficient_funds  EXCEPTION;
  PRAGMA EXCEPTION_INIT(insufficient_funds, -4097);
END trans_data;
/
```

Example 10-2 Passing Associative Array to Standalone Subprogram

In this example, the specification for the package `aa_pkg` declares an associative array type, `aa_type`. Then, the standalone procedure `print_aa` declares a formal parameter of type `aa_type`. Next, the anonymous block declares a variable of type `aa_type`, populates it, and passes it to the procedure `print_aa`, which prints it.

```
CREATE OR REPLACE PACKAGE aa_pkg AUTHID DEFINER IS
  TYPE aa_type IS TABLE OF INTEGER INDEX BY VARCHAR2(15);
END;
/
CREATE OR REPLACE PROCEDURE print_aa (
  aa aa_pkg.aa_type
) AUTHID DEFINER IS
  i  VARCHAR2(15);
BEGIN
  i := aa.FIRST;
 
  WHILE i IS NOT NULL LOOP
    DBMS_OUTPUT.PUT_LINE (aa(i) || '  ' || i);
    i := aa.NEXT(i);
  END LOOP;
END;
/
DECLARE
  aa_var  aa_pkg.aa_type;
BEGIN
  aa_var('zero') := 0;
  aa_var('one') := 1;
  aa_var('two') := 2;
  print_aa(aa_var);
END;
/
```

Result:

```
1  one
2  two
0  zero
```