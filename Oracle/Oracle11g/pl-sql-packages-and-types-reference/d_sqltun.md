---
title: DBMS_SQLTUNE
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_sqltun.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 140 DBMS\_SQLTUNE

The `DBMS_SQLTUNE` package is the interface for tuning SQL on demand. The related package `DBMS_AUTO_SQLTUNE` package provides the interface for SQL Tuning Advisor run as an automated task.

The chapter contains the following topics:

---

## Using DBMS\_SQLTUNE

- Overview
- Security Model

---

### Overview

The `DBMS_SQLTUNE` package provides a number interrelated areas of functionality:

- SQL Tuning Advisor Subprograms
- SQL Profile Subprograms
- SQL Tuning Set Subprograms
- Real-time SQL Monitoring Subprograms

SQL Tuning Advisor

The SQL Tuning Advisor is one of a suite of Advisors, a set of expert systems that identifies and helps resolve database performance problems. Specifically, the SQL Tuning Advisor automates the tuning process of problematic SQL statements. That is, it takes one or more SQL statements as input and gives precise advice on how to tune the statements. The advice is provided is in the form of precise SQL actions for tuning the SQL along with their expected performance benefit.

The group of SQL Tuning Advisor Subprograms provide a task-oriented interface that lets you access the Advisor. You can call the following subprograms in the order given to use some of the SQL Tuning Advisor's features:

1. You use the CREATE\_TUNING\_TASK Functions to create a tuning task for tuning a single statement or a group of SQL statements.
2. The EXECUTE\_TUNING\_TASK Function & Procedure executes a previously created tuning task.
3. The REPORT\_TUNING\_TASK Function displays the results of a tuning task.
4. You use the SCRIPT\_TUNING\_TASK Function to create a SQL\*PLUS script which can then be executed to implement a set of Advisor recommendations

SQL Profile Subprograms

The SQL Tuning Advisor may recommend the creation of a SQL profile to improve the performance of a statement. SQL profiles consist of auxiliary statistics specific to the statement. The query optimizer makes estimates about cardinality, selectivity, and cost that can sometimes be off by a significant amount, resulting in poor execution plans. The SQL profile addresses this problem by collecting additional information using sampling and partial execution techniques to adjust these estimates.

The group of SQL Profile Subprograms provides a mechanism for delivering statistics to the optimizer that targets one particular SQL statement, and helps the optimizer make good decisions for that statement by giving it the most accurate statistical information possible. For example:

- You can use the ACCEPT\_SQL\_PROFILE Procedure and Function to accept a SQL profile recommended by the SQL Tuning Advisor.
- You can alter the `STATUS`, `NAME`, `DESCRIPTION`, and `CATEGORY` attributes of an existing SQL profile with the ALTER\_SQL\_PROFILE Procedure.
- You can drop a SQL profile with the DROP\_SQL\_PROFILE Procedure.

SQL Tuning Sets

The SQL Tuning Advisor input can be a single SQL statement or a set of statements. When tuning multiple statements in one advisor task, you give the input in the form of a SQL tuning set (STS). A SQL tuning set is a database object that stores SQL statements along with their execution context in a system-provided schema. SQL tuning sets provide an infrastructure for dealing with SQL workloads and simplify tuning of a large number of SQL statements.

SQL tuning sets store SQL statements along with

- The execution context, such as the parsing schema name and bind values
- Execution statistics such as average elapsed time and execution count
- Execution plans - which are the sequence of operations Oracle performs to run SQL statements
- Row source statistics such as the number of rows processed for each operation executed within the plan

SQL tuning sets can be created by filtering or ranking SQL statements from several sources:

- The cursor cache using the SELECT\_CURSOR\_CACHE Function
- Top SQL statements from the Automatic Workload Repository using the SELECT\_WORKLOAD\_REPOSITORY Functions
- Other SQL tuning sets using the SELECT\_SQLSET Function
- SQL Performance Analyzer task comparison results using the SELECT\_SQLPA\_TASK Function
- SQL Trace files using the SELECT\_SQL\_TRACE Function
- A user-defined workload

The complete group of SQL Tuning Set Subprograms facilitates this functionality. As examples:

- You use the CREATE\_SQLSET Procedure and Function to creates a SQL tuning set object in the database
- The LOAD\_SQLSET Procedure populates the SQL tuning set with a set of selected SQL
- The CAPTURE\_CURSOR\_CACHE\_SQLSET Procedure collects SQL statements from the cursor cache over a specified time interval, attempting to build a realistic picture of system workload.

Import/Export SQL Tuning Sets and SQL Profiles

You use `DBMS_SQLTUNE` subprograms to move SQL profiles and SQL tuning sets from one system to another using a common programmatic model. In both cases, you create a staging table on the source system and populate that staging table with the relevant data. You then move that staging table to the destination system following the method of your choice (such as datapump, import/export, or database link), where it is used to reconstitute the objects in their original form. These steps are implemented by means of subprograms included in this package:

1. Call the CREATE\_STGTAB\_SQLPROF Procedure or the CREATE\_STGTAB\_SQLSET Procedure to create the staging table on the source system.
2. Call the PACK\_STGTAB\_SQLPROF Procedure or PACK\_STGTAB\_SQLSET Procedure to populate the staging table with information from the source system.
3. Once you have moved the staging table to the destination system, you call the UNPACK\_STGTAB\_SQLPROF Procedure or the UNPACK\_STGTAB\_SQLSET Procedure to recreate the object on the new system.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/sql_tune.htm#PFGRF02802) for more information about programmatic flow

Automatic Tuning Task Functions

The automated system task `SYS_AUTO_SQL_TUNING_TASK` is created by the database as part of the catalog scripts. This task automatically chooses a set of high-load SQL from AWR and runs the SQL Tuning Advisor on this SQL. The automated task performs the same comprehensive analysis as any other SQL Tuning task.

You can obtain a report on the activity of the Automatic SQL Tuning task through the `DBMS_AUTO_SQLTUNE.REPORT_AUTO_TUNING_TASK` API. See the `DBMS_AUTO_SQLTUNE` package for the list of subprograms that you can use to manage the automated SQL tuning task.

See Also:

[Using DBMS\_AUTO\_SQLTUNE](d_autosta.md)

Real-time SQL Monitoring

Real-time SQL Monitoring allows DBAs or performance analysts to monitor the execution of long-running SQL statements while they are executing. Both cursor statistics (such as CPU times and IO times) and execution plan statistics (such as number of output rows, memory and temp space used) are updated close to real-time during statement execution. These statistics are exposed by the `V$SQL_MONITOR` and `V$SQL_PLAN_MONITOR` views. In addition, `DBMS_SQLTUNE` provides a subprogram `REPORT_SQL_MONITOR` to report on monitoring information.

---

### Security Model

This package is available to `PUBLIC` and performs its own security checking:

- As the SQL Tuning advisor relies on the advisor framework, all tuning task interfaces (`XXX_TUNING_TASK`) require privilege `ADVISOR`.
- SQL tuning set subprograms (`XXX_SQLSET`) require either the `ADMINISTER` `SQL` `TUNING` `SET` or the `ADMINISTER` `ANY` `SQL` `TUNING` `SET` privilege. Users having the `ADMINISTER` `SQL` `TUNING` `SET` privilege can only create and modify a SQL tuning set they own, while the `ADMINISTER` `ANY` `SQL` `TUNING` `SET` privilege allows them to operate upon all SQL tuning sets, even those owned by other users. For example, using the CREATE\_SQLSET Procedure and Function you can create a SQL tuning set to be owned by another user. In this case, the user need not necessarily have the `ADMINISTER` `SQL` `TUNING` `SET` privilege to operate upon her tuning set.
- Previously, three different privileges were needed to invoke subprograms concerned with SQL profiles:
	- `CREATE` `ANY` `SQL` `PROFILE`
		- `ALTER` `ANY` `SQL` `PROFILE`
		- `DROP` `ANY` `SQL` `PROFILE`
	These have now been deprecated in favor of `ADMINISTER` `SQL` `MANAGEMENT` `OBJECT`

---

## Data Structures

The `DBMS_SQLTUNE` package defines the following `OBJECT` type

Object Types

- SQLSET\_ROW Object Type

---

### SQLSET\_ROW Object Type

The `SQLSET_ROW` object models the content of a SQL tuning set for the user. Logically, a SQL tuning set is a collection of `SQLSET_ROW` s where each `SQLSET_ROW` contains a single SQL statement along with its execution context, statistics, binds, and plan. The `SELECT_XXX` subprograms each model a data source as a collection of `SQLSET_ROWs`, unique by (`sql_id`, `plan_hash_value`). Similarly, the `LOAD_SQLSET` procedure takes as input a cursor whose row type is `SQLSET_ROW`, treating each `SQLSET_ROW` in isolation according to the policies requested by the user.

Several subprograms in the `DBMS_SQLTUNE` package accept basic filters on the content of a SQL tuning set or data source. These filters are expressed in terms of the attributes within the `SQLSET_ROW` as defined.

Syntax

```
CREATE TYPE sqlset_row AS object (
  sql_id                   VARCHAR(13),
  force_matching_signature NUMBER,
  sql_text                 CLOB,
  object_list              sql_objects,
  bind_data                RAW(2000),
  parsing_schema_name      VARCHAR2(30),
  module                   VARCHAR2(48),
  action                   VARCHAR2(32),
  elapsed_time             NUMBER,
  cpu_time                 NUMBER,
  buffer_gets              NUMBER,
  disk_reads               NUMBER,
  direct_writes            NUMBER,
  rows_processed           NUMBER,
  fetches                  NUMBER,
  executions               NUMBER,
  end_of_fetch_count       NUMBER,
  optimizer_cost           NUMBER,
  optimizer_env            RAW(2000),
  priority                 NUMBER,
  command_type             NUMBER,
  first_load_time          VARCHAR2(19),
  stat_period              NUMBER,
  active_stat_period       NUMBER,
  other                    CLOB,
  plan_hash_value          NUMBER,
  sql_plan                 sql_plan_table_type,
  bind_list                sql_binds)
```

Attributes

Table 140-1 SQLSET\_ROW Attributes

| Attribute | Description |
| --- | --- |
| `sql_id` | Unique SQL ID |
| `forcing_matching_signature` | Signature with literals, case, and whitespace removed |
| `sql_text` | Full text for the statement |
| `object_list` | Currently not implemented |
| `bind_data` | Bind data as captured for this SQL. Note that you cannot stipulate an argument for this parameter and also for `bind_list` - they are mutually exclusive. |
| `parsing_schema_name` | Schema where the SQL is parsed |
| `module` | Last application module for the SQL |
| `action` | Last application action for the SQL |
| `elapsed_time` | Sum total elapsed time for this SQL statement |
| `cpu_time` | Sum total CPU time for this SQL statement |
| `buffer_gets` | Sum total number of buffer gets |
| `disk_reads` | Sum total number of disk reads |
| `direct_writes` | Sum total number of direct writes |
| `rows_processed` | Sum total number of rows processed by this SQL |
| `fetches` | Sum total number of fetches |
| `executions` | Total executions of this SQL |
| `end_of_fetch_count` | Number of times the statement was fully executed with all of its rows fetched |
| `optimizer_cost` | Optimizer cost for this SQL |
| `optimizer_env` | Optimizer environment for this SQL statement |
| `priority` | User-defined priority (1,2,3) |
| `command_type` | Statement type, such as `INSERT` or `SELECT`. |
| `first_load_time` | Load time of parent cursor |
| `stat_period` | Period of time (seconds) when the statistics of this SQL statement were collected |
| `active_stat_period` | Effective period of time (in seconds) during which the SQL statement was active |
| `other` | Other column for user defined attributes |
| `plan_hash_value` | Plan hash value of the plan |
| `sql_plan` | Explain plan |
| `bind_list` | List of user specified binds for SQL This is used for user-specified workloads. Note that you cannot stipulate an argument for this parameter and also for `bind_data` - they are mutually exclusive. |

---

## Subprogram Groups

`DBMS_SQLTUNE` subprograms are grouped by function:

- SQL Tuning Advisor Subprograms
- SQL Profile Subprograms
- SQL Tuning Set Subprograms
- Real-time SQL Monitoring Subprograms
- SQL Performance Reporting Subprograms

---

### SQL Tuning Advisor Subprograms

This subprogram group provides an interface to manage SQL tuning tasks.

Table 140-2 SQL Tuning Task Subprograms

| Subprogram | Description |
| --- | --- |
| CANCEL\_TUNING\_TASK Procedure | Cancels the currently executing tuning task |
| CREATE\_SQL\_PLAN\_BASELINE Procedure | Creates a SQL plan baseline for an existing plan |
| CREATE\_TUNING\_TASK Functions | Creates a tuning of a single statement or SQL tuning set for either the SQL Tuning Advisor |
| DROP\_TUNING\_TASK Procedure | Drops a SQL tuning task |
| EXECUTE\_TUNING\_TASK Function & Procedure | Executes a previously created tuning task |
| IMPLEMENT\_TUNING\_TASK Function | Implements a set of SQL profile recommendations made by the SQL Tuning Advisor |
| INTERRUPT\_TUNING\_TASK Procedure | Interrupts the currently executing tuning task |
| REPORT\_AUTO\_TUNING\_TASK Function | Displays a report from the automatic tuning task, reporting on a range of executions |
| REPORT\_TUNING\_TASK Function | Displays the results of a tuning task |
| RESET\_TUNING\_TASK Procedure | Resets the currently executing tuning task to its initial state |
| RESUME\_TUNING\_TASK Procedure | Resumes a previously interrupted task that was created to process a SQL tuning set |
| SCRIPT\_TUNING\_TASK Function | Creates a SQL\*PLUS script which can then be executed to implement a set of SQL Tuning Advisor recommendations |
| SET\_TUNING\_TASK\_PARAMETER Procedures | Updates the value of a SQL tuning parameter of type `VARCHAR2` or `NUMBER` |

The Summary of DBMS\_SQLTUNE Subprograms contains a complete listing of all subprograms in the package.

---

### SQL Profile Subprograms

This subprogram group provides an interface to manage SQL profiles.

Table 140-3 SQL Profile Subprograms

| Subprogram | Description |
| --- | --- |
| ACCEPT\_SQL\_PROFILE Procedure and Function | Creates a SQL profile for the specified tuning task |
| ALTER\_SQL\_PROFILE Procedure | Alters specific attributes of an existing SQL profile object |
| CREATE\_STGTAB\_SQLPROF Procedure | Creates the staging table used for copying SQL profiles from one system to another |
| DROP\_SQL\_PROFILE Procedure | Drops the named SQL profile from the database |
| PACK\_STGTAB\_SQLPROF Procedure | Moves profile data out of the `SYS` schema into the staging table |
| REMAP\_STGTAB\_SQLPROF Procedure | Changes the profile data values kept in the staging table prior to performing an unpack operation |
| SQLTEXT\_TO\_SIGNATURE Function | Returns a SQL text's signature |
| UNPACK\_STGTAB\_SQLPROF Procedure | Uses the profile data stored in the staging table to create profiles on this system |

The Summary of DBMS\_SQLTUNE Subprograms contains a complete listing of all subprograms in the package.

---

### SQL Tuning Set Subprograms

This subprogram group provides an interface to manage SQL tuning sets.

Table 140-4 SQL Tuning Set Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_SQLSET\_REFERENCE Function | Adds a new reference to an existing SQL tuning set to indicate its use by a client |
| CAPTURE\_CURSOR\_CACHE\_SQLSET Procedure | Over a specified time interval incrementally captures a workload from the cursor cache into a SQL tuning set |
| CREATE\_SQLSET Procedure and Function | Creates a SQL tuning set object in the database |
| CREATE\_STGTAB\_SQLSET Procedure | Creates a staging table through which SQL Tuning Sets are imported and exported |
| DELETE\_SQLSET Procedure | Deletes a set of SQL statements from a SQL tuning set |
| DROP\_SQLSET Procedure | Drops a SQL tuning set if it is not active |
| LOAD\_SQLSET Procedure | Populates the SQL tuning set with a set of selected SQL |
| PACK\_STGTAB\_SQLSET Procedure | Copies tuning sets out of the `SYS` schema into the staging table |
| REMOVE\_SQLSET\_REFERENCE Procedure | Deactivates a SQL tuning set to indicate it is no longer used by the client |
| SELECT\_CURSOR\_CACHE Function | Collects SQL statements from the cursor cache |
| SELECT\_SQL\_TRACE Function | Reads the content of one or more trace files and returns the SQL statements it finds in the format of `sqlset_row` |
| SELECT\_SQLPA\_TASK Function | Collects SQL statements from a SQL performance analyzer comparison task |
| SELECT\_SQLSET Function | Collects SQL statements from an existing SQL tuning set |
| SELECT\_WORKLOAD\_REPOSITORY Functions | Collects SQL statements from the workload repository |
| UNPACK\_STGTAB\_SQLSET Procedure | Copies one or more SQL tuning sets from the staging table |
| UPDATE\_SQLSET Procedures | Updates whether selected string fields for a SQL statement in a SQL tuning set or the set numerical attributes of a SQL in a SQL tuning set |

The Summary of DBMS\_SQLTUNE Subprograms contains a complete listing of all subprograms in the package.

---

### Real-time SQL Monitoring Subprograms

This subprogram group provides function to report on monitoring data collected in `V$SQL_MONITOR` and `V$SQL_PLAN_MONITOR`.

Table 140-5 SQL Tuning Set Subprograms

| Subprogram | Description |
| --- | --- |
| REPORT\_SQL\_MONITOR Function | Reports on real-time SQL Monitoring |
| REPORT\_SQL\_MONITOR\_LIST Function | Builds a report for all or a sub-set of statements monitored by Oracle |

---

### SQL Performance Reporting Subprograms

This subprogram group provides detailed reports on SQL performance using statistics from the cursor cache and automatic workload repository (AWR).

Table 140-6 SQL Performance Reporting Subprograms

| Subprogram | Description |
| --- | --- |
| REPORT\_SQL\_DETAIL Function | Reports on a specific SQLID |

---

## Summary of DBMS\_SQLTUNE Subprograms

Table 140-7 DBMS\_SQLTUNE Package Subprograms

| Subprogram | Description | Group |
| --- | --- | --- |
| ACCEPT\_SQL\_PROFILE Procedure and Function | Create a SQL profile for the specified tuning task | SQL Profile Subprograms |
| ADD\_SQLSET\_REFERENCE Function | Adds a new reference to an existing SQL tuning set to indicate its use by a client | SQL Tuning Set Subprograms |
| ALTER\_SQL\_PROFILE Procedure | Alters specific attributes of an existing SQL profile object | SQL Profile Subprograms |
| CANCEL\_TUNING\_TASK Procedure | Cancels the currently executing tuning task | SQL Tuning Advisor Subprograms |
| CAPTURE\_CURSOR\_CACHE\_SQLSET Procedure | Over a specified time interval incrementally captures a workload from the cursor cache into a SQL tuning set | SQL Tuning Set Subprograms |
| CREATE\_SQL\_PLAN\_BASELINE Procedure | Creates a SQL plan baseline for an existing plan | SQL Tuning Advisor Subprograms |
| CREATE\_SQLSET Procedure and Function | Creates a SQL tuning set object in the database | SQL Tuning Set Subprograms |
| CREATE\_STGTAB\_SQLPROF Procedure | Creates the staging table used for copying SQL profiles from one system to another | SQL Profile Subprograms |
| CREATE\_STGTAB\_SQLSET Procedure | Creates a staging table through which SQL tuning sets are imported and exported | SQL Tuning Set Subprograms |
| CREATE\_TUNING\_TASK Functions | Creates a tuning of a single statement or SQL tuning set for either the SQL Tuning Advisor | SQL Tuning Advisor Subprograms |
| DELETE\_SQLSET Procedure | Deletes a set of SQL statements from a SQL tuning set | SQL Tuning Set Subprograms |
| DROP\_SQL\_PROFILE Procedure | Drops the named SQL profile from the database | SQL Profile Subprograms |
| DROP\_SQLSET Procedure | Drops a SQL tuning set if it is not active | SQL Tuning Set Subprograms |
| DROP\_TUNING\_TASK Procedure | Drops a SQL tuning task | SQL Tuning Advisor Subprograms |
| EXECUTE\_TUNING\_TASK Function & Procedure | Executes a previously created tuning task | SQL Tuning Advisor Subprograms |
| IMPLEMENT\_TUNING\_TASK Function | implements a set of SQL profile recommendations made by the SQL Tuning Advisor | SQL Tuning Advisor Subprograms |
| INTERRUPT\_TUNING\_TASK Procedure | Interrupts the currently executing tuning task | SQL Tuning Advisor Subprograms |
| LOAD\_SQLSET Procedure | Populates the SQL tuning set with a set of selected SQL | SQL Tuning Set Subprograms |
| PACK\_STGTAB\_SQLPROF Procedure | Moves profile data out of the `SYS` schema into the staging table | SQL Profile Subprograms |
| PACK\_STGTAB\_SQLSET Procedure | Moves tuning sets out of the `SYS` schema into the staging table | SQL Tuning Set Subprograms |
| REMAP\_STGTAB\_SQLPROF Procedure | Changes the profile data values kept in the staging table prior to performing an unpack operation | SQL Profile Subprograms |
| REMAP\_STGTAB\_SQLSET Procedure | Changes the tuning set names and owners in the staging table so that they can be unpacked with different values than they had on the host system | SQL Tuning Set Subprograms |
| REMOVE\_SQLSET\_REFERENCE Procedure | Deactivates a SQL tuning set to indicate it is no longer used by the client | SQL Tuning Set Subprograms |
| REPORT\_AUTO\_TUNING\_TASK Function | Displays a report from the automatic tuning task, reporting on a range of subtasks | SQL Tuning Set Subprograms |
| REPORT\_SQL\_DETAIL Function | Reports on a specific SQLID | SQL Performance Reporting Subprograms |
| REPORT\_SQL\_MONITOR Function | Displays a report on real-time SQL monitoring | Real-time SQL Monitoring Subprograms |
| REPORT\_SQL\_MONITOR\_LIST Function | Builds a report for all or a sub-set of statements monitored by Oracle | Real-time SQL Monitoring Subprograms |
| REPORT\_TUNING\_TASK Function | Displays the results of a tuning task | SQL Tuning Set Subprograms |
| RESET\_TUNING\_TASK Procedure | Resets the currently executing tuning task to its initial state | SQL Tuning Advisor Subprograms |
| RESUME\_TUNING\_TASK Procedure | Resumes a previously interrupted task that was created to process a SQL tuning set | SQL Tuning Advisor Subprograms |
| SCRIPT\_TUNING\_TASK Function | Creates a SQL\*PLUS script which can then be executed to implement a set of SQL Tuning Advisor recommendations | SQL Tuning Advisor Subprograms |
| SELECT\_CURSOR\_CACHE Function | Collects SQL statements from the cursor cache | SQL Tuning Set Subprograms |
| SELECT\_SQL\_TRACE Function | Reads the content of one or more trace files and returns the SQL statements it finds in the format of `sqlset_row` | SQL Tuning Set Subprograms |
| SELECT\_SQLSET Function | Collects SQL statements from an existing SQL tuning set | SQL Tuning Set Subprograms |
| SELECT\_WORKLOAD\_REPOSITORY Functions | Collects SQL statements from the workload repository | SQL Tuning Set Subprograms |
| SET\_TUNING\_TASK\_PARAMETER Procedures | Updates the value of a SQL tuning parameter of type `VARCHAR2` or `NUMBER` | SQL Tuning Advisor Subprograms |
| SQLTEXT\_TO\_SIGNATURE Function | Returns a SQL text's signature | SQL Profile Subprograms |
| UNPACK\_STGTAB\_SQLPROF Procedure | Uses the profile data stored in the staging table to create profiles on this system | SQL Profile Subprograms |
| UNPACK\_STGTAB\_SQLSET Procedure | Moves one or more SQL tuning sets from the staging table | SQL Tuning Set Subprograms |
| UPDATE\_SQLSET Procedures | Updates selected fields for a SQL statement in a SQL tuning set | SQL Tuning Set Subprograms |

---

### ACCEPT\_SQL\_PROFILE Procedure and Function

This procedure creates a SQL profile recommended by the SQL Tuning Advisor. The SQL text is normalized for matching purposes though it is stored in the data dictionary in de-normalized form for readability. SQL text is provided through a reference to the SQL Tuning task. If the referenced SQL statement doesn't exist, an error is reported.

See Also:

SQL Profile Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.ACCEPT_SQL_PROFILE (
   task_name    IN  VARCHAR2,
   object_id    IN  NUMBER   := NULL,
   name         IN  VARCHAR2 := NULL,
   description  IN  VARCHAR2 := NULL,
   category     IN  VARCHAR2 := NULL);
   task_owner   IN VARCHAR2  := NULL,
   replace      IN BOOLEAN   := FALSE,
   force_match  IN BOOLEAN   := FALSE,
   profile_type IN VARCHAR2  := REGULAR_PROFILE);
```
```
DBMS_SQLTUNE.ACCEPT_SQL_PROFILE (
   task_name    IN  VARCHAR2,
   object_id    IN  NUMBER   := NULL,
   name         IN  VARCHAR2 := NULL,
   description  IN  VARCHAR2 := NULL,
   category     IN  VARCHAR2 := NULL;
   task_owner   IN VARCHAR2  := NULL,
   replace      IN BOOLEAN   := FALSE,
   force_match  IN BOOLEAN   := FALSE,
   profile_type IN VARCHAR2  := REGULAR_PROFILE)
 RETURN VARCHAR2;
```

Parameters

Table 140-8 ACCEPT\_SQL\_PROFILE Procedure and Function Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | The (mandatory) name of the SQL tuning task |
| `object_id` | The identifier of the advisor framework object representing the SQL statement associated with the tuning task |
| `name` | The name of the SQL profile. It cannot contain double quotation marks. The name is case sensitive. If not specified, the system generates a unique name for the SQL profile. |
| `description` | A user specified string describing the purpose of the SQL profile. The description is truncated if longer than 256 characters. The maximum size is 500 characters. |
| `category` | This is the category name which must match the value of the `SQLTUNE_CATEGORY` parameter in a session for the session to use this SQL profile. It defaults to the value " `DEFAULT` ". This is also the default of the `SQLTUNE_CATEGORY` parameter. The category must be a valid Oracle identifier. The category name specified is always converted to upper case. The combination of the normalized SQL text and category name creates a unique key for a SQL profile. An `ACCEPT_SQL_PROFILE` fails if this combination is duplicated. |
| `task_owner` | Owner of the tuning task. This is an optional parameter that has to be specified to accept a SQL profile associated to a tuning task owned by another user. The current user is the default value. |
| `replace` | If the profile already exists, it is replaced if this argument is `TRUE`. It is an error to pass a name that is already being used for another signature/category pair, even with replace set to `TRUE`. |
| `force_match` | If `TRUE` this causes SQL profiles to target all SQL statements which have the same text after normalizing all literal values into bind variables. (Note that if a combination of literal values and bind values is used in a SQL statement, no bind transformation occurs.) This is analogous to the matching algorithm used by the `FORCE` option of the `cursor_sharing` parameter.  If `FALSE`, literals are not transformed. This is analogous to the matching algorithm used by the `EXACT` option of the `cursor_sharing` parameter. |
| `profile_type` | Options:  - `REGULAR_PROFILE` - profile without a change to parallel execution (Default, equivalent to `NULL`). Note that if the SQL statement currently has a parallel execution plan, the regular profile will cause the optimizer to choose a different, but still parallel, execution plan. - `PX_PROFILE` - regular profile with a change to parallel execution |

Return Values

The name of the SQL profile.

Usage Notes

The `CREATE` `ANY` `SQL PROFILE` privilege is required.

Examples

You use both the procedure and the function versions of the subprogram in the same way except you must specify a return value to invoke the function. Here we give examples of the procedure only.

In this example, you tune a single SQL statement form the workload repository and you create the SQL profile recommended by SQL Tuning Advisor.

```
variable stmt_task VARCHAR2(64);
variable sts_task VARCHAR2(64);
 
-- create a tuning task tune the statement 
EXEC :stmt_task := DBMS_SQLTUNE.CREATE_TUNING_TASK(
   begin_snap  => 1, -
   end_snap    => 2, -
   sql_id      => 'ay1m3ssvtrh24');
 
-- execute the resulting task 
EXEC DBMS_SQLTUNE.EXECUTE_TUNING_TASK(:stmt_task);
 
EXEC DBMS_SQLTUNE.ACCEPT_SQL_PROFILE(:stmt_task);
```

Note that you do not have to specify the ID (that is, `object_id`) for the advisor framework object created by SQL Tuning Advisor to represent the tuned SQL statement.

You might also want to accept the recommended SQL profile in a different category, (for example, `TEST`), so that it is not used by default.

```
EXEC DBMS_SQLTUNE.ACCEPT_SQL_PROFILE (
   task_name  =>  :stmt_task, -
   category   =>  'TEST');
```

You can use command `ALTER` `SESSION` `SET` `SQLTUNE_CATEGORY` = `'TEST'` to see how this profile behaves.

The following call creates a SQL profile that targets any SQL statement with the same `force_matching_signature` as the tuned statement.

```
EXEC DBMS_SQLTUNE.ACCEPT_SQL_PROFILE (task_name   =>  :stmt_task, -
                                      force_match =>  TRUE);
```

In the following example, you tune a SQL tuning set, and you create a SQL profile for only one of the SQL statements in the SQL tuning set. The SQL statement is represented by an advisor framework object with ID equal to '5'. Please notice that you must pass an object id to the `ACCEPT_SQL_PROFILE` procedure because there are potentially many SQL profiles for the tuning task. This object id is given along with the report.

```
EXEC :sts_task := DBMS_SQLTUNE.CREATE_TUNING_TASK ( -
  sqlset_name   => 'my_workload',  -
  rank1         => 'ELAPSED_TIME', -
  time_limit    => 3600,           -
  description   => 'my workload ordered by elapsed time');
 
-- execute the resulting task 
EXEC DBMS_SQLTUNE.EXECUTE_TUNING_TASK(:sts_task);

 -- create the profile for the sql statement corresponding to object_id = 5.
EXEC DBMS_SQLTUNE.ACCEPT_SQL_PROFILE (
   task_name  =>  :sts_task, -
   object_id  =>  5);
```

---

### ADD\_SQLSET\_REFERENCE Function

This procedure adds a new reference to an existing SQL tuning set to indicate its use by a client.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.ADD_SQLSET_REFERENCE (
   sqlset_name  IN  VARCHAR2,
   description  IN  VARCHAR2 := NULL)
 RETURN NUMBER;
```

Parameters

Table 140-9 ADD\_SQLSET\_REFERENCE Function Parameters

| Parameter | Description |
| --- | --- |
| `sqlset_name` | The SQL tuning set name |
| `description` | The description of the usage of SQL tuning set. The description is truncated if longer than 256 characters. |

Return Values

The identifier of the added reference.

Examples

You can add reference to a SQL tuning set. This prevents the tuning set from being modified while it is being used. References are automatically added when you invoke SQL Tuning Advisor on the SQL tuning set, so you should use this function for custom purposes only.The function returns a reference ID that is used to remove it later. You use the `REMOVE_SQLSET_REFERENCE Procedure` to delete references to a SQL tuning set.

```
variable rid number; 
EXEC :rid := DBMS_SQLTUNE.ADD_SQLSET_REFERENCE( -
                                sqlset_name => 'my_workload', -
                                description => 'my sts reference');
```

You can use the views `USER/DBA_SQLSET_REFERENCES` to find all references on a given SQL tuning set.

---

### ALTER\_SQL\_PROFILE Procedure

This procedure alters specific attributes of an existing SQL profile object. The following attributes can be altered (using these attribute names):

- " `STATUS` " can be set to " `ENABLED` " or " `DISABLED` "
- " `NAME` " can be reset to a valid name which must be a valid Oracle identifier and must be unique.
- " `DESCRIPTION` " can be set to any string of size no more than 500 characters
- " `CATEGORY` " can be reset to a valid category name which must be a valid Oracle identifier and must be unique when combined with normalized SQL text)

See Also:

SQL Profile Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.ALTER_SQL_PROFILE (
   name                 IN  VARCHAR2,
   attribute_name       IN  VARCHAR2,
   value                IN  VARCHAR2);
```

Parameters

Table 140-10 ALTER\_SQL\_PROFILE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | The (mandatory) name of the existing SQL profile to alter |
| `attribute_name` | The (mandatory) attribute name to alter (case insensitive) using valid attribute names |
| `value` | The (mandatory) new value of the attribute using valid attribute values |

Usage Notes

Requires the `ALTER` `ANY` `SQL PROFILE` privilege.

Examples

```
-- Disable a profile, so it is not be used by any sessions.
EXEC DBMS_SQLTUNE.ALTER_SQL_PROFILE ( name            =>  :pname,   -
                                      attribute_name  =>  'STATUS', -
                                      value           =>  'DISABLED');
 
-- Enable it back:
EXEC DBMS_SQLTUNE.ALTER_SQL_PROFILE ( name            =>   :pname,   -
                                      attribute_name  =>   'STATUS', -
                                      value           =>   'ENABLED');
 
-- Change the category of the profile so it is used only by sessions
-- with category set to TEST.
-- Use ALTER SESSION SET SQLTUNE_CATEGORY = 'TEST' to see how this profile 
-- behaves.
EXEC DBMS_SQLTUNE.ALTER_SQL_PROFILE ( name            =>  :pname,   -
                                      attribute_name  =>  'CATEGORY', -
                                      value           =>  'TEST');
 
-- Change it back:
EXEC DBMS_SQLTUNE.ALTER_SQL_PROFILE ( name            =>  :pname,   -
                                      attribute_name  =>  'CATEGORY', -
                                      value           =>  'DEFAULT');
```

---

### CANCEL\_TUNING\_TASK Procedure

This procedure cancels the currently executing tuning task. All intermediate result data is deleted.

See Also:

SQL Tuning Advisor Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.CANCEL_TUNING_TASK(
 task_name         IN VARCHAR2);
```

Parameters

Table 140-11 CANCEL\_TUNING\_TASK Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | The name of the task to cancel |

Examples

You cancel a task when you need to stop it executing and do not require to view any already-completed results.

```
EXEC DBMS_SQLTUNE.CANCEL_TUNING_TASK(:my_task);
```

---

### CAPTURE\_CURSOR\_CACHE\_SQLSET Procedure

Over a specified time interval this procedure incrementally captures a workload from the cursor cache into a SQL tuning set. The procedure captures a workload from the cursor cache into a SQL tuning set, polling the cache multiple times over a time period and updating the workload data stored there. It can execute over as long a period as required to capture an entire system workload.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.CAPTURE_CURSOR_CACHE_SQLSET (
    sqlset_name         IN VARCHAR2, 
    time_limit          IN POSITIVE := 1800,
    repeat_interval     IN POSITIVE := 300,
    capture_option      IN VARCHAR2 := 'MERGE',
    capture_mode        IN NUMBER   := MODE_REPLACE_OLD_STATS,
    basic_filter        IN VARCHAR2 := NULL,
    sqlset_owner        IN VARCHAR2 := NULL,
    recursive_sql       IN VARCHAR2 := HAS_RECURSIVE_SQL);
```

Parameters

Table 140-12 CAPTURE\_CURSOR\_CACHE\_SQLSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sqlset_name` | The SQL tuning set name |
| `time_limit` | The total amount of time, in seconds, to execute |
| `repeat_interval` | The amount of time, in seconds, to pause between sampling |
| `capture_option` | During capture, either insert new statements, update existing statements, or both. ' `INSERT` ', ' `UPDATE` ', or ' `MERGE` ' just like `load_option` in `load_sqlset` |
| `capture_mode` | Capture mode (`UPDATE` and `MERGE` capture options). Possible values:  - `MODE_REPLACE_OLD_STATS` - Replace statistics when the number of executions seen is greater than that stored in the SQL tuning set - `MODE_ACCUMULATE_STATS` - Add new values to current values for SQL we already store. Note that this mode detects if a statement has been aged out, so the final value for a statistics is the sum of the statistics of all cursors that statement existed under. |
| `basic_filter` | Filter to apply to cursor cache on each sampling (see `SELECT_XXX` subprograms). If `basic_filter` is not set by the caller, the subprogram captures only statements of the type `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, and `MERGE`. |
| `sqlset_owner` | The owner of the SQL tuning set or `NULL` for current schema owner |
| `recursive_sql` | Filter that includes recursive SQL in the SQL tuning set (`HAS_RECURSIVE_SQL`) or excludes it (`NO_RECURSIVE_SQL`). |

Examples

In this example capture takes place over a 30-second period, polling the cache once every five seconds. This captures all statements run during that period but not before or after. If the same statement appears a second time, the process replaces the stored statement with the new occurrence.

Note that in production systems the time limit and repeat interval would be set much higher. You should tune the `time_limit` and `repeat_interval` parameters based on the workload time and cursor cache turnover properties of your system.

```
EXEC DBMS_SQLTUNE.CAPTURE_CURSOR_CACHE_SQLSET( -
                                        sqlset_name     => 'my_workload', -
                                        time_limit      =>  30, -
                                        repeat_interval =>  5);
```

In the following call you accumulate execution statistics as you go. This option produces an accurate picture of the cumulative activity of each cursor, even across age-outs, but it is more expensive than the previous example.

```
EXEC DBMS_SQLTUNE.CAPTURE_CURSOR_CACHE_SQLSET( -
                         sqlset_name     => 'my_workload', -
                         time_limit      => 30, -
                         repeat_interval => 5, -
                         capture_mode    => dbms_sqltune.MODE_ACCUMULATE_STATS);
```

This call performs a very inexpensive capture where you only insert new statements and do not update their statistics once they have been inserted into the SQL tuning set

```
EXEC DBMS_SQLTUNE.CAPTURE_CURSOR_CACHE_SQLSET( -
                                    sqlset_name     => 'my_workload', -
                                    time_limit      => 30, -
                                    repeat_interval => 5, -
                                    capture_option  => 'INSERT');
```

---

### CREATE\_SQL\_PLAN\_BASELINE Procedure

This procedure creates a SQL plan baseline for an execution plan. It can be used in the context of an Alternative Plan Finding made by the SQL Tuning Advisor.

See Also:

SQL Tuning Advisor Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.CREATE_SQL_PLAN_BASELINE (
   task_name            IN VARCHAR2,
   object_id            IN NUMBER := NULL,
   plan_hash_value      IN NUMBER,
   owner_name           IN VARCHAR2 := NULL);
```

Parameters

Table 140-13 CREATE\_SQL\_PLAN\_BASELINE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task for which to get a script |
| `object_id` | Object ID to which the SQL corresponds |
| `plan_hash_value` | Plan to create plan baseline |
| owner\_name | Owner of the relevant tuning task. Defaults to the current schema owner. |

---

### CREATE\_SQLSET Procedure and Function

The procedure creates a SQL tuning set object in the database.

The function causes the system to generate a name for the SQL tuning set.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.CREATE_SQLSET (
   sqlset_name  IN  VARCHAR2,
   description  IN  VARCHAR2 := NULL
   sqlset_owner IN  VARCHAR2 := NULL);
```
```
DBMS_SQLTUNE.CREATE_SQLSET (
   sqlset_name  IN  VARCHAR2 := NULL,
   description  IN  VARCHAR2 := NULL,
   sqlset_owner IN  VARCHAR2 := NULL)
 RETURN VARCHAR2;
```

Parameters

Table 140-14 CREATE\_SQLSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sqlset_name` | The SQL tuning set name |
| `description` | The description of the SQL tuning set |
| `sqlset_owner` | The owner of the SQL tuning set, or `NULL` for the current schema owner |

Examples

```
EXEC DBMS_SQLTUNE.CREATE_SQLSET(- 
  sqlset_name => 'my_workload', -
  description => 'complete application workload');
```

---

### CREATE\_STGTAB\_SQLPROF Procedure

This procedure creates the staging table used for copying SQL profiles from one system to another.

See Also:

SQL Profile Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.CREATE_STGTAB_SQLPROF (
   table_name            IN VARCHAR2,
   schema_name           IN VARCHAR2 := NULL,
   tablespace_name       IN VARCHAR2 := NULL);
```

Parameters

Table 140-15 CREATE\_STGTAB\_SQLPROF Procedure Parameters

| Parameter | Description |
| --- | --- |
| `table_name` | The name of the table to create (case-insensitive unless double quoted). Required. |
| `schema_name` | The schema to create the table in, or `NULL` for current schema (case-insensitive unless double quoted) |
| `tablespace_name` | The tablespace to store the staging table within, or `NULL` for current user's default tablespace (case-insensitive unless double quoted) |

Usage Notes

- Call this procedure once before issuing a call to the PACK\_STGTAB\_SQLPROF Procedure.
- This procedure can be called multiple times if you would like to have different SQL profiles in different staging tables.
- Note that this is a DDL operation, so it does not occur within a transaction.

Examples

Create a staging table to store profile data that can be moved to another system.

```
EXEC DBMS_SQLTUNE.CREATE_STGTAB_SQLPROF (table_name  => 'PROFILE_STGTAB');
```

---

### CREATE\_STGTAB\_SQLSET Procedure

This procedure creates a staging table through which SQL tuning sets are imported and exported

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.CREATE_STGTAB_SQLSET (
   table_name           IN VARCHAR2,
   schema_name          IN VARCHAR2 := NULL,
   tablespace_name      IN VARCHAR2 := NULL,
   db_version           IN NUMBER   := NULL);
```

Parameters

Table 140-16 CREATE\_STGTAB\_SQLSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `table_name` | Name of the table to create (case-sensitive) |
| `schema_name` | Schema in which to create the table in, or `NULL` for current schema (case-sensitive) |
| `tablespace_name` | Tablespace in which to store the staging table, or `NULL` for current user's default tablespace (case-sensitive) |
| `db_version` | Database (DB) version determining the format of the staging table. User can also create an older DB version staging table to export STS to an older DB version. One of the following values:  - `NULL` (default) — current DB version - `STS_STGTAB_10_2_VERSION` — 10.2 DB version - `STS_STGTAB_11_1_VERSION` — 11.1 DB version - `STS_STGTAB_11_2_VERSION` — 11.2 DB version |

Usage Notes

- Call this procedure once before issuing a call to the PACK\_STGTAB\_SQLSET Procedure.
- This procedure can be called multiple times if you would like to have different tuning sets in different staging tables.
- Note that this is a DDL operation, so it does not occur within a transaction.
- Users issuing the call must have permission to `CREATE` `TABLE` in the schema provided and the relevant tablespace.
- Please note that the staging table contains nested table columns and indexes, so it should not be renamed.

Examples

Create a staging table for packing and eventually exporting a SQL tuning sets

```
EXEC DBMS_SQLTUNE.CREATE_STGTAB_SQLSET(table_name => 'STGTAB_SQLSET');
```

Create a staging table to pack a SQL tuning set in Oracle Database 10g Release 2 (10.2) format

```
EXEC DBMS_SQLTUNE.CREATE_STGTAB_SQLSET(
   table_name => 'STGTAB_SQLSET',
   db_version => DBMS_SQLTUNE.STS_STGTAB_10_2_VERSION)
```

Create a staging table to pack a SQL tuning set in Oracle Databasae 11g Release 1 (11.1) format

```
EXEC DBMS_SQLTUNE.CREATE_STGTAB_SQLSET(
   table_name => 'STGTAB_SQLSET',
   db_version => DBMS_SQLTUNE.STS_STGTAB_11_1_VERSION)
```

---

### CREATE\_TUNING\_TASK Functions

You can use different forms of this function to:

- Create a tuning task for a single statement given its text.
- Create a tuning task for a single statement from the Cursor Cache given its identifier.
- Create a tuning task for a single statement from the workload repository given a range of snapshot identifiers.
- Create a tuning task for a SQL tuning set.
- Create tuning task for a SQL Performance Analyzer

In all cases, the function mainly creates an advisor task and sets its parameters.

See Also:

SQL Tuning Advisor Subprograms for other subprograms in this group

Syntax

SQL text format:

```
DBMS_SQLTUNE.CREATE_TUNING_TASK(
  sql_text         IN CLOB,
  bind_list        IN sql_binds := NULL,
  user_name        IN VARCHAR2  := NULL,
  scope            IN VARCHAR2  := SCOPE_COMPREHENSIVE,
  time_limit       IN NUMBER    := TIME_LIMIT_DEFAULT,
  task_name        IN VARCHAR2  := NULL,
  description      IN VARCHAR2  := NULL)
RETURN VARCHAR2;
```

SQL ID format:

```
DBMS_SQLTUNE.CREATE_TUNING_TASK(
  sql_id           IN VARCHAR2,
  plan_hash_value  IN NUMBER    := NULL,
  scope            IN VARCHAR2  := SCOPE_COMPREHENSIVE,
  time_limit       IN NUMBER    := TIME_LIMIT_DEFAULT,
  task_name        IN VARCHAR2  := NULL,
  description      IN VARCHAR2  := NULL)
RETURN VARCHAR2;
```

Workload Repository format:

```
DBMS_SQLTUNE.CREATE_TUNING_TASK(
  begin_snap       IN NUMBER,
  end_snap         IN NUMBER,
  sql_id           IN VARCHAR2,
  plan_hash_value  IN NUMBER    := NULL,
  scope            IN VARCHAR2  := SCOPE_COMPREHENSIVE,
  time_limit       IN NUMBER    := TIME_LIMIT_DEFAULT,
  task_name        IN VARCHAR2  := NULL,
  description      IN VARCHAR2  := NULL)
RETURN VARCHAR2;
```

SQLSET format:

```
DBMS_SQLTUNE.CREATE_TUNING_TASK(
  sqlset_name       IN VARCHAR2,
  basic_filter      IN VARCHAR2 :=  NULL,
  object_filter     IN VARCHAR2 :=  NULL,
  rank1             IN VARCHAR2 :=  NULL,
  rank2             IN VARCHAR2 :=  NULL,
  rank3             IN VARCHAR2 :=  NULL,
  result_percentage IN NUMBER   :=  NULL,
  result_limit      IN NUMBER   :=  NULL,
  scope             IN VARCHAR2 :=  SCOPE_COMPREHENSIVE,
  time_limit        IN NUMBER   :=  TIME_LIMIT_DEFAULT,
  task_name         IN VARCHAR2 :=  NULL,
  description       IN VARCHAR2 :=  NULL
  plan_filter       IN VARCHAR2 :=  'MAX_ELAPSED_TIME',
  sqlset_owner      IN VARCHAR2 :=  NULL)
RETURN VARCHAR2;
```

SQL Performance Analyzer format:

```
DBMS_SQLTUNE.CREATE_TUNING_TASK(
   spa_task_name     IN VARCHAR2,
   spa_task_owner    IN VARCHAR2 :=  NULL,
   spa_compare_exec  IN VARCHAR2 :=  NULL,
   basic_filter      IN VARCHAR2 :=  NULL,
   time_limit        IN NUMBER   :=  TIME_LIMIT_DEFAULT,
   task_name         IN VARCHAR2 :=  NULL,
   description       IN VARCHAR2 :=  NULL)
 RETURN VARCHAR2;
```

Parameters

Table 140-17 CREATE\_TUNING\_TASK Function Parameters

| Parameter | Description |
| --- | --- |
| `sql_text` | Text of a SQL statement |
| `begin_snap` | Begin snapshot identifier |
| `end_snap` | End snapshot identifier |
| `sql_id` | Identifier of a SQL statement |
| `bind_list` | An ordered list of bind values in ANYDATA type |
| `plan_hash_value` | Hash value of the SQL execution plan |
| `sqlset_name` | SQL tuning set name |
| `basic_filter` | SQL predicate to filter the SQL from the SQL tuning set |
| `object_filter` | Object filter |
| `rank(i)` | Order-by clause on the selected SQL |
| `result_percentage` | Percentage on the sum of a ranking measure |
| `result_limit` | Top L(imit) SQL from the (filtered/ranked) SQL |
| `user_name` | Username for whom the statement is to be tuned |
| `scope` | Tuning scope (limited/comprehensive) |
| `time_limit` | The maximum duration in seconds for the tuning session |
| `task_name` | Optional tuning task name |
| `description` | Description of the SQL tuning session to a maximum of 256 characters |
| `plan_filter` | Plan filter. It is applicable in case there are multiple plans (`plan_hash_value`) associated with the same statement. This filter allows for selecting one plan (`plan_hash_value`) only. Possible values are:  - `LAST_GENERATED`: plan with the most recent timestamp - `FIRST_GENERATED`: plan with the earliest timestamp, the opposite to `LAST_GENERATED` - `LAST_LOADED`: plan with the most recent `first_load_time` statistics information - `FIRST_LOADED`: plan with the earliest `first_load_time` statistics information, the opposite to `LAST_LOADED` - `MAX_ELAPSED_TIME`: plan with the maximum elapsed time - `MAX_BUFFER_GETS`: plan with the maximum buffer gets - `MAX_DISK_READS`: plan with the maximum disk reads - `MAX_DIRECT_WRITES`: plan with the maximum direct writes - `MAX_OPTIMIZER_COST`: plan with the maximum optimizer cost |
| `sqlset_owner` | Owner of the SQL tuning set, or `NULL` for the current schema owner |
| `spa_task_name` | Name of the SQL Performance Analyzer task whose regressions are to be tuned |
| `spa_task_owner` | Owner of specified SQL Performance Analyzer task or `NULL` for current user |
| `spa_compare_exec` | Execution name of Compare Performance trial of SQL Performance Analyzer task. If `NULL`, we use the most recent execution of the given SQL Performance Analyzer task, of type `COMPARE` `PERFORMANCE` |

Return Values

A SQL tuning task name that is unique by user (two different users can give the same name to their advisor tasks).

Usage Notes

With regard to the form of this subprogram that takes a SQL tuning set, filters provided to this function are evaluated as part of a SQL run by the current user. As such, they are executed with that user's security privileges and can contain any constructs and subqueries that user can access, but no more.

Examples

```
variable stmt_task VARCHAR2(64);
variable sts_task  VARCHAR2(64);
variable spa_tune_task VARCHAR2(64);
```

Create Tuning Task with SQL Text format

```
EXEC :stmt_task := DBMS_SQLTUNE.CREATE_TUNING_TASK( -
  sql_text => 'select quantity_sold from sales s, times t where s.time_id = t.time_id and s.time_id = TO_DATE(''24-NOV-00'')');
```

Create Tuning Task with SQL ID format

```
EXEC :stmt_task := DBMS_SQLTUNE.CREATE_TUNING_TASK(sql_id => 'ay1m3ssvtrh24');
 
-- tune in limited scope 
EXEC :stmt_task := DBMS_SQLTUNE.CREATE_TUNING_TASK(sql_id => 'ay1m3ssvtrh24', -
   scope => 'LIMITED');
 
-- only give 10 minutes for tuning statement
EXEC :stmt_task := DBMS_SQLTUNE.CREATE_TUNING_TASK(sql_id => 'ay1m3ssvtrh24', -
   time_limit => 600);
```

Create Tuning Task with AWR Snapshot format

```
EXEC :stmt_task := DBMS_SQLTUNE.CREATE_TUNING_TASK(begin_snap => 1, -
   end_snap => 2, sql_id => 'ay1m3ssvtrh24');
```

Create Tuning Task with SQL Tuning Set format

```
-- First we need to load an STS, then tune it
-- Tune our statements in order by buffer gets, time limit of one hour
-- the default ranking measure is elapsed time.
EXEC :sts_task := DBMS_SQLTUNE.CREATE_TUNING_TASK( -
  sqlset_name  => 'my_workload', -
  rank1        => 'BUFFER_GETS', -
  time_limit   => 3600, -
  description  => 'tune my workload ordered by buffer gets');
```

Create Tuning Task with SPA Task format

```
-- Tune the SQLs that were reported as having regressed from the compare 
-- performance execution of the SPA task named task_123
EXEC :spa_tune_task := DBMS_SQLTUNE.CREATE_TUNING_TASK(
   spa_task_name     => 'task_123',
   spa_task_owner    => 'SCOTT',
   spa_compare_exec  => 'exec1');
```

---

### DELETE\_SQLSET Procedure

This procedure deletes a set of SQL statements from a SQL tuning set.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.DELETE_SQLSET (
   sqlset_name   IN  VARCHAR2,
   basic_filter  IN  VARCHAR2 := NULL,
   sqlset_owner  IN  VARCHAR2 := NULL);
```

Parameters

Table 140-18 DELETE\_SQLSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sqlset_name` | The SQL tuning set name |
| `basic_filter` | SQL predicate to filter the SQL from the SQL tuning set. This basic filter is used as a where clause on the SQL tuning set content to select a desired subset of SQL from the Tuning Set. |
| `sqlset_owner` | The owner of the SQL tuning set, or `NULL` for current schema owner |

Examples

```
-- Delete all statements in a sql tuning set.
EXEC DBMS_SQLTUNE.DELETE_SQLSET(sqlset_name   => 'my_workload');
 
-- Delete all statements in a sql tuning set which ran for less than a second
EXEC DBMS_SQLTUNE.DELETE_SQLSET(sqlset_name   => 'my_workload', -
                                basic_filter  => 'elapsed_time < 1000000');
```

---

### DROP\_SQL\_PROFILE Procedure

This procedure drops the named SQL profile from the database.

See Also:

SQL Profile Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.DROP_SQL_PROFILE (
   name          IN  VARCHAR2,
   ignore        IN  BOOLEAN  := FALSE);
```

Parameters

Table 140-19 DROP\_SQL\_PROFILE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | The (mandatory) name of SQL profile to be dropped. The name is case sensitive. |
| `ignore` | Ignores errors due to object not existing |

Usage Notes

Requires the " `DROP` `ANY` `SQL PROFILE` " privilege.

Examples

```
-- Drop the profile:
EXEC DBMS_SQLTUNE.DROP_SQL_PROFILE(:pname);
```

---

### DROP\_SQLSET Procedure

This procedure drops a SQL tuning set if it is not active.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.DROP_SQLSET (
   sqlset_name   IN  VARCHAR2,
   sqlset_owner  IN  VARCHAR2 := NULL);
```

Parameters

Table 140-20 DROP\_SQLSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sqlset_name` | The SQL tuning set name |
| `sqlset_owner` | The owner of the SQL tuning set, or `NULL` for current schema owner |

Usage Notes

You cannot drop a SQL tuning set when it is referenced by one or more clients.

Examples

```
-- Drop the sqlset.
EXEC DBMS_SQLTUNE.DROP_SQLSET ('my_workload');
```

---

### DROP\_TUNING\_TASK Procedure

This procedure drops a SQL tuning task. The task and all its result data are deleted.

See Also:

SQL Tuning Advisor Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.DROP_TUNING_TASK(
 task_name         IN VARCHAR2);
```

Parameters

Table 140-21 DROP\_TUNING\_TASK Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | The name of the tuning task to drop |

---

### EXECUTE\_TUNING\_TASK Function & Procedure

This function and procedure executes a previously created tuning task. Both the function and the procedure run in the context of a new task execution. The difference is that the function version returns that new execution name.

See Also:

SQL Tuning Advisor Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.EXECUTE_TUNING_TASK(
   task_name         IN VARCHAR2,
   execution_name    IN VARCHAR2               := NULL,
   execution_params  IN dbms_advisor.argList   := NULL,
   execution_desc    IN VARCHAR2               := NULL)
 RETURN VARCHAR2;
```
```
DBMS_SQLTUNE.EXECUTE_TUNING_TASK(
   task_name         IN VARCHAR2,
   execution_name    IN VARCHAR2               := NULL,
   execution_params  IN dbms_advisor.argList   := NULL,
   execution_desc    IN VARCHAR2               := NULL);
```

Parameters

Table 140-22 EXECUTE\_TUNING\_TASK Function & Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the tuning task to execute |
| execution\_name | A name to qualify and identify an execution. If not specified, it is generated by the advisor and returned by function. |
| execution\_params | List of parameters (name, value) for the specified execution. The execution parameters have effect only on the execution for which they are specified. They override the values for the parameters stored in the task (set through the SET\_TUNING\_TASK\_PARAMETER Procedures). |
| `execution_desc` | A 256-length string describing the execution |

Usage Notes

A tuning task can be executed multiples times without having to reset it.

Examples

```
EXEC DBMS_SQLTUNE.EXECUTE_TUNING_TASK(:stmt_task);
```

---

### IMPLEMENT\_TUNING\_TASK Function

This function implements a set of SQL profile recommendations made by the SQL Tuning Advisor. Call this subprogram is equivalent to calling the SCRIPT\_TUNING\_TASK Function and then running the script.

See Also:

SQL Tuning Advisor Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.IMPLEMENT_TUNING_TASK(
    task_name      IN VARCHAR2,
    rec_type       IN VARCHAR2 := REC_TYPE_SQL_PROFILES,
    owner_name     IN VARCHAR2 := NULL,
    execution_name IN VARCHAR2 := NULL);
```

Parameters

Table 140-23 IMPLEMENT\_TUNING\_TASK Function Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the tuning task for which to implement recommendations |
| rec\_type | Filter the types of recommendations to implement. Only ' `PROFILES` ' is supported. |
| `owner_name` | Owner of the relevant tuning task or `NULL` for the current user. |
| `execution_name` | name of the task execution to use. If `NULL`, recommendations from the last task execution are implemented. |

---

### INTERRUPT\_TUNING\_TASK Procedure

This procedure interrupts the currently executing tuning task. The task ends its operations as it would at normal exit so that the user can access the intermediate results.

See Also:

SQL Tuning Advisor Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.INTERRUPT_TUNING_TASK(
 task_name         IN VARCHAR2);
```

Parameters

Table 140-24 INTERRUPT\_TUNING\_TASK Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the tuning task to interrupt |

Examples

```
EXEC DBMS_SQLTUNE.INTERRUPT_TUNING_TASK(:my_task);
```

---

### LOAD\_SQLSET Procedure

This procedure populates the SQL tuning set with a set of selected SQL. You can call the procedure multiple times to add new SQL statements or replace attributes of existing statements.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.LOAD_SQLSET (
   sqlset_name       IN  VARCHAR2,
   populate_cursor   IN  sqlset_cursor,
   load_option       IN VARCHAR2 := 'INSERT', 
   update_option     IN VARCHAR2 := 'REPLACE', 
   update_condition  IN VARCHAR2 :=  NULL,
   update_attributes IN VARCHAR2 :=  NULL,
   ignore_null       IN BOOLEAN  :=  TRUE,
   commit_rows       IN POSITIVE :=  NULL,
   sqlset_owner      IN VARCHAR2 := NULL);
```

Parameters

Table 140-25 LOAD\_SQLSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sqlset_name` | The SQL tuning set name to populate |
| `populate_cursor` | The cursor reference from which to populate |
| `load_option` | Specifies how the statements are loaded into the SQL tuning set. The possible values are:  - `INSERT` (default) - add only new statements - `UPDATE` - update existing the SQL statements and ignores any new statements - `MERGE` - this is a combination of the two other options. This option inserts new statements and updates the information of the existing ones. |
| `update_option` | Specifies how the existing statements are updated. This parameter is considered only if load\_option is specified with ' `UPDATE` '/' `MERGE` ' as an option. The possible values are:  - `REPLACE` (default) - update the statement using the new statistics, bind list, object list, and so on. - `ACCUMULATE` - when possible combine attributes (for example, statistics like `elapsed_time`, and so on) otherwise just replace the old values (for example, module, action, and so on) by the new provided ones. The SQL statement attributes that can be accumulated are: `elapsed_time`, `buffer_gets`, `direct_writes`, `disk_reads`, `row_processed`, `fetches`, `executions`, `end_of_fetch_count`, `stat_period` and `active_stat_period`. |
| `update_condition` | Specifies a where clause to execute the update operation. The update is performed only if the specified condition is true. The condition can refer to either the data source or destination. The condition must use the following prefixes to refer to attributes from the source or the destination:  - `OLD` - to refer to statement attributes from the SQL tuning set (destination) - `NEW` - to refer to statements attributes from the input statements (source) |
| `update_attributes` | Specifies the list of a SQL statement attributes to update during a merge or update operation.The possible values are:  - `NULL` (default) - the content of the input cursor except the execution context. On other terms, it is equivalent to `ALL` without execution context like module, action, and so on. - `BASIC` - statistics and binds only - `TYPICAL` - `BASIC` + SQL plans (without row source statistics) and without object reference list - `ALL` - all attributes including the execution context attributes like module, action, and so on. - List of comma separated attribute names to update - `EXECUTION_CONTEXT`, `EXECUTION_STATISTICS`, `BIND_LIST`, `OBJECT_LIST`, `SQL_PLAN`, `SQL_PLAN_STATISTICS` (similar to `SQL_PLAN` + row source statistics) |
| `ignore_null` | If `TRUE` do not update an attribute if the new value is `NULL`. That is, do not override with `NULL` values unless intentional. |
| `commit_rows` | If a value is provided, the load commits after each set of that many statements is inserted. If `NULL` is provided, the load commits only once, at the end of the operation. Providing a value for this argument allows you to monitor the progress of a SQL tuning set load operation in the `DBA_` / `USER_SQLSET` views. The `STATEMENT_COUNT` value increases as new SQL statements are loaded. |
| `sqlset_owner` | The owner of the SQL tuning set, or the current schema owner or `NULL` for current owner |

Exceptions

- This procedure returns an error when `sqlset_name` is invalid, or a corresponding SQL tuning set does not exist, or the `populate_cursor` is incorrect and cannot be executed.
- Exceptions are also raised when invalid filters are provided. Filters can be invalid either because they don't parse (for example, they refer to attributes not in sqlset\_row), or because they violate the user's privileges.

Usage Notes

Rows in the input `populate_cursor` must be of type `SQLSET_ROW`.

Examples

In this example, you create and populate a SQL tuning set with all cursor cache statements with an elapsed time of 5 seconds or more excluding statements that belong to `SYS` schema (to simulate an application user workload). You select all attributes of the SQL statements and load them in the tuning set using the default mode, which loads only new statements, since the SQL tuning set is empty.

```
-- create the tuning set
EXEC DBMS_SQLTUNE.CREATE_SQLSET('my_workload');
-- populate the tuning set from the cursor cache
DECLARE
 cur DBMS_SQLTUNE.SQLSET_CURSOR;
BEGIN
 OPEN cur FOR
   SELECT VALUE(P)
     FROM table(
       DBMS_SQLTUNE.SELECT_CURSOR_CACHE(
         'parsing_schema_name <> ''SYS'' AND elapsed_time > 5000000',
          NULL, NULL, NULL, NULL, 1, NULL,
         'ALL')) P;
 
DBMS_SQLTUNE.LOAD_SQLSET(sqlset_name => 'my_workload',
                        populate_cursor => cur);
 
END;
/
```

Suppose now you wish to augment this information with what is stored in the workload repository (AWR). You populate the tuning set with `'ACCUMULATE'` as your `update_option` because it is assumed the cursors currently in the cache had aged out since the snapshot was taken.

You omit the `elapsed_time` filter because it is assumed that any statement captured in AWR is important, but still you throw away the `SYS` -parsed cursors to avoid recursive SQL.

```
DECLARE
  cur DBMS_SQLTUNE.SQLSET_CURSOR;
BEGIN
  OPEN cur FOR
    SELECT VALUE(P)
      FROM table(
        DBMS_SQLTUNE.SELECT_WORKLOAD_REPOSITORY(1,2,
                                                'parsing_schema_name <> ''SYS''',
                                                NULL, NULL,NULL,NULL,
                                                1,
                                                NULL,
                                                'ALL')) P;

  DBMS_SQLTUNE.LOAD_SQLSET(sqlset_name => 'my_workload',
                           populate_cursor => cur,
                           Using DBMS_SQLTUNE
                           load_option => 'MERGE',
                           update_option => 'ACCUMULATE');
END;
```

The following example is a simple load that only inserts new statements from the workload repository, skipping existing ones (in the SQL tuning set). Note that `'INSERT'` is the default value for the `load_option` argument of the `LOAD_SQLSET` procedure.

```
DECLARE
  cur sys_refcursor;
BEGIN
  OPEN cur FOR
  SELECT VALUE(P)
  FROM table(DBMS_SQLTUNE.SELECT_WORKLOAD_REPOSITORY(1,2)) P;
  
  DBMS_SQLTUNE.LOAD_SQLSET(sqlset_name => 'my_workload',
populate_cursor => cur);
END;
/
```

The next example demonstrates a load with `UPDATE` option. This updates statements that already exist in the SQL tuning set but does not add new ones. By default, old statistics are replaced by their new values.

```
DECLARE
  cur sys_refcursor;
BEGIN
  OPEN cur FOR
    SELECT VALUE(P)
    FROM table(DBMS_SQLTUNE.SELECT_CURSOR_CACHE) P;
  
  DBMS_SQLTUNE.LOAD_SQLSET(sqlset_name => 'my_workload',
                           populate_cursor => cur,
                           load_option => 'UPDATE');
END;
/
```

---

### PACK\_STGTAB\_SQLPROF Procedure

This procedure copies profile data from the `SYS`. schema into the staging table.

See Also:

SQL Profile Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.PACK_STGTAB_SQLPROF (
   profile_name          IN VARCHAR2 := '%',
   profile_category      IN VARCHAR2 := 'DEFAULT',
   staging_table_name    IN VARCHAR2,
   staging_schema_owner  IN VARCHAR2 := NULL);
```

Parameters

Table 140-26 PACK\_STGTAB\_SQLPROF Procedure Parameters

| Parameter | Description |
| --- | --- |
| `profile_name` | The name of the profile to pack (% wildcards acceptable, case-sensitive) |
| `profile_category` | The category to pack profiles from (% wildcards acceptable, case-sensitive) |
| `staging_table_name` | The name of the table to use (case-insensitive unless double quoted). Required. |
| `staging_schema_owner` | The schema where the table resides, or `NULL` for current schema (case-insensitive unless double quoted) |

Usage Notes

- This procedures requires `ADMINISTER SQL MANAGEMENT OBJECT` privilege and `INSERT` privilege on the staging table.
- Note that this function issues a `COMMIT` after packing each SQL profile, so if an error is raised mid-execution, clear the staging table by deleting its rows.

Examples

Put only those profiles in the `DEFAULT` category into the staging table. This corresponds to all profiles used by default on this system.

```
EXEC DBMS_SQLTUNE.PACK_STGTAB_SQLPROF (staging_table_name => 'PROFILE_STGTAB');
```

This is another example where you put all profiles into the staging table. Note this moves profiles that are not currently being used by default but are in other categories, such as for testing purposes.

```
EXEC DBMS_SQLTUNE.PACK_STGTAB_SQLPROF (profile_category => '%', -
                                      staging_table_name => 'PROFILE_STGTAB');
```

---

### PACK\_STGTAB\_SQLSET Procedure

This procedure copies one or more SQL tuning sets from their location in the `SYS` schema to a staging table created by the CREATE\_STGTAB\_SQLSET Procedure.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.PACK_STGTAB_SQLSET (
   sqlset_name          IN VARCHAR2,
   sqlset_owner         IN VARCHAR2 := NULL,
   staging_table_name   IN VARCHAR2,
   staging_schema_owner IN VARCHAR2 := NULL,
   db_version           IN NUMBER := NULL);
```

Parameters

Table 140-27 PACK\_STGTAB\_SQLSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sqlset_name` | The name of the SQL tuning set to pack (% wildcards acceptable, case-sensitive) |
| `sqlset_owner` | The category from which to pack SQL tuning sets (% wildcards acceptable, case-sensitive) |
| `staging_table_name` | The name of the table to use (case-sensitive) |
| `staging_schema_owner` | The schema where the table resides, or `NULL` for current schema (case-sensitive) |
| `db_version` | Database (DB) version determining the format of the staging table. User can also create an older DB version staging table to export STS to an older DB version. One of the following values:  - `NULL` (default) — current DB version - `STS_STGTAB_10_2_VERSION` — 10.2 DB version - `STS_STGTAB_11_1_VERSION` — 11.1 DB version - `STS_STGTAB_11_2_VERSION` — 11.2 DB version |

Usage Notes

- This procedure can be called several times to move more than one SQL tuning set. Users can then move the populated staging table to another system using any method, such as database link or datapump. Users can then call the UNPACK\_STGTAB\_SQLSET Procedure create the SQL tuning set on the other system.
- Note that this function issues a `COMMIT` after packing each SQL tuning set, so if an error is raised mid-execution, clear the staging table by deleting its rows.

Examples

Put all SQL tuning sets on the system in the staging table

\-- to create a staging table, see the `CREATE_STGTAB_SQLSET Procedure`

```
EXEC DBMS_SQLTUNE.PACK_STGTAB_SQLSET(sqlset_name        => '%', -
                                     sqlset_owner       => '%', -
                                     staging_table_name => 'STGTAB_SQLSET');
```

Put only those SQL tuning sets owned by the current user in the staging table

```
EXEC DBMS_SQLTUNE.PACK_STGTAB_SQLSET(
   sqlset_name           => '%',
   staging_table_name    => 'STGTAB_SQLSET');
```

Pack a specific SQL tuning set

```
EXEC DBMS_SQLTUNE.PACK_STGTAB_SQLSET(
   sqlset_name           => 'my_workload', -
   staging_table_name    => 'STGTAB_SQLSET');
```

Pack a second SQL tuning set

```
EXEC DBMS_SQLTUNE.PACK_STGTAB_SQLSET(
   sqlset_name           => 'workload_subset', -
   staging_table_name    => 'STGTAB_SQLSET');
```

Pack the STS my\_workload to a staging table STGTAB\_SQLSET created for Oracle Database 10g Release 2 (10.2)

```
EXEC DBMS_SQLTUNE.PACK_STGTAB_SQLSET(
   sqlset_name          => 'workload_subset', 
   staging_table_name   => 'STGTAB_SQLSET', 
   db_version           => DBMS_SQLTUNE.STS_STGTAB_10_2_VERSION);
```

Pack the STS my\_workload to a staging table STGTAB\_SQLSET created for Oracle Database 11g Release 1 (11.1)

```
EXEC DBMS_SQLTUNE.PACK_STGTAB_SQLSET(
   sqlset_name          => 'workload_subset', 
   staging_table_name   => 'STGTAB_SQLSET', 
   db_version           => DBMS_SQLTUNE.STS_STGTAB_11_1_VERSION);
```

---

### REMAP\_STGTAB\_SQLPROF Procedure

This procedure allows DBAs to change the profile data values kept in the staging table prior to performing an unpack operation. The procedure can be used to change the category of a profile.It can be used to change the name of a profile if one already exists on the system with the same name.

See Also:

SQL Profile Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.REMAP_STGTAB_SQLPROF (
  old_profile_name      IN VARCHAR2,
  new_profile_name      IN VARCHAR2 := NULL,
  new_profile_category  IN VARCHAR2 := NULL,
  staging_table_name    IN VARCHAR2,
  staging_schema_owner  IN VARCHAR2 := NULL);
```

Parameters

Table 140-28 REMAP\_STGTAB\_SQLPROF Procedure Parameters

| Parameter | Description |
| --- | --- |
| `old_profile_name` | The name of the profile to target for a remap operation (case-sensitive) |
| `new_profile_name` | The new name of the profile, or `NULL` to remain the same (case-sensitive) |
| `new_profile_category` | The new category for the profile, or `NULL` to remain the same (case-sensitive) |
| `staging_table_name` | The name of the table on which to perform the remap operation (case-sensitive). Required. |
| `staging_schema_owner` | The schema where the table resides, or `NULL` for current schema (case-sensitive) |

Usage Notes

Using this procedure requires the `UPDATE` privilege on the staging table.

Examples

Change the name of a profile before we unpack, to avoid conflicts

```
EXEC DBMS_SQLTUNE.REMAP_STGTAB_SQLPROF(old_profile_name    => :pname,          -
                                       new_profile_name    => 'IMP' || :pname, -
                                       staging_table_name  => 'PROFILE_STGTAB');
```

Change the SQL profile in the staging table to be `'TEST'` category before we import it. This way users can test the profile on the new system before it is active.

```
EXEC DBMS_SQLTUNE.REMAP_STGTAB_SQLPROF(old_profile_name     => :pname,       -
                                       new_profile_category => 'TEST',       -
                                       staging_table_name   => 'PROFILE_STGTAB');
```

---

### REMAP\_STGTAB\_SQLSET Procedure

This procedure changes the tuning set names and owners in the staging table so that they can be unpacked with different values than they had on the host system.

See Also:

SQL Profile Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.REMAP_STGTAB_SQLSET (
   old_sqlset_name        IN VARCHAR2,
   old_sqlset_owner       IN VARCHAR2 := NULL,
   new_sqlset_name        IN VARCHAR2 := NULL,
   new_sqlset_owner       IN VARCHAR2 := NULL,
   staging_table_name     IN VARCHAR2,
   taging_schema_owner   IN VARCHAR2 := NULL);
```

Parameters

Table 140-29 REMAP\_STGTAB\_SQLSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `old_sqlset_name` | The name of the tuning set to target for a remap operation. Wildcards are not supported. |
| `old_sqlset_owner` | The new name of the tuning set owner to target for a remap operation. `NULL` for current schema owner |
| `new_sqlset_name` | The new name for the tuning set, or `NULL` to keep the same tuning set name. |
| `new_sqlset_owner` | The new owner for the tuning set, or `NULL` to remain the same owner name. |
| `staging_table_name` | The name of the table on which to perform the remap operation (case-sensitive) |
| `staging_schema_owner` | The name of staging table owner, or `NULL` for current schema owner (case-sensitive) |

Usage Notes

You can call this procedure multiple times to remap more than one tuning set name or owner. Note that this procedure only handles one tuning set per call.

Examples

```
-- Change the name of an STS in the staging table before we unpack it.
EXEC DBMS_SQLTUNE.REMAP_STGTAB_SQLSET(old_sqlset_name    => 'my_workload', -
                                      old_sqlset_owner   => 'SH', -
                                      new_sqlset_name    => 'imp_workload', -
                                      staging_table_name => 'STGTAB_SQLSET');
 
-- Change the owner of an STS in the staging table before we unpack it.
EXEC DBMS_SQLTUNE.REMAP_STGTAB_SQLSET(old_sqlset_name    => 'imp_workload', -
                                      old_sqlset_owner   => 'SH', -
                                      new_sqlset_owner   => 'SYS', -
                                      staging_table_name => 'STGTAB_SQLSET');
```

---

### REMOVE\_SQLSET\_REFERENCE Procedure

This procedure deactivates a SQL tuning set to indicate it is no longer used by the client.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.REMOVE_SQLSET_REFERENCE (
   sqlset_name   IN  VARCHAR2,
   reference_id  IN  NUMBER);
```

Parameters

Table 140-30 REMOVE\_SQLSET\_REFERENCE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sqlset_name` | The SQL tuning set name |
| `reference_id` | The identifier of the reference to remove |

Examples

You can remove references on a given SQL tuning set when you finish using it and want to make it writable again.

```
EXEC DBMS_SQLTUNE.REMOVE_SQLSET_REFERENCE( -
                                sqlset_name   => 'my_workload', -
                                reference_id  => :rid);
```

Use views `USER/DBA_SQLSET_REFERENCES` to find all references on a given SQL tuning set.

---

### REPORT\_AUTO\_TUNING\_TASK Function

This function displays a report from the automatic tuning task. This function reports on a range of task executions, whereas the REPORT\_TUNING\_TASK Function reports on a single execution. Note that this function is deprecated in Oracle Database 11g Release 2 (11.2) in favor of `DBMS_AUTO_SQLTUNE.REPORT_AUTO_TUNING_TASK`.

See Also:

- SQL Tuning Set Subprograms for other subprograms in this group
- [REPORT\_AUTO\_TUNING\_TASK Function](d_autosta.md)

Syntax

```
DBMS_SQLTUNE.REPORT_AUTO_TUNING_TASK(
    begin_exec     IN VARCHAR2  := NULL,
    end_exec       IN VARCHAR2  := NULL,
    type           IN VARCHAR2  := TYPE_TEXT,
    level          IN VARCHAR2  := LEVEL_TYPICAL,
    section        IN VARCHAR2  := SECTION_ALL,
    object_id      IN NUMBER    := NULL,
    result_limit   IN NUMBER    := NULL)
  RETURN CLOB;
```

Parameters

Table 140-31 REPORT\_AUTO\_TUNING\_TASK Function Parameters

| Parameter | Description |
| --- | --- |
| `begin_exec` | Name of execution from which to begin the report. `NULL` retrieves a report on the most recent run |
| `end_exec` | Name of execution at which to end the report. `NULL` retrieves a report on the most recent run. |
| `type` | Type of the report to produce. Possible values are `TYPE_TEXT` which produces a text report |
| `level` | Level of detail in the report:  - `LEVEL_BASIC`: simple version of the report. Just show info about the actions taken by the advisor. - `LEVEL_TYPICAL`: show information about every statement analyzed, including requests not implemented. - `LEVEL_ALL`: highly detailed report level, also provides annotations about statements skipped over. |
| `section` | Optionally limit the report to a single section (`ALL` for all sections):  - `SECTION_SUMMARY` - summary information - `SECTION_FINDINGS` - tuning findings - `SECTION_PLAN` - explain plans - `SECTION_INFORMATION` - general information - `SECTION_ERROR` - statements with errors - `SECTION_ALL` - all statements |
| `object_id` | Advisor framework object id that represents a single statement to restrict reporting to. `NULL` for all statements. Only valid for reports that target a single execution. |
| `result_limit` | Maximum number of SQL statements to show in the report |

Return Values

A `CLOB` containing the desired report.

---

### REPORT\_SQL\_DETAIL Function

This function builds a report for a specific SQLID. For each SQLID it gives various statistics and details as obtained from the `V$` views and AWR.

See Also:

SQL Performance Reporting Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.REPORT_SQL_DETAIL(
   sql_id                   IN  VARCHAR2   DEFAULT NULL,
   sql_plan_hash_value      IN  NUMBER     DEFAULT NULL,
   start_time               IN  DATE       DEFAULT NULL,
   duration                 IN  NUMBER     DEFAULT NULL,
   inst_id                  IN  NUMBER     DEFAULT NULL,
   dbid                     IN  NUMBER     DEFAULT NULL,
   event_detail             IN  VARCHAR2   DEFAULT 'YES',
   bucket_max_count         IN  NUMBER     DEFAULT 128,
   bucket_interval          IN  NUMBER     DEFAULT NULL,
   top_n                    IN  NUMBER     DEFAULT 10,
   report_level             IN  VARCHAR2   DEFAULT 'TYPICAL',
   type                     IN  VARCHAR2   DEFAULT 'ACTIVE')
 RETURN CLOB;
```

Parameters

Table 140-32 REPORT\_SQL\_DETAIL Function Parameters

| Parameter | Description |
| --- | --- |
| `sql_id` | SQLID for which monitoring information should be displayed. If `NULL` (the default), display statistics for the SQLID of the last SQL statement executed in the current session. |
| `sql_plan_hash_value` | Displays SQL statistics and details for a specific `plan_hash_value`. If `NULL` (default), displays statistics and details for all plans of the SQL\_ID. |
| `start_time` | If specified, shows SQL activity (from gv$ `ACTIVE_SESSION_HISTORY`) starting at this time. On Oracle RAC, the minimum `start_time` is the earliest `sample_time` of the in-memory ASH buffers across all instances. If `NULL` (default), one hour before the current time. |
| `duration` | Duration of activity in seconds for the report. If `NULL` (default) uses a value of 1 hour. |
| `inst_id` | Target instance to get SQL details from. If `NULL`, uses data from all instances. If 0 or -1, uses current instance. |
| `dbid` | DBID from which to get SQL details. If `NULL`, uses current DBID. |
| `event_detail` | When set to `'NO'`, the activity is aggregated by `wait_class` only. Use `'YES'` (the default) to aggregate by (`wait_class`, `event_name`). |
| `bucket_max_count` | If specified, this should be the maximum number of histogram buckets created in the report. If not specified, a value of 128 is used. |
| `bucket_interval` | If specified, this represents the exact time interval in seconds, of all histogram buckets. If specified, `bucket_max_count` is ignored. |
| `top_n` | Controls the number of entries to display per dimension in the top dimensions section. If not specified, a default value of 10 is used. |
| `report_level` | Level of detail for the report, either `'BASIC'`, `'TYPICAL'` or `'ALL'`. Default assumes `'TYPICAL'`. Their meanings are explained below.  In addition, individual report sections can also be enabled or disabled by using a +/- `section_name`. Several sections are defined:  - `'TOP'` - Show top values for the ASH dimensions for a SQL statement; `ON` by default - `'SPM'` - Show existing plan baselines for a SQL statement; `OFF` by default - `'MISMATCH'` - Show reasons for creating new child cursors (sharing criteria violations); `OFF` by default. - `'STATS'` - Show SQL execution statistics per plan from `GV$SQLAREA_PLAN_HASH`; `ON` by default - `'ACTIVITY'` - Show top activity from ASH for each plan of a SQL statement; `ON` by default - `'ACTIVITY_ALL'` - Show top activity from ASH for each line of the plan for a SQL statement; `OFF` by default - `'HISTOGRAM'` - Show activity histogram for each plan of a SQL statement (plan timeline histogram); `ON` by default - `'SESSIONS'` - Show activity for top sessions for each plan of a SQL statement; `OFF` by default - `'MONITOR'` - Show show one monitored SQL execution per execution plan; `ON` by default - `'XPLAN'` - Show execution plans; `ON` by default - `'BINDS'` - show captured bind data; `ON` by default  In addition, SQL text can be specified at different levels:  - \- `SQL_TEXT` - No SQL text in report - `+SQL_TEXT` - OK with partial SQL text up to the first 2000 chars as stored in `GV$SQL_MONITOR` - `-SQL_FULLTEXT` - No full SQL text (`+SQL_TEXT`) - `+SQL_FULLTEXT` - Show full SQL text (default value)  The meanings of the three top-level report levels are:  - `NONE` - minimum possible - `BASIC` - `SQL_TEXT+STATS+ACTIVITY+HISTOGRAM` - `TYPICAL` - `SQL_FULLTEXT+TOP+STATS+ACTIVITY+HISTOGRAM+XPLAN+MONITOR` - `ALL` - everything  Only one of these 4 levels can be specified and, if it is, it has to be at the start of the `REPORT_LEVEL` string |
| `type` | Report format: `'ACTIVE'` by default. Can also be `'XML'` (see Usage Notes). |

Return Values

A `CLOB` containing the desired report.

Usage Notes

- `ACTIVE` reports have a rich, interactive user interface similar to Enterprise Manager while not requiring any EM installation. The report file built is in HTML format, so it can be interpreted by most modern browsers. The code powering the active report is downloaded transparently by the web browser when the report is first viewed, hence viewing it requires outside connectivity.
- The invoker needs the `SELECT` privilege on the following views:
	- `V$SESSION`
		- `DBA_ADVISOR_FINDINGS`
		- `V$DATABASE`
		- `GV$ASH_INFO`
		- `GV$ACTIVE_SESSION_HISTORY`
		- `GV$SQLAREA_PLAN_HASH`
		- `GV$SQL`
		- `DBA_HIST_SNAPSHOT`
		- `DBA_HIST_WR_CONTROL`
		- `DBA_HIST_ACTIVE_SESS_HISTORY`
		- `DBA_HIST_SQLSTAT`
		- `DBA_HIST_SQL_BIND_METADATA`
		- `DBA_HIST_SQLTEXT`
		- `DBA_SQL_PLAN_BASELINES`
		- `DBA_SQL_PROFILES`
		- `DBA_ADVISOR_TASKS`
		- `DBA_SERVICES`
		- `DBA_USERS`
		- `DBA_OBJECTS`
		- `DBA_PROCEDURES`
- The invoker needs the `EXECUTE` privilege on the [DBMS\_XPLAN](d_xplan.md) package.
- Finally, the invoker requires all privileges required by `DBMS_SQLTUNE.REPORT_SQL_MONITOR` an `DBMS_SQLTUNE.REPORT_SQL_MONITOR_LIST` as it calls these functions.

---

### REPORT\_SQL\_MONITOR Function

This function builds a report (text, simple HTML, active HTML, XML) for the monitoring information collected on behalf of the targeted statement execution.

See Also:

Real-time SQL Monitoring Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.REPORT_SQL_MONITOR(
   sql_id                    IN VARCHAR2  DEFAULT  NULL,
   session_id                IN NUMBER    DEFAULT  NULL,
   session_serial            IN NUMBER    DEFAULT  NULL,
   sql_exec_start            IN DATE      DEFAULT  NULL,
   sql_exec_id               IN NUMBER    DEFAULT  NULL,
   inst_id                   IN NUMBER    DEFAULT  NULL,
   start_time_filter         IN DATE      DEFAULT  NULL,
   end_time_filter           IN DATE      DEFAULT  NULL,
   instance_id_filter        IN NUMBER    DEFAULT  NULL,
   parallel_filter           IN VARCHAR2  DEFAULT  NULL,
   plan_line_filter          IN NUMBER    DEFAULT  NULL,
   event_detail              IN VARCHAR2  DEFAULT  'YES',
   bucket_max_count          IN NUMBER    DEFAULT  128,
   bucket_interval           IN NUMBER    DEFAULT  NULL,
   base_path                 IN VARCHAR2  DEFAULT  NULL,
   last_refresh_time         IN DATE      DEFAULT  NULL,
   report_level              IN VARCHAR2  DEFAULT 'TYPICAL',
   type                      IN VARCHAR2  DEFAULT 'TEXT',
   sql_plan_hash_value       IN NUMBER    DEFAULT  NULL)
 RETURN CLOB;
```

Parameters

Table 140-33 REPORT\_SQL\_MONITOR Function Parameters

| Parameter | Description |
| --- | --- |
| `sql_id` | SQL\_ID for which monitoring information should be displayed. Use `NULL` (the default) to report on the last statement monitored by Oracle. |
| `session_id` | If not `NULL`, this parameters targets only the sub-set of statements executed by the specified session. Default is `NULL`. Use `USERENV` (' `SID` ') for current session. |
| `session_serial` | In addition to the `session_id` parameter, one can also specify its session serial to ensure that the desired session incarnation is targeted. This parameter is ignored when `session_id` is `NULL`. |
| `sql_exec_start` | This parameter, along with `sql_exec_id`, is only applicable when `sql_id` is also specified. Jointly, they can be used to display monitoring information associated to any execution of the statement identified by `sql_id`, assuming that this statement was monitored. When `NULL` (the default), the last monitored execution of SQL `sql_id` is shown. |
| `sql_exec_id` | This parameter, along with `sql_exec_start`, is only applicable when `sql_id` is also specified. Jointly, they can be used to display monitoring information associated to any execution of the statement identified by `sql_id`, assuming that this statement was monitored. When `NULL` (the default), the last monitored execution of SQL `sql_id` is shown. |
| `inst_id` | Only considers statements started on the specified instance. Use -1 to target the login instance. `NULL` (default) targets all instances. |
| `start_time_filter` | If not `NULL`, the report considers only the activity (from `GV$ACTIVE_SESSION_HISTORY`) recorded after the specified date. If `NULL`, the reported activity starts when the execution of the targeted SQL statement has started. |
| `end_time_filter` | If not `NULL`, the report shows only the activity (from `GV$ACTIVE_SESSION_HISTORY`) collected before the date `end_time_filter`. If `NULL`, the reported activity ends when the targeted SQL statement execution has ended or is the current time if the statement is still executing. |
| `instance_id_filter` | Only applies when the execution runs parallel across multiple Oracle Real Application Cluster (Oracle RAC) instances. This parameter allows to only report the activity of the specified instance. Use a `NULL` value (the default) to include the activity on all instances where the parallel query was executed. |
| `parallel_filter` | Applies only to parallel execution and allows reporting the activity of only a subset of the processes involved in the parallel execution (Query Coordinator and/or Parallel eXecution servers). The value of this parameter can be:  - `NULL` to target all processes - `[qc][servers(<svr_grp>[,] <svr_set>[,] <srv_num>)]: 'qc'` stands for query coordinator and `servers()` stipulate which PX servers to consider.  The following examples show how to target a subset of the parallel processes:  - `qc`: targets only the query coordinator - `servers(1)`: targets all parallel execution servers in group number 1. Note that statement running parallel have one main server group (group number 1) plus one additional group for each nested sub-query running parallel. - `servers(,2)`: targets all parallel execution servers from any group but only running in set 1 of each group (each group has at most two set of parallel execution servers) - `servers(1,1)`: consider only group 1, set 1 - `servers(1,2,4)`: consider only group 1, set 2, server number 4. This reports for a single parallel server process - `qc servers(1,2,4)`: same as above by also including the query coordinator |
| `event_detail` | When value is ' `YES` ' (the default), reported activity from `GV$ACTIVE_SESSION_HISTORY` is aggregated by (`wait_class`, `event_name`). Use ' `NO` ' to only aggregate by `wait_class`. |
| `bucket_max_count` | If specified, this should be the maximum number of histogram buckets created in the report |
| `bucket_interval` | If specified, this represents the exact time interval in seconds, of all histogram buckets. If specified, `bucket_max_count` is ignored. |
| `base_path` | URL path for flex HTML resources since flex HTML format is required to access external files (java scripts and the flash SWF file itself) |
| `last_refresh_time` | If not `NULL` (default is `NULL`), the time when the report was last retrieved (see `SYSDATE` attribute of the report tag). Use this option to display the report of a running query, and when the report is refreshed on a regular basis. This optimizes the size of the report since only the new or changed information is returned. In particular, the following are optimized:  - SQL text is not returned when this option is specified - activity histogram starts at the bucket that intersect at that time. The entire content of the bucket is returned, even if `last_refresh_time` is after the start of that bucket |
| `report_level` | Level of detail for the report, either `'NONE'`, `'BASIC'`, `'TYPICAL'` or `'ALL'`. Default assumes `'TYPICAL'`. Their meanings are explained below.  In addition, individual report sections can also be enabled or disabled by using a +/- `section_name`. Several sections are defined:  - `'XPLAN'` - Show explain plan; `ON` by default - `'PLAN'` - Show plan monitoring statistics; `ON` by default - `'SESSIONS'` - Show session details. Applies only to parallel queries; `ON` by default - `'INSTANCE'` - Show instance details. Applies only to parallel and cross instance; `ON` by default - `'PARALLEL'` - An umbrella parameter for specifying `sessions+instance` details - `'ACTIVITY'` - Show activity summary at global level, plan line level and session or instance level (if applicable); `ON` by default - `'BINDS'` - Show bind information when available; `ON` by default - `'METRICS'` - Show metric data (CPU, IOs,...) over time; `ON` by default - `'ACTIVITY_HISTOGRAM'` - Show an histogram of the overall query activity; `ON` by default - `'PLAN_HISTOGRAM'` - Show activity histogram at plan line level; `OFF` by default - `'OTHER'` - Other info; `ON` by default  In addition, SQL text can be specified at different levels:  - `SQL_TEXT` - No SQL text in report - `+SQL_TEXT` - OK with partial SQL text up to the first 2000 chars as stored in `GV$SQL_MONITOR` - `-SQL_FULLTEXT` - No full SQL text (`+SQL_TEXT`) - `+SQL_FULLTEXT` - Show full SQL text (default value) |
| `report_level` (contd.) | The meanings of the three top-level report levels are:  - `NONE` - minimum possible - `+BASIC` - `SQL_TEXT-PLAN-XPLAN-SESSIONS-INSTANCE-ACTIVITY_HISTOGRAM-PLAN_HISTOGRAM-METRICS` - `TYPICAL` - everything but `PLAN_HISTOGRAM` - `ALL` - everything  Only one of these 4 levels can be specified and, if it is, it has to be at the start of the `REPORT_LEVEL` string |
| `type` | Report format, `'TEXT'` by default. Can be `'TEXT',` ' `HTML'`, `'XML'` or `'ACTIVE'` (see Usage Notes). |
| `sql_plan_hash_value` | Target only those SQL executions with the specified `plan_hash_value`. Default is `NULL`. |

Return Values

A `CLOB` containing the desired report.

Usage Notes

- The target SQL statement for this report can be:
	- The last SQL monitored by Oracle (this is the default behavior, so there is no need to specify any parameter)The last SQL executed by a specific session and monitored by Oracle. The session is identified by its session id and optionally it serial number. For example, use `session_id` `=>` `USERENV ('SID')` for the current session or `session_id` `=>` `20`, `session_serial` `=>` `103` for session ID 20, serial number 103.The last execution of a specific statement identified by its `sql_id`.A specific execution of a SQL statement identified by its execution key (`sql_id`, `sql_exec_start` and `sql_exec_id`).
- This report produces performance data exposed by several fixed views, listed below. For this reason, the invoker of the report function must have privilege to select data from these fixed views (such as the `SELECT_CATALOG` role).
	- `GV$SQL_MONITOR`
		- `GV$SQL_PLAN_MONITOR`
		- `GV$SQL_PLAN`
		- `GV$ACTIVE_SESSION_HISTORY`
		- `GV$SESSION_LONGOPS`
		- `GV$SQL`
- The `bucket_max_count` and `bucket_interval` parameters control the activity histogram. By default, the maximum number of buckets is set to 128 and the RDBMS derives the bucket\_interval based on this. The bucket\_interval (value is in seconds) is computed such that it is the smallest possible power of 2 value (starting at 1s) without exceeding the maximum number of buckets. For example, if the query has executed for 600s, the RDBMS selects a `bucket_interval` of 8s (a power of two) given that 600/8 = 74 which is less than 128 buckets maximum. Smaller than 8s would be 4s which would lead to more buckets than the 128 maximum. If bucket\_interval is specified, the RDBMS uses that value instead of deriving it from `bucket_max_count`.
- `ACTIVE` reports have a rich, interactive user interface similar to Enterprise Manager while not requiring any EM installation. The report file built is in HTML format, so it can be interpreted by most modern browsers. The code powering the active report is downloaded transparently by the web browser when the report is first viewed, hence viewing it requires outside connectivity.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information about SQL real-time monitoring.

---

### REPORT\_SQL\_MONITOR\_LIST Function

This function builds a report for all or a sub-set of statements monitored by Oracle. For each statement, the subprogram gives key information and associated global statistics.

Use the REPORT\_SQL\_MONITOR Function to get detail monitoring information for a single SQL statement

See Also:

SQL Performance Reporting Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.REPORT_SQL_MONITOR_LIST(
   sql_id                    IN VARCHAR2  DEFAULT  NULL,
   session_id                IN NUMBER    DEFAULT  NULL,
   session_serial            IN NUMBER    DEFAULT  NULL,
   inst_id                   IN NUMBER    DEFAULT  NULL,
   active_since_date         IN DATE      DEFAULT  NULL,
   active_since_sec          IN NUMBER    DEFAULT  NULL,
   last_refresh_time         IN DATE      DEFAULT  NULL,
   report_level              IN VARCHAR2  DEFAULT  'TYPICAL',
   auto_refresh              IN NUMBER    DEFAULT  NULL,
   base_path                 IN VARCHAR2  DEFAULT  NULL,
   type                      IN VARCHAR2  DEFAULT 'TEXT')
 RETURN CLOB;
```

Parameters

Table 140-34 REPORT\_SQL\_MONITOR\_LIST Function Parameters

| Parameter | Description |
| --- | --- |
| `sql_id` | `SQL_ID` for which monitoring information should be displayed. Use `NULL` (the default) to report on the last statement monitored by Oracle. |
| `session_id` | If not `NULL`, this parameters targets only the sub-set of statements executed by the specified session. Default is `NULL`. Use `-1` or `USERENV` (' `SID` ') for current session. |
| `session_serial` | In addition to the `session_id` parameter, you can also specify its session serial to ensure that the desired session incarnation is targeted. This parameter is ignored when `session_id` is `NULL`. |
| `inst_id` | Only considers statements started on the specified instance. Use -1 to target the login instance. `NULL` (default) targets all instances. |
| `active_since_date` | If not `NULL` (default), returns only monitored statements active since the specified time. This includes all statements that are still executing along with all statements that have completed their execution after the specified date and time. |
| `active_since_sec` | Same as active\_since\_date but with the date specified relative to the current sysdate minus a specified number of seconds. For example, use 3600 to apply a limit of 1 hour. |
| `last_refresh_time` | If not `NULL` (default), the date and time when the list report was last retrieved. This optimizes the case where an application shows the list and refreshes the report on a regular basis (such as once every 5 seconds). In this case, the report shows detail about the execution of monitored queries that active since the specified `last_refresh_time`. For other queries, the report returns the execution key (`sql_id`, `sql_exec_start`, `sql_exec_id`). For queries with a first refresh time after the specified date, only the SQL execution key and statistics are returned. |
| `report_level` | Level of detail for the report. The level can be either:  - `BASIC` - SQL text up to 200 characters - `TYPICAL` - include full SQL text assuming that cursor has not aged out, in which case the SQL text is included up to 2000 characters - `ALL` - currently the same as `TYPICAL` |
| `auto_refresh` | Currently non-operational, reserved for future use |
| `base_path` | URL path for flex HTML resources since flex HTML format is required to access external files (java scripts and the flash SWF file itself) |
| `type` | Report format, `'TEXT'` by default. Can be `'TEXT',` ' `HTML'` or `'XML'`. |

Return Values

A report (XML, text, HTML) for the list of SQL statements that have been monitored.

Usage Notes

The user tuning this function needs to have privilege to access the following fixed views: `GV$SQL_MONITOR` and `GV$SQL`

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information about SQL real-time monitoring.

---

### REPORT\_TUNING\_TASK Function

This procedure displays the results of a tuning task.

See Also:

SQL Performance Reporting Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.REPORT_TUNING_TASK(
   task_name       IN   VARCHAR2,
   type            IN   VARCHAR2   := 'TEXT',
   level           IN   VARCHAR2   := 'TYPICAL',
   section         IN   VARCHAR2   := ALL,
   object_id       IN   NUMBER     := NULL,
   result_limit    IN   NUMBER     := NULL,
   owner_name      IN    VARCHAR2  := NULL,
   execution_name  IN  VARCHAR2    := NULL)
RETURN CLOB;
```

Parameters

Table 140-35 REPORT\_TUNING\_TASK Function Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the tuning task to report |
| `type` | Type of the report to produce. Possible values are `TEXT` which produces a text report. |
| `level` | Level of detail in the report:  - `BASIC`: simple version of the report. Just show info about the actions taken by the advisor. - `TYPICAL`: show information about every statement analyzed, including requests not implemented. - `ALL`: highly detailed report level, also provides annotations about statements skipped over. |
| `section` | Optionally limit the report to a single section (`ALL` for all sections):  - `SUMMARY` - summary information - `FINDINGS` - tuning findings - `PLAN` - explain plans - `INFORMATION` - general information - `ERROR` - statements with errors - `ALL` - all statements |
| `object_id` | Advisor framework object id that represents a single statement to restrict reporting to. `NULL` for all statements. Only valid for reports that target a single execution. |
| `result_limit` | Maximum number of SQL statements to show in the report |
| `owner_name` | Owner of the relevant tuning task. Defaults to the current schema owner. |
| `execution_name` | Name of the task execution to use. If `NULL`, the report is generated for the last task execution. |

Return Values

A `CLOB` containing the desired report.

Examples

```
-- Get the whole report for the single statement case.
SELECT DBMS_SQLTUNE.REPORT_TUNING_TASK(:stmt_task) from dual;
 
-- Show me the summary for the sts case.
SELECT DBMS_SQLTUNE.REPORT_TUNING_TASK(:sts_task, 'TEXT', 'TYPICAL', 'SUMMARY')
FROM DUAL;
 
-- Show me the findings for the statement I'm interested in.
SELECT DBMS_SQLTUNE.REPORT_TUNING_TASK(:sts_task, 'TEXT', 'TYPICAL', 'FINDINGS', 5) from dual;
```

---

### RESET\_TUNING\_TASK Procedure

This procedure is called on a tuning task that is not currently executing to prepare it for re-execution.

See Also:

SQL Tuning Advisor Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.RESET_TUNING_TASK(
 task_name         IN VARCHAR2);
```

Parameters

Table 140-36 RESET\_TUNING\_TASK Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | The name of the tuning task to reset |

Examples

```
-- reset and re-execute a task
EXEC DBMS_SQLTUNE.RESET_TUNING_TASK(:sts_task);
 
-- re-execute the task
EXEC DBMS_SQLTUNE.EXECUTE_TUNING_TASK(:sts_task);
```

---

### RESUME\_TUNING\_TASK Procedure

This procedure resumes a previously interrupted task that was created to process a SQL tuning set.

See Also:

SQL Tuning Advisor Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.RESUME_TUNING_TASK(
 task_name         IN VARCHAR2,
 basic_filter      IN VARCHAR2 := NULL);
```

Parameters

Table 140-37 RESUME\_TUNING\_TASK Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | The name of the tuning task to resume |
| `basic_filter` | A SQL predicate to filter the SQL from the SQL tuning set. Note that this filter is applied in conjunction with the basic filter (i.e., parameter `basic_filter`) when calling CREATE\_TUNING\_TASK Functions. |

Usage Notes

Resuming a single SQL tuning task (a task that was created to tune a single SQL statement as compared to a SQL tuning set) is not supported.

Examples

```
-- Interrupt the task
EXEC DBMS_SQLTUNE.INTERRUPT_TUNING_TASK(:conc_task);
 
-- Once a task is interrupted, we can elect to reset it, resume it, or check
-- out its results and then decide.  For this example we will just resume.
 
EXEC DBMS_SQLTUNE.RESUME_TUNING_TASK(:conc_task);
```

---

### SCRIPT\_TUNING\_TASK Function

This function creates a SQL\*PLUS script which can then be executed to implement a set of Advisor recommendations.

See Also:

SQL Tuning Advisor Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.SCRIPT_TUNING_TASK(
  task_name         IN VARCHAR2,
  rec_type          IN VARCHAR2  := REC_TYPE_ALL,
  object_id         IN NUMBER    := NULL,
  result_limit      IN NUMNBER   := NULL,
  owner_name        IN VARCHAR2  := NULL,
  execution_name    IN VARCHAR2  := NULL)
 RETURN CLOB;
```

Parameters

Table 140-38 SCRIPT\_TUNING\_TASK Function Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the tuning task for which to apply a script |
| `rec_type` | Filter the script by types of recommendations to include. Any subset of the following separated by commas: or ' `ALL`: ' `'PROFILES'` ' `'STATISTICS'` ' `'INDEXES'`. For example, a script with profiles and statistics: `'PROFILES,STATISTICS'` |
| `object_id` | Optionally filters by a single object ID |
| `result_limit` | Optionally shows commands for only top N SQL (ordered by object\_id and ignored if an object\_id is also specified) |
| `owner_name` | Owner of the relevant tuning task. Defaults to the current schema owner |
| `excution_name` | Name of the task execution to use. If `NULL`, the script is generated for the last task execution. |

Return Values

Returns a script in the form of a `CLOB`.

Usage Notes

- Once the script is returned, it should then by checked by the DBA and executed.
- Wrap with a call to `DBMS_ADVISOR.CREATE_FILE` to put it into a file.

Examples

```
SET LINESIZE 140
 
-- Get a script for all actions recommended by the task.
SELECT DBMS_SQLTUNE.SCRIPT_TUNING_TASK(:stmt_task) FROM DUAL;
 
-- Get a script of just the sql profiles we should create.
SELECT DBMS_SQLTUNE.SCRIPT_TUNING_TASK(:stmt_task, 'PROFILES') FROM DUAL;
 
-- get a script of just stale / missing stats
SELECT DBMS_SQLTUNE.SCRIPT_TUNING_TASK(:stmt_task, 'STATISTICS') FROM DUAL;
 
-- Get a script with recommendations about just one SQL statement when we have
-- tuned an entire STS.
SELECT DBMS_SQLTUNE.SCRIPT_TUNING_TASK(:sts_task, 'ALL', 5) FROM DUAL;
```

---

### SELECT\_CURSOR\_CACHE Function

This function collects SQL statements from the SQL Cursor Cache.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.SELECT_CURSOR_CACHE (
  basic_filter        IN   VARCHAR2 := NULL,
  object_filter       IN   VARCHAR2 := NULL,
  ranking_measure1    IN   VARCHAR2 := NULL,
  ranking_measure2    IN   VARCHAR2 := NULL,
  ranking_measure3    IN   VARCHAR2 := NULL,
  result_percentage   IN   NUMBER   := 1,
  result_limit        IN   NUMBER   := NULL,
  attribute_list      IN   VARCHAR2 := NULL,
  recursive_sql       IN   VARCHAR2 := HAS_RECURSIVE_SQL)
 RETURN sys.sqlset PIPELINED;
```

Parameters

Table 140-39 SELECT\_CURSOR\_CACHE Function Parameters

| Parameter | Description |
| --- | --- |
| `basic_filter` | The SQL predicate to filter the SQL from the cursor cache defined on attributes of the `SQLSET_ROW`. If `basic_filter` is not set by the caller, the subprogram captures only statements of the type `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, and `MERGE`. |
| `object_filter` | Currently not supported. |
| `ranking_measure(n)` | An order-by clause on the selected SQL. |
| `result_percentage` | A filter which picks the top N% according to the ranking measure given. Note that this applies only if one ranking measure is given. |
| `result_limit` | The top L(imit) SQL from the (filtered) source ranked by the ranking measure |
| `attribute_list` | List of SQL statement attributes to return in the result. The possible values are:  - `TYPICAL` - `BASIC` + SQL plan (without row source statistics) and without object reference list (default) - `BASIC` - all attributes (such as execution statistics and binds) are returned except the plans. The execution context is always part of the result. - `ALL` - return all attributes - Comma separated list of attribute names this allows to return only a subset of SQL attributes: `EXECUTION_STATISTICS`, `BIND_LIST`, `OBJECT_LIST`, SQL\_PLAN,`SQL_PLAN_STATISTICS`: similar to `SQL_PLAN` + row source statistics |
| `recursive_sql` | Filter that includes recursive SQL in the SQL tuning set (`HAS_RECURSIVE_SQL`) or excludes it (`NO_RECURSIVE_SQL`). |

Return Values

This function returns a one `SQLSET_ROW` per `SQL_ID` or `PLAN_HASH_VALUE` pair found in each data source.

Usage Notes

- Filters provided to this function are evaluated as part of a SQL run by the current user. As such, they are executed with that user's security privileges and can contain any constructs and subqueries that user can access, but no more.
- Users need privileges on the cursor cache views.

Examples

```
-- Get sql ids and sql text for statements with 500 buffer gets.
SELECT sql_id, sql_text 
FROM table(DBMS_SQLTUNE.SELECT_CURSOR_CACHE('buffer_gets > 500')) 
ORDER BY sql_id;
 
-- Get all the information we have about a particular statement.
SELECT * 
FROM table(DBMS_SQLTUNE.SELECT_CURSOR_CACHE('sql_id = ''4rm4183czbs7j'''));
 
-- Notice that some statements can have multiple plans.  The output of the
-- SELECT_XXX table functions is unique by (sql_id, plan_hash_value).  This is
-- because a data source can store multiple plans per sql statement.
SELECT sql_id, plan_hash_value
FROM table(dbms_sqltune.select_cursor_cache('sql_id = ''ay1m3ssvtrh24'''))
ORDER BY sql_id, plan_hash_value;
 
-- PL/SQL examples: load_sqlset is called after opening a cursor, along the
-- lines given below
 
-- Select all statements in the cursor cache.
DECLARE
  cur sys_refcursor;
BEGIN
  OPEN cur FOR
    SELECT value(P) 
    FROM table(DBMS_SQLTUNE.SELECT_CURSOR_CACHE) P;
 
  -- Process each statement (or pass cursor to load_sqlset).
 
  CLOSE cur;
END;/
 
 
-- Look for statements not parsed by SYS.
DECLARE
  cur sys_refcursor;
BEGIN
  OPEN cur for
    SELECT VALUE(P) 
    FROM table(
     DBMS_SQLTUNE.SELECT_CURSOR_CACHE('parsing_schema_name <> ''SYS''')) P;
 
  -- Process each statement (or pass cursor to load_sqlset).
 
  CLOSE cur;
end;/
 
 
-- All statements from a particular module/action.
DECLARE
  cur sys_refcursor;
BEGIN
  OPEN cur FOR
    SELECT VALUE(P) 
    FROM table(
      DBMS_SQLTUNE.SELECT_CURSOR_CACHE(
         'module = ''MY_APPLICATION'' and action = ''MY_ACTION''')) P;
 
  -- Process each statement (or pass cursor to load_sqlset)
 
  CLOSE cur;
END;/
 
 
-- all statements that ran for at least five seconds
DECLARE
  cur sys_refcursor;
BEGIN
  OPEN cur FOR
    SELECT VALUE(P) 
    FROM table(DBMS_SQLTUNE.SELECT_CURSOR_CACHE('elapsed_time > 5000000')) P;
 
  -- Process each statement (or pass cursor to load_sqlset)
 
  CLOSE cur;
end;/
 
 
-- select all statements that pass a simple buffer_gets threshold and 
-- are coming from an APPS user
DECLARE
  cur sys_refcursor;
BEGIN
  OPEN cur FOR
    SELECT VALUE(P) 
    FROM table(
      DBMS_SQLTUNE.SELECT_CURSOR_CACHE(
        'buffer_gets > 100 and parsing_schema_name = ''APPS'''))P;
 
  -- Process each statement (or pass cursor to load_sqlset)
 
  CLOSE cur;
end;/
 
 
-- select all statements exceeding 5 seconds in elapsed time, but also
-- select the plans (by default we only select execution stats and binds
-- for performance reasons - in this case the SQL_PLAN attribute of sqlset_row
-- is NULL) 
DECLARE
  cur sys_refcursor;
BEGIN
  OPEN cur FOR
    SELECT VALUE(P) 
    FROM table(dbms_sqltune.select_cursor_cache(
      'elapsed_time > 5000000', NULL, NULL, NULL, NULL, 1, NULL,
      'EXECUTION_STATISTICS, SQL_BINDS, SQL_PLAN')) P;
 
  -- Process each statement (or pass cursor to load_sqlset)
 
  CLOSE cur;
END;/
 
 
-- Select the top 100 statements in the cursor cache ordering by elapsed_time.
DECLARE
  cur sys_refcursor;
BEGIN
  OPEN cur FOR
    SELECT VALUE(P) 
    FROM table(DBMS_SQLTUNE.SELECT_CURSOR_CACHE(NULL,
                                                NULL,
                                                'ELAPSED_TIME', NULL, NULL,
                                                1,
                                                100)) P;
 
  -- Process each statement (or pass cursor to load_sqlset)
 
  CLOSE cur;
end;/
 
 
-- Select the set of statements which cumulatively account for 90% of the 
-- buffer gets in the cursor cache.  This means that the buffer gets of all
-- of these statements added up is approximately 90% of the sum of all 
-- statements currently in the cache.
DECLARE
  cur sys_refcursor;
BEGIN
  OPEN cur FOR
    SELECT VALUE(P) 
    FROM table(DBMS_SQLTUNE.SELECT_CURSOR_CACHE(NULL,
                                                NULL,
                                                'BUFFER_GETS', NULL, NULL,
                                                .9)) P;
 
  -- Process each statement (or pass cursor to load_sqlset).
 
  CLOSE cur;
END;
/
```

---

### SELECT\_SQL\_TRACE Function

This table function reads the content of one or more trace files and returns the SQL statements it finds in the format of `sqlset_row`.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.SELECT_SQL_TRACE (
  directory              IN VARCHAR2,
  file_name              IN VARCHAR2 := NULL,
  mapping_table_name     IN VARCHAR2 := NULL,
  mapping_table_owner    IN VARCHAR2 := NULL,,
  select_mode            IN POSITIVE := SINGLE_EXECUTION,
  options                IN BINARY_INTEGER := LIMITED_COMMAND_TYPE,
  pattern_start          IN VARCHAR2 := NULL,
  pattern_end            IN VARCHAR2 := NULL,
  result_limit           IN POSITIVE := NULL)
 RETURN sys.sqlset PIPELINED;
```

Parameters

Table 140-40 SELECT\_SQL\_TRACE Function Parameters

| Parameter | Description |
| --- | --- |
| `directory` | The directory object containing the trace file(s). This field is mandatory. |
| `file_name` | All or part of name of the trace file(s) to process. If `NULL` then the current or most recent file in the specified location or path is used. `'%'` wildcards are supported for matching trace file names. |
| `mapping_table_name` | The mapping table name. Note that the mapping table name is case insensitive. If the mapping table name is `NULL`, the mappings in the current database is used. |
| `mapping_table_owner` | the mapping table owner. If it is `NULL`, the current user is used. |
| `select_mode` | the mode for selecting SQL from the trace. By default, it is `SINGLE_EXECUTION`.  - `SINGLE_EXECUTION` - return one execution of a SQL.(default). - `ALL_EXECUTIONS` - return all executions. |
| `options` | The options. By default, it is `LIMITED_COMMAND_TYPE` which can be specified to include SQL statements from all Oracle command types.  - `LIMITED_COMMAND_TYPE` - returns the SQL statements with the command types `CREATE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, `UPSERT`. It is the default. - `ALL_COMMAND_TYPE` - returns the SQL statements with all command types. |
| `pattern_start` | Opening delimiting pattern of the trace file section(s) to consider. CURRENTLY INOPERABLE. |
| `pattern_end` | closing delimiting pattern of the trace file section(s) to process. CURRENTLY INOPERABLE. |
| `result_limit` | Top SQL from the (filtered) source. Default to `MAXSB4` if `NULL`. |

Return Values

This function returns a `SQLSET_ROW` object.

Examples

The following code shows how to enable SQL trace for a few SQL statements and load the results into a SQL tuning set:

```
-- turn on the SQL trace in the capture database
ALTER SESSION SET EVENTS '10046 TRACE NAME CONTEXT FOREVER, LEVEL 4'

-- run sql statements
SELECT 1 FROM DUAL;
SELECT COUNT(*) FROM dba_tables WHERE table_name = :mytab;
 
ALTER SESSION SET EVENTS '10046 TRACE NAME CONTEXT OFF';
 
-- create mapping table from the capture database
CREATE TABLE mapping AS
SELECT object_id id, owner, substr(object_name, 1, 30) name
   FROM dba_objects
   WHERE object_type NOT IN ('CONSUMER GROUP', 'EVALUATION CONTEXT',
                             'FUNCTION', 'INDEXTYPE', 'JAVA CLASS',
                             'JAVA DATA', 'JAVA RESOURCE', 'LIBRARY',
                             'LOB', 'OPERATOR', 'PACKAGE',
                             'PACKAGE BODY', 'PROCEDURE', 'QUEUE',
                             'RESOURCE PLAN', 'TRIGGER', 'TYPE',
                             'TYPE BODY')
UNION ALL
SELECT user_id id, username owner, NULL name
   FROM dba_users;
 
-- create the directory object where the SQL traces are stored
CREATE DIRECTORY SQL_TRACE_DIR as '/home/foo/trace';

-- create the STS
EXEC DBMS_SQLTUNE.CREATE_SQLSET('my_sts', 'test purpose');
 
-- load the SQL statements into STS from SQL TRACE
DECLARE
   cur sys_refcursor;
BEGIN
   OPEN cur FOR
   SELECT value(p)
     FROM TABLE(
        DBMS_SQLTUNE.SELECT_SQL_TRACE(
           directory=>'SQL_TRACE_DIR',
           file_name=>'%trc',
           mapping_table_name=>'mapping')) p;
   DBMS_SQLTUNE.LOAD_SQLSET('my_sts', cur);
   CLOSE cur;
END;
/
```

---

### SELECT\_SQLPA\_TASK Function

This function collects SQL statements from a SQL Performance Analyzer comparison task.

See Also:

- SQL Tuning Set Subprograms for other subprograms in this group
- [Oracle Database Real Application Testing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41481/toc.htm)

Syntax

```
DBMS_SQLTUNE.SELECT_SQLPA_TASK(
    task_name         IN VARCHAR2,
    task_owner        IN VARCHAR2 := NULL,
    execution_name    IN VARCHAR2 := NULL,
    level_filter      IN VARCHAR2 := 'REGRESSED',
    basic_filter      IN VARCHAR2 := NULL,
    object_filter     IN VARCHAR2 := NULL,
    attribute_list    IN VARCHAR2 := 'TYPICAL')
  RETURN sys.sqlset PIPELINED;
```

Parameters

Table 140-41 SELECT\_SQLPA\_TASK Function Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the SQL Performance Analyzer task |
| `task_owner` | Owner of the SQL Performance Analyzer task. If `NULL`, then assume the current user. |
| `execution_name` | Name of the SQL Performance Analyzer task execution (type `COMPARE PERFORMANCE`) from which the provided filters will be applied. If `NULL`, then assume the most recent `COMPARE PERFORMANCE` execution. |
| `level_filter` | Filter to specify which subset of SQLs to include. Same format as `DBMS_SQLPA`. `REPORT_ANALYSIS_TASK``.LEVEL`, with some possible strings removed.  - `IMPROVED` includes only improved SQL. - `REGRESSED` includes only regressed SQL (default). - `CHANGED` includes only SQL with changed performance. - `UNCHANGED` includes only SQL with unchanged performance. - `CHANGED_PLANS` includes only SQL with plan changes. - `UNCHANGED_PLANS` includes only SQL with unchanged plans. - `ERRORS` includes only SQL with errors only. - `MISSING_SQL` includes only missing SQL statements (across STS). - `NEW_SQL` includes only new SQL statements (across STS). |
| `basic filter` | SQL predicate to filter the SQL in addition to the level filters. |
| `object_filter` | Currently not supported. |
| `attribute_list` | List of SQL statement attributes to return in the result. The possible values are:  - `TYPICAL` - `BASIC` + SQL plan (without row source statistics) and without object reference list (default) - `BASIC` - all attributes (such as execution statistics and binds) are returned except the plans. The execution context is always part of the result. - `ALL` - return all attributes - Comma-separated list of attribute names this allows to return only a subset of SQL attributes: `EXECUTION_STATISTICS`, `SQL_BINDS`, `SQL_PLAN_STATISTICS` (similar to `SQL_PLAN` + row source statistics). |

Return Values

This function returns a SQL tuning set object.

Usage Notes

For example, you can use this function to create a SQL tuning set containing the subset of SQL statements that regressed during a SQL Performance Analyzer (SPA) experiment. You can also specify other arbitrary filters.

---

### SELECT\_SQLSET Function

This function reads SQLSET contents.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.SELECT_SQLSET (
  sqlset_name         IN   VARCHAR2,
  basic_filter        IN   VARCHAR2 := NULL,
  object_filter       IN   VARCHAR2 := NULL,
  ranking_measure1    IN   VARCHAR2 := NULL,
  ranking_measure2    IN   VARCHAR2 := NULL,
  ranking_measure3    IN   VARCHAR2 := NULL,
  result_percentage   IN   NUMBER   := 1,
  result_limit        IN   NUMBER   := NULL)
  attribute_list      IN   VARCHAR2 := NULL,
  plan_filter         IN   VARCHAR2 := NULL,
  sqlset_owner        IN   VARCHAR2 := NULL,
  recursive_sql       IN   VARCHAR2 := HAS_RECURSIVE_SQL)
 RETURN sys.sqlset PIPELINED;
```

Parameters

Table 140-42 SELECT\_SQLSET Function Parameters

| Parameter | Description |
| --- | --- |
| `sqlset_name` | The SQL tuning set name |
| `basic_filter` | The SQL predicate to filter the SQL from the SQL tuning set defined on attributes of the `SQLSET_ROW` |
| `object_filter` | Currently not supported. |
| `ranking_measure(n)` | An order-by clause on the selected SQL |
| `result_percentage` | A filter which picks the top N% according to the ranking measure given. Note that this applies only if one ranking measure is given. |
| `result_limit` | The top L(imit) SQL from the (filtered) source ranked by the ranking measure |
| `attribute_list` | List of SQL statement attributes to return in the result. The possible values are:  - `TYPICAL` - `BASIC` + SQL plan (without row source statistics) and without object reference list (default) - `BASIC` - all attributes (such as execution statistics and binds) are returned except the plans. The execution context is always part of the result. - `ALL` - return all attributes - Comma-separated list of attribute names this allows to return only a subset of SQL attributes: `EXECUTION_STATISTICS`, `SQL_BINDS`, `SQL_PLAN_STATISTICS` (similar to `SQL_PLAN` + row source statistics). |
| `plan_filter` | The plan filter |
| `sqlset_owner` | The owner of the SQL tuning set, or `NULL` for the current schema owner |
| `recursive_sql` | Filter that includes recursive SQL in the SQL tuning set (`HAS_RECURSIVE_SQL`) or excludes it (`NO_RECURSIVE_SQL`). |

Return Values

This function returns a one `SQLSET_ROW` per `SQL_ID` or `PLAN_HASH_VALUE` pair found in each data source.

Usage Notes

Filters provided to this function are evaluated as part of a SQL run by the current user. As such, they are executed with that user's security privileges and can contain any constructs and subqueries that user can access, but no more.

Examples

```
-- select from a sql tuning set
DECLARE
  cur sys_refcursor;
BEGIN
  OPEN cur FOR
    SELECT VALUE (P) 
    FROM table(dbms_sqltune.select_sqlset('my_workload')) P;
 
  -- Process each statement (or pass cursor to load_sqlset)
 
  CLOSE cur;
END;
/
```

---

### SELECT\_WORKLOAD\_REPOSITORY Functions

This function collects SQL statements from the workload repository. The overloaded forms let you:

- Collect SQL statements from all snapshots between `begin_snap` and `end_snap`.
- Collect SQL statements from a workload repository baseline.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.SELECT_WORKLOAD_REPOSITORY (
  begin_snap        IN NUMBER,
  end_snap          IN NUMBER,
  basic_filter      IN VARCHAR2 := NULL,
  object_filter     IN VARCHAR2 := NULL,
  ranking_measure1  IN VARCHAR2 := NULL,
  ranking_measure2  IN VARCHAR2 := NULL,
  ranking_measure3  IN VARCHAR2 := NULL,
  result_percentage IN NUMBER   := 1,
  result_limit      IN NUMBER   := NULL,
  attribute_list    IN VARCHAR2 := NULL,
  recursive_sql     IN VARCHAR2 := HAS_RECURSIVE_SQL)
 RETURN sys.sqlset PIPELINED;

DBMS_SQLTUNE.SELECT_WORKLAOD REPOSITORY (
  baseline_name     IN VARCHAR2,
  basic_filter      IN VARCHAR2 := NULL,
  object_filter     IN VARCHAR2 := NULL,
  ranking_measure1  IN VARCHAR2 := NULL,
  ranking_measure2  IN VARCHAR2 := NULL,
  ranking_measure3  IN VARCHAR2 := NULL,
  result_percentage IN NUMBER   := 1,
  result_limit      IN NUMBER   := NULL,
  attribute_list    IN VARCHAR2 := NULL,
  recursive_sql     IN VARCHAR2 := HAS_RECURSIVE_SQL)
 RETURN sys.sqlset PIPELINED;
```

Parameters

Table 140-43 SELECT\_WORKLOAD\_REPOSITORY Function Parameters

| Parameter | Description |
| --- | --- |
| `begin_snap` | Begin snapshot (non-inclusive). |
| `end_snap` | End snapshot (inclusive). |
| `baseline_name` | The name of the baseline period. |
| `basic_filter` | The SQL predicate to filter the SQL from the workload repository defined on attributes of the `SQLSET_ROW`. If `basic_filter` is not set by the caller, the subprogram captures only statements of the type `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, and `MERGE`. |
| `object_filter` | Currently not supported. |
| `ranking_measure(n)` | An order-by clause on the selected SQL. |
| `result_percentage` | A filter which picks the top N% according to the ranking measure given. Note that this applies only if one ranking measure is given. |
| `result_limit` | The top L(imit) SQL from the (filtered) source ranked by the ranking measure. |
| `attribute_list` | List of SQL statement attributes to return in the result. The possible values are:  - `TYPICAL` - `BASIC` + SQL plan (without row source statistics) and without object reference list (default) - `BASIC` - all attributes (such as execution statistics and binds) are returned except the plans. The execution context is always part of the result. - `ALL` - return all attributes - Comma-separated list of attribute names this allows to return only a subset of SQL attributes: `EXECUTION_STATISTICS`, `SQL_BINDS`, `SQL_PLAN_STATISTICS` (similar to `SQL_PLAN` + row source statistics). |
| `recursive_sql` | Filter that includes recursive SQL in the SQL tuning set (`HAS_RECURSIVE_SQL`) or excludes it (`NO_RECURSIVE_SQL`). |

Return Values

This function returns a one `SQLSET_ROW` per `SQL_ID` or `PLAN_HASH_VALUE` pair found in each data source.

Usage Notes

Filters provided to this function are evaluated as part of a SQL run by the current user. As such, they are executed with that user's security privileges and can contain any constructs and subqueries that user can access, but no more.

Examples

```
-- select statements from snapshots 1-2
DECLARE
  cur sys_refcursor;
BEGIN
  OPEN cur FOR
    SELECT VALUE (P) 
    FROM table(dbms_sqltune.select_workload_repository(1,2)) P;
 
  -- Process each statement (or pass cursor to load_sqlset)
 
  CLOSE cur;
END;
/
```

---

### SET\_TUNING\_TASK\_PARAMETER Procedures

This procedure updates the value of a SQL tuning parameter of type `VARCHAR2` or `NUMBER`.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.SET_TUNING_TASK_PARAMETER(
   task_name    IN  VARCHAR2,
   parameter    IN  VARCHAR2,
   value        IN  VARCHAR2);
```
```
DBMS_SQLTUNE.SET_TUNING_TASK_PARAMETER(
   task_name    IN  VARCHAR2,
   parameter    IN  VARCHAR2,
   value        IN  NUMBER);
```

Parameters

Table 140-44 SET\_TUNING\_TASK\_PARAMETER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `task_name` | Identifier of the task to execute |
| `parameter` | Name of the parameter to set. The possible tuning parameters that can be set by this procedure using the parameter in the form `VARCHAR2`:  - `APPLY_CAPTURED_COMPILENV`: indicates whether the advisor could use the compilation environment captured with the SQL statements. The default is `0` (that is, `NO`). - `BASIC_FILTER`: basic filter for SQL tuning set - `DAYS_TO_EXPIRE`: number of days until the task is deleted - `DEFAULT_EXECUTION_TYPE`: the task defaults to this type of execution when none is specified by the EXECUTE\_TUNING\_TASK Function & Procedure - `EXECUTION_DAYS_TO_EXPIRE`: number of days until the tasks's executions is deleted (without deleting the task) - `LOCAL_TIME_LIMIT`: per-statement time out (seconds) - `MODE`: tuning scope (comprehensive, limited) - `OBJECT_FILTER`: object filter for SQL tuning set - `PLAN_FILTER`: plan filter for SQL tuning set (see `SELECT_SQLSET` for possible values) - `RANK_MEASURE1`: first ranking measure for SQL tuning set - `RANK_MEASURE2`: second possible ranking measure for SQL tuning set - `RANK_MEASURE3`: third possible ranking measure for SQL tuning set - `RESUME_FILTER`: a extra filter for SQL tuning sets besides `BASIC_FILTER` - `SQL_LIMIT`: maximum number of SQL statements to tune - `SQL_PERCENTAGE`: percentage filter of SQL tuning set statements - `TEST_EXECUTE`: `FULL` / `AUTO` / `OFF`. 	\* `FULL` - test-execute for as much time as necessary, up to the local time limit for the SQL (or the global task time limit if no SQL time limit is set) 	\* `AUTO` - test-execute for an automatically-chosen time proportional to the tuning time 	\* `OFF` - do not test-execute - `TIME_LIMIT`: global time out (seconds) - `USERNAME`: username under which the statement is parsed |
| `value` | New value of the specified parameter |

Usage Notes

When setting automatic tuning task parameters, use the [SET\_AUTO\_TUNING\_TASK\_PARAMETER Procedures](d_autosta.md) in the [DBMS\_AUTO\_SQLTUNE](d_autosta.md) package.

---

### SQLTEXT\_TO\_SIGNATURE Function

This function returns a SQL text's signature. The signature can be used to identify SQL text in `dba_sql_profiles`.

See Also:

SQL Profile Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.SQLTEXT_TO_SIGNATURE (
  sql_text    IN CLOB,  force_match IN BOOLEAN  := FALSE)
 RETURN NUMBER;
```

Parameters

Table 140-45 SQLTEXT\_TO\_SIGNATURE Function Parameters

| Parameter | Description |
| --- | --- |
| `sql_text` | SQL text whose signature is required. Required. |
| `force_match` | If `TRUE`, this returns a signature that supports SQL matching with literal values transformed into bind variables. If `FALSE`, returns the signature based on the text with literals not transformed |

Return Values

This function returns the signature of the specified SQL text.

---

### UNPACK\_STGTAB\_SQLPROF Procedure

This procedure copies profile data stored in the staging table to create profiles on the system.

See Also:

SQL Profile Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.UNPACK_STGTAB_SQLPROF (
   profile_name          IN VARCHAR2 := '%',
   profile_category      IN VARCHAR2 := 'DEFAULT',
   replace               IN BOOLEAN,
   staging_table_name    IN VARCHAR2,
   staging_schema_owner  IN VARCHAR2 := NULL);
```

Parameters

Table 140-46 UNPACK\_STGTAB\_SQLPROF Procedure Parameters

| Parameter | Description |
| --- | --- |
| `profile_name` | The name of the profile to unpack (% wildcards acceptable, case-sensitive) |
| `profile_category` | The category from which to unpack profiles (% wildcards acceptable, case-sensitive) |
| `replace` | The option to replace profiles if they already exist. Note that profiles cannot be replaced if one in the staging table has the same name as an active profile in a different SQL statement.If `FALSE`, this function raises errors if you try to create a profile that already exists |
| `staging_table_name` | The name of the table on which to perform the remap operation (case-insensitive unless double quoted). Required. |
| `staging_schema_owner` | The schema where the table resides, or `NULL` for current schema (case-insensitive unless double quoted) |

Usage Notes

Using this procedure requires the `CREATE` `ANY` `SQL` `PROFILE` privilege and the `SELECT` privilege on staging table.

Examples

```
-- Unpack all profiles stored in a staging table
EXEC DBMS_SQLTUNE.UNPACK_STGTAB_SQLPROF(replace            => FALSE, -
                                        staging_table_name => 'PROFILE_STGTAB');
 
-- If there is a failure during the unpack operation, users can find the profile
-- we failed on and perform a remap_stgtab_sqlprof operation targeting it.  Then
-- they can resume the unpack operation by setting replace to TRUE so that
-- the profiles that were already created are replaced
EXEC DBMS_SQLTUNE.UNPACK_STGTAB_SQLPROF(replace            => TRUE, -
                                        staging_table_name => 'PROFILE_STGTAB');
```

---

### UNPACK\_STGTAB\_SQLSET Procedure

This procedure copies one or more SQL tuning sets from their location in the staging table into the SQL tuning sets schema, making them proper SQL tuning sets.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.UNPACK_STGTAB_SQLSET (
   sqlset_name          IN VARCHAR2 := '%',
   sqlset_owner         IN VARCHAR2 := NULL,
   replace              IN BOOLEAN,
   staging_table_name   IN VARCHAR2,
   staging_schema_owner IN VARCHAR2 := NULL);
```

Parameters

Table 140-47 UNPACK\_STGTAB\_SQLSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sqlset_name` | The name of the tuning set to unpack (not NULL). Wildcard characters ('%') are supported to unpack multiple tuning sets in a single call. For example, just specify '%' to unpack all tuning sets from the staging table. |
| `sqlset_owner` | The name of tuning set owner, or `NULL` for current schema owner. Wildcards supported. |
| `replace` | Replaces tuning set if they already exist.If `FALSE`, raises errors if you try to create a tuning set that already exists |
| `staging_table_name` | The name of the staging table, moved after a call to the PACK\_STGTAB\_SQLSET Procedure (case-sensitive) |
| `staging_schema_owner` | The name of staging table owner, or `NULL` for current schema owner (case-sensitive) |

Usage Notes

- Users can drop the staging table after this procedure completes successfully.
- The unpack procedure commits after successfully loading each SQL tuning set. If it fails with one tuning set, no part of that tuning set will have been unpacked, but those which the subprogram had already apprehended continue to exist.
- When failures occur due to SQL tuning set name or owner conflicts, users should use the REMAP\_STGTAB\_SQLSET Procedure to patch the staging table, and then call this procedure again to unpack those tuning sets that remain.

Examples

```
-- unpack all STS in the staging table
EXEC DBMS_SQLTUNE.UNPACK_STGTAB_SQLSET(sqlset_name         => '%', -
                                       sqlset_owner        => '%', -
                                       replace             => FALSE, -
                                       staging_table_name  => 'STGTAB_SQLSET');
 
-- errors can arise during STS unpack when a STS in the staging table has the
-- same name/owner as STS on the system.  In this case, users should call
-- remap_stgtab_sqlset to patch the staging table and with which to call unpack
-- Replace set to TRUE.
EXEC DBMS_SQLTUNE.UNPACK_STGTAB_SQLSET(sqlset_name         => '%', -
                                       sqlset_owner        => '%', -
                                       replace             => TRUE, -
                                       staging_table_name  => 'STGTAB_SQLSET');
```

---

### UPDATE\_SQLSET Procedures

This procedure updates selected fields for SQL statement in a SQL tuning set.

See Also:

SQL Tuning Set Subprograms for other subprograms in this group

Syntax

```
DBMS_SQLTUNE.UPDATE_SQLSET (
   sqlset_name      IN  VARCHAR2,
   sql_id           IN  VARCHAR2,
   attribute_name   IN  VARCHAR2,
   attribute_value  IN  VARCHAR2 := NULL);

DBMS_SQLTUNE.UPDATE_SQLSET (
   sqlset_name      IN  VARCHAR2,
   sql_id           IN  VARCHAR2,
   attribute_name   IN  VARCHAR2,
   attribute_value IN NUMBER := NULL);
```

Parameters

Table 140-48 UPDATE\_SQLSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sqlset_name` | The SQL tuning set name |
| `sql_id` | The identifier of the statement to update |
| `attribute_name` | The name of the attribute to modify |
| `attribute_value` | The new value of the attribute |