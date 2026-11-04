---
title: "MySQL :: MySQL 26.7 Reference Manual :: 9.3.3 Backup Strategy Summary"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/backup-strategy-summary.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 9.3.3 Backup Strategy Summary

In case of an operating system crash or power failure, `InnoDB` itself does all the job of recovering data. But to make sure that you can sleep well, observe the following guidelines:

- Always tun the MySQL server with binary logging enabled (that is the default setting for MySQL 26.7). If you have such safe media, this technique can also be good for disk load balancing (which results in a performance improvement).
- Make periodic full backups, using the [**mysqldump**](mysqldump.md) command shown earlier in [Section 9.3.1, “Establishing a Backup Policy”](backup-policy.md), that makes an online, nonblocking backup.
- Make periodic incremental backups by flushing the logs with [`FLUSH LOGS`](flush.md) or [**mysqladmin flush-logs**](mysqladmin.md).