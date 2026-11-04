---
title: Configuring Oracle Data Guard
book: High Availability Best Practices
doc_id: E10803-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10803/config_dg.htm
tags:
  - oracle
  - 11g
  - high-availability-best-practices
---

## 9 Configuring Oracle Data Guard

The proper configuration of Oracle Data Guard is essential to ensuring that all standby databases work properly and perform their roles within the necessary service levels after switchovers and failovers.

The best practices for Oracle Data Guard build on the best practices described in [Chapter 5, "Configuring Oracle Database."](config_db.md)

This chapter contains the following topics:

## 9.1 Oracle Data Guard Configuration Best Practices

Data Guard is the Oracle optimized solution for Data availability and protection. It excels at simple, fast, and reliable one-way replication of a complete Oracle Database to provide High Availability and Disaster Recovery. Data Guard offers various deployment options that address unplanned outages, pre-production testing, and planned maintenance. Active Data Guard, an extension of basic Data Guard capabilities, further enables production offload of read-only workload to a synchronized physical standby database, automatic repair of corrupt blocks, and offload of fast incremental backups.

The focus of Data Guard is High Availability and Data Recovery. Data Guard design principles are simplicity, high performance, and application transparency.

Data Guard is not intended to be a full-featured replication solution. Oracle GoldenGate is the solution recommended for advanced replication requirements, such as multi-master replication, granular replication of a subset of a database, many to one replication topologies, and data integration. Oracle GoldenGate also provides additional options for reducing downtime for planned maintenance and for heterogeneous platform migrations.

Depending upon your requirements, the most efficient solution to use may be using Data Guard alone, using Data Guard with Oracle GoldenGate in a complementary manner, or just using Oracle GoldenGate.

For more information about Data Guard and Oracle GoldenGate see the Product Technical Brief on Oracle Active Data Guard and Oracle GoldenGate at

`http://www.oracle.com/technetwork/middleware/goldengate/overview/index.html`

Table 9-1 provides a summary of the Data Guard deployment options that are appropriate, depending on your requirements. Two or more options may be used in combination to address multiple requirements. This chapter also presents the Best practices for implementing each option.

Table 9-1 Requirements and Data Guard Deployment Options

| Requirement | Data Guard Deployment Options |
| --- | --- |
| Zero data loss protection and availability for Oracle Database | Data Guard Maximum Protection or Maximum Availability (SYNC transport) and Redo Apply (physical standby) |
| Near-zero data loss (single-digit seconds) and availability for Oracle Database | Data Guard Maximum Performance (ASYNC transport) and Redo Apply |
| Multi-site protection, including topology with local zero data loss standby for HA and remote asynchronous standby for geographic disaster recovery for Oracle Database | Multi-standby Data Guard configuration and Redo Apply |
| Fastest possible database failover | Data Guard Fast-Start Failover with Oracle Data Guard broker for automatic failure detection and database failover. Automatic failover of accompanying client applications to the new production database is implemented using Oracle Fast Application Notification (FAN) and Oracle Client Failover Best Practices.  For more information, see the MAA white paper "Client Failover Best Practices for Data Guard 11g Release 2" from the MAA Best Practices area for Oracle Database at  `http://www.oracle.com/goto/maa` |
| Offload read-only queries and fast incremental backups to a synchronized standby database. Use the standby database to automatically repair corrupt blocks, transparent to the application and user | Active Data Guard. Active Data Guard can be purchased in either of the following ways: (1) standalone as an option license for Oracle Database Enterprise Edition, or (2) included with an Oracle GoldenGate license. |
| Pre-production testing | Snapshot Standby. A snapshot standby is a physical standby database that is temporarily open read/write for test and other read/write activity independent of primary database transactions. A snapshot standby is easily converted back into a synchronized standby database when testing is complete. Snapshot Standby is an included feature of Data Guard Redo Apply and is an ideal complement for Oracle Real Application Testing. |
| Planned maintenance: certain platform migrations such as Windows to Linux, data center moves, patching and upgrading system software or Oracle Database | Data Guard switchover, planned role transition, using Redo Apply. Redo Apply and Standby-First Patch Apply for qualifying patches from 11.2.0.1 onward. SQL Apply and Data Guard Database Rolling Upgrades (10.1 onward). Data Guard Transient Logical Standby (Upgrades Made Easy) from 11.1.0.7 onward.  For more information, see the MAA white paper, "Database Rolling Upgrades Made Easy by Using a Data Guard Physical Standby Database", from the MAA Best Practices area for Oracle Database at  `http://www.oracle.com/goto/maa` |
| Data Protection for data residing outside of the Oracle Database | When practical, move operating system file system data into Oracle Database using Oracle Database File System (DBFS). Data Guard protects DBFS data in the same manner as any other Oracle data.  Data that must remain in operating system files can be protected using Oracle ASM Cluster File System (Oracle ACFS) or storage mirroring, and Data Guard. |

Note:

Standby-First Patch allows you to apply a patch initially to a physical standby database while the primary database remains at the previous software release (this applies for certain types of patches and does not apply for Oracle patch sets and major release upgrades; use the Data Guard transient logical standby method for patch sets and major releases). Once you are satisfied with the change, then you perform a switchover to the standby database. The fallback is to switchback if required. For more information, see "Oracle Patch Assurance - Data Guard Standby-First Patch Apply" in My Oracle Support Note 1265700.1 at

`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1265700.1`

See Also:

- [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/unplanned.htm#HAOVW120) for a description of the high availability solutions and benefits provided by Oracle Data Guard and standby databases
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/concepts.htm#SBYDB00010) provides complete information about Oracle Data Guard
- [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/dgmgrl.htm#DGBKR585) for information about the DGMGRL command-line interface

## 9.2 Determine Protection Mode and Data Guard Transport

Oracle Data Guard Zero Data Loss protection provides both a guarantee of that data is protected and the simplest recovery. For these reasons a Zero Data Loss protection mode, either Oracle Data Guard Maximum Protection or Maximum Availability, is recommended. While both modes use Oracle Data Guard synchronous redo transport by default, there are differences in the rule-sets used to govern behavior at failover time that must be considered, as described below. Oracle Data Guard synchronous redo transport, however, can impact primary database performance if round-trip network latency between primary and standby databases is too great (latency is a function of distance and how 'clean' the network is). If this is the case (testing is easy to do, a DBA may change protection modes and transport methods dynamically), then use Oracle Data Guard Maximum Performance. Maximum Performance uses Oracle Data Guard asynchronous transport services and does not have any impact on primary database performance regardless of network latency. In an environment with sufficient bandwidth to accommodate redo volume, data loss potential is measured in single-digit seconds when using Maximum Performance.

To determine the appropriate data protection mode for your application, consult Oracle Data Guard Concepts and Administration.

Best practices for the protection mode:

- Maximum Protection mode guarantees that no data loss will occur if the primary database fails, even in the case of multiple failures (for example, the network between the primary and standby fails, and then at a later time, the primary fails). This is enforced by never signaling commit success for a primary database transaction until at least one synchronous Data Guard standby has acknowledged that redo has been hardened to disk. Without such an acknowledgment the primary database will stall and eventually shut down rather than allow unprotected transactions to commit. To maintain availability in cases where the primary database is operational but the standby database is not, the best practice is to always have a minimum of two synchronous standby databases in a Maximum Protection configuration. Primary database availability is not impacted if it receives acknowledgment from at least one synchronous standby database.
- Maximum Availability mode guarantees that no data loss will occur in cases where the primary database experiences the first failure to impact the configuration. Unlike the previous protection mode, Maximum Availability will wait a maximum of NET\_TIMEOUT seconds for an acknowledgment from a standby database, after which it will signal commit success to the application and move to the next transaction. Primary database availability (thus the name of the protection mode) is not impacted by an inability to communicate with the standby (for example, due to standby or network outages). Oracle Data Guard will continue to ping the standby and automatically re-establish connection and resynchronize the standby database when possible, but during the period when primary and standby have diverged there will be data loss should a second failure impact the primary database. For this reason, it is a best practice to monitor protection level (simple to do using Enterprise Manager Grid Control) and quickly resolve any disruption in communication between primary and standby before a second failure can occur.
- Maximum Performance mode (the default mode) provides the highest level of data protection that is possible without affecting the performance or the availability of the primary database. This is accomplished by allowing a transaction to commit as soon as the redo data needed to recover that transaction is written to the local online redo log at the primary database (the same behavior as if there were no standby database). Oracle Data Guard transmits redo to the standby database directly from the primary log buffer asynchronous to the local online redo log write. There is never any wait for standby acknowledgment. Similar to Maximum Availability, it is a best practice to monitor protection level (simple to do using Enterprise Manager Grid Control) and quickly resolve any disruption in communication between primary and standby before a second failure can occur.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/protection.htm#SBYDB02000) for information about Data Guard Protection Modes

### 9.2.1 Use Redo Transport Services Best Practices

At a high level, the Redo Transport best practices for planning and implementing redo transport services for Oracle Data Guard are as follows:

- Use the `SYNC` redo transport mode for a high degree of synchronization between the primary and standby databases. Use `SYNC` redo transport for zero data loss protection where performance service levels can tolerate the impact caused by network latency.
- Use the `ASYNC` redo transport mode for minimal impact on the primary database, but with a lower degree of synchronization. Use `ASYNC` redo transport when zero data loss protection is not required or when the performance impact caused by network latency makes it impractical to use `SYNC`.
- Optimize network throughput following the best practices described in Section 9.2.2, "Assess Performance with Proposed Network Configuration".

### 9.2.2 Assess Performance with Proposed Network Configuration

Oracle recommends that you conduct a performance assessment with your proposed network configuration and current, or anticipated, peak redo rate. The network effect between the primary and standby databases, and the effect on the primary database throughput must be understood. Because the network between the primary and standby databases is essential for the two databases to remain synchronized, the infrastructure must have the following characteristics:

- Sufficient bandwidth to accommodate the maximum redo generation rate
- If using the `SYNC` transport, then minimal latency is necessary to reduce the performance impact on the primary database
- Multiple network paths for network redundancy

In configurations that use a dedicated network connection the required bandwidth is determined by the maximum redo rate of the primary database and the efficiency of the network. Depending on the data protection mode, there are other recommended practices and performance considerations. Maximum protection mode and maximum availability mode require `SYNC` transport.

The maximum performance protection mode use `ASYNC` redo transport. Use `ASYNC` redo transport when data loss can be tolerated or when the performance impact caused by network latency makes it impractical to use `SYNC` (use `SYNC` redo transport for zero data loss protection).

Unlike the `ASYNC` transport mode, the `SYNC` transport mode can affect the primary database performance due to the incurred network latency. Distance and network configuration directly influence latency, while high latency can slow the potential transaction throughput and quicken response time. The network configuration, number of repeaters, the overhead of protocol conversions, and the number of routers also affect the overall network latency and transaction response time.

## 9.3 General Data Guard Configuration Best Practices

Use the following configuration best practices for Data Guard:

- Use Oracle Data Guard Broker with Oracle Data Guard
- Use Recovery Manager to Create Standby Databases
- Use Flashback Database for Reinstatement After Failover
- Use FORCE LOGGING Mode
- Use a Simple, Robust Archiving Strategy and Configuration
- Use Standby Redo Logs and Configure Size Appropriately
- Use Data Guard Transport and Network Configuration Best Practices
- Use Data Guard Redo Apply Best Practices
- Implement Multiple Standby Databases

### 9.3.1 Use Oracle Data Guard Broker with Oracle Data Guard

Use Oracle Data Guard broker to create, manage, and monitor a Data Guard configuration. You can perform all Data Guard management operations locally or remotely through the Oracle Data Guard broker's easy-to-use interfaces: the Data Guard management pages in Oracle Enterprise Manager, which is the broker's graphical user interface (GUI), and the Data Guard command-line interface called DGMGRL.

The broker's interfaces improve usability and centralize management and monitoring of the Data Guard configuration. Available as a feature of the Enterprise Edition and Personal Edition of the Oracle database, the broker is also integrated with the Oracle database and Oracle Enterprise Manager.

The benefits of using Oracle Data Guard broker include:

- Enhanced disaster protection.
- Higher availability and scalability with Oracle Real Application Clusters (Oracle RAC) Databases.
- Automated creation of a Data Guard configuration.
- Easy configuration of additional standby databases.
- Simplified, centralized, and extended management.
- Simplified switchover and failover operations.
- Fast Application Notification (FAN) after failovers.
- Built-in monitoring and alert and control mechanisms.
- Transparent to application.

See Also:

[Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/concepts.htm#DGBKR020) for more information about the configuration requirements for the Data Guard Broker

### 9.3.2 Use Recovery Manager to Create Standby Databases

Oracle recommends that you use the Recovery Manager (RMAN) utility to simplify the process of creating a physical standby database.

You can either create a standby database from backups of your primary database, or create a standby database over the network:

- Use the RMAN `DUPLICATE TARGET DATABASE FOR STANDBY` command to create a standby database from backups of your primary database.
	You can use any backup copy of the primary database to create the physical standby database if the necessary archived redo log files to completely recover the database are accessible by the server session on the standby host. RMAN restores the most recent data files unless you execute the `SET UNTIL` command.
- Use the RMAN `FROM ACTIVE DATABASE` option to create the standby database over the network if a preexisting database backup is not accessible to the standby system.
	RMAN copies the data files directly from the primary database to the standby database. The primary database must be mounted or open.

You must choose between active and backup-based duplication. If you do not specify the `FROM ACTIVE DATABASE` option, then RMAN performs backup-based duplication. Creating a standby database over the network is advantageous because:

- You can transfer redo data directly to the remote host over the network without first having to go through the steps of performing a backup on the primary database. (Restoration requires multiple steps including storing the backup locally on the primary database, transferring the backup over the network, storing the backup locally on the standby database, and then restoring the backup on the standby database.)
- With active duplication you can backup a database (as it is running) from Oracle ASM, and restore the backup to a host over the network and place the files directly into Oracle ASM.
	Before this feature, restoration required you to backup the primary and copy the backup files on the primary host file system, transfer the backup files over the network, place the backup files on the standby host file system, and then restore the files into Oracle ASM.

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB04700) for information about using RMAN to Back Up and Restore Files
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rcmbackp.htm#SBYDB01500) for information about Creating a Standby Database with Recovery Manager
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmdupdb.htm#BRADV010)

### 9.3.3 Use Flashback Database for Reinstatement After Failover

Enable Flashback Database on both the primary and standby database so that, in case the original primary database has not been damaged, you can reinstate the original primary database as a new standby database following a failover. If there is a failure during the switchover process, then it can easily be reversed when Flashback Database is enabled. For more information, see [Section 5.1.4, "Enable Flashback Database"](config_db.md).

### 9.3.4 Use FORCE LOGGING Mode

When the primary database is in `FORCE LOGGING` mode, all database data changes are logged. `FORCE LOGGING` mode ensures that the standby database remains consistent with the primary database. If this is not possible because you require the load performance with `NOLOGGING` operations, then you must ensure that the corresponding physical standby data files are subsequently synchronized. To synchronize the physical standby data files, either apply an incremental backup created from the primary database or replace the affected standby data files with a backup of the primary data files taken after the nologging operation. Before the file transfer, you must stop Redo Apply on the physical standby database.

You can enable force logging immediately by issuing an `ALTER DATABASE FORCE LOGGING` statement. If you specify `FORCE LOGGING`, then Oracle waits for all ongoing unlogged operations to finish.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11096) for information about Specifying FORCE LOGGING Mode
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/create_ps.htm#SBYDB4719) for information about Enable Forced Logging

### 9.3.5 Use a Simple, Robust Archiving Strategy and Configuration

This archiving strategy is based on the following assumptions:

- Each database uses a fast recovery area.
- The primary database instances archive remotely to only one apply instance.

Table 9-2 describes the recommendations for a robust archiving strategy when managing a Data Guard configuration through SQL\*Plus. All of the following items are handled automatically when Oracle Data Guard broker is managing a configuration.

Table 9-2 Archiving Recommendations

| Recommendation | Description |
| --- | --- |
| Start archiving on the primary and standby databases | Maintaining a standby database requires that you enable and start archiving on the primary database, as follows:  ``` SQL> SHUTDOWN IMMEDIATE SQL> STARTUP MOUNT; SQL> ALTER DATABASE ARCHIVELOG; SQL> ALTER DATABASE OPEN; ```  Archiving must also be enabled on the standby database to support role transitions. To enable archiving on the standby database:  ``` SQL> SHUTDOWN IMMEDIATE; SQL> STARTUP MOUNT; SQL> ALTER DATABASE ARCHIVELOG; ``` |
| Use a consistent log format (`LOG_ARCHIVE_FORMAT`). | The `LOG_ARCHIVE_FORMAT` parameter should specify the thread, sequence, and resetlogs ID attributes, and the parameter settings should be consistent across all instances. For example: `LOG_ARCHIVE_FORMAT=arch_%t_%S_%r.arc`  Note: If the fast recovery area is used, then this format is ignored. |
| Perform remote archiving to only one standby instance and node for each Oracle RAC standby database. | All primary database instances archive to one standby destination, using the same net service name. Oracle Net Services connect-time failover is used to automatically switch to the "secondary" standby host when the "primary" standby instance has an outage.  If the archives are accessible from all nodes because Oracle ASM or some other shared file system is being used for the fast recovery area, then remote archiving can be spread across the different nodes of an Oracle RAC standby database. |
| Specify role-based destinations with the `VALID_FOR` attribute | The `VALID_FOR` attribute enables you to configure destination attributes for both the primary and the standby database roles in one server parameter file (SPFILE), so that the Data Guard configuration operates properly after a role transition. This simplifies switchovers and failovers by removing the need to enable and disable the role-specific parameter files after a role transition. |

The following example illustrates the recommended initialization parameters for a primary database communicating to a physical standby database. There are two instances, `SALES1` and `SALES2`, running in maximum protection mode.

```
*.DB_RECOVERY_FILE_DEST=+RECO
*.LOG_ARCHIVE_DEST_1='SERVICE=SALES_stby SYNC AFFIRM NET_TIMEOUT=30
    REOPEN=300 VALID_FOR=(ONLINE_LOGFILES, ALL_ROLES) DB_UNIQUE_NAME=SALES_stby'
*.LOG_ARCHIVE_DEST_STATE_1=ENABLE
```

The fast recovery area must be accessible to any node within the cluster and use a shared file system technology such as automatic storage management (Oracle ASM), a cluster file system, a global file system, or high availability network file system (HA NFS). You can also mount the file system manually to any node within the cluster very quickly. This is necessary for recovery because all archived redo log files must be accessible on all nodes.

On the standby database nodes, recovery from a different node is required when a failure occurs on the node applying redo and the apply service cannot be restarted. In that case, any of the existing standby instances residing on a different node can initiate managed recovery. In the worst case, when the standby archived redo log files are inaccessible, the managed recovery process (MRP) on the different node fetches the archived redo log files using the FAL server to retrieve from the primary node directly.

When configuring hardware vendor shared file system technology, verify the performance and availability implications. Investigate the following issues before adopting this strategy:

- Is the shared file system accessible by any node regardless of the number of node failures?
- What is the performance impact when implementing a shared file system?
- Is there any effect on the interconnect traffic?

### 9.3.6 Use Standby Redo Logs and Configure Size Appropriately

You should configure standby redo logs on all primary and standby databases for improved availability and performance.

For each redo log thread (a thread is associated with an OracleRAC database instance), number of Standby Redo Logs = number of Redo Log Groups + 1

The additional standby redo log eliminates the possibility of a standby database waiting on standby redo log. For example, if a primary database has two instances (threads) and each thread has three online log groups, then you should pre-configure 8 standby redo logs on the primary database and each standby database. Furthermore, if the primary or standby databases are not a symmetrical Real Application Cluster (example 8-node primary Oracle RAC cluster compared to 2-node standby Oracle RAC cluster), then the primary and standby databases should still have an equal number of standby redo logs and all threads should be represented.

The statements in Example 9-1 create three standby logs per thread.

Example 9-1 Create Standby Log Members

```
SQL> ALTER DATABASE ADD STANDBY LOGFILE THREAD 1 SIZE 1G;SQL> ALTER DATABASE ADD STANDBY LOGFILE THREAD 1 SIZE 1G;SQL> ALTER DATABASE ADD STANDBY LOGFILE THREAD 1 SIZE 1G;SQL> ALTER DATABASE ADD STANDBY LOGFILE THREAD 1 SIZE 1G;SQL> ALTER DATABASE ADD STANDBY LOGFILE THREAD 2 SIZE 1G;SQL> ALTER DATABASE ADD STANDBY LOGFILE THREAD 2 SIZE 1G;SQL> ALTER DATABASE ADD STANDBY LOGFILE THREAD 2 SIZE 1G;SQL> ALTER DATABASE ADD STANDBY LOGFILE THREAD 2 SIZE 1G;
```

Consider the following additional guidelines when creating standby redo logs:

- Create the same number of standby redo logs on both the primary and standby databases.
- Create all online redo logs and standby redo logs for both primary and standby databases so that they are the same size.
- Create standby redo logs in the first available ASM high redundancy disk group, or ensure that the logs are protected using external storage redundancy.
- In an Oracle RAC environment, create standby redo logs on a shared disk.
- In an Oracle RAC environment, assign a thread when the standby redo log is created as described in Example 9-1.
- Do not multiplex the standby redo logs.

To check the number and group numbers of the redo logs, query the `V$LOG` view:

```
SQL> SELECT * FROM V$LOG;
```

To check the results of the `ALTER DATABASE ADD STANDBY LOGFILE THREAD` statements, query the `V$STANDBY_LOG` view:

```
SQL> SELECT * FROM V$STANDBY_LOG;
```

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/log_transport.htm#SBYDB4752) for information about managing standby redo logs

### 9.3.7 Use Data Guard Transport and Network Configuration Best Practices

The best practices for Data Guard transport and network configuration include:

- Set the LOG\_ARCHIVE\_MAX\_PROCESSES Parameter
- Set the Network Configuration and Highest Network Redo Rates

#### 9.3.7.1 Set the LOG\_ARCHIVE\_MAX\_PROCESSES Parameter

In most cases the default for `LOG_ARCHIVE_MAX_PROCESSES` is sufficient. However, in a Data Guard configurations that have multiple standby databases it may be necessary to increase the number of archive processes. The value of the `LOG_ARCHIVE_MAX_PROCESSES` initialization parameter must be at least one greater than the total number of all remote destinations. Use the following equation when setting the `LOG_ARCHIVE_MAX_PROCESSES` parameter for highly available environments:

```
LOG_ARCHIVE_MAX_PROCESSES = sum(remote_destinations) + count(threads)
```

You can adjust these parameter settings after evaluating and testing the initial settings in your production environment.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/archredo.htm#ADMIN11337) for more information about Adjusting the Number of Archiver Processes

#### 9.3.7.2 Set the Network Configuration and Highest Network Redo Rates

To set the network configuration and highest network redo rates:

- Properly Configure TCP Send / Receive Buffer Sizes
- Increase SDU Size
- Set TCP.NODELAY to YES
- Determine When to Use Redo Transport Compression

Properly Configure TCP Send / Receive Buffer Sizes

To achieve high network throughput, especially for a high-latency, high-bandwidth network, the minimum recommended setting for the sizes of the TCP send and receive socket buffers is the bandwidth-delay product (BDP) of the network link between the primary and standby systems. Settings higher than the BDP may show incremental improvement. For example, in the MAA Linux test lab, simulated high-latency, high-bandwidth networks realized small, incremental increases in throughput when using TCP send and receive socket buffer settings up to three times the BDP.

BDP is product of the network bandwidth and latency. Socket buffer sizes are set using the Oracle Net parameters `RECV_BUF_SIZE` and `SEND_BUF_SIZE`, so that the socket buffer size setting affects only Oracle TCP connections. The operating system may impose limits on the socket buffer size that must be adjusted so Oracle can use larger values. For example, on Linux, the parameters `net.core.rmem_max` and `net.core.wmem_max` limit the socket buffer size and must be set larger than `RECV_BUF_SIZE` and `SEND_BUF_SIZE`.

Set the send and receive buffer sizes at either the value you calculated or 10 MB (10,485,760 bytes), whichever is larger. For example, if bandwidth is 622 Mbits and latency is 30 ms, then you would calculate the minimum size for the `RECV_BUF_SIZE` and `SEND_BUF_SIZE` parameters as follows: 622,000,000 / 8 x 0.030 = 2,332,500 bytes. Then, multiply the BDP 2,332,500 x 3 for a total of 6,997,500.

In this example, you would set the initialization parameters as follows:

`RECV_BUF_SIZE=10485760`

`SEND_BUF_SIZE=10485760`

Increase SDU Size

With Oracle Net Services it is possible to control data transfer by adjusting the size of the Oracle Net setting for the session data unit (SDU). Oracle internal testing has shown that setting the SDU to its maximum value of 65535 can improve performance for the SYNC transport. You can set SDU on a per connection basis using the SDU parameter in the local naming configuration file (`TNSNAMES.ORA`) and the listener configuration file (`LISTENER.ORA`), or you can set the SDU for all Oracle Net connections with the profile parameter `DEFAULT_SDU_SIZE` in the `SQLNET.ORA` file.

Note that the `ASYNC` transport uses the new streaming protocol and increasing the SDU size from the default has no performance benefit.

See Also:

[Oracle Database Net Services Reference](https://docs.oracle.com/cd/E11882_01/network.112/e10835/toc.htm) for more information about the [`SDU`](https://docs.oracle.com/cd/E11882_01/network.112/e10835/tnsnames.htm#NETRF275) and [`DEFAULT_SDU_SIZE`](https://docs.oracle.com/cd/E11882_01/network.112/e10835/sqlnet.htm#NETRF006) parameters

Set TCP.NODELAY to YES

To preempt delays in buffer flushing in the TCP protocol stack, disable the TCP Nagle algorithm by setting `TCP.NODELAY` to `YES` in the `SQLNET.ORA` file on both the primary and standby systems.

See Also:

[Oracle Database Net Services Reference](https://docs.oracle.com/cd/E11882_01/network.112/e10835/sqlnet.htm#NETRF239) for more information about the `TCP.NODELAY` parameter

Determine When to Use Redo Transport Compression

In Oracle Database 11g Release 2 (11.2.0.2) redo transport compression is no longer limited to compressing redo data only when a redo gap is being resolved. When compression is enabled for a destination, all redo data sent to that destination is compressed.

In general, compression is most beneficial when used over low bandwidth networks. As the network bandwidth increases, the benefit is reduced. Compressing redo in a Data Guard environment is beneficial if:

- Sufficient CPU resources are available for the compression processing.
- The database redo rate is being throttled by a low bandwidth network.

Before enabling compression, assess the available CPU resources and decide if enabling compression is feasible. For complete information about enabling compression, see "Redo Transport Compression in a Data Guard Environment" in My Oracle Support Note 729551.1 at

`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=729551.1`

### 9.3.8 Use Data Guard Redo Apply Best Practices

To improve the Redo Apply rate of a physical standby database (and media recovery):

- Maximize I/O Rates on Standby Redo Logs and Archived Redo Logs
- Assess Recovery Rate
- Set `DB_BLOCK_CHECKSUM` = `FULL` and `DB_BLOCK_CHECKING=MEDIUM` or `FULL`
- Set DB\_CACHE\_SIZE to a Value Greater than on the Primary Database
- Assess Database Wait Events
- Tune I/O Operations
- Assess System Resources

See Also:

The MAA white paper "Active Data Guard 11g Best Practices (includes best practices for Redo Apply)" from the MAA Best Practices area for Oracle Database at

`http://www.oracle.com/goto/maa`

#### 9.3.8.1 Maximize I/O Rates on Standby Redo Logs and Archived Redo Logs

Measure read I/O rates on the standby redo logs and archived redo log directories. Concurrent writing of shipped redo on a standby database might reduce the redo read rate due to I/O saturation. The overall recovery rate is always bounded by the rate at which redo can be read; so ensure that the redo read rate surpasses your required recovery rate.

#### 9.3.8.2 Assess Recovery Rate

To obtain the history of recovery rates, use the following query to get a history of recovery progress:

```
SELECT * FROM V$RECOVERY_PROGRESS;
```

If your `ACTIVE` `APPLY` `RATE` is greater than the maximum redo generation rate at the primary database or twice the average generation rate at the primary database, then no tuning is required; otherwise follow the tuning tips below. The redo generation rate for the primary database can be monitored from Enterprise Manager or extracted from AWR reports under statistic `REDO` `SIZE`. If `CHECKPOINT` `TIME` `PER` `LOG` is greater than ten seconds, then investigate tuning I/O and checkpoints.

#### 9.3.8.3 Set DB\_BLOCK\_CHECKSUM=FULL and DB\_BLOCK\_CHECKING=MEDIUM or FULL

Redo apply performance should be fast enough to keep up with most applications' redo generation rates but you can temporarily disable `DB_BLOCK_CHECKING` to speed up recovery. If you disable `DB_BLOCK_CHECKING`, you will disable in-memory block semantic checks as described in My Oracle Support [note 1302539.1](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1302539.1).

Note:

To check for block corruption that was not preventable through the `DB_BLOCK_CHECKING` parameter, use:
- RMAN `BACKUP` command with the `VALIDATE` option
- `DBVERIFY` utility
- `ANALYZE` `TABLE` `tablename` `VALIDATE` `STRUCTURE` `CASCADE` SQL statement

Set the `DB_LOST_WRITE_PROTECT` parameter to `FULL` on the standby database to enable Oracle to detect writes that are lost in the I/O subsystem. The impact on redo apply is very small for OLTP applications and generally less than 5 percent.

See Also:

[Section 5.1.6.1, "Preventing Widespread Data Corruption"](config_db.md)

#### 9.3.8.4 Set DB\_CACHE\_SIZE to a Value Greater than on the Primary Database

Set `DB_CACHE_SIZE` to a value greater than that for the primary database. Set `DB_KEEP_CACHE_SIZE` and `DB_RECYCLE_CACHE_SIZE` to `0`.

Having a large database cache size can improve media recovery performance by reducing the amount of physical data block reads. Because media recovery does not require `DB_KEEP_CACHE_SIZE` and `DB_RECYCLE_CACHE_SIZE` or require a large `SHARED_POOL_SIZE`, the memory can be reallocated to the `DB_CACHE_SIZE`.

Before converting the standby database into a primary database, reset these parameters to the primary database settings.

#### 9.3.8.5 Assess Database Wait Events

With the Active Data Guard option and real-time query, you can use Statspack from the primary database to collect data from a standby database that is opened read-only and performing recovery. Any tuning or troubleshooting exercise should start with collecting Standby Statspack reports. For complete details about installing and using Standby Statspack, see "Installing and Using Standby Statspack in 11g" in My Oracle Support Note 454848.1 at

`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=454848.1`

If you do not have a license for the Active Data Guard option, you can determine the top system and session wait events by querying the standby database's `V$SYSTEM_EVENT`, `V$SESSION_WAIT`, and `V$EVENT_HISTOGRAM` and looking for the largest `TIME_WAITED` value. You may have to capture multiple snapshots of the query results and manually extract the difference to accurately assess a certain time period.

If recovery is applying a lot of redo data efficiently, the system is I/O bound and the I/O wait should be reasonable for your system. The vast majority of wait events related to parallel recovery coordinators and slaves apply to the coordinator. Slaves are either applying changes (clocking on CPU) or waiting for changes to be passed from the coordinator.

Typically, in a properly tuned system, the top wait event is `db file parallel write` followed by `checkpoint completed`. Consult the table below for tuning advice in cases where `db file parallel write` is not the top wait event. The database wait events are shown in Table 9-3 and Table 9-4.

Table 9-3 Parallel Recovery Coordinator Wait Events

| Wait Name | Description | Tuning |
| --- | --- | --- |
| `Log file sequential read` | The parallel recovery coordinator is waiting on I/O from the online redo log or the archived redo log. | Tune or increase the I/O bandwidth for the ASM diskgroup where the archive logs or online redo logs reside. |
| `Parallel recovery read buffer free` | This event indicates that all read buffers are being used by slaves, and usually indicates that the recovery slaves lag behind the coordinator. | Tune or increase the I/O bandwidth for the ASM diskgroup where data files reside. |
| `Parallel recovery change buffer free` | The parallel recovery coordinator is waiting for a buffer to be released by a recovery slave. Again, this is a sign the recovery slaves are behind the coordinator. | Tune or increase the I/O bandwidth for the ASM diskgroup where data files reside. |
| `Datafile init write` | The parallel recovery coordinator is waiting for a file resize to finish, as would occur with file auto extend. | Tune or increase the I/O bandwidth for the ASM diskgroup where data files reside. |
| `Parallel recovery control message reply` | The coordinator has sent a synchronous control messages to all slaves, and is waiting for all slaves to reply. | This is a non-tunable event. |

When dealing with recovery slave events, it is important to know how many slaves were started. Divide the wait time for any recovery slave event by the number of slaves. Table 9-4 describes the parallel recovery slave wait events.

Table 9-4 Parallel Recovery Slave Wait Events

| Wait Name | Description | Tuning |
| --- | --- | --- |
| `Parallel recovery slave next change` | The parallel recovery slave is waiting for a change to be shipped from the coordinator. This is in essence an idle event for the recovery slave. To determine the amount of CPU a recovery slave is using, divide the time spent in this event by the number of slaves started and subtract that value from the total elapsed time. This may be close, because there are some waits involved. | Tune or increase the I/O bandwidth for the ASM diskgroup where the archive logs or online redo logs reside. |
| `DB File Sequential Read` | A parallel recovery slave (or serial recovery process) is waiting for a batch of synchronous data block reads to complete. | Tune or increase the I/O bandwidth for the ASM diskgroup where data files reside. |
| `Checkpoint completed` | Recovery is waiting for checkpointing to complete, and Redo Apply is not applying any changes currently. | Tune or increase the I/O bandwidth for the ASM diskgroup where data files reside.  Also, increase the number of `db_writer_processes` until the `checkpoint completed` wait event is lower than the `db file parallel write` wait event. Consider also increasing the online log file size on the primary and standby to decrease the number of full checkpoints at log switch boundaries. |
| `Recovery read` | A parallel recovery slave is waiting for a batched data block I/O. | Tune or increase the I/O bandwidth for the ASM diskgroup where data files reside. |

#### 9.3.8.6 Tune I/O Operations

DBWR must write out modified blocks from the buffer cache to the data files. Always use native asynchronous I/O by setting `DISK_ASYNCH_IO` to `TRUE` (default). In the rare case that asynchronous I/O is not available, use `DBWR_IO_SLAVES` to improve the effective data block write rate with synchronous I/O.

Ensure that you have sufficient I/O bandwidth and that I/O response time is reasonable for your system either by doing some base I/O tests, comparing the I/O statistics with those for the primary database, or by looking at some historical I/O metrics. Be aware that I/O response time may vary when many applications share the same storage infrastructure such as with a Storage Area Network (SAN) or Network Attached Storage (NAS).

#### 9.3.8.7 Assess System Resources

Use system commands such as UNIX `sar` and `vmstat` commands, or use system monitoring tools to assess the system resources. Alternatively, you can monitor using Oracle Enterprise Manager, AWR reports, or performance views such as `V$SYSTEM_EVENT`, `V$ASM_DISK` and `V$OSSTAT`.

1. If there are I/O bottlenecks or excessive wait I/O operations, then investigate operational or application changes that increased the I/O volume. If the high waits are due to insufficient I/O bandwidth, then add more disks to the relevant Oracle ASM disk group. Verify that this is not a bus or controller bottleneck or any other I/O bottleneck. The read I/O rate from the standby redo log should be greater than the expected recovery rate.
2. Check for excessive swapping or memory paging.
3. Check to ensure the recovery coordinator or MRP is not CPU bound during recovery.

### 9.3.9 Implement Multiple Standby Databases

You should deploy multiple standby databases for any of the following purposes. When desired, use standby databases for these purposes while reserving at least one standby database to serve as the primary failover target:

- To provide continuous protection following failover
	The standby databases in a multiple standby configuration that are not the target of the role transition (these databases are referred to as bystander standby databases) automatically apply redo data received from the new primary database.
- To achieve zero data loss protection while also guarding against widespread geographic disasters that extend beyond the limits of synchronous communication
	For example, one standby database that receives redo data synchronously is located 200 miles away, and a second standby database that receives redo data asynchronously is located 1,500 miles away from the primary.
- To perform rolling database upgrades while maintaining disaster protection throughout the rolling upgrade process
- To perform testing and other ad-hoc tasks while maintaining disaster-recovery protection

Use Multiple Standby Databases Best Practices

The [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/unplanned.htm#HAOVW120) describes how a multiple standby database architecture is virtually identical to that of single standby database architectures. Therefore, the configuration guidelines for implementing multiple standby databases described in this section complement the existing best practices for physical and logical standby databases.

When deploying multiple standby databases, use the following best practices:

- Use Oracle Data Guard broker (described in [Chapter 12, "Monitoring for High Availability"](monitor.md)) to manage your configuration and perform role transitions. However, if you choose to use SQL\*Plus statements, see the MAA white paper "Multiple Standby Databases Best Practices" for best practices from the MAA Best Practices area for Oracle Database at
	`http://www.oracle.com/goto/maa`
- If you are using Flashback Database for the sole purpose of reinstating databases following a failover, a `DB_FLASHBACK_RETENTION_TARGET` of 120 minutes is the minimum recommended value. When you use Flashback Database to quickly reinstate the original primary as the standby after a failover, instead of re-creating the entire standby database from backups or from the primary database, when using Fast-start Failover, ensure the `UNDO_RETENTION` and `DB_FLASHBACK_RETENTION_TARGET` initialization parameters are set to a minimum of 120 so that reinstatement is still possible after a prolonged outage. On a standby the flashback barrier cannot be guaranteed to be published every 30 minutes as it is on a primary. Thus, when enabling flashback database on a standby, the `DB_FLASHBACK_RETENTION_TARGET` should be a minimum of 120. Since the primary and standby should match, this implies the same for the primary.
- Enable supplemental logging in configurations containing logical standby databases. When creating a configuration with both physical and logical standby databases, issue the `ALTER DATABASE ADD SUPPLEMENTAL LOG DATA` statement to enable supplemental logging in the following situations:
	- When adding a logical standby database to an existing configuration consisting of all physical standby databases, you must enable supplemental logging on all existing physical standby databases in the configuration.
		- When adding a physical standby database to an existing configuration that contains a logical standby database, you must enable supplemental logging on the physical standby database when you create it.
	As part of the logical standby database creation supplemental logging is automatically enabled on the primary. Enabling supplemental logging is a control file change and therefore the change is not propagated to each physical standby database. Supplemental logging is enabled automatically on a logical standby database when it is first converted from a physical standby database to a logical standby database as part of the dictionary build process.To enable supplemental logging, issue the following SQL\*Plus statement when connected to a physical standby database:
	```
	SQL> ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (PRIMARY KEY, UNIQUE INDEX) COLUMNS;
	```
- If logical standby databases are not configured to perform real-time queries, then consider configuring SQL Apply to delay applying redo data to the logical standby database. By delaying the application of redo, you can minimize the need to manually reinstate the logical standby database after failing over to a physical standby database.
	To set a time delay, use the `DELAY=minutes` attribute of the `LOG_ARCHIVE_DEST_` `n` initialization parameter.

See Also:

- [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/unplanned.htm#HAOVW120) to learn about the benefits of using multiple standby database and for implementation examples
- [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/architectures.htm#HAOVW225) for an overview of multiple standby database architectures
- The MAA white paper "Multiple Standby Databases Best Practices" from the MAA Best Practices area for Oracle Database at
	`http://www.oracle.com/goto/maa`

## 9.4 Oracle Data Guard Role Transition Best Practices

With proper planning and execution, Data Guard role transitions can effectively minimize downtime and ensure that the database environment is restored with minimal impact on the business. Using a physical standby database, MAA testing has determined that switchover and failover times with Oracle Data Guard 11g have been reduced to seconds. This section describes best practices for both switchover and failover.

### 9.4.1 Oracle Data Guard Switchovers Best Practices

A database switchover performed by Oracle Data Guard is a planned transition that includes a series of steps to switch roles between a standby database and a primary database. Following a successful switchover operation, the standby database assumes the primary role and the primary database becomes a standby database. Switchovers are typically completed in only seconds to minutes. At times the term switchback is also used within the scope of database role management. A switchback operation is a subsequent switchover operation to return the roles to their original state.

Data Guard enables you to change these roles dynamically by:

- Using Oracle Enterprise Manager
- Using the Oracle Data Guard broker's DGMGRL command-line interface
- Issuing SQL statements, as described in [Section 14.2.1.3, "How to Perform Data Guard Switchover"](schedule_outage.md)

See Also:

[Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/toc.htm) for information about using Oracle Enterprise Manager or Oracle Data Guard broker's DGMGRL command-line interface to perform database switchover

To optimize switchover processing, perform the following steps before performing a switchover:

- Disconnect all sessions possible using the `ALTER` `SYSTEM` `KILL` `SESSION` SQL\*Plus command.
- Stop job processing by setting the `AQ_TM_PROCESSES` parameter to `0`.
- Cancel any specified apply delay by using the `NODELAY` keyword to stop and restart log apply services on the standby database.
	```
	ALTER DATABASE RECOVER MANAGED STANDBY DATABASE CANCEL;
	ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE NODELAY;
	```
	You can view the current delay setting on the primary database by querying the `DELAY_MINS` column of the `V$ARCHIVE_DEST` view.
- For physical standby databases in an Oracle RAC environment, ensure there is only one instance active for each primary and standby database.
- Configure the standby database to use real-time apply and, if possible, ensure the databases are synchronized before the switchover operation to optimize switchover processing.
	For the fastest switchover, use real-time apply so that redo data is applied to the standby database as soon as it is received, and the standby database is synchronized with the primary database before the switchover operation to minimize switchover time. To enable real-time apply use the following SQL\*Plus statement:
	```
	ALTER DATABASE RECOVER MANAGED STANDBY DATABASE DISCONNECT USING CURRENT LOGFILE;
	```
- For a physical standby database, reduce the number of archiver (ARCn) processes to the minimum needed for both remote and local archiving. Additional archiver processes can take additional time to shut down, thereby increasing the overall time it takes to perform a switchover. After the switchover has completed you can reenable the additional archiver processes.
- Set the `LOG_FILE_NAME_CONVERT` initialization parameter to any valid value for the environment, or if it is not needed set the parameter to null.
	As part of a switchover, the standby database must clear the online redo log files on the standby database before opening as a primary database. The time needed to complete the I/O can significantly increase the overall switchover time. By setting the `LOG_FILE_NAME_CONVERT` parameter, the standby database can pre-create the online redo logs the first time the MRP process is started. You can also pre-create empty online redo logs by issuing the SQL\*Plus `ALTER DATABASE CLEAR LOGFILE` statement on the standby database.

See Also:

Support notes for switchover best practices for Data Guard Physical Standby (11.2.0.2):
- If using SQL\*Plus, see "11.2 Data Guard Physical Standby Switchover Best Practices using SQL\*Plus" in My Oracle Support Note 1304939.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1304939.1`
- If using the Oracle Data Guard broker or Oracle Enterprise Manager, see "11.2 Data Guard Physical Standby Switchover Best Practices using the Broker" in My Oracle Support Note 1305019.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1305019.1`
- The MAA white paper "Switchover and Failover Best Practices" from the MAA Best Practices area for Oracle Database at
	`http://www.oracle.com/goto/maa`

### 9.4.2 Oracle Data Guard Failovers Best Practices

A failover is typically used only when the primary database becomes unavailable, and there is no possibility of restoring it to service within a reasonable period. During a failover the primary database is taken offline at one site and a standby database is brought online as the primary database.

With Data Guard the process of failover can be completely automated using fast-start failover or it can be a manual, user driven process. Oracle recommends using fast-start failover to eliminate the uncertainty inherent in a process that requires manual intervention. Fast-start failover automatically executes a failover within seconds of an outage being detected.

- Comparing Fast-Start Failover and Manual Failover
- Failover Best Practices (Manual Failover and Fast-Start Failover)
- Fast-Start Failover Best Practices
- Manual Failover Best Practices

See Also:

For a comprehensive review of Oracle Data Guard failover best practices, see:
- [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/sofo.htm#DGBKR330) for information about Switchover and Failover Operations
- "Data Guard Fast-Start Failover" MAA white paper from the MAA Best Practices area for Oracle Database at
	`http://www.oracle.com/goto/maa`
- "11.2 Data Guard Physical Standby Switchover Best Practices using SQL\*Plus" in My Oracle Support Note 1304939.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1304939.1`
- "11.2 Data Guard Physical Standby Switchover Best Practices using the Broker" in My Oracle Support Note 1305019.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1305019.1`

#### 9.4.2.1 Comparing Fast-Start Failover and Manual Failover

There are two distinct types of failover: manual failover and fast-start failover. An administrator initiates manual failover when the primary database fails. In contrast, Data Guard automatically initiates a fast-start failover without human intervention after the primary database has been unavailable for a set period (the fast-start failover threshold).

Table 9-5 compares fast-start failover and manual failover.

Table 9-5 Comparing Fast-Start Failover and Manual Failover

| Points of Comparison | Fast-Start Failover | Manual Failover |
| --- | --- | --- |
| Benefits | Allows you to increase availability with less need for manual intervention, thereby reducing management costs. | Gives you control over exactly when a failover occurs and to which target standby database. |
| Failover triggers | The following conditions automatically trigger a fast-start failover:  - Database instance failure (or last instance failure in an Oracle RAC configuration). - Shutdown abort (or a shutdown abort of the last instance in an Oracle RAC configuration). - Specific conditions that are detected through the database health-check mechanism (for example, data files taken offline due to I/O errors). 	Fast-start failover can be enabled for these conditions (`ENABLE FAST_START FAILOVER CONDITION`) and `ORA` errors raised by the Oracle server when they occur. 	See [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/sofo.htm#DGBKR392) for a full list of conditions. - Both the observer and the standby database lose their network connection to the primary database. - Application initiated fast-start failover using the `DBMS_DG.INITIATE_FS_FAILOVER` PL/SQL procedure. | A manual failover is user initiated and involves performing a series of steps to convert a standby database into a primary database. A manual failover should be performed due to an unplanned outage such as:  - Site disaster which results in the primary database becoming unavailable (all instances of an Oracle RAC primary database). - User errors that cannot be repaired in a timely fashion. - Data failures, which impact the production application. |
| Management | Use the following tools to manage fast-start failover failovers:  - Oracle Enterprise Manager - The Oracle Data Guard broker command-line interface (DGMGRL)  See [Section 14.2.1.3, "How to Perform Data Guard Switchover"](schedule_outage.md). | Use the following tools to perform manual failovers:  - Oracle Enterprise Manager - The Oracle Data Guard broker command-line interface (DGMGRL) - SQL statements  See [Section 13.2.2.3, "Best Practices for Performing Manual Failover"](outage.md). |
| Restoring the original primary database after failover | Following a fast-start failover, Oracle Data Guard broker can automatically reconfigure the original primary database as a standby database upon reconnection to the configuration (`FastStartFailoverAutoReinstate`), or you can delay the reconfiguration to allow diagnostics on the failed primary. Automatic reconfiguration enables Data Guard to restore disaster protection in the configuration quickly and easily, returning the database to a protected state as soon as possible. | After manual failover, you must reinstate the original primary database as a standby database to restore fault tolerance. |
| Restoring bystander standby databases after failover | Oracle Data Guard broker coordinates the role transition on all databases in the configuration.  Bystanders that do no require reinstatement are available as viable standby databases to the new primary. Bystanders that require reinstatement are automatically reinstated by the observer. | A benefit of using Oracle Data Guard broker is that it provides the status of bystander databases and indicates whether a database must be reinstated. Status information is not readily available when using SQL\*Plus statements to manage failover.  See [Section 13.3.2, "Restoring a Standby Database After a Failover"](outage.md). |
| Application failover | Oracle Data Guard broker automatically publishes FAN/AQ (Advanced Queuing) and FAN/ONS (Oracle Notification Service) notifications after a failover. Clients that are also configured for Fast Connection Failover can use these notifications to connect to the new primary database. You can also use the `DB_ROLE_CHANGE` system event to help user applications locate services on the primary database. (These events are also available for manual failovers performed by the broker. See [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/dbresource.htm#DGBKR300).) | Oracle Data Guard broker automatically publishes FAN/AQ (Advanced Queuing) and FAN/ONS (Oracle Notification Service) notifications after a failover. Clients that are also configured for Fast Connection Failover can use these notifications to connect to the new primary database. You can also use the DB\_ROLE\_CHANGE system event to help user applications locate services on the primary database. (These events are also available for manual failovers performed by the broker. See [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/dbresource.htm#DGBKR300).) |

#### 9.4.2.2 Failover Best Practices (Manual Failover and Fast-Start Failover)

To optimize failover processing:

- Enable Flashback Database to reinstate the failed primary databases after a failover operation has completed. Flashback Database facilitates fast point-in-time recovery, if needed.
- Use real-time apply with Flashback Database to apply redo data to the standby database as soon as it is received, and to quickly rewind the database should user error or logical corruption be detected.
- Consider configuring multiple standby databases to maintain data protection following a failover.
- Set the `LOG_FILE_NAME_CONVERT` parameter. As part of a failover, the standby database must clear its online redo logs before opening as the primary database. The time needed to complete this I/O can add significantly to the overall failover time. By setting the `LOG_FILE_NAME_CONVERT` parameter, the standby pre-creates the online redo logs the first time the MRP process is started. You can also pre-create empty online redo logs by issuing the SQL\*Plus `ALTER DATABASE CLEAR LOGFILE` statement on the standby database.
- Use fast-start failover. The MAA tests running Oracle Database 11g show that failovers performed using Oracle Data Guard broker and fast-start failover offer a significant improvement in availability. For more information, see Section 9.4.2.3, "Fast-Start Failover Best Practices".
- For physical standby databases, do the following:
	- When transitioning from read-only mode to Redo Apply (recovery) mode, restart the database.
		- Go directly to the `OPEN` state from the `MOUNTED` state instead of restarting the standby database (as required in releases before Oracle Database 11g release 2).
		- See the MAA white paper "Oracle Data Guard Redo Apply and Media Recovery" to optimize media recovery for Redo Apply from the MAA Best Practices area for Oracle Database at
		`http://www.oracle.com/goto/maa`

#### 9.4.2.3 Fast-Start Failover Best Practices

Fast-start failover automatically, quickly, and reliably fails over to a designated standby database if the primary database fails, without requiring manual intervention to execute the failover. You can use fast-start failover only in an Oracle Data Guard configuration that is managed by Oracle Data Guard broker.

The Oracle Data Guard configuration can be running in either the maximum availability or maximum performance mode with fast-start failover. When fast-start failover is enabled, the broker ensures fast-start failover is possible only when the configured data loss guarantee can be upheld. Maximum availability mode provides an automatic failover environment guaranteed to lose no data. Maximum performance mode provides an automatic failover environment guaranteed to lose no more than the amount of data (in seconds) specified by the `FastStartFailoverLagLimit` configuration property.

Use the following fast-start failover best practices in addition to the generic best practices listed in the Section 9.4.2.2, "Failover Best Practices (Manual Failover and Fast-Start Failover)":

- Run the fast-start failover observer process on a host that is not located in the same data center as the primary or standby database.
	Ideally, you should run the observer on a system that is equally distant from the primary and standby databases. The observer should connect to the primary and standby databases using the same network as any end-user client. If the designated observer fails, Oracle Enterprise Manager can detect it and automatically restart the observer. If the observer cannot run at a third site, then you should install the observer on the same network as the application. If a third, independent location is not available, then locate the observer in the standby data center on a separate host and isolate the observer as much as possible from failures affecting the standby database.
- Make the observer highly available by using Oracle Enterprise Manager to configure the original primary database to be automatically reinstated as a standby database when a connection to the database is reestablished. Also, Oracle Enterprise Manager enables you to define an alternate host on which to restart the observer.
	After the failover completes, the original primary database is automatically reinstated as a standby database when a connection to it is reestablished, if you set the `FastStartFailoverAutoReinstate` configuration property to `TRUE`.
- Set the value of the `FastStartFailoverThreshold` property according to your configuration characteristics, as described in Table 9-6.
	Table 9-6 Minimum Recommended Settings for FastStartFailoverThreshold
	| Configuration | Minimum Recommended Setting |
	| --- | --- |
	| Single-instance primary, low latency, and a reliable network | 15 seconds |
	| Single-instance primary and a high latency network over WAN | 30 seconds |
	| Oracle RAC primary | Oracle RAC miscount + reconfiguration time + 30 seconds |

Test your configuration using the settings shown in Table 9-6 to ensure that the fast-start failover threshold is not so aggressive that it induces false failovers, or so high it does not meet your failover requirements.

#### 9.4.2.4 Manual Failover Best Practices

You should perform a manual failover, which is user-driven, only in case of an emergency and the failover should be initiated due to an unplanned outage such as:

- Site disaster that results in the primary database becoming unavailable
- User errors that cannot be repaired in a timely fashion
- Data failures, to include widespread corruption, which affects the production application

Use the following manual failover best practices in addition to the generic best practices listed in Section 9.4.2.2, "Failover Best Practices (Manual Failover and Fast-Start Failover)":

- Reinstate the original primary database as a standby database to restore fault tolerance to your environment. The standby database can be quickly reinstated by using Flashback Database. See [Section 13.3.2, "Restoring a Standby Database After a Failover."](outage.md)

See Also:

For physical standby databases see the MAA white paper "Oracle Data Guard Redo Apply and Media Recovery" from the MAA Best Practices area for Oracle Database at

`http://www.oracle.com/goto/maa`

## 9.5 Use Oracle Active Data Guard Best Practices

If you have a license for the Oracle Active Data Guard option then you can open a physical standby database for read-only access while Redo Apply on the standby database continues to apply redo data received from the primary database. All queries reading from the physical standby database execute in real time and return current results, providing more efficient use of system resources and additional assurance that the standby is healthy without compromising data protection or extending recovery time if a failover is required. Hence, this capability is referred to as [real-time query](glossary.md).

Note:

A physical standby database can be open for read-only access while Redo Apply is active if a license for the Oracle Active Data Guard option has been purchased. This capability, known as real-time query also provides the ability to have block-change tracking on the standby database, thus allowing incremental backups to be performed on the standby.

To deploy real-time query:

- Ensure Active Data Guard is enabled.
	The easiest and best way to view the status of Oracle Active Data Guard is on the Data Guard overview page through Oracle Enterprise Manager.
	Alternatively, query the `v$database` view on the standby database and confirm the status of " `READ ONLY WITH APPLY` ':
	```
	SQL> SELECT open_mode FROM V$DATABASE;
	OPEN_MODE
	--------------------
	READ ONLY WITH APPLY
	```
- Use real-time apply on the standby database so that changes are applied as soon as the redo data is received.
	Oracle Data Guard broker automatically enables real-time apply when the configuration is created. If you are using the SQL\*Plus command-line to create your configuration, then enable real-time apply as follows:
	Issue the statement:
	```
	ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE
	```
- Enable Flashback Database on the standby database to minimize downtime for logical corruptions.
- Monitor standby performance by using Standby Statspack. For complete details about installing and using Standby Statspack, see "Installing and Using Standby Statspack in 11g" in My Oracle Support Note 454848.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=454848.1`
- When you deploy real-time query to offload queries from a primary database to a physical standby database, monitor the apply lag to ensure that it is within acceptable limits. See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/manage_ps.htm#SBYDB4778) for information about Monitoring Apply Lag in a Real-time Query Environment.
- Create an Oracle Data Guard broker configuration to simplify management and to enable automatic apply instance failover on an Oracle RAC standby database.

See Also:

The "Active Data Guard 11g Best Practices (includes best practices for Redo Apply)" white paper available from the MAA Best Practices area for Oracle Database at

`http://www.oracle.com/goto/maa`

## 9.6 Use Snapshot Standby Database Best Practices

Beginning with Oracle Database release 11g, you can convert a physical standby database into a fully updatable standby database called a [snapshot standby database](glossary.md).

To convert a physical standby database into a snapshot standby database, issue the SQL\*Plus `ALTER DATABASE CONVERT TO SNAPSHOT STANDBY` statement. This command causes Oracle Data Guard to perform the following actions:

1. Recover all available redo data
2. Create a guaranteed restore point
3. Activate the standby database as a primary database
4. Open the database as a snapshot standby database

To convert the snapshot standby back to a physical standby, issue the `ALTER DATABASE CONVERT TO PHYSICAL STANDBY` statement. This command causes the physical standby database to be flashed back to the guaranteed restore point that was created before the `ALTER DATABASE CONVERT TO SNAPSHOT STANDBY` statement was issued. Then, you must perform the following actions:

1. Restart the physical standby database
2. Restart Redo Apply on the physical standby database

To create and manage snapshot standby databases:

- Use the Oracle Data Guard broker to manage your Oracle Data Guard configuration, because it simplifies the management of snapshot standby databases. The broker will automatically convert a snapshot standby database into a physical standby database as part of a failover operation. Without the broker, this conversion must be manually performed before initiating a failover.
- Create multiple standby databases if your business requires a fast recovery time objective (RTO).
- Ensure the physical standby database that you convert to a snapshot standby is caught up with the primary database, or has a minimal apply lag. See Section 9.3.8, "Use Data Guard Redo Apply Best Practices" for information about tuning media recovery.
- Configure a fast recovery area and ensure there is sufficient I/O bandwidth available. This is necessary because snapshot standby databases use guaranteed restore points.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/manage_ps.htm#SBYDB00708) for complete information about creating a snapshot standby database

## 9.7 Assessing Data Guard Performance

To accurately assess the primary database performance after adding Data Guard standby databases, obtain a history of statistics from the [`V$SYSMETRIC_SUMMARY` view](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3092.htm#REFRN30345) or Automatic Workload Repository (AWR) snapshots before and after deploying Oracle Data Guard with the same application profile and load.

To assess the application profile, compare the following statistics:

- Physical reads per transaction
- Physical writes per transaction
- CPU usage per transaction
- Redo generated per transaction

To assess the application performance, compare the following statistics:

- Redo generated per second or redo rate
- User commits per second or transactions per second
- Database time per second
- Response time per transaction
- SQL service response time

If the application profile has changed between the two scenarios, then this is not a fair comparison. Repeat the test or tune the database or system with the general principles outlined in the [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm).

If the application profile is similar and you observe application performance changes on the primary database because of a decrease in throughput or an increase in response time, then assess these common problem areas:

- CPU utilization
	If you are experiencing high load (excessive CPU usage of over 90%, paging and swapping), then tune the system before proceeding with Data Guard. Use the [`V$OSSTAT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2085.htm#REFRN30321) view or the [`V$SYSMETRIC_HISTORY`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4059.htm#REFRN23451) view to monitor system usage statistics from the operating system.
- Higher I/O wait events
	If you are experiencing higher I/O waits from the log writer or database writer processes, then the slower I/O effects throughput and response time. To observe the I/O effects, look at the historical data of the following wait events:
	- `Log file parallel writes`
		- `Log file sequential reads`
		- `Log file parallel reads`
		- `Data file parallel writes`
		- `Data file sequential reads parallel writes`

With `SYNC` transport, commits take more time because of the need to guarantee that the redo data is available on the standby database before foreground processes get an acknowledgment from the log writer (LGWR) background process that the commit has completed. A LGWR process commit includes the following wait events:

- `Log File Parallel Write` (local write for the LGWR process)
- `LGWR wait on SENDREQ`
	This wait event includes:
	- Time to put the packet into the network
		- Time to send the packet to the standby database
		- RFS write or standby write to the standby redo log, which includes the RFS I/O wait event plus additional overhead for checksums
		- Time to send a network acknowledgment back to the primary database (for example, single trip latency time)

Longer commit times for the LGWR process can cause longer response time and lower throughput, especially for small time-sensitive transactions. However, you may obtain sufficient gains by tuning the log writer local write (`Log File Parallel Write` wait event) or the different components that comprise the `LGWR wait on SENDREQ` wait event.

To tune the disk write I/O (`Log File Parallel Write` or the RFS I/O), add more spindles or increase the I/O bandwidth.

To reduce the network time:

- Tune the Oracle Net send and receive buffer sizes
- Set SDU=65535 (for more information, see Section 9.3.7.2, "Set the Network Configuration and Highest Network Redo Rates")
- Increase the network bandwidth if there is saturation
- Possibly find a closer site to reduce the network latency

With `ASYNC` transport, the LGWR process never waits for the network server processes to return before writing a `COMMIT` record to the current log file. However, if the network server processes has fallen behind and the redo to be shipped has been flushed from the log buffer, then the network server process reads from the online redo logs. This causes more I/O contention and possibly longer wait times for the log writer process writes (`Log File Parallel Write`). If I/O bandwidth and sufficient spindles are not allocated, then the log file parallel writes and log file sequential reads increase, which may affect throughput and response time. In most cases, adding sufficient spindles reduces the I/O latency.

Note:

To enable most of the statistical gathering and advisors, ensure the `STATISTICS_LEVEL` initialization parameter is set to `TYPICAL` (recommended) or `ALL`.

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for general performance tuning and troubleshooting best practices
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/autostat.htm#PFGRF02601) for Overview of the Automatic Workload Repository (AWR) and on Generating Automatic Workload Repository Reports
- The MAA white paper "Data Guard Redo Transport & Network Best Practices" from the MAA Best Practices area for Oracle Database at
	`http://www.oracle.com/goto/maa`