---
title: "Chapter 17 Troubleshooting for MySQL Enterprise Backup"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/meb-troubleshooting.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

To troubleshoot issues regarding backup and restore with the MySQL Enterprise Backup product, consider the following aspects:

- Before troubleshooting any problem, familiarize yourself with the known limits and restrictions on the product, in [Appendix B, *Limitations of MySQL Enterprise Backup*](bugs.backup.md).
- If **mysqlbackup** encounters problems during operating system calls, it returns the corresponding OS error codes. You might need to consult your operating system's documentation for the meaning of those error codes and how to handle them.
- The output from **mysqlbackup** is sent to `stderr` rather than `stdout`. By default, the same output is also saved to a log file in the `backup_dir` for use in error diagnosis. See [Section 20.11, “Message Logging Options”](backup-message-logging-options.md) for details on how to configure this logging feature.
- Incremental backups, when performed using the [`--start-lsn`](backup-incremental-options.md) option, require care to specify a sequence of time periods. You must record the final LSN value at the end of each backup, and specify that value in the next incremental backup. You must also make sure that the full backup you restore is prepared correctly first, so that it contains all the changes from the sequence of incremental backups.
- As **mysqlbackup** proceeds, it writes progress information into the `mysql.backup_progress` table. When the command finishes the backup operation, it records status information in the `mysql.backup_history` table. You can query those tables to monitor ongoing backup jobs, see how much time has been used for various stages, and check if any errors have occurred.