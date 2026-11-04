---
title: "Appendix A Frequently Asked Questions for MySQL Enterprise Backup"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/meb-faq.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

This section lists some common questions about MySQL Enterprise Backup, with answers and pointers to further information.

**Questions**

- A.1: What versions of the MySQL server does MySQL Enterprise Backup 8.0.46 support?
- A.2: What is the big `ibdata` file that is in all the backups?
- A.3: Can I back up non-InnoDB data with MySQL Enterprise Backup?
- A.4: What happens if the apply-log or apply-incremental-backup step is interrupted?
- A.5: Why is the option `--defaults-file` not recognized?
- A.6: Can I back up a database server on one OS platform and restore it on another one using MySQL Enterprise Backup?
- A.7: What if I have included the binary log or relay log in my backup but do not want to restore it?
- A.8: What would happen if I start a server directly using a raw directory backup, without running either the copy-back or the apply-log operation?

**Questions and Answers**

**A.1:** **What versions of the MySQL server does MySQL Enterprise Backup 8.0.46 support?**

See [Section C.3, “Compatibility with MySQL Versions”](bugs.compatibility.md) for details of compatibility between different releases of MySQL Enterprise Backup and MySQL Server.

**A.2:** **What is the big `ibdata` file that is in all the backups?**

You might find your backup data taking more space than expected because of a large file with a name such as `ibdata1`. This file represents the InnoDB [system tablespace](glossary.md), which grows but never shrinks as a database server operates, and is included in every full and incremental backup. To reduce the space taken up by this file in your backup data:

- After doing a [full backup](glossary.md), do a succession of [incremental backups](glossary.md), which take up less space. The `ibdata1` file in the incremental backups is typically much smaller, containing only the portions of the system tablespace that changed since the full backup.
- Set the configuration option [`innodb_file_per_table=1`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#sysvar_innodb_file_per_table) before creating your biggest or most active InnoDB tables. Those tables are split off from the system tablespaces into separate `.ibd` files; the tables can then be individually included or excluded from backups, and disk space is freed when the tables are dropped or truncated.
- If your system tablespace is very large because you created a high volume of InnoDB data before turning on the [`innodb_file_per_table`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#sysvar_innodb_file_per_table) setting, you might use **mysqldump** to create a dump of your entire server instance, then turn on [`innodb_file_per_table`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#sysvar_innodb_file_per_table) before re-creating the databases, so that all the table data is kept outside the system tablespace.

**A.3:** **Can I back up non-InnoDB data with MySQL Enterprise Backup?**

While MySQL Enterprise Backup can back up non-InnoDB data (like MYISAM tables), the MySQL server to be backed up must support InnoDB (i.e., the backup process will fail if the server was started up with the [`--innodb=OFF`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#option_mysqld_innodb) or [`--skip-innodb`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#option_mysqld_innodb) option), and the server must contain at least one InnoDB table.

**A.4:** **What happens if the apply-log or apply-incremental-backup step is interrupted?**

If **mysqlbackup** is interrupted during the [`apply-log`](backup-commands-update.md) or [`apply-incremental-backup`](backup-commands-update.md) stage, the backup data is OK. The file operations performed by those options can be performed multiple times without harming the consistency of the backup data. Just run the same **mysqlbackup** command again, and when it completes successfully, all the necessary changes are present in the backup data.

**A.5:** **Why is the option `--defaults-file` not recognized?**

When you specify the [`--defaults-file`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/option-file-options.html#option_general_defaults-file) option, it must be the first option going after **mysqlbackup**. Otherwise, the error message makes it look as if the option name is not recognized.

**A.6:** **Can I back up a database server on one OS platform and restore it on another one using MySQL Enterprise Backup?**

See [Section C.2, “Cross-Platform Compatibility”](platforms.compatibility.md) for details.

**A.7:** **What if I have included the binary log or relay log in my backup but do not want to restore it?**

If you want to skip the restore of the binary log, relay log, or both during a restore, use the [`--skip-binlog`](backup-capacity-options.md) option, the [`--skip-relaylog`](backup-capacity-options.md) option, or both with your [`copy-back`](backup-commands-restore.md) or [`copy-back-and-apply-log`](backup-commands-restore.md) command.

**A.8:** **What would happen if I start a server directly using a raw directory backup, without running either the copy-back or the apply-log operation?**

*This should never be attempted.* Not only would the server crash, but the backup would likely get corrupted and become unusable. This is because the directory backup contains metadata created by **mysqlbackup** that the MySQL server would not understand; also, the raw backup might be inconsistent and need to be brought up-to-date by an [apply-log operation](backup-commands-update.md), so that changes made to the database server during the backup process can be applied.