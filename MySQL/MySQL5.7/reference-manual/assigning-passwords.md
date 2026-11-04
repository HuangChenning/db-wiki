---
title: "6.2.10 Assigning Account Passwords"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/assigning-passwords.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 6.2.10 Assigning Account Passwords

Required credentials for clients that connect to the MySQL server can include a password. This section describes how to assign passwords for MySQL accounts.

MySQL stores credentials in the `user` table in the `mysql` system database. Operations that assign or modify passwords are permitted only to users with the [`CREATE USER`](privileges-provided.md) privilege, or, alternatively, privileges for the `mysql` database ([`INSERT`](privileges-provided.md) privilege to create new accounts, [`UPDATE`](privileges-provided.md) privilege to modify existing accounts). If the [`read_only`](server-system-variables.md) system variable is enabled, use of account-modification statements such as [`CREATE USER`](create-user.md) or [`ALTER USER`](alter-user.md) additionally requires the [`SUPER`](privileges-provided.md) privilege.

The discussion here summarizes syntax only for the most common password-assignment statements. For complete details on other possibilities, see [Section 13.7.1.2, “CREATE USER Statement”](create-user.md), [Section 13.7.1.1, “ALTER USER Statement”](alter-user.md), [Section 13.7.1.4, “GRANT Statement”](grant.md), and [Section 13.7.1.7, “SET PASSWORD Statement”](set-password.md).

MySQL uses plugins to perform client authentication; see [Section 6.2.13, “Pluggable Authentication”](pluggable-authentication.md). In password-assigning statements, the authentication plugin associated with an account performs any hashing required of a cleartext password specified. This enables MySQL to obfuscate passwords prior to storing them in the `mysql.user` system table. For the statements described here, MySQL automatically hashes the password specified. There are also syntax for [`CREATE       USER`](create-user.md) and [`ALTER USER`](alter-user.md) that permits hashed values to be specified literally. For details, see the descriptions of those statements.

To assign a password when you create a new account, use [`CREATE USER`](create-user.md) and include an `IDENTIFIED BY` clause:

```
CREATE USER 'jeffrey'@'localhost' IDENTIFIED BY 'password';
```

[`CREATE USER`](create-user.md) also supports syntax for specifying the account authentication plugin. See [Section 13.7.1.2, “CREATE USER Statement”](create-user.md).

To assign or change a password for an existing account, use the [`ALTER USER`](alter-user.md) statement with an `IDENTIFIED BY` clause:

```
ALTER USER 'jeffrey'@'localhost' IDENTIFIED BY 'password';
```

If you are not connected as an anonymous user, you can change your own password without naming your own account literally:

```
ALTER USER USER() IDENTIFIED BY 'password';
```

To change an account password from the command line, use the [**mysqladmin**](mysqladmin.md) command:

```
mysqladmin -u user_name -h host_name password "password"
```

The account for which this command sets the password is the one with a row in the `mysql.user` system table that matches *`user_name`* in the `User` column and the client host *from which you connect* in the `Host` column.

Warning

Setting a password using [**mysqladmin**](mysqladmin.md) should be considered *insecure*. On some systems, your password becomes visible to system status programs such as **ps** that may be invoked by other users to display command lines. MySQL clients typically overwrite the command-line password argument with zeros during their initialization sequence. However, there is still a brief interval during which the value is visible. Also, on some systems this overwriting strategy is ineffective and the password remains visible to **ps**. (SystemV Unix systems and perhaps others are subject to this problem.)

If you are using MySQL Replication, be aware that, currently, a password used by a replica as part of a [`CHANGE MASTER TO`](change-master-to.md) statement is effectively limited to 32 characters in length; if the password is longer, any excess characters are truncated. This is not due to any limit imposed by the MySQL Server generally, but rather is an issue specific to MySQL Replication. (For more information, see Bug #43439.)