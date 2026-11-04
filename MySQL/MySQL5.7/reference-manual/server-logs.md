---
title: "5.4 MySQL Server Logs"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/server-logs.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

MySQL Server has several logs that can help you find out what activity is taking place.

| Log Type | Information Written to Log |
| --- | --- |
| Error log | Problems encountered starting, running, or stopping [**mysqld**](mysqld.md) |
| General query log | Established client connections and statements received from clients |
| Binary log | Statements that change data (also used for replication) |
| Relay log | Data changes received from a replication source server |
| Slow query log | Queries that took more than [`long_query_time`](server-system-variables.md) seconds to execute |
| DDL log (metadata log) | Metadata operations performed by DDL statements |

By default, no logs are enabled, except the error log on Windows. (The DDL log is always created when required, and has no user-configurable options; see [Section 5.4.6, “The DDL Log”](ddl-log.md).) The following log-specific sections provide information about the server options that enable logging.

By default, the server writes files for all enabled logs in the data directory. You can force the server to close and reopen the log files (or in some cases switch to a new log file) by flushing the logs. Log flushing occurs when you issue a [`FLUSH LOGS`](flush.md) statement; execute [**mysqladmin**](mysqladmin.md) with a `flush-logs` or `refresh` argument; or execute [**mysqldump**](mysqldump.md) with a [`--flush-logs`](mysqldump.md) option. See [Section 13.7.6.3, “FLUSH Statement”](flush.md), [Section 4.5.2, “mysqladmin — A MySQL Server Administration Program”](mysqladmin.md), and [Section 4.5.4, “mysqldump — A Database Backup Program”](mysqldump.md). In addition, the binary log is flushed when its size reaches the value of the [`max_binlog_size`](replication-options-binary-log.md) system variable.

You can control the general query and slow query logs during runtime. You can enable or disable logging, or change the log file name. You can tell the server to write general query and slow query entries to log tables, log files, or both. For details, see [Section 5.4.1, “Selecting General Query Log and Slow Query Log Output Destinations”](log-destinations.md), [Section 5.4.3, “The General Query Log”](query-log.md), and [Section 5.4.5, “The Slow Query Log”](slow-query-log.md).

The relay log is used only on replicas, to hold data changes from the replication source server that must also be made on the replica. For discussion of relay log contents and configuration, see [Section 16.2.4.1, “The Relay Log”](replica-logs-relaylog.md).

For information about log maintenance operations such as expiration of old log files, see [Section 5.4.7, “Server Log Maintenance”](log-file-maintenance.md).

For information about keeping logs secure, see [Section 6.1.2.3, “Passwords and Logging”](password-logging.md).