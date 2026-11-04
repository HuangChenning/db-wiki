---
title: "5.4 Restoring a Backup with a Database Server Upgrade or Downgrade"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/restore-upgrade.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

Important

You may encounter technical challenges during a server upgrade or downgrade, and it is beyond the function of MySQL Enterprise Backup, as a backup tool, to ensure a successful server upgrade or downgrade. Users interested in the topic are advised to consult the MySQL server manual, especially the [Upgrading MySQL](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/upgrading.html) and [Downgrading MySQL](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/downgrading.html) sections, and pay careful attention to the requirements and restrictions discussed there.

You can facilitate a server upgrade or downgrade by using MySQL Enterprise Backup to make a backup of your data from a *source server*, restore it to a new *target server*, and, after some preparations, start a different version of MySQL Server on the restored data (see [In-Place Upgrade](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/upgrade-binary-package.html#upgrade-procedure-inplace) for details and limitaions). Here are a number of things that users should pay attention to when restoring a backup with a database server upgrade or downgrade:

- *Restoring a database server with a server downgrade* should only be performed when the MySQL servers on the source and the target servers are in the same release series. Downgrading to a lower series (for example, from 9.7 to 8.0) might cause server crashes or data corruption.
- *Restoring a database server with a server upgrade* requires the following steps, the skipping of any of which might crash the restored server:
	1. Back up the data on the source server.
	2. Using *the same version of MySQL Enterprise Backup with which the backup was taken*, restore the data to the target server by running a [`copy-back-and-apply-log`](backup-commands-restore.md) operation on the backup.
	3. Install on the target server *the same version of MySQL Server that was running on the source server when your backup was created*.
	4. Start the MySQL Server you just installed. Your restored data go through an abbreviated [crash recovery](glossary.md) process in preparation for a server upgrade.
	5. Perform a slow shutdown of the MySQL Server you just started in the last step by issuing the `SET                   GLOBAL innodb_fast_shutdown=0` statement and then shutting the server down. This ensures that all dirty pages are flushed, and hence there will be no redo log processing later for the upgraded server.
	6. Install the newer MySQL Server version on the target server.
	7. Start the newer MySQL Server version you just installed on the data directory you have restored and prepared in the earlier steps.
	8. Perform any other additional [upgrade steps](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/upgrading.html) that might be required for your platform or distribution as documented in the MySQL reference manual.
	After performing these steps, check your data to make sure that your restore has been successful.