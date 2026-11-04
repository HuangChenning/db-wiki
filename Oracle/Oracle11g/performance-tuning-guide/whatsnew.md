---
title: "What's New in Oracle Database Performance Tuning Guide?"
book: Performance Tuning Guide
doc_id: E41573-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41573/whatsnew.htm
tags:
  - oracle
  - 11g
  - performance-tuning-guide
---

This section describes new performance tuning features of Oracle Database 11g Release 2 (11.2) and provides pointers to additional information. The features and enhancements described in this section comprise the overall effort to optimize database performance.

For a summary of all new features for Oracle Database 11g Release 2 (11.2), see [Oracle Database New Features Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41360/toc.htm).

## Oracle Database 11g Release 2 (11.2.0.4) New Features in Oracle Database Performance

The new and updated performance tuning features include:

- Dynamic statistics enhancements
	In previous releases, Oracle Database only gathered dynamic statistics (previously called dynamic sampling) when one or more of the tables in a query did not have optimizer statistics. Starting in Oracle Database 11g Release 2 (11.2.0.4), the optimizer can automatically decide whether dynamic statistics are useful and which dynamic statistics level to use for all SQL statements. For example, the optimizer automatically decides whether to gather dynamic statistics during table scans, index access, joins, and `GROUP BY` operations. The enhanced behavior is enabled only when the `OPTIMIZER_DYNAMIC_SAMPLING` initialization parameter is set to the new value of `11`.
	See ["Controlling Dynamic Statistics"](stats.md).

## Oracle Database 11g Release 2 (11.2.0.2) New Features in Oracle Database Performance

The new and updated performance tuning features include:

- Resource Manager enhancements for parallel statement queuing
	You can use Resource Manager to control the order of statements in a parallel statement queue. For example, you can ensure that high-priority statements spend less time in the queue. Also, you can use a directive to prevent one consumer group from monopolizing all of the parallel servers, and to specify the maximum time in seconds that a parallel statement can wait to be launched.
	For more information, see ["Managing CPU Resources Using Oracle Database Resource Manager"](os.md) and [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/parallel002.htm#VLDBG1396).
- Resource Manager enhancements for CPU utilization limit
	You can use Resource Manager to limit the CPU consumption of a consumer group. This feature restricts the CPU consumption of low-priority sessions and can help provide more consistent performance for the workload in a consumer group.
	For more information, see ["Managing CPU Resources Using Oracle Database Resource Manager"](os.md).
- New package for Automatic SQL Tuning
	The `DBMS_AUTO_SQLTUNE` package is the new interface for managing the Automatic SQL Tuning task. Unlike the SQL Tuning Advisor package `DBMS_SQLTUNE`, which requires `ADVISOR` privileges, `DBMS_AUTO_SQLTUNE` requires the `DBA` role.
	For more information, see ["Configuring Automatic SQL Tuning"](sql_tune.md).
- Oracle Orion I/O Calibration Tool Documentation
	Oracle Orion is a tool for predicting the performance of an Oracle database without having to install Oracle or create a database. Unlike other I/O calibration tools, Oracle Orion is expressly designed for simulating Oracle database I/O workloads using the same I/O software stack as Oracle. Orion can also simulate the effect of striping performed by Oracle Automatic Storage Management.
	For more information, see ["I/O Calibration with the Oracle Orion Calibration Tool"](iodesign.md).

## Oracle Database 11g Release 2 (11.2.0.1) New Features in Oracle Database Performance

The new and updated performance tuning features include:

- New Automatic Workload Repository (AWR) views
	AWR supports several new historical views, including `DBA_HIST_DB_CACHE_ADVICE` and `DBA_HIST_IOSTAT_DETAIL`.
	For more information, see ["Using Automatic Workload Repository Views"](autostat.md).
- New Automatic Workload Repository reports
	New AWR reports and AWR Compare Periods reports have been added for Oracle Real Application Clusters (Oracle RAC).
	For more information, see ["Generating Automatic Workload Repository Reports"](autostat.md) and ["Generating Automatic Workload Repository Compare Periods Reports"](autostat.md).
- Table annotation support for the client result cache
	The client result cache supports table annotations.
	For more information, see ["Using Result Cache Table Annotations"](memory.md).
- Enhancement to the `RESULT_CACHE` annotation for PL/SQL functions
	In Oracle Database 11g Release 1 (11.1), PL/SQL functions that performed queries referencing annotated tables required the `RELIES_ON` clause. This clause has been deprecated and is no longer required.
- Hints specifying parallelism at the statement level
	The scope of the parallel hints has been extended to include the statement level.
	For more information, see ["Hints for Parallel Execution"](hintsref.md).
- In-Memory Parallel Execution
	When using parallel query, you can configure the database to use the database buffer cache instead of performing direct reads into the PGA for a SQL statement. This configuration may be appropriate when database servers have a large amount of memory. Also, an Oracle Real Applications Cluster (Oracle RAC) database can aggregate the size of the buffer cache of all nodes, thereby caching larger objects and caching more queries.
	For more information, see ["Using the Buffer Cache Effectively"](memory.md).
- Hints for online application upgrades
	The online application upgrade hints suggest how to handle conflicting `INSERT` and `UPDATE` operations when performing an online application upgrade using edition-based redefinition. For more information, see ["Hints for Online Application Upgrade"](hintsref.md).
- SQL Tuning Advisor enhancements
	This release includes the following enhancements to SQL Tuning Advisor:
	- While tuning a SQL statement, SQL Tuning Advisor searches real-time and historical performance data for alternative execution plans for the statement. If plans other than the original plan exist, then SQL Tuning Advisor reports an alternative plan finding. See ["Alternative Plan Analysis"](sql_tune.md).
		- You can transport a SQL tuning set to any database created in Oracle Database 10g (Release 2) or later. This technique is useful when using SQL Performance Analyzer to tune regressions on a test database. See ["Transporting a SQL Tuning Set"](sql_tune.md).
		- Sometimes SQL Tuning Advisor may recommend accepting a profile that uses the Automatic Degree of Parallelism (Auto DOP) feature. A parallel query profile is only recommended when the original plan is serial and when parallel execution can significantly reduce the elapsed time for a long-running query. See ["SQL Profile Recommendations"](sql_tune.md).
- Migrating stored outlines to SQL plan baselines
	Oracle Database enables you to safely migrate from stored outlines to SQL plan baselines. After the migration, you can maintain the same plan stability you had using stored outlines while being able to utilize the more advanced features provided by the SQL Plan Management framework. For more information, see ["Migrating Stored Outlines to SQL Plan Baselines"](optplanmgmt.md).