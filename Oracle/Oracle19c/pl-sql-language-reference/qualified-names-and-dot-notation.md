---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/qualified-names-and-dot-notation.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Qualified Names and Dot Notation

When one named item belongs to another named item, you can (and sometimes must) qualify the name of the "child" item with the name of the "parent" item, using dot notation. For example:

| When referencing... | You must qualify its name with... | Using this syntax... |
| --- | --- | --- |
| Field of a record | Name of the record | `record_name.field_name` |
| Method of a collection | Name of the collection | `collection_name.method` |
| Pseudocolumn `CURRVAL` | Name of a sequence | `sequence_name``.CURRVAL` |
| Pseudocolumn `NEXTVAL` | Name of a sequence | `sequence_name``.NEXTVAL` |

If an identifier is declared in a named PL/SQL unit, you can qualify its simple name (the name in its declaration) with the name of the unit (block, subprogram, or package), using this syntax:

```
unit_name.simple_identifier_name
```

If the identifier is not visible, then you must qualify its name (see " [Scope and Visibility of Identifiers](scope-and-visibility-identifiers.md) ").

If an identifier belongs to another schema, then you must qualify its name with the name of the schema, using this syntax:

```
schema_name.package_name
```

A simple name can be qualified with multiple names, as Example B-1 shows.

Some examples of possibly ambiguous qualified names are:

- Field or attribute of a function return value, for example:
	```
	func_name().field_name
	func_name().attribute_name
	```
- Schema object owned by another schema, for example:
	```
	schema_name.table_name
	schema_name.procedure_name()
	schema_name.type_name.member_name()
	```
- Package object owned by another user, for example:
	```
	schema_name.package_name.procedure_name()
	schema_name.package_name.record_name.field_name
	```
- Record containing an ADT, for example:
	```
	record_name.field_name.attribute_name
	record_name.field_name.member_name()
	```

Example B-1 Qualified Names

```
CREATE OR REPLACE PACKAGE pkg1 AUTHID DEFINER AS
  m NUMBER;
  TYPE t1 IS RECORD (a NUMBER);
  v1 t1;
  TYPE t2 IS TABLE OF t1 INDEX BY PLS_INTEGER;
  v2 t2; 
  FUNCTION f1 (p1 NUMBER) RETURN t1;
  FUNCTION f2 (q1 NUMBER) RETURN t2;
END pkg1;
/

CREATE OR REPLACE PACKAGE BODY pkg1 AS
  FUNCTION f1 (p1 NUMBER) RETURN t1 IS
    n NUMBER;
  BEGIN
     n := m;             -- Unqualified variable name
     n := pkg1.m;        -- Variable name qualified by package name
     n := pkg1.f1.p1;    -- Parameter name qualified by function name,
                         --  which is qualified by package name
     n := v1.a;          -- Variable name followed by component name
     n := pkg1.v1.a;     -- Variable name qualified by package name
                         --  and followed by component name
     n := v2(10).a;      -- Indexed name followed by component name
     n := f1(10).a;      -- Function invocation followed by component name
     n := f2(10)(10).a;  -- Function invocation followed by indexed name
                         --  and followed by component name
     n := hr.pkg1.f2(10)(10).a;  -- Schema name, package name,
                                 -- function invocation, index, component name
     v1.a := p1;
     RETURN v1;
   END f1;

   FUNCTION f2 (q1 NUMBER) RETURN t2 IS
     v_t1 t1;
     v_t2 t2;
   BEGIN
     v_t1.a := q1;
     v_t2(1) := v_t1;
     RETURN v_t2;
   END f2;
END pkg1;
/
```