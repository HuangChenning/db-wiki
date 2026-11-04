---
title: "4.3.4 Making a Compressed Backup"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup.compressed.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

### 4.3.4 Making a Compressed Backup

To save disk space, you can compress InnoDB backup data files by using the [`--compress`](backup-compression-options.md) option of **mysqlbackup**. Compression lets you keep more sets of backup data on hand or save transmission time when sending the backup data to another server. Also, compression often results in faster backups because of reduced IO.

The backup compression feature works only for InnoDB tables. After the InnoDB tablespace files are compressed during backup, they receive the `.ibz` extension. To avoid wasting CPU cycles without saving additional disk space, `--compress` does not attempt to compress tables that were already-compressed on the server (see [Creating Compressed Tables](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-compression-usage.html)); nevertheless, such tablespace files are also saved with the `.ibz` extension inside the backup.

Note

When there is unused space within an InnoDB tablespace file, the entire file is copied during an uncompressed backup. Perform a compressed backup to avoid the storage overhead for the unused space.

The binary log and relay log files are compressed and saved with the `.bz` extension when being included in a compressed backup.

You cannot use the [`--compress`](backup-compression-options.md) option for incremental backups created only with the redo log (i.e., with the [`--incremental-with-redo-log-only`](backup-incremental-options.md) option).

You can also select the compression algorithm to use by the [`--compress-method`](backup-compression-options.md) option and, when using the ZLIB or LZMA compression algorithm, the level of compression by the [`--compress-level`](backup-compression-options.md) option. See [Section 20.6, “Compression Options”](backup-compression-options.md) for details.

This is a sample command for making a compressed single-file backup:

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf --compress --backup-image=backup.img backup-to-image
```

*Advanced:* This is a sample command for making a compressed directory backup:

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf --compress-method=zlib --compress-level=5 backup
```

This is a sample command for making a compressed and [prepared](glossary.md) directory backup:

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf --compress-method=zlib --compress-level=5 backup-and-apply-log
```

Warning

Compression ratio is low for encrypted InnoDB tables. Creating a compressed backup with a database containing many encrypted InnoDB tables is not recommended.

Note

See the [limitation](bugs.backup.md) that applies to compressed backups in [Appendix B, *Limitations of MySQL Enterprise Backup*](bugs.backup.md).