---
title: "1.3.3 Files Backed up for Data Stored with MyISAM and Other Storage Engines"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/meb-files-backed-up-myisam.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 1.3.3 Files Backed up for Data Stored with MyISAM and Other Storage Engines

**mysqlbackup** also backs up the [.MYD files](glossary.md), [.MYI files](glossary.md), and the [.sdi](glossary.md) files associated with the MyISAM tables. Files with other extensions that are backed up are shown in [Table 1.1, “Types of Files in a Backup”](meb-files-backed-up-summary.md).

Note

While MySQL Enterprise Backup can back up non-InnoDB data (like MYISAM tables), the MySQL server to be backed up must support InnoDB (i.e., the backup process will fail if the server was started up with the [`--innodb=OFF`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#option_mysqld_innodb) or [`--skip-innodb`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#option_mysqld_innodb) option), and the server must contain at least one InnoDB table.

MyISAM tables and these other types of files cannot be backed up in the same non-blocking way as InnoDB tables can be. They can be backed up using the [warm backup](glossary.md) technique: changes to these tables are prevented while they are being backed up, possibly making the database unresponsive for a time, but no shutdown is required during the backup.