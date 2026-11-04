---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/oracle-ai-database-configuration-best-practices.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 9 Oracle Database Configuration Best Practices

Adopt the Oracle MAA best practices for configuring all Oracle single-instance databases to reduce or avoid outages, reduce the risk of corruption, and improve recovery performance.

Note that the following Oracle Database best practices are used to configure the Oracle MAA Bronze reference architecture, and they are also the base database base practices for the other MAA reference architectures: Silver (Oracle RAC), Gold (Oracle Data Guard), and Platinum (Oracle GoldenGate).

### Use a Server Parameter File (SPFILE)

The server parameter file (SPFILE) enables a single, central parameter file to hold all database initialization parameters associated with all instances of a database. This provides a simple, persistent, and robust environment for managing database parameters. SPFILE is recommended to be placed in the DATA ASM disk group.

### Enable Archive Log Mode and Forced Logging

Running the database in `ARCHIVELOG` mode and using database `FORCE LOGGING` mode are prerequisites for database recovery operations.

The `ARCHIVELOG` mode enables online database backup and is necessary to recover the database to a point in time later than what has been restored. Features such as Oracle Data Guard and Flashback Database require that the production database run in `ARCHIVELOG` mode.

If you can isolate data that never needs to be recovered within specific tablespaces, then you can use tablespace level `FORCE LOGGING` attributes instead of the database `FORCE LOGGING` mode.

### Configure an Alternate Local Archiving Destination

The local archive destination, usually `LOG_ARCHIVE_DEST_1`, should have an alternate local destination on a different ASM disk group. This configuration prevents database hanging due to lack of archive log space if `DB_RECOVERY_FILE_DEST` fills up or is unavailable for any reason.

Table 9-1 Alternate Local Archiving Configuration Parameters

| Database Parameter | LOG\_ARCHIVE\_DEST\_n parameter settings for local archive destinations |
| --- | --- |
| `LOG_ARCHIVE_DEST_n` | `LOCATION=USE_DB_FILE_RECOVERY_DEST`  `VALID_FOR=(ALL_LOGFILES,ALL_ROLES)`  `MAX_FAILURE=1`  `REOPEN=5`  `DB_UNIQUE_NAME=db_unique_name` of the database  `ALTERNATE=` some other log archive destination. Must be log\_archive\_dest\_\[1-10\] |
| `LOG_ARCHIVE_DEST_y` | `LOCATION=` A disk group other than the disk group used for `DB_RECOVERY_FILE_DEST`. Usually the DATA disk group.  `VALID_FOR=(ALL_LOGFILES,ALL_ROLES)`  `MAX_FAILURE=1`  `REOPEN=5`  `ALTERNATE=` the primary local archive log destination: usually `LOG_ARCHIVE_DEST_1` |
| `DB_RECOVERY_FILE_DEST` | Archive destination, for example, a RECO disk group |
| `LOG_ARCHIVE_DEST_STATE_n` | `ENABLE` |
| `LOG_ARCHIVE_DEST_STATE_y` | `ALTERNATE` |

Sample parameter settings:

- `LOG_ARCHIVE_DEST_1='LOCATION=USE_DB_FILE_RECOVERY_DEST                     VALID_FOR=(ALL_LOGFILES,ALL_ROLES) MAX_FAILURE=1 REOPEN=5                         DB_UNIQUE_NAME=db_unique_name of the database                     ALTERNATE=LOG_ARCHIVE_DEST_10'`
- `LOG_ARCHIVE_DEST_10='LOCATION=+DATA VALID_FOR=(ALL_LOGFILES,ALL_ROLES)                     MAX_FAILURE=1 REOPEN=5 DB_UNIQUE_NAME=db_unique_name of the                         database ALTERNATE=LOG_ARCHIVE_DEST_1'`
- `LOG_ARCHIVE_DEST_STATE_1 =enable`
- `LOG_ARCHIVE_DEST_STATE_10=alternate`
- `DB_RECOVERY_FILE_DEST=typically the RECO disk                     group`

### Use a Fast Recovery Area

The Fast Recovery Area is Oracle-managed disk space that provides a centralized disk location for backup and recovery files.

The Fast Recovery Area is defined by setting the following database initialization parameters:

- `DB_RECOVERY_FILE_DEST` specifies the default location for the fast recovery area. Set this parameter to the RECO disk group.
- `DB_RECOVERY_FILE_DEST_SIZE` specifies (in bytes) the hard limit on the total space to be used by database recovery files created in the recovery area location.
	Set this parameter to a value large enough to store archived logs, flashback logs and any local database backup files locally. Having the files locally can reduce your recovery time after restoring a backup. RMAN will automatically manage these files according to your RMAN backup and data retention policies. Typically customers store 24 hours of data in the destination
	When your system hosts many databases sharing the same `DB_RECOVERY_FILE_DEST_SIZE`, space needs to manage and monitored holistically. Recommended to alert when RECO disk group for example is 90% full.

### Enable Flashback Database

Flashback Database provides an efficient alternative to point-in-time recovery for reversing unwanted database changes.

Flashback Database lets you rewind an entire database backward in time, reversing the effects of database changes within a time window. The effects are similar to database point-in-time recovery. You can flash back a database by running a single RMAN command or a SQL\*Plus statement instead of using a complex procedure.

To enable Flashback Database, configure a fast recovery area and set a flashback retention target using the best practices listed below. This retention target specifies how far back you can rewind a database with Flashback Database.

- Know your application performance baseline before you enable flashback database to help determine the overhead and to assess the application workload implications of enabling flashback database.
- Ensure that the fast recovery area space is sufficient to hold the flashback database flashback logs. A general rule of thumb is that the volume of flashback log generation is approximately the same order of magnitude as redo log generation. For example, if you intend to set `DB_FLASHBACK_RETENTION_TARGET` to 24 hours, and if the database generates 20 GB of redo in a day, then allow 20 GB to 30 GB disk space for the flashback logs.
	- An additional method to determine fast recovery area sizing is to enable flashback database and allow the database to run for a short period of time (2-3 hours). Query `V$FLASHBACK_DATABASE_STAT.ESTIMATED_FLASHBACK_SIZE` to retrieve the estimated amount of space required for the fast recovery area.
		- Note that the `DB_FLASHBACK_RETENTION_TARGET` is a target and there is no guarantee that you can flashback the database that far. In some cases if there is space pressure in the fast recovery area where the flashback logs are stored, then the oldest flashback logs may be deleted. To guarantee a flashback point-in-time you must use guaranteed restore points.
- Ensure that there is sufficient I/O bandwidth to the fast recovery area. Insufficient I/O bandwidth with flashback database on is usually indicated by a high occurrence of the `FLASHBACK BUF FREE BY RVWR` wait event.
- To monitor the progress of a flashback database operation you can query the `V$SESSION_LONGOPS` view. An example query to monitor progress is
	```
	SELECT sofar, totalwork, units FROM v$session_longops WHERE opname = 'Flashback Database';
	```
- For repetitive tests where you must flashback to the same point, use flashback database guaranteed restore points instead of enabling flashback database. This will minimize space usage.
- Flashback PDB can rewind a pluggable database without affecting other PDBs in the CDB. You can also create PDB restore points.

### Set FAST\_START\_MTTR\_TARGET Initialization Parameter

With Fast-Start Fault Recovery, the `FAST_START_MTTR_TARGET` initialization parameter simplifies the configuration of recovery time from instance or system failure.

The `FAST_START_MTTR_TARGET` parameter specifies a target for the expected recovery time objective (RTO), which is the time, in seconds, that it should take to start the instance and perform cache recovery. When you set this parameter, the database manages incremental checkpoint writes in an attempt to meet the target. If you have chosen a practical value for this parameter, then you can expect your database to recover, on average, in approximately the number of seconds you have chosen.

Initially, set the `FAST_START_MTTR_TARGET` initialization parameter to 300 (seconds), or to the value required for your expected recovery time objective (RTO). As you set or lower this value, database writer (DBWR) will become more active to meet your recovery targets.

Make sure that you have sufficient IO bandwidth to handle potential higher load. See the Database Performance Tuning Guide for information about monitoring and tuning `FAST_START_MTTR_TARGET`.

Outage testing for cases such as node or instance failures during peak loads is recommended.

### Protect Against Data Corruption

Oracle Database corruption prevention, detection, and repair capabilities are built on internal knowledge of the data and transactions it protects, and on the intelligent integration of its comprehensive high availability solutions.

A data block is corrupted when it is not in a recognized Oracle Database format, or its contents are not internally consistent. Data block corruption can damage internal Oracle control information or application and user data, leading to crippling loss of critical data and services.

When Oracle Database detects corruption, it offers block media recovery and data file media recovery to recover the data. You can undo database-wide logical corruptions caused by human or application errors with Oracle Flashback Technologies. Tools are also available for proactive validation of logical data structures. For example, the SQL\*Plus `ANALYZE TABLE` statement detects inter-block corruptions.

The following are best practices for protecting your database against corruption.

- Use Oracle Automatic Storage Management (Oracle ASM) to provide disk mirroring to protect against disk failures.
- Use the `HIGH` redundancy disk type for optimal corruption repair with Oracle ASM.
	Using Oracle ASM redundancy for disk groups provides mirrored extents that can be used by the database if an I/O error or corruption is encountered. For continued protection, Oracle ASM redundancy lets you move an extent to a different area on a disk if an I/O error occurs. The Oracle ASM redundancy mechanism is useful if you have bad sectors returning media errors.
- Enable Flashback technologies for fast point-in-time recovery from logical corruptions that are most often caused by human error, and for fast reinstatement of a primary database following failover.
- Implement a backup and recovery strategy with Recovery Manager (RMAN) and periodically use the RMAN `BACKUP VALIDATE CHECK LOGICAL` scan to detect corruptions.
	Use RMAN and Oracle Secure Backup for additional block checks during backup and restore operations. Use Zero Data Loss Recovery Appliance for backup and recovery validation including corruption checks and repairs, central backup validation, reduced production database impact, and Enterprise Cloud backup and recovery solutions.
- Set database initialization parameter `DB_BLOCK_CHECKSUM=TYPICAL` or `FULL`.
- Evaluate setting `DB_BLOCK_CHECKING=MEDIUM` or `FULL`, but only after a full performance evaluation with the application.

### Set the LOG\_BUFFER Initialization Parameter to 128MB or Higher

Set the `LOG_BUFFER` initialization parameter to a minimum of 128 MB for databases with flashback enabled.

### Set USE\_LARGE\_PAGES=ONLY

On Linux, the database’s SGA should leverage large pages for consistent performance and stability.

There are two ways to ensure this happens with the `USE_LARGE_PAGES` parameter:

- `USE_LARGE_PAGES=ONLY` - Hugepages must be preallocated before instance startup.
- `USE_LARGE_PAGES=AUTO_ONLY` - Hugepages are dynamically acquired at instance startup time, but this dynamic acquisition can fail if memory is fragmented or if another instance is starting up and dynamically acquiring hugepages at the same time.

The MAA best practice is `USE_LARGE_PAGES=ONLY`. This recommendation is applicable for Cloud and non-Cloud environments, and all Cloud and Exadata automation tools ensure this configuration is in place.

Note:

Oracle RDBMS 19c default for `USE_LARGE_PAGES` on Exadata is `AUTO_ONLY`, but this value will be deprecated in the future.

### Use Bigfile Tablespace

As databases grow larger more data files are added to smallfile tablespaces, which requires additional administration, monitoring, and maintenance, while negatively impacting database open time and role transition time in Oracle Data Guard environments.

Bigfile tablespaces allow a single large data file per tablespace, up to 32TB for 8k blocksize and 128TB for 32k blocksize. The single data file reduces the number of files in the database thus improving database checkpoint, database open, and role transition time, while improving administration costs.

Recommendations include:

- For new database design and deployment, use bigfile tablespaces and partitioning to minimize the number of data files. Partitioning of large tables prevents having an enormous bigfile. A reasonable bigfile should still be 16TB or less.
	- For very large tables that have different retention policies, or have different access requirements, use Oracle Partitioning as part of your database and object design. Oracle Partitioning can also work around any potential bigfile size limitation.
		- For very large tablespaces, use bigfile tablespaces instead of many smallfile data files. Bigfile tablespaces are only supported for locally managed tablespaces with automatic segment space management.
		- There are no negative trade-offs for using bigfile tablespaces, other than understanding the maximum limits for your `DB_BLOCK_SIZE`. To continue to ensure good database backup and restore performance, you should also use the `RMAN SECTION SIZE` parameter to parallelize backup and restore operations when there are bigfile tablespaces.
- For existing databases with a lot of data files, focus on tablespaces that have the most data files and evaluate if you can use the `ALTER                             TABLE MOVE` or online redefinition to migrate tables or partitions to bigfile tablespaces.

The following tables show a recent Data Guard performance test which demonstrates that reducing the number of data files in the database from 9000 data files to ~100 data files improved failover times by 10x and switchover times by 4 times.

| Unplanned Outage/DR (Failover) | Initial Configuration | Tuned MAA Configuration |
| --- | --- | --- |
| Close to Mount (C2M) | 21 secs | 1 sec |
| Terminal Recovery (TR) | 154 secs | 2 secs |
| Convert to Primary (C2P) | 114 secs | 5 secs |
| Open new Primary (OnP) | 98 secs | 28 secs |
| Open PDB and Start Service (OPDB) | 146 secs | 16 secs |
| Total App Downtime | 533 secs or 8min 53 secs | 52 secs (90% drop) |

| Planned DR Switch (Switchover) | Initial Configuration | Tuned MAA Configuration |
| --- | --- | --- |
| Convert Primary to Standby | 26 secs | 21 sec |
| Convert Standby to Primary (C2P) | 47 secs | 7 secs |
| Open new Primary (OnP) | 152 secs | 14 secs |
| Open PDB and Start Service (OPDB) | 130 secs | 39 secs |
| Total App Downtime | 355 secs or 5 minutes 55 secs | 81 secs (78% drop) |

For existing databases with a lot of data files, the following table compares the use of `ALTER TABLE MOVE` or `DBMS_REDEFINITION` to migrate tables or partitions to bigfile tablespaces.

| Areas of Interest or Use Cases | DBMS\_REDEFINITION | ALTER TABLE MOVE ONLINE |
| --- | --- | --- |
| Application Impact | - No DDL changes allowed during move - Application blackout of seconds during activation | - No DDL changes allowed during move - Application blackout during final switch unknown |
| Application Functionality Supported | - DML supported - PDML supported - No DDL changes allowed during move | - DML supported - PDML not supported - No DDL changes allowed during move |
| Impact of indexes | - Available during move - Indexes maintained | - Available during move - Indexes maintained after move (with `UPDATE                                             INDEXES` clause) - Indexes moved separately (`REBUILD                                         ONLINE`) |
| Space Requirements | Double space required (tables+indexes) | Double space required (tables+indexes) |
| Table Partition Functionality | Move entire partitioned table with one execution | Move partition by partition in order to maintain all indexes |
| Statistics Management | New statistics can be created before activation | New statistics created after activation |
| Monitoring Progress | You can query the `V$ONLINE_REDEF` view to monitor the progress of an online table redefinition operation. | Query `V$SESSION_LONGOPS?` |
| Resume on failure | Restart-able | Unknown |
| Rollback | Yes | N/A |
| Restrictions | - Tables with `LONG` columns can be redefined online, but those columns must be converted to `CLOBS`. Also, `LONG                                                 RAW` columns must be converted to `BLOBS`. Tables with `LOB` columns are acceptable. - Index-organized table can be moved - Domain indexes can be moved - Parallel DML and direct path `INSERT` operations are allowed  Many 'corner case' restrictions with `DBMS_REDEFINITION`. See [Restrictions for Online Redefinition of Tables](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=ADMIN-GUID-CB5589F0-B328-4620-8809-C53696972B4C) in Oracle Database Administrator’s Guide | - Cannot move a table with a `LONG` or `RAW` column - Cannot move partitioned index-organized table. - Cannot move if a domain index is defined on the table like spatial, XML, or a Text index. - Parallel DML and direct path `INSERT` operations are not possible during a table move. - Cannot move index-organized tables that contain any `LOB`, `VARRAY`, Oracle-supplied type, or user-defined object type columns. |
| Documentation and References | See [DBMS\_REDEFINITION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=ARPLS-GUID-2BA796C4-8B4D-49B4-8A35-4C6F789CD374) in Oracle Database PL/SQL Packages and Types Reference | See [ALTER TABLE](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=SQLRF-GUID-552E7373-BF93-477D-9DA3-B2C9386F2877) in Oracle Database SQL Language Reference |

### Use Automatic Shared Memory Management and Avoid Memory Paging

Enable Automatic Shared Memory Management by setting the `SGA_TARGET` parameter, and set the `USE_LARGE_PAGES` database initialization parameter to `AUTO_ONLY` or `ONLY` and the `USE_LARGE_PAGES` ASM initialization parameter to `TRUE`.

Use the following guidelines in addition to setting `SGA_TARGET` to enable Automatic Shared Memory Management.

- The sum of SGA and PGA memory allocations on the database server should always be less than your system's physical memory while still accommodating memory required for processes, PGA, and other applications running on the same database server.
- To get an accurate understanding of memory use, monitor PGA memory and host-based memory use by querying `V$PGASTAT` for operating systems statistics.
- Avoid memory paging by adjusting the number of databases and applications, or reducing the allocated memory settings.
	Set `PGA_AGGREGATE_LIMIT` to specify a hard limit on PGA memory usage. If the `PGA_AGGREGATE_LIMIT` value is exceeded, Oracle Database first terminates session calls that are consuming the most untunable PGA memory. Then, if the total PGA memory usage is still over the limit, the sessions that are using the most untunable memory will be terminated.

Set the database initialization parameter `USE_LARGE_PAGES=AUTO_ONLY` or `ONLY`, and set the ASM initialization parameter `USE_LARGE_PAGES=TRUE`.

- Make sure that the entire SGA of a database instance is stored in HugePages by setting the `init.ora` parameter `USE_LARGE_PAGES=ONLY`, or set to `AUTO_ONLY` on Exadata systems.
	Setting `USE_LARGE_PAGES=ONLY` is recommended for database instances, because this parameter ensures that an instance will only start when it can get all of its memory for SGA from HugePages.
- For ASM instances leave the parameter `USE_LARGE_PAGES=ONLY` (the default value). This setting still ensures that HugePages are used when available, but also ensures that ASM as part of Grid Infrastructure starts when HugePages are not configured, or insufficiently configured.
- Use Automatic Shared Memory Management, because HugePages are not compatible with Automatic Memory Management.

### Use Oracle Clusterware

Oracle Clusterware lets servers communicate with each other, so that they appear to function as a collective unit. Oracle Clusterware has high availability options for all Oracle databases including for single instance Oracle databases. Oracle Clusterware is one of minimum requirements in making applications highly available.

Oracle Clusterware provides the infrastructure necessary to run Oracle Real Application Clusters (Oracle RAC), Oracle RAC One Node, and Oracle Restart. Oracle Grid Infrastructure is the software that provides the infrastructure for an enterprise grid architecture. In a cluster, this software includes Oracle Clusterware and Oracle ASM.

For a standalone server, the Grid Infrastructure includes Oracle Restart and Oracle ASM. Oracle Restart provides managed startup and restart of a single-instance (non-clustered) Oracle database, Oracle ASM instance, service, listener, and any other process running on the server. If an interruption of a service occurs after a hardware or software failure, Oracle Restart automatically restarts the component.

Oracle Clusterware manages resources and resource groups to increase their availability, based on how you configure them. You can configure your resources and resource groups so that Oracle Clusterware:

- Starts resources and resource groups during cluster or server start
- Restarts resources and resource groups when failures occur
- Relocates resources and resource groups to other servers, if the servers are available

For more information, see Oracle Clusterware Administration and Deployment Guide topics, [High Availability Options for Oracle Database](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=CWADD-GUID-C54E2511-24E2-452B-B4C7-0D5A93A751A9) and [Making Applications Highly Available Using Oracle Clusterware](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=CWADD-GUID-13400D83-3FF4-482E-B7A7-41C864A491DC).