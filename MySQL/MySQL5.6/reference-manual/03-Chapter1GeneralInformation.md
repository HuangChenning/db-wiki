---
title: Chapter 1 General Information
book: MySQL 5.6 Reference Manual
version: "5.6"
source: "MySQL/MySQL5.6/sources/refman-5.6-en.pdf#page=29"
tags:
  - mysql
  - mysql-5.6
  - reference-manual
---

## Table of Contents

1.1 About This Manual ....................................................................................................................... 2

1.2 Overview of the MySQL Database Management System ................................................................ 4

1.2.1 What is MySQL? ............................................................................................................... 4

1.2.2 The Main Features of MySQL ............................................................................................ 5

1.2.3 History of MySQL .............................................................................................................. 8

1.3 What Is New in MySQL 5.6 .......................................................................................................... 9

1.4 Server and Status Variables and Options Added, Deprecated, or Removed in MySQL 5.6 ............... 22

1.5 How to Report Bugs or Problems ................................................................................................ 37

1.6 MySQL Standards Compliance .................................................................................................... 42

1.6.1 MySQL Extensions to Standard SQL ................................................................................ 43

1.6.2 MySQL Differences from Standard SQL ............................................................................ 46

1.6.3 How MySQL Deals with Constraints ................................................................................. 49

1.7 Credits ....................................................................................................................................... 53

1.7.1 Contributors to MySQL ..................................................................................................... 53

1.7.2 Documenters and translators ............................................................................................ 57

1.7.3 Packages that support MySQL ......................................................................................... 59

1.7.4 Tools that were used to create MySQL ............................................................................. 59

1.7.5 Supporters of MySQL ...................................................................................................... 60 The MySQL software delivers a very fast, multithreaded, multi-user, and robust SQL (Structured Query Language) database server. MySQL Server is intended for mission-critical, heavy-load production systems as well as for embedding into mass-deployed software. Oracle is a registered trademark of Oracle Corporation and/or its affiliates. MySQL is a trademark of Oracle Corporation and/or its affiliates, and shall not be used by Customer without Oracle's express written authorization. Other names may be trademarks of their respective owners.

The MySQL software is Dual Licensed. Users can choose to use the MySQL software as an Open Source product under the terms of the GNU General Public License (http://www.fsf.org/licenses/) or can purchase a standard commercial license from Oracle. See http://www.mysql.com/company/legal/licensing/ for more information on our licensing policies.

The following list describes some sections of particular interest in this manual:

- For a discussion of MySQL Database Server capabilities, see Section 1.2.2, “The Main Features of

MySQL”.

- For an overview of new MySQL features, see Section 1.3, “What Is New in MySQL 5.6”. For information

about the changes in each version, see the Release Notes.

- For installation instructions, see Chapter 2, Installing and Upgrading MySQL. For information about

upgrading MySQL, see Section 2.11, “Upgrading MySQL”.

- For a tutorial introduction to the MySQL Database Server, see Chapter 3, Tutorial.
- For information about configuring and administering MySQL Server, see Chapter 5, MySQL Server

Administration.

- For information about security in MySQL, see Chapter 6, Security.
- For information about setting up replication servers, see Chapter 17, Replication.

About This Manual

- For information about MySQL Enterprise, the commercial MySQL release with advanced features and

management tools, see Chapter 24, MySQL Enterprise Edition.

- For answers to a number of questions that are often asked concerning the MySQL Database Server and

its capabilities, see Appendix A, MySQL 5.6 Frequently Asked Questions.

- For a history of new features and bug fixes, see the Release Notes.

Important To report problems or bugs, please use the instructions at Section 1.5,“How to Report Bugs or Problems”. If you find a security bug in MySQL Server, please let us know immediately by sending an email message to`<secalert_us@oracle.com>`. Exception: Support customers should report all problems, including security bugs, to Oracle Support.

## 1.1 About This Manual

This is the Reference Manual for the MySQL Database System, version 5.6, through release 5.6.51.

Differences between minor versions of MySQL 5.6 are noted in the present text with reference to release numbers (5.6.x). For license information, see the Legal Notices.

This manual is not intended for use with older versions of the MySQL software due to the many functional and other differences between MySQL 5.6 and previous versions. If you are using an earlier release of the MySQL software, please refer to the appropriate manual. For example, MySQL 5.5 Reference Manual covers the 5.5 series of MySQL software releases.

If you are using MySQL 5.7, please refer to the MySQL 5.7 Reference Manual.

Because this manual serves as a reference, it does not provide general instruction on SQL or relational database concepts. It also does not teach you how to use your operating system or command-line interpreter.

The MySQL Database Software is under constant development, and the Reference Manual is updated frequently as well. The most recent version of the manual is available online in searchable form at https://dev.mysql.com/doc/. Other formats also are available there, including downloadable HTML and PDF versions.

If you have questions about using MySQL, join the MySQL Community Slack. If you have suggestions concerning additions or corrections to the manual itself, please send them to the http://www.mysql.com/company/contact/.

> Typographical and Syntax Conventions

This manual uses certain typographical conventions:

- `Text in this style` is used for SQL statements; database, table, and column names; program

listings and source code; and environment variables. Example: “To reload the grant tables, use the`FLUSH PRIVILEGES` statement.”

- `Text in this style` indicates input that you type in examples.
- `Text in this style` indicates the names of executable programs and scripts, examples being

`mysql` (the MySQL command-line client program) and `mysqld` (the MySQL server executable).

- `Text in this style` is used for variable input for which you should substitute a value of your own

choosing.

Typographical and Syntax Conventions

- Text in this style is used for emphasis.
- Text in this style is used in table headings and to convey especially strong emphasis.
- `Text in this style` is used to indicate a program option that affects how the program is executed,

or that supplies information that is needed for the program to function in a certain way. Example: “The `--``host` option (short form `-h`) tells the `mysql` client program the hostname or IP address of the MySQL server that it should connect to”.

- File names and directory names are written like this: “The global `my.cnf` file is located in the `/etc`

directory.”

- Character sequences are written like this: “To specify a wildcard, use the ‘%’ character.”

When commands or statements are prefixed by a prompt, we use these:

```
$> type a command here
#> type a command as root here
C:\> type a command here (Windows only)
mysql> type a mysql statement here
```

Commands are issued in your command interpreter. On Unix, this is typically a program such as `sh`, `csh`,or `bash`. On Windows, the equivalent program is `command.com` or `cmd.exe`, typically run in a console window. Statements prefixed by `mysql` are issued in the `mysql` command-line client.

Note When you enter a command or statement shown in an example, do not type the prompt shown in the example.

In some areas different systems may be distinguished from each other to show that commands should be executed in two different environments. For example, while working with replication the commands might be prefixed with `source` and `replica`:

```
source> type a mysql statement on the replication source here
replica> type a mysql statement on the replica here
```

Database, table, and column names must often be substituted into statements. To indicate that such substitution is necessary, this manual uses `db_name`, `tbl_name`, and `col_name`. For example, you might see a statement like this:

```
mysql> SELECT col_name FROM db_name.tbl_name;
```

This means that if you were to enter a similar statement, you would supply your own database, table, and column names, perhaps like this:

```
mysql> SELECT author_name FROM biblio_db.author_list;
```

SQL keywords are not case-sensitive and may be written in any lettercase. This manual uses uppercase.

In syntax descriptions, square brackets (“[” and “]”) indicate optional words or clauses. For example, in the following statement, `IF EXISTS` is optional:

```
DROP TABLE [IF EXISTS] tbl_name
```

When a syntax element consists of a number of alternatives, the alternatives are separated by vertical bars(“|”). When one member from a set of choices may be chosen, the alternatives are listed within square brackets (“[” and “]”):

```
TRIM([[BOTH | LEADING | TRAILING] [remstr] FROM] str)
```

Manual Authorship When one member from a set of choices must be chosen, the alternatives are listed within braces (“{” and“}”):

```
{DESCRIBE | DESC} tbl_name [col_name | wild]
```

An ellipsis (`...`) indicates the omission of a section of a statement, typically to provide a shorter version of more complex syntax. For example, `SELECT ... INTO OUTFILE` is shorthand for the form of `SELECT`statement that has an `INTO OUTFILE` clause following other parts of the statement.

An ellipsis can also indicate that the preceding syntax element of a statement may be repeated. In the following example, multiple `reset_option` values may be given, with each of those after the first preceded by commas:

```
RESET reset_option [,reset_option] ...
```

Commands for setting shell variables are shown using Bourne shell syntax. For example, the sequence to set the `CC` environment variable and run the `configure` command looks like this in Bourne shell syntax:

```
$> CC=gcc ./configure
```

If you are using `csh` or `tcsh`, you must issue commands somewhat differently:

```
$> setenv CC gcc
$> ./configure
```

> Manual Authorship

The Reference Manual source files are written in DocBook XML format. The HTML version and other formats are produced automatically, primarily using the DocBook XSL stylesheets. For information about DocBook, see http://docbook.org/This manual was originally written by David Axmark and Michael “Monty” Widenius. It is maintained by the MySQL Documentation Team, consisting of Chris Cole, Aijaz Fatima, Edward Gilmore, Stefan Hinz, David Hollis, Philip Olson, Daniel So, and Jon Stephens.

## 1.2 Overview of the MySQL Database Management System

### 1.2.1 What is MySQL?

MySQL, the most popular Open Source SQL database management system, is developed, distributed, and supported by Oracle Corporation.

The MySQL website (http://www.mysql.com/) provides the latest information about MySQL software.

- MySQL is a database management system.

A database is a structured collection of data. It may be anything from a simple shopping list to a picture gallery or the vast amounts of information in a corporate network. To add, access, and process data stored in a computer database, you need a database management system such as MySQL Server.

Since computers are very good at handling large amounts of data, database management systems play a central role in computing, as standalone utilities, or as parts of other applications.

- MySQL databases are relational.

A relational database stores data in separate tables rather than putting all the data in one big storeroom.

The database structures are organized into physical files optimized for speed. The logical model,with objects such as databases, tables, views, rows, and columns, offers a flexible programming environment. You set up rules governing the relationships between different data fields, such as one-to-The Main Features of MySQL one, one-to-many, unique, required or optional, and “pointers” between different tables. The database enforces these rules, so that with a well-designed database, your application never sees inconsistent,duplicate, orphan, out-of-date, or missing data.

The SQL part of “MySQL” stands for “Structured Query Language”. SQL is the most common standardized language used to access databases. Depending on your programming environment, you might enter SQL directly (for example, to generate reports), embed SQL statements into code written in another language, or use a language-specific API that hides the SQL syntax.

SQL is defined by the ANSI/ISO SQL Standard. The SQL standard has been evolving since 1986 and several versions exist. In this manual, “SQL-92” refers to the standard released in 1992, “SQL:1999”refers to the standard released in 1999, and “SQL:2003” refers to the current version of the standard. We use the phrase “the SQL standard” to mean the current version of the SQL Standard at any time.

- MySQL software is Open Source.

Open Source means that it is possible for anyone to use and modify the software. Anybody can download the MySQL software from the Internet and use it without paying anything. If you wish, you may study the source code and change it to suit your needs. The MySQL software uses the GPL (GNU General Public License), http://www.fsf.org/licenses/, to define what you may and may not do with the software in different situations. If you feel uncomfortable with the GPL or need to embed MySQL code into a commercial application, you can buy a commercially licensed version from us. See the MySQL Licensing Overview for more information (http://www.mysql.com/company/legal/licensing/).

- The MySQL Database Server is very fast, reliable, scalable, and easy to use.

If that is what you are looking for, you should give it a try. MySQL Server can run comfortably on a desktop or laptop, alongside your other applications, web servers, and so on, requiring little or no attention. If you dedicate an entire machine to MySQL, you can adjust the settings to take advantage of all the memory, CPU power, and I/O capacity available. MySQL can also scale up to clusters of machines, networked together.

MySQL Server was originally developed to handle large databases much faster than existing solutions and has been successfully used in highly demanding production environments for several years.

Although under constant development, MySQL Server today offers a rich and useful set of functions.

Its connectivity, speed, and security make MySQL Server highly suited for accessing databases on the Internet.

- MySQL Server works in client/server or embedded systems.

The MySQL Database Software is a client/server system that consists of a multithreaded SQL server that supports different back ends, several different client programs and libraries, administrative tools, and a wide range of application programming interfaces (APIs).

We also provide MySQL Server as an embedded multithreaded library that you can link into your application to get a smaller, faster, easier-to-manage standalone product.

- A large amount of contributed MySQL software is available.

MySQL Server has a practical set of features developed in close cooperation with our users. It is very likely that your favorite application or language supports the MySQL Database Server.

The official way to pronounce “MySQL” is “My Ess Que Ell” (not “my sequel”), but we do not mind if you pronounce it as “my sequel” or in some other localized way.

### 1.2.2 The Main Features of MySQL

The Main Features of MySQL This section describes some of the important characteristics of the MySQL Database Software. In most respects, the roadmap applies to all versions of MySQL. For information about features as they are introduced into MySQL on a series-specific basis, see the “In a Nutshell” section of the appropriate Manual:

- MySQL 8.0: What Is New in MySQL 8.0
- MySQL 5.7: What Is New in MySQL 5.7
- MySQL 5.6: Section 1.3, “What Is New in MySQL 5.6”

> Internals and Portability

- Written in C and C++.
- Tested with a broad range of different compilers.
- Works on many different platforms. See https://www.mysql.com/support/supportedplatforms/

database.html.

- For portability, configured using `CMake`.
- Tested with Purify (a commercial memory leakage detector) as well as with Valgrind, a GPL tool (http://

developer.kde.org/~sewardj/).

- Uses multi-layered server design with independent modules.
- Designed to be fully multithreaded using kernel threads, to easily use multiple CPUs if they are available.
- Provides transactional and nontransactional storage engines.
- Uses very fast B-tree disk tables (`MyISAM`) with index compression.
- Designed to make it relatively easy to add other storage engines. This is useful if you want to provide an

SQL interface for an in-house database.

- Uses a very fast thread-based memory allocation system.
- Executes very fast joins using an optimized nested-loop join.
- Implements in-memory hash tables, which are used as temporary tables.
- Implements SQL functions using a highly optimized class library that should be as fast as possible.

Usually there is no memory allocation at all after query initialization.

- Provides the server as a separate program for use in a client/server networked environment.

> Data Types

- Many data types: signed/unsigned integers 1, 2, 3, 4, and 8 bytes long, `FLOAT`, `DOUBLE`, `CHAR`,

```
VARCHAR, BINARY, VARBINARY, TEXT, BLOB, DATE, TIME, DATETIME, TIMESTAMP, YEAR, SET, ENUM,
```

and OpenGIS spatial types. See Chapter 11, Data Types.

- Fixed-length and variable-length string types.

> Statements and Functions

- Full operator and function support in the `SELECT` list and `WHERE` clause of queries. For example:

```
mysql> SELECT CONCAT(first_name, ' ', last_name)
-> FROM citizen
-> WHERE income/dependents > 10000 AND age > 30;
```

The Main Features of MySQL

- Full support for SQL `GROUP BY` and `ORDER BY` clauses. Support for group functions (`COUNT()`, `AVG()`,

```
STD(), SUM(), MAX(), MIN(), and GROUP_CONCAT()).
```

- Support for `LEFT OUTER JOIN` and `RIGHT OUTER JOIN` with both standard SQL and ODBC syntax.
- Support for aliases on tables and columns as required by standard SQL.
- Support for `DELETE`, `INSERT`, `REPLACE`, and `UPDATE` to return the number of rows that were changed

(affected), or to return the number of rows matched instead by setting a flag when connecting to the server.

- Support for MySQL-specific `SHOW` statements that retrieve information about databases, storage

engines, tables, and indexes. Support for the `INFORMATION_SCHEMA` database, implemented according to standard SQL.

- An `EXPLAIN` statement to show how the optimizer resolves a query.
- Independence of function names from table or column names. For example, `ABS` is a valid column name.

The only restriction is that for a function call, no spaces are permitted between the function name and the “(” that follows it. See Section 9.3, “Keywords and Reserved Words”.

- You can refer to tables from different databases in the same statement.

> Security

- A privilege and password system that is very flexible and secure, and that enables host-based

verification.

- Password security by encryption of all password traffic when you connect to a server.

> Scalability and Limits

- Support for large databases. We use MySQL Server with databases that contain 50 million records. We

also know of users who use MySQL Server with 200,000 tables and about 5,000,000,000 rows.

- Support for up to 64 indexes per table. Each index may consist of 1 to 16 columns or parts of columns.

The maximum index width for `InnoDB` tables is either 767 bytes or 3072 bytes. See Section 14.22,“InnoDB Limits”. The maximum index width for `MyISAM` tables is 1000 bytes. See Section 15.2, “The MyISAM Storage Engine”. An index may use a prefix of a column for `CHAR`, `VARCHAR`, `BLOB`, or `TEXT`column types.

> Connectivity

- Clients can connect to MySQL Server using several protocols:
- Clients can connect using TCP/IP sockets on any platform.
- On Windows systems, clients can connect using named pipes if the server is started with the

`named_pipe` system variable enabled. Windows servers also support shared-memory connections if started with the `shared_memory` system variable enabled. Clients can connect through shared memory by using the `--protocol=memory` option.

- On Unix systems, clients can connect using Unix domain socket files.
- MySQL client programs can be written in many languages. A client library written in C is available for

clients written in C or C++, or for any language that provides C bindings.

- APIs for C, C++, Eiffel, Java, Perl, PHP, Python, Ruby, and Tcl are available, enabling MySQL clients to

be written in many languages. See Chapter 23, Connectors and APIs.

History of MySQL

- The Connector/ODBC (MyODBC) interface provides MySQL support for client programs that use ODBC

(Open Database Connectivity) connections. For example, you can use MS Access to connect to your MySQL server. Clients can be run on Windows or Unix. Connector/ODBC source is available. All ODBC

2.5 functions are supported, as are many others. See MySQL Connector/ODBC Developer Guide.

- The Connector/J interface provides MySQL support for Java client programs that use JDBC connections.

Clients can be run on Windows or Unix. Connector/J source is available. See MySQL Connector/J 8.0 Developer Guide.

- MySQL Connector/NET enables developers to easily create .NET applications that require secure,

high-performance data connectivity with MySQL. It implements the required ADO.NET interfaces and integrates into ADO.NET aware tools. Developers can build applications using their choice of .NET languages. MySQL Connector/NET is a fully managed ADO.NET driver written in 100% pure C#. See MySQL Connector/NET Developer Guide.

> Localization

- The server can provide error messages to clients in many languages. See Section 10.12, “Setting the

Error Message Language”.

- Full support for several different character sets, including `latin1` (cp1252), `german`, `big5`, `ujis`,

several Unicode character sets, and more. For example, the Scandinavian characters “å”, “ä” and “ö” are permitted in table and column names.

- All data is saved in the chosen character set.
- Sorting and comparisons are done according to the default character set and collation. is possible

to change this when the MySQL server is started (see Section 10.3.2, “Server Character Set and Collation”). To see an example of very advanced sorting, look at the Czech sorting code. MySQL Server supports many different character sets that can be specified at compile time and runtime.

- The server time zone can be changed dynamically, and individual clients can specify their own time

zone. See Section 5.1.13, “MySQL Server Time Zone Support”.

> Clients and Tools

- MySQL includes several client and utility programs. These include both command-line programs such as

`mysqldump` and `mysqladmin`, and graphical programs such as MySQL Workbench.

- MySQL Server has built-in support for SQL statements to check, optimize, and repair tables. These

statements are available from the command line through the `mysqlcheck` client. MySQL also includes`myisamchk`, a very fast command-line utility for performing these operations on `MyISAM` tables. See Chapter 4, MySQL Programs.

- MySQL programs can be invoked with the `--help` or `-?` option to obtain online assistance.

### 1.2.3 History of MySQL

We started out with the intention of using the `mSQL` database system to connect to our tables using our own fast low-level (ISAM) routines. However, after some testing, we came to the conclusion that `mSQL` was not fast enough or flexible enough for our needs. This resulted in a new SQL interface to our database but with almost the same API interface as `mSQL`. This API was designed to enable third-party code that was written for use with `mSQL` to be ported easily for use with MySQL.

MySQL is named after co-founder Monty Widenius's daughter, My.

The name of the MySQL Dolphin (our logo) is “Sakila,” which was chosen from a huge list of names suggested by users in our “Name the Dolphin” contest. The winning name was submitted by Ambrose What Is New in MySQL 5.6 Twebaze, an Open Source software developer from Eswatini (formerly Swaziland), Africa. According to Ambrose, the feminine name Sakila has its roots in SiSwati, the local language of Eswatini. Sakila is also the name of a town in Arusha, Tanzania, near Ambrose's country of origin, Uganda.

## 1.3 What Is New in MySQL 5.6

This section summarizes what has been added to, deprecated in, and removed from MySQL 5.6. A companion section lists MySQL server options and variables that have been added, deprecated, or removed in MySQL 5.6; see Section 1.4, “Server and Status Variables and Options Added, Deprecated, or Removed in MySQL 5.6”.

- Features Added in MySQL 5.6
- Features Deprecated in MySQL 5.6
- Features Removed in MySQL 5.6

> Features Added in MySQL 5.6

The following features have been added to MySQL 5.6:

- Security improvements. These security improvements were made:
- MySQL now provides a method for storing authentication credentials encrypted in an option file named

`.mylogin.cnf`. To create the file, use the `mysql_config_editor` utility. The file can be read later by MySQL client programs to obtain authentication credentials for connecting to a MySQL server.

`mysql_config_editor` writes the `.mylogin.cnf` file using encryption so the credentials are not stored as clear text, and its contents when decrypted by client programs are used only in memory.

In this way, passwords can be stored in a file in non-cleartext format and used later without ever needing to be exposed on the command line or in an environment variable. For more information, see Section 4.6.6, “mysql_config_editor — MySQL Configuration Utility”.

- MySQL now supports stronger encryption for user account passwords, available through an

authentication plugin named `sha256_password` that implements SHA-256 password hashing. This plugin is built in, so it is always available and need not be loaded explicitly. For more information,including instructions for creating accounts that use SHA-256 passwords, see Section 6.4.1.4,“SHA-256 Pluggable Authentication”.

- The `mysql.user` system table now has a `password_expired` column. Its default value is `'N'`,

but can be set to `'Y'` with the new `ALTER USER` statement. After an account's password has been expired, all operations performed in subsequent connections to the server using the account result in an error until the user issues a `SET PASSWORD` statement to establish a new account password.

For more information, see Section 13.7.1.1, “ALTER USER Statement”, and Section 6.2.10, “Server Handling of Expired Passwords”.

- MySQL now has provision for checking password security:
- In statements that assign a password supplied as a cleartext value, the value is checked

against the current password policy and rejected if it is weak (the statement returns an`ER_NOT_VALID_PASSWORD` error). This affects the `CREATE USER`, `GRANT`, and `SET PASSWORD`statements. Passwords given as arguments to the `PASSWORD()` and `OLD_PASSWORD()` functions are checked as well.

- The strength of potential passwords can be assessed using the new

`VALIDATE_PASSWORD_STRENGTH()` SQL function, which takes a password argument and returns an integer from 0 (weak) to 100 (strong).

Features Added in MySQL 5.6 Both capabilities are implemented by the `validate_password` plugin. For more information, see Section 6.4.3, “The Password Validation Plugin”.

- `mysql_upgrade` now produces a warning if it finds user accounts with passwords hashed with

the older pre-4.1 hashing method. Such accounts should be updated to use more secure password hashing. See Section 6.1.2.4, “Password Hashing in MySQL”

- On Unix platforms, `mysql_install_db` supports a new option, `--random-passwords`, that

provides for more secure MySQL installation. Invoking `mysql_install_db` with `--random-``passwords` causes it to assign a random password to the MySQL `root` accounts, set the “password expired” flag for those accounts, and remove the anonymous-user MySQL accounts. For additional details, see Section 4.4.3, “mysql_install_db — Initialize MySQL Data Directory”.

- Logging has been modified so that passwords do not appear in plain text in statements written to the

general query log, slow query log, and binary log. See Section 6.1.2.3, “Passwords and Logging”.

The `mysql` client no longer logs to its history file statements that refer to passwords. See Section 4.5.1.3, “mysql Client Logging”.

- `START SLAVE` syntax has been modified to permit connection parameters to be specified for

connecting to the source. This provides an alternative to storing the password in the `master.info`file. See Section 13.4.2.5, “START SLAVE Statement”.

- MySQL now sets the access control granted to clients on the named pipe to the minimum necessary

for successful communication on Windows. Newer MySQL client software can open named pipe connections without any additional configuration. If older client software cannot be upgraded immediately, the new `named_pipe_full_access_group` system variable can be used to give a Windows group the necessary permissions to open a named pipe connection. Membership in the full-access group should be restricted and temporary.

- MySQL Enterprise. The format of the file generated by the audit log plugin was changed for better

compatibility with Oracle Audit Vault. See Section 6.4.4, “MySQL Enterprise Audit”, and Section 6.4.4.3,“Audit Log File Formats”.

The audit log plugin included in MySQL Enterprise Edition now has the capability of filtering audited events based on user account and event status. Several new system variables provide DBAs with filtering control. In addition, audit log plugin reporting capability has been improved by the addition Features Added in MySQL 5.6 of several status variables. For more information, see Section 6.4.4.4, “Configuring Audit Logging Characteristics”, and Audit Log Plugin Status Variables.

MySQL Enterprise Edition now includes a set of encryption functions based on the OpenSSL library that expose OpenSSL capabilities at the SQL level. These functions enable Enterprise applications to perform the following operations:

- Implement added data protection using public-key asymmetric cryptography
- Create public and private keys and digital signatures
- Perform asymmetric encryption and decryption
- Use cryptographic hashing for digital signing and data verification and validation

For more information, see Section 6.5, “MySQL Enterprise Encryption”.

MySQL Enterprise Edition now includes MySQL Enterprise Firewall, an application-level firewall that enables database administrators to permit or deny SQL statement execution based on matching against allowlists of accepted statement patterns. This helps harden MySQL Server against attacks such as SQL injection or attempts to exploit applications by using them outside of their legitimate query workload characteristics. For more information, see Section 6.4.5, “MySQL Enterprise Firewall”.

- Changes to server defaults. Beginning with MySQL 5.6.6, several MySQL Server parameter

defaults differ from the defaults in previous releases. The motivation for these changes is to provide better out-of-box performance and to reduce the need for database administrators to change settings manually. For more information, see Section 5.1.2.1, “Changes to Server Defaults”.

- InnoDB enhancements. These `InnoDB` enhancements were added:
- You can create `FULLTEXT` indexes on `InnoDB` tables, and query them using the `MATCH() ...`

`AGAINST` syntax. This feature includes a new proximity search operator (@) and several new configuration options and `INFORMATION_SCHEMA` tables: See Section 14.6.2.3, “InnoDB Full-Text Indexes” for more information.

- Several `ALTER TABLE` operations can be performed without copying the table, without blocking

inserts, updates, and deletes to the table, or both. These enhancements are known collectively as online DDL. See Section 14.13, “InnoDB and Online DDL” for details.

- `InnoDB` now supports the `DATA DIRECTORY='directory'` clause of the `CREATE TABLE`

statement, which permits creating tables outside of the data directory. This enhancement provides the flexibility to createtables in locations that better suit your server environment. For example, you can place busy tables on an SSD device, or large tables on a high-capacity HDD device.

For more information, see Section 14.6.1.2, “Creating Tables Externally”.

- `InnoDB` now supports the notion of “transportable tablespaces”, allowing file-per-table tablespaces

(`.ibd` files) to be exported from a running MySQL instance and imported into another running instance without inconsistencies or mismatches caused by buffered data, in-progress transactions,and internal bookkeeping details such as the space ID and LSN.

The `FOR EXPORT` clause of the `FLUSH TABLE` command writes any unsaved changes from `InnoDB`memory buffers to the `.ibd` file. After copying the `.ibd` file and a separate metadata file to the Features Added in MySQL 5.6 other server, the `DISCARD TABLESPACE` and `IMPORT TABLESPACE` clauses of the `ALTER TABLE`statement are used to bring the table data into a different MySQL instance.

This enhancement provides the flexibility to move tables that reside in file-per-table tablespaces around to better suit your server environment. For example, you could move busy tables to an SSD device, or move large tables to a high-capacity HDD device. For more information, see Section 14.6.1.3, “Importing InnoDB Tables”.

- You can now set the `InnoDB` page size for uncompressed tables to 8KB or 4KB, as an alternative

to the default 16KB. This setting is controlled by the `innodb_page_size` configuration option. You specify the size when creating the MySQL instance. All `InnoDB` tablespaces within an instance share the same page size. Smaller page sizes can help to avoid redundant or inefficient I/O for certain combinations of workload and storage devices, particularly SSD devices with small block sizes.

- Improvements to the algorithms for adaptive flushing make I/O operations more efficient and

consistent under a variety of workloads. The new algorithm and default configuration values are expected to improve performance and concurrency for most users. Advanced users can fine-tune their I/O responsiveness through several configuration options. See Section 14.8.3.4, “Configuring Buffer Pool Flushing” for details.

- You can code MySQL applications that access `InnoDB` tables through a NoSQL-style API. This

feature uses the popular `memcached` daemon to relay requests such as `ADD`, `SET`, and `GET` for key-value pairs. These simple operations to store and retrieve data avoid the SQL overhead such as parsing and constructing a query execution plan. You can access the same data through the NoSQL API and SQL. For example, you might use the NoSQL API for fast updates and lookups, and SQL for complex queries and compatibility with existing applications. See Section 14.20, “InnoDB memcached Plugin” for details.

- Optimizer statistics for `InnoDB` tables are gathered at more predictable intervals and can persist

across server restarts, for improved plan stability. You can also control the amount of sampling done for `InnoDB` indexes, to make the optimizer statistics more accurate and improve the query execution plan. See Section 14.8.11.1, “Configuring Persistent Optimizer Statistics Parameters” for details.

- New optimizations apply to read-only transactions, improving performance and concurrency for ad-

hoc queries and report-generating applications. These optimizations are applied automatically when practical, or you can specify `START TRANSACTION READ ONLY` to ensure the transaction is read-only. See Section 8.5.3, “Optimizing InnoDB Read-Only Transactions” for details.

- You can move the `InnoDB` undo log out of the system tablespace into one or more separate

tablespaces. The I/O patterns for the undo log make these new tablespaces good candidates to move to SSD storage, while keeping the system tablespace on hard disk storage. For details, see Section 14.6.3.3, “Undo Tablespaces”.

- You can improve the efficiency of the `InnoDB` checksum feature by specifying the configuration option

`innodb_checksum_algorithm=crc32`, which turns on a faster checksum algorithm. This option replaces the `innodb_checksums` option. Data written using the old checksum algorithm (option value `innodb`) is fully upward-compatible; tablespaces modified using the new checksum algorithm(option value `crc32`) cannot be downgraded to an earlier version of MySQL that does not support the

```
innodb_checksum_algorithm option.
```

- The `InnoDB` redo log files now have a maximum combined size of 512GB, increased from 4GB. You

can specify the larger values through the `innodb_log_file_size` option. The startup behavior now automatically handles the situation where the size of the existing redo log files does not match the size specified by `innodb_log_file_size` and `innodb_log_files_in_group`.

Features Added in MySQL 5.6

- The `--innodb-read-only` option lets you run a MySQL server in read-only mode. You can access

`InnoDB` tables on read-only media such as a DVD or CD, or set up a data warehouse with multiple instances all sharing the same data directory. See Section 14.8.2, “Configuring InnoDB for Read-Only Operation” for usage details.

- A new configuration option, `innodb_compression_level`, allows you to select a compression

level for `InnoDB` compressed tables, from the familiar range of 0-9 used by `zlib`. You can also control whether compressed pages in the buffer pool are stored in the redo log when an update operation causes pages to be compressed again. This behavior is controlled by the`innodb_log_compressed_pages` configuration option.

- Data blocks in an `InnoDB` compressed table contain a certain amount of empty space (padding)

to allow DML operations to modify the row data without re-compressing the new values. Too much padding can increase the chance of a compression failure, requiring a page split, when the data does need to be re-compressed after extensive changes. The amount of padding can now be adjusted dynamically, so that DBAs can reduce the rate of compression failures without re-creating the entire table with new parameters, or re-creating the entire instance with a different page size. The associated new configuration options are `innodb_compression_failure_threshold_pct`,

```
innodb_compression_pad_pct_max.
```

- Several new `InnoDB`-related `INFORMATION_SCHEMA` tables provide information about the `InnoDB`

buffer pool, metadata about tables, indexes, and foreign keys from the `InnoDB` data dictionary,and low-level information about performance metrics that complements the information from the Performance Schema tables.

- To ease the memory load on systems with huge numbers of tables, `InnoDB` now frees up the memory

associated with an opened table using an LRU algorithm to select tables that have gone the longest without being accessed. To reserve more memory to hold metadata for open `InnoDB` tables, increase the value of the `table_definition_cache` configuration option. `InnoDB` treats this value as a“soft limit” for the number of open table instances in the `InnoDB` data dictionary cache. For additional information, refer to the `table_definition_cache` documentation.

- `InnoDB` has several internal performance enhancements, including reducing contention by splitting

the kernel mutex, moving flushing operations from the main thread to a separate thread, enabling multiple purge threads, and reducing contention for the buffer pool on large-memory systems.

- `InnoDB` uses a new, faster algorithm to detect deadlocks. Information about all `InnoDB` deadlocks

can be written to the MySQL server error log, to help diagnose application issues.

- To avoid a lengthy warmup period after restarting the server, particularly for instances with large

`InnoDB` buffer pools, you can reload pages into the buffer pool immediately after a restart. MySQL can dump a compact data file at shutdown, then consult that data file to find the pages to reload on the next restart. You can also manually dump or reload the buffer pool at any time, for example during benchmarking or after complex report-generation queries. See Section 14.8.3.5, “Saving and Restoring the Buffer Pool State” for details.

- As of MySQL 5.6.16, `innochecksum` provides support for files greater than 2GB in size. Previously,

`innochecksum` only supported files up to 2GB in size.

- As of MySQL 5.6.16, new global configuration parameters, `innodb_status_output` and

`innodb_status_output_locks`, allow you to dynamically enable and disable the standard `InnoDB`Monitor and `InnoDB` Lock Monitor for periodic output. Enabling and disabling monitors for periodic output by creating and dropping specially named tables is deprecated and may be removed in a future release. For additional information, see Section 14.17, “InnoDB Monitors”.

Features Added in MySQL 5.6

- As of MySQL 5.6.17, Online DDL support is extended to the following operations for regular and

partitioned `InnoDB` tables:

```
- OPTIMIZE TABLE
- ALTER TABLE ... FORCE
```

- `ALTER TABLE ... ENGINE=INNODB` (when run on an `InnoDB` table)

Online DDL support reduces table rebuild time and permits concurrent DML. See Section 14.13,“InnoDB and Online DDL”.

- As of MySQL 5.6.42, the zlib library version bundled with MySQL was raised from version 1.2.3 to

version 1.2.11. MySQL implements compression with the help of the zlib library.

If you use `InnoDB` compressed tables, see Section 2.11.3, “Changes in MySQL 5.6” for related upgrade implications.

- Partitioning. These table-partitioning enhancements were added:
- The maximum number of partitions is increased to 8192. This number includes all partitions and all

subpartitions of the table.

- It is now possible to exchange a partition of a partitioned table or a subpartition of a subpartitioned

table with a nonpartitioned table that otherwise has the same structure using the `ALTER TABLE ...``EXCHANGE PARTITION` statement. This can be used, for example, to import and export partitions. For more information and examples, see Section 19.3.3, “Exchanging Partitions and Subpartitions with Tables”.

- Explicit selection of one or more partitions or subpartitions is now supported for queries, as well as

for many data modification statements, that act on partitioned tables. For example, assume a table t with some integer column c has 4 partitions named `p0`, `p1`, `p2`, and `p3`. Then the query `SELECT *``FROM t PARTITION (p0, p1) WHERE c < 5` returns only those rows from partitions `p0` and `p1`for which c is less than 5.

The following statements support explicit partition selection:

```
- SELECT
- DELETE
- INSERT
- REPLACE
- UPDATE
- LOAD DATA.
- LOAD XML.
```

For syntax, see the descriptions of the individual statements. For additional information and examples,see Section 19.5, “Partition Selection”.

- Partition lock pruning greatly improves performance of many DML and DDL statements acting on

tables with many partitions by helping to eliminate locks on partitions that are not affected by these Features Added in MySQL 5.6 statements. Such statements include many `SELECT`, `SELECT ... PARTITION`, `UPDATE`, `REPLACE`,`INSERT`, as well as many other statements. For more information, including a complete listing of the statements whose performance has thus been improved, see Section 19.6.4, “Partitioning and Locking”.

- Performance Schema. The Performance Schema includes several new features:
- Instrumentation for table input and output. Instrumented operations include row-level accesses to

persistent base tables or temporary tables. Operations that affect rows are fetch, insert, update, and delete.

- Event filtering by table, based on schema and/or table names.
- Event filtering by thread. More information is collected for threads.
- Summary tables for table and index I/O, and for table locks.
- Instrumentation for statements and stages within statements.
- Configuration of instruments and consumers at server startup, which previously was possible only at

runtime.

- MySQL NDB Cluster. MySQL NDB Cluster is released as a separate product; the most recent GA

releases are based on MySQL 5.6 and use version 7.3 of the `NDB` storage engine. Clustering support is not available in mainline MySQL Server 5.6 releases. For more information about MySQL NDB Cluster

7.3, see Chapter 18, MySQL NDB Cluster 7.3 and NDB Cluster 7.4. The latest current development version is MySQL NDB Cluster 7.4, based on version 7.4 of the `NDB` storage engine and MySQL Server

5.6. MySQL NDB Cluster 7.4 is currently available for testing and evaluation. The most recent MySQL NDB Cluster 7.4 release can be obtained from https://dev.mysql.com/downloads/cluster/.

For more information and an overview of improvements made in MySQL NDB Cluster 7.4, see Section 18.2.4.2, “What is New in NDB Cluster 7.4”.

MySQL NDB Cluster 7.2, the previous GA release, is based on MySQL Server 5.5, although we recommend that new deployments use MySQL NDB Cluster 7.3.

- Replication and logging. These replication enhancements were added:
- MySQL now supports transaction-based replication using global transaction identifiers (also known

as “GTIDs”). This makes it possible to identify and track each transaction when it is committed on the originating server and as it is applied by any replicas.

Enabling of GTIDs in a replication setup is done primarily using the new `gtid_mode` and`enforce_gtid_consistency` system variables. For information about additional options and variables introduced in support of GTIDs, see Section 17.1.4.5, “Global Transaction ID Options and Variables”.

When using GTIDs it is not necessary to refer to log files or positions within those files when starting a new replica or failing over to a new source, which greatly simplifies these tasks. For more information Features Added in MySQL 5.6 about provisioning servers for GTID replication with or without referring to binary log files, see Section 17.1.3.3, “Using GTIDs for Failover and Scaleout”.

GTID-based replication is completely transaction-based, which makes it simple to check the consistency of sources and replicas. If all transactions committed on a given source are also committed on a given replica, consistency between the two servers is guaranteed.

For more complete information about the implementation and use of GTIDs in MySQL Replication, see Section 17.1.3, “Replication with Global Transaction Identifiers”.

- MySQL row-based replication now supports row image control. By logging only those columns

required for uniquely identifying and executing changes on each row (as opposed to all columns) for each row change, it is possible to save disk space, network resources, and memory usage. You can determine whether full or minimal rows are logged by setting the `binlog_row_image` server system variable to one of the values `minimal` (log required columns only), `full` (log all columns), or `noblob`(log all columns except for unneeded `BLOB` or `TEXT` columns). See System Variables Used with Binary Logging, for more information.

- Binary logs written and read by the MySQL Server are now crash-safe, because only complete events

(or transactions) are logged or read back. By default, the server logs the length of the event as well as the event itself and uses this information to verify that the event was written correctly. You can also cause the server to write checksums for the events using CRC32 checksums by setting the`binlog_checksum` system variable. To cause the server to read checksums from the binary log, use the `master_verify_checksum` system variable. The `--slave-sql-verify-checksum` system variable causes the replica SQL thread to read checksums from the relay log.

- MySQL now supports logging of source connection information and of replica relay log

information to tables as well as files. Use of these tables can be controlled independently, by the`master_info_repository` and `relay_log_info_repository` system variable system variables. Setting `master_info_repository` to `TABLE` causes connection information logging to the `slave_master_info` table. Setting `relay_log_info_repository` to `TABLE` causes relay log information logging to the `slave_relay_log_info` table. Both tables are created automatically in the `mysql` system database.

In order for replication to be resilient to unexpected halts, the `slave_master_info` and`slave_relay_log_info` tables must each use a transactional storage engine, and beginning with MySQL 5.6.6, these tables are created using `InnoDB` for this reason. (Bug #13538891) If you are using a previous MySQL 5.6 release in which both of these tables use `MyISAM`, this means that,prior to starting replication, you must convert both of them to a transactional storage engine (such as`InnoDB`) if you wish for replication to be resilient to unexpected halts. You can do this in such cases by means of the appropriate `ALTER TABLE ... ENGINE=...` statements. You should not attempt to change the storage engine used by either of these tables while replication is actually running.

See Section 17.3.2, “Handling an Unexpected Halt of a Replica Server”, for more information.

- `mysqlbinlog` now has the capability to back up a binary log in its original binary format. When

invoked with the `--read-from-remote-server` and `--raw` options, `mysqlbinlog` connects to a server, requests the log files, and writes output files in the same format as the originals. See Section 4.6.8.3, “Using mysqlbinlog to Back Up Binary Log Files”.

Features Added in MySQL 5.6

- MySQL now supports delayed replication such that a replica server deliberately lags behind the source

by at least a specified amount of time. The default delay is 0 seconds. Use the new `MASTER_DELAY`option for `CHANGE MASTER TO` to set the delay.

Delayed replication can be used for purposes such as protecting against user mistakes on the source(a DBA can roll back a delayed replica to the time just before the disaster) or testing how the system behaves when there is a lag. See Section 17.3.10, “Delayed Replication”.

- A replica having multiple network interfaces can now be caused to use only one of these (to the

exclusion of the others) by using the `MASTER_BIND` option when issuing a `CHANGE MASTER TO`statement.

- The `log_bin_basename` system variable has been added. This variable contains the complete

filename and path to the binary log file. Whereas the `log_bin` system variable shows only whether or not binary logging is enabled, `log_bin_basename` reflects the name set with the `--log-bin` server option.

Similarly, the `relay_log_basename` system variable shows the filename and complete path to the relay log file.

- MySQL Replication now supports parallel execution of transactions with multithreading on the replica.

When parallel execution is enabled, the replica SQL thread acts as the coordinator for a number of replica worker threads as determined by the value of the `slave_parallel_workers` server system variable. The current implementation of multithreading on the replica assumes that data and updates are partitioned on a per-database basis, and that updates within a given database occur in the same relative order as they do on the source. However, it is not necessary to coordinate transactions between different databases. Transactions can then also be distributed per database, which means that a worker thread on the replica can process successive transactions on a given database without waiting for updates to other databases to complete.

Since transactions on different databases can occur in a different order on the replica than on the source, simply checking for the most recently executed transaction is not a guarantee that all previous transactions on the source have been executed on the replica. This has implications for logging and recovery when using a multithreaded replica. For information about how to interpret binary logging information when using multithreading on the replica, see Section 13.7.5.35, “SHOW SLAVE STATUS Statement”.

- Optimizer enhancements. These query optimizer improvements were implemented:
- The optimizer now more efficiently handles queries (and subqueries) of the following form:

```
SELECT ... FROM single_table ... ORDER BY non_index_column [DESC] LIMIT [M,]N;
```

That type of query is common in web applications that display only a few rows from a larger result set.

For example:

```
SELECT col1, ... FROM t1 ... ORDER BY name LIMIT 10;
SELECT col1, ... FROM t1 ... ORDER BY RAND() LIMIT 15;
```

The sort buffer has a size of `sort_buffer_size`. If the sort elements for N rows are small enough to fit in the sort buffer (M+N rows if M was specified), the server can avoid using a merge file and perform the sort entirely in memory. For details, see Section 8.2.1.16, “LIMIT Query Optimization”.

- The optimizer implements Disk-Sweep Multi-Range Read. Reading rows using a range scan on

a secondary index can result in many random disk accesses to the base table when the table is large and not stored in the storage engine's cache. With the Disk-Sweep Multi-Range Read (MRR)Features Added in MySQL 5.6 optimization, MySQL tries to reduce the number of random disk access for range scans by first scanning the index only and collecting the keys for the relevant rows. Then the keys are sorted and finally the rows are retrieved from the base table using the order of the primary key. The motivation for Disk-sweep MRR is to reduce the number of random disk accesses and instead achieve a more sequential scan of the base table data. For more information, see Section 8.2.1.10, “Multi-Range Read Optimization”.

- The optimizer implements Index Condition Pushdown (ICP), an optimization for the case where

MySQL retrieves rows from a table using an index. Without ICP, the storage engine traverses the index to locate rows in the base table and returns them to the MySQL server which evaluates the`WHERE` condition for the rows. With ICP enabled, and if parts of the `WHERE` condition can be evaluated by using only fields from the index, the MySQL server pushes this part of the `WHERE` condition down to the storage engine. The storage engine then evaluates the pushed index condition by using the index entry and only if this is satisfied is base row be read. ICP can reduce the number of accesses the storage engine has to do against the base table and the number of accesses the MySQL server has to do against the storage engine. For more information, see Section 8.2.1.5, “Index Condition Pushdown Optimization”.

- The `EXPLAIN` statement now provides execution plan information for `DELETE`, `INSERT`, `REPLACE`,

and `UPDATE` statements. Previously, `EXPLAIN` provided information only for `SELECT` statements.

In addition, the `EXPLAIN` statement now can produce output in JSON format. See Section 13.8.2,“EXPLAIN Statement”.

- The optimizer more efficiently handles subqueries in the `FROM` clause (that is, derived tables).

Materialization of subqueries in the `FROM` clause is postponed until their contents are needed during query execution, which improves performance. In addition, during query execution, the optimizer may add an index to a derived table to speed up row retrieval from it. For more information, see Section 8.2.2.4, “Optimizing Derived Tables”.

- The optimizer uses semijoin and materialization strategies to optimize subquery execution. See

Section 8.2.2.1, “Optimizing Subqueries with Semijoin Transformations”, and Section 8.2.2.2,“Optimizing Subqueries with Materialization”.

- A Batched Key Access (BKA) join algorithm is now available that uses both index access to the joined

table and a join buffer. The BKA algorithm supports inner join, outer join, and semijoin operations,including nested outer joins and nested semijoins. Benefits of BKA include improved join performance due to more efficient table scanning. For more information, see Section 8.2.1.11, “Block Nested-Loop and Batched Key Access Joins”.

- The optimizer now has a tracing capability, primarily for use by developers. The interface is

provided by a set of `optimizer_trace_xxx` system variables and the Information Schema`OPTIMIZER_TRACE` table. For details, see MySQL Internals: Tracing the Optimizer.

- Condition handling. MySQL now supports the `GET DIAGNOSTICS` statement. `GET DIAGNOSTICS`

provides applications a standardized way to obtain information from the diagnostics area, such as Features Added in MySQL 5.6 whether the previous SQL statement produced an exception and what it was. For more information, see Section 13.6.7.3, “GET DIAGNOSTICS Statement”.

In addition, several deficiencies in condition handler processing rules were corrected so that MySQL behavior is more like standard SQL:

- Block scope is used in determining which handler to select. Previously, a stored program was treated

as having a single scope for handler selection.

- Condition precedence is more accurately resolved.
- Diagnostics area clearing has changed. Bug #55843 caused handled conditions to be cleared from

the diagnostics area before activating the handler. This made condition information unavailable within the handler. Now condition information is available to the handler, which can inspect it with the `GET``DIAGNOSTICS` statement. The condition information is cleared when the handler exits, if it has not already been cleared during handler execution.

- Previously, handlers were activated as soon as a condition occurred. Now they are not activated until

the statement in which the condition occurred finishes execution, at which point the most appropriate handler is chosen. This can make a difference for statements that raise multiple conditions, if a condition raised later during statement execution has higher precedence than an earlier condition and there are handlers in the same scope for both conditions. Previously, the handler for the first condition raised would be chosen, even if it had a lower precedence than other handlers. Now the handler for the condition with highest precedence is chosen, even if it is not the first condition raised by the statement.

For more information, see Section 13.6.7.6, “Scope Rules for Handlers”.

- Data types. These data type changes have been implemented:
- MySQL now permits fractional seconds for `TIME`, `DATETIME`, and `TIMESTAMP` values, with up to

microseconds (6 digits) precision. See Section 11.2.7, “Fractional Seconds in Time Values”.

- Previously, at most one `TIMESTAMP` column per table could be automatically initialized or updated

to the current date and time. This restriction has been lifted. Any `TIMESTAMP` column definition can have any combination of `DEFAULT CURRENT_TIMESTAMP` and `ON UPDATE CURRENT_TIMESTAMP`clauses. In addition, these clauses now can be used with `DATETIME` column definitions. For more information, see Section 11.2.6, “Automatic Initialization and Updating for TIMESTAMP and DATETIME”.

- In MySQL, the `TIMESTAMP` data type differs in nonstandard ways from other data types in

terms of default value and assignment of automatic initialization and update attributes. These behaviors remain the default but now are deprecated, and can be turned off by enabling the`explicit_defaults_for_timestamp` system variable at server startup. See Section 11.2.6,“Automatic Initialization and Updating for TIMESTAMP and DATETIME”, and Section 5.1.7, “Server System Variables”.

- Host cache. MySQL now provides more information about the causes of errors that occur when

clients connect to the server, as well as improved access to the host cache, which contains client IP Features Deprecated in MySQL 5.6 address and host name information and is used to avoid DNS lookups. These changes have been implemented:

- New `Connection_errors_xxx` status variables provide information about connection errors that do

not apply to specific client IP addresses.

- Counters have been added to the host cache to track errors that do apply to specific IP addresses,

and a new `host_cache` Performance Schema table exposes the contents of the host cache so that it can be examined using `SELECT` statements. Access to host cache contents makes it possible to answer questions such as how many hosts are cached, what kinds of connection errors are occurring for which hosts, or how close host error counts are to reaching the `max_connect_errors` system variable limit.

- The host cache size now is configurable using the `host_cache_size` system variable.

For more information, see Section 5.1.11.2, “DNS Lookups and the Host Cache”, and Section 22.12.10.1, “The host_cache Table”.

- OpenGIS. The OpenGIS specification defines functions that test the relationship between two

geometry values. MySQL originally implemented these functions such that they used object bounding rectangles and returned the same result as the corresponding MBR-based functions. Corresponding versions are now available that use precise object shapes. These versions are named with an `ST_`prefix. For example, `Contains()` uses object bounding rectangles, whereas `ST_Contains()` uses object shapes. For more information, see Section 12.17.9, “Functions That Test Spatial Relations Between Geometry Objects”.

> Features Deprecated in MySQL 5.6

The following features are deprecated in MySQL 5.6; you should expect them to be removed in a future series. Where alternatives are shown, applications should be updated to use them.

For applications that use features deprecated in MySQL 5.6 that have been removed in a higher MySQL series, statements may fail when replicated from a MySQL 5.6 source to a higher-series replica, or may have different effects on source and replica. To avoid such problems, applications that use features deprecated in 5.6 should be revised to avoid them and use alternatives when possible.

- The `ERROR_FOR_DIVISION_BY_ZERO`, `NO_ZERO_DATE`, and `NO_ZERO_IN_DATE` SQL modes are

deprecated and setting the `sql_mode` value to include any of them generates a warning. In MySQL

5.7, these modes do nothing. Instead, their effects are included in the effects of strict SQL mode(`STRICT_ALL_TABLES` or `STRICT_TRANS_TABLES`). The motivation for the change in MySQL 5.7 is to reduce the number of SQL modes with an effect dependent on strict mode and make them part of strict mode itself.

To make advance preparation for an upgrade to MySQL 5.7, see SQL Mode Changes in MySQL 5.7.

That discussion provides guidelines to assess whether your applications are affected by the SQL mode changes in MySQL 5.7.

- Relying on implicit `GROUP BY` sorting in MySQL 5.6 is deprecated. To achieve a specific sort order of

grouped results, it is preferable to use an explicit `ORDER BY` clause. `GROUP BY` sorting is a MySQL extension that may change in a future release; for example, to make it possible for the optimizer to order groupings in whatever manner it deems most efficient and to avoid the sorting overhead.

- Pre-4.1 passwords and the `mysql_old_password` authentication plugin. Passwords stored in

the older hash format used before MySQL 4.1 are less secure than passwords that use the native password hashing method and should be avoided. Pre-4.1 passwords and the `mysql_old_password`authentication plugin are now deprecated. To prevent connections using accounts that have pre-4.1 Features Removed in MySQL 5.6 password hashes, the `secure_auth` system variable is now enabled by default. (To permit connections for accounts that have such password hashes, start the server with `--secure_auth=0`. However,because pre-4.1 passwords are deprecated, disabling `secure_auth` is also deprecated.)DBAs are advised to convert accounts that use the `mysql_old_password` authentication plugin to use`mysql_native_password` instead. For account upgrade instructions, see Section 6.4.1.3, “Migrating Away from Pre-4.1 Password Hashing and the mysql_old_password Plugin”.

The `OLD_PASSWORD()` function generates pre-4.1 password hashes, as does `PASSWORD()` if the `old_passwords` system variable is set to 1. `OLD_PASSWORD()` and `old_passwords=1` are deprecated.

- The `--skip-innodb` option and its synonyms (`--innodb=OFF`, `--disable-innodb`, and so forth).
- The `innodb_locks_unsafe_for_binlog` system variable.
- The `date_format`, `datetime_format`, and `time_format` system variables, which are unused.
- The `have_profiling`, `profiling`, and `profiling_history_size` system variables.
- The `innodb_use_sys_malloc` and `innodb_additional_mem_pool_size` system variables.
- The `timed_mutexes` system variable. It does nothing and has no effect.
- The `--language` option. Use the `--lc-messages-dir` and `--lc-messages` options instead.
- The `IGNORE` clause for `ALTER TABLE`. `ALTER IGNORE TABLE` causes problems for replication,

prevents online `ALTER TABLE` for unique index creation, and causes problems with foreign keys (rows removed in the parent table).

```
- The msql2mysql, mysql_convert_table_format, mysql_find_rows,
mysql_fix_extensions, mysql_setpermission, mysql_waitpid, mysql_zap, mysqlaccess,
```

and `mysqlbug` utilities.

- The `mysqlhotcopy` utility. Alternatives include `mysqldump` and MySQL Enterprise Backup.

> Features Removed in MySQL 5.6

The following items are obsolete and have been removed in MySQL 5.6. Where alternatives are shown,applications should be updated to use them.

For MySQL 5.5 applications that use features removed in MySQL 5.6, statements may fail when replicated from a MySQL 5.5 source to a MySQL 5.6 replica, or may have different effects on source and replica. To avoid such problems, applications that use features removed in MySQL 5.6 should be revised to avoid them and use alternatives when possible.

- The `--log` server option and the `log` system variable. Instead, use the `general_log` system variable

to enable the general query log and the `general_log_file` system variable to set the general query log file name.

- The `log_slow_queries` system variable. Instead, use the `slow_query_log` system variable to

enable the slow query log and the `slow_query_log_file` system variable to set the slow query log file name.

- The `--one-thread` server option. Use `--thread_handling=no-threads` instead.
- The `--safe-mode` server option.

Server and Status Variables and Options Added, Deprecated, or Removed in MySQL 5.6

- The `--skip-thread-priority` server option.
- The `--table-cache` server option. Use the `table_open_cache` system variable instead.
- The `--init-rpl-role` and `--rpl-recovery-rank` options, the `rpl_recovery_rank` system

variable, and the `Rpl_status` status variable.

- The `engine_condition_pushdown` system variable. Use the `engine_condition_pushdown` flag

of the `optimizer_switch` variable instead.

- The `have_csv`, `have_innodb`, `have_ndbcluster`, and `have_partitioning` system variables. Use

`SHOW PLUGINS` or query the `PLUGINS` table in the `INFORMATION_SCHEMA` database instead.

- The `sql_big_tables` system variable. Use `big_tables` instead.
- The `sql_low_priority_updates` system variable. Use `low_priority_updates` instead.
- The `sql_max_join_size` system variable. Use `max_join_size` instead.
- The `max_long_data_size` system variable. Use `max_allowed_packet` instead.
- The `FLUSH MASTER` and `FLUSH SLAVE` statements. Use the `RESET MASTER` and `RESET SLAVE`

statements instead.

- The `SLAVE START` and `SLAVE STOP` statements. Use The `START SLAVE` and `STOP SLAVE`

statements.

- The `SHOW AUTHORS` and `SHOW CONTRIBUTORS` statements.
- The `OPTION` and `ONE_SHOT` modifiers for the `SET` statement.
- It is explicitly disallowed to assign the value `DEFAULT` to stored procedure or function parameters or

stored program local variables (for example with a `SET var_name = DEFAULT` statement). It remains permissible to assign `DEFAULT` to system variables, as before.

- Most `SHOW ENGINE INNODB MUTEX` output is removed in 5.6.14. `SHOW ENGINE INNODB MUTEX`

output is removed entirely in MySQL 5.7.2. Comparable information can be generated by creating views on Performance Schema tables.

> 1.4 Server and Status Variables and Options Added, Deprecated, or

## Removed in MySQL 5.6

- Options and Variables Introduced in MySQL 5.6
- Options and Variables Deprecated in MySQL 5.6
- Options and Variables Removed in MySQL 5.6

This section lists server variables, status variables, and options that were added for the first time, have been deprecated, or have been removed in MySQL 5.6.

> Options and Variables Introduced in MySQL 5.6

The following system variables, status variables, and server options have been added in MySQL 5.6.

- `Audit_log_current_size`: Audit log file current size. Added in MySQL 5.6.20.

Options and Variables Introduced in MySQL 5.6

- `Audit_log_event_max_drop_size`: Size of largest dropped audited event. Added in MySQL 5.6.20.
- `Audit_log_events`: Number of handled audited events. Added in MySQL 5.6.20.
- `Audit_log_events_filtered`: Number of filtered audited events. Added in MySQL 5.6.20.
- `Audit_log_events_lost`: Number of dropped audited events. Added in MySQL 5.6.20.
- `Audit_log_events_written`: Number of written audited events. Added in MySQL 5.6.20.
- `Audit_log_total_size`: Combined size of written audited events. Added in MySQL 5.6.20.
- `Audit_log_write_waits`: Number of write-delayed audited events. Added in MySQL 5.6.20.
- `Binlog_stmt_cache_disk_use`: Number of nontransactional statements that used temporary file

instead of binary log statement cache. Added in MySQL 5.6.1.

- `Binlog_stmt_cache_use`: Number of statements that used temporary binary log statement cache.

Added in MySQL 5.6.1.

- `Com_alter_user`: Count of ALTER USER statements. Added in MySQL 5.6.6.
- `Com_get_diagnostics`: Count of GET DIAGNOSTICS statements. Added in MySQL 5.6.4.
- `Connection_control_delay_generated`: How many times server delayed connection request.

Added in MySQL 5.6.35.

- `Connection_errors_accept`: Number of errors calling accept on listening port. Added in MySQL

5.6.5.

- `Connection_errors_internal`: Number of connections refused due to internal errors. Added in

MySQL 5.6.5.

- `Connection_errors_max_connections`: Number of connections refused due to max_connections

limit. Added in MySQL 5.6.5.

- `Connection_errors_peer_address`: Number of errors searching for connection client IP addresses.

Added in MySQL 5.6.5.

- `Connection_errors_select`: Number of errors calling select/poll on listening port. Added in MySQL

5.6.5.

- `Connection_errors_tcpwrap`: Number of connections refused by libwrap. Added in MySQL 5.6.5.
- `Firewall_access_denied`: Number of statements rejected by MySQL Enterprise Firewall. Added in

MySQL 5.6.24.

- `Firewall_access_granted`: Number of statements accepted by MySQL Enterprise Firewall. Added

in MySQL 5.6.24.

- `Firewall_cached_entries`: Number of statements recorded by MySQL Enterprise Firewall. Added

in MySQL 5.6.24.

- `Handler_external_lock`: Number of locks started while statement executed. Added in MySQL 5.6.2.
- `Handler_mrr_init`: Number of times storage engine MRR implementation is used for table access.

Added in MySQL 5.6.1.

- `Handler_read_last`: Number of requests to read last index entry. Added in MySQL 5.6.1.

Options and Variables Introduced in MySQL 5.6

- `Innodb_available_undo_logs`: Total number of InnoDB rollback segments; different from

innodb_rollback_segments, which displays number of active rollback segments. Added in MySQL 5.6.5.

- `Innodb_buffer_pool_bytes_data`: Number of bytes containing data (dirty or clean) in buffer pool.

Added in MySQL 5.6.10.

- `Innodb_buffer_pool_bytes_dirty`: Number of bytes currently dirty in buffer pool. Added in MySQL

5.6.10.

- `Innodb_buffer_pool_dump_status`: Display status of buffer pool recording operation triggered by

innodb_buffer_pool_dump_at_shutdown or innodb_buffer_pool_dump_now. Added in MySQL 5.6.3.

- `Innodb_buffer_pool_load_status`: Display status of buffer pool warmup operation triggered by

innodb_buffer_pool_load_at_startup or innodb_buffer_pool_load_now. Added in MySQL 5.6.3.

- `Innodb_num_open_files`: Number of physical files currently opened by InnoDB. Added in MySQL

5.6.2.

- `Last_query_partial_plans`: Number of iterations in execution plan construction for previous

statement. Added in MySQL 5.6.5.

- `Performance_schema_accounts_lost`: How many accounts table rows could not be added. Added

in MySQL 5.6.3.

- `Performance_schema_digest_lost`: How many digests could not be instrumented. Added in

MySQL 5.6.5.

- `Performance_schema_hosts_lost`: How many hosts table rows could not be added. Added in

MySQL 5.6.3.

- `Performance_schema_session_connect_attrs_lost`: Number of connections for which attribute

strings could not be created. Added in MySQL 5.6.6.

- `Performance_schema_socket_classes_lost`: How many socket instruments could not be loaded.

Added in MySQL 5.6.3.

- `Performance_schema_socket_instances_lost`: How many socket instrument instances could not

be created. Added in MySQL 5.6.3.

- `Performance_schema_stage_classes_lost`: How many stage instruments could not be loaded.

Added in MySQL 5.6.3.

- `Performance_schema_statement_classes_lost`: How many statement instruments could not be

loaded. Added in MySQL 5.6.3.

- `Performance_schema_users_lost`: How many users table rows could not be added. Added in

MySQL 5.6.3.

- `Rsa_public_key`: sha256_password authentication plugin RSA public key value. Added in MySQL

5.6.6.

- `Slave_last_heartbeat`: Shows when latest heartbeat signal was received, in TIMESTAMP format.

Added in MySQL 5.6.1.

- `Slave_rows_last_search_algorithm_used`: Search algorithm most recently used by this replica

to locate rows for row-based replication (index, table, or hash scan). Added in MySQL 5.6.6.

- `Ssl_server_not_after`: SSL certificate last valid date. Added in MySQL 5.6.3.

Options and Variables Introduced in MySQL 5.6

- `Ssl_server_not_before`: SSL certificate first valid date. Added in MySQL 5.6.3.
- `Table_open_cache_hits`: Number of hits for open tables cache lookups. Added in MySQL 5.6.6.
- `Table_open_cache_misses`: Number of misses for open tables cache lookups. Added in MySQL

5.6.6.

- `Table_open_cache_overflows`: Number of overflows for open tables cache. Added in MySQL 5.6.6.
- `audit-log`: Whether to activate audit log plugin. Added in MySQL 5.6.10.
- `audit_log_buffer_size`: Size of audit log buffer. Added in MySQL 5.6.10.
- `audit_log_connection_policy`: Audit logging policy for connection-related events. Added in

MySQL 5.6.20.

- `audit_log_current_session`: Whether to audit current session. Added in MySQL 5.6.20.
- `audit_log_exclude_accounts`: Accounts not to audit. Added in MySQL 5.6.20.
- `audit_log_file`: Name of audit log file. Added in MySQL 5.6.10.
- `audit_log_flush`: Close and reopen audit log file. Added in MySQL 5.6.10.
- `audit_log_format`: Audit log file format. Added in MySQL 5.6.14.
- `audit_log_include_accounts`: Accounts to audit. Added in MySQL 5.6.20.
- `audit_log_policy`: Audit logging policy. Added in MySQL 5.6.10.
- `audit_log_rotate_on_size`: Close and reopen audit log file at this size. Added in MySQL 5.6.10.
- `audit_log_statement_policy`: Audit logging policy for statement-related events. Added in MySQL

5.6.20.

- `audit_log_strategy`: Audit logging strategy. Added in MySQL 5.6.10.
- `authentication_windows_log_level`: Windows authentication plugin logging level. Added in

MySQL 5.6.10.

- `authentication_windows_use_principal_name`: Whether to use Windows authentication plugin

principal name. Added in MySQL 5.6.10.

- `avoid_temporal_upgrade`: Whether ALTER TABLE should upgrade pre-5.6.4 temporal columns.

Added in MySQL 5.6.24.

- `bind_address`: IP address or host name to bind to. Added in MySQL 5.6.1.
- `binlog-checksum`: Enable/disable binary log checksums. Added in MySQL 5.6.2.
- `binlog_checksum`: Enable/disable binary log checksums. Added in MySQL 5.6.2.
- `binlog_error_action`: Controls what happens when server cannot write to binary log. Added in

MySQL 5.6.22.

- `binlog_gtid_simple_recovery`: Controls how binary logs are iterated during GTID recovery. Added

in MySQL 5.6.23.

- `binlog_max_flush_queue_time`: How long to read transactions before flushing to binary log. Added

in MySQL 5.6.6.

Options and Variables Introduced in MySQL 5.6

- `binlog_order_commits`: Whether to commit in same order as writes to binary log. Added in MySQL

5.6.6.

- `binlog_row_image`: Use full or minimal images when logging row changes. Added in MySQL 5.6.2.
- `binlog_rows_query_log_events`: When enabled, enables logging of rows query log events when

using row-based logging. Disabled by default. Do not enable when producing logs for pre-5.6 replicas/readers. Added in MySQL 5.6.2.

- `binlog_stmt_cache_size`: Size of cache to hold nontransactional statements for binary log during

transaction. Added in MySQL 5.6.1.

- `binlogging_impossible_mode`: Deprecated and later removed. Use binlog_error_action instead.

Added in MySQL 5.6.20.

- `block_encryption_mode`: Mode for block-based encryption algorithms. Added in MySQL 5.6.17.
- `connection_control_failed_connections_threshold`: Consecutive failed connection attempts

before delays occur. Added in MySQL 5.6.35.

- `connection_control_max_connection_delay`: Maximum delay (milliseconds) for server response

to failed connection attempts. Added in MySQL 5.6.35.

- `connection_control_min_connection_delay`: Minimum delay (milliseconds) for server response

to failed connection attempts. Added in MySQL 5.6.35.

- `core_file`: Write core file on server crashes. Added in MySQL 5.6.2.
- `daemon_memcached_enable_binlog`: . Added in MySQL 5.6.6.
- `daemon_memcached_engine_lib_name`: Shared library implementing InnoDB memcached plugin.

Added in MySQL 5.6.6.

- `daemon_memcached_engine_lib_path`: Directory which contains shared library implementing

InnoDB memcached plugin. Added in MySQL 5.6.6.

- `daemon_memcached_option`: Space-separated options which are passed to underlying memcached

daemon on startup. Added in MySQL 5.6.6.

- `daemon_memcached_r_batch_size`: Specifies how many memcached read operations to perform

before doing COMMIT to start new transaction. Added in MySQL 5.6.6.

- `daemon_memcached_w_batch_size`: Specifies how many memcached write operations to perform

before doing COMMIT to start new transaction. Added in MySQL 5.6.6.

- `default-authentication-plugin`: Default authentication plugin. Added in MySQL 5.6.6.
- `default_tmp_storage_engine`: Default storage engine (table type) for TEMPORARY tables. Added

in MySQL 5.6.3.

- `disable-gtid-unsafe-statements`: Obsolete: Replaced by enforce_gtid_consistency in MySQL

5.6.9. Added in MySQL 5.6.5.

- `disable_gtid_unsafe_statements`: Obsolete: Replaced by enforce_gtid_consistency in MySQL

5.6.9. Added in MySQL 5.6.5.

- `disconnect_on_expired_password`: Whether server disconnects clients with expired passwords if

clients cannot handle such accounts. Added in MySQL 5.6.10.

Options and Variables Introduced in MySQL 5.6

- `end_markers_in_json`: Whether optimizer JSON output should add end markers. Added in MySQL

5.6.5.

- `enforce_gtid_consistency`: Prevents execution of statements that cannot be logged in

transactionally safe manner. Added in MySQL 5.6.9.

- `eq_range_index_dive_limit`: Cutoff for switching from index dives to index statistics. Added in

MySQL 5.6.5.

- `explicit_defaults_for_timestamp`: Whether TIMESTAMP columns are nullable and have

DEFAULT NULL. Added in MySQL 5.6.6.

- `gtid_done`: Obsolete: Replaced by gtid_executed in MySQL 5.6.9. Added in MySQL 5.6.5.
- `gtid_executed`: Global: All GTIDs in binary log (global) or current transaction (session). Read-only.

Added in MySQL 5.6.9.

- `gtid_lost`: Obsolete: Replaced by gtid_purged in MySQL 5.6.9. Added in MySQL 5.6.5.
- `gtid_mode`: Controls whether GTID based logging is enabled and what type of transactions logs can

contain. Added in MySQL 5.6.5.

- `gtid_next`: Specifies GTID for next statement to execute; see documentation for details. Added in

MySQL 5.6.5.

- `gtid_owned`: Set of GTIDs owned by this client (session), or by all clients, together with thread ID of

owner (global). Read-only. Added in MySQL 5.6.5.

- `gtid_purged`: Set of all GTIDs that have been purged from binary log. Added in MySQL 5.6.9.
- `host_cache_size`: Size of host cache. Added in MySQL 5.6.5.
- `ignore-db-dir`: Treat directory as nondatabase directory. Added in MySQL 5.6.3.
- `ignore_db_dirs`: Directories treated as nondatabase directories. Added in MySQL 5.6.3.
- `innodb_adaptive_flushing_lwm`: Low water mark representing percentage of redo log capacity at

which adaptive flushing is enabled. Added in MySQL 5.6.6.

- `innodb_adaptive_max_sleep_delay`: Allows InnoDB to adjust value of innodb_thread_sleep_delay

up or down automatically, according to current workload. Added in MySQL 5.6.3.

- `innodb_api_bk_commit_interval`: How often to auto-commit idle connections which use InnoDB

memcached interface, in seconds. Added in MySQL 5.6.7.

- `innodb_api_disable_rowlock`: . Added in MySQL 5.6.6.
- `innodb_api_enable_binlog`: Allows use of InnoDB memcached plugin with MySQL binary log.

Added in MySQL 5.6.6.

- `innodb_api_enable_mdl`: Locks table used by InnoDB memcached plugin, so that it cannot be

dropped or altered by DDL through SQL interface. Added in MySQL 5.6.6.

- `innodb_api_trx_level`: Allows control of transaction isolation level on queries processed by

memcached interface. Added in MySQL 5.6.6.

- `innodb_buffer_pool_dump_at_shutdown`: Specifies whether to record pages cached in InnoDB

buffer pool when MySQL server is shut down, to shorten warmup process at next restart. Added in MySQL 5.6.3.

Options and Variables Introduced in MySQL 5.6

- `innodb_buffer_pool_dump_now`: Immediately record pages cached in InnoDB buffer pool. Added in

MySQL 5.6.3.

- `innodb_buffer_pool_filename`: Specifies file containing list of page numbers produced by

innodb_buffer_pool_dump_at_shutdown or innodb_buffer_pool_dump_now. Added in MySQL 5.6.3.

- `innodb_buffer_pool_load_abort`: Interrupts process of restoring InnoDB buffer pool contents

triggered by innodb_buffer_pool_load_at_startup or innodb_buffer_pool_load_now. Added in MySQL

5.6.3.

- `innodb_buffer_pool_load_at_startup`: Specifies that, on MySQL server startup, InnoDB buffer

pool is automatically "warmed up" by loading same pages it held at earlier time. Added in MySQL 5.6.3.

- `innodb_buffer_pool_load_now`: Immediately "warms up" InnoDB buffer pool by loading set of data

pages, without waiting for server restart. Added in MySQL 5.6.3.

- `innodb_change_buffer_max_size`: Maximum size for InnoDB change buffer, as percentage of total

size of buffer pool. Added in MySQL 5.6.2.

- `innodb_checksum_algorithm`: Specifies how to generate and verify checksum stored in each disk

block of each InnoDB tablespace. Added in MySQL 5.6.3.

- `innodb_cmp_per_index_enabled`: Enables per-index compression-related statistics in

INFORMATION_SCHEMA.INNODB_CMP_PER_INDEX table. Added in MySQL 5.6.7.

- `innodb_compression_failure_threshold_pct`: Cutoff point at which MySQL begins adding

padding within compressed pages to avoid expensive compression failures. Added in MySQL 5.6.7.

- `innodb_compression_level`: Level of zlib compression to use for InnoDB compressed tables and

indexes. Added in MySQL 5.6.7.

- `innodb_compression_pad_pct_max`: Maximum percentage that can be reserved as free space

within each compressed page, to avoid compression failures when tightly packed data is recompressed.

Added in MySQL 5.6.7.

- `innodb_disable_sort_file_cache`: Disable OS file system cache for merge-sort temporary files.

Added in MySQL 5.6.4.

- `innodb_fil_make_page_dirty_debug`: Dirties first page of specified tablespace. Added in MySQL

5.6.17.

- `innodb_flush_log_at_timeout`: Write and flush logs every N seconds. Added in MySQL 5.6.6.
- `innodb_flush_neighbors`: Specifies whether or not flushing page from InnoDB buffer pool also

flushes other dirty pages in same extent. Added in MySQL 5.6.3.

- `innodb_flushing_avg_loops`: Number of iterations for which InnoDB keeps previously calculated

snapshot of flushing state, controlling how quickly adaptive flushing responds to changing workloads.

Added in MySQL 5.6.6.

- `innodb_force_load_corrupted`: Lets InnoDB load tables at startup that are marked as corrupted;

use only during troubleshooting. Added in MySQL 5.6.3.

- `innodb_ft_aux_table`: Qualified name of InnoDB table containing FULLTEXT index for diagnostic

purposes. Added in MySQL 5.6.4.

- `innodb_ft_cache_size`: Size of cache holding parsed document in memory while creating InnoDB

FULLTEXT index. Added in MySQL 5.6.4.

Options and Variables Introduced in MySQL 5.6

- `innodb_ft_enable_diag_print`: Whether to enable additional full-text search diagnostic output.

Added in MySQL 5.6.4.

- `innodb_ft_enable_stopword`: Omit stop words from search index during creation of InnoDB

FULLTEXT index. Added in MySQL 5.6.4.

- `innodb_ft_max_token_size`: Maximum length of words that are stored in InnoDB FULLTEXT index.

Added in MySQL 5.6.4.

- `innodb_ft_min_token_size`: Minimum length of words that are stored in InnoDB FULLTEXT index.

Added in MySQL 5.6.4.

- `innodb_ft_num_word_optimize`: Number of words to process during each OPTIMIZE TABLE

operation on InnoDB FULLTEXT index. Added in MySQL 5.6.4.

- `innodb_ft_result_cache_limit`: InnoDB FULLTEXT search query result cache limit. Added in

MySQL 5.6.13.

- `innodb_ft_server_stopword_table`: Specifies table holding list of stopwords

for InnoDB FULLTEXT indexes, overriding default stopword list; can be overridden by innodb_ft_user_stopword_table. Added in MySQL 5.6.4.

- `innodb_ft_sort_pll_degree`: Number of threads used to create InnoDB FULLTEXT index in

parallel, when building search index for large table. Added in MySQL 5.6.4.

- `innodb_ft_total_cache_size`: Total memory allocated for InnoDB FULLTEXT search index cache.

Added in MySQL 5.6.13.

- `innodb_ft_user_stopword_table`: Specifies table holding list of stopwords for InnoDB FULLTEXT

indexes, overriding default stopword list as well as innodb_ft_server_stopword_table. Added in MySQL

5.6.4.

- `innodb_io_capacity_max`: Limit up to which InnoDB is allowed to extend innodb_io_capacity setting

in case of emergency. Added in MySQL 5.6.6.

- `innodb_large_prefix`: Enables longer keys for column prefix indexes. Added in MySQL 5.6.3.
- `innodb_log_checkpoint_now`: Debug option that forces InnoDB to write checkpoint. Added in

MySQL 5.6.12.

- `innodb_log_compressed_pages`: Specifies whether images of re-compressed pages are stored in

InnoDB redo logs. Added in MySQL 5.6.11.

- `innodb_lru_scan_depth`: Influences algorithms and heuristics for flush operation for InnoDB buffer

pool. Added in MySQL 5.6.3.

- `innodb_max_dirty_pages_pct_lwm`: Low water mark representing percentage of dirty pages where

preflushing is enabled to control dirty page ratio. Added in MySQL 5.6.6.

- `innodb_max_purge_lag_delay`: Maximum delay in milliseconds for formula calculated using

innodb_max_purge_lag configuration option. Added in MySQL 5.6.5.

- `innodb_monitor_disable`: Turns off one or more counters in information_schema.innodb_metrics

table. Added in MySQL 5.6.2.

- `innodb_monitor_enable`: Turns on one or more counters in information_schema.innodb_metrics

table. Added in MySQL 5.6.2.

Options and Variables Introduced in MySQL 5.6

- `innodb_monitor_reset`: Resets count value for one or more counters in

information_schema.innodb_metrics table to zero. Added in MySQL 5.6.2.

- `innodb_monitor_reset_all`: Resets all values (minimum, maximum, and so on) for one or more

counters in information_schema.innodb_metrics table. Added in MySQL 5.6.2.

- `innodb_numa_interleave`: Enables NUMA MPOL_INTERLEAVE memory policy for allocation of

InnoDB buffer pool. Added in MySQL 5.6.27.

- `innodb_online_alter_log_max_size`: Upper limit on size of temporary log files used during online

DDL operations for InnoDB tables. Added in MySQL 5.6.6.

- `innodb_optimize_fulltext_only`: Causes OPTIMIZE TABLE statement for InnoDB table to

process newly added, deleted, and updated token data for FULLTEXT index, rather than to reorganize data in clustered index of table. Added in MySQL 5.6.4.

- `innodb_page_size`: Specifies page size for all InnoDB tablespaces in instance. Added in MySQL

5.6.4.

- `innodb_print_all_deadlocks`: During shutdown, prints information about all InnoDB deadlocks to

server error log. Added in MySQL 5.6.2.

- `innodb_random_read_ahead`: Enables random read-ahead technique for optimizing InnoDB I/O.

Added in MySQL 5.6.3.

- `innodb_read_only`: Starts server in read-only mode. Added in MySQL 5.6.7.
- `innodb_rollback_segments`: Defines number of rollback segments in system tablespace for InnoDB

to use within transaction. Added in MySQL 5.6.2.

- `innodb_saved_page_number_debug`: Saves page number. Added in MySQL 5.6.17.
- `innodb_sort_buffer_size`: Specifies size of buffer used for sorting data during creation of InnoDB

index. Added in MySQL 5.6.4.

- `innodb_stats_auto_recalc`: Causes InnoDB to recalculate persistent statistics automatically after

table data is changed substantially. Added in MySQL 5.6.6.

- `innodb_stats_include_delete_marked`: Include delete-marked records when calculating

persistent InnoDB statistics. Added in MySQL 5.6.35.

- `innodb_stats_method`: Specifies how InnoDB index statistics collection code should treat NULLs.

Added in MySQL 5.6.2.

- `innodb_stats_persistent`: Turns on InnoDB persistent statistics feature. Added in MySQL 5.6.6.
- `innodb_stats_persistent_sample_pages`: Number of pages to sample in each InnoDB index,

when persistent statistics feature is also enabled. Added in MySQL 5.6.2.

- `innodb_stats_transient_sample_pages`: Number of pages to sample in each InnoDB index,

when persistent statistics feature is turned off (default). Added in MySQL 5.6.2.

- `innodb_status_output`: Used to enable or disable periodic output for standard InnoDB Monitor. Also

used in combination with innodb_status_output_locks to enable and disable periodic output for InnoDB Lock Monitor. Added in MySQL 5.6.16.

- `innodb_status_output_locks`: Used to enable or disable periodic output for standard InnoDB

Lock Monitor. innodb_status_output must also be enabled to produce periodic output for InnoDB Lock Monitor. Added in MySQL 5.6.16.

Options and Variables Introduced in MySQL 5.6

- `innodb_sync_array_size`: Splits internal data structure used to coordinate threads, for higher

concurrency in workloads with large numbers of waiting threads. Added in MySQL 5.6.3.

- `innodb_tmpdir`: Directory location for temporary table files created during online ALTER TABLE

operations. Added in MySQL 5.6.29.

- `innodb_undo_directory`: Relative or absolute directory path where InnoDB creates separate

tablespaces for undo logs; typically used to place those logs on different storage device. Added in MySQL 5.6.3.

- `innodb_undo_logs`: Number of undo logs (rollback segments) used by InnoDB; alias for

innodb_rollback_segments. Added in MySQL 5.6.3.

- `innodb_undo_tablespaces`: Number of tablespace files that rollback segments are divided between.

Added in MySQL 5.6.3.

- `log-raw`: Whether to log queries without rewriting. Added in MySQL 5.6.3.
- `log_bin_basename`: Path and base name for binary log files. Added in MySQL 5.6.2.
- `log_bin_use_v1_row_events`: Whether server is using version 1 binary log row events. Added in

MySQL 5.6.6.

- `log_slow_admin_statements`: Log slow OPTIMIZE, ANALYZE, ALTER and other administrative

statements to slow query log if it is open. Added in MySQL 5.6.11.

- `log_slow_slave_statements`: Cause slow statements as executed by replica to be written to slow

query log. Added in MySQL 5.6.11.

- `log_throttle_queries_not_using_indexes`: Throttle write rate to slow log for queries not using

indexes slow query log if it is open. Added in MySQL 5.6.5.

- `master_info_repository`: Whether to write connection metadata repository, containing source

information and replication I/O thread location in source's binary log, to file or table. Added in MySQL

5.6.2.

- `master_verify_checksum`: Cause source to examine checksums when reading from binary log.

Added in MySQL 5.6.2.

- `max_binlog_stmt_cache_size`: Can be used to restrict total size used to cache all nontransactional

statements during transaction. Added in MySQL 5.6.1.

- `max_digest_length`: Maximum digest size in bytes. Added in MySQL 5.6.24.
- `metadata_locks_cache_size`: Size of metadata locks cache. Added in MySQL 5.6.4.
- `metadata_locks_hash_instances`: Number of metadata lock hashes. Added in MySQL 5.6.8.
- `mysql_firewall_max_query_size`: Maximum size of recorded statements. Added in MySQL 5.6.24.
- `mysql_firewall_mode`: Whether MySQL Enterprise Firewall is operational. Added in MySQL 5.6.24.
- `mysql_firewall_trace`: Whether to enable firewall trace. Added in MySQL 5.6.24.
- `named_pipe_full_access_group`: Name of Windows group granted full access to named pipe.

Added in MySQL 5.6.43.

- `optimizer_join_cache_level`: How join buffers are used. Added in MySQL 5.6.1.

Options and Variables Introduced in MySQL 5.6

- `optimizer_trace`: Control optimizer tracing. Added in MySQL 5.6.3.
- `optimizer_trace_features`: Control optimizer tracing. Added in MySQL 5.6.3.
- `optimizer_trace_limit`: Control optimizer tracing. Added in MySQL 5.6.3.
- `optimizer_trace_max_mem_size`: Control optimizer tracing. Added in MySQL 5.6.3.
- `optimizer_trace_offset`: Control optimizer tracing. Added in MySQL 5.6.3.
- `performance-schema-consumer-events-stages-current`: Configure events-stages-current

consumer. Added in MySQL 5.6.4.

- `performance-schema-consumer-events-stages-history`: Configure events-stages-history

consumer. Added in MySQL 5.6.4.

- `performance-schema-consumer-events-stages-history-long`: Configure events-stages-

history-long consumer. Added in MySQL 5.6.4.

- `performance-schema-consumer-events-statements-current`: Configure events-statements-

current consumer. Added in MySQL 5.6.4.

- `performance-schema-consumer-events-statements-history`: Configure events-statements-

history consumer. Added in MySQL 5.6.4.

- `performance-schema-consumer-events-statements-history-long`: Configure events-

statements-history-long consumer. Added in MySQL 5.6.4.

- `performance-schema-consumer-events-waits-current`: Configure events-waits-current

consumer. Added in MySQL 5.6.4.

- `performance-schema-consumer-events-waits-history`: Configure events-waits-history

consumer. Added in MySQL 5.6.4.

- `performance-schema-consumer-events-waits-history-long`: Configure events-waits-history-

long consumer. Added in MySQL 5.6.4.

- `performance-schema-consumer-global-instrumentation`: Configure global-instrumentation

consumer. Added in MySQL 5.6.4.

- `performance-schema-consumer-statements-digest`: Configure statements-digest consumer.

Added in MySQL 5.6.5.

- `performance-schema-consumer-thread-instrumentation`: Configure thread-instrumentation

consumer. Added in MySQL 5.6.4.

- `performance-schema-instrument`: Configure Performance Schema instrument. Added in MySQL

5.6.4.

- `performance_schema_accounts_size`: Number of rows in accounts table. Added in MySQL 5.6.3.
- `performance_schema_digests_size`: Number of rows in events_statements_summary_by_digest

table. Added in MySQL 5.6.5.

- `performance_schema_events_stages_history_long_size`: Number of rows in

events_stages_history_long table. Added in MySQL 5.6.3.

- `performance_schema_events_stages_history_size`: Number of rows per thread in

events_stages_history table. Added in MySQL 5.6.3.

Options and Variables Introduced in MySQL 5.6

- `performance_schema_events_statements_history_long_size`: Number of rows in

events_statements_history_long table. Added in MySQL 5.6.3.

- `performance_schema_events_statements_history_size`: Number of rows per thread in

events_statements_history table. Added in MySQL 5.6.3.

- `performance_schema_hosts_size`: Number of rows in hosts table. Added in MySQL 5.6.3.
- `performance_schema_max_digest_length`: Maximum Performance Schema digest size in bytes.

Added in MySQL 5.6.26.

- `performance_schema_max_socket_classes`: Maximum number of socket instruments. Added in

MySQL 5.6.3.

- `performance_schema_max_socket_instances`: Maximum number of instrumented socket objects.

Added in MySQL 5.6.3.

- `performance_schema_max_stage_classes`: Maximum number of stage instruments. Added in

MySQL 5.6.3.

- `performance_schema_max_statement_classes`: Maximum number of statement instruments.

Added in MySQL 5.6.3.

- `performance_schema_session_connect_attrs_size`: Size of connection attribute strings buffer

per thread. Added in MySQL 5.6.6.

- `performance_schema_setup_actors_size`: Number of rows in setup_actors table. Added in

MySQL 5.6.1.

- `performance_schema_setup_objects_size`: Number of rows in setup_objects table. Added in

MySQL 5.6.1.

- `performance_schema_users_size`: Number of rows in users table. Added in MySQL 5.6.3.
- `plugin-load-add`: Add to list of plugins to load at startup. Added in MySQL 5.6.3.
- `pseudo_slave_mode`: For internal server use. Added in MySQL 5.6.10.
- `relay_log_basename`: Complete path to relay log, including file name. Added in MySQL 5.6.2.
- `relay_log_info_repository`: Whether to write location of replication SQL thread in relay logs to file

or table. Added in MySQL 5.6.2.

- `rpl_stop_slave_timeout`: Number of seconds that STOP REPLICA or STOP SLAVE waits before

timing out. Added in MySQL 5.6.13.

- `sha256_password_private_key_path`: SHA256 authentication plugin private key path name.

Added in MySQL 5.6.6.

- `sha256_password_public_key_path`: SHA256 authentication plugin public key path name. Added

in MySQL 5.6.6.

- `show_old_temporals`: Whether SHOW CREATE TABLE should indicate pre-5.6.4 temporal columns.

Added in MySQL 5.6.24.

- `simplified_binlog_gtid_recovery`: Renamed to binlog_gtid_simple_recovery. Added in MySQL

5.6.21.

- `slave-sql-verify-checksum`: Cause replica to examine checksums when reading from relay log.

Added in MySQL 5.6.2.

Options and Variables Introduced in MySQL 5.6

- `slave_checkpoint_group`: Maximum number of transactions processed by multithreaded replica

before checkpoint operation is called to update progress status. Not supported by NDB Cluster. Added in MySQL 5.6.3.

- `slave_checkpoint_period`: Update progress status of multithreaded replica and flush relay log info

to disk after this number of milliseconds. Not supported by NDB Cluster. Added in MySQL 5.6.3.

- `slave_max_allowed_packet`: Maximum size, in bytes, of packet that can be sent from replication

source server to replica; overrides max_allowed_packet. Added in MySQL 5.6.6.

- `slave_parallel_workers`: Number of applier threads for executing replication transactions in

parallel; 0 or 1 disables replica multithreading. NDB Cluster: see documentation. Added in MySQL 5.6.3.

- `slave_pending_jobs_size_max`: Maximum size of replica worker queues holding events not yet

applied. Added in MySQL 5.6.3.

- `slave_rows_search_algorithms`: Determines search algorithms used for replica update batching.

Any 2 or 3 from this list: INDEX_SEARCH, TABLE_SCAN, HASH_SCAN. Added in MySQL 5.6.6.

- `slave_sql_verify_checksum`: Cause replica to examine checksums when reading from relay log.

Added in MySQL 5.6.2.

- `slow-start-timeout`: Wait before trying to kill windows service at startup. Added in MySQL 5.6.5.
- `ssl_crl`: File that contains certificate revocation lists. Added in MySQL 5.6.3.
- `ssl_crlpath`: Directory that contains certificate revocation list files. Added in MySQL 5.6.3.
- `stored_program_cache`: Sets "soft" upper limit for number of cached stored routines per connection.

Stored procedures and stored functions are cached separately; this variable sets size for both of these.

Added in MySQL 5.6.5.

- `table_open_cache_instances`: Number of open tables cache instances. Added in MySQL 5.6.6.
- `thread_pool_algorithm`: Thread pool algorithm. Added in MySQL 5.6.10.
- `thread_pool_high_priority_connection`: Whether current session is high priority. Added in

MySQL 5.6.10.

- `thread_pool_max_unused_threads`: Maximum permissible number of unused threads. Added in

MySQL 5.6.10.

- `thread_pool_prio_kickup_timer`: How long before statement is moved to high-priority execution.

Added in MySQL 5.6.10.

- `thread_pool_size`: Number of thread groups in thread pool. Added in MySQL 5.6.10.
- `thread_pool_stall_limit`: How long before statement is defined as stalled. Added in MySQL

5.6.10.

- `transaction-read-only`: Default transaction access mode. Added in MySQL 5.6.5.
- `tx_read_only`: Default transaction access mode. Added in MySQL 5.6.5.
- `validate-password`: Whether to activate password validation plugin. Added in MySQL 5.6.6.
- `validate-user-plugins`: Whether to perform additional validation of user plugins. Added in MySQL

5.6.11.

Options and Variables Deprecated in MySQL 5.6

- `validate_password_dictionary_file`: validate_password dictionary file. Added in MySQL 5.6.6.
- `validate_password_dictionary_file_last_parsed`: When dictionary file was last parsed.

Added in MySQL 5.6.26.

- `validate_password_dictionary_file_words_count`: Number of words in dictionary file. Added

in MySQL 5.6.26.

- `validate_password_length`: validate_password required password length. Added in MySQL 5.6.6.
- `validate_password_mixed_case_count`: validate_password required number of uppercase/

lowercase characters. Added in MySQL 5.6.6.

- `validate_password_number_count`: validate_password required number of digit characters. Added

in MySQL 5.6.6.

- `validate_password_policy`: validate_password password policy. Added in MySQL 5.6.6.
- `validate_password_special_char_count`: validate_password required number of special

characters. Added in MySQL 5.6.6.

> Options and Variables Deprecated in MySQL 5.6

The following system variables, status variables, and options have been deprecated in MySQL 5.6.

- `Delayed_errors`: Number of rows written with INSERT DELAYED for which some error occurred.

Deprecated in MySQL 5.6.7.

- `Delayed_insert_threads`: Number of INSERT DELAYED thread handlers in use. Deprecated in

MySQL 5.6.7.

- `Delayed_writes`: Number of INSERT DELAYED rows written. Deprecated in MySQL 5.6.7.
- `Not_flushed_delayed_rows`: Number of rows waiting to be written in INSERT DELAY queues.

Deprecated in MySQL 5.6.7.

- `avoid_temporal_upgrade`: Whether ALTER TABLE should upgrade pre-5.6.4 temporal columns.

Deprecated in MySQL 5.6.24.

- `binlogging_impossible_mode`: Deprecated and later removed. Use binlog_error_action instead.

Deprecated in MySQL 5.6.22.

- `delayed_insert_limit`: After inserting delayed_insert_limit rows, INSERT DELAYED handler checks

whether there are any SELECT statements pending. If so, it allows these to execute before continuing.

Deprecated in MySQL 5.6.7.

- `delayed_insert_timeout`: How many seconds INSERT DELAYED thread should wait for INSERT

statements before terminating. Deprecated in MySQL 5.6.7.

- `delayed_queue_size`: What size queue (in rows) should be allocated for handling INSERT

DELAYED. Deprecated in MySQL 5.6.7.

- `explicit_defaults_for_timestamp`: Whether TIMESTAMP columns are nullable and have

DEFAULT NULL. Deprecated in MySQL 5.6.6.

- `have_profiling`: Whether statement profiling capability is available. Deprecated in MySQL 5.6.8.
- `innodb`: Enable InnoDB (if this version of MySQL supports it). Deprecated in MySQL 5.6.21.

Options and Variables Removed in MySQL 5.6

- `innodb_additional_mem_pool_size`: Size of memory pool InnoDB uses to store data dictionary

information and other internal data structures. Deprecated in MySQL 5.6.3.

- `innodb_checksums`: Enable InnoDB checksums validation. Deprecated in MySQL 5.6.3.
- `innodb_locks_unsafe_for_binlog`: Force InnoDB not to use next-key locking. Instead use only

row-level locking. Deprecated in MySQL 5.6.3.

- `innodb_stats_sample_pages`: Number of index pages to sample for index distribution statistics.

Deprecated in MySQL 5.6.3.

- `innodb_use_sys_malloc`: Whether InnoDB uses OS or own memory allocator. Deprecated in MySQL

5.6.3.

- `language`: Client error messages in given language. May be given as full path. Deprecated in MySQL

5.6.1.

- `master-retry-count`: Number of tries replica makes to connect to source before giving up.

Deprecated in MySQL 5.6.1.

- `max_delayed_threads`: Do not start more than this number of threads to handle INSERT DELAYED

statements. If set to zero, which means INSERT DELAYED is not used. Deprecated in MySQL 5.6.7.

- `max_insert_delayed_threads`: Synonym for max_delayed_threads. Deprecated in MySQL 5.6.7.
- `max_tmp_tables`: Unused. Deprecated in MySQL 5.6.7.
- `multi_range_count`: Maximum number of ranges to send to table handler at once during range

selects. Deprecated in MySQL 5.6.7.

- `profiling`: Enable or disable statement profiling. Deprecated in MySQL 5.6.8.
- `profiling_history_size`: How many statements to maintain profiling information for. Deprecated in

MySQL 5.6.8.

- `show_old_temporals`: Whether SHOW CREATE TABLE should indicate pre-5.6.4 temporal columns.

Deprecated in MySQL 5.6.24.

- `simplified_binlog_gtid_recovery`: Renamed to binlog_gtid_simple_recovery. Deprecated in

MySQL 5.6.23.

- `thread_concurrency`: Permits application to provide hint to threads system for desired number of

threads which should be run at one time. Deprecated in MySQL 5.6.1.

- `timed_mutexes`: Specify whether to time mutexes (only InnoDB mutexes are currently supported).

Deprecated in MySQL 5.6.20.

> Options and Variables Removed in MySQL 5.6

The following system variables, status variables, and options have been removed in MySQL 5.6.

- `Com_show_new_master`: Count of SHOW NEW MASTER statements. Removed in MySQL 5.6.2.
- `bind-address`: IP address or host name to bind to. Removed in MySQL 5.6.1.
- `disable-gtid-unsafe-statements`: Obsolete: Replaced by enforce_gtid_consistency in MySQL

5.6.9. Removed in MySQL 5.6.9.

How to Report Bugs or Problems

- `disable_gtid_unsafe_statements`: Obsolete: Replaced by enforce_gtid_consistency in MySQL

5.6.9. Removed in MySQL 5.6.9.

- `engine_condition_pushdown`: Push supported query conditions to storage engine. Removed in

MySQL 5.6.1.

- `gtid_done`: Obsolete: Replaced by gtid_executed in MySQL 5.6.9. Removed in MySQL 5.6.9.
- `gtid_lost`: Obsolete: Replaced by gtid_purged in MySQL 5.6.9. Removed in MySQL 5.6.9.
- `have_csv`: Whether mysqld supports csv tables. Removed in MySQL 5.6.1.
- `have_innodb`: Whether mysqld supports InnoDB tables. Removed in MySQL 5.6.1.
- `have_partitioning`: Whether mysqld supports partitioning. Removed in MySQL 5.6.1.
- `log`: Log connections and queries to file. Removed in MySQL 5.6.1.
- `log-slow-admin-statements`: Log slow OPTIMIZE, ANALYZE, ALTER and other administrative

statements to slow query log if it is open. Removed in MySQL 5.6.11.

- `log-slow-slave-statements`: Cause slow statements as executed by replica to be written to slow

query log. Removed in MySQL 5.6.11.

- `log_slow_queries`: Whether to log slow queries. Logging defaults to hostname-slow.log file. Must be

enabled to activate other slow query log options. Removed in MySQL 5.6.1.

- `mysql_firewall_max_query_size`: Maximum size of recorded statements. Removed in MySQL

5.6.26.

- `one-thread`: Only use one thread (for debugging under Linux). Removed in MySQL 5.6.1.
- `optimizer_join_cache_level`: How join buffers are used. Removed in MySQL 5.6.3.
- `safe-mode`: Skip some optimization stages (for testing). Removed in MySQL 5.6.6.
- `skip-thread-priority`: Do not give threads different priorities. Removed in MySQL 5.6.1.
- `sql_big_tables`: This variable is deprecated, and is mapped to big_tables. Removed in MySQL 5.6.1.
- `sql_low_priority_updates`: This variable is deprecated, and is mapped to low_priority_updates.

Removed in MySQL 5.6.1.

- `sql_max_join_size`: This variable is deprecated, and is mapped to max_join_size. Removed in

MySQL 5.6.1.

## 1.5 How to Report Bugs or Problems

Before posting a bug report about a problem, please try to verify that it is a bug and that it has not been reported already:

- Start by searching the MySQL online manual at https://dev.mysql.com/doc/. We try to keep the manual

up to date by updating it frequently with solutions to newly found problems. In addition, the release notes accompanying the manual can be particularly useful since it is quite possible that a newer version contains a solution to your problem. The release notes are available at the location just given for the manual.

- If you get a parse error for an SQL statement, please check your syntax closely. If you cannot find

something wrong with it, it is extremely likely that your current version of MySQL Server doesn't support How to Report Bugs or Problems the syntax you are using. If you are using the current version and the manual doesn't cover the syntax that you are using, MySQL Server doesn't support your statement.

If the manual covers the syntax you are using, but you have an older version of MySQL Server, you should check the MySQL change history to see when the syntax was implemented. In this case, you have the option of upgrading to a newer version of MySQL Server.

- For solutions to some common problems, see Section B.3, “Problems and Common Errors”.
- Search the bugs database at http://bugs.mysql.com/ to see whether the bug has been reported and

fixed.

- You can also use http://www.mysql.com/search/ to search all the Web pages (including the manual) that

are located at the MySQL website.

If you cannot find an answer in the manual, the bugs database, or the mailing list archives, check with your local MySQL expert. If you still cannot find an answer to your question, please use the following guidelines for reporting the bug.

The normal way to report bugs is to visit http://bugs.mysql.com/, which is the address for our bugs database. This database is public and can be browsed and searched by anyone. If you log in to the system, you can enter new reports.

Bugs posted in the bugs database at http://bugs.mysql.com/ that are corrected for a given release are noted in the release notes.

If you find a security bug in MySQL Server, please let us know immediately by sending an email message to `<secalert_us@oracle.com>`. Exception: Support customers should report all problems, including security bugs, to Oracle Support at http://support.oracle.com/.

To discuss problems with other users, you can use the MySQL Community Slack.

Writing a good bug report takes patience, but doing it right the first time saves time both for us and for yourself. A good bug report, containing a full test case for the bug, makes it very likely that we will fix the bug in the next release. This section helps you write your report correctly so that you do not waste your time doing things that may not help us much or at all. Please read this section carefully and make sure that all the information described here is included in your report.

Preferably, you should test the problem using the latest production or development version of MySQL Server before posting. Anyone should be able to repeat the bug by just using `mysql test <``script_file` on your test case or by running the shell or Perl script that you include in the bug report.

Any bug that we are able to repeat has a high chance of being fixed in the next MySQL release.

It is most helpful when a good description of the problem is included in the bug report. That is, give a good example of everything you did that led to the problem and describe, in exact detail, the problem itself.

The best reports are those that include a full example showing how to reproduce the bug or problem. See Section 5.8, “Debugging MySQL”.

Remember that it is possible for us to respond to a report containing too much information, but not to one containing too little. People often omit facts because they think they know the cause of a problem and assume that some details do not matter. A good principle to follow is that if you are in doubt about stating something, state it. It is faster and less troublesome to write a couple more lines in your report than to wait longer for the answer if we must ask you to provide information that was missing from the initial report.

The most common errors made in bug reports are (a) not including the version number of the MySQL distribution that you use, and (b) not fully describing the platform on which the MySQL server is installed How to Report Bugs or Problems(including the platform type and version number). These are highly relevant pieces of information, and in 99 cases out of 100, the bug report is useless without them. Very often we get questions like, “Why doesn't this work for me?” Then we find that the feature requested wasn't implemented in that MySQL version,or that a bug described in a report has been fixed in newer MySQL versions. Errors often are platform-dependent. In such cases, it is next to impossible for us to fix anything without knowing the operating system and the version number of the platform.

If you compiled MySQL from source, remember also to provide information about your compiler if it is related to the problem. Often people find bugs in compilers and think the problem is MySQL-related.

Most compilers are under development all the time and become better version by version. To determine whether your problem depends on your compiler, we need to know what compiler you used. Note that every compiling problem should be regarded as a bug and reported accordingly.

If a program produces an error message, it is very important to include the message in your report. If we try to search for something from the archives, it is better that the error message reported exactly matches the one that the program produces. (Even the lettercase should be observed.) It is best to copy and paste the entire error message into your report. You should never try to reproduce the message from memory.

If you have a problem with Connector/ODBC (MyODBC), please try to generate a trace file and send it with your report. See How to Report Connector/ODBC Problems or Bugs.

If your report includes long query output lines from test cases that you run with the `mysql` command-line tool, you can make the output more readable by using the `--vertical` option or the `\G` statement terminator. The `EXPLAIN SELECT` example later in this section demonstrates the use of `\G`.

Please include the following information in your report:

- The version number of the MySQL distribution you are using (for example, MySQL 5.7.10). You can find

out which version you are running by executing `mysqladmin version`. The `mysqladmin` program can be found in the `bin` directory under your MySQL installation directory.

- The manufacturer and model of the machine on which you experience the problem.
- The operating system name and version. If you work with Windows, you can usually get the name and

version number by double-clicking your My Computer icon and pulling down the “Help/About Windows”menu. For most Unix-like operating systems, you can get this information by executing the command

```
uname -a.
```

- Sometimes the amount of memory (real and virtual) is relevant. If in doubt, include these values.
- The contents of the `docs/INFO_BIN` file from your MySQL installation. This file contains information

about how MySQL was configured and compiled.

- If you are using a source distribution of the MySQL software, include the name and version number of

the compiler that you used. If you have a binary distribution, include the distribution name.

- If the problem occurs during compilation, include the exact error messages and also a few lines of

context around the offending code in the file where the error occurs.

- If `mysqld` died, you should also report the statement that caused `mysqld` to unexpectedly exit. You can

usually get this information by running `mysqld` with query logging enabled, and then looking in the log after `mysqld` exits. See Section 5.8, “Debugging MySQL”.

- If a database table is related to the problem, include the output from the `SHOW CREATE TABLE`

`db_name.tbl_name` statement in the bug report. This is a very easy way to get the definition of any table in a database. The information helps us create a situation matching the one that you have experienced.

How to Report Bugs or Problems

- The SQL mode in effect when the problem occurred can be significant, so please report the value of

the `sql_mode` system variable. For stored procedure, stored function, and trigger objects, the relevant`sql_mode` value is the one in effect when the object was created. For a stored procedure or function,the `SHOW CREATE PROCEDURE` or `SHOW CREATE FUNCTION` statement shows the relevant SQL mode,or you can query `INFORMATION_SCHEMA` for the information:

```
SELECT ROUTINE_SCHEMA, ROUTINE_NAME, SQL_MODE
FROM INFORMATION_SCHEMA.ROUTINES;
```

For triggers, you can use this statement:

```
SELECT EVENT_OBJECT_SCHEMA, EVENT_OBJECT_TABLE, TRIGGER_NAME, SQL_MODE
FROM INFORMATION_SCHEMA.TRIGGERS;
```

- For performance-related bugs or problems with `SELECT` statements, you should always include the

output of `EXPLAIN SELECT ...`, and at least the number of rows that the `SELECT` statement produces.

You should also include the output from `SHOW CREATE TABLE tbl_name` for each table that is involved. The more information you provide about your situation, the more likely it is that someone can help you.

The following is an example of a very good bug report. The statements are run using the `mysql`command-line tool. Note the use of the `\G` statement terminator for statements that would otherwise provide very long output lines that are difficult to read.

```
mysql> SHOW VARIABLES;
mysql> SHOW COLUMNS FROM ...\G
<output from SHOW COLUMNS>
mysql> EXPLAIN SELECT ...\G
<output from EXPLAIN>
mysql> FLUSH STATUS;
mysql> SELECT ...;
<A short version of the output from SELECT,
including the time taken to run the query>
mysql> SHOW STATUS;
<output from SHOW STATUS>
```

- If a bug or problem occurs while running `mysqld`, try to provide an input script that reproduces the

anomaly. This script should include any necessary source files. The more closely the script can reproduce your situation, the better. If you can make a reproducible test case, you should upload it to be attached to the bug report.

If you cannot provide a script, you should at least include the output from `mysqladmin variables``extended-status processlist` in your report to provide some information on how your system is performing.

- If you cannot produce a test case with only a few rows, or if the test table is too big to be included in the

bug report (more than 10 rows), you should dump your tables using `mysqldump` and create a `README`file that describes your problem. Create a compressed archive of your files using `tar` and `gzip` or `zip`.

After you initiate a bug report for our bugs database at http://bugs.mysql.com/, click the Files tab in the bug report for instructions on uploading the archive to the bugs database.

- If you believe that the MySQL server produces a strange result from a statement, include not only the

result, but also your opinion of what the result should be, and an explanation describing the basis for your opinion.

- When you provide an example of the problem, it is better to use the table names, variable names, and

so forth that exist in your actual situation than to come up with new names. The problem could be related to the name of a table or variable. These cases are rare, perhaps, but it is better to be safe than sorry.

After all, it should be easier for you to provide an example that uses your actual situation, and it is by all How to Report Bugs or Problems means better for us. If you have data that you do not want to be visible to others in the bug report, you can upload it using the Files tab as previously described. If the information is really top secret and you do not want to show it even to us, go ahead and provide an example using other names, but please regard this as the last choice.

- Include all the options given to the relevant programs, if possible. For example, indicate the options that

you use when you start the `mysqld` server, as well as the options that you use to run any MySQL client programs. The options to programs such as `mysqld` and `mysql`, and to the `configure` script, are often key to resolving problems and are very relevant. It is never a bad idea to include them. If your problem involves a program written in a language such as Perl or PHP, please include the language processor's version number, as well as the version for any modules that the program uses. For example, if you have a Perl script that uses the `DBI` and `DBD::mysql` modules, include the version numbers for Perl, `DBI`,and `DBD::mysql`.

- If your question is related to the privilege system, please include the output of `mysqladmin reload`,

and all the error messages you get when trying to connect. When you test your privileges, you should execute `mysqladmin reload version` and try to connect with the program that gives you trouble.

- If you have a patch for a bug, do include it. But do not assume that the patch is all we need, or that we

can use it, if you do not provide some necessary information such as test cases showing the bug that your patch fixes. We might find problems with your patch or we might not understand it at all. If so, we cannot use it.

If we cannot verify the exact purpose of the patch, we will not use it. Test cases help us here. Show that the patch handles all the situations that may occur. If we find a borderline case (even a rare one) where the patch will not work, it may be useless.

- Guesses about what the bug is, why it occurs, or what it depends on are usually wrong. Even the

MySQL team cannot guess such things without first using a debugger to determine the real cause of a bug.

- Indicate in your bug report that you have checked the reference manual and mail archive so that others

know you have tried to solve the problem yourself.

- If your data appears corrupt or you get errors when you access a particular table, first check your tables

with `CHECK TABLE`. If that statement reports any errors:

- The `InnoDB` crash recovery mechanism handles cleanup when the server is restarted after being

killed, so in typical operation there is no need to “repair” tables. If you encounter an error with`InnoDB` tables, restart the server and see whether the problem persists, or whether the error affected only cached data in memory. If data is corrupted on disk, consider restarting with the`innodb_force_recovery` option enabled so that you can dump the affected tables.

- For non-transactional tables, try to repair them with `REPAIR TABLE` or with `myisamchk`. See

Chapter 5, MySQL Server Administration.

If you are running Windows, please verify the value of `lower_case_table_names` using the `SHOW``VARIABLES LIKE 'lower_case_table_names'` statement. This variable affects how the server handles lettercase of database and table names. Its effect for a given value should be as described in Section 9.2.3, “Identifier Case Sensitivity”.

- If you often get corrupted tables, you should try to find out when and why this happens. In this case,

the error log in the MySQL data directory may contain some information about what happened. (This is the file with the `.err` suffix in the name.) See Section 5.4.2, “The Error Log”. Please include any relevant information from this file in your bug report. Normally `mysqld` should never corrupt a table if nothing killed it in the middle of an update. If you can find the cause of `mysqld` dying, it is much easier MySQL Standards Compliance for us to provide you with a fix for the problem. See Section B.3.1, “How to Determine What Is Causing a Problem”.

- If possible, download and install the most recent version of MySQL Server and check whether it solves

your problem. All versions of the MySQL software are thoroughly tested and should work without problems. We believe in making everything as backward-compatible as possible, and you should be able to switch MySQL versions without difficulty. See Section 2.1.2, “Which MySQL Version and Distribution to Install”.

## 1.6 MySQL Standards Compliance

This section describes how MySQL relates to the ANSI/ISO SQL standards. MySQL Server has many extensions to the SQL standard, and here you can find out what they are and how to use them. You can also find information about functionality missing from MySQL Server, and how to work around some of the differences.

The SQL standard has been evolving since 1986 and several versions exist. In this manual, “SQL-92”refers to the standard released in 1992. “SQL:1999”, “SQL:2003”, “SQL:2008”, and “SQL:2011” refer to the versions of the standard released in the corresponding years, with the last being the most recent version.

We use the phrase “the SQL standard” or “standard SQL” to mean the current version of the SQL Standard at any time.

One of our main goals with the product is to continue to work toward compliance with the SQL standard,but without sacrificing speed or reliability. We are not afraid to add extensions to SQL or support for non-SQL features if this greatly increases the usability of MySQL Server for a large segment of our user base.

The `HANDLER` interface is an example of this strategy. See Section 13.2.4, “HANDLER Statement”.

We continue to support transactional and nontransactional databases to satisfy both mission-critical 24/7 usage and heavy Web or logging usage.

MySQL Server was originally designed to work with medium-sized databases (10-100 million rows,or about 100MB per table) on small computer systems. Today MySQL Server handles terabyte-sized databases, but the code can also be compiled in a reduced version suitable for hand-held and embedded devices. The compact design of the MySQL server makes development in both directions possible without any conflicts in the source tree.

We are not targeting real-time support, although MySQL replication capabilities offer significant functionality.

MySQL supports ODBC levels 0 to 3.51.

MySQL supports high-availability database clustering using the `NDBCLUSTER` storage engine. See Chapter 18, MySQL NDB Cluster 7.3 and NDB Cluster 7.4.

We implement XML functionality which supports most of the W3C XPath standard. See Section 12.12,“XML Functions”.

> Selecting SQL Modes

The MySQL server can operate in different SQL modes, and can apply these modes differently for different clients, depending on the value of the `sql_mode` system variable. DBAs can set the global SQL mode to match site server operating requirements, and each application can set its session SQL mode to its own requirements.

Modes affect the SQL syntax MySQL supports and the data validation checks it performs. This makes it easier to use MySQL in different environments and to use MySQL together with other database servers.

Running MySQL in ANSI Mode For more information on setting the SQL mode, see Section 5.1.10, “Server SQL Modes”.

> Running MySQL in ANSI Mode

To run MySQL Server in ANSI mode, start `mysqld` with the `--ansi` option. Running the server in ANSI mode is the same as starting it with the following options:

```
--transaction-isolation=SERIALIZABLE --sql-mode=ANSI
```

To achieve the same effect at runtime, execute these two statements:

```
SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SET GLOBAL sql_mode = 'ANSI';
```

You can see that setting the `sql_mode` system variable to `'ANSI'` enables all SQL mode options that are relevant for ANSI mode as follows:

```
mysql> SET GLOBAL sql_mode='ANSI';
mysql> SELECT @@GLOBAL.sql_mode;
-> 'REAL_AS_FLOAT,PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ANSI'
```

Running the server in ANSI mode with `--ansi` is not quite the same as setting the SQL mode to `'ANSI'`because the `--ansi` option also sets the transaction isolation level.

See Section 5.1.6, “Server Command Options”.

### 1.6.1 MySQL Extensions to Standard SQL

MySQL Server supports some extensions that you are not likely to find in other SQL DBMSs. Be warned that if you use them, your code may not be portable to other SQL servers. In some cases, you can write code that includes MySQL extensions, but is still portable, by using comments of the following form:

```
/*! MySQL-specific code */
```

In this case, MySQL Server parses and executes the code within the comment as it would any other SQL statement, but other SQL servers should ignore the extensions. For example, MySQL Server recognizes the `STRAIGHT_JOIN` keyword in the following statement, but other servers do not:

```
SELECT /*! STRAIGHT_JOIN */ col1 FROM table1,table2 WHERE ...
```

If you add a version number after the ! character, the syntax within the comment is executed only if the MySQL version is greater than or equal to the specified version number. The `KEY_BLOCK_SIZE` clause in the following comment is executed only by servers from MySQL 5.1.10 or higher:

```
CREATE TABLE t1(a INT, KEY (a)) /*!50110 KEY_BLOCK_SIZE=1024 */;
```

The following descriptions list MySQL extensions, organized by category.

- Organization of data on disk

MySQL Server maps each database to a directory under the MySQL data directory, and maps tables within a database to file names in the database directory. This has a few implications:

- Database and table names are case-sensitive in MySQL Server on operating systems that

have case-sensitive file names (such as most Unix systems). See Section 9.2.3, “Identifier Case Sensitivity”.

- You can use standard system commands to back up, rename, move, delete, and copy tables that

are managed by the `MyISAM` storage engine. For example, it is possible to rename a `MyISAM` table by renaming the `.MYD`, `.MYI`, and `.frm` files to which the table corresponds. (Nevertheless, it is MySQL Extensions to Standard SQL preferable to use `RENAME TABLE` or `ALTER TABLE ... RENAME` and let the server rename the files.)

- General language syntax
- By default, strings can be enclosed by " as well as '. If the `ANSI_QUOTES` SQL mode is enabled,

strings can be enclosed only by ' and the server interprets strings enclosed by " as identifiers.

- \ is the escape character in strings.
- In SQL statements, you can access tables from different databases with the `db_name.tbl_name`

syntax. Some SQL servers provide the same functionality but call this `User space`. MySQL Server doesn't support tablespaces such as used in statements like this: `CREATE TABLE`

```
ralph.my_table ... IN my_tablespace.
```

- SQL statement syntax
- The `ANALYZE TABLE`, `CHECK TABLE`, `OPTIMIZE TABLE`, and `REPAIR TABLE` statements.
- The `CREATE DATABASE`, `DROP DATABASE`, and `ALTER DATABASE` statements. See Section 13.1.10,

“CREATE DATABASE Statement”, Section 13.1.21, “DROP DATABASE Statement”, and Section 13.1.1, “ALTER DATABASE Statement”.

- The `DO` statement.
- `EXPLAIN SELECT` to obtain a description of how tables are processed by the query optimizer.
- The `FLUSH` and `RESET` statements.
- The `SET` statement. See Section 13.7.4.1, “SET Syntax for Variable Assignment”.
- The `SHOW` statement. See Section 13.7.5, “SHOW Statements”. The information produced by many of

the MySQL-specific `SHOW` statements can be obtained in more standard fashion by using `SELECT` to query `INFORMATION_SCHEMA`. See Chapter 21, INFORMATION_SCHEMA Tables.

- Use of `LOAD DATA`. In many cases, this syntax is compatible with Oracle `LOAD DATA`. See

Section 13.2.6, “LOAD DATA Statement”.

- Use of `RENAME TABLE`. See Section 13.1.32, “RENAME TABLE Statement”.
- Use of `REPLACE` instead of `DELETE` plus `INSERT`. See Section 13.2.8, “REPLACE Statement”.

```
- Use of CHANGE col_name, DROP col_name, or DROP INDEX, IGNORE or RENAME in ALTER TABLE
```

statements. Use of multiple `ADD`, `ALTER`, `DROP`, or `CHANGE` clauses in an `ALTER TABLE` statement.

See Section 13.1.7, “ALTER TABLE Statement”.

- Use of index names, indexes on a prefix of a column, and use of `INDEX` or `KEY` in `CREATE TABLE`

statements. See Section 13.1.17, “CREATE TABLE Statement”.

- Use of `TEMPORARY` or `IF NOT EXISTS` with `CREATE TABLE`.
- Use of `IF EXISTS` with `DROP TABLE` and `DROP DATABASE`.
- The capability of dropping multiple tables with a single `DROP TABLE` statement.
- The `ORDER BY` and `LIMIT` clauses of the `UPDATE` and `DELETE` statements.

```
- INSERT INTO tbl_name SET col_name = ... syntax.
```

MySQL Extensions to Standard SQL

- The `DELAYED` clause of the `INSERT` and `REPLACE` statements.
- The `LOW_PRIORITY` clause of the `INSERT`, `REPLACE`, `DELETE`, and `UPDATE` statements.
- Use of `INTO OUTFILE` or `INTO DUMPFILE` in `SELECT` statements. See Section 13.2.9, “SELECT

Statement”.

- Options such as `STRAIGHT_JOIN` or `SQL_SMALL_RESULT` in `SELECT` statements.
- You don't need to name all selected columns in the `GROUP BY` clause. This gives better performance

for some very specific, but quite normal queries. See Section 12.19, “Aggregate Functions”.

- You can specify `ASC` and `DESC` with `GROUP BY`, not just with `ORDER BY`.
- The ability to set variables in a statement with the `:=` assignment operator. See Section 9.4, “User-

Defined Variables”.

- Data types
- The `MEDIUMINT`, `SET`, and `ENUM` data types, and the various `BLOB` and `TEXT` data types.
- The `AUTO_INCREMENT`, `BINARY`, `NULL`, `UNSIGNED`, and `ZEROFILL` data type attributes.
- Functions and operators
- To make it easier for users who migrate from other SQL environments, MySQL Server supports

aliases for many functions. For example, all string functions support both standard SQL syntax and ODBC syntax.

- MySQL Server understands the `||` and `&&` operators to mean logical OR and AND, as in the

C programming language. In MySQL Server, `||` and `OR` are synonyms, as are `&&` and `AND`.

Because of this nice syntax, MySQL Server doesn't support the standard SQL `||` operator for string concatenation; use `CONCAT()` instead. Because `CONCAT()` takes any number of arguments, it is easy to convert use of the `||` operator to MySQL Server.

- Use of `COUNT(DISTINCT value_list)` where `value_list` has more than one element.
- String comparisons are case-insensitive by default, with sort ordering determined by the collation of

the current character set, which is `latin1` (cp1252 West European) by default. To perform case-sensitive comparisons instead, you should declare your columns with the `BINARY` attribute or use the`BINARY` cast, which causes comparisons to be done using the underlying character code values rather than a lexical ordering.

- The % operator is a synonym for `MOD()`. That is, `N % M` is equivalent to `MOD(N,M)`. % is supported

for C programmers and for compatibility with PostgreSQL.

- The =, `<>`, `<=`, <, `>=`, >, `<<`, `>>`, `<=>`, `AND`, `OR`, or `LIKE` operators may be used in expressions in the

output column list (to the left of the `FROM`) in `SELECT` statements. For example:

```
mysql> SELECT col1=1 AND col2=2 FROM my_table;
```

- The `LAST_INSERT_ID()` function returns the most recent `AUTO_INCREMENT` value. See

Section 12.16, “Information Functions”.

- `LIKE` is permitted on numeric values.
- The `REGEXP` and `NOT REGEXP` extended regular expression operators.

MySQL Differences from Standard SQL

- `CONCAT()` or `CHAR()` with one argument or more than two arguments. (In MySQL Server, these

functions can take a variable number of arguments.)

```
- The BIT_COUNT(), CASE, ELT(), FROM_DAYS(), FORMAT(), IF(), PASSWORD(), ENCRYPT(),
MD5(), ENCODE(), DECODE(), PERIOD_ADD(), PERIOD_DIFF(), TO_DAYS(), and WEEKDAY()
```

functions.

- Use of `TRIM()` to trim substrings. Standard SQL supports removal of single characters only.
- The `GROUP BY` functions `STD()`, `BIT_OR()`, `BIT_AND()`, `BIT_XOR()`, and `GROUP_CONCAT()`. See

Section 12.19, “Aggregate Functions”.

### 1.6.2 MySQL Differences from Standard SQL

We try to make MySQL Server follow the ANSI SQL standard and the ODBC SQL standard, but MySQL Server performs operations differently in some cases:

- There are several differences between the MySQL and standard SQL privilege systems. For example, in

MySQL, privileges for a table are not automatically revoked when you delete a table. You must explicitly issue a `REVOKE` statement to revoke privileges for a table. For more information, see Section 13.7.1.6,“REVOKE Statement”.

- The `CAST()` function does not support cast to `REAL` or `BIGINT`. See Section 12.11, “Cast Functions and

Operators”.

#### 1.6.2.1 SELECT INTO TABLE Differences

MySQL Server doesn't support the `SELECT ... INTO TABLE` Sybase SQL extension. Instead, MySQL Server supports the `INSERT INTO ... SELECT` standard SQL syntax, which is basically the same thing.

See Section 13.2.5.1, “INSERT ... SELECT Statement”. For example:

```
INSERT INTO tbl_temp2 (fld_id)
SELECT tbl_temp1.fld_order_id
FROM tbl_temp1 WHERE tbl_temp1.fld_order_id > 100;
```

Alternatively, you can use `SELECT ... INTO OUTFILE` or `CREATE TABLE ... SELECT`.

You can use `SELECT ... INTO` with user-defined variables. The same syntax can also be used inside stored routines using cursors and local variables. See Section 13.2.9.1, “SELECT ... INTO Statement”.

#### 1.6.2.2 UPDATE Differences

If you access a column from the table to be updated in an expression, `UPDATE` uses the current value of the column. The second assignment in the following statement sets `col2` to the current (updated) `col1`value, not the original `col1` value. The result is that `col1` and `col2` have the same value. This behavior differs from standard SQL.

```
UPDATE t1 SET col1 = col1 + 1, col2 = col1;
```

#### 1.6.2.3 FOREIGN KEY Constraint Differences

The MySQL implementation of foreign key constraints differs from the SQL standard in the following key respects:

- If there are several rows in the parent table with the same referenced key value, `InnoDB` performs a

foreign key check as if the other parent rows with the same key value do not exist. For example, if you MySQL Differences from Standard SQL define a `RESTRICT` type constraint, and there is a child row with several parent rows, `InnoDB` does not permit the deletion of any of the parent rows.

- If `ON UPDATE CASCADE` or `ON UPDATE SET NULL` recurses to update the same table it has previously

updated during the same cascade, it acts like `RESTRICT`. This means that you cannot use self-referential `ON UPDATE CASCADE` or `ON UPDATE SET NULL` operations. This is to prevent infinite loops resulting from cascaded updates. A self-referential `ON DELETE SET NULL`, on the other hand, is possible, as is a self-referential `ON DELETE CASCADE`. Cascading operations may not be nested more than 15 levels deep.

- In an SQL statement that inserts, deletes, or updates many rows, foreign key constraints (like unique

constraints) are checked row-by-row. When performing foreign key checks, `InnoDB` sets shared row-level locks on child or parent records that it must examine. MySQL checks foreign key constraints immediately; the check is not deferred to transaction commit. According to the SQL standard, the default behavior should be deferred checking. That is, constraints are only checked after the entire SQL statement has been processed. This means that it is not possible to delete a row that refers to itself using a foreign key.

- No storage engine, including `InnoDB`, recognizes or enforces the `MATCH` clause used in referential-

integrity constraint definitions. Use of an explicit `MATCH` clause does not have the specified effect, and it causes `ON DELETE` and `ON UPDATE` clauses to be ignored. Specifying the `MATCH` should be avoided.

The `MATCH` clause in the SQL standard controls how `NULL` values in a composite (multiple-column)foreign key are handled when comparing to a primary key in the referenced table. MySQL essentially implements the semantics defined by `MATCH SIMPLE`, which permits a foreign key to be all or partially`NULL`. In that case, a (child table) row containing such a foreign key can be inserted even though it does not match any row in the referenced (parent) table. (It is possible to implement other semantics using triggers.)

- MySQL requires that the referenced columns be indexed for performance reasons. However, MySQL

does not enforce a requirement that the referenced columns be `UNIQUE` or be declared `NOT NULL`.

A `FOREIGN KEY` constraint that references a non-`UNIQUE` key is not standard SQL but rather an`InnoDB` extension. The `NDB` storage engine, on the other hand, requires an explicit unique key (or primary key) on any column referenced as a foreign key.

The handling of foreign key references to nonunique keys or keys that contain `NULL` values is not well defined for operations such as `UPDATE` or `DELETE CASCADE`. You are advised to use foreign keys that reference only `UNIQUE` (including `PRIMARY`) and `NOT NULL` keys.

- For storage engines that do not support foreign keys (such as `MyISAM`), MySQL Server parses and

ignores foreign key specifications.

- MySQL parses but ignores “inline `REFERENCES` specifications” (as defined in the SQL standard) where

the references are defined as part of the column specification. MySQL accepts `REFERENCES` clauses only when specified as part of a separate `FOREIGN KEY` specification.

Defining a column to use a `REFERENCES tbl_name(col_name)` clause has no actual effect and serves only as a memo or comment to you that the column which you are currently defining is intended to refer to a column in another table. It is important to realize when using this syntax that:

- MySQL does not perform any sort of check to make sure that `col_name` actually exists in `tbl_name`

(or even that `tbl_name` itself exists).

- MySQL does not perform any sort of action on `tbl_name` such as deleting rows in response to

actions taken on rows in the table which you are defining; in other words, this syntax induces no `ON`MySQL Differences from Standard SQL`DELETE` or `ON UPDATE` behavior whatsoever. (Although you can write an `ON DELETE` or `ON UPDATE`clause as part of the `REFERENCES` clause, it is also ignored.)

- This syntax creates a column; it does not create any sort of index or key.

You can use a column so created as a join column, as shown here:

```
CREATE TABLE person (
id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
name CHAR(60) NOT NULL,
PRIMARY KEY (id)
);
CREATE TABLE shirt (
id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
style ENUM('t-shirt', 'polo', 'dress') NOT NULL,
color ENUM('red', 'blue', 'orange', 'white', 'black') NOT NULL,
owner SMALLINT UNSIGNED NOT NULL REFERENCES person(id),
PRIMARY KEY (id)
);
INSERT INTO person VALUES (NULL, 'Antonio Paz');
SELECT @last := LAST_INSERT_ID();
INSERT INTO shirt VALUES
(NULL, 'polo', 'blue', @last),
(NULL, 'dress', 'white', @last),
(NULL, 't-shirt', 'blue', @last);
INSERT INTO person VALUES (NULL, 'Lilliana Angelovska');
SELECT @last := LAST_INSERT_ID();
INSERT INTO shirt VALUES
(NULL, 'dress', 'orange', @last),
(NULL, 'polo', 'red', @last),
(NULL, 'dress', 'blue', @last),
(NULL, 't-shirt', 'white', @last);
SELECT * FROM person;
+----+---------------------+
| id | name                |
+----+---------------------+
|  1 | Antonio Paz         |
|  2 | Lilliana Angelovska |
+----+---------------------+
SELECT * FROM shirt;
+----+---------+--------+-------+
| id | style   | color  | owner |
+----+---------+--------+-------+
|  1 | polo    | blue   |     1 |
|  2 | dress   | white  |     1 |
|  3 | t-shirt | blue   |     1 |
|  4 | dress   | orange |     2 |
|  5 | polo    | red    |     2 |
|  6 | dress   | blue   |     2 |
|  7 | t-shirt | white  |     2 |
+----+---------+--------+-------+
SELECT s.* FROM person p INNER JOIN shirt s
ON s.owner = p.id
WHERE p.name LIKE 'Lilliana%'
AND s.color <> 'white';
```

How MySQL Deals with Constraints

```
+----+-------+--------+-------+
| id | style | color  | owner |
+----+-------+--------+-------+
|  4 | dress | orange |     2 |
|  5 | polo  | red    |     2 |
|  6 | dress | blue   |     2 |
+----+-------+--------+-------+
```

When used in this fashion, the `REFERENCES` clause is not displayed in the output of `SHOW CREATE`

```
TABLE or DESCRIBE:
SHOW CREATE TABLE shirt\G
*************************** 1. row ***************************
Table: shirt
Create Table: CREATE TABLE `shirt` (
`id` smallint(5) unsigned NOT NULL auto_increment,
`style` enum('t-shirt','polo','dress') NOT NULL,
`color` enum('red','blue','orange','white','black') NOT NULL,
`owner` smallint(5) unsigned NOT NULL,
PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1
```

For information about foreign key constraints, see Section 13.1.17.5, “FOREIGN KEY Constraints”.

#### 1.6.2.4 '--' as the Start of a Comment

Standard SQL uses the C syntax `/* this is a comment */` for comments, and MySQL Server supports this syntax as well. MySQL also support extensions to this syntax that enable MySQL-specific SQL to be embedded in the comment, as described in Section 9.6, “Comments”.

Standard SQL uses “`--`” as a start-comment sequence. MySQL Server uses # as the start comment character. MySQL Server also supports a variant of the `--` comment style. That is, the `--` start-comment sequence must be followed by a space (or by a control character such as a newline). The space is required to prevent problems with automatically generated SQL queries that use constructs such as the following,where we automatically insert the value of the payment for `payment`:

```
UPDATE account SET credit=credit-payment
```

Consider about what happens if `payment` has a negative value such as `-1`:

```
UPDATE account SET credit=credit--1
```

`credit--1` is a valid expression in SQL, but `--` is interpreted as the start of a comment, part of the expression is discarded. The result is a statement that has a completely different meaning than intended:

```
UPDATE account SET credit=credit
```

The statement produces no change in value at all. This illustrates that permitting comments to start with `--`can have serious consequences.

Using our implementation requires a space following the `--` for it to be recognized as a start-comment sequence in MySQL Server. Therefore, `credit--1` is safe to use.

### 1.6.3 How MySQL Deals with Constraints

MySQL enables you to work both with transactional tables that permit rollback and with nontransactional tables that do not. Because of this, constraint handling is a bit different in MySQL than in other DBMSs. We must handle the case when you have inserted or updated a lot of rows in a nontransactional table for which changes cannot be rolled back when an error occurs.

How MySQL Deals with Constraints The basic philosophy is that MySQL Server tries to produce an error for anything that it can detect while parsing a statement to be executed, and tries to recover from any errors that occur while executing the statement. We do this in most cases, but not yet for all.

The options MySQL has when an error occurs are to stop the statement in the middle or to recover as well as possible from the problem and continue. By default, the server follows the latter course. This means, for example, that the server may coerce invalid values to the closest valid values.

Several SQL mode options are available to provide greater control over handling of bad data values and whether to continue statement execution or abort when errors occur. Using these options, you can configure MySQL Server to act in a more traditional fashion that is like other DBMSs that reject improper input. The SQL mode can be set globally at server startup to affect all clients. Individual clients can set the SQL mode at runtime, which enables each client to select the behavior most appropriate for its requirements. See Section 5.1.10, “Server SQL Modes”.

The following sections describe how MySQL Server handles different types of constraints.

#### 1.6.3.1 PRIMARY KEY and UNIQUE Index Constraints

Normally, errors occur for data-change statements (such as `INSERT` or `UPDATE`) that would violate primary-key, unique-key, or foreign-key constraints. If you are using a transactional storage engine such as `InnoDB`, MySQL automatically rolls back the statement. If you are using a nontransactional storage engine, MySQL stops processing the statement at the row for which the error occurred and leaves any remaining rows unprocessed.

MySQL supports an `IGNORE` keyword for `INSERT`, `UPDATE`, and so forth. If you use it, MySQL ignores primary-key or unique-key violations and continues processing with the next row. See the section for the statement that you are using (Section 13.2.5, “INSERT Statement”, Section 13.2.11, “UPDATE Statement”,and so forth).

You can get information about the number of rows actually inserted or updated with the `mysql_info()` C API function. You can also use the `SHOW WARNINGS` statement. See mysql_info(), and Section 13.7.5.41,“SHOW WARNINGS Statement”.

Only `InnoDB` tables support foreign keys. See Section 13.1.17.5, “FOREIGN KEY Constraints”.

#### 1.6.3.2 FOREIGN KEY Constraints

Foreign keys let you cross-reference related data across tables, and foreign key constraints help keep this spread-out data consistent.

MySQL supports `ON UPDATE` and `ON DELETE` foreign key references in `CREATE TABLE` and `ALTER``TABLE` statements. The available referential actions are `RESTRICT` (the default), `CASCADE`, `SET NULL`,and `NO ACTION`.

Note`NDB` does not support `ON UPDATE CASCADE` actions where the referenced column is the parent table's primary key.

`SET DEFAULT` is also supported by the MySQL Server but is currently rejected as invalid by `InnoDB` and`NDB`. Since MySQL does not support deferred constraint checking, `NO ACTION` is treated as `RESTRICT`.

For the exact syntax supported by MySQL for foreign keys, see Section 13.1.17.5, “FOREIGN KEY Constraints”.

`MATCH FULL`, `MATCH PARTIAL`, and `MATCH SIMPLE` are allowed, but their use should be avoided,as they cause the MySQL Server to ignore any `ON DELETE` or `ON UPDATE` clause used in the same How MySQL Deals with Constraints statement. `MATCH` options do not have any other effect in MySQL, which in effect enforces `MATCH SIMPLE`semantics full-time.

MySQL requires that foreign key columns be indexed; if you create a table with a foreign key constraint but no index on a given column, an index is created. Exception: NDB Cluster requires an explicit unique key(or primary key) on the foreign key column.

You can obtain information about foreign keys from the Information Schema `KEY_COLUMN_USAGE` table.

An example of a query against this table is shown here:

```
mysql> SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME
> FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
> WHERE REFERENCED_TABLE_SCHEMA IS NOT NULL;
+--------------+---------------+-------------+-----------------+
| TABLE_SCHEMA | TABLE_NAME    | COLUMN_NAME | CONSTRAINT_NAME |
+--------------+---------------+-------------+-----------------+
| fk1          | myuser        | myuser_id   | f               |
| fk1          | product_order | customer_id | f2              |
| fk1          | product_order | product_id  | f1              |
+--------------+---------------+-------------+-----------------+
3 rows in set (0.01 sec)
```

Information about foreign keys on `InnoDB` tables can also be found in the `INNODB_SYS_FOREIGN` and`INNODB_SYS_FOREIGN_COLS` tables, in the `INFORMATION_SCHEMA` database.

#### 1.6.3.3 Constraints on Invalid Data

By default, MySQL is forgiving of invalid or improper data values and coerces them to valid values for data entry. However, you can enable strict SQL mode such that the server rejects invalid values and aborts the statement in which they occur. See Section 5.1.10, “Server SQL Modes”.

This section describes the default (forgiving) behavior of MySQL, as well as the strict SQL mode and how it differs.

If you are not using strict mode, then whenever you insert an “incorrect” value into a column, such as a `NULL` into a `NOT NULL` column or a too-large numeric value into a numeric column, MySQL sets the column to the “best possible value” instead of producing an error: The following rules describe in more detail how this works:

- If you try to store an out of range value into a numeric column, MySQL Server instead stores zero, the

smallest possible value, or the largest possible value, whichever is closest to the invalid value.

- For strings, MySQL stores either the empty string or as much of the string as can be stored in the

column.

- If you try to store a string that does not start with a number into a numeric column, MySQL Server stores

0.

- Invalid values for `ENUM` and `SET` columns are handled as described in Section 1.6.3.4, “ENUM and SET

Constraints”.

- MySQL permits you to store certain incorrect date values into `DATE` and `DATETIME` columns (such

as `'2000-02-31'` or `'2000-02-00'`). In this case, when an application has not enabled strict SQL mode, it up to the application to validate the dates before storing them. If MySQL can store a date value and retrieve exactly the same value, MySQL stores it as given. If the date is totally wrong (outside the server's ability to store it), the special “zero” date value `'0000-00-00'` is stored in the column instead.

- If you try to store `NULL` into a column that doesn't take `NULL` values, an error occurs for single-

row `INSERT` statements. For multiple-row `INSERT` statements or for `INSERT INTO ... SELECT`How MySQL Deals with Constraints statements, MySQL Server stores the implicit default value for the column data type. In general, this is 0 for numeric types, the empty string (`''`) for string types, and the “zero” value for date and time types.

Implicit default values are discussed in Section 11.5, “Data Type Default Values”.

- If an `INSERT` statement specifies no value for a column, MySQL inserts its default value if the column

definition includes an explicit `DEFAULT` clause. If the definition has no such `DEFAULT` clause, MySQL inserts the implicit default value for the column data type.

The reason for using the preceding rules when strict mode is not in effect is that we cannot check these conditions until the statement has begun executing. We cannot just roll back if we encounter a problem after updating a few rows, because the storage engine may not support rollback. The option of terminating the statement is not that good; in this case, the update would be “half done,” which is probably the worst possible scenario. In this case, it is better to “do the best you can” and then continue as if nothing happened.

You can select stricter treatment of input values by using the `STRICT_TRANS_TABLES` or`STRICT_ALL_TABLES` SQL modes:

```
SET sql_mode = 'STRICT_TRANS_TABLES';
SET sql_mode = 'STRICT_ALL_TABLES';
```

`STRICT_TRANS_TABLES` enables strict mode for transactional storage engines, and also to some extent for nontransactional engines. It works like this:

- For transactional storage engines, bad data values occurring anywhere in a statement cause the

statement to abort and roll back.

- For nontransactional storage engines, a statement aborts if the error occurs in the first row to be inserted

or updated. (When the error occurs in the first row, the statement can be aborted to leave the table unchanged, just as for a transactional table.) Errors in rows after the first do not abort the statement,because the table has already been changed by the first row. Instead, bad data values are adjusted and result in warnings rather than errors. In other words, with `STRICT_TRANS_TABLES`, a wrong value causes MySQL to roll back all updates done so far, if that can be done without changing the table. But once the table has been changed, further errors result in adjustments and warnings.

For even stricter checking, enable `STRICT_ALL_TABLES`. This is the same as `STRICT_TRANS_TABLES`except that for nontransactional storage engines, errors abort the statement even for bad data in rows following the first row. This means that if an error occurs partway through a multiple-row insert or update for a nontransactional table, a partial update results. Earlier rows are inserted or updated, but those from the point of the error on are not. To avoid this for nontransactional tables, either use single-row statements or else use `STRICT_TRANS_TABLES` if conversion warnings rather than errors are acceptable. To avoid problems in the first place, do not use MySQL to check column content. It is safest (and often faster) to let the application ensure that it passes only valid values to the database.

With either of the strict mode options, you can cause errors to be treated as warnings by using `INSERT``IGNORE` or `UPDATE IGNORE` rather than `INSERT` or `UPDATE` without `IGNORE`.

#### 1.6.3.4 ENUM and SET Constraints

`ENUM` and `SET` columns provide an efficient way to define columns that can contain only a given set of values. See Section 11.3.5, “The ENUM Type”, and Section 11.3.6, “The SET Type”.

With strict mode enabled (see Section 5.1.10, “Server SQL Modes”), the definition of a `ENUM` or `SET`column acts as a constraint on values entered into the column. An error occurs for values that do not satisfy these conditions:Credits

- An `ENUM` value must be one of those listed in the column definition, or the internal numeric equivalent

thereof. The value cannot be the error value (that is, 0 or the empty string). For a column defined as`ENUM('a','b','c')`, values such as `''`, `'d'`, or `'ax'` are invalid and are rejected.

- A `SET` value must be the empty string or a value consisting only of the values listed in the column

definition separated by commas. For a column defined as `SET('a','b','c')`, values such as `'d'` or`'a,b,c,d'` are invalid and are rejected.

Errors for invalid values can be suppressed in strict mode if you use `INSERT IGNORE` or `UPDATE``IGNORE`. In this case, a warning is generated rather than an error. For `ENUM`, the value is inserted as the error member (0). For `SET`, the value is inserted as given except that any invalid substrings are deleted.

For example, `'a,x,b,y'` results in a value of `'a,b'`.

## 1.7 Credits

The following sections list developers, contributors, and supporters that have helped to make MySQL what it is today.

### 1.7.1 Contributors to MySQL

Although Oracle Corporation and/or its affiliates own all copyrights in the `MySQL server` and the `MySQL``manual`, we wish to recognize those who have made contributions of one kind or another to the `MySQL``distribution`. Contributors are listed here, in somewhat random order:

- Gianmassimo Vigazzola `<qwerg@mbox.vol.it>` or `<qwerg@tin.it>`

The initial port to Win32/NT.

- Per Eric Olsson

For constructive criticism and real testing of the dynamic record format.

- Irena Pancirov `<irena@mail.yacc.it>`

Win32 port with Borland compiler. `mysqlshutdown.exe` and `mysqlwatch.exe`.

- David J. Hughes

For the effort to make a shareware SQL database. At TcX, the predecessor of MySQL AB, we started with `mSQL`, but found that it couldn't satisfy our purposes so instead we wrote an SQL interface to our application builder Unireg. `mysqladmin` and `mysql` client are programs that were largely influenced by their `mSQL` counterparts. We have put a lot of effort into making the MySQL syntax a superset of`mSQL`. Many of the API's ideas are borrowed from `mSQL` to make it easy to port free `mSQL` programs to the MySQL API. The MySQL software doesn't contain any code from `mSQL`. Two files in the distribution (`client/insert_test.c` and `client/select_test.c`) are based on the corresponding(noncopyrighted) files in the `mSQL` distribution, but are modified as examples showing the changes necessary to convert code from `mSQL` to MySQL Server. (`mSQL` is copyrighted David J. Hughes.)

- Patrick Lynch

For helping us acquire http://www.mysql.com/.

- Fred Lindberg

For setting up qmail to handle the MySQL mailing list and for the incredible help we got in managing the MySQL mailing lists.

Contributors to MySQL

- Igor Romanenko `<igor@frog.kiev.ua>`

`mysqldump` (previously `msqldump`, but ported and enhanced by Monty).

- Yuri Dario

For keeping up and extending the MySQL OS/2 port.

- Tim Bunce

Author of `mysqlhotcopy`.

- Zarko Mocnik `<zarko.mocnik@dem.si>`

Sorting for Slovenian language.

- "TAMITO" `<tommy@valley.ne.jp>`

The `_MB` character set macros and the ujis and sjis character sets.

- Joshua Chamas `<joshua@chamas.com>`

Base for concurrent insert, extended date syntax, debugging on NT, and answering on the MySQL mailing list.

- Yves Carlier `<Yves.Carlier@rug.ac.be>`

`mysqlaccess`, a program to show the access rights for a user.

- Rhys Jones `<rhys@wales.com>` (And GWE Technologies Limited)

For one of the early JDBC drivers.

- Dr Xiaokun Kelvin ZHU `<X.Zhu@brad.ac.uk>`

Further development of one of the early JDBC drivers and other MySQL-related Java tools.

- James Cooper `<pixel@organic.com>`

For setting up a searchable mailing list archive at his site.

- Rick Mehalick `<Rick_Mehalick@i-o.com>`

For `xmysql`, a graphical X client for MySQL Server.

- Doug Sisk `<sisk@wix.com>`

For providing RPM packages of MySQL for Red Hat Linux.

- Diemand Alexander V. `<axeld@vial.ethz.ch>`

For providing RPM packages of MySQL for Red Hat Linux-Alpha.

- Antoni Pamies Olive `<toni@readysoft.es>`

For providing RPM versions of a lot of MySQL clients for Intel and SPARC.

- Jay Bloodworth `<jay@pathways.sde.state.sc.us>`

For providing RPM versions for MySQL 3.21.

Contributors to MySQL

- David Sacerdote `<davids@secnet.com>`

Ideas for secure checking of DNS host names.

- Wei-Jou Chen `<jou@nematic.ieo.nctu.edu.tw>`

Some support for Chinese(BIG5) characters.

```
- Wei He <hewei@mail.ied.ac.cn>
```

A lot of functionality for the Chinese(GBK) character set.

- Jan Pazdziora `<adelton@fi.muni.cz>`

Czech sorting order.

- Zeev Suraski `<bourbon@netvision.net.il>`

`FROM_UNIXTIME()` time formatting, `ENCRYPT()` functions, and `bison` advisor. Active mailing list member.

- Luuk de Boer `<luuk@wxs.nl>`

Ported (and extended) the benchmark suite to `DBI`/`DBD`. Have been of great help with `crash-me` and running benchmarks. Some new date functions. The `mysql_setpermission` script.

- Alexis Mikhailov `<root@medinf.chuvashia.su>`

Loadable functions; `CREATE FUNCTION` and `DROP FUNCTION`.

- Andreas F. Bobak `<bobak@relog.ch>`

The `AGGREGATE` extension to loadable functions.

- Ross Wakelin `<R.Wakelin@march.co.uk>`

Help to set up InstallShield for MySQL-Win32.

- Jethro Wright III `<jetman@li.net>`

The `libmysql.dll` library.

- James Pereria `<jpereira@iafrica.com>`

Mysqlmanager, a Win32 GUI tool for administering MySQL Servers.

- Curt Sampson `<cjs@portal.ca>`

Porting of MIT-pthreads to NetBSD/Alpha and NetBSD 1.3/i386.

- Martin Ramsch `<m.ramsch@computer.org>`

Examples in the MySQL Tutorial.

- Steve Harvey

For making `mysqlaccess` more secure.

- Konark IA-64 Centre of Persistent Systems Private Limited

Contributors to MySQL Help with the Win64 port of the MySQL server.

- Albert Chin-A-Young.

Configure updates for Tru64, large file support and better TCP wrappers support.

- John Birrell

Emulation of `pthread_mutex()` for OS/2.

- Benjamin Pflugmann

Extended `MERGE` tables to handle `INSERTS`. Active member on the MySQL mailing lists.

- Jocelyn Fournier

Excellent spotting and reporting innumerable bugs (especially in the MySQL 4.1 subquery code).

- Marc Liyanage

Maintaining the OS X packages and providing invaluable feedback on how to create OS X packages.

- Robert Rutherford

Providing invaluable information and feedback about the QNX port.

- Previous developers of NDB Cluster

Lots of people were involved in various ways summer students, master thesis students, employees. In total more than 100 people so too many to mention here. Notable name is Ataullah Dabaghi who up until 1999 contributed around a third of the code base. A special thanks also to developers of the AXE system which provided much of the architectural foundations for NDB Cluster with blocks, signals and crash tracing functionality. Also credit should be given to those who believed in the ideas enough to allocate of their budgets for its development from 1992 to present time.

- Google Inc.

We wish to recognize Google Inc. for contributions to the MySQL distribution: Mark Callaghan's SMP Performance patches and other patches.

Other contributors, bugfinders, and testers: James H. Thompson, Maurizio Menghini, Wojciech Tryc, Luca Berra, Zarko Mocnik, Wim Bonis, Elmar Haneke, `<jehamby@lightside>`,

```
<psmith@BayNetworks.com>, <duane@connect.com.au>, Ted Deppner <ted@psyber.com>, Mike
```

Simons, Jaakko Hyvatti.

And lots of bug report/patches from the folks on the mailing list.

A big tribute goes to those that help us answer questions on the MySQL mailing lists:

- Daniel Koch `<dkoch@amcity.com>`

Irix setup.

- Luuk de Boer `<luuk@wxs.nl>`

Benchmark questions.

- Tim Sailer `<tps@users.buoy.com>`

Documenters and translators`DBD::mysql` questions.

- Boyd Lynn Gerber `<gerberb@zenez.com>`

SCO-related questions.

- Richard Mehalick `<RM186061@shellus.com>`

`xmysql`-related questions and basic installation questions.

- Zeev Suraski `<bourbon@netvision.net.il>`

Apache module configuration questions (log & auth), PHP-related questions, SQL syntax-related questions and other general questions.

- Francesc Guasch `<frankie@citel.upc.es>`

General questions.

- Jonathan J Smith `<jsmith@wtp.net>`

Questions pertaining to OS-specifics with Linux, SQL syntax, and other things that might need some work.

- David Sklar `<sklar@student.net>`

Using MySQL from PHP and Perl.

- Alistair MacDonald `<A.MacDonald@uel.ac.uk>`

Is flexible and can handle Linux and perhaps HP-UX.

- John Lyon `<jlyon@imag.net>`

Questions about installing MySQL on Linux systems, using either `.rpm` files or compiling from source.

- Lorvid Ltd. `<lorvid@WOLFENET.com>`

Simple billing/license/support/copyright issues.

- Patrick Sherrill `<patrick@coconet.com>`

ODBC and VisualC++ interface questions.

- Randy Harmon `<rjharmon@uptimecomputers.com>`

`DBD`, Linux, some SQL syntax questions.

### 1.7.2 Documenters and translators

The following people have helped us with writing the MySQL documentation and translating the documentation or error messages in MySQL.

- Kim Aldale

Helped to rewrite Monty's and David's early attempts at English into English.

- Michael J. Miller Jr. `<mke@terrapin.turbolift.com>`

Documenters and translators For the first MySQL manual. And a lot of spelling/language fixes for the FAQ (that turned into the MySQL manual a long time ago).

- Yan Cailin

First translator of the MySQL Reference Manual into simplified Chinese in early 2000 on which the Big5 and HK coded versions were based.

- Jay Flaherty `<fty@mediapulse.com>`

Big parts of the Perl `DBI`/`DBD` section in the manual.

- Paul Southworth `<pauls@etext.org>`, Ray Loyzaga `<yar@cs.su.oz.au>`

Proof-reading of the Reference Manual.

- Therrien Gilbert `<gilbert@ican.net>`, Jean-Marc Pouyot `<jmp@scalaire.fr>`

French error messages.

- Petr Snajdr, `<snajdr@pvt.net>`

Czech error messages.

- Jaroslaw Lewandowski `<jotel@itnet.com.pl>`

Polish error messages.

- Miguel Angel Fernandez Roiz

Spanish error messages.

- Roy-Magne Mo `<rmo@www.hivolda.no>`

Norwegian error messages and testing of MySQL 3.21.xx.

- Timur I. Bakeyev `<root@timur.tatarstan.ru>`

Russian error messages.

- `<brenno@dewinter.com>` & Filippo Grassilli `<phil@hyppo.com>`

Italian error messages.

- Dirk Munzinger `<dirk@trinity.saar.de>`

German error messages.

- Billik Stefan `<billik@sun.uniag.sk>`

Slovak error messages.

- Stefan Saroiu `<tzoompy@cs.washington.edu>`

Romanian error messages.

- Peter Feher

Hungarian error messages.

Packages that support MySQL

- Roberto M. Serqueira

Portuguese error messages.

- Carsten H. Pedersen

Danish error messages.

- Arjen Lentz

Dutch error messages, completing earlier partial translation (also work on consistency and spelling).

### 1.7.3 Packages that support MySQL

The following is a list of creators/maintainers of some of the most important API/packages/applications that a lot of people use with MySQL.

We cannot list every possible package here because the list would then be way to hard to maintain. For other packages, please refer to the software portal at http://solutions.mysql.com/software/.

- Tim Bunce, Alligator Descartes

For the `DBD` (Perl) interface.

- Andreas Koenig `<a.koenig@mind.de>`

For the Perl interface for MySQL Server.

- Jochen Wiedmann `<wiedmann@neckar-alb.de>`

For maintaining the Perl `DBD::mysql` module.

- Eugene Chan `<eugene@acenet.com.sg>`

For porting PHP for MySQL Server.

- Georg Richter

MySQL 4.1 testing and bug hunting. New PHP 5.0 `mysqli` extension (API) for use with MySQL 4.1 and up.

- Giovanni Maruzzelli `<maruzz@matrice.it>`

For porting iODBC (Unix ODBC).

- Xavier Leroy `<Xavier.Leroy@inria.fr>`

The author of LinuxThreads (used by the MySQL Server on Linux).

### 1.7.4 Tools that were used to create MySQL

The following is a list of some of the tools we have used to create MySQL. We use this to express our thanks to those that has created them as without these we could not have made MySQL what it is today.

- Free Software Foundation

From whom we got an excellent compiler (`gcc`), an excellent debugger (`gdb` and the `libc` library (from which we have borrowed `strto.c` to get some code working in Linux).

Supporters of MySQL

- Free Software Foundation & The XEmacs development team

For a really great editor/environment.

- Julian Seward

Author of `valgrind`, an excellent memory checker tool that has helped us find a lot of otherwise hard to find bugs in MySQL.

- Dorothea Lütkehaus and Andreas Zeller

For `DDD` (The Data Display Debugger) which is an excellent graphical front end to `gdb`).

### 1.7.5 Supporters of MySQL

Although Oracle Corporation and/or its affiliates own all copyrights in the `MySQL server` and the `MySQL``manual`, we wish to recognize the following companies, which helped us finance the development of the`MySQL server`, such as by paying us for developing a new feature or giving us hardware for development of the `MySQL server`.

- VA Linux / Andover.net

Funded replication.

- NuSphere

Editing of the MySQL manual.

- Stork Design studio

The MySQL website in use between 1998-2000.

- Intel

Contributed to development on Windows and Linux platforms.

- Compaq

Contributed to Development on Linux/Alpha.

- SWSoft

Development on the embedded `mysqld` version.

- FutureQuest

The `--skip-show-database` option.
