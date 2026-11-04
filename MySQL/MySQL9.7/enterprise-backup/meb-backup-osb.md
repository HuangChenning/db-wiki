---
title: "11.1 Backing Up to Tape with Oracle Secure Backup"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/meb-backup-osb.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

Tape drives are affordable, high-capacity storage devices for backup data. MySQL Enterprise Backup can interface with media management software (MMS) such as Oracle Secure Backup (OSB) to drive MySQL backup and restore jobs. The media management software must support Version 2 or higher of the System Backup to Tape (SBT) API.

On the MySQL Enterprise Backup side, you run the backup job as a single-file backup using the [`--backup-image`](backup-repository-options.md) parameter, with the prefix `sbt:` in front of the filename, and optionally pass other `--sbt-*` parameters to **mysqlbackup** to control various aspects of the SBT processing. The `--sbt-*` options are listed in [Section 20.9, “Single-File Backup Options”](backup-single-file-options.md).

On the OSB side, you can schedule MySQL Enterprise Backup jobs by specifying a configurable command that calls **mysqlbackup**. You control OSB features such as encryption by defining a “storage selector” that applies those features to a particular backup, and passing the name of the storage selector to OSB using the MySQL Enterprise Backup parameter [``--sbt-database-name=*`storage_selector`*``](backup-single-file-options.md).

**To back up MySQL data to tape:**

- Specify the [``--backup-image=sbt:*`name`*``](backup-repository-options.md) parameter of **mysqlbackup** to uniquely identify the backup data. The `sbt:` prefix sends the backup data to the MMS rather than a local file, and the remainder of the argument value is used as the unique backup name within the MMS.
- Specify the [`--sbt-database-name`](backup-single-file-options.md) parameter of **mysqlbackup** to enable the OSB operator to configure a storage selector for backups from this MySQL source. (This parameter refers to a “storage selector” defined by the OSB operator, not to any MySQL database name.) By default, **mysqlbackup** supplies a value of `MySQL` for this MMS parameter. The argument to this option is limited to 8 bytes.
- If you have multiple media management programs installed, to select the specific SBT library to use, specify the [`--sbt-lib-path`](backup-single-file-options.md) parameter of the **mysqlbackup** command. If you do not specify the [`--sbt-lib-path`](backup-single-file-options.md) parameter, **mysqlbackup** uses the normal operating system paths and environment variables to locate the SBT library, which is named `libobk.so` on Linux and Unix systems and `ORASBT.DLL` on Windows systems. When you specify [`--sbt-lib-path`](backup-single-file-options.md), you can use a different filename for the library in addition to specifying the path.
- Specify any other product-specific settings that are normally controlled by environment variables using the [`--sbt-environment`](backup-single-file-options.md) option.

Each time an online backup is made to a tape using the SBT API, besides recording the backup in the `mysql.backup_history` and the `mysql.backup_progress` tables, an entry is also made to the `mysql.backup_sbt_history` table on the backed up MySQL instance. That facilitates the management of tape backups by allowing easy look-ups for information on them. The definition of the `backup_sbt_history` table is shown below:

```
mysql> DESCRIBE \`backup_sbt_history\`;
+--------------------+---------------+------+-----+---------------------+----------------+
| Field              | Type          | Null | Key | Default             | Extra          |
+--------------------+---------------+------+-----+---------------------+----------------+
| id                 | int           | NO   | PRI | NULL                | auto_increment |
| backup_id          | bigint        | NO   |     | NULL                |                |
| backup_file_name   | varchar(4096) | NO   |     | NULL                |                |
| file_creation_time | timestamp     | NO   |     | 0000-00-00 00:00:00 |                |
| file_expiry_time   | timestamp     | NO   |     | 0000-00-00 00:00:00 |                |
| volume_label       | varchar(64)   | NO   |     | NULL                |                |
| sbt_error_msg      | varchar(4096) | NO   |     | NULL                |                |
| sbt_error_code     | int           | NO   |     | NULL                |                |
+--------------------+---------------+------+-----+---------------------+----------------+
```

Here are the descriptions for the fields in the table:

- `id`: Auto-increment primary key for the table.
- `backup_id`: The backup's ID, which is also recorded in the backup's entries in the `mysql.backup_history` and the `mysql.backup_progress` tables.
- `backup_file_name`: The file name provided by the user through the [``--backup-image=sbt:*`name`*``](backup-repository-options.md) option.
- `file_creation_time`: Creation date and time for the tape backup.
- `file_expiry_time`: Expiration date and time for the tape backup.
- `volume_label`: Volume label for the physical medium which contains the tape backup.
- `sbt_error_msg`: Error message, when an error occurs while retrieving information for the tape backup.
- `sbt_error_code`: Error code, when an error occurs while retrieving information for the tape backup.

Multiple entries, one for each volume label, are created in the `mysql.backup_sbt_history` table, if the backup is split across multiple volumes.

Here are some sample entries in the `mysql.backup_sbt_history` table:

```
mysql> SELECT * FROM mysql.backup_sbt_history;
+----+-------------------+------------------+---------------------+---------------------+-----------------+---------------+----------------+
| id | backup_id         | backup_file_name | file_creation_time  | file_expiry_time    | volume_label    | sbt_error_msg | sbt_error_code |
+----+-------------------+------------------+---------------------+---------------------+-----------------+---------------+----------------+
|  1 | 15921945689894983 | backup_img1.msb  | 2020-06-15 07:16:09 | 2020-06-15 07:16:09 | /sbt_bup_dir    |               |              0 |
|  2 | 15921945689894983 | backup_img1.msb  | 2020-06-15 07:16:09 | 2020-06-15 07:16:09 | backup_img1.msb |               |              0 |
+----+-------------------+------------------+---------------------+---------------------+-----------------+---------------+----------------+
2 rows in set (0.00 sec)
```

A backup to tape always uses one write thread.

**To restore MySQL data from tape:**

- Specify the [``--backup-image=sbt:*`name`*``](backup-repository-options.md) parameter of **mysqlbackup** as part of the restore operation. Use the same *`name`* value which was used during the backup. This single parameter retrieves the appropriate data from the appropriate tape device.
- Optionally use the [`--sbt-lib-path`](backup-single-file-options.md) option, using the same value as for the backup operation.
- Specify any other product-specific settings that are normally controlled by environment variables using the [`--sbt-environment`](backup-single-file-options.md) option.

For product-specific information about Oracle Secure Backup, see [the Oracle Secure Backup documentation](http://www.oracle.com/technetwork/database/database-technologies/secure-backup/documentation/index.html).

**Example 11.1 Sample mysqlbackup Commands Using MySQL Enterprise Backup with Oracle Secure Backup**

```
# Uses libobk.so or ORASBT.DLL, at standard locations:
mysqlbackup --port=3306 --protocol=tcp --user=root --password \
  --backup-image=sbt:backup-shoeprod-2011-05-30 \
  --backup-dir=/backup backup-to-image

# Associates this backup with storage selector 'shoeprod':
mysqlbackup --port=3306 --protocol=tcp --user=root --password \
  --backup-image=sbt:backup-shoeprod-2011-05-30 \
  --sbt-database-name=shoeprod \
  --backup-dir=/backup backup-to-image

# Uses an alternative SBT library, /opt/Other-MMS.so:
mysqlbackup --port=3306 --protocol=tcp --user=root --password \
  --backup-image=sbt:backup-shoeprod-2011-05-30 \
  --sbt-lib-path=/opt/Other-MMS.so \
  --backup-dir=/backup backup-to-image
```