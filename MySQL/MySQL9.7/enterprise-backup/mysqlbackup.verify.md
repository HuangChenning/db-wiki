---
title: "4.2.3 Verifying a Backup"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/mysqlbackup.verify.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

### 4.2.3 Verifying a Backup

You can check the integrity of your backup using the [`validate`](backup-commands-validate.md) command. The following is a sample command for validating a backup image and the output for the successful validation:

```
$ mysqlbackup --backup-image=/home/meb/mysql/backups/testback3.mbi validate
MySQL Enterprise Backup  Ver 8.4.0-commercial for Linux on x86_64 (MySQL Enterprise - Commercial)
Copyright (c) 2003, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Starting with following command line ...
mysqlbackup
--backup-image=/home/meb/mysql/backups/testback3.mbi
validate

IMPORTANT: Please check that mysqlbackup run completes successfully.
           At the end of a successful 'validate' run mysqlbackup
           prints "mysqlbackup completed OK!".

240426 13:09:04 MAIN     INFO: Backup Image MEB version string: 8.4.0
240426 13:09:04 MAIN     INFO: MySQL server version is '8.4.0'
240426 13:09:04 MAIN     INFO: The backup image has no keyring.
240426 13:09:04 MAIN     INFO: Creating 14 buffers each of size 16777216.
240426 13:09:04 MAIN     INFO: Validate operation starts with following threads
                               1 read-threads    6 process-threads
240426 13:09:04 MAIN     INFO: Validating image ... /home/meb/mysql/backups/testback3.mbi
240426 13:09:04 PCR1     INFO: Validate: [Dir]: meta
240426 13:09:04 PCR3     INFO: Validate: [Dir]: datadir/mysql
240426 13:09:04 PCR3     INFO: Validate: [Dir]: datadir/performance_schema
240426 13:09:04 PCR6     INFO: Validate: [Dir]: datadir/pets
240426 13:09:04 PCR6     INFO: Validate: [Dir]: datadir/sys
240426 13:09:04 MAIN     INFO: datadir/mysql.ibd validated.
240426 13:09:04 MAIN     INFO: datadir/mysql/backup_history.ibd validated.
240426 13:09:04 MAIN     INFO: datadir/mysql/backup_progress.ibd validated.
240426 13:09:04 MAIN     INFO: datadir/sys/sys_config.ibd validated.
240426 13:09:04 MAIN     INFO: datadir/undo_001 validated.
240426 13:09:04 MAIN     INFO: datadir/pets/cats.ibd validated.
240426 13:09:04 MAIN     INFO: datadir/undo_002 validated.
240426 13:09:04 MAIN     INFO: datadir/ibdata1 validated.
240426 13:09:04 MAIN     INFO: Validate operation completed successfully.
240426 13:09:04 MAIN     INFO: Backup Image validation successful.
240426 13:09:04 MAIN     INFO: Source Image Path = /home/meb/mysql/backups/testback3.mbi

mysqlbackup completed OK!
```

Furthermore, you can also verify that your backup has been successful by restoring the backup data on a different server and run the MySQL daemon (**mysqld**) on the new data directory. You can then execute `SHOW` statements to verify the database and table structures, and execute queries to verify further details of the database. See [Section 4.2.4, “Restoring a Database”](mysqlbackup.restore.md) for the basic steps for restoring a backup, and see [Chapter 5, *Recovering or Restoring a Database Server*](restoring.md) for more detailed instructions.

Warning

**Do not try to verify a backup by starting a MySQL Server using a backup directly**. **You should never start a server using a raw [backup directory](glossary.md) as a data directory**, as the two types of directories are different and the action will crash the server and might corrupt your backup. Start the server only after performing the proper [restore operation](backup-commands-restore.md). See [Appendix A, *Frequently Asked Questions for MySQL Enterprise Backup*](meb-faq.md) for details."