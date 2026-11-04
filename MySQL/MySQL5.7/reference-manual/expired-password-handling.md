---
title: "6.2.12 Server Handling of Expired Passwords"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/expired-password-handling.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 6.2.12 Server Handling of Expired Passwords

MySQL provides password-expiration capability, which enables database administrators to require that users reset their password. Passwords can be expired manually, and on the basis of a policy for automatic expiration (see [Section 6.2.11, “Password Management”](password-management.md)).

The [`ALTER USER`](alter-user.md) statement enables account password expiration. For example:

```
ALTER USER 'myuser'@'localhost' PASSWORD EXPIRE;
```

For each connection that uses an account with an expired password, the server either disconnects the client or restricts the client to “sandbox mode,” in which the server permits the client to perform only those operations necessary to reset the expired password. Which action is taken by the server depends on both client and server settings, as discussed later.

If the server disconnects the client, it returns an [`ER_MUST_CHANGE_PASSWORD_LOGIN`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_must_change_password_login) error:

```
$> mysql -u myuser -p
Password: ******
ERROR 1862 (HY000): Your password has expired. To log in you must
change it using a client that supports expired passwords.
```

If the server restricts the client to sandbox mode, these operations are permitted within the client session:

- The client can reset the account password with [`ALTER USER`](alter-user.md) or [`SET PASSWORD`](set-password.md). After that has been done, the server restores normal access for the session, as well as for subsequent connections that use the account.
	Note
	Although it is possible to “reset” an expired password by setting it to its current value, it is preferable, as a matter of good policy, to choose a different password.
- The client can use the [`SET`](set-variable.md) statement, which is useful before MySQL 5.7.6 if [`SET PASSWORD`](set-password.md) must be used instead of [`ALTER USER`](alter-user.md) and the account uses an authentication plugin for which the [`old_passwords`](server-system-variables.md) system variable must first be set to a nondefault value to perform password hashing in a specific way.

For any operation not permitted within the session, the server returns an [`ER_MUST_CHANGE_PASSWORD`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_must_change_password) error:

```
mysql> USE performance_schema;
ERROR 1820 (HY000): You must reset your password using ALTER USER
statement before executing this statement.

mysql> SELECT 1;
ERROR 1820 (HY000): You must reset your password using ALTER USER
statement before executing this statement.
```

That is what normally happens for interactive invocations of the [**mysql**](mysql.md) client because by default such invocations are put in sandbox mode. To resume normal functioning, select a new password.

For noninteractive invocations of the [**mysql**](mysql.md) client (for example, in batch mode), the server normally disconnects the client if the password is expired. To permit noninteractive [**mysql**](mysql.md) invocations to stay connected so that the password can be changed (using the statements permitted in sandbox mode), add the [`--connect-expired-password`](mysql-command-options.md) option to the [**mysql**](mysql.md) command.

As mentioned previously, whether the server disconnects an expired-password client or restricts it to sandbox mode depends on a combination of client and server settings. The following discussion describes the relevant settings and how they interact.

Note

This discussion applies only for accounts with expired passwords. If a client connects using a nonexpired password, the server handles the client normally.

On the client side, a given client indicates whether it can handle sandbox mode for expired passwords. For clients that use the C client library, there are two ways to do this:

- Pass the `MYSQL_OPT_CAN_HANDLE_EXPIRED_PASSWORDS` flag to [`mysql_options()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-options.html) prior to connecting:
	```
	my_bool arg = 1;
	mysql_options(mysql,
	              MYSQL_OPT_CAN_HANDLE_EXPIRED_PASSWORDS,
	              &arg);
	```
	This is the technique used within the [**mysql**](mysql.md) client, which enables `MYSQL_OPT_CAN_HANDLE_EXPIRED_PASSWORDS` if invoked interactively or with the [`--connect-expired-password`](mysql-command-options.md) option.
- Pass the `CLIENT_CAN_HANDLE_EXPIRED_PASSWORDS` flag to [`mysql_real_connect()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-real-connect.html) at connect time:
	```
	MYSQL mysql;
	mysql_init(&mysql);
	if (!mysql_real_connect(&mysql,
	                        host, user, password, db,
	                        port, unix_socket,
	                        CLIENT_CAN_HANDLE_EXPIRED_PASSWORDS))
	{
	  ... handle error ...
	}
	```

Other MySQL Connectors have their own conventions for indicating readiness to handle sandbox mode. See the documentation for the Connector in which you are interested.

On the server side, if a client indicates that it can handle expired passwords, the server puts it in sandbox mode.

If a client does not indicate that it can handle expired passwords (or uses an older version of the client library that cannot so indicate), the server action depends on the value of the [`disconnect_on_expired_password`](server-system-variables.md) system variable:

- If [`disconnect_on_expired_password`](server-system-variables.md) is enabled (the default), the server disconnects the client with an [`ER_MUST_CHANGE_PASSWORD_LOGIN`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_must_change_password_login) error.
- If [`disconnect_on_expired_password`](server-system-variables.md) is disabled, the server puts the client in sandbox mode.