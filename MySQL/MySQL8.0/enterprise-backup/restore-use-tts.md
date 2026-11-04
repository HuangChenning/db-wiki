---
title: "5.1.5 Restoring Backups Created with the --use-tts Option"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/restore-use-tts.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 5.1.5 Restoring Backups Created with the --use-tts Option

Requirements for restoring backups created with [transportable tablespaces (TTS)](glossary.md) (that is, created with the [`--use-tts`](backup-partial-options.md) option) are similar to those listed in [Section 5.1.4, “Table-Level Recovery (TLR)”](restore.partial.md), with some differences noted in the section. The following is some additional information on partial restores using TTS backups

To backup and restore backups created using TTS, extra privileges are required of the user through which **mysqlbackup** connects to the server; see [Section 4.1.2, “Grant MySQL Privileges to Backup Administrator”](mysqlbackup.privileges.md) for details.

When restoring a single-file backup created with the option setting [`--use-tts`](backup-partial-options.md) = `with-minimum-locking`, the folder specified with [`--backup-dir`](backup-repository-options.md), besides holding temporary output, status files, and metadata, is also used for extracting temporarily all the tables in the backup and for performing an [`apply-log`](backup-commands-update.md) operation to make the data up-to-date before restoring them to the server's data directory.

You can rename a table when restoring it from a TTS backup by using the [`--rename`](backup-partial-options.md) option (the option is not supported for [non-TTS backups](glossary.md)):

**Example 5.9 Restoring and Renaming a Table from a TTS Backup**

```
# Using fully qualified table names:
mysqlbackup --socket=/tmp/restoreserver.sock \
   --backup-dir=/BackupDirTemp --backup-image=/home/user/dbadmin/backups/tts-backup.mbi \
  --include-tables="^sales\.cars" --rename="sales.cars to sales.autos" copy-back-and-apply-log

# It works the same if database names are omitted in the argument for --rename:
mysqlbackup --socket=/tmp/restoreserver.sock \
  --backup-dir=/BackupDirTemp --backup-image=/home/user/dbadmin/backups/tts-backup.mbi \
  --include-tables="^sales\.cars" --rename="cars to autos" copy-back-and-apply-log

# A table can be restored into another database; the target database is created if it is not existing on the server:
mysqlbackup --socket=/tmp/restoreserver.sock \
  --backup-dir=/BackupDirTemp --backup-image=/home/user/dbadmin/backups/tts-backup.mbi \
  --include-tables="^sales\.cars" --rename="sales.cars to new_sales.autos" copy-back-and-apply-log
```