---
title: Apply Services
book: Data Guard Concepts and Administration
doc_id: E41134-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41134/log_apply.htm
tags:
  - oracle
  - 11g
  - data-guard-concepts-and-administration
---

## 7 Apply Services

This chapter describes how redo data is applied to a standby database. It includes the following topics:

## 7.1 Introduction to Apply Services

Apply services automatically apply redo to standby databases to maintain synchronization with the primary database and allow transactionally consistent access to the data.

By default, apply services waits for a standby redo log file to be archived before applying the redo that it contains. However, you can enable real-time apply, which allows apply services to apply the redo in the current standby redo log file as it is being filled. Real-time apply is described in more detail in Section 7.2.1.

Apply services use the following methods to maintain physical and logical standby databases:

- Redo Apply (physical standby databases only)
	Uses media recovery to keep the primary and physical standby databases synchronized.
- SQL Apply (logical standby databases only)
	Reconstitutes SQL statements from the redo received from the primary database and executes the SQL statements against the logical standby database.

The sections in this chapter describe Redo Apply, SQL Apply, real-time apply, and delayed apply in more detail.

## 7.2 Apply Services Configuration Options

This section contains the following topics:

- Using Real-Time Apply to Apply Redo Data Immediately
- Specifying a Time Delay for the Application of Archived Redo Log Files

### 7.2.1 Using Real-Time Apply to Apply Redo Data Immediately

If the real-time apply feature is enabled, apply services can apply redo data as it is received, without waiting for the current standby redo log file to be archived. This results in faster switchover and failover times because the standby redo log files have been applied already to the standby database by the time the failover or switchover begins.

Use the `ALTER DATABASE` statement to enable the real-time apply feature, as follows:

- For physical standby databases, issue the `ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE` statement.
- For logical standby databases, issue the `ALTER DATABASE START LOGICAL STANDBY APPLY IMMEDIATE` statement.

Real-time apply requires a standby database that is configured with a standby redo log and that is in ARCHIVELOG mode.

Figure 7-1 shows a Data Guard configuration with a local destination and a standby destination. As the remote file server (RFS) process writes the redo data to standby redo log files on the standby database, apply services can recover redo from standby redo log files as they are being filled.

Figure 7-1 Applying Redo Data to a Standby Destination Using Real-Time Apply

![Figure 7-1 Applying Redo Data to a Standby Destination Using Real-Time Apply](img/sbydb049.gif)

> The illustration is described in the paragraph preceding the figure.
>
> Copyright © 1999, 2014, Oracle and/or its affiliates. All rights reserved.  
> [Legal Notices](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

### 7.2.2 Specifying a Time Delay for the Application of Archived Redo Log Files

In some cases, you may want to create a time lag between the time when redo data is received from the primary site and when it is applied to the standby database. You can specify a time interval (in minutes) to protect against the application of corrupted or erroneous data to the standby database. When you set a `DELAY` interval, it does not delay the transport of the redo data to the standby database. Instead, the time lag you specify begins when the redo data is completely archived at the standby destination.

Note:

If you define a delay for a destination that has real-time apply enabled, the delay is ignored.

Specifying a Time Delay

You can set a time delay on primary and standby databases using the `DE` `LAY=` `minutes` attribute of the `LOG_ARCHIVE_DEST_` `n` initialization parameter to delay applying archived redo log files to the standby database. By default, there is no time delay. If you specify the `DELAY` attribute without specifying a value, then the default delay interval is 30 minutes.

Canceling a Time Delay

You can cancel a specified delay interval as follows:

- For physical standby databases, use the `NODELAY` keyword of the `RECOVER MANAGED STANDBY DATABASE` clause:
	```
	SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE NODELAY;
	```
- For logical standby databases, specify the following SQL statement:
	```
	SQL> ALTER DATABASE START LOGICAL STANDBY APPLY NODELAY;
	```

These commands result in apply services immediately beginning to apply archived redo log files to the standby database, before the time interval expires.

#### 7.2.2.1 Using Flashback Database as an Alternative to Setting a Time Delay

As an alternative to setting an apply delay, you can use Flashback Database to recover from the application of corrupted or erroneous data to the standby database. Flashback Database can quickly and easily flash back a standby database to an arbitrary point in time.

See [Chapter 13](scenarios.md) for scenarios showing how to use Data Guard with Flashback Database, and [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for more information about enabling and using Flashback Database.

## 7.3 Applying Redo Data to Physical Standby Databases

By default, the redo data is applied from archived redo log files. When performing Redo Apply, a physical standby database can use the real-time apply feature to apply redo directly from the standby redo log files as they are being written by the RFS process.

This section contains the following topics:

- Starting Redo Apply
- Stopping Redo Apply
- Monitoring Redo Apply on Physical Standby Databases

### 7.3.1 Starting Redo Apply

To start apply services on a physical standby database, ensure the physical standby database is started and mounted and then start Redo Apply using the SQL `ALTER DATABASE RECOVER MANAGED STANDBY DATABASE` statement.

You can specify that Redo Apply runs as a foreground session or as a background process, and enable it with real-time apply.

- To start Redo Apply in the foreground, issue the following SQL statement:
	```
	SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE;
	```
	If you start a foreground session, control is not returned to the command prompt until recovery is canceled by another session.
- To start Redo Apply in the background, include the `DISCONNECT` keyword on the SQL statement. For example:
	```
	SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE DISCONNECT;
	```
	This statement starts a detached server process and immediately returns control to the user. While the managed recovery process is performing recovery in the background, the foreground process that issued the `RECOVER` statement can continue performing other tasks. This does not disconnect the current SQL session.
- To start real-time apply, include the `USING CURRENT LOGFILE` clause on the SQL statement. For example:
	```
	SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE;
	```

### 7.3.2 Stopping Redo Apply

To stop Redo Apply, issue the following SQL statement:

```
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE CANCEL;
```

### 7.3.3 Monitoring Redo Apply on Physical Standby Databases

To monitor the status of apply services on a physical standby database, see [Section 9.5.1](manage_ps.md). You can also monitor the standby database using Oracle Enterprise Manager. Also, see the [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for complete reference information about views.

## 7.4 Applying Redo Data to Logical Standby Databases

SQL Apply converts the data from the archived redo log or standby redo log into SQL statements and then executes these SQL statements on the logical standby database. Because the logical standby database remains open, tables that are maintained can be used simultaneously for other tasks such as reporting, summations, and queries.

This section contains the following topics:

- Starting SQL Apply
- Stopping SQL Apply on a Logical Standby Database
- Monitoring SQL Apply on Logical Standby Databases

### 7.4.1 Starting SQL Apply

To start SQL Apply, start the logical standby database and issue the following statement:

```
SQL> ALTER DATABASE START LOGICAL STANDBY APPLY;
```

To start real-time apply on the logical standby database to immediately apply redo data from the standby redo log files on the logical standby database, include the `IMMEDIATE` keyword as shown in the following statement:

```
SQL>  ALTER DATABASE START LOGICAL STANDBY APPLY IMMEDIATE;
```

### 7.4.2 Stopping SQL Apply on a Logical Standby Database

To stop SQL Apply, issue the following statement on the logical standby database:

```
SQL> ALTER DATABASE STOP LOGICAL STANDBY APPLY;
```

When you issue this statement, SQL Apply waits until it has committed all complete transactions that were in the process of being applied. Thus, this command may not stop the SQL Apply processes immediately.

### 7.4.3 Monitoring SQL Apply on Logical Standby Databases

To monitor SQL Apply, see [Section 10.3](manage_ls.md). You can also monitor the standby database using Oracle Enterprise Manager. See [Appendix A, "Troubleshooting Data Guard"](troubleshooting.md) and [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/toc.htm).