---
title: SQL Tuning Guide
book: SQL Tuning Guide
doc_id: E85762-06
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/tgsql/generating-and-displaying-execution-plans.html
tags:
  - oracle
  - 12c
  - sql-tuning-guide
---

A thorough understanding of execution plans is essential to SQL tuning.

This chapter contains the following topics:

### 6.1 Introduction to Execution Plans

The combination of the steps that Oracle Database uses to execute a statement is an **execution plan**.

Each step either retrieves rows of data physically from the database or prepares them for the user issuing the statement. An execution plan includes an [access path](glossary.md) for each table that the statement accesses and an ordering of the tables (the [join order](glossary.md)) with the appropriate [join method](glossary.md).

### 6.2 About Plan Generation and Display

The `EXPLAIN PLAN` statement displays execution plans that the optimizer chooses for `SELECT`, `UPDATE`, `INSERT`, and `DELETE` statements.

This section contains the following topics:

#### 6.2.1 About the Plan Explanation

A statement execution plan is the sequence of operations that the database performs to run the statement.

The [row source tree](glossary.md) is the core of the execution plan. The tree shows the following information:

- An ordering of the tables referenced by the statement
- An access method for each table mentioned in the statement
- A join method for tables affected by join operations in the statement
- Data operations like filter, sort, or aggregation

In addition to the row source tree, the plan table contains information about the following:

- Optimization, such as the cost and cardinality of each operation
- Partitioning, such as the set of accessed partitions
- Parallel execution, such as the distribution method of join inputs

You can use the `EXPLAIN PLAN` results to determine whether the optimizer chose a particular execution plan, such as a nested loops join. The results also help you to understand the optimizer decisions, such as why the optimizer chose a nested loops join instead of a hash join.

See Also:

- " [SQL Row Source Generation](sql-processing.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=SQLRF01601) to learn about the `EXPLAIN PLAN` statement

#### 6.2.2 Why Execution Plans Change

Execution plans can and do change as the underlying optimizer inputs change.

`EXPLAIN PLAN` output shows how the database would run the SQL statement when the statement was explained. This plan can differ from the actual execution plan a SQL statement uses because of differences in the execution environment and explain plan environment.

Note:

To avoid possible SQL performance regression that may result from execution plan changes, consider using SQL plan management.

This section contains the following topics:

See Also:

- " [Overview of SQL Plan Management](overview-of-sql-plan-management.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=ARPLS150) to learn about the `DBMS_SPM` package

##### 6.2.2.1 Different Schemas

Schemas can differ for various reasons.

Principal reasons include the following:

- The execution and explain plan occur on different databases.
- The user explaining the statement is different from the user running the statement. Two users might be pointing to different objects in the same database, resulting in different execution plans.
- Schema changes (often changes in indexes) between the two operations.

##### 6.2.2.2 Different Costs

Even if the schemas are the same, the optimizer can choose different execution plans when the costs are different.

Some factors that affect the costs include the following:

- Data volume and statistics
- Bind variable types and values
- Initialization parameters set globally or at session level

#### 6.2.3 Guideline for Minimizing Throw-Away

Examining an explain plan enables you to look for rows that are thrown-away.

The database often throws away rows in the following situations:

- Full scans
- Unselective range scans
- Late predicate filters
- Wrong join order
- Late filter operations

In the plan shown in Example 6-1, the last step is a very [unselective](glossary.md) range scan that is executed 76,563 times, accesses 11,432,983 rows, throws away 99% of them, and retains 76,563 rows. Why access 11,432,983 rows to realize that only 76,563 rows are needed?

Example 6-1 Looking for Thrown-Away Rows in an Explain Plan

```
Rows      Execution Plan
--------  ----------------------------------------------------
      12  SORT AGGREGATE
       2   SORT GROUP BY
   76563    NESTED LOOPS
   76575     NESTED LOOPS
      19      TABLE ACCESS FULL CN_PAYRUNS_ALL
   76570      TABLE ACCESS BY INDEX ROWID CN_POSTING_DETAILS_ALL
   76570       INDEX RANGE SCAN (object id 178321)
   76563     TABLE ACCESS BY INDEX ROWID CN_PAYMENT_WORKSHEETS_ALL
11432983      INDEX RANGE SCAN (object id 186024)
```

#### 6.2.4 Guidelines for Evaluating Execution Plans Using EXPLAIN PLAN

The execution plan operation alone cannot differentiate between well-tuned statements and those that perform suboptimally.

For example, an `EXPLAIN PLAN` output that shows that a statement uses an index does not necessarily mean that the statement runs efficiently. Sometimes indexes are extremely inefficient. In this case, a good practice is to examine the following:

- The columns of the index being used
- Their selectivity (fraction of table being accessed)

It is best to use `EXPLAIN PLAN` to determine an access plan, and then later prove that it is the optimal plan through testing. When evaluating a plan, examine the statement's actual resource consumption.

This section contains the following topics:

#### 6.2.5 Guidelines for Evaluating Plans Using the V$SQL\_PLAN Views

As an alternative to running the `EXPLAIN PLAN` command and displaying the plan, you can display the plan by querying the `V$SQL_PLAN` view.

`V$SQL_PLAN` contains the execution plan for every statement stored in the shared SQL area. Its definition is similar to `PLAN_TABLE`.

The advantage of `V$SQL_PLAN` over `EXPLAIN PLAN` is that you do not need to know the compilation environment that was used to execute a particular statement. For `EXPLAIN PLAN`, you would need to set up an identical environment to get the same plan when executing the statement.

The `V$SQL_PLAN_STATISTICS` view provides the actual execution statistics for every operation in the plan, such as the number of output rows and elapsed time. All statistics, except the number of output rows, are cumulative. For example, the statistics for a join operation also includes the statistics for its two inputs. The statistics in `V$SQL_PLAN_STATISTICS` are available for cursors that have been compiled with the `STATISTICS_LEVEL` initialization parameter set to `ALL`.

The `V$SQL_PLAN_STATISTICS_ALL` view enables side by side comparisons of the estimates that the optimizer provides for the number of rows and elapsed time. This view combines both `V$SQL_PLAN` and `V$SQL_PLAN_STATISTICS` information for every cursor.

See Also:

- " [PLAN\_TABLE Columns](reading-execution-plans.md) "
- " [Monitoring Database Operations](monitoring-database-operations.md) " for information about the `V$SQL_PLAN_MONITOR` view
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=REFRN-GUID-87561B21-721C-42EB-8E3D-28251C9BC50C) for more information about `V$SQL_PLAN` views
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=REFRN-GUID-16B23F95-8644-407A-A6C8-E85CADFA61FF) for information about the `STATISTICS_LEVEL` initialization parameter

#### 6.2.6 EXPLAIN PLAN Restrictions

Oracle Database does not support `EXPLAIN PLAN` for statements performing implicit type conversion of date bind variables.

With bind variables in general, the `EXPLAIN PLAN` output might not represent the real execution plan.

From the text of a SQL statement, `TKPROF` cannot determine the types of the bind variables. It assumes that the type is `VARCHAR`, and gives an error message otherwise. You can avoid this limitation by putting appropriate type conversions in the SQL statement.

See Also:

- " [Performing Application Tracing](performing-application-tracing.md) "
- " [Guideline for Avoiding the Argument Trap](performing-application-tracing.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=SQLRF-GUID-A3C0D836-BADB-44E5-A5D4-265BA5968483) to learn more about SQL data types

#### 6.2.7 Guidelines for Creating PLAN\_TABLE

The `PLAN_TABLE` is automatically created as a public synonym to a global temporary table.

This temporary table holds the output of `EXPLAIN PLAN` statements for all users. `PLAN_TABLE` is the default sample output table into which the `EXPLAIN` `PLAN` statement inserts rows describing execution plans.

While a `PLAN_TABLE` table is automatically set up for each user, you can use the SQL script `catplan.sql` to manually create the global temporary table and the `PLAN_TABLE` synonym. The name and location of this script depends on your operating system. On UNIX and Linux, the script is located in the `$ORACLE_HOME/rdbms/admin` directory.

For example, start a SQL\*Plus session, connect with `SYSDBA` privileges, and run the script as follows:

```
@$ORACLE_HOME/rdbms/admin/catplan.sql
```

Oracle recommends that you drop and rebuild your local `PLAN_TABLE` table after upgrading the version of the database because the columns might change. This can cause scripts to fail or cause `TKPROF` to fail, if you are specifying the table.

If you do not want to use the name `PLAN_TABLE`, create a new synonym after running the `catplan.sql` script. For example:

```
CREATE OR REPLACE PUBLIC SYNONYM my_plan_table for plan_table$
```

See Also:

- " [PLAN\_TABLE Columns](reading-execution-plans.md) " for a description of the columns in the table
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=SQLRF-GUID-A806C82F-1171-478E-A910-F9C6C42739B2) to learn about `CREATE SYNONYM`

### 6.3 Generating Plan Output Using the EXPLAIN PLAN Statement

The `EXPLAIN PLAN` statement enables you to examine the execution plan that the optimizer chose for a SQL statement.

This section contains the following topics:

#### 6.3.1 Explaining a SQL Statement: Basic Steps

Use `EXPLAIN PLAN` to store the plan for a SQL statement in `PLAN_TABLE`.

Prerequisites

This task assumes that a sample output table named `PLAN_TABLE` exists in your schema. If this table does not exist, then run the SQL script `catplan.sql`.

To execute `EXPLAIN PLAN`, you must have the following privileges:

- You must have the privileges necessary to insert rows into an existing output table that you specify to hold the execution plan
- You must also have the privileges necessary to execute the SQL statement for which you are determining the execution plan. If the SQL statement accesses a view, then you must have privileges to access any tables and views on which the view is based. If the view is based on another view that is based on a table, then you must have privileges to access both the other view and its underlying table.

To examine the execution plan produced by an `EXPLAIN PLAN` statement, you must have the privileges necessary to query the output table.

To explain a statement:

1. Start SQL\*Plus or SQL Developer, and log in to the database as a user with the requisite permissions.
2. Include the `EXPLAIN PLAN FOR` clause immediately before the SQL statement.
	The following example explains the plan for a query of the `employees` table:
	```
	EXPLAIN PLAN FOR
	  SELECT e.last_name, d.department_name, e.salary
	  FROM   employees e, departments d
	  WHERE  salary < 3000
	  AND    e.department_id = d.department_id
	  ORDER BY salary DESC;
	```
3. After issuing the `EXPLAIN PLAN` statement, use a script or package provided by Oracle Database to display the most recent plan table output.
	The following example uses the `DBMS_XPLAN.DISPLAY` function:
	```
	SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY(format => 'ALL'));
	```
4. Review the plan output.
	For example, the following plan shows a hash join:
	```
	SQL> SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY(format => 'ALL'));
	Plan hash value: 3556827125
	-----------------------------------------------------------------------------------
	| Id  | Operation           | Name        | Rows  | Bytes | Cost (%CPU)| Time     |
	-----------------------------------------------------------------------------------
	|   0 | SELECT STATEMENT    |             |     4 |   124 |     5  (20)| 00:00:01 |
	|   1 |  SORT ORDER BY      |             |     4 |   124 |     5  (20)| 00:00:01 |
	|*  2 |   HASH JOIN         |             |     4 |   124 |     4   (0)| 00:00:01 |
	|*  3 |    TABLE ACCESS FULL| EMPLOYEES   |     4 |    60 |     2   (0)| 00:00:01 |
	|   4 |    TABLE ACCESS FULL| DEPARTMENTS |    27 |   432 |     2   (0)| 00:00:01 |
	-----------------------------------------------------------------------------------
	Query Block Name / Object Alias (identified by operation id):
	-------------------------------------------------------------
	   1 - SEL$1
	   3 - SEL$1 / E@SEL$1
	   4 - SEL$1 / D@SEL$1
	Predicate Information (identified by operation id):
	---------------------------------------------------
	   2 - access("E"."DEPARTMENT_ID"="D"."DEPARTMENT_ID")
	   3 - filter("SALARY"<3000)
	Column Projection Information (identified by operation id):
	-----------------------------------------------------------
	   1 - (#keys=1) INTERNAL_FUNCTION("E"."SALARY")[22],
	       "E"."LAST_NAME"[VARCHAR2,25], "D"."DEPARTMENT_NAME"[VARCHAR2,30]
	   2 - (#keys=1) "E"."LAST_NAME"[VARCHAR2,25], "SALARY"[NUMBER,22],
	       "D"."DEPARTMENT_NAME"[VARCHAR2,30], "D"."DEPARTMENT_NAME"[VARCHAR2,30]
	   3 - "E"."LAST_NAME"[VARCHAR2,25], "SALARY"[NUMBER,22],
	       "E"."DEPARTMENT_ID"[NUMBER,22]
	   4 - "D"."DEPARTMENT_ID"[NUMBER,22], "D"."DEPARTMENT_NAME"[VARCHAR2,30]
	Note
	-----
	   - this is an adaptive plan
	```
	The execution order in `EXPLAIN PLAN` output begins with the line that is the furthest indented to the right. The next step is the parent of that line. If two lines are indented equally, then the top line is normally executed first.
	Note:
	The steps in the `EXPLAIN PLAN` output in this chapter may be different on your database. The optimizer may choose different execution plans, depending on database configurations.

See Also:

- " Guidelines for Creating PLAN\_TABLE "
- " Displaying PLAN\_TABLE Output "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=SQLRF-GUID-FD540872-4ED3-4936-96A2-362539931BA0) for the syntax and semantics of `EXPLAIN PLAN`

#### 6.3.2 Executing EXPLAIN PLAN Using a Statement ID

With multiple statements, you can specify a statement identifier and use that to identify your specific execution plan.

Before using `SET STATEMENT ID`, remove any existing rows for that statement ID. In the following example, `st1` is specified as the statement identifier.

Example 6-2 Using EXPLAIN PLAN with the STATEMENT ID Clause

```
EXPLAIN PLAN
  SET STATEMENT_ID = 'st1' FOR
  SELECT last_name FROM employees;
```

#### 6.3.3 Directing EXPLAIN PLAN Output to a Nondefault Table

You can specify the `INTO` clause to specify a different table.

The following statement directs output to `my_plan_table`:

```
EXPLAIN PLAN
  INTO my_plan_table FOR
  SELECT last_name FROM employees;
```

You can specify a statement ID when using the `INTO` clause, as in the following statement:

```
EXPLAIN PLAN
   SET STATEMENT_ID = 'st1'
   INTO my_plan_table FOR
   SELECT last_name FROM employees;
```

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=SQLRF01601) for a complete description of `EXPLAIN PLAN` syntax.

### 6.4 Displaying PLAN\_TABLE Output

You can use scripts or a package to display the plan output.

After you have explained the plan, use the following SQL scripts or PL/SQL package provided by Oracle Database to display the most recent plan table output:

- `utlxpls.sql`
	This script displays the plan table output for serial processing. Example 6-4 is an example of the plan table output when using the `utlxpls.sql` script.
- `utlxplp.sql`
	This script displays the plan table output including parallel execution columns.
- `DBMS_XPLAN.DISPLAY` table function
	This function accepts options for displaying the plan table output. You can specify:
	- A plan table name if you are using a table different than `PLAN_TABLE`
		- A statement ID if you have set a statement ID with the `EXPLAIN PLAN`
		- A format option that determines the level of detail: `BASIC`, `SERIAL`, `TYPICAL`, and `ALL`
	Examples of using `DBMS_XPLAN` to display `PLAN_TABLE` output are:
	```
	SELECT PLAN_TABLE_OUTPUT FROM TABLE(DBMS_XPLAN.DISPLAY());
	SELECT PLAN_TABLE_OUTPUT 
	  FROM TABLE(DBMS_XPLAN.DISPLAY('MY_PLAN_TABLE', 'st1','TYPICAL'));
	```
	This section contains the following topics:
	See Also:
	[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/tgsql&id=ARPLS378) for more information about the `DBMS_XPLAN` package

#### 6.4.1 Displaying an Execution Plan: Example

This example uses `EXPLAIN PLAN` to examine a SQL statement that selects the `employee_id`, `job_title`, `salary`, and `department_name` for the employees whose IDs are less than 103.

Example 6-3 Using EXPLAIN PLAN

```
EXPLAIN PLAN FOR
  SELECT e.employee_id, j.job_title, e.salary, d.department_name
  FROM   employees e, jobs j, departments d
  WHERE  e.employee_id < 103
  AND    e.job_id = j.job_id 
  AND    e.department_id = d.department_id;
```

Example 6-4 EXPLAIN PLAN Output

The following output table shows the execution plan that the optimizer chose to execute the SQL statement in Example 6-3:

```
-----------------------------------------------------------------------------------
| Id  | Operation                     |  Name        | Rows  | Bytes | Cost (%CPU)|
-----------------------------------------------------------------------------------
|   0 | SELECT STATEMENT              |              |     3 |   189 |    10  (10)|
|   1 |  NESTED LOOPS                 |              |     3 |   189 |    10  (10)|
|   2 |   NESTED LOOPS                |              |     3 |   141 |     7  (15)|
|*  3 |    TABLE ACCESS FULL          | EMPLOYEES    |     3 |    60 |     4  (25)|
|   4 |    TABLE ACCESS BY INDEX ROWID| JOBS         |    19 |   513 |     2  (50)|
|*  5 |     INDEX UNIQUE SCAN         | JOB_ID_PK    |     1 |       |            |
|   6 |   TABLE ACCESS BY INDEX ROWID | DEPARTMENTS  |    27 |   432 |     2  (50)|
|*  7 |    INDEX UNIQUE SCAN          | DEPT_ID_PK   |     1 |       |            |
-----------------------------------------------------------------------------------

Predicate Information (identified by operation id):
---------------------------------------------------
   3 - filter("E"."EMPLOYEE_ID"<103)
   5 - access("E"."JOB_ID"="J"."JOB_ID")
   7 - access("E"."DEPARTMENT_ID"="D"."DEPARTMENT_ID"

------------------------------------------------------------------------------------------------
| Id | Operation                       | Name          | Rows  | Bytes | Cost (%CPU)| Time     |
------------------------------------------------------------------------------------------------
|  0 | SELECT STATEMENT                |               |     3 |   189 |     8  (13)| 00:00:01 |
|  1 |  NESTED LOOPS                   |               |       |       |            |          |
|  2 |   NESTED LOOPS                  |               |     3 |   189 |     8  (13)| 00:00:01 |
|  3 |    MERGE JOIN                   |               |     3 |   141 |     5  (20)| 00:00:01 |
|  4 |     TABLE ACCESS BY INDEX ROWID | JOBS          |    19 |   513 |     2   (0)| 00:00:01 |
|  5 |      INDEX FULL SCAN            | JOB_ID_PK     |    19 |       |     1   (0)| 00:00:01 |
|* 6 |     SORT JOIN                   |               |     3 |    60 |     3  (34)| 00:00:01 |
|  7 |      TABLE ACCESS BY INDEX ROWID| EMPLOYEES     |     3 |    60 |     2   (0)| 00:00:01 |
|* 8 |       INDEX RANGE SCAN          | EMP_EMP_ID_PK |     3 |       |     1   (0)| 00:00:01 |
|* 9 |    INDEX UNIQUE SCAN            | DEPT_ID_PK    |     1 |       |     0   (0)| 00:00:01 |
| 10 |   TABLE ACCESS BY INDEX ROWID   | DEPARTMENTS   |     1 |    16 |     1   (0)| 00:00:01 |
------------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   6 - access("E"."JOB_ID"="J"."JOB_ID")
       filter("E"."JOB_ID"="J"."JOB_ID")
   8 - access("E"."EMPLOYEE_ID"<103)
   9 - access("E"."DEPARTMENT_ID"="D"."DEPARTMENT_ID")
```

#### 6.4.2 Customizing PLAN\_TABLE Output

If you have specified a statement identifier, then you can write your own script to query the `PLAN_TABLE`.

For example:

- Start with ID = 0 and given `STATEMENT_ID`.
- Use the `CONNECT BY` clause to walk the tree from parent to child, the join keys being `STATEMENT_ID = PRIOR STATMENT_ID` and `PARENT_ID = PRIOR ID`.
- Use the pseudo-column `LEVEL` (associated with `CONNECT BY`) to indent the children.
	```
	SELECT  cardinality "Rows", lpad(' ',level-1) || operation
	        ||' '||options||' '||object_name "Plan"
	FROM    PLAN_TABLE
	CONNECT BY prior id = parent_id
	        AND prior statement_id = statement_id
	  START WITH id = 0
	        AND statement_id = 'st1'
	  ORDER BY id;
	   Rows Plan
	------- ----------------------------------------
	        SELECT STATEMENT
	         TABLE ACCESS FULL EMPLOYEES
	```
	The `NULL` in the `Rows` column indicates that the optimizer does not have any statistics on the table. Analyzing the table shows the following:
	```
	Rows Plan
	------- ----------------------------------------
	  16957 SELECT STATEMENT
	  16957  TABLE ACCESS FULL EMPLOYEES
	```
	You can also select the `COST`. This is useful for comparing execution plans or for understanding why the optimizer chooses one execution plan over another.
	Note:
	These simplified examples are not valid for recursive SQL.