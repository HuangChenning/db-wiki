---
title: "7.3.3 Backup Strategy Summary"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/backup-strategy-summary.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 7.3.3 Backup Strategy Summary

In case of an operating system crash or power failure, `InnoDB` itself does all the job of recovering data. But to make sure that you can sleep well, observe the following guidelines:

- Always run the MySQL server with the [`--log-bin`](replication-options-binary-log.md) option, or even [``--log-bin=*`log_name`*``](replication-options-binary-log.md), where the log file name is located on some safe media different from the drive on which the data directory is located. If you have such safe media, this technique can also be good for disk load balancing (which results in a performance improvement).
- Make periodic full backups, using the [**mysqldump**](mysqldump.md) command shown earlier in [Section 7.3.1, “Establishing a Backup Policy”](backup-policy.md), that makes an online, nonblocking backup.
- Make periodic incremental backups by flushing the logs with [`FLUSH LOGS`](flush.md) or [**mysqladmin flush-logs**](mysqladmin.md).