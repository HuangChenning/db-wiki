---
title: "14.6.6 Redo Log"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/innodb-redo-log.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 14.6.6 Redo Log

The redo log is a disk-based data structure used during crash recovery to correct data written by incomplete transactions. During normal operations, the redo log encodes requests to change table data that result from SQL statements or low-level API calls. Modifications that did not finish updating the data files before an unexpected shutdown are replayed automatically during initialization, and before connections are accepted. For information about the role of the redo log in crash recovery, see [Section 14.19.2, “InnoDB Recovery”](innodb-recovery.md).

By default, the redo log is physically represented on disk by two files named `ib_logfile0` and `ib_logfile1`. MySQL writes to the redo log files in a circular fashion. Data in the redo log is encoded in terms of records affected; this data is collectively referred to as redo. The passage of data through the redo log is represented by an ever-increasing [LSN](glossary.md) value.

Information and procedures related to redo logs are described under the following topics in the section:

#### Changing the Number or Size of InnoDB Redo Log Files

To change the number or the size of your `InnoDB` [redo log](glossary.md) files, perform the following steps:

1. Stop the MySQL server and make sure that it shuts down without errors.
2. Edit `my.cnf` to change the log file configuration. To change the log file size, configure [`innodb_log_file_size`](innodb-parameters.md). To increase the number of log files, configure [`innodb_log_files_in_group`](innodb-parameters.md).
3. Start the MySQL server again.

If `InnoDB` detects that the [`innodb_log_file_size`](innodb-parameters.md) differs from the redo log file size, it writes a log checkpoint, closes and removes the old log files, creates new log files at the requested size, and opens the new log files.