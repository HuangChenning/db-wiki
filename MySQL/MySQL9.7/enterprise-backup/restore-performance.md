---
title: "13.2 Optimizing Restore Performance"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/restore-performance.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

This section describes the performance considerations for restoring a database server with MySQL Enterprise Backup. This subject is important because:

- The restore operation is the phase of the backup-restore cycle that tends to vary substantially between different backup methods. For example, backup performance might be acceptable using **mysqldump**, but **mysqldump** typically takes much longer than MySQL Enterprise Backup for a restore operation.
- The restore operation is often performed during an emergency, where it is critical to minimize the downtime of the application or web site.
- The restore operation (except for [Table-Level Restore](restore.partial.md)) is always performed with the database server shut down.
- The restore operation is mainly dependent on low-level considerations, such as I/O and network speed for transferring files, and CPU speed, processor cores, and so on for uncompressing data.

For the combination of options you can specify for a restore job, see [Section 19.3, “Restore Operations”](backup-commands-restore.md).

### Restoring Different Classes of Backup Data

Restoring a partial backup takes less time than restoring a full backup, because there is less data to physically copy. See [Section 4.3.5, “Making a Partial Backup”](partial.md) for information about partial backups.

Restoring a compressed backup takes more time than restoring an uncompressed backup, because the time needed to uncompress the data is typically greater than any time saved by transferring less data across the network. If you need to rearrange your storage to free up enough space to uncompress the backup before restoring it, include that administration work in your estimate of the total time required. In an emergency, the time needed to uncompress the backup data before restoring it might be unacceptable. on the database server to hold both the compressed backup and the uncompressed data. Thus, the more critical the data is, the more likely that you might choose not to use compression: accepting a slower, larger backup to ensure that the restore process is as fast and reliable as possible. See [Section 20.6, “Compression Options”](backup-compression-options.md) for information about making compressed backups.

The unpacking process to restore a single-file backup is typically not expensive either in terms of raw speed or extra storage. Each file is unpacked directly to its final destination, the same as if it was copied individually. Thus, if you can speed up the backup substantially or decrease its storage requirements by using single-file backups, that typically does not involve a tradeoff with restore time. See [Section 19.5, “Other Single-File Backup Operations”](backup-commands-single-file.md) for information about making single-file backups.

### The Apply-Log Phase (for Directory Backups only)

See [Advanced: Apply-Log Phase (for Directory Backups only)](backup-performance.md) for performance considerations regarding the apply-log phase.

### Network Performance

For data processing operations, you might know the conventional advice that Unix sockets are faster than TCP/IP for communicating with the database. Although the **mysqlbackup** command supports the options `--protocol=tcp`, `--protocol=socket`, and `--protocol=pipe`, these options do not have a significant effect on backup or restore performance. These processes involve file-copy operations rather than client/server network traffic. The database communication controlled by the `--protocol` option is low-volume. For example, **mysqlbackup** retrieves information about database parameters through the database connection, but not table or index data.

### Parallel Restore

**mysqlbackup** can take advantage of modern multicore CPUs and operating system threads to perform backup operations in parallel. See [Section 20.10, “Performance / Scalability / Capacity Options”](backup-capacity-options.md) for the options to control how many threads are used for different aspects of the restore process. If you see that there is unused system capacity during a restore, consider increasing the values for these options and testing whether doing so increases restore performance:

- When tuning and testing backup performance using a RAID storage configuration, consider the combination of option settings `--read-threads=3 --process-threads=6         --write-threads=3`. Compare against the combination `--read-threads=1 --process-threads=6         --write-threads=1`.
- When tuning and testing backup performance using a non-RAID storage configuration, consider the combination of option settings `--read-threads=1 --process-threads=6         --write-threads=1`.
- When you increase the values for any of the 3 “threads” options, also increase the value of the [`--limit-memory`](backup-capacity-options.md) option, to give the extra threads enough memory to do their work.
- If the CPU is not too busy (less than 80% CPU utilization), increase the value of the [`--process-threads`](backup-capacity-options.md) option.
- If the storage device that you are restoring from (the source drive) can handle more I/O requests, increase the value of the [`--read-threads`](backup-capacity-options.md) option (not applicable to restores of single-file backups, which always use a single read thread).
- If the storage device that you are restoring to (the destination drive) can handle more I/O requests, increase the value of the [`--write-threads`](backup-capacity-options.md) option.

For an apply-log operation, the [`--process-threads`](backup-capacity-options.md) option controls the number of threads that read and write modified datafile pages in parallel; those threads are usually I/O bound, even though they also perform some in-memory processing.

Depending on your operating system, you can measure resource utilization using commands such as **top**, **iostat**, **sar**, **dtrace**, or a graphical performance monitor. Do not increase the number of read or write threads `iowait` once the system `iowait` value reaches approximately 20%.