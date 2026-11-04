---
title: "4.7.1 mysql_config — Display Options for Compiling Clients"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-config.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 4.7.1 mysql\_config — Display Options for Compiling Clients

**mysql\_config** provides you with useful information for compiling your MySQL client and connecting it to MySQL. It is a shell script, so it is available only on Unix and Unix-like systems.

Note

As of MySQL 5.7.9, **pkg-config** can be used as an alternative to **mysql\_config** for obtaining information such as compiler flags or link libraries required to compile MySQL applications. For more information, see [Building C API Client Programs Using pkg-config](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/c-api-building-clients-pkg-config.html).

Note

As of MySQL 5.7.4, for binary distributions for Solaris, **mysql\_config** does not provide arguments for linking with the embedded library. To get linking arguments for the embedded library, use the **mysql\_server\_config** script instead.

**mysql\_config** supports the following options.

- `--cflags`
	C Compiler flags to find include files and critical compiler flags and defines used when compiling the `libmysqlclient` library. The options returned are tied to the specific compiler that was used when the library was created and might clash with the settings for your own compiler. Use `--include` for more portable options that contain only include paths.
- `--cxxflags`
	Like `--cflags`, but for C++ compiler flags.
- `--include`
	Compiler options to find MySQL include files.
- `--libmysqld-libs`, `--embedded-libs`, `--embedded`
	Libraries and options required to link with `libmysqld`, the MySQL embedded server.
	Note
	The `libmysqld` embedded server library is deprecated as of MySQL 5.7.19 and has been removed in MySQL 8.0.
- `--libs`
	Libraries and options required to link with the MySQL client library.
- `--libs_r`
	Libraries and options required to link with the thread-safe MySQL client library. In MySQL 5.7, all client libraries are thread-safe, so this option need not be used. The `--libs` option can be used in all cases.
- `--plugindir`
	The default plugin directory path name, defined when configuring MySQL.
- `--port`
	The default TCP/IP port number, defined when configuring MySQL.
- `--socket`
	The default Unix socket file, defined when configuring MySQL.
- ``--variable=*`var_name`*``
	Display the value of the named configuration variable. Permitted *`var_name`* values are `pkgincludedir` (the header file directory), `pkglibdir` (the library directory), and `plugindir` (the plugin directory).
- `--version`
	Version number for the MySQL distribution.

If you invoke **mysql\_config** with no options, it displays a list of all options that it supports, and their values:

```
$> mysql_config
Usage: /usr/local/mysql/bin/mysql_config [options]
Options:
  --cflags         [-I/usr/local/mysql/include/mysql -mcpu=pentiumpro]
  --cxxflags       [-I/usr/local/mysql/include/mysql -mcpu=pentiumpro]
  --include        [-I/usr/local/mysql/include/mysql]
  --libs           [-L/usr/local/mysql/lib/mysql -lmysqlclient
                    -lpthread -lm -lrt -lssl -lcrypto -ldl]
  --libs_r         [-L/usr/local/mysql/lib/mysql -lmysqlclient_r
                    -lpthread -lm -lrt -lssl -lcrypto -ldl]
  --plugindir      [/usr/local/mysql/lib/plugin]
  --socket         [/tmp/mysql.sock]
  --port           [3306]
  --version        [5.7.9]
  --libmysqld-libs [-L/usr/local/mysql/lib/mysql -lmysqld
                    -lpthread -lm -lrt -lssl -lcrypto -ldl -lcrypt]
  --variable=VAR   VAR is one of:
          pkgincludedir [/usr/local/mysql/include]
          pkglibdir     [/usr/local/mysql/lib]
          plugindir     [/usr/local/mysql/lib/plugin]
```

You can use **mysql\_config** within a command line using backticks to include the output that it produces for particular options. For example, to compile and link a MySQL client program, use **mysql\_config** as follows:

```
gcc -c \`mysql_config --cflags\` progname.c
gcc -o progname progname.o \`mysql_config --libs\`
```