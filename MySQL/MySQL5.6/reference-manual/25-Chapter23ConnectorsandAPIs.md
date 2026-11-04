---
title: Chapter 23 Connectors and APIs
book: MySQL 5.6 Reference Manual
version: "5.6"
source: "MySQL/MySQL5.6/sources/refman-5.6-en.pdf#page=3511"
tags:
  - mysql
  - mysql-5.6
  - reference-manual
---

## Table of Contents

23.1 MySQL Connector/C++ ......................................................................................................... 3486

23.2 MySQL Connector/J .............................................................................................................. 3486

23.3 MySQL Connector/NET ......................................................................................................... 3486

23.4 MySQL Connector/ODBC ...................................................................................................... 3486

23.5 MySQL Connector/Python ..................................................................................................... 3486

23.6 libmysqld, the Embedded MySQL Server Library .................................................................... 3487

23.6.1 Compiling Programs with libmysqld ............................................................................. 3487

23.6.2 Restrictions When Using the Embedded MySQL Server ............................................... 3488

23.6.3 Options with the Embedded Server ............................................................................. 3488

23.6.4 Embedded Server Examples ....................................................................................... 3489

23.7 MySQL C API ....................................................................................................................... 3492

23.8 MySQL PHP API .................................................................................................................. 3492

23.9 MySQL Perl API ................................................................................................................... 3492

23.10 MySQL Python API ............................................................................................................. 3493

23.11 MySQL Ruby APIs .............................................................................................................. 3493

23.11.1 The MySQL/Ruby API .............................................................................................. 3494

23.11.2 The Ruby/MySQL API .............................................................................................. 3494

23.12 MySQL Tcl API ................................................................................................................... 3494

23.13 MySQL Eiffel Wrapper ......................................................................................................... 3494 MySQL Connectors provide connectivity to the MySQL server for client programs. APIs provide low-level access to the MySQL protocol and MySQL resources. Both Connectors and the APIs enable you to connect and execute MySQL statements from another language or environment, including ODBC, Java(JDBC), Perl, Python, PHP, Ruby, and native C and embedded MySQL instances.

> MySQL Connectors

Oracle develops a number of connectors:

- Connector/C++ enables C++ applications to connect to MySQL.
- Connector/J provides driver support for connecting to MySQL from Java applications using the standard

Java Database Connectivity (JDBC) API.

- Connector/NET enables developers to create .NET applications that connect to MySQL. Connector/NET

implements a fully functional ADO.NET interface and provides support for use with ADO.NET aware tools. Applications that use Connector/NET can be written in any supported .NET language.

MySQL for Visual Studio works with Connector/NET and Microsoft Visual Studio 2012, 2013, 2015,and 2017. MySQL for Visual Studio provides access to MySQL objects and data from Visual Studio. As a Visual Studio package, it integrates directly into Server Explorer providing the ability to create new connections and work with MySQL database objects.

- Connector/ODBC provides driver support for connecting to MySQL using the Open Database

Connectivity (ODBC) API. Support is available for ODBC connectivity from Windows, Unix, and macOS platforms.

- Connector/Python provides driver support for connecting to MySQL from Python applications using an

API that is compliant with the Python DB API version 2.0. No additional Python modules or MySQL client libraries are required.

The MySQL C API

> The MySQL C API

For direct access to using MySQL natively within a C application, there are two methods:

- The C API provides low-level access to the MySQL client/server protocol through the `libmysqlclient`

client library. This is the primary method used to connect to an instance of the MySQL server, and is used both by MySQL command-line clients and many of the MySQL Connectors and third-party APIs detailed here.

`libmysqlclient` is included in MySQL distributions.

- `libmysqld` is an embedded MySQL server library that enables you to embed an instance of the MySQL

server into your C applications.

`libmysqld` is included in MySQL distributions.

See also MySQL C API Implementations.

To access MySQL from a C application, or to build an interface to MySQL for a language not supported by the Connectors or APIs in this chapter, the C API is where to start. A number of programmer's utilities are available to help with the process; see Section 4.7, “Program Development Utilities”.

> Third-Party MySQL APIs

The remaining APIs described in this chapter provide an interface to MySQL from specific application languages. These third-party solutions are not developed or supported by Oracle. Basic information on their usage and abilities is provided here for reference purposes only.

All the third-party language APIs are developed using one of two methods, using `libmysqlclient` or by implementing a native driver. The two solutions offer different benefits:

- Using `libmysqlclient` offers complete compatibility with MySQL because it uses the same libraries

as the MySQL client applications. However, the feature set is limited to the implementation and interfaces exposed through `libmysqlclient` and the performance may be lower as data is copied between the native language, and the MySQL API components.

- Native drivers are an implementation of the MySQL network protocol entirely within the host language

or environment. Native drivers are fast, as there is less copying of data between components, and they can offer advanced functionality not available through the standard MySQL API. Native drivers are also easier for end users to build and deploy because no copy of the MySQL client libraries is needed to build the native driver components.

Table 23.1, “MySQL APIs and Interfaces” lists many of the libraries and interfaces available for MySQL.

Table 23.1 MySQL APIs and Interfaces Environment API Type Notes Ada GNU Ada MySQL `libmysqlclient` See MySQL Bindings for Bindings GNU Ada C C API `libmysqlclient` See MySQL 5.6 C API Developer Guide.

C++ Connector/C++ `libmysqlclient` See MySQL Connector/C++ 8.0 Developer Guide.

MySQL++ `libmysqlclient` See MySQL++ website.

Third-Party MySQL APIs Environment API Type Notes MySQL wrapped `libmysqlclient` See MySQL wrapped.

Cocoa MySQL-Cocoa `libmysqlclient` Compatible with the Objective-C Cocoa environment.

See http://mysql-cocoa.sourceforge.net/D MySQL for D `libmysqlclient` See MySQL for D.

Eiffel Eiffel MySQL `libmysqlclient` See Section 23.13,“MySQL Eiffel Wrapper”.

```
Erlang  erlang-mysql-driver libmysqlclient  See erlang-mysql-
driver.
```

Haskell Haskell MySQL Bindings Native Driver See Brian O'Sullivan's pure Haskell MySQL bindings.

`hsql-mysql` `libmysqlclient` See MySQL driver for Haskell.

Java/JDBC Connector/J Native Driver See MySQL Connector/J

8.0 Developer Guide.

Kaya MyDB `libmysqlclient` See MyDB.

Lua LuaSQL `libmysqlclient` See LuaSQL.

.NET/Mono Connector/NET Native Driver See MySQL Connector/NET Developer Guide.

Objective Caml OBjective Caml MySQL `libmysqlclient` See MySQL Bindings for Bindings Objective Caml.

Octave Database bindings for `libmysqlclient` See Database bindings GNU Octave for GNU Octave.

ODBC Connector/ODBC `libmysqlclient` See MySQL Connector/ODBC Developer Guide.

Perl `DBI`/`DBD::mysql` `libmysqlclient` See Section 23.9,“MySQL Perl API”.

`Net::MySQL` Native Driver See `Net::MySQL` at CPAN PHP `mysql`, `ext/mysql` `libmysqlclient` See MySQL and PHP.

interface (deprecated)`mysqli`, `ext/mysqli` `libmysqlclient` See MySQL and PHP.

interface`PDO_MYSQL` `libmysqlclient` See MySQL and PHP.

PDO mysqlnd Native Driver Python Connector/Python Native Driver See MySQL Connector/Python Developer Guide.

Python Connector/Python C `libmysqlclient` See MySQL Connector/Extension Python Developer Guide.

MySQLdb `libmysqlclient` See Section 23.10,“MySQL Python API”.

MySQL Connector/C++Environment API Type Notes Ruby mysql2 `libmysqlclient` Uses `libmysqlclient`.

See Section 23.11,“MySQL Ruby APIs”.

Scheme `Myscsh` `libmysqlclient` See `Myscsh`.

SPL `sql_mysql` `libmysqlclient` See `sql_mysql` for SPL.

Tcl MySQLtcl `libmysqlclient` See Section 23.12,“MySQL Tcl API”.

## 23.1 MySQL Connector/C++

The MySQL Connector/C++ manual is published in standalone form, not as part of the MySQL Reference Manual. For information, see these documents:

- Main manual: MySQL Connector/C++ 8.0 Developer Guide
- Release notes: MySQL Connector/C++ Release Notes

## 23.2 MySQL Connector/J

The MySQL Connector/J manual is published in standalone form, not as part of the MySQL Reference Manual. For information, see these documents:

- Main manual: MySQL Connector/J Developer Guide
- Release notes: MySQL Connector/J Release Notes

## 23.3 MySQL Connector/NET

The MySQL Connector/NET manual is published in standalone form, not as part of the MySQL Reference Manual. For information, see these documents:

- Main manual: MySQL Connector/NET Developer Guide
- Release notes: MySQL Connector/NET Release Notes

## 23.4 MySQL Connector/ODBC

The MySQL Connector/ODBC manual is published in standalone form, not as part of the MySQL Reference Manual. For information, see these documents:

- Main manual: MySQL Connector/ODBC Developer Guide
- Release notes: MySQL Connector/ODBC Release Notes

## 23.5 MySQL Connector/Python

The MySQL Connector/Python manual is published in standalone form, not as part of the MySQL Reference Manual. For information, see these documents:

- Main manual: MySQL Connector/Python Developer Guide

libmysqld, the Embedded MySQL Server Library

- Release notes: MySQL Connector/Python Release Notes

## 23.6 libmysqld, the Embedded MySQL Server Library

The embedded MySQL server library makes it possible to run a full-featured MySQL server inside a client application. The main benefits are increased speed and more simple management for embedded applications.

The embedded server library is based on the client/server version of MySQL, which is written in C/C++.

Consequently, the embedded server also is written in C/C++. There is no embedded server available in other languages.

The API is identical for the embedded MySQL version and the client/server version. To change a threaded application to use the embedded library, you normally only have to add calls to the following functions.

Table 23.2 MySQL Embedded Server Library Functions Function When to Call`mysql_library_init()` Call it before any other MySQL function is called,preferably early in the `main()` function.

`mysql_library_end()` Call it before your program exits.

`mysql_thread_init()` Call it in each thread you create that accesses MySQL.

`mysql_thread_end()` Call it before calling `pthread_exit()`.

Then, link your code with `libmysqld.a` instead of `libmysqlclient.a`. To ensure binary compatibility between your application and the server library, always compile your application against headers for the same series of MySQL that was used to compile the server library. For example, if `libmysqld` was compiled against MySQL 5.5 headers, do not compile your application against MySQL 5.6 headers, or vice versa.

Because the `mysql_library_xxx()` functions are also included in `libmysqlclient.a`, you can change between the embedded and the client/server version by just linking your application with the right library. See mysql_library_init().

One difference between the embedded server and the standalone server is that for the embedded server,authentication for connections is disabled by default.

### 23.6.1 Compiling Programs with libmysqld

In precompiled binary MySQL distributions that include `libmysqld`, the embedded server library, MySQL builds the library using the appropriate vendor compiler if there is one.

To get a `libmysqld` library if you build MySQL from source yourself, you should configure MySQL with the `-DWITH_EMBEDDED_SERVER=1` option. See Section 2.9.7, “MySQL Source-Configuration Options”.

When you link your program with `libmysqld`, you must also include the system-specific `pthread`libraries and some libraries that the MySQL server uses. You can get the full list of libraries by executing

```
mysql_config --libmysqld-libs.
```

The correct flags for compiling and linking a threaded program must be used, even if you do not directly call any thread functions in your code.

Restrictions When Using the Embedded MySQL Server To compile a C program to include the necessary files to embed the MySQL server library into an executable version of a program, the compiler needs to know where to find various files and needs instructions on how to compile the program. The following example shows how a program could be compiled from the command line, assuming that you are using `gcc`, use the GNU C compiler:

```
gcc mysql_test.c -o mysql_test \
`/usr/local/mysql/bin/mysql_config --include --libmysqld-libs`
```

Immediately following the `gcc` command is the name of the C program source file. After it, the `-o` option is given to indicate that the file name that follows is the name that the compiler is to give to the output file,the compiled program. The next line of code tells the compiler to obtain the location of the include files and libraries and other settings for the system on which it is compiled. The `mysql_config` command is contained in backticks, not single quotation marks.

On some non-`gcc` platforms, the embedded library depends on C++ runtime libraries and linking against the embedded library might result in missing-symbol errors. To solve this, link using a C++ compiler or explicitly list the required libraries on the link command line.

### 23.6.2 Restrictions When Using the Embedded MySQL Server

The embedded server has the following limitations:

- No loadable functions.
- No stack trace on core dump.
- You cannot set this up as a source or a replica (no replication).
- Very large result sets may be unusable on low memory systems.
- You cannot connect to an embedded server from an outside process with sockets or TCP/IP. However,

you can connect to an intermediate application, which in turn can connect to an embedded server on the behalf of a remote client or outside process.

- `libmysqld` does not support encrypted connections. An implication is that if an application linked

against `libmysqld` establishes a connection to a remote server, the connection cannot be encrypted.

- `InnoDB` is not reentrant in the embedded server and cannot be used for multiple connections, either

successively or simultaneously.

- The Event Scheduler is not available. Because of this, the `event_scheduler` system variable is

disabled.

- The Performance Schema is not available.

Some of these limitations can be changed by editing the `mysql_embed.h` include file and recompiling MySQL.

### 23.6.3 Options with the Embedded Server

Any options that may be given with the `mysqld` server daemon, may be used with an embedded server library. Server options may be given in an array as an argument to the `mysql_library_init()`,which initializes the server. They also may be given in an option file like `my.cnf`. To specify an option file for a C program, use the `--defaults-file` option as one of the elements of the second argument of the `mysql_library_init()` function. See mysql_library_init(), for more information on the`mysql_library_init()` function.

Embedded Server Examples Using option files can make it easier to switch between a client/server application and one where MySQL is embedded. Put common options under the `[server]` group. These are read by both MySQL versions.

Client/server-specific options should go under the `[mysqld]` section. Put options specific to the embedded MySQL server library in the `[embedded]` section. Options specific to applications go under section labeled`[ApplicationName_SERVER]`. See Section 4.2.2.2, “Using Option Files”.

### 23.6.4 Embedded Server Examples

These two example programs should work without any changes on a Linux or FreeBSD system. For other operating systems, minor changes are needed, mostly with file paths. These examples are designed to give enough details for you to understand the problem, without the clutter that is a necessary part of a real application. The first example is very straightforward. The second example is a little more advanced with some error checking. The first is followed by a command-line entry for compiling the program. The second is followed by a GNUmake file that may be used for compiling instead.

> Example 1

```
test1_libmysqld.c
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include "mysql.h"
MYSQL *mysql;
MYSQL_RES *results;
MYSQL_ROW record;
static char *server_options[] = \
{ "mysql_test", "--defaults-file=my.cnf", NULL };
int num_elements = (sizeof(server_options) / sizeof(char *)) - 1;
static char *server_groups[] = { "libmysqld_server",
"libmysqld_client", NULL };
int main(void)
{
mysql_library_init(num_elements, server_options, server_groups);
mysql = mysql_init(NULL);
mysql_options(mysql, MYSQL_READ_DEFAULT_GROUP, "libmysqld_client");
mysql_options(mysql, MYSQL_OPT_USE_EMBEDDED_CONNECTION, NULL);
mysql_real_connect(mysql, NULL,NULL,NULL, "database1", 0,NULL,0);
mysql_query(mysql, "SELECT column1, column2 FROM table1");
results = mysql_store_result(mysql);
while((record = mysql_fetch_row(results))) {
printf("%s - %s \n", record[0], record[1]);
}
mysql_free_result(results);
mysql_close(mysql);
mysql_library_end();
return 0;
}
```

Here is the command line for compiling the above program:

```
gcc test1_libmysqld.c -o test1_libmysqld \
`/usr/local/mysql/bin/mysql_config --include --libmysqld-libs`
```

Embedded Server Examples Example 2 To try the example, create an `test2_libmysqld` directory at the same level as the MySQL source directory. Save the `test2_libmysqld.c` source and the `GNUmakefile` in the directory, and run GNU`make` from inside the `test2_libmysqld` directory.

```
test2_libmysqld.c
/*
* A simple example client, using the embedded MySQL server library
*/
#include <mysql.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
MYSQL *db_connect(const char *dbname);
void db_disconnect(MYSQL *db);
void db_do_query(MYSQL *db, const char *query);
const char *server_groups[] = {
"test2_libmysqld_SERVER", "embedded", "server", NULL
};
int
main(int argc, char **argv)
{
MYSQL *one, *two;
/* mysql_library_init() must be called before any other mysql
* functions.
*
* You can use mysql_library_init(0, NULL, NULL), and it
* initializes the server using groups = {
*   "server", "embedded", NULL
*  }.
*
* In your $HOME/.my.cnf file, you probably want to put:
[test2_libmysqld_SERVER]
language = /path/to/source/of/mysql/sql/share/english
* You could, of course, modify argc and argv before passing
* them to this function.  Or you could create new ones in any
* way you like.  But all of the arguments in argv (except for
* argv[0], which is the program name) should be valid options
* for the MySQL server.
*
* If you link this client against the normal mysqlclient
* library, this function is just a stub that does nothing.
*/
mysql_library_init(argc, argv, (char **)server_groups);
one = db_connect("test");
two = db_connect(NULL);
db_do_query(one, "SHOW TABLE STATUS");
db_do_query(two, "SHOW DATABASES");
mysql_close(two);
mysql_close(one);
/* This must be called after all other mysql functions */
mysql_library_end();
```

Embedded Server Examples

```
exit(EXIT_SUCCESS);
}
static void
die(MYSQL *db, char *fmt, ...)
{
va_list ap;
va_start(ap, fmt);
vfprintf(stderr, fmt, ap);
va_end(ap);
(void)putc('\n', stderr);
if (db)
db_disconnect(db);
exit(EXIT_FAILURE);
}
MYSQL *
db_connect(const char *dbname)
{
MYSQL *db = mysql_init(NULL);
if (!db)
die(db, "mysql_init failed: no memory");
/*
* Notice that the client and server use separate group names.
* This is critical, because the server does not accept the
* client's options, and vice versa.
*/
mysql_options(db, MYSQL_READ_DEFAULT_GROUP, "test2_libmysqld_CLIENT");
if (!mysql_real_connect(db, NULL, NULL, NULL, dbname, 0, NULL, 0))
die(db, "mysql_real_connect failed: %s", mysql_error(db));
return db;
}
void
db_disconnect(MYSQL *db)
{
mysql_close(db);
}
void
db_do_query(MYSQL *db, const char *query)
{
if (mysql_query(db, query) != 0)
goto err;
if (mysql_field_count(db) > 0)
{
MYSQL_RES   *res;
MYSQL_ROW    row, end_row;
int num_fields;
if (!(res = mysql_store_result(db)))
goto err;
num_fields = mysql_num_fields(res);
while ((row = mysql_fetch_row(res)))
{
(void)fputs(">> ", stdout);
for (end_row = row + num_fields; row < end_row; ++row)
(void)printf("%s\t", row ? (char*)*row : "NULL");
(void)fputc('\n', stdout);
}
(void)fputc('\n', stdout);
mysql_free_result(res);
}
else
(void)printf("Affected rows: %lld\n", mysql_affected_rows(db));
```

MySQL C API

```
return;
err:
die(db, "db_do_query failed: %s [%s]", mysql_error(db), query);
}
GNUmakefile
# This assumes the MySQL software is installed in /usr/local/mysql
inc      := /usr/local/mysql/include/mysql
lib      := /usr/local/mysql/lib
# If you have not installed the MySQL software yet, try this instead
#inc      := $(HOME)/mysql-5.6/include
#lib      := $(HOME)/mysql-5.6/libmysqld
CC       := gcc
CPPFLAGS := -I$(inc) -D_THREAD_SAFE -D_REENTRANT
CFLAGS   := -g -W -Wall
LDFLAGS  := -static
# You can change -lmysqld to -lmysqlclient to use the
# client/server library
LDLIBS    = -L$(lib) -lmysqld -lm -ldl -lcrypt
ifneq (,$(shell grep FreeBSD /COPYRIGHT 2>/dev/null))
# FreeBSD
LDFLAGS += -pthread
else
# Assume Linux
LDLIBS += -lpthread
endif
# This works for simple one-file test programs
sources := $(wildcard *.c)
objects := $(patsubst %c,%o,$(sources))
targets := $(basename $(sources))
all: $(targets)
clean:
rm -f $(targets) $(objects) *.core
```

## 23.7 MySQL C API

The MySQL C API Developer Guide is published in standalone form, not as part of the MySQL Reference Manual. See MySQL 5.6 C API Developer Guide.

## 23.8 MySQL PHP API

The MySQL PHP API manual is now published in standalone form, not as part of the MySQL Reference Manual. See MySQL and PHP.

## 23.9 MySQL Perl API

The Perl `DBI` module provides a generic interface for database access. You can write a DBI script that works with many different database engines without change. To use DBI with MySQL, install the following:

1. The `DBI` module.
2. The `DBD::mysql` module. This is the DataBase Driver (DBD) module for Perl.

MySQL Python API

3. Optionally, the DBD module for any other type of database server you want to access.

Perl DBI is the recommended Perl interface. It replaces an older interface called `mysqlperl`, which should be considered obsolete.

These sections contain information about using Perl with MySQL and writing MySQL applications in Perl:

- For installation instructions for Perl DBI support, see Section 2.13, “Perl Installation Notes”.
- For an example of reading options from option files, see Section 5.7.4, “Using Client Programs in a

Multiple-Server Environment”.

- For secure coding tips, see Section 6.1.1, “Security Guidelines”.
- For debugging tips, see Section 5.8.1.4, “Debugging mysqld under gdb”.
- For some Perl-specific environment variables, see Section 4.9, “Environment Variables”.
- For considerations for running on macOS, see Section 2.4, “Installing MySQL on macOS”.
- For ways to quote string literals, see Section 9.1.1, “String Literals”.

DBI information is available at the command line, online, or in printed form:

- Once you have the `DBI` and `DBD::mysql` modules installed, you can get information about them at the

command line with the `perldoc` command:

```
$> perldoc DBI
$> perldoc DBI::FAQ
$> perldoc DBD::mysql
```

You can also use `pod2man`, `pod2html`, and so on to translate this information into other formats.

- For online information about Perl DBI, visit the DBI website, http://dbi.perl.org/. That site hosts a general

DBI mailing list.

- For printed information, the official DBI book is Programming the Perl DBI (Alligator Descartes and Tim

Bunce, O'Reilly & Associates, 2000). Information about the book is available at the DBI website, http://dbi.perl.org/.

## 23.10 MySQL Python API

`MySQLdb` is a third-party driver that provides MySQL support for Python, compliant with the Python DB API version 2.0. It can be found at http://sourceforge.net/projects/mysql-python/.

The new MySQL Connector/Python component provides an interface to the same Python API, and is built into the MySQL Server and supported by Oracle. See MySQL Connector/Python Developer Guide for details on the Connector, as well as coding guidelines for Python applications and sample Python code.

## 23.11 MySQL Ruby APIs

The `mysql2` Ruby gem provides an API for connecting to MySQL, performing queries, and iterating through results; it is intended to support MySQL 5.6, 5.7, and 8.0. For more information, see the `mysql2`page at RubyGems.org or the project's GitHub page.

For background and syntax information about the Ruby language, see Ruby Programming Language.

The MySQL/Ruby API

### 23.11.1 The MySQL/Ruby API

The MySQL/Ruby module provides access to MySQL databases using Ruby through `libmysqlclient`.

For information on installing the module, and the functions exposed, see MySQL/Ruby.

### 23.11.2 The Ruby/MySQL API

The Ruby/MySQL module provides access to MySQL databases using Ruby through a native driver interface using the MySQL network protocol.

For information on installing the module, and the functions exposed, see Ruby/MySQL.

## 23.12 MySQL Tcl API

`MySQLtcl` is a simple API for accessing a MySQL database server from the Tcl programming language. It can be found at http://www.xdobry.de/mysqltcl/.

## 23.13 MySQL Eiffel Wrapper

Eiffel MySQL is an interface to the MySQL database server using the Eiffel programming language, written by Michael Ravits. It can be found at http://efsa.sourceforge.net/archive/ravits/mysql.htm.
