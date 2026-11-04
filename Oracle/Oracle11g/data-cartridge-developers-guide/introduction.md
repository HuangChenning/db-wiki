---
title: Introduction to Data Cartridges
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/introduction.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 1 Introduction to Data Cartridges

In addition to the efficient and secure management of data ordered under the relational model, Oracle provides support for data organized under the object model. Object types and other features such as large objects (`LOB` s), external procedures, extensible indexing, and query optimization can be used to build powerful, reusable server-based components called data cartridges.

This chapter contains these topics:

## Overview of Data Cartridges

Data cartridges extend the capabilities of the Oracle server by taking advantage of Oracle Extensibility Architecture framework. This framework lets you capture business logic and processes associated with specialized or domain-specific data in user-defined data types. Data cartridges that provide new behavior without needing additional attributes have the option of using packages rather than user-defined types. Either way, you determine how the server interprets, stores, retrieves, and indexes the application data. Data cartridges package this functionality, creating software components that plug into a server and extend its capabilities into a new domain, making the database itself extensible.

You can customize the indexing and query optimization mechanisms of an extensible database management system and provide specialized services or more efficient processing for user-defined business objects and rich types. When you register your implementations with the server through extensibility interfaces, you direct the server to implement your customized processing instructions instead of its own default processes.

The extensibility interfaces consist of functions that the server calls to execute the custom indexing or optimizing behavior implemented for a data cartridge. The interfaces are defined by Oracle; as a cartridge developer, you must implement the functions or interfaces that have the specialized behavior you require in your application. In general, you implement the functions as static methods of an object type. An object type that implements the extensible indexing interface is called an indextype; an object type that implements the extensible optimizing interface is called a statistics type.

Data cartridges have the following key characteristics:

- Data cartridges are server-based. Their constituents reside on the server or are accessed from the server. The server runs all data cartridge processes, or dispatches these processes as external procedures.
- Data cartridges extend the server. They define new types and behavior, enabling the server to perform processes that were are otherwise unavailable to it, in component form. Data cartridges can use these new types and behaviors in their applications.
- Data cartridges are integrated with the server. The Oracle Extensibility Framework defines a set of interfaces that integrate data cartridges with the components of the server engine, allowing for domain-specific indexing, domain-specific optimized access to the CPU resources, and domain-specific optimization of I/O access to cartridge data.
- Data cartridges are packaged. A data cartridge is installed as a unit. After it is installed, the data cartridge handles all access issues for each user, including verification of schemas and privileges.

## Uses of Data Cartridges

Most industries have evolved sophisticated models to handle complex data objects that form the essence of their business. These data objects are both the structures that relate different units of information and the operations that are performed on them.

The simple names given to data objects often conceal considerable complexity. For example, the banking industry has many different types of bank accounts. Each bank account has customer demographic information, balance information, transaction information, and rules that embody its behavior (deposit, withdrawal, interest accrual, and so forth). When using data cartridges and their object-relational extension, application programmers and independent software vendors can encapsulate business logic in software components that integrate with the Oracle server and enhance it to support data types, processes, and logic to model business objects.

While business models have developed increasingly complex data objects, information technology has made it necessary to work with new and complex kinds of data, such as satellite images, X-rays, animal sounds, seismic vibrations, and chemical models. Complex and multimedia data types are now frequently stored and retrieved, queried and analyzed.

Web-based applications routinely include many different kinds of complex data. Including application-specific data types and the associated business logic requires a new class of networked, content-rich, multitiered, distributed applications. Data cartridges help you meet this need by combining scalar and unstructured data types in domain-specific components.

### Data Cartridge Domains

Data cartridges are typically domain-specific, characterized by content and scope of their target domain.

In terms of content, a data cartridge can accommodate scalar, complex, and multimedia data. Scalar data can be modeled using native SQL types such as `INTEGER`, `NUMBER`, or `CHAR`. Complex data include matrices, temperature and magnetic grids, and compound documents. Unstructured multimedia data includes such information as video, voice, and image data.

In terms of scope, a data cartridge can have either broad horizontal (cross-industry) coverage, or it can be specialized for a specific type of business. For example, a data cartridge for general storage and retrieval of text-based data is cross-industry in scope; a data cartridge for the storage and retrieval of legal documents for litigation support is industry-specific. Table 1-1 shows a way of classifying data cartridge domains according to their content and scope, with some examples.

Table 1-1 Data Cartridge Domains; Content and Scope

| Content | Cross-Industry Uses | Industry-Specific Extensions |
| --- | --- | --- |
| Scalar Data | Statistical conversion | Financial and Petroleum |
| Multimedia and Complex Unstructured Data | Text | Image |
| Audio/Video | Spatial | Legal |
| Medical | Broadcasting | Utilities |

You can also use scalar data types to construct more complex user-defined types. The object-relational database management system provides foundational data cartridges that package multimedia and complex data. These data cartridges can be used in developing applications across many different industries:

- Oracle Text uses the tokenized serial byte stream database model are used to implement display compress, reformat, and indexing behavior.
- Oracle Multimedia uses the database model for structured large objects to support storage and management of image, audio and video.
- Oracle Spatial is for use with geometric objects (points, lines, polygons); it implements project, rotate, transform and map behavior.

Another way of viewing the relationship of cartridges to domains is to consider basic multimedia data types as an extensible foundation that can be customized for specific industries. For example, medical applications can customize the Oracle Text for records, Oracle Multimedia for MRI results and heartbeat monitoring, and Oracle Spatial for demographic analysis.

A cartridge that provides basic services can be deployed across many industries. A cartridge can also leverage domain expertise across an industry. These cartridges can be further extended for more specialized vertical applications.

## Extending the Server: Services and Interfaces

The Oracle server provides services for basic data storage, query processing, optimization, and indexing. Applications use these services to access database capabilities. However, data cartridges have specialized needs because they incorporate domain-specific data. To accommodate these specialized applications, these basic services have been made extensible; where standard Oracle services are not adequate for meeting a data cartridge's requirements, you can provide additional services that satisfy the requirements of the specific data cartridge. Every data cartridge can provide its own implementations of these services.

For example, if you are developing a spatial data cartridge for geographic information systems (GIS) applications, you must to implement routines that create a spatial index, insert an entry into the index, update the index, delete from the index, and perform other required operations. Thus, you extend the indexing service of the server.

See Also:

[Chapter 15, "Power Demand Cartridge Example"](pwr_example.md).

### Extensibility Services

This section describes some extensible services, highlighting major Oracle capabilities as they relate to data cartridge development. Figure 1-2 shows the standard services implemented by the Oracle server.

Figure 1-1 Oracle Services

![Description of Figure 1-1 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci009.gif "Description of Figure 1-1 follows")  
[Description of "Figure 1-1 Oracle Services"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci009.htm)  

#### Extensible Type System

The Oracle universal data server provides both native and extensible type system services. Historically, most applications have focused on accessing and modifying corporate data that is stored in tables composed of native SQL data types, such as `INTEGER`, `NUMBER`, `DATE`, and `CHAR`. Oracle adds support for new types, including:

- User-defined object types
- Collections, such as `VARRAY` (varying length array) and nested tables
- Relationships (`REF` s)
- Large object types (`LOB` s), such as binary large objects (`BLOB` s), character large objects (`CLOB` s), and external binary files (`BFILE` s)

##### User-Defined Types

A user-defined type extents the modeling capabilities of the native data types and from them both because it is defined by a user, and because it specifies both the underlying persistent data (attributes) and the related behaviors (methods).

With user-defined types, you can make better models of complex entities in the real world by binding data attributes to semantic behaviors. A user-defined type can have one or more attributes, each with a name and a type. The type of an attribute can be a native SQL type, a `LOB`, a collection, another object type, or a `REF` type.

See Also:

- [Chapter 3, "Defining Object Types"](obj_types.md) for type definition syntax.
- [Oracle Database Object-Relational Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11822/adobjint.htm#ADOBJ001) for more information on user-defined types.

A method is a procedure or a function that is part of a user-defined type. Methods can access and manipulate attributes of their type while running within the execution environment of the Oracle server, or when they are dispatched outside the server as part of the extensible server execution environment.

##### Collection Types

Collections are SQL data types that contain multiple elements. Elements, or values, of a collection are all from the same type hierarchy. In Oracle, collections of complex types can be `VARRAY` s or nested tables.

A `VARRAY` type contains a variable number of ordered elements and can be used for a column of a table or an attribute of an object type. The element type of a `VARRAY` can be either a native data type, such as `NUMBER`, or a user-defined type.

To provide the semantics of an unordered collection, you could create a nested table using Oracle SQL As with a `VARRAY`, a nested table can define a column of a table or an attribute of a user-defined type.

##### Reference Types

If you create an object table in Oracle, you can obtain a reference, `REF`, that behaves like a database pointer to an associated row object. References are important for navigating among object instances. Because `REF` s rely on the underlying object identity, you can only use a `REF` with an object stored as a row in an object table, or with objects composed from an object view.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions145.htm#SQLRF00694) for details of the `REF` operator.
- [Oracle Database Object-Relational Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11822/adobjint.htm#ADOBJ001) for more information about objects.

##### Large Objects

Large object types, or `LOB` s, handle the storage demands of images, video clips, documents, and other forms of unstructured data. `LOB` s storage optimizes space requirements and efficient access.

`LOB` s are composed of locators and the related binary or character data. The locators are stored inline with other table columns. Internal `LOB` s (`BLOB` s, `CLOBs`, and `NCLOB` s) can store data in a separate database storage area. External `LOB` s (`BFILE` s) store the data outside the database tablespaces, in operating system files. A table can contain multiple `LOB` columns, in contrast to the limit of a single `LONG` `RAW` column for each table. Each `LOB` column can be stored in a separate tablespace, and even on different secondary storage devices.

You can create, modify, and delete tables and object types that contain `LOB` s using the Oracle SQL data definition language (DDL) extensions. Using the Oracle SQL data manipulation language (DML) statements, you can insert and delete complete `LOBs`. There is also an extensive set of statements for piece-wise reading, writing, and manipulating of `LOB` s within Java, PL/SQL, and the Oracle Call Interface.

For internal `LOB` types, both the locators and related data participate fully in the transactional model of the Oracle server. The data for `BFILEs` does not participate in transactions; however, `BFILE` locators are fully supported by Oracle server transactions.

Unlike scalar quantities, a `LOB` value cannot be indexed by built-in indexing schemes. However, you can use the various `LOB` APIs to build modules, including methods of user-defined types, to access and manipulate `LOB` content. You can define the semantics of data residing in `LOB` s and manipulate this data using the extensible indexing framework.

See Also:

- [Chapter 6, "Working with Multimedia Data Types"](lobs.md) for information on how to use `LOBs` to store and manipulate binary and character data that represents your domain.
- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/adlob_working.htm#ADLOB002) for detailed discussions of large objects.

#### Extensible Server Execution Environment

The Oracle type system decouples the implementation of a member method for a user-defined type from the specification of that method. Oracle data cartridge components can be implemented using a large number of popular programming languages, such as PL/SQL, C, C++, or Java, extending the database server run-time environment by user-defined methods, functions, and procedures.

Java offers data cartridge developers a powerful implementation choice for data cartridge behavior. PL/SQL is a powerful procedural language that supports all the object extensions for SQL. With PL/SQL, program logic can execute on the server and perform traditional procedural language operations such as loops, if-then-else clauses, and array access.

While PL/SQL and Java are powerful, certain computation-intensive operations such as a Fast Fourier Transform or an image format conversion are handled more efficiently by C programs. You can call C language programs from the server, running them in a separate address space, thus insulating the server and protecting the database from corruption by external procedure failures.

With certain reasonable restrictions, external procedures can callback the Oracle Server using OCI. Callbacks are particularly useful for processing `LOB` s. External procedure can use callbacks to perform piece-wise reads or writes of `LOB` s stored in the database, or to manipulate domain indexes stored as index-organized tables in the database.

Figure 1-2 External Programs Executing in a Separate Address Space

![Description of Figure 1-2 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci010.gif "Description of Figure 1-2 follows")  
[Description of "Figure 1-2 External Programs Executing in a Separate Address Space"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci010.htm)  

#### Extensible Indexing

Basic database management systems support a few types of access methods, such as B+ trees and hash indexes, on a limited set of data types, such as numbers and strings. For simple data types like integers and small strings, all aspects of indexing can easily be handled by the database system. As data becomes more complex with addition of text, spatial, image, video, and audio information, it requires complex data types and specialized indexing techniques.

Complex data types have application-specific formats, indexing requirements, and selection predicates. For example, there are many different means of document encoding (ODA, XML, plain text) and information retrieval techniques (keyword, full-text boolean, similarity, and probabilistic). Similarly, R-trees are an efficient method of indexing spatial data. To enable you to define the index types necessary for your business requirements, Oracle provides an extensible indexing framework.

Such user-defined indexes are called domain indexes because they index data in an application-specific domain. The cartridge is responsible for defining the index structure, maintaining the index content during load and update operations, and searching the index during query processing. The physical index can be stored either in the Oracle database as tables, or externally as a file.

A domain index is a schema object. It is created, managed, and accessed by routines implemented as methods of a user-defined type called an indextype. The routines that an indextype must implement, and the operations the routines must perform, are described in [Chapter 8, "Building Domain Indexes"](dom_idx.md). Implementation of the routines is specific to an application, and must therefore be completed by the cartridge developer.

With extensible indexing, the application must have the following processes:

- Define the structure of the domain index.
- Store the index data, either inside or outside the Oracle database.
- Manage, retrieve, and use the index data to evaluate user queries.

When the database system handles the physical storage of domain indexes, data cartridges must have the following processes:

- Define the format and content of an index. Cartridges define an index structure that can accommodate a complex data object.
- Build, delete, and update a domain index. Cartridges build and maintain the index structures. Because indexes are modeled as collections of tuples, they directly support in-place updates.
- Access and interpret the content of an index. Cartridges become an integral component of query processing by handling content-related clauses for database queries.

Typical relational and object-relational database management systems do not support extensible indexing. Consequently, many applications maintain file-based indexes for complex data in relational database tables. A considerable amount of code and effort is required to complete the following tasks:

- Maintain consistency between external indexes and the related relational data.
- Support compound queries involving tabular values and external indexes.
- Manage the system, performing backup, recovery, storage allocation, and so on, with multiple forms of persistent storage, such as files and databases.

By supporting extensible indexes, the Oracle server significantly reduces the level of effort needed to develop solutions involving high-performance access to complex data types.

#### Extensible Optimizer

The extensible optimizer lets user-defined functions and indexes collect statistical information, such as selectivity and cost functions, and generates an execution plan for a SQL statement. This information is used by the optimizer in choosing a query plan, thus extending the optimizer to use the user-supplied information. The rule-based optimizer remains unchanged.

An execution plan generated by the optimizer includes an access method for each table in the `FROM` clause, and an ordering, called the join order, of the tables in the `FROM` clause. System-defined access methods include indexes, hash clusters, and table scans. For each table in the join order, the optimizer chooses a plan by generating a set of join orders or permutations, computing the cost of each, and selecting the one with the lowest cost. The cost of the join order is the sum of the access method and join method costs.

The cost model is a group of algorithms used for calculating the cost of a given operation. It can include varying levels of detail about the physical environment in which the query runs. The current cost model includes the number of disk accesses and estimates of network costs, with minor adjustments.

The optimizer also uses statistics about the objects referenced in the query to calculate cost and selectivity, or the fraction of rows in a table that a query selects (between 0 and 100, a percentage). The `DBMS_STATS` package contains methods for generating these statistics.

Extensibility allows users to define new operators, index types, and domain indexes, and enables the control of the three main components used by the optimizer to select an execution plan: statistics, selectivity, and cost.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_stats.htm#ARPLS059) for information about `DBMS_STATS`.

### Extensibility Interfaces

There are three classes of extensibility interfaces: DBMS interfaces, cartridge basic service interfaces, and data cartridge interfaces.

#### DBMS Interfaces

The DBMS interfaces offer the simplest kind of extensibility services. They can be used through extensions to SQL or to the Oracle Call Interface (OCI). For example, the extensible type manager uses the `CREATE` `TYPE` syntax in SQL. Similarly, extensible indexing uses DDL and DML support for specifying and manipulating indexes.

#### Cartridge Basic Service Interfaces

Cartridge basic interfaces provide generic services like memory management, context management, internationalization, and cartridge-specific management. They implement behavior for new data types for the server's execution environment, and provide routines that help developers implement portable and robust server-side methods.

#### Data Cartridge Interfaces

When processing user-defined indextypes, Oracle calls data cartridge functions to perform index search or fetch operations. For user-defined query optimization, the query optimizer calls functions implemented by the data cartridge to compute the cost of user-defined operators or functions.