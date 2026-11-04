---
title: "4.2.2 Backing Up an Entire MySQL Instance"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/mysqlbackup.backup.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

### 4.2.2 Backing Up an Entire MySQL Instance

In the following illustration, we back up an entire MySQL instance to a single file using the [`backup-to-image`](backup-commands-backup.md) command, which appears at the end of the sample command. We specify some of the connection information for the database using the `--user` and `--host` options (and, with the `--password` option, tell **mysqlbackup** to prompt for a user password). The location and filename for the single-file backup is specified using the [`--backup-image`](backup-repository-options.md) option, and the location for an empty folder to store temporary files is supplied with the [`--backup-dir`](backup-repository-options.md) option.

The output echoes all the parameters used by the backup operation, including several that are retrieved automatically using the database connection. The unique ID for this backup job is recorded in special tables that **mysqlbackup** creates inside the MySQL instance, allowing you to monitor long-running backups and view information on previous backups. The final output section repeats the location of the backup data and provides the [LSN](glossary.md) values that you might use when you perform an [incremental backup](glossary.md) next time over the [full backup](glossary.md) that has just been made.

```
$ mysqlbackup --user=mysqlbackup --password --host=127.0.0.1 --backup-dir=/home/meb/mysql/backup-temp \
   --backup-image=/home/meb/mysql/backups/testback3.mbi --with-timestamp backup-to-image
MySQL Enterprise Backup  Ver 8.4.0-commercial for Linux on x86_64 (MySQL Enterprise - Commercial)
Copyright (c) 2003, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Starting with following command line ...
mysqlbackup
--user=mysqlbackup
--password
--host=127.0.0.1
--backup-dir=/home/meb/mysql/backup-temp
--backup-image=/home/meb/mysql/backups/testback3.mbi
--with-timestamp
backup-to-image

IMPORTANT: Please check that mysqlbackup run completes successfully.
           At the end of a successful 'backup-to-image' run mysqlbackup
           prints "mysqlbackup completed OK!".

Enter password: 
240426 13:01:23 MAIN     INFO: Establishing connection to server.
240426 13:01:23 MAIN     INFO: No SSL options specified.
240426 13:01:23 MAIN     INFO: MySQL server version is '8.4.0-commercial'
240426 13:01:23 MAIN     INFO: MySQL server compile os version is 'Linux'
240426 13:01:23 MAIN     INFO: SSL/TLS version used for connection is TLSv1.3
240426 13:01:23 MAIN     INFO: Got some server configuration information from running server.

240426 13:01:23 MAIN     INFO: Establishing connection to server for locking.
240426 13:01:23 MAIN     INFO: No SSL options specified.
240426 13:01:23 MAIN     INFO: Backup directory created: '/home/meb/mysql/backup-temp/2024-04-26_13-01-23'
240426 13:01:23 MAIN     INFO: MySQL server version_comment is 'MySQL Enterprise Server - Commercial'
240426 13:01:23 MAIN     INFO: Mysqlbackup component not installed.
240426 13:01:23 MAIN     INFO: MEB logfile created at /home/meb/mysql/backup-temp/2024-04-26_13-01-23/meta/MEB_2024-04-26.13-01-23_backup-to-image.log

240426 13:01:23 MAIN     INFO: The MySQL server has no active keyring.
--------------------------------------------------------------------
                       Server Repository Options:
--------------------------------------------------------------------
  datadir                        = /home/admin/mysql/mysql-datadir/
  innodb_data_home_dir           = 
  innodb_data_file_path          = ibdata1:12M:autoextend
  innodb_log_group_home_dir      = /home/admin/mysql/mysql-datadir/
  innodb_undo_directory          = /home/admin/mysql/mysql-datadir/
  innodb_undo_tablespaces        = 2
  innodb_buffer_pool_filename    = ib_buffer_pool
  innodb_page_size               = 16384
  innodb_checksum_algorithm      = crc32

--------------------------------------------------------------------
                       Backup Config Options:
--------------------------------------------------------------------
  datadir                        = /home/meb/mysql/backup-temp/2024-04-26_13-01-23/datadir
  innodb_data_home_dir           = /home/meb/mysql/backup-temp/2024-04-26_13-01-23/datadir
  innodb_data_file_path          = ibdata1:12M:autoextend
  innodb_log_group_home_dir      = /home/meb/mysql/backup-temp/2024-04-26_13-01-23/datadir
  innodb_undo_directory          = /home/meb/mysql/backup-temp/2024-04-26_13-01-23/datadir
  innodb_undo_tablespaces        = 2
  innodb_buffer_pool_filename    = ib_buffer_pool
  innodb_page_size               = 16384
  innodb_checksum_algorithm      = crc32

Backup Image Path = /home/meb/mysql/backups/testback3.mbi
240426 13:01:23 MAIN     INFO: Unique generated backup id for this is 17141508838810794

240426 13:01:23 MAIN     INFO: Copying the server config file '/home/admin/mysql/mysql-datadir/auto.cnf'
240426 13:01:23 MAIN     INFO: Creating 14 buffers each of size 16777216.
240426 13:01:23 MAIN     INFO: The server is not configured for redo log archiving. The system variable innodb_redo_log_archive_dirs is not set.
240426 13:01:23 MAIN     INFO: Found checkpoint at lsn 20525419.
240426 13:01:23 MAIN     INFO: Starting log scan from lsn = 20525056 at offset = 870763 and checkpoint = 20525419 in file /home/admin/mysql/mysql-datadir/#innodb_redo/#ib_redo6.
240426 13:01:23 MAIN     INFO: Full Image Backup operation starts with following threads
                               1 read-threads    6 process-threads    1 write-threads
240426 13:01:23 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2024-04-26_13-01-23/backup-my.cnf.
240426 13:01:23 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2024-04-26_13-01-23/meta/backup_create.xml.
240426 13:01:23 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2024-04-26_13-01-23/datadir/backup-auto.cnf.
240426 13:01:23 RLP1     INFO: Starting to parse redo log at lsn = 20525297, whereas checkpoint_lsn = 20525419 and start_lsn = 20525056.
240426 13:01:23 RDR1     INFO: Starting to copy all innodb files...
240426 13:01:23 RDR1     INFO: Copying /home/admin/mysql/mysql-datadir/ibdata1.
240426 13:01:24 RDR1     INFO: Starting to copy all undo files...
240426 13:01:24 RDR1     INFO: Copying /home/admin/mysql/mysql-datadir/undo_002.
240426 13:01:24 RDR1     INFO: Copying /home/admin/mysql/mysql-datadir/undo_001.
240426 13:01:24 RDR1     INFO: Starting to lock instance for backup...
240426 13:01:24 RDR1     INFO: The server instance is locked for backup.
240426 13:01:24 RDR1     INFO: The server instance is unlocked after 0.003 seconds.
240426 13:01:24 RDR1     INFO: Copying /home/admin/mysql/mysql-datadir/sys/sys_config.ibd.
240426 13:01:24 RDR1     INFO: Copying /home/admin/mysql/mysql-datadir/pets/cats.ibd.
240426 13:01:24 RDR1     INFO: Copying /home/admin/mysql/mysql-datadir/mysql/backup_progress.ibd.
240426 13:01:24 RDR1     INFO: Copying /home/admin/mysql/mysql-datadir/mysql/backup_history.ibd.
240426 13:01:24 RDR1     INFO: Copying /home/admin/mysql/mysql-datadir/mysql.ibd.
240426 13:01:24 RDR1     INFO: Completing the copy of innodb files.
240426 13:01:24 RDR1     INFO: Requesting a dump of the InnoDB buffer pool
240426 13:01:24 RDR1     INFO: Waiting for the dump of the InnoDB buffer pool to complete
240426 13:01:24 RDR1     INFO: The dump of the InnoDB buffer pool completed
240426 13:01:24 RDR1     INFO: Binary Log Basename: '/home/admin/mysql/mysql-datadir/binlog'
240426 13:01:24 RDR1     INFO: Binary Log Index:    '/home/admin/mysql/mysql-datadir/binlog.index'
240426 13:01:24 RDR1     INFO: Relay Channel:      'group_replication_applier'
240426 13:01:24 RDR1     INFO: Relay Log Basename: '/home/admin/mysql/mysql-datadir/admin-XBox3-relay-bin-group_replication_applier'
240426 13:01:24 RDR1     INFO: Relay Channel:      'group_replication_recovery'
240426 13:01:24 RDR1     INFO: Relay Log Basename: '/home/admin/mysql/mysql-datadir/admin-XBox3-relay-bin-group_replication_recovery'
240426 13:01:24 RDR1     INFO: Starting to copy Binlog files.
240426 13:01:24 RDR1     INFO: Starting to lock instance for backup...
240426 13:01:24 RDR1     INFO: The server instance is locked for backup.
240426 13:01:24 RDR1     INFO: The MySQL server has no active keyring.
240426 13:01:24 RDR1     INFO: Requesting flush of redo log reading after LSN 20530626.
240426 13:01:24 RDR1     INFO: Requesting flush of redo log processing after LSN 20530626.
240426 13:01:24 RDR1     INFO: Completed flush of redo log reading after LSN 20531088.
240426 13:01:24 RDR1     INFO: Completed flush of redo log processing after LSN 20531088.
240426 13:01:24 RDR1     INFO: Starting to read-lock tables...
240426 13:01:24 RDR1     INFO: No tables to read-lock.
240426 13:01:24 RDR1     INFO: Opening backup source directory '/home/admin/mysql/mysql-datadir'
240426 13:01:24 RDR1     INFO: Starting to copy non-innodb files in subdirs of '/home/admin/mysql/mysql-datadir'
240426 13:01:24 WTR1     INFO: Adding database directory: datadir/mysql
240426 13:01:24 WTR1     INFO: Adding database directory: datadir/performance_schema
240426 13:01:24 RDR1     INFO: Completing the copy of all non-innodb files.
240426 13:01:24 WTR1     INFO: Adding database directory: datadir/pets
240426 13:01:24 WTR1     INFO: Adding database directory: datadir/sys
240426 13:01:24 RDR1     INFO: Requesting consistency information...
240426 13:01:24 RDR1     INFO: Locked the consistency point for 1902 microseconds.
240426 13:01:24 RDR1     INFO: Consistency point server_uuid 'c6d42eaa-03e9-11ef-ae5e-0800276c22b0'.
240426 13:01:24 RDR1     INFO: Consistency point gtid_executed ''.
240426 13:01:24 RDR1     INFO: Consistency point binary_log_file 'binlog.000001'.
240426 13:01:24 RDR1     INFO: Consistency point binary_log_position 3807.
240426 13:01:24 RDR1     INFO: Consistency point InnoDB lsn 20531571.
240426 13:01:24 RDR1     INFO: Consistency point InnoDB lsn_checkpoint 20525419.
240426 13:01:24 RDR1     INFO: Requesting completion of redo log copy after LSN 20531571.
240426 13:01:24 RLW1     INFO: A copied database page was modified at 20529721. (This is the highest lsn found on a page)
240426 13:01:24 RLW1     INFO: Scanned log up to lsn 20531571.
240426 13:01:24 RLW1     INFO: Was able to parse the log up to lsn 20531571.
240426 13:01:24 RLW1     INFO: Copied redo log
                               log_start_lsn    20525056
                               start_checkpoint 20525419
                               start_lsn        20525419
                               last_checkpoint  20525419
                               consistency_lsn  20531571
                               log_end_lsn      20531571
240426 13:01:24 RLR1     INFO: Redo log reader waited 87 times for a total of 435.00 ms for logs to generate.
240426 13:01:24 RDR1     INFO: Truncating binary log index '/home/meb/mysql/backup-temp/2024-04-26_13-01-23/datadir/binlog.index' to 16.
240426 13:01:24 RDR1     INFO: Truncating binary log 'binlog.000001' to 3807.
240426 13:01:24 RDR1     INFO: Copying /home/admin/mysql/mysql-datadir/binlog.000001.
240426 13:01:24 RDR1     INFO: Completed the copy of binlog files...
240426 13:01:24 RDR1     INFO: The server instance is unlocked after 0.130 seconds.
240426 13:01:24 RDR1     INFO: Reading all global variables from the server.
240426 13:01:24 RDR1     INFO: Completed reading of all 623 global variables from the server.
240426 13:01:24 RDR1     INFO: Writing server defaults files 'server-my.cnf' and 'server-all.cnf' for server '8.4.0-commercial' in '/home/meb/mysql/backup-temp/2024-04-26_13-01-23'.
240426 13:01:24 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2024-04-26_13-01-23/meta/backup_variables.txt.
240426 13:01:24 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2024-04-26_13-01-23/datadir/ibbackup_logfile.
240426 13:01:24 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2024-04-26_13-01-23/server-all.cnf.
240426 13:01:24 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2024-04-26_13-01-23/server-my.cnf.
240426 13:01:24 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2024-04-26_13-01-23/meta/backup_content.xml.
240426 13:01:24 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2024-04-26_13-01-23/meta/image_files.xml.
240426 13:01:24 MAIN     INFO: Full Image Backup operation completed successfully.
240426 13:01:24 MAIN     INFO: Backup image created successfully.
240426 13:01:24 MAIN     INFO: Image Path = /home/meb/mysql/backups/testback3.mbi
240426 13:01:24 MAIN     INFO: MySQL binlog position: filename binlog.000001, position 3807.

-------------------------------------------------------------
   Parameters Summary         
-------------------------------------------------------------
   Start LSN                  : 20525056
   Last Checkpoint LSN        : 20525419
   End LSN                    : 20531571
-------------------------------------------------------------

mysqlbackup completed OK!
```