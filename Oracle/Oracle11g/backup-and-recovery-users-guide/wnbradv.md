---
title: "What's New in Backup and Recovery?"
book: "Backup and Recovery User's Guide"
doc_id: E10642-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10642/wnbradv.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-users-guide
---

This section describes new features of backup and recovery for Oracle Database 11g Release 2 and provides pointers to additional information.

The release of Recovery Manager (RMAN) continues to enhance and extend the reliability, efficiency, and availability of Oracle Database backup and recovery. Some highlights in this release are the inclusion of Oracle's Database Backup Cloud offering, referred to as Oracle Secure Backup (OSB) Cloud Module, the addition of Expanded Backup Compression Levels, and several DUPLICATE Database Command Enhancements.

## New Backup and Recovery Features for Oracle 11g Release 2

The following Backup and Recovery features are new in Oracle Database 11g Release 2 (11.2):

- Oracle Secure Backup (OSB) Cloud Module
	Users can take advantage of the Internet-based data storage services offered by Amazon Simple Storage Service (Amazon S3) for their RMAN backup and recovery tasks. The OSB Cloud Module interface extends the Amazon S3 functionality and provides an easy-to-manage, cost-efficient, and scalable alternative to maintaining in-house data storage and a local, fully configured backup infrastructure.
	See Also:
	Appendix C in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/web_services001.htm#RCMRF90490)
- DUPLICATE Database Command Enhancements
	Users can duplicate a database without connecting to a target database. The only requirements for this operation are a connection to a catalog and an auxiliary database. This new functionality is useful when the target database is not always available.
	Users can also duplicate a database without connecting to a target database and a recovery catalog. In this case, the only requirement is that you provide a disk backup location where RMAN can find all the backups, data file copies, archived logs, and control file copies for database duplication. This database duplication enhancement is helpful when it is not possible to connect to the target database and the recovery catalog.
	When you duplicate from a target database, RMAN determines if any excluded tablespaces contain `SYS-` owned objects, materialized views, and identifies tablespaces that are not self-contained before starting any duplication operations.
	See Also:
	[Chapter 24, "Duplicating a Database"](rcmdupdb.md), and [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta020.htm#RCMRF126) to learn about the associated `DUPLICATE` command options `NOREDO` and `UNDO TABLESPACE`
- RMAN Tablespace Point-in-Time Recovery (TSPITR) Enhancements
	TSPITR can be used to recover a dropped tablespace and to recover to a point in time before the tablespace was brought online. The latter TSPITR operation can be repeated as many times as necessary.
	Note:
	Before this release, TSPITR did not operate on dropped tablespaces.
- Automatic Block Repair
	The enhancements to corrupt block detection make block repair more efficient and increase availability. The automatic block repair enhancement complements the Oracle Database 11g Release 1 automatic block corruption detection.
	A detected corrupt block (for example, through a user's SQL query) is now automatically repaired by using a good block from a physical standby database. With automatic block repair, a user querying data in the corrupt block no longer sees the corrupt block error message displayed (`ORA-01578`). Instead, there is a pause while the corrupt block is repaired, and then the results of the SQL query are returned. The automatic block repair is transparent to the user unless the repair fails. Block recovery is faster because no redo must be applied to the block that is taken from the physical standby database.
	Automatic block repair requires an Oracle Active Data Guard license because real-time query mode must be enabled on the physical standby database.
	The operation occurs automatically but can also be explicitly invoked with the RMAN `RECOVER BLOCK` command.
	See Also:
	[Chapter 19, "Performing Block Media Recovery"](rcmblock.md) and the [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2001.htm#RCMRF140) `RECOVER` command
- `SET NEWNAME` Options
	The `SET NEWNAME` command is more powerful and easier to use. You can use this command on a specific tablespace or on all data files and temp files. You can also change the names for multiple files in the database.
	A new string format identifier " `%b` " makes it easier to move files around. Using `SET NEWNAME` with the format identifier " `%b` " enables you to designate a file name without its directory path. This option is particularly useful when you want to keep the names of your data files the same but move the data files to a different directory location.

See Also:

- [Chapter 25, "Duplicating a Database: Advanced Topics"](rcmdupad.md)
- [Example 25-2, "Duplicating with SET NEWNAME FOR DATAFILE and FOR TABLESPACE"](rcmdupad.md)
- The `SET` option in the [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/toc.htm) to learn about the enhanced `SET NEWNAME` functionality

- `CONVERT DATABASE` Option
	A new option, `SKIP UNNECESSARY DATAFILES,` is now supported for the `CONVERT DATABASE` command. When the option is invoked, the only data files that are converted are those that require RMAN processing during transfer between the specified platforms. The rest of the data files can be used by the destination database through shared storage or path name. By skipping the conversion of data files that do not contain undo segments, overall database transport time can be reduced. You can use this option when converting at the source or converting `ON DESTINATION PLATFORM`.

See Also:

The `CONVERT DATABASE` option in the [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta012.htm#RCMRF90102)

- Expanded Backup Compression Levels
	RMAN now offers a wider range of compression levels with the Advanced Compression Option (ACO). Although the existing `BASIC` compression option may be suitable for most environments, you may want to explore the ACO backup compression levels (`LOW`, `MEDIUM`, and `HIGH`) to achieve better performance or higher compression ratios.

See Also:

["Binary Compression for Backup Sets"](rcmcncpt.md) and the `CONFIGURE`... `COMPRESSION ALGORITHM` command option in the [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113)

- `INCARNATION` Specifier Enhancement
	Incarnations may now be used to further qualify archived redo log ranges for the `BACKUP`, `RESTORE`, and `LIST` commands. You can now specify `ALL` or `CURRENT` or designate a particular incarnation number when listing ranges of archived logs.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl002.htm#RCMRF90421) for settings and examples

- `TO DESTINATION` syntax has been added to the `BACKUP` command. This addition enables you to designate a specific directory location for backups to disk and is primarily for use with the `BACKUP RECOVERY AREA` command. If backup optimization is enabled, then RMAN only skips backups of identical files that reside in the directory location specified by the `TO DESTINATION` option.

See Also:

`BACKUP` command and examples of the new setting in the [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta003.htm#RCMRF166)

### Changes in RMAN Functionality or Prerequisites

The Block Change Tracking feature can be used at a physical standby database only if the Oracle Active Data Guard option is licensed.