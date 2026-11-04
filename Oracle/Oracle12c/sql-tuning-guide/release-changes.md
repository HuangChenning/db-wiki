---
title: SQL Tuning Guide
book: SQL Tuning Guide
doc_id: E85762-06
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/tgsql/release-changes.html
tags:
  - oracle
  - 12c
  - sql-tuning-guide
---

This preface describes the most important changes in Oracle Database SQL Tuning Guide.

This preface contains the following topics:

### Changes in Oracle Database 12c Release 2 (12.2.0.1)

Oracle Database SQL Tuning Guide for Oracle Database 12c Release 2 (12.2.0.1) has the following changes.

#### New Features

The following features are new in this release:

- Advisor enhancements
	- Optimizer Statistics Advisor
		Optimizer Statistics Advisor is built-in diagnostic software that analyzes the quality of statistics and statistics-related tasks. The advisor task runs automatically in the maintenance window, but you can also run it on demand. You can then view the advisor report. If the advisor makes recommendations, then in some cases you can run system-generated scripts to implement them.
		See " [Analyzing Statistics Using Optimizer Statistics Advisor](optimizer-statistics-advisor.md) ".
		- Active Data Guard Support for SQL Tuning Advisor
		Using database links, you can tune a standby database workload on a primary database.
		See " [Local and Remote SQL Tuning](sql-tuning-advisor.md) ".
- `DBMS_STATS` enhancements
	- `DBMS_STATS` preference for automatic column group statistics
		If the `DBMS_STATS` preference `AUTO_STAT_EXTENSIONS` is set to `ON` (by default it is `OFF`), then a SQL plan directive can automatically trigger the creation of column group statistics based on usage of predicates in the workload.
		See " [Purpose of Optimizer Statistics Preferences](options-for-optimizer-statistics-gathering.md) ".
		- `DBMS_STATS` support for external table scan rates and In-Memory column store (IM column store) statistics
		If the database uses an IM column store, then you can set the `im_imcu_count` parameter to the number of IMCUs in the table or partition, and `im_block_count` to the number of blocks. For an external table, `scanrate` specifies the rate at which data is scanned in MB/second.
		See " [Guideline for External Tables](gathering-optimizer-statistics.md) ".
		- `DBMS_STATS` statistics preference `PREFERENCE_OVERRIDES_PARAMETER`
		The `PREFERENCE_OVERRIDES_PARAMETER` statistics preference determines whether, when gathering optimizer statistics, to override the input value of a parameter with the statistics preference. In this way, you control when the database honors a parameter value passed to the statistics gathering procedures.
		See " [Statistics Preference Overrides](options-for-optimizer-statistics-gathering.md) ".
		- Access to current statistics does not require `FLUSH_DATABASE_MONITORING_INFO`
		You no longer need to ensure that view metadata is up-to-date by using `DBMS_STATS.FLUSH_DATABASE_MONITORING_INFO` to save monitoring information to disk. The statistics shown in `DBA_TAB_STATISTICS` and `DBA_IND_STATISTICS` come from the same source as `DBA_TAB_MODIFICATIONS`, which means these views show statistics obtained from disk and memory.
		See " [Determining When Optimizer Statistics Are Stale](gathering-optimizer-statistics.md) ".
- Separate controls for adaptive plans and adaptive statistics
	The `OPTIMIZER_ADAPTIVE_PLANS` initialization parameter enables (default) or disables adaptive plans. The `OPTIMIZER_ADAPTIVE_STATISTICS` initialization parameter enables or disables (default) adaptive statistics.
	See " [When Adaptive Query Plans Are Enabled](query-optimizer-concepts.md) " and " [When Adaptive Statistics Are Enabled](query-optimizer-concepts.md) ".
- Join enhancements
	- Join groups
		A join group is a user-created object that lists two columns that can be meaningfully joined. In certain queries, join groups enable the database to eliminate the performance overhead of decompressing and hashing column values. Join groups require an IM column store.
		See " [In-Memory Join Groups](joins.md) ".
		- Band join enhancements
		A band join is a special type of nonequijoin in which key values in one data set must fall within the specified range (“band”) of the second data set. When the database detects a band join, the database evaluates the costs of band joins more efficiently, avoiding unnecessary scans of rows that fall outside the defined bands. In most cases, optimized performance is comparable to an equijoin.
		See " [Band Joins](joins.md) ".
- Cursor management enhancements
	- Cursor-duration temporary tables
		To materialize the intermediate results of a query, Oracle Database may create a cursor-duration temporary table in memory during query compilation. For complex operations such as `WITH` clause queries and star transformations, this internal optimization, which enhances the materialization of intermediate results from repetitively used subqueries, improves performance and optimizes I/O.
		See " [Cursor-Duration Temporary Tables](query-transformations.md) ".
		- Fine-grained cursor invalidation
		Starting in this release, you can specify deferred invalidation on DDL statements. When shared SQL areas are marked rolling invalid, the database assigns each one a randomly generated time period. A hard parse occurs only if the query executes after the time period has expired. In this way, the database can diffuse the performance overhead of hard parsing over time.
		See " [About the Life Cycle of Shared Cursors](improving-rwp-cursor-sharing.md) ".
- `OR` expansion enhancement
	In previous releases, the optimizer used the `CONCATENATION` operator to perform the `OR` expansion. Now the optimizer uses the `UNION-ALL` operator instead. This enhancement provides several benefits, including enabling interaction among various transformations, and avoiding the sharing of query structures.
	See " [OR Expansion](query-transformations.md) ".
- SQL plan management enhancements
	- You can now capture plans from AWR. See " [Manual Plan Capture](overview-of-sql-plan-management.md) ".
		- In previous releases, automatic capture applied to all repeatable queries. Starting in this release, you can create filters to capture only the plans for statements that you choose. See " [Eligibility for Automatic Initial Plan Capture](overview-of-sql-plan-management.md) ".
- Real-Time database operation monitoring enhancements
	A session can start or stop a database operation in a different session by specifying its session ID and serial number.
	See " [Defining a Composite Database Operation](monitoring-database-operations.md) ".
- Expression tracking
	SQL statements commonly include expressions such as plus (`+`) or minus (`-`). More complicated examples include PL/SQL functions or SQL functions such as `LTRIM` and `TO_NUMBER`. The Expression Statistics Store (ESS) maintains usage information about expressions identified during compilation and captured during execution.
	See " [About the Expression Statistics Store (ESS)](query-optimizer-concepts.md) ".
- Enhancements for application tracing in a multitenant environment
	CDB administrators and PDB administrators can use new `V$` views to access trace data that is relevant for a specific PDB.
	See " [End-to-End Application Tracing in a Multitenant Environment](performing-application-tracing.md) ".

#### Desupported Features

The following features are desupported in Oracle Database 12c Release 2 (12.2.0.1).

- The `OPTIMIZER_ADAPTIVE_FEATURES` initialization parameter

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=UPGRD60000) for a list of desupported features

#### Other Changes

This topic describes additional changes in the release.

- New Real-World Performance content
	In this release, the book incorporates information provided by the Real-World Performance group, including the following:
	- " [Improving Real-World Performance Through Cursor Sharing](improving-rwp-cursor-sharing.md) " explains how to use bind variables and new features such as adaptive cursor sharing

### Changes in Oracle Database 12c Release 1 (12.1.0.2)

Oracle Database SQL Tuning Guide for Oracle Database 12c Release 1 (12.1.0.2) has the following changes.

#### New Features

The following features are new in this release.

- In-Memory aggregation
	This optimization minimizes the join and `GROUP BY` processing required for each row when joining a single large table to multiple small tables, as in a star schema. `VECTOR` `GROUP BY` aggregation uses the infrastructure related to parallel query (PQ) processing, and blends it with CPU-efficient algorithms to maximize the performance and effectiveness of the initial aggregation performed before redistributing fact data.
	See " [In-Memory Aggregation (VECTOR GROUP BY)](query-transformations.md) ".
- SQL Monitor support for adaptive query plans
	SQL Monitor supports adaptive query plans in the following ways:
	- Indicates whether a query plan is adaptive, and show its current status: resolving or resolved.
		- Provides a list that enables you to select the current, full, or final query plans
		See " [Adaptive Query Plans](query-optimizer-concepts.md) " to learn more about adaptive query plans, and " [Monitoring SQL Executions Using Cloud Control](monitoring-database-operations.md) " to learn more about SQL Monitor.

### Changes in Oracle Database 12c Release 1 (12.1.0.1)

Oracle Database SQL Tuning Guide for Oracle Database 12c Release 1 (12.1) has the following changes.

#### New Features

The following features are new in this release.

- Adaptive SQL Plan Management (SPM)
	The SPM Evolve Advisor is a task infrastructure that enables you to schedule an evolve task, rerun an evolve task, and generate persistent reports. The new automatic evolve task, `SYS_AUTO_SPM_EVOLVE_TASK`, runs in the default maintenance window. This task ranks all unaccepted plans and runs the evolve process for them. If the task finds a new plan that performs better than existing plan, the task automatically accepts the plan. You can also run evolution tasks manually using the `DBMS_SPM` package.
	See " [Managing the SPM Evolve Advisor Task](managing-sql-plan-baselines.md) ".
- Adaptive query optimization
	Adaptive query optimization is a set of capabilities that enable the optimizer to make run-time adjustments to execution plans and discover additional information that can lead to better statistics. The set of capabilities include:
	- Adaptive query plans
		An [adaptive query plan](glossary.md) has built-in options that enable the [final plan](glossary.md) for a statement to differ from the [default plan](glossary.md). During the first execution, before a specific subplan becomes active, the optimizer makes a final decision about which option to use. The optimizer bases its choice on observations made during the execution up to this point. The ability of the optimizer to adapt plans can improve query performance.
		See " [Adaptive Query Plans](query-optimizer-concepts.md) ".
		- Automatic reoptimization
		When using [automatic reoptimization](glossary.md), the optimizer monitors the initial execution of a query. If the actual execution statistics vary significantly from the original plan statistics, then the optimizer records the execution statistics and uses them to choose a better plan the next time the statement executes. The database uses information obtained during automatic reoptimization to generate SQL plan directives automatically.
		See " [Automatic Reoptimization](query-optimizer-concepts.md) ".
		- SQL plan directives
		In releases earlier than Oracle Database 12c, the database stored compilation and execution statistics in the shared SQL area, which is nonpersistent. Starting in this release, the database can use a [SQL plan directive](glossary.md), which is additional information and instructions that the optimizer can use to generate a more optimal plan. The database stores SQL plan directives persistently in the `SYSAUX` tablespace. When generating an execution plan, the optimizer can use SQL plan directives to obtain more information about the objects accessed in the plan.
		See " [SQL Plan Directives](optimizer-statistics-concepts.md) ".
		- Dynamic statistics enhancements
		In releases earlier than Oracle Database 12c, Oracle Database only used dynamic statistics (previously called dynamic sampling) when one or more of the tables in a query did not have optimizer statistics. Starting in this release, the optimizer automatically decides whether dynamic statistics are useful and which dynamic statistics level to use for all SQL statements. Dynamic statistics gathers are persistent and usable by other queries.
		See " [Supplemental Dynamic Statistics](optimizer-statistics-concepts.md) ".
- New types of histograms
	This release introduces top frequency and hybrid histograms. If a column contains more than 254 distinct values, and if the top 254 most frequent values occupy more than 99% of the data, then the database creates a [top frequency histogram](glossary.md) using the top 254 most frequent values. By ignoring the nonpopular values, which are statistically insignificant, the database can produce a better quality histogram for highly popular values. A [hybrid histogram](glossary.md) is an enhanced height-based histogram that stores the exact frequency of each endpoint in the sample, and ensures that a value is never stored in multiple buckets.
	Also, regular frequency histograms have been enhanced. The optimizer computes frequency histograms during NDV computation based on a full scan of the data rather than a small sample (when `AUTO_SAMPLING` is used). The enhanced frequency histograms ensure that even highly infrequent values are properly represented with accurate bucket counts within a histogram.
	See " [Histograms](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/tgsql/histograms.html#GUID-BE10EBFC-FEFC-4530-90DF-1443D9AD9B64 "A histogram is a special type of column statistic that provides more detailed information about the data distribution in a table column. A histogram sorts values into \"buckets,\" as you might sort coins into buckets.") ".
- Monitoring database operations
	Real-Time Database Operations Monitoring enables you to monitor long running database tasks such as batch jobs, scheduler jobs, and Extraction, Transformation, and Loading (ETL) jobs as a composite business operation. This feature tracks the progress of SQL and PL/SQL queries associated with the business operation being monitored. As a DBA or developer, you can define business operations for monitoring by explicitly specifying the start and end of the operation or implicitly with tags that identify the operation.
	See " [Monitoring Database Operations](monitoring-database-operations.md) ".
- Concurrent statistics gathering
	You can concurrently gather optimizer statistics on multiple tables, table partitions, or table subpartitions. By fully utilizing multiprocessor environments, the database can reduce the overall time required to gather statistics. Oracle Scheduler and Advanced Queuing create and manage jobs to gather statistics concurrently. The scheduler decides how many jobs to execute concurrently, and how many to queue based on available system resources and the value of the `JOB_QUEUE_PROCESSES` initialization parameter.
	See " [Gathering Optimizer Statistics Concurrently](gathering-optimizer-statistics.md) ".
- Reporting mode for `DBMS_STATS` statistics gathering functions
	You can run the `DBMS_STATS` functions in reporting mode. In this mode, the optimizer does not actually gather statistics, but reports objects that would be processed if you were to use a specified statistics gathering function.
	See " [Running Statistics Gathering Functions in Reporting Mode](gathering-optimizer-statistics.md) ".
- Reports on past statistics gathering operations
	You can use `DBMS_STATS` functions to report on a specific statistics gathering operation or on operations that occurred during a specified time.
	See " [Reporting on Past Statistics Gathering Operations](managing-historical-optimizer-statistics.md) ".
- Automatic column group creation
	With [column group statistics](glossary.md), the database gathers optimizer statistics on a group of columns treated as a unit. Starting in Oracle Database 12c, the database automatically determines which column groups are required in a specified workload or SQL tuning set, and then creates the column groups. Thus, for any specified workload, you no longer need to know which columns from each table must be grouped.
	See " [Detecting Useful Column Groups for a Specific Workload](managing-extended-statistics.md) ".
- Session-private statistics for global temporary tables
	Starting in this release, global temporary tables have a different set of optimizer statistics for each session. Session-specific statistics improve performance and manageability of temporary tables because users no longer need to set statistics for a global temporary table in each session or rely on dynamic statistics. The possibility of errors in cardinality estimates for global temporary tables is lower, ensuring that the optimizer has the necessary information to determine an optimal execution plan.
	See " [Session-Specific Statistics for Global Temporary Tables](optimizer-statistics-concepts.md) ".
- SQL Test Case Builder enhancements
	SQL Test Case Builder can capture and replay actions and events that enable you to diagnose incidents that depend on certain dynamic and volatile factors. This capability is especially useful for parallel query and automatic memory management.
	See [Gathering Diagnostic Data with SQL Test Case Builder](sql-test-case-builder.md).
- Online statistics gathering for bulk loads
	A [bulk load](glossary.md) is a `CREATE TABLE AS SELECT` or `INSERT INTO ... SELECT` operation. In releases earlier than Oracle Database 12c, you needed to manually gather statistics after a bulk load to avoid the possibility of a suboptimal execution plan caused by stale statistics. Starting in this release, Oracle Database gathers optimizer statistics automatically, which improves both performance and manageability.
	See " [Online Statistics Gathering for Bulk Loads](optimizer-statistics-concepts.md) ".
- Reuse of synopses after partition maintenance operations
	`ALTER TABLE EXCHANGE` is a common partition maintenance operation. During a partition exchange, the statistics of the partition and the table are also exchanged. A [synopsis](glossary.md) is a set of auxiliary statistics gathered on a partitioned table when the `INCREMENTAL` value is set to `true`. In releases earlier than Oracle Database 12c, you could not gather table-level synopses on a table. Thus, you could not gather table-level synopses on a table, exchange the table with a partition, and end up with synopses on the partition. You had to explicitly gather optimizer statistics in incremental mode to create the missing synopses. Starting in this release, you can gather table-level synopses on a table. When you exchange this table with a partition in an incremental mode table, the synopses are also exchanged.
	See " [Maintaining Incremental Statistics for Partition Maintenance Operations](gathering-optimizer-statistics.md) ".
- Automatic updates of global statistics for tables with stale or locked partition statistics
	Incremental statistics can automatically calculate global statistics for a partitioned table even if the partition or subpartition statistics are stale and locked.
	See " [Maintaining Incremental Statistics for Tables with Stale or Locked Partition Statistics](gathering-optimizer-statistics.md) ".
- Cube query performance enhancements
	These enhancements minimize CPU and memory consumption and reduce I/O for queries against cubes.
	See [Table 7-7](reading-execution-plans.md) to learn about the `CUBE JOIN` operation.

#### Deprecated Features

The following features are deprecated in this release, and may be desupported in a future release.

- Stored outlines
	See " [Managing SQL Plan Baselines](managing-sql-plan-baselines.md) " for information about alternatives.
- The `SIMILAR` value for the `CURSOR_SHARING` initialization parameter
	This value is deprecated. Use `FORCE` instead.
	See " [Do Not Use CURSOR\_SHARING = FORCE as a Permanent Fix](improving-rwp-cursor-sharing.md) ".

#### Desupported Features

Some features previously described in this document are desupported in Oracle Database 12c.

See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=UPGRD60000) for a list of desupported features.

#### Other Changes

The following are additional changes in the release.

- New tuning books
	The Oracle Database 11g Oracle Database Performance Tuning Guide has been divided into two books for Oracle Database 12c:
	- Oracle Database Performance Tuning Guide, which contains only topics that pertain to tuning the database
		- Oracle Database SQL Tuning Guide, which contains only topics that pertain to tuning SQL