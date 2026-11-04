---
title: "6.5.6 mysqlpump — A Database Backup Program"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysqlpump.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 6.5.6 mysqlpump — A Database Backup Program

The **mysqlpump** client utility performs [logical backups](glossary.md), producing a set of SQL statements that can be executed to reproduce the original database object definitions and table data. It dumps one or more MySQL databases for backup or transfer to another SQL server.

Note

**mysqlpump** is deprecated as of MySQL 8.0.34; expect it to be removed in a future version of MySQL. You can use such MySQL programs as [**mysqldump**](mysqldump.md) and MySQL Shell to perform logical backups, dump databases, and similar tasks instead.

Tip

Consider using the [MySQL Shell dump utilities](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.0-en/mysql-shell-utilities-dump-instance-schema.html), which provide parallel dumping with multiple threads, file compression, and progress information display, as well as cloud features such as Oracle Cloud Infrastructure Object Storage streaming, and MySQL HeatWave compatibility checks and modifications. Dumps can be easily imported into a MySQL Server instance or a MySQL HeatWave DB System using the [MySQL Shell load dump utilities](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.0-en/mysql-shell-utilities-load-dump.html). Installation instructions for MySQL Shell can be found [here](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.0-en/mysql-shell-install.html).

**mysqlpump** features include:

- Parallel processing of databases, and of objects within databases, to speed up the dump process
- Better control over which databases and database objects (tables, stored programs, user accounts) to dump
- Dumping of user accounts as account-management statements ([`CREATE USER`](create-user.md), [`GRANT`](grant.md)) rather than as inserts into the `mysql` system database
- Capability of creating compressed output
- Progress indicator (the values are estimates)
- For dump file reloading, faster secondary index creation for `InnoDB` tables by adding indexes after rows are inserted

Note

**mysqlpump** uses MySQL features introduced in MySQL 5.7, and thus assumes use with MySQL 5.7 or higher.

**mysqlpump** requires at least the [`SELECT`](privileges-provided.md) privilege for dumped tables, [`SHOW VIEW`](privileges-provided.md) for dumped views, [`TRIGGER`](privileges-provided.md) for dumped triggers, and [`LOCK TABLES`](privileges-provided.md) if the `--single-transaction` option is not used. The [`SELECT`](privileges-provided.md) privilege on the `mysql` system database is required to dump user definitions. Certain options might require other privileges as noted in the option descriptions.

To reload a dump file, you must have the privileges required to execute the statements that it contains, such as the appropriate `CREATE` privileges for objects created by those statements.

A dump made using PowerShell on Windows with output redirection creates a file that has UTF-16 encoding:

```
mysqlpump [options] > dump.sql
```

However, UTF-16 is not permitted as a connection character set (see [Section 12.4, “Connection Character Sets and Collations”](charset-connection.md)), so the dump file cannot be loaded correctly. To work around this issue, use the `--result-file` option, which creates the output in ASCII format:

```
mysqlpump [options] --result-file=dump.sql
```

#### mysqlpump Invocation Syntax

By default, **mysqlpump** dumps all databases (with certain exceptions noted in mysqlpump Restrictions). To specify this behavior explicitly, use the `--all-databases` option:

```
mysqlpump --all-databases
```

To dump a single database, or certain tables within that database, name the database on the command line, optionally followed by table names:

```
mysqlpump db_name
mysqlpump db_name tbl_name1 tbl_name2 ...
```

To treat all name arguments as database names, use the `--databases` option:

```
mysqlpump --databases db_name1 db_name2 ...
```

By default, **mysqlpump** does not dump user account definitions, even if you dump the `mysql` system database that contains the grant tables. To dump grant table contents as logical definitions in the form of [`CREATE USER`](create-user.md) and [`GRANT`](grant.md) statements, use the `--users` option and suppress all database dumping:

```
mysqlpump --exclude-databases=% --users
```

In the preceding command, `%` is a wildcard that matches all database names for the `--exclude-databases` option.

**mysqlpump** supports several options for including or excluding databases, tables, stored programs, and user definitions. See mysqlpump Object Selection.

To reload a dump file, execute the statements that it contains. For example, use the [**mysql**](mysql.md) client:

```
mysqlpump [options] > dump.sql
mysql < dump.sql
```

The following discussion provides additional **mysqlpump** usage examples.

To see a list of the options **mysqlpump** supports, issue the command **mysqlpump --help**.

#### mysqlpump Option Summary

**mysqlpump** supports the following options, which can be specified on the command line or in the `[mysqlpump]` and `[client]` groups of an option file. (Prior to MySQL 8.0.20, **mysqlpump** read the `[mysql_dump]` group rather than `[mysqlpump]`. As of 8.0.20, `[mysql_dump]` is still accepted but is deprecated.) For information about option files used by MySQL programs, see [Section 6.2.2.2, “Using Option Files”](option-files.md).

**Table 6.17 mysqlpump Options**

| Option Name | Description | Deprecated |
| --- | --- | --- |
| \--add-drop-database | Add DROP DATABASE statement before each CREATE DATABASE statement |  |
| \--add-drop-table | Add DROP TABLE statement before each CREATE TABLE statement |  |
| \--add-drop-user | Add DROP USER statement before each CREATE USER statement |  |
| \--add-locks | Surround each table dump with LOCK TABLES and UNLOCK TABLES statements |  |
| \--all-databases | Dump all databases |  |
| \--bind-address | Use specified network interface to connect to MySQL Server |  |
| \--character-sets-dir | Directory where character sets are installed |  |
| \--column-statistics | Write ANALYZE TABLE statements to generate statistics histograms |  |
| \--complete-insert | Use complete INSERT statements that include column names |  |
| \--compress | Compress all information sent between client and server | Yes |
| \--compress-output | Output compression algorithm |  |
| \--compression-algorithms | Permitted compression algorithms for connections to server |  |
| \--databases | Interpret all name arguments as database names |  |
| \--debug | Write debugging log |  |
| \--debug-check | Print debugging information when program exits |  |
| \--debug-info | Print debugging information, memory, and CPU statistics when program exits |  |
| \--default-auth | Authentication plugin to use |  |
| \--default-character-set | Specify default character set |  |
| \--default-parallelism | Default number of threads for parallel processing |  |
| \--defaults-extra-file | Read named option file in addition to usual option files |  |
| \--defaults-file | Read only named option file |  |
| \--defaults-group-suffix | Option group suffix value |  |
| \--defer-table-indexes | For reloading, defer index creation until after loading table rows |  |
| \--events | Dump events from dumped databases |  |
| \--exclude-databases | Databases to exclude from dump |  |
| \--exclude-events | Events to exclude from dump |  |
| \--exclude-routines | Routines to exclude from dump |  |
| \--exclude-tables | Tables to exclude from dump |  |
| \--exclude-triggers | Triggers to exclude from dump |  |
| \--exclude-users | Users to exclude from dump |  |
| \--extended-insert | Use multiple-row INSERT syntax |  |
| \--get-server-public-key | Request RSA public key from server |  |
| \--help | Display help message and exit |  |
| \--hex-blob | Dump binary columns using hexadecimal notation |  |
| \--host | Host on which MySQL server is located |  |
| \--include-databases | Databases to include in dump |  |
| \--include-events | Events to include in dump |  |
| \--include-routines | Routines to include in dump |  |
| \--include-tables | Tables to include in dump |  |
| \--include-triggers | Triggers to include in dump |  |
| \--include-users | Users to include in dump |  |
| \--insert-ignore | Write INSERT IGNORE rather than INSERT statements |  |
| \--log-error-file | Append warnings and errors to named file |  |
| \--login-path | Read login path options from.mylogin.cnf |  |
| \--max-allowed-packet | Maximum packet length to send to or receive from server |  |
| \--net-buffer-length | Buffer size for TCP/IP and socket communication |  |
| \--no-create-db | Do not write CREATE DATABASE statements |  |
| \--no-create-info | Do not write CREATE TABLE statements that re-create each dumped table |  |
| \--no-defaults | Read no option files |  |
| \--parallel-schemas | Specify schema-processing parallelism |  |
| \--password | Password to use when connecting to server |  |
| \--password1 | First multifactor authentication password to use when connecting to server |  |
| \--password2 | Second multifactor authentication password to use when connecting to server |  |
| \--password3 | Third multifactor authentication password to use when connecting to server |  |
| \--plugin-dir | Directory where plugins are installed |  |
| \--port | TCP/IP port number for connection |  |
| \--print-defaults | Print default options |  |
| \--protocol | Transport protocol to use |  |
| \--replace | Write REPLACE statements rather than INSERT statements |  |
| \--result-file | Direct output to a given file |  |
| \--routines | Dump stored routines (procedures and functions) from dumped databases |  |
| \--server-public-key-path | Path name to file containing RSA public key |  |
| \--set-charset | Add SET NAMES default\_character\_set to output |  |
| \--set-gtid-purged | Whether to add SET @@GLOBAL.GTID\_PURGED to output |  |
| \--single-transaction | Dump tables within single transaction |  |
| \--skip-definer | Omit DEFINER and SQL SECURITY clauses from view and stored program CREATE statements |  |
| \--skip-dump-rows | Do not dump table rows |  |
| \--skip-generated-invisible-primary-key | Do not dump information about generated invisible primary keys |  |
| \--socket | Unix socket file or Windows named pipe to use |  |
| \--ssl-ca | File that contains list of trusted SSL Certificate Authorities |  |
| \--ssl-capath | Directory that contains trusted SSL Certificate Authority certificate files |  |
| \--ssl-cert | File that contains X.509 certificate |  |
| \--ssl-cipher | Permissible ciphers for connection encryption |  |
| \--ssl-crl | File that contains certificate revocation lists |  |
| \--ssl-crlpath | Directory that contains certificate revocation-list files |  |
| \--ssl-fips-mode | Whether to enable FIPS mode on client side | Yes |
| \--ssl-key | File that contains X.509 key |  |
| \--ssl-mode | Desired security state of connection to server |  |
| \--ssl-session-data | File that contains SSL session data |  |
| \--ssl-session-data-continue-on-failed-reuse | Whether to establish connections if session reuse fails |  |
| \--tls-ciphersuites | Permissible TLSv1.3 ciphersuites for encrypted connections |  |
| \--tls-version | Permissible TLS protocols for encrypted connections |  |
| \--triggers | Dump triggers for each dumped table |  |
| \--tz-utc | Add SET TIME\_ZONE='+00:00' to dump file |  |
| \--user | MySQL user name to use when connecting to server |  |
| \--users | Dump user accounts |  |
| \--version | Display version information and exit |  |
| \--watch-progress | Display progress indicator |  |
| \--zstd-compression-level | Compression level for connections to server that use zstd compression |  |

#### mysqlpump Option Descriptions

- `--help`, `-?`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display a help message and exit.
- `--add-drop-database`
	| Command-Line Format | `--add-drop-database` |
	| --- | --- |
	Write a [`DROP DATABASE`](drop-database.md) statement before each [`CREATE             DATABASE`](create-database.md) statement.
	Note
	In MySQL 8.0, the `mysql` schema is considered a system schema that cannot be dropped by end users. If `--add-drop-database` is used with `--all-databases` or with `--databases` where the list of schemas to be dumped includes `mysql`, the dump file contains a `` DROP DATABASE `mysql` `` statement that causes an error when the dump file is reloaded.
	Instead, to use `--add-drop-database`, use `--databases` with a list of schemas to be dumped, where the list does not include `mysql`.
- `--add-drop-table`
	| Command-Line Format | `--add-drop-table` |
	| --- | --- |
	Write a [`DROP TABLE`](drop-table.md) statement before each [`CREATE TABLE`](create-table.md) statement.
- `--add-drop-user`
	| Command-Line Format | `--add-drop-user` |
	| --- | --- |
	Write a [`DROP USER`](drop-user.md) statement before each [`CREATE USER`](create-user.md) statement.
- `--add-locks`
	| Command-Line Format | `--add-locks` |
	| --- | --- |
	Surround each table dump with [`LOCK             TABLES`](lock-tables.md) and [`UNLOCK             TABLES`](lock-tables.md) statements. This results in faster inserts when the dump file is reloaded. See [Section 10.2.5.1, “Optimizing INSERT Statements”](insert-optimization.md).
	This option does not work with parallelism because [`INSERT`](insert.md) statements from different tables can be interleaved and [`UNLOCK             TABLES`](lock-tables.md) following the end of the inserts for one table could release locks on tables for which inserts remain.
	`--add-locks` and `--single-transaction` are mutually exclusive.
- `--all-databases`, `-A`
	| Command-Line Format | `--all-databases` |
	| --- | --- |
	Dump all databases (with certain exceptions noted in mysqlpump Restrictions). This is the default behavior if no other is specified explicitly.
	`--all-databases` and `--databases` are mutually exclusive.
	Note
	See the `--add-drop-database` description for information about an incompatibility of that option with `--all-databases`.
	Prior to MySQL 8.0, the [`--routines`](mysqldump.md) and [`--events`](mysqldump.md) options for [**mysqldump**](mysqldump.md) and **mysqlpump** were not required to include stored routines and events when using the [`--all-databases`](mysqldump.md) option: The dump included the `mysql` system database, and therefore also the `mysql.proc` and `mysql.event` tables containing stored routine and event definitions. As of MySQL 8.0, the `mysql.event` and `mysql.proc` tables are not used. Definitions for the corresponding objects are stored in data dictionary tables, but those tables are not dumped. To include stored routines and events in a dump made using [`--all-databases`](mysqldump.md), use the [`--routines`](mysqldump.md) and [`--events`](mysqldump.md) options explicitly.
- ``--bind-address=*`ip_address`*``
	| Command-Line Format | `--bind-address=ip_address` |
	| --- | --- |
	On a computer having multiple network interfaces, use this option to select which interface to use for connecting to the MySQL server.
- ``--character-sets-dir=*`path`*``
	| Command-Line Format | `--character-sets-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The directory where character sets are installed. See [Section 12.15, “Character Set Configuration”](charset-configuration.md).
- `--column-statistics`
	| Command-Line Format | `--column-statistics` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	Add [`ANALYZE TABLE`](analyze-table.md) statements to the output to generate histogram statistics for dumped tables when the dump file is reloaded. This option is disabled by default because histogram generation for large tables can take a long time.
- `--complete-insert`
	| Command-Line Format | `--complete-insert` |
	| --- | --- |
	Write complete [`INSERT`](insert.md) statements that include column names.
- `--compress`, `-C`
	| Command-Line Format | `--compress[={OFF\|ON}]` |
	| --- | --- |
	| Deprecated | Yes |
	| Type | Boolean |
	| Default Value | `OFF` |
	Compress all information sent between the client and the server if possible. See [Section 6.2.8, “Connection Compression Control”](connection-compression-control.md).
	As of MySQL 8.0.18, this option is deprecated. Expect it to be removed in a future version of MySQL. See [Configuring Legacy Connection Compression](connection-compression-control.md).
- ``--compress-output=*`algorithm`*``
	| Command-Line Format | `--compress-output=algorithm` |
	| --- | --- |
	| Type | Enumeration |
	| Valid Values | `LZ4`  `ZLIB` |
	By default, **mysqlpump** does not compress output. This option specifies output compression using the specified algorithm. Permitted algorithms are `LZ4` and `ZLIB`.
	To uncompress compressed output, you must have an appropriate utility. If the system commands **lz4** and **openssl zlib** are not available, MySQL distributions include [**lz4\_decompress**](lz4-decompress.md) and [**zlib\_decompress**](zlib-decompress.md) utilities that can be used to decompress **mysqlpump** output that was compressed using the `--compress-output=LZ4` and `--compress-output=ZLIB` options. For more information, see [Section 6.8.1, “lz4\_decompress — Decompress mysqlpump LZ4-Compressed Output”](lz4-decompress.md), and [Section 6.8.3, “zlib\_decompress — Decompress mysqlpump ZLIB-Compressed Output”](zlib-decompress.md).
- ``--compression-algorithms=*`value`*``
	| Command-Line Format | `--compression-algorithms=value` |
	| --- | --- |
	| Type | Set |
	| Default Value | `uncompressed` |
	| Valid Values | `zlib`  `zstd`  `uncompressed` |
	The permitted compression algorithms for connections to the server. The available algorithms are the same as for the [`protocol_compression_algorithms`](server-system-variables.md) system variable. The default value is `uncompressed`.
	For more information, see [Section 6.2.8, “Connection Compression Control”](connection-compression-control.md).
	This option was added in MySQL 8.0.18.
- `--databases`, `-B`
	| Command-Line Format | `--databases` |
	| --- | --- |
	Normally, **mysqlpump** treats the first name argument on the command line as a database name and any following names as table names. With this option, it treats all name arguments as database names. [`CREATE DATABASE`](create-database.md) statements are included in the output before each new database.
	`--all-databases` and `--databases` are mutually exclusive.
	Note
	See the `--add-drop-database` description for information about an incompatibility of that option with `--databases`.
- [``--debug[=*`debug_options`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysqlpump.html#option_mysqlpump_debug), ``-#             [*`debug_options`*]``
	| Command-Line Format | `--debug[=debug_options]` |
	| --- | --- |
	| Type | String |
	| Default Value | `d:t:O,/tmp/mysqlpump.trace` |
	Write a debugging log. A typical *`debug_options`* string is ``d:t:o,*`file_name`*``. The default is `d:t:O,/tmp/mysqlpump.trace`.
	This option is available only if MySQL was built using [`WITH_DEBUG`](source-configuration-options.md). MySQL release binaries provided by Oracle are *not* built using this option.
- `--debug-check`
	| Command-Line Format | `--debug-check` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Print some debugging information when the program exits.
	This option is available only if MySQL was built using [`WITH_DEBUG`](source-configuration-options.md). MySQL release binaries provided by Oracle are *not* built using this option.
- `--debug-info`, `-T`
	| Command-Line Format | `--debug-info` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Print debugging information and memory and CPU usage statistics when the program exits.
	This option is available only if MySQL was built using [`WITH_DEBUG`](source-configuration-options.md). MySQL release binaries provided by Oracle are *not* built using this option.
- ``--default-auth=*`plugin`*``
	| Command-Line Format | `--default-auth=plugin` |
	| --- | --- |
	| Type | String |
	A hint about which client-side authentication plugin to use. See [Section 8.2.17, “Pluggable Authentication”](pluggable-authentication.md).
- ``--default-character-set=*`charset_name`*``
	| Command-Line Format | `--default-character-set=charset_name` |
	| --- | --- |
	| Type | String |
	| Default Value | `utf8` |
	Use *`charset_name`* as the default character set. See [Section 12.15, “Character Set Configuration”](charset-configuration.md). If no character set is specified, **mysqlpump** uses `utf8mb4`.
- ``--default-parallelism=*`N`*``
	| Command-Line Format | `--default-parallelism=N` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `2` |
	The default number of threads for each parallel processing queue. The default is 2.
	The `--parallel-schemas` option also affects parallelism and can be used to override the default number of threads. For more information, see mysqlpump Parallel Processing.
	With `--default-parallelism=0` and no `--parallel-schemas` options, **mysqlpump** runs as a single-threaded process and creates no queues.
	With parallelism enabled, it is possible for output from different databases to be interleaved.
- ``--defaults-extra-file=*`file_name`*``
	| Command-Line Format | `--defaults-extra-file=file_name` |
	| --- | --- |
	| Type | File name |
	Read this option file after the global option file but (on Unix) before the user option file. If the file does not exist or is otherwise inaccessible, an error occurs. If *`file_name`* is not an absolute path name, it is interpreted relative to the current directory.
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--defaults-file=*`file_name`*``
	| Command-Line Format | `--defaults-file=file_name` |
	| --- | --- |
	| Type | File name |
	Use only the given option file. If the file does not exist or is otherwise inaccessible, an error occurs. If *`file_name`* is not an absolute path name, it is interpreted relative to the current directory.
	Exception: Even with [`--defaults-file`](option-file-options.md), client programs read `.mylogin.cnf`.
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--defaults-group-suffix=*`str`*``
	| Command-Line Format | `--defaults-group-suffix=str` |
	| --- | --- |
	| Type | String |
	Read not only the usual option groups, but also groups with the usual names and a suffix of *`str`*. For example, **mysqlpump** normally reads the `[client]` and `[mysqlpump]` groups. If this option is given as `--defaults-group-suffix=_other`, **mysqlpump** also reads the `[client_other]` and `[mysqlpump_other]` groups.
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--defer-table-indexes`
	| Command-Line Format | `--defer-table-indexes` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `TRUE` |
	In the dump output, defer index creation for each table until after its rows have been loaded. This works for all storage engines, but for `InnoDB` applies only for secondary indexes.
	This option is enabled by default; use `--skip-defer-table-indexes` to disable it.
- `--events`
	| Command-Line Format | `--events` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `TRUE` |
	Include Event Scheduler events for the dumped databases in the output. Event dumping requires the [`EVENT`](privileges-provided.md) privileges for those databases.
	The output generated by using `--events` contains [`CREATE EVENT`](create-event.md) statements to create the events.
	This option is enabled by default; use `--skip-events` to disable it.
- ``--exclude-databases=*`db_list`*``
	| Command-Line Format | `--exclude-databases=db_list` |
	| --- | --- |
	| Type | String |
	Do not dump the databases in *`db_list`*, which is a list of one or more comma-separated database names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.
- ``--exclude-events=*`event_list`*``
	| Command-Line Format | `--exclude-events=event_list` |
	| --- | --- |
	| Type | String |
	Do not dump the databases in *`event_list`*, which is a list of one or more comma-separated event names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.
- ``--exclude-routines=*`routine_list`*``
	| Command-Line Format | `--exclude-routines=routine_list` |
	| --- | --- |
	| Type | String |
	Do not dump the events in *`routine_list`*, which is a list of one or more comma-separated routine (stored procedure or function) names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.
- ``--exclude-tables=*`table_list`*``
	| Command-Line Format | `--exclude-tables=table_list` |
	| --- | --- |
	| Type | String |
	Do not dump the tables in *`table_list`*, which is a list of one or more comma-separated table names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.
- ``--exclude-triggers=*`trigger_list`*``
	| Command-Line Format | `--exclude-triggers=trigger_list` |
	| --- | --- |
	| Type | String |
	Do not dump the triggers in *`trigger_list`*, which is a list of one or more comma-separated trigger names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.
- ``--exclude-users=*`user_list`*``
	| Command-Line Format | `--exclude-users=user_list` |
	| --- | --- |
	| Type | String |
	Do not dump the user accounts in *`user_list`*, which is a list of one or more comma-separated account names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.
- ``--extended-insert=*`N`*``
	| Command-Line Format | `--extended-insert=N` |
	| --- | --- |
	Write [`INSERT`](insert.md) statements using multiple-row syntax that includes several `VALUES` lists. This results in a smaller dump file and speeds up inserts when the file is reloaded.
	The option value indicates the number of rows to include in each [`INSERT`](insert.md) statement. The default is 250. A value of 1 produces one [`INSERT`](insert.md) statement per table row.
- `--get-server-public-key`
	| Command-Line Format | `--get-server-public-key` |
	| --- | --- |
	| Type | Boolean |
	Request from the server the public key required for RSA key pair-based password exchange. This option applies to clients that authenticate with the `caching_sha2_password` authentication plugin. For that plugin, the server does not send the public key unless requested. This option is ignored for accounts that do not authenticate with that plugin. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection.
	If ``--server-public-key-path=*`file_name`*`` is given and specifies a valid public key file, it takes precedence over `--get-server-public-key`.
	For information about the `caching_sha2_password` plugin, see [Section 8.4.1.2, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).
- `--hex-blob`
	| Command-Line Format | `--hex-blob` |
	| --- | --- |
	Dump binary columns using hexadecimal notation (for example, `'abc'` becomes `0x616263`). The affected data types are [`BINARY`](binary-varbinary.md), [`VARBINARY`](binary-varbinary.md), [`BLOB`](blob.md) types, [`BIT`](bit-type.md), all spatial data types, and other non-binary data types when used with the [`binary` character set](charset-binary-set.md).
- ``--host=*`host_name`*``, ``-h *`host_name`*``
	| Command-Line Format | `--host` |
	| --- | --- |
	Dump data from the MySQL server on the given host.
- ``--include-databases=*`db_list`*``
	| Command-Line Format | `--include-databases=db_list` |
	| --- | --- |
	| Type | String |
	Dump the databases in *`db_list`*, which is a list of one or more comma-separated database names. The dump includes all objects in the named databases. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.
- ``--include-events=*`event_list`*``
	| Command-Line Format | `--include-events=event_list` |
	| --- | --- |
	| Type | String |
	Dump the events in *`event_list`*, which is a list of one or more comma-separated event names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.
- ``--include-routines=*`routine_list`*``
	| Command-Line Format | `--include-routines=routine_list` |
	| --- | --- |
	| Type | String |
	Dump the routines in *`routine_list`*, which is a list of one or more comma-separated routine (stored procedure or function) names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.
- ``--include-tables=*`table_list`*``
	| Command-Line Format | `--include-tables=table_list` |
	| --- | --- |
	| Type | String |
	Dump the tables in *`table_list`*, which is a list of one or more comma-separated table names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.
- ``--include-triggers=*`trigger_list`*``
	| Command-Line Format | `--include-triggers=trigger_list` |
	| --- | --- |
	| Type | String |
	Dump the triggers in *`trigger_list`*, which is a list of one or more comma-separated trigger names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.
- ``--include-users=*`user_list`*``
	| Command-Line Format | `--include-users=user_list` |
	| --- | --- |
	| Type | String |
	Dump the user accounts in *`user_list`*, which is a list of one or more comma-separated user names. Multiple instances of this option are additive. For more information, see mysqlpump Object Selection.
- `--insert-ignore`
	| Command-Line Format | `--insert-ignore` |
	| --- | --- |
	Write [`INSERT             IGNORE`](insert.md) statements rather than [`INSERT`](insert.md) statements.
- ``--log-error-file=*`file_name`*``
	| Command-Line Format | `--log-error-file=file_name` |
	| --- | --- |
	| Type | File name |
	Log warnings and errors by appending them to the named file. If this option is not given, **mysqlpump** writes warnings and errors to the standard error output.
- ``--login-path=*`name`*``
	| Command-Line Format | `--login-path=name` |
	| --- | --- |
	| Type | String |
	Read options from the named login path in the `.mylogin.cnf` login path file. A “login path” is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 6.6.7, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--max-allowed-packet=*`N`*``
	| Command-Line Format | `--max-allowed-packet=N` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `25165824` |
	The maximum size of the buffer for client/server communication. The default is 24MB, the maximum is 1GB.
- ``--net-buffer-length=*`N`*``
	| Command-Line Format | `--net-buffer-length=N` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `1047552` |
	The initial size of the buffer for client/server communication. When creating multiple-row [`INSERT`](insert.md) statements (as with the `--extended-insert` option), **mysqlpump** creates rows up to *`N`* bytes long. If you use this option to increase the value, ensure that the MySQL server [`net_buffer_length`](server-system-variables.md) system variable has a value at least this large.
- `--no-create-db`
	| Command-Line Format | `--no-create-db` |
	| --- | --- |
	Suppress any [`CREATE DATABASE`](create-database.md) statements that might otherwise be included in the output.
- `--no-create-info`, `-t`
	| Command-Line Format | `--no-create-info` |
	| --- | --- |
	Do not write [`CREATE TABLE`](create-table.md) statements that create each dumped table.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read any option files. If program startup fails due to reading unknown options from an option file, `--no-defaults` can be used to prevent them from being read.
	The exception is that the `.mylogin.cnf` file is read in all cases, if it exists. This permits passwords to be specified in a safer way than on the command line even when `--no-defaults` is used. To create `.mylogin.cnf`, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 6.6.7, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- [``--parallel-schemas=[*`N`*:]*`db_list`*``](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysqlpump.html#option_mysqlpump_parallel-schemas)
	| Command-Line Format | `--parallel-schemas=[N:]schema_list` |
	| --- | --- |
	| Type | String |
	Create a queue for processing the databases in *`db_list`*, which is a list of one or more comma-separated database names. If *`N`* is given, the queue uses *`N`* threads. If *`N`* is not given, the `--default-parallelism` option determines the number of queue threads.
	Multiple instances of this option create multiple queues. **mysqlpump** also creates a default queue to use for databases not named in any `--parallel-schemas` option, and for dumping user definitions if command options select them. For more information, see mysqlpump Parallel Processing.
- [``--password[=*`password`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysqlpump.html#option_mysqlpump_password), ``-p[*`password`*]``
	| Command-Line Format | `--password[=password]` |
	| --- | --- |
	| Type | String |
	The password of the MySQL account used for connecting to the server. The password value is optional. If not given, **mysqlpump** prompts for one. If given, there must be *no space* between `--password=` or `-p` and the password following it. If no password option is specified, the default is to send no password.
	Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See [Section 8.1.2.1, “End-User Guidelines for Password Security”](password-security-user.md).
	To explicitly specify that there is no password and that **mysqlpump** should not prompt for one, use the `--skip-password` option.
- [``--password1[=*`pass_val`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysqlpump.html#option_mysqlpump_password1)
	The password for multifactor authentication factor 1 of the MySQL account used for connecting to the server. The password value is optional. If not given, **mysqlpump** prompts for one. If given, there must be *no space* between `--password1=` and the password following it. If no password option is specified, the default is to send no password.
	Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See [Section 8.1.2.1, “End-User Guidelines for Password Security”](password-security-user.md).
	To explicitly specify that there is no password and that **mysqlpump** should not prompt for one, use the `--skip-password1` option.
	`--password1` and `--password` are synonymous, as are `--skip-password1` and `--skip-password`.
- [``--password2[=*`pass_val`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysqlpump.html#option_mysqlpump_password2)
	The password for multifactor authentication factor 2 of the MySQL account used for connecting to the server. The semantics of this option are similar to the semantics for `--password1`; see the description of that option for details.
- [``--password3[=*`pass_val`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysqlpump.html#option_mysqlpump_password3)
	The password for multifactor authentication factor 3 of the MySQL account used for connecting to the server. The semantics of this option are similar to the semantics for `--password1`; see the description of that option for details.
- ``--plugin-dir=*`dir_name`*``
	| Command-Line Format | `--plugin-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The directory in which to look for plugins. Specify this option if the `--default-auth` option is used to specify an authentication plugin but **mysqlpump** does not find it. See [Section 8.2.17, “Pluggable Authentication”](pluggable-authentication.md).
- ``--port=*`port_num`*``, ``-P *`port_num`*``
	| Command-Line Format | `--port=port_num` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `3306` |
	For TCP/IP connections, the port number to use.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print the program name and all options that it gets from option files.
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--protocol={TCP|SOCKET|PIPE|MEMORY}`
	| Command-Line Format | `--protocol=type` |
	| --- | --- |
	| Type | String |
	| Default Value | `[see text]` |
	| Valid Values | `TCP`  `SOCKET`  `PIPE`  `MEMORY` |
	The transport protocol to use for connecting to the server. It is useful when the other connection parameters normally result in use of a protocol other than the one you want. For details on the permissible values, see [Section 6.2.7, “Connection Transport Protocols”](transport-protocols.md).
- `--replace`
	| Command-Line Format | `--replace` |
	| --- | --- |
	Write [`REPLACE`](replace.md) statements rather than [`INSERT`](insert.md) statements.
- ``--result-file=*`file_name`*``
	| Command-Line Format | `--result-file=file_name` |
	| --- | --- |
	| Type | File name |
	Direct output to the named file. The result file is created and its previous contents overwritten, even if an error occurs while generating the dump.
	This option should be used on Windows to prevent newline `\n` characters from being converted to `\r\n` carriage return/newline sequences.
- `--routines`
	| Command-Line Format | `--routines` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `TRUE` |
	Include stored routines (procedures and functions) for the dumped databases in the output. This option requires the global [`SELECT`](privileges-provided.md) privilege.
	The output generated by using `--routines` contains [`CREATE PROCEDURE`](create-procedure.md) and [`CREATE FUNCTION`](create-function.md) statements to create the routines.
	This option is enabled by default; use `--skip-routines` to disable it.
- ``--server-public-key-path=*`file_name`*``
	| Command-Line Format | `--server-public-key-path=file_name` |
	| --- | --- |
	| Type | File name |
	The path name to a file in PEM format containing a client-side copy of the public key required by the server for RSA key pair-based password exchange. This option applies to clients that authenticate with the `sha256_password` or `caching_sha2_password` authentication plugin. This option is ignored for accounts that do not authenticate with one of those plugins. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection.
	If ``--server-public-key-path=*`file_name`*`` is given and specifies a valid public key file, it takes precedence over `--get-server-public-key`.
	For `sha256_password`, this option applies only if MySQL was built using OpenSSL.
	For information about the `sha256_password` and `caching_sha2_password` plugins, see [Section 8.4.1.3, “SHA-256 Pluggable Authentication”](sha256-pluggable-authentication.md), and [Section 8.4.1.2, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).
- `--set-charset`
	| Command-Line Format | `--set-charset` |
	| --- | --- |
	Write [``SET NAMES             *`default_character_set`*``](set-names.md) to the output.
	This option is enabled by default. To disable it and suppress the [`SET NAMES`](set-names.md) statement, use `--skip-set-charset`.
- ``--set-gtid-purged=*`value`*``
	| Command-Line Format | `--set-gtid-purged=value` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `AUTO` |
	| Valid Values | `OFF`  `ON`  `AUTO` |
	This option enables control over global transaction ID (GTID) information written to the dump file, by indicating whether to add a [`SET             @@GLOBAL.gtid_purged`](set-variable.md) statement to the output. This option may also cause a statement to be written to the output that disables binary logging while the dump file is being reloaded.
	The following table shows the permitted option values. The default value is `AUTO`.
	| Value | Meaning |
	| --- | --- |
	| `OFF` | Add no `SET` statement to the output. |
	| `ON` | Add a `SET` statement to the output. An error occurs if GTIDs are not enabled on the server. |
	| `AUTO` | Add a `SET` statement to the output if GTIDs are enabled on the server. |
	The `--set-gtid-purged` option has the following effect on binary logging when the dump file is reloaded:
	- `--set-gtid-purged=OFF`: `SET                 @@SESSION.SQL_LOG_BIN=0;` is not added to the output.
	- `--set-gtid-purged=ON`: `SET                 @@SESSION.SQL_LOG_BIN=0;` is added to the output.
	- `--set-gtid-purged=AUTO`: `SET                 @@SESSION.SQL_LOG_BIN=0;` is added to the output if GTIDs are enabled on the server you are backing up (that is, if `AUTO` evaluates to `ON`).
- `--single-transaction`
	| Command-Line Format | `--single-transaction` |
	| --- | --- |
	This option sets the transaction isolation mode to [`REPEATABLE READ`](innodb-transaction-isolation-levels.md) and sends a [`START             TRANSACTION`](commit.md) SQL statement to the server before dumping data. It is useful only with transactional tables such as `InnoDB`, because then it dumps the consistent state of the database at the time when [`START             TRANSACTION`](commit.md) was issued without blocking any applications.
	When using this option, you should keep in mind that only `InnoDB` tables are dumped in a consistent state. For example, any `MyISAM` or `MEMORY` tables dumped while using this option may still change state.
	While a `--single-transaction` dump is in process, to ensure a valid dump file (correct table contents and binary log coordinates), no other connection should use the following statements: [`ALTER TABLE`](alter-table.md), [`CREATE TABLE`](create-table.md), [`DROP TABLE`](drop-table.md), [`RENAME TABLE`](rename-table.md), [`TRUNCATE TABLE`](truncate-table.md). A consistent read is not isolated from those statements, so use of them on a table to be dumped can cause the [`SELECT`](select.md) that is performed by **mysqlpump** to retrieve the table contents to obtain incorrect contents or fail.
	`--add-locks` and `--single-transaction` are mutually exclusive.
- `--skip-definer`
	| Command-Line Format | `--skip-definer` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Omit `DEFINER` and `SQL             SECURITY` clauses from the `CREATE` statements for views and stored programs. The dump file, when reloaded, creates objects that use the default `DEFINER` and `SQL             SECURITY` values. See [Section 27.6, “Stored Object Access Control”](stored-objects-security.md).
- `--skip-dump-rows`, `-d`
	| Command-Line Format | `--skip-dump-rows` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Do not dump table rows.
- `--skip-generated-invisible-primary-key`
	| Command-Line Format | `--skip-generated-invisible-primary-key` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	This option is available beginning with MySQL 8.0.30, and causes generated invisible primary keys (GIPKs) to be excluded from the dump. See [Section 15.1.20.11, “Generated Invisible Primary Keys”](create-table-gipks.md), for more information about GIPKs and GIPK mode.
- ``--socket=*`path`*``, ``-S *`path`*``
	| Command-Line Format | `--socket={file_name\|pipe_name}` |
	| --- | --- |
	| Type | String |
	For connections to `localhost`, the Unix socket file to use, or, on Windows, the name of the named pipe to use.
	On Windows, this option applies only if the server was started with the [`named_pipe`](server-system-variables.md) system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the [`named_pipe_full_access_group`](server-system-variables.md) system variable.
- `--ssl*`
	Options that begin with `--ssl` specify whether to connect to the server using encryption and indicate where to find SSL keys and certificates. See [Command Options for Encrypted Connections](connection-options.md).
- `--ssl-fips-mode={OFF|ON|STRICT}`
	| Command-Line Format | `--ssl-fips-mode={OFF\|ON\|STRICT}` |
	| --- | --- |
	| Deprecated | Yes |
	| Type | Enumeration |
	| Default Value | `OFF` |
	| Valid Values | `OFF`  `ON`  `STRICT` |
	Controls whether to enable FIPS mode on the client side. The `--ssl-fips-mode` option differs from other ``--ssl-*`xxx`*`` options in that it is not used to establish encrypted connections, but rather to affect which cryptographic operations to permit. See [Section 8.8, “FIPS Support”](fips-mode.md).
	These `--ssl-fips-mode` values are permitted:
	- `OFF`: Disable FIPS mode.
	- `ON`: Enable FIPS mode.
	- `STRICT`: Enable “strict” FIPS mode.
	Note
	If the OpenSSL FIPS Object Module is not available, the only permitted value for `--ssl-fips-mode` is `OFF`. In this case, setting `--ssl-fips-mode` to `ON` or `STRICT` causes the client to produce a warning at startup and to operate in non-FIPS mode.
	As of MySQL 8.0.34, this option is deprecated. Expect it to be removed in a future version of MySQL.
- ``--tls-ciphersuites=*`ciphersuite_list`*``
	| Command-Line Format | `--tls-ciphersuites=ciphersuite_list` |
	| --- | --- |
	| Type | String |
	The permissible ciphersuites for encrypted connections that use TLSv1.3. The value is a list of one or more colon-separated ciphersuite names. The ciphersuites that can be named for this option depend on the SSL library used to compile MySQL. For details, see [Section 8.3.2, “Encrypted Connection TLS Protocols and Ciphers”](encrypted-connection-protocols-ciphers.md).
	This option was added in MySQL 8.0.16.
- ``--tls-version=*`protocol_list`*``
	| Command-Line Format | `--tls-version=protocol_list` |
	| --- | --- |
	| Type | String |
	| Default Value | `TLSv1,TLSv1.1,TLSv1.2,TLSv1.3` (OpenSSL 1.1.1 or higher)  `TLSv1,TLSv1.1,TLSv1.2` (otherwise) |
	The permissible TLS protocols for encrypted connections. The value is a list of one or more comma-separated protocol names. The protocols that can be named for this option depend on the SSL library used to compile MySQL. For details, see [Section 8.3.2, “Encrypted Connection TLS Protocols and Ciphers”](encrypted-connection-protocols-ciphers.md).
- `--triggers`
	| Command-Line Format | `--triggers` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `TRUE` |
	Include triggers for each dumped table in the output.
	This option is enabled by default; use `--skip-triggers` to disable it.
- `--tz-utc`
	| Command-Line Format | `--tz-utc` |
	| --- | --- |
	This option enables [`TIMESTAMP`](datetime.md) columns to be dumped and reloaded between servers in different time zones. **mysqlpump** sets its connection time zone to UTC and adds `SET             TIME_ZONE='+00:00'` to the dump file. Without this option, [`TIMESTAMP`](datetime.md) columns are dumped and reloaded in the time zones local to the source and destination servers, which can cause the values to change if the servers are in different time zones. `--tz-utc` also protects against changes due to daylight saving time.
	This option is enabled by default; use `--skip-tz-utc` to disable it.
- ``--user=*`user_name`*``, ``-u *`user_name`*``
	| Command-Line Format | `--user=user_name` |
	| --- | --- |
	| Type | String |
	The user name of the MySQL account to use for connecting to the server.
	If you are using the `Rewriter` plugin with MySQL 8.0.31 or later, you should grant this user the [`SKIP_QUERY_REWRITE`](privileges-provided.md) privilege.
- `--users`
	| Command-Line Format | `--users` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Dump user accounts as logical definitions in the form of [`CREATE USER`](create-user.md) and [`GRANT`](grant.md) statements.
	User definitions are stored in the grant tables in the `mysql` system database. By default, **mysqlpump** does not include the grant tables in `mysql` database dumps. To dump the contents of the grant tables as logical definitions, use the `--users` option and suppress all database dumping:
	```
	mysqlpump --exclude-databases=% --users
	```
- `--version`, `-V`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.
- `--watch-progress`
	| Command-Line Format | `--watch-progress` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `TRUE` |
	Periodically display a progress indicator that provides information about the completed and total number of tables, rows, and other objects.
	This option is enabled by default; use `--skip-watch-progress` to disable it.
- ``--zstd-compression-level=*`level`*``
	| Command-Line Format | `--zstd-compression-level=#` |
	| --- | --- |
	| Type | Integer |
	The compression level to use for connections to the server that use the `zstd` compression algorithm. The permitted levels are from 1 to 22, with larger values indicating increasing levels of compression. The default `zstd` compression level is 3. The compression level setting has no effect on connections that do not use `zstd` compression.
	For more information, see [Section 6.2.8, “Connection Compression Control”](connection-compression-control.md).
	This option was added in MySQL 8.0.18.

#### mysqlpump Object Selection

**mysqlpump** has a set of inclusion and exclusion options that enable filtering of several object types and provide flexible control over which objects to dump:

- `--include-databases` and `--exclude-databases` apply to databases and all objects within them.
- `--include-tables` and `--exclude-tables` apply to tables. These options also affect triggers associated with tables unless the trigger-specific options are given.
- `--include-triggers` and `--exclude-triggers` apply to triggers.
- `--include-routines` and `--exclude-routines` apply to stored procedures and functions. If a routine option matches a stored procedure name, it also matches a stored function of the same name.
- `--include-events` and `--exclude-events` apply to Event Scheduler events.
- `--include-users` and `--exclude-users` apply to user accounts.

Any inclusion or exclusion option may be given multiple times. The effect is additive. Order of these options does not matter.

The value of each inclusion and exclusion option is a list of comma-separated names of the appropriate object type. For example:

```
--exclude-databases=test,world
--include-tables=customer,invoice
```

Wildcard characters are permitted in the object names:

- `%` matches any sequence of zero or more characters.
- `_` matches any single character.

For example, `--include-tables=t%,__tmp` matches all table names that begin with `t` and all five-character table names that end with `tmp`.

For users, a name specified without a host part is interpreted with an implied host of `%`. For example, `u1` and `u1@%` are equivalent. This is the same equivalence that applies in MySQL generally (see [Section 8.2.4, “Specifying Account Names”](account-names.md)).

Inclusion and exclusion options interact as follows:

- By default, with no inclusion or exclusion options, **mysqlpump** dumps all databases (with certain exceptions noted in mysqlpump Restrictions).
- If inclusion options are given in the absence of exclusion options, only the objects named as included are dumped.
- If exclusion options are given in the absence of inclusion options, all objects are dumped except those named as excluded.
- If inclusion and exclusion options are given, all objects named as excluded and not named as included are not dumped. All other objects are dumped.

If multiple databases are being dumped, it is possible to name tables, triggers, and routines in a specific database by qualifying the object names with the database name. The following command dumps databases `db1` and `db2`, but excludes tables `db1.t1` and `db2.t2`:

```
mysqlpump --include-databases=db1,db2 --exclude-tables=db1.t1,db2.t2
```

The following options provide alternative ways to specify which databases to dump:

- The `--all-databases` option dumps all databases (with certain exceptions noted in mysqlpump Restrictions). It is equivalent to specifying no object options at all (the default **mysqlpump** action is to dump everything).
	`--include-databases=%` is similar to `--all-databases`, but selects all databases for dumping, even those that are exceptions for `--all-databases`.
- The `--databases` option causes **mysqlpump** to treat all name arguments as names of databases to dump. It is equivalent to an `--include-databases` option that names the same databases.

#### mysqlpump Parallel Processing

**mysqlpump** can use parallelism to achieve concurrent processing. You can select concurrency between databases (to dump multiple databases simultaneously) and within databases (to dump multiple objects from a given database simultaneously).

By default, **mysqlpump** sets up one queue with two threads. You can create additional queues and control the number of threads assigned to each one, including the default queue:

- ``--default-parallelism=*`N`*`` specifies the default number of threads used for each queue. In the absence of this option, *`N`* is 2.
	The default queue always uses the default number of threads. Additional queues use the default number of threads unless you specify otherwise.
- [``--parallel-schemas=[*`N`*:]*`db_list`*``](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysqlpump.html#option_mysqlpump_parallel-schemas) sets up a processing queue for dumping the databases named in *`db_list`* and optionally specifies how many threads the queue uses. *`db_list`* is a list of comma-separated database names. If the option argument begins with ``*`N`*:``, the queue uses *`N`* threads. Otherwise, the `--default-parallelism` option determines the number of queue threads.
	Multiple instances of the `--parallel-schemas` option create multiple queues.
	Names in the database list are permitted to contain the same `%` and `_` wildcard characters supported for filtering options (see mysqlpump Object Selection).

**mysqlpump** uses the default queue for processing any databases not named explicitly with a `--parallel-schemas` option, and for dumping user definitions if command options select them.

In general, with multiple queues, **mysqlpump** uses parallelism between the sets of databases processed by the queues, to dump multiple databases simultaneously. For a queue that uses multiple threads, **mysqlpump** uses parallelism within databases, to dump multiple objects from a given database simultaneously. Exceptions can occur; for example, **mysqlpump** may block queues while it obtains from the server lists of objects in databases.

With parallelism enabled, it is possible for output from different databases to be interleaved. For example, [`INSERT`](insert.md) statements from multiple tables dumped in parallel can be interleaved; the statements are not written in any particular order. This does not affect reloading because output statements qualify object names with database names or are preceded by [`USE`](use.md) statements as required.

The granularity for parallelism is a single database object. For example, a single table cannot be dumped in parallel using multiple threads.

Examples:

```
mysqlpump --parallel-schemas=db1,db2 --parallel-schemas=db3
```

**mysqlpump** sets up a queue to process `db1` and `db2`, another queue to process `db3`, and a default queue to process all other databases. All queues use two threads.

```
mysqlpump --parallel-schemas=db1,db2 --parallel-schemas=db3
          --default-parallelism=4
```

This is the same as the previous example except that all queues use four threads.

```
mysqlpump --parallel-schemas=5:db1,db2 --parallel-schemas=3:db3
```

The queue for `db1` and `db2` uses five threads, the queue for `db3` uses three threads, and the default queue uses the default of two threads.

As a special case, with `--default-parallelism=0` and no `--parallel-schemas` options, **mysqlpump** runs as a single-threaded process and creates no queues.

#### mysqlpump Restrictions

**mysqlpump** does not dump the `performance_schema`, `ndbinfo`, or `sys` schema by default. To dump any of these, name them explicitly on the command line. You can also name them with the `--databases` or `--include-databases` option.

**mysqlpump** does not dump the `INFORMATION_SCHEMA` schema.

**mysqlpump** does not dump `InnoDB` [`CREATE         TABLESPACE`](create-tablespace.md) statements.

**mysqlpump** dumps user accounts in logical form using [`CREATE USER`](create-user.md) and [`GRANT`](grant.md) statements (for example, when you use the `--include-users` or `--users` option). For this reason, dumps of the `mysql` system database do not by default include the grant tables that contain user definitions: `user`, `db`, `tables_priv`, `columns_priv`, `procs_priv`, or `proxies_priv`. To dump any of the grant tables, name the `mysql` database followed by the table names:

```
mysqlpump mysql user db ...
```