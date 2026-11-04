---
title: "4.5.5 mysqlimport — A Data Import Program"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysqlimport.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 4.5.5 mysqlimport — A Data Import Program

The **mysqlimport** client provides a command-line interface to the [`LOAD         DATA`](load-data.md) SQL statement. Most options to **mysqlimport** correspond directly to clauses of [`LOAD DATA`](load-data.md) syntax. See [Section 13.2.6, “LOAD DATA Statement”](load-data.md).

Invoke **mysqlimport** like this:

```
mysqlimport [options] db_name textfile1 [textfile2 ...]
```

For each text file named on the command line, **mysqlimport** strips any extension from the file name and uses the result to determine the name of the table into which to import the file's contents. For example, files named `patient.txt`, `patient.text`, and `patient` all would be imported into a table named `patient`.

**mysqlimport** supports the following options, which can be specified on the command line or in the `[mysqlimport]` and `[client]` groups of an option file. For information about option files used by MySQL programs, see [Section 4.2.2.2, “Using Option Files”](option-files.md).

**Table 4.17 mysqlimport Options**

| Option Name | Description | Deprecated |
| --- | --- | --- |
| \--bind-address | Use specified network interface to connect to MySQL Server |  |
| \--character-sets-dir | Directory where character sets can be found |  |
| \--columns | This option takes a comma-separated list of column names as its value |  |
| \--compress | Compress all information sent between client and server |  |
| \--debug | Write debugging log |  |
| \--debug-check | Print debugging information when program exits |  |
| \--debug-info | Print debugging information, memory, and CPU statistics when program exits |  |
| \--default-auth | Authentication plugin to use |  |
| \--default-character-set | Specify default character set |  |
| \--defaults-extra-file | Read named option file in addition to usual option files |  |
| \--defaults-file | Read only named option file |  |
| \--defaults-group-suffix | Option group suffix value |  |
| \--delete | Empty the table before importing the text file |  |
| \--enable-cleartext-plugin | Enable cleartext authentication plugin |  |
| \--fields-enclosed-by | This option has the same meaning as the corresponding clause for LOAD DATA |  |
| \--fields-escaped-by | This option has the same meaning as the corresponding clause for LOAD DATA |  |
| \--fields-optionally-enclosed-by | This option has the same meaning as the corresponding clause for LOAD DATA |  |
| \--fields-terminated-by | This option has the same meaning as the corresponding clause for LOAD DATA |  |
| \--force | Continue even if an SQL error occurs |  |
| \--get-server-public-key | Request RSA public key from server |  |
| \--help | Display help message and exit |  |
| \--host | Host on which MySQL server is located |  |
| \--ignore | See the description for the --replace option |  |
| \--ignore-lines | Ignore the first N lines of the data file |  |
| \--lines-terminated-by | This option has the same meaning as the corresponding clause for LOAD DATA |  |
| \--local | Read input files locally from the client host |  |
| \--lock-tables | Lock all tables for writing before processing any text files |  |
| \--login-path | Read login path options from.mylogin.cnf |  |
| \--low-priority | Use LOW\_PRIORITY when loading the table |  |
| \--no-defaults | Read no option files |  |
| \--password | Password to use when connecting to server |  |
| \--pipe | Connect to server using named pipe (Windows only) |  |
| \--plugin-dir | Directory where plugins are installed |  |
| \--port | TCP/IP port number for connection |  |
| \--print-defaults | Print default options |  |
| \--protocol | Transport protocol to use |  |
| \--replace | The --replace and --ignore options control handling of input rows that duplicate existing rows on unique key values |  |
| \--secure-auth | Do not send passwords to server in old (pre-4.1) format | Yes |
| \--server-public-key-path | Path name to file containing RSA public key |  |
| \--shared-memory-base-name | Shared-memory name for shared-memory connections (Windows only) |  |
| \--silent | Produce output only when errors occur |  |
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
| \--tls-version | Permissible TLS protocols for encrypted connections |  |
| \--use-threads | Number of threads for parallel file-loading |  |
| \--user | MySQL user name to use when connecting to server |  |
| \--verbose | Verbose mode |  |
| \--version | Display version information and exit |  |

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
	The directory where character sets are installed. See [Section 10.15, “Character Set Configuration”](charset-configuration.md).
- ``--columns=*`column_list`*``, ``-c *`column_list`*``
	| Command-Line Format | `--columns=column_list` |
	| --- | --- |
	This option takes a list of comma-separated column names as its value. The order of the column names indicates how to match data file columns with table columns.
- `--compress`, `-C`
	| Command-Line Format | `--compress[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	Compress all information sent between the client and the server if possible. See [Section 4.2.6, “Connection Compression Control”](connection-compression-control.md).
- [``--debug[=*`debug_options`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/mysqlimport.html#option_mysqlimport_debug), ``-#             [*`debug_options`*]``
	| Command-Line Format | `--debug[=debug_options]` |
	| --- | --- |
	| Type | String |
	| Default Value | `d:t:o` |
	Write a debugging log. A typical *`debug_options`* string is ``d:t:o,*`file_name`*``. The default is `d:t:o`.
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
- ``--default-character-set=*`charset_name`*``
	| Command-Line Format | `--default-character-set=charset_name` |
	| --- | --- |
	| Type | String |
	Use *`charset_name`* as the default character set. See [Section 10.15, “Character Set Configuration”](charset-configuration.md).
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
	Read not only the usual option groups, but also groups with the usual names and a suffix of *`str`*. For example, **mysqlimport** normally reads the `[client]` and `[mysqlimport]` groups. If this option is given as `--defaults-group-suffix=_other`, **mysqlimport** also reads the `[client_other]` and `[mysqlimport_other]` groups.
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--delete`, `-D`
	| Command-Line Format | `--delete` |
	| --- | --- |
	Empty the table before importing the text file.
- `--enable-cleartext-plugin`
	| Command-Line Format | `--enable-cleartext-plugin` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Enable the `mysql_clear_password` cleartext authentication plugin. (See [Section 6.4.1.6, “Client-Side Cleartext Pluggable Authentication”](cleartext-pluggable-authentication.md).)
	This option was added in MySQL 5.7.10.
- `--fields-terminated-by=...`, `--fields-enclosed-by=...`, `--fields-optionally-enclosed-by=...`, `--fields-escaped-by=...`
	| Command-Line Format | `--fields-terminated-by=string` |
	| --- | --- |
	| Type | String |
	| Command-Line Format | `--fields-enclosed-by=string` |
	| --- | --- |
	| Type | String |
	| Command-Line Format | `--fields-optionally-enclosed-by=string` |
	| --- | --- |
	| Type | String |
	| Command-Line Format | `--fields-escaped-by` |
	| --- | --- |
	| Type | String |
	These options have the same meaning as the corresponding clauses for [`LOAD DATA`](load-data.md). See [Section 13.2.6, “LOAD DATA Statement”](load-data.md).
- `--force`, `-f`
	| Command-Line Format | `--force` |
	| --- | --- |
	Ignore errors. For example, if a table for a text file does not exist, continue processing any remaining files. Without `--force`, **mysqlimport** exits if a table does not exist.
- `--get-server-public-key`
	| Command-Line Format | `--get-server-public-key` |
	| --- | --- |
	| Type | Boolean |
	Request from the server the public key required for RSA key pair-based password exchange. This option applies to clients that authenticate with the `caching_sha2_password` authentication plugin. For that plugin, the server does not send the public key unless requested. This option is ignored for accounts that do not authenticate with that plugin. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection.
	If ``--server-public-key-path=*`file_name`*`` is given and specifies a valid public key file, it takes precedence over `--get-server-public-key`.
	For information about the `caching_sha2_password` plugin, see [Section 6.4.1.4, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).
	The `--get-server-public-key` option was added in MySQL 5.7.23.
- ``--host=*`host_name`*``, ``-h *`host_name`*``
	| Command-Line Format | `--host=host_name` |
	| --- | --- |
	| Type | String |
	| Default Value | `localhost` |
	Import data to the MySQL server on the given host. The default host is `localhost`.
- `--ignore`, `-i`
	| Command-Line Format | `--ignore` |
	| --- | --- |
	See the description for the `--replace` option.
- ``--ignore-lines=*`N`*``
	| Command-Line Format | `--ignore-lines=#` |
	| --- | --- |
	| Type | Numeric |
	Ignore the first *`N`* lines of the data file.
- `--lines-terminated-by=...`
	| Command-Line Format | `--lines-terminated-by=string` |
	| --- | --- |
	| Type | String |
	This option has the same meaning as the corresponding clause for [`LOAD DATA`](load-data.md). For example, to import Windows files that have lines terminated with carriage return/linefeed pairs, use `--lines-terminated-by="\r\n"`. (You might have to double the backslashes, depending on the escaping conventions of your command interpreter.) See [Section 13.2.6, “LOAD DATA Statement”](load-data.md).
- `--local`, `-L`
	| Command-Line Format | `--local` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	By default, files are read by the server on the server host. With this option, **mysqlimport** reads input files locally on the client host.
	Successful use of `LOCAL` load operations within **mysqlimport** also requires that the server permits local loading; see [Section 6.1.6, “Security Considerations for LOAD DATA LOCAL”](load-data-local-security.md)
- [`--lock-tables`](mysqldump.md), `-l`
	| Command-Line Format | `--lock-tables` |
	| --- | --- |
	Lock *all* tables for writing before processing any text files. This ensures that all tables are synchronized on the server.
- ``--login-path=*`name`*``
	| Command-Line Format | `--login-path=name` |
	| --- | --- |
	| Type | String |
	Read options from the named login path in the `.mylogin.cnf` login path file. A “login path” is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 4.6.6, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--low-priority`
	| Command-Line Format | `--low-priority` |
	| --- | --- |
	Use `LOW_PRIORITY` when loading the table. This affects only storage engines that use only table-level locking (such as `MyISAM`, `MEMORY`, and `MERGE`).
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read any option files. If program startup fails due to reading unknown options from an option file, `--no-defaults` can be used to prevent them from being read.
	The exception is that the `.mylogin.cnf` file is read in all cases, if it exists. This permits passwords to be specified in a safer way than on the command line even when `--no-defaults` is used. To create `.mylogin.cnf`, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 4.6.6, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- [``--password[=*`password`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/mysqlimport.html#option_mysqlimport_password), ``-p[*`password`*]``
	| Command-Line Format | `--password[=password]` |
	| --- | --- |
	| Type | String |
	The password of the MySQL account used for connecting to the server. The password value is optional. If not given, **mysqlimport** prompts for one. If given, there must be *no space* between `--password=` or `-p` and the password following it. If no password option is specified, the default is to send no password.
	Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See [Section 6.1.2.1, “End-User Guidelines for Password Security”](password-security-user.md).
	To explicitly specify that there is no password and that **mysqlimport** should not prompt for one, use the `--skip-password` option.
- `--pipe`, `-W`
	| Command-Line Format | `--pipe` |
	| --- | --- |
	| Type | String |
	On Windows, connect to the server using a named pipe. This option applies only if the server was started with the [`named_pipe`](server-system-variables.md) system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the [`named_pipe_full_access_group`](server-system-variables.md) system variable.
- ``--plugin-dir=*`dir_name`*``
	| Command-Line Format | `--plugin-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The directory in which to look for plugins. Specify this option if the `--default-auth` option is used to specify an authentication plugin but **mysqlimport** does not find it. See [Section 6.2.13, “Pluggable Authentication”](pluggable-authentication.md).
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
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--protocol={TCP|SOCKET|PIPE|MEMORY}`
	| Command-Line Format | `--protocol=type` |
	| --- | --- |
	| Type | String |
	| Default Value | `[see text]` |
	| Valid Values | `TCP`  `SOCKET`  `PIPE`  `MEMORY` |
	The transport protocol to use for connecting to the server. It is useful when the other connection parameters normally result in use of a protocol other than the one you want. For details on the permissible values, see [Section 4.2.5, “Connection Transport Protocols”](transport-protocols.md).
- `--replace`, `-r`
	| Command-Line Format | `--replace` |
	| --- | --- |
	The `--replace` and `--ignore` options control handling of input rows that duplicate existing rows on unique key values. If you specify `--replace`, new rows replace existing rows that have the same unique key value. If you specify `--ignore`, input rows that duplicate an existing row on a unique key value are skipped. If you do not specify either option, an error occurs when a duplicate key value is found, and the rest of the text file is ignored.
- `--secure-auth`
	| Command-Line Format | `--secure-auth` |
	| --- | --- |
	| Deprecated | Yes |
	Do not send passwords to the server in old (pre-4.1) format. This prevents connections except for servers that use the newer password format.
	As of MySQL 5.7.5, this option is deprecated;expect it to be removed in a future MySQL release. It is always enabled and attempting to disable it (`--skip-secure-auth`, `--secure-auth=0`) produces an error. Before MySQL 5.7.5, this option is enabled by default but can be disabled.
	Note
	Passwords that use the pre-4.1 hashing method are less secure than passwords that use the native password hashing method and should be avoided. Pre-4.1 passwords are deprecated and support for them was removed in MySQL 5.7.5. For account upgrade instructions, see [Section 6.4.1.3, “Migrating Away from Pre-4.1 Password Hashing and the mysql\_old\_password Plugin”](account-upgrades.md).
- ``--server-public-key-path=*`file_name`*``
	| Command-Line Format | `--server-public-key-path=file_name` |
	| --- | --- |
	| Type | File name |
	The path name to a file in PEM format containing a client-side copy of the public key required by the server for RSA key pair-based password exchange. This option applies to clients that authenticate with the `sha256_password` or `caching_sha2_password` authentication plugin. This option is ignored for accounts that do not authenticate with one of those plugins. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection.
	If ``--server-public-key-path=*`file_name`*`` is given and specifies a valid public key file, it takes precedence over `--get-server-public-key`.
	For `sha256_password`, this option applies only if MySQL was built using OpenSSL.
	For information about the `sha256_password` and `caching_sha2_password` plugins, see [Section 6.4.1.5, “SHA-256 Pluggable Authentication”](sha256-pluggable-authentication.md), and [Section 6.4.1.4, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).
	The `--server-public-key-path` option was added in MySQL 5.7.23.
- ``--shared-memory-base-name=*`name`*``
	| Command-Line Format | `--shared-memory-base-name=name` |
	| --- | --- |
	| Platform Specific | Windows |
	On Windows, the shared-memory name to use for connections made using shared memory to a local server. The default value is `MYSQL`. The shared-memory name is case-sensitive.
	This option applies only if the server was started with the [`shared_memory`](server-system-variables.md) system variable enabled to support shared-memory connections.
- `--silent`, `-s`
	| Command-Line Format | `--silent` |
	| --- | --- |
	Silent mode. Produce output only when errors occur.
- ``--socket=*`path`*``, ``-S *`path`*``
	| Command-Line Format | `--socket={file_name\|pipe_name}` |
	| --- | --- |
	| Type | String |
	For connections to `localhost`, the Unix socket file to use, or, on Windows, the name of the named pipe to use.
	On Windows, this option applies only if the server was started with the [`named_pipe`](server-system-variables.md) system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the [`named_pipe_full_access_group`](server-system-variables.md) system variable.
- `--ssl*`
	Options that begin with `--ssl` specify whether to connect to the server using encryption and indicate where to find SSL keys and certificates. See [Command Options for Encrypted Connections](connection-options.md).
- ``--tls-version=*`protocol_list`*``
	| Command-Line Format | `--tls-version=protocol_list` |
	| --- | --- |
	| Type | String |
	| Default Value | `TLSv1,TLSv1.1,TLSv1.2` |
	The permissible TLS protocols for encrypted connections. The value is a list of one or more comma-separated protocol names. The protocols that can be named for this option depend on the SSL library used to compile MySQL. For details, see [Section 6.3.2, “Encrypted Connection TLS Protocols and Ciphers”](encrypted-connection-protocols-ciphers.md).
	This option was added in MySQL 5.7.10.
- ``--user=*`user_name`*``, ``-u *`user_name`*``
	| Command-Line Format | `--user=user_name,` |
	| --- | --- |
	| Type | String |
	The user name of the MySQL account to use for connecting to the server.
- ``--use-threads=*`N`*``
	| Command-Line Format | `--use-threads=#` |
	| --- | --- |
	| Type | Numeric |
	Load files in parallel using *`N`* threads.
- `--verbose`, `-v`
	| Command-Line Format | `--verbose` |
	| --- | --- |
	Verbose mode. Print more information about what the program does.
- `--version`, `-V`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.

Here is a sample session that demonstrates use of **mysqlimport**:

```
$> mysql -e 'CREATE TABLE imptest(id INT, n VARCHAR(30))' test
$> ed
a
100     Max Sydow
101     Count Dracula
.
w imptest.txt
32
q
$> od -c imptest.txt
0000000   1   0   0  \t   M   a   x       S   y   d   o   w  \n   1   0
0000020   1  \t   C   o   u   n   t       D   r   a   c   u   l   a  \n
0000040
$> mysqlimport --local test imptest.txt
test.imptest: Records: 2  Deleted: 0  Skipped: 0  Warnings: 0
$> mysql -e 'SELECT * FROM imptest' test
+------+---------------+
| id   | n             |
+------+---------------+
|  100 | Max Sydow     |
|  101 | Count Dracula |
+------+---------------+
```