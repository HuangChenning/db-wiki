---
title: "14.5.4 Log Buffer"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/innodb-redo-log-buffer.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 14.5.4 Log Buffer

The log buffer is the memory area that holds data to be written to the log files on disk. Log buffer size is defined by the [`innodb_log_buffer_size`](innodb-parameters.md) variable. The default size is 16MB. The contents of the log buffer are periodically flushed to disk. A large log buffer enables large transactions to run without the need to write redo log data to disk before the transactions commit. Thus, if you have transactions that update, insert, or delete many rows, increasing the size of the log buffer saves disk I/O.

The [`innodb_flush_log_at_trx_commit`](innodb-parameters.md) variable controls how the contents of the log buffer are written and flushed to disk. The [`innodb_flush_log_at_timeout`](innodb-parameters.md) variable controls log flushing frequency.

For related information, see [Memory Configuration](innodb-init-startup-configuration.md), and [Section 8.5.4, “Optimizing InnoDB Redo Logging”](optimizing-innodb-logging.md).