---
title: "4.1.3 Designate a Location for the Backup Directory"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/backup-prep-storage.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 4.1.3 Designate a Location for the Backup Directory

Most **mysqlbackup** operations, including those on single-file backups, write data or metadata to a designated directory referred to as the “ [backup directory](glossary.md) ” in this manual. See the description for [`--backup-dir`](backup-repository-options.md) for details on its usage for different operations.

Choose in advance for this directory a location on a file system with sufficient storage; it could even be remotely mounted from a different server. You specify the path to this directory with the [`--backup-dir`](backup-repository-options.md) option for many **mysqlbackup** commands.

If you use the backup directory as a location to store your backups, it is preferable to keep each backup within a timestamped subdirectory underneath the main backup directory. To make **mysqlbackup** create these subdirectories automatically, specify the [`--with-timestamp`](backup-repository-options.md) option each time you run **mysqlbackup**.