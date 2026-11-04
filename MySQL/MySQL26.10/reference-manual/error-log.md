---
title: "MySQL :: MySQL 26.10 Reference Manual :: 7.4.2 The Error Log"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/error-log.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 7.4.2 The Error Log

This section discusses how to configure the MySQL server for logging of diagnostic messages to the error log. For information about selecting the error message character set and language, see [Section 12.6, “Error Message Character Set”](charset-errors.md), and [Section 12.12, “Setting the Error Message Language”](error-message-language.md).

The error log contains a record of [**mysqld**](mysqld.md) startup and shutdown times. It also contains diagnostic messages such as errors, warnings, and notes that occur during server startup and shutdown, and while the server is running. For example, if [**mysqld**](mysqld.md) notices that a table needs to be automatically checked or repaired, it writes a message to the error log.

During server startup and data-directory initialization, the server writes a separate System event containing the complete update-aware version. The event uses the `ER_SERVER_VERSION_INFO` error symbol and has the following message text:

```svg
[System] Server version with update: '26.10.0.0'
```

Any applicable build or runtime suffix follows the update component. The existing startup message containing the three-part compatibility version is unchanged.

Depending on error log configuration, error messages may also populate the Performance Schema [`error_log`](performance-schema-error-log-table.md) table, to provide an SQL interface to the log and enable its contents to be queried. See [Section 29.12.23.3, “The error\_log Table”](performance-schema-error-log-table.md).

On some operating systems, the error log contains a stack trace if [**mysqld**](mysqld.md) exits abnormally. The trace can be used to determine where [**mysqld**](mysqld.md) exited. See [Section 7.9, “Debugging MySQL”](debugging-mysql.md).

When the server starts, it can recover an unprocessed stack trace from the previous server run and emit the trace through the configured error logging pipeline. Each line of the trace is emitted as a separate mandatory system event with the [`ER_STACK_BACKTRACE`](https://dev.mysql.com/doc/mysql-errors/26.10/en/server-error-reference.html#error_er_stack_backtrace) error symbol. Consequently, every configured log sink writes the trace in its own format. If an enabled sink supports the Performance Schema [`error_log`](performance-schema-error-log-table.md) table, the trace is also available through that table.

Stack-trace information that was previously available only in the traditional error log can therefore be written to other destinations, such as JSON logs, the system log, or the Windows Event Log. It can also be visible to users who have permission to query [`error_log`](performance-schema-error-log-table.md).

If used to start [**mysqld**](mysqld.md), [**mysqld\_safe**](mysqld-safe.md) may write messages to the error log. For example, when [**mysqld\_safe**](mysqld-safe.md) notices abnormal [**mysqld**](mysqld.md) exits, it restarts [**mysqld**](mysqld.md) and writes a `mysqld       restarted` message to the error log.

The following sections discuss aspects of configuring error logging.