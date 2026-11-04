---
title: "2 Day + Performance Tuning Guide"
book: "2 Day + Performance Tuning Guide"
doc_id: F32092-02
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/tdppt/changes-in-this-release.html
tags:
  - oracle
  - 21c
  - 2-day-performance-tuning-guide
---

This preface contains:

### Changes in Oracle Database Release 19c, Version 19.1

The following are the changes in Oracle Database 2 Day + Performance Tuning Guide for Oracle Database release 19c, version 19.1.

#### New Features

The following features are new in this release:

- Automatic Database Diagnostic Monitor (ADDM) support for pluggable databases (PDBs)
	You can now use ADDM to analyze AWR data in PDBs for identifying and resolving performance related issues.
	See " [ADDM for a Multitenant Environment](automatic-database-performance-monitoring.md) " for more information.
- Real-time SQL monitoring functionality enabled for non-administrative database users
	The database users without the administrative privileges can also now view the execution plans and performance metrics of their SQL statements by navigating to the Monitored SQL Executions page of Oracle Enterprise Manager Cloud Control (Cloud Control).
	See the section " [Monitoring Database Operations in Cloud Control](monitoring-real-time-database-operations.md) " for more information.

#### Desupported Features

The following feature is desupported in this release.

- Oracle Streams
	Starting in Oracle Database 19c, the Oracle Streams feature is desupported. Use Oracle GoldenGate to replace all replication features of Oracle Streams.

### Changes in Oracle Database Release 18c, Version 18.1

There are no changes in Oracle Database 2 Day + Performance Tuning Guide for Oracle Database release 18c, version 18.1. For the Oracle Database performance related features that are new in this release, see [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=TGDBA-GUID-2849E6FD-0B81-4200-8E78-E525E9DDE197) and [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=TGSQL-GUID-144C43B5-FC35-4AB6-88C2-4C5DC6319ADA).

### Changes in Oracle Database 12c Release 2 (12.2)

There are no changes in Oracle Database 2 Day + Performance Tuning Guide for Oracle Database 12c Release 2 (12.2). For the Oracle Database performance related features that are new in this release, see [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=TGDBA-GUID-4699EF9B-1269-41D2-81DE-73371680BA37).

### Changes in Oracle Database 12c Release 1 (12.1.0.2)

The following are changes in Oracle Database 2 Day + Performance Tuning Guide for Oracle Database 12c Release 1 (12.1.0.2).

#### New Features

The following features are new in this release:

- Manageability support for In-Memory Column Store
	The new Oracle Database In-Memory Column Store (IM column store) feature accelerates database performance of analytics, data warehousing, and online transaction processing (OLTP) applications.
	SQL Monitor report, ASH report, and AWR report now show statistics for various in-memory operations.
	- In-memory statistics in SQL Monitor report: Activity % in Time and Wait Statistics panel, Activity column in Plan Statistics table, and Activity tab in SQL Monitor report show CPU consumed by SQL commands while executing in-memory query operations. SQL Monitor report now supports Adaptive plans. The Execution plan shows Resolving or Resolved icon depending upon the current status of that plan. The Plan Statistics tab contains a drop down list to show current plan, final plan, and full plan. It also contains Plan Note button, which when clicked, shows the notes that are generated in the explain plan for the SQL statement.
		- In-memory statistics in ASH report: ASH report header table shows the size of in-memory pool under In Memory Area column. Top Events, Top SQL, and Activity Over Time sections show CPU consumption by various in-memory operations.
		- In-memory statistics in AWR report: AWR report contains a new section - In-Memory Segments Statistics - that shows in-memory segment consumption based on various attributes, such as, scans, DB block changes, populate CUs, and repopulate CUs. Time Model Statistics section shows statistics related to in-memory CPU usage and Instance Activity Statistics section shows statistics related to in-memory activities.

#### Other Changes

The following are additional changes in the release:

- Changes in ASH Analytics page
	In the Average Active Sessions chart on ASH analytics page, you can now click on CPU wait class to see its breakdown by CPU usage based on various in-memory operations as well as total CPU used for operations other than in-memory operations.
	See " [Determining the Cause of Spikes in Database Activity](monitoring-real-time-database-performance.md) " for more information.

### Changes in Oracle Database 12c Release 1 (12.1.0.1)

The following are changes in Oracle Database 2 Day + Performance Tuning Guide for Oracle Database 12c Release 1 (12.1.0.1).

#### New Features

The following features are new in this release:

- Real-time database operations monitoring
	Real-Time database operations monitoring tracks and reports on active and recently completed database operations. You can monitor details of the execution of a single SQL or PL/SQL statement. You can also monitor the progress of long-running operations such as a batch job, or extract, transform, and load (ETL) processing.
	See " [Monitoring Real-Time Database Operations](monitoring-real-time-database-operations.md) " for information on this feature.

#### Desupported Features

Oracle Enterprise Manager Database Control is no longer supported by Oracle.

#### Other Changes

The following are additional changes in the release:

- Oracle Enterprise Manager Cloud Control
	In previous releases of Oracle Database, you used Oracle Enterprise Manager Database Control (Database Control) to manage database performance tuning from a graphical user interface. In this release, you can use the Oracle Enterprise Manager Cloud Control (Cloud Control) graphical user interface. Cloud Control provides more functionality than Database Control. The procedures in this guide use Cloud Control.
	You must install Cloud Control separately from Oracle Database.
	See Also:
	[Oracle Enterprise Manager Cloud Control Basic Installation Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tdppt&id=EMBSC)
- ASH Analytics page
	Cloud Control has the ASH Analytics page, which graphically displays recent Active Session History information.
	See " [Determining the Cause of Spikes in Database Activity](monitoring-real-time-database-performance.md) " for more information.
- Real-Time ADDM
	Cloud Control has the Real-Time ADDM page, from which you can run automatic database diagnostic monitoring in real time to diagnose problems with a slow or hung database.
	See " [Diagnosing Serious Performance Problems in Real Time](unresolvable-reference.md) " for more information.