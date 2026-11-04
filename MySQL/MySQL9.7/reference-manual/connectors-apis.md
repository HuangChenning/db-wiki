---
title: "Chapter 31 Connectors and APIs"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/connectors-apis.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

MySQL Connectors provide connectivity to the MySQL server for client programs. APIs provide low-level access to MySQL resources using either the classic MySQL protocol or X Protocol. Both Connectors and the APIs enable you to connect and execute MySQL statements from another language or environment, including ODBC, Java (JDBC), C++, Python, Node.js, PHP, Perl, Ruby, and C.

## MySQL Connectors

Oracle develops a number of connectors:

- [Connector/C++](https://docs.oracle.com/cd/E17952_01/connector-cpp-9.7-en/) enables C++ applications to connect to MySQL.
- [Connector/J](https://docs.oracle.com/cd/E17952_01/connector-j-en/) provides driver support for connecting to MySQL from Java applications using the standard Java Database Connectivity (JDBC) API.
- [Connector/NET](https://docs.oracle.com/cd/E17952_01/connector-net-en/) enables developers to create.NET applications that connect to MySQL. Connector/NET implements a fully functional ADO.NET interface and provides support for use with ADO.NET aware tools. Applications that use Connector/NET can be written in any supported.NET language.
- [Connector/ODBC](https://docs.oracle.com/cd/E17952_01/connector-odbc-en/) provides driver support for connecting to MySQL using the Open Database Connectivity (ODBC) API. Support is available for ODBC connectivity from Windows, Unix, and macOS platforms.
- [Connector/Python](https://docs.oracle.com/cd/E17952_01/connector-python-en/) provides driver support for connecting to MySQL from Python applications using an API that is compliant with the [Python DB API version 2.0](http://www.python.org/dev/peps/pep-0249/). No additional Python modules or MySQL client libraries are required.
- `Connector/Node.js` provides an asynchronous API for connecting to MySQL from Node.js applications using X Protocol. Connector/Node.js supports managing database sessions and schemas, working with MySQL Document Store collections and using raw SQL statements.

## The MySQL C API

For direct access to using MySQL natively within a C application, the [C API](https://docs.oracle.com/cd/E17952_01/c-api-9.7-en/) provides low-level access to the MySQL client/server protocol through the `libmysqlclient` client library. This is the primary method used to connect to an instance of the MySQL server, and is used both by MySQL command-line clients and many of the MySQL Connectors and third-party APIs detailed here.

`libmysqlclient` is included in MySQL distributions distributions.

See also [MySQL C API Implementations](https://docs.oracle.com/cd/E17952_01/c-api-9.7-en/c-api-implementations.html).

To access MySQL from a C application, or to build an interface to MySQL for a language not supported by the Connectors or APIs in this chapter, the [C API](https://docs.oracle.com/cd/E17952_01/c-api-9.7-en/) is where to start. A number of programmer's utilities are available to help with the process; see [Section 6.7, “Program Development Utilities”](programs-development.md).

## Third-Party MySQL APIs

The remaining APIs described in this chapter provide an interface to MySQL from specific application languages. These third-party solutions are not developed or supported by Oracle. Basic information on their usage and abilities is provided here for reference purposes only.

All the third-party language APIs are developed using one of two methods, using `libmysqlclient` or by implementing a native driver. The two solutions offer different benefits:

- Using *`libmysqlclient`* offers complete compatibility with MySQL because it uses the same libraries as the MySQL client applications. However, the feature set is limited to the implementation and interfaces exposed through `libmysqlclient` and the performance may be lower as data is copied between the native language, and the MySQL API components.
- *Native drivers* are an implementation of the MySQL network protocol entirely within the host language or environment. Native drivers are fast, as there is less copying of data between components, and they can offer advanced functionality not available through the standard MySQL API. Native drivers are also easier for end users to build and deploy because no copy of the MySQL client libraries is needed to build the native driver components.

Table 31.1, “MySQL APIs and Interfaces” lists many of the libraries and interfaces available for MySQL.

**Table 31.1 MySQL APIs and Interfaces**

| Environment | API | Type | Notes |
| --- | --- | --- | --- |
| Ada | GNU Ada MySQL Bindings | `libmysqlclient` | See [MySQL Bindings for GNU Ada](http://gnade.sourceforge.net/) |
| C | C API | `libmysqlclient` | See [MySQL 9.7 C API Developer Guide](https://docs.oracle.com/cd/E17952_01/c-api-9.7-en/). |
| C++ | Connector/C++ | `libmysqlclient` | See [MySQL Connector/C++ 9.7 Developer Guide](https://docs.oracle.com/cd/E17952_01/connector-cpp-9.7-en/). |
|  | MySQL++ | `libmysqlclient` | See [MySQL++ website](http://tangentsoft.net/mysql++/doc/). |
|  | MySQL wrapped | `libmysqlclient` | See [MySQL wrapped](http://www.alhem.net/project/mysql/). |
| Cocoa | MySQL-Cocoa | `libmysqlclient` | Compatible with the Objective-C Cocoa environment. See [http://mysql-cocoa.sourceforge.net/](http://mysql-cocoa.sourceforge.net/) |
| D | MySQL for D | `libmysqlclient` | See [MySQL for D](http://www.steinmole.de/d/). |
| Eiffel | Eiffel MySQL | `libmysqlclient` | See [Section 31.13, “MySQL Eiffel Wrapper”](apis-eiffel.md). |
| Erlang | `erlang-mysql-driver` | `libmysqlclient` | See [`erlang-mysql-driver`.](http://code.google.com/p/erlang-mysql-driver/) |
| Haskell | Haskell MySQL Bindings | Native Driver | See [Brian O'Sullivan's pure Haskell MySQL bindings](http://www.serpentine.com/blog/software/mysql/). |
|  | `hsql-mysql` | `libmysqlclient` | See [MySQL driver for Haskell](http://hackage.haskell.org/cgi-bin/hackage-scripts/package/hsql-mysql-1.7). |
| Java/JDBC | Connector/J | Native Driver | See [MySQL Connector/J Developer Guide](https://docs.oracle.com/cd/E17952_01/connector-j-en/). |
| Kaya | MyDB | `libmysqlclient` | See [MyDB](http://kayalang.org/library/latest/MyDB). |
| Lua | LuaSQL | `libmysqlclient` | See [LuaSQL](http://keplerproject.github.io/luasql/doc/us/). |
| .NET/Mono | Connector/NET | Native Driver | See [MySQL Connector/NET Developer Guide](https://docs.oracle.com/cd/E17952_01/connector-net-en/). |
| Objective Caml | OBjective Caml MySQL Bindings | `libmysqlclient` | See [MySQL Bindings for Objective Caml](http://raevnos.pennmush.org/code/ocaml-mysql/). |
| Octave | Database bindings for GNU Octave | `libmysqlclient` | See [Database bindings for GNU Octave](http://octave.sourceforge.net/database/index.html). |
| ODBC | Connector/ODBC | `libmysqlclient` | See [MySQL Connector/ODBC Developer Guide](https://docs.oracle.com/cd/E17952_01/connector-odbc-en/). |
| Perl | `DBI` / `DBD::mysql` | `libmysqlclient` | See [Section 31.9, “MySQL Perl API”](apis-perl.md). |
|  | `Net::MySQL` | Native Driver | See [`Net::MySQL`](http://search.cpan.org/dist/Net-MySQL/MySQL.pm) at CPAN |
| PHP | `mysql`, `ext/mysql` interface (deprecated) | `libmysqlclient` | See [MySQL and PHP](https://docs.oracle.com/cd/E17952_01/apis-php-en/). |
|  | `mysqli`, `ext/mysqli` interface | `libmysqlclient` | See [MySQL and PHP](https://docs.oracle.com/cd/E17952_01/apis-php-en/). |
|  | `PDO_MYSQL` | `libmysqlclient` | See [MySQL and PHP](https://docs.oracle.com/cd/E17952_01/apis-php-en/). |
|  | PDO mysqlnd | Native Driver |  |
| Python | Connector/Python | Native Driver | See [MySQL Connector/Python Developer Guide](https://docs.oracle.com/cd/E17952_01/connector-python-en/). |
| Python | Connector/Python C Extension | `libmysqlclient` | See [MySQL Connector/Python Developer Guide](https://docs.oracle.com/cd/E17952_01/connector-python-en/). |
|  | MySQLdb | `libmysqlclient` | See [Section 31.10, “MySQL Python API”](apis-python.md). |
| Ruby | mysql2 | `libmysqlclient` | Uses `libmysqlclient`. See [Section 31.11, “MySQL Ruby APIs”](apis-ruby.md). |
| Scheme | `Myscsh` | `libmysqlclient` | See [`Myscsh`](https://github.com/aehrisch/myscsh). |
| SPL | `sql_mysql` | `libmysqlclient` | See [`sql_mysql` for SPL](http://www.clifford.at/spl/spldoc/sql_mysql.html). |
| Tcl | MySQLtcl | `libmysqlclient` | See [Section 31.12, “MySQL Tcl API”](apis-tcl.md). |