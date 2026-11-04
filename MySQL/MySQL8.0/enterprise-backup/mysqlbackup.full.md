---
title: "4.3.2 Making a Full Backup"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/mysqlbackup.full.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 4.3.2 Making a Full Backup

Most backup strategies start with a complete backup of the MySQL server, from which you can restore all databases and tables. After you have created a [full backup](glossary.md), you might perform [incremental backups](glossary.md) (which are smaller and faster) for the next several backup tasks. You then make a full backup periodically to begin the cycle again.

For sample commands for making a full backup, see [Section 4.2.2, “Backing Up an Entire MySQL Instance”](mysqlbackup.backup.md).

This section outlines some of the things to consider when deciding on a strategy for creating full backups. As we shall see, factors like speed, capacity, and convenience are all relevant for your decisions.

#### Options on Command Line or in Configuration File?

For clarity, the examples in this manual often show some of the command-line options that are used with the **mysqlbackup** commands. For convenience and consistency, you can include those options that remain unchanged for most backup jobs into the `[mysqlbackup]` section of the MySQL configuration file that you supply to **mysqlbackup**. **mysqlbackup** also picks up the options from the `[mysqld]` section if they are present there. Putting the options into a configuration file can simplify backup administration for you: for example, putting port information into a configuration file, you can avoid the need to edit your backup scripts each time the database instance switches to a different port. See [Chapter 21, *Configuration Files and Parameters*](config-file-parameters.md) for details about the use of configuration files.

#### Using a Single Backup Directory or Timestamped Subdirectories?

For convenience, the [`--with-timestamp`](backup-repository-options.md) option creates uniquely named subdirectories under the [backup directory](glossary.md) to hold the backup data (permanent or temporary) and metadata. The timestamped subdirectories make it simpler to establish retention periods, allowing easy removal and archiving of backup data that has passed a certain age.

If you do use a single backup directory (that is, if you omit the `--with-timestamp` option), specify a new, unique directory name for each backup job.

For incremental backups that uses the `--incremental-base` option to specify the directory containing the previous backup, in order to make the directory names predictable, you might prefer to not use the `--with-timestamp` option and generate a sequence of directory names with your backup script instead.

#### Always Full Backup, or Full Backup plus Incremental Backups?

If your InnoDB data volume is small, or if your database is so busy that a high percentage of data changes between backups, you might want to run a full backup each time. However, you can usually save time and storage space by running periodic full backups and then several incremental backups in between them, as described in [Section 4.3.3, “Making a Differential or Incremental Backup”](mysqlbackup.incremental.md).

#### Use Compression or Not?

Creating a compressed backup can save you considerable storage space and reduce I/O usage significantly. And with the LZ4 compression method, the overhead for processing compression is quite low. In cases where database backups are moving from a faster disk system where the active database files sit to a possibly slower storage, compression will often significantly lower the overall backup time. It can result in reduced restoration time as well. In general, we recommend LZ4 compression over no compression for most users, as LZ4-based backups often finish in a shorter time period. However, test out MySQL Enterprise Backup within your environment to determine what is the most efficient approach. For more discussions on compressed backups, see [Section 4.3.4, “Making a Compressed Backup”](backup.compressed.md).