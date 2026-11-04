---
title: "7.1.1 Configuring the Server"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/server-configuration.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 7.1.1 Configuring the Server

The MySQL server, [**mysqld**](mysqld.md), has many command options and system variables that can be set at startup to configure its operation. To determine the default command option and system variable values used by the server, execute this command:

```
$> mysqld --verbose --help
```

The command produces a list of all [**mysqld**](mysqld.md) options and configurable system variables. Its output includes the default option and variable values and looks something like this:

```
abort-slave-event-count           0
allow-suspicious-udfs             FALSE
archive                           ON
auto-increment-increment          1
auto-increment-offset             1
autocommit                        TRUE
automatic-sp-privileges           TRUE
avoid-temporal-upgrade            FALSE
back-log                          80
basedir                           /home/jon/bin/mysql-8.0/
...
tmpdir                            /tmp
transaction-alloc-block-size      8192
transaction-isolation             REPEATABLE-READ
transaction-prealloc-size         4096
transaction-read-only             FALSE
transaction-write-set-extraction  XXHASH64
updatable-views-with-limit        YES
validate-user-plugins             TRUE
verbose                           TRUE
wait-timeout                      28800
```

To see the current system variable values actually used by the server as it runs, connect to it and execute this statement:

```
mysql> SHOW VARIABLES;
```

To see some statistical and status indicators for a running server, execute this statement:

```
mysql> SHOW STATUS;
```

System variable and status information also is available using the [**mysqladmin**](mysqladmin.md) command:

```
$> mysqladmin variables
$> mysqladmin extended-status
```

For a full description of all command options, system variables, and status variables, see these sections:

- [Section 7.1.7, “Server Command Options”](server-options.md)
- [Section 7.1.8, “Server System Variables”](server-system-variables.md)
- [Section 7.1.10, “Server Status Variables”](server-status-variables.md)

More detailed monitoring information is available from the Performance Schema; see [Chapter 29, *MySQL Performance Schema*](performance-schema.md). In addition, the MySQL `sys` schema is a set of objects that provides convenient access to data collected by the Performance Schema; see [Chapter 30, *MySQL sys Schema*](sys-schema.md).

If you specify an option on the command line for [**mysqld**](mysqld.md) or [**mysqld\_safe**](mysqld-safe.md), it remains in effect only for that invocation of the server. To use the option every time the server runs, put it in an option file. See [Section 6.2.2.2, “Using Option Files”](option-files.md).