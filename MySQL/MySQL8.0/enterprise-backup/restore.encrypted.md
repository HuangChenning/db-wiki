---
title: "5.1.2 Restoring an Encrypted Backup Image"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/restore.encrypted.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 5.1.2 Restoring an Encrypted Backup Image

Restore an encrypted backup image named *`<image_name>`* to *`<restoreDir>`* on the server with [`copy-back-and-apply-log`](backup-commands-restore.md), using the encryption key contained in a file named *`<keyFile>`*:

**Example 5.5 Restoring an Encrypted Backup Image**

```
mysqlbackup --defaults-file=<my.cnf> --backup-image=<image_name> \
 --backup-dir=<backupTmpDir> --datadir=<restoreDir> --decrypt --key-file=<keyFile> copy-back-and-apply-log
```

See [Section 20.13, “Encryption Options”](backup-encryption-options.md) for more details on backup encryption and decryption.