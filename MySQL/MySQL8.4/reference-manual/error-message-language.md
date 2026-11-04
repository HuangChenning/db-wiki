---
title: "12.12 Setting the Error Message Language"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/error-message-language.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

By default, [**mysqld**](mysqld.md) produces error messages in English, but they can be displayed instead in any of several other languages: Czech, Danish, Dutch, Estonian, French, German, Greek, Hungarian, Italian, Japanese, Korean, Norwegian, Norwegian-ny, Polish, Portuguese, Romanian, Russian, Slovak, Spanish, or Swedish. This applies to messages the server writes to the error log and sends to clients.

To select the language in which the server writes error messages, follow the instructions in this section. For information about changing the character set for error messages (rather than the language), see [Section 12.6, “Error Message Character Set”](charset-errors.md). For general information about configuring error logging, see [Section 7.4.2, “The Error Log”](error-log.md).

The server searches for the error message file using these rules:

- It looks for the file in a directory constructed from two system variable values, [`lc_messages_dir`](server-system-variables.md) and [`lc_messages`](server-system-variables.md), with the latter converted to a language name. Suppose that you start the server using this command:
	```
	mysqld --lc_messages_dir=/usr/share/mysql --lc_messages=fr_FR
	```
	In this case, [**mysqld**](mysqld.md) maps the locale `fr_FR` to the language `french` and looks for the error file in the `/usr/share/mysql/french` directory.
	By default, the language files are located in the ``share/mysql/*`LANGUAGE`*`` directory under the MySQL base directory.
- If the message file cannot be found in the directory constructed as just described, the server ignores the [`lc_messages`](server-system-variables.md) value and uses only the [`lc_messages_dir`](server-system-variables.md) value as the location in which to look.
- If the server cannot find the configured message file, it writes a message to the error log to indicate the problem and defaults to built-in English messages.

The [`lc_messages_dir`](server-system-variables.md) system variable can be set only at server startup and has only a global read-only value at runtime. [`lc_messages`](server-system-variables.md) can be set at server startup and has global and session values that can be modified at runtime. Thus, the error message language can be changed while the server is running, and each client can have its own error message language by setting its session [`lc_messages`](server-system-variables.md) value to the desired locale name. For example, if the server is using the `fr_FR` locale for error messages, a client can execute this statement to receive error messages in English:

```
SET lc_messages = 'en_US';
```