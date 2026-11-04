---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-collections-and-records.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## 5 PL/SQL Collections and Records

PL/SQL lets you define two kinds of composite data types: collection and record.

A composite data type stores values that have internal components. You can pass entire composite variables to subprograms as parameters, and you can access internal components of composite variables individually. Internal components can be either scalar or composite. You can use scalar components wherever you can use scalar variables. You can use composite components wherever you can use composite variables of the same type.

Note:

If you pass a composite variable as a parameter to a remote subprogram, then you must create a redundant loop-back `DATABASE` `LINK`, so that when the remote subprogram compiles, the type checker that verifies the source uses the same definition of the user-defined composite variable type as the invoker uses.

In a collection, the internal components always have the same data type, and are called elements. You can access each element of a collection variable by its unique index, with this syntax: `variable_name` `(``index``)`. To create a collection variable, you either define a collection type and then create a variable of that type or use `%TYPE`.

In a record, the internal components can have different data types, and are called fields. You can access each field of a record variable by its name, with this syntax: `variable_name.field_name`. To create a record variable, you either define a `RECORD` type and then create a variable of that type or use `%ROWTYPE` or `%TYPE`.

You can create a collection of records, and a record that contains collections.

Collection Topics

- [Collection Types](collection-types.md)
- [Associative Arrays](associative-arrays.md)
- [Varrays (Variable-Size Arrays)](varrays-variable-size-arrays.md)
- [Nested Tables](nested-tables.md)
- [Collection Constructors](collection-constructors.md)
- [Qualified Expressions Overview](qualified-expressions-overview.md)
- [Assigning Values to Collection Variables](assigning-values-collection-variables.md)
- [Multidimensional Collections](multidimensional-collections.md)
- [Collection Comparisons](collection-comparisons.md)
- [Collection Methods](collection-methods.md)
- [Collection Types Defined in Package Specifications](collection-types-defined-package-specifications.md)

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01205) for information about the `CREATE` `DATABASE` `LINK` statement
- " [Querying a Collection](cursor-variables.md) "
- " [BULK COLLECT Clause](bulk-sql-and-bulk-binding.md) " for information about retrieving query results into a collection
- " [Collection Variable Declaration](collection-variable.md) " for syntax and semantics of collection type definition and collection variable declaration

Record Topics

Note:

The components of an explicitly listed composite data structure (such as a collection constructor or record initializer) can be evaluated in any order. If a program determines order of evaluation, then at the point where the program does so, its behavior is undefined.