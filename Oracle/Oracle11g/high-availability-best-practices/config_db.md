---
title: Configuring Oracle Database
book: High Availability Best Practices
doc_id: E10803-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10803/config_db.htm
tags:
  - oracle
  - 11g
  - high-availability-best-practices
---

## 5 Configuring Oracle Database

This chapter describes best practices for configuring all Oracle databases, including single-instance, Oracle RAC databases, Oracle RAC One Node databases, and the primary and standby databases in Oracle Data Guard configurations (for more information about High Availability architectures, see [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/architectures.htm#HAOVW004)). Adopt these best practices to reduce or avoid outages, reduce the risk of corruption, and to improve recovery performance.

This chapter contains the following topics:

- Database Configuration High Availability and Fast Recoverability Best Practices
- Recommendations to Improve Manageability

See Also:

[Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/architectures.htm#HAOVW004) for more information about high availability architectures

## 5.1 Database Configuration High Availability and Fast Recoverability Best Practices

To reduce recovery time and increase database availability and redundancy:

### 5.1.1 Set the Database ARCHIVELOG Mode and FORCE LOGGING Mode

Running the database in `ARCHIVELOG` mode and using database `FORCE LOGGING` mode are prerequisites for database recovery operations. The `ARCHIVELOG` mode enables online database backup and is necessary to recover the database to a point in time later than what has been restored. Features such as Oracle Data Guard and Flashback Database require that the production database run in `ARCHIVELOG` mode.

If you can isolate data that never needs to be recovered within specific tablespaces, then you can use tablespace level `FORCE` `LOGGING` attributes instead of the database `FORCE` `LOGGING` mode.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/archredo.htm#ADMIN11333) for more information about controlling archiving mode
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11096) for information about Specifying `FORCE` `LOGGING` Mode
- See “Reduce Overhead and Redo Volume During ETL Operations in the technical white paper, "Oracle Data Guard: Disaster Recovery for Oracle Exadata Database Machine" from the MAA Best Practices area for Exadata Database Machine at
	`http://www.oracle.com/goto/maa`

### 5.1.2 Configure the Size of Redo Log Files and Groups Appropriately

Use Oracle log multiplexing to create multiple redo log members in each redo group, one in the data area and one in the Fast Recovery Area (unless the redo logs are in an Oracle ASM high redundancy disk group). This protects against a failure involving the redo log, such as a disk or I/O failure for one member, or a user error that accidentally removes a member through an operating system command. If at least one redo log member is available, then the instance can continue to function.

To size redo log files and groups:

- Use a minimum of three redo log groups: this helps prevent the log writer process (LGWR) from waiting for a group to be available following a log switch.
- All online redo logs and standby redo logs are equal size.
- Use redo log size = 4GB or redo log size >= peak redo rate x 20 minutes
- Locate redo logs on high performance disks.
- Place log files in a high redundancy disk group, or multiplex log files across different normal redundancy disk groups, if using ASM redundancy.
	Note:
	Do not multiplex the standby redo logs.

See Also:

- [Chapter 9, "Configuring Oracle Data Guard"](config_dg.md)
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/onlineredo.htm#ADMIN007) for more information about managing redo logs
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/onlineredo.htm#ADMIN11309) for information about Multiplexing Redo Log Files
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/standby.htm#SBYDB00100) for more information about online, archived, and standby redo log files

### 5.1.3 Use a Fast Recovery Area

The Fast Recovery Area is Oracle managed disk space that provides a centralized disk location for backup and recovery files.

The Fast Recovery Area is defined by setting the following database initialization parameters:

- `DB_RECOVERY_FILE_DEST`: specifies the default location for the fast recovery area.
- `DB_RECOVERY_FILE_DEST_SIZE`: specifies (in bytes) the hard limit on the total space to be used by database recovery files created in the recovery area location.

The Oracle Suggested Backup Strategy described in the [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/backrest.htm#ADMQS09322) recommends using the fast recovery area as the primary location for recovery. When the fast recovery area is properly sized, files needed for repair are readily available. The minimum recommended disk limit is the combined size of the database, incremental backups, all archived redo logs that have not been copied to tape, and flashback logs.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11103) for information about Specifying a Fast Recovery Area
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfb.htm#BRADV89422) for detailed information about sizing the fast recovery area and setting the retention period
- [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/backrest.htm#ADMQS09322)

### 5.1.4 Enable Flashback Database

Flashback Database provides an efficient alternative to point-in-time recovery for reversing unwanted database changes. Flashback Database enables you to rewind an entire database backward in time, reversing the effects of database changes within a time window. The effects are similar to database point-in-time recovery (DBPITR). You can flash back a database by issuing a single RMAN command or a SQL\*Plus statement instead of using a complex procedure.

To enable Flashback Database, you configure a fast recovery area and set a flashback retention target. This retention target specifies how far back you can rewind a database with Flashback Database. For more information about specifying a fast recovery area, see Section 5.1.3, "Use a Fast Recovery Area".

When configuring and enabling Flashback Database:

- Know your application performance baseline before you enable flashback to help determine the overhead and to assess the application workload implications of turning on flashback database.
- Ensure the fast recovery area space is sufficient to hold the flashback database flashback logs. For more information about sizing the fast recovery area, see the [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfb.htm#BRADV89422). A general rule of thumb is to note that the volume of flashback log generation is approximately the same order of magnitude as redo log generation. For example, if you intend to set `DB_FLASHBACK_RETENTION_TARGET` to 24 hours, and if the database generates 20 GB of redo in a day, then a rule of thumb is to allow 20 GB to 30 GB disk space for the flashback logs. The same rule applies for guaranteed restore points. For example, if the database generates 20 GB redo every day, and if the guaranteed restore point will be kept for a day, then plan to allocate 20 to 30 GB.
	- An additional method to determine fast recovery area sizing is to enable flashback database and allow the database to run for a short period (2-3 hours). The estimated amount of space required for the fast recovery area can be retrieved by querying `V$FLASHBACK_DATABASE_STAT.ESTIMATED_FLASHBACK_SIZE`.
		- Note that the `DB_FLASHBACK_RETENTION_TARGET` is a target and there is no guarantee that you can flashback the database that far. In some cases if there is space pressure in the fast recovery area where the flashback logs are stored then the oldest flashback logs may be deleted. For a detailed explanation of the fast recovery area deletion rules see the [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmmaint.htm#BRADV89612). To guarantee a flashback point-in-time you must use guaranteed restore points.
- Set the Oracle Enterprise Manager monitoring metric, "Recovery Area Free Space (%)" for proactive alerts of space issues with the fast recovery area.
- Ensure there is sufficient I/O bandwidth to the fast recovery area. Insufficient I/O bandwidth with flashback database on is usually indicated by a high occurrence of the `"FLASHBACK BUF FREE BY RVWR"` wait event in an Automatic Workload Repository (AWR) report.
- Set the `LOG_BUFFER` initialization parameter to at least 8 MB to give flashback database more buffer space in memory. For large databases with more than a 4GB SGA, you may consider setting `LOG_BUFFER` to values in the range of 32-64 MB (for more information about `LOG_BUFFER` and valid values on 32-bit and 64-bit operating systems, see [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams133.htm#REFRN10094)).
- Set the parameter `PARALLEL_EXECUTION_MESSAGE_SIZE` to at least 8192. This improves the media recovery phase of any flashback database operation.
- If you have a Data Guard standby database, always set `DB_FLASHBACK_RETENTION_TARGET` to the same value on the standby database(s) as the primary. Set `DB_FLASHBACK_RETENTION_TARGET` initialization parameter to the largest value prescribed by any of the following conditions that apply:
	- To leverage flashback database to reinstate your failed primary database after Data Guard failover, for most cases set `DB_FLASHBACK_RETENTION_TARGET` to a minimum of 60 (mins) to enable reinstatement of a failed primary.
		- Consider cases where there are multiple outages, for example, first a network outage, followed later by a primary database outage, that may result in a transport lag between primary and standby database at failover time. For such cases set `DB_FLASHBACK_RETENTION_TARGET` to a value equal to the sum of 60 (mins) plus the maximum transport lag to accommodate. This ensures that the failed primary database can be flashed back to an SCN that precedes the SCN at which the standby became primary - a requirement for primary reinstatement.
		- If using Flashback Database for fast point in time recovery from user error or logical corruptions, set `DB_FLASHBACK_RETENTION_TARGET` to a value equal to the farthest time in the past to which the database should be recovered.
- Review [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfb.htm#BRADV8183) for information about Configuring the Fast Recovery Area.
- To monitor the progress of a flashback database operation you can query the `V$SESSION_LONGOPS` view. An example query to monitor progress is:
	```
	select * from v$session_longops where opname like 'Flashback%';
	```
- For repetitive tests where you must flashback to the same point, use Flashback database guaranteed restore points (GRP) instead of enabling flashback database to minimize space utilization.
- In general, the performance effect of enabling Flashback Database is minimal. In 11.2.0.2 there are significant performance enhancements to nearly eliminate any overhead when you first enable flashback database, and during batch direct loads. For more information, see "Flashback Database Best Practices & Performance" in My Oracle Support Note 565535.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=565535.1`

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/flashdb.htm#BRADV180) for more information about guaranteed restore points and Flashback Database
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/flashdb.htm#BRADV598) for information about configuring the environment for optimal Flashback Database performance
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/flashdb.htm#BRADV71000) for information about configuring Oracle Flashback Database and Restore Points
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/role_management.htm#SBYDB4774) for information about Using Flashback Database After a Role Transition
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/scenarios.htm#SBYDB00910) for information about Converting a Failed Primary Into a Standby Database Using Flashback Database
- [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10822/tdppt_method.htm#TDPPT007) for information about Gathering Database Statistics Using the Automatic Workload Repository (AWR)
- The MAA white paper "Active Data Guard 11g Best Practices (includes best practices for Redo Apply)" for more information about media recovery best practices from the MAA Best Practices area for Oracle Database at
	`http://www.oracle.com/goto/maa`

### 5.1.5 Set FAST START MTTR TARGET Initialization Parameter

The Fast-Start Fault Recovery feature reduces the time required to recover from a crash and makes the recovery bounded and predictable by limiting the number of dirty buffers and the number of redo records generated between the most recent redo record and the last checkpoint.

Set the `FAST_START_MTTR_TARGET` initialization parameter to control instance recovery time. With the Fast-Start Fault Recovery feature, the `FAST_START_MTTR_TARGET` initialization parameter simplifies the configuration of recovery time from instance or system failure. This parameter specifies a target for the expected [recovery time objective (RTO)](glossary.md), which is the time, in seconds, that it should take to start the instance and perform cache recovery. When you set this parameter, the database manages incremental checkpoint writes in an attempt to meet the target. If you have chosen a practical value for this parameter, then you can expect your database to recover, on average, in approximately the number of seconds you have chosen.

Initially, set the `FAST_START_MTTR_TARGET` initialization parameter to 300 (seconds) or to the value required for your expected [recovery time objective (RTO)](glossary.md).

Outage testing for cases such as for node or instance failures during peak loads is recommended.

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/instance_tune.htm#PFGRF13009) for information about Tuning Instance Recovery Performance: Fast-Start Fault Recovery
- The MAA white paper "Optimizing Availability During Unplanned Outages Using Oracle Clusterware and Oracle RAC" for more best practices from the MAA Best Practices area for Oracle Database at
	`http://www.oracle.com/goto/maa`

### 5.1.6 Protect Against Data Corruption

A data block is corrupted when it is not in a recognized Oracle Database format, or its contents are not internally consistent. Data block corruption can damage internal Oracle control information or application and user data, leading to crippling loss of critical data and services. The Oracle Database corruption prevention, detection, and repair capabilities are built on internal knowledge of the data and transactions it protects, and on the intelligent integration of its comprehensive high availability solutions. For more information about recovery from data corruption, see [Section 13.2.6, "Recovering from Data Corruption"](outage.md).

Once the corruption is detected, Oracle offers Data Guard, block media recovery, and data file media recovery to recover the data. Database-wide logical corruptions caused by human or application errors can be undone with Oracle Flashback Technologies. Tools are also available for proactive validation of logical data structures. For example, the SQL\*Plus `ANALYZE TABLE` statement detects inter-block corruptions.

See Also:

- "Preventing, Detecting, and Repairing Block Corruption: Database 11g" MAA white paper from the MAA Best Practices area for Oracle Database at
	`http://www.oracle.com/goto/maa`
- "Best Practices for Corruption Detection, Prevention, and Automatic Repair - in a Data Guard Configuration" in My Oracle Support Note 1302539.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1302539.1`

#### 5.1.6.1 Preventing Widespread Data Corruption

To achieve the most comprehensive data corruption prevention and detection:

- Use Oracle Data Guard with physical standby databases to prevent widespread block corruption. Oracle Data Guard is the best solution for protecting Oracle data against data loss and corruption, and lost writes. For more information, see [Section 9.3, "General Data Guard Configuration Best Practices"](config_dg.md).
- Set the Oracle Database block-corruption initialization parameters on the Data Guard primary and standby databases:
	| On the Primary database set... | On the Standby databases set... |
	| --- | --- |
	| ``` DB_BLOCK_CHECKSUM=FULL DB_LOST_WRITE_PROTECT=TYPICAL DB_BLOCK_CHECKING=FULL ``` | ``` DB_BLOCK_CHECKSUM=FULL DB_LOST_WRITE_PROTECT=TYPICAL DB_BLOCK_CHECKING=FULL ``` |
	Performance overhead is incurred on every block change, therefore performance testing is of particular importance when setting the `DB_BLOCK_CHECKING` parameter. Oracle highly recommends the minimum setting of `DB_BLOCK_CHECKING=MEDIUM` (block checks on data blocks but not index blocks) on either the primary or standby database. If the performance overhead of enabling `DB_BLOCK_CHECKING` to `MEDIUM` or `FULL` is unacceptable on your primary database, then set `DB_BLOCK_CHECKING` to `MEDIUM` or `FULL` for your standby databases.
	Caution:
	A thorough performance assessment is recommended when changing these settings.
	See Also:
	- [Section 9.3.8, "Use Data Guard Redo Apply Best Practices"](config_dg.md)
	- For the most current information, see the My Oracle Support Note 1302539.1: "Best Practices for Corruption Detection, Prevention, and Automatic Repair - in a Data Guard Configuration" at
		`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1302539.1`
- Use Oracle Automatic Storage Management (Oracle ASM) to provide disk mirroring to protect against disk failures. For more information, see [Section 4.2, "Use Automatic Storage Management (Oracle ASM) to Manage Database Files"](config_storage.md).
- Use Oracle ASM `HIGH REDUNDANCY` for optimal corruption repair. Using Oracle ASM redundancy for disk groups provides mirrored extents that can be used by the database if an I/O error or corruption is encountered. For continued protection, Oracle ASM redundancy provides the ability to move an extent to a different area on a disk if an I/O error occurs. The Oracle ASM redundancy mechanism is useful if you have bad sectors returning media sense errors. For more information, see [Section 4.3.2, "Use Redundancy to Protect from Disk Failure"](config_storage.md).
- Use the Oracle Active Data Guard option for automatic block repair. For more information about Active Data Guard, see [Section 9.5, "Use Oracle Active Data Guard Best Practices"](config_dg.md).
- Configure and use Configure Data Recovery Advisor to automatically diagnose data failures. For more information, see Section 5.2.2, "Use Data Recovery Adviser to Detect, Analyze and Repair Data Failures".
- Enable Flashback Technologies for fast point-in-time recovery from logical corruptions most often caused by human error and for fast reinstatement of a primary database following failover. For more information, see Section 5.1.4, "Enable Flashback Database".
- Implement a backup and recovery strategy with Recovery Manager (RMAN) and periodically use the RMAN `BACKUP VALIDATE CHECK LOGICAL...` scan to detect corruptions. For more information, see [Chapter 8, "Configuring Backup and Recovery."](config_backuprec.md) Use RMAN and Oracle Secure Backup for additional block checks during backup and restore operations.

#### 5.1.6.2 Detecting and Monitoring Data Corruption

If corrupt data is written to disk or if a component failure causes good data to become corrupt after it is written, then it is critical to detect the corrupted blocks as soon as possible.

To monitor the database for errors and alerts:

- Use Enterprise Manager to monitor the availability of all discovered targets and detect errors and alerts. You can also review all targets in a single view from the HA Console. For more information, see [Chapter 12, "Monitoring for High Availability"](monitor.md) for more information about Enterprise Manager.
- Query the `V$DATABASE_BLOCK_CORRUPTION` view that is automatically updated when block corruption is detected or repaired.
- Configure Data Recovery Advisor to automatically diagnose data failures, determine and present appropriate repair options, and perform repair operations at the user's request. See Section 5.2.2, "Use Data Recovery Adviser to Detect, Analyze and Repair Data Failures" for more information.
	Note:
	Data Recovery Advisor integrates with the Oracle Enterprise Manager Support Workbench (Support Workbench), the Health Monitor, and RMAN.
- Use Data Guard to detect physical corruptions and to detect lost writes.
	Data Guard can detect physical corruptions when the apply process stops due to a corrupted block in the redo steam or when it detects a lost write. Use Enterprise Manager to manage and monitor your Data Guard configuration. By taking advantage of Automatic Block Media Recovery, a corrupt block found on either a primary database or a physical standby database can be fixed automatically when the Active Data Guard option is used. For more information about Automatic Block Media Recovery, see [Section 13.2.6.2, "Use Active Data Guard"](outage.md).
- Use SQL\*Plus to detect data file corruptions and interblock corruptions
	Issue the `ANALYZE TABLE` tablename `VALIDATE STRUCTURE CASCADE` SQL\*Plus statement. After determining the corruptions, the table can be re-created or another action can be taken.

See Also:

- [Section 13.2.6, "Recovering from Data Corruption"](outage.md)
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/manage_ps.htm#SBYDB4782) for more information about Oracle Active Data Guard option and the Automatic Block Repair feature
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmblock.htm#BRADV89781) for information about Performing Block Media Recovery

### 5.1.7 Set DISK\_ASYNCH\_IO Initialization Parameter

Under most circumstances, Oracle Database automatically detects if asynchronous I/O is available and appropriate for a particular platform and enables asynchronous I/O through the [`DISK_ASYNCH_IO`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams079.htm#REFRN10048) initialization parameter. However, for optimal performance, it is always a best practice to ensure that asynchronous I/O is actually being used. Query the [`V$IOSTAT_FILE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2009.htm#REFRN30441) view to determine whether asynchronous I/O is used:

```
SQL> select file_no,filetype_name,asynch_io from v$iostat_file;
```

To explicitly enable asynchronous I/O, set the `DISK_ASYNCH_IO` initialization parameter to `TRUE`:

```
ALTER SYSTEM SET DISK_ASYNCH_IO=TRUE SCOPE=SPFILE SID='*';
```

Note that if you are using Oracle ASM, it performs I/O asynchronously by default.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams079.htm#REFRN10048) for more information about the [`DISK_ASYNCH_IO`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams079.htm#REFRN10048) initialization parameter

### 5.1.8 Set LOG\_BUFFER Initialization Parameter to 8 MB or Higher

Set the `LOG_BUFFER` initialization parameter to minimum of 8 MB.

Set `LOG_BUFFER` to a minimum of 64 MB for databases with flashback enabled and 4GB or higher SGAs.

Set `LOG_BUFFER` to a minimum of 128 MB if you are using Oracle Data Guard with asynchronous redo transport and redo generation rate is higher than 20, because you may need to increase the value of the LOG\_BUFFER parameter to avoid disk I/Os to online redo logs. Refer to [Chapter 9, "Configuring Oracle Data Guard,"](config_dg.md) for details.

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/memory.htm#PFGRF94347) for information about Configuring and Using the Redo Log Buffer
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams133.htm#REFRN10094) for more information about `LOG_BUFFER` and valid values on 32-bit and 64-bit operating systems
- For more information about using a buffer hit rate histogram for determining optimal size for log buffer to support redo transport, see "View `X$LOGBUF_READHIST` and In-Memory Log Buffer Hit Rate Histogram" in My Oracle Support Note 951152.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=951152.1`

### 5.1.9 Use Automatic Shared Memory Management and Avoid Memory Paging

For any systems with 4 GB or more memory, disable Automatic Memory Management by setting `MEMORY_TARGET=0` and enable Automatic Shared Memory Management by setting `SGA_TARGET`.

The sum of SGA and PGA memory allocations on the database server should always be less than your system's physical memory, and conservatively should be less than 75% of total system memory. However, `PGA_AGGREGATE_TARGET` is not a hard limit, and for some Data Warehouse or reporting applications, the PGA memory can grow to be 3 X `PGA_AGGREGATE_TARGET`.

Monitor PGA memory and host-based memory utilization using Oracle Enterprise Manager, or by querying `v$pgastat` and operating systems statistics, to get an accurate understanding of memory utilization.

Avoid memory paging by adjusting the number of databases and applications, or reducing the allocated memory settings.

On Linux Operating systems it is recommended that you configure HugePages so that ASM and database instances can use it for their SGA. HugePages is a feature integrated into the Linux kernel from release 2.6. This feature provides the alternative to the 4K page size providing bigger pages. Using HugePages has the benefit of saving memory resources by decreasing page table overhead while making sure the memory is not paged to disk. This contributes to faster overall memory performance. Next to this overall node stability will benefit from using HugePages.

Ensuring the entire SGA of a database instance is stored in HugePages can be accomplished by setting the `init.ora` parameter `use_large_pages=only`. Setting this parameter will ensure that an instance will start only when it can get all of its memory for SGA from HugePages. For this reason the setting `use_large_pages=only` is recommended for database instances.

For ASM instances leave `use_large_pages=true` (the default value). This setting still ensures that HugePages are used when available, but also ensures that ASM as part of Grid Infrastructure starts when HugePages are not or insufficiently configured.

Use Automatic Shared Memory Management, as HugePages are not compatible with Automatic Memory Management.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/memory.htm#ADMIN11203) for more information
- For information about configuring HugePages, see "Shell Script to Calculate Values Recommended Linux HugePages / HugeTLB Configuration" and "HugePages on Linux: What It Is... and What It Is Not..." in My Oracle Support Notes 401749.1 and 361323.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=401749.1`
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=361323.1`

### 5.1.10 Disable Parallel Recovery for Instance Recovery

When the value of `RECOVERY_ESTIMATED_IOS` in the `V$INSTANCE_RECOVERY` view is small (for example, < 5000), then the overhead of parallel recovery may outweigh any benefit. This typically occurs with a very aggressive setting of `FAST_START_MTTR_TARGET`. In this case, set `RECOVERY_PARALLELISM` to 1 to disable parallel recovery.

## 5.2 Recommendations to Improve Manageability

To improve Oracle Database manageability:

- Use Oracle Clusterware with Oracle RAC or Oracle Restart
- Use Data Recovery Adviser to Detect, Analyze and Repair Data Failures
- Use Automatic Performance Tuning Features
- Use a Server Parameter File
- Use Automatic Undo Management
- Use Locally Managed Tablespaces
- Use Automatic Segment Space Management
- Use Temporary Tablespaces and Specify a Default Temporary Tablespace
- Use Resumable Space Allocation
- Use Database Resource Manager

### 5.2.1 Use Oracle Clusterware with Oracle RAC or Oracle Restart

Configure Oracle Clusterware with Oracle Real Application Clusters (Oracle RAC) or Oracle Restart to automatically restart key application and Oracle services such as the Oracle ASM instance, listeners, application agents, and processes.

Oracle Restart enhances the availability of a single-instance (nonclustered) Oracle database and its components. Oracle Restart is used in single-instance environments only. For Oracle Real Application Clusters (Oracle RAC) environments, the functionality to automatically restart components is provided by Oracle Clusterware.

If you configure Oracle Restart, it automatically restarts the database, the listener, and other Oracle components after a hardware or software failure or whenever the database's host computer restarts. It also ensures that the Oracle components are restarted in the proper order, in accordance with component dependencies.

Oracle Restart runs out of the Oracle Grid Infrastructure home, which you install separately from Oracle Database homes.

See Also:

- [Chapter 6, "Configuring Oracle Database with Oracle Clusterware"](config_cw.md)
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/restart.htm#ADMIN12721) for information about configuring Oracle Restart

### 5.2.2 Use Data Recovery Adviser to Detect, Analyze and Repair Data Failures

Use Data Recovery Advisor to quickly diagnose data failures, determine and present appropriate repair options, and execute repairs at the user's request. In this context, a data failure is a corruption or loss of persistent data on disk. By providing a centralized tool for automated data repair, Data Recovery Advisor improves the manageability and reliability of an Oracle database and thus helps reduce the Mean Time To Recover (MTTR). Data Recovery Advisor can diagnose failures based on symptoms, such as:

- Components that are not accessible because they do not exist, do not have the correct access permissions, are taken offline, and so on
- Physical corruptions such as block checksum failures, invalid block header field values, and so on
- Logical corruptions caused by software bugs
- Incompatibility failures caused by an incorrect version of a component
- I/O failures such as a limit on the number of open files exceeded, channels inaccessible, network or I/O errors, and so on
- Configuration errors such as an incorrect initialization parameter value that prevents the opening of the database

If failures are diagnosed, then they are recorded in the Automatic Diagnostic Repository (ADR). Data Recovery Advisor intelligently determines recovery strategies by:

- Generating repair advice and repairing failures only after failures have been detected by the database and stored in ADR
- Aggregating failures for efficient recovery
- Presenting only feasible recovery options
- Indicating any data loss for each option

Typically, Data Recovery Advisor presents both automated and manual repair options. If appropriate, you can choose to have Data Recovery Advisor automatically perform a repair, verify the repair success, and close the relevant repaired failures.

Note:

In the current release, Data Recovery Advisor only supports single-instance databases. Oracle RAC databases are not supported. See [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmrepai.htm#BRADV89724) for more information about Data Recovery Advisor supported database configurations.

See Also:

- [Section 13.2.6, "Recovering from Data Corruption"](outage.md) for more information about using Data Recovery Advisor
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmrepai.htm#BRADV246) for information about diagnosing and repairing failures with Data Recovery Advisor

### 5.2.3 Use Automatic Performance Tuning Features

Effective data collection and analysis is essential for identifying and correcting performance problems. Oracle provides several tools that gather information regarding database performance.

The Oracle Database automatic performance tuning features include:

- Automatic Workload Repository (AWR)
- Automatic Database Diagnostic Monitor (ADDM)
- SQL Tuning Advisor
- SQL Access Advisor
- Active Session History Reports (ASH)

When using Automatic Workload Repository (AWR), consider the following best practices:

- Create a baseline of performance data to be used for comparison purposes should problems arise. This baseline should be representative of the peak load on the system.
- Set the AWR automatic snapshot interval to 10-20 minutes to capture performance peaks during stress testing or to diagnose performance issues.
- Under usual workloads a 60-minute interval is sufficient.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/autostat.htm#PFGRF94183) for more information about Managing the Automatic Workload Repository

### 5.2.4 Use a Server Parameter File

The server parameter file (SPFILE) enables a single, central parameter file to hold all database initialization parameters associated with all instances of a database. This provides a simple, persistent, and robust environment for managing database parameters. An SPFILE is required when using Oracle Data Guard broker.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/start.htm#ADMIN12826) for information about managing initialization parameters with an SPFILE
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/admin.htm#RACAD020) for information about initialization parameters with Real Application Clusters
- [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/install.htm#DGBKR090) for information about other prerequisites for using the broker

### 5.2.5 Use Automatic Undo Management

With automatic undo management, the Oracle Database server effectively and efficiently manages undo space, leading to lower administrative complexity and cost. When Oracle Database internally manages undo segments, undo block and consistent read contention are eliminated because the size and number of undo segments are automatically adjusted to meet the current workload requirement.

To use automatic undo management, set the following initialization parameters:

- `UNDO_MANAGEMENT`
	Set this parameter to `AUTO`.
- `UNDO_RETENTION`
	Specify the desired time in seconds to retain undo data. Set this parameter to the same value on all instances.
- `UNDO_TABLESPACE`
	Specify a unique undo tablespace for each instance.

Advanced object recovery features, such as Flashback Query, Flashback Version Query, Flashback Transaction Query, and Flashback Table, require automatic undo management. The success of these features depends on the availability of undo information to view data as of a previous point in time.

By default, Oracle Database automatically tunes undo retention by collecting database usage statistics and estimating undo capacity needs. Unless you enable retention guarantee for the undo tablespace (by specifying the `RETENTION GUARANTEE` clause on either the `CREATE DATABASE` or the `CREATE UNDO TABLESPACE` statement), Oracle Database may reduce the undo retention below the specified `UNDO_RETENTION` value.

Note:

By default, ongoing transactions can overwrite undo data even if the `UNDO_RETENTION` parameter setting specifies that the undo data should be maintained. To guarantee that unexpired undo data is not overwritten, you must enable `RETENTION GUARANTEE` for the undo tablespace.

If there is a requirement to use Flashback technology features, the best practice recommendations is to enable `RETENTION GUARANTEE` for the undo tablespace and set a value for `UNDO_RETENTION` based on the following guidelines:

1. Establish how long it would take to detect when erroneous transactions have been carried out. Multiply this value by two.
2. Use the Undo Advisor to compute the minimum undo tablespace size based on setting `UNDO_RETENTION` to the value recommended in step 1.
3. If the undo tablespace has the `AUTOEXTEND` option disabled, allocate enough space as determined in step 2 or reduce the value of the `UNDO_RETENTION` parameter.
4. If the undo tablespace has the `AUTOEXTEND` option enabled, make sure there is sufficient disk space available to extend the data files to the size determined in step 2. Make sure the autoextend `MAXSIZE` value you specified is large enough.

With the `RETENTION GUARANTEE` option, if the tablespace is configured with less space than the transaction throughput requires, then the following sequence of events occurs:

1. If you have an autoextensible file, then the file automatically grows to accommodate the retained undo data.
2. A warning alert reports the disk is at 85% full.
3. A critical alert reports the disk is at 97% full.
4. Transactions receive an out-of-space error.

See Also:

- [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/storage.htm#ADMQS0635) for information about computing the minimum undo tablespace size using the Undo Advisor
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/undo.htm#ADMIN013) for more information about the `UNDO_RETENTION` setting and the size of the undo tablespace

### 5.2.6 Use Locally Managed Tablespaces

Locally managed tablespaces perform better than dictionary-managed tablespaces, are easier to manage, and when combined with uniform extents eliminate extent fragmentation concerns. Locally managed tablespaces use bitmaps stored in the data file headers and, unlike dictionary managed tablespaces, do not contend for centrally managed resources for space allocations and de-allocations.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tspaces.htm#ADMIN011) for more information about locally managed tablespaces

### 5.2.7 Use Automatic Segment Space Management

Automatic segment space management simplifies space administration tasks, thus reducing the chance of human error. An added benefit is the elimination of performance tuning related to space management. It facilitates management of free space within objects such as tables or indexes, improves space utilization, and provides significantly better performance and scalability with simplified administration. The automatic segment space management feature is enabled by default for all tablespaces created using default attributes.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tspaces.htm#ADMIN10065) for more information about automatic segment space management

### 5.2.8 Use Temporary Tablespaces and Specify a Default Temporary Tablespace

Temporary tablespaces improve the concurrency of multiple sort operations, reduce sort operation overhead, and avoid data dictionary space management operations. This is a more efficient way of handling temporary segments, from the perspective of both system resource usage and database performance.

The best practice is to specify a default temporary tablespace for the entire database to ensure that temporary segments are used for the most efficient sort operations, whether individual users have been assigned a temporary tablespace.

| To Specify a Default Temporary Tablespace... | Then... |
| --- | --- |
| When creating the database... | Use the `DEFAULT TEMPORARY TABLESPACE` clause of the `CREATE DATABASE` statement |
| After database creation... | Use the `ALTER DATABASE` statement |

Using the default temporary tablespace ensures that all disk sorting occurs in a temporary tablespace and that other tablespaces are not mistakenly used for sorting.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN002) for more information about managing tablespaces

### 5.2.9 Use Resumable Space Allocation

Resumable space allocation provides a way to suspend and later resume database operations if there are space allocation failures. The affected operation is suspended instead of the database returning an error. No processes must be restarted. When the space problem is resolved, the suspended operation is automatically resumed.

To use resumable space allocation, you can set it at the system level with the `RESUMABLE_TIMEOUT` initialization parameter, or enable it at the session level using clauses of the `ALTER SESSION` statement (for example, issue the `ALTER` `SESSION` `ENABLE` `RESUMABLE` statement). The default for a new session is resumable mode disabled, unless you explicitly set the `RESUMABLE_TIMEOUT` initialization parameter to a nonzero value.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/schema.htm#ADMIN11581) for more information about managing resumable space allocation

### 5.2.10 Use Database Resource Manager

Oracle Database Resource Manager (the Resource Manager) gives database administrators more control over resource management decisions, so that resource allocation can be aligned with the business objectives of an enterprise. The Resource Manager provides the ability to prioritize work within the Oracle Database server. Availability of the database encompasses both its functionality and performance. If the database is available but users are not getting the level of performance they need, then availability and service level objectives are not being met. Application performance, to a large extent, is affected by how resources are distributed among the applications that access the database. The main goal of the Resource Manager is to give the Oracle Database server more control over resource management decisions, thus circumventing problems resulting from inefficient operating system management and operating system resource managers.

When you use the Resource Manager:

- Use Enterprise Manager to manage resource plans.
- When you test with the Resource Manager, ensure there is sufficient load on the system to make CPU resources scarce.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dbrm.htm#ADMIN027) for more information about Oracle Database Resource Manager
- For information about configuring and troubleshooting Database Resource Manager, see "Resource Manager Training (11.2 features included)" in My Oracle Support Note 1119407.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1119407.1`