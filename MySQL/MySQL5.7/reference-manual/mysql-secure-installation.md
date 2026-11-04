---
title: "4.4.4 mysql_secure_installation — Improve MySQL Installation Security"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-secure-installation.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 4.4.4 mysql\_secure\_installation — Improve MySQL Installation Security

This program enables you to improve the security of your MySQL installation in the following ways:

- You can set a password for `root` accounts.
- You can remove `root` accounts that are accessible from outside the local host.
- You can remove anonymous-user accounts.
- You can remove the `test` database (which by default can be accessed by all users, even anonymous users), and privileges that permit anyone to access databases with names that start with `test_`.

**mysql\_secure\_installation** helps you implement security recommendations similar to those described at [Section 2.9.4, “Securing the Initial MySQL Account”](default-privileges.md).

Normal usage is to connect to the local MySQL server; invoke **mysql\_secure\_installation** without arguments:

```
mysql_secure_installation
```

When executed, **mysql\_secure\_installation** prompts you to determine which actions to perform.

The `validate_password` plugin can be used for password strength checking. If the plugin is not installed, **mysql\_secure\_installation** prompts the user whether to install it. Any passwords entered later are checked using the plugin if it is enabled.

Most of the usual MySQL client options such as `--host` and `--port` can be used on the command line and in option files. For example, to connect to the local server over IPv6 using port 3307, use this command:

```
mysql_secure_installation --host=::1 --port=3307
```

**mysql\_secure\_installation** supports the following options, which can be specified on the command line or in the `[mysql_secure_installation]` and `[client]` groups of an option file. For information about option files used by MySQL programs, see [Section 4.2.2.2, “Using Option Files”](option-files.md).

**Table 4.10 mysql\_secure\_installation Options**

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
| \--ssl | Enable connection encryption |
| \--ssl-ca | File that contains list of trusted SSL Certificate Authorities |
| \--ssl-capath | Directory that contains trusted SSL Certificate Authority certificate files |
| \--ssl-cert | File that contains X.509 certificate |
| \--ssl-cipher | Permissible ciphers for connection encryption |
| \--ssl-crl | File that contains certificate revocation lists |
| \--ssl-crlpath | Directory that contains certificate revocation-list files |
| \--ssl-key | File that contains X.509 key |
| [\--ssl-mode](mysql-command-options.md) | Desired security state of connection to server |
| \--ssl-verify-server-cert | Verify host name against server certificate Common Name identity |
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
	Read not only the usual option groups, but also groups with the usual names and a suffix of *`str`*. For example, **mysql\_secure\_installation** normally reads the `[client]` and `[mysql_secure_installation]` groups. If this option is given as `--defaults-group-suffix=_other`, **mysql\_secure\_installation** also reads the `[client_other]` and `[mysql_secure_installation_other]` groups.
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--host=*`host_name`*``, ``-h *`host_name`*``
	| Command-Line Format | `--host` |
	| --- | --- |
	Connect to the MySQL server on the given host.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read any option files. If program startup fails due to reading unknown options from an option file, `--no-defaults` can be used to prevent them from being read.
	The exception is that the `.mylogin.cnf` file is read in all cases, if it exists. This permits passwords to be specified in a safer way than on the command line even when `--no-defaults` is used. To create `.mylogin.cnf`, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 4.6.6, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
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
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--protocol={TCP|SOCKET|PIPE|MEMORY}`
	| Command-Line Format | `--protocol=type` |
	| --- | --- |
	| Type | String |
	| Default Value | `[see text]` |
	| Valid Values | `TCP`  `SOCKET`  `PIPE`  `MEMORY` |
	The transport protocol to use for connecting to the server. It is useful when the other connection parameters normally result in use of a protocol other than the one you want. For details on the permissible values, see [Section 4.2.5, “Connection Transport Protocols”](transport-protocols.md).
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