---
title: "13.1 Optimizing Backup Performance"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/backup-performance.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

This section describes the performance considerations for backing up a database with MySQL Enterprise Backup. When optimizing and tuning the backup procedure, measure both the raw performance (how long it takes the backup to complete) and the amount of overhead on the database server. When measuring backup performance, consider:

- The limits imposed by your backup procedures. For example, if you take a backup every 8 hours, the backup must take less than 8 hours to finish.
- The limits imposed by your network and storage infrastructure. For example, if you need to fit many backups on a particular storage device, you might use compressed backups, even if that made the backup process slower.
- The tradeoff between backup time and restore time. You might choose a set of options resulting in a slightly slower backup, if those options enable the restore to be much faster. See [Section 13.2, “Optimizing Restore Performance”](restore-performance.md) for performance information for the restore process.

### Full or Incremental Backup

After taking a full backup, subsequent backups can be performed more quickly by doing incremental backups, where only the changed data is backed up. For an incremental backup, specify the [`--incremental`](backup-incremental-options.md) or [`--incremental-with-redo-log-only`](backup-incremental-options.md) option to **mysqlbackup**. See [Section 20.7, “Incremental Backup Options”](backup-incremental-options.md) for information about these options. For usage instructions for the backup and apply stages of incremental backups, see [Section 4.3.3, “Making a Differential or Incremental Backup”](mysqlbackup.incremental.md).

### Compressed Backup

Compressing the backup data before transmitting it to another server involves additional CPU overhead on the database server where the backup takes place, but less network traffic and less disk I/O on the server that is the final destination for the backup data. Consider the load on your database server, the bandwidth of your network, and the relative capacities of the database and destination servers when deciding whether or not to use compression. See [Section 4.3.4, “Making a Compressed Backup”](backup.compressed.md) and [Section 20.6, “Compression Options”](backup-compression-options.md) for information about creating compressed backups.

Compression involves a tradeoff between backup performance and restore performance. In an emergency, the time needed to uncompress the backup data before restoring it might be unacceptable. There might also be storage issues if there is not enough free space on the database server to hold both the compressed backup and the uncompressed data. Thus, the more critical the data is, the more likely that you might choose not to use compression: accepting a slower, larger backup to ensure that the restore process is as fast and reliable as possible.

### InnoDB Configuration Options Settings

As discussed later, there are a number of reasons why you might prefer to run with the setting [`innodb_file_per_table=1`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#sysvar_innodb_file_per_table).

### Parallel Backup

**mysqlbackup** can take advantage of modern multicore CPUs and operating system threads to perform backup operations in parallel. See [Section 20.10, “Performance / Scalability / Capacity Options”](backup-capacity-options.md) for the options to control how many threads are used for different aspects of the backup process. If you see that there is unused system capacity during backups, consider increasing the values for these options and testing whether doing so increases backup performance:

- When tuning and testing backup performance using a RAID storage configuration, consider the combination of option settings `--read-threads=3 --process-threads=6         --write-threads=3`. Compare against the combination `--read-threads=1 --process-threads=6         --write-threads=1`.
- When tuning and testing backup performance using a non-RAID storage configuration, consider the combination of option settings `--read-threads=1 --process-threads=6         --write-threads=1`.
- When you increase the values for any of the 3 “threads” options, also increase the value of the [`--limit-memory`](backup-capacity-options.md) option, to give the extra threads enough memory to do their work.
- If the CPU is not too busy (less than 80% CPU utilization), increase the value of the [`--process-threads`](backup-capacity-options.md) option.
- If the storage device that you are backing up from (the source drive) can handle more I/O requests, increase the value of the [`--read-threads`](backup-capacity-options.md) option.
- If the storage device that you are backing up to (the destination drive) can handle more I/O requests, increase the value of the [`--write-threads`](backup-capacity-options.md) option (not applicable to single-file backups, which always use a single write thread).

Depending on your operating system, you can measure resource utilization using commands such as **top**, **iostat**, **sar**, **dtrace**, or a graphical performance monitor. Do not increase the number of read or write threads once the system `iowait` value reaches approximately 20%.

### MyISAM Considerations

Important

- Although **mysqlbackup** backs up InnoDB tables without interrupting database use, the final stage that copies non-InnoDB files (such as MyISAM tables and `.sdi` files) temporarily puts those tables into a read-only state, using the statement ``FLUSH           TABLES *`tbl_name [, tbl_name]`* ...           WITH READ LOCK``. For best backup performance and minimal impact on database processing:
	1. Do not run long [INSERT](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/insert.html), [UPDATE](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/update.html), or [DELETE](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/delete.html) queries at the time of the backup run.
	2. Keep your MyISAM tables relatively small and primarily for read-only or read-mostly work.
	Then the time where non-InnoDB tables are read-locked will be short and the normal processing of **mysqld** will not be disturbed much. If the preceding conditions are not met in your database application, use the [`--only-innodb`](backup-partial-options.md) option to back up only InnoDB tables, or use the [`--no-locking`](backup-capacity-options.md) option. Note that files copied under the `--no-locking` setting cannot be guaranteed to have consistent data.
- For a large database server, a backup run might take a long time. Always check that **mysqlbackup** has completed successfully, either by verifying that **mysqlbackup** returned exit code 0, or by observing that **mysqlbackup** has printed the text “mysqlbackup completed OK!”.
- Schedule backups during periods when no DDL operations involving tables are running. See [Appendix B, *Limitations of MySQL Enterprise Backup*](bugs.backup.md) for restrictions on backups at the same time as DDL operations.

### Network Performance

For data processing operations, you might know the conventional advice that Unix sockets are faster than TCP/IP for communicating with the database server. Although the **mysqlbackup** command supports the options `--protocol=tcp`, `--protocol=socket`, and `--protocol=pipe`, these options do not have a significant effect on backup or restore performance. These processes involve file-copy operations rather than client/server network traffic. The database server communication controlled by the `--protocol` option is low-volume. For example, **mysqlbackup** retrieves information about database server parameters through the database server connection, but not table or index data.

### Data Size

If certain tables or databases contain non-critical information, or are rarely updated, you can leave them out of your most frequent backups and back them up on a less frequent schedule. See [Section 20.8, “Partial Backup and Restore Options”](backup-partial-options.md) for information about the relevant options, and [Section 4.3.5, “Making a Partial Backup”](partial.md) for instructions about leaving out data from specific tables, databases, or storage engines. Partial backups are faster because they copy, compress, and transmit a smaller volume of data.

To minimize the overall size of `InnoDB` data files, consider enabling the MySQL configuration option [`innodb_file_per_table`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#sysvar_innodb_file_per_table). This option can minimize data size for `InnoDB` tables in several ways:

- It prevents the `InnoDB` system tablespace from ballooning in size, allocating disk space that can afterwards only be used by MySQL. For example, sometimes huge amounts of data are only needed temporarily, or are loaded by mistake or during experimentation. Without the [`innodb_file_per_table`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#sysvar_innodb_file_per_table) option, the system tablespace expands to hold all this data, and never shrinks afterward.
- It immediately frees the disk space taken up by an `InnoDB` table and its indexes when the table is dropped or truncated. Each table and its associated indexes are represented by a [.ibd file](glossary.md) that is deleted or emptied by these DDL operations.
- It allows unused space within a `.ibd` file to be reclaimed by the [`OPTIMIZE         TABLE`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/optimize-table.html) statement, when substantial amounts of data are removed or indexes are dropped.
- It enables partial backups where you back up some `InnoDB` tables and not others, as discussed in [Section 4.3.5, “Making a Partial Backup”](partial.md).
- It allows the use of table compression for InnoDB tables.

In general, using table compression by having `ROW_FORMAT=COMPRESSED` decreases table sizes and increase backup and restore performance. However, as a trade-off, table compression can potentially increase redo log sizes and thus slow down incremental backups and restores, as well as [`apply-log`](backup-commands-update.md) operations. See [How Compression Works for InnoDB Tables](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-compression-internals.html) for details.

Avoid creating indexes that are not used by queries. Because indexes take up space in the backup data, unnecessary indexes slow down the backup process. (The copying and scanning mechanisms used by **mysqlbackup** do not rely on indexes to do their work.) For example, it is typically not helpful to create an index on each column of a table, because only one index is used by any query. Because the primary key columns are included in each `InnoDB` secondary index, it wastes space to define primary keys composed of numerous or lengthy columns, or multiple secondary indexes with different permutations of the same columns.

### Advanced: Apply-Log Phase (for Directory Backups only)

If you store the backup data on a separate machine, and that machine is not as busy the machine hosting the database server, you can offload some postprocessing work (the [apply-log](glossary.md) phase) to that separate machine. [Apply-log Operation](backup-commands-update.md)

There is always a performance tradeoff between doing the apply-log phase immediately after the initial backup (makes restore faster), or postponing it until right before the restore (makes backup faster). In an emergency, restore performance is the most important consideration. Thus, the more crucial the data is, the more important it is to run the apply-log phase immediately after the backup. Either combine the backup and apply-log phases on the same server by specifying the [`backup-and-apply-log`](backup-commands-backup.md) option, or perform the fast initial backup, transfer the backup data to another server, and then perform the apply-log phase using one of the options from [Apply-log Operation](backup-commands-update.md).