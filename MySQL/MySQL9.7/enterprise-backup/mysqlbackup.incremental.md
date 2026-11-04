---
title: "4.3.3 Making a Differential or Incremental Backup"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/mysqlbackup.incremental.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

### 4.3.3 Making a Differential or Incremental Backup

Assuming a good portion of the data on your MySQL server remains unchanged over time, you can increase the speed and reduce the required storage space for your regular backups by backing up not all the data on the server each time, but only the changes to the data which have taken place over time. In order to that, after making first a full backup that contains all data, you can do one of the following:

- **Performing a series of differential backups.** Each differential backups includes all the changes made to the data since the last full backup was performed. To restore data up to, for example, time `t`, you simply restore first the full backup, and then, on top of it, the differential backup taken for time `t`.
- **Perform a series of incremental backup.** Each [incremental backup](glossary.md) only includes the changes since the previous backup, which can itself be a full or incremental backup. The first backup in an incremental series is always then a differential backup; but after that, each incremental backup only contains the changes made since that last incremental backup. Each subsequent incremental backup is thus usually smaller in size than a differential backup, and is faster to make; that allows you to make very frequent incremental backups, and then enables you to restore the database to a more precise point in time when necessary. However, restoring data with incremental backups might take longer and more work: in general, to restore data up to, for example, time `t`, you start with restoring the full backup, and then restore the incremental backups one by one, until you are finished with the incremental backup taken for time t.

MySQL Enterprise Backup supports both incremental and differential backups. You should decide on which backup strategy to adopt by looking at such factors like how much storage space you have, how quickly you have to be able to restore data, and so on.

MySQL Enterprise Backup treats differential backup as a special case of incremental backup that has a full backup as its base. To create a differential backup, simply follow the instructions below for performing incremental backups, and make sure you specify a full backup as the base of your incremental backup; you should also ignore any instructions that only apply to the handling of multiple incremental backups.

Note

You can create a differential backup easily using the option [`--incremental-base=history:last_full_backup`](backup-incremental-options.md).

See [Section 20.7, “Incremental Backup Options”](backup-incremental-options.md), for descriptions of the **mysqlbackup** options used for incremental backups. An Incremental backup is enabled with one of the two options: [`--incremental`](backup-incremental-options.md) and [`--incremental-with-redo-log-only`](backup-incremental-options.md) option. See Creating Incremental Backups Using Only the Redo Log for their differences.

When creating an incremental backup, you have to indicate to **mysqlbackup** the point in time of the previous full or incremental backup. For convenience, you can use the [`--incremental-base`](backup-incremental-options.md) option to automatically derive the necessary [log sequence number](glossary.md) (LSN) from the metadata stored in a previous backup directory or on the server. Or, you can specify an explicit LSN value using the [`--start-lsn`](backup-incremental-options.md) option, providing to **mysqlbackup** the ending LSN from a previous full or incremental backup (see Other Considerations for Incremental Backups on some limitation that applies when using the [`--start-lsn`](backup-incremental-options.md) option).

To prepare the backup data to be restored, you combine all incremental backups with an original full backup. Typically, you perform a new full backup after a designated period of time, after which you can discard the older incremental backup data.

#### Creating Incremental Backups Using Only the Redo Log

The [`--incremental-with-redo-log-only`](backup-incremental-options.md) might offer some benefits over the [`--incremental`](backup-incremental-options.md) option for creating an incremental backup:

- The changes to the InnoDB tables are determined based on the contents of the `InnoDB` [redo log](glossary.md). Since the redo log has a maximum size that you know in advance, depending on the size of your database, the amount of DML activities, and the size of the redo log, it usually requires less I/O to read the changes from the redo log than to scan the InnoDB tablespace files to locate the changed pages.
- A system variable, [`innodb_redo_log_capacity`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-parameters.html#sysvar_innodb_redo_log_capacity), controls the amount of disk space occupied by redo log files. If the redo log files occupy less space than the value of [`innodb_redo_log_capacity`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-parameters.html#sysvar_innodb_redo_log_capacity), dirty pages are flushed from the buffer pool to tablespace data files less aggressively, allowing the disk space occupied by the redo log files to grow faster. If the space occupied by the redo log files gets close to the specified value, dirty pages are flushed more aggressively, so that the disk space occupied by redo log files is kept within the specified limit. See [Configuring Redo Log Capacity](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-redo-log.html#innodb-modifying-redo-log-capacity) for details.
	With the way the redo log is now maintained, it becomes more likely that when an incremental backup using only the redo log is started, the redo log files storing the changes to the database since the last backup are already processed and are no longer available. To prevent that situation, you should register `mysqlbackup` (the MySQL user who creates backups) with the server as an external consumer of the redo log by the following UDF command, before the creation of any data that is to be included in the redo-log-only incremental backup:
	```
	DO innodb_redo_log_consumer_register();
	```
	This prevents InnoDB from removing or recycling redo log files that contain transactions not backed up yet by **mysqlbackup**. After each redo-log-only incremental backup, run the following UDF to advance to a new LSN checkpoint, so that the server may now process the redo log files that are no longer required by **mysqlbackup**:
	```
	DO innodb_redo_log_consumer_advance($lsn);
	```
	`$lsn` is the highest LSN value included in a finished incremental backup.
	The steps above assume that the connection session that initiated the `DO             innodb_redo_log_consumer_register();` UDF is kept open in between the base backup or the last incremental backup and the latest redo-log-only incremental backup. One way to help ensure that is to have the server spawning on the same machine a special client that connects to the Server by, for example, a Unix socket (if it is a Unix machine) through a connection session that initiates the UDF and is then left open for as long as it is needed. That setup will provide a stable connection session for keeping `mysqlbackup` as a consumer of the redo log.
- This type of incremental backup is not so forgiving of too-low [`--start-lsn`](backup-incremental-options.md) values as the standard `--incremental` option is. For example, you cannot make a full backup and then make a series of [`--incremental-with-redo-log-only`](backup-incremental-options.md) backups all using the same `--start-lsn` value. Make sure to specify the precise end LSN of the previous backup as the start LSN of the next incremental backup; do not use arbitrary values.
	Note
	To ensure the LSN values match up exactly between successive incremental backups, it is recommended that you always use the [`--incremental-base`](backup-incremental-options.md) option when you use the [`--incremental-with-redo-log-only`](backup-incremental-options.md) option.
- To judge whether this type of incremental backup is practical and efficient for a particular MySQL instance:
	- Measure how fast the data changes within the InnoDB redo log files. Check the [LSN](glossary.md) periodically to decide how much redo data accumulates over the course of some number of hours or days.
	- Compare the rate of redo log accumulation with the redo log capacity, and use this ratio to see how often to take an incremental backup. For example, if you are producing 1GB of redo log data per day, and the combined size of your redo clog capacity (which is specified by [`innodb_redo_log_capacity`](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-parameters.html#sysvar_innodb_redo_log_capacity) ) is 7GB, you would schedule incremental backups more frequently than once a week. You might perform incremental backups every day or two, to avoid a potential issue when a sudden flurry of updates produced more redo log data than usual.
	- Benchmark incremental backup times using both the [`--incremental`](backup-incremental-options.md) and [`--incremental-with-redo-log-only`](backup-incremental-options.md) options, to confirm if the redo log backup technique performs faster and with less overhead than the traditional incremental backup method. The result could depend on the size of your data, the amount of DML activity, and the capacity of your redo log. Do your testing on a server with a realistic data volume and a realistic workload. For example, if you have huge redo log files, reading them in the course of an incremental backup could take as long as reading the InnoDB data files using the traditional incremental technique. Conversely, if your data volume is large, reading all the data files to find the few changed pages could be less efficient than processing the much smaller redo log files.
	- Backup compression (i.e., use of the [compression options](backup-compression-options.md)) is not supported when you perform incremental backups with the redo log only. If backup compression is important to you, do not use the [`--incremental-with-redo-log-only`](backup-incremental-options.md) option.

#### Incremental Backup Using Page Tracking

**mysqlbackup** supports creating incremental backups using the page tracking functionality of the MySQL Server, by which **mysqlbackup** looks for changed pages in the InnoDB data files that have been modified since the last backup and then copies them. In general, incremental backups using page tracking are faster than other kinds of incremental backups performed by **mysqlbackup** if the majority of the data in the database has not been modified. Using this feature requires the following to be done on the server before the base backup for the incremental backup is made:

- Install the `mysqlbackup` component, which comes with the MySQL Enterprise Server 9.7 installation, by running this command at a **mysql** client connected to the server:
	```
	INSTALL COMPONENT "file://component_mysqlbackup";
	```
- Start page tracking with the following function:
	```
	SELECT mysqlbackup_page_track_set(true);
	```
	The LSN value starting from which changed pages have been tracked is returned by this function:
	```
	SELECT mysqlbackup_page_track_get_start_lsn();
	```
	You can stop page tracking with the following function:
	```
	SELECT mysqlbackup_page_track_set(false);
	```

Note

The previously mentioned functions regarding page tracking require the `BACKUP_ADMIN` privilege to run.

When the [`--incremental`](backup-incremental-options.md) option is used without any value specified, **mysqlbackup** performs an incremental backup using the page tracking functionality. User can also specifies [`--incremental=page-track`](backup-incremental-options.md) to make **mysqlbackup** use the page tracking functionality. However, the prerequisites for making use of the page tracking functionality for incremental backups are:

- Page tracking is functioning properly on the server, and it has been enabled (with `SELECT             mysqlbackup_page_track_set(true)`) before the base backup was created; if that is not the case, **mysqlbackup** throws an error when [`--incremental=page-track`](backup-incremental-options.md), or it performs a full-scan incremental backup instead when [`--incremental`](backup-incremental-options.md) is unspecified.
- The number of changed pages is less than 50% of the total number of pages; if that is not the case, **mysqlbackup** throws an error when [`--incremental=page-track`](backup-incremental-options.md), or it performs a full-scan incremental backup instead when [`--incremental`](backup-incremental-options.md) is unspecified.

Note

**mysqlbackup** needs to be started with enough memory to process all the tracked pages in memory. If there is not enough memory, **mysqlbackup** throws an error and then exits. Here are some guidelines for assuring enough memory for the operation:

- The default value of 400 \[MB\] for the [`--limit-memory`](backup-capacity-options.md) option allows **mysqlbackup** to handle about 800GB of changed data. Adjust the value for the option according to your data size.
- The page tracking feature uses the memory buffers configured for **mysqlbackup** for sorting the pages. Determine the number of buffers needed for page sorting by the following steps:
	- Before running the incremental backup, perform the following query on the server to determine the `end_lsn` for the base backup:
		```
		SELECT end_lsn FROM mysql.backup_history WHERE exit_state = 'SUCCESS' 
		AND backup_type != 'TTS' AND server_uuid = @@server_uuid 
		ORDER BY end_time DESC, end_lsn DESC LIMIT 0,1;
		```
	- Run the following query on the server to get the number of changed pages since the base backup was created (retry the query if it returns a negative value):
		```
		SELECT mysqlbackup_page_track_get_changed_page_count(<the above end_lsn>, 0);
		```
	- Every changed page needs 8 bytes in the sorting buffer. So, multiply the `changed_page_count` value obtained in the last step by 8 to get the number of bytes needed for the sorting buffer.
	- Each buffer has 16 Megabytes (16777216 bytes). So, divide the number of bytes needed for the sorting buffers calculated in the last step by 16777216 and round the result up to the next integer, to get the number of buffers needed for sorting.
	- Make sure the value for the option [`--number-of-buffers`](backup-capacity-options.md) is no smaller than the number of required sorting buffers you calculated in the last step. Remember that there could be more changed pages created while you are doing this calculation, so you might want to give **mysqlbackup** a few more extra buffers.
- The default memory limit of 400MB should be able to support up to 25 buffers (up to 18 buffers only for cloud backups); increase the memory limit if you need more buffers than that by changing the value of the [`--limit-memory`](backup-capacity-options.md) option.

Page tracking creates a file under the server's datadir for collecting information about changed pages. This file keeps growing until page tracking is stopped. If the server is stopped and restarted, a new page tracking file is created, but the old file persists and continues to grow until page tracking is deactivated explicitly. Using a sequence of SQL statements similar to the following, you can purge any old page-tracking data that you no longer need:

```
SELECT mysqlbackup_page_track_set(false); 
SELECT mysqlbackup_page_track_purge_up_to(9223372036854775807);
/* Supply to the loadable function the LSN up to which you want to 
purge page tracking data. 9223372036854775807 is the highest possible LSN, 
which causes all page tracking files to be purged.*/
SELECT mysqlbackup_page_track_set(true);
```

This can be run, for example, before every full backup.

#### Full-scan versus Optimistic Incremental Backup

When the [`--incremental`](backup-incremental-options.md) option is set to `full-scan`, **mysqlbackup** performs a full-scan incremental backup, in which it scans all InnoDB data files in the server's data directory to find pages that have been changed since the last backup was made and then copies those pages. A full-scan incremental backup might not be very efficient when not many tables have been modified since the last back up.

An optimistic incremental backup, on the other hand, only scans for changed pages in InnoDB data files that have been modified since the last backup, thus saving some unnecessary scan time. An optimistic incremental backup can be performed by specifying [`--incremental=optimistic`](backup-incremental-options.md). While an optimistic increment backup might shorten the backup time, it has the following limitations:

- Since this feature makes use of the modification times of the files in the server's data directory, two things must have remained unchanged since the previous backup: (1) the system time on the server, and (2) the location of the data directory. Otherwise, the backup might fail, or an inconsistent incremental backup might be produced.
- Optimistic incremental backups cannot be performed with the [`--incremental-with-redo-log-only`](backup-incremental-options.md), for which **mysqlbackup** reads the redo log files instead of scanning the files in the data directory.
- If the [`--start-lsn`](backup-incremental-options.md) option is used, a full scan is performed even if [`--incremental=optimistic`](backup-incremental-options.md) is specified since, in that case, **mysqlbackup** cannot determine the point in time for which the previous backup is consistent, and thus has no time frame to determine which files have been modified recently.

For these and other cases in which an optimistic incremental backup is not desirable, perform a full-scan incremental backup, or an incremental backup using page tracking. See [Section 4.1.2, “Grant MySQL Privileges to Backup Administrator”](mysqlbackup.privileges.md) on the privileges required for **mysqlbackup** to perform an optimistic incremental backup. Also see [Using Optimistic Backups and Optimistic Incremental Backups Together](meb-backup-optimistic.md) on how to utilize the two features together in a backup schedule.

#### Other Considerations for Incremental Backups

The incremental backup feature is primarily intended for InnoDB tables, or non-InnoDB tables that are read-only or rarely updated. Incremental backups detect changes at the level of [pages](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/glossary.html#glos_page) in the InnoDB [data files](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/glossary.html#glos_data_files), as opposed to table rows; each page that has changed is backed up. Thus, the space and time savings are not exactly proportional to the percentage of changed InnoDB rows or columns.

For non-InnoDB files, the entire file is always included in an incremental backup, which means the savings for backup resources are less significant when comparing with the case with InnoDB tables.

No binary log files are copied into the incremental backup if the [`--start-lsn`](backup-incremental-options.md) option is used. To include binary log files for the period covered by the incremental backup, use the [`--incremental-base`](backup-incremental-options.md) option instead, which provides the necessary information for **mysqlbackup** to ensure that no gap exists between binary log data included in the previous backup and the current incremental backup.

#### Examples of Incremental Backups

These examples use **mysqlbackup** to make an incremental backup of a MySQL server, including all databases and tables. We show two alternatives, one using the [`--incremental-base`](backup-incremental-options.md) option and the other using the [`--start-lsn`](backup-incremental-options.md) option.

With the `--incremental-base` option, you do not have to keep track of LSN values between one backup and the next. Instead, you can do one of the following:

- Tell **mysqlbackup** to query the `end_lsn` value from the last successful [non-TTS backup](glossary.md) as recorded in the `backup_history` table on the server using [`--incremental-base`](backup-incremental-options.md) `=history:last_backup` or `history:last_full_backup`.
- *Advanced:* For directory backups, specify the directory of the previous backup (either full or incremental) with [``--incremental-base=dir:*`directory_path`*``](backup-incremental-options.md), and **mysqlbackup** will figure out the starting point for this backup based on the metadata of the earlier one. Because you need a known set of directory names, you might want to use hardcoded names or generate a sequence of names in your own backup script, rather than using the [`--with-timestamp`](backup-repository-options.md) option. If your last backup was a single-file, you can still use [``--incremental-base=dir:*`directory_path`*``](backup-incremental-options.md) to provide the location of the temporary directory you supplied with the [`--backup-dir`](backup-repository-options.md) option during the last backup

In the following example, the [`--incremental-base=history:last_backup`](backup-incremental-options.md) option is used, given which **mysqlbackup** fetches the LSN of the last successful (non-TTS) full or partial backup from the `mysql.backup_history` table and performs an incremental backup basing on that.

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf \
  --incremental --incremental-base=history:last_backup \
  --backup-dir=/home/dbadmin/temp_dir \
  --backup-image=incremental_image1.bi \
   backup-to-image
```

In the following example, an incremental backup similar to the one in the last example but optimistic in nature is performed.

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf \
  --incremental=optimistic --incremental-base=history:last_backup \
  --backup-dir=/home/dbadmin/temp_dir \
  --backup-image=incremental_image1.bi 
   backup-to-image
```

*Advanced:* Use the following command to create an incremental directory backup using the [``--incremental-base=dir:*`directory_path`*``](backup-incremental-options.md) option; the backup is saved at the location specified by [`--incremental-backup-dir`](backup-incremental-options.md):

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf --incremental \
  --incremental-base=dir:/incr-backup/wednesday \
  --incremental-backup-dir=/incr-backup/thursday \
  backup
```

You can also use the [`--start-lsn`](backup-incremental-options.md) option to specify where the incremental backup should start. You have to record the LSN of the previous backup reported by **mysqlbackup** at the end of the backup:

```
mysqlbackup: Was able to parse the log up to lsn 2654255716
```

The number is also recorded in the `meta/backup_variables.txt` file in the folder specified by [`--backup-dir`](backup-repository-options.md) during the backup. Supply then that number to **mysqlbackup** using the `--start-lsn` option. The incremental backup then includes all changes that came *after* the specified LSN.

To create an incremental backup image with the `--start-lsn` option, use the following command, specifying with [`--backup-dir`](backup-repository-options.md) the backup directory, which, in this case, is a directory for storing the metadata for the backup and some temporary files:

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf --incremental \
  --start-lsn=2654255716 \
  --with-timestamp \
  --backup-dir=/incr-tmp \
  --backup-image=/incr-backup/incremental_image.bi \
  backup-to-image
```

In the following example though, because [`--backup-image`](backup-repository-options.md) does not provide a full path to the image file to be created, the incremental backup image is created under the folder specified by [`--backup-dir`](backup-repository-options.md):

```
mysqlbackup --defaults-file=/home/dbadmin/my.cnf --incremental \
  --start-lsn=2654255716 \
  --with-timestamp \
  --backup-dir=/incr-images \
  --backup-image=incremental_image1.bi \
  backup-to-image
```

#### Maintaining a backup schedule:

- On a regular schedule determined by date or amount of database activity, take more incremental or differential backups.
- Optionally, periodically start the cycle over again by taking a [full, uncompressed](mysqlbackup.full.md) or [compressed](backup.compressed.md) backup. Typically, this milestone happens when you can archive and clear out your oldest backup data.

On how to restore your database using the incremental backups, see [Section 5.1.3, “Restoring an Incremental Backup”](restore.incremental.md)