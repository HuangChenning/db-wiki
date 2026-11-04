---
title: "5.1.1 Restoring a Compressed Backup"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/restore.compressed-backup.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 5.1.1 Restoring a Compressed Backup

Note

For MySQL Enterprise Backup 8.0.21 and later: The [`--uncompress`](backup-compression-options.md) option is no longer needed when restoring a compressed backup.

Restore a compressed backup image named *`<image_name>`*, using the [`--backup-dir`](backup-repository-options.md) option to specify the temporary directory into which temporary output, status files, and backup metadata will be saved:

**Example 5.2 Restoring a Compressed Backup**

```
mysqlbackup --defaults-file=<my.cnf> -uroot --backup-image=<image_name> \
  --backup-dir=<backupTmpDir> --datadir=<restoreDir> --uncompress copy-back-and-apply-log
```

*Advanced:* Do the same for a compressed directory backup at *`<backupDir>`* to *`<restoreDir>`* on the server using [`copy-back-and-apply-log`](backup-commands-restore.md):

**Example 5.3 Restoring a Compressed Directory Backup**

```
mysqlbackup --defaults-file=<my.cnf> -uroot --backup-dir=<backupDir> --datadir=<restoreDir> \
  --uncompress copy-back-and-apply-log
```

To restore a compressed and [prepared](glossary.md) directory backup created with the **backup-and-apply-log** command (which is only supported for MySQL Enterprise Backup 4.0.1 and later), use the [`copy-back`](backup-commands-restore.md) command and the [`--uncompress`](backup-compression-options.md) option:

**Example 5.4 Restoring a Compressed and Prepared Directory Backup**

```
mysqlbackup --defaults-file=<my.cnf> -uroot --backup-dir=<backupDir> --datadir=<restoreDir> \
  --uncompress copy-back
```

See [Section 4.3.4, “Making a Compressed Backup”](backup.compressed.md) and [Section 20.6, “Compression Options”](backup-compression-options.md) for more details on compressed backups.