---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/oracle-flashback-best-practices.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 10 Oracle Flashback Best Practices

Oracle Database Flashback Technologies is a unique and rich set of data recovery solutions that let the database reverse human errors by selectively and efficiently undoing the effects of a mistake.

Before Flashback was introduced to Oracle Database, it might have taken minutes to damage a database but hours to recover it. With Flashback, correcting an error takes about as long as it took to make it. In addition, the time required to recover from this error is not dependent on the database size, which is a capability unique to Oracle Database.

Flashback supports database recovery at all levels, including the row, transaction, table, and the entire database. Flashback provides an ever-growing set of features to view and rewind data back and forth in time, and address several critical high availability and disaster recovery use cases. The list of features and use cases, as well as some key examples, can be found in [Oracle Flashback Technology](ha-features.md).

The Flashback features give you the capability to query historical data, perform change analysis, and perform the self-service repair to recover from logical corruptions while the database is online. With Oracle Flashback Technology, you can indeed undo the past.

### Oracle Flashback Performance Observations

After adopting the configuration and operational best practices and applying recommended patches, Oracle has observed the following performance observations when Flashback Database is enabled on the primary or standby databases.

- Flashing back a database or a PDB to the previous hour usually takes seconds and minutes, even with a very high workload. It finishes in a fraction of the time it takes to apply a given amount of redo. Here are some observations:
	- Flashing back a large batch workload consisting of 400 GB of changes completed in less than 5 minutes.
		- Flashing back of a heavy OLTP of 8GB of changes completed in less than 2 minutes.
		- Due to many variables, there is no rule-of-thumb or calculation to estimate the time to complete a flashback. The tests which produced these observations were done on Exadata to remove system bottlenecks such as storage I/O bandwidth.
- The impact on OLTP workload on the primary database is usually less than 5 percent.
- The impact of a large insert (batch inserts, for example) or direct load operations is usually less than 5 percent if Flashback block new optimization is in effect; otherwise, the impact can vary dramatically (2-40% impact), so testing is required.
	Refer to the Flashback use cases that mention block new optimization descriptions and exceptions in Oracle Flashback Performance Tuning for Specific Application Use Cases.
- Enabling Flashback database can reduce peak redo apply performance rates on a physical standby database if the standby system cannot handle the additional I/O throughput requirements in the Fast Recovery Area. However, even with Flashback database enabled on the standby, the achievable redo apply rates with Flashback enabled are still very high and can outperform application redo generation rates.

The following lists describe the critical flashback milestones and key performance improvements across different Oracle Database software releases:

Oracle Database 12c Release 2 (12.2)

- Flashback Pluggable Database enables the flashback of individual PDBs without affecting other PDBs.
- PDB Restore Points enable an ease of use method to set an alias to an SCN. This alias can then be used for flashback PDB or Point-In-Time Recovery.

Oracle Database 19c

- Creating a Restore Point on a primary database automatically propagates to a standby database, and creates a corresponding Restore Point on the standby database.
- When Flashback Database is enabled on both the primary and standby databases in an Oracle Data Guard configuration, flashing back the primary database causes the standby database to automatically flash back as well.

Oracle Database 21c

- Migrate Flashback Data Archive-enabled tables between different database releases
- Flashback Database support for data file resizing operations
- PDBs can be recovered to an orphan PDB incarnation within the same CDB incarnation or an ancestor incarnation

### Oracle Flashback Configuration Best Practices

The following are Oracle MAA best practices for configuring Flashback technologies in Oracle Database.

Setting DB\_FLASHBACK\_RETENTION\_TARGET

Set the `DB_FLASHBACK_RETENTION_TARGET` initialization parameter to the largest value prescribed by any of the following conditions that apply:

- To leverage Flashback database to reinstate your failed primary database after Oracle Data Guard failover, set `DB_FLASHBACK_RETENTION_TARGET` to a minimum of 60 (minutes) to enable reinstatement of a failed primary. When enabling Flashback database, a couple of hours are required to generate sufficient flashback data into the flashback logs before reinstatement is possible. You can query `V$FLASHBACK_DATABASE_LOG` to find the oldest flashback time.
- Consider cases where there are multiple outages (for example, a network outage, followed later by a primary database outage) that may result in a transport lag between the primary and standby databases at failover time. For such cases, set `DB_FLASHBACK_RETENTION_TARGET` to a value equal to the sum of 60 (mins) plus the maximum transport lag that you wish to accommodate. This ensures that the failed primary database can be flashed back to an SCN that precedes the SCN at which the standby became primary. This is a requirement for primary reinstatement.
- If you are using Flashback Database for fast point-in-time recovery from user error or logical corruptions, set `DB_FLASHBACK_RETENTION_TARGET` to a value equal to the farthest time in the past that you wish to be able to recover from.
- In most cases, `DB_FLASHBACK_RETENTION_TARGET` should be set to the same value on the primary and standby.

Sizing the Fast Recovery Area

Flashback Database uses its own logging mechanism, creating flashback logs and storing them in the Fast Recovery Area (FRA). Ensure that the FRA has allocated sufficient space to accommodate the flashback logs for the target retention size and for peak batch rates. Sizing the FRA is described in detail in the Oracle Backup and Recovery documentation, but generally the volume of flashback log generation is similar in magnitude to redo log generation. Use the following conservative formula and approach:

Target FRA = Current FRA + `DB_FLASHBACK_RETENTION_TARGET` x 60 x Peak Redo Rate (MB/sec)

Example:
- Current FRA or `DB_RECOVERY_FILE_DEST_SIZE` =1000GB
- Target `DB_FLASHBACK_RETENTION_TARGET` =360 (360 minutes)
- From AWR:
	- The peak redo rate for OLTP workload is 3 MB/sec for the database
		- The peak redo rate for the batch workload is 30 MB/sec for the database, and the longest duration is 4 hours
		- The worst-case redo generation size for a 6 hour window is ( 240 minutes x 30 MB/sec x 60 secs/min) + (120 minutes x 3 MB/sec x 60 secs/min ) = 453,600 MB, or approximately 443 GB
- Proposed FRA or `DB_RECOVERY_FILE_DEST_SIZE` = 443 GB +1000 GB = 1443 GB

An additional method to determine FRA sizing is to enable Flashback Database and allow the database applications to run for a short period (2-3 hours), and then query `V$FLASHBACK_DATABASE_STAT.ESTIMATED_FLASHBACK_SIZE`.

Note that the `DB_FLASHBACK_RETENTION_TARGET` is a target, and there is no guarantee that you can flash back the database that far. The oldest flashback logs may be deleted if there is space pressure in the FRA where the flashback logs are stored. See [Maintaining the Fast Recovery Area](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=BRADV-GUID-A60E5493-8988-40E5-9E70-36AE6A0DFD69) in Oracle Database Backup and Recovery User’s Guide for a detailed explanation of the FRA deletion rules. You must use guaranteed restore points (GRP) to guarantee a flashback point-in-time. The required flashback logs will never be recycled or purged with GRP until GRP is dropped. The database can stop responding if there is a GRP but there is insufficient space, so you must allocate more space in the FRA depending on the intended duration of the GRP.

Configuring sufficient I/O bandwidth for Fast Recovery Area

Insufficient I/O bandwidth with Flashback Database on is usually indicated by a high occurrence of the "FLASHBACK BUF FREE BY RVWR" wait event in an Automatic Workload Repository (AWR) report for OLTP workloads and "FLASHBACK LOG FILE WRITE" latency > 30 ms for large insert operations.

In general, flashback I/Os are 1 MB in size. The overall write throughput would be similar to the redo generation rate if database force logging were enabled, or identical to your load rate for direct load operations. For simplicity, configure one large shared storage GRID and configure DATA on the outer portion of the disks or LUNS and RECO (FRA) on the inner amount of the disks or LUNS. This is done automatically for Exadata systems.

Setting LOG\_BUFFER

To give Flashback Database more buffer space in memory, set the initialization parameter `LOG_BUFFER=256MB` or higher, depending on operating system limits.

### Oracle Flashback Operational Best Practices

The following are Oracle MAA recommended operational best practices for Flashback Database.

- Gather database statistics using Automatic Workload Repository (AWR) or Oracle Enterprise Manager before and after enabling Flashback Database, so you can measure the impact of enabling Flashback Database.
- Using Oracle Enterprise Manager, set the Enterprise Manager monitoring metric,"Recovery Area Free Space (%)" for proactive alerts of space issues with the fast recovery area (FRA).
- To monitor the progress of a Flashback Database operation, you can query the `V$SESSION_LONGOPS` view. For example,
	`select * from v$session_longops where opname like                         'Flashback%';`
	If more detail is required on the Flashback Database operation, generate a detailed trace of the Flashback Database operation in the DIAGNOSTIC\_DEST trace directory for the database by setting database parameter `_FLASHBACK_VERBOSE_INFO=TRUE`.
- When using Flashback Database to perform repeated tests on a test database, it is recommended that you use Guaranteed Restore Points (GRP) only, without explicitly turning on Flashback Database. To minimize space usage and flashback performance overhead, follow this recommended approach:
	```
	Create Guaranteed Restore Point (GRP)
	Execute test
	loop
	     Flashback database to GRP
	     Open resetlogs
	     Create new GRP
	     Drop old GRP
	     Execute
	testEnd loop
	```
- Follow the Oracle Data Guard redo apply best practices described in [Redo Apply Troubleshooting and Tuning](redo-apply-troubleshooting-and-tuning.md).

### Oracle Flashback Performance Tuning for Specific Application Use Cases

Performance Tuning for OLTP Workloads

The "flashback buf free by RVWR" wait event only occurs when Flashback Database is enabled. A session waits for the recovery writer (RVWR) to write flashback data to the flashback logs on disk because the buffers are full. The session may need to wait until RVWR can free up the buffers.

Suppose this event becomes one of the top wait events for the database. In that case, it is typically because the file system or storage system for the Fast Recovery Area (FRA) has insufficient I/O bandwidth to accommodate additional I/O from the Flashback writes. Refer to the Flashback Database section in the Oracle Database Backup and Recovery User’s Guide for tuning considerations and evaluate the corresponding I/O and storage statistics.

Table 10-1 Top 5 Timed Foreground Events

| Event | Waits | Times | Average wait (ms) | % database time | Wait class |
| --- | --- | --- | --- | --- | --- |
| write complete waits | 1,842 | 23,938 | 12995 | 33.68 | Configuration |
| flashback buf free by RVWR | 53,916 | 20,350 | 377 | 28.63 | Configuration |
| cell single block physical read | 3,029,626 | 16,348 | 5 | 23.00 | User I/O |
| buffer busy waits | 6,248 | 5,513 | 882 | 7.76 | Concurrency |
| DB CPU |  | 1,757 |  | 2.47 |  |

Performance Tuning for Direct Path Operations

Look at the "flashback log write bytes" and "physical write bytes" system statistics found in `v$sysstat`, in your AWR reports, or Oracle Enterprise Manager.

- "flashback log write bytes" = The total size in bytes of Flashback Database data written by RVWR to Flashback Database logs
- "physical write bytes" = The total size in bytes of all disk writes from the database application activity (and not other kinds of instance activity).

If (flashback log write bytes) / (physical write bytes) < 5%, then Flashback is not impacting your performance.

Otherwise, evaluate any operational changes or bug fixes that will allow you to use the Flashback block new optimization feature (refer to performance observation section above). Furthermore, ignore the "flashback log file sync" wait event, even if it's one of the top wait events.

Example of block new optimization in effect

In this example:

- flashback log write bytes = 1,223,442,432
- physical write bytes = 184,412,282,880

The result of (flashback log write bytes) / (physical write bytes) = 0.0066 < 5%, implies that there’s only a fraction of flashback data compared to the physical writes within this interval where there are direct load operations. Even in this case, the "flashback log file sync" wait event was the 2nd highest wait event in the database, as shown in the following table.

Table 10-2 Top 5 Timed Foreground Events

| Event | Waits | Times | Average wait (ms) | % database time | Wait class |
| --- | --- | --- | --- | --- | --- |
| direct path write | 136,553 | 7,875 | 58 | 39.12 | User I/O |
| flashback log file sync | 91,566 | 5,887 | 64 | 29.25 | User I/O |
| DB CPU |  | 3,092 |  | 15.36 |  |
| log buffer space | 20,545 | 1,737 | 85 | 8.63 | Configuration |
| gc buffer busy release | 1,277 | 487 | 382 | 2.42 | Cluster |

Example of block new optimization not in effect

In this example:

- flashback log write bytes= 184,438,194,176
- physical write bytes =184,405,925,888

The result of (flashback log write bytes) / (physical write bytes) = 100% > 5%, implies that in this case all direct writes also result in flashback log writes. Listed here are the top wait events for this case.

Table 10-3 Top 5 Timed Foreground Events

| Event | Waits | Times | Average wait (ms) | % database time | Wait class |
| --- | --- | --- | --- | --- | --- |
| flashback log file sync | 170,088 | 22,385 | 132 | 52.04 | User I/O |
| direct path write | 278,185 | 8,284 | 30 | 19.26 | User I/O |
| flashback buf free by RVWR | 38,396 | 5,048 | 131 | 11.74 | Configuration |
| direct path read | 220,618 | 4,242 | 19 | 9.86 | User I/O |
| DB CPU |  | 2,788 |  | 6.48 |  |

Performance Tuning for Conventional Load Operations

The following examples illustrate two conventional loads, one that uses block new optimization and one that does not.

Example of block new optimization not in effect

The example below does not use the block new optimization because of a truncate just before loading the table. The wait events for a conventional load without block new optimization show a fairly large amount of total wait time spent in "flashback log file sync". This is because of time needed to read them before the image of the block into the buffer cache and well as writing the block to the flashback log.

Table 10-4 Top 5 Timed Foreground Events

| Event | Waits | Times | Average wait (ms) | % database time | Wait class |
| --- | --- | --- | --- | --- | --- |
| flashback log file sync | 235,187 | 13,728 | 58 | 30.82 | User I/O |
| direct path write | 558,037 | 10,818 | 19 | 24.29 | User I/O |
| direct path read | 459,076 | 8,419 | 18 | 18.90 | User I/O |
| DB CPU |  | 6,171 |  | 13.85 |  |
| flashback buf free by RVWR | 79,463 | 4,268 | 54 | 9.58 | Configuration |

Looking at the instance statistics below you can see very little increase in the statistics that track block new optimizations.

| Statistic | Total | Per second | Per transaction |
| --- | --- | --- | --- |
| flashback cache read optimizations for block new | 62 | 0.06 | 1.13 |
| flashback direct read optimizations for block new | 8 | 0.01 | 0.15 |
| flashback log write bytes | 177,533,280,256 | 177,245,433.67 | 3,227,877,822.84 |
| flashback log writes | 18,917 | 18.89 | 343.95 |

If the "flashback cache read optimizations for block new" is much smaller than "flashback log writes" then the block new optimization does not have an effect.

The best tuning recommendation for the above load operation would be to increase I/O bandwidth or, perhaps better, change the manner in which the load is performed so that it can take advantage of block new optimizations. You can also wait until you are outside the flashback retention target, or remove the object from recycle bin if it was dropped.

Example of block new optimization not effect

The wait events for a conventional load with block new optimization show a relatively small amount of total time spent in "flashback log file sync" compared to other database waits, as shown here.

Table 10-5 Top 5 Timed Foreground Events

| Event | Waits | Times | Average wait (ms) | % database time | Wait class |
| --- | --- | --- | --- | --- | --- |
| direct path write | 284,115 | 8,977 | 32 | 34.20 | User I/O |
| DB CPU |  | 6,284 |  | 23.94 |  |
| log buffer space | 128,879 | 5,081 | 39 | 19.36 | Configuration |
| flashback log file sync | 139,546 | 3,178 | 23 | 12.11 | User I/O |
| latch: redo allocation | 95,887 | 1,511 | 16 | 5.76 | Other |

Looking at the instance statistics you can see that the statistics that track block new operations have significantly increased during the load.

| Statistic | Total | Per second | Per transaction |
| --- | --- | --- | --- |
| flashback cache read optimizations for block new | 329 | 0.53 | 9.68 |
| flashback direct read optimizations for block new | 698,410 | 1,116.43 | 20,541.47 |
| flashback log write bytes | 1,197,514,752 | 1,914,271.66 | 35,221,022.12 |
| flashback log writes | 18,951 | 30.29 | 557.38 |