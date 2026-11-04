---
title: Using Plan Stability
book: Performance Tuning Guide
doc_id: E41573-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41573/outlines.htm
tags:
  - oracle
  - 11g
  - performance-tuning-guide
---

## 20 Using Plan Stability

This chapter describes how to use plan stability to preserve performance characteristics. Plan stability also facilitates migration from the rule-based optimizer to the query optimizer when you upgrade to a new Oracle Database release.

This chapter contains the following topics:

- Using Plan Stability to Preserve Execution Plans
- Using Plan Stability with Query Optimizer Upgrades

Note:

Stored outlines will be desupported in a future release in favor of SQL plan management. In Oracle Database 11g, stored outlines continue to function as in past releases. However, Oracle strongly recommends that you use SQL plan management for new applications. SQL plan management creates SQL plan baselines, which offer superior SQL performance and stability compared with stored outlines.

If you have existing stored outlines, then consider migrating them to SQL plan baselines by following the steps in ["Migrating Stored Outlines to SQL Plan Baselines"](optplanmgmt.md). When the migration is complete, disable or remove the stored outlines.

See Also:

- [Chapter 15, "Using SQL Plan Management"](optplanmgmt.md) for information about SQL plan management
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_spm.htm#ARPLS150) for information about the `DBMS_SPM` package
- [Oracle Database Licensing Information](https://docs.oracle.com/cd/E11882_01/license.112/e47877/editions.htm#DBLIC116) to determine whether your database edition includes SQL Plan Management

## 20.1 Using Plan Stability to Preserve Execution Plans

Plan stability prevents certain database environment changes from affecting the performance characteristics of applications. Such changes include changes in optimizer statistics, changes to the optimizer mode settings, and changes to parameters affecting the sizes of memory structures, such as `SORT_AREA_SIZE` and `BITMAP_MERGE_AREA_SIZE`. Plan stability is most useful when you cannot risk any performance changes in an application.

Plan stability preserves execution plans in stored outlines. An outline is implemented as a set of optimizer hints that are associated with the SQL statement. If the use of the outline is enabled for the statement, then Oracle Database automatically considers the stored hints and tries to generate an execution plan in accordance with those hints.

Oracle Database can create a public or private stored outline for one or all SQL statements. The optimizer then generates equivalent execution plans from the outlines when you enable the use of stored outlines. You can group outlines into categories and control which category of outlines Oracle Database uses to simplify outline administration and deployment.

The plans that Oracle Database maintains in stored outlines remain consistent despite changes to a system's configuration or statistics. Using stored outlines also stabilizes the generated execution plan if the optimizer changes in subsequent Oracle Database releases.

Note:

If you develop applications for mass distribution, then you can use stored outlines to ensure that all customers access the same execution plans.

### 20.1.1 Using Hints with Plan Stability

The degree to which plan stability controls execution plans is dictated by how much the Oracle Database hint mechanism controls execution plans, because Oracle Database uses hints to record stored plans.

There is a one-to-one correspondence between SQL text and its stored outline. If you specify a different literal in a predicate, then a different outline applies. To avoid this situation, replace literals in applications with bind variables.

See Also:

Oracle Database can allow similar statements to share SQL by replacing literals with system-generated bind variables. This works with plan stability if the outline was generated using the `CREATE_STORED_OUTLINES` parameter, not the `CREATE` `OUTLINE` statement. Also, the outline must have been created with the `CURSOR_SHARING` parameter set to `FORCE`, and the parameter must also set to `FORCE` when attempting to use the outline. See [Chapter 7, "Configuring and Using Memory"](memory.md) for more information.

Plan stability relies on preserving execution plans at a point in time when performance is satisfactory. In many environments, however, attributes for data types such as `dates` or `order numbers` can change rapidly. In these cases, permanent use of an execution plan can result in performance degradation over time as the data characteristics change.

This implies that techniques that rely on preserving plans in dynamic environments are somewhat contrary to the purpose of using query optimization. Query optimization attempts to produce execution plans based on statistics that accurately reflect the state of the data. Thus, you must balance the need to control plan stability with the benefit obtained from the optimizer's ability to adjust to changes in data characteristics.

#### 20.1.1.1 How Outlines Use Hints

An outline consists primarily of a set of hints that is equivalent to the optimizer's results for the execution plan generation of a particular SQL statement. When Oracle Database creates an outline, plan stability examines the optimization results using the same data used to generate the execution plan. That is, Oracle Database uses the input to the execution plan to generate an outline, and not the execution plan itself.

Note:

Oracle Database creates the `USER_OUTLINES` and `USER_OUTLINE_HINTS` views in the `SYS` tablespace based on data in the `OL$` and `OL$HINTS` tables, respectively. Direct manipulation of the `OL$`, `OL$HINTS`, and `OL$NODES` tables is prohibited.

You can embed hints in SQL statements, but this has no effect on how Oracle Database uses outlines. Oracle Database considers a SQL statement that you revised with hints to be different from the original SQL statement stored in the outline.

### 20.1.2 Storing Outlines

Oracle Database stores outline data in the `OL$`, `OL$HINTS`, and `OL$NODES` tables. Unless you remove them, Oracle Database retains outlines indefinitely.

The only effect outlines have on caching execution plans is that the database uses the outline category name in addition to the SQL text to determine whether the plan is in cache. This ensures that Oracle Database does not use an execution plan compiled under one category to execute a SQL statement that the database should compile under a different category.

### 20.1.3 Enabling Plan Stability

Settings for several parameters, especially those ending with the suffix `_ENABLED`, must be consistent across execution environments for outlines to function properly. These parameters are:

- `QUERY_REWRITE_ENABLED`
- `STAR_TRANSFORMATION_ENABLED`
- `OPTIMIZER_FEATURES_ENABLE`

### 20.1.4 Using Supplied Packages to Manage Stored Outlines

The `DBMS_OUTLN` and `DBMS_OUTLN_EDIT` package provides procedures used for managing stored outlines and their outline categories.

Users need the `EXECUTE_CATALOG_ROLE` role to execute `DBMS_OUTLN`, but public has execute privileges on `DBMS_OUTLN_EDIT`. The `DBMS_OUTLN_EDIT` package is an invoker's rights package.

Some of the useful `DBMS_OUTLN` and `DBMS_OUTLN_EDIT` procedures are:

- `CLEAR_USED` - Clears specified outline
- `DROP_BY_CAT` - Drops outlines that belong to a specified category
- `UPDATE_BY_CAT` - Changes the category of outlines in one specified category to a new specified category
- `EXACT_TEXT_SIGNATURES` - Computes an outline signature according to an exact text matching scheme
- `GENERATE_SIGNATURE` - Generates a signature for the specified SQL text
	See Also:
	[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_outln.htm#ARPLS034) for detailed information on using `DBMS_OUTLN` package procedures

### 20.1.5 Creating Outlines

Oracle Database can automatically create outlines for all SQL statements, or you can create them for specific SQL statements. In either case, the outlines derive their input from the optimizer.

Oracle Database creates stored outlines automatically when you set the initialization parameter `CREATE_STORED_OUTLINES` to `true`. When activated, Oracle Database creates outlines for all compiled SQL statements. You can create stored outlines for specific statements using the `CREATE` `OUTLINE` statement.

When creating or editing a private outline, the outline data is written to global temporary tables in the `SYSTEM` schema. These tables are accessible with the `OL$`, `OL$HINTS`, and `OL$NODES` synonyms.

Note:

You must ensure that schemas in which outlines are to be created have the `CREATE` `ANY` `OUTLINE` privilege. Otherwise, despite having turned on the `CREATE_STORED_OUTLINE` initialization parameter, no outlines appear in the database after you run the application.

Also, the default system tablespace can become exhausted if the `CREATE_STORED_OUTLINES` initialization parameter is enabled and the running application has many literal SQL statements. If this happens, then use the `DBMS_OUTLN`.`DROP_UNUSED` procedure to remove those literal SQL outlines.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_6005.htm#SQLRF01305) for more information on the `CREATE` `OUTLINE` statement
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_outln.htm#ARPLS034) for more information on the `DBMS_OUTLN` and `DBMS_OUTLN_EDIT` packages
- "Moving from RBO to the Query Optimizer" to learn how to move from the rule-based optimizer to the query optimizer

#### 20.1.5.1 Using Category Names for Stored Outlines

You can categorize outlines to simplify the management task. The `CREATE` `OUTLINE` statement allows for specification of a category. The `DEFAULT` category is chosen if unspecified. Likewise, the `CREATE_STORED_OUTLINES` initialization parameter lets you specify a category name, where specifying `true` produces outlines in the `DEFAULT` category.

If you specify a category name using the `CREATE_STORED_OUTLINES` initialization parameter, then Oracle Database assigns all subsequently created outlines to that category until you reset the category name. Set the parameter to `false` to suspend outline generation.

If you set `CREATE_STORED_OUTLINES` to `true`, or if you use the `CREATE` `OUTLINE` statement without a category name, then Oracle Database assigns outlines to the category name of `DEFAULT`.

### 20.1.6 Using Stored Outlines

When you activate the use of stored outlines, Oracle Database always uses the query optimizer. Outlines rely on hints. To be effective, most hints require the optimizer.

To use stored outlines when Oracle Database compiles a SQL statement, set the system parameter `USE_STORED_OUTLINES` to `true` or to a category name. If you set `USE_STORED_OUTLINES` to `true`, then Oracle Database uses outlines in the `default` category. If you specify a category with the `USE_STORED_OUTLINES` parameter, then Oracle Database uses outlines in that category until you reset the parameter to another category name or until you suspend outline use by setting `USE_STORED_OUTLINES` to `false`. If you specify a category name, and if Oracle Database does not find an outline in that category that matches the SQL statement, then the database searches for an outline in the `default` category.

To use a specific outline rather than all the outlines in a category, execute the `ALTER` `OUTLINE` statement to enable the specific outline. To use the outlines in a category except for a specific outline, use the `ALTER` `OUTLINE` statement to disable the specific outline in the category that is being used. The `ALTER` `OUTLINE` statement can also rename a stored outline, reassign it to a different category, or regenerate it.

The designated outlines only control the compilation of SQL statements that have outlines. If you set `USE_STORED_OUTLINES` to `false`, then Oracle Database does not use outlines. When you set `USE_STORED_OUTLINES` to `false` and you set `CREATE_STORED_OUTLINES` to `true`, Oracle Database creates outlines but does not use them.

The `USE_PRIVATE_OUTLINES` parameter lets you control the use of private outlines. A private outline is an outline seen only in the current session and whose data resides in the current parsing schema. Any changes made to such an outline are not seen by any other session on the system, and applying a private outline to the compilation of a statement can only be done in the current session with the `USE_PRIVATE_OUTLINES` parameter. Only when you explicitly choose to save your edits back to the public area are they seen by the rest of the users.

While the optimizer usually chooses optimal plans for queries, there are times when users know things about the execution environment that are inconsistent with the heuristics that the optimizer follows. By editing outlines directly, you can tune the SQL query without having to alter the application.

When the `USE_PRIVATE_OUTLINES` parameter is enabled and an outlined SQL statement is issued, the optimizer retrieves the outline from the session private area rather than the public area used when `USE_STORED_OUTLINES` is enabled. If no outline exists in the session private area, then the optimizer does not use an outline to compile the statement.

Any `CREATE` `OUTLINE` statement requires the `CREATE` `ANY` `OUTLINE` privilege. Specification of the `FROM` clause also requires the `SELECT` privilege. This privilege should be granted only to those users who would have the authority to view SQL text and hint text associated with the outlined statements. This role is required for the `CREATE` `OUTLINE` `FROM` command unless the issuer of the command is also the owner of the outline.

Note:

The `USE_STORED_OUTLINES` and `USE_PRIVATE_OUTLINES` parameters are system or session specific. They are not initialization parameters. For more information on these parameters, see the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm).

You can test whether the database is using an outline with the `V$SQL` view. Query the `OUTLINE_CATEGORY` column in conjunction with the SQL statement. If the database applied an outline, then this column contains the category to which the outline belongs. Otherwise, it is `NULL`. The `OUTLINE_SID` column tells you whether this particular cursor is using a public outline (value is 0) or a private outline (session's SID of the corresponding session using it).

For example:

```
SELECT OUTLINE_CATEGORY, OUTLINE_SID
  FROM V$SQL 
  WHERE SQL_TEXT LIKE 'SELECT COUNT(*) FROM emp%';
```

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_2005.htm#SQLRF00810) to learn about the `ALTER` `OUTLINE` statement

### 20.1.7 Viewing Outline Data

You can access information about outlines and related hint data that Oracle Database stores in the data dictionary from the following views:

- `USER_OUTLINES`
- `USER_OUTLINE_HINTS`
- `ALL_OUTLINES`
- `ALL_OUTLINE_HINTS`
- `DBA_OUTLINES`
- `DBA_OUTLINE_HINTS`

Use the following syntax to obtain outline information from the `USER_OUTLINES` view, where the outline category is `mycat`:

```
SELECT NAME, SQL_TEXT 
  FROM USER_OUTLINES 
  WHERE CATEGORY='mycat';
```

Oracle Database responds by displaying the names and text of all outlines in category `mycat`.

To see all generated hints for the outline `name1`, use the following syntax:

```
SELECT HINT 
  FROM USER_OUTLINE_HINTS 
  WHERE NAME='name1';
```

You can check the flags in `_OUTLINES` views for information about compatibility, format, and whether an outline is enabled. For example, check the `ENABLED` field in the `USER_OUTLINES` view to determine whether an outline is enabled or not.

```
SELECT NAME, CATEGORY, ENABLED FROM USER_OUTLINES;
```

### 20.1.8 Moving Outline Tables

Oracle Database creates the `USER_OUTLINES` and `USER_OUTLINE_HINTS` views based on data in the `OL$` and `OL$HINTS` tables, respectively. These tables and the `OL$NODES` table reside in the `outln` schema.

The `outln` schema stores data in the `SYSTEM` tablespace. If outlines use too much space in the `SYSTEM` tablespace, then you can move them. To achieve this goal, create a separate tablespace and move the outline tables into this tablespace.

Note:

The default system tablespace could become exhausted if the `CREATE_STORED_OUTLINES` parameter is on and if the running application has many literal SQL statements. In this case, use the `DBMS_OUTLN`.`DROP_UNUSED` procedure to remove the literal SQL outlines.

To move outline tables into a new tablespace:

1. Use the Oracle Data Pump Export utility to export the `OL$`, `OL$HINTS`, and `OL$NODES` tables.
	The following example exports these tables to the `exp.dmp` file located in the directory that maps to the `outln_dir` object:
	```
	% expdp outln DIRECTORY=outln_dir DUMPFILE=exp.dmp TABLES=OL$,OL$HINTS,OL$NODES
	Password: password
	```
2. Start SQL\*Plus and connect to the database as the `outln` user, as shown in the following example:
	```
	SQL> CONNECT outln
	Enter password: password
	```
3. Remove the previous `OL$`, `OL$HINTS`, and `OL$NODES` tables, as shown in the following example:
	```
	SQL> DROP TABLE OL$;
	SQL> DROP TABLE OL$HINTS; 
	SQL> DROP TABLE OL$NODES;
	```
4. Create a new tablespace for the tables.
	The following example connects as `SYSTEM` and creates a tablespace named `outln_ts`:
	```
	SQL> CONNECT SYSTEM
	Enter password: password
	SQL> CREATE TABLESPACE outln_ts DATAFILE 'tspace.dat' SIZE 2M
	  2 DEFAULT STORAGE ( INITIAL 10K NEXT 20K MINEXTENTS 1 MAXEXTENTS 999
	  3                   PCTINCREASE 10 ) ONLINE;
	```
5. Change the default tablespace for the `outln` schema.
	The following statement changes the default tablespace to `outln_ts`:
	```
	SQL> ALTER USER OUTLN DEFAULT TABLESPACE outln_ts;
	```
6. To force the import into the `outln_ts` tablespace, perform the following tasks:
	1. Set the quota for the `SYSTEM` tablespace to `0K` for the `outln` user.
		2. Revoke the `UNLIMITED TABLESPACE` privilege and all roles, such as the `RESOURCE` role, that have unlimited tablespace privileges or quotas.
		3. Set a quota for the `outln` tablespace.
7. Use the Data Pump Import utility to import the `OL$`, `OL$HINTS`, and `OL$NODES` tables, as in the following example:
	```
	% impdp outln DIRECTORY=outln_dir DUMPFILE=exp.dmp TABLES=OL$,OL$HINTS,OL$NODES
	Password: password
	```
	When the import completes, the `OL$`, `OL$HINTS`, and `OL$NODES` tables are re-created in the schema named `outln` and reside in the `outln_ts` tablespace.
8. Optionally, adjust the tablespace quotas for the `outln` user appropriately by adding any privileges and roles that were removed in a previous step.

See Also:

- [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_overview.htm#SUTIL100) for detailed information about using the Data Pump Export and Import utilities
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_outln.htm#ARPLS034) for detailed information about using the `DBMS_OUTLN` package

## 20.2 Using Plan Stability with Query Optimizer Upgrades

This section describes procedures you can use to significantly improve performance by taking advantage of query optimizer functionality. Plan stability provides a way to preserve a system's targeted execution plans with satisfactory performance while also taking advantage of new query optimizer features for the rest of the SQL statements.

While there are classes of SQL statements and features where an exact reproduction of the original execution plan is not guaranteed, plan stability can still be a highly useful part of the migration. Before the migration, outline capturing of execution plan should be turned on until all or most of the applications SQL-statement have been covered.

If performance problems for some specific SQL-statement occur after migration, then you can turn on the stored outline for the specified statement as a way of restoring the old behavior. Stored outlines are not always the best way of resolving a migration related performance problem because they prevent plans from adapting to changing data properties. However, stored outlines add to the arsenal of techniques that you can use to address such problems.

Topics covered in this section are:

- Moving from RBO to the Query Optimizer
- Moving to a New Oracle Release under the Query Optimizer

### 20.2.1 Moving from RBO to the Query Optimizer

If an application was developed using the rule-based optimizer, then a considerable amount of effort might have gone into manually tuning the SQL statements to optimize performance. You can use plan stability to leverage the effort that has gone into performance tuning by preserving the behavior of the application when upgrading from rule-based to query optimization.

By creating outlines for an application before switching to query optimization, the plans generated by the rule-based optimizer can be used, while statements generated by newly written applications developed after the switch use query plans. To create and use outlines for an application, use the following process.

Note:

Carefully read this procedure and consider its implications before executing it!
1. Ensure that schemas in which outlines are to be created have the `CREATE` `ANY` `OUTLINE` privilege. For example, from `SYS`:
	```
	GRANT CREATE ANY OUTLINE TO user-name
	```
2. Execute syntax similar to the following to designate; for example, the `RBOCAT` outline category.
	```
	ALTER SESSION SET CREATE_STORED_OUTLINES = rbocat;
	```
3. Run the application long enough to capture stored outlines for all important SQL statements.
4. Suspend outline generation:
	```
	ALTER SESSION SET CREATE_STORED_OUTLINES = FALSE;
	```
5. Gather statistics with the `DBMS_STATS` package.
6. Alter the parameter `OPTIMIZER_MODE` to `CHOOSE`.
7. Enter the following syntax to make Oracle database use the outlines in category `RBOCAT`:
	```
	ALTER SESSION SET USE_STORED_OUTLINES = rbocat;
	```
8. Run the application.
	Subject to the limitations of plan stability, access paths for this application's SQL statements should be unchanged.
	Note:
	If a query was not executed in step 2, then you can capture the old behavior of the query even after switching to query optimization. To achieve this goal, change the optimizer mode to `RULE`, create an outline for the query, and then change the optimizer mode back to `CHOOSE`.

### 20.2.2 Moving to a New Oracle Release under the Query Optimizer

When upgrading to a new Oracle Database release under query optimization, some SQL statements may have their execution plans changed because of changes in the optimizer. While such changes benefit performance, you might have applications that perform so well that you would consider any changes in their behavior to be an unnecessary risk. For such applications, you can create outlines before the upgrade using the following procedure.

Note:

Carefully read this procedure and consider its implications before running it!
1. Enter the following syntax to enable outline creation:
	```
	ALTER SESSION SET CREATE_STORED_OUTLINES = ALL_QUERIES;
	```
2. Run the application long enough to capture stored outlines for all critical SQL statements.
3. Enter this syntax to suspend outline generation:
	```
	ALTER SESSION SET CREATE_STORED_OUTLINES = FALSE;
	```
4. Upgrade the production system to the new version of the RDBMS.
5. Run the application.

After the upgrade, you can enable the use of stored outlines, or alternatively, you can use the outlines that were stored as a backup if you find that some statements exhibit performance degradation after the upgrade.

With the latter approach, you can selectively use the stored outlines for such problematic statements as follows:

1. For each problematic SQL statement, change the `CATEGORY` of the associated stored outline to a category name similar to this:
	```
	ALTER OUTLINE outline_name CHANGE CATEGORY TO problemcat;
	```
2. Enter this syntax to make Oracle database use outlines from the category `problemcat`.
	```
	ALTER SESSION SET USE_STORED_OUTLINES = problemcat;
	```

#### 20.2.2.1 Upgrading with a Test System

A test database, separate from the production database, is useful for conducting experiments with optimizer behavior after an upgrade. You can migrate statistics from the production system to the test system using import/export. This technique alleviates the need to fill the tables in the test database with data.

You can move outlines between the systems by category. For example, after you create outlines in the `problemcat` category, export them by category using the query-based export option. This is a convenient and efficient way to export only selected outlines from one database to another without exporting all outlines in the source database. Use the Data Pump Export utility with the `QUERY` parameter as in the following example (note the use of the line continuation character):

```
% expdp outln DIRECTORY=outln_dir DUMPFILE=exp_file.dmp \
?  TABLES=OL$,OL$HINTS,OL$NODES QUERY='WHERE CATEGORY="problemcat"'
Password: password
```

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_overview.htm#SUTIL100) for detailed information about using the Data Pump Export and Import utilities