---
title: "1.2.2 The Main Features of MySQL"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/features.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 1.2.2 The Main Features of MySQL

This section describes some of the important characteristics of the MySQL Database Software. In most respects, the roadmap applies to all versions of MySQL. For information about features as they are introduced into MySQL on a series-specific basis, see the “In a Nutshell” section of the appropriate Manual:

- MySQL 8.4: [What Is New in MySQL 8.4 since MySQL 8.0](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/mysql-nutshell.html)
- MySQL 8.0: [What Is New in MySQL 8.0](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-nutshell.html)
- MySQL 5.7: [What Is New in MySQL 5.7](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/mysql-nutshell.html)

#### Internals and Portability

- Written in C and C++.
- Tested with a broad range of different compilers.
- Works on many different platforms. See [https://www.mysql.com/support/supportedplatforms/database.html](https://www.mysql.com/support/supportedplatforms/database.html).
- For portability, configured using **CMake**.
- Tested with Purify (a commercial memory leakage detector) as well as with Valgrind, a GPL tool ([https://valgrind.org/](https://valgrind.org/)).
- Uses multi-layered server design with independent modules.
- Designed to be fully multithreaded using kernel threads, to easily use multiple CPUs if they are available.
- Provides transactional and nontransactional storage engines.
- Uses very fast B-tree disk tables (`MyISAM`) with index compression.
- Designed to make it relatively easy to add other storage engines. This is useful if you want to provide an SQL interface for an in-house database.
- Uses a very fast thread-based memory allocation system.
- Executes very fast joins using an optimized nested-loop join.
- Implements in-memory hash tables, which are used as temporary tables.
- Implements SQL functions using a highly optimized class library that should be as fast as possible. Usually there is no memory allocation at all after query initialization.
- Provides the server as a separate program for use in a client/server networked environment.

#### Data Types

- Many data types: signed/unsigned integers 1, 2, 3, 4, and 8 bytes long, [`FLOAT`](floating-point-types.md), [`DOUBLE`](floating-point-types.md), [`CHAR`](char.md), [`VARCHAR`](char.md), [`BINARY`](binary-varbinary.md), [`VARBINARY`](binary-varbinary.md), [`TEXT`](blob.md), [`BLOB`](blob.md), [`DATE`](datetime.md), [`TIME`](time.md), [`DATETIME`](datetime.md), [`TIMESTAMP`](datetime.md), [`YEAR`](year.md), [`SET`](set.md), [`ENUM`](enum.md), and OpenGIS spatial types. See [Chapter 13, *Data Types*](data-types.md).
- Fixed-length and variable-length string types.

#### Statements and Functions

- Full operator and function support in the [`SELECT`](select.md) list and `WHERE` clause of queries. For example:
	```
	mysql> SELECT CONCAT(first_name, ' ', last_name)
	    -> FROM citizen
	    -> WHERE income/dependents > 10000 AND age > 30;
	```
- Full support for SQL `GROUP BY` and `ORDER BY` clauses. Support for group functions ([`COUNT()`](aggregate-functions.md), [`AVG()`](aggregate-functions.md), [`STD()`](aggregate-functions.md), [`SUM()`](aggregate-functions.md), [`MAX()`](aggregate-functions.md), [`MIN()`](aggregate-functions.md), and [`GROUP_CONCAT()`](aggregate-functions.md)).
- Support for `LEFT OUTER JOIN` and `RIGHT OUTER JOIN` with both standard SQL and ODBC syntax.
- Support for aliases on tables and columns as required by standard SQL.
- Support for [`DELETE`](delete.md), [`INSERT`](insert.md), [`REPLACE`](replace.md), and [`UPDATE`](update.md) to return the number of rows that were changed (affected), or to return the number of rows matched instead by setting a flag when connecting to the server.
- Support for MySQL-specific [`SHOW`](show.md) statements that retrieve information about databases, storage engines, tables, and indexes. Support for the `INFORMATION_SCHEMA` database, implemented according to standard SQL.
- An [`EXPLAIN`](explain.md) statement to show how the optimizer resolves a query.
- Independence of function names from table or column names. For example, `ABS` is a valid column name. The only restriction is that for a function call, no spaces are permitted between the function name and the “ `(`” that follows it. See [Section 11.3, “Keywords and Reserved Words”](keywords.md).
- You can refer to tables from different databases in the same statement.

#### Security

- A privilege and password system that is very flexible and secure, and that enables host-based verification.
- Password security by encryption of all password traffic when you connect to a server.

#### Scalability and Limits

- Support for large databases. We use MySQL Server with databases that contain 50 million records. We also know of users who use MySQL Server with 200,000 tables and about 5,000,000,000 rows.
- Support for up to 64 indexes per table. Each index may consist of 1 to 16 columns or parts of columns. The maximum index width for [`InnoDB`](innodb-storage-engine.md) tables is either 767 bytes or 3072 bytes. See [Section 17.21, “InnoDB Limits”](innodb-limits.md). The maximum index width for [`MyISAM`](myisam-storage-engine.md) tables is 1000 bytes. See [Section 18.2, “The MyISAM Storage Engine”](myisam-storage-engine.md). An index may use a prefix of a column for [`CHAR`](char.md), [`VARCHAR`](char.md), [`BLOB`](blob.md), or [`TEXT`](blob.md) column types.

#### Connectivity

- Clients can connect to MySQL Server using several protocols:
	- Clients can connect using TCP/IP sockets on any platform.
	- On Windows systems, clients can connect using named pipes if the server is started with the [`named_pipe`](server-system-variables.md) system variable enabled. Windows servers also support shared-memory connections if started with the [`shared_memory`](server-system-variables.md) system variable enabled. Clients can connect through shared memory by using the [`--protocol=memory`](connection-options.md) option.
	- On Unix systems, clients can connect using Unix domain socket files.
- MySQL client programs can be written in many languages. A client library written in C is available for clients written in C or C++, or for any language that provides C bindings.
- APIs for C, C++, Eiffel, Java, Perl, PHP, Python, Ruby, and Tcl are available, enabling MySQL clients to be written in many languages. See [Chapter 31, *Connectors and APIs*](connectors-apis.md).
- The Connector/ODBC (MyODBC) interface provides MySQL support for client programs that use ODBC (Open Database Connectivity) connections. For example, you can use MS Access to connect to your MySQL server. Clients can be run on Windows or Unix. Connector/ODBC source is available. All ODBC 2.5 functions are supported, as are many others. See [MySQL Connector/ODBC Developer Guide](https://docs.oracle.com/cd/E17952_01/connector-odbc-en/).
- The Connector/J interface provides MySQL support for Java client programs that use JDBC connections. Clients can be run on Windows or Unix. Connector/J source is available. See [MySQL Connector/J Developer Guide](https://docs.oracle.com/cd/E17952_01/connector-j-en/).
- MySQL Connector/NET enables developers to easily create.NET applications that require secure, high-performance data connectivity with MySQL. It implements the required ADO.NET interfaces and integrates into ADO.NET aware tools. Developers can build applications using their choice of.NET languages. MySQL Connector/NET is a fully managed ADO.NET driver written in 100% pure C#. See [MySQL Connector/NET Developer Guide](https://docs.oracle.com/cd/E17952_01/connector-net-en/).

#### Localization

- The server can provide error messages to clients in many languages. See [Section 12.12, “Setting the Error Message Language”](error-message-language.md).
- Full support for several different character sets, including `latin1` (cp1252), `german`, `big5`, `ujis`, several Unicode character sets, and more. For example, the Scandinavian characters “ `å` ”, “ `ä` ” and “ `ö` ” are permitted in table and column names.
- All data is saved in the chosen character set.
- Sorting and comparisons are done according to the default character set and collation. It is possible to change this when the MySQL server is started (see [Section 12.3.2, “Server Character Set and Collation”](charset-server.md)). To see an example of very advanced sorting, look at the Czech sorting code. MySQL Server supports many different character sets that can be specified at compile time and runtime.
- The server time zone can be changed dynamically, and individual clients can specify their own time zone. See [Section 7.1.15, “MySQL Server Time Zone Support”](time-zone-support.md).

#### Clients and Tools

- MySQL includes several client and utility programs. These include both command-line programs such as [**mysqldump**](mysqldump.md) and [**mysqladmin**](mysqladmin.md), and graphical programs such as [MySQL Workbench](workbench.md).
- MySQL Server has built-in support for SQL statements to check, optimize, and repair tables. These statements are available from the command line through the [**mysqlcheck**](mysqlcheck.md) client. MySQL also includes [**myisamchk**](myisamchk.md), a very fast command-line utility for performing these operations on `MyISAM` tables. See [Chapter 6, *MySQL Programs*](programs.md).
- MySQL programs can be invoked with the `--help` or `-?` option to obtain online assistance.