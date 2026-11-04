---
title: "4.4.7 mysql_upgrade — Check and Upgrade MySQL Tables"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-upgrade.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 4.4.7 mysql\_upgrade — Check and Upgrade MySQL Tables

Each time you upgrade MySQL, you should execute **mysql\_upgrade**, which looks for incompatibilities with the upgraded MySQL server:

- It upgrades the system tables in the `mysql` schema so that you can take advantage of new privileges or capabilities that might have been added.
- It upgrades the Performance Schema and `sys` schema.
- It examines user schemas.

If **mysql\_upgrade** finds that a table has a possible incompatibility, it performs a table check and, if problems are found, attempts a table repair. If the table cannot be repaired, see [Section 2.10.12, “Rebuilding or Repairing Tables or Indexes”](rebuilding-tables.md) for manual table repair strategies.

**mysql\_upgrade** communicates directly with the MySQL server, sending it the SQL statements required to perform an upgrade.

Important

In MySQL 5.7.11, the default [`--early-plugin-load`](server-options.md) value is the name of the `keyring_file` plugin library file, causing that plugin to be loaded by default. In MySQL 5.7.12 and higher, the default [`--early-plugin-load`](server-options.md) value is empty; to load the `keyring_file` plugin, you must explicitly specify the option with a value naming the `keyring_file` plugin library file.

`InnoDB` tablespace encryption requires that the keyring plugin to be used be loaded prior to `InnoDB` initialization, so this change of default [`--early-plugin-load`](server-options.md) value introduces an incompatibility for upgrades from 5.7.11 to 5.7.12 or higher. Administrators who have encrypted `InnoDB` tablespaces must take explicit action to ensure continued loading of the keyring plugin: Start the server with an [`--early-plugin-load`](server-options.md) option that names the plugin library file. For additional information, see [Section 6.4.4.1, “Keyring Plugin Installation”](keyring-plugin-installation.md).

Important

If you upgrade to MySQL 5.7.2 or later from a version older than 5.7.2, a change to the `mysql.user` table requires a special sequence of steps to perform an upgrade using **mysql\_upgrade**. For details, see [Section 2.10.3, “Changes in MySQL 5.7”](upgrading-from-previous-series.md).

Note

On Windows, you must run **mysql\_upgrade** with administrator privileges. You can do this by running a Command Prompt as Administrator and running the command. Failure to do so may result in the upgrade failing to execute correctly.

Caution

You should always back up your current MySQL installation *before* performing an upgrade. See [Section 7.2, “Database Backup Methods”](backup-methods.md).

Some upgrade incompatibilities may require special handling *before* upgrading your MySQL installation and running **mysql\_upgrade**. See [Section 2.10, “Upgrading MySQL”](upgrading.md), for instructions on determining whether any such incompatibilities apply to your installation and how to handle them.

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

By default, **mysql\_upgrade** runs as the MySQL `root` user. If the `root` password is expired when you run **mysql\_upgrade**, it displays a message telling you that your password is expired and that **mysql\_upgrade** failed as a result. To correct this, reset the `root` password to unexpire it and run **mysql\_upgrade** again. First, connect to the server as `root`:

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

Unless invoked with the `--upgrade-system-tables` option, **mysql\_upgrade** processes all tables in all user schemas as necessary. Table checking might take a long time to complete. Each table is locked and therefore unavailable to other sessions while it is being processed. Check and repair operations can be time-consuming, particularly for large tables. Table checking uses the `FOR UPGRADE` option of the [`CHECK TABLE`](check-table.md) statement. For details about what this option entails, see [Section 13.7.2.2, “CHECK TABLE Statement”](check-table.md).

**mysql\_upgrade** marks all checked and repaired tables with the current MySQL version number. This ensures that the next time you run **mysql\_upgrade** with the same version of the server, it can be determined whether there is any need to check or repair a given table again.

**mysql\_upgrade** saves the MySQL version number in a file named `mysql_upgrade_info` in the data directory. This is used to quickly check whether all tables have been checked for this release so that table-checking can be skipped. To ignore this file and perform the check regardless, use the `--force` option.

**mysql\_upgrade** checks `mysql.user` system table rows and, for any row with an empty `plugin` column, sets that column to `'mysql_native_password'` or `'mysql_old_password'` depending on the hash format of the `Password` column value.

Support for pre-4.1 password hashing and `mysql_old_password` has been removed, so **mysql\_upgrade** sets empty `plugin` values to `'mysql_native_password'` if the credentials use a hash format compatible with that plugin. Rows with a pre-4.1 password hash must be upgraded manually. For account upgrade instructions, see [Section 6.4.1.3, “Migrating Away from Pre-4.1 Password Hashing and the mysql\_old\_password Plugin”](account-upgrades.md).

**mysql\_upgrade** does not upgrade the contents of the time zone tables or help tables. For upgrade instructions, see [Section 5.1.13, “MySQL Server Time Zone Support”](time-zone-support.md), and [Section 5.1.14, “Server-Side Help Support”](server-side-help-support.md).

Unless invoked with the `--skip-sys-schema` option, **mysql\_upgrade** installs the `sys` schema if it is not installed, and upgrades it to the current version otherwise. An error occurs if a `sys` schema exists but has no `version` view, on the assumption that its absence indicates a user-created schema:

```
A sys schema exists with no sys.version view. If
you have a user created sys schema, this must be renamed for the
upgrade to succeed.
```

To upgrade in this case, remove or rename the existing `sys` schema first.

**mysql\_upgrade** checks for partitioned `InnoDB` tables that were created using the generic partitioning handler and attempts to upgrade them to `InnoDB` native partitioning. (Bug #76734, Bug #20727344) You can upgrade such tables individually in the [**mysql**](mysql.md) client using the [`ALTER         TABLE ... UPGRADE PARTITIONING`](alter-table-partition-operations.md) SQL statement.

**mysql\_upgrade** supports the following options, which can be specified on the command line or in the `[mysql_upgrade]` and `[client]` groups of an option file. For information about option files used by MySQL programs, see [Section 4.2.2.2, “Using Option Files”](option-files.md).

**Table 4.12 mysql\_upgrade Options**

| Option Name | Description |
| --- | --- |
| \--bind-address | Use specified network interface to connect to MySQL Server |
| \--character-sets-dir | Directory where character sets are installed |
| \--compress | Compress all information sent between client and server |
| \--debug | Write debugging log |
| \--debug-check | Print debugging information when program exits |
| \--debug-info | Print debugging information, memory, and CPU statistics when program exits |
| \--default-auth | Authentication plugin to use |
| \--default-character-set | Specify default character set |
| \--defaults-extra-file | Read named option file in addition to usual option files |
| \--defaults-file | Read only named option file |
| \--defaults-group-suffix | Option group suffix value |
| \--force | Force execution even if mysql\_upgrade has already been executed for current MySQL version |
| \--help | Display help message and exit |
| \--host | Host on which MySQL server is located |
| \--login-path | Read login path options from.mylogin.cnf |
| \--max-allowed-packet | Maximum packet length to send to or receive from server |
| \--net-buffer-length | Buffer size for TCP/IP and socket communication |
| \--no-defaults | Read no option files |
| \--password | Password to use when connecting to server |
| \--pipe | Connect to server using named pipe (Windows only) |
| \--plugin-dir | Directory where plugins are installed |
| \--port | TCP/IP port number for connection |
| \--print-defaults | Print default options |
| \--protocol | Transport protocol to use |
| \--shared-memory-base-name | Shared-memory name for shared-memory connections (Windows only) |
| \--skip-sys-schema | Do not install or upgrade sys schema |
| \--socket | Unix socket file or Windows named pipe to use |
| \--ssl | Enable connection encryption |
| \--ssl-ca | File that contains list of trusted SSL Certificate Authorities |
| \--ssl-capath | Directory that contains trusted SSL Certificate Authority certificate files |
| \--ssl-cert | File that contains X.509 certificate |
| \--ssl-cipher | Permissible ciphers for connection encryption |
| \--ssl-crl | File that contains certificate revocation lists |
| \--ssl-crlpath | Directory that contains certificate revocation-list files |
| \--ssl-key | File that contains X.509 key |
| \--ssl-mode | Desired security state of connection to server |
| \--ssl-verify-server-cert | Verify host name against server certificate Common Name identity |
| \--tls-version | Permissible TLS protocols for encrypted connections |
| \--upgrade-system-tables | Update only system tables, not user schemas |
| \--user | MySQL user name to use when connecting to server |
| \--verbose | Verbose mode |
| \--version-check | Check for proper server version |
| \--write-binlog | Write all statements to binary log |

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
	The directory where character sets are installed. See [Section 10.15, “Character Set Configuration”](charset-configuration.md).
- `--compress`, `-C`
	| Command-Line Format | `--compress[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	Compress all information sent between the client and the server if possible. See [Section 4.2.6, “Connection Compression Control”](connection-compression-control.md).
- [``--debug[=*`debug_options`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/mysql-upgrade.html#option_mysql_upgrade_debug), ``-#             [*`debug_options`*]``
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
	A hint about which client-side authentication plugin to use. See [Section 6.2.13, “Pluggable Authentication”](pluggable-authentication.md).
- ``--default-character-set=*`charset_name`*``
	| Command-Line Format | `--default-character-set=name` |
	| --- | --- |
	| Type | String |
	Use *`charset_name`* as the default character set. See [Section 10.15, “Character Set Configuration”](charset-configuration.md).
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
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--defaults-group-suffix=*`str`*``
	| Command-Line Format | `--defaults-group-suffix=str` |
	| --- | --- |
	| Type | String |
	Read not only the usual option groups, but also groups with the usual names and a suffix of *`str`*. For example, **mysql\_upgrade** normally reads the `[client]` and `[mysql_upgrade]` groups. If this option is given as `--defaults-group-suffix=_other`, **mysql\_upgrade** also reads the `[client_other]` and `[mysql_upgrade_other]` groups.
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--force`
	| Command-Line Format | `--force` |
	| --- | --- |
	| Type | Boolean |
	Ignore the `mysql_upgrade_info` file and force execution even if **mysql\_upgrade** has already been executed for the current version of MySQL.
- ``--host=*`host_name`*``, ``-h *`host_name`*``
	| Command-Line Format | `--host=name` |
	| --- | --- |
	| Type | String |
	Connect to the MySQL server on the given host.
- ``--login-path=*`name`*``
	| Command-Line Format | `--login-path=name` |
	| --- | --- |
	| Type | String |
	Read options from the named login path in the `.mylogin.cnf` login path file. A “login path” is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 4.6.6, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
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
	The exception is that the `.mylogin.cnf` file is read in all cases, if it exists. This permits passwords to be specified in a safer way than on the command line even when `--no-defaults` is used. To create `.mylogin.cnf`, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 4.6.6, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- [``--password[=*`password`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/mysql-upgrade.html#option_mysql_upgrade_password), ``-p[*`password`*]``
	| Command-Line Format | `--password[=name]` |
	| --- | --- |
	| Type | String |
	The password of the MySQL account used for connecting to the server. The password value is optional. If not given, **mysql\_upgrade** prompts for one. If given, there must be *no space* between `--password=` or `-p` and the password following it. If no password option is specified, the default is to send no password.
	Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See [Section 6.1.2.1, “End-User Guidelines for Password Security”](password-security-user.md).
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
	The directory in which to look for plugins. Specify this option if the `--default-auth` option is used to specify an authentication plugin but **mysql\_upgrade** does not find it. See [Section 6.2.13, “Pluggable Authentication”](pluggable-authentication.md).
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
	The transport protocol to use for connecting to the server. It is useful when the other connection parameters normally result in use of a protocol other than the one you want. For details on the permissible values, see [Section 4.2.5, “Connection Transport Protocols”](transport-protocols.md).
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
- ``--tls-version=*`protocol_list`*``
	| Command-Line Format | `--tls-version=protocol_list` |
	| --- | --- |
	| Type | String |
	| Default Value | `TLSv1,TLSv1.1,TLSv1.2` |
	The permissible TLS protocols for encrypted connections. The value is a list of one or more comma-separated protocol names. The protocols that can be named for this option depend on the SSL library used to compile MySQL. For details, see [Section 6.3.2, “Encrypted Connection TLS Protocols and Ciphers”](encrypted-connection-protocols-ciphers.md).
	This option was added in MySQL 5.7.10.
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