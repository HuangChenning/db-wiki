---
title: Database Objects
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/sql_elements007.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Oracle Database recognizes objects that are associated with a particular schema and objects that are not associated with any particular schema, as described in the sections that follow.

## Schema Objects

A schema is a collection of logical structures of data, or schema objects. A schema is owned by a database user and has the same name as that user. Each user owns a single schema. Schema objects can be created and manipulated with SQL and include the following types of objects:

  
Clusters  
Constraints  
Database links  
Database triggers  
Dimensions  
External procedure libraries  
Index-organized tables  
Indexes  
Indextypes  
Java classes, Java resources, Java sources  
Materialized views  
Materialized view logs  
Mining models  
Object tables  
Object types  
Object views  
Operators  
Packages  
Sequences  
Stored functions, stored procedures  
Synonyms  
Tables  
Views

## Nonschema Objects

Other types of objects are also stored in the database and can be created and manipulated with SQL but are not contained in a schema:

  
Contexts  
Directories  
Editions  
Restore points  
Roles  
Rollback segments  
Tablespaces  
Users  

In this reference, each type of object is described in [Chapter 10](statements_1.md) through [Chapter 19](statements_10.md), in the section devoted to the statement that creates the database object. These statements begin with the keyword `CREATE`. For example, for the definition of a cluster, see [CREATE CLUSTER](statements_5001.md).

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT010) for an overview of database objects

You must provide names for most types of database objects when you create them. These names must follow the rules listed in the sections that follow.