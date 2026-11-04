---
title: "4.2.4 Restoring a Database"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/mysqlbackup.restore.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

### 4.2.4 Restoring a Database

To restore a MySQL instance from a backup to a database server:

- Shut down the database server.
- Delete all files inside the server's data directory. Also delete all files inside the directories specified by the [`--innodb_data_home_dir`](server-repository-options.md), [`--innodb_log_group_home_dir`](server-repository-options.md), and [`--innodb_undo_directory`](server-repository-options.md) options for restore, if the directories are different from the data directory.
- Use, for example, the [`copy-back-and-apply-log`](backup-commands-restore.md) command, which converts the raw backup into a prepared backup by updating it to a consistent state, and then copies the tables, indexes, metadata, and any other required files onto a target server. For the various options that you can specify for this operation, see [Section 19.3, “Restore Operations”](backup-commands-restore.md).

In the illustration below, the single-file backup created in the example given in [Section 4.2.2, “Backing Up an Entire MySQL Instance”](mysqlbackup.backup.md) is restored using the [`copy-back-and-apply-log`](backup-commands-restore.md) command. The following options are used:

- [`--datadir`](server-repository-options.md) supplies the location of the data directory for restoring the data. You must specify this option for any restore operation, either at the command line or in a defaults file.
- [`--backup-image`](backup-repository-options.md) provides the path of the single-file backup.
- [`--backup-dir`](backup-repository-options.md) provides the location of an empty folder to store some temporary files created during the restore procedure.

```
$ mysqlbackup --datadir=/home/admin/mysql/mysql-datadir \
  --backup-image=/home/meb/mysql/backups/testback3.mbi --backup-dir=/home/meb/mysql/backup-tmp2 \
    copy-back-and-apply-log
MySQL Enterprise Backup  Ver 8.4.0-commercial for Linux on x86_64 (MySQL Enterprise - Commercial)
Copyright (c) 2003, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Starting with following command line ...
mysqlbackup
--datadir=/home/admin/mysql/mysql-datadir
--backup-image=/home/meb/mysql/backups/testback3.mbi
--backup-dir=/home/meb/mysql/backup-tmp2
copy-back-and-apply-log

IMPORTANT: Please check that mysqlbackup run completes successfully.
           At the end of a successful 'copy-back-and-apply-log' run mysqlbackup
           prints "mysqlbackup completed OK!".

240426 13:17:07 MAIN     INFO: Backup Image MEB version string: 8.4.0
240426 13:17:07 MAIN     INFO: MySQL server version is '8.4.0'
240426 13:17:07 MAIN     INFO: Backup directory created: '/home/meb/mysql/backup-tmp2'
240426 13:17:07 MAIN  WARNING: If you restore to a server of a different version, the innodb_data_file_path parameter might have a different default. In that case you need to add 'innodb_data_file_path=ibdata1:12M:autoextend' to the target server configuration.
240426 13:17:07 MAIN     INFO: MEB logfile created at /home/meb/mysql/backup-tmp2/meta/MEB_2024-04-26.13-17-07_copy-back-and-apply-log.log

240426 13:17:07 MAIN     INFO: The backup image has no keyring.
--------------------------------------------------------------------
                       Server Repository Options:
--------------------------------------------------------------------
  datadir                        = /home/admin/mysql/mysql-datadir
  innodb_data_home_dir           = /home/admin/mysql/mysql-datadir
  innodb_data_file_path          = ibdata1:12M:autoextend
  innodb_log_group_home_dir      = /home/admin/mysql/mysql-datadir
  innodb_undo_directory          = /home/admin/mysql/mysql-datadir
  innodb_undo_tablespaces        = 2
  innodb_buffer_pool_filename    = ib_buffer_pool
  innodb_page_size               = Null
  innodb_checksum_algorithm      = crc32

--------------------------------------------------------------------
                       Backup Config Options:
--------------------------------------------------------------------
  datadir                        = /home/meb/mysql/backup-tmp2/datadir
  innodb_data_home_dir           = /home/meb/mysql/backup-tmp2/datadir
  innodb_data_file_path          = ibdata1:12M:autoextend
  innodb_log_group_home_dir      = /home/meb/mysql/backup-tmp2/datadir
  innodb_undo_directory          = /home/meb/mysql/backup-tmp2/datadir
  innodb_undo_tablespaces        = 2
  innodb_buffer_pool_filename    = ib_buffer_pool
  innodb_page_size               = 16384
  innodb_checksum_algorithm      = crc32

240426 13:17:07 MAIN     INFO: Creating 14 buffers each of size 16777216.
240426 13:17:07 MAIN     INFO: Copy-back-and-apply-log from image operation starts with following threads
                               1 read-threads    6 process-threads    1 write-threads
240426 13:17:07 RDR1     INFO: Copying ibdata1.
240426 13:17:07 PCR3     INFO: Copying database directory: meta
240426 13:17:07 RDR1     INFO: Copying undo_002.
240426 13:17:07 RDR1     INFO: Copying undo_001.
240426 13:17:07 RDR1     INFO: Copying sys/sys_config.ibd.
240426 13:17:07 RDR1     INFO: Copying pets/cats.ibd.
240426 13:17:07 RDR1     INFO: Copying mysql/backup_progress.ibd.
240426 13:17:07 RDR1     INFO: Copying mysql/backup_history.ibd.
240426 13:17:07 RDR1     INFO: Copying mysql.ibd.
240426 13:17:07 PCR1     INFO: Copying database directory: mysql
240426 13:17:07 PCR1     INFO: Copying database directory: performance_schema
240426 13:17:08 PCR5     INFO: Copying database directory: pets
240426 13:17:08 PCR5     INFO: Copying database directory: sys
240426 13:17:08 RDR1     INFO: Binary Log Basename: 'binlog'
240426 13:17:08 RDR1     INFO: Binlog Log Index:    '/home/admin/mysql/mysql-datadir/binlog.index'
240426 13:17:08 RDR1     INFO: Copying binlog.000001.
240426 13:17:08 MAIN     INFO: read_backup_variables_txt_file: '/home/meb/mysql/backup-tmp2/meta/backup_variables.txt'
240426 13:17:08 MAIN     INFO: backup variable mysql_version=8.4.0-commercial
240426 13:17:08 MAIN     INFO: MySQL server version is '8.4.0-commercial'
240426 13:17:08 MAIN     INFO: Restoring ...8.4.0-commercial version
240426 13:17:08 MAIN     INFO: backup variable meb_version=8.4.0
240426 13:17:08 MAIN     INFO: backup variable start_lsn=20525056
240426 13:17:08 MAIN     INFO: backup variable last_checkpoint=20525419
240426 13:17:08 MAIN     INFO: backup variable end_lsn=20531571
240426 13:17:08 MAIN     INFO: backup variable apply_log_done=0
240426 13:17:08 MAIN     INFO: backup variable is_incremental=0
240426 13:17:08 MAIN     INFO: backup variable is_incremental_with_redo_log_only=0
240426 13:17:08 MAIN     INFO: backup variable is_partial=0
240426 13:17:08 MAIN     INFO: backup variable is_compressed=0
240426 13:17:08 MAIN     INFO: backup variable is_skip_binlog=0
240426 13:17:08 MAIN     INFO: backup variable is_skip_relaylog=0
240426 13:17:08 MAIN     INFO: backup variable is_skip_unused_pages=0
240426 13:17:08 MAIN     INFO: backup variable is_onlyinnodb=0
240426 13:17:08 MAIN     INFO: backup variable binlog_position=binlog.000001:3807
240426 13:17:08 MAIN     INFO: backup variable binlog_index=binlog.index
240426 13:17:08 MAIN     INFO: backup variable has_tde_tables=0
240426 13:17:08 MAIN     INFO: backup variable start_time_utc=1714150880468548
240426 13:17:08 MAIN     INFO: backup variable end_time_utc=1714150884925922
240426 13:17:08 MAIN     INFO: backup variable consistency_time_utc=1714150884898388
240426 13:17:08 MAIN     INFO: backup variable mysql_version_comment=MySQL Enterprise Server - Commercial
240426 13:17:08 MAIN     INFO: backup variable log_bin_name=binlog
240426 13:17:08 MAIN     INFO: backup variable log_bin_index_name=binlog
240426 13:17:08 MAIN     INFO: backup variable innodb_undo_files_count=2
240426 13:17:08 MAIN     INFO: Copy-back operation completed successfully.
240426 13:17:08 MAIN     INFO: Source Image Path = /home/meb/mysql/backups/testback3.mbi

240426 13:17:08 MAIN     INFO: read_backup_variables_txt_file: '/home/meb/mysql/backup-tmp2/meta/backup_variables.txt'
240426 13:17:08 MAIN     INFO: backup variable mysql_version=8.4.0-commercial
240426 13:17:08 MAIN     INFO: MySQL server version is '8.4.0-commercial'
240426 13:17:08 MAIN     INFO: Restoring ...8.4.0-commercial version
240426 13:17:08 MAIN     INFO: backup variable meb_version=8.4.0
240426 13:17:08 MAIN     INFO: backup variable start_lsn=20525056
240426 13:17:08 MAIN     INFO: backup variable last_checkpoint=20525419
240426 13:17:08 MAIN     INFO: backup variable end_lsn=20531571
240426 13:17:08 MAIN     INFO: backup variable apply_log_done=0
240426 13:17:08 MAIN     INFO: backup variable is_incremental=0
240426 13:17:08 MAIN     INFO: backup variable is_incremental_with_redo_log_only=0
240426 13:17:08 MAIN     INFO: backup variable is_partial=0
240426 13:17:08 MAIN     INFO: backup variable is_compressed=0
240426 13:17:08 MAIN     INFO: backup variable is_skip_binlog=0
240426 13:17:08 MAIN     INFO: backup variable is_skip_relaylog=0
240426 13:17:08 MAIN     INFO: backup variable is_skip_unused_pages=0
240426 13:17:08 MAIN     INFO: backup variable is_onlyinnodb=0
240426 13:17:08 MAIN     INFO: backup variable binlog_position=binlog.000001:3807
240426 13:17:08 MAIN     INFO: backup variable binlog_index=binlog.index
240426 13:17:08 MAIN     INFO: backup variable has_tde_tables=0
240426 13:17:08 MAIN     INFO: backup variable start_time_utc=1714150880468548
240426 13:17:08 MAIN     INFO: backup variable end_time_utc=1714150884925922
240426 13:17:08 MAIN     INFO: backup variable consistency_time_utc=1714150884898388
240426 13:17:08 MAIN     INFO: backup variable mysql_version_comment=MySQL Enterprise Server - Commercial
240426 13:17:08 MAIN     INFO: backup variable log_bin_name=binlog
240426 13:17:08 MAIN     INFO: backup variable log_bin_index_name=binlog
240426 13:17:08 MAIN     INFO: backup variable innodb_undo_files_count=2
240426 13:17:08 MAIN     INFO: Creating 14 buffers each of size 65536.
240426 13:17:08 MAIN     INFO: Apply-log operation starts with following threads
                               1 read-threads    1 process-threads    6 apply-threads
240426 13:17:08 MAIN     INFO: Using up to 100 MB of memory.
240426 13:17:08 MAIN     INFO: ibbackup_logfile's creation parameters:
          start lsn 20525056, end lsn 20531571,
          start checkpoint 20525419.
240426 13:17:08 MAIN     INFO: Loading the space id : 0, space name : /home/admin/mysql/mysql-datadir/ibdata1.
240426 13:17:08 MAIN     INFO: Loading the space id 4 name '/home/admin/mysql/mysql-datadir/mysql/backup_history.ibd'.
240426 13:17:08 MAIN     INFO: Loading the space id 3 name '/home/admin/mysql/mysql-datadir/mysql/backup_progress.ibd'.
240426 13:17:08 MAIN     INFO: Loading the space id 2 name '/home/admin/mysql/mysql-datadir/pets/cats.ibd'.
240426 13:17:08 MAIN     INFO: Loading the space id 1 name '/home/admin/mysql/mysql-datadir/sys/sys_config.ibd'.
240426 13:17:08 MAIN     INFO: Loading the space id 4294967294 name '/home/admin/mysql/mysql-datadir/mysql.ibd'.
240426 13:17:08 MAIN     INFO: Loading the space id 4294967279 name '/home/admin/mysql/mysql-datadir/undo_001'.
240426 13:17:08 MAIN     INFO: Loading the space id 4294967278 name '/home/admin/mysql/mysql-datadir/undo_002'.
240426 13:17:08 PCR1     INFO: Starting to parse redo log at lsn = 20525297, whereas checkpoint_lsn = 20525419 and start_lsn = 20525056.
240426 13:17:08 PCR1     INFO: Doing recovery: scanned up to log sequence number 20531571.
240426 13:17:08 PCR1     INFO: Starting to apply a batch of log records to the database....
InnoDB: Progress in percent: 7 14 21 28 35 
240426 13:17:08 PCR1     INFO: Create redo log files. target start_lsn 0 last_checkpoint 0 end_lsn 0
240426 13:17:08 PCR1     INFO: Create redo log files. source start_lsn 20525056 last_checkpoint 20525419 end_lsn 20531571
240426 13:17:08 PCR1     INFO: Updating last checkpoint to 20525419 in redo log
240426 13:17:08 PCR1     INFO: We were able to parse ibbackup_logfile up to lsn 20531571.
240426 13:17:08 PCR1     INFO: Last MySQL binlog file position 0 3807, file name binlog.000001
240426 13:17:08 PCR1     INFO: The first data file is '/home/admin/mysql/mysql-datadir/ibdata1'
                               and the new created log files are at '/home/admin/mysql/mysql-datadir'
240426 13:17:08 MAIN     INFO: Apply-log operation completed successfully.
240426 13:17:08 MAIN     INFO: Full Backup has been restored successfully.

mysqlbackup completed OK! with 1 warnings
```

Now the original database directory is restored from the backup.

**Starting the Restored Server.** When the following InnoDB settings are different on the backed-up and the restored server, it is important to configure the restored server with the settings from the backed up server (otherwise, your restored server might not start):

If you are not sure about those settings for your backed-up server, they were actually stored in the `backup-my.cnf` file during the backup—you can find the file either in the temporary directory you specified with [`--backup-dir`](backup-repository-options.md) when you restored the single-image backup, or in a backup directory you could create by unpacking the backup image using the [`extract`](backup-commands-single-file.md) command. If the values of these options differ from those on the target server, add them to the configuration file you are using to start the target server afterwards; alternatively, you can also supply them as command line options to **mysqld**.

Depending on how you are going to start the restored server, you might need to adjust the ownership of the restored data directory. For example, if the server is going to be started by the user `mysql`, use the following command to change the owner attribute of the data directory and the files under it to the `mysql` user, and the group attribute to the `mysql` group.

```
$ chown -R mysql:mysql /path/to/datadir
```

You are now ready to start the restored database server. For more discussions on how to perform different kinds of restores, see [Section 5.1, “Performing a Restore Operation”](restore.md).