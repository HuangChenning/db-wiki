---
title: "7.4.2 The Error Log"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/error-log.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 7.4.2 The Error Log

This section discusses how to configure the MySQL server for logging of diagnostic messages to the error log. For information about selecting the error message character set and language, see [Section 12.6, “Error Message Character Set”](charset-errors.md), and [Section 12.12, “Setting the Error Message Language”](error-message-language.md).

The error log contains a record of [**mysqld**](mysqld.md) startup and shutdown times. It also contains diagnostic messages such as errors, warnings, and notes that occur during server startup and shutdown, and while the server is running. For example, if [**mysqld**](mysqld.md) notices that a table needs to be automatically checked or repaired, it writes a message to the error log.

Depending on error log configuration, error messages may also populate the Performance Schema [`error_log`](performance-schema-error-log-table.md) table, to provide an SQL interface to the log and enable its contents to be queried. See [Section 29.12.22.2, “The error\_log Table”](performance-schema-error-log-table.md).

On some operating systems, the error log contains a stack trace if [**mysqld**](mysqld.md) exits abnormally. The trace can be used to determine where [**mysqld**](mysqld.md) exited. See [Section 7.9, “Debugging MySQL”](debugging-mysql.md).

If used to start [**mysqld**](mysqld.md), [**mysqld\_safe**](mysqld-safe.md) may write messages to the error log. For example, when [**mysqld\_safe**](mysqld-safe.md) notices abnormal [**mysqld**](mysqld.md) exits, it restarts [**mysqld**](mysqld.md) and writes a `mysqld       restarted` message to the error log.

The following sections discuss aspects of configuring error logging.