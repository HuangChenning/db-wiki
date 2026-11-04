---
title: "6.5.4 mysqldump — A Database Backup Program"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/mysqldump.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 6.5.4 mysqldump — A Database Backup Program

The **mysqldump** client utility performs [logical backups](glossary.md), producing a set of SQL statements that can be executed to reproduce the original database object definitions and table data. It dumps one or more MySQL databases for backup or transfer to another SQL server. The **mysqldump** command can also generate output in CSV, other delimited text, or XML format.

Tip

Consider using the [MySQL Shell dump utilities](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.4-en/mysql-shell-utilities-dump-instance-schema.html), which provide parallel dumping with multiple threads, file compression, and progress information display, as well as cloud features such as Oracle Cloud Infrastructure Object Storage streaming, and MySQL HeatWave compatibility checks and modifications. Dumps can be easily imported into a MySQL Server instance or a MySQL HeatWave DB System using the [MySQL Shell load dump utilities](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.4-en/mysql-shell-utilities-load-dump.html). Installation instructions for MySQL Shell can be found [here](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.4-en/mysql-shell-install.html).

**mysqldump** requires at least the [`SELECT`](privileges-provided.md) privilege for dumped tables, [`SHOW VIEW`](privileges-provided.md) for dumped views, [`TRIGGER`](privileges-provided.md) for dumped triggers, [`LOCK TABLES`](privileges-provided.md) if the `--single-transaction` option is not used, [`PROCESS`](privileges-provided.md) if the `--no-tablespaces` option is not used, and the [`RELOAD`](privileges-provided.md) or [`FLUSH_TABLES`](privileges-provided.md) privilege with `--single-transaction` if both [`gtid_mode=ON`](replication-options-gtids.md) and [`gtid_purged=ON|AUTO`](replication-options-gtids.md). Certain options might require other privileges as noted in the option descriptions.

To reload a dump file, you must have the privileges required to execute the statements that it contains, such as the appropriate `CREATE` privileges for objects created by those statements.

**mysqldump** output can include [`ALTER DATABASE`](alter-database.md) statements that change the database collation. These may be used when dumping stored programs to preserve their character encodings. To reload a dump file containing such statements, the `ALTER` privilege for the affected database is required.

A dump made using PowerShell on Windows with output redirection creates a file that has UTF-16 encoding:

```
mysqldump [options] > dump.sql
```

However, UTF-16 is not permitted as a connection character set (see [Impermissible Client Character Sets](charset-connection.md)), so the dump file cannot be loaded correctly. To work around this issue, use the `--result-file` option, which creates the output in ASCII format:

```
mysqldump [options] --result-file=dump.sql
```

It is not recommended to load a dump file when GTIDs are enabled on the server ([`gtid_mode=ON`](replication-options-gtids.md)), if your dump file includes system tables. **mysqldump** issues DML instructions for the system tables which use the non-transactional MyISAM storage engine, and this combination is not permitted when GTIDs are enabled.

#### Performance and Scalability Considerations

`mysqldump` advantages include the convenience and flexibility of viewing or even editing the output before restoring. You can clone databases for development and DBA work, or produce slight variations of an existing database for testing. It is not intended as a fast or scalable solution for backing up substantial amounts of data. With large data sizes, even if the backup step takes a reasonable time, restoring the data can be very slow because replaying the SQL statements involves disk I/O for insertion, index creation, and so on.

For large-scale backup and restore, a [physical](glossary.md) backup is more appropriate, to copy the data files in their original format so that they can be restored quickly.

If your tables are primarily [`InnoDB`](innodb-storage-engine.md) tables, or if you have a mix of `InnoDB` and [`MyISAM`](myisam-storage-engine.md) tables, consider using **mysqlbackup**, which is available as part of MySQL Enterprise. This tool provides high performance for `InnoDB` backups with minimal disruption; it can also back up tables from `MyISAM` and other storage engines; it also provides a number of convenient options to accommodate different backup scenarios. See [Section 32.1, “MySQL Enterprise Backup Overview”](mysql-enterprise-backup.md).

**mysqldump** can retrieve and dump table contents row by row, or it can retrieve the entire content from a table and buffer it in memory before dumping it. Buffering in memory can be a problem if you are dumping large tables. To dump tables row by row, use the `--quick` option (or `--opt`, which enables `--quick`). The `--opt` option (and hence `--quick`) is enabled by default, so to enable memory buffering, use `--skip-quick`.

If you are using a recent version of **mysqldump** to generate a dump to be reloaded into a very old MySQL server, use the `--skip-opt` option instead of the `--opt` or `--extended-insert` option.

For additional information about **mysqldump**, see [Section 9.4, “Using mysqldump for Backups”](using-mysqldump.md).

#### Invocation Syntax

There are in general three ways to use **mysqldump** —in order to dump a set of one or more tables, a set of one or more complete databases, or an entire MySQL server—as shown here:

```
mysqldump [options] db_name [tbl_name ...]
mysqldump [options] --databases db_name ...
mysqldump [options] --all-databases
```

To dump entire databases, do not name any tables following *`db_name`*, or use the `--databases` or `--all-databases` option.

To see a list of the options your version of **mysqldump** supports, issue the command **mysqldump** `--help`.

#### Option Syntax - Alphabetical Summary

**mysqldump** supports the following options, which can be specified on the command line or in the `[mysqldump]` and `[client]` groups of an option file. For information about option files used by MySQL programs, see [Section 6.2.2.2, “Using Option Files”](option-files.md).

**Table 6.13 mysqldump Options**

| Option Name | Description |
| --- | --- |
| \--add-drop-database | Add DROP DATABASE statement before each CREATE DATABASE statement |
| \--add-drop-table | Add DROP TABLE statement before each CREATE TABLE statement |
| \--add-drop-trigger | Add DROP TRIGGER statement before each CREATE TRIGGER statement |
| \--add-locks | Surround each table dump with LOCK TABLES and UNLOCK TABLES statements |
| \--all-databases | Dump all tables in all databases |
| \--allow-keywords | Allow creation of column names that are keywords |
| \--apply-replica-statements | Include STOP REPLICA prior to CHANGE REPLICATION SOURCE TO statement and START REPLICA at end of output |
| \--apply-slave-statements | Include STOP SLAVE prior to CHANGE MASTER statement and START SLAVE at end of output |
| \--bind-address | Use specified network interface to connect to MySQL Server |
| \--character-sets-dir | Directory where character sets are installed |
| \--column-statistics | Write ANALYZE TABLE statements to generate statistics histograms |
| \--comments | Add comments to dump file |
| \--compact | Produce more compact output |
| \--compatible | Produce output that is more compatible with other database systems or with older MySQL servers |
| \--complete-insert | Use complete INSERT statements that include column names |
| \--compress | Compress all information sent between client and server |
| \--compression-algorithms | Permitted compression algorithms for connections to server |
| \--create-options | Include all MySQL-specific table options in CREATE TABLE statements |
| \--databases | Interpret all name arguments as database names |
| \--debug | Write debugging log |
| \--debug-check | Print debugging information when program exits |
| \--debug-info | Print debugging information, memory, and CPU statistics when program exits |
| \--default-auth | Authentication plugin to use |
| \--default-character-set | Specify default character set |
| \--defaults-extra-file | Read named option file in addition to usual option files |
| \--defaults-file | Read only named option file |
| \--defaults-group-suffix | Option group suffix value |
| \--delete-master-logs | On a replication source server, delete the binary logs after performing the dump operation |
| \--delete-source-logs | On a replication source server, delete the binary logs after performing the dump operation |
| \--disable-keys | For each table, surround INSERT statements with statements to disable and enable keys |
| \--dump-date | Include dump date as "Dump completed on" comment if --comments is given |
| \--dump-replica | Include CHANGE REPLICATION SOURCE TO statement that lists binary log coordinates of replica's source |
| \--dump-slave | Include CHANGE MASTER statement that lists binary log coordinates of replica's source |
| \--enable-cleartext-plugin | Enable cleartext authentication plugin |
| \--events | Dump events from dumped databases |
| \--extended-insert | Use multiple-row INSERT syntax |
| \--fields-enclosed-by | This option is used with the --tab option and has the same meaning as the corresponding clause for LOAD DATA |
| \--fields-escaped-by | This option is used with the --tab option and has the same meaning as the corresponding clause for LOAD DATA |
| \--fields-optionally-enclosed-by | This option is used with the --tab option and has the same meaning as the corresponding clause for LOAD DATA |
| \--fields-terminated-by | This option is used with the --tab option and has the same meaning as the corresponding clause for LOAD DATA |
| \--flush-logs | Flush MySQL server log files before starting dump |
| \--flush-privileges | Emit a FLUSH PRIVILEGES statement after dumping mysql database |
| \--force | Continue even if an SQL error occurs during a table dump |
| \--get-server-public-key | Request RSA public key from server |
| \--help | Display help message and exit |
| \--hex-blob | Dump binary columns using hexadecimal notation |
| \--host | Host on which MySQL server is located |
| \--ignore-error | Ignore specified errors |
| \--ignore-table | Do not dump given table |
| \--ignore-views | Skip dumping table views |
| \--include-master-host-port | Include MASTER\_HOST/MASTER\_PORT options in CHANGE MASTER statement produced with --dump-slave |
| \--include-source-host-port | Include SOURCE\_HOST and SOURCE\_PORT options in CHANGE REPLICATION SOURCE TO statement produced with --dump-replica |
| \--init-command | Single SQL statement to execute after connecting or re-connecting to MySQL server; resets existing defined commands |
| \--init-command-add | Add an additional SQL statement to execute after connecting or re-connecting to MySQL server |
| \--insert-ignore | Write INSERT IGNORE rather than INSERT statements |
| \--lines-terminated-by | This option is used with the --tab option and has the same meaning as the corresponding clause for LOAD DATA |
| \--lock-all-tables | Lock all tables across all databases |
| \--lock-tables | Lock all tables before dumping them |
| \--log-error | Append warnings and errors to named file |
| \--login-path | Read login path options from.mylogin.cnf |
| \--master-data | Write the binary log file name and position to the output |
| \--max-allowed-packet | Maximum packet length to send to or receive from server |
| \--mysqld-long-query-time | Session value for slow query threshold |
| \--net-buffer-length | Buffer size for TCP/IP and socket communication |
| \--network-timeout | Increase network timeouts to permit larger table dumps |
| \--no-autocommit | Enclose the INSERT statements for each dumped table within SET autocommit = 0 and COMMIT statements |
| \--no-create-db | Do not write CREATE DATABASE statements |
| \--no-create-info | Do not write CREATE TABLE statements that re-create each dumped table |
| \--no-data | Do not dump table contents |
| \--no-defaults | Read no option files |
| \--no-login-paths | Do not read login paths from the login path file |
| \--no-set-names | Same as --skip-set-charset |
| \--no-tablespaces | Do not write any CREATE LOGFILE GROUP or CREATE TABLESPACE statements in output |
| \--opt | Shorthand for --add-drop-table --add-locks --create-options --disable-keys --extended-insert --lock-tables --quick --set-charset |
| \--order-by-primary | Dump each table's rows sorted by its primary key, or by its first unique index |
| \--output-as-version | Determines replica and event terminology used in dumps; for compatibility with older versions |
| \--password | Password to use when connecting to server |
| \--password1 | First multifactor authentication password to use when connecting to server |
| \--password2 | Second multifactor authentication password to use when connecting to server |
| \--password3 | Third multifactor authentication password to use when connecting to server |
| \--pipe | Connect to server using named pipe (Windows only) |
| \--plugin-authentication-kerberos-client-mode | Permit GSSAPI pluggable authentication through the MIT Kerberos library on Windows |
| \--plugin-dir | Directory where plugins are installed |
| \--port | TCP/IP port number for connection |
| \--print-defaults | Print default options |
| \--protocol | Transport protocol to use |
| \--quick | Retrieve rows for a table from the server a row at a time |
| \--quote-names | Quote identifiers within backtick characters |
| \--replace | Write REPLACE statements rather than INSERT statements |
| \--result-file | Direct output to a given file |
| \--routines | Dump stored routines (procedures and functions) from dumped databases |
| \--server-public-key-path | Path name to file containing RSA public key |
| \--set-charset | Add SET NAMES default\_character\_set to output |
| \--set-gtid-purged | Whether to add SET @@GLOBAL.GTID\_PURGED to output |
| \--shared-memory-base-name | Shared-memory name for shared-memory connections (Windows only) |
| \--show-create-skip-secondary-engine | Exclude SECONDARY ENGINE clause from CREATE TABLE statements |
| \--single-transaction | Issue a BEGIN SQL statement before dumping data from server |
| \--skip-add-drop-table | Do not add a DROP TABLE statement before each CREATE TABLE statement |
| \--skip-add-locks | Do not add locks |
| \--skip-comments | Do not add comments to dump file |
| \--skip-compact | Do not produce more compact output |
| \--skip-disable-keys | Do not disable keys |
| \--skip-extended-insert | Turn off extended-insert |
| \--skip-generated-invisible-primary-key | Do not include generated invisible primary keys in dump file |
| \--skip-opt | Turn off options set by --opt |
| \--skip-quick | Do not retrieve rows for a table from the server a row at a time |
| \--skip-quote-names | Do not quote identifiers |
| \--skip-set-charset | Do not write SET NAMES statement |
| \--skip-triggers | Do not dump triggers |
| \--skip-tz-utc | Turn off tz-utc |
| \--socket | Unix socket file or Windows named pipe to use |
| \--source-data | Write the binary log file name and position to the output |
| \--ssl-ca | File that contains list of trusted SSL Certificate Authorities |
| \--ssl-capath | Directory that contains trusted SSL Certificate Authority certificate files |
| \--ssl-cert | File that contains X.509 certificate |
| \--ssl-cipher | Permissible ciphers for connection encryption |
| \--ssl-crl | File that contains certificate revocation lists |
| \--ssl-crlpath | Directory that contains certificate revocation-list files |
| \--ssl-fips-mode | Whether to enable FIPS mode on client side |
| \--ssl-key | File that contains X.509 key |
| \--ssl-mode | Desired security state of connection to server |
| \--ssl-session-data | File that contains SSL session data |
| \--ssl-session-data-continue-on-failed-reuse | Whether to establish connections if session reuse fails |
| \--tab | Produce tab-separated data files |
| \--tables | Override --databases or -B option |
| \--tls-ciphersuites | Permissible TLSv1.3 ciphersuites for encrypted connections |
| \--tls-sni-servername | Server name supplied by the client |
| \--tls-version | Permissible TLS protocols for encrypted connections |
| \--triggers | Dump triggers for each dumped table |
| \--tz-utc | Add SET TIME\_ZONE='+00:00' to dump file |
| \--user | MySQL user name to use when connecting to server |
| \--verbose | Verbose mode |
| \--version | Display version information and exit |
| \--where | Dump only rows selected by given WHERE condition |
| \--xml | Produce XML output |
| \--zstd-compression-level | Compression level for connections to server that use zstd compression |

#### Connection Options

The **mysqldump** command logs into a MySQL server to extract information. The following options specify how to connect to the MySQL server, either on the same machine or a remote system.

- ``--bind-address=*`ip_address`*``
	| Command-Line Format | `--bind-address=ip_address` |
	| --- | --- |
	On a computer having multiple network interfaces, use this option to select which interface to use for connecting to the MySQL server.
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
- ``--default-auth=*`plugin`*``
	| Command-Line Format | `--default-auth=plugin` |
	| --- | --- |
	| Type | String |
	A hint about which client-side authentication plugin to use. See [Section 8.2.17, “Pluggable Authentication”](pluggable-authentication.md).
- `--enable-cleartext-plugin`
	| Command-Line Format | `--enable-cleartext-plugin` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Enable the `mysql_clear_password` cleartext authentication plugin. (See [Section 8.4.1.4, “Client-Side Cleartext Pluggable Authentication”](cleartext-pluggable-authentication.md).)
- `--get-server-public-key`
	| Command-Line Format | `--get-server-public-key` |
	| --- | --- |
	| Type | Boolean |
	Request from the server the public key required for RSA key pair-based password exchange. This option applies to clients that authenticate with the `caching_sha2_password` authentication plugin. For that plugin, the server does not send the public key unless requested. This option is ignored for accounts that do not authenticate with that plugin. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection.
	If ``--server-public-key-path=*`file_name`*`` is given and specifies a valid public key file, it takes precedence over `--get-server-public-key`.
	For information about the `caching_sha2_password` plugin, see [Section 8.4.1.2, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).
- ``--host=*`host_name`*``, ``-h *`host_name`*``
	| Command-Line Format | `--host` |
	| --- | --- |
	Dump data from the MySQL server on the given host. The default host is `localhost`.
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
- [``--password[=*`password`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/mysqldump.html#option_mysqldump_password), ``-p[*`password`*]``
	| Command-Line Format | `--password[=password]` |
	| --- | --- |
	| Type | String |
	The password of the MySQL account used for connecting to the server. The password value is optional. If not given, **mysqldump** prompts for one. If given, there must be *no space* between `--password=` or `-p` and the password following it. If no password option is specified, the default is to send no password.
	Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See [Section 8.1.2.1, “End-User Guidelines for Password Security”](password-security-user.md).
	To explicitly specify that there is no password and that **mysqldump** should not prompt for one, use the `--skip-password` option.
- [``--password1[=*`pass_val`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/mysqldump.html#option_mysqldump_password1)
	The password for multifactor authentication factor 1 of the MySQL account used for connecting to the server. The password value is optional. If not given, **mysqldump** prompts for one. If given, there must be *no space* between `--password1=` and the password following it. If no password option is specified, the default is to send no password.
	Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See [Section 8.1.2.1, “End-User Guidelines for Password Security”](password-security-user.md).
	To explicitly specify that there is no password and that **mysqldump** should not prompt for one, use the `--skip-password1` option.
	`--password1` and `--password` are synonymous, as are `--skip-password1` and `--skip-password`.
- [``--password2[=*`pass_val`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/mysqldump.html#option_mysqldump_password2)
	The password for multifactor authentication factor 2 of the MySQL account used for connecting to the server. The semantics of this option are similar to the semantics for `--password1`; see the description of that option for details.
- [``--password3[=*`pass_val`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/mysqldump.html#option_mysqldump_password3)
	The password for multifactor authentication factor 3 of the MySQL account used for connecting to the server. The semantics of this option are similar to the semantics for `--password1`; see the description of that option for details.
- `--pipe`, `-W`
	| Command-Line Format | `--pipe` |
	| --- | --- |
	| Type | String |
	On Windows, connect to the server using a named pipe. This option applies only if the server was started with the [`named_pipe`](server-system-variables.md) system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the [`named_pipe_full_access_group`](server-system-variables.md) system variable.
- ``--plugin-authentication-kerberos-client-mode=*`value`*``
	| Command-Line Format | `--plugin-authentication-kerberos-client-mode` |
	| --- | --- |
	| Type | String |
	| Default Value | `SSPI` |
	| Valid Values | `GSSAPI` |
	On Windows, the `authentication_kerberos_client` authentication plugin supports this plugin option. It provides two possible values that the client user can set at runtime: `SSPI` and `GSSAPI`.
	The default value for the client-side plugin option uses Security Support Provider Interface (SSPI), which is capable of acquiring credentials from the Windows in-memory cache. Alternatively, the client user can select a mode that supports Generic Security Service Application Program Interface (GSSAPI) through the MIT Kerberos library on Windows. GSSAPI is capable of acquiring cached credentials previously generated by using the **kinit** command.
	For more information, see [Commands for Windows Clients in GSSAPI Mode](kerberos-pluggable-authentication.md).
- ``--plugin-dir=*`dir_name`*``
	| Command-Line Format | `--plugin-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The directory in which to look for plugins. Specify this option if the `--default-auth` option is used to specify an authentication plugin but **mysqldump** does not find it. See [Section 8.2.17, “Pluggable Authentication”](pluggable-authentication.md).
- ``--port=*`port_num`*``, ``-P *`port_num`*``
	| Command-Line Format | `--port=port_num` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `3306` |
	For TCP/IP connections, the port number to use.
- `--protocol={TCP|SOCKET|PIPE|MEMORY}`
	| Command-Line Format | `--protocol=type` |
	| --- | --- |
	| Type | String |
	| Default Value | `[see text]` |
	| Valid Values | `TCP`  `SOCKET`  `PIPE`  `MEMORY` |
	The transport protocol to use for connecting to the server. It is useful when the other connection parameters normally result in use of a protocol other than the one you want. For details on the permissible values, see [Section 6.2.7, “Connection Transport Protocols”](transport-protocols.md).
- ``--server-public-key-path=*`file_name`*``
	| Command-Line Format | `--server-public-key-path=file_name` |
	| --- | --- |
	| Type | File name |
	The path name to a file in PEM format containing a client-side copy of the public key required by the server for RSA key pair-based password exchange. This option applies to clients that authenticate with the `sha256_password` (deprecated) or `caching_sha2_password` authentication plugin. This option is ignored for accounts that do not authenticate with one of those plugins. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection.
	If ``--server-public-key-path=*`file_name`*`` is given and specifies a valid public key file, it takes precedence over `--get-server-public-key`.
	For `sha256_password` (deprecated), this option applies only if MySQL was built using OpenSSL.
	For information about the `sha256_password` and `caching_sha2_password` plugins, see [Section 8.4.1.3, “SHA-256 Pluggable Authentication”](sha256-pluggable-authentication.md), and [Section 8.4.1.2, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).
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
	When specified, the name is passed to the `libmysqlclient` C API library using the `MYSQL_OPT_TLS_SNI_SERVERNAME` option of [`mysql_options()`](https://docs.oracle.com/cd/E17952_01/c-api-8.4-en/mysql-options.html). The server name is not case-sensitive. To show which server name the client specified for the current session, if any, check the [`Tls_sni_server_name`](server-status-variables.md) status variable.
	Server Name Indication (SNI) is an extension to the TLS protocol (OpenSSL must be compiled using TLS extensions for this option to function). The MySQL implementation of SNI represents the client-side only.
- ``--tls-version=*`protocol_list`*``
	| Command-Line Format | `--tls-version=protocol_list` |
	| --- | --- |
	| Type | String |
	| Default Value | `TLSv1,TLSv1.1,TLSv1.2,TLSv1.3` (OpenSSL 1.1.1 or higher)  `TLSv1,TLSv1.1,TLSv1.2` (otherwise) |
	The permissible TLS protocols for encrypted connections. The value is a list of one or more comma-separated protocol names. The protocols that can be named for this option depend on the SSL library used to compile MySQL. For details, see [Section 8.3.2, “Encrypted Connection TLS Protocols and Ciphers”](encrypted-connection-protocols-ciphers.md).
- ``--user=*`user_name`*``, ``-u *`user_name`*``
	| Command-Line Format | `--user=user_name` |
	| --- | --- |
	| Type | String |
	The user name of the MySQL account to use for connecting to the server.
	If you are using the `Rewriter` plugin, you should grant this user the [`SKIP_QUERY_REWRITE`](privileges-provided.md) privilege.
- ``--zstd-compression-level=*`level`*``
	| Command-Line Format | `--zstd-compression-level=#` |
	| --- | --- |
	| Type | Integer |
	The compression level to use for connections to the server that use the `zstd` compression algorithm. The permitted levels are from 1 to 22, with larger values indicating increasing levels of compression. The default `zstd` compression level is 3. The compression level setting has no effect on connections that do not use `zstd` compression.
	For more information, see [Section 6.2.8, “Connection Compression Control”](connection-compression-control.md).

#### Option-File Options

These options are used to control which option files to read.

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
	Read not only the usual option groups, but also groups with the usual names and a suffix of *`str`*. For example, **mysqldump** normally reads the `[client]` and `[mysqldump]` groups. If this option is given as `--defaults-group-suffix=_other`, **mysqldump** also reads the `[client_other]` and `[mysqldump_other]` groups.
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read any option files. If program startup fails due to reading unknown options from an option file, `--no-defaults` can be used to prevent them from being read.
	The exception is that the `.mylogin.cnf` file is read in all cases, if it exists. This permits passwords to be specified in a safer way than on the command line even when `--no-defaults` is used. To create `.mylogin.cnf`, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 6.6.7, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print the program name and all options that it gets from option files.
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).

#### DDL Options

Usage scenarios for **mysqldump** include setting up an entire new MySQL instance (including database tables), and replacing data inside an existing instance with existing databases and tables. The following options let you specify which things to tear down and set up when restoring a dump, by encoding various DDL statements within the dump file.

- `--add-drop-database`
	| Command-Line Format | `--add-drop-database` |
	| --- | --- |
	Write a [`DROP DATABASE`](drop-database.md) statement before each [`CREATE             DATABASE`](create-database.md) statement. This option is typically used in conjunction with the `--all-databases` or `--databases` option because no [`CREATE DATABASE`](create-database.md) statements are written unless one of those options is specified.
	Note
	In MySQL 8.4, the `mysql` schema is considered a system schema that cannot be dropped by end users. If `--add-drop-database` is used with `--all-databases` or with `--databases` where the list of schemas to be dumped includes `mysql`, the dump file contains a `` DROP DATABASE `mysql` `` statement that causes an error when the dump file is reloaded.
	Instead, to use `--add-drop-database`, use `--databases` with a list of schemas to be dumped, where the list does not include `mysql`.
- `--add-drop-table`
	| Command-Line Format | `--add-drop-table` |
	| --- | --- |
	Write a [`DROP TABLE`](drop-table.md) statement before each [`CREATE TABLE`](create-table.md) statement.
- `--add-drop-trigger`
	| Command-Line Format | `--add-drop-trigger` |
	| --- | --- |
	Write a [`DROP TRIGGER`](drop-trigger.md) statement before each [`CREATE             TRIGGER`](create-trigger.md) statement.
- `--all-tablespaces`, `-Y`
	| Command-Line Format | `--all-tablespaces` |
	| --- | --- |
	Adds to a table dump all SQL statements needed to create any tablespaces used by an [`NDB`](mysql-cluster.md) table. This information is not otherwise included in the output from **mysqldump**. This option is currently relevant only to NDB Cluster tables.
- `--no-create-db`, `-n`
	| Command-Line Format | `--no-create-db` |
	| --- | --- |
	Suppress the [`CREATE DATABASE`](create-database.md) statements that are otherwise included in the output if the `--databases` or `--all-databases` option is given.
- `--no-create-info`, `-t`
	| Command-Line Format | `--no-create-info` |
	| --- | --- |
	Do not write [`CREATE TABLE`](create-table.md) statements that create each dumped table.
	Note
	This option does *not* exclude statements creating log file groups or tablespaces from **mysqldump** output; however, you can use the `--no-tablespaces` option for this purpose.
- `--no-tablespaces`, `-y`
	| Command-Line Format | `--no-tablespaces` |
	| --- | --- |
	This option suppresses all [`CREATE             LOGFILE GROUP`](create-logfile-group.md) and [`CREATE             TABLESPACE`](create-tablespace.md) statements in the output of **mysqldump**.
- `--replace`
	| Command-Line Format | `--replace` |
	| --- | --- |
	Write [`REPLACE`](replace.md) statements rather than [`INSERT`](insert.md) statements.

#### Debug Options

The following options print debugging information, encode debugging information in the dump file, or let the dump operation proceed regardless of potential problems.

- `--allow-keywords`
	| Command-Line Format | `--allow-keywords` |
	| --- | --- |
	Permit creation of column names that are keywords. This works by prefixing each column name with the table name.
- `--comments`, `-i`
	| Command-Line Format | `--comments` |
	| --- | --- |
	Write additional information in the dump file such as program version, server version, and host. This option is enabled by default. To suppress this additional information, use `--skip-comments`.
- [``--debug[=*`debug_options`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/mysqldump.html#option_mysqldump_debug), ``-#             [*`debug_options`*]``
	| Command-Line Format | `--debug[=debug_options]` |
	| --- | --- |
	| Type | String |
	| Default Value | `d:t:o,/tmp/mysqldump.trace` |
	Write a debugging log. A typical *`debug_options`* string is ``d:t:o,*`file_name`*``. The default value is `d:t:o,/tmp/mysqldump.trace`.
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
- `--dump-date`
	| Command-Line Format | `--dump-date` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `TRUE` |
	If the `--comments` option is given, **mysqldump** produces a comment at the end of the dump of the following form:
	```
	-- Dump completed on DATE
	```
	However, the date causes dump files taken at different times to appear to be different, even if the data are otherwise identical. `--dump-date` and `--skip-dump-date` control whether the date is added to the comment. The default is `--dump-date` (include the date in the comment). `--skip-dump-date` suppresses date printing.
- `--force`, `-f`
	| Command-Line Format | `--force` |
	| --- | --- |
	Ignore all errors; continue even if an SQL error occurs during a table dump.
	One use for this option is to cause **mysqldump** to continue executing even when it encounters a view that has become invalid because the definition refers to a table that has been dropped. Without `--force`, **mysqldump** exits with an error message. With `--force`, **mysqldump** prints the error message, but it also writes an SQL comment containing the view definition to the dump output and continues executing.
	If the `--ignore-error` option is also given to ignore specific errors, `--force` takes precedence.
- ``--log-error=*`file_name`*``
	| Command-Line Format | `--log-error=file_name` |
	| --- | --- |
	| Type | File name |
	Log warnings and errors by appending them to the named file. The default is to do no logging.
- `--skip-comments`
	| Command-Line Format | `--skip-comments` |
	| --- | --- |
	See the description for the `--comments` option.
- `--verbose`, `-v`
	| Command-Line Format | `--verbose` |
	| --- | --- |
	Verbose mode. Print more information about what the program does.

#### Help Options

The following options display information about the **mysqldump** command itself.

- `--help`, `-?`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display a help message and exit.
- `--version`, `-V`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.

#### Internationalization Options

The following options change how the **mysqldump** command represents character data with national language settings.

- ``--character-sets-dir=*`dir_name`*``
	| Command-Line Format | `--character-sets-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The directory where character sets are installed. See [Section 12.15, “Character Set Configuration”](charset-configuration.md).
- ``--default-character-set=*`charset_name`*``
	| Command-Line Format | `--default-character-set=charset_name` |
	| --- | --- |
	| Type | String |
	| Default Value | `utf8` |
	Use *`charset_name`* as the default character set. See [Section 12.15, “Character Set Configuration”](charset-configuration.md). If no character set is specified, **mysqldump** uses `utf8mb4`.
- `--no-set-names`, `-N`
	| Command-Line Format | `--no-set-names` |
	| --- | --- |
	| Deprecated | Yes |
	Turns off the `--set-charset` setting, the same as specifying `--skip-set-charset`.
- `--set-charset`
	| Command-Line Format | `--set-charset` |
	| --- | --- |
	| Disabled by | `skip-set-charset` |
	Write [``SET NAMES             *`default_character_set`*``](set-names.md) to the output. This option is enabled by default. To suppress the [`SET NAMES`](set-names.md) statement, use `--skip-set-charset`.

#### Replication Options

The **mysqldump** command is frequently used to create an empty instance, or an instance including data, on a replica server in a replication configuration. The following options apply to dumping and restoring data on replication source servers and replicas.

- `--apply-replica-statements`
	| Command-Line Format | `--apply-replica-statements` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	For a replica dump produced with the `--dump-replica` option, this option adds a [`STOP             REPLICA`](stop-replica.md) statement before the statement with the binary log coordinates, and a [`START             REPLICA`](start-replica.md) statement at the end of the output.
- `--apply-slave-statements`
	| Command-Line Format | `--apply-slave-statements` |
	| --- | --- |
	| Deprecated | Yes |
	| Type | Boolean |
	| Default Value | `FALSE` |
	This is a deprecated alias for `--apply-replica-statements`.
- `--delete-source-logs`
	| Command-Line Format | `--delete-source-logs` |
	| --- | --- |
	On a replication source server, delete the binary logs by sending a [`PURGE BINARY LOGS`](purge-binary-logs.md) statement to the server after performing the dump operation. The options require the [`RELOAD`](privileges-provided.md) privilege as well as privileges sufficient to execute that statement. This option automatically enables `--source-data`.
- `--delete-master-logs`
	| Command-Line Format | `--delete-master-logs` |
	| --- | --- |
	| Deprecated | Yes |
	This is a deprecated alias for `--delete-source-logs`.
- [``--dump-replica[=*`value`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/mysqldump.html#option_mysqldump_dump-replica)
	| Command-Line Format | `--dump-replica[=value]` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `1` |
	| Valid Values | `1`  `2` |
	This option is similar to `--source-data`, except that it is used to dump a replica server to produce a dump file that can be used to set up another server as a replica that has the same source as the dumped server. The option causes the dump output to include a [`CHANGE             REPLICATION SOURCE TO`](change-replication-source-to.md) statement that indicates the binary log coordinates (file name and position) of the dumped replica's source. The [`CHANGE REPLICATION SOURCE TO`](change-replication-source-to.md) statement reads the values of `Relay_Master_Log_File` and `Exec_Master_Log_Pos` from the [`SHOW             REPLICA STATUS`](show-replica-status.md) output and uses them for `SOURCE_LOG_FILE` and `SOURCE_LOG_POS` respectively. These are the replication source server coordinates from which the replica starts replicating.
	Note
	Inconsistencies in the sequence of transactions from the relay log which have been executed can cause the wrong position to be used. See [Section 19.5.1.34, “Replication and Transaction Inconsistencies”](replication-features-transaction-inconsistencies.md) for more information.
	`--dump-replica` causes the coordinates from the source to be used rather than those of the dumped server, as is done by the `--source-data` option. In addition, specifying this option overrides the `--source-data` option.
	Warning
	`--dump-replica` should not be used if the server where the dump is going to be applied uses [`gtid_mode=ON`](replication-options-gtids.md) and `SOURCE_AUTO_POSITION=1`.
	The option value is handled the same way as for `--source-data`. Setting no value or 1 causes a [`CHANGE REPLICATION             SOURCE TO`](change-replication-source-to.md) statement to be written to the dump. Setting 2 causes the statement to be written but encased in SQL comments. It has the same effect as `--source-data` in terms of enabling or disabling other options and in how locking is handled.
	`--dump-replica` causes **mysqldump** to stop the replication SQL thread before the dump and restart it again after.
	`--dump-replica` sends a [`SHOW             REPLICA STATUS`](show-replica-status.md) statement to the server to obtain information, so they require privileges sufficient to execute that statement.
	`--apply-replica-statements` and `--include-source-host-port` options can be used in conjunction with `--dump-replica`.
- [``--dump-slave[=*`value`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/mysqldump.html#option_mysqldump_dump-slave)
	| Command-Line Format | `--dump-slave[=value]` |
	| --- | --- |
	| Deprecated | Yes |
	| Type | Numeric |
	| Default Value | `1` |
	| Valid Values | `1`  `2` |
	This is a deprecated alias for `--dump-replica`.
- `--include-source-host-port`
	| Command-Line Format | `--include-source-host-port` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Adds the `SOURCE_HOST` and `SOURCE_PORT` options for the host name and TCP/IP port number of the replica's source, to the [`CHANGE REPLICATION SOURCE TO`](change-replication-source-to.md) statement in a replica dump produced with the `--dump-replica` option.
- `--include-master-host-port`
	| Command-Line Format | `--include-master-host-port` |
	| --- | --- |
	| Deprecated | Yes |
	| Type | Boolean |
	| Default Value | `FALSE` |
	This is a deprecated alias for `--include-source-host-port`.
- [``--master-data[=*`value`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/mysqldump.html#option_mysqldump_master-data)
	| Command-Line Format | `--master-data[=value]` |
	| --- | --- |
	| Deprecated | Yes |
	| Type | Numeric |
	| Default Value | `1` |
	| Valid Values | `1`  `2` |
	This is a deprecated alias for `--source-data`.
- ``--output-as-version=*`value`*``
	| Command-Line Format | `--output-as-version=value` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `SERVER` |
	| Valid Values | `BEFORE_8_0_23`  `BEFORE_8_2_0` |
	Determines the level of terminology used for statements relating to replicas and events, making it possible to create dumps compatible with older versions of MySQL that do not accept the newer terminology. This option can take any one of the following values, with effects described as listed here:
	- `SERVER`: Reads the server version and uses the latest versions of statements compatible with that version. This is the default value.
	- `BEFORE_8_0_23`: Replication SQL statements using deprecated terms such as “slave” and “master” are written to the output in place of those using “replica” and “source”, as in MySQL versions prior to 8.0.23.
		This option also duplicates the effects of `BEFORE_8_2_0` on the output of [`SHOW CREATE EVENT`](show-create-event.md).
	- `BEFORE_8_2_0`: This option causes [`SHOW CREATE EVENT`](show-create-event.md) to reflect how the event would have been created in a MySQL server prior to version 8.2.0, displaying `DISABLE ON SLAVE` rather than `DISABLE ON REPLICA`.
	This option affects the output from `--events`, `--dump-replica`, `--source-data`, `--apply-replica-statements`, and `--include-source-host-port`.
- [``--source-data[=*`value`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/mysqldump.html#option_mysqldump_source-data)
	| Command-Line Format | `--source-data[=value]` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `1` |
	| Valid Values | `1`  `2` |
	Used to dump a replication source server to produce a dump file that can be used to set up another server as a replica of the source. The options cause the dump output to include a [`CHANGE REPLICATION SOURCE             TO`](change-replication-source-to.md) statement that indicates the binary log coordinates (file name and position) of the dumped server. These are the replication source server coordinates from which the replica should start replicating after you load the dump file into the replica.
	If the option value is 2, the [`CHANGE             REPLICATION SOURCE TO`](change-replication-source-to.md) statement is written as an SQL comment, and thus is informative only; it has no effect when the dump file is reloaded. If the option value is 1, the statement is not written as a comment and takes effect when the dump file is reloaded. If no option value is specified, the default value is 1.
	`--source-data` sends a [`SHOW BINARY LOG STATUS`](show-binary-log-status.md) statement to the server to obtain information, so they require privileges sufficient to execute that statement. This option also requires the [`RELOAD`](privileges-provided.md) privilege and the binary log must be enabled.
	`--source-data` automatically turns off `--lock-tables`. They also turn on `--lock-all-tables`, unless `--single-transaction` also is specified, in which case, a global read lock is acquired only for a short time at the beginning of the dump (see the description for `--single-transaction`). In all cases, any action on logs happens at the exact moment of the dump.
	It is also possible to set up a replica by dumping an existing replica of the source, using the `--dump-replica` option, which overrides `--source-data` causing it to be ignored.
- ``--set-gtid-purged=*`value`*``
	| Command-Line Format | `--set-gtid-purged=value` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `AUTO` |
	| Valid Values | `OFF`  `ON`  `AUTO` |
	This option is for servers that use GTID-based replication ([`gtid_mode=ON`](replication-options-gtids.md)). It controls the inclusion of a `SET             @@GLOBAL.gtid_purged` statement in the dump output, which updates the value of [`gtid_purged`](replication-options-gtids.md) on a server where the dump file is reloaded, to add the GTID set from the source server's [`gtid_executed`](replication-options-gtids.md) system variable. [`gtid_purged`](replication-options-gtids.md) holds the GTIDs of all transactions that have been applied on the server, but do not exist on any binary log file on the server. **mysqldump** therefore adds the GTIDs for the transactions that were executed on the source server, so that the target server records these transactions as applied, although it does not have them in its binary logs. `--set-gtid-purged` also controls the inclusion of a `SET             @@SESSION.sql_log_bin=0` statement, which disables binary logging while the dump file is being reloaded. This statement prevents new GTIDs from being generated and assigned to the transactions in the dump file as they are executed, so that the original GTIDs for the transactions are used.
	If you do not set the `--set-gtid-purged` option, the default is that a `SET             @@GLOBAL.gtid_purged` statement is included in the dump output if GTIDs are enabled on the server you are backing up, and the set of GTIDs in the global value of the [`gtid_executed`](replication-options-gtids.md) system variable is not empty. A `SET             @@SESSION.sql_log_bin=0` statement is also included if GTIDs are enabled on the server.
	You can either replace the value of [`gtid_purged`](replication-options-gtids.md) with a specified GTID set, or add a plus sign (+) to the statement to append a specified GTID set to the GTID set that is already held by `gtid_purged`. The `SET @@GLOBAL.gtid_purged` statement recorded by **mysqldump** includes a plus sign (`+`) in a version-specific comment, such that MySQL adds the GTID set from the dump file to the existing `gtid_purged` value.
	It is important to note that the value that is included by **mysqldump** for the `SET             @@GLOBAL.gtid_purged` statement includes the GTIDs of all transactions in the [`gtid_executed`](replication-options-gtids.md) set on the server, even those that changed suppressed parts of the database, or other databases on the server that were not included in a partial dump. This can mean that after the [`gtid_purged`](replication-options-gtids.md) value has been updated on the server where the dump file is replayed, GTIDs are present that do not relate to any data on the target server. If you do not replay any further dump files on the target server, the extraneous GTIDs do not cause any problems with the future operation of the server, but they make it harder to compare or reconcile GTID sets on different servers in the replication topology. If you do replay a further dump file on the target server that contains the same GTIDs (for example, another partial dump from the same origin server), any `SET             @@GLOBAL.gtid_purged` statement in the second dump file fails. In this case, either remove the statement manually before replaying the dump file, or output the dump file without the statement.
	If the `SET @@GLOBAL.gtid_purged` statement would not have the desired result on your target server, you can exclude the statement from the output, or include it but comment it out so that it is not actioned automatically. You can also include the statement but manually edit it in the dump file to achieve the desired result.
	The possible values for the `--set-gtid-purged` option are as follows:
	`AUTO`
	The default value. If GTIDs are enabled on the server you are backing up and [`gtid_executed`](replication-options-gtids.md) is not empty, `SET @@GLOBAL.gtid_purged` is added to the output, containing the GTID set from [`gtid_executed`](replication-options-gtids.md). If GTIDs are enabled, `SET                   @@SESSION.sql_log_bin=0` is added to the output. If GTIDs are not enabled on the server, the statements are not added to the output.
	`OFF`
	`SET @@GLOBAL.gtid_purged` is not added to the output, and `SET                   @@SESSION.sql_log_bin=0` is not added to the output. For a server where GTIDs are not in use, use this option or `AUTO`. Only use this option for a server where GTIDs are in use if you are sure that the required GTID set is already present in [`gtid_purged`](replication-options-gtids.md) on the target server and should not be changed, or if you plan to identify and add any missing GTIDs manually.
	`ON`
	If GTIDs are enabled on the server you are backing up, `SET @@GLOBAL.gtid_purged` is added to the output (unless [`gtid_executed`](replication-options-gtids.md) is empty), and `SET                   @@SESSION.sql_log_bin=0` is added to the output. An error occurs if you set this option but GTIDs are not enabled on the server. For a server where GTIDs are in use, use this option or `AUTO`, unless you are sure that the GTIDs in [`gtid_executed`](replication-options-gtids.md) are not needed on the target server.
	`COMMENTED`
	If GTIDs are enabled on the server you are backing up, `SET @@GLOBAL.gtid_purged` is added to the output (unless [`gtid_executed`](replication-options-gtids.md) is empty), but it is commented out. This means that the value of [`gtid_executed`](replication-options-gtids.md) is available in the output, but no action is taken automatically when the dump file is reloaded. `SET @@SESSION.sql_log_bin=0` is added to the output, and it is not commented out. With `COMMENTED`, you can control the use of the [`gtid_executed`](replication-options-gtids.md) set manually or through automation. For example, you might prefer to do this if you are migrating data to another server that already has different active databases.

#### Format Options

The following options specify how to represent the entire dump file or certain kinds of data in the dump file. They also control whether certain optional information is written to the dump file.

- `--compact`
	| Command-Line Format | `--compact` |
	| --- | --- |
	Produce more compact output. This option enables the `--skip-add-drop-table`, `--skip-add-locks`, `--skip-comments`, `--skip-disable-keys`, and `--skip-set-charset` options.
- ``--compatible=*`name`*``
	| Command-Line Format | `--compatible=name[,name,...]` |
	| --- | --- |
	| Type | String |
	| Default Value | `''` |
	| Valid Values | `ansi` |
	Produce output that is more compatible with other database systems or with older MySQL servers. The only permitted value for this option is `ansi`, which has the same meaning as the corresponding option for setting the server SQL mode. See [Section 7.1.11, “Server SQL Modes”](sql-mode.md).
- `--complete-insert`, `-c`
	| Command-Line Format | `--complete-insert` |
	| --- | --- |
	Use complete [`INSERT`](insert.md) statements that include column names.
- `--create-options`
	| Command-Line Format | `--create-options` |
	| --- | --- |
	Include all MySQL-specific table options in the [`CREATE TABLE`](create-table.md) statements.
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
	These options are used with the `--tab` option and have the same meaning as the corresponding `FIELDS` clauses for [`LOAD DATA`](load-data.md). See [Section 15.2.9, “LOAD DATA Statement”](load-data.md).
- `--hex-blob`
	| Command-Line Format | `--hex-blob` |
	| --- | --- |
	Dump binary columns using hexadecimal notation (for example, `'abc'` becomes `0x616263`). The affected data types are [`BINARY`](binary-varbinary.md), [`VARBINARY`](binary-varbinary.md), [`BLOB`](blob.md) types, [`BIT`](bit-type.md), all spatial data types, and other non-binary data types when used with the [`binary` character set](charset-binary-set.md).
	The `--hex-blob` option is ignored when the `--tab` is used.
- `--lines-terminated-by=...`
	| Command-Line Format | `--lines-terminated-by=string` |
	| --- | --- |
	| Type | String |
	This option is used with the `--tab` option and has the same meaning as the corresponding `LINES` clause for [`LOAD DATA`](load-data.md). See [Section 15.2.9, “LOAD DATA Statement”](load-data.md).
- `--quote-names`, `-Q`
	| Command-Line Format | `--quote-names` |
	| --- | --- |
	| Disabled by | `skip-quote-names` |
	Quote identifiers (such as database, table, and column names) within `` ` `` characters. If the [`ANSI_QUOTES`](sql-mode.md) SQL mode is enabled, identifiers are quoted within `"` characters. This option is enabled by default. It can be disabled with `--skip-quote-names`, but this option should be given after any option such as `--compatible` that may enable `--quote-names`.
- ``--result-file=*`file_name`*``, ``-r *`file_name`*``
	| Command-Line Format | `--result-file=file_name` |
	| --- | --- |
	| Type | File name |
	Direct output to the named file. The result file is created and its previous contents overwritten, even if an error occurs while generating the dump.
	This option should be used on Windows to prevent newline `\n` characters from being converted to `\r\n` carriage return/newline sequences.
- ``--show-create-skip-secondary-engine=*`value`*``
	| Command-Line Format | `--show-create-skip-secondary-engine` |
	| --- | --- |
	Excludes the `SECONDARY ENGINE` clause from [`CREATE TABLE`](create-table.md) statements. It does so by enabling the [`show_create_table_skip_secondary_engine`](https://dev.mysql.com/doc/heatwave/en/heatwave-system-variables.html#sysvar_show_create_table_skip_secondary_engine) system variable for the duration of the dump operation. Alternatively, you can enable the [`show_create_table_skip_secondary_engine`](https://dev.mysql.com/doc/heatwave/en/heatwave-system-variables.html#sysvar_show_create_table_skip_secondary_engine) system variable prior to using **mysqldump**.
- ``--tab=*`dir_name`*``, ``-T *`dir_name`*``
	| Command-Line Format | `--tab=dir_name` |
	| --- | --- |
	| Type | Directory name |
	Produce tab-separated text-format data files. For each dumped table, **mysqldump** creates a ``*`tbl_name`*.sql`` file that contains the [`CREATE             TABLE`](create-table.md) statement that creates the table, and the server writes a ``*`tbl_name`*.txt`` file that contains its data. The option value is the directory in which to write the files.
	Note
	This option should be used only when **mysqldump** is run on the same machine as the [**mysqld**](mysqld.md) server. Because the server creates `*.txt` files in the directory that you specify, the directory must be writable by the server and the MySQL account that you use must have the [`FILE`](privileges-provided.md) privilege. Because **mysqldump** creates `*.sql` in the same directory, it must be writable by your system login account.
	By default, the `.txt` data files are formatted using tab characters between column values and a newline at the end of each line. The format can be specified explicitly using the ``--fields-*`xxx`*`` and `--lines-terminated-by` options.
	Column values are converted to the character set specified by the `--default-character-set` option.
- `--tz-utc`
	| Command-Line Format | `--tz-utc` |
	| --- | --- |
	| Disabled by | `skip-tz-utc` |
	This option enables [`TIMESTAMP`](datetime.md) columns to be dumped and reloaded between servers in different time zones. **mysqldump** sets its connection time zone to UTC and adds `SET             TIME_ZONE='+00:00'` to the dump file. Without this option, [`TIMESTAMP`](datetime.md) columns are dumped and reloaded in the time zones local to the source and destination servers, which can cause the values to change if the servers are in different time zones. `--tz-utc` also protects against changes due to daylight saving time. `--tz-utc` is enabled by default. To disable it, use `--skip-tz-utc`.
- `--xml`, `-X`
	| Command-Line Format | `--xml` |
	| --- | --- |
	Write dump output as well-formed XML.
	**`NULL`, `'NULL'`, and Empty Values**: For a column named *`column_name`*, the `NULL` value, an empty string, and the string value `'NULL'` are distinguished from one another in the output generated by this option as follows.
	| Value: | XML Representation: |
	| --- | --- |
	| `NULL` (*unknown value*) | ``<field                     name="*`column_name`*"                     xsi:nil="true" />`` |
	| `''` (*empty string*) | ``<field                     name="*`column_name`*"></field>`` |
	| `'NULL'` (*string value*) | ``<field                     name="*`column_name`*">NULL</field>`` |
	The output from the [**mysql**](mysql.md) client when run using the [`--xml`](mysql-command-options.md) option also follows the preceding rules. (See [Section 6.5.1.1, “mysql Client Options”](mysql-command-options.md).)
	XML output from **mysqldump** includes the XML namespace, as shown here:
	```
	$> mysqldump --xml -u root world City
	<?xml version="1.0"?>
	<mysqldump xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<database name="world">
	<table_structure name="City">
	<field Field="ID" Type="int(11)" Null="NO" Key="PRI" Extra="auto_increment" />
	<field Field="Name" Type="char(35)" Null="NO" Key="" Default="" Extra="" />
	<field Field="CountryCode" Type="char(3)" Null="NO" Key="" Default="" Extra="" />
	<field Field="District" Type="char(20)" Null="NO" Key="" Default="" Extra="" />
	<field Field="Population" Type="int(11)" Null="NO" Key="" Default="0" Extra="" />
	<key Table="City" Non_unique="0" Key_name="PRIMARY" Seq_in_index="1" Column_name="ID"
	Collation="A" Cardinality="4079" Null="" Index_type="BTREE" Comment="" />
	<options Name="City" Engine="MyISAM" Version="10" Row_format="Fixed" Rows="4079"
	Avg_row_length="67" Data_length="273293" Max_data_length="18858823439613951"
	Index_length="43008" Data_free="0" Auto_increment="4080"
	Create_time="2007-03-31 01:47:01" Update_time="2007-03-31 01:47:02"
	Collation="latin1_swedish_ci" Create_options="" Comment="" />
	</table_structure>
	<table_data name="City">
	<row>
	<field name="ID">1</field>
	<field name="Name">Kabul</field>
	<field name="CountryCode">AFG</field>
	<field name="District">Kabol</field>
	<field name="Population">1780000</field>
	</row>
	...
	<row>
	<field name="ID">4079</field>
	<field name="Name">Rafah</field>
	<field name="CountryCode">PSE</field>
	<field name="District">Rafah</field>
	<field name="Population">92020</field>
	</row>
	</table_data>
	</database>
	</mysqldump>
	```

#### Filtering Options

The following options control which kinds of schema objects are written to the dump file: by category, such as triggers or events; by name, for example, choosing which databases and tables to dump; or even filtering rows from the table data using a `WHERE` clause.

- `--all-databases`, `-A`
	| Command-Line Format | `--all-databases` |
	| --- | --- |
	Dump all tables in all databases. This is the same as using the `--databases` option and naming all the databases on the command line.
	Note
	See the `--add-drop-database` description for information about an incompatibility of that option with `--all-databases`.
	Prior to MySQL 8.4, the `--routines` and `--events` options for **mysqldump** were not required to include stored routines and events when using the `--all-databases` option: The dump included the `mysql` system database, and therefore also the `mysql.proc` and `mysql.event` tables containing stored routine and event definitions. As of MySQL 8.4, the `mysql.event` and `mysql.proc` tables are not used. Definitions for the corresponding objects are stored in data dictionary tables, but those tables are not dumped. To include stored routines and events in a dump made using `--all-databases`, use the `--routines` and `--events` options explicitly.
- `--databases`, `-B`
	| Command-Line Format | `--databases` |
	| --- | --- |
	Dump several databases. Normally, **mysqldump** treats the first name argument on the command line as a database name and following names as table names. With this option, it treats all name arguments as database names. [`CREATE             DATABASE`](create-database.md) and [`USE`](use.md) statements are included in the output before each new database.
	This option may be used to dump the `performance_schema` database, which normally is not dumped even with the `--all-databases` option. (Also use the `--skip-lock-tables` option.)
	Note
	See the `--add-drop-database` description for information about an incompatibility of that option with `--databases`.
- `--events`, `-E`
	| Command-Line Format | `--events` |
	| --- | --- |
	Include Event Scheduler events for the dumped databases in the output. This option requires the [`EVENT`](privileges-provided.md) privileges for those databases.
	The output generated by using `--events` contains [`CREATE EVENT`](create-event.md) statements to create the events.
- [``--ignore-error=*`error[,error]...`*``](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/mysqldump.html#option_mysqldump_ignore-error)
	| Command-Line Format | `--ignore-error=error[,error]...` |
	| --- | --- |
	| Type | String |
	Ignore the specified errors. The option value is a list of comma-separated error numbers specifying the errors to ignore during **mysqldump** execution. If the `--force` option is also given to ignore all errors, `--force` takes precedence.
- ``--ignore-table=*`db_name.tbl_name`*``
	| Command-Line Format | `--ignore-table=db_name.tbl_name` |
	| --- | --- |
	| Type | String |
	Do not dump the given table, which must be specified using both the database and table names. To ignore multiple tables, use this option multiple times. This option also can be used to ignore views.
- ``--ignore-views=*`boolean`*``
	| Command-Line Format | `--ignore-views` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Skips table views in the dump file.
- ``--init-command=*`str`*``
	| Command-Line Format | `--init-command=str` |
	| --- | --- |
	| Type | String |
	Single SQL statement to execute after connecting to the MySQL server. The definition resets existing statements defined by it or `init-command-add`.
- ``--init-command-add=*`str`*``
	| Command-Line Format | `--init-command-add=str` |
	| --- | --- |
	| Type | String |
	Add an additional SQL statement to execute after connecting or reconnecting to the MySQL server. It's usable without `--init-command` but has no effect if used before it because `init-command` resets the list of commands to call.
- `--no-data`, `-d`
	| Command-Line Format | `--no-data` |
	| --- | --- |
	Do not write any table row information (that is, do not dump table contents). This is useful if you want to dump only the [`CREATE TABLE`](create-table.md) statement for the table (for example, to create an empty copy of the table by loading the dump file).
- `--routines`, `-R`
	| Command-Line Format | `--routines` |
	| --- | --- |
	Include stored routines (procedures and functions) for the dumped databases in the output. This option requires the global [`SELECT`](privileges-provided.md) privilege.
	The output generated by using `--routines` contains [`CREATE PROCEDURE`](create-procedure.md) and [`CREATE FUNCTION`](create-function.md) statements to create the routines.
- `--skip-generated-invisible-primary-key`
	| Command-Line Format | `--skip-generated-invisible-primary-key` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	This option causes generated invisible primary keys to be excluded from the output. For more information, see [Section 15.1.20.11, “Generated Invisible Primary Keys”](create-table-gipks.md).
- `--tables`
	| Command-Line Format | `--tables` |
	| --- | --- |
	Override the `--databases` or `-B` option. **mysqldump** regards all name arguments following the option as table names.
- `--triggers`
	| Command-Line Format | `--triggers` |
	| --- | --- |
	| Disabled by | `skip-triggers` |
	Include triggers for each dumped table in the output. This option is enabled by default; disable it with `--skip-triggers`.
	To be able to dump a table's triggers, you must have the [`TRIGGER`](privileges-provided.md) privilege for the table.
	Multiple triggers are permitted. **mysqldump** dumps triggers in activation order so that when the dump file is reloaded, triggers are created in the same activation order. However, if a **mysqldump** dump file contains multiple triggers for a table that have the same trigger event and action time, an error occurs for attempts to load the dump file into an older server that does not support multiple triggers. (For a workaround, see [Downgrade Notes](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/downgrading-to-previous-series.html); you can convert triggers to be compatible with older servers.)
- ``--where='*`where_condition`*'``, ``-w             '*`where_condition`*'``
	| Command-Line Format | `--where='where_condition'` |
	| --- | --- |
	Dump only rows selected by the given `WHERE` condition. Quotes around the condition are mandatory if it contains spaces or other characters that are special to your command interpreter.
	Examples:
	```
	--where="user='jimf'"
	-w"userid>1"
	-w"userid<1"
	```

#### Performance Options

The following options are the most relevant for the performance particularly of the restore operations. For large data sets, restore operation (processing the `INSERT` statements in the dump file) is the most time-consuming part. When it is urgent to restore data quickly, plan and test the performance of this stage in advance. For restore times measured in hours, you might prefer an alternative backup and restore solution, such as [MySQL Enterprise Backup](mysql-enterprise-backup.md) for `InnoDB` -only and mixed-use databases.

Performance is also affected by the transactional options, primarily for the dump operation.

- `--column-statistics`
	| Command-Line Format | `--column-statistics` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	Add [`ANALYZE TABLE`](analyze-table.md) statements to the output to generate histogram statistics for dumped tables when the dump file is reloaded. This option is disabled by default because histogram generation for large tables can take a long time.
- `--disable-keys`, `-K`
	| Command-Line Format | `--disable-keys` |
	| --- | --- |
	For each table, surround the [`INSERT`](insert.md) statements with ``/*!40000 ALTER TABLE             *`tbl_name`* DISABLE KEYS             */;`` and ``/*!40000 ALTER TABLE             *`tbl_name`* ENABLE KEYS             */;`` statements. This makes loading the dump file faster because the indexes are created after all rows are inserted. This option is effective only for nonunique indexes of `MyISAM` tables.
- `--extended-insert`, `-e`
	| Command-Line Format | `--extended-insert` |
	| --- | --- |
	| Disabled by | `skip-extended-insert` |
	Write [`INSERT`](insert.md) statements using multiple-row syntax that includes several `VALUES` lists. This results in a smaller dump file and speeds up inserts when the file is reloaded.
- `--insert-ignore`
	| Command-Line Format | `--insert-ignore` |
	| --- | --- |
	Write [`INSERT             IGNORE`](insert.md) statements rather than [`INSERT`](insert.md) statements.
- ``--max-allowed-packet=*`value`*``
	| Command-Line Format | `--max-allowed-packet=value` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `25165824` |
	The maximum size of the buffer for client/server communication. The default is 24MB, the maximum is 1GB.
	Note
	The value of this option is specific to **mysqldump** and should not be confused with the MySQL server's [`max_allowed_packet`](server-system-variables.md) system variable; the server value cannot be exceeded by a single packet from **mysqldump**, regardless of any setting for the **mysqldump** option, even if the latter is larger.
- ``--mysqld-long-query-time=*`value`*``
	| Command-Line Format | `--mysqld-long-query-time=value` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `Server global setting` |
	Set the session value of the [`long_query_time`](server-system-variables.md) system variable. Use this option if you want to increase the time allowed for queries from **mysqldump** before they are logged to the slow query log file. **mysqldump** performs a full table scan, which means its queries can often exceed a global [`long_query_time`](server-system-variables.md) setting that is useful for regular queries. The default global setting is 10 seconds.
	You can use `--mysqld-long-query-time` to specify a session value from 0 (meaning that every query from **mysqldump** is logged to the slow query log) to 31536000, which is 365 days in seconds. For **mysqldump** ’s option, you can only specify whole seconds. When you do not specify this option, the server’s global setting applies to **mysqldump** ’s queries.
- ``--net-buffer-length=*`value`*``
	| Command-Line Format | `--net-buffer-length=value` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `16384` |
	The initial size of the buffer for client/server communication. When creating multiple-row [`INSERT`](insert.md) statements (as with the `--extended-insert` or `--opt` option), **mysqldump** creates rows up to `--net-buffer-length` bytes long. If you increase this variable, ensure that the MySQL server [`net_buffer_length`](server-system-variables.md) system variable has a value at least this large.
- `--network-timeout`, `-M`
	| Command-Line Format | `--network-timeout[={0\|1}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `TRUE` |
	Enable large tables to be dumped by setting `--max-allowed-packet` to its maximum value and network read and write timeouts to a large value. This option is enabled by default. To disable it, use `--skip-network-timeout`.
- `--opt`
	| Command-Line Format | `--opt` |
	| --- | --- |
	| Disabled by | `skip-opt` |
	This option, enabled by default, is shorthand for the combination of `--add-drop-table` `--add-locks` `--create-options` `--disable-keys` `--extended-insert` `--lock-tables` `--quick` `--set-charset`. It gives a fast dump operation and produces a dump file that can be reloaded into a MySQL server quickly.
	Because the `--opt` option is enabled by default, you only specify its converse, the `--skip-opt` to turn off several default settings. See the discussion of `mysqldump` option groups for information about selectively enabling or disabling a subset of the options affected by `--opt`.
- `--quick`, `-q`
	| Command-Line Format | `--quick` |
	| --- | --- |
	| Disabled by | `skip-quick` |
	This option is useful for dumping large tables. It forces **mysqldump** to retrieve rows for a table from the server a row at a time rather than retrieving the entire row set and buffering it in memory before writing it out.
- `--skip-opt`
	| Command-Line Format | `--skip-opt` |
	| --- | --- |
	See the description for the `--opt` option.

#### Transactional Options

The following options trade off the performance of the dump operation, against the reliability and consistency of the exported data.

- `--add-locks`
	| Command-Line Format | `--add-locks` |
	| --- | --- |
	Surround each table dump with [`LOCK             TABLES`](lock-tables.md) and [`UNLOCK             TABLES`](lock-tables.md) statements. This results in faster inserts when the dump file is reloaded. See [Section 10.2.5.1, “Optimizing INSERT Statements”](insert-optimization.md).
- `--flush-logs`, `-F`
	| Command-Line Format | `--flush-logs` |
	| --- | --- |
	Flush the MySQL server log files before starting the dump. This option requires the [`RELOAD`](privileges-provided.md) privilege. If you use this option in combination with the `--all-databases` option, the logs are flushed *for each database dumped*. The exception is when using `--lock-all-tables`, `--source-data`, or `--single-transaction`. In these cases, the logs are flushed only once, corresponding to the moment that all tables are locked by [`FLUSH TABLES WITH READ LOCK`](flush.md). If you want your dump and the log flush to happen at exactly the same moment, you should use `--flush-logs` together with `--lock-all-tables`, `--source-data`, or `--single-transaction`.
- `--flush-privileges`
	| Command-Line Format | `--flush-privileges` |
	| --- | --- |
	Add a [`FLUSH PRIVILEGES`](flush.md) statement to the dump output after dumping the `mysql` database. This option should be used any time the dump contains the `mysql` database and any other database that depends on the data in the `mysql` database for proper restoration.
	Because the dump file contains a [`FLUSH             PRIVILEGES`](flush.md) statement, reloading the file requires privileges sufficient to execute that statement.
- `--lock-all-tables`, `-x`
	| Command-Line Format | `--lock-all-tables` |
	| --- | --- |
	Lock all tables across all databases. This is achieved by acquiring a global read lock for the duration of the whole dump. This option automatically turns off `--single-transaction` and `--lock-tables`.
- `--lock-tables`, `-l`
	| Command-Line Format | `--lock-tables` |
	| --- | --- |
	For each dumped database, lock all tables to be dumped before dumping them. The tables are locked with `READ LOCAL` to permit concurrent inserts in the case of `MyISAM` tables. For transactional tables such as `InnoDB`, `--single-transaction` is a much better option than `--lock-tables` because it does not need to lock the tables at all.
	Because `--lock-tables` locks tables for each database separately, this option does not guarantee that the tables in the dump file are logically consistent between databases. Tables in different databases may be dumped in completely different states.
	Some options, such as `--opt`, automatically enable `--lock-tables`. If you want to override this, use `--skip-lock-tables` at the end of the option list.
- `--no-autocommit`
	| Command-Line Format | `--no-autocommit` |
	| --- | --- |
	Enclose the [`INSERT`](insert.md) statements for each dumped table within `SET autocommit =             0` and [`COMMIT`](commit.md) statements.
- `--order-by-primary`
	| Command-Line Format | `--order-by-primary` |
	| --- | --- |
	Dump each table's rows sorted by its primary key, or by its first unique index, if such an index exists. This is useful when dumping a `MyISAM` table to be loaded into an `InnoDB` table, but makes the dump operation take considerably longer.
- ``--shared-memory-base-name=*`name`*``
	| Command-Line Format | `--shared-memory-base-name=name` |
	| --- | --- |
	| Platform Specific | Windows |
	On Windows, the shared-memory name to use for connections made using shared memory to a local server. The default value is `MYSQL`. The shared-memory name is case-sensitive.
	This option applies only if the server was started with the [`shared_memory`](server-system-variables.md) system variable enabled to support shared-memory connections.
- `--single-transaction`
	| Command-Line Format | `--single-transaction` |
	| --- | --- |
	This option sets the transaction isolation mode to [`REPEATABLE READ`](innodb-transaction-isolation-levels.md) and sends a [`START             TRANSACTION`](commit.md) SQL statement to the server before dumping data. It is useful only with transactional tables such as `InnoDB`, because then it dumps the consistent state of the database at the time when [`START             TRANSACTION`](commit.md) was issued without blocking any applications.
	The [`RELOAD`](privileges-provided.md) or [`FLUSH_TABLES`](privileges-provided.md) privilege is required with `--single-transaction` if both [`gtid_mode=ON`](replication-options-gtids.md) and [`gtid_purged=ON|AUTO`](replication-options-gtids.md).
	When using this option, you should keep in mind that only `InnoDB` tables are dumped in a consistent state. For example, any `MyISAM` or `MEMORY` tables dumped while using this option may still change state.
	While a `--single-transaction` dump is in process, to ensure a valid dump file (correct table contents and binary log coordinates), no other connection should use the following statements: [`ALTER TABLE`](alter-table.md), [`CREATE TABLE`](create-table.md), [`DROP TABLE`](drop-table.md), [`RENAME TABLE`](rename-table.md), [`TRUNCATE TABLE`](truncate-table.md). A consistent read is not isolated from those statements, so use of them on a table to be dumped can cause the [`SELECT`](select.md) that is performed by **mysqldump** to retrieve the table contents to obtain incorrect contents or fail.
	The `--single-transaction` option and the `--lock-tables` option are mutually exclusive because [`LOCK             TABLES`](lock-tables.md) causes any pending transactions to be committed implicitly.
	To dump large tables, combine the `--single-transaction` option with the `--quick` option.

#### Option Groups

- The `--opt` option turns on several settings that work together to perform a fast dump operation. All of these settings are on by default, because `--opt` is on by default. Thus you rarely if ever specify `--opt`. Instead, you can turn these settings off as a group by specifying `--skip-opt`, then optionally re-enable certain settings by specifying the associated options later on the command line.
- The `--compact` option turns off several settings that control whether optional statements and comments appear in the output. Again, you can follow this option with other options that re-enable certain settings, or turn all the settings on by using the `--skip-compact` form.

When you selectively enable or disable the effect of a group option, order is important because options are processed first to last. For example, `--disable-keys` `--lock-tables` `--skip-opt` would not have the intended effect; it is the same as `--skip-opt` by itself.

#### Examples

To make a backup of an entire database:

```
mysqldump db_name > backup-file.sql
```

To load the dump file back into the server:

```
mysql db_name < backup-file.sql
```

Another way to reload the dump file:

```
mysql -e "source /path-to-backup/backup-file.sql" db_name
```

**mysqldump** is also very useful for populating databases by copying data from one MySQL server to another:

```
mysqldump --opt db_name | mysql --host=remote_host -C db_name
```

You can dump several databases with one command:

```
mysqldump --databases db_name1 [db_name2 ...] > my_databases.sql
```

To dump all databases, use the `--all-databases` option:

```
mysqldump --all-databases > all_databases.sql
```

For `InnoDB` tables, **mysqldump** provides a way of making an online backup:

```
mysqldump --all-databases --source-data --single-transaction > all_databases.sql
```

This backup acquires a global read lock on all tables (using [`FLUSH TABLES WITH READ LOCK`](flush.md)) at the beginning of the dump. As soon as this lock has been acquired, the binary log coordinates are read and the lock is released. If long updating statements are running when the [`FLUSH`](flush.md) statement is issued, the MySQL server may get stalled until those statements finish. After that, the dump becomes lock free and does not disturb reads and writes on the tables. If the update statements that the MySQL server receives are short (in terms of execution time), the initial lock period should not be noticeable, even with many updates.

For point-in-time recovery (also known as “roll-forward,” when you need to restore an old backup and replay the changes that happened since that backup), it is often useful to rotate the binary log (see [Section 7.4.4, “The Binary Log”](binary-log.md)) or at least know the binary log coordinates to which the dump corresponds:

```
mysqldump --all-databases --source-data=2 > all_databases.sql
```

Or:

```
mysqldump --all-databases --flush-logs --source-data=2 > all_databases.sql
```

The `--source-data` option can be used simultaneously with the `--single-transaction` option, which provides a convenient way to make an online backup suitable for use prior to point-in-time recovery if tables are stored using the `InnoDB` storage engine.

For more information on making backups, see [Section 9.2, “Database Backup Methods”](backup-methods.md), and [Section 9.3, “Example Backup and Recovery Strategy”](backup-strategy-example.md).

- To select the effect of `--opt` except for some features, use the `--skip` option for each feature. To disable extended inserts and memory buffering, use `--opt` `--skip-extended-insert` `--skip-quick`. (Actually, `--skip-extended-insert` `--skip-quick` is sufficient because `--opt` is on by default.)
- To reverse `--opt` for all features except disabling of indexes and table locking, use `--skip-opt` `--disable-keys` `--lock-tables`.

#### Restrictions

**mysqldump** does not dump the `performance_schema` or `sys` schema by default. To dump any of these, name them explicitly on the command line. You can also name them with the `--databases` option. For `performance_schema`, also use the `--skip-lock-tables` option.

**mysqldump** does not dump the `INFORMATION_SCHEMA` schema.

**mysqldump** does not dump `InnoDB` [`CREATE         TABLESPACE`](create-tablespace.md) statements.

**mysqldump** does not dump the NDB Cluster [`ndbinfo`](mysql-cluster-ndbinfo.md) information database.

**mysqldump** includes statements to recreate the `general_log` and `slow_query_log` tables for dumps of the `mysql` database. Log table contents are not dumped.

If you encounter problems backing up views due to insufficient privileges, see [Section 27.9, “Restrictions on Views”](view-restrictions.md) for a workaround.