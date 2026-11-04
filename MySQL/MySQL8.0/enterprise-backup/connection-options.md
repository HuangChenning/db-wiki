---
title: "20.2 Connection Options"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/connection-options.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

When **mysqlbackup** creates a backup, it sends SQL commands to a MySQL server using a database server connection. The way to create a connection is similar to what is described in [Connecting to the MySQL Server Using Command Options](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/connecting.html) of the [MySQL 8.0 Reference Manual](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/).

As part of the **mysqlbackup** invocation, specify the appropriate `--user`, `--password`, `--port`, and other options to connect to the MySQL server. You can specify the connection-specific MySQL client options listed below in the `[mysqlbackup]` or `[client]` sections of a MySQL configuration file, or through **mysqlbackup** command-line options (click on the option name to see its description in the [mysql Client Options](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-command-options.html) section of the [MySQL 8.0 Reference Manual](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/)):

Notes

- **mysqlbackup** reads only `--user`, `--password`, `--port`, and `--socket` options from the `[client]` group, and ignores any other connection options.
- If you do not provide a value for the `--password`, the command prompts for one from the keyboard.
- The `--host` option is allowed in the configuration file for compatibility, but it has no effect. **mysqlbackup** always connects to the local server's IP address.
- If none of the algorithms specified by `--compression-algorithms` are permitted by the server, connection to the server will not be established.

- [`--login-path`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-command-options.html#option_mysql_login-path) = *`name`*
- [`--port`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-command-options.html#option_mysql_port) = *`port-num`*
- [`--protocol`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-command-options.html#option_mysql_protocol) = `{tcp|socket|pipe|memory}`
- [`--pipe`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-command-options.html#option_mysql_pipe) (alias for `--protocol=pipe`)
- [`--user`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-command-options.html#option_mysql_user) = *`name`* (short option: `-u`)
- [`--host`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-command-options.html#option_mysql_host) = *`hostname`*
- [`--socket`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-command-options.html#option_mysql_socket) = *`name`*
- [`--shared-memory-base-name`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/server-system-variables.html#sysvar_shared_memory_base_name) = *`value`* (Windows only)
- [`--character-sets-dir`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-command-options.html#option_mysql_character-sets-dir) = *`PATH`*
- [`--default-character-set`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-command-options.html#option_mysql_default-character-set) = *`VALUE`*
- [`--password`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-command-options.html#option_mysql_password) \[= *`value`*\] (short option: `-p`)
- [`--connect-timeout`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-command-options.html#option_mysql_connect-timeout)
- [`--ssl-mode`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/connection-options.html#option_general_ssl-mode) = *`mode`*
- [`--ssl-key`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/connection-options.html#option_general_ssl-key) = *`file_name`*
- [`--ssl-cert`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/connection-options.html#option_general_ssl-cert) = *`file_name`*
- [`--ssl-ca`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/connection-options.html#option_general_ssl-ca) = *`file_name`*
- [`--ssl-capath`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/connection-options.html#option_general_ssl-capath) = *`directory_name`*
- [`--ssl-cipher`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/connection-options.html#option_general_ssl-cipher) = *`cipher_list`*
- [`--ssl-fips-mode`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/connection-options.html#option_general_ssl-fips-mode) = `{OFF|ON|STRICT}`
- [`--tls-version`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/connection-options.html#option_general_tls-version) = *`protocol_list`*
- [`--compression-algorithms`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/connection-options.html#option_general_compression-algorithms) = *`name`* (*for release 8.0.18 and later*)
- [`--zstd-compression-level`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/connection-options.html#option_general_zstd-compression-level) = *`number`* (*for release 8.0.18 and later*)

Most other connection parameters used by the **mysql** command are recognized, but silently ignored. Unknown connection parameters cause **mysqlbackup** to throw an error and quit.