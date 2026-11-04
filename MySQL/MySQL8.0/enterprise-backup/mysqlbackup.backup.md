---
title: "4.2.2 Backing Up an Entire MySQL Instance"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/mysqlbackup.backup.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 4.2.2 Backing Up an Entire MySQL Instance

In the following example, we back up an entire MySQL instance to a single file using the [`backup-to-image`](backup-commands-backup.md) command, which appears at the end of the sample command. We specify some of the connection information for the database using the `--user` and `--host` options (and, with the `--password` option, tell **mysqlbackup** to prompt for a user password). The location and filename for the single-file backup is specified using the [`--backup-image`](backup-repository-options.md) option, and the location for an empty folder to store temporary files is supplied with the [`--backup-dir`](backup-repository-options.md) option.

The output echoes all the parameters used by the backup operation, including several that are retrieved automatically using the database connection. The unique ID for this backup job is recorded in special tables that **mysqlbackup** creates inside the MySQL instance, allowing you to monitor long-running backups and view information on previous backups. The final output section repeats the location of the backup data and provides the [LSN](glossary.md) values that you might use when you perform an [incremental backup](glossary.md) next time over the [full backup](glossary.md) that has just been made.

```
$ ./bin/mysqlbackup --user=mysqlbackup --password --host=127.0.0.1 --backup-dir=/home/meb/mysql/backup-temp \
   --backup-image=/home/meb/mysql/backups/testback3.mbi --with-timestamp backup-to-image
MySQL Enterprise Backup  Ver 8.0.31-commercial for Linux on x86_64 (MySQL Enterprise - Commercial)
Copyright (c) 2003, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Starting with following command line ...
./bin/mysqlbackup
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
220913 14:49:04 MAIN     INFO: Establishing connection to server.
220913 14:49:04 MAIN     INFO: No SSL options specified.
220913 14:49:04 MAIN     INFO: MySQL server version is '8.0.31-commercial'
220913 14:49:04 MAIN     INFO: MySQL server compile os version is 'Linux'
220913 14:49:04 MAIN     INFO: SSL/TLS version used for connection is TLSv1.3
220913 14:49:04 MAIN     INFO: Got some server configuration information from running server.

220913 14:49:04 MAIN     INFO: Establishing connection to server for locking.
220913 14:49:04 MAIN     INFO: No SSL options specified.
220913 14:49:04 MAIN     INFO: Backup directory created: '/home/meb/mysql/backup-temp/2022-09-13_14-49-04'
220913 14:49:04 MAIN     INFO: MySQL server version_comment is 'MySQL Enterprise Server - Commercial'
220913 14:49:04 MAIN     INFO: Mysqlbackup component not installed.
220913 14:49:04 MAIN     INFO: MEB logfile created at /home/meb/mysql/backup-temp/2022-09-13_14-49-04/meta/MEB_2022-09-13.14-49-04_backup-to-image.log

220913 14:49:04 MAIN     INFO: The MySQL server has no active keyring.
--------------------------------------------------------------------
                       Server Repository Options:
--------------------------------------------------------------------
  datadir                        = /home/meb/mysql/mysql-datadir/
  innodb_data_home_dir           = 
  innodb_data_file_path          = ibdata1:12M:autoextend
  innodb_log_group_home_dir      = /home/meb/mysql/mysql-datadir/
  innodb_undo_directory          = /home/meb/mysql/mysql-datadir/
  innodb_undo_tablespaces        = 2
  innodb_buffer_pool_filename    = ib_buffer_pool
  innodb_page_size               = 16384
  innodb_checksum_algorithm      = crc32

--------------------------------------------------------------------
                       Backup Config Options:
--------------------------------------------------------------------
  datadir                        = /home/meb/mysql/backup-temp/2022-09-13_14-49-04/datadir
  innodb_data_home_dir           = /home/meb/mysql/backup-temp/2022-09-13_14-49-04/datadir
  innodb_data_file_path          = ibdata1:12M:autoextend
  innodb_log_group_home_dir      = /home/meb/mysql/backup-temp/2022-09-13_14-49-04/datadir
  innodb_undo_directory          = /home/meb/mysql/backup-temp/2022-09-13_14-49-04/datadir
  innodb_undo_tablespaces        = 2
  innodb_buffer_pool_filename    = ib_buffer_pool
  innodb_page_size               = 16384
  innodb_checksum_algorithm      = crc32

Backup Image Path = /home/meb/mysql/backups/testback3.mbi
220913 14:49:04 MAIN     INFO: Unique generated backup id for this is 16630949446348741

220913 14:49:04 MAIN     INFO: Copying the server config file '/home/meb/mysql/mysql-datadir/auto.cnf'
220913 14:49:04 MAIN     INFO: Creating 14 buffers each of size 16777216.
220913 14:49:04 MAIN     INFO: The server is not configured for redo log archiving. The system variable innodb_redo_log_archive_dirs is not set.
220913 14:49:04 MAIN     INFO: Found checkpoint at lsn 19778447.
220913 14:49:04 MAIN     INFO: Starting log scan from lsn = 19778048 at offset = 123791 and checkpoint = 19778447 in file /home/meb/mysql/mysql-datadir/#innodb_redo/#ib_redo6.
220913 14:49:04 MAIN     INFO: Full Image Backup operation starts with following threads
                               1 read-threads    6 process-threads    1 write-threads
220913 14:49:04 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2022-09-13_14-49-04/backup-my.cnf.
220913 14:49:04 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2022-09-13_14-49-04/meta/backup_create.xml.
220913 14:49:04 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2022-09-13_14-49-04/datadir/backup-auto.cnf.
220913 14:49:04 RLP1     INFO: Starting to parse redo log at lsn = 19778077, whereas checkpoint_lsn = 19778447 and start_lsn = 19778048.
220913 14:49:04 RDR1     INFO: Starting to copy all innodb files...
220913 14:49:04 RDR1     INFO: Copying /home/meb/mysql/mysql-datadir/ibdata1.
220913 14:49:04 RDR1     INFO: Starting to copy all undo files...
220913 14:49:04 RDR1     INFO: Copying /home/meb/mysql/mysql-datadir/undo_002.
220913 14:49:04 RDR1     INFO: Copying /home/meb/mysql/mysql-datadir/undo_001.
220913 14:49:04 RDR1     INFO: Starting to lock instance for backup...
220913 14:49:04 RDR1     INFO: The server instance is locked for backup.
220913 14:49:04 RDR1     INFO: The server instance is unlocked after 0.004 seconds.
220913 14:49:04 RDR1     INFO: Copying /home/meb/mysql/mysql-datadir/sys/sys_config.ibd.
220913 14:49:04 RDR1     INFO: Copying /home/meb/mysql/mysql-datadir/Test/test1.ibd.
220913 14:49:04 RDR1     INFO: Copying /home/meb/mysql/mysql-datadir/mysql/backup_progress.ibd.
220913 14:49:04 RDR1     INFO: Copying /home/meb/mysql/mysql-datadir/mysql/backup_history.ibd.
220913 14:49:04 RDR1     INFO: Copying /home/meb/mysql/mysql-datadir/mysql.ibd.
220913 14:49:04 RDR1     INFO: Completing the copy of innodb files.
220913 14:49:04 RDR1     INFO: Requesting a dump of the InnoDB buffer pool
220913 14:49:04 RDR1     INFO: Waiting for the dump of the InnoDB buffer pool to complete
220913 14:49:04 RDR1     INFO: The dump of the InnoDB buffer pool completed
220913 14:49:04 RDR1     INFO: Binary Log Basename: '/home/meb/mysql/mysql-datadir/binlog'
220913 14:49:04 RDR1     INFO: Binary Log Index:    '/home/meb/mysql/mysql-datadir/binlog.index'
220913 14:49:04 RDR1     INFO: Relay Channel:      'group_replication_applier'
220913 14:49:04 RDR1     INFO: Relay Log Basename: '/home/meb/mysql/mysql-datadir/meb-XBox3-relay-bin-group_replication_applier'
220913 14:49:04 RDR1     INFO: Relay Channel:      'group_replication_recovery'
220913 14:49:04 RDR1     INFO: Relay Log Basename: '/home/meb/mysql/mysql-datadir/meb-XBox3-relay-bin-group_replication_recovery'
220913 14:49:04 RDR1     INFO: Starting to copy Binlog files.
220913 14:49:04 RDR1     INFO: Copying /home/meb/mysql/mysql-datadir/binlog.000001.
220913 14:49:04 RDR1     INFO: Starting to lock instance for backup...
220913 14:49:04 RDR1     INFO: The server instance is locked for backup.
220913 14:49:04 RDR1     INFO: The MySQL server has no active keyring.
220913 14:49:04 RDR1     INFO: Requesting flush of redo log reading after LSN 19781380.
220913 14:49:04 RDR1     INFO: Requesting flush of redo log processing after LSN 19781380.
220913 14:49:04 RDR1     INFO: Completed flush of redo log reading after LSN 19784275.
220913 14:49:04 RDR1     INFO: Completed flush of redo log processing after LSN 19784275.
220913 14:49:04 RDR1     INFO: Starting to read-lock tables...
220913 14:49:04 RDR1     INFO: No tables to read-lock.
220913 14:49:04 RDR1     INFO: Opening backup source directory '/home/meb/mysql/mysql-datadir'
220913 14:49:04 RDR1     INFO: Starting to copy non-innodb files in subdirs of '/home/meb/mysql/mysql-datadir'
220913 14:49:04 WTR1     INFO: Adding database directory: datadir/Test
220913 14:49:04 WTR1     INFO: Adding database directory: datadir/mysql
220913 14:49:04 WTR1     INFO: Adding database directory: datadir/performance_schema
220913 14:49:04 RDR1     INFO: Completing the copy of all non-innodb files.
220913 14:49:04 WTR1     INFO: Adding database directory: datadir/sys
220913 14:49:04 RDR1     INFO: Requesting consistency information...
220913 14:49:04 RDR1     INFO: Locked the consistency point for 353 microseconds.
220913 14:49:04 RDR1     INFO: Consistency point server_uuid '98bbd252-3374-11ed-8e69-0800276c22b0'.
220913 14:49:04 RDR1     INFO: Consistency point gtid_executed ''.
220913 14:49:04 RDR1     INFO: Consistency point binary_log_file 'binlog.000002'.
220913 14:49:04 RDR1     INFO: Consistency point binary_log_position 157.
220913 14:49:04 RDR1     INFO: Consistency point InnoDB lsn 19785442.
220913 14:49:04 RDR1     INFO: Consistency point InnoDB lsn_checkpoint 19778447.
220913 14:49:04 RDR1     INFO: Requesting completion of redo log copy after LSN 19785442.
220913 14:49:04 RLW1     INFO: A copied database page was modified at 19778447. (This is the highest lsn found on a page)
220913 14:49:04 RLW1     INFO: Scanned log up to lsn 19785442.
220913 14:49:04 RLW1     INFO: Was able to parse the log up to lsn 19785442.
220913 14:49:04 RLR1     INFO: Redo log reader waited 33 times for a total of 165.00 ms for logs to generate.
220913 14:49:04 RLW1     INFO: Copied redo log
                               log_start_lsn    19778048
                               start_checkpoint 19778447
                               start_lsn        19778447
                               last_checkpoint  19778447
                               consistency_lsn  19785442
                               log_end_lsn      19785442
220913 14:49:04 RDR1     INFO: Truncating binary log index '/home/meb/mysql/backup-temp/2022-09-13_14-49-04/datadir/binlog.index' to 32.
220913 14:49:04 RDR1     INFO: Truncating binary log 'binlog.000002' to 157.
220913 14:49:04 RDR1     INFO: Copying /home/meb/mysql/mysql-datadir/binlog.000002.
220913 14:49:04 RDR1     INFO: Completed the copy of binlog files...
220913 14:49:04 RDR1     INFO: The server instance is unlocked after 0.100 seconds.
220913 14:49:04 RDR1     INFO: Reading all global variables from the server.
220913 14:49:04 RDR1     INFO: Completed reading of all 631 global variables from the server.
220913 14:49:04 RDR1     INFO: Writing server defaults files 'server-my.cnf' and 'server-all.cnf' for server '8.0.31-commercial' in '/home/meb/mysql/backup-temp/2022-09-13_14-49-04'.
220913 14:49:04 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2022-09-13_14-49-04/meta/backup_variables.txt.
220913 14:49:04 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2022-09-13_14-49-04/datadir/ibbackup_logfile.
220913 14:49:04 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2022-09-13_14-49-04/server-all.cnf.
220913 14:49:04 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2022-09-13_14-49-04/server-my.cnf.
220913 14:49:04 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2022-09-13_14-49-04/meta/backup_content.xml.
220913 14:49:05 RDR1     INFO: Copying meta file /home/meb/mysql/backup-temp/2022-09-13_14-49-04/meta/image_files.xml.
220913 14:49:05 MAIN     INFO: Full Image Backup operation completed successfully.
220913 14:49:05 MAIN     INFO: Backup image created successfully.
220913 14:49:05 MAIN     INFO: Image Path = /home/meb/mysql/backups/testback3.mbi
220913 14:49:05 MAIN     INFO: MySQL binlog position: filename binlog.000002, position 157

-------------------------------------------------------------
   Parameters Summary         
-------------------------------------------------------------
   Start LSN                  : 19778048
   Last Checkpoint LSN        : 19778447
   End LSN                    : 19785442
-------------------------------------------------------------

mysqlbackup completed OK!
```