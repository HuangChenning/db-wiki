---
title: "6.6.8 mysql_migrate_keyring — Keyring Key Migration Utility"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysql-migrate-keyring.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 6.6.8 mysql\_migrate\_keyring — Keyring Key Migration Utility

The **mysql\_migrate\_keyring** utility migrates keys between one keyring component and another. It supports offline and online migrations.

Invoke **mysql\_migrate\_keyring** like this (enter the command on a single line):

```
mysql_migrate_keyring
  --component-dir=dir_name
  --source-keyring=name
  --destination-keyring=name
  [other options]
```

For information about key migrations and instructions describing how to perform them using **mysql\_migrate\_keyring** and other methods, see [Section 8.4.4.14, “Migrating Keys Between Keyring Keystores”](keyring-key-migration.md).

**mysql\_migrate\_keyring** supports the following options, which can be specified on the command line or in the `[mysql_migrate_keyring]` group of an option file. For information about option files used by MySQL programs, see [Section 6.2.2.2, “Using Option Files”](option-files.md).

**Table 6.22 mysql\_migrate\_keyring Options**

| Option Name | Description | Deprecated |
| --- | --- | --- |
| \--component-dir | Directory for keyring components |  |
| \--defaults-extra-file | Read named option file in addition to usual option files |  |
| \--defaults-file | Read only named option file |  |
| \--defaults-group-suffix | Option group suffix value |  |
| \--destination-keyring | Destination keyring component name |  |
| \--destination-keyring-configuration-dir | Destination keyring component configuration directory |  |
| \--get-server-public-key | Request RSA public key from server |  |
| \--help | Display help message and exit |  |
| \--host | Host on which MySQL server is located |  |
| \--login-path | Read login path options from.mylogin.cnf |  |
| \--no-defaults | Read no option files |  |
| \--online-migration | Migration source is an active server |  |
| \--password | Password to use when connecting to server |  |
| \--port | TCP/IP port number for connection |  |
| \--print-defaults | Print default options |  |
| \--server-public-key-path | Path name to file containing RSA public key |  |
| \--socket | Unix socket file or Windows named pipe to use |  |
| \--source-keyring | Source keyring component name |  |
| \--source-keyring-configuration-dir | Source keyring component configuration directory |  |
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
| \--user | MySQL user name to use when connecting to server |  |
| \--verbose | Verbose mode |  |
| \--version | Display version information and exit |  |

- `--help`, `-h`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display a help message and exit.
- ``--component-dir=*`dir_name`*``
	| Command-Line Format | `--component-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The directory where keyring components are located. This is typically the value of the [`plugin_dir`](server-system-variables.md) system variable for the local MySQL server.
	Note
	`--component-dir`, `--source-keyring`, and `--destination-keyring` are mandatory for all keyring migration operations performed by **mysql\_migrate\_keyring**. In addition, the source and destination components must differ, and both components must be properly configured so that **mysql\_migrate\_keyring** can load and use them.
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
	Read not only the usual option groups, but also groups with the usual names and a suffix of *`str`*. For example, **mysql\_migrate\_keyring** normally reads the `[mysql_migrate_keyring]` group. If this option is given as `--defaults-group-suffix=_other`, **mysql\_migrate\_keyring** also reads the `[mysql_migrate_keyring_other]` group.
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--destination-keyring=*`name`*``
	| Command-Line Format | `--destination-keyring=name` |
	| --- | --- |
	| Type | String |
	The destination keyring component for key migration. The format and interpretation of the option value is the same as described for the `--source-keyring` option.
	Note
	`--component-dir`, `--source-keyring`, and `--destination-keyring` are mandatory for all keyring migration operations performed by **mysql\_migrate\_keyring**. In addition, the source and destination components must differ, and both components must be properly configured so that **mysql\_migrate\_keyring** can load and use them.
- ``--destination-keyring-configuration-dir=*`dir_name`*``
	| Command-Line Format | `--destination-keyring-configuration-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	This option applies only if the destination keyring component global configuration file contains `"read_local_config": true`, indicating that component configuration is contained in the local configuration file. The option value specifies the directory containing that local file.
- `--get-server-public-key`
	| Command-Line Format | `--get-server-public-key` |
	| --- | --- |
	| Type | Boolean |
	Request from the server the public key required for RSA key pair-based password exchange. This option applies to clients that authenticate with the `caching_sha2_password` authentication plugin. For that plugin, the server does not send the public key unless requested. This option is ignored for accounts that do not authenticate with that plugin. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection.
	If ``--server-public-key-path=*`file_name`*`` is given and specifies a valid public key file, it takes precedence over `--get-server-public-key`.
	For information about the `caching_sha2_password` plugin, see [Section 8.4.1.2, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).
- ``--host=*`host_name`*``, ``-h *`host_name`*``
	| Command-Line Format | `--host=host_name` |
	| --- | --- |
	| Type | String |
	| Default Value | `localhost` |
	The host location of the running server that is currently using one of the key migration keystores. Migration always occurs on the local host, so the option always specifies a value for connecting to a local server, such as `localhost`, `127.0.0.1`, `::1`, or the local host IP address or host name.
- ``--login-path=*`name`*``
	| Command-Line Format | `--login-path=name` |
	| --- | --- |
	| Type | String |
	Read options from the named login path in the `.mylogin.cnf` login path file. A “login path” is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 6.6.7, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read any option files. If program startup fails due to reading unknown options from an option file, `--no-defaults` can be used to prevent them from being read.
	The exception is that the `.mylogin.cnf` file is read in all cases, if it exists. This permits passwords to be specified in a safer way than on the command line even when `--no-defaults` is used. To create `.mylogin.cnf`, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 6.6.7, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--online-migration`
	| Command-Line Format | `--online-migration` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	This option is mandatory when a running server is using the keyring. It tells **mysql\_migrate\_keyring** to perform an online key migration. The option has these effects:
	- **mysql\_migrate\_keyring** connects to the server using any connection options specified; these options are otherwise ignored.
	- After **mysql\_migrate\_keyring** connects to the server, it tells the server to pause keyring operations. When key copying is complete, **mysql\_migrate\_keyring** tells the server it can resume keyring operations before disconnecting.
- [``--password[=*`password`*]``](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-migrate-keyring.html#option_mysql_migrate_keyring_password), ``-p[*`password`*]``
	| Command-Line Format | `--password[=password]` |
	| --- | --- |
	| Type | String |
	The password of the MySQL account used for connecting to the running server that is currently using one of the key migration keystores. The password value is optional. If not given, **mysql\_migrate\_keyring** prompts for one. If given, there must be *no space* between `--password=` or `-p` and the password following it. If no password option is specified, the default is to send no password.
	Specifying a password on the command line should be considered insecure. To avoid giving the password on the command line, use an option file. See [Section 8.1.2.1, “End-User Guidelines for Password Security”](password-security-user.md).
	To explicitly specify that there is no password and that **mysql\_migrate\_keyring** should not prompt for one, use the `--skip-password` option.
- ``--port=*`port_num`*``, ``-P *`port_num`*``
	| Command-Line Format | `--port=port_num` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `0` |
	For TCP/IP connections, the port number for connecting to the running server that is currently using one of the key migration keystores.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print the program name and all options that it gets from option files.
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--server-public-key-path=*`file_name`*``
	| Command-Line Format | `--server-public-key-path=file_name` |
	| --- | --- |
	| Type | File name |
	The path name to a file in PEM format containing a client-side copy of the public key required by the server for RSA key pair-based password exchange. This option applies to clients that authenticate with the `sha256_password` or `caching_sha2_password` authentication plugin. This option is ignored for accounts that do not authenticate with one of those plugins. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection.
	If ``--server-public-key-path=*`file_name`*`` is given and specifies a valid public key file, it takes precedence over `--get-server-public-key`.
	For `sha256_password`, this option applies only if MySQL was built using OpenSSL.
	For information about the `sha256_password` and `caching_sha2_password` plugins, see [Section 8.4.1.3, “SHA-256 Pluggable Authentication”](sha256-pluggable-authentication.md), and [Section 8.4.1.2, “Caching SHA-2 Pluggable Authentication”](caching-sha2-pluggable-authentication.md).
- ``--socket=*`path`*``, ``-S *`path`*``
	| Command-Line Format | `--socket={file_name\|pipe_name}` |
	| --- | --- |
	| Type | String |
	For Unix socket file or Windows named pipe connections, the socket file or named pipe for connecting to the running server that is currently using one of the key migration keystores.
	On Windows, this option applies only if the server was started with the [`named_pipe`](server-system-variables.md) system variable enabled to support named-pipe connections. In addition, the user making the connection must be a member of the Windows group specified by the [`named_pipe_full_access_group`](server-system-variables.md) system variable.
- ``--source-keyring=*`name`*``
	| Command-Line Format | `--source-keyring=name` |
	| --- | --- |
	| Type | String |
	The source keyring component for key migration. This is the component library file name specified without any platform-specific extension such as `.so` or `.dll`. For example, to use the component for which the library file is `component_keyring_file.so`, specify the option as `--source-keyring=component_keyring_file`.
	Note
	`--component-dir`, `--source-keyring`, and `--destination-keyring` are mandatory for all keyring migration operations performed by **mysql\_migrate\_keyring**. In addition, the source and destination components must differ, and both components must be properly configured so that **mysql\_migrate\_keyring** can load and use them.
- ``--source-keyring-configuration-dir=*`dir_name`*``
	| Command-Line Format | `--source-keyring-configuration-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	This option applies only if the source keyring component global configuration file contains `"read_local_config": true`, indicating that component configuration is contained in the local configuration file. The option value specifies the directory containing that local file.
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
	The user name of the MySQL account used for connecting to the running server that is currently using one of the key migration keystores.
- `--verbose`, `-v`
	| Command-Line Format | `--verbose` |
	| --- | --- |
	Verbose mode. Produce more output about what the program does.
- `--version`, `-V`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.