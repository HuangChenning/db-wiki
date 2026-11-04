---
title: "4.6.7 mysqlbinlog — Utility for Processing Binary Log Files"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysqlbinlog.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 4.6.7 mysqlbinlog — Utility for Processing Binary Log Files

The server's binary log consists of files containing “events” that describe modifications to database contents. The server writes these files in binary format. To display their contents in text format, use the **mysqlbinlog** utility. You can also use **mysqlbinlog** to display the contents of relay log files written by a replica server in a replication setup because relay logs have the same format as binary logs. The binary log and relay log are discussed further in [Section 5.4.4, “The Binary Log”](binary-log.md), and [Section 16.2.4, “Relay Log and Replication Metadata Repositories”](replica-logs.md).

Invoke **mysqlbinlog** like this:

```
mysqlbinlog [options] log_file ...
```

For example, to display the contents of the binary log file named `binlog.000003`, use this command:

```
mysqlbinlog binlog.000003
```

The output includes events contained in `binlog.000003`. For statement-based logging, event information includes the SQL statement, the ID of the server on which it was executed, the timestamp when the statement was executed, how much time it took, and so forth. For row-based logging, the event indicates a row change rather than an SQL statement. See [Section 16.2.1, “Replication Formats”](replication-formats.md), for information about logging modes.

Events are preceded by header comments that provide additional information. For example:

```
# at 141
#100309  9:28:36 server id 123  end_log_pos 245
  Query thread_id=3350  exec_time=11  error_code=0
```

In the first line, the number following `at` indicates the file offset, or starting position, of the event in the binary log file.

The second line starts with a date and time indicating when the statement started on the server where the event originated. For replication, this timestamp is propagated to replica servers. `server id` is the [`server_id`](replication-options.md) value of the server where the event originated. `end_log_pos` indicates where the next event starts (that is, it is the end position of the current event + 1). `thread_id` indicates which thread executed the event. `exec_time` is the time spent executing the event, on a replication source server. On a replica, it is the difference of the end execution time on the replica minus the beginning execution time on the source. The difference serves as an indicator of how much replication lags behind the source. `error_code` indicates the result from executing the event. Zero means that no error occurred.

Note

When using event groups, the file offsets of events may be grouped together and the comments of events may be grouped together. Do not mistake these grouped events for blank file offsets.

The output from **mysqlbinlog** can be re-executed (for example, by using it as input to [**mysql**](mysql.md)) to redo the statements in the log. This is useful for recovery operations after an unexpected server exit. For other usage examples, see the discussion later in this section and in [Section 7.5, “Point-in-Time (Incremental) Recovery”](point-in-time-recovery.md).

You can use **mysqlbinlog** to read binary log files directly and apply them to the local MySQL server. You can also read binary logs from a remote server by using the `--read-from-remote-server` option. To read remote binary logs, the connection parameter options can be given to indicate how to connect to the server. These options are `--host`, `--password`, `--port`, `--protocol`, `--socket`, and `--user`.

When running **mysqlbinlog** against a large binary log, be careful that the filesystem has enough space for the resulting files. To configure the directory that **mysqlbinlog** uses for temporary files, use the `TMPDIR` environment variable.

**mysqlbinlog** sets the value of [`pseudo_slave_mode`](server-system-variables.md) to true before executing any SQL statements. This system variable affects the handling of XA transactions.

**mysqlbinlog** supports the following options, which can be specified on the command line or in the `[mysqlbinlog]` and `[client]` groups of an option file. For information about option files used by MySQL programs, see [Section 4.2.2.2, “Using Option Files”](option-files.md).

**Table 4.23 mysqlbinlog Options**

| Option Name | Description | Deprecated |
| --- | --- | --- |
| \--base64-output | Print binary log entries using base-64 encoding |  |
| \--bind-address | Use specified network interface to connect to MySQL Server |  |
| \--binlog-row-event-max-size | Binary log max event size |  |
| \--character-sets-dir | Directory where character sets are installed |  |
| \--connection-server-id | Used for testing and debugging. See text for applicable default values and other particulars |  |
| \--database | List entries for just this database |  |
| \--debug | Write debugging log |  |
| \--debug-check | Print debugging information when program exits |  |
| \--debug-info | Print debugging information, memory, and CPU statistics when program exits |  |
| \--default-auth | Authentication plugin to use |  |
| \--defaults-extra-file | Read named option file in addition to usual option files |  |
| \--defaults-file | Read only named option file |  |
| \--defaults-group-suffix | Option group suffix value |  |
| \--disable-log-bin | Disable binary logging |  |
| \--exclude-gtids | Do not show any of the groups in the GTID set provided |  |
| \--force-if-open | Read binary log files even if open or not closed properly |  |
| \--force-read | If mysqlbinlog reads a binary log event that it does not recognize, it prints a warning |  |
| \--get-server-public-key | Request RSA public key from server |  |
| \--help | Display help message and exit |  |
| \--hexdump | Display a hex dump of the log in comments |  |
| \--host | Host on which MySQL server is located |  |
| \--idempotent | Cause the server to use idempotent mode while processing binary log updates from this session only |  |
| \--include-gtids | Show only the groups in the GTID set provided |  |
| \--local-load | Prepare local temporary files for LOAD DATA in the specified directory |  |
| \--login-path | Read login path options from.mylogin.cnf |  |
| \--no-defaults | Read no option files |  |
| \--offset | Skip the first N entries in the log |  |
| \--open-files-limit | Specify the number of open file descriptors to reserve |  |
| \--password | Password to use when connecting to server |  |
| \--plugin-dir | Directory where plugins are installed |  |
| \--port | TCP/IP port number for connection |  |
| \--print-defaults | Print default options |  |
| \--protocol | Transport protocol to use |  |
| \--raw | Write events in raw (binary) format to output files |  |
| \--read-from-remote-master | Read the binary log from a MySQL replication source server rather than reading a local log file |  |
| \--read-from-remote-server | Read binary log from MySQL server rather than local log file |  |
| \--result-file | Direct output to named file |  |
| \--rewrite-db | Create rewrite rules for databases when playing back from logs written in row-based format. Can be used multiple times |  |
| \--secure-auth | Do not send passwords to server in old (pre-4.1) format | Yes |
| \--server-id | Extract only those events created by the server having the given server ID |  |
| \--server-id-bits | Tell mysqlbinlog how to interpret server IDs in binary log when log was written by a mysqld having its server-id-bits set to less than the maximum; supported only by MySQL Cluster version of mysqlbinlog |  |
| \--server-public-key-path | Path name to file containing RSA public key |  |
| \--set-charset | Add a SET NAMES charset\_name statement to the output |  |
| \--shared-memory-base-name | Shared-memory name for shared-memory connections (Windows only) |  |
| \--short-form | Display only the statements contained in the log |  |
| \--skip-gtids | Do not include the GTIDs from the binary log files in the output dump file |  |
| \--socket | Unix socket file or Windows named pipe to use |  |
| \--ssl | Enable connection encryption |  |
| \--ssl-ca | File that contains list of trusted SSL Certificate Authorities |  |
| \--ssl-capath | Directory that contains trusted SSL Certificate Authority certificate files |  |
| \--ssl-cert | File that contains X.509 certificate |  |
| \--ssl-cipher | Permissible ciphers for connection encryption |  |
| \--ssl-crl | File that contains certificate revocation lists |  |
| \--ssl-crlpath | Directory that contains certificate revocation-list files |  |
| \--ssl-key | File that contains X.509 key |  |
| \--ssl-mode | Desired security state of connection to server |  |
| \--ssl-verify-server-cert | Verify host name against server certificate Common Name identity |  |
| \--start-datetime | Read binary log from first event with timestamp equal to or later than datetime argument |  |
| \--start-position | Decode binary log from first event with position equal to or greater than argument |  |
| \--stop-datetime | Stop reading binary log at first event with timestamp equal to or greater than datetime argument |  |
| \--stop-never | Stay connected to server after reading last binary log file |  |
| \--stop-never-slave-server-id | Slave server ID to report when connecting to server |  |
| \--stop-position | Stop decoding binary log at first event with position equal to or greater than argument |  |
| \--tls-version | Permissible TLS protocols for encrypted connections |  |
| \--to-last-log | Do not stop at the end of requested binary log from a MySQL server, but rather continue printing to end of last binary log |  |
| \--user | MySQL user name to use when connecting to server |  |
| \--verbose | Reconstruct row events as SQL statements |  |
| \--verify-binlog-checksum | Verify checksums in binary log |  |
| \--version | Display version information and exit |  |

- `--help`, `-?`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display a help message and exit.
- ``--base64-output=*`value`*``
	| Command-Line Format | `--base64-output=value` |
	| --- | --- |
	| Type | String |
	| Default Value | `AUTO` |
	| Valid Values | `AUTO`  `NEVER`  `DECODE-ROWS` |
	This option determines when events should be displayed encoded as base-64 strings using [`BINLOG`](binlog.md) statements. The option has these permissible values (not case-sensitive):
	- `AUTO` ("automatic") or `UNSPEC` ("unspecified") displays [`BINLOG`](binlog.md) statements automatically when necessary (that is, for format description events and row events). If no `--base64-output` option is given, the effect is the same as `--base64-output=AUTO`.
		Note
		Automatic [`BINLOG`](binlog.md) display is the only safe behavior if you intend to use the output of **mysqlbinlog** to re-execute binary log file contents. The other option values are intended only for debugging or testing purposes because they may produce output that does not include all events in executable form.
	- `NEVER` causes [`BINLOG`](binlog.md) statements not to be displayed. **mysqlbinlog** exits with an error if a row event is found that must be displayed using [`BINLOG`](binlog.md).
	- `DECODE-ROWS` specifies to **mysqlbinlog** that you intend for row events to be decoded and displayed as commented SQL statements by also specifying the `--verbose` option. Like `NEVER`, `DECODE-ROWS` suppresses display of [`BINLOG`](binlog.md) statements, but unlike `NEVER`, it does not exit with an error if a row event is found.
	For examples that show the effect of `--base64-output` and `--verbose` on row event output, see [Section 4.6.7.2, “mysqlbinlog Row Event Display”](mysqlbinlog-row-events.md).
- ``--bind-address=*`ip_address`*``
	| Command-Line Format | `--bind-address=ip_address` |
	| --- | --- |
	On a computer having multiple network interfaces, use this option to select which interface to use for connecting to the MySQL server.
- ``--binlog-row-event-max-size=*`N`*``
	| Command-Line Format | `--binlog-row-event-max-size=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `4294967040` |
	| Minimum Value | `256` |
	| Maximum Value | `18446744073709547520` |
	Specify the maximum size of a row-based binary log event, in bytes. Rows are grouped into events smaller than this size if possible. The value should be a multiple of 256. The default is 4GB.
- ``--character-sets-dir=*`dir_name`*``
	| Command-Line Format | `--character-sets-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The directory where character sets are installed. See [Section 10.15, “Character Set Configuration”](charset-configuration.md).
- ``--connection-server-id=*`server_id`*``
	| Command-Line Format | `--connection-server-id=#]` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0 (1)` |
	| Minimum Value | `0 (1)` |
	| Maximum Value | `4294967295` |
	This option is used to test a MySQL server for support of the `BINLOG_DUMP_NON_BLOCK` connection flag. It is not required for normal operations.
	The effective default and minimum values for this option depend on whether **mysqlbinlog** is run in blocking mode or non-blocking mode. When **mysqlbinlog** is run in blocking mode, the default (and minimum) value is 1; when run in non-blocking mode, the default (and minimum) value is 0.
- ``--database=*`db_name`*``, ``-d *`db_name`*``
	| Command-Line Format | `--database=db_name` |
	| --- | --- |
	| Type | String |
	This option causes **mysqlbinlog** to output entries from the binary log (local log only) that occur while *`db_name`* is been selected as the default database by [`USE`](use.md).
	The `--database` option for **mysqlbinlog** is similar to the [`--binlog-do-db`](replication-options-binary-log.md) option for [**mysqld**](mysqld.md), but can be used to specify only one database. If `--database` is given multiple times, only the last instance is used.
	The effects of this option depend on whether the statement-based or row-based logging format is in use, in the same way that the effects of [`--binlog-do-db`](replication-options-binary-log.md) depend on whether statement-based or row-based logging is in use.
	**Statement-based logging.** The `--database` option works as follows:
	- While *`db_name`* is the default database, statements are output whether they modify tables in *`db_name`* or a different database.
	- Unless *`db_name`* is selected as the default database, statements are not output, even if they modify tables in *`db_name`*.
	- There is an exception for [`CREATE                 DATABASE`](create-database.md), [`ALTER                 DATABASE`](alter-database.md), and [`DROP                 DATABASE`](drop-database.md). The database being *created, altered, or dropped* is considered to be the default database when determining whether to output the statement.
	Suppose that the binary log was created by executing these statements using statement-based-logging:
	```
	INSERT INTO test.t1 (i) VALUES(100);
	INSERT INTO db2.t2 (j)  VALUES(200);
	USE test;
	INSERT INTO test.t1 (i) VALUES(101);
	INSERT INTO t1 (i)      VALUES(102);
	INSERT INTO db2.t2 (j)  VALUES(201);
	USE db2;
	INSERT INTO test.t1 (i) VALUES(103);
	INSERT INTO db2.t2 (j)  VALUES(202);
	INSERT INTO t2 (j)      VALUES(203);
	```
	**mysqlbinlog --database=test** does not output the first two [`INSERT`](insert.md) statements because there is no default database. It outputs the three [`INSERT`](insert.md) statements following [`USE             test`](use.md), but not the three [`INSERT`](insert.md) statements following [`USE db2`](use.md).
	**mysqlbinlog --database=db2** does not output the first two [`INSERT`](insert.md) statements because there is no default database. It does not output the three [`INSERT`](insert.md) statements following [`USE test`](use.md), but does output the three [`INSERT`](insert.md) statements following [`USE db2`](use.md).
	**Row-based logging.** **mysqlbinlog** outputs only entries that change tables belonging to *`db_name`*. The default database has no effect on this. Suppose that the binary log just described was created using row-based logging rather than statement-based logging. **mysqlbinlog --database=test** outputs only those entries that modify `t1` in the test database, regardless of whether [`USE`](use.md) was issued or what the default database is.
	If a server is running with [`binlog_format`](replication-options-binary-log.md) set to `MIXED` and you want it to be possible to use **mysqlbinlog** with the `--database` option, you must ensure that tables that are modified are in the database selected by [`USE`](use.md). (In particular, no cross-database updates should be used.)
	When used together with the `--rewrite-db` option, the `--rewrite-db` option is applied first; then the `--database` option is applied, using the rewritten database name. The order in which the options are provided makes no difference in this regard.
- [``--debug[=*`debug_options`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/mysqlbinlog.html#option_mysqlbinlog_debug), ``-#             [*`debug_options`*]``
	| Command-Line Format | `--debug[=debug_options]` |
	| --- | --- |
	| Type | String |
	| Default Value | `d:t:o,/tmp/mysqlbinlog.trace` |
	Write a debugging log. A typical *`debug_options`* string is ``d:t:o,*`file_name`*``. The default is `d:t:o,/tmp/mysqlbinlog.trace`.
	This option is available only if MySQL was built using [`WITH_DEBUG`](source-configuration-options.md). MySQL release binaries provided by Oracle are *not* built using this option.
- `--debug-check`
	| Command-Line Format | `--debug-check` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Print some debugging information when the program exits.
	This option is available only if MySQL was built using [`WITH_DEBUG`](source-configuration-options.md). MySQL release binaries provided by Oracle are *not* built using this option.
- `--debug-info`
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
	A hint about which client-side authentication plugin to use. See [Section 6.2.13, “Pluggable Authentication”](pluggable-authentication.md).
- ``--defaults-extra-file=*`file_name`*``
	| Command-Line Format | `--defaults-extra-file=file_name` |
	| --- | --- |
	| Type | File name |
	Read this option file after the global option file but (on Unix) before the user option file. If the file does not exist or is otherwise inaccessible, an error occurs. If *`file_name`* is not an absolute path name, it is interpreted relative to the current directory.
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--defaults-file=*`file_name`*``
	| Command-Line Format | `--defaults-file=file_name` |
	| --- | --- |
	| Type | File name |
	Use only the given option file. If the file does not exist or is otherwise inaccessible, an error occurs. If *`file_name`* is not an absolute path name, it is interpreted relative to the current directory.
	Exception: Even with [`--defaults-file`](option-file-options.md), client programs read `.mylogin.cnf`.
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--defaults-group-suffix=*`str`*``
	| Command-Line Format | `--defaults-group-suffix=str` |
	| --- | --- |
	| Type | String |
	Read not only the usual option groups, but also groups with the usual names and a suffix of *`str`*. For example, **mysqlbinlog** normally reads the `[client]` and `[mysqlbinlog]` groups. If this option is given as `--defaults-group-suffix=_other`, **mysqlbinlog** also reads the `[client_other]` and `[mysqlbinlog_other]` groups.
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--disable-log-bin`, `-D`
	| Command-Line Format | `--disable-log-bin` |
	| --- | --- |
	Disable binary logging. This is useful for avoiding an endless loop if you use the `--to-last-log` option and are sending the output to the same MySQL server. This option also is useful when restoring after an unexpected exit to avoid duplication of the statements you have logged.
	This option causes **mysqlbinlog** to include a [`SET             sql_log_bin = 0`](set-sql-log-bin.md) statement in its output to disable binary logging of the remaining output. Manipulating the session value of the [`sql_log_bin`](replication-options-binary-log.md) system variable is a restricted operation, so this option requires that you have privileges sufficient to set restricted session variables. See [Section 5.1.8.1, “System Variable Privileges”](system-variable-privileges.md).
- ``--exclude-gtids=*`gtid_set`*``
	| Command-Line Format | `--exclude-gtids=gtid_set` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	Do not display any of the groups listed in the *`gtid_set`*.
- `--force-if-open`, `-F`
	| Command-Line Format | `--force-if-open` |
	| --- | --- |
	Read binary log files even if they are open or were not closed properly.
- `--force-read`, `-f`
	| Command-Line Format | `--force-read` |
	| --- | --- |
	With this option, if **mysqlbinlog** reads a binary log event that it does not recognize, it prints a warning, ignores the event, and continues. Without this option, **mysqlbinlog** stops if it reads such an event.
- `--get-server-public-key`
	| Command-Line Format | `--get-server-public-key` |
	| --- | --- |
	| Type | Boolean |
	Request from the server the public key required for RSA key pair-based password exchange. This option applies to clients that authenticate with the `caching_sha2_password` authentication plugin. For that plugin, the server does not send the public key unless requested. This option is ignored for accounts that do not authenticate with that plugin. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection.
	If ``--server-public-key-path=*`file_name`*`` is given and specifies a valid public key file, it takes precedence over `--get-server-public-key`.
	For information about the `caching_sha2_password` plugin, see [Section 6.4.1.4, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).
	The `--get-server-public-key` option was added in MySQL 5.7.23.
- `--hexdump`, `-H`
	| Command-Line Format | `--hexdump` |
	| --- | --- |
	Display a hex dump of the log in comments, as described in [Section 4.6.7.1, “mysqlbinlog Hex Dump Format”](mysqlbinlog-hexdump.md). The hex output can be helpful for replication debugging.
- ``--host=*`host_name`*``, ``-h *`host_name`*``
	| Command-Line Format | `--host=host_name` |
	| --- | --- |
	| Type | String |
	| Default Value | `localhost` |
	Get the binary log from the MySQL server on the given host.
- `--idempotent`
	| Command-Line Format | `--idempotent` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `true` |
	Tell the MySQL Server to use idempotent mode while processing updates; this causes suppression of any duplicate-key or key-not-found errors that the server encounters in the current session while processing updates. This option may prove useful whenever it is desirable or necessary to replay one or more binary logs to a MySQL Server which may not contain all of the data to which the logs refer.
	The scope of effect for this option includes the current **mysqlbinlog** client and session only.
- ``--include-gtids=*`gtid_set`*``
	| Command-Line Format | `--include-gtids=gtid_set` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	Display only the groups listed in the *`gtid_set`*.
- ``--local-load=*`dir_name`*``, ``-l *`dir_name`*``
	| Command-Line Format | `--local-load=dir_name` |
	| --- | --- |
	| Type | Directory name |
	For data loading operations corresponding to [`LOAD DATA`](load-data.md) statements, **mysqlbinlog** extracts the files from the binary log events, writes them as temporary files to the local file system, and writes [`LOAD DATA             LOCAL`](load-data.md) statements to cause the files to be loaded. By default, **mysqlbinlog** writes these temporary files to an operating system-specific directory. The `--local-load` option can be used to explicitly specify the directory where **mysqlbinlog** should prepare local temporary files.
	Important
	These temporary files are not automatically removed by **mysqlbinlog** or any other MySQL program.
- ``--login-path=*`name`*``
	| Command-Line Format | `--login-path=name` |
	| --- | --- |
	| Type | String |
	Read options from the named login path in the `.mylogin.cnf` login path file. A “login path” is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 4.6.6, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read any option files. If program startup fails due to reading unknown options from an option file, `--no-defaults` can be used to prevent them from being read.
	The exception is that the `.mylogin.cnf` file is read in all cases, if it exists. This permits passwords to be specified in a safer way than on the command line even when `--no-defaults` is used. To create `.mylogin.cnf`, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 4.6.6, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--offset=*`N`*``, ``-o *`N`*``
	| Command-Line Format | `--offset=#` |
	| --- | --- |
	| Type | Numeric |
	Skip the first *`N`* entries in the log.
- ``--open-files-limit=*`N`*``
	| Command-Line Format | `--open-files-limit=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `8` |
	| Minimum Value | `1` |
	| Maximum Value | `[platform dependent]` |
	Specify the number of open file descriptors to reserve.
- [``--password[=*`password`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/mysqlbinlog.html#option_mysqlbinlog_password), ``-p[*`password`*]``
	| Command-Line Format | `--password[=password]` |
	| --- | --- |
	| Type | String |
	The password of the MySQL account used for connecting to the server. The password value is optional. If not given, **mysqlbinlog** prompts for one. If given, there must be *no space* between `--password=` or `-p` and the password following it. If no password option is specified, the default is to send no password.
	Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See [Section 6.1.2.1, “End-User Guidelines for Password Security”](password-security-user.md).
	To explicitly specify that there is no password and that **mysqlbinlog** should not prompt for one, use the `--skip-password` option.
- ``--plugin-dir=*`dir_name`*``
	| Command-Line Format | `--plugin-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The directory in which to look for plugins. Specify this option if the `--default-auth` option is used to specify an authentication plugin but **mysqlbinlog** does not find it. See [Section 6.2.13, “Pluggable Authentication”](pluggable-authentication.md).
- ``--port=*`port_num`*``, ``-P *`port_num`*``
	| Command-Line Format | `--port=port_num` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `3306` |
	The TCP/IP port number to use for connecting to a remote server.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print the program name and all options that it gets from option files.
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--protocol={TCP|SOCKET|PIPE|MEMORY}`
	| Command-Line Format | `--protocol=type` |
	| --- | --- |
	| Type | String |
	| Default Value | `[see text]` |
	| Valid Values | `TCP`  `SOCKET`  `PIPE`  `MEMORY` |
	The transport protocol to use for connecting to the server. It is useful when the other connection parameters normally result in use of a protocol other than the one you want. For details on the permissible values, see [Section 4.2.5, “Connection Transport Protocols”](transport-protocols.md).
- `--raw`
	| Command-Line Format | `--raw` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	By default, **mysqlbinlog** reads binary log files and writes events in text format. The `--raw` option tells **mysqlbinlog** to write them in their original binary format. Its use requires that `--read-from-remote-server` also be used because the files are requested from a server. **mysqlbinlog** writes one output file for each file read from the server. The `--raw` option can be used to make a backup of a server's binary log. With the `--stop-never` option, the backup is “live” because **mysqlbinlog** stays connected to the server. By default, output files are written in the current directory with the same names as the original log files. Output file names can be modified using the `--result-file` option. For more information, see [Section 4.6.7.3, “Using mysqlbinlog to Back Up Binary Log Files”](mysqlbinlog-backup.md).
- ``--read-from-remote-master=*`type`*``
	| Command-Line Format | `--read-from-remote-master=type` |
	| --- | --- |
	Read binary logs from a MySQL server with the `COM_BINLOG_DUMP` or `COM_BINLOG_DUMP_GTID` commands by setting the option value to either `BINLOG-DUMP-NON-GTIDS` or `BINLOG-DUMP-GTIDS`, respectively. If `--read-from-remote-master=BINLOG-DUMP-GTIDS` is combined with `--exclude-gtids`, transactions can be filtered out on the source, avoiding unnecessary network traffic.
	The connection parameter options are used with this option or the `--read-from-remote-server` option. These options are `--host`, `--password`, `--port`, `--protocol`, `--socket`, and `--user`. If neither of the remote options is specified, the connection parameter options are ignored.
	The [`REPLICATION SLAVE`](privileges-provided.md) privilege is required to use this option.
- ``--read-from-remote-server=*`file_name`*``, `-R`
	| Command-Line Format | `--read-from-remote-server=file_name` |
	| --- | --- |
	Read the binary log from a MySQL server rather than reading a local log file. This option requires that the remote server be running. It works only for binary log files on the remote server, not relay log files, and takes only the binary log file name (including the numeric suffix) as its argument, while ignoring any path.
	The connection parameter options are used with this option or the `--read-from-remote-master` option. These options are `--host`, `--password`, `--port`, `--protocol`, `--socket`, and `--user`. If neither of the remote options is specified, the connection parameter options are ignored.
	The [`REPLICATION SLAVE`](privileges-provided.md) privilege is required to use this option.
	This option is like `--read-from-remote-master=BINLOG-DUMP-NON-GTIDS`.
- ``--result-file=*`name`*``, ``-r *`name`*``
	| Command-Line Format | `--result-file=name` |
	| --- | --- |
	Without the `--raw` option, this option indicates the file to which **mysqlbinlog** writes text output. With `--raw`, **mysqlbinlog** writes one binary output file for each log file transferred from the server, writing them by default in the current directory using the same names as the original log file. In this case, the `--result-file` option value is treated as a prefix that modifies output file names.
- ``--rewrite-db='*`from_name`*->*`to_name`*'``
	| Command-Line Format | `--rewrite-db='oldname->newname'` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	When reading from a row-based or statement-based log, rewrite all occurrences of *`from_name`* to *`to_name`*. Rewriting is done on the rows, for row-based logs, as well as on the [`USE`](use.md) clauses, for statement-based logs. In MySQL versions prior to 5.7.8, this option was only for use when restoring tables logged using the row-based format.
	Warning
	Statements in which table names are qualified with database names are not rewritten to use the new name when using this option.
	The rewrite rule employed as a value for this option is a string having the form ``'*`from_name`*->*`to_name`*'``, as shown previously, and for this reason must be enclosed by quotation marks.
	To employ multiple rewrite rules, specify the option multiple times, as shown here:
	```
	mysqlbinlog --rewrite-db='dbcurrent->dbold' --rewrite-db='dbtest->dbcurrent' \
	    binlog.00001 > /tmp/statements.sql
	```
	When used together with the `--database` option, the `--rewrite-db` option is applied first; then `--database` option is applied, using the rewritten database name. The order in which the options are provided makes no difference in this regard.
	This means that, for example, if **mysqlbinlog** is started with `--rewrite-db='mydb->yourdb'             --database=yourdb`, then all updates to any tables in databases `mydb` and `yourdb` are included in the output. On the other hand, if it is started with `--rewrite-db='mydb->yourdb'             --database=mydb`, then **mysqlbinlog** outputs no statements at all: since all updates to `mydb` are first rewritten as updates to `yourdb` before applying the `--database` option, there remain no updates that match `--database=mydb`.
- `--secure-auth`
	| Command-Line Format | `--secure-auth` |
	| --- | --- |
	| Deprecated | Yes |
	Do not send passwords to the server in old (pre-4.1) format. This prevents connections except for servers that use the newer password format.
	As of MySQL 5.7.5, this option is deprecated; expect it to be removed in a future MySQL release. It is always enabled and attempting to disable it (`--skip-secure-auth`, `--secure-auth=0`) produces an error. Before MySQL 5.7.5, this option is enabled by default but can be disabled.
	Note
	Passwords that use the pre-4.1 hashing method are less secure than passwords that use the native password hashing method and should be avoided. Pre-4.1 passwords are deprecated and support for them was removed in MySQL 5.7.5. For account upgrade instructions, see [Section 6.4.1.3, “Migrating Away from Pre-4.1 Password Hashing and the mysql\_old\_password Plugin”](account-upgrades.md).
- ``--server-id=*`id`*``
	| Command-Line Format | `--server-id=id` |
	| --- | --- |
	| Type | Numeric |
	Display only those events created by the server having the given server ID.
- ``--server-id-bits=*`N`*``
	| Command-Line Format | `--server-id-bits=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `32` |
	| Minimum Value | `7` |
	| Maximum Value | `32` |
	Use only the first *`N`* bits of the [`server_id`](replication-options.md) to identify the server. If the binary log was written by a [**mysqld**](mysqld.md) with server-id-bits set to less than 32 and user data stored in the most significant bit, running **mysqlbinlog** with `--server-id-bits` set to 32 enables this data to be seen.
	This option is supported only by the version of **mysqlbinlog** supplied with the NDB Cluster distribution, or built with NDB Cluster support.
- ``--server-public-key-path=*`file_name`*``
	| Command-Line Format | `--server-public-key-path=file_name` |
	| --- | --- |
	| Type | File name |
	The path name to a file in PEM format containing a client-side copy of the public key required by the server for RSA key pair-based password exchange. This option applies to clients that authenticate with the `sha256_password` or `caching_sha2_password` authentication plugin. This option is ignored for accounts that do not authenticate with one of those plugins. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection.
	If ``--server-public-key-path=*`file_name`*`` is given and specifies a valid public key file, it takes precedence over `--get-server-public-key`.
	For `sha256_password`, this option applies only if MySQL was built using OpenSSL.
	For information about the `sha256_password` and `caching_sha2_password` plugins, see [Section 6.4.1.5, “SHA-256 Pluggable Authentication”](sha256-pluggable-authentication.md), and [Section 6.4.1.4, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).
	The `--server-public-key-path` option was added in MySQL 5.7.23.
- ``--set-charset=*`charset_name`*``
	| Command-Line Format | `--set-charset=charset_name` |
	| --- | --- |
	| Type | String |
	Add a [``SET NAMES             *`charset_name`*``](set-names.md) statement to the output to specify the character set to be used for processing log files.
- ``--shared-memory-base-name=*`name`*``
	| Command-Line Format | `--shared-memory-base-name=name` |
	| --- | --- |
	| Platform Specific | Windows |
	On Windows, the shared-memory name to use for connections made using shared memory to a local server. The default value is `MYSQL`. The shared-memory name is case-sensitive.
	This option applies only if the server was started with the [`shared_memory`](server-system-variables.md) system variable enabled to support shared-memory connections.
- `--short-form`, `-s`
	| Command-Line Format | `--short-form` |
	| --- | --- |
	Display only the statements contained in the log, without any extra information or row-based events. This is for testing only, and should not be used in production systems.
- [`--skip-gtids[=(true|false)]`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/mysqlbinlog.html#option_mysqlbinlog_skip-gtids)
	| Command-Line Format | `--skip-gtids[=true\|false]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `false` |
	Do not include the GTIDs from the binary log files in the output dump file. For example:
	```
	mysqlbinlog --skip-gtids binlog.000001 >  /tmp/dump.sql
	mysql -u root -p -e "source /tmp/dump.sql"
	```
	You should not normally use this option in production or in recovery, except in the specific, and rare, scenarios where the GTIDs are actively unwanted. For example, an administrator might want to duplicate selected transactions (such as table definitions) from a deployment to another, unrelated, deployment that will not replicate to or from the original. In that scenario, `--skip-gtids` can be used to enable the administrator to apply the transactions as if they were new, and ensure that the deployments remain unrelated. However, you should only use this option if the inclusion of the GTIDs causes a known issue for your use case.
- ``--socket=*`path`*``, ``-S *`path`*``
	| Command-Line Format | `--socket={file_name\|pipe_name}` |
	| --- | --- |
	| Type | String |
	For connections to `localhost`, the Unix socket file to use, or, on Windows, the name of the named pipe to use.
	On Windows, this option applies only if the server was started with the [`named_pipe`](server-system-variables.md) system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the [`named_pipe_full_access_group`](server-system-variables.md) system variable.
- `--ssl*`
	Options that begin with `--ssl` specify whether to connect to the server using encryption and indicate where to find SSL keys and certificates. See [Command Options for Encrypted Connections](connection-options.md).
- ``--start-datetime=*`datetime`*``
	| Command-Line Format | `--start-datetime=datetime` |
	| --- | --- |
	| Type | Datetime |
	Start reading the binary log at the first event having a timestamp equal to or later than the *`datetime`* argument. The *`datetime`* value is relative to the local time zone on the machine where you run **mysqlbinlog**. The value should be in a format accepted for the [`DATETIME`](datetime.md) or [`TIMESTAMP`](datetime.md) data types. For example:
	```
	mysqlbinlog --start-datetime="2005-12-25 11:25:56" binlog.000003
	```
	This option is useful for point-in-time recovery. See [Section 7.5, “Point-in-Time (Incremental) Recovery”](point-in-time-recovery.md).
- ``--start-position=*`N`*``, ``-j *`N`*``
	| Command-Line Format | `--start-position=#` |
	| --- | --- |
	| Type | Numeric |
	Start reading the binary log at the first event having a position equal to or greater than *`N`*. This option applies to the first log file named on the command line.
	This option is useful for point-in-time recovery. See [Section 7.5, “Point-in-Time (Incremental) Recovery”](point-in-time-recovery.md).
- ``--stop-datetime=*`datetime`*``
	| Command-Line Format | `--stop-datetime=datetime` |
	| --- | --- |
	Stop reading the binary log at the first event having a timestamp equal to or later than the *`datetime`* argument. See the description of the `--start-datetime` option for information about the *`datetime`* value.
	This option is useful for point-in-time recovery. See [Section 7.5, “Point-in-Time (Incremental) Recovery”](point-in-time-recovery.md).
- `--stop-never`
	| Command-Line Format | `--stop-never` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	This option is used with `--read-from-remote-server`. It tells **mysqlbinlog** to remain connected to the server. Otherwise **mysqlbinlog** exits when the last log file has been transferred from the server. `--stop-never` implies `--to-last-log`, so only the first log file to transfer need be named on the command line.
	`--stop-never` is commonly used with `--raw` to make a live binary log backup, but also can be used without `--raw` to maintain a continuous text display of log events as the server generates them.
- ``--stop-never-slave-server-id=*`id`*``
	| Command-Line Format | `--stop-never-slave-server-id=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `65535` |
	| Minimum Value | `1` |
	With `--stop-never`, **mysqlbinlog** reports a server ID of 65535 when it connects to the server. `--stop-never-slave-server-id` explicitly specifies the server ID to report. It can be used to avoid a conflict with the ID of a replica server or another **mysqlbinlog** process. See [Section 4.6.7.4, “Specifying the mysqlbinlog Server ID”](mysqlbinlog-server-id.md).
- ``--stop-position=*`N`*``
	| Command-Line Format | `--stop-position=#` |
	| --- | --- |
	| Type | Numeric |
	Stop reading the binary log at the first event having a position equal to or greater than *`N`*. This option applies to the last log file named on the command line.
	This option is useful for point-in-time recovery. See [Section 7.5, “Point-in-Time (Incremental) Recovery”](point-in-time-recovery.md).
- ``--tls-version=*`protocol_list`*``
	| Command-Line Format | `--tls-version=protocol_list` |
	| --- | --- |
	| Type | String |
	| Default Value | `TLSv1,TLSv1.1,TLSv1.2` |
	The permissible TLS protocols for encrypted connections. The value is a list of one or more comma-separated protocol names. The protocols that can be named for this option depend on the SSL library used to compile MySQL. For details, see [Section 6.3.2, “Encrypted Connection TLS Protocols and Ciphers”](encrypted-connection-protocols-ciphers.md).
	This option was added in MySQL 5.7.10.
- `--to-last-log`, `-t`
	| Command-Line Format | `--to-last-log` |
	| --- | --- |
	Do not stop at the end of the requested binary log from a MySQL server, but rather continue printing until the end of the last binary log. If you send the output to the same MySQL server, this may lead to an endless loop. This option requires `--read-from-remote-server`.
- ``--user=*`user_name`*``, ``-u *`user_name`*``
	| Command-Line Format | `--user=user_name,` |
	| --- | --- |
	| Type | String |
	The user name of the MySQL account to use when connecting to a remote server.
- `--verbose`, `-v`
	| Command-Line Format | `--verbose` |
	| --- | --- |
	Reconstruct row events and display them as commented SQL statements. If this option is given twice (by passing in either "-vv" or "--verbose --verbose"), the output includes comments to indicate column data types and some metadata, and row query log events if so configured.
	For examples that show the effect of `--base64-output` and `--verbose` on row event output, see [Section 4.6.7.2, “mysqlbinlog Row Event Display”](mysqlbinlog-row-events.md).
- `--verify-binlog-checksum`, `-c`
	| Command-Line Format | `--verify-binlog-checksum` |
	| --- | --- |
	Verify checksums in binary log files.
- `--version`, `-V`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.
	In MySQL 5.7, the version number shown by **mysqlbinlog** when using this option is 3.4.

You can pipe the output of **mysqlbinlog** into the [**mysql**](mysql.md) client to execute the events contained in the binary log. This technique is used to recover from an unexpected exit when you have an old backup (see [Section 7.5, “Point-in-Time (Incremental) Recovery”](point-in-time-recovery.md)). For example:

```
mysqlbinlog binlog.000001 | mysql -u root -p
```

Or:

```
mysqlbinlog binlog.[0-9]* | mysql -u root -p
```

If the statements produced by **mysqlbinlog** may contain [`BLOB`](blob.md) values, these may cause problems when [**mysql**](mysql.md) processes them. In this case, invoke [**mysql**](mysql.md) with the [`--binary-mode`](mysql-command-options.md) option.

You can also redirect the output of **mysqlbinlog** to a text file instead, if you need to modify the statement log first (for example, to remove statements that you do not want to execute for some reason). After editing the file, execute the statements that it contains by using it as input to the [**mysql**](mysql.md) program:

```
mysqlbinlog binlog.000001 > tmpfile
... edit tmpfile ...
mysql -u root -p < tmpfile
```

When **mysqlbinlog** is invoked with the `--start-position` option, it displays only those events with an offset in the binary log greater than or equal to a given position (the given position must match the start of one event). It also has options to stop and start when it sees an event with a given date and time. This enables you to perform point-in-time recovery using the `--stop-datetime` option (to be able to say, for example, “roll forward my databases to how they were today at 10:30 a.m.”).

**Processing multiple files.** If you have more than one binary log to execute on the MySQL server, the safe method is to process them all using a single connection to the server. Here is an example that demonstrates what may be *unsafe*:

```
mysqlbinlog binlog.000001 | mysql -u root -p # DANGER!!
mysqlbinlog binlog.000002 | mysql -u root -p # DANGER!!
```

Processing binary logs this way using multiple connections to the server causes problems if the first log file contains a [`CREATE TEMPORARY         TABLE`](create-table.md) statement and the second log contains a statement that uses the temporary table. When the first [**mysql**](mysql.md) process terminates, the server drops the temporary table. When the second [**mysql**](mysql.md) process attempts to use the table, the server reports “unknown table.”

To avoid problems like this, use a *single* [**mysql**](mysql.md) process to execute the contents of all binary logs that you want to process. Here is one way to do so:

```
mysqlbinlog binlog.000001 binlog.000002 | mysql -u root -p
```

Another approach is to write all the logs to a single file and then process the file:

```
mysqlbinlog binlog.000001 >  /tmp/statements.sql
mysqlbinlog binlog.000002 >> /tmp/statements.sql
mysql -u root -p -e "source /tmp/statements.sql"
```

**mysqlbinlog** can produce output that reproduces a [`LOAD DATA`](load-data.md) operation without the original data file. **mysqlbinlog** copies the data to a temporary file and writes a [`LOAD DATA         LOCAL`](load-data.md) statement that refers to the file. The default location of the directory where these files are written is system-specific. To specify a directory explicitly, use the `--local-load` option.

Because **mysqlbinlog** converts [`LOAD DATA`](load-data.md) statements to [`LOAD DATA         LOCAL`](load-data.md) statements (that is, it adds `LOCAL`), both the client and the server that you use to process the statements must be configured with the `LOCAL` capability enabled. See [Section 6.1.6, “Security Considerations for LOAD DATA LOCAL”](load-data-local-security.md).

Warning

The temporary files created for [`LOAD DATA           LOCAL`](load-data.md) statements are *not* automatically deleted because they are needed until you actually execute those statements. You should delete the temporary files yourself after you no longer need the statement log. The files can be found in the temporary file directory and have names like *`original_file_name-#-#`*.