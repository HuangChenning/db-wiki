---
title: Scalability / Capacity Options
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/backup-capacity-options.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

## 20.10 Performance / Scalability / Capacity Options

These options limit the resources used by the backup process, in order to minimize backup overhead for busy or huge databases, or specify behaviors of the process when encountering resource issues.

- ``--number-of-buffers=*`num_buffers`*``
	| Command-Line Format | `--number-of-buffers=NUMBER` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `14` |
	| Minimum Value | `1` |
	Specifies the number of buffers, each 16MB in size, to use during multithreaded options.
	Use a high number for CPU-intensive processing such as backup, particularly when using compression. Use a low number for disk-intensive processing such as restoring a backup. This value should be at least as high as the number of read threads or write threads, depending on the type of operation.
	Default: currently 14.
	For compression or incremental backup operations, the buffer size is slightly more than 16MB to accommodate the headers.
	One additional buffer is used for single-file incremental backup and single-file compressed backup.
	Compressed backup, compressed single-file backup, and uncompress apply-log operations require one additional buffer for each process thread.
	If you change the number of read, write, and processing threads, you can experiment with changing this value so that it is slightly larger than the total number of threads specified by those other options. See [Section 13.1, “Optimizing Backup Performance”](backup-performance.md) and [Section 13.2, “Optimizing Restore Performance”](restore-performance.md) for additional advice about recommended combinations of values for this and other performance-related options for various hardware configurations, such as RAID or non-RAID storage devices.
- ``--read-threads=*`num_threads`*``
	| Command-Line Format | `--read-threads=NUMBER` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `1` |
	| Minimum Value | `1` |
	| Maximum Value | `15` |
	Specifies the number of threads to use for reading data from disk. This option applies to these kinds of operations: [`copy-back`](backup-commands-restore.md), [`copy-back-and-apply-log`](backup-commands-restore.md) (for directory backups only), [`extract`](backup-commands-single-file.md), [`backup`](backup-commands-backup.md), and [`backup-and-apply-log`](backup-commands-backup.md). If you specify a value of 0, it is silently adjusted to 1. The maximum is 15. If you supply a negative value, it is silently adjusted to 15. For the following operations, the number of read threads is always 1 regardless of this option's setting:
	See [Section 13.1, “Optimizing Backup Performance”](backup-performance.md) and [Section 13.2, “Optimizing Restore Performance”](restore-performance.md) for advice about recommended combinations of values for `--read-threads`, `--process-threads`, and `--write-threads` for various hardware configurations, such as RAID or non-RAID storage devices.
	Default: 1.
- ``--process-threads=*`num_threads`*``
	| Command-Line Format | `--process-threads=NUMBER` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `6` |
	| Minimum Value | `1` |
	| Maximum Value | `15` |
	Specifies the number of threads to use for processing data, including compression and uncompression, encryption and decryption, apply-log operations, and packing and extracting of backup images. For [`backup-and-apply-log`](backup-commands-backup.md), [`copy-back-and-apply-log`](backup-commands-restore.md), and [`apply-incremental-backup`](backup-commands-update.md), `--process-threads` sets the worker threads number for the apply-log phase of the operation. The option is ignored for those operations that do not involve data processing like [`copy-back`](backup-commands-restore.md) (unless decryption or uncompression is involved ), [`backup-dir-to-image`](backup-commands-single-file.md), or a backup operation that uses the [`--incremental-with-redo-log-only`](backup-incremental-options.md) option.
	Default: 6 for all operations to which the option is applicable.
	If you specify a value of 0, it is silently adjusted to 1. The maximum is 15. If you supply a negative value, it is silently adjusted to 15. See [Section 13.1, “Optimizing Backup Performance”](backup-performance.md) and [Section 13.2, “Optimizing Restore Performance”](restore-performance.md) for advice about recommended combinations of values for `--read-threads`, `--process-threads`, and `--write-threads` for various hardware configurations, such as RAID or non-RAID storage devices.
- ``--write-threads=*`num_threads`*``
	| Command-Line Format | `--write-threads=NUMBER` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `1` |
	| Minimum Value | `1` |
	| Maximum Value | `15` |
	Specifies the number of threads to use for writing data to disk. This option applies to these kinds of operations: [`copy-back`](backup-commands-restore.md), [`copy-back-and-apply-log`](backup-commands-restore.md), [`extract`](backup-commands-single-file.md), [`backup`](backup-commands-backup.md), and [`backup-and-apply-log`](backup-commands-backup.md) (when applied to directory backups). For the supported operations, multiple write threads are supported for any write target that is seekable; `--write-threads` is forced to be 1 only when the write target is non-seekable. The option is ignored for other operations like single-file backups (uses 1 write thread always), [`list-image`](backup-commands-single-file.md) (uses no write threads), and [`validate`](backup-commands-validate.md) (uses no write threads).
	If you specify a value of 0, it is silently adjusted to 1 (for operations that uses write threads). The maximum is 15. If you supply a negative value, it is silently adjusted to 15.For [`apply-log`](backup-commands-update.md) operations and the apply-log phase of [`copy-back-and-apply-log`](backup-commands-restore.md), [`backup-and-apply-log`](backup-commands-backup.md), or [`apply-incremental-backup`](backup-commands-update.md), the number of write threads is always 0 regardless of this option's setting. See [Section 13.1, “Optimizing Backup Performance”](backup-performance.md) and [Section 13.2, “Optimizing Restore Performance”](restore-performance.md) for advice about recommended combinations of values for `--read-threads`, `--process-threads`, and `--write-threads` for various hardware configurations, such as RAID or non-RAID storage devices.
	Default: 1.
- `--limit-memory` = *`MB`*
	| Command-Line Format | `--limit-memory=MB` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `100 for apply-log (without uncompression), 400 for other operations` |
	| Minimum Value | `0` |
	| Maximum Value | `999999` |
	| Unit | megabyte |
	Specify maximum memory in megabytes that can be used by **mysqlbackup**. It applies to all operations. Do not include any suffixes such as `mb` or `kb` in the option value.
	Default: 100 for [`apply-log`](backup-commands-update.md) without uncompression, 400 for all other operations (in megabytes).
	The memory limit specified by this option also caps the number of 16MB buffers available for multithreaded processing. For example, with a 400 MB limit, the maximum number of buffers is 25 (except for a cloud backup, for which extra memory is needed, and the maximum number of buffers is 18). If additional buffers are required because you increased the values for `--read-threads`, `--process-threads`, `--write-threads`, and/or `--number-of-buffers`, increase the `--limit-memory` value accordingly.
- `--sleep` = *`MS`*
	| Command-Line Format | `--sleep=MS` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `0` |
	| Unit | millisecond |
	Specify the number in milliseconds to sleep after copying a certain amount of data from InnoDB tables. Each block of data is 1024 InnoDB data pages, typically totalling 16MB. This is to limit the CPU and I/O overhead on the database server.
	Default: 0 (no voluntary sleeps).
- `--no-locking`
	Disables all locking during backup (see [The Backup Process](meb-backup-process.md) for details). It can be used to back up a server with less disruption to normal database processing. There could be inconsistencies in both InnoDB and non-InnoDB data if any changes are made while those files are being backed up.
- `--lock-wait-timeout`
	| Command-Line Format | `--lock-wait-timeout=S` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `60` |
	| Minimum Value | `1` |
	| Unit | second |
	The option is no longer supported.
- ``--page-reread-time=*`MS`*``
	| Command-Line Format | `--page-reread-time=MS` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `100` |
	| Unit | millisecond |
	Interval in milliseconds that **mysqlbackup** waits before re-reading a [page](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/glossary.html#glos_page) that fails a checksum test. A busy server could be writing a page at the same moment that **mysqlbackup** is reading it. Can be a floating-point number, such as 0.05 meaning 50 microseconds. Best possible resolution is 1 microsecond, but it could be worse on some platforms. Default is 100 milliseconds (0.1 second).
- ``--page-reread-count=*`number`*``
	| Command-Line Format | `--page-reread-count=number` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `500` |
	Maximum number of re-read attempts, when a [page](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/glossary.html#glos_page) fails a checksum test. A busy server could be writing a page at the same moment that **mysqlbackup** is reading it. If the same page fails this many checksum tests consecutively, with a pause based on the `--page-reread-time` option between each attempt, the backup fails. Default is 500.
- `--on-disk-full={abort|abort_and_remove|warn}`
	| Command-Line Format | `--on-disk-full=option` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `abort` |
	| Valid Values | `abort`  `warn`  `abort_and_remove` |
	Specifies the behavior when a backup process encounters a disk-full condition. This option is only for backup operations ([`backup`](backup-commands-backup.md), [`backup-and-apply-log`](backup-commands-backup.md), and [`backup-to-image`](backup-commands-backup.md)).
	- `abort`: Abort backup, without removing the backup directory. The disk remains full.
	- `abort_and_remove`: Abort backup and remove the backup directory.
	- `warn`: Write a warning message every 30 seconds and retry backup until disk space becomes available.
	Default: `abort`.
- `--skip-unused-pages`
	Skip unused pages in tablespaces when backing up InnoDB tables. This option is applicable to the [`backup`](backup-commands-backup.md) and [`backup-to-image`](backup-commands-backup.md) operations, but not to [incremental](backup-incremental-options.md) backups. The option is ignored by the [`backup-and-apply-log`](backup-commands-backup.md) operation.
	Note that backups created with the `--skip-unused-pages` option cannot be restored using [`copy-back-and-apply-log`](backup-commands-restore.md).
	Unused pages are free pages often caused by bulk delete of data. By skipping the unused pages during backups, this option can reduce the backup sizes and thus the required disk space and I/O resources for the operations. However, subsequent [`apply-log`](backup-commands-update.md) operations on the backups will take more time to complete, as the unused pages are inserted back into the tables during the operations.
- `--skip-binlog`
	Skip including the binary log files in the backup during a backup operation, or skip copying the binary log files onto a server during a restore operation.
	Binary log files, together with the binary log index file, are backed up and restored by default for all kinds of backups (full, incremental (see [Binary Log and Relay Log Restore](restore.incremental.md) for exceptions), compressed, partial (except for [TTS](glossary.md) backups), single-file, etc.). See [Table 1.1, “Types of Files in a Backup”](meb-files-backed-up-summary.md), for details. Use this option to skip backing up binary logs for the following situations if resource or performance issues arise.:
	The option makes binary log to be skipped not just for the current backup operation, but also for all subsequent incremental backups that are based on the current backup.
	When an incremental backup is restored with the `--skip-binlog` option, **mysqlbackup** renames any binary log files that have already been restored onto the server by adding to them the `.old` extension.
- `--skip-relaylog`
	When working with a replica server, skip including the relay log files in the backup during a backup operation, or skip copying the relay log files onto a server during a restore operation.
	Relay log files, together with the relay log index file and the `master.info` and the `slave.info` files, are backed up and restored by default for all kinds of backups (full, incremental (see [Binary Log and Relay Log Restore](restore.incremental.md) for exceptions), compressed, partial (except for [TTS](glossary.md) backups), single-file, etc.) of a replica server. See [Table 1.1, “Types of Files in a Backup”](meb-files-backed-up-summary.md), for details. Use this option to skip backing up or restoring relay logs if resource, performance, or other issues arise.
	Note
	If a user runs a [FLUSH LOGS](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/flush.html) statement while backup is in progress for a replica, the backup process will fail. Use the `--skip-relaylog` option if you expect a [FLUSH LOGS](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/flush.html) statement will be run during the backup and it is not necessary to include the relay logs in the backup.
- `--no-redo-log-archive`
	Skip using [redo log archiving](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-redo-log.html#innodb-redo-log-archiving) on the server during backup, which is used by default. The option has no effects for operations other than backups. See [Chapter 7, *Backing up Using Redo Log Archiving*](meb-redo-log-archiving.md) for details.
- `--skip-final-rescan`
	Skip the final rescan for InnoDB tables that have been modified by DDL operations, which is supposed to take place after **mysqlbackup** puts the database server under a [backup lock](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/lock-instance-for-backup.html) near the end of a backup operation. This potentially shortens the duration for the lock and reduces the backup's impact on the server's normal operation, especially when many tables are being backed up.
	Warning
	This option can cause an incomplete or inconsistent backup if, during the backup operation, DDL operations are executed on any InnoDB tables whose [file-per-table](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/glossary.html#glos_file_per_table) tablespaces are outside the MySQL data directory (i.e., any [InnoDB tables created using the `DATA DIRECTORY` table option](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/innodb-create-table-external.html)).
	The option is ignored for backups using the [`--incremental-with-redo-log-only`](backup-incremental-options.md) option and for non-backup operations.
- `--optimistic-time` \[= *`DATE-TIME`*\]
	| Command-Line Format | `--optimistic-time=DATE-TIME` |
	| --- | --- |
	| Type | String |
	| Default Value | `now` |
	Perform an optimistic backup with the value specified with the option as the “optimistic time”—a time after which the tables that have not been modified are taken as “inactive tables.” The “inactive tables”are believed to be unlikely to change during the backup process. The inactive tables are backed up in the optimistic phase of the backup, and all other tables are backed up in the normal phase. See [Section 4.3.6, “Making an Optimistic Backup”](meb-backup-optimistic.md) for details on the concept, use cases, and command samples for an optimistic backup.
	Accepted formats for specifying the option include:
	- `now`: This includes all tables into the optimistic phase of the backup process. It is the default value for the option when no value is specified.
	- *`{Number}{Unit}`*: Indicates the optimistic time as a time at a certain duration into the past. *`{Unit}`* can be any one of `years`, `months`, `hours`, and `minutes`. Some examples for option strings in this format include: `5years`, `2days`,`13months`, `23hours`, and `35minutes`.
	- A date-time format in any of the following forms: `YYMMDD`, `YYYYMMDD`, `YYMMDDHHMMSS`, `YYYYMMDDHHMMSS`, `YY-MM-DD`, `YYYY-MM-DD`, `YY-MM-DD                   HH.MM.SS`, or `YYYYMMDDTHHMMSS` (where `T` is the character `T`).
	When both the `optimistic-time` and the `optimistic-busy-tables` options are used and they come into conflict on determining which tables are to be backed up in the optimistic phase, `optimistic-busy-tables` takes precedence over `optimistic-time`.
- `--optimistic-busy-tables` = *`REGEXP`*
	| Command-Line Format | `--optimistic-busy-tables=REGEXP` |
	| --- | --- |
	| Type | String |
	Perform an optimistic backup, using the regular expression specified with the option to select tables that will be skipped in the first phase of an optimistic backup, because they are likely to be modified during the backup process. Tables whose fully qualified names (in the form of *`database_name`*.*`table_name`*) are matched by the regular expression are taken as “busy tables”, which will be backed up in the second or the “normal” phase of the backup. Tables whose fully qualified names are NOT matched by the regular expression are taken as “inactive tables”, which will be backed up in the first or the “optimistic” phase of the backup. See [Section 4.3.6, “Making an Optimistic Backup”](meb-backup-optimistic.md) for details on the concept, use cases, and command samples for an optimistic backup.
	MySQL Enterprise Backup will throw an error if the option is used but no regular expression is supplied with it.
	When both the `optimistic-time` and the `optimistic-busy-tables` options are used and they come into conflict on determining which tables are to be “optimistic”, `optimistic-busy-tables` takes precedence over `optimistic-time`.
- `--free-os-buffers` \[= *`NUMBER`*\]
	| Command-Line Format | `--free-os-buffers[=NUMBER]` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `2` |
	| Valid Values | `0`  `1`  `2`  `3`  `4`  `5` |
	Default: Automatic syncing disabled.
	*Only on platforms supporting `posix_fadvise()`:* **mysqlbackup** advises the file system with `posix_fadvise()` to free blocks from the system buffer cache, in order to minimize the impact on the system by **mysqlbackup**. The manner `posix_fadvise()` is used depends on the argument for the option:
	- `0`: Do not use `posix_fadvise()` at all
	- `1`, or no number given with the option: Use `posix_fadvise()` for reading and writing, and syncing files at close. This option preserves the behavior of earlier versions of **mysqlbackup**.
	- `2`, or option not used: Use `posix_fadvise()` for reading or writing, depending on the operation.
	- `3`: Use `posix_fadvise()` for reading and writing.
	- `4`: Use `posix_fadvise()` for reading only.
	- `5`: Use `posix_fadvise()` for writing only.
	Default: `2`.