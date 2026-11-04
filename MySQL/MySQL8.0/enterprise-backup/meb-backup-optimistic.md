---
title: "4.3.6 Making an Optimistic Backup"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/meb-backup-optimistic.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 4.3.6 Making an Optimistic Backup

Optimistic backup is a feature for improving performance for backing up and restoring huge databases in which only a small number of tables are modified frequently.

During a hot backup of a huge database (say, in the order of terabytes), huge redo log files could be generated on the server when the backup is in progress. As the redo log files grow faster than they can be processed by **mysqlbackup**, the backup operation can actually fail when **mysqlbackup** cannot catch up with the redo log cycles and LSNs get overwritten by the server before they are read by **mysqlbackup**. Moreover, the [`apply-log`](backup-commands-update.md) step for [preparing a backup for restoration](backup-apply-log.md) can take a very long time as **mysqlbackup** has huge `ibbackup_logfile` files (created from the big redo log files) to apply to the backup. The problems are intensified when the I/O resources available for reading and writing the redo logs are scarce during the backup and restoration processes.

Optimistic backup relieves the problems by dividing the backup process into two internal phases, which are transparent to the users:

1. Optimistic phase: In this first phase, tables that are unlikely to be modified during the backup process (referred to as the “inactive tables” below, identified by the user with the [`optimistic-time`](backup-capacity-options.md) option or, by exclusion, with the [`optimistic-busy-tables`](backup-capacity-options.md) option) are backed up without any locks on the MySQL instance. And because those tables are not expected to be changed before the backup is finished, redo logs, undo logs, and system table spaces are not backed up by **mysqlbackup** in this phase.
2. Normal phase: In this second phase, tables that are not backed up in the first phase (referred to as the “busy tables” below) are being backed up in a manner similar to how they are processed in an ordinary backup: the InnoDB files are copied first, and then other relevant files and copied or processed with various locks applied to the database at different times. The redo logs, undo logs, and the system tablespace are also backed up in this phase.

An optimistic backup occurs whenever the [`optimistic-time`](backup-capacity-options.md) or [`optimistic-busy-tables`](backup-capacity-options.md) option is used. For how to use the options, see detailed descriptions for them in [Section 20.10, “Performance / Scalability / Capacity Options”](backup-capacity-options.md). If, as expected, the list of inactive tables identified by the optimistic options do not change during the backup (or, even if it changes by a small percentage), most users will find that the overall backup time is reduced significantly compared to an ordinary backup, as the size of the redo log data to be backed up will be far smaller. Additionally, restore time for the backup will also be reduced, as the [`apply-log`](backup-commands-update.md) operation will be much faster because of the smaller redo log. However, if it turns out that the list of inactive tables identified changed by a significant portion during the backup process, benefits of performing an optimistic back up will become limited and, in the worst case, an optimistic backup might actually take longer to perform and, for a single-file backup, the size of the backup will be larger when comparing with an ordinary backup. Therefore, users should be careful in identifying which tables are “inactive” and which are “busy” when trying to perform an optimistic backup.

Notes

- An optimistic backup cannot be performed for an incremental backup or a backup using [transportable tablespaces (TTS)](glossary.md).
- Do not perform a DDL operation on the server in parallel with an optimistic backup, or the backup will fail.

The following examples illustrate how to make an optimistic backup.

**Example 4.24 Optimistic Backup Using the Option ``optimistic-time=*`YYMMDDHHMMSS`*``**

In this example, tables that have been modified since the noon of May 16, 2011 are treated as busy tables and backed up in the normal phase of an optimistic backup, and all other tables are backed up in the optimistic phase:

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf --optimistic-time=110516120000 \
  --backup-image=<image-name> --backup-dir=<temp-dir>  backup-to-image
```

**Example 4.25 Optimistic Backup Using the Option `optimistic-time=now`**

In this example, all tables are treated as inactive tables and backed up in the optimistic phase of an optimistic backup:

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf --optimistic-time=now \ 
 --backup-image=<image-name> --backup-dir=<temp-dir> backup-to-image
```

**Example 4.26 Optimistic Backup Using the `optimistic-busy-tables` Option**

In this example, tables in `mydatabase` that are prefixed by `mytables-` in their names are treated as busy tables and backed up in the normal phase of an optimistic backup, and all other tables are backed up in the optimistic phase:

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf --optimistic-busy-tables="^mydatabase\.mytables-.*" \
 --backup-image=<image-name> --backup-dir=<temp-dir> backup
```

When you use both the `optimistic-time` and `optimistic-busy-tables` options and they come into conflict on determining which tables are to be busy tables, `optimistic-busy-tables` takes precedence over `optimistic-time`. For example:

**Example 4.27 Optimistic and Partial Backup Using both the `optimistic-busy-tables` and `optimistic-time` Options**

In this example, tables in `mydatabase` that are prefixed by `mytables-` in their names are treated as busy tables and backed up in the normal phase, even if they have not been modified since May 16, 2010, the time specified by `optimistic-time`:

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf --optimistic-busy-tables="^mydatabase\.mytables-.*" \
  --optimistic-time=100516  --backup-image=<image-name> --backup-dir=<temp-dir>  backup
```

#### Using Optimistic Backups and Optimistic Incremental Backups Together

By utilizing optimistic backup and [optimistic incremental backup](mysqlbackup.incremental.md) together in your backup schedule, you can speed up backups for huge databases, especially when only a relatively small number of tables have been modified since a certain time and not many tables are being modified on a frequent basis. Below is a sample sequence of commands illustrating a weekly backup schedule that makes use of the two features; it also includes the steps for restoring the data to a certain day.

```
# A full optimistic backup performed on 2017/02/04, Sat, at 1130 PM.
# The --optimistic-time option is used to specify an optimistic time of 2016/08/16, 0800 PM 

mysqlbackup --defaults-file=/home/admin/my.cnf --optimistic-time=160816200000 \ 
  --backup-dir=/home/admin/temp_dir --backup-image=/home/admin/backups/mydb_full_201702042330.bi \
  --with-timestamp \
  backup-to-image  

# A sequence of optimistic incremental backups are then performed on each the following six days at 1130 PM
# On Sunday, 2017/02/05 
mysqlbackup --defaults-file=/home/admin/my.cnf \
  --incremental=optimistic --incremental-base=history:last_backup \
  --backup-dir=/home/admin/temp_dir \
  --backup-image=/home/admin/backups/mydb_incremental__201702052330.bi \
  --with-timestamp \
  backup-to-image
# On Monday, 2017/02/06
mysqlbackup --defaults-file=/home/admin/my.cnf \
  --incremental=optimistic --incremental-base=history:last_backup \
  --backup-dir=/home/admin/temp_dir \
  --backup-image=/home/admin/backups/mydb_incremental__201702062330.bi \
  --with-timestamp \
  backup-to-image
# On Tuesday, 2017/02/07
mysqlbackup --defaults-file=/home/admin/my.cnf \
  --incremental=optimistic --incremental-base=history:last_backup \
  --backup-dir=/home/admin/temp_dir \
  --backup-image=/home/admin/backups/mydb_incremental__201702072330.bi \
  --with-timestamp \
  backup-to-image
# On Wednesday, 2017/02/08
mysqlbackup --defaults-file=/home/admin/my.cnf \
  --incremental=optimistic --incremental-base=history:last_backup \
  --backup-dir=/home/admin/temp_dir \
  --backup-image=/home/admin/backups/mydb_incremental__201702082330.bi \
  --with-timestamp backup-to-image
# On Thursday, 2017/02/09
mysqlbackup --defaults-file=/home/admin/my.cnf \
  --incremental=optimistic --incremental-base=history:last_backup \
  --backup-dir=/home/admin/temp_dir \
  --backup-image=/home/admin/backups/mydb_incremental__201702092330.bi \
  --with-timestamp \
  backup-to-image
# On Friday, 2017/02/10
mysqlbackup --defaults-file=/home/admin/my.cnf \
  --incremental=optimistic --incremental-base=history:last_backup \
  --backup-dir=/home/admin/temp_dir \
  --backup-image=/home/admin/backups/mydb_incremental__201702102330.bi \
  --with-timestamp \
  backup-to-image

# Another full optimistic backup is performed on Saturday, 2017/02/11
mysqlbackup --defaults-file=/home/dbadmin/my.cnf --optimistic-time=110516200000 \  
 --backup-dir=/home/admin/temp_dir --backup-image=/home/admin/backups/mydb_full_201702112330.bi \
  --with-timestamp \
  backup-to-image

# Restore the database to its state at Tuesday, 2017/02/07, at 11:30 PM
# First, restore the full optimistic backup taken on the Saturday before, which was 2017/02/04:
mysqlbackup --defaults-file=/etc/my.cnf --backup-image=/home/admin/backups/mydb_full_201702042330.bi \
  --backup-dir=/home/admin/temp_dir --datadir=/var/lib/mysql \
  --with-timestamp \
  copy-back-and-apply-log
# Next, restore the optimistic incremental taken on the Sunday, Monday, and Tuesday that follow:  
mysqlbackup --defaults-file=/etc/my.cnf --backup-image=/home/admin/backups/mydb_incremental__201702052330.bi \
  --backup-dir=/home/admin/temp_dir --datadir=/var/lib/mysql --incremental \
  --with-timestamp \
  copy-back-and-apply-log
mysqlbackup --defaults-file=/etc/my.cnf --backup-image=/home/admin/backups/mydb_incremental__201702062330.bi \
  --backup-dir=/home/admin/temp_dir --datadir=/var/lib/mysql --incremental \
  --with-timestamp \
  copy-back-and-apply-log
mysqlbackup --defaults-file=/etc/my.cnf --backup-image=/home/admin/backups/mydb_incremental__201702072330.bi \
  --backup-dir=/home/admin/temp_dir --datadir=/var/lib/mysql --incremental \
  --with-timestamp \
  copy-back-and-apply-log
```