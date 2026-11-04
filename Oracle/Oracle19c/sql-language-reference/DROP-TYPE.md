---
title: DROP TYPE
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/DROP-TYPE.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Purpose

Object types are defined using PL/SQL. Refer to [*Oracle Database PL/SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=LNPLS99989) for complete information on creating, altering, and dropping object types.

Use the `DROP` `TYPE` statement to drop the specification and body of an object type, a varray, or a nested table type.

## Prerequisites

The object type, varray, or nested table type must be in your own schema or you must have the `DROP` `ANY` `TYPE` system privilege.

## Syntax

## drop\_type::=

[Description of the illustration drop\_type.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/drop_type.html)

## Semantics

## IF EXISTS

Specify `IF EXISTS` to drop an existing type.

## schema

Specify the schema containing the type. If you omit *schema*, then Oracle Database assumes the type is in your own schema.

## type\_name

Specify the name of the object, varray, or nested table type to be dropped. You can drop only types with no type or table dependencies.

If *type\_name* is a supertype, then this statement will fail unless you also specify `FORCE`. If you specify `FORCE`, then the database invalidates all subtypes depending on this supertype.

If *type\_name* is a statistics type, then this statement will fail unless you also specify `FORCE`. If you specify `FORCE`, then the database first disassociates all objects that are associated with *type\_name* and then drops *type\_name*.

**See Also:** [ASSOCIATE STATISTICS](ASSOCIATE-STATISTICS.md) and [DISASSOCIATE STATISTICS](DISASSOCIATE-STATISTICS.md) for more information on statistics types

If *type\_name* is an object type that has been associated with a statistics type, then the database first attempts to disassociate *type\_name* from the statistics type and then drops *type\_name*. However, if statistics have been collected using the statistics type, then the database will be unable to disassociate *type\_name* from the statistics type, and this statement will fail.

If *type\_name* is an implementation type for an indextype, then the indextype will be marked `INVALID`.

If *type\_name* has a public synonym defined on it, then the database will also drop the synonym.

Unless you specify `FORCE`, you can drop only object types, nested tables, or varray types that are standalone schema objects with no dependencies. This is the default behavior.

**See Also:** [CREATE INDEXTYPE](CREATE-INDEXTYPE.md)

## FORCE

Specify `FORCE` to drop the type even if it has dependent database objects. Oracle Database marks `UNUSED` all columns dependent on the type to be dropped, and those columns become inaccessible. **Note:** Oracle does not recommend that you specify `FORCE` to drop object types with dependencies. This operation is not recoverable and could cause the data in the dependent tables or columns to become inaccessible.

## VALIDATE

If you specify `VALIDATE` when dropping a type, then Oracle Database checks for stored instances of this type within substitutable columns of any of its supertypes. If no such instances are found, then the database completes the drop operation.

This clause is meaningful only for subtypes. Oracle recommends the use of this option to safely drop subtypes that do not have any explicit type or table dependencies.

## Examples

**Dropping an Object Type: Example**

The following statement removes object type `person_t`. See [*Oracle Database PL/SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=LNPLS01383) for the example that creates this object type. Any columns that are dependent on person\_t are marked `UNUSED` and become inaccessible.

```md
DROP TYPE person_t FORCE;
```