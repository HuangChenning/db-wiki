---
title: "MySQL :: MySQL 26.7 Reference Manual :: 8.1.6 Security Considerations for LOAD DATA LOCAL"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/load-data-local-security.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 8.1.6 Security Considerations for LOAD DATA LOCAL

The [`LOAD DATA`](load-data.md) statement loads a data file into a table. The statement can load a file located on the server host, or, if the `LOCAL` keyword is specified, on the client host.

The `LOCAL` version of [`LOAD       DATA`](load-data.md) has two potential security issues:

- Because [`LOAD DATA           LOCAL`](load-data.md) is an SQL statement, parsing occurs on the server side, and transfer of the file from the client host to the server host is initiated by the MySQL server, which tells the client the file named in the statement. In theory, a patched server could tell the client program to transfer a file of the server's choosing rather than the file named in the statement. Such a server could access any file on the client host to which the client user has read access. (A patched server could in fact reply with a file-transfer request to any statement, not just [`LOAD DATA           LOCAL`](load-data.md), so a more fundamental issue is that clients should not connect to untrusted servers.)
- In a Web environment where the clients are connecting from a Web server, a user could use [`LOAD DATA           LOCAL`](load-data.md) to read any files that the Web server process has read access to (assuming that a user could run any statement against the SQL server). In this environment, the client with respect to the MySQL server actually is the Web server, not a remote program being run by users who connect to the Web server.

To avoid connecting to untrusted servers, clients can establish a secure connection and verify the server identity by connecting using the [`--ssl-mode=VERIFY_IDENTITY`](connection-options.md) option and the appropriate CA certificate. To implement this level of verification, you must first ensure that the CA certificate for the server is reliably available to the replica, otherwise availability issues will result. For more information, see [Command Options for Encrypted Connections](connection-options.md).

To avoid [`LOAD DATA`](load-data.md) issues, clients should avoid using `LOCAL` unless proper client-side precautions have been taken.

For control over local data loading, MySQL permits the capability to be enabled or disabled. MySQL also enables clients to restrict local data loading operations to files located in a designated directory.

#### Enabling or Disabling Local Data Loading Capability

Administrators and applications can configure whether to permit local data loading as follows:

- On the server side:
	- The [`local_infile`](server-system-variables.md) system variable controls server-side `LOCAL` capability. Depending on the [`local_infile`](server-system-variables.md) setting, the server refuses or permits local data loading by clients that request local data loading.
	- By default, [`local_infile`](server-system-variables.md) is disabled. (This is a change from previous versions of MySQL.) To cause the server to refuse or permit [`LOAD DATA                 LOCAL`](load-data.md) statements explicitly (regardless of how client programs and libraries are configured at build time or runtime), start [**mysqld**](mysqld.md) with [`local_infile`](server-system-variables.md) disabled or enabled. [`local_infile`](server-system-variables.md) can also be set at runtime.
- On the client side:
	- The [`ENABLED_LOCAL_INFILE`](source-configuration-options.md) **CMake** option controls the compiled-in default `LOCAL` capability for the MySQL client library (see [Section 2.8.7, “MySQL Source-Configuration Options”](source-configuration-options.md)). Clients that make no explicit arrangements therefore have `LOCAL` capability disabled or enabled according to the [`ENABLED_LOCAL_INFILE`](source-configuration-options.md) setting specified at MySQL build time.
	- By default, the client library in MySQL binary distributions is compiled with [`ENABLED_LOCAL_INFILE`](source-configuration-options.md) disabled. If you compile MySQL from source, configure it with [`ENABLED_LOCAL_INFILE`](source-configuration-options.md) disabled or enabled based on whether clients that make no explicit arrangements should have `LOCAL` capability disabled or enabled.
	- For client programs that use the C API, local data loading capability is determined by the default compiled into the MySQL client library. To enable or disable it explicitly, invoke the [`mysql_options()`](https://dev.mysql.com/doc/c-api/26.7/en/mysql-options.html) C API function to disable or enable the `MYSQL_OPT_LOCAL_INFILE` option. See [mysql\_options()](https://dev.mysql.com/doc/c-api/26.7/en/mysql-options.html).
	- For the [**mysql**](mysql.md) client, local data loading capability is determined by the default compiled into the MySQL client library. To disable or enable it explicitly, use the [`--local-infile=0`](mysql-command-options.md) or [`--local-infile[=1]`](https://dev.mysql.com/doc/refman/26.7/en/mysql-command-options.html#option_mysql_local-infile) option.
	- For the [**mysqlimport**](mysqlimport.md) client, local data loading is not used by default. To disable or enable it explicitly, use the [`--local=0`](mysqlimport.md) or [`--local[=1]`](https://dev.mysql.com/doc/refman/26.7/en/mysqlimport.html#option_mysqlimport_local) option.
	- If you use [`LOAD DATA                 LOCAL`](load-data.md) in Perl scripts or other programs that read the `[client]` group from option files, you can add a `local-infile` option setting to that group. To prevent problems for programs that do not understand this option, specify it using the [`loose-`](option-modifiers.md) prefix:
		```svg
		[client]
		loose-local-infile=0
		```
		or:
		```svg
		[client]
		loose-local-infile=1
		```
	- In all cases, successful use of a `LOCAL` load operation by a client also requires that the server permits local loading.

If `LOCAL` capability is disabled, on either the server or client side, a client that attempts to issue a [`LOAD DATA         LOCAL`](load-data.md) statement receives the following error message:

```svg
ERROR 3950 (42000): Loading local data is disabled; this must be
enabled on both the client and server side
```

#### Restricting Files Permitted for Local Data Loading

The MySQL client library enables client applications to restrict local data loading operations to files located in a designated directory. Certain MySQL client programs take advantage of this capability.

Client programs that use the C API can control which files to permit for load data loading using the `MYSQL_OPT_LOCAL_INFILE` and `MYSQL_OPT_LOAD_DATA_LOCAL_DIR` options of the [`mysql_options()`](https://dev.mysql.com/doc/c-api/26.7/en/mysql-options.html) C API function (see [mysql\_options()](https://dev.mysql.com/doc/c-api/26.7/en/mysql-options.html)).

The effect of `MYSQL_OPT_LOAD_DATA_LOCAL_DIR` depends on whether `LOCAL` data loading is enabled or disabled:

- If `LOCAL` data loading is enabled, either by default in the MySQL client library or by explicitly enabling `MYSQL_OPT_LOCAL_INFILE`, the `MYSQL_OPT_LOAD_DATA_LOCAL_DIR` option has no effect.
- If `LOCAL` data loading is disabled, either by default in the MySQL client library or by explicitly disabling `MYSQL_OPT_LOCAL_INFILE`, the `MYSQL_OPT_LOAD_DATA_LOCAL_DIR` option can be used to designate a permitted directory for locally loaded files. In this case, `LOCAL` data loading is permitted but restricted to files located in the designated directory. Interpretation of the `MYSQL_OPT_LOAD_DATA_LOCAL_DIR` value is as follows:
	- If the value is the null pointer (the default), it names no directory, with the result that no files are permitted for `LOCAL` data loading.
	- If the value is a directory path name, `LOCAL` data loading is permitted but restricted to files located in the named directory. Comparison of the directory path name and the path name of files to be loaded is case-sensitive regardless of the case sensitivity of the underlying file system.

MySQL client programs use the preceding [`mysql_options()`](https://dev.mysql.com/doc/c-api/26.7/en/mysql-options.html) options as follows:

- The [**mysql**](mysql.md) client has a [`--load-data-local-dir`](mysql-command-options.md) option that takes a directory path or an empty string. [**mysql**](mysql.md) uses the option value to set the `MYSQL_OPT_LOAD_DATA_LOCAL_DIR` option (with an empty string setting the value to the null pointer). The effect of [`--load-data-local-dir`](mysql-command-options.md) depends on whether `LOCAL` data loading is enabled:
	- If `LOCAL` data loading is enabled, either by default in the MySQL client library or by specifying [`--local-infile[=1]`](https://dev.mysql.com/doc/refman/26.7/en/mysql-command-options.html#option_mysql_local-infile), the [`--load-data-local-dir`](mysql-command-options.md) option is ignored.
	- If `LOCAL` data loading is disabled, either by default in the MySQL client library or by specifying [`--local-infile=0`](mysql-command-options.md), the [`--load-data-local-dir`](mysql-command-options.md) option applies.
	When [`--load-data-local-dir`](mysql-command-options.md) applies, the option value designates the directory in which local data files must be located. Comparison of the directory path name and the path name of files to be loaded is case-sensitive regardless of the case sensitivity of the underlying file system. If the option value is the empty string, it names no directory, with the result that no files are permitted for local data loading.
- [**mysqlimport**](mysqlimport.md) sets `MYSQL_OPT_LOAD_DATA_LOCAL_DIR` for each file that it processes so that the directory containing the file is the permitted local loading directory.
- For data loading operations corresponding to [`LOAD DATA`](load-data.md) statements, [**mysqlbinlog**](mysqlbinlog.md) extracts the files from the binary log events, writes them as temporary files to the local file system, and writes [`LOAD DATA             LOCAL`](load-data.md) statements to cause the files to be loaded. By default, [**mysqlbinlog**](mysqlbinlog.md) writes these temporary files to an operating system-specific directory. The [`--local-load`](mysqlbinlog.md) option can be used to explicitly specify the directory where [**mysqlbinlog**](mysqlbinlog.md) should prepare local temporary files.
	Because other processes can write files to the default system-specific directory, it is advisable to specify the [`--local-load`](mysqlbinlog.md) option to [**mysqlbinlog**](mysqlbinlog.md) to designate a different directory for data files, and then designate that same directory by specifying the [`--load-data-local-dir`](mysql-command-options.md) option to [**mysql**](mysql.md) when processing the output from [**mysqlbinlog**](mysqlbinlog.md).

#### MySQL Shell and Local Data Loading

MySQL Shell provides a number of utilities to dump tables, schemas, or server instances and load them into other instances. When you use these utilities to handle the data, MySQL Shell provides additional functions such as input preprocessing, multithreaded parallel loading, file compression and decompression, and handling access to Oracle Cloud Infrastructure Object Storage buckets. To get the best functionality, always use the most recent version available of MySQL Shell's dump and dump loading utilities.

MySQL Shell's data upload utilities use [`LOAD DATA LOCAL         INFILE`](load-data.md) statements to upload data, so the [`local_infile`](server-system-variables.md) system variable must be set to `ON` on the target server instance. You can do this before uploading the data, and remove it again afterwards. The utilities handle the file transfer requests safely to deal with the security considerations discussed in this topic.

MySQL Shell includes these dump and dump loading utilities:

Table export utility `util.exportTable()`

Exports a MySQL relational table into a data file, which can be uploaded to a MySQL server instance using MySQL Shell's parallel table import utility, imported to a different application, or used as a logical backup. The utility has preset options and customization options to produce different output formats.

Parallel table import utility `util.importTable()`

Imports a data file to a MySQL relational table. The data file can be the output from MySQL Shell's table export utility or another format supported by the utility's preset and customization options. The utility can carry out input preprocessing before adding the data to the table. It can accept multiple data files to merge into a single relational table, and automatically decompresses compressed files.

Instance dump utility `util.dumpInstance()`, schema dump utility `util.dumpSchemas()`, and table dump utility `util.dumpTables()`

Export an instance, schema, or table to a set of dump files, which can then be uploaded to a MySQL instance using MySQL Shell's dump loading utility. The utilities provide Oracle Cloud Infrastructure Object Storage streaming, MySQL HeatWave Service compatibility checks and modifications, and the ability to carry out a dry run to identify issues before proceeding with the dump.

Dump loading utility `util.loadDump()`

Import dump files created using MySQL Shell's instance, schema, or table dump utility into a MySQL HeatWave Service DB System or a MySQL Server instance. The utility manages the upload process and provides data streaming from remote storage, parallel loading of tables or table chunks, progress state tracking, resume and reset capability, and the option of concurrent loading while the dump is still taking place. MySQL Shell’s parallel table import utility can be used in combination with the dump loading utility to modify data before uploading it to the target MySQL instance.

For details of the utilities, see [MySQL Shell Utilities](https://dev.mysql.com/doc/mysql-shell/26.7/en/mysql-shell-utilities.html).