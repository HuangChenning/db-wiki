---
title: "MySQL :: MySQL 26.10 Reference Manual :: 6.4.2 mysql_secure_installation — Improve MySQL Installation Security"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/mysql-secure-installation.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 6.4.2 mysql\_secure\_installation — Improve MySQL Installation Security

This program enables you to improve the security of your MySQL installation in the following ways:

- You can set a password for `root` accounts.
- You can remove `root` accounts that are accessible from outside the local host.
- You can remove anonymous-user accounts.
- You can remove the `test` database (which by default can be accessed by all users, even anonymous users), and privileges that permit anyone to access databases with names that start with `test_`.

**mysql\_secure\_installation** helps you implement security recommendations similar to those described at [Section 2.9.4, “Securing the Initial MySQL Account”](default-privileges.md).

Normal usage is to connect to the local MySQL server; invoke **mysql\_secure\_installation** without arguments:

```svg
mysql_secure_installation
```

When executed, **mysql\_secure\_installation** prompts you to determine which actions to perform.

The `validate_password` component can be used for password strength checking. If the plugin is not installed, **mysql\_secure\_installation** prompts the user whether to install it. Any passwords entered later are checked using the plugin if it is enabled.

Most of the usual MySQL client options such as `--host` and `--port` can be used on the command line and in option files. For example, to connect to the local server over IPv6 using port 3307, use this command:

```svg
mysql_secure_installation --host=::1 --port=3307
```

**mysql\_secure\_installation** supports the following options, which can be specified on the command line or in the `[mysql_secure_installation]` and `[client]` groups of an option file. For information about option files used by MySQL programs, see [Section 6.2.2.2, “Using Option Files”](option-files.md).

**Table 6.9 mysql\_secure\_installation Options**

| Option Name | Description |
| --- | --- |
| [\--defaults-extra-file](option-file-options.md) | Read named option file in addition to usual option files |
| [\--defaults-file](option-file-options.md) | Read only named option file |
| [\--defaults-group-suffix](option-file-options.md) | Option group suffix value |
| \--help | Display help message and exit |
| \--host | Host on which MySQL server is located |
| [\--no-defaults](option-file-options.md) | Read no option files |
| \--password | Accepted but always ignored. Whenever mysql\_secure\_installation is invoked, the user is prompted for a password, regardless |
| \--port | TCP/IP port number for connection |
| [\--print-defaults](option-file-options.md) | Print default options |
| \--protocol | Transport protocol to use |
| \--socket | Unix socket file or Windows named pipe to use |
| \--ssl-ca | File that contains list of trusted SSL Certificate Authorities |
| \--ssl-capath | Directory that contains trusted SSL Certificate Authority certificate files |
| \--ssl-cert | File that contains X.509 certificate |
| \--ssl-cipher | Permissible ciphers for connection encryption |
| \--ssl-crl | File that contains certificate revocation lists |
| \--ssl-crlpath | Directory that contains certificate revocation-list files |
| \--ssl-fips-mode | Whether to enable FIPS mode on client side |
| \--ssl-key | File that contains X.509 key |
| [\--ssl-mode](mysql-command-options.md) | Desired security state of connection to server |
| \--ssl-session-data | File that contains SSL session data |
| \--ssl-session-data-continue-on-failed-reuse | Whether to establish connections if session reuse fails |
| \--tls-ciphersuites | Permissible TLSv1.3 ciphersuites for encrypted connections |
| \--tls-sni-servername | Server name supplied by the client |
| \--tls-version | Permissible TLS protocols for encrypted connections |
| \--use-default | Execute with no user interactivity |
| \--user | MySQL user name to use when connecting to server |

- `--help`, `-?`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display a help message and exit.
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
	Read not only the usual option groups, but also groups with the usual names and a suffix of *`str`*. For example, **mysql\_secure\_installation** normally reads the `[client]` and `[mysql_secure_installation]` groups. If this option is given as `--defaults-group-suffix=_other`, **mysql\_secure\_installation** also reads the `[client_other]` and `[mysql_secure_installation_other]` groups.
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--host=*`host_name`*``, ``-h *`host_name`*``
	| Command-Line Format | `--host` |
	| --- | --- |
	Connect to the MySQL server on the given host.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read any option files. If program startup fails due to reading unknown options from an option file, `--no-defaults` can be used to prevent them from being read.
	The exception is that the `.mylogin.cnf` file is read in all cases, if it exists. This permits passwords to be specified in a safer way than on the command line even when `--no-defaults` is used. To create `.mylogin.cnf`, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 6.6.7, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 6.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--password=*`password`*``, ``-p *`password`*``
	| Command-Line Format | `--password=password` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	This option is accepted but ignored. Whether or not this option is used, **mysql\_secure\_installation** always prompts the user for a password.
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
- ``--socket=*`path`*``, ``-S *`path`*``
	| Command-Line Format | `--socket={file_name\|pipe_name}` |
	| --- | --- |
	| Type | String |
	For connections to `localhost`, the Unix socket file to use, or, on Windows, the name of the named pipe to use.
	On Windows, this option applies only if the server was started with the [`named_pipe`](server-system-variables.md) system variable enabled to support named-pipe connections. In addition, the connection must be a member of the Windows group specified by the [`named_pipe_full_access_group`](server-system-variables.md) system variable.
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
- `--use-default`
	| Command-Line Format | `--use-default` |
	| --- | --- |
	| Type | Boolean |
	Execute noninteractively. This option can be used for unattended installation operations.
- ``--user=*`user_name`*``, ``-u *`user_name`*``
	| Command-Line Format | `--user=user_name` |
	| --- | --- |
	| Type | String |
	The user name of the MySQL account to use for connecting to the server.