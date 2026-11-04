---
title: "17.5.4 Log Buffer"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/innodb-redo-log-buffer.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 17.5.4 Log Buffer

The log buffer is the memory area that holds data to be written to the log files on disk. Log buffer size is defined by the [`innodb_log_buffer_size`](innodb-parameters.md) variable. The default size is 64MB. The contents of the log buffer are periodically flushed to disk. A large log buffer enables large transactions to run without the need to write redo log data to disk before the transactions commit. Thus, if you have transactions that update, insert, or delete many rows, increasing the size of the log buffer saves disk I/O.

The [`innodb_flush_log_at_trx_commit`](innodb-parameters.md) variable controls how the contents of the log buffer are written and flushed to disk. The [`innodb_flush_log_at_timeout`](innodb-parameters.md) variable controls log flushing frequency.

For related information, see [Memory Configuration](innodb-init-startup-configuration.md), and [Section 10.5.4, “Optimizing InnoDB Redo Logging”](optimizing-innodb-logging.md).