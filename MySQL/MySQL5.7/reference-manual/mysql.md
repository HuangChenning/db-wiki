---
title: "4.5.1 mysql — The MySQL Command-Line Client"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 4.5.1 mysql — The MySQL Command-Line Client

**mysql** is a simple SQL shell with input line editing capabilities. It supports interactive and noninteractive use. When used interactively, query results are presented in an ASCII-table format. When used noninteractively (for example, as a filter), the result is presented in tab-separated format. The output format can be changed using command options.

If you have problems due to insufficient memory for large result sets, use the [`--quick`](mysql-command-options.md) option. This forces **mysql** to retrieve results from the server a row at a time rather than retrieving the entire result set and buffering it in memory before displaying it. This is done by returning the result set using the [`mysql_use_result()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-use-result.html) C API function in the client/server library rather than [`mysql_store_result()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-store-result.html).

Note

Alternatively, MySQL Shell offers access to the X DevAPI. For details, see [MySQL Shell 8.0](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.0-en/).

Using **mysql** is very easy. Invoke it from the prompt of your command interpreter as follows:

```
mysql db_name
```

Or:

```
mysql --user=user_name --password db_name
```

In this case, you'll need to enter your password in response to the prompt that **mysql** displays:

```
Enter password: your_password
```

Then type an SQL statement, end it with `;`, `\g`, or `\G` and press Enter.

Typing **Control+C** interrupts the current statement if there is one, or cancels any partial input line otherwise.

You can execute SQL statements in a script file (batch file) like this:

```
mysql db_name < script.sql > output.tab
```

On Unix, the **mysql** client logs statements executed interactively to a history file. See [Section 4.5.1.3, “mysql Client Logging”](mysql-logging.md).