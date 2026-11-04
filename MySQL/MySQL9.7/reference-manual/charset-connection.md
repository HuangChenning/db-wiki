---
title: "12.4 Connection Character Sets and Collations"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/charset-connection.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

A “connection” is what a client program makes when it connects to the server, to begin a session within which it interacts with the server. The client sends SQL statements, such as queries, over the session connection. The server sends responses, such as result sets or error messages, over the connection back to the client.

### Connection Character Set and Collation System Variables

Several character set and collation system variables relate to a client's interaction with the server. Some of these have been mentioned in earlier sections:

- The [`character_set_server`](server-system-variables.md) and [`collation_server`](server-system-variables.md) system variables indicate the server character set and collation. See [Section 12.3.2, “Server Character Set and Collation”](charset-server.md).
- The [`character_set_database`](server-system-variables.md) and [`collation_database`](server-system-variables.md) system variables indicate the character set and collation of the default database. See [Section 12.3.3, “Database Character Set and Collation”](charset-database.md).

Additional character set and collation system variables are involved in handling traffic for the connection between a client and the server. Every client has session-specific connection-related character set and collation system variables. These session system variable values are initialized at connect time, but can be changed within the session.

Several questions about character set and collation handling for client connections can be answered in terms of system variables:

- What character set are statements in when they leave the client?
	The server takes the [`character_set_client`](server-system-variables.md) system variable to be the character set in which statements are sent by the client.
	Note
	Some character sets cannot be used as the client character set. See Impermissible Client Character Sets.
- What character set should the server translate statements to after receiving them?
	To determine this, the server uses the [`character_set_connection`](server-system-variables.md) and [`collation_connection`](server-system-variables.md) system variables:
	- The server converts statements sent by the client from [`character_set_client`](server-system-variables.md) to [`character_set_connection`](server-system-variables.md). Exception: For string literals that have an introducer such as `_utf8mb4` or `_latin2`, the introducer determines the character set. See [Section 12.3.8, “Character Set Introducers”](charset-introducer.md).
	- [`collation_connection`](server-system-variables.md) is important for comparisons of literal strings. For comparisons of strings with column values, [`collation_connection`](server-system-variables.md) does not matter because columns have their own collation, which has a higher collation precedence (see [Section 12.8.4, “Collation Coercibility in Expressions”](charset-collation-coercibility.md)).
- What character set should the server translate query results to before shipping them back to the client?
	The [`character_set_results`](server-system-variables.md) system variable indicates the character set in which the server returns query results to the client. This includes result data such as column values, result metadata such as column names, and error messages.
	To tell the server to perform no conversion of result sets or error messages, set [`character_set_results`](server-system-variables.md) to `NULL` or `binary`:
	```
	SET character_set_results = NULL;
	SET character_set_results = binary;
	```
	For more information about character sets and error messages, see [Section 12.6, “Error Message Character Set”](charset-errors.md).

To see the values of the character set and collation system variables that apply to the current session, use this statement:

```
SELECT * FROM performance_schema.session_variables
WHERE VARIABLE_NAME IN (
  'character_set_client', 'character_set_connection',
  'character_set_results', 'collation_connection'
) ORDER BY VARIABLE_NAME;
```

The following simpler statements also display the connection variables, but include other related variables as well. They can be useful to see *all* character set and collation system variables:

```
SHOW SESSION VARIABLES LIKE 'character\_set\_%';
SHOW SESSION VARIABLES LIKE 'collation\_%';
```

Clients can fine-tune the settings for these variables, or depend on the defaults (in which case, you can skip the rest of this section). If you do not use the defaults, you must change the character settings *for each connection to the server*.

### Impermissible Client Character Sets

The [`character_set_client`](server-system-variables.md) system variable cannot be set to certain character sets:

```
ucs2
utf16
utf16le
utf32
```

Attempting to use any of those character sets as the client character set produces an error:

```
mysql> SET character_set_client = 'ucs2';
ERROR 1231 (42000): Variable 'character_set_client'
can't be set to the value of 'ucs2'
```

The same error occurs if any of those character sets are used in the following contexts, all of which result in an attempt to set [`character_set_client`](server-system-variables.md) to the named character set:

### Client Program Connection Character Set Configuration

When a client connects to the server, it indicates which character set it wants to use for communication with the server. (Actually, the client indicates the default collation for that character set, from which the server can determine the character set.) The server uses this information to set the [`character_set_client`](server-system-variables.md), [`character_set_results`](server-system-variables.md), [`character_set_connection`](server-system-variables.md) system variables to the character set, and [`collation_connection`](server-system-variables.md) to the character set default collation. In effect, the server performs the equivalent of a [`SET NAMES`](set-names.md) operation.

If the server does not support the requested character set or collation, it falls back to using the server character set and collation to configure the connection. For additional detail about this fallback behavior, see Connection Character Set Error Handling.

The [**mysql**](mysql.md), [**mysqladmin**](mysqladmin.md), [**mysqlcheck**](mysqlcheck.md), [**mysqlimport**](mysqlimport.md), and [**mysqlshow**](mysqlshow.md) client programs determine the default character set to use as follows:

- In the absence of other information, each client uses the compiled-in default character set, usually `utf8mb4`.
- Each client can autodetect which character set to use based on the operating system setting, such as the value of the `LANG` or `LC_ALL` locale environment variable on Unix systems or the code page setting on Windows systems. For systems on which the locale is available from the OS, the client uses it to set the default character set rather than using the compiled-in default. For example, setting `LANG` to `ru_RU.KOI8-R` causes the `koi8r` character set to be used. Thus, users can configure the locale in their environment for use by MySQL clients.
	The OS character set is mapped to the closest MySQL character set if there is no exact match. If the client does not support the matching character set, it uses the compiled-in default. For example, `utf8` and `utf-8` map to `utf8mb4`, and `ucs2` is not supported as a connection character set, so it maps to the compiled-in default.
	C applications can use character set autodetection based on the OS setting by invoking [`mysql_options()`](https://docs.oracle.com/cd/E17952_01/c-api-9.7-en/mysql-options.html) as follows before connecting to the server:
	```
	mysql_options(mysql,
	              MYSQL_SET_CHARSET_NAME,
	              MYSQL_AUTODETECT_CHARSET_NAME);
	```
- Each client supports a [`--default-character-set`](mysql-command-options.md) option, which enables users to specify the character set explicitly to override whatever default the client otherwise determines.
	Note
	Some character sets cannot be used as the client character set. Attempting to use them with [`--default-character-set`](mysql-command-options.md) produces an error. See Impermissible Client Character Sets.

With the [**mysql**](mysql.md) client, to use a character set different from the default, you could explicitly execute a [`SET NAMES`](set-names.md) statement every time you connect to the server (see Client Program Connection Character Set Configuration). To accomplish the same result more easily, specify the character set in your option file. For example, the following option file setting changes the three connection-related character set system variables set to `koi8r` each time you invoke [**mysql**](mysql.md):

```
[mysql]
default-character-set=koi8r
```

If you are using the [**mysql**](mysql.md) client with auto-reconnect enabled (which is not recommended), it is preferable to use the `charset` command rather than [`SET NAMES`](set-names.md). For example:

```
mysql> charset koi8r
Charset changed
```

The `charset` command issues a [`SET NAMES`](set-names.md) statement, and also changes the default character set that [**mysql**](mysql.md) uses when it reconnects after the connection has dropped.

When configuration client programs, you must also consider the environment within which they execute. See [Section 12.5, “Configuring Application Character Set and Collation”](charset-applications.md).

### SQL Statements for Connection Character Set Configuration

After a connection has been established, clients can change the character set and collation system variables for the current session. These variables can be changed individually using [`SET`](set-statement.md) statements, but two more convenient statements affect the connection-related character set system variables as a group:

- ``SET NAMES '*`charset_name`*'             [COLLATE             '*`collation_name`*']``
	[`SET NAMES`](set-names.md) indicates what character set the client uses to send SQL statements to the server. Thus, [`SET             NAMES 'cp1251'`](set-names.md) tells the server, “future incoming messages from this client are in character set `cp1251`.” It also specifies the character set that the server should use for sending results back to the client. (For example, it indicates what character set to use for column values if you use a [`SELECT`](select.md) statement that produces a result set.)
	A [``SET NAMES             '*`charset_name`*'``](set-names.md) statement is equivalent to these three statements:
	```
	SET character_set_client = charset_name;
	SET character_set_results = charset_name;
	SET character_set_connection = charset_name;
	```
	Setting [`character_set_connection`](server-system-variables.md) to *`charset_name`* also implicitly sets [`collation_connection`](server-system-variables.md) to the default collation for *`charset_name`*. It is unnecessary to set that collation explicitly. To specify a particular collation to use for [`collation_connection`](server-system-variables.md), add a `COLLATE` clause:
	```
	SET NAMES 'charset_name' COLLATE 'collation_name'
	```
- ``SET CHARACTER SET             '*`charset_name`*`` '
	[`SET CHARACTER SET`](set-character-set.md) is similar to [`SET NAMES`](set-names.md) but sets [`character_set_connection`](server-system-variables.md) and [`collation_connection`](server-system-variables.md) to [`character_set_database`](server-system-variables.md) and [`collation_database`](server-system-variables.md) (which, as mentioned previously, indicate the character set and collation of the default database).
	A [``SET             CHARACTER SET             *`charset_name`*``](set-character-set.md) statement is equivalent to these three statements:
	```
	SET character_set_client = charset_name;
	SET character_set_results = charset_name;
	SET collation_connection = @@collation_database;
	```
	Setting [`collation_connection`](server-system-variables.md) also implicitly sets [`character_set_connection`](server-system-variables.md) to the character set associated with the collation (equivalent to executing `SET character_set_connection =             @@character_set_database`). It is unnecessary to set [`character_set_connection`](server-system-variables.md) explicitly.

Note

Some character sets cannot be used as the client character set. Attempting to use them with [`SET           NAMES`](set-names.md) or [`SET CHARACTER           SET`](set-character-set.md) produces an error. See Impermissible Client Character Sets.

Example: Suppose that `column1` is defined as `CHAR(5) CHARACTER SET latin2`. If you do not say [`SET NAMES`](set-names.md) or [`SET CHARACTER SET`](set-character-set.md), then for `SELECT column1 FROM t`, the server sends back all the values for `column1` using the character set that the client specified when it connected. On the other hand, if you say `SET NAMES 'latin1'` or `SET CHARACTER SET 'latin1'` before issuing the [`SELECT`](select.md) statement, the server converts the `latin2` values to `latin1` just before sending results back. Conversion may be lossy for characters that are not in both character sets.

### Connection Character Set Error Handling

Attempts to use an inappropriate connection character set or collation can produce an error, or cause the server to fall back to its default character set and collation for a given connection. This section describes problems that can occur when configuring the connection character set. These problems can occur when establishing a connection or when changing the character set within an established connection.

#### Connect-Time Error Handling

Some character sets cannot be used as the client character set; see Impermissible Client Character Sets. If you specify a character set that is valid but not permitted as a client character set, the server returns an error:

```
$> mysql --default-character-set=ucs2
ERROR 1231 (42000): Variable 'character_set_client' can't be set to
the value of 'ucs2'
```

If you specify a character set that the client does not recognize, it produces an error:

```
$> mysql --default-character-set=bogus
mysql: Character set 'bogus' is not a compiled character set and is
not specified in the '/usr/local/mysql/share/charsets/Index.xml' file
ERROR 2019 (HY000): Can't initialize character set bogus
(path: /usr/local/mysql/share/charsets/)
```

If you specify a character set that the client recognizes but the server does not, the server falls back to its default character set and collation. Suppose that the server is configured to use `latin1` and `latin1_swedish_ci` as its defaults, and that it does not recognize `gb18030` as a valid character set. A client that specifies [`--default-character-set=gb18030`](mysql-command-options.md) is able to connect to the server, but the resulting character set is not what the client wants:

```
mysql> SHOW SESSION VARIABLES LIKE 'character\_set\_%';
+--------------------------+--------+
| Variable_name            | Value  |
+--------------------------+--------+
| character_set_client     | latin1 |
| character_set_connection | latin1 |
...
| character_set_results    | latin1 |
...
+--------------------------+--------+
mysql> SHOW SESSION VARIABLES LIKE 'collation_connection';
+----------------------+-------------------+
| Variable_name        | Value             |
+----------------------+-------------------+
| collation_connection | latin1_swedish_ci |
+----------------------+-------------------+
```

You can see that the connection system variables have been set to reflect a character set and collation of `latin1` and `latin1_swedish_ci`. This occurs because the server cannot satisfy the client character set request and falls back to its defaults.

In this case, the client cannot use the character set that it wants because the server does not support it. The client must either be willing to use a different character set, or connect to a different server that supports the desired character set.

The same problem occurs when the client tells the server to use a character set that the server recognizes, but the default collation for that character set on the client side is not known on the server side.

#### Runtime Error Handling

Within an established connection, the client can request a change of connection character set and collation with [`SET NAMES`](set-names.md) or [`SET CHARACTER SET`](set-character-set.md).

Some character sets cannot be used as the client character set; see Impermissible Client Character Sets. If you specify a character set that is valid but not permitted as a client character set, the server returns an error:

```
mysql> SET NAMES 'ucs2';
ERROR 1231 (42000): Variable 'character_set_client' can't be set to
the value of 'ucs2'
```

If the server does not recognize the character set (or the collation), it produces an error:

```
mysql> SET NAMES 'bogus';
ERROR 1115 (42000): Unknown character set: 'bogus'

mysql> SET NAMES 'utf8mb4' COLLATE 'bogus';
ERROR 1273 (HY000): Unknown collation: 'bogus'
```

A client that wants to verify whether its requested character set was honored by the server can execute the following statement after connecting and checking that the result is the expected character set:

```
SELECT @@character_set_client;
```