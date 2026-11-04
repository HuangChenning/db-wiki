---
title: "6.2.1 Account User Names and Passwords"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/user-names.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 6.2.1 Account User Names and Passwords

MySQL stores accounts in the `user` table of the `mysql` system database. An account is defined in terms of a user name and the client host or hosts from which the user can connect to the server. For information about account representation in the `user` table, see [Section 6.2.3, “Grant Tables”](grant-tables.md).

An account may also have authentication credentials such as a password. The credentials are handled by the account authentication plugin. MySQL supports multiple authentication plugins. Some of them use built-in authentication methods, whereas others enable authentication using external authentication methods. See [Section 6.2.13, “Pluggable Authentication”](pluggable-authentication.md).

There are several distinctions between the way user names and passwords are used by MySQL and your operating system:

- User names, as used by MySQL for authentication purposes, have nothing to do with user names (login names) as used by Windows or Unix. On Unix, most MySQL clients by default try to log in using the current Unix user name as the MySQL user name, but that is for convenience only. The default can be overridden easily, because client programs permit any user name to be specified with a `-u` or `--user` option. This means that anyone can attempt to connect to the server using any user name, so you cannot make a database secure in any way unless all MySQL accounts have passwords. Anyone who specifies a user name for an account that has no password can connect successfully to the server.
- MySQL user names are up to 32 characters long. Operating system user names may have a different maximum length.
	Warning
	The MySQL user name length limit is hardcoded in MySQL servers and clients, and trying to circumvent it by modifying the definitions of the tables in the `mysql` database *does not work*.
	You should never alter the structure of tables in the `mysql` database in any manner whatsoever except by means of the procedure that is described in [Section 2.10, “Upgrading MySQL”](upgrading.md). Attempting to redefine the MySQL system tables in any other fashion results in undefined and unsupported behavior. The server is free to ignore rows that become malformed as a result of such modifications.
- To authenticate client connections for accounts that use built-in authentication methods, the server uses passwords stored in the `user` table. These passwords are distinct from passwords for logging in to your operating system. There is no necessary connection between the “external” password you use to log in to a Windows or Unix machine and the password you use to access the MySQL server on that machine.
	If the server authenticates a client using some other plugin, the authentication method that the plugin implements may or may not use a password stored in the `user` table. In this case, it is possible that an external password is also used to authenticate to the MySQL server.
- Passwords stored in the `user` table are encrypted using plugin-specific algorithms. For information about MySQL native password hashing, see [Section 6.1.2.4, “Password Hashing in MySQL”](password-hashing.md).
- If the user name and password contain only ASCII characters, it is possible to connect to the server regardless of character set settings. To enable connections when the user name or password contain non-ASCII characters, client applications should call the [`mysql_options()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-options.html) C API function with the `MYSQL_SET_CHARSET_NAME` option and appropriate character set name as arguments. This causes authentication to take place using the specified character set. Otherwise, authentication fails unless the server default character set is the same as the encoding in the authentication defaults.
	Standard MySQL client programs support a `--default-character-set` option that causes [`mysql_options()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-options.html) to be called as just described. In addition, character set autodetection is supported as described in [Section 10.4, “Connection Character Sets and Collations”](charset-connection.md). For programs that use a connector that is not based on the C API, the connector may provide an equivalent to [`mysql_options()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-options.html) that can be used instead. Check the connector documentation.
	The preceding notes do not apply for `ucs2`, `utf16`, and `utf32`, which are not permitted as client character sets.

The MySQL installation process populates the grant tables with an initial `root` account, as described in [Section 2.9.4, “Securing the Initial MySQL Account”](default-privileges.md), which also discusses how to assign a password to it. Thereafter, you normally set up, modify, and remove MySQL accounts using statements such as [`CREATE USER`](create-user.md), [`DROP USER`](drop-user.md), [`GRANT`](grant.md), and [`REVOKE`](revoke.md). See [Section 6.2.7, “Adding Accounts, Assigning Privileges, and Dropping Accounts”](creating-accounts.md), and [Section 13.7.1, “Account Management Statements”](account-management-statements.md).

To connect to a MySQL server with a command-line client, specify user name and password options as necessary for the account that you want to use:

```
$> mysql --user=finley --password db_name
```

If you prefer short options, the command looks like this:

```
$> mysql -u finley -p db_name
```

If you omit the password value following the [`--password`](connection-options.md) or `-p` option on the command line (as just shown), the client prompts for one. Alternatively, the password can be specified on the command line:

```
$> mysql --user=finley --password=password db_name
$> mysql -u finley -ppassword db_name
```

If you use the `-p` option, there must be *no space* between `-p` and the following password value.

Specifying a password on the command line should be considered insecure. See [Section 6.1.2.1, “End-User Guidelines for Password Security”](password-security-user.md). To avoid giving the password on the command line, use an option file or a login path file. See [Section 4.2.2.2, “Using Option Files”](option-files.md), and [Section 4.6.6, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).

For additional information about specifying user names, passwords, and other connection parameters, see [Section 4.2.4, “Connecting to the MySQL Server Using Command Options”](connecting.md).