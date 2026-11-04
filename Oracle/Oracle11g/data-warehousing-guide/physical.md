---
title: Physical Design in Data Warehouses
book: Data Warehousing Guide
doc_id: E25554-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25554/physical.htm
tags:
  - oracle
  - 11g
  - data-warehousing-guide
---

## 3 Physical Design in Data Warehouses

This chapter describes the physical design of a data warehousing environment, and includes the following topics:

- Moving from Logical to Physical Design
- Physical Design

## Moving from Logical to Physical Design

Logical design is what you draw with a pen and paper or design with Oracle Warehouse Builder or Oracle Designer before building your data warehouse. Physical design is the creation of the database with SQL statements.

During the physical design process, you convert the data gathered during the logical design phase into a description of the physical database structure. Physical design decisions are mainly driven by query performance and database maintenance aspects. For example, choosing a partitioning strategy that meets common query requirements enables Oracle Database to take advantage of partition pruning, a way of narrowing a search before performing it.

See Also:

- [Chapter 5, "Partitioning in Data Warehouses"](parpart.md) for further information regarding partitioning
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for further conceptual material regarding all design matters

## Physical Design

During the logical design phase, you defined a model for your data warehouse consisting of entities, attributes, and relationships. The entities are linked together using relationships. Attributes are used to describe the entities. The [unique identifier](glossary.md) (UID) distinguishes between one instance of an entity and another.

Figure 3-1 illustrates a graphical way of distinguishing between logical and physical designs.

Figure 3-1 Logical Design Compared with Physical Design

![Description of Figure 3-1 follows](https://docs.oracle.com/cd/E11882_01/server.112/e25554/dwhsg006.gif)  
[Description of "Figure 3-1 Logical Design Compared with Physical Design"](https://docs.oracle.com/cd/E11882_01/server.112/e25554/img_text/dwhsg006.htm)  

During the physical design process, you translate the expected schemas into actual database structures. At this time, you must map:

- Entities to tables
- Relationships to foreign key constraints
- Attributes to columns
- Primary unique identifiers to primary key constraints
- Unique identifiers to unique key constraints

### Physical Design Structures

Once you have converted your logical design to a physical one, you must create some or all of the following structures:

Some of these structures require disk space. Others exist only in the data dictionary. Additionally, the following structures may be created for performance improvement:

- Indexes and Partitioned Indexes
- Materialized Views

### Tablespaces

A tablespace consists of one or more datafiles, which are physical structures within the operating system you are using. A datafile is associated with only one tablespace. From a design perspective, tablespaces are containers for physical design structures.

Tablespaces need to be separated by differences. For example, tables should be separated from their indexes and small tables should be separated from large tables. Tablespaces should also represent logical business units if possible. Because a tablespace is the coarsest granularity for backup and recovery or the transportable tablespaces mechanism, the logical business design affects availability and maintenance operations.

You can now use ultralarge data files, a significant improvement in very large databases.

See Also:

[Chapter 4, "Hardware and I/O Considerations in Data Warehouses"](hardware.md) for information regarding tablespaces

### Tables and Partitioned Tables

Tables are the basic unit of data storage. They are the container for the expected amount of raw data in your data warehouse.

Using partitioned tables instead of nonpartitioned ones addresses the key problem of supporting very large data volumes by allowing you to divide them into smaller and more manageable pieces. The main design criterion for partitioning is manageability, though you also see performance benefits in most cases because of partition pruning or intelligent parallel processing. For example, you might choose a partitioning strategy based on a sales transaction date and a monthly granularity. If you have four years' worth of data, you can delete a month's data as it becomes older than four years with a single, fast DDL statement and load new data while only affecting 1/48th of the complete table. Business questions regarding the last quarter only affect three months, which is equivalent to three partitions, or 3/48ths of the total volume.

Partitioning large tables improves performance because each partitioned piece is more manageable. Typically, you partition based on transaction dates in a data warehouse. For example, each month, one month's worth of data can be assigned its own partition.

#### Table Compression

You can save disk space, increase memory efficiency, and improve query performance by compressing heap-organized tables. This often leads to better scalability and query performance. You can enable compression at the tablespace, table, or partition level. A typical type of heap-organized table you should consider for table compression is partitioned tables. Although compressed tables or partitions are updatable, there is some overhead in updating these tables, and high update activity may work against compression by causing some space to be wasted.

OLTP table compression is best suited for tables with significant update activity. Hybrid Columnar Compression, a feature of certain Oracle storage systems, utilizes a combination of both row and columnar methods for storing data. When data is loaded, groups of rows are stored in columnar format, with the values for a given column stored and compressed together. Storing column data together, with the same data type and similar characteristics, drastically increases the storage savings achieved from compression. Hybrid Columnar Compression provides multiple levels of compression and is best suited for tables or partitions with minimal update activity.

### Views

A view is a tailored presentation of the data contained in one or more tables or other views. A view takes the output of a query and treats it as a table. Views do not require any space in the database.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm)

### Integrity Constraints

Integrity constraints are used to enforce business rules associated with your database and to prevent having invalid information in the tables. Integrity constraints in data warehousing differ from constraints in OLTP environments. In OLTP environments, they primarily prevent the insertion of invalid data into a record, which is not a big problem in data warehousing environments because accuracy has already been guaranteed. In data warehousing environments, constraints are only used for query rewrite. `NOT` `NULL` constraints are particularly common in data warehouses. Under some specific circumstances, constraints need space in the database. These constraints are in the form of the underlying unique index.

See Also:

[Chapter 8, "Integrity Constraints"](constra.md)

### Indexes and Partitioned Indexes

Indexes are optional structures associated with tables or clusters. In addition to the classical B-tree indexes, bitmap indexes are very common in data warehousing environments. Bitmap indexes are optimized index structures for set-oriented operations. Additionally, they are necessary for some optimized data access methods such as star transformations.

Indexes are just like tables in that you can partition them, although the partitioning strategy is not dependent upon the table structure. Partitioning indexes makes it easier to manage the data warehouse during refresh and improves query performance.

See Also:

[Chapter 7, "Indexes"](indexes.md) and [Chapter 16, "Maintaining the Data Warehouse"](refresh.md)

### Materialized Views

Materialized views are query results that have been stored in advance so long-running calculations are not necessary when you actually execute your SQL statements. From a physical design point of view, materialized views resemble tables or partitioned tables and behave like indexes in that they are used transparently and improve performance.

See Also:

[Chapter 9, "Basic Materialized Views"](basicmv.md)

### Dimensions

A dimension is a schema object that defines hierarchical relationships between columns or column sets. A hierarchical relationship is a functional dependency from one level of a hierarchy to the next one. A dimension is a container of logical relationships and does not require any space in the database. A typical dimension is city, state (or province), region, and country.

See Also:

[Chapter 11, "Dimensions"](dimen.md)