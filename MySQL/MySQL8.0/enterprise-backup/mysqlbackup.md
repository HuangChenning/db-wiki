---
title: "Chapter 18 mysqlbackup"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/mysqlbackup.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

The **mysqlbackup** client is an easy-to-use tool for all backup and restore operations. During backup operations, **mysqlbackup** backs up:

- All InnoDB tables and indexes, including:
	- The InnoDB [system tablespace](glossary.md), which, by default contains all the InnoDB tables.
	- Any separate data files produced with the InnoDB [file-per-table](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/glossary.html#glos_file_per_table) setting. Each one contains one table and its associated indexes. Each data file can use either the original [Antelope](glossary.md) or the new [Barracuda](glossary.md) file format.
- All MyISAM tables and indexes.
- Tables managed by other storage engines.
- Other files underneath the MySQL data directory, such as the `.sdi` files that record the structure of MyISAM tables.
- Any other files in the database subdirectories under the server's data directory.

In addition to creating backups, **mysqlbackup** can pack and unpack backup data, apply to the backup data any changes to InnoDB tables that occurred during the backup operation, and restore data, index, and log files back to their original locations, or to other places.

Here are some sample commands to start a backup operation with **mysqlbackup** are:

```
# Information about data files can be retrieved through the database server connection.
# Specify connection options on the command line.
mysqlbackup --user=dba --password --port=3306 \
  --with-timestamp --backup-dir=/export/backups \
  backup

# Or we can include the above options in the configuration file
# under the [mysqlbackup] section, and just specify the configuration file
# and the 'backup' operation.
mysqlbackup --defaults-file=/usr/local/mysql/my.cnf backup

# Or we can specify the configuration file as above, but
# override some of those options on the command line.
mysqlbackup --defaults-file=/usr/local/mysql/my.cnf \
  --compress --user=backupadmin --password --port=18080 \
  backup
```

The `--user` and the `--password` you specify are used to connect to the MySQL server. This MySQL user must have certain privileges in the MySQL server, as described in [Section 4.1.2, “Grant MySQL Privileges to Backup Administrator”](mysqlbackup.privileges.md).

The [`--with-timestamp`](backup-repository-options.md) option places the backup in a subdirectory created under the directory you specified above. The name of the backup subdirectory is formed from the date and the clock time of the backup run.

For the meanings of other command-line options, see [Chapter 20, ***mysqlbackup** Command-Line Options*](mysqlbackup.usage.md). For information about configuration files, see [Chapter 21, *Configuration Files and Parameters*](config-file-parameters.md).

Make sure that the user or the cron job running **mysqlbackup** has the rights to copy files from the MySQL database directories to the backup directory.

Make sure that your connection timeouts are long enough so that the **mysqlbackup** command can keep the connection to the server open for the duration of the backup run. **mysqlbackup** pings the server after copying each database to keep the connection alive.

Review [Section 13.1, “Optimizing Backup Performance”](backup-performance.md) to understand the various issues that can impact the performance of MySQL Enterprise Backup.