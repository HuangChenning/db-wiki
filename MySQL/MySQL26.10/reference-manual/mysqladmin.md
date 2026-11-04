---
title: "MySQL :: MySQL 26.10 Reference Manual :: 6.5.2 mysqladmin — A MySQL Server Administration Program"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/mysqladmin.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 6.5.2 mysqladmin — A MySQL Server Administration Program

**mysqladmin** is a client for performing administrative operations. You can use it to check the server's configuration and current status, to create and drop databases, and more.

Invoke **mysqladmin** like this:

```svg
mysqladmin [options] command [command-arg] [command [command-arg]] ...
```

**mysqladmin** supports the following commands. Some of the commands take an argument following the command name.

- ``create *`db_name`*``
	Create a new database named *`db_name`*.
- `debug`
	Tells the server to write debug information to the error log. The connected user must have the [`SUPER`](privileges-provided.md) privilege. Format and content of this information is subject to change.
	This includes information about the Event Scheduler. See [Section 27.5.5, “Event Scheduler Status”](events-status-info.md).
- ``drop *`db_name`*``
	Delete the database named *`db_name`* and all its tables.
- `extended-status`
	Display the server status variables and their values.
- `flush-hosts`
	Flush all information in the host cache. See [Section 7.1.12.3, “DNS Lookups and the Host Cache”](host-cache.md).
- ``flush-logs [*`log_type`*             ...]``
	Flush all logs.
	The **mysqladmin flush-logs** command permits optional log types to be given, to specify which logs to flush. Following the `flush-logs` command, you can provide a space-separated list of one or more of the following log types: `binary`, `engine`, `error`, `general`, `relay`, `slow`. These correspond to the log types that can be specified for the [`FLUSH             LOGS`](flush.md) SQL statement.
- `flush-privileges`
	Reload the grant tables (same as `reload`).
	Deprecated, and raises a warning; you should expect this command to be removed in a future version of MySQL.
- `flush-status`
	Clear status variables.
- `flush-tables`
	Flush all tables.
- ``kill             *`id`*,*`id`*,...``
	Kill server threads. If multiple thread ID values are given, there must be no spaces in the list.
	To kill threads belonging to other users, the connected user must have the [`CONNECTION_ADMIN`](privileges-provided.md) privilege (or the deprecated [`SUPER`](privileges-provided.md) privilege).
- ``password             *`new_password`*``
	Set a new password. This changes the password to *`new_password`* for the account that you use with **mysqladmin** for connecting to the server. Thus, the next time you invoke **mysqladmin** (or any other client program) using the same account, you must specify the new password.
	Warning
	Setting a password using **mysqladmin** should be considered *insecure*. On some systems, your password becomes visible to system status programs such as **ps** that may be invoked by other users to display command lines. MySQL clients typically overwrite the command-line password argument with zeros during their initialization sequence. However, there is still a brief interval during which the value is visible. Also, on some systems this overwriting strategy is ineffective and the password remains visible to **ps**. (SystemV Unix systems and perhaps others are subject to this problem.)
	If the *`new_password`* value contains spaces or other characters that are special to your command interpreter, you need to enclose it within quotation marks. On Windows, be sure to use double quotation marks rather than single quotation marks; single quotation marks are not stripped from the password, but rather are interpreted as part of the password. For example:
	```svg
	mysqladmin password "my new password"
	```
	The new password can be omitted following the `password` command. In this case, **mysqladmin** prompts for the password value, which enables you to avoid specifying the password on the command line. Omitting the password value should be done only if `password` is the final command on the **mysqladmin** command line. Otherwise, the next argument is taken as the password.
	Caution
	Do not use this command used if the server was started with the [`--skip-grant-tables`](server-options.md) option. No password change is applied. This is true even if you precede the `password` command with `flush-privileges` on the same command line to re-enable the grant tables because the flush operation occurs after you connect. However, you can use **mysqladmin flush-privileges** to re-enable the grant tables and then use a separate **mysqladmin password** command to change the password.
- `ping`
	Check whether the server is available. The return status from **mysqladmin** is 0 if the server is running, 1 if it is not. This is 0 even in case of an error such as `Access denied`, because this means that the server is running but refused the connection, which is different from the server not running.
- `processlist`
	Show a list of active server threads. This is like the output of the [`SHOW             PROCESSLIST`](show-processlist.md) statement. If the `--verbose` option is given, the output is like that of [`SHOW FULL             PROCESSLIST`](show-processlist.md). (See [Section 15.7.7.33, “SHOW PROCESSLIST Statement”](show-processlist.md).)
- `reload`
	Reload the grant tables.
	Deprecated, and raises a warning; you should expect this command to be removed in a future version of MySQL.
- `refresh`
	Flush all tables and close and open log files.
	Flushing of privileges by this command is deprecated; you should expect this behavior to be removed in a future version of MySQL.
- `shutdown`
	Stop the server.
- `start-replica`
	Start replication on a replica server.
- `start-slave`
	This is a deprecated alias for start-replica.
- `status`
	Display a short server status message.
- `stop-replica`
	Stop replication on a replica server.
- `stop-slave`
	This is a deprecated alias for stop-replica.
- `variables`
	Display the server system variables and their values.
- `version`
	Display version information from the server.

All commands can be shortened to any unique prefix. For example:

```svg
$> mysqladmin proc stat
+----+-------+-----------+----+---------+------+-------+------------------+
| Id | User  | Host      | db | Command | Time | State | Info             |
+----+-------+-----------+----+---------+------+-------+------------------+
| 51 | jones | localhost |    | Query   | 0    |       | show processlist |
+----+-------+-----------+----+---------+------+-------+------------------+
Uptime: 1473624  Threads: 1  Questions: 39487
Slow queries: 0  Opens: 541  Flush tables: 1
Open tables: 19  Queries per second avg: 0.0268
```

The **mysqladmin status** command result displays the following values:

- [`Uptime`](server-status-variables.md)
	The number of seconds the MySQL server has been running.
- `Threads`
	The number of active threads (clients).
- [`Questions`](server-status-variables.md)
	The number of questions (queries) from clients since the server was started.
- `Slow queries`
	The number of queries that have taken more than [`long_query_time`](server-system-variables.md) seconds. See [Section 7.4.5, “The Slow Query Log”](slow-query-log.md).
- `Opens`
	The number of tables the server has opened.
- `Flush tables`
	The number of `flush-*`, `refresh`, and `reload` commands the server has executed.
- `Open tables`
	The number of tables that currently are open.

If you execute **mysqladmin shutdown** when connecting to a local server using a Unix socket file, **mysqladmin** waits until the server's process ID file has been removed, to ensure that the server has stopped properly.

**mysqladmin** supports the following options, which can be specified on the command line or in the `[mysqladmin]` and `[client]` groups of an option file. For information about option files used by MySQL programs, see [Section 6.2.2.2, “Using Option Files”](option-files.md).

**Table 6.11 mysqladmin Options**

| Option Name | Description |
| --- | --- |
| \--bind-address | Use specified network interface to connect to MySQL Server |
| \--character-sets-dir | Directory where character sets can be found |
| \--compress | Compress all information sent between client and server |
| \--compression-algorithms | Permitted compression algorithms for connections to server |
| \--connect-timeout | Number of seconds before connection timeout |
| \--count | Number of iterations to make for repeated command execution |
| \--debug | Write debugging log |
| \--debug-check | Print debugging information when program exits |
| \--debug-info | Print debugging information, memory, and CPU statistics when program exits |
| \--default-auth | Authentication plugin to use |
| \--default-character-set | Specify default character set |
| \--defaults-extra-file | Read named option file in addition to usual option files |
| \--defaults-file | Read only named option file |
| \--defaults-group-suffix | Option group suffix value |
| \--enable-cleartext-plugin | Enable cleartext authentication plugin |
| \--force | Continue even if an SQL error occurs |
| \--get-server-public-key | Request RSA public key from server |
| \--help | Display help message and exit |
| \--host | Host on which MySQL server is located |
| \--login-path | Read login path options from.mylogin.cnf |
| \--no-beep | Do not beep when errors occur |
| \--no-defaults | Read no option files |
| \--no-login-paths | Do not read login paths from the login path file |
| \--password | Password to use when connecting to server |
| \--password1 | First multifactor authentication password to use when connecting to server |
| \--password2 | Second multifactor authentication password to use when connecting to server |
| \--password3 | Third multifactor authentication password to use when connecting to server |
| \--pipe | Connect to server using named pipe (Windows only) |
| \--plugin-dir | Directory where plugins are installed |
| \--port | TCP/IP port number for connection |
| \--print-defaults | Print default options |
| \--protocol | Transport protocol to use |
| \--relative | Show the difference between the current and previous values when used with the --sleep option |
| \--server-public-key-path | Path name to file containing RSA public key |
| \--shared-memory-base-name | Shared-memory name for shared-memory connections (Windows only) |
| \--show-warnings | Show warnings after statement execution |
| \--shutdown-timeout | The maximum number of seconds to wait for server shutdown |
| \--silent | Silent mode |
| \--sleep | Execute commands repeatedly, sleeping for delay seconds in between |
| \--socket | Unix socket file or Windows named pipe to use |
| \--ssl-ca | File that contains list of trusted SSL Certificate Authorities |
| \--ssl-capath | Directory that contains trusted SSL Certificate Authority certificate files |
| \--ssl-cert | File that contains X.509 certificate |
| \--ssl-cipher | Permissible ciphers for connection encryption |
| \--ssl-fips-mode | Whether to enable FIPS mode on client side |
| \--ssl-key | File that contains X.509 key |
| \--ssl-mode | Desired security state of connection to server |
| \--ssl-session-data | File that contains SSL session data |
| \--ssl-session-data-continue-on-failed-reuse | Whether to establish connections if session reuse fails |
| \--tls-ciphersuites | Permissible TLSv1.3 ciphersuites for encrypted connections |
| \--tls-sni-servername | Server name supplied by the client |
| \--tls-version | Permissible TLS protocols for encrypted connections |
| \--user | MySQL user name to use when connecting to server |
| \--verbose | Verbose mode |
| \--version | Display version information and exit |
| \--vertical | Print query output rows vertically (one line per column value) |
| \--wait | If the connection cannot be established, wait and retry instead of aborting |
| \--zstd-compression-level | Compression level for connections to server that use zstd compression |

- `--help`, `-?`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display a help message and exit.
- ``--bind-address=*`ip_address`*``
	| Command-Line Format | `--bind-address=ip_address` |
	| --- | --- |
	On a computer having multiple network interfaces, use this option to select which interface to use for connecting to the MySQL server.
- ``--character-sets-dir=*`dir_name`*``
	| Command-Line Format | `--character-sets-dir=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	The directory where character sets are installed. See [Section 12.15, “Character Set Configuration”](charset-configuration.md).
- `--compress`, `-C`
	| Command-Line Format | `--compress[={OFF\|ON}]` |
	| --- | --- |
	| Deprecated | Yes |
	| Type | Boolean |
	| Default Value | `OFF` |
	Compress all information sent between the client and the server if possible. See [Section 6.2.8, “Connection Compression Control”](connection-compression-control.md).
	This option is deprecated. Expect it to be removed in a future version of MySQL. See [Configuring Legacy Connection Compression](connection-compression-control.md).
- ``--compression-algorithms=*`value`*``
	| Command-Line Format | `--compression-algorithms=value` |
	| --- | --- |
	| Type | Set |
	| Default Value | `uncompressed` |
	| Valid Values | `zlib`  `zstd`  `uncompressed` |
	The permitted compression algorithms for connections to the server. The available algorithms are the same as for the [`protocol_compression_algorithms`](server-system-variables.md) system variable. The default value is `uncompressed`.
	For more information, see [Section 6.2.8, “Connection Compression Control”](connection-compression-control.md).
- ``--connect-timeout=*`value`*``
	| Command-Line Format | `--connect-timeout=value` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `43200` |
	The maximum number of seconds before connection timeout. The default value is 43200 (12 hours).
- ``--count=*`N`*``, ``-c *`N`*``
	| Command-Line Format | `--count=#` |
	| --- | --- |
	The number of iterations to make for repeated command execution if the `--sleep` option is given.
- [``--debug[=*`debug_options`*]``](https://dev.mysql.com/doc/refman/26.10/en/mysqladmin.html#option_mysqladmin_debug), ``-#             [*`debug_options`*]``
	| Command-Line Format | `--debug[=debug_options]` |
	| --- | --- |
	| Type | String |
	| Default Value | `d:t:o,/tmp/mysqladmin.trace` |
	Write a debugging log. A typical *`debug_options`* string is ``d:t:o,*`file_name`*``. The default is `d:t:o,/tmp/mysqladmin.trace`.
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
	A hint about which client-side authentication plugin to use. See [Section 8.2.17, “Pluggable Authentication”](pluggable-authentication.md).
- ``--default-character-set=*`charset_name`*``
	| Command-Line Format | `--default-character-set=charset_name` |
	| --- | --- |
	| Type | String |
	Use *`charset_name`* as the default character set. See [Section 12.15, “Character Set Configuration”](charset-configuration.md).
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
	Read not only the usual option groups, but also groups with the usual names and a suffix of *`str`*. For example, **mysqladmin** normally reads the `[client]` and `[mysqladmin]` groups. If this option is given as `--defaults-group-suffix=_other`, **mysqladmin** also reads the `[client_other]` and `[mysqladmin_other]` groups.
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--enable-cleartext-plugin`
	| Command-Line Format | `--enable-cleartext-plugin` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Enable the `mysql_clear_password` cleartext authentication plugin. (See [Section 8.4.1.3, “Client-Side Cleartext Pluggable Authentication”](cleartext-pluggable-authentication.md).)
- `--force`, `-f`
	| Command-Line Format | `--force` |
	| --- | --- |
	Do not ask for confirmation for the ``drop             *`db_name`*`` command. With multiple commands, continue even if an error occurs.
- `--get-server-public-key`
	| Command-Line Format | `--get-server-public-key` |
	| --- | --- |
	| Type | Boolean |
	Request from the server the public key required for RSA key pair-based password exchange. This option applies to clients that authenticate with the `caching_sha2_password` authentication plugin. For that plugin, the server does not send the public key unless requested. This option is ignored for accounts that do not authenticate with that plugin. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection.
	If ``--server-public-key-path=*`file_name`*`` is given and specifies a valid public key file, it takes precedence over `--get-server-public-key`.
	For information about the `caching_sha2_password` plugin, see [Section 8.4.1.1, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).
- ``--host=*`host_name`*``, ``-h *`host_name`*``
	| Command-Line Format | `--host=host_name` |
	| --- | --- |
	| Type | String |
	| Default Value | `localhost` |
	Connect to the MySQL server on the given host.
- ``--login-path=*`name`*``
	| Command-Line Format | `--login-path=name` |
	| --- | --- |
	| Type | String |
	Read options from the named login path in the `.mylogin.cnf` login path file. A “login path” is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 6.6.7, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--no-login-paths`
	| Command-Line Format | `--no-login-paths` |
	| --- | --- |
	Skips reading options from the login path file.
	See `--login-path` for related information.
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--no-beep`, `-b`
	| Command-Line Format | `--no-beep` |
	| --- | --- |
	Suppress the warning beep that is emitted by default for errors such as a failure to connect to the server.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read any option files. If program startup fails due to reading unknown options from an option file, `--no-defaults` can be used to prevent them from being read.
	The exception is that the `.mylogin.cnf` file is read in all cases, if it exists. This permits passwords to be specified in a safer way than on the command line even when `--no-defaults` is used. To create `.mylogin.cnf`, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 6.6.7, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- [``--password[=*`password`*]``](https://dev.mysql.com/doc/refman/26.10/en/mysqladmin.html#option_mysqladmin_password), ``-p[*`password`*]``
	| Command-Line Format | `--password[=password]` |
	| --- | --- |
	| Type | String |
	The password of the MySQL account used for connecting to the server. The password value is optional. If not given, **mysqladmin** prompts for one. If given, there must be *no space* between `--password=` or `-p` and the password following it. If no password option is specified, the default is to send no password.
	Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See [Section 8.1.2.1, “End-User Guidelines for Password Security”](password-security-user.md).
	To explicitly specify that there is no password and that **mysqladmin** should not prompt for one, use the `--skip-password` option.
- [``--password1[=*`pass_val`*]``](https://dev.mysql.com/doc/refman/26.10/en/mysqladmin.html#option_mysqladmin_password1)
	The password for multifactor authentication factor 1 of the MySQL account used for connecting to the server. The password value is optional. If not given, [**mysql**](mysql.md) prompts for one. If given, there must be *no space* between `--password1=` and the password following it. If no password option is specified, the default is to send no password.
	Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See [Section 8.1.2.1, “End-User Guidelines for Password Security”](password-security-user.md).
	To explicitly specify that there is no password and that **mysqladmin** should not prompt for one, use the `--skip-password1` option.
	`--password1` and `--password` are synonymous, as are [`--skip-password1`](mysql-command-options.md) and [`--skip-password`](mysql-command-options.md).
- [``--password2[=*`pass_val`*]``](https://dev.mysql.com/doc/refman/26.10/en/mysqladmin.html#option_mysqladmin_password2)
	The password for multifactor authentication factor 2 of the MySQL account used for connecting to the server. The semantics of this option are similar to the semantics for `--password1`; see the description of that option for details.
- [``--password3[=*`pass_val`*]``](https://dev.mysql.com/doc/refman/26.10/en/mysqladmin.html#option_mysqladmin_password3)
	The password for multifactor authentication factor 3 of the MySQL account used for connecting to the server. The semantics of this option are similar to the semantics for `--password1`; see the description of that option for details.
- `--pipe`, `-W`
	| Command-Line Format | `--pipe` |
	| --- | --- |
	| Type | String |
	On Windows, connect to the server using a named pipe. This option applies only if the server was started with the [`named_pipe`](server-system-variables.md) system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the [`named_pipe_full_access_group`](server-system-variables.md) system variable.
- ``--plugin-dir=*`dir_name`*``
	| Command-Line Format | `--plugin-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The directory in which to look for plugins. Specify this option if the `--default-auth` option is used to specify an authentication plugin but **mysqladmin** does not find it. See [Section 8.2.17, “Pluggable Authentication”](pluggable-authentication.md).
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
- `--relative`, `-r`
	| Command-Line Format | `--relative` |
	| --- | --- |
	Show the difference between the current and previous values when used with the `--sleep` option. This option works only with the `extended-status` command.
- ``--server-public-key-path=*`file_name`*``
	| Command-Line Format | `--server-public-key-path=file_name` |
	| --- | --- |
	| Type | File name |
	The path name to a file in PEM format containing a client-side copy of the public key required by the server for RSA key pair-based password exchange. This option applies to clients that authenticate with the `sha256_password` or `caching_sha2_password` authentication plugin. This option is ignored for accounts that do not authenticate with one of those plugins. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection.
	If ``--server-public-key-path=*`file_name`*`` is given and specifies a valid public key file, it takes precedence over `--get-server-public-key`.
	For `sha256_password`, this option applies only if MySQL was built using OpenSSL.
	For information about the `sha256_password` and `caching_sha2_password` plugins, see [Section 8.4.1.2, “SHA-256 Pluggable Authentication”](sha256-pluggable-authentication.md), and [Section 8.4.1.1, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).
- ``--shared-memory-base-name=*`name`*``
	| Command-Line Format | `--shared-memory-base-name=name` |
	| --- | --- |
	| Platform Specific | Windows |
	On Windows, the shared-memory name to use for connections made using shared memory to a local server. The default value is `MYSQL`. The shared-memory name is case-sensitive.
	This option applies only if the server was started with the [`shared_memory`](server-system-variables.md) system variable enabled to support shared-memory connections.
- `--show-warnings`
	| Command-Line Format | `--show-warnings` |
	| --- | --- |
	Show warnings resulting from execution of statements sent to the server.
- ``--shutdown-timeout=*`value`*``
	| Command-Line Format | `--shutdown-timeout=seconds` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `3600` |
	The maximum number of seconds to wait for server shutdown. The default value is 3600 (1 hour).
- `--silent`, `-s`
	| Command-Line Format | `--silent` |
	| --- | --- |
	Exit silently if a connection to the server cannot be established.
- ``--sleep=*`delay`*``, ``-i *`delay`*``
	| Command-Line Format | `--sleep=delay` |
	| --- | --- |
	Execute commands repeatedly, sleeping for *`delay`* seconds in between. The `--count` option determines the number of iterations. If `--count` is not given, **mysqladmin** executes commands indefinitely until interrupted.
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
	This option is deprecated. Expect it to be removed in a future version of MySQL.
- ``--tls-ciphersuites=*`ciphersuite_list`*``
	| Command-Line Format | `--tls-ciphersuites=ciphersuite_list` |
	| --- | --- |
	| Type | String |
	The permissible ciphersuites for encrypted connections that use TLSv1.3. The value is a list of one or more colon-separated ciphersuite names. The ciphersuites that can be named for this option depend on the SSL library used to compile MySQL. For details, see [Section 8.3.2, “Encrypted Connection TLS Protocols and Ciphers”](encrypted-connection-protocols-ciphers.md).
- ``--tls-sni-servername=*`server_name`*``
	| Command-Line Format | `--tls-sni-servername=server_name` |
	| --- | --- |
	| Type | String |
	When specified, the name is passed to the `libmysqlclient` C API library using the `MYSQL_OPT_TLS_SNI_SERVERNAME` option of [`mysql_options()`](https://dev.mysql.com/doc/c-api/26.10/en/mysql-options.html). The server name is not case-sensitive. To show which server name the client specified for the current session, if any, check the [`Tls_sni_server_name`](server-status-variables.md) status variable.
	Server Name Indication (SNI) is an extension to the TLS protocol (OpenSSL must be compiled using TLS extensions for this option to function). The MySQL implementation of SNI represents the client-side only.
- ``--tls-version=*`protocol_list`*``
	| Command-Line Format | `--tls-version=protocol_list` |
	| --- | --- |
	| Type | String |
	| Default Value | `TLSv1,TLSv1.1,TLSv1.2,TLSv1.3` (OpenSSL 1.1.1 or higher)  `TLSv1,TLSv1.1,TLSv1.2` (otherwise) |
	The permissible TLS protocols for encrypted connections. The value is a list of one or more comma-separated protocol names. The protocols that can be named for this option depend on the SSL library used to compile MySQL. For details, see [Section 8.3.2, “Encrypted Connection TLS Protocols and Ciphers”](encrypted-connection-protocols-ciphers.md).
- ``--user=*`user_name`*``, ``-u *`user_name`*``
	| Command-Line Format | `--user=user_name,` |
	| --- | --- |
	| Type | String |
	The user name of the MySQL account to use for connecting to the server.
	If you are using the `Rewriter` plugin, grant this user the [`SKIP_QUERY_REWRITE`](privileges-provided.md) privilege.
- `--verbose`, `-v`
	| Command-Line Format | `--verbose` |
	| --- | --- |
	Verbose mode. Print more information about what the program does.
- `--version`, `-V`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.
- `--vertical`, `-E`
	| Command-Line Format | `--vertical` |
	| --- | --- |
	Print output vertically. This is similar to `--relative`, but prints output vertically.
- [``--wait[=*`count`*]``](https://dev.mysql.com/doc/refman/26.10/en/mysqladmin.html#option_mysqladmin_wait), ``-w[*`count`*]``
	| Command-Line Format | `--wait` |
	| --- | --- |
	If the connection cannot be established, wait and retry instead of aborting. If a *`count`* value is given, it indicates the number of times to retry. The default is one time.
- ``--zstd-compression-level=*`level`*``
	| Command-Line Format | `--zstd-compression-level=#` |
	| --- | --- |
	| Type | Integer |
	The compression level to use for connections to the server that use the `zstd` compression algorithm. The permitted levels are from 1 to 22, with larger values indicating increasing levels of compression. The default `zstd` compression level is 3. The compression level setting has no effect on connections that do not use `zstd` compression.
	For more information, see [Section 6.2.8, “Connection Compression Control”](connection-compression-control.md).