---
title: "8.5.4 Optimizing InnoDB Redo Logging"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/optimizing-innodb-logging.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 8.5.4 Optimizing InnoDB Redo Logging

Consider the following guidelines for optimizing redo logging:

- Make your redo log files big, even as big as the [buffer pool](glossary.md). When `InnoDB` has written the redo log files full, it must write the modified contents of the buffer pool to disk in a [checkpoint](glossary.md). Small redo log files cause many unnecessary disk writes. Although historically big redo log files caused lengthy recovery times, recovery is now much faster and you can confidently use large redo log files.
	The size and number of redo log files are configured using the [`innodb_log_file_size`](innodb-parameters.md) and [`innodb_log_files_in_group`](innodb-parameters.md) configuration options. For information about modifying an existing redo log file configuration, see [Changing the Number or Size of InnoDB Redo Log Files](innodb-redo-log.md).
- Consider increasing the size of the [log buffer](glossary.md). A large log buffer enables large [transactions](glossary.md) to run without a need to write the log to disk before the transactions [commit](glossary.md). Thus, if you have transactions that update, insert, or delete many rows, making the log buffer larger saves disk I/O. Log buffer size is configured using the [`innodb_log_buffer_size`](innodb-parameters.md) configuration option.
- Configure the [`innodb_log_write_ahead_size`](innodb-parameters.md) configuration option to avoid “read-on-write”. This option defines the write-ahead block size for the redo log. Set [`innodb_log_write_ahead_size`](innodb-parameters.md) to match the operating system or file system cache block size. Read-on-write occurs when redo log blocks are not entirely cached to the operating system or file system due to a mismatch between write-ahead block size for the redo log and operating system or file system cache block size.
	Valid values for [`innodb_log_write_ahead_size`](innodb-parameters.md) are multiples of the `InnoDB` log file block size (2 <sup>n</sup>). The minimum value is the `InnoDB` log file block size (512). Write-ahead does not occur when the minimum value is specified. The maximum value is equal to the [`innodb_page_size`](innodb-parameters.md) value. If you specify a value for [`innodb_log_write_ahead_size`](innodb-parameters.md) that is larger than the [`innodb_page_size`](innodb-parameters.md) value, the [`innodb_log_write_ahead_size`](innodb-parameters.md) setting is truncated to the [`innodb_page_size`](innodb-parameters.md) value.
	Setting the [`innodb_log_write_ahead_size`](innodb-parameters.md) value too low in relation to the operating system or file system cache block size results in read-on-write. Setting the value too high may have a slight impact on `fsync` performance for log file writes due to several blocks being written at once.