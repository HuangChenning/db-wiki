---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: F31835-17
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/admin/troubleshooting-problems-with-read-only-materialized-views.html
tags:
  - oracle
  - 21c
  - administrators-guide
---

## 39 Troubleshooting Problems with Read-Only Materialized Views

You can diagnose and solve problems with database links, materialized view creation, and materialized view refresh.

**Parent topic:** [Managing Read-Only Materialized Views](managing-read-only-materialized-views.md)

### 39.1 Diagnosing Problems with Database Links

If you think a database link is not functioning properly, then you can drop and re-create it using Oracle Enterprise Manager Cloud Control, SQL\*Plus, or another tool.

- Ensure that the database link name is the same as the global name of the target database.
- Ensure that the scheduled interval is what you want.
- Ensure that the scheduled interval is not shorter than the required execution time.

If you used a connection qualifier in a database link to a given database, then the other databases that link to that database must have the same connection qualifier. For example, suppose you create a database link as follows:

```
CREATE DATABASE LINK dbs1.example.com@myethernet CONNECT TO myadmin
  IDENTIFIED BY password USING 'connect_string_myethernet';
```

All the databases, whether master databases or materialized view databases, associated with `dbs1.example.com@myethernet` must include `myethernet` as the connection qualifier.

See Also:

- " [Using Connection Qualifiers to Specify Service Names Within Link Names](managing-a-distributed-database.md) " for more information database links and connection qualifiers
- " [Required Database Links for Materialized Views](planning-for-read-only-materialized-views.md) "

**Parent topic:** Troubleshooting Problems with Read-Only Materialized Views

### 39.2 Problems Creating Materialized Views

There are items to check if you have problems creating a materialized view.

If you unsuccessfully attempt to create a materialized view, then try the following:

- Ensure that you have the necessary privileges to create the materialized view. You need `SELECT` privilege on the master table and its materialized view log. See " [Required Privileges](planning-for-read-only-materialized-views.md) " for more information.
- If you are trying to create a fast refresh primary key or subquery materialized view, then ensure that the materialized view log on the master table logs primary keys.
- If you are trying to create a fast refresh rowid materialized view, then ensure that the materialized view log on the master table logs rowids.
- Check if the materialized view log has the required columns added for subquery materialized views. See " [Logging Columns in a Materialized View Log](planning-for-read-only-materialized-views.md) " for information.
- Check if the materialized view log exists for all tables that are involved in a fast refresh materialized view. If the materialized view contains a subquery, then each table referenced in the subquery should have a materialized view log.

**Parent topic:** Troubleshooting Problems with Read-Only Materialized Views

### 39.3 Refresh Problems

You can diagnose and solve common refresh problems.

- Common Refresh Problems  
	Several common factors can prevent the automatic refresh of a group of materialized views.
- Automatic Refresh Retries  
	When Oracle Database fails to refresh a refresh group automatically, the refresh group remains due for its refresh to complete.
- Fast Refresh Errors at New Materialized View Databases  
	In some cases, a materialized view log for a master table might be purged during the creation of a materialized view at a new materialized view database.
- Materialized Views Continually Refreshing  
	If you encounter a situation where Oracle Database continually refreshes a group of materialized views, then check the group's refresh interval.
- Materialized View Logs Growing Too Large  
	If a materialized view log at a master database is growing too large, then check to see whether a network or database failure has prevented the master database from becoming aware that a materialized view has been dropped.

**Parent topic:** Troubleshooting Problems with Read-Only Materialized Views

#### 39.3.1 Common Refresh Problems

Several common factors can prevent the automatic refresh of a group of materialized views.

These factors include the following:

- The lack of a job slave at the materialized view database
- An intervening network or server failure
- An intervening server shutdown

When a refresh group is experiencing problems, ensure that none of the preceding situations is preventing Oracle Database from completing group refreshes.

**Parent topic:** Refresh Problems

#### 39.3.2 Automatic Refresh Retries

When Oracle Database fails to refresh a refresh group automatically, the refresh group remains due for its refresh to complete.

Oracle Database will retry an automatic refresh of a group with the following behavior:

- Oracle Database retries the refresh group refresh first one minute later, then two minutes later, four minutes later, and so on, with the retry interval doubling with each failed attempt to refresh the group.
- Oracle Database does not allow the retry interval to exceed the refresh interval itself.
- Oracle Database retries the automatic refresh up to sixteen times.

If after 16 attempts to refresh a refresh group Oracle Database continues to encounter errors, then Oracle Database considers the group broken. You can query the `BROKEN` column of the `USER_REFRESH` and `USER_REFRESH_CHILDREN` data dictionary views to see the current status of a refresh group.

The errors causing Oracle Database to consider a refresh group broken are recorded in a trace file. After you correct the problems preventing a refresh group from refreshing successfully, you must refresh the refresh group manually. Oracle Database then resets the broken flag so that automatic refreshes can happen again.

See Also:

The name of the materialized view trace file is of the form jn, where n is operating system specific. See the Oracle documentation for your operating system for the name on your system.

**Parent topic:** Refresh Problems

#### 39.3.3 Fast Refresh Errors at New Materialized View Databases

In some cases, a materialized view log for a master table might be purged during the creation of a materialized view at a new materialized view database.

When this happens, you might encounter the following errors:

```
ORA-12004 REFRESH FAST cannot be used for materialized view materialized_view_name
ORA-12034 materialized view log on materialized_view_name younger than last refresh
```

See Also:

" [Adding a New Materialized View Database](creating-and-managing-read-only-materialized-views.md) " for a complete description of how to avoid this problem.

**Parent topic:** Refresh Problems

#### 39.3.4 Materialized Views Continually Refreshing

If you encounter a situation where Oracle Database continually refreshes a group of materialized views, then check the group's refresh interval.

Oracle Database evaluates a refresh group's automatic refresh interval before starting the refresh. If a refresh group's refresh interval is less than the amount of time it takes to refresh all materialized views in the group, then Oracle Database continually starts a refresh group refresh each time the job slave checks the queue of outstanding jobs.

**Parent topic:** Refresh Problems

#### 39.3.5 Materialized View Logs Growing Too Large

If a materialized view log at a master database is growing too large, then check to see whether a network or database failure has prevented the master database from becoming aware that a materialized view has been dropped.

You might need to purge part of the materialized view log or unregister the unused materialized view database.

**Parent topic:** Refresh Problems

### 39.4 Advanced Troubleshooting of Refresh Problems

There are several items you can check if you have problems with refreshing a materialized view.

If you have a problem refreshing a materialized view, then try the following:

- Check the `NEXT_DATE` value in the `DBA_REFRESH_CHILDREN` view to determine if the refresh has been scheduled.
- If the refresh interval has passed, then check the `DBA_REFRESH` view for the associated job number for the materialized view refresh and then diagnose the problem with job queues.
- Check if there are job slaves running. Check the `JOB_QUEUE_PROCESSES` initialization parameter, query the `DBA_JOBS_RUNNING` view, and use your operating system to check if the job slaves are still running.
- You also might encounter an error if you attempt to define a master detail relationship between two materialized views. You should define master detail relationships only on the master tables by using declarative referential integrity constraints. The related materialized views should then be placed in the same refresh group to preserve this relationship. However, you can define deferred (or deferrable) constraints on materialized views.
- Materialized views in the same refresh groups have their rows updated in a single transaction. Such a transaction can be very large, requiring either a large rollback segment at the materialized view database, with the rollback segment specified to be used during refresh, or more frequent refreshes to reduce the transaction size.
- If Oracle error `ORA-12004` occurs, then the master database might have run out of rollback segments when trying to maintain the materialized view log, or the materialized view log might be out of date. For example, the materialized view log might have been purged or re-created.
- Complete refreshes of a single materialized view internally use the `TRUNCATE` feature to increase speed and reduce rollback segment requirements. However, until the materialized view refresh is complete, users might temporarily see no data in the materialized view. Refreshes of multiple materialized views (for example, refresh groups) do not use the `TRUNCATE` feature.
- Reorganization of the master table (for example, to reclaim system resources) should `TRUNCATE` the master table to force rowid materialized views to do complete refreshes. Otherwise, the materialized views have incorrect references to master table rowids. You use the `BEGIN_TABLE_REORGANIZATION` and `END_TABLE_REORGANIZATION` procedures in the `DBMS_MVIEW` package to reorganize a master table.
- If while refreshing you see an `ORA-00942` (table or view does not exist), then check your database links and ensure that you still have the required privileges on the master table and the materialized view log.
- If a fast refresh was succeeding but then fails, then check whether:
	- The materialized view log was truncated, purged, or dropped.
		- You still have the required privileges on the materialized view log.
- If a force refresh takes an inordinately long time, then check if the materialized view log used by the refresh has been dropped.
- If the materialized view was created with `BUILD` `DEFERRED`, and its first fast refresh fails, then ensure that a previous complete refresh was done successfully before checking for other problems.

**Parent topic:** Troubleshooting Problems with Read-Only Materialized Views