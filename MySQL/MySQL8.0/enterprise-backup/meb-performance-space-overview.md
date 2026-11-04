---
title: "1.2 Overview of Backup Types"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/meb-performance-space-overview.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

When it comes to formulating your backup strategy, performance and storage space are the key considerations. You want the backup to complete quickly, with as little CPU overhead on the database server as possible. You also want the backup data to be compact, so you can keep multiple backups on hand to restore at a moment's notice. Transferring the backup data to a different system should be quick and convenient. Under such considerations, various strategies for backing up your database often give you different advantages, for the different trade-offs you make when choosing a particular strategy. To choose the strategy that best fits your needs, you have to understand the nature of each kind of backups that MySQL Enterprise Backup can perform, for which this section is giving a brief overview.

### Kinds of backups according to the level of service disruption

Depending on how the database operations would be disrupted during a backup, the backup is classified as “hot,”“warm,” or “cold”:

- *Very Low to Low Level of Disruption:* A [hot backup](glossary.md) is a backup performed while the database is running. This type of backups does not block normal database operations. It captures even changes that occur while the backup is happening. Comparing to the other backup types, it causes the least disruption to the database server, and it is a desirable backup option when you want to avoid taking your application, web site, or web service offline. However, before a hot backup can be restored, there needs to be an extra process of preparing the backup to make it consistent (i.e., correctly reflecting the state of the state of the database at the time the backup was completed). See [Section 5.1.7, “Advanced: Preparing and Restoring a Directory Backup”](backup-apply-log.md) for more explanations.
	When connected to a running MySQL server, MySQL Enterprise Backup performs hot backup for InnoDB tables.
- *Medium to High Level of Disruption:* A [warm backup](glossary.md) is a backup performed with the database put under a read-only state. This type of backups blocks any write operations to the tables during the backup process, but still allow tables to be read.
	When connected to a running MySQL server, MySQL Enterprise Backup backs up all MyISAM and other non-InnoDB tables using the [warm backup](glossary.md) technique after all InnoDB tables have already been backed up with the [hot backup](glossary.md) method. Therefore, to back up as much data as possible during the hot backup phase, you should designate InnoDB as the default storage engine for new tables (which is the default setting for MySQL servers), or convert existing tables to use the InnoDB storage engine.
- *High to Very High Level of Disruption:* A [cold backup](glossary.md) is a backup created while the database is stopped. It is very disruptive to a database service. *MySQL Enterprise Backup 8.0 does not support [cold backups](glossary.md)*.

### Kinds of backups according to whether all data, or recent changes only are backed up

According to whether you want to include all data into your backup or only the recent changes, and according to recent changes since when, you can perform either a full backup, a differential backup, or an incremental backup. The three types of backups have different levels of requirements for CPU overhead and disk space, thus are suitable for different situations:

- A [full backup](glossary.md) includes the complete data from the database (except in cases where some tables are excluded with the [partial backup options](backup-partial-options.md)).
- A [differential backup](glossary.md) includes all changes to the data since the last full backup. It is faster than a full backup, saves storage space on the database server, and saves on network traffic when the backup is being transferred to a different server. However, it requires additional processing to make the backup ready for restore, which you can perform on a different system to minimize CPU overhead on the database server.
- An [Incremental backup](glossary.md) includes all changes to the data since the last backup. It offers similar advantages over a full backup as a differential backup does, and often to a even greater extent by further decreasing the backup size. But it might also require more preparations on a longer series of backups, before a restore can be performed.

### Compressed versus uncompressed backups

Backup compression saves you storage space and network traffic to transfer the backup data onto a different server. Compression does add some CPU overhead, but the overhead is algorithm dependent and it is fairly low for the default algorithm used by MySQL Enterprise Backup. Also, compression often reduces the IO overhead by a great deal, which might shorten the restore time, especially for slower IO devices. However, during the restore process, you need time for decompression and also storage space for both the compressed and decompressed data at the same time. So, take into account the additional storage space and the extra time needed during a restore when considering whether to create compressed backups.

When streaming backup data to another server, you might want to compress the backup either on the original server or the destination server, depending on which server has more spare CPU capacity and how much network traffic the compression could save.