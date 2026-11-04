---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/collection-types.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Collection Types

PL/SQL has three collection types—associative array, `VARRAY` (variable-size array), and nested table.

Table 5-1 summarizes their similarities and differences.

Table 5-1 PL/SQL Collection Types

| Collection Type | Number of Elements | Index Type | Dense or Sparse | Uninitialized Status | Where Defined | Can Be ADT Attribute Data Type |
| --- | --- | --- | --- | --- | --- | --- |
| Associative array (or index-by table) | Unspecified | String or `PLS_INTEGER` | Either | Empty | In PL/SQL block or package | No |
| `VARRAY` (variable-size array) | Specified | Integer | Always dense | Null | In PL/SQL block or package or at schema level | Only if defined at schema level |
| Nested table | Unspecified | Integer | Starts dense, can become sparse | Null | In PL/SQL block or package or at schema level | Only if defined at schema level |

Number of Elements

If the number of elements is specified, it is the maximum number of elements in the collection. If the number of elements is unspecified, the maximum number of elements in the collection is the upper limit of the index type.

Dense or Sparse

A dense collection has no gaps between elements—every element between the first and last element is defined and has a value (the value can be `NULL` unless the element has a `NOT` `NULL` constraint). A sparse collection has gaps between elements.

Uninitialized Status

An empty collection exists but has no elements. To add elements to an empty collection, invoke the `EXTEND` method (described in " [EXTEND Collection Method](collection-methods.md) ").

A null collection (also called an atomically null collection) does not exist. To change a null collection to an existing collection, you must initialize it, either by making it empty or by assigning a non- `NULL` value to it (for details, see " [Collection Constructors](collection-constructors.md) " and " [Assigning Values to Collection Variables](assigning-values-collection-variables.md) "). You cannot use the `EXTEND` method to initialize a null collection.

Where Defined

A collection type defined in a PL/SQL block is a local type. It is available only in the block, and is stored in the database only if the block is in a standalone or package subprogram. (Standalone and package subprograms are explained in " [Nested, Package, and Standalone Subprograms](nested-package-and-standalone-subprograms.md) ".)

A collection type defined in a package specification is a public item. You can reference it from outside the package by qualifying it with the package name (`package_name.type_name`). It is stored in the database until you drop the package. (Packages are explained in [PL/SQL Packages](plsql-packages.md).)

A collection type defined at schema level is a standalone type. You create it with the " [CREATE TYPE Statement](CREATE-TYPE-statement.md) ". It is stored in the database until you drop it with the " [DROP TYPE Statement](DROP-TYPE-statement.md) ".

Note:

A collection type defined in a package specification is incompatible with an identically defined local or standalone collection type (see [Example 5-33](collection-types-defined-package-specifications.md) and [Example 5-34](collection-types-defined-package-specifications.md)).

Can Be ADT Attribute Data Type

To be an ADT attribute data type, a collection type must be a standalone collection type. For other restrictions, see [Restrictions on datatype](CREATE-TYPE-statement.md).

Translating Non-PL/SQL Composite Types to PL/SQL Composite Types

If you have code or business logic that uses another language, you can usually translate the array and set types of that language directly to PL/SQL collection types. For example:

| Non-PL/SQL Composite Type | Equivalent PL/SQL Composite Type |
| --- | --- |
| Hash table | Associative array |
| Unordered table | Associative array |
| Set | Nested table |
| Bag | Nested table |
| Array | `VARRAY` |

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF00613) for information about the `CAST` function, which converts one SQL data type or collection-typed value into another SQL data type or collection-typed value.