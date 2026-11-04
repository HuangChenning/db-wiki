---
title: "1.3.2 Files Backed up for InnoDB Data"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/meb-files-backed-up-innodb.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

### 1.3.2 Files Backed up for InnoDB Data

The InnoDB-related data files that are backed up include the [ibdata\* files](glossary.md) (which represent the [system tablespace](glossary.md) and possibly the data for some user tables), any [.ibd files](glossary.md) (which contains data from user tables created with the [file-per-table](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/glossary.html#glos_file_per_table) setting enabled), and the data extracted from the [ib\_logfile\* files](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/glossary.html#glos_ib_logfile) (the [redo log](glossary.md) information representing changes that occur while the backup is running), which is stored in a new backup file [ibbackup\_logfile](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/glossary.html#glos_ibbackup_logfile).

If you use the compressed backup feature, the `.ibd` files are renamed in their compressed form to [.ibz files](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/glossary.html#glos_ibz_file).

The backed-up files, as they are originally copied, form a [raw backup](glossary.md) that requires further processing. The [apply](glossary.md) step (either as part of a [`copy-back-and-apply-log`](backup-commands-restore.md) command or a [`backup-and-apply-log`](backup-commands-backup.md) command, or as a separate [`apply-log`](backup-commands-update.md) command) updates the backed-up files based on the changes recorded in the `ibbackup_logfile` file. At this point, the data corresponds to a single point in time.

Note

To avoid concurrency issues during backups of busy databases, you can use the [`--only-innodb`](backup-partial-options.md) option to back up only InnoDB tables and the associated data.