---
title: Record Variable Declaration
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/record_definition.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

A record variable is a composite variable whose internal components, called fields, can have different data types. The value of a record variable and the values of its fields can change.

You reference an entire record variable by its name. You reference a record field with the syntax `record.field`.

You can create a record variable in any of these ways:

- Define a record type and then declare a variable of that type.
- Use `%ROWTYPE` to declare a record variable that represents either a full or partial row of a database table or view.
- Use `%TYPE` to declare a record variable of the same type as a previously declared record variable.

Topics

- Syntax
- Semantics
- Examples
- Related Topics

See ["rowtype\_attribute::="](rowtype_attribute.md).

Semantics

record\_type\_definition

record\_type

Name of the record type that you are defining.

field\_definition

field

Name of the field that you are defining.

datatype

Data type of the field that you are defining.

NOT NULL

Imposes the `NOT` `NULL` constraint on the field that you are defining. For information about this constraint, see ["NOT NULL Constraint"](fundamentals.md).

expression

Expression whose data type is compatible with `datatype`. When `record_variable_declaration` is elaborated, the value of `expression` is assigned to `record`.`field`. This value is the initial value of the field.

record\_variable\_declaration

record\_1

Name of the record variable that you are declaring.

record\_type

Name of a previously defined record type. `record_type` is the data type of `record_1`.

rowtype\_attribute

See ["%ROWTYPE Attribute"](rowtype_attribute.md).

record\_2

Name of a previously declared record variable.

%TYPE

See ["%TYPE Attribute"](type_attribute.md).