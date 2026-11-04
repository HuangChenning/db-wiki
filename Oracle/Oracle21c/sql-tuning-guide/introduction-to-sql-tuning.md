---
title: SQL Tuning Guide
book: SQL Tuning Guide
doc_id: F31828-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/tgsql/introduction-to-sql-tuning.html
tags:
  - oracle
  - 21c
  - sql-tuning-guide
---

SQL tuning is the attempt to diagnose and repair SQL statements that fail to meet a performance standard.

### 1.1 Changes in Oracle Database Release 21c for SQL Tuning Guide

The following features are new in this release:

- Session-level controls for automatic indexing
	By setting the `OPTIMIZER_SESSION_TYPE` initialization parameter to `ADHOC` in a session, you can suspend automatic indexing for queries in this session. The automatic indexing process does not identify index candidates, or create and verify indexes. This control may be useful for ad hoc queries or testing new functionality.
	See " Automatic Indexing ".
- Controls for enabling or disabling the gathering of real-time statistics.
	When the `OPTIMIZER_REAL_TIME_STATISTICS` initialization parameter is set to `true`, Oracle Database automatically gathers real-time statistics during conventional DML operations. The default setting is `false`, which means real-time statistics are disabled.
- Additional controls for SQL Quarantine
	To enable SQL Quarantine to create configurations automatically after the Resource Manager terminates a query, set the `OPTIMIZER_CAPTURE_SQL_QUARANTINE` initialization parameter to `TRUE` (the default is `FALSE`). To disable the use of existing SQL Quarantine configurations, set `OPTIMIZER_USE_SQL_QUARANTINE` to `FALSE` (the default is `TRUE`).

### 1.2 About SQL Tuning

SQL tuning is the iterative process of improving SQL statement performance to meet specific, measurable, and achievable goals.

SQL tuning implies fixing problems in deployed applications. In contrast, application design sets the security and performance goals before deploying an application.

See Also:

- [SQL Performance Methodology](sql-performance-methodology.md)
- " [Guidelines for Designing Your Application](sql-performance-methodology.md) " to learn how to design for SQL performance

### 1.3 Purpose of SQL Tuning

A SQL statement becomes a problem when it fails to perform according to a predetermined and measurable standard.

After you have identified the problem, a typical tuning session has one of the following goals:

- Reduce [user response time](glossary.md), which means decreasing the time between when a user issues a statement and receives a response
- Improve [throughput](glossary.md), which means using the least amount of resources necessary to process all rows accessed by a statement

For a response time problem, consider an online book seller application that hangs for three minutes after a customer updates the shopping cart. Contrast with a three-minute [parallel query](glossary.md) in a data warehouse that consumes all of the database host CPU, preventing other queries from running. In each case, the user response time is three minutes, but the cause of the problem is different, and so is the tuning goal.

### 1.4 Prerequisites for SQL Tuning

SQL performance tuning requires a foundation of database knowledge.

If you are tuning SQL performance, then this manual assumes that you have the knowledge and skills shown in the following table.

Table 1-1 Required Knowledge

| Required Knowledge | Description | To Learn More |
| --- | --- | --- |
| Database architecture | Database architecture is not the domain of administrators alone. As a developer, you want to develop applications in the least amount of time against an Oracle database, which requires exploiting the database architecture and features. For example, not understanding Oracle Database concurrency controls and multiversioning read consistency may make an application corrupt the integrity of the data, run slowly, and decrease scalability. | [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=CNCPT015) explains the basic relational data structures, transaction management, storage structures, and instance architecture of Oracle Database. |
| SQL and PL/SQL | Because of the existence of GUI-based tools, it is possible to create applications and administer a database without knowing SQL. However, it is impossible to tune applications or a database without knowing SQL. | [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=CNCPT015) includes an introduction to Oracle SQL and PL/SQL. You must also have a working knowledge of [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=SQLRF001), [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=LNPLS001), and [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=ARPLS001). |
| SQL tuning tools | The database generates performance statistics, and provides SQL tuning tools that interpret these statistics. | [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=GUID-30B13942-F6D7-4958-8D07-762EBD0C61F2) provides an introduction to the principal SQL tuning tools. |

### 1.5 Tasks and Tools for SQL Tuning

After you have identified the goal for a tuning session, for example, reducing user response time from three minutes to less than a second, the problem becomes how to accomplish this goal.

#### 1.5.1 SQL Tuning Tasks

The specifics of a tuning session depend on many factors, including whether you tune proactively or reactively.

In proactive SQL tuning, you regularly use SQL Tuning Advisor to determine whether you can make SQL statements perform better. In reactive SQL tuning, you correct a SQL-related problem that a user has experienced.

Whether you tune proactively or reactively, a typical SQL tuning session involves all or most of the following tasks:

1. Identifying high-load SQL statements
	Review past execution history to find the statements responsible for a large share of the application workload and system resources.
2. Gathering performance-related data
	The [optimizer statistics](glossary.md) are crucial to SQL tuning. If these statistics do not exist or are no longer accurate, then the optimizer cannot generate the best plan. Other data relevant to SQL performance include the structure of tables and views that the statement accessed, and definitions of any indexes available to the statement.
3. Determining the causes of the problem
	Typically, causes of SQL performance problems include:
	- Inefficiently designed SQL statements
		If a SQL statement is written so that it performs unnecessary work, then the optimizer cannot do much to improve its performance. Examples of inefficient design include
		- Neglecting to add a [join condition](glossary.md), which leads to a [Cartesian join](glossary.md)
				- Using hints to specify a large table as the [driving table](glossary.md) in a join
				- Specifying `UNION` instead of `UNION ALL`
				- Making a [subquery](glossary.md) execute for every row in an outer query
		- Suboptimal execution plans
		The [query optimizer](glossary.md) (also called the [optimizer](glossary.md)) is internal software that determines which [execution plan](glossary.md) is most efficient. Sometimes the optimizer chooses a plan with a suboptimal [access path](glossary.md), which is the means by which the database retrieves data from the database. For example, the plan for a query predicate with low [selectivity](glossary.md) may use a [full table scan](glossary.md) on a large table instead of an index.
		You can compare the execution plan of an optimally performing SQL statement to the plan of the statement when it performs suboptimally. This comparison, along with information such as changes in data volumes, can help identify causes of performance degradation.
		- Missing SQL access structures
		Absence of SQL access structures, such as indexes and materialized views, is a typical reason for suboptimal SQL performance. The optimal set of access structures can improve SQL performance by orders of magnitude.
		- Stale optimizer statistics
		Statistics gathered by `DBMS_STATS` can become stale when the statistics maintenance operations, either automatic or manual, cannot keep up with the changes to the table data caused by DML. Because stale statistics on a table do not accurately reflect the table data, the optimizer can make decisions based on faulty information and generate suboptimal execution plans.
		- Hardware problems
		Suboptimal performance might be connected with memory, I/O, and CPU problems.
4. Defining the scope of the problem
	The scope of the solution must match the scope of the problem. Consider a problem at the database level and a problem at the statement level. For example, the shared pool is too small, which causes cursors to age out quickly, which in turn causes many hard parses. Using an initialization parameter to increase the shared pool size fixes the problem at the database level and improves performance for all sessions. However, if a single SQL statement is not using a helpful index, then changing the optimizer initialization parameters for the entire database could harm overall performance. If a single SQL statement has a problem, then an appropriately scoped solution addresses just this problem with this statement.
5. Implementing corrective actions for suboptimally performing SQL statements
	These actions vary depending on circumstances. For example, you might rewrite a SQL statement to be more efficient, avoiding unnecessary hard parsing by rewriting the statement to use bind variables. You might also use equijoins, remove functions from `WHERE` clauses, and break a complex SQL statement into multiple simple statements.
	In some cases, you improve SQL performance not by rewriting the statement, but by restructuring schema objects. For example, you might index a new [access path](glossary.md), or reorder columns in a concatenated index. You might also partition a table, introduce derived values, or even change the database design.
6. Preventing SQL performance regressions
	To ensure optimal SQL performance, verify that execution plans continue to provide optimal performance, and choose better plans if they come available. You can achieve these goals using optimizer statistics, SQL profiles, and SQL plan baselines.

See Also:

- " [Shared Pool Check](sql-processing.md) "
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=CNCPT-GUID-1CB2BA23-4386-46DA-9146-5FE0E4599AC6) to learn more about the shared pool

#### 1.5.2 SQL Tuning Tools

SQL tuning tools are either automated or manual.

In this context, a tool is automated if the database itself can provide diagnosis, advice, or corrective actions. A manual tool requires you to perform all of these operations.

All tuning tools depend on the basic tools of the dynamic performance views, statistics, and metrics that the database instance collects. The database itself contains the data and metadata required to tune SQL statements.

##### 1.5.2.1 Automated SQL Tuning Tools

Oracle Database provides several advisors relevant for SQL tuning.

Additionally, [SQL plan management](glossary.md) is a mechanism that can prevent performance regressions and also help you to improve SQL performance.

All of the automated SQL tuning tools can use SQL tuning sets as input. A [SQL tuning set (STS)](glossary.md) is a database object that includes one or more SQL statements along with their execution statistics and execution context.

See Also:

- " [About SQL Tuning Sets](managing-sql-tuning-sets.md) "
- [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=TDPPT-GUID-13081B28-AB2A-485F-B836-74DAA9961BAA) to learn more about managing SQL tuning sets

###### 1.5.2.1.1 Automatic Database Diagnostic Monitor (ADDM)

ADDM is self-diagnostic software built into Oracle Database.

ADDM can automatically locate the root causes of performance problems, provide recommendations for correction, and quantify the expected benefits. ADDM also identifies areas where no action is necessary.

ADDM and other advisors use [Automatic Workload Repository (AWR)](glossary.md), which is an infrastructure that provides services to database components to collect, maintain, and use statistics. ADDM examines and analyzes statistics in AWR to determine possible performance problems, including high-load SQL.

For example, you can configure ADDM to run nightly. In the morning, you can examine the latest ADDM report to see what might have caused a problem and if there is a recommended fix. The report might show that a particular `SELECT` statement consumed a huge amount of CPU, and recommend that you run SQL Tuning Advisor.

See Also:

- [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=TDPPT020)
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=GUID-F1FBA929-4FCF-4872-AEE6-2DF716B5BD43)

###### 1.5.2.1.2 SQL Tuning Advisor

SQL Tuning Advisor is internal diagnostic software that identifies problematic SQL statements and recommends how to improve statement performance.

When run during database maintenance windows as an automated maintenance task, SQL Tuning Advisor is known as [Automatic SQL Tuning Advisor](glossary.md).

SQL Tuning Advisor takes one or more SQL statements as an input and invokes the [Automatic Tuning Optimizer](glossary.md) to perform SQL tuning on the statements. The advisor performs the following types of analysis:

- Checks for missing or stale statistics
- Builds SQL profiles
	A [SQL profile](glossary.md) is a set of auxiliary information specific to a SQL statement. A SQL profile contains corrections for suboptimal optimizer estimates discovered during Automatic SQL Tuning. This information can improve optimizer estimates for [cardinality](glossary.md), which is the number of rows that is estimated to be or actually is returned by an operation in an execution plan, and selectivity. These improved estimates lead the optimizer to select better plans.
- Explores whether a different access path can significantly improve performance
- Identifies SQL statements that lend themselves to suboptimal plans

The output is in the form of advice or recommendations, along with a rationale for each recommendation and its expected benefit. The recommendation relates to a collection of statistics on objects, creation of new indexes, restructuring of the SQL statement, or creation of a SQL profile. You can choose to accept the recommendations to complete the tuning of the SQL statements.

See Also:

- " [Analyzing SQL with SQL Tuning Advisor](sql-tuning-advisor.md) "
- [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=TDPPT020)

###### 1.5.2.1.3 SQL Access Advisor

**SQL Access Advisor** is internal diagnostic software that recommends which materialized views, indexes, and materialized view logs to create, drop, or retain.

SQL Access Advisor takes an actual workload as input, or the advisor can derive a hypothetical workload from the schema. SQL Access Advisor considers the trade-offs between space usage and query performance, and recommends the most cost-effective configuration of new and existing materialized views and indexes. The advisor also makes recommendations about partitioning.

See Also:

- " [About SQL Access Advisor](sql-access-advisor.md) "
- [Oracle Database 2 Day + Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=TDPPT170)
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=GUID-E4149397-FF37-4367-A12F-675433715904) to learn more about automated indexing
- [Oracle Database Licensing Information User Manual](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=DBLIC-GUID-0F9EB85D-4610-4EDF-89C2-4916A0E7AC87) for details on whether automated indexing is supported for different editions and services

###### 1.5.2.1.4 Automatic Indexing

Oracle Database can constantly monitor the application workload, creating and managing indexes automatically.

Note:

See [Oracle Database Licensing Information User Manual](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=DBLIC-GUID-0F9EB85D-4610-4EDF-89C2-4916A0E7AC87) for details on which features are supported for different editions and services.

Creating indexes manually requires deep knowledge of the data model, application, and data distribution. Often DBAs make choices about which indexes to create, and then never revise their choices. As a result, opportunities for improvement are lost, and unnecessary indexes can become a performance liability. Automatic index management solves this problem.

###### 1.5.2.1.4.1 How Automatic Indexing Works

The automatic indexing process runs in the background every 15 minutes and performs the following operations:

1. Automatic index candidates are identified based on the usage of table columns in SQL statements. Ensure that table statistics are up to date. Tables without statistics are not considered for automatic indexing. Tables with stale statistics are not considered for automatic indexing.
2. Index candidates are initially created invisible and unusable. They are not visible to the application workload. Invisible automatic indexes cannot be used by SQL statements in the application workload.
	Automatic indexes can be single-column or multi-column. They are considered for the following:
	- Table columns (including virtual columns)
		- Partitioned and non-partitioned tables
		- Selected expressions (for example, JSON expressions)
3. A sample of workload SQL statements is tested against the candidate indexes. During this verification phase, some or all candidate indexes will be built and made valid so that the performance effect on SQL statements can be measured. All candidate indexes remain invisible during the verification step.
	If the performance of SQL statements is not improved by using the candidate indexes, they remain invisible.
4. Candidate valid indexes found to improve SQL performance will be made visible and available to the application workload. Candidate indexes that do not improve SQL performance will revert to invisible and be unusable after a short delay.
	During the verification stage, if an index is found to be beneficial, but an individual SQL statement suffers a performance regression, a SQL plan baseline is created to prevent the regression when the index is made visible.
5. Unusable and unused valid indexes are deleted by the automatic indexing process.
	The automatic indexing process runs in the background every 15 minutes and performs the following operations:
	1. Automatic index candidates are identified based on the usage of table columns in SQL statements. Ensure that table statistics are up to date. Tables without statistics are not considered for automatic indexing. Tables with stale statistics are not considered for automatic indexing.
		2. Index candidates are initially created invisible and unusable. They are not visible to the application workload. Invisible automatic indexes cannot be used by SQL statements in the application workload.
		Automatic indexes can be single-column or multi-column. They are considered for the following:
		- Table columns (including virtual columns)
				- Partitioned and non-partitioned tables
				- Selected expressions (for example, JSON expressions)
		3. A sample of workload SQL statements is tested against the candidate indexes. During this verification phase, some or all candidate indexes will be built and made valid so that the performance effect on SQL statements can be measured. All candidate indexes remain invisible during the verification step.
		If the performance of SQL statements is not improved by using the candidate indexes, they remain invisible.
		4. Candidate valid indexes found to improve SQL performance will be made visible and available to the application workload. Candidate indexes that do not improve SQL performance will revert to invisible and be unusable after a short delay.
		During the verification stage, if an index is found to be beneficial, but an individual SQL statement suffers a performance regression, a SQL plan baseline is created to prevent the regression when the index is made visible.
		5. Unusable and unused valid indexes are deleted by the automatic indexing process.
		Note:
		By default, the unused automatic indexes are deleted after 373 days. The period for retaining the unused automatic indexes in a database can be configured using the `DBMS_AUTO_INDEX.CONFIGURE` procedure.

See Also:

[Configuring Automatic Indexing in Oracle Database](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=ADMIN-GUID-A8B4BB05-2711-497A-8276-127076DAA518)

###### 1.5.2.1.4.2 Enabling and Managing Automatic Indexing

The DBMS\_AUTO\_INDEX package provides options for configuring, dropping, monitoring, and reporting on automatic indexing.

You can use the DBMS\_AUTO\_INDEX package to do the following:
- Enable automatic indexing.
	`EXEC                             DBMS_AUTO_INDEX.CONFIGURE('AUTO_INDEX_MODE','IMPLEMENT')`
- Configure additional settings, such as how long to retain unused auto indexes
	`EXEC                             DBMS_AUTO_INDEX.CONFIGURE('AUTO_INDEX_RETENTION_FOR_AUTO','180')`
- Drop an automatic index. Carefully note the use of single and double quotation marks in the first example.
	Drop a single index owned by a schema and allow recreate.
	```
	EXEC DBMS_AUTO_INDEX.DROP_AUTO_INDEXES('SH','"SYS_AI_612UD3J5NGF0C"',TRUE)
	```
	Drop all indexes owned by a schema and allow recreate.
	```
	EXEC DBMS_AUTO_INDEX.DROP_AUTO_INDEXES('SH',NULL,TRUE)
	```
	Drop all indexes owned by a schema and disallow recreate. Then, change the recreation status back to `allow`.
	```
	EXEC DBMS_AUTO_INDEX.DROP_AUTO_INDEXES('HR',NULL)
	EXEC DBMS_AUTO_INDEX.DROP_AUTO_INDEXES('HR',NULL,TRUE)
	```
- Report on the automatic indexing task and configuration settings.

Additional Controls

By setting the `OPTIMIZER_SESSION_TYPE` initialization parameter to `ADHOC` in a session, you can suspend automatic indexing for queries in this session. The automatic indexing process does not identify index candidates, or create and verify indexes. This control may be useful for ad hoc queries or testing new functionality.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=GUID-E4149397-FF37-4367-A12F-675433715904) to learn more about automatic indexing
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=GUID-78C59A20-2F92-448F-96F7-6C4FBB355E42) to learn about the procedures and functions available in the `DBMS_AUTO_INDEX` package
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=REFRN-GUID-5D392CB8-B483-45F5-8230-210CE845BC42) to learn more about `OPTIMIZER_SESSION_TYPE`.

###### 1.5.2.1.5 SQL Plan Management

SQL plan management is a preventative mechanism that enables the optimizer to automatically manage execution plans, ensuring that the database uses only known or verified plans.

This mechanism can build a [SQL plan baseline](glossary.md), which contains one or more accepted plans for each SQL statement. By using baselines, SQL plan management can prevent plan regressions from environmental changes, while permitting the optimizer to discover and use better plans.

See Also:

- " [Overview of SQL Plan Management](overview-of-sql-plan-management.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=ARPLS-GUID-D6EC284C-053D-417D-B887-94422BCB4E3A)
	to learn about the `DBMS_SPM` package

###### 1.5.2.1.6 SQL Performance Analyzer

SQL Performance Analyzer determines the effect of a change on a SQL workload by identifying performance divergence for each SQL statement.

System changes such as upgrading a database or adding an index may cause changes to execution plans, affecting SQL performance. By using SQL Performance Analyzer, you can accurately forecast the effect of system changes on SQL performance. Using this information, you can tune the database when SQL performance regresses, or validate and measure the gain when SQL performance improves.

##### 1.5.2.2 Manual SQL Tuning Tools

In some situations, you may want to run manual tools in addition to the automated tools. Alternatively, you may not have access to the automated tools.

###### 1.5.2.2.1 Execution Plans

Execution plans are the principal diagnostic tool in manual SQL tuning. For example, you can view plans to determine whether the optimizer selects the plan you expect, or identify the effect of creating an index on a table.

You can display execution plans in multiple ways. The following tools are the most commonly used:

- `DBMS_XPLAN`
	You can use the `DBMS_XPLAN` package methods to display the execution plan generated by the `EXPLAIN PLAN` command and query of `V$SQL_PLAN`.
- `EXPLAIN PLAN`
	This SQL statement enables you to view the execution plan that the optimizer would use to execute a SQL statement without actually executing the statement. See [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=SQLRF01601).
- `V$SQL_PLAN` and related views
	These views contain information about executed SQL statements, and their execution plans, that are still in the shared pool. See [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=REFRN30250).
- `AUTOTRACE`
	The `AUTOTRACE` command in SQL\*Plus generates the execution plan and statistics about the performance of a query. This command provides statistics such as disk reads and memory reads. See [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=SQPUG018).

###### 1.5.2.2.2 Real-Time SQL Monitoring and Real-Time Database Operations

The Real-Time SQL Monitoring feature of Oracle Database enables you to monitor the performance of SQL statements while they are executing. By default, SQL monitoring starts automatically when a statement runs in parallel, or when it has consumed at least 5 seconds of CPU or I/O time in a single execution.

A [database operation](glossary.md) is a set of database tasks defined by end users or application code, for example, a batch job or Extraction, Transformation, and Loading (ETL) processing. You can define, monitor, and report on database operations. Real-Time Database Operations provides the ability to monitor composite operations automatically. The database automatically monitors parallel queries, DML, and DDL statements as soon as execution begins.

Oracle Enterprise Manager Cloud Control (Cloud Control) provides easy-to-use SQL monitoring pages. Alternatively, you can monitor SQL-related statistics using the `V$SQL_MONITOR` and `V$SQL_PLAN_MONITOR` views. You can use these views with the following views to get more information about executions that you are monitoring:

- `V$ACTIVE_SESSION_HISTORY`
- `V$SESSION`
- `V$SESSION_LONGOPS`
- `V$SQL`
- `V$SQL_PLAN`

See Also:

- " [About Monitoring Database Operations](monitoring-database-operations.md) "
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=GUID-8C5690B0-DE10-4460-86DF-80111869CF4C) to learn about the `V$` views

###### 1.5.2.2.3 Application Tracing

A **SQL trace file** provides performance information on individual SQL statements: parse counts, physical and logical reads, misses on the library cache, and so on.

Trace files are sometimes useful for diagnosing SQL performance problems. You can enable and disable SQL tracing for a specific session using the `DBMS_MONITOR` or `DBMS_SESSION` packages. Oracle Database implements tracing by generating a trace file for each server process when you enable the tracing mechanism.

Oracle Database provides the following command-line tools for analyzing trace files:

- `TKPROF`
	This utility accepts as input a trace file produced by the SQL Trace facility, and then produces a formatted output file.
- `trcsess`
	This utility consolidates trace output from multiple trace files based on criteria such as session ID, client ID, and service ID. After `trcsess` merges the trace information into a single output file, you can format the output file with `TKPROF`. `trcsess` is useful for consolidating the tracing of a particular session for performance or debugging purposes.

End-to-End Application Tracing simplifies the process of diagnosing performance problems in multitier environments. In these environments, the middle tier routes a request from an end client to different database sessions, making it difficult to track a client across database sessions. End-to-End application tracing uses a client ID to uniquely trace a specific end-client through all tiers to the database.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=ARPLS091) to learn more about `DBMS_MONITOR` and `DBMS_SESSION`

###### 1.5.2.2.4 Optimizer Hints

A **hint** is an instruction passed to the optimizer through comments in a SQL statement.

Hints enable you to make decisions normally made automatically by the optimizer. In a test or development environment, hints are useful for testing the performance of a specific access path. For example, you may know that a specific index is more selective for certain queries. In this case, you may use hints to instruct the optimizer to use a better execution plan, as in the following example:

```
SELECT /*+ INDEX (employees emp_department_ix) */ 
       employee_id, department_id 
FROM   employees
WHERE  department_id > 50;
```

Sometimes the database may not use a hint because of typos, invalid arguments, conflicting hints, and hints that are made invalid by transformations. Starting in Oracle Database 19c, you can generate a report about which hints were used or not used during plan generation.

See Also:

- " [Influencing the Optimizer with Hints](influencing-the-optimizer.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=SQLRF-GUID-D316D545-89E2-4D54-977F-FC97815CD62E) to learn more about hints

#### 1.5.3 User Interfaces to SQL Tuning Tools

Cloud Control is a system management tool that provides centralized management of a database environment. Cloud Control provides access to most tuning tools.

By combining a graphical console, Oracle Management Servers, Oracle Intelligent Agents, common services, and administrative tools, Cloud Control provides a comprehensive system management platform.

You can access all SQL tuning tools using a command-line interface. For example, the `DBMS_SQLTUNE` package is the command-line interface for SQL Tuning Advisor.

Oracle recommends Cloud Control as the best interface for database administration and tuning. In cases where the command-line interface better illustrates a particular concept or task, this manual uses command-line examples. However, in these cases the tuning tasks include a reference to the principal Cloud Control page associated with the task.