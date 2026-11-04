---
title: "5.4.2 The Error Log"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/error-log.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 5.4.2 The Error Log

This section discusses how to configure the MySQL server for logging of diagnostic messages to the error log. For information about selecting the error message character set and language, see [Section 10.6, “Error Message Character Set”](charset-errors.md), and [Section 10.12, “Setting the Error Message Language”](error-message-language.md).

The error log contains a record of [**mysqld**](mysqld.md) startup and shutdown times. It also contains diagnostic messages such as errors, warnings, and notes that occur during server startup and shutdown, and while the server is running. For example, if [**mysqld**](mysqld.md) notices that a table needs to be automatically checked or repaired, it writes a message to the error log.

On some operating systems, the error log contains a stack trace if [**mysqld**](mysqld.md) exits abnormally. The trace can be used to determine where [**mysqld**](mysqld.md) exited. See [Section 5.8, “Debugging MySQL”](debugging-mysql.md).

If used to start [**mysqld**](mysqld.md), [**mysqld\_safe**](mysqld-safe.md) may write messages to the error log. For example, when [**mysqld\_safe**](mysqld-safe.md) notices abnormal [**mysqld**](mysqld.md) exits, it restarts [**mysqld**](mysqld.md) and writes a `mysqld       restarted` message to the error log.

The following sections discuss aspects of configuring error logging. In the discussion, “console” means `stderr`, the standard error output. This is your terminal or console window unless the standard error output has been redirected to a different destination.

The server interprets options that determine where to write error messages somewhat differently for Windows and Unix systems. Be sure to configure error logging using the information appropriate to your platform.