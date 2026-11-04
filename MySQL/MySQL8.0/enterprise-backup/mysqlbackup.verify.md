---
title: "4.2.3 Verifying a Backup"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/mysqlbackup.verify.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 4.2.3 Verifying a Backup

You can check the integrity of your backup using the [`validate`](backup-commands-validate.md) command. The following is a sample command for validating a backup image and the output for the successful validation:

```
$ mysqlbackup --backup-image=/home/meb/mysql/backups/testback3.mbi validate
MySQL Enterprise Backup  Ver 8.0.31-commercial for Linux on x86_64 (MySQL Enterprise - Commercial)
Copyright (c) 2003, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Starting with following command line ...
./bin/mysqlbackup
--backup-image=/home/meb/mysql/backups/testback3.mbi
validate

IMPORTANT: Please check that mysqlbackup run completes successfully.
           At the end of a successful 'validate' run mysqlbackup
           prints "mysqlbackup completed OK!".

220913 14:53:38 MAIN     INFO: Backup Image MEB version string: 8.0.31
220913 14:53:38 MAIN     INFO: MySQL server version is '8.0.31'
220913 14:53:38 MAIN     INFO: The backup image has no keyring.
220913 14:53:38 MAIN     INFO: Creating 14 buffers each of size 16777216.
220913 14:53:38 MAIN     INFO: Validate operation starts with following threads
                               1 read-threads    6 process-threads
220913 14:53:38 MAIN     INFO: Validating image ... /home/meb/mysql/backups/testback3.mbi
220913 14:53:38 PCR6     INFO: Validate: [Dir]: meta
220913 14:53:39 PCR6     INFO: Validate: [Dir]: datadir/Test
220913 14:53:39 PCR6     INFO: Validate: [Dir]: datadir/mysql
220913 14:53:39 PCR6     INFO: Validate: [Dir]: datadir/performance_schema
220913 14:53:39 PCR3     INFO: Validate: [Dir]: datadir/sys
220913 14:53:39 MAIN     INFO: datadir/mysql.ibd validated.
220913 14:53:39 MAIN     INFO: datadir/undo_002 validated.
220913 14:53:39 MAIN     INFO: datadir/sys/sys_config.ibd validated.
220913 14:53:39 MAIN     INFO: datadir/ibdata1 validated.
220913 14:53:39 MAIN     INFO: datadir/undo_001 validated.
220913 14:53:39 MAIN     INFO: datadir/Test/test1.ibd validated.
220913 14:53:39 MAIN     INFO: datadir/mysql/backup_history.ibd validated.
220913 14:53:39 MAIN     INFO: datadir/mysql/backup_progress.ibd validated.
220913 14:53:39 MAIN     INFO: Validate operation completed successfully.
220913 14:53:39 MAIN     INFO: Backup Image validation successful.
220913 14:53:39 MAIN     INFO: Source Image Path = /home/meb/mysql/backups/testback3.mbi

mysqlbackup completed OK!
```

Furthermore, you can also verify that your backup has been successful by restoring the backup data on a different server and run the MySQL daemon (**mysqld**) on the new data directory. You can then execute `SHOW` statements to verify the database and table structures, and execute queries to verify further details of the database. See [Section 4.2.4, “Restoring a Database”](mysqlbackup.restore.md) for the basic steps for restoring a backup, and see [Chapter 5, *Recovering or Restoring a Database Server*](restoring.md) for more detailed instructions.

Warning

**Do not try to verify a backup by starting a MySQL Server using a backup directly**. **You should never start a server using a raw [backup directory](glossary.md) as a data directory**, as the two types of directories are different and the action will crash the server and might corrupt your backup. Start the server only after performing the proper [restore operation](backup-commands-restore.md). See [Appendix A, *Frequently Asked Questions for MySQL Enterprise Backup*](meb-faq.md) for details."