---
title: "MySQL :: MySQL 26.10 Reference Manual :: 6.5.1 mysql — The MySQL Command-Line Client"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/mysql.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 6.5.1 mysql — The MySQL Command-Line Client

**mysql** is a simple SQL shell with input line editing capabilities. It supports interactive and noninteractive use. When used interactively, query results are presented in an ASCII-table format. When used noninteractively (for example, as a filter), the result is presented in tab-separated format. The output format can be changed using command options.

If you have problems due to insufficient memory for large result sets, use the [`--quick`](mysql-command-options.md) option. This forces **mysql** to retrieve results from the server a row at a time rather than retrieving the entire result set and buffering it in memory before displaying it. This is done by returning the result set using the [`mysql_use_result()`](https://dev.mysql.com/doc/c-api/26.10/en/mysql-use-result.html) C API function in the client/server library rather than [`mysql_store_result()`](https://dev.mysql.com/doc/c-api/26.10/en/mysql-store-result.html).

Note

Alternatively, MySQL Shell offers access to the X DevAPI. For details, see [MySQL Shell 26.10](https://dev.mysql.com/doc/mysql-shell/26.10/en/).

Using **mysql** is very easy. Invoke it from the prompt of your command interpreter as follows:

```svg
mysql db_name
```

Or:

```svg
mysql --user=user_name --password db_name
```

In this case, you'll need to enter your password in response to the prompt that **mysql** displays:

```svg
Enter password: your_password
```

Then type an SQL statement, end it with `;`, `\g`, or `\G` and press Enter.

Typing **Control+C** interrupts the current statement if there is one, or cancels any partial input line otherwise.

You can execute SQL statements in a script file (batch file) like this:

```svg
mysql db_name < script.sql > output.tab
```

On Unix, the **mysql** client logs statements executed interactively to a history file. See [Section 6.5.1.3, “mysql Client Logging”](mysql-logging.md).