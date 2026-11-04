---
title: Concepts for Database Developers
book: Concepts
doc_id: E40540-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40540/cncptdev.htm
tags:
  - oracle
  - 11g
  - concepts
---

## 19 Concepts for Database Developers

The Oracle Database developer creates and maintains a database application. This section presents a brief overview of what a database developer does and the development tools available.

This section contains the following topics:

## Duties of Database Developers

An Oracle developer is responsible for creating or maintaining the database components of an application that uses the Oracle technology stack. Oracle developers either develop new applications or convert existing applications to run in an Oracle Database environment. For this reason, developers work closely with the database administrators, sharing knowledge and information.

Oracle database developers can expect to be involved in the following tasks:

- Implementing the data model required by the application
- Creating [schema objects](glossary.md) and implementing rules for [data integrity](glossary.md)
- Choosing a programming environment for a new development project
- Writing server-side [PL/SQL](glossary.md) or Java subprograms and client-side procedural code that use [SQL](glossary.md) statements
- Creating the application interface with the chosen development tool
- Establishing a Globalization Support environment for developing globalized applications
- Instantiating applications in different databases for development, testing, education, and deployment in a production environment

The preceding tasks, and many others, are described in [Oracle Database 2 Day Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10766/tdddg_intro.htm#TDDDG10000) and [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm).

See Also:

["Introduction to Server-Side Programming"](srvrside.md)

## Tools for Database Developers

Oracle provides several tools for use in developing database applications. This section describes some commonly used development tools.

### SQL Developer

SQL Developer is a graphical version of [SQL\*Plus](glossary.md), written in Java, that supports development in SQL and PL/SQL. You can connect to any Oracle database schema using standard database authentication. SQL Developer enables you to:

- Browse, create, edit, and delete schema objects
- Execute SQL statements
- Edit and debug PL/SQL program units
- Manipulate and export data
- Create and display reports

SQL Developer is available in the default Oracle Database installation and by free download.

See Also:

[Oracle Database 2 Day Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10766/tdddg_connecting.htm#TDDDG12200) and [Oracle SQL Developer User's Guide](https://docs.oracle.com/cd/E11882_01/doc.112/e12152/intro.htm#RPTUG10000) to learn how to use SQL Developer

### Oracle Application Express

Oracle Application Express (APEX) is a Web application development tool for Oracle Database. The tool uses built-in features such as user interface themes, navigational controls, form handlers, and flexible reports to accelerate application development.

Oracle Application Express installs with the database and consists of data in tables and PL/SQL code. When you run an application, your browser sends a URL request that is translated into an Oracle Application Express PL/SQL call. After the database processes the PL/SQL, the results are relayed back to the browser as HTML. This cycle happens each time you request or submit a page.

You can use Oracle Application Express with the embedded PL/SQL gateway. The gateway runs in the XML DB HTTP server in the database and provides the necessary infrastructure to create dynamic applications. As shown in Figure 19-1, the embedded PL/SQL gateway simplifies the application architecture by eliminating the middle tier.

Figure 19-1 Application Express with Embedded PL/SQL Gateway

![Figure 19-1 Application Express with Embedded PL/SQL Gateway](img/cncpt317.gif)

> This illustration graphically depicts the architecture of Oracle Application Express when using the Embedded PL/SQL Gateway instead of Oracle HTTP Server (Apache). It shows arrows going in both directions between the Web browser and the Oracle database. The Application Express engine resides within the Oracle database.
>
> [Copyright © 1993, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

See Also:

[Oracle Database 2 Day + Application Express Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11946/intro_app.htm#TDPAX01000) to learn how to use APEX

### Oracle JDeveloper

Oracle JDeveloper is an integrated development environment (IDE) for building service-oriented applications using the latest industry standards for Java, XML, Web services, and SQL. Oracle JDeveloper supports the complete software development life cycle, with integrated features for modeling, coding, debugging, testing, profiling, tuning, and deploying applications.

JDeveloper uses windows for various application development tools. For example, when creating a Java application, you can use tools such as the Java Visual Editor and Component Palette. In addition to these tools, JDeveloper provides a range of navigators to help you organize and view the contents of your projects.

See Also:

- [Oracle Database 2 Day + Java Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e12137/introduction.htm#TDPJD106) to learn how to use JDeveloper
- You can download JDeveloper from the following URL: `http://www.oracle.com/technetwork/developer-tools/jdev/downloads/`

### Oracle JPublisher

Java Publisher (JPublisher) is a simple and convenient tool to create Java programs that access database tables. Java code stubs generated by JDeveloper present object-relational structures in the database as Java classes. These classes can represent the following user-defined database entities in a Java program:

- SQL object types
- Object reference types
- SQL collection types
- PL/SQL packages

You can specify and customize the mapping of these entities to Java classes in a strongly typed paradigm, so that a specific Java type is associated with a specific user-defined SQL type. JPublisher can also generate classes for PL/SQL packages. These classes have wrapper methods to call the [stored procedure](glossary.md) in the package.

See Also:

[Oracle Database JPublisher User's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e10587/toc.htm)

### Oracle Developer Tools for Visual Studio.NET

Oracle Developer Tools for Visual Studio.NET is a set of application tools integrated with the Visual Studio.NET environment. These tools provide GUI access to Oracle functionality, enable the user to perform a wide range of application development tasks, and improve development productivity and ease of use.

Oracle Developer Tools support the programming and implementation of.NET stored procedures using Visual Basic, C#, and other.NET languages. These procedures are written in a.NET language and contain SQL or PL/SQL statements.

See Also:

[Oracle Database 2 Day +.NET Developer's Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10767/introduction.htm#TDPNG10000)

## Topics for Database Developers

[Chapter 17](cmntopc.md) describes topics important for both developers and administrators. This section covers topics that are most essential to database developers and that have not been discussed elsewhere in the manual.

This section contains the following topics:

- Principles of Application Design and Tuning
- Client-Side Database Programming
- Globalization Support
- Unstructured Data

### Principles of Application Design and Tuning

Oracle developers must design, create, and tune database applications so that they achieve security and performance goals. The following principles of application design and tuning are useful guidelines:

- Understand how Oracle Database works
	As a developer, you want to develop applications in the least amount of time against an Oracle database, which requires exploiting the database architecture and features. For example, not understanding Oracle Database [concurrency](glossary.md) controls and multiversioning [read consistency](glossary.md) may make an application corrupt the integrity of the data, run slowly, and decrease scalability (see ["Introduction to Data Concurrency and Consistency"](consist.md)).
- Use bind variables
	When a [query](glossary.md) uses [bind variables](glossary.md), the database can compile it once and store the [query plan](glossary.md) in the [shared pool](glossary.md). If the same statement is executed again, then the database can perform a [soft parse](glossary.md) and reuse the plan. In contrast, a [hard parse](glossary.md) takes longer and uses more resources (see ["SQL Parsing"](sqllangu.md)). Using bind variables to allow soft parsing is very efficient and is the way the database intends developers to work.
- Implement [integrity constraints](glossary.md) in the server rather than in the client
	Using primary and foreign keys enables data to be reused in multiple applications. Coding the rules in a client means that other clients do not have access to these rules when running against the databases (see ["Advantages of Integrity Constraints"](datainte.md)).
- Build a test environment with representative data and session activity
	A test environment that simulates your live production environment provides multiple benefits. For example, you can benchmark the application to ensure that it scales and performs well. Also, you can use a test environment to measure the performance impact of changes to the database, and ensure that upgrades and patches work correctly.
- Design the data model with the goal of good performance
	Typically, attempts to use generic data models result in poor performance. A well-designed data model answer the most common queries as efficiently as possible. For example, the data model should use the type of indexes that provide the best performance. Tuning after deployment is undesirable because changes to logic and physical structures may be difficult or impossible.
- Define clear performance goals and keep historical records of metrics
	An important facet of development is determining exactly how the application is expected to perform and scale. For example, you should use metrics that include expected user load, transactions per second, acceptable response times, and so on. Good practice dictates that you maintain historical records of performance metrics. In this way, you can monitor performance proactively and reactively (see ["Performance Diagnostics and Tuning"](cncptdba.md)).
- Instrument the application code
	Good development practice involves adding debugging code to your application. The ability to generate trace files is useful for debugging and diagnosing performance problems.

See Also:

[Oracle Database 2 Day Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10766/tdddg_deploying.htm#TDDDG70000) for considerations when designing and deploying database applications

### Client-Side Database Programming

As explained in [Chapter 8, "Server-Side Programming: PL/SQL and Java"](srvrside.md), two basic techniques enable procedural database applications to use SQL: server-side programming with PL/SQL and Java, and client-side programming with precompilers and APIs. This section provides a brief overview of client-side database programming.

See Also:

[Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_environments.htm#ADFNS00109) to learn how to choose a programming environment

#### Embedded SQL

Historically, client/server programs have used embedded SQL to interact with the database. This section explains options for using embedded SQL.

##### Oracle Precompilers

Client/server programs are typically written using precompilers, which are programming tools that enable you to embed SQL statements in high-level programs. For example, the Oracle Pro\*C/C++ precompiler enables you to embed SQL statements in a C or C++ source file. Oracle precompilers are also available for COBOL and FORTRAN.

A precompiler provides several benefits, including the following:

- Increases productivity because you typically write less code than equivalent OCI applications
- Enables you to create highly customized applications
- Allows close monitoring of resource use, SQL statement execution, and various run-time indicators
- Saves time because the precompiler, not you, translates each embedded SQL statement into calls to the Oracle Database run-time library
- Uses the Object Type Translator to map Oracle Database object types and collections into C data types to be used in the Pro\*C/C++ application
- Provides compile time type checking of object types and collections and automatic type conversion from database types to C data types

The client application containing the SQL statements is the host program. This program is written in the host language. In the host program, you can mix complete SQL statements with complete C statements and use C variables or structures in SQL statements. When embedding SQL statements you must begin them with the keywords `EXEC SQL` and end them with a semicolon. Pro\*C/C++ translates `EXEC SQL` statements into calls to the run-time library SQLLIB.

Many embedded SQL statements differ from their interactive counterparts only through the addition of a new clause or the use of program variables. The following example compares interactive and embedded `ROLLBACK` statements:

```
ROLLBACK;           -- interactive
EXEC SQL ROLLBACK;  -- embedded
```

The statements have the same effect, but you would use the first in an interactive SQL environment (such as SQL Developer), and the second in a Pro\*C/C++ program.

A precompiler accepts the host program as input, translates the embedded SQL statements into standard database run-time library calls, and generates a source program that you can compile, link, and run in the usual way. Figure 19-2 illustrates typical steps of developing programs that use precompilers.

Figure 19-2 Program Development with Precompilers

![Figure 19-2 Program Development with Precompilers](img/cncpt253.gif)

> This graphic is depicted as a large, downward-pointing arrow. The arrow contains a stack of boxes. From top to bottom, the boxes are: Editor, Host Program (labeled "With embedded SQL statements"), Oracle Precompiler, Source Program (labeled "With all SQL statements replaced by library calls"), Compiler, Object Program, Linker (pointed to by an Oracle Runtime Library (SQLLIB) box). The arrow point to an Executable Program box.
  

See Also:

- [Pro\*C/C++ Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10825/toc.htm) for a complete description of the Pro\*C/C++ precompiler
- [Pro\*FORTRAN Supplement to the Oracle Precompilers Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10828/toc.htm)

##### SQLJ

SQLJ is an ANSI SQL-1999 standard for embedding SQL statements in Java source code. SQLJ provides a simpler alternative to the Java Database Connectivity (JDBC) API for client-side SQL data access from Java.

The SQLJ interface is the Java equivalent of the Pro\* interfaces. You insert SQL statements in your Java source code. Afterward, you submit the Java source files to the SQLJ translator, which translates the embedded SQL to pure JDBC-based Java code.

See Also:

["SQLJ"](srvrside.md)

#### Client-Side APIs

Most developers today use an API to embed SQL in their database applications. For example, two popular APIs for enabling programs to communicate with Oracle Database are Open Database Connectivity (ODBC) and JDBC. The Oracle Call Interface (OCI) and Oracle C++ Call Interface (OCCI) are two other common APIs for client-side programming.

##### OCI and OCCI

As an alternative to precompilers, Oracle provides the OCI and OCCI APIs. OCI lets you manipulate data and schemas in a database using a host programming language such as C. OCCI is an object-oriented interface suitable for use with C++. Both APIs enable developers to use native subprogram invocations to access Oracle Database and control SQL execution.

In some cases, OCI provides better performance or more features than higher-level interfaces. OCI and OCCI provide many features, including the following:

- Support for all SQL [DDL](glossary.md), [DML](glossary.md), query, and transaction control facilities available through Oracle Database
- Instant client, a way to deploy applications when disk space is an issue
- Thread management, connection pooling, globalization functions, and direct path loading of data from a C application

OCI and OCCI provide a library of standard database access and retrieval functions in the form of a dynamic run-time library (OCILIB). This library can be linked in an application at run time. Thus, you can compile and link an OCI or OCCI program in the same way as a nondatabase application, avoiding a separate preprocessing or precompilation step. Figure 19-3 illustrates the development process.

Figure 19-3 Development Process Using OCI or OCCI

![Figure 19-3 Development Process Using OCI or OCCI](img/cncpt307.gif)

> This illustration shows the Source Files being processed by the Host Language Compiler, which produces object files.
>
> The object files are next linked by the host linker, with the OCI Library, which outputs the application executable.
>
> The application can then communicate with the Oracle Server.
>
> [Copyright © 1993, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

##### ODBC and JDBC

ODBC is a standard API that enables applications to connect to a database and then prepare and run SQL statements. ODBC is independent of programming language, database, and operating system. The goal of ODBC is to enable any application to access data contained in any database.

A database driver is software that sits between an application and the database. The driver translates the API calls made by the application into commands that the database can process. By using an ODBC driver, an application can access any data source, including data stored in spreadsheets. The ODBC driver performs all mappings between the ODBC standard and the database.

The Oracle ODBC driver provided by Oracle enables ODBC-compliant applications to access Oracle Database. For example, an application written in Visual Basic can use ODBC to query and update tables in an Oracle database.

JDBC is a low-level Java interface that enables Java applications to interact with Oracle database. Like ODBC, JDBC is a vendor-independent API. The JDBC standard is defined by Sun Microsystems and implemented through the `java.sql` interfaces.

The JDBC standard enables individual providers to implement and extend the standard with their own JDBC drivers. Oracle provides the following JDBC drivers for client-side programming:

- JDBC thin driver
	This pure Java driver resides on the client side without an Oracle client installation. It is platform-independent and usable with both applets and applications.
- JDBC OCI driver
	This driver resides on the client-side with an Oracle client installation. It is usable only with applications. The JDBC OCI driver, which is written in both C and Java, converts JDBC calls to OCI calls.

The following snippets are from a Java program that uses the JDBC OCI driver to create a `Statement` object and query the `dual` table:

```
// Create a statement
Statement stmt = conn.createStatement();
 
// Query dual table
ResultSet rset = stmt.executeQuery("SELECT 'Hello World' FROM DUAL");
```

See Also:

- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_environments.htm#ADFNS00103) and Oracle Database 2 Day + Java Developer's Guide to learn more about JDBC
- [Oracle Database Gateway for ODBC User's Guide](https://docs.oracle.com/cd/E11882_01/gateways.112/e12070/intro.htm#ODBCU100)

### Globalization Support

Oracle Database globalization support enables you to store, process, and retrieve data in native languages. Thus, you can develop multilingual applications and software that can be accessed and run from anywhere in the world simultaneously.

Developers who write globalized database application must do the following:

- Understand the Oracle Database globalization support architecture, including the properties of the different character sets, territories, languages, and linguistic sort definitions
- Understand the globalization functionality of their middle-tier programming environment, including how it can interact and synchronize with the locale model of the database
- Design and write code capable of simultaneously supporting multiple clients running on different operating systems, with different character sets and locale requirements

For example, an application may be required to render content of the user interface and process data in languages and locale preferences of native users. For example, the application must process multibyte Kanji data, display messages and dates in the proper regional format, and process 7-bit ASCII data without requiring users to change settings.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch1overview.htm#NLSPG001) for more information about globalization

#### Globalization Support Environment

The globalization support environment includes the client application and the database. You can control language-dependent operations by setting parameters and environment variables on the client and server, which may exist in separate locations.

Note:

In previous releases, Oracle referred to globalization support capabilities as National Language Support (NLS) features. NLS is actually a subset of globalization support and provides the ability to choose a national language and store data in a specific character set.

Oracle Database provides globalization support for features such as:

- Native languages and territories
- Local formats for date, time, numbers, and currency
- Calendar systems (Gregorian, Japanese, Imperial, Thai Buddha, and so on)
- Multiple character sets, including Unicode
- Character semantics

##### Character Sets

A key component of globalization support is a character set, which is an encoding scheme used to display characters on your computer screen. The following distinction is important in application development:

- A database character set determines which languages can be represented in a database. The character set is specified at database creation.
	Note:
	After a database is created, changing its character set is usually very expensive in terms of time and resources. This operation may require converting all character data by exporting the whole database and importing it back.
- A client character set is the character set for data entered or displayed by a client application. The character set for the client and database can be different.

A group of characters (for example, alphabetic characters, ideographs, symbols, punctuation marks, and control characters) can be encoded as a character set. An encoded character set assigns a unique numeric code, called a code point or encoded value, to each character in the set. Code points are important in a global environment because of the potential need to convert data between different character sets.

The computer industry uses many encoded character sets. These sets differ in the number of characters available, the characters available for use, code points assigned to each character, and so on. Oracle Database supports most national, international, and vendor-specific encoded character set standards.

Oracle Database supports the following classes of encoded character sets:

- Single-Byte character sets
	Each character occupies one byte. An example of a 7-bit character set is US7ASCII. An example of an 8-bit character set is WE8DEC.
- Multibyte character sets
	Each character occupies multiple bytes. Multibyte sets are commonly used for Asian languages.
- Unicode
	The universal encoded character set enables you to store information in any language by using a single character set. Unicode provides a unique code value for every character, regardless of the platform, program, or language.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch11charsetmig.htm#NLSPG011) to learn about character set migration

##### Locale-Specific Settings

A locale is a linguistic and cultural environment in which a system or program is running. NLS parameters determine locale-specific behavior on both the client and database. A database session uses NLS settings when executing statements on behalf of a client. For example, the database makes the correct territory usage of the thousands separator for a client.

Typically, the `NLS_LANG` environment variable on the client host specifies the locale for both the server session and client application. The process is as follows:

1. When a client application starts, it initializes the client NLS environment from the environment settings.
	All NLS operations performed locally, such as displaying formatting in Oracle Developer applications, use these settings.
2. The client communicates the information defined by `NLS_LANG` to the database when it connects.
3. The database session initializes its NLS environment based on the settings communicated by the client.
	If the client did not specify settings, then the session uses the settings in the initialization parameter file. The database uses the initialization parameter settings only if the client did not specify any NLS settings. If the client specified some NLS settings, then the remaining NLS settings default.

Each session started on behalf of a client application may run in the same or a different locale as other sessions. For example, one session may use the German locale while another uses the French locale. Also, each session may have the same or different language requirements specified.

Table 19-1 shows two clients using different `NLS_LANG` settings. A user starts SQL\*Plus on each host, logs on to the same database as `hr`, and runs the same query simultaneously. The result for each session differs because of the locale-specific NLS setting for floating-point numbers.

Table 19-1 Locale-Specific NLS Settings

| t | Client Host 1 | Client Host 2 |
| --- | --- | --- |
| t0 | ``` $ export NLS_LANG=American_America.US7ASCII ``` | ``` $ export NLS_LANG=German_Germany.US7ASCII ``` |
| t1 | ``` $ sqlplus /nolog SQL> CONNECT hr@proddb Enter password: ******* SQL> SELECT 999/10 FROM DUAL;   999/10 ---------- 99.9 ``` | ``` $ sqlplus /nolog SQL> CONNECT hr@proddb Enter password: ******* SQL> SELECT 999/10 FROM DUAL;   999/10 ---------- 99,9 ``` |

See Also:

[Oracle Database 2 Day + Java Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e12137/globapps.htm#TDPJD253) and [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch3globenv.htm#NLSPG189) to learn about NLS settings

#### Oracle Globalization Development Kit

The Oracle Globalization Development Kit (GDK) simplifies the development process and reduces the cost of developing Internet applications used to support a global environment. The GDK includes comprehensive programming APIs for both Java and PL/SQL, code samples, and documentation that address many of the design, development, and deployment issues encountered while creating global applications.

The GDK mainly consists of two parts: GDK for Java and GDK for PL/SQL. GDK for Java provides globalization support to Java applications. GDK for PL/SQL provides globalization support to the PL/SQL programming environment. The features offered in the two parts are not identical.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch8gdk.htm#NLSPG008)

### Unstructured Data

The traditional relational model deals with simple structured data that fits into simple tables. Oracle Database also provides support for unstructured data, which cannot be decomposed into standard components. Unstructured data includes text, graphic images, video clips, and sound waveforms.

Oracle Database includes data types to handle unstructured content. These data types appear as native types in the database and can be queried using SQL.

#### Overview of XML in Oracle Database

Oracle XML DB is a set of Oracle Database technologies related to high-performance XML storage and retrieval. XML DB provides native XML support by encompassing both SQL and XML data models in an interoperable manner.

Oracle XML DB is suited for any Java or PL/SQL application where some or all of the data processed by the application is represented using XML. For example, the application may have large numbers of XML documents that must be ingested, generated, validated, and searched.

Oracle XML DB provides many features, including the following:

- The native `XMLType` data type, which can represent an XML document in the database so that it is accessible by SQL
- Support for XML standards such as XML Schema, XPath, XQuery, XSLT, and DOM
- `XMLIndex`, which supports all forms of XML data, from highly structured to completely unstructured

Example 19-1 creates a table `orders` of type `XMLType`. The example also creates a SQL [directory object](glossary.md), which is a logical name in the database for a physical directory on the host computer. This directory contains XML files. The example inserts XML content from the `purchaseOrder.xml` file into the `orders` table.

Example 19-1 XMLType

```
CREATE TABLE orders OF XMLType;
CREATE DIRECTORY xmldir AS path_to_folder_containing_XML_file;
INSERT INTO orders VALUES (XMLType(bfilename('XMLDIR', 'purchaseOrder.xml'),
                                       nls_charset_id('AL32UTF8')));
```

The Oracle XML developer's kits (XDK) contain the basic building blocks for reading, manipulating, transforming, and viewing XML documents, whether on a file system or in a database. APIs and tools are available for Java, C, and C++. The production Oracle XDKs are fully supported and come with a commercial redistribution license.

#### Overview of LOBs

The [large object (LOB)](glossary.md) data types enable you to store and manipulate large blocks of unstructured data in binary or character format. LOBs provide efficient, random, piece-wise access to the data.

##### Internal LOBs

An internal LOB stores data in the database itself rather than in external files. Internal LOBS include the following:

- `CLOB` (character LOB), which stores large amounts of text, such as text or XML files, in the database character set
- `NCLOB` (national character set LOB), which stores Unicode data
- `BLOB` (binary LOB), which stores large amounts of binary information as a bit stream and is not subject to character set translation

The database stores LOBs differently from other data types. Creating a LOB column implicitly creates a LOB segment and a LOB index (see ["User Segment Creation"](logical.md)). The tablespace containing the LOB segment and LOB index, which are always stored together, may be different from the tablespace containing the table.

Note:

Sometimes the database can store small amounts of LOB data in the table itself rather than in a separate LOB segment.

The LOB segment stores data in pieces called chunks. A chunk is a logically contiguous set of data blocks and is the smallest unit of allocation for a LOB. A row in the table stores a pointer called a LOB locator, which points to the LOB index. When the table is queried, the database uses the LOB index to quickly locate the LOB chunks.

The database manages [read consistency](glossary.md) for LOB segments differently from other data (see ["Read Consistency and Undo Segments"](consist.md)). Instead of using [undo data](glossary.md) to record changes, the database stores the before images in the segment itself. When a transaction changes a LOB, the database allocates a new chunk and leaves the old data in place. If the transaction rolls back, then the database rolls back the changes to the index, which points to the old chunk.

##### External LOBs

A `BFILE` (binary file LOB) is an external LOB because the database stores a pointer to a file in the operating system. The external data is read-only.

A `BFILE` uses a directory object to locate data. The amount of space consumed depends on the length of the directory object name and the length of the file name.

A `BFILE` does not use the same read consistency mechanism as internal LOBS because the binary file is external to the database. If the data in the file changes, then repeated reads from the same binary file may produce different results.

##### SecureFiles

SecureFiles is a LOB data type specifically engineered to deliver high performance for file data comparable to that of traditional file systems, while retaining the advantages of Oracle Database. The `SECUREFILE` LOB parameter enables advanced features typically found in high-end file systems, such as deduplication, compression, encryption, and journaling.

See Also:

- ["Oracle Data Types"](tablecls.md)
- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/adlob_smart.htm#ADLOB4444) to learn more about LOB data types

#### Overview of Oracle Text

Oracle Text (Text) is a fast and accurate full-text retrieval technology integrated with Oracle Database. Oracle Text indexes any document or textual content stored in file systems, databases, or on the Web. These documents can be searched based on their textual content, metadata, or attributes.

Oracle Text provides the following advantages:

- Oracle Text allows text searches to be combined with regular database searches in a single SQL statement. The Text index is in the database, and Text queries are run in the Oracle Database process. The [optimizer](glossary.md) can choose the best [execution plan](glossary.md) for any query, giving the best performance for ad hoc queries involving Text and structured criteria.
- You can use Oracle Text with XML data. In particular, you can combine `XMLIndex` with Oracle Text indexing, taking advantage of both XML and a full-text index.
- The Oracle Text SQL API makes it simple and intuitive to create and maintain Oracle Text indexes and run searches.

For a use case, suppose you must create a catalog index for an auction site that sells electronic equipment. New inventory is added every day. Item descriptions, bid dates, and prices must be stored together. The application requires good response time for mixed queries. First, you create and populate a `catalog` table. You then use Oracle Text to create a `CTXCAT` index that you can query with the `CATSEARCH` operator in a `SELECT ... WHERE CATSEARCH` statement.

Figure 19-4 illustrates the relation of the catalog table, its `CTXCAT` index, and the catalog application that uses the `CATSEARCH` operator to query the index.

Figure 19-4 Catalog Query Application

![Figure 19-4 Catalog Query Application](img/ccapp017.gif)

> This illustration shows a generalized schema of a catalog query application. It shows a CTXCAT index and a document table as part of the database, and a two-way arrow between the database and a catalog application, representing a SQL CATSEARCH query.
>
> [Copyright © 1993, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

See Also:

- [Oracle Text Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/text.112/e24435/overview.htm#CCAPP9001) and [Oracle Text Reference](https://docs.oracle.com/cd/E11882_01/text.112/e24436/toc.htm)
- [Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/xdb09sea.htm#ADXDB1000) to learn how to perform full-text search over XML data

#### Overview of Oracle Multimedia

Oracle Multimedia enables Oracle Database to store, manage, and retrieve images, medical images that follow the Digital Imaging and Communications in Medicine (DICOM) standard, audio, and video data in an integrated fashion with other enterprise information. Oracle Multimedia provides object types and methods for:

- Extracting metadata and attributes from multimedia data
- Embedding metadata created by applications into image and DICOM data
- Obtaining and managing multimedia data from Oracle Database, Web servers, file systems, and other servers
- Performing operations such as thumbnail generation on image and DICOM data
- Making DICOM data anonymous
- Checking DICOM data for conformity to user-defined validation rules

See Also:

- [Oracle Multimedia User's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10777/ch_intr.htm#IMURG1000) and [Oracle Multimedia Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e10776/toc.htm)
- [Oracle Multimedia DICOM Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10778/ch_intro.htm#IMDCM1000) and [Oracle Multimedia DICOM Java API Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e10781/toc.htm)
- [Oracle Multimedia Java API Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e10779/toc.htm) and [Oracle Multimedia Servlets and JSP Java API Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e10780/toc.htm)

#### Overview of Oracle Spatial

Oracle Spatial (Spatial) provides a SQL schema and functions that facilitate the storage, retrieval, update, and query of collections of spatial features in an Oracle database. Oracle Spatial makes spatial data management easier to users of location-enabled applications and geographic information system (GIS) applications.

An example of spatial data is a road map. The spatial data indicates the Earth location (such as longitude and latitude) of objects on the map. When the map is rendered, this spatial data is used to project the locations of the objects on a two-dimensional piece of paper. A GIS is often used to store, retrieve, and render this Earth-relative spatial data. When spatial data is stored in an Oracle database, the data can be easily manipulated, retrieved, and related to other data.

See Also:

[Oracle Spatial Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11830/sdo_intro.htm#SPATL010)