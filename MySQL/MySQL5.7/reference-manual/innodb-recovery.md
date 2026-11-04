---
title: "14.19.2 InnoDB Recovery"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/innodb-recovery.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 14.19.2 InnoDB Recovery

This section describes `InnoDB` recovery. Topics include:

#### Point-in-Time Recovery

To recover an `InnoDB` database to the present from the time at which the physical backup was made, you must run MySQL server with binary logging enabled, even before taking the backup. To achieve point-in-time recovery after restoring a backup, you can apply changes from the binary log that occurred after the backup was made. See [Section 7.5, “Point-in-Time (Incremental) Recovery”](point-in-time-recovery.md).

#### Recovery from Data Corruption or Disk Failure

If your database becomes corrupted or disk failure occurs, you must perform the recovery using a backup. In the case of corruption, first find a backup that is not corrupted. After restoring the base backup, do a point-in-time recovery from the binary log files using [**mysqlbinlog**](mysqlbinlog.md) and [**mysql**](mysql.md) to restore the changes that occurred after the backup was made.

In some cases of database corruption, it is enough to dump, drop, and re-create one or a few corrupt tables. You can use the [`CHECK TABLE`](check-table.md) statement to check whether a table is corrupt, although [`CHECK         TABLE`](check-table.md) naturally cannot detect every possible kind of corruption.

In some cases, apparent database page corruption is actually due to the operating system corrupting its own file cache, and the data on disk may be okay. It is best to try restarting the computer first. Doing so may eliminate errors that appeared to be database page corruption. If MySQL still has trouble starting because of `InnoDB` consistency problems, see [Section 14.22.2, “Forcing InnoDB Recovery”](forcing-innodb-recovery.md) for steps to start the instance in recovery mode, which permits you to dump the data.

#### InnoDB Crash Recovery

To recover from an unexpected MySQL server exit, the only requirement is to restart the MySQL server. `InnoDB` automatically checks the logs and performs a roll-forward of the database to the present. `InnoDB` automatically rolls back uncommitted transactions that were present at the time of the crash. During recovery, [**mysqld**](mysqld.md) displays output similar to this:

```
InnoDB: Log scan progressed past the checkpoint lsn 369163704
InnoDB: Doing recovery: scanned up to log sequence number 374340608
InnoDB: Doing recovery: scanned up to log sequence number 379583488
InnoDB: Doing recovery: scanned up to log sequence number 384826368
InnoDB: Doing recovery: scanned up to log sequence number 390069248
InnoDB: Doing recovery: scanned up to log sequence number 395312128
InnoDB: Doing recovery: scanned up to log sequence number 400555008
InnoDB: Doing recovery: scanned up to log sequence number 405797888
InnoDB: Doing recovery: scanned up to log sequence number 411040768
InnoDB: Doing recovery: scanned up to log sequence number 414724794
InnoDB: Database was not shutdown normally!
InnoDB: Starting crash recovery.
InnoDB: 1 transaction(s) which must be rolled back or cleaned up in
total 518425 row operations to undo
InnoDB: Trx id counter is 1792
InnoDB: Starting an apply batch of log records to the database...
InnoDB: Progress in percent: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37
38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59
60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99
InnoDB: Apply batch completed
...
InnoDB: Starting in background the rollback of uncommitted transactions
InnoDB: Rolling back trx with id 1511, 518425 rows to undo
...
InnoDB: Waiting for purge to start
InnoDB: 5.7.18 started; log sequence number 414724794
...
./mysqld: ready for connections.
```

`InnoDB` [crash recovery](glossary.md) consists of several steps:

- Tablespace discovery
	Tablespace discovery is the process that `InnoDB` uses to identify tablespaces that require redo log application. See Tablespace Discovery During Crash Recovery.
- [Redo log](glossary.md) application
	Redo log application is performed during initialization, before accepting any connections. If all changes are flushed from the [buffer pool](glossary.md) to the [tablespaces](glossary.md) (`ibdata*` and `*.ibd` files) at the time of the shutdown or crash, redo log application is skipped. `InnoDB` also skips redo log application if redo log files are missing at startup.
	Removing redo logs to speed up recovery is not recommended, even if some data loss is acceptable. Removing redo logs should only be considered after a clean shutdown, with [`innodb_fast_shutdown`](innodb-parameters.md) set to `0` or `1`.
	For information about the process that `InnoDB` uses to identify tablespaces that require redo log application, see Tablespace Discovery During Crash Recovery.
- [Roll back](glossary.md) of incomplete [transactions](glossary.md)
	Incomplete transactions are any transactions that were active at the time of unexpected exit or [fast shutdown](glossary.md). The time it takes to roll back an incomplete transaction can be three or four times the amount of time a transaction is active before it is interrupted, depending on server load.
	You cannot cancel transactions that are being rolled back. In extreme cases, when rolling back transactions is expected to take an exceptionally long time, it may be faster to start `InnoDB` with an [`innodb_force_recovery`](innodb-parameters.md) setting of `3` or greater. See [Section 14.22.2, “Forcing InnoDB Recovery”](forcing-innodb-recovery.md).
- [Change buffer](glossary.md) merge
	Applying changes from the change buffer (part of the [system tablespace](glossary.md)) to leaf pages of secondary indexes, as the index pages are read to the buffer pool.
- [Purge](glossary.md)
	Deleting delete-marked records that are no longer visible to active transactions.

The steps that follow redo log application do not depend on the redo log (other than for logging the writes) and are performed in parallel with normal processing. Of these, only rollback of incomplete transactions is special to crash recovery. The insert buffer merge and the purge are performed during normal processing.

After redo log application, `InnoDB` attempts to accept connections as early as possible, to reduce downtime. As part of crash recovery, `InnoDB` rolls back transactions that were not committed or in `XA         PREPARE` state when the server exited. The rollback is performed by a background thread, executed in parallel with transactions from new connections. Until the rollback operation is completed, new connections may encounter locking conflicts with recovered transactions.

In most situations, even if the MySQL server was killed unexpectedly in the middle of heavy activity, the recovery process happens automatically and no action is required of the DBA. If a hardware failure or severe system error corrupted `InnoDB` data, MySQL might refuse to start. In this case, see [Section 14.22.2, “Forcing InnoDB Recovery”](forcing-innodb-recovery.md).

For information about the binary log and `InnoDB` crash recovery, see [Section 5.4.4, “The Binary Log”](binary-log.md).

#### Tablespace Discovery During Crash Recovery

If, during recovery, `InnoDB` encounters redo logs written since the last checkpoint, the redo logs must be applied to affected tablespaces. The process that identifies affected tablespaces during recovery is referred to as *tablespace discovery*.

Tablespace discovery is performed by scanning redo logs from the last checkpoint to the end of the log for `MLOG_FILE_NAME` records that are written when a tablespace page is modified. An `MLOG_FILE_NAME` record contains the tablespace space ID and file name.

On startup, `InnoDB` opens the system tablespace and redo log. If there are redo log records written since the last checkpoint, affected tablespace files are opened based on `MLOG_FILE_NAME` records.

`MLOG_FILE_NAME` records are written for all persistent tablespace types including file-per-table tablespaces, general tablespaces, the system tablespace, and undo log tablespaces.

Redo-log-based discovery has the following characteristics:

- Only tablespace `*.ibd` files modified since the last checkpoint are accessed.
- Tablespace `*.ibd` files that are not attached to the `InnoDB` instance are ignored when redo logs are applied.
- If `MLOG_FILE_NAME` records for the system tablespace do not match the server configuration affecting system tablespace data file names, recovery fails with an error before redo logs are applied.
- If tablespace files referenced in the scanned portion of the log are missing, startup is refused.
- Redo logs for missing tablespace `*.ibd` files are only disregarded if there is a file-delete redo log record (`MLOG_FILE_DELETE`) in the log. For example, a table rename failure could result in a “missing” `*.ibd` file without an `MLOG_FILE_DELETE` record. In this case, you could manually rename the tablespace file and restart crash recovery, or you could restart the server in recovery mode using the [`innodb_force_recovery`](innodb-parameters.md) option. Missing `*.ibd` files are ignored when the server is started in recovery mode.

Redo-log-based discovery, introduced in MySQL 5.7, replaces directory scans that were used in earlier MySQL releases to construct a “space ID-to-tablespace file name” map that was required to apply redo logs.