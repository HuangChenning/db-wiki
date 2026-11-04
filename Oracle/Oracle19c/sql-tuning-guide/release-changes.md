---
title: SQL Tuning Guide
book: SQL Tuning Guide
doc_id: E96095-19
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/tgsql/release-changes.html
tags:
  - oracle
  - 19c
  - sql-tuning-guide
---

## Changes in This Release for Oracle Database SQL Tuning Guide

### Changes in Oracle Database Release 19c, Version 19.10

This section lists changes in Oracle Database Tuning Guide for Oracle Database release 19c, version 19.10.

The following initialization parameter is new in Oracle Database release 19c, version 19.6:

- `OPTIMIZER_REAL_TIME_STATISTICS`
	See [About Optimizer Initialization Parameters](influencing-the-optimizer.md)

### Changes in Oracle Database Release 19c, Version 19.6

This section lists changes in Oracle Database Tuning Guide for Oracle Database release 19c, version 19.6.

The following initialization parameter is new in Oracle Database release 19c, version 19.6:

- `OPTIMIZER_SESSION _TYPE`
	See [About Optimizer Initialization Parameters](influencing-the-optimizer.md)

### Changes in Oracle Database Release 19c, Version 19.1

Oracle Database SQL Tuning Guide for Oracle Database release 19c, version 19.1 has the following changes.

#### New Features

The following features are new in this release:

- Automatic resolution of SQL plan regressions
	SQL plan management searches for SQL statements in Automatic Workload Repository (AWR). Prioritizing by highest load, SPM Evolve Advisor looks for alternative plans in all available sources, adding better performing plans to the SQL plan baseline automatically. The automatic task runs in the maintenance window.
	See " [Automatic SQL Plan Management](managing-sql-plan-baselines.md) ".
- High-frequency SPM Evolve Advisor task
	You can configure the Automatic SPM Evolve Advisor task to run every hour, outside of the maintenance window. Consequently, the optimizer has more frequent opportunities to find and evolve better performing plans.
	See [Configuring the High-Frequency Automatic SPM Evolve Advisor Task](managing-sql-plan-baselines.md).
- Reporting on hint usage
	Oracle Database includes a hint usage reporting mechanism that reports whether hints were used during plan generation. In some cases, the report explains why a hint was not used, for example, a syntax error or conflict between hints. You can generate hint usage reports with the standard `DBMS_XPLAN` display functions.
	See " [Reporting on Hints](influencing-the-optimizer.md) ".
- Plan comparison function
	The `DBMS_XPLAN.COMPARE_PLANS` function takes a reference plan and a list of test plans and highlights the differences between them. Users can triage plan reproducibility issues by identifying the source of differences.
	See " [Comparing Execution Plans](generating-and-displaying-execution-plans.md) ".
- Real-time statistics
	Oracle Database can automatically gather real-time statistics during conventional DML operations. These statistics augment the standard statistics gathered by `DBMS_STATS` jobs.
	See " [Real-Time Statistics](optimizer-statistics-concepts.md) ".
- High-frequency automatic optimizer statistics collection
	This lightweight task periodically gathers statistics for stale objects. The default interval is 15 minutes. In contrast to the automated statistics collection job, the high-frequency task does not perform actions such as purging statistics for non-existent objects or invoking Optimizer Statistics Advisor.
	See " [Configuring High-Frequency Automatic Optimizer Statistics Collection](gathering-optimizer-statistics.md) ".
- Statistics maintenance enhancements
	Partition move, merge, and coalesce operations maintain both global and partition-level statistics.
	See " [Online Statistics Gathering](optimizer-statistics-concepts.md) ".
- Real-time SQL monitoring for developers
	Database users who do not have the `SELECT_CATALOG_ROLE` can generate and view SQL Monitor reports for their own SQL statements, including execution plans and performance metrics.
	See " [Generating and Accessing SQL Monitor Reports](monitoring-database-operations.md) ".
- Quarantine for runaway SQL statements
	Oracle Database automatically quarantines SQL statements terminated by Oracle Database Resource Manager (Resource Manager) for breaking resource limits. By putting plans on a “blacklist,” the database prevents resource-hogging statements from executing again.
	See " [About Quarantined SQL Plans](query-optimizer-concepts.md) ".
- Automatic indexing
	An automatic background task monitors system workloads, and then creates and maintains indexes suitable for the statements in the workload. The database validates the performance effects of the indexes and keeps or alters its decisions constantly to maximize performance. For example, the database might create an index on columns used in a statement predicate when the index improves query performance significantly.
	See " [Automatic Indexing](introduction-to-sql-tuning.md) ".

See Also:

[Oracle Database Licensing Information User Manual](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/tgsql&id=DBLIC-GUID-0F9EB85D-4610-4EDF-89C2-4916A0E7AC87) for details on which features are supported for different editions and services

#### Other Changes

This topic describes additional changes in the release.

The chapter on SQL Test Case Builder is now merged with the diagnosability content in [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/tgsql&id=GUID-8DEB1BE0-8FB9-4FB2-A19A-17CF6F5791C3).

### Changes in Oracle Database Release 18c, Version 18.1

Oracle Database SQL Tuning Guide for Oracle Database release 18c, version 18.1 has the following changes.

#### New Features

The following features are new in this release:

- Private temporary tables
	Private temporary tables are temporary database objects that are automatically dropped at the end of a transaction or a session. A private temporary table is stored in memory and is visible only to the session that created it. A private temporary table confines the scope of a temporary table to a session or a transaction, thus providing more flexibility in application coding, leading to easier code maintenance and a better ready-to-use functionality.
	See " [Statistics for Global Temporary Tables](optimizer-statistics-concepts.md) ".
- Approximate Top-N Query Processing
	To obtain “top n” query results much faster than traditional queries, use the `APPROX_SUM` and `APPROX_COUNT` SQL functions with `APPROX_RANK`.
	See " [About Approximate Query Processing](query-optimizer-concepts.md) ".
- SQL Tuning Advisor enhancements for Oracle Exadata Database Machine
	SQL Tuning Advisor can recommend an Exadata-aware SQL profile. On Oracle Exadata Database Machine, the cost of smart scans depends on the system statistics I/O seek time (`ioseektim`), multiblock read count (`mbrc`), and I/O transfer speed (`iotfrspeed`). The values of these statistics usually differ on Exadata and can thus influence the choice of plan. If system statistics are stale, and if gathering them improves performance, then SQL Tuning Advisor recommends accepting an Exadata-aware SQL profile.
	See " [Statistical Analysis](sql-tuning-advisor.md) " and " [Statistics in SQL Profiles](managing-sql-profiles.md) ".
- New package for managing SQL tuning sets
	You can use `DBMS_SQLSET` instead of `DBMS_SQLTUNE` to create, modify, drop, and perform all other SQL tuning set operations.
	See " [Command-Line Interface to SQL Tuning Sets](managing-sql-tuning-sets.md) ".
- Scalable sequences
	Scalable sequences alleviate index leaf block contention when loading data into tables that use sequence values as keys.
- Decoupling `OPTIMIZER_ADAPTIVE_STATISTICS` from performance feedback
	Unlike in previous releases, setting the `OPTIMIZER_ADAPTIVE_STATISTICS` initialization parameter to `TRUE` or `FALSE` now has no effect on performance feedback.