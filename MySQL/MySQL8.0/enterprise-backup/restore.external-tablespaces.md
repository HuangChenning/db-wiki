---
title: "5.1.6 Restoring External InnoDB Tablespaces to Different Locations"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/restore.external-tablespaces.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 5.1.6 Restoring External InnoDB Tablespaces to Different Locations

When a backup contains external InnoDB tablespaces that resided outside of the backed-up server's data directory, you can restore them to locations different from their original ones by updating their path names in the [tablespace\_tracker](meb-files-backed-up-summary.md) file inside the backup; see description of the file in [Table 1.1, “Types of Files in a Backup”](meb-files-backed-up-summary.md) for details.