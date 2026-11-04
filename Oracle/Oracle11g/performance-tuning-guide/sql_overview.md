---
title: SQL Tuning Overview
book: Performance Tuning Guide
doc_id: E41573-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41573/sql_overview.htm
tags:
  - oracle
  - 11g
  - performance-tuning-guide
---

## 16 SQL Tuning Overview

This chapter discusses goals for tuning, how to identify high-resource SQL statements, explains what should be collected, provides tuning suggestions, and discusses how to create SQL test cases to troubleshoot problems in SQL.

This chapter contains the following sections:

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/sqllangu.htm#CNCPT015) for an overview of SQL
- [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/montune.htm#ADMQS010) to learn how to monitor the database

## 16.1 Introduction to SQL Tuning

SQL tuning involves the following basic steps:

- Identifying high load or top SQL statements that are responsible for a large share of the application workload and system resources, by reviewing past SQL execution history available in the system
- Verifying that the execution plans produced by the query optimizer for these statements perform reasonably
- Implementing corrective actions to generate better execution plans for poorly performing SQL statements

The previous steps are repeated until the system performance reaches a satisfactory level or no more statements can be tuned.

## 16.2 Goals for Tuning

The objective of tuning a system is either to reduce the response time for end users of the system, or to reduce the resources used to process the same work. You can accomplish both of these objectives in several ways:

- Reduce the Workload
- Balance the Workload
- Parallelize the Workload

### 16.2.1 Reduce the Workload

SQL tuning commonly involves finding more efficient ways to process the same workload. It is possible to change the execution plan of the statement without altering the functionality to reduce the resource consumption.

Two examples of how you can resource usage are as follows:

1. If a commonly executed query must access a small percentage of data in the table, then the database can execute it more efficiently by using an index. By creating such an index, you reduce the amount of resources used.
2. If a user is looking at the first twenty rows of the 10,000 rows returned in a specific sort order, and if the query (and sort order) can be satisfied by an index, then the user does not need to access and sort the 10,000 rows to see the first 20 rows.

### 16.2.2 Balance the Workload

Systems often tend to have peak usage in the daytime when real users are connected to the system, and low usage in the nighttime. If you can schedule noncritical reports and batch jobs to run in the nighttime and reduce their concurrency during day time, then the database frees up resources for the more critical programs in the day.

### 16.2.3 Parallelize the Workload

Queries that access large amounts of data (typical data warehouse queries) can often run in parallel. Parallelism is extremely useful for reducing response time in a low concurrency data warehouse. However, for OLTP environments, which tend to be high concurrency, parallelism can adversely impact other users by increasing the overall resource usage of the program.

## 16.3 Identifying High-Load SQL

This section describes the steps involved in identifying and gathering data on high-load SQL statements. High-load SQL are poorly-performing, resource-intensive SQL statements that impact the performance of an Oracle database. The following tools can identify high-load SQL statements:

- Automatic Database Diagnostic Monitor
- Automatic SQL tuning
- Automatic Workload Repository
- `V$SQL` view
- Custom Workload
- SQL Trace

### 16.3.1 Identifying Resource-Intensive SQL

The first step in identifying resource-intensive SQL is to categorize the problem you are attempting to fix:

- Is the problem specific to a single program (or small number of programs)?
- Is the problem generic over the application?

#### 16.3.1.1 Tuning a Specific Program

If you are tuning a specific program (GUI or 3GL), then identifying the SQL to examine is a simple matter of looking at the SQL executed within the program. Oracle Enterprise Manager (Enterprise Manager) provides tools for identifying resource intensive SQL statements, generating explain plans, and evaluating SQL performance.

If it is not possible to identify the SQL (for example, the SQL is generated dynamically), then use `SQL_TRACE` to generate a trace file that contains the SQL executed, then use `TKPROF` to generate an output file.

The SQL statements in the `TKPROF` output file can be ordered by various parameters, such as the execution elapsed time (`exeela`), which usually assists in the identification by ordering the SQL statements by elapsed time (with highest elapsed time SQL statements at the top of the file). This makes the job of identifying the poorly performing SQL easier if there are many SQL statements in the file.

#### 16.3.1.2 Tuning an Application / Reducing Load

If the whole application is performing poorly, or if you are attempting to reduce the overall CPU or I/O load on the database server, then identifying resource-intensive SQL involves the following steps:

1. Determine which period in the day you would like to examine; typically this is the application's peak processing time.
2. Gather operating system and Oracle Database statistics at the beginning and end of that period. The minimum of Oracle Database statistics gathered should be file I/O (`V$FILESTAT`), system statistics (`V$SYSSTAT`), and SQL statistics (`V$SQLAREA`, `V$SQL`, or `V$SQLSTATS`, `V$SQLTEXT`, `V$SQL_PLAN`, and `V$SQL_PLAN_STATISTICS`).
	See Also:
	- [Chapter 6, "Automatic Performance Diagnostics"](diag.md) to learn how to gather Oracle database instance performance data
	- ["Real-Time SQL Monitoring"](instance_tune.md) for information about the `V$SQL_PLAN_MONITOR` view
3. Using the data collected in step two, identify the SQL statements using the most resources. A good way to identify candidate SQL statements is to query `V$SQLSTATS`. `V$SQLSTATS` contains resource usage information for all SQL statements in the shared pool. The data in `V$SQLSTATS` should be ordered by resource usage. The most common resources are:
	- Buffer gets (`V$SQLSTATS`.`BUFFER_GETS`, for high CPU using statements)
		- Disk reads (`V$SQLSTATS`.`DISK_READS`, for high I/O statements)
		- Sorts (`V$SQLSTATS`.`SORTS`, for many sorts)

One method to identify which SQL statements are creating the highest load is to compare the resources used by a SQL statement to the total amount of that resource used in the period. For `BUFFER_GETS`, divide each SQL statement's `BUFFER_GETS` by the total number of buffer gets during the period. The total number of buffer gets in the system is available in the `V$SYSSTAT` table, for the statistic session logical reads.

Similarly, it is possible to apportion the percentage of disk reads a statement performs out of the total disk reads performed by the system by dividing `V$SQL_STATS.DISK_READS` by the value for the `V$SYSSTAT` statistic physical reads. The SQL sections of the Automatic Workload Repository report include this data, so you do not need to perform the percentage calculations manually.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_part.htm#REFRN003) for information about dynamic performance views

After you have identified the candidate SQL statements, the next stage is to gather information that is necessary to examine the statements and tune them.

### 16.3.2 Gathering Data on the SQL Identified

If you are most concerned with CPU, then examine the top SQL statements that performed the most `BUFFER_GETS` during that interval. Otherwise, start with the SQL statement that performed the most `DISK_READS`.

#### 16.3.2.1 Information to Gather During Tuning

The tuning process begins by determining the structure of the underlying tables and indexes. The information gathered includes the following:

1. Complete SQL text from `V$SQLTEXT`
2. Structure of the tables referenced in the SQL statement, usually by describing the table in SQL\*Plus
3. Definitions of any indexes (columns, column orders), and whether the indexes are unique or non-unique
4. Optimizer statistics for the segments (including the number of rows each table, selectivity of the index columns), including the date when the segments were last analyzed
5. Definitions of any views referred to in the SQL statement
6. Repeat steps two, three, and four for any tables referenced in the view definitions found in step five
7. Optimizer plan for the SQL statement (either from `EXPLAIN` `PLAN`, `V$SQL_PLAN`, or the `TKPROF` output)
8. Any previous optimizer plans for that SQL statement
	Note:
	It is important to generate and review execution plans for all of the key SQL statements in your application. Doing so lets you compare the optimizer execution plans of a SQL statement when the statement performed well to the plan when that the statement is not performing well. Having the comparison, along with information such as changes in data volumes, can assist in identifying the cause of performance degradation.

## 16.4 Automatic SQL Tuning Features

Because the manual SQL tuning process poses many challenges to the application developer, the SQL tuning process has been automated by the automatic SQL tuning features of Oracle Database. These features are designed to work equally well for OLTP and Data Warehouse type applications:

- ADDM
- SQL Tuning Advisor
- SQL Tuning Sets
- SQL Access Advisor

See Also:

[Chapter 17, "Automatic SQL Tuning"](sql_tune.md).

### 16.4.1 ADDM

The Automatic Database Diagnostic Monitor (ADDM) analyzes the information collected by the AWR for possible performance problems with Oracle Database, including high-load SQL statements. See ["Overview of the Automatic Database Diagnostic Monitor"](diag.md).

### 16.4.2 SQL Tuning Advisor

SQL Tuning Advisor optimizes SQL statements that have been identified as high-load SQL statements. By default, Oracle Database automatically identifies problematic SQL statements and implements tuning recommendations using SQL Tuning Advisor during system maintenance windows as an automated maintenance task, searching for ways to improve the execution plans of the high-load SQL statements. You can also choose to run SQL Tuning Advisor at any time on any given SQL workload to improve performance. See ["Tuning Reactively with SQL Tuning Advisor"](sql_tune.md).

### 16.4.3 SQL Tuning Sets

When multiple SQL statements serve as input to ADDM, SQL Tuning Advisor, or SQL Access Advisor, the database constructs and stores a SQL tuning set (STS). The STS includes the set of SQL statements along with their associated execution context and basic execution statistics. See ["Managing SQL Tuning Sets"](sql_tune.md).

### 16.4.4 SQL Access Advisor

In addition to SQL Tuning Advisor, SQL Access Advisor provides advice on materialized views, indexes, and materialized view logs. SQL Access Advisor helps you achieve performance goals by recommending the proper set of materialized views, materialized view logs, and indexes for a given workload. In general, as the number of materialized views and indexes and the space allocated to them is increased, query performance improves. SQL Access Advisor considers the trade-offs between space usage and query performance, and recommends the most cost-effective configuration of new and existing materialized views and indexes. See ["Using SQL Access Advisor"](advisor.md).

## 16.5 Developing Efficient SQL Statements

This section describes ways you can improve SQL statement efficiency:

- Verifying Optimizer Statistics
- Reviewing the Execution Plan
- Restructuring the SQL Statements
- Restructuring the Indexes
- Modifying or Disabling Triggers and Constraints
- Restructuring the Data
- Maintaining Execution Plans Over Time
- Visiting Data as Few Times as Possible
	Note:
	The guidelines described in this section are oriented to production of frequently executed SQL. Most techniques that are discouraged here can legitimately be employed in ad hoc statements or in applications run infrequently where performance is not critical.

### 16.5.1 Verifying Optimizer Statistics

The query optimizer uses statistics gathered on tables and indexes when determining the optimal execution plan. If these statistics have not been gathered, or if the statistics are no longer representative of the data stored within the database, then the optimizer does not have sufficient information to generate the best plan.

Things to check:

- If you gather statistics for some tables in your database, then it is probably best to gather statistics for all tables. This is especially true if your application includes SQL statements that perform joins.
- If the optimizer statistics in the data dictionary are no longer representative of the data in the tables and indexes, then gather new statistics. One way to check whether the dictionary statistics are stale is to compare the real cardinality (row count) of a table to the value of `DBA_TABLES.NUM_ROWS`. Additionally, if there is significant data skew on predicate columns, then consider using histograms.

### 16.5.2 Reviewing the Execution Plan

When tuning (or writing) a SQL statement in an OLTP environment, the goal is to drive from the table that has the most selective filter. This means that there are fewer rows passed to the next step. If the next step is a join, then this means that fewer rows are joined. Check to see whether the access paths are optimal.

When examining the optimizer execution plan, look for the following:

- The driving table has the best filter.
- The join order in each step returns the fewest number of rows to the next step (that is, the join order should reflect, where possible, going to the best not-yet-used filters).
- The join method is appropriate for the number of rows being returned. For example, nested loop joins through indexes may not be optimal when the statement returns many rows.
- The database uses views efficiently. Look at the `SELECT` list to see whether access to the view is necessary.
- There are any unintentional Cartesian products (even with small tables).
- Each table is being accessed efficiently:
	Consider the predicates in the SQL statement and the number of rows in the table. Look for suspicious activity, such as a full table scans on tables with large number of rows, which have predicates in the where clause. Determine why an index is not used for such a selective predicate.
	A full table scan does not mean inefficiency. It might be more efficient to perform a full table scan on a small table, or to perform a full table scan to leverage a better join method (for example, hash\_join) for the number of rows returned.

If any of these conditions are not optimal, then consider restructuring the SQL statement or the indexes available on the tables.

### 16.5.3 Restructuring the SQL Statements

Often, rewriting an inefficient SQL statement is easier than modifying it. If you understand the purpose of a given statement, then you might be able to quickly and easily write a new statement that meets the requirement.

#### 16.5.3.1 Compose Predicates Using AND and =

To improve SQL efficiency, use equijoins whenever possible. Statements that perform equijoins on untransformed column values are the easiest to tune.

#### 16.5.3.2 Avoid Transformed Columns in the WHERE Clause

Use untransformed column values. For example, use:

```
WHERE a.order_no = b.order_no
```

rather than:

```
WHERE TO_NUMBER (SUBSTR(a.order_no, INSTR(b.order_no, '.') - 1))
= TO_NUMBER (SUBSTR(a.order_no, INSTR(b.order_no, '.') - 1))
```

Do not use SQL functions in predicate clauses or `WHERE` clauses. Any expression using a column, such as a function having the column as its argument, causes the optimizer to ignore the possibility of using an index on that column, even a unique index, unless there is a function-based index defined that the database can use.

Avoid mixed-mode expressions, and beware of implicit type conversions. When you want to use an index on the `VARCHAR2` column `charcol`, but the `WHERE` clause looks like this:

```
AND charcol = numexpr
```

where `numexpr` is an expression of number type (for example, 1, `USERENV` (' `SESSIONID` '), `numcol`, `numcol` +0,...), Oracle Database translates that expression into:

```
AND TO_NUMBER(charcol) = numexpr
```

Avoid the following kinds of complex expressions:

- `col1` = `NVL` `(:b1`,`col1)`
- `NVL` (`col1,-999`) = ….
- `TO_DATE` (), `TO_NUMBER` (), and so on

These expressions prevent the optimizer from assigning valid cardinality or selectivity estimates and can in turn affect the overall plan and the join method.

Add the predicate versus using `NVL` () technique.

For example:

```
SELECT employee_num, full_name Name, employee_id 
  FROM mtl_employees_current_view 
  WHERE (employee_num = NVL (:b1,employee_num)) AND (organization_id=:1) 
  ORDER BY employee_num;
```

Also:

```
SELECT employee_num, full_name Name, employee_id 
  FROM mtl_employees_current_view 
  WHERE (employee_num = :b1) AND (organization_id=:1) 
  ORDER BY employee_num;
```

If a column of type `NUMBER` is used in a `WHERE` clause to filter predicates with a literal value, then use a `TO_NUMBER` function in the `WHERE` clause predicate to ensure you can use the index on the `NUMBER` column. For example, if `numcol` is a column of type `NUMBER`, then a `WHERE` clause containing `numcol=TO_NUMBER('5')` enables the database to use the index on `numcol`.

If a query joins two tables, and if the join columns have different data types (for example, `NUMBER` and `VARCHAR2`), then Oracle Database implicitly performs data type conversion. For example, if the join condition is `varcol=numcol`, then the database implicitly converts the condition to `TO_NUMBER(varcol)=numcol`. If an index exists on the `varcol` column, then explicitly set the type conversion to `varcol=TO_CHAR(numcol)`, thus enabling the database to use the index.

See Also:

[Chapter 14, "Using Indexes and Clusters"](data_acc.md) for more information on function-based indexes

#### 16.5.3.3 Write Separate SQL Statements for Specific Tasks

SQL is not a procedural language. Using one piece of SQL to do many different things usually results in a less-than-optimal result for each task. If you want SQL to accomplish different things, then write various statements, rather than writing one statement to do different things depending on the parameters you give it.

Note:

Oracle Forms and Reports are powerful development tools that allow application logic to be coded using PL/SQL (triggers or program units). This helps reduce the complexity of SQL by allowing complex logic to be handled in the Forms or Reports. You can also invoke a server side PL/SQL package that performs the few SQL statements in place of a single large complex SQL statement. Because the package is a server-side unit, there are no issues surrounding client to database round-trips and network traffic.

It is always better to write separate SQL statements for different tasks, but if you must use one SQL statement, then you can make a very complex statement slightly less complex by using the `UNION` `ALL` operator.

Optimization (determining the execution plan) takes place before the database knows the values substituted in the query. An execution plan cannot, therefore, depend on what those values are. For example:

```
SELECT info 
FROM tables
WHERE ...
```
```
AND somecolumn BETWEEN DECODE(:loval, 'ALL', somecolumn, :loval)
AND DECODE(:hival, 'ALL', somecolumn, :hival);
```

Written as shown, the database cannot use an index on the `somecolumn` column, because the expression involving that column uses the same column on both sides of the `BETWEEN`.

This is not a problem if there is some other highly selective, indexable condition you can use to access the driving table. Often, however, this is not the case. Frequently, you might want to use an index on a condition like that shown but need to know the values of:`loval`, and so on, in advance. With this information, you can rule out the `ALL` case, which should not use the index.

To use the index whenever real values are given for:`loval` and:`hival` (if you expect narrow ranges, even ranges where:`loval` often equals:`hival`), you can rewrite the example in the following logically equivalent form:

```
SELECT /* change this half of UNION ALL if other half changes */ info
FROM   tables 
WHERE  ...
```
```
AND    somecolumn BETWEEN :loval AND :hival
AND   (:hival != 'ALL' AND :loval != 'ALL')
```
```
UNION ALL 
SELECT /* Change this half of UNION ALL if other half changes. */ info
FROM   tables
WHERE  ...
```
```
AND (:hival = 'ALL' OR :loval = 'ALL');
```

If you run `EXPLAIN` `PLAN` on the new query, then you seem to get both a desirable and an undesirable execution plan. However, the first condition the database evaluates for either half of the `UNION` `ALL` is the combined condition on whether `:hival` and `:loval` are `ALL`. The database evaluates this condition before actually getting any rows from the execution plan for that part of the query.

When the condition comes back false for one part of the `UNION` `ALL` query, that part is not evaluated further. Only the part of the execution plan that is optimum for the values provided is actually carried out. Because the final conditions on `:hival` and `:loval` are guaranteed to be mutually exclusive, only one half of the `UNION` `ALL` actually returns rows. (The `ALL` in `UNION` `ALL` is logically valid because of this exclusivity. It allows the plan to be carried out without an expensive sort to rule out duplicate rows for the two halves of the query.)

### 16.5.4 Controlling the Access Path and Join Order with Hints

You can influence the optimizer's choices by setting the optimizer approach and goal, and by gathering representative statistics for the query optimizer. Sometimes, the application designer, who has more information about a particular application's data than is available to the optimizer, can choose a more effective way to execute a SQL statement. You can use hints in SQL statements to instruct the optimizer about how the statement should be executed.

Hints, such as /\*+ `FULL` \*/ control access paths. For example:

```
SELECT /*+ FULL(e) */ e.last_name
  FROM employees e
 WHERE e.job_id = 'CLERK';
```

Join order can have a significant effect on performance. The main objective of SQL tuning is to avoid performing unnecessary work to access rows that do not affect the result. This leads to three general rules:

- Avoid a full-table scan if it is more efficient to get the required rows through an index.
- Avoid using an index that fetches 10,000 rows from the driving table if you could instead use another index that fetches 100 rows.
- Choose the join order so as to join fewer rows to tables later in the join order.

The following example shows how to tune join order effectively:

```
SELECT info
FROM taba a, tabb b, tabc c
WHERE a.acol BETWEEN 100 AND 200
```
```
AND b.bcol BETWEEN 10000 AND 20000
AND c.ccol BETWEEN 10000 AND 20000
AND a.key1 = b.key1
AND a.key2 = c.key2;
```
1. Choose the driving table and the driving index (if any).
	The first three conditions in the previous example are filter conditions applying to only a single table each. The last two conditions are join conditions.
	Filter conditions dominate the choice of driving table and index. In general, the driving table is the one containing the filter condition that eliminates the highest percentage of the table. Thus, because the range of 100 to 200 is narrow compared with the range of `acol`, but the ranges of 10000 and 20000 are relatively large, `taba` is the driving table, all else being equal.
	With nested loop joins, the joins all happen through the join indexes, the indexes on the primary or foreign keys used to connect that table to an earlier table in the join tree. Rarely do you use the indexes on the non-join conditions, except for the driving table. Thus, after `taba` is chosen as the driving table, use the indexes on `b`.`key1` and `c`.`key2` to drive into `tabb` and `tabc`, respectively.
2. Choose the best join order, driving to the best unused filters earliest.
	You can reduce the work of the following join by first joining to the table with the best still-unused filter. Thus, if " `bcol` `BETWEEN`..." is more restrictive (rejects a higher percentage of the rows seen) than " `ccol` `BETWEEN`...", then the last join becomes easier (with fewer rows) if `tabb` is joined before `tabc`.
3. You can use the `ORDERED` or `STAR` hint to force the join order.
	See Also:
	["Hints for Join Orders"](hintsref.md)

#### 16.5.4.1 Use Caution When Managing Views

Be careful when joining views, when performing outer joins to views, and when reusing an existing view for a new purpose.

##### 16.5.4.1.1 Use Caution When Joining Complex Views

Joins to complex views are not recommended, particularly joins from one complex view to another. Often this results in the entire view being instantiated, and then the query is run against the view data.

For example, the following statement creates a view that lists employees and departments:

```
CREATE OR REPLACE VIEW emp_dept
AS
SELECT d.department_id, d.department_name, d.location_id,
     e.employee_id, e.last_name, e.first_name, e.salary, e.job_id
FROM  departments d
     ,employees e
WHERE e.department_id (+) = d.department_id;
```

The following query finds employees in a specified state:

```
SELECT v.last_name, v.first_name, l.state_province
  FROM locations l, emp_dept v
 WHERE l.state_province = 'California'
  AND   v.location_id = l.location_id (+);
```

In the following plan table output, note that the `emp_dept` view is instantiated:

```
--------------------------------------------------------------------------------
| Operation                 |  Name    |  Rows | Bytes|  Cost  | Pstart| Pstop |
--------------------------------------------------------------------------------
| SELECT STATEMENT          |          |       |      |        |       |       |
|  FILTER                   |          |       |      |        |       |       |
|   NESTED LOOPS OUTER      |          |       |      |        |       |       |
|    VIEW                   |EMP_DEPT  |       |      |        |       |       |
|     NESTED LOOPS OUTER    |          |       |      |        |       |       |
|      TABLE ACCESS FULL    |DEPARTMEN |       |      |        |       |       |
|      TABLE ACCESS BY INDEX|EMPLOYEES |       |      |        |       |       |
|       INDEX RANGE SCAN    |EMP_DEPAR |       |      |        |       |       |
|    TABLE ACCESS BY INDEX R|LOCATIONS |       |      |        |       |       |
|     INDEX UNIQUE SCAN     |LOC_ID_PK |       |      |        |       |       |
--------------------------------------------------------------------------------
```

##### 16.5.4.1.2 Do Not Recycle Views

Beware of writing a view for one purpose and then using it for other purposes to which it might be ill-suited. Querying from a view requires all tables from the view to be accessed for the data to be returned. Before reusing a view, determine whether all tables in the view need to be accessed to return the data. If not, then do not use the view. Instead, use the base table(s), or if necessary, define a new view. The goal is to refer to the minimum number of tables and views necessary to return the required data.

Consider the following example:

```
SELECT department_name 
FROM emp_dept
WHERE department_id = 10;
```

The entire view is first instantiated by performing a join of the `employees` and `departments` tables and then aggregating the data. However, you can obtain `department_name` and `department_id` directly from the `departments` table. It is inefficient to obtain this information by querying the `emp_dept` view.

##### 16.5.4.1.3 Use Caution When Unnesting Subqueries

Subquery unnesting merges the body of the subquery into the body of the statement that contains it, allowing the optimizer to consider them together when evaluating access paths and joins.

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/toc.htm) for an explanation of the dangers with subquery unnesting

##### 16.5.4.1.4 Use Caution When Performing Outer Joins to Views

In the case of an outer join to a multi-table view, the query optimizer (in Release 8.1.6 and later) can drive from an outer join column, if an equality predicate is defined on it.

An outer join within a view is problematic because the performance implications of the outer join are not visible.

#### 16.5.4.2 Store Intermediate Results

Intermediate, or staging, tables are quite common in relational database systems, because they temporarily store some intermediate results. In many applications they are useful, but Oracle Database requires additional resources to create them. Always consider whether the benefit they could bring is more than the cost to create them. Avoid staging tables when the information is not reused multiple times.

Some additional considerations:

- Storing intermediate results in staging tables could improve application performance. In general, whenever an intermediate result is usable by multiple following queries, it is worthwhile to store it in a staging table. The benefit of not retrieving data multiple times with a complex statement at the second usage of the intermediate result is better than the cost to materialize it.
- Long and complex queries are hard to understand and optimize. Staging tables can break a complicated SQL statement into several smaller statements, and then store the result of each step.
- Consider using materialized views. These are precomputed tables comprising aggregated or joined data from fact and possibly dimension tables.
	See Also:
	[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/toc.htm) for detailed information on using materialized views

### 16.5.5 Restructuring the Indexes

Often, there is a beneficial impact on performance by restructuring indexes. This can involve the following:

- Remove nonselective indexes to speed the DML.
- Index performance-critical access paths.
- Consider reordering columns in existing concatenated indexes.
- Add columns to the index to improve selectivity.

Do not use indexes as a panacea. Application developers sometimes think that performance improves when they create more indexes. If a single programmer creates an appropriate index, then this index may improve the application's performance. However, if 50 developers each create an index, then application performance will probably be hampered.

### 16.5.6 Modifying or Disabling Triggers and Constraints

Using triggers consumes system resources. If you use too many triggers, then performance may be adversely affected. In this case, you might need to modify or disable the triggers.

### 16.5.7 Restructuring the Data

After restructuring the indexes and the statement, consider restructuring the data:

- Introduce derived values. Avoid `GROUP` `BY` in response-critical code.
- Review your data design. Change the design of your system if it can improve performance.
- Consider partitioning, if appropriate.

### 16.5.8 Maintaining Execution Plans Over Time

You can maintain the existing execution plan of SQL statements over time either using stored statistics or SQL plan baselines. Storing optimizer statistics for tables will apply to all SQL statements that refer to those tables. Storing an execution plan as a SQL plan baseline maintains the plan for set of SQL statements. If both statistics and a SQL plan baseline are available for a SQL statement, then the optimizer first uses a cost-based search method to build a best-cost plan, and then tries to find a matching plan in the SQL plan baseline. If a match is found, then the optimizer proceeds using this plan. Otherwise, it evaluates the cost of each of the accepted plans in the SQL plan baseline and selects the plan with the lowest cost.

### 16.5.9 Visiting Data as Few Times as Possible

Applications should try to access each row only once. This reduces network traffic and reduces database load. Consider doing the following:

- Combine Multiples Scans Using CASE Expressions
- Use DML with RETURNING Clause
- Modify All the Data Needed in One Statement

#### 16.5.9.1 Combine Multiples Scans Using CASE Expressions

Often, it is necessary to calculate different aggregates on various sets of tables. Usually, you achieve this goal with multiple scans on the table, but it is easy to calculate all the aggregates with a single scan. Eliminating n-1 scans can greatly improve performance.

You can combine multiple scans into one scan by moving the `WHERE` condition of each scan into a `CASE` expression, which filters the data for the aggregation. For each aggregation, there could be another column that retrieves the data.

The following example asks for the count of all employees who earn less then 2000, between 2000 and 4000, and more than 4000 each month. You can obtain this result by executing three separate queries:

```
SELECT COUNT (*)
  FROM employees
  WHERE salary < 2000;

SELECT COUNT (*)
  FROM employees
  WHERE salary BETWEEN 2000 AND 4000;

SELECT COUNT (*)
  FROM employees
  WHERE salary>4000;
```

However, it is more efficient to run the entire query in a single statement. Each number is calculated as one column. The count uses a filter with the `CASE` expression to count only the rows where the condition is valid. For example:

```
SELECT COUNT (CASE WHEN salary < 2000 
                   THEN 1 ELSE null END) count1, 
       COUNT (CASE WHEN salary BETWEEN 2001 AND 4000 
                   THEN 1 ELSE null END) count2, 
       COUNT (CASE WHEN salary > 4000 
                   THEN 1 ELSE null END) count3 
  FROM employees;
```

This is a very simple example. The ranges could be overlapping, the functions for the aggregates could be different, and so on.

#### 16.5.9.2 Use DML with RETURNING Clause

When appropriate, use `INSERT`, `UPDATE`, or `DELETE`... `RETURNING` to select and modify data with a single call. This technique improves performance by reducing the number of calls to the database.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for syntax on the `INSERT`, `UPDATE`, and `DELETE` statements

#### 16.5.9.3 Modify All the Data Needed in One Statement

When possible, use array processing. This means that an array of bind variable values is passed to Oracle Database for repeated execution. This is appropriate for iterative processes in which multiple rows of a set are subject to the same operation.

For example:

```
BEGIN
 FOR pos_rec IN (SELECT * 
   FROM order_positions 
   WHERE order_id = :id) LOOP
      DELETE FROM order_positions
      WHERE order_id = pos_rec.order_id AND
        order_position = pos_rec.order_position;
 END LOOP;
 DELETE FROM orders 
 WHERE order_id = :id;
END;
```

Alternatively, you could define a cascading constraint on `orders`. In the previous example, one `SELECT` and n `DELETE` s are executed. When a user issues the `DELETE` on `orders` `DELETE` `FROM` `orders` `WHERE` `order_id` = `:id`, the database automatically deletes the positions with a single `DELETE` statement.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) or [Oracle Database Heterogeneous Connectivity User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11050/toc.htm) to learn how to tune distributed queries

## 16.6 Building SQL Test Cases

For many SQL-related problems, obtaining a reproducible test case makes it easier to resolve the problem. Starting with the 11g Release 2 (11.2), Oracle Database contains the SQL Test Case Builder, which automates the somewhat difficult and time-consuming process of gathering and reproducing as much information as possible about a problem and the environment in which it occurred.

SQL Test Case Builder captures information pertaining to a SQL-related problem, along with the exact environment under which the problem occurred, so that you can reproduce and test the problem on a separate database. After the test case is ready, you can upload the problem to Oracle Support to enable support personnel to reproduce and troubleshoot the problem.

The information gathered by SQL Test Case Builder includes the query being executed, table and index definitions (but not the actual data), PL/SQL functions, procedures, and packages, optimizer statistics, and initialization parameter settings.

### 16.6.1 Creating a Test Case

You can access the SQL Test Case Builder from Enterprise Manager or manually using the `DBMS_SQLDIAG` package.

#### 16.6.1.1 Accessing SQL Test Case Builder from Enterprise Manager

From Enterprise Manager, the SQL Test Case Builder is accessible only when a SQL incident occurs. A SQL-related problem is referred to as a SQL incident, and each SQL incident is identified by an incident number. You can access the SQL Test Case Builder from the `Support Workbench` page in Enterprise Manager.

You can access the `Support Workbench` page in either of the following ways:

- In the Database Home page of Enterprise Manager, under `Diagnostic Summary`, click the link to `Active Incidents` (indicating the number of active incidents). This opens the `Support Workbench` page, with the incidents listed in a table.
- Click Advisor Central under `Related Links` to open the `Advisor Central` page. Next, click SQL Advisors and then Click here to go to Support Workbench to open the `Support Workbench` page.

From the `Support Workbench` page, to access the SQL Test Case Builder:

1. Click an incident ID to open the problem details for the particular incident.
2. Next, click Oracle Support in the `Investigate and Resolve` section.
3. Click Generate Additional Dumps and Test Cases.
4. For a particular incident, click the icon in the `Go To Task` column to run the SQL Test Case Builder.
	The output of the SQL Test Case Builder is a SQL script that contains the commands required to re-create all the necessary objects and the environment. SQL Test Case Builder stores the file in the following location, where inc\_num refers to the incident number and run\_num refers to the run number:
	```
	$ADR_HOME/incident/incdir_inc_num/SQLTCB_run num
	```
	For example, a valid output file name could be as follows:
	```
	$ORACLE_HOME/log/diag/rdbms/dbsa/dbsa/incident/incdir_2657/SQLTCB_1
	```

#### 16.6.1.2 Accessing SQL Test Case Builder Using DBMS\_SQLDIAG

You can also invoke the SQL Test Case Builder manually, using the `DBMS_SQLDIAG` package. This package consists of various subprograms for the SQL Test Case Builder, some of which are listed in Table 16-1.

Table 16-1 SQL Test Case Builder Procedures in DBMS\_SQLDIAG

| Procedure Name | Function |
| --- | --- |
| `EXPORT_SQL_TESTCASE` | Generates a SQL test case |
| `EXPORT_SQL_TESTCASE_DIR_BY_INC` | Generates a SQL test case corresponding to the incident ID passed as an argument |
| `EXPORT_SQL_TESTCASE_DIR_BY_TXT` | Generates a SQL test case corresponding to the SQL text passed as an argument |

For more information on this package and all of its procedures and parameters, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm).