---
title: "MySQL :: MySQL 26.7 Reference Manual :: 7.8 Running Multiple MySQL Instances on One Machine"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/multiple-servers.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 7.8 Running Multiple MySQL Instances on One Machine

In some cases, you might want to run multiple instances of MySQL on a single machine. You might want to test a new MySQL release while leaving an existing production setup undisturbed. Or you might want to give different users access to different [**mysqld**](mysqld.md) servers that they manage themselves. (For example, you might be an Internet Service Provider that wants to provide independent MySQL installations for different customers.)

It is possible to use a different MySQL server binary per instance, or use the same binary for multiple instances, or any combination of the two approaches. For example, you might run a server from MySQL 9.7 and one from MySQL 26.7, to see how different versions handle a given workload. Or you might run multiple instances of the current production version, each managing a different set of databases.

Whether or not you use distinct server binaries, each instance that you run must be configured with unique values for several operating parameters. This eliminates the potential for conflict between instances. Parameters can be set on the command line, in option files, or by setting environment variables. See [Section 6.2.2, “Specifying Program Options”](program-options.md). To see the values used by a given instance, connect to it and execute a [`SHOW     VARIABLES`](show-variables.md) statement.

The primary resource managed by a MySQL instance is the data directory. Each instance should use a different data directory, the location of which is specified using the [``--datadir=*`dir_name`*``](server-system-variables.md) option. For methods of configuring each instance with its own data directory, and warnings about the dangers of failing to do so, see [Section 7.8.1, “Setting Up Multiple Data Directories”](multiple-data-directories.md).

In addition to using different data directories, several other options must have different values for each server instance:

- [``--port=*`port_num`*``](server-options.md)
	[`--port`](server-options.md) controls the port number for TCP/IP connections. Alternatively, if the host has multiple network addresses, you can set the [`bind_address`](server-system-variables.md) system variable to cause each server to listen to a different address.
- [``--socket={*`file_name`*|*`pipe_name`*}``](server-options.md)
	[`--socket`](server-options.md) controls the Unix socket file path on Unix or the named-pipe name on Windows. On Windows, it is necessary to specify distinct pipe names only for those servers configured to permit named-pipe connections.
- [``--shared-memory-base-name=*`name`*``](server-system-variables.md)
	This option is used only on Windows. It designates the shared-memory name used by a Windows server to permit clients to connect using shared memory. It is necessary to specify distinct shared-memory names only for those servers configured to permit shared-memory connections.
- [``--pid-file=*`file_name`*``](server-system-variables.md)
	This option indicates the path name of the file in which the server writes its process ID.

If you use the following log file options, their values must differ for each server:

For further discussion of log file options, see [Section 7.4, “MySQL Server Logs”](server-logs.md).

To achieve better performance, you can specify the following option differently for each server, to spread the load between several physical disks:

- [``--tmpdir=*`dir_name`*``](server-options.md)

Having different temporary directories also makes it easier to determine which MySQL server created any given temporary file.

If you have multiple MySQL installations in different locations, you can specify the base directory for each installation with the [``--basedir=*`dir_name`*``](server-system-variables.md) option. This causes each instance to automatically use a different data directory, log files, and PID file because the default for each of those parameters is relative to the base directory. In that case, the only other options you need to specify are the [`--socket`](server-options.md) and [`--port`](server-options.md) options. Suppose that you install different versions of MySQL using `tar` file binary distributions. These install in different locations, so you can start the server for each installation using the command **bin/mysqld\_safe** under its corresponding base directory. [**mysqld\_safe**](mysqld-safe.md) determines the proper [`--basedir`](server-system-variables.md) option to pass to [**mysqld**](mysqld.md), and you need specify only the [`--socket`](mysqld-safe.md) and [`--port`](mysqld-safe.md) options to [**mysqld\_safe**](mysqld-safe.md).

As discussed in the following sections, it is possible to start additional servers by specifying appropriate command options or by setting environment variables. However, if you need to run multiple servers on a more permanent basis, it is more convenient to use option files to specify for each server those option values that must be unique to it. The [`--defaults-file`](option-file-options.md) option is useful for this purpose.