---
title: Defining Object Types
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/obj_types.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 3 Defining Object Types

This chapter provides an example of starting with a schema for a data cartridge. Object types are crucial to building data cartridges in that they enable domain-level abstractions to be captured in the database.

This chapter contains these topics:

- Objects and Object Types
- Assigning an Object Identifier to an Object Type
- Constructor Methods
- Object Comparison
	See Also:
	The following manuals for additional information about creating and using object types:
	- [Oracle Database Object-Relational Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11822/toc.htm)
	- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm)
	- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm)
	- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm)

## Objects and Object Types

In the Oracle Object-Relational Database Management System (ORDBMS), you use object types to model real-world entities. An object type has attributes, which reflect the entity's structure, and methods, which implement the operations on the entity. Attributes are defined using built-in types or other object types. Methods are functions or procedures written in PL/SQL or an external language, like C, and stored in the database.

A typical use for an object type is to impose structure on some part of the data in the database. For example, an object type named `DataStream` could be used by a cartridge to store large amounts of data in a character LOB (a data type for large objects). This object type has attributes such as an identifier, a name, a date, and so on. The statement in Example 3-1 defines the `DataStream` data type:

Example 3-1 Defining a DataStream data type

```
create or replace type DataStream as object (
   id integer, 
   name varchar2(20),
   createdOn date,
   data clob, 
   MEMBER FUNCTION DataStreamMin  return pls_integer,
   MEMBER FUNCTION DataStreamMax  return pls_integer,
   MAP MEMBER FUNCTION DataStreamToInt  return integer,
   PRAGMA restrict_references(DataStreamMin, WNDS, WNPS),
   PRAGMA restrict_references(DataStreamMax, WNDS, WNPS));
```

A method is a procedure or function that is part of the object type definition and that can operate on the object type data attributes. Such methods are called member methods, and they take the keyword `MEMBER` when you specify them as a component of the object type. The `DataStream` type definition declares three methods. The first two, `DataStreamMin` and `DataStreamMax`, calculate the minimum and maximum values, respectively, in the data stream stored inside the character `LOB`.

The third method, `DataStreamToInt`, a map method, governs comparisons between instances of data stream type.

See Also:

"Object Comparison" for information about map methods

The pragma (compiler directive) `RESTRICT_REFERENCES` is necessary for security, and is discussed in the following sections.

After declaring the type, define the type body. The body contains the code for type methods. Example 3-2 shows the type body definition for the `DataStream` type. It defines the member function methods, `DataStreamMin` and `DataStreamMax`, and the map method `DataStreamToInt`.

Example 3-2 Defining the Type Body

```
CREATE OR REPLACE TYPE BODY DataStream IS
    MEMBER FUNCTION DataStreamMin return pls_integer is 
      a pls_integer := DS_Package.ds_findmin(data); 
      begin return a; end; 
    MEMBER FUNCTION DataStreamMax return pls_integer is 
      b pls_integer := DS_Package.ds_findmax(data); 
      begin return b; end; 
    MAP MEMBER FUNCTION DataStreamToInt return integer is 
      c integer := id; 
      begin return c; end; 
end;
```

`DataStreamMin` and `DataStreamMax` are call routines in a PL/SQL package named `DS_Package`. Since these methods are likely to be compute-intensive (they process numbers stored in the `CLOB` to determine minimum and maximum values), they are defined as external procedures and implemented in C. The external dispatch is routed through a PL/SQL package named `DS_Package`. Such packages are discussed in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm).

The third method, `DataStreamToInt`, is implemented in PL/SQL. Because we have a identifier, `id`, attribute in `DataStream`, this method can return the value of the identifier attribute. Most map methods, however, are more complex than `DataStreamToInt`.

See Also:

- [Chapter 6, "Working with Multimedia Data Types"](lobs.md)
- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/toc.htm) for general information about LOBs

## Assigning an Object Identifier to an Object Type

The `CREATE` `TYPE` statement has an optional keyword `OID`, which associates a user-specified object identifier (`OID`) with the type definition. It necessary to anyone who creates an object type used in several database.s

Each type has an `OID`. If you create an object type and do not specify an `OID`, Oracle generates an `OID` and assigns it to the type. Oracle uses the `OID` internally for operations pertaining to that type. Using the same `OID` for a type is important if you plan to share instances of the type across databases for such operations as export/import and distributed queries.

Note:

In `CREATE` `TYPE` with `OID`, an `OID` is assigned to the type itself. Each row in a table with a column of the specified type has a row-specific `OID`.

Consider creating a `SpecialPerson` type, and then instantiating this type in two different databases in tables named `SpecialPersonTable1` and `SpecialPersonTable2`. The RDBMS must know that the `SpecialPerson` type is the same type in both instances, and therefore the type must be defined using the same `OID` in both databases. If you do not specify an `OID` with `CREATE` `TYPE`, a unique identifier is created automatically by the RDBMS. The syntax for specifying an `OID` for an object type is in Example 3-3.

Example 3-3 Specifying an ODI for an Object Type

```
CREATE OR REPLACE TYPE type_name OID 'oid' AS OBJECT (attribute datatype [,...]);
```

In Example 3-4, the `SELECT` statement generates an `OID`, and the `CREATE` `TYPE` statement uses the `OID` in creating an object type named `mytype`. Be sure to use the `SELECT` statement to generate a different `OID` for each object type to be created, because this is the only way to guarantee that each `OID` is valid and globally unique.

Example 3-4 Assigning and Using OIDs

```
SQLPLUS> SELECT SYS_OP_GUID() FROM DUAL; 
SYS_OP_GUID()                    
-------------------------------- 
19A57209ECB73F91E03400400B40BBE3 
1 row selected. 
 
SQLPLUS> CREATE TYPE mytype OID '19A57209ECB73F91E03400400B40BBE3'
     2> AS OBJECT (attrib1 NUMBER); 
Statement processed.
```

## Constructor Methods

Oracle implicitly defines a constructor method for each object type that you define. The name of the constructor method is identical to the name of the object type. The parameters of the constructor method are exactly the data attributes of the object type, and they occur in the same order as the attribute definition for the object type. Only one constructor method can be defined for each object type.

In Example 3-5, the system creates a type named `rational_type` and implicitly creates a constructor method for this object type.

Example 3-5 Creating a Type

```
CREATE TYPE rational_type (
     numerator integer,
     denominator integer);
```

When you instantiate an object of `rational_type`, you invoke the constructor method, as demonstrated in Example 3-6:

Example 3-6 Instantiating a Type Object

```
CREATE TABLE some_table (
     c1 integer, c2 rational_type);
INSERT INTO some_table
     VALUES (42, rational_type(223, 71));
```

## Object Comparison

SQL performs comparison operations on objects. Some comparisons are explicit, using the comparison operators (=, <, >, <>, <=, >=,!=) and the `BETWEEN` and `IN` predicates. Other comparisons are implicit, as in the `GROUP` `BY`, `ORDER` `BY`, `DISTINCT`, and `UNIQUE` clauses.

Comparison of objects uses special member functions of the object type: map methods and order methods. To perform object comparison, you must implement either a map method or an order method in the `CREATE` `TYPE` and `CREATE` `TYPE` `BODY` statements. In Example 3-7, the type body for the `DataStream` type implements the map member function:

Example 3-7 Implementing a Member Function

```
MAP MEMBER FUNCTION DataStreamToInt return integer is 
      c integer := id; 
      begin return c; end;
```

This definition of the map member function relies on the presence of the `id` attribute of the `DataStream` type to map instances to integers. Whenever a comparison operation is required between objects of type `DataStream`, the map function `DataStreamToInt()` is called implicitly by the system.

The object type `rational_type` does not have a simple `id` attribute like `DataStream`. Instead, its map member function is complicated, as demonstrated in Example 3-8. Because a map function can return any of the built-in types, `rational_type` can return a value or type `REAL`.

Example 3-8 Implementing Functions for Types Without a Simple Id Attributte

```
MAP MEMBER FUNCTION RationalToReal RETURN REAL IS
     BEGIN
         RETURN numerator/denominator;
     END;
...
```

If you have not defined a map or order function for an object type, it can only support equality comparisons. Oracle SQL performs the comparison by doing a field-by-field comparison of the attributes of that type.