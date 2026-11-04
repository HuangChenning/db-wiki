---
title: "6.4.5 mysql_upgrade — Check and Upgrade MySQL Tables"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysql-upgrade.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 6.4.5 mysql\_upgrade — Check and Upgrade MySQL Tables

Note

As of MySQL 8.0.16, the MySQL server performs the upgrade tasks previously handled by **mysql\_upgrade** (for details, see [Section 3.4, “What the MySQL Upgrade Process Upgrades”](upgrading-what-is-upgraded.md)). Consequently, **mysql\_upgrade** is unneeded and is deprecated as of that version; expect it to be removed in a future version of MySQL. Because **mysql\_upgrade** no longer performs upgrade tasks, it exits with status 0 unconditionally.

Each time you upgrade MySQL, you should execute **mysql\_upgrade**, which looks for incompatibilities with the upgraded MySQL server:

- It upgrades the system tables in the `mysql` schema so that you can take advantage of new privileges or capabilities that might have been added.
- It upgrades the Performance Schema, `INFORMATION_SCHEMA`, and `sys` schema.
- It examines user schemas.

If **mysql\_upgrade** finds that a table has a possible incompatibility, it performs a table check and, if problems are found, attempts a table repair. If the table cannot be repaired, see [Section 3.14, “Rebuilding or Repairing Tables or Indexes”](rebuilding-tables.md) for manual table repair strategies.

**mysql\_upgrade** communicates directly with the MySQL server, sending it the SQL statements required to perform an upgrade.

Caution

You should always back up your current MySQL installation *before* performing an upgrade. See [Section 9.2, “Database Backup Methods”](backup-methods.md).

Some upgrade incompatibilities may require special handling *before* upgrading your MySQL installation and running **mysql\_upgrade**. See [Chapter 3, *Upgrading MySQL*](upgrading.md), for instructions on determining whether any such incompatibilities apply to your installation and how to handle them.

Use **mysql\_upgrade** like this:

1. Ensure that the server is running.
2. Invoke **mysql\_upgrade** to upgrade the system tables in the `mysql` schema and check and repair tables in other schemas:
	```
	mysql_upgrade [options]
	```
3. Stop the server and restart it so that any system table changes take effect.

If you have multiple MySQL server instances to upgrade, invoke **mysql\_upgrade** with connection parameters appropriate for connecting to each of the desired servers. For example, with servers running on the local host on parts 3306 through 3308, upgrade each of them by connecting to the appropriate port:

```
mysql_upgrade --protocol=tcp -P 3306 [other_options]
mysql_upgrade --protocol=tcp -P 3307 [other_options]
mysql_upgrade --protocol=tcp -P 3308 [other_options]
```

For local host connections on Unix, the `--protocol=tcp` option forces a connection using TCP/IP rather than the Unix socket file.

By default, **mysql\_upgrade** runs as the MySQL `root` user. If the `root` password is expired when you run **mysql\_upgrade**, it displays a message that your password is expired and that **mysql\_upgrade** failed as a result. To correct this, reset the `root` password to unexpire it and run **mysql\_upgrade** again. First, connect to the server as `root`:

```
$> mysql -u root -p
Enter password: ****  <- enter root password here
```

Reset the password using [`ALTER         USER`](alter-user.md):

```
mysql> ALTER USER USER() IDENTIFIED BY 'root-password';
```

Then exit [**mysql**](mysql.md) and run **mysql\_upgrade** again:

```
$> mysql_upgrade [options]
```

If you run the server with the [`disabled_storage_engines`](server-system-variables.md) system variable set to disable certain storage engines (for example, `MyISAM`), **mysql\_upgrade** might fail with an error like this:

```
mysql_upgrade: [ERROR] 3161: Storage engine MyISAM is disabled
(Table creation is disallowed).
```

To handle this, restart the server with [`disabled_storage_engines`](server-system-variables.md) disabled. Then you should be able to run **mysql\_upgrade** successfully. After that, restart the server with [`disabled_storage_engines`](server-system-variables.md) set to its original value.

Unless invoked with the `--upgrade-system-tables` option, **mysql\_upgrade** processes all tables in all user schemas as necessary. Table checking might take a long time to complete. Each table is locked and therefore unavailable to other sessions while it is being processed. Check and repair operations can be time-consuming, particularly for large tables. Table checking uses the `FOR UPGRADE` option of the [`CHECK TABLE`](check-table.md) statement. For details about what this option entails, see [Section 15.7.3.2, “CHECK TABLE Statement”](check-table.md).

**mysql\_upgrade** marks all checked and repaired tables with the current MySQL version number. This ensures that the next time you run **mysql\_upgrade** with the same version of the server, it can be determined whether there is any need to check or repair a given table again.

**mysql\_upgrade** saves the MySQL version number in a file named `mysql_upgrade_info` in the data directory. This is used to quickly check whether all tables have been checked for this release so that table-checking can be skipped. To ignore this file and perform the check regardless, use the `--force` option.

Note

The `mysql_upgrade_info` file is deprecated; expect it to be removed in a future version of MySQL.

**mysql\_upgrade** checks `mysql.user` system table rows and, for any row with an empty `plugin` column, sets that column to `'mysql_native_password'` if the credentials use a hash format compatible with that plugin. Rows with a pre-4.1 password hash must be upgraded manually.

**mysql\_upgrade** does not upgrade the contents of the time zone tables or help tables. For upgrade instructions, see [Section 7.1.15, “MySQL Server Time Zone Support”](time-zone-support.md), and [Section 7.1.17, “Server-Side Help Support”](server-side-help-support.md).

Unless invoked with the `--skip-sys-schema` option, **mysql\_upgrade** installs the `sys` schema if it is not installed, and upgrades it to the current version otherwise. An error occurs if a `sys` schema exists but has no `version` view, on the assumption that its absence indicates a user-created schema:

```
A sys schema exists with no sys.version view. If
you have a user created sys schema, this must be renamed for the
upgrade to succeed.
```

To upgrade in this case, remove or rename the existing `sys` schema first.

**mysql\_upgrade** supports the following options, which can be specified on the command line or in the `[mysql_upgrade]` and `[client]` groups of an option file. For information about option files used by MySQL programs, see [Section 6.2.2.2, “Using Option Files”](option-files.md).

**Table 6.11 mysql\_upgrade Options**

| Option Name | Description | Deprecated |
| --- | --- | --- |
| \--bind-address | Use specified network interface to connect to MySQL Server |  |
| \--character-sets-dir | Directory where character sets are installed |  |
| \--compress | Compress all information sent between client and server | Yes |
| \--compression-algorithms | Permitted compression algorithms for connections to server |  |
| \--debug | Write debugging log |  |
| \--debug-check | Print debugging information when program exits |  |
| \--debug-info | Print debugging information, memory, and CPU statistics when program exits |  |
| \--default-auth | Authentication plugin to use |  |
| \--default-character-set | Specify default character set |  |
| \--defaults-extra-file | Read named option file in addition to usual option files |  |
| \--defaults-file | Read only named option file |  |
| \--defaults-group-suffix | Option group suffix value |  |
| \--force | Force execution even if mysql\_upgrade has already been executed for current MySQL version |  |
| \--get-server-public-key | Request RSA public key from server |  |
| \--help | Display help message and exit |  |
| \--host | Host on which MySQL server is located |  |
| \--login-path | Read login path options from.mylogin.cnf |  |
| \--max-allowed-packet | Maximum packet length to send to or receive from server |  |
| \--net-buffer-length | Buffer size for TCP/IP and socket communication |  |
| \--no-defaults | Read no option files |  |
| \--password | Password to use when connecting to server |  |
| \--pipe | Connect to server using named pipe (Windows only) |  |
| \--plugin-dir | Directory where plugins are installed |  |
| \--port | TCP/IP port number for connection |  |
| \--print-defaults | Print default options |  |
| \--protocol | Transport protocol to use |  |
| \--server-public-key-path | Path name to file containing RSA public key |  |
| \--shared-memory-base-name | Shared-memory name for shared-memory connections (Windows only) |  |
| \--skip-sys-schema | Do not install or upgrade sys schema |  |
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
| \--upgrade-system-tables | Update only system tables, not user schemas |  |
| \--user | MySQL user name to use when connecting to server |  |
| \--verbose | Verbose mode |  |
| \--version-check | Check for proper server version |  |
| \--write-binlog | Write all statements to binary log |  |
| \--zstd-compression-level | Compression level for connections to server that use zstd compression |  |

- `--help`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display a short help message and exit.
- ``--bind-address=*`ip_address`*``
	| Command-Line Format | `--bind-address=ip_address` |
	| --- | --- |
	On a computer having multiple network interfaces, use this option to select which interface to use for connecting to the MySQL server.
- ``--character-sets-dir=*`dir_name`*``
	| Command-Line Format | `--character-sets-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The directory where character sets are installed. See [Section 12.15, “Character Set Configuration”](charset-configuration.md).
- `--compress`, `-C`
	| Command-Line Format | `--compress[={OFF\|ON}]` |
	| --- | --- |
	| Deprecated | Yes |
	| Type | Boolean |
	| Default Value | `OFF` |
	Compress all information sent between the client and the server if possible. See [Section 6.2.8, “Connection Compression Control”](connection-compression-control.md).
	As of MySQL 8.0.18, this option is deprecated. Expect it to be removed in a future version of MySQL. See [Configuring Legacy Connection Compression](connection-compression-control.md).
- ``--compression-algorithms=*`value`*``
	| Command-Line Format | `--compression-algorithms=value` |
	| --- | --- |
	| Type | Set |
	| Default Value | `uncompressed` |
	| Valid Values | `zlib`  `zstd`  `uncompressed` |
	The permitted compression algorithms for connections to the server. The available algorithms are the same as for the [`protocol_compression_algorithms`](server-system-variables.md) system variable. The default value is `uncompressed`.
	For more information, see [Section 6.2.8, “Connection Compression Control”](connection-compression-control.md).
	This option was added in MySQL 8.0.18.
- [``--debug[=*`debug_options`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-upgrade.html#option_mysql_upgrade_debug), ``-#             [*`debug_options`*]``
	| Command-Line Format | `--debug[=#]` |
	| --- | --- |
	| Type | String |
	| Default Value | `d:t:O,/tmp/mysql_upgrade.trace` |
	Write a debugging log. A typical *`debug_options`* string is ``d:t:o,*`file_name`*``. The default is `d:t:O,/tmp/mysql_upgrade.trace`.
- `--debug-check`
	| Command-Line Format | `--debug-check` |
	| --- | --- |
	| Type | Boolean |
	Print some debugging information when the program exits.
- `--debug-info`, `-T`
	| Command-Line Format | `--debug-info` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Print debugging information and memory and CPU usage statistics when the program exits.
- ``--default-auth=*`plugin`*``
	| Command-Line Format | `--default-auth=plugin` |
	| --- | --- |
	| Type | String |
	A hint about which client-side authentication plugin to use. See [Section 8.2.17, “Pluggable Authentication”](pluggable-authentication.md).
- ``--default-character-set=*`charset_name`*``
	| Command-Line Format | `--default-character-set=name` |
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
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--defaults-group-suffix=*`str`*``
	| Command-Line Format | `--defaults-group-suffix=str` |
	| --- | --- |
	| Type | String |
	Read not only the usual option groups, but also groups with the usual names and a suffix of *`str`*. For example, **mysql\_upgrade** normally reads the `[client]` and `[mysql_upgrade]` groups. If this option is given as `--defaults-group-suffix=_other`, **mysql\_upgrade** also reads the `[client_other]` and `[mysql_upgrade_other]` groups.
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--force`
	| Command-Line Format | `--force` |
	| --- | --- |
	| Type | Boolean |
	Ignore the `mysql_upgrade_info` file and force execution even if **mysql\_upgrade** has already been executed for the current version of MySQL.
- `--get-server-public-key`
	| Command-Line Format | `--get-server-public-key` |
	| --- | --- |
	| Type | Boolean |
	Request from the server the public key required for RSA key pair-based password exchange. This option applies to clients that authenticate with the `caching_sha2_password` authentication plugin. For that plugin, the server does not send the public key unless requested. This option is ignored for accounts that do not authenticate with that plugin. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection.
	If ``--server-public-key-path=*`file_name`*`` is given and specifies a valid public key file, it takes precedence over `--get-server-public-key`.
	For information about the `caching_sha2_password` plugin, see [Section 8.4.1.2, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).
- ``--host=*`host_name`*``, ``-h *`host_name`*``
	| Command-Line Format | `--host=name` |
	| --- | --- |
	| Type | String |
	Connect to the MySQL server on the given host.
- ``--login-path=*`name`*``
	| Command-Line Format | `--login-path=name` |
	| --- | --- |
	| Type | String |
	Read options from the named login path in the `.mylogin.cnf` login path file. A “login path” is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 6.6.7, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--max-allowed-packet=*`value`*``
	| Command-Line Format | `--max-allowed-packet=value` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `25165824` |
	| Minimum Value | `4096` |
	| Maximum Value | `2147483648` |
	The maximum size of the buffer for client/server communication. The default value is 24MB. The minimum and maximum values are 4KB and 2GB.
- ``--net-buffer-length=*`value`*``
	| Command-Line Format | `--net-buffer-length=value` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `1047552` |
	| Minimum Value | `4096` |
	| Maximum Value | `16777216` |
	The initial size of the buffer for client/server communication. The default value is 1MB − 1KB. The minimum and maximum values are 4KB and 16MB.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read any option files. If program startup fails due to reading unknown options from an option file, `--no-defaults` can be used to prevent them from being read.
	The exception is that the `.mylogin.cnf` file is read in all cases, if it exists. This permits passwords to be specified in a safer way than on the command line even when `--no-defaults` is used. To create `.mylogin.cnf`, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 6.6.7, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- [``--password[=*`password`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-upgrade.html#option_mysql_upgrade_password), ``-p[*`password`*]``
	| Command-Line Format | `--password[=name]` |
	| --- | --- |
	| Type | String |
	The password of the MySQL account used for connecting to the server. The password value is optional. If not given, **mysql\_upgrade** prompts for one. If given, there must be *no space* between `--password=` or `-p` and the password following it. If no password option is specified, the default is to send no password.
	Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See [Section 8.1.2.1, “End-User Guidelines for Password Security”](password-security-user.md).
	To explicitly specify that there is no password and that **mysql\_upgrade** should not prompt for one, use the `--skip-password` option.
- `--pipe`, `-W`
	| Command-Line Format | `--pipe` |
	| --- | --- |
	| Type | String |
	On Windows, connect to the server using a named pipe. This option applies only if the server was started with the [`named_pipe`](server-system-variables.md) system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the [`named_pipe_full_access_group`](server-system-variables.md) system variable.
- ``--plugin-dir=*`dir_name`*``
	| Command-Line Format | `--plugin-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The directory in which to look for plugins. Specify this option if the `--default-auth` option is used to specify an authentication plugin but **mysql\_upgrade** does not find it. See [Section 8.2.17, “Pluggable Authentication”](pluggable-authentication.md).
- ``--port=*`port_num`*``, ``-P *`port_num`*``
	| Command-Line Format | `--port=#` |
	| --- | --- |
	| Type | Numeric |
	For TCP/IP connections, the port number to use.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print the program name and all options that it gets from option files.
- `--protocol={TCP|SOCKET|PIPE|MEMORY}`
	| Command-Line Format | `--protocol=name` |
	| --- | --- |
	| Type | String |
	The transport protocol to use for connecting to the server. It is useful when the other connection parameters normally result in use of a protocol other than the one you want. For details on the permissible values, see [Section 6.2.7, “Connection Transport Protocols”](transport-protocols.md).
- ``--server-public-key-path=*`file_name`*``
	| Command-Line Format | `--server-public-key-path=file_name` |
	| --- | --- |
	| Type | File name |
	The path name to a file in PEM format containing a client-side copy of the public key required by the server for RSA key pair-based password exchange. This option applies to clients that authenticate with the `sha256_password` or `caching_sha2_password` authentication plugin. This option is ignored for accounts that do not authenticate with one of those plugins. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection.
	If ``--server-public-key-path=*`file_name`*`` is given and specifies a valid public key file, it takes precedence over `--get-server-public-key`.
	For `sha256_password`, this option applies only if MySQL was built using OpenSSL.
	For information about the `sha256_password` and `caching_sha2_password` plugins, see [Section 8.4.1.3, “SHA-256 Pluggable Authentication”](sha256-pluggable-authentication.md), and [Section 8.4.1.2, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).
- ``--shared-memory-base-name=*`name`*``
	| Command-Line Format | `--shared-memory-base-name=name` |
	| --- | --- |
	| Platform Specific | Windows |
	On Windows, the shared-memory name to use for connections made using shared memory to a local server. The default value is `MYSQL`. The shared-memory name is case-sensitive.
	This option applies only if the server was started with the [`shared_memory`](server-system-variables.md) system variable enabled to support shared-memory connections.
- `--skip-sys-schema`
	| Command-Line Format | `--skip-sys-schema` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	By default, **mysql\_upgrade** installs the `sys` schema if it is not installed, and upgrades it to the current version otherwise. The `--skip-sys-schema` option suppresses this behavior.
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
- `--upgrade-system-tables`, `-s`
	| Command-Line Format | `--upgrade-system-tables` |
	| --- | --- |
	| Type | Boolean |
	Upgrade only the system tables in the `mysql` schema, do not upgrade user schemas.
- ``--user=*`user_name`*``, ``-u *`user_name`*``
	| Command-Line Format | `--user=name` |
	| --- | --- |
	| Type | String |
	The user name of the MySQL account to use for connecting to the server. The default user name is `root`.
- `--verbose`
	| Command-Line Format | `--verbose` |
	| --- | --- |
	| Type | Boolean |
	Verbose mode. Print more information about what the program does.
- `--version-check`, `-k`
	| Command-Line Format | `--version-check` |
	| --- | --- |
	| Type | Boolean |
	Check the version of the server to which **mysql\_upgrade** is connecting to verify that it is the same as the version for which **mysql\_upgrade** was built. If not, **mysql\_upgrade** exits. This option is enabled by default; to disable the check, use `--skip-version-check`.
- `--write-binlog`
	| Command-Line Format | `--write-binlog` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	By default, binary logging by **mysql\_upgrade** is disabled. Invoke the program with `--write-binlog` if you want its actions to be written to the binary log.
	When the server is running with global transaction identifiers (GTIDs) enabled ([`gtid_mode=ON`](replication-options-gtids.md)), do not enable binary logging by **mysql\_upgrade**.
- ``--zstd-compression-level=*`level`*``
	| Command-Line Format | `--zstd-compression-level=#` |
	| --- | --- |
	| Type | Integer |
	The compression level to use for connections to the server that use the `zstd` compression algorithm. The permitted levels are from 1 to 22, with larger values indicating increasing levels of compression. The default `zstd` compression level is 3. The compression level setting has no effect on connections that do not use `zstd` compression.
	For more information, see [Section 6.2.8, “Connection Compression Control”](connection-compression-control.md).
	This option was added in MySQL 8.0.18.