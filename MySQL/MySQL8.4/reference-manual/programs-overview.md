---
title: "6.1 Overview of MySQL Programs"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/programs-overview.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

There are many different programs in a MySQL installation. This section provides a brief overview of them. Later sections provide a more detailed description of each one, with the exception of NDB Cluster programs. Each program's description indicates its invocation syntax and the options that it supports. [Section 25.5, “NDB Cluster Programs”](mysql-cluster-programs.md), describes programs specific to NDB Cluster.

Most MySQL distributions include all of these programs, except for those programs that are platform-specific. (For example, the server startup scripts are not used on Windows.) The exception is that RPM distributions are more specialized. There is one RPM for the server, another for client programs, and so forth. If you appear to be missing one or more programs, see [Chapter 2, *Installing MySQL*](installing.md), for information on types of distributions and what they contain. It may be that you have a distribution that does not include all programs and you need to install an additional package.

Each MySQL program takes many different options. Most programs provide a `--help` option that you can use to get a description of the program's different options. For example, try [**mysql --help**](mysql.md).

You can override default option values for MySQL programs by specifying options on the command line or in an option file. See [Section 6.2, “Using MySQL Programs”](programs-using.md), for general information on invoking programs and specifying program options.

The MySQL server, [**mysqld**](mysqld.md), is the main program that does most of the work in a MySQL installation. The server is accompanied by several related scripts that assist you in starting and stopping the server:

- [**mysqld**](mysqld.md)
	The SQL daemon (that is, the MySQL server). To use client programs, [**mysqld**](mysqld.md) must be running, because clients gain access to databases by connecting to the server. See [Section 6.3.1, “mysqld — The MySQL Server”](mysqld.md).
- [**mysqld\_safe**](mysqld-safe.md)
	A server startup script. [**mysqld\_safe**](mysqld-safe.md) attempts to start [**mysqld**](mysqld.md). See [Section 6.3.2, “mysqld\_safe — MySQL Server Startup Script”](mysqld-safe.md).
- [**mysql.server**](mysql-server.md)
	A server startup script. This script is used on systems that use System V-style run directories containing scripts that start system services for particular run levels. It invokes [**mysqld\_safe**](mysqld-safe.md) to start the MySQL server. See [Section 6.3.3, “mysql.server — MySQL Server Startup Script”](mysql-server.md).
- [**mysqld\_multi**](mysqld-multi.md)
	A server startup script that can start or stop multiple servers installed on the system. See [Section 6.3.4, “mysqld\_multi — Manage Multiple MySQL Servers”](mysqld-multi.md).

Several programs perform setup operations during MySQL installation or upgrading:

- [**comp\_err**](comp-err.md)
	This program is used during the MySQL build/installation process. It compiles error message files from the error source files. See [Section 6.4.1, “comp\_err — Compile MySQL Error Message File”](comp-err.md).
- [**mysql\_secure\_installation**](mysql-secure-installation.md)
	This program enables you to improve the security of your MySQL installation. See [Section 6.4.2, “mysql\_secure\_installation — Improve MySQL Installation Security”](mysql-secure-installation.md).
- [**mysql\_tzinfo\_to\_sql**](mysql-tzinfo-to-sql.md)
	This program loads the time zone tables in the `mysql` database using the contents of the host system zoneinfo database (the set of files describing time zones). See [Section 6.4.3, “mysql\_tzinfo\_to\_sql — Load the Time Zone Tables”](mysql-tzinfo-to-sql.md).

MySQL client programs that connect to the MySQL server:

- [**mysql**](mysql.md)
	The command-line tool for interactively entering SQL statements or executing them from a file in batch mode. See [Section 6.5.1, “mysql — The MySQL Command-Line Client”](mysql.md).
- [**mysqladmin**](mysqladmin.md)
	A client that performs administrative operations, such as creating or dropping databases, reloading the grant tables, flushing tables to disk, and reopening log files. [**mysqladmin**](mysqladmin.md) can also be used to retrieve version, process, and status information from the server. See [Section 6.5.2, “mysqladmin — A MySQL Server Administration Program”](mysqladmin.md).
- [**mysqlcheck**](mysqlcheck.md)
	A table-maintenance client that checks, repairs, analyzes, and optimizes tables. See [Section 6.5.3, “mysqlcheck — A Table Maintenance Program”](mysqlcheck.md).
- [**mysqldump**](mysqldump.md)
	A client that dumps a MySQL database into a file as SQL, text, or XML. See [Section 6.5.4, “mysqldump — A Database Backup Program”](mysqldump.md).
- [**mysqlimport**](mysqlimport.md)
	A client that imports text files into their respective tables using [`LOAD DATA`](load-data.md). See [Section 6.5.5, “mysqlimport — A Data Import Program”](mysqlimport.md).
- **mysqlsh**
	MySQL Shell is an advanced client and code editor for MySQL Server. See [MySQL Shell 8.4](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.4-en/). In addition to the provided SQL functionality, similar to [**mysql**](mysql.md), MySQL Shell provides scripting capabilities for JavaScript and Python and includes APIs for working with MySQL. X DevAPI enables you to work with both relational and document data, see [Chapter 22, *Using MySQL as a Document Store*](document-store.md). AdminAPI enables you to work with InnoDB Cluster, see [MySQL AdminAPI](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.4-en/admin-api-userguide.html).
- [**mysqlshow**](mysqlshow.md)
	A client that displays information about databases, tables, columns, and indexes. See [Section 6.5.6, “mysqlshow — Display Database, Table, and Column Information”](mysqlshow.md).
- [**mysqlslap**](mysqlslap.md)
	A client that is designed to emulate client load for a MySQL server and report the timing of each stage. It works as if multiple clients are accessing the server. See [Section 6.5.7, “mysqlslap — A Load Emulation Client”](mysqlslap.md).

MySQL administrative and utility programs:

- [**innochecksum**](innochecksum.md)
	An offline `InnoDB` offline file checksum utility. See [Section 6.6.2, “innochecksum — Offline InnoDB File Checksum Utility”](innochecksum.md).
- [**myisam\_ftdump**](myisam-ftdump.md)
	A utility that displays information about full-text indexes in `MyISAM` tables. See [Section 6.6.3, “myisam\_ftdump — Display Full-Text Index information”](myisam-ftdump.md).
- [**myisamchk**](myisamchk.md)
	A utility to describe, check, optimize, and repair `MyISAM` tables. See [Section 6.6.4, “myisamchk — MyISAM Table-Maintenance Utility”](myisamchk.md).
- [**myisamlog**](myisamlog.md)
	A utility that processes the contents of a `MyISAM` log file. See [Section 6.6.5, “myisamlog — Display MyISAM Log File Contents”](myisamlog.md).
- [**myisampack**](myisampack.md)
	A utility that compresses `MyISAM` tables to produce smaller read-only tables. See [Section 6.6.6, “myisampack — Generate Compressed, Read-Only MyISAM Tables”](myisampack.md).
- [**mysql\_config\_editor**](mysql-config-editor.md)
	A utility that enables you to store authentication credentials in a secure, encrypted login path file named `.mylogin.cnf`. See [Section 6.6.7, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
- [**mysql\_migrate\_keyring**](mysql-migrate-keyring.md)
	A utility for migrating keys between one keyring component and another. See [Section 6.6.8, “mysql\_migrate\_keyring — Keyring Key Migration Utility”](mysql-migrate-keyring.md).
- [**mysqlbinlog**](mysqlbinlog.md)
	A utility for reading statements from a binary log. The log of executed statements contained in the binary log files can be used to help recover from a crash. See [Section 6.6.9, “mysqlbinlog — Utility for Processing Binary Log Files”](mysqlbinlog.md).
- [**mysqldumpslow**](mysqldumpslow.md)
	A utility to read and summarize the contents of a slow query log. See [Section 6.6.10, “mysqldumpslow — Summarize Slow Query Log Files”](mysqldumpslow.md).

MySQL program-development utilities:

- [**mysql\_config**](mysql-config.md)
	A shell script that produces the option values needed when compiling MySQL programs. See [Section 6.7.1, “mysql\_config — Display Options for Compiling Clients”](mysql-config.md).
- [**my\_print\_defaults**](my-print-defaults.md)
	A utility that shows which options are present in option groups of option files. See [Section 6.7.2, “my\_print\_defaults — Display Options from Option Files”](my-print-defaults.md).

Miscellaneous utilities:

- [**perror**](perror.md)
	A utility that displays the meaning of system or MySQL error codes. See [Section 6.8.1, “perror — Display MySQL Error Message Information”](perror.md).

Oracle Corporation also provides the [MySQL Workbench](workbench.md) GUI tool, which is used to administer MySQL servers and databases, to create, execute, and evaluate queries, and to migrate schemas and data from other relational database management systems for use with MySQL.

MySQL client programs that communicate with the server using the MySQL client/server library use the following environment variables.

| Environment Variable | Meaning |
| --- | --- |
| `MYSQL_UNIX_PORT` | The default Unix socket file; used for connections to `localhost` |
| `MYSQL_TCP_PORT` | The default port number; used for TCP/IP connections |
| `MYSQL_DEBUG` | Debug trace options when debugging |
| `TMPDIR` | The directory where temporary tables and files are created |

For a full list of environment variables used by MySQL programs, see [Section 6.9, “Environment Variables”](environment-variables.md).