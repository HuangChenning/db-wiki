---
title: Appendix A MySQL 5.6 Frequently Asked Questions
book: MySQL 5.6 Reference Manual
version: "5.6"
source: "MySQL/MySQL5.6/sources/refman-5.6-en.pdf#page=3531"
tags:
  - mysql
  - mysql-5.6
  - reference-manual
---

## Table of Contents

A.1 MySQL 5.6 FAQ: General ....................................................................................................... 3503 A.2 MySQL 5.6 FAQ: Storage Engines .......................................................................................... 3505 A.3 MySQL 5.6 FAQ: Server SQL Mode ........................................................................................ 3505 A.4 MySQL 5.6 FAQ: Stored Procedures and Functions ................................................................. 3506 A.5 MySQL 5.6 FAQ: Triggers ...................................................................................................... 3510 A.6 MySQL 5.6 FAQ: Views .......................................................................................................... 3512 A.7 MySQL 5.6 FAQ: INFORMATION_SCHEMA ........................................................................... 3513 A.8 MySQL 5.6 FAQ: Migration ..................................................................................................... 3514 A.9 MySQL 5.6 FAQ: Security ....................................................................................................... 3514 A.10 MySQL 5.6 FAQ: NDB Cluster .............................................................................................. 3515 A.11 MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean Character Sets .............................. 3529 A.12 MySQL 5.6 FAQ: Connectors & APIs .................................................................................... 3541 A.13 MySQL 5.6 FAQ: C API, libmysql .......................................................................................... 3542 A.14 MySQL 5.6 FAQ: Replication ................................................................................................ 3542 A.15 MySQL 5.6 FAQ: MySQL Enterprise Thread Pool .................................................................. 3546 A.16 MySQL 5.6 FAQ: InnoDB Change Buffer ............................................................................... 3548 A.17 MySQL 5.6 FAQ: Virtualization Support ................................................................................. 3550

## A.1 MySQL 5.6 FAQ: General

A.1.1 Which version of MySQL is production-ready (GA)? .............................................................. 3503 A.1.2 Can MySQL 5.6 do subqueries? .......................................................................................... 3504 A.1.3 Can MySQL 5.6 perform multiple-table inserts, updates, and deletes? .................................... 3504 A.1.4 Does MySQL 5.6 have a Query Cache? Does it work on Server, Instance or Database? .......... 3504 A.1.5 Does MySQL 5.6 have Sequences? ..................................................................................... 3504 A.1.6 Does MySQL 5.6 have a `NOW()` function with fractions of seconds? ....................................... 3504 A.1.7 Does MySQL 5.6 work with multi-core processors? ............................................................... 3504 A.1.8 Why do I see multiple processes for `mysqld`? ...................................................................... 3504 A.1.9 Can MySQL 5.6 perform ACID transactions? ........................................................................ 3505 A.1.1. Which version of MySQL is production-ready (GA)?

MySQL 8.0, 5.7, and MySQL 5.6 are supported for production use.

MySQL 8.0 achieved General Availability (GA) status with MySQL 8.0.11, which was released for production use on 19 April 2018.

MySQL 5.7 achieved General Availability (GA) status with MySQL 5.7.9, which was released for production use on 21 October 2015.

MySQL 5.6 achieved General Availability (GA) status with MySQL 5.6.10, which was released for production use on 5 February 2013.

MySQL 5.5 achieved General Availability (GA) status with MySQL 5.5.8, which was released for production use on 3 December 2010. Active development for MySQL 5.5 has ended.

MySQL 5.1 achieved General Availability (GA) status with MySQL 5.1.30, which was released for production use on 14 November 2008. Active development for MySQL 5.1 has ended.

MySQL 5.6 FAQ: General MySQL 5.0 achieved General Availability (GA) status with MySQL 5.0.15, which was released for production use on 19 October 2005. Active development for MySQL 5.0 has ended.

> A.1.2. Can MySQL 5.6 do subqueries?

Yes. See Section 13.2.10, “Subqueries”.

> A.1.3. Can MySQL 5.6 perform multiple-table inserts, updates, and deletes?

Yes. For the syntax required to perform multiple-table updates, see Section 13.2.11, “UPDATE Statement”; for that required to perform multiple-table deletes, see Section 13.2.2, “DELETE Statement”.

A multiple-table insert can be accomplished using a trigger whose `FOR EACH ROW` clause contains multiple `INSERT` statements within a `BEGIN ... END` block. See Section 20.3, “Using Triggers”.

> A.1.4. Does MySQL 5.6 have a Query Cache? Does it work on Server, Instance or Database?

Yes. The query cache operates on the server level, caching complete result sets matched with the original query string. If an exactly identical query is made (which often happens, particularly in web applications), no parsing or execution is necessary; the result is sent directly from the cache.

Various tuning options are available. See Section 8.10.3, “The MySQL Query Cache”.

> A.1.5. Does MySQL 5.6 have Sequences?

No. However, MySQL has an `AUTO_INCREMENT` system, which in MySQL 5.6 can also handle inserts in a multi-source replication setup. With the `auto_increment_increment` and`auto_increment_offset` system variables, you can set each server to generate auto-increment values that don't conflict with other servers. The `auto_increment_increment` value should be greater than the number of servers, and each server should have a unique offset.

> A.1.6. Does MySQL 5.6 have a `NOW()` function with fractions of seconds?

Yes, see Section 11.2.7, “Fractional Seconds in Time Values”.

> A.1.7. Does MySQL 5.6 work with multi-core processors?

Yes. MySQL is fully multithreaded, and makes use of all CPUs made available to it. Not all CPUs may be available; modern operating systems should be able to utilize all underlying CPUs, but also make it possible to restrict a process to a specific CPU or sets of CPUs.

On Windows, there is currently a limit to the number of (logical) processors that `mysqld` can use: a single processor group, which is limited to a maximum of 64 logical processors.

Use of multiple cores may be seen in these ways:

- A single core is usually used to service the commands issued from one session.
- A few background threads make limited use of extra cores; for example, to keep background I/O

tasks moving.

- If the database is I/O-bound (indicated by CPU consumption less than capacity), adding more

CPUs is futile. If the database is partitioned into an I/O-bound part and a CPU-bond part, adding CPUs may still be useful.

> A.1.8. Why do I see multiple processes for `mysqld`?

MySQL 5.6 FAQ: Storage Engines`mysqld` is a single-process program, not a multi-process program, and does not fork or launch other processes. However, `mysqld` is multithreaded and some process-reporting system utilities display separate entries for each thread of multithreaded processes, which may lead to the appearance of multiple `mysqld` processes when in fact there is only one.

> A.1.9. Can MySQL 5.6 perform ACID transactions?

Yes. All current MySQL versions support transactions. The `InnoDB` storage engine offers full ACID transactions with row-level locking, multi-versioning, nonlocking repeatable reads, and all four SQL standard isolation levels.

The `NDB` storage engine supports the `READ COMMITTED` transaction isolation level only.

## A.2 MySQL 5.6 FAQ: Storage Engines

A.2.1 Where can I obtain complete documentation for MySQL storage engines? .............................. 3505 A.2.2 Are there any new storage engines in MySQL 5.6? ............................................................... 3505 A.2.3 Have any storage engines been removed in MySQL 5.6? ...................................................... 3505 A.2.4 What are the unique benefits of the `ARCHIVE` storage engine? .............................................. 3505 A.2.1. Where can I obtain complete documentation for MySQL storage engines?

See Chapter 15, Alternative Storage Engines. That chapter contains information about all MySQL storage engines except for the `InnoDB` storage engine and the `NDB` storage engine (used for MySQL Cluster). `InnoDB` is covered in Chapter 14, The InnoDB Storage Engine. `NDB` is covered in Chapter 18, MySQL NDB Cluster 7.3 and NDB Cluster 7.4.

> A.2.2. Are there any new storage engines in MySQL 5.6?

The features from the optional `InnoDB Plugin` from MySQL 5.1 are folded into the built-in `InnoDB`storage engine, so you can take advantage of features such as the Barracuda file format, `InnoDB`table compression, and the new configuration options for performance. See Chapter 14, The InnoDB Storage Engine for details. `InnoDB` also becomes the default storage engine for new tables.

See Section 14.1, “Introduction to InnoDB” for details.

> A.2.3. Have any storage engines been removed in MySQL 5.6?

No.

> A.2.4. What are the unique benefits of the `ARCHIVE` storage engine?

The `ARCHIVE` storage engine stores large amounts of data without indexes; it has a small footprint,and performs selects using table scans. See Section 15.5, “The ARCHIVE Storage Engine”, for details.

## A.3 MySQL 5.6 FAQ: Server SQL Mode

A.3.1 What are server SQL modes? .............................................................................................. 3505 A.3.2 How many server SQL modes are there? ............................................................................. 3506 A.3.3 How do you determine the server SQL mode? ...................................................................... 3506 A.3.4 Is the mode dependent on the database or connection? ........................................................ 3506 A.3.5 Can the rules for strict mode be extended? .......................................................................... 3506 A.3.6 Does strict mode impact performance? ................................................................................. 3506 A.3.7 What is the default server SQL mode when MySQL 5.6 is installed? ...................................... 3506 A.3.1. What are server SQL modes?

MySQL 5.6 FAQ: Stored Procedures and Functions Server SQL modes define what SQL syntax MySQL should support and what kind of data validation checks it should perform. This makes it easier to use MySQL in different environments and to use MySQL together with other database servers. The MySQL Server apply these modes individually to different clients. For more information, see Section 5.1.10, “Server SQL Modes”.

> A.3.2. How many server SQL modes are there?

Each mode can be independently switched on and off. See Section 5.1.10, “Server SQL Modes”, for a complete list of available modes.

> A.3.3. How do you determine the server SQL mode?

You can set the default SQL mode (for `mysqld` startup) with the `--sql-mode` option. Using the statement `SET [GLOBAL|SESSION] sql_mode='modes'`, you can change the settings from within a connection, either locally to the connection, or to take effect globally. You can retrieve the current mode by issuing a `SELECT @@sql_mode` statement.

> A.3.4. Is the mode dependent on the database or connection?

A mode is not linked to a particular database. Modes can be set locally to the session (connection),or globally for the server. you can change these settings using `SET [GLOBAL|SESSION]`

```
sql_mode='modes'.
```

> A.3.5. Can the rules for strict mode be extended?

When we refer to strict mode, we mean a mode where at least one of the modes `TRADITIONAL`,`STRICT_TRANS_TABLES`, or `STRICT_ALL_TABLES` is enabled. Options can be combined, so you can add restrictions to a mode. See Section 5.1.10, “Server SQL Modes”, for more information.

> A.3.6. Does strict mode impact performance?

The intensive validation of input data that some settings requires more time than if the validation is not done. While the performance impact is not that great, if you do not require such validation(perhaps your application already handles all of this), then MySQL gives you the option of leaving strict mode disabled. However, if you do require it, strict mode can provide such validation.

> A.3.7. What is the default server SQL mode when MySQL 5.6 is installed?

The default SQL mode is `NO_ENGINE_SUBSTITUTION`. For information about all available modes and default MySQL behavior, see Section 5.1.10, “Server SQL Modes”.

## A.4 MySQL 5.6 FAQ: Stored Procedures and Functions

A.4.1 Does MySQL 5.6 support stored procedures and functions? .................................................. 3507 A.4.2 Where can I find documentation for MySQL stored procedures and stored functions? .............. 3507 A.4.3 Is there a discussion forum for MySQL stored procedures? .................................................... 3507 A.4.4 Where can I find the ANSI SQL 2003 specification for stored procedures? .............................. 3507 A.4.5 How do you manage stored routines? .................................................................................. 3507 A.4.6 Is there a way to view all stored procedures and stored functions in a given database? ............ 3507 A.4.7 Where are stored procedures stored? ................................................................................... 3508 A.4.8 Is it possible to group stored procedures or stored functions into packages? ........................... 3508 A.4.9 Can a stored procedure call another stored procedure? ......................................................... 3508 A.4.10 Can a stored procedure call a trigger? ................................................................................ 3508 A.4.11 Can a stored procedure access tables? .............................................................................. 3508 A.4.12 Do stored procedures have a statement for raising application errors? .................................. 3508 A.4.13 Do stored procedures provide exception handling? .............................................................. 3508 A.4.14 Can MySQL 5.6 stored routines return result sets? .............................................................. 3508 A.4.15 Is `WITH RECOMPILE` supported for stored procedures? ...................................................... 3508 MySQL 5.6 FAQ: Stored Procedures and Functions A.4.16 Is there a MySQL equivalent to using `mod_plsql` as a gateway on Apache to talk directly to a stored procedure in the database? ................................................................................... 3508 A.4.17 Can I pass an array as input to a stored procedure? ........................................................... 3508 A.4.18 Can I pass a cursor as an `IN` parameter to a stored procedure? .......................................... 3508 A.4.19 Can I return a cursor as an `OUT` parameter from a stored procedure? ................................... 3509 A.4.20 Can I print out a variable's value within a stored routine for debugging purposes? .................. 3509 A.4.21 Can I commit or roll back transactions inside a stored procedure? ........................................ 3509 A.4.22 Do MySQL 5.6 stored procedures and functions work with replication? ................................. 3509 A.4.23 Are stored procedures and functions created on a replication source server replicated to a replica? .............................................................................................................................. 3509 A.4.24 How are actions that take place inside stored procedures and functions replicated? ............... 3509 A.4.25 Are there special security requirements for using stored procedures and functions together with replication? .................................................................................................................. 3509 A.4.26 What limitations exist for replicating stored procedure and function actions? .......................... 3509 A.4.27 Do the preceding limitations affect the ability of MySQL to do point-in-time recovery? ............. 3510 A.4.28 What is being done to correct the aforementioned limitations? .............................................. 3510 A.4.1. Does MySQL 5.6 support stored procedures and functions?

Yes. MySQL 5.6 supports two types of stored routines, stored procedures and stored functions.

> A.4.2. Where can I find documentation for MySQL stored procedures and stored functions?

See Section 20.2, “Using Stored Routines”.

> A.4.3. Is there a discussion forum for MySQL stored procedures?

Yes. See https://forums.mysql.com/list.php?98.

> A.4.4. Where can I find the ANSI SQL 2003 specification for stored procedures?

Unfortunately, the official specifications are not freely available (ANSI makes them available for purchase). However, there are books, such as SQL-99 Complete, Really by Peter Gulutzan and Trudy Pelzer, that provide a comprehensive overview of the standard, including coverage of stored procedures.

> A.4.5. How do you manage stored routines?

It is always good practice to use a clear naming scheme for your stored routines. You can manage stored procedures with `CREATE [FUNCTION|PROCEDURE]`, `ALTER [FUNCTION|`

```
PROCEDURE], DROP [FUNCTION|PROCEDURE], and SHOW CREATE [FUNCTION|PROCEDURE].
```

You can obtain information about existing stored procedures using the `ROUTINES` table in the `INFORMATION_SCHEMA` database (see Section 21.3.19, “The INFORMATION_SCHEMA ROUTINES Table”).

> A.4.6. Is there a way to view all stored procedures and stored functions in a given database?

Yes. For a database named `dbname`, use this query on the `INFORMATION_SCHEMA.ROUTINES`table:

```
SELECT ROUTINE_TYPE, ROUTINE_NAME
FROM INFORMATION_SCHEMA.ROUTINES
WHERE ROUTINE_SCHEMA='dbname';
```

For more information, see Section 21.3.19, “The INFORMATION_SCHEMA ROUTINES Table”.

The body of a stored routine can be viewed using `SHOW CREATE FUNCTION` (for a stored function)or `SHOW CREATE PROCEDURE` (for a stored procedure). See Section 13.7.5.11, “SHOW CREATE PROCEDURE Statement”, for more information.

MySQL 5.6 FAQ: Stored Procedures and Functions A.4.7. Where are stored procedures stored?

In the `proc` table of the `mysql` system database. However, you should not access the tables in the system database directly. Instead, query the `INFORMATION_SCHEMA` `ROUTINES` and`PARAMETERS` tables. See Section 21.3.19, “The INFORMATION_SCHEMA ROUTINES Table”, and Section 21.3.13, “The INFORMATION_SCHEMA PARAMETERS Table”.

You can also use `SHOW CREATE FUNCTION` to obtain information about stored functions, and`SHOW CREATE PROCEDURE` to obtain information about stored procedures. See Section 13.7.5.11,“SHOW CREATE PROCEDURE Statement”.

> A.4.8. Is it possible to group stored procedures or stored functions into packages?

No. This is not supported in MySQL 5.6.

> A.4.9. Can a stored procedure call another stored procedure?

Yes.

> A.4.10.Can a stored procedure call a trigger?

A stored procedure can execute an SQL statement, such as an `UPDATE`, that causes a trigger to activate.

> A.4.11.Can a stored procedure access tables?

Yes. A stored procedure can access one or more tables as required.

> A.4.12.Do stored procedures have a statement for raising application errors?

Yes. MySQL 5.6 implements the SQL standard `SIGNAL` and `RESIGNAL` statements. See Section 13.6.7, “Condition Handling”.

> A.4.13.Do stored procedures provide exception handling?

MySQL implements `HANDLER` definitions according to the SQL standard. See Section 13.6.7.2,“DECLARE ... HANDLER Statement”, for details.

> A.4.14.Can MySQL 5.6 stored routines return result sets?

Stored procedures can, but stored functions cannot. If you perform an ordinary `SELECT` inside a stored procedure, the result set is returned directly to the client. You need to use the MySQL 4.1 (or higher) client/server protocol for this to work. This means that, for example, in PHP, you need to use the `mysqli` extension rather than the old `mysql` extension.

> A.4.15.Is `WITH RECOMPILE` supported for stored procedures?

Not in MySQL 5.6.

A.4.16.Is there a MySQL equivalent to using `mod_plsql` as a gateway on Apache to talk directly to a stored procedure in the database?

There is no equivalent in MySQL 5.6.

> A.4.17.Can I pass an array as input to a stored procedure?

Not in MySQL 5.6.

> A.4.18.Can I pass a cursor as an `IN` parameter to a stored procedure?

In MySQL 5.6, cursors are available inside stored procedures only.

MySQL 5.6 FAQ: Stored Procedures and Functions A.4.19.Can I return a cursor as an `OUT` parameter from a stored procedure?

In MySQL 5.6, cursors are available inside stored procedures only. However, if you do not open a cursor on a `SELECT`, the result is sent directly to the client. You can also `SELECT INTO` variables.

See Section 13.2.9, “SELECT Statement”.

> A.4.20.Can I print out a variable's value within a stored routine for debugging purposes?

Yes, you can do this in a stored procedure, but not in a stored function. If you perform an ordinary`SELECT` inside a stored procedure, the result set is returned directly to the client. You must use the MySQL 4.1 (or above) client/server protocol for this to work. This means that, for example, in PHP,you need to use the `mysqli` extension rather than the old `mysql` extension.

> A.4.21.Can I commit or roll back transactions inside a stored procedure?

Yes. However, you cannot perform transactional operations within a stored function.

> A.4.22.Do MySQL 5.6 stored procedures and functions work with replication?

Yes, standard actions carried out in stored procedures and functions are replicated from a replication source server to a replica. There are a few limitations that are described in detail in Section 20.7, “Stored Program Binary Logging”.

> A.4.23.Are stored procedures and functions created on a replication source server replicated to a replica?

Yes, creation of stored procedures and functions carried out through normal DDL statements on a replication source server are replicated to a replica, so that the objects exist on both servers. `ALTER`and `DROP` statements for stored procedures and functions are also replicated.

> A.4.24.How are actions that take place inside stored procedures and functions replicated?

MySQL records each DML event that occurs in a stored procedure and replicates those individual actions to a replica. The actual calls made to execute stored procedures are not replicated.

Stored functions that change data are logged as function invocations, not as the DML events that occur inside each function.

A.4.25.Are there special security requirements for using stored procedures and functions together with replication?

Yes. Because a replica has authority to execute any statement read from a source's binary log,special security constraints exist for using stored functions with replication. If replication or binary logging in general (for the purpose of point-in-time recovery) is active, then MySQL DBAs have two security options open to them:

1. Any user wishing to create stored functions must be granted the `SUPER` privilege.
2. Alternatively, a DBA can set the `log_bin_trust_function_creators` system variable to 1,

which enables anyone with the standard `CREATE ROUTINE` privilege to create stored functions.

> A.4.26.What limitations exist for replicating stored procedure and function actions?

Nondeterministic (random) or time-based actions embedded in stored procedures may not replicate properly. By their very nature, randomly produced results are not predictable and cannot be exactly reproduced; therefore, random actions replicated to a replica do not mirror those performed on a source. Declaring stored functions to be `DETERMINISTIC` or setting the`log_bin_trust_function_creators` system variable to 0 keeps random operations producing random values from being invoked.

MySQL 5.6 FAQ: Triggers In addition, time-based actions cannot be reproduced on a replica because the timing of such actions in a stored procedure is not reproducible through the binary log used for replication. It records only DML events and does not factor in timing constraints.

Finally, nontransactional tables for which errors occur during large DML actions (such as bulk inserts) may experience replication issues in that a source may be partially updated from DML activity, but no updates are done to the replica because of the errors that occurred. A workaround is for a function's DML actions to be carried out with the `IGNORE` keyword so that updates on the source that cause errors are ignored and updates that do not cause errors are replicated to the replica.

> A.4.27.Do the preceding limitations affect the ability of MySQL to do point-in-time recovery?

The same limitations that affect replication do affect point-in-time recovery.

> A.4.28.What is being done to correct the aforementioned limitations?

You can choose either statement-based replication or row-based replication. The original replication implementation is based on statement-based binary logging. Row-based binary logging resolves the limitations mentioned earlier.

Mixed replication is also available (by starting the server with `--binlog-format=mixed`). This hybrid form of replication “knows” whether statement-level replication can safely be used, or row-level replication is required.

For additional information, see Section 17.1.2, “Replication Formats”.

## A.5 MySQL 5.6 FAQ: Triggers

A.5.1 Where can I find the documentation for MySQL 5.6 triggers? ................................................. 3510 A.5.2 Is there a discussion forum for MySQL Triggers? .................................................................. 3510 A.5.3 Does MySQL 5.6 have statement-level or row-level triggers? ................................................. 3510 A.5.4 Are there any default triggers? ............................................................................................. 3510 A.5.5 How are triggers managed in MySQL? ................................................................................. 3511 A.5.6 Is there a way to view all triggers in a given database? ......................................................... 3511 A.5.7 Where are triggers stored? .................................................................................................. 3511 A.5.8 Can a trigger call a stored procedure? .................................................................................. 3511 A.5.9 Can triggers access tables? ................................................................................................. 3511 A.5.10 Can a table have multiple triggers with the same trigger event and action time? ..................... 3511 A.5.11 Is it possible for a trigger to update tables on a remote server? ............................................ 3511 A.5.12 Do triggers work with replication? ....................................................................................... 3511 A.5.13 How are actions carried out through triggers on a source replicated to a replica? ................... 3512 A.5.1. Where can I find the documentation for MySQL 5.6 triggers?

See Section 20.3, “Using Triggers”.

> A.5.2. Is there a discussion forum for MySQL Triggers?

Yes. It is available at https://forums.mysql.com/list.php?99.

> A.5.3. Does MySQL 5.6 have statement-level or row-level triggers?

In MySQL 5.6, all triggers are `FOR EACH ROW`; that is, the trigger is activated for each row that is inserted, updated, or deleted. MySQL 5.6 does not support triggers using `FOR EACH STATEMENT`.

> A.5.4. Are there any default triggers?

MySQL 5.6 FAQ: Triggers Not explicitly. MySQL does have specific special behavior for some `TIMESTAMP` columns, as well as for columns which are defined using `AUTO_INCREMENT`.

> A.5.5. How are triggers managed in MySQL?

In MySQL 5.6, triggers can be created using the `CREATE TRIGGER` statement, and dropped using`DROP TRIGGER`. See Section 13.1.19, “CREATE TRIGGER Statement”, and Section 13.1.30,“DROP TRIGGER Statement”, for more about these statements.

Information about triggers can be obtained by querying the `INFORMATION_SCHEMA.TRIGGERS`table. See Section 21.3.27, “The INFORMATION_SCHEMA TRIGGERS Table”.

> A.5.6. Is there a way to view all triggers in a given database?

Yes. You can obtain a listing of all triggers defined on database `dbname` using a query on the`INFORMATION_SCHEMA.TRIGGERS` table such as the one shown here:

```
SELECT TRIGGER_NAME, EVENT_MANIPULATION, EVENT_OBJECT_TABLE, ACTION_STATEMENT
FROM INFORMATION_SCHEMA.TRIGGERS
WHERE TRIGGER_SCHEMA='dbname';
```

For more information about this table, see Section 21.3.27, “The INFORMATION_SCHEMA TRIGGERS Table”.

You can also use the `SHOW TRIGGERS` statement, which is specific to MySQL. See Section 13.7.5.39, “SHOW TRIGGERS Statement”.

> A.5.7. Where are triggers stored?

Triggers are stored in `.TRG` files, with one such file one per table.

> A.5.8. Can a trigger call a stored procedure?

Yes.

> A.5.9. Can triggers access tables?

A trigger can access both old and new data in its own table. A trigger can also affect other tables,but it is not permitted to modify a table that is already being used (for reading or writing) by the statement that invoked the function or trigger.

> A.5.10.Can a table have multiple triggers with the same trigger event and action time?

In MySQL 5.6, there cannot be multiple triggers for a given table that have the same trigger event and action time. For example, you cannot have two `BEFORE UPDATE` triggers for a table. This limitation is lifted in MySQL 5.7.

> A.5.11.Is it possible for a trigger to update tables on a remote server?

Yes. A table on a remote server could be updated using the `FEDERATED` storage engine. (See Section 15.8, “The FEDERATED Storage Engine”).

> A.5.12.Do triggers work with replication?

Yes. However, the way in which they work depends whether you are using MySQL's “classic”statement-based or row-based replication format.

When using statement-based replication, triggers on the replica are executed by statements that are executed on the source (and replicated to the replica).

MySQL 5.6 FAQ: Views When using row-based replication, triggers are not executed on the replica due to statements that were run on the source and then replicated to the replica. Instead, when using row-based replication, the changes caused by executing the trigger on the source are applied on the replica.

For more information, see Section 17.4.1.33, “Replication and Triggers”.

> A.5.13.How are actions carried out through triggers on a source replicated to a replica?

Again, this depends on whether you are using statement-based or row-based replication.

Statement-based replication. First, the triggers that exist on a source must be re-created on the replica server. Once this is done, the replication flow works as any other standard DML statement that participates in replication. For example, consider a table `EMP` that has an `AFTER` insert trigger,which exists on a replication source server. The same `EMP` table and `AFTER` insert trigger exist on the replica server as well. The replication flow would be:

1. An `INSERT` statement is made to `EMP`.
2. The `AFTER` trigger on `EMP` activates.
3. The `INSERT` statement is written to the binary log.
4. The replica picks up the `INSERT` statement to `EMP` and executes it.
5. The `AFTER` trigger on `EMP` that exists on the replica activates.

Row-based replication. When you use row-based replication, the changes caused by executing the trigger on the source are applied on the replica. However, the triggers themselves are not actually executed on the replica under row-based replication. This is because, if both the source and the replica applied the changes from the source and, in addition, the trigger causing these changes were applied on the replica, the changes would in effect be applied twice on the replica, leading to different data on the source and the replica.

In most cases, the outcome is the same for both row-based and statement-based replication.

However, if you use different triggers on the source and replica, you cannot use row-based replication. (This is because the row-based format replicates the changes made by triggers executing on the source to the replicas, rather than the statements that caused the triggers to execute, and the corresponding triggers on the replica are not executed.) Instead, any statements causing such triggers to be executed must be replicated using statement-based replication.

For more information, see Section 17.4.1.33, “Replication and Triggers”.

## A.6 MySQL 5.6 FAQ: Views

A.6.1 Where can I find documentation covering MySQL Views? ...................................................... 3512 A.6.2 Is there a discussion forum for MySQL Views? ..................................................................... 3513 A.6.3 What happens to a view if an underlying table is dropped or renamed? .................................. 3513 A.6.4 Does MySQL 5.6 have table snapshots? .............................................................................. 3513 A.6.5 Does MySQL 5.6 have materialized views? .......................................................................... 3513 A.6.6 Can you insert into views that are based on joins? ................................................................ 3513 A.6.1. Where can I find documentation covering MySQL Views?

See Section 20.5, “Using Views”.

You may also find the MySQL User Forums to be helpful.

MySQL 5.6 FAQ: INFORMATION_SCHEMA A.6.2. Is there a discussion forum for MySQL Views?

See the MySQL User Forums.

> A.6.3. What happens to a view if an underlying table is dropped or renamed?

After a view has been created, it is possible to drop or alter a table or view to which the definition refers. To check a view definition for problems of this kind, use the `CHECK TABLE` statement. (See Section 13.7.2.2, “CHECK TABLE Statement”.)A.6.4. Does MySQL 5.6 have table snapshots?

No.

> A.6.5. Does MySQL 5.6 have materialized views?

No.

> A.6.6. Can you insert into views that are based on joins?

It is possible, provided that your `INSERT` statement has a column list that makes it clear there is only one table involved.

You cannot insert into multiple tables with a single insert on a view.

## A.7 MySQL 5.6 FAQ: INFORMATION_SCHEMA

A.7.1 Where can I find documentation for the MySQL `INFORMATION_SCHEMA` database? ................ 3513 A.7.2 Is there a discussion forum for `INFORMATION_SCHEMA`? ....................................................... 3513 A.7.3 Where can I find the ANSI SQL 2003 specification for `INFORMATION_SCHEMA`? ..................... 3513 A.7.4 What is the difference between the Oracle Data Dictionary and MySQL`INFORMATION_SCHEMA`? .................................................................................................... 3513 A.7.5 Can I add to or otherwise modify the tables found in the `INFORMATION_SCHEMA` database? .... 3513 A.7.1. Where can I find documentation for the MySQL `INFORMATION_SCHEMA` database?

See Chapter 21, INFORMATION_SCHEMA Tables.

You may also find the MySQL User Forums to be helpful.

> A.7.2. Is there a discussion forum for `INFORMATION_SCHEMA`?

See the MySQL User Forums.

> A.7.3. Where can I find the ANSI SQL 2003 specification for `INFORMATION_SCHEMA`?

Unfortunately, the official specifications are not freely available. (ANSI makes them available for purchase.) However, there are books available, such as SQL-99 Complete, Really by Peter Gulutzan and Trudy Pelzer, that provide a comprehensive overview of the standard, including

```
INFORMATION_SCHEMA.
```

> A.7.4. What is the difference between the Oracle Data Dictionary and MySQL `INFORMATION_SCHEMA`?

Both Oracle and MySQL provide metadata in tables. However, Oracle and MySQL use different table names and column names. The MySQL implementation is more similar to those found in DB2 and SQL Server, which also support `INFORMATION_SCHEMA` as defined in the SQL standard.

> A.7.5. Can I add to or otherwise modify the tables found in the `INFORMATION_SCHEMA` database?

MySQL 5.6 FAQ: Migration No. Since applications may rely on a certain standard structure, this should not be modified.

For this reason, we cannot support bugs or other issues which result from modifying`INFORMATION_SCHEMA` tables or data.

## A.8 MySQL 5.6 FAQ: Migration

A.8.1 Where can I find information on how to migrate from MySQL 5.5 to MySQL 5.6? ..................... 3514 A.8.2 How has storage engine (table type) support changed in MySQL 5.6 from previous versions? ... 3514 A.8.1. Where can I find information on how to migrate from MySQL 5.5 to MySQL 5.6?

For detailed upgrade information, see Section 2.11, “Upgrading MySQL”. Do not skip a major version when upgrading, but rather complete the process in steps, upgrading from one major version to the next in each step. This may seem more complicated, but ultimately saves time and trouble. If you encounter problems during the upgrade, their origin is easier to identify, either by you or, if you have a MySQL Enterprise subscription, by MySQL support.

> A.8.2. How has storage engine (table type) support changed in MySQL 5.6 from previous versions?

Storage engine support has changed as follows:

- Support for `ISAM` tables was removed in MySQL 5.0 and you should now use the `MyISAM` storage

engine in place of `ISAM`. To convert a table `tblname` from `ISAM` to `MyISAM`, simply issue a statement such as this one:

```
ALTER TABLE tblname ENGINE=MYISAM;
```

- Internal `RAID` for `MyISAM` tables was also removed in MySQL 5.0. This was formerly used to

allow large tables in file systems that did not support file sizes greater than 2GB. All modern file systems allow for larger tables; in addition, there are now other solutions such as `MERGE` tables and views.

- The `VARCHAR` column type now retains trailing spaces in all storage engines.
- `MEMORY` tables (formerly known as `HEAP` tables) can also contain `VARCHAR` columns.

## A.9 MySQL 5.6 FAQ: Security

A.9.1 Where can I find documentation that addresses security issues for MySQL? ........................... 3514 A.9.2 What is the default authentication plugin in MySQL 5.6? ........................................................ 3515 A.9.3 Does MySQL 5.6 have native support for SSL? .................................................................... 3515 A.9.4 Is SSL support built into MySQL binaries, or must I recompile the binary myself to enable it? .... 3515 A.9.5 Does MySQL 5.6 have built-in authentication against LDAP directories? ................................. 3515 A.9.6 Does MySQL 5.6 include support for Roles Based Access Control (RBAC)? ........................... 3515 A.9.1. Where can I find documentation that addresses security issues for MySQL?

The best place to start is Chapter 6, Security.

Other portions of the MySQL Documentation which you may find useful with regard to specific security concerns include the following:

- Section 6.1.1, “Security Guidelines”.
- Section 6.1.3, “Making MySQL Secure Against Attackers”.
- Section B.3.3.2, “How to Reset the Root Password”.

MySQL 5.6 FAQ: NDB Cluster

- Section 6.1.5, “How to Run MySQL as a Normal User”.
- Section 6.1.4, “Security-Related mysqld Options and Variables”.
- Section 6.1.6, “Security Considerations for LOAD DATA LOCAL”.
- Section 2.10, “Postinstallation Setup and Testing”.
- Section 6.3, “Using Encrypted Connections”.
- Loadable Function Security Precautions.

There is also the Secure Deployment Guide, which provides procedures for deploying a generic binary distribution of MySQL Enterprise Edition Server with features for managing the security of your MySQL installation.

> A.9.2. What is the default authentication plugin in MySQL 5.6?

The default authentication plugin in MySQL 5.6 is `mysql_native_password`. For information about this plugin, see Section 6.4.1.1, “Native Pluggable Authentication”. For general information about pluggable authentication and other available authentication plugins, see Section 6.2.11,“Pluggable Authentication”, and Section 6.4.1, “Authentication Plugins”.

> A.9.3. Does MySQL 5.6 have native support for SSL?

Most 5.6 binaries have support for SSL connections between the client and server. See Section 6.3,“Using Encrypted Connections”.

You can also tunnel a connection using SSH, if (for example) the client application does not support SSL connections. For an example, see Section 6.3.5, “Connecting to MySQL Remotely from Windows with SSH”.

> A.9.4. Is SSL support built into MySQL binaries, or must I recompile the binary myself to enable it?

Most 5.6 binaries have SSL enabled for client/server connections that are secured, authenticated, or both. See Section 6.3, “Using Encrypted Connections”.

> A.9.5. Does MySQL 5.6 have built-in authentication against LDAP directories?

The Enterprise edition includes a PAM Authentication Plugin that supports authentication against an LDAP directory.

> A.9.6. Does MySQL 5.6 include support for Roles Based Access Control (RBAC)?

Not at this time.

## A.10 MySQL 5.6 FAQ: NDB Cluster

In the following section, we answer questions that are frequently asked about NDB Cluster and the `NDB`storage engine.

A.10.1 Which versions of the MySQL software support NDB Cluster? Do I have to compile from source? .............................................................................................................................. 3516 A.10.2 What do “NDB” and “NDBCLUSTER” mean? ...................................................................... 3517 A.10.3 What is the difference between using NDB Cluster versus using MySQL Replication? ............ 3517 A.10.4 Do I need any special networking to run NDB Cluster? How do computers in a cluster communicate? .................................................................................................................... 3518 MySQL 5.6 FAQ: NDB Cluster A.10.5 How many computers do I need to run an NDB Cluster, and why? ....................................... 3518 A.10.6 What do the different computers do in an NDB Cluster? ...................................................... 3518 A.10.7 When I run the `SHOW` command in the NDB Cluster management client, I see a line of output that looks like this: .............................................................................................................. 3519 A.10.8 With which operating systems can I use NDB Cluster? ........................................................ 3519 A.10.9 What are the hardware requirements for running NDB Cluster? ............................................ 3519 A.10.10 How much RAM do I need to use NDB Cluster? Is it possible to use disk memory at all? ...... 3520 A.10.11 What file systems can I use with NDB Cluster? What about network file systems or network shares? .............................................................................................................................. 3521 A.10.12 Can I run NDB Cluster nodes inside virtual machines (such as those created by VMWare,VirtualBox, Parallels, or Xen)? ............................................................................................. 3521 A.10.13 I am trying to populate an NDB Cluster database. The loading process terminates prematurely and I get an error message like this one: .......................................................... 3521 A.10.14 NDB Cluster uses TCP/IP. Does this mean that I can run it over the Internet, with one or more nodes in remote locations? ......................................................................................... 3522 A.10.15 Do I have to learn a new programming or query language to use NDB Cluster? ................... 3522 A.10.16 What programming languages and APIs are supported by NDB Cluster? ............................ 3522 A.10.17 Does NDB Cluster include any management tools? ........................................................... 3523 A.10.18 How do I find out what an error or warning message means when using NDB Cluster? ......... 3523 A.10.19 Is NDB Cluster transaction-safe? What isolation levels are supported? ................................ 3523 A.10.20 What storage engines are supported by NDB Cluster? ....................................................... 3523 A.10.21 In the event of a catastrophic failure— for example, the whole city loses power and my UPS fails—would I lose all my data? ........................................................................................... 3523 A.10.22 Is it possible to use `FULLTEXT` indexes with NDB Cluster? ................................................ 3523 A.10.23 Can I run multiple nodes on a single computer? ................................................................ 3523 A.10.24 Can I add data nodes to an NDB Cluster without restarting it? ............................................ 3524 A.10.25 Are there any limitations that I should be aware of when using NDB Cluster? ...................... 3524 A.10.26 Does NDB Cluster support foreign keys? .......................................................................... 3525 A.10.27 How do I import an existing MySQL database into an NDB Cluster? ................................... 3525 A.10.28 How do NDB Cluster nodes communicate with one another? ............................................. 3525 A.10.29 What is an arbitrator? ...................................................................................................... 3525 A.10.30 What data types are supported by NDB Cluster? ............................................................... 3526 A.10.31 How do I start and stop NDB Cluster? .............................................................................. 3526 A.10.32 What happens to NDB Cluster data when the NDB Cluster is shut down? ........................... 3527 A.10.33 Is it a good idea to have more than one management node for an NDB Cluster? .................. 3527 A.10.34 Can I mix different kinds of hardware and operating systems in one NDB Cluster? ............... 3527 A.10.35 Can I run two data nodes on a single host? Two SQL nodes? ............................................ 3527 A.10.36 Can I use host names with NDB Cluster? ......................................................................... 3527 A.10.37 Does NDB Cluster support IPv6? ...................................................................................... 3527 A.10.38 How do I handle MySQL users in an NDB Cluster having multiple MySQL servers? ............. 3528 A.10.39 How do I continue to send queries in the event that one of the SQL nodes fails? .................. 3528 A.10.40 How do I back up and restore an NDB Cluster? ................................................................ 3528 A.10.41 What is an “angel process”? ............................................................................................. 3528 A.10.1.Which versions of the MySQL software support NDB Cluster? Do I have to compile from source?

NDB Cluster is not supported in standard MySQL Server 5.6 releases. Instead, MySQL NDB Cluster is provided as a separate product. Available NDB Cluster release series include the following:

- NDB Cluster 7.2. This series is no longer supported for new deployments or maintained.

Users of NDB Cluster 7.2 should upgrade to a newer release series as soon as possible. We recommend that new deployments use the latest NDB Cluster 8.0 release.

- NDB Cluster 7.3. This series is a previous General Availability (GA) version of NDB Cluster,

still available for production use, although we recommend that new deployments use the latest MySQL 5.6 FAQ: NDB Cluster NDB Cluster 8.0 release. The most recent NDB Cluster 7.3 release can be obtained from https://dev.mysql.com/downloads/cluster/.

- NDB Cluster 7.4. This series is a previous General Availability (GA) version of NDB Cluster,

still available for production use, although we recommend that new deployments use the latest NDB Cluster 8.0 release. The most recent NDB Cluster 7.4 release can be obtained from https://dev.mysql.com/downloads/cluster/.

- NDB Cluster 7.5. This series is a previous General Availability (GA) version of NDB Cluster,

still available for production use, although we recommend that new deployments use the latest NDB Cluster 7.6 release. The latest NDB Cluster 7.5 releases can be obtained from https://dev.mysql.com/downloads/cluster/.

- NDB Cluster 7.6. This series is a previous General Availability (GA) version of NDB Cluster,

still available for production use, although we recommend that new deployments use the latest NDB Cluster 8.0 release. The latest NDB Cluster 7.6 releases can be obtained from https://dev.mysql.com/downloads/cluster/.

- NDB Cluster 8.0. This series is the most recent General Availability (GA) version of NDB

Cluster, based on version 8.0 of the `NDB` storage engine and MySQL Server 8.0. NDB Cluster 8.0 is available for production use; new deployments intended for production should use the latest GA release in this series, which is currently NDB Cluster 8.0.33. You can obtain the most recent NDB Cluster 8.0 release from https://dev.mysql.com/downloads/cluster/. For information about new features and other important changes in this series, see What is New in MySQL NDB Cluster.

You can obtain and compile NDB Cluster from source (see Section 18.3.1.4, “Building NDB Cluster from Source on Linux”, and Section 18.3.2.2, “Compiling and Installing NDB Cluster from Source on Windows”), but for all but the most specialized cases, we recommend using one of the following installers provided by Oracle that is appropriate to your operating platform and circumstances:

- Linux binary release (`tar.gz` file)
- Linux RPM package
- Linux `.deb` file
- Windows binary “no-install” release
- Windows MSI Installer

Installation packages may also be available from your platform's package management system.

You can determine whether your MySQL Server has `NDB` support using one of the statements `SHOW`

```
VARIABLES LIKE 'have_%', SHOW ENGINES, or SHOW PLUGINS.
```

> A.10.2.What do “NDB” and “NDBCLUSTER” mean?

“NDB” stands for “Network Database”. `NDB` and `NDBCLUSTER` are both names for the storage engine that enables clustering support with MySQL. `NDB` is preferred, but either name is correct.

> A.10.3.What is the difference between using NDB Cluster versus using MySQL Replication?

In traditional MySQL replication, a source MySQL server updates one or more replicas.

Transactions are committed sequentially, and a slow transaction can cause the replica to lag behind the source. This means that if the source fails, it is possible that the replica might not have recorded the last few transactions. If a transaction-safe engine such as `InnoDB` is being used, a transaction is either completed on the replica or not applied at all, but replication does not guarantee that all MySQL 5.6 FAQ: NDB Cluster data on the source and the replica remains consistent at all times. In NDB Cluster, all data nodes are kept in synchrony, and a transaction committed by any one data node is committed for all data nodes. In the event of a data node failure, all remaining data nodes remain in a consistent state.

In short, whereas standard MySQL replication is asynchronous, NDB Cluster is synchronous.

Asynchronous replication is also available in NDB Cluster. NDB Cluster Replication (also sometimes known as “geo-replication”) includes the capability to replicate both between two NDB Clusters, and from an NDB Cluster to a non-Cluster MySQL server. See Section 18.7, “NDB Cluster Replication”.

A.10.4.Do I need any special networking to run NDB Cluster? How do computers in a cluster communicate?

NDB Cluster is intended to be used in a high-bandwidth environment, with computers connecting using TCP/IP. Its performance depends directly upon the connection speed between the cluster's computers. The minimum connectivity requirements for NDB Cluster include a typical 100-megabit Ethernet network or the equivalent. We recommend you use gigabit Ethernet whenever available.

> A.10.5.How many computers do I need to run an NDB Cluster, and why?

A minimum of three computers is required to run a viable cluster. However, the minimum recommended number of computers in an NDB Cluster is four: one each to run the management and SQL nodes, and two computers to serve as data nodes. The purpose of the two data nodes is to provide redundancy; the management node must run on a separate machine to guarantee continued arbitration services in the event that one of the data nodes fails.

To provide increased throughput and high availability, you should use multiple SQL nodes (MySQL Servers connected to the cluster). It is also possible (although not strictly necessary) to run multiple management servers.

> A.10.6.What do the different computers do in an NDB Cluster?

An NDB Cluster has both a physical and logical organization, with computers being the physical elements. The logical or functional elements of a cluster are referred to as nodes, and a computer housing a cluster node is sometimes referred to as a cluster host. There are three types of nodes,each corresponding to a specific role within the cluster. These are:

- Management node. This node provides management services for the cluster as a whole,

including startup, shutdown, backups, and configuration data for the other nodes. The management node server is implemented as the application `ndb_mgmd`; the management client used to control NDB Cluster is `ndb_mgm`. See Section 18.5.4, “ndb_mgmd — The NDB Cluster Management Server Daemon”, and Section 18.5.5, “ndb_mgm — The NDB Cluster Management Client”, for information about these programs.

- Data node. This type of node stores and replicates data. Data node functionality is handled by

instances of the `NDB` data node process `ndbd`. For more information, see Section 18.5.1, “ndbd —The NDB Cluster Data Node Daemon”.

- SQL node. This is simply an instance of MySQL Server (`mysqld`) that is built with support

for the `NDBCLUSTER` storage engine and started with the `--ndb-cluster` option to enable the engine and the `--ndb-connectstring` option to enable it to connect to an NDB Cluster management server. For more about these options, see MySQL Server Options for NDB Cluster.

Note An API node is any application that makes direct use of Cluster data nodes for data storage and retrieval. An SQL node can thus be considered a MySQL 5.6 FAQ: NDB Cluster type of API node that uses a MySQL Server to provide an SQL interface to the Cluster. You can write such applications (that do not depend on a MySQL Server) using the NDB API, which supplies a direct, object-oriented transaction and scanning interface to NDB Cluster data; see NDB Cluster API Overview: The NDB API, for more information.

A.10.7.When I run the `SHOW` command in the NDB Cluster management client, I see a line of output that looks like this:

```
id=2    @10.100.10.32  (Version: 8.0.33-ndb-8.0.33 Nodegroup: 0, *)
```

What does the * mean? How is this node different from the others?

The simplest answer is, “It's not something you can control, and it's nothing that you need to worry about in any case, unless you're a software engineer writing or analyzing the NDB Cluster source code”.

If you don't find that answer satisfactory, here's a longer and more technical version:A number of mechanisms in NDB Cluster require distributed coordination among the data nodes.

These distributed algorithms and protocols include global checkpointing, DDL (schema) changes,and node restart handling. To make this coordination simpler, the data nodes “elect” one of their number to act as leader. There is no user-facing mechanism for influencing this selection, which is completely automatic; the fact that it is automatic is a key part of NDB Cluster's internal architecture.

When a node acts as the “leader” for any of these mechanisms, it is usually the point of coordination for the activity, and the other nodes act as “followers”, carrying out their parts of the activity as directed by the leader. If the node acting as leader fails, then the remaining nodes elect a new leader. Tasks in progress that were being coordinated by the old leader may either fail or be continued by the new leader, depending on the actual mechanism involved.

It is possible for some of these different mechanisms and protocols to have different leader nodes,but in general the same leader is chosen for all of them. The node indicated as the leader in the output of `SHOW` in the management client is known internally as the `DICT` manager, responsible for coordinating DDL and metadata activity.

NDB Cluster is designed in such a way that the choice of leader has no discernible effect outside the cluster itself. For example, the current leader does not have significantly higher CPU or resource usage than the other data nodes, and failure of the leader should not have a significantly different impact on the cluster than the failure of any other data node.

> A.10.8.With which operating systems can I use NDB Cluster?

NDB Cluster is supported on most Unix-like operating systems. NDB Cluster is also supported in production settings on Microsoft Windows operating systems.

For more detailed information concerning the level of support which is offered for NDB Cluster on various operating system versions, operating system distributions, and hardware platforms, please refer to https://www.mysql.com/support/supportedplatforms/cluster.html.

> A.10.9.What are the hardware requirements for running NDB Cluster?

NDB Cluster should run on any platform for which `NDB`-enabled binaries are available. For data nodes and API nodes, faster CPUs and more memory are likely to improve performance, and 64-bit CPUs are likely to be more effective than 32-bit processors. There must be sufficient memory on machines used for data nodes to hold each node's share of the database (see How much RAM do I Need? for more information). For a computer which is used only for running the NDB Cluster MySQL 5.6 FAQ: NDB Cluster management server, the requirements are minimal; a common desktop PC (or the equivalent) is generally sufficient for this task. Nodes can communicate through the standard TCP/IP network and hardware. They can also use the high-speed SCI protocol; however, special networking hardware and software are required to use SCI (see Section 18.4.4, “Using High-Speed Interconnects with NDB Cluster”).

> A.10.10.How much RAM do I need to use NDB Cluster? Is it possible to use disk memory at all?

NDB Cluster was originally implemented as in-memory only, but all versions currently available also provide the ability to store NDB Cluster on disk. See Section 18.6.11, “NDB Cluster Disk Data Tables”, for more information.

For in-memory `NDB` tables, you can use the following formula for obtaining a rough estimate of how much RAM is needed for each data node in the cluster:

```
(SizeofDatabase × NumberOfReplicas × 1.1 ) / NumberOfDataNodes
```

To calculate the memory requirements more exactly requires determining, for each table in the cluster database, the storage space required per row (see Section 11.6, “Data Type Storage Requirements”, for details), and multiplying this by the number of rows. You must also remember to account for any column indexes as follows:

- Each primary key or hash index created for an `NDBCLUSTER` table requires 21−25 bytes per

record. These indexes use `IndexMemory`.

- Each ordered index requires 10 bytes storage per record, using `DataMemory`.
- Creating a primary key or unique index also creates an ordered index, unless this index is created

with `USING HASH`. In other words:

- A primary key or unique index on a Cluster table normally takes up 31 to 35 bytes per record.
- However, if the primary key or unique index is created with `USING HASH`, then it requires only

21 to 25 bytes per record.

Creating NDB Cluster tables with `USING HASH` for all primary keys and unique indexes generally causes table updates to run more quickly—in some cases by a much as 20 to 30 percent faster than updates on tables where `USING HASH` was not used in creating primary and unique keys. This is due to the fact that less memory is required (because no ordered indexes are created), and that less CPU must be utilized (because fewer indexes must be read and possibly updated). However, it also means that queries that could otherwise use range scans must be satisfied by other means, which can result in slower selects.

When calculating Cluster memory requirements, you may find useful the `ndb_size.pl` utility which is available in recent MySQL 5.6 releases. This Perl script connects to a current (non-Cluster)MySQL database and creates a report on how much space that database would require if it used the `NDBCLUSTER` storage engine. For more information, see Section 18.5.26, “ndb_size.pl —NDBCLUSTER Size Requirement Estimator”.

It is especially important to keep in mind that every NDB Cluster table must have a primary key.

The `NDB` storage engine creates a primary key automatically if none is defined; this primary key is created without `USING HASH`.

You can determine how much memory is being used for storage of NDB Cluster data and indexes at any given time using the `REPORT MEMORYUSAGE` command in the `ndb_mgm` client; see Section 18.6.1, “Commands in the NDB Cluster Management Client”, for more information. In MySQL 5.6 FAQ: NDB Cluster addition, warnings are written to the cluster log when 80% of available `DataMemory` or (prior to NDB 7.6) `IndexMemory` is in use, and again when usage reaches 90%, 99%, and 100%.

> A.10.11.What file systems can I use with NDB Cluster? What about network file systems or network shares?

Generally, any file system that is native to the host operating system should work well with NDB Cluster. If you find that a given file system works particularly well (or not so especially well) with NDB Cluster, we invite you to discuss your findings in the NDB Cluster Forums.

For Windows, we recommend that you use `NTFS` file systems for NDB Cluster, just as we do for standard MySQL. We do not test NDB Cluster with `FAT` or `VFAT` file systems. Because of this, we do not recommend their use with MySQL or NDB Cluster.

NDB Cluster is implemented as a shared-nothing solution; the idea behind this is that the failure of a single piece of hardware should not cause the failure of multiple cluster nodes, or possibly even the failure of the cluster as a whole. For this reason, the use of network shares or network file systems is not supported for NDB Cluster. This also applies to shared storage devices such as SANs.

A.10.12.Can I run NDB Cluster nodes inside virtual machines (such as those created by VMWare,VirtualBox, Parallels, or Xen)?

NDB Cluster is supported for use in virtual machines. We currently support and test using Oracle VM.

Some NDB Cluster users have successfully deployed NDB Cluster using other virtualization products; in such cases, Oracle can provide NDB Cluster support, but issues specific to the virtual environment must be referred to that product's vendor.

A.10.13.I am trying to populate an NDB Cluster database. The loading process terminates prematurely and I get an error message like this one:

```
ERROR 1114: The table 'my_cluster_table' is full
```

Why is this happening?

The cause is very likely to be that your setup does not provide sufficient RAM for all table data and all indexes, including the primary key required by the `NDB` storage engine and automatically created in the event that the table definition does not include the definition of a primary key.

It is also worth noting that all data nodes should have the same amount of RAM, since no data node in a cluster can use more memory than the least amount available to any individual data node. For example, if there are four computers hosting Cluster data nodes, and three of these have 3GB of RAM available to store Cluster data while the remaining data node has only 1GB RAM, then each data node can devote at most 1GB to NDB Cluster data and indexes.

In some cases it is possible to get `Table is full` errors in MySQL client applications even when`ndb_mgm -e "ALL REPORT MEMORYUSAGE"` shows significant free `DataMemory`. You can force`NDB` to create extra partitions for NDB Cluster tables and thus have more memory available for hash indexes by using the `MAX_ROWS` option for `CREATE TABLE`. In general, setting `MAX_ROWS` to twice the number of rows that you expect to store in the table should be sufficient.

For similar reasons, you can also sometimes encounter problems with data node restarts on nodes that are heavily loaded with data. The `MinFreePct` parameter can help with this issue by reserving a portion (5% by default) of `DataMemory` and (prior to NDB 7.6) `IndexMemory` for use in restarts.

This reserved memory is not available for storing `NDB` tables or data.

MySQL 5.6 FAQ: NDB Cluster A.10.14.NDB Cluster uses TCP/IP. Does this mean that I can run it over the Internet, with one or more nodes in remote locations?

It is very unlikely that a cluster would perform reliably under such conditions, as NDB Cluster was designed and implemented with the assumption that it would be run under conditions guaranteeing dedicated high-speed connectivity such as that found in a LAN setting using 100 Mbps or gigabit Ethernet—preferably the latter. We neither test nor warrant its performance using anything slower than this.

Also, it is extremely important to keep in mind that communications between the nodes in an NDB Cluster are not secure; they are neither encrypted nor safeguarded by any other protective mechanism. The most secure configuration for a cluster is in a private network behind a firewall,with no direct access to any Cluster data or management nodes from outside. (For SQL nodes, you should take the same precautions as you would with any other instance of the MySQL server.) For more information, see Section 18.6.17, “NDB Cluster Security Issues”.

> A.10.15.Do I have to learn a new programming or query language to use NDB Cluster?

No. Although some specialized commands are used to manage and configure the cluster itself, only standard (My)SQL statements are required for the following operations:

- Creating, altering, and dropping tables
- Inserting, updating, and deleting table data
- Creating, changing, and dropping primary and unique indexes

Some specialized configuration parameters and files are required to set up an NDB Cluster—see Section 18.4.3, “NDB Cluster Configuration Files”, for information about these.

A few simple commands are used in the NDB Cluster management client (`ndb_mgm`) for tasks such as starting and stopping cluster nodes. See Section 18.6.1, “Commands in the NDB Cluster Management Client”.

> A.10.16.What programming languages and APIs are supported by NDB Cluster?

NDB Cluster supports the same programming APIs and languages as the standard MySQL Server,including ODBC, .Net, the MySQL C API, and numerous drivers for popular scripting languages such as PHP, Perl, and Python. NDB Cluster applications written using these APIs behave similarly to other MySQL applications; they transmit SQL statements to a MySQL Server (in the case of NDB Cluster, an SQL node), and receive responses containing rows of data. For more information about these APIs, see Chapter 23, Connectors and APIs.

NDB Cluster also supports application programming using the NDB API, which provides a low-level C++ interface to NDB Cluster data without needing to go through a MySQL Server. See The NDB API. In addition, many `NDBCLUSTER` management functions are exposed by the C-language MGM API; see The MGM API, for more information.

NDB Cluster also supports Java application programming using ClusterJ, which supports a domain object model of data using sessions and transactions. See Java and NDB Cluster, for more information.

In addition, NDB Cluster provides support for `memcached`, allowing developers to access data stored in NDB Cluster using the `memcached` interface; for more information, see ndbmemcache—Memcache API for NDB Cluster (NO LONGER SUPPORTED).

MySQL 5.6 FAQ: NDB Cluster NDB Cluster also includes adapters supporting NoSQL applications written against `Node.js`, with NDB Cluster as the data store. See MySQL NoSQL Connector for JavaScript, for more information.

> A.10.17.Does NDB Cluster include any management tools?

NDB Cluster includes a command line client for performing basic management functions. See Section 18.5.5, “ndb_mgm — The NDB Cluster Management Client”, and Section 18.6.1,“Commands in the NDB Cluster Management Client”.

NDB Cluster 7.6 and earlier are also supported by MySQL Cluster Manager, a separate product providing an advanced command line interface that can automate many NDB Cluster management tasks such as rolling restarts and configuration changes. Beginning with version 1.4.8, MySQL Cluster Manager also provides experimental support for NDB Cluster 8.0. For more information about MySQL Cluster Manager, see MySQL Cluster Manager 1.4.8 User Manual.

> A.10.18.How do I find out what an error or warning message means when using NDB Cluster?

There are two ways in which this can be done:

- From within the `mysql` client, use `SHOW ERRORS` or `SHOW WARNINGS` immediately upon being

notified of the error or warning condition.

- From a system shell prompt, use `perror --ndb error_code`.

> A.10.19.Is NDB Cluster transaction-safe? What isolation levels are supported?

Yes. For tables created with the `NDB` storage engine, transactions are supported. Currently, NDB Cluster supports only the `READ COMMITTED` transaction isolation level.

> A.10.20.What storage engines are supported by NDB Cluster?

NDB Cluster requires the `NDB` storage engine. That is, in order for a table to be shared between nodes in an NDB Cluster, the table must be created using `ENGINE=NDB` (or the equivalent option

```
ENGINE=NDBCLUSTER).
```

It is possible to create tables using other storage engines (such as `InnoDB` or `MyISAM`) on a MySQL server being used with NDB Cluster, but since these tables do not use `NDB`, they do not participate in clustering; each such table is strictly local to the individual MySQL server instance on which it is created.

An NDB Cluster cannot be created using the `InnoDB` storage engine. For information about the differences between the `NDB` and `InnoDB` storage engines, see Section 18.2.6, “MySQL Server Using InnoDB Compared with NDB Cluster”.

A.10.21.In the event of a catastrophic failure— for example, the whole city loses power and my UPS fails—would I lose all my data?

All committed transactions are logged. Therefore, although it is possible that some data could be lost in the event of a catastrophe, this should be quite limited. Data loss can be further reduced by minimizing the number of operations per transaction. (It is not a good idea to perform large numbers of operations per transaction in any case.)A.10.22.Is it possible to use `FULLTEXT` indexes with NDB Cluster?

`FULLTEXT` indexing is currently supported only by the `InnoDB` and `MyISAM` storage engines. See Section 12.10, “Full-Text Search Functions”, for more information.

> A.10.23.Can I run multiple nodes on a single computer?

MySQL 5.6 FAQ: NDB Cluster It is possible but not always advisable. One of the chief reasons to run a cluster is to provide redundancy. To obtain the full benefits of this redundancy, each node should reside on a separate machine. If you place multiple nodes on a single machine and that machine fails, you lose all of those nodes. For this reason, if you do run multiple data nodes on a single machine, it is extremely important that they be set up in such a way that the failure of this machine does not cause the loss of all the data nodes in a given node group.

Given that NDB Cluster can be run on commodity hardware loaded with a low-cost (or even no-cost)operating system, the expense of an extra machine or two is well worth it to safeguard mission-critical data. It also worth noting that the requirements for a cluster host running a management node are minimal. This task can be accomplished with a 300 MHz Pentium or equivalent CPU and sufficient RAM for the operating system, plus a small amount of overhead for the `ndb_mgmd` and`ndb_mgm` processes.

It is acceptable to run multiple cluster data nodes on a single host that has multiple CPUs, cores,or both. The NDB Cluster distribution also provides a multithreaded version of the data node binary intended for use on such systems. For more information, see Section 18.5.3, “ndbmtd — The NDB Cluster Data Node Daemon (Multi-Threaded)”.

It is also possible in some cases to run data nodes and SQL nodes concurrently on the same machine; how well such an arrangement performs is dependent on a number of factors such as number of cores and CPUs as well as the amount of disk and memory available to the data node and SQL node processes, and you must take these factors into account when planning such a configuration.

> A.10.24.Can I add data nodes to an NDB Cluster without restarting it?

It is possible to add new data nodes to a running NDB Cluster without taking the cluster offline. For more information, see Section 18.6.7, “Adding NDB Cluster Data Nodes Online”.

For other types of NDB Cluster nodes, a rolling restart is all that is required (see Section 18.6.5,“Performing a Rolling Restart of an NDB Cluster”).

> A.10.25.Are there any limitations that I should be aware of when using NDB Cluster?

Limitations on `NDB` tables in MySQL NDB Cluster include the following:

- Temporary tables are not supported; a `CREATE TEMPORARY TABLE` statement using

`ENGINE=NDB` or `ENGINE=NDBCLUSTER` fails with an error.

- The only types of user-defined partitioning supported for `NDBCLUSTER` tables are `KEY` and

`LINEAR KEY`. Trying to create an `NDB` table using any other partitioning type fails with an error.

- `FULLTEXT` indexes are not supported.
- Index prefixes are not supported. Only complete columns may be indexed.
- Spatial indexes are not supported (although spatial columns can be used). See Section 11.4,

“Spatial Data Types”.

- Support for partial transactions and partial rollbacks is comparable to that of other transactional

storage engines such as `InnoDB` that can roll back individual statements.

- The maximum number of attributes allowed per table is 512. Attribute names cannot be any

longer than 31 characters. For each table, the maximum combined length of the table and database names is 122 characters.

MySQL 5.6 FAQ: NDB Cluster

- Priot to NDB 8.0, the maximum size for a table row is 14 kilobytes, not counting `BLOB` values. In

NDB 8.0, this maximum is increased to 30000 bytes. See Section 18.2.7.5, “Limits Associated with Database Objects in NDB Cluster”, for more information.

There is no set limit for the number of rows per `NDB` table. Limits on table size depend on a number of factors, in particular on the amount of RAM available to each data node.

For a complete listing of limitations in NDB Cluster, see Section 18.2.7, “Known Limitations of NDB Cluster”. See also Section 18.2.7.11, “Previous NDB Cluster Issues Resolved in NDB Cluster 7.3”.

> A.10.26.Does NDB Cluster support foreign keys?

NDB Cluster provides support for foreign key constraints which is comparable to that found in the `InnoDB` storage engine; see Section 1.6.3.2, “FOREIGN KEY Constraints”, for more detailed information, as well as Section 13.1.17.5, “FOREIGN KEY Constraints”. Applications requiring foreign key support should use NDB Cluster 7.3, 7.4, 7.5, or later.

> A.10.27.How do I import an existing MySQL database into an NDB Cluster?

You can import databases into NDB Cluster much as you would with any other version of MySQL.

Other than the limitations mentioned elsewhere in this FAQ, the only other special requirement is that any tables to be included in the cluster must use the `NDB` storage engine. This means that the tables must be created with `ENGINE=NDB` or `ENGINE=NDBCLUSTER`.

It is also possible to convert existing tables that use other storage engines to `NDBCLUSTER` using one or more `ALTER TABLE` statement. However, the definition of the table must be compatible with the `NDBCLUSTER` storage engine prior to making the conversion. In MySQL 5.6, an additional workaround is also required; see Section 18.2.7, “Known Limitations of NDB Cluster”, for details.

> A.10.28.How do NDB Cluster nodes communicate with one another?

Cluster nodes can communicate through any of three different transport mechanisms: TCP/IP, SHM(shared memory), and SCI (Scalable Coherent Interface). Where available, SHM is used by default between nodes residing on the same cluster host; however, this is considered experimental. SCI is a high-speed (1 gigabit per second and higher), high-availability protocol used in building scalable multi-processor systems; it requires special hardware and drivers. See Section 18.4.4, “Using High-Speed Interconnects with NDB Cluster”, for more about using SCI as a transport mechanism for NDB Cluster.

> A.10.29.What is an arbitrator?

If one or more data nodes in a cluster fail, it is possible that not all cluster data nodes are able to“see” one another. In fact, it is possible that two sets of data nodes might become isolated from one another in a network partitioning, also known as a “split-brain” scenario. This type of situation is undesirable because each set of data nodes tries to behave as though it is the entire cluster. An arbitrator is required to decide between the competing sets of data nodes.

When all data nodes in at least one node group are alive, network partitioning is not an issue,because no single subset of the cluster can form a functional cluster on its own. The real problem arises when no single node group has all its nodes alive, in which case network partitioning (the“split-brain” scenario) becomes possible. Then an arbitrator is required. All cluster nodes recognize the same node as the arbitrator, which is normally the management server; however, it is possible to configure any of the MySQL Servers in the cluster to act as the arbitrator instead. The arbitrator accepts the first set of cluster nodes to contact it, and tells the remaining set to shut down. Arbitrator selection is controlled by the `ArbitrationRank` configuration parameter for MySQL Server and management server nodes. You can also use the `ArbitrationRank` configuration parameter MySQL 5.6 FAQ: NDB Cluster to control the arbitrator selection process. For more information about these parameters, see Section 18.4.3.5, “Defining an NDB Cluster Management Server”.

The role of arbitrator does not in and of itself impose any heavy demands upon the host so designated, and thus the arbitrator host does not need to be particularly fast or to have extra memory especially for this purpose.

> A.10.30.What data types are supported by NDB Cluster?

NDB Cluster supports all of the usual MySQL data types, including those associated with MySQL's spatial extensions; however, the `NDB` storage engine does not support spatial indexes.

(Spatial indexes are supported only by `MyISAM`; see Section 11.4, “Spatial Data Types”, for more information.) In addition, there are some differences with regard to indexes when used with `NDB`tables.

Note NDB Cluster Disk Data tables (that is, tables created with `TABLESPACE ...`

```
STORAGE DISK ENGINE=NDB or TABLESPACE ... STORAGE DISK
```

`ENGINE=NDBCLUSTER`) have only fixed-width rows. This means that (for example) each Disk Data table record containing a `VARCHAR(255)` column requires space for 255 characters (as required for the character set and collation being used for the table), regardless of the actual number of characters stored therein.

See Section 18.2.7, “Known Limitations of NDB Cluster”, for more information about these issues.

> A.10.31.How do I start and stop NDB Cluster?

It is necessary to start each node in the cluster separately, in the following order:

1. Start the management node, using the `ndb_mgmd` command.

You must include the `-f` or `--config-file` option to tell the management node where its configuration file can be found.

2. Start each data node with the `ndbd` command.

Each data node must be started with the `-c` or `--ndb-connectstring` option so that the data node knows how to connect to the management server.

3. Start each MySQL Server (SQL node) using your preferred startup script, such as

```
mysqld_safe.
```

Each MySQL Server must be started with the `--ndbcluster` and `--ndb-connectstring`options. These options cause `mysqld` to enable `NDBCLUSTER` storage engine support and how to connect to the management server.

Each of these commands must be run from a system shell on the machine housing the affected node. (You do not have to be physically present at the machine—a remote login shell can be used for this purpose.) You can verify that the cluster is running by starting the `NDB` management client`ndb_mgm` on the machine housing the management node and issuing the `SHOW` or `ALL STATUS`command.

To shut down a running cluster, issue the command `SHUTDOWN` in the management client.

Alternatively, you may enter the following command in a system shell:MySQL 5.6 FAQ: NDB Cluster

```
$> ndb_mgm -e "SHUTDOWN"
```

(The quotation marks in this example are optional, since there are no spaces in the command string following the `-e` option; in addition, the `SHUTDOWN` command, like other management client commands, is not case-sensitive.)Either of these commands causes the `ndb_mgm`, `ndb_mgm`, and any `ndbd` processes to terminate gracefully. MySQL servers running as SQL nodes can be stopped using `mysqladmin shutdown`.

For more information, see Section 18.6.1, “Commands in the NDB Cluster Management Client”, and Section 18.3.6, “Safe Shutdown and Restart of NDB Cluster”.

MySQL Cluster Manager provides additional ways to handle starting ansd stopping of NDB Cluster nodes. See MySQL Cluster Manager 1.4.8 User Manual, for more information about this tool.

> A.10.32.What happens to NDB Cluster data when the NDB Cluster is shut down?

The data that was held in memory by the cluster's data nodes is written to disk, and is reloaded into memory the next time that the cluster is started.

> A.10.33.Is it a good idea to have more than one management node for an NDB Cluster?

It can be helpful as a fail-safe. Only one management node controls the cluster at any given time,but it is possible to configure one management node as primary, and one or more additional management nodes to take over in the event that the primary management node fails.

See Section 18.4.3, “NDB Cluster Configuration Files”, for information on how to configure NDB Cluster management nodes.

> A.10.34.Can I mix different kinds of hardware and operating systems in one NDB Cluster?

Yes, as long as all machines and operating systems have the same “endianness” (all big-endian or all little-endian).

It is also possible to use software from different NDB Cluster releases on different nodes. However,we support such use only as part of a rolling upgrade procedure (see Section 18.6.5, “Performing a Rolling Restart of an NDB Cluster”).

> A.10.35.Can I run two data nodes on a single host? Two SQL nodes?

Yes, it is possible to do this. In the case of multiple data nodes, it is advisable (but not required) for each node to use a different data directory. If you want to run multiple SQL nodes on one machine,each instance of `mysqld` must use a different TCP/IP port.

Running data nodes and SQL nodes together on the same host is possible, but you should be aware that the `ndbd` or `ndbmtd` processes may compete for memory with `mysqld`.

> A.10.36.Can I use host names with NDB Cluster?

Yes, it is possible to use DNS and DHCP for cluster hosts. However, if your application requires“five nines” availability, you should use fixed (numeric) IP addresses, since making communication between Cluster hosts dependent on services such as DNS and DHCP introduces additional potential points of failure.

> A.10.37.Does NDB Cluster support IPv6?

IPv6 is supported for connections between SQL nodes (MySQL servers), but connections between all other types of NDB Cluster nodes must use IPv4.

MySQL 5.6 FAQ: NDB Cluster In practical terms, this means that you can use IPv6 for replication between NDB Clusters, but connections between nodes in the same NDB Cluster must use IPv4. For more information, see Section 18.7.3, “Known Issues in NDB Cluster Replication”.

> A.10.38.How do I handle MySQL users in an NDB Cluster having multiple MySQL servers?

MySQL user accounts and privileges are normally not automatically propagated between different MySQL servers accessing the same NDB Cluster. MySQL NDB Cluster provides support for distributed privileges, which you can enable by following a procedure provided in the documentation;

see Section 18.6.13, “Distributed Privileges Using Shared Grant Tables”, for more information.

Important The mechanism for handling users distributed or shared between NDB Cluster SQL nodes has changed significantly in NDB 8.0; this implementation is not compatible with that in NDB 7.6 and earlier. See Privilege Synchronization and NDB_STORED_USER, for details.

> A.10.39.How do I continue to send queries in the event that one of the SQL nodes fails?

MySQL NDB Cluster does not provide any sort of automatic failover between SQL nodes. Your application must be prepared to handle the loss of SQL nodes and to fail over between them.

> A.10.40.How do I back up and restore an NDB Cluster?

You can use the NDB Cluster native backup and restore functionality in the NDB management client and the `ndb_restore` program. See Section 18.6.8, “Online Backup of NDB Cluster”, and Section 18.5.22, “ndb_restore — Restore an NDB Cluster Backup”.

You can also use the traditional functionality provided for this purpose in `mysqldump` and the MySQL server. See Section 4.5.4, “mysqldump — A Database Backup Program”, for more information.

> A.10.41.What is an “angel process”?

This process monitors and, if necessary, attempts to restart the data node process. If you check the list of active processes on your system after starting `ndbd`, you can see that there are actually 2 processes running by that name, as shown here (we omit the output from `ndb_mgmd` and `ndbd` for brevity):

```
$> ./ndb_mgmd
$> ps aux | grep ndb
me      23002  0.0  0.0 122948  3104 ?        Ssl  14:14   0:00 ./ndb_mgmd
me      23025  0.0  0.0   5284   820 pts/2    S+   14:14   0:00 grep ndb
$> ./ndbd -c 127.0.0.1 --initial
$> ps aux | grep ndb
me      23002  0.0  0.0 123080  3356 ?        Ssl  14:14   0:00 ./ndb_mgmd
me      23096  0.0  0.0  35876  2036 ?        Ss   14:14   0:00 ./ndbmtd -c 127.0.0.1 --initial
me      23097  1.0  2.4 524116 91096 ?        Sl   14:14   0:00 ./ndbmtd -c 127.0.0.1 --initial
me      23168  0.0  0.0   5284   812 pts/2    R+   14:15   0:00 grep ndb
```

The `ndbd` process showing `0.0` for both memory and CPU usage is the angel process (although it actually does use a very small amount of each). This process merely checks to see if the main `ndbd`or `ndbmtd` process (the primary data node process which actually handles the data) is running. If permitted to do so (for example, if the `StopOnError` configuration parameter is set to `false`), the angel process tries to restart the primary data node process.

MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean Character Sets

> A.11 MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean

## Character Sets

This set of Frequently Asked Questions derives from the experience of MySQL's Support and Development groups in handling many inquiries about CJK (Chinese-Japanese-Korean) issues.

A.11.1 What CJK character sets are available in MySQL? .............................................................. 3529 A.11.2 I have inserted CJK characters into my table. Why does `SELECT` display them as “?”characters? ......................................................................................................................... 3530 A.11.3 What problems should I be aware of when working with the Big5 Chinese character set? ....... 3532 A.11.4 Why do Japanese character set conversions fail? ............................................................... 3532 A.11.5 What should I do if I want to convert SJIS `81CA` to `cp932`? ................................................. 3534 A.11.6 How does MySQL represent the Yen (¥) sign? ................................................................... 3534 A.11.7 Of what issues should I be aware when working with Korean character sets in MySQL? ......... 3534 A.11.8 Why do I get `Incorrect string value` error messages? .............................................. 3534 A.11.9 Why does my GUI front end or browser display CJK characters incorrectly in my application using Access, PHP, or another API? ................................................................................... 3535 A.11.10 I've upgraded to MySQL 5.6. How can I revert to behavior like that in MySQL 4.0 with regard to character sets? ............................................................................................................... 3536 A.11.11 Why do some `LIKE` and `FULLTEXT` searches with CJK characters fail? .............................. 3537 A.11.12 How do I know whether character X is available in all character sets? ................................. 3537 A.11.13 Why do CJK strings sort incorrectly in Unicode? (I) ........................................................... 3538 A.11.14 Why do CJK strings sort incorrectly in Unicode? (II) ........................................................... 3540 A.11.15 Why are my supplementary characters rejected by MySQL? .............................................. 3541 A.11.16 Should “CJK” be “CJKV”? ................................................................................................ 3541 A.11.17 Does MySQL permit CJK characters to be used in database and table names? ................... 3541 A.11.18 Where can I find translations of the MySQL Manual into Chinese, Japanese, and Korean? ... 3541 A.11.19 Where can I get help with CJK and related issues in MySQL? ............................................ 3541 A.11.1.What CJK character sets are available in MySQL?

The list of CJK character sets may vary depending on your MySQL version. For example,the `gb18030` character set is not supported prior to MySQL 5.7.4. However, since the name of the applicable language appears in the `DESCRIPTION` column for every entry in the`INFORMATION_SCHEMA.CHARACTER_SETS` table, you can obtain a current list of all the non-Unicode CJK character sets using this query:

```
mysql> SELECT CHARACTER_SET_NAME, DESCRIPTION
FROM INFORMATION_SCHEMA.CHARACTER_SETS
WHERE DESCRIPTION LIKE '%Chin%'
OR DESCRIPTION LIKE '%Japanese%'
OR DESCRIPTION LIKE '%Korean%'
ORDER BY CHARACTER_SET_NAME;
+--------------------+---------------------------------+
| CHARACTER_SET_NAME | DESCRIPTION                     |
+--------------------+---------------------------------+
| big5               | Big5 Traditional Chinese        |
| cp932              | SJIS for Windows Japanese       |
| eucjpms            | UJIS for Windows Japanese       |
| euckr              | EUC-KR Korean                   |
| gb18030            | China National Standard GB18030 |
| gb2312             | GB2312 Simplified Chinese       |
| gbk                | GBK Simplified Chinese          |
| sjis               | Shift-JIS Japanese              |
| ujis               | EUC-JP Japanese                 |
+--------------------+---------------------------------+
```

MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean Character Sets(For more information, see Section 21.3.2, “The INFORMATION_SCHEMA CHARACTER_SETS Table”.)MySQL supports three variants of the GB (Guojia Biaozhun, or National Standard, or Simplified Chinese) character sets which are official in the People's Republic of China: `gb2312`, `gbk`, and (as of MySQL 5.7.4) `gb18030`.

Sometimes people try to insert `gbk` characters into `gb2312`, and it works most of the time because`gbk` is a superset of `gb2312`. But eventually they try to insert a rarer Chinese character and it does not work. (For an example, see Bug #16072).

Here, we try to clarify exactly what characters are legitimate in `gb2312` or `gbk`, with reference to the official documents. Please check these references before reporting `gb2312` or `gbk` bugs:

- The MySQL `gbk` character set is in reality “Microsoft code page 936”. This differs from the official

`gbk` for characters `A1A4` (middle dot), `A1AA` (em dash), `A6E0-A6F5`, and `A8BB-A8C0`.

- For a listing of `gbk`/Unicode mappings, see http://www.unicode.org/Public/MAPPINGS/

VENDORS/MICSFT/WINDOWS/CP936.TXT.

It is also possible to store CJK characters in Unicode character sets, although the available collations may not sort characters quite as you expect:

- The `utf8` and `ucs2` character sets support the characters from Unicode Basic Multilingual Plane

(BMP). These characters have code point values between `U+0000` and `U+FFFF`.

- The `utf8mb4`, `utf16`, `utf16le`, and `utf32` character sets support BMP characters, as well as

supplementary characters that lie outside the BMP. Supplementary characters have code point values between `U+10000` and `U+10FFFF`.

The collation used for a Unicode character set determines the ability to sort (that is, distinguish)characters in the set:

- Collations based on Unicode Collation Algorithm (UCA) 4.0.0 distinguish only BMP characters.
- Collations based on UCA 5.2.0 or 9.0.0 distinguish BMP and supplementary characters.
- Non-UCA collations may not distinguish all Unicode characters. For example, the `utf8mb4`

default collation is `utf8mb4_general_ci`, which distinguishes only BMP characters.

Moreover, distinguishing characters is not the same as ordering them per the conventions of a given CJK language. Currently, MySQL has only one CJK-specific UCA collation,`gb18030_unicode_520_ci` (which requires use of the non-Unicode `gb18030` character set).

For information about Unicode collations and their differentiating properties, including collation properties for supplementary characters, see Section 10.10.1, “Unicode Character Sets”.

> A.11.2.I have inserted CJK characters into my table. Why does `SELECT` display them as “?” characters?

This problem is usually due to a setting in MySQL that does not match the settings for the application program or the operating system. Here are some common steps for correcting these types of issues:

- Be certain of what MySQL version you are using.

Use the statement `SELECT VERSION();` to determine this.

MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean Character Sets

- Make sure that the database is actually using the desired character set.

People often think that the client character set is always the same as either the server character set or the character set used for display purposes. However, both of these are false assumptions.

You can make sure by checking the result of `SHOW CREATE TABLE tablename` or, better yet,by using this statement:

```
SELECT character_set_name, collation_name
FROM information_schema.columns
WHERE table_schema = your_database_name
AND table_name = your_table_name
AND column_name = your_column_name;
```

- Determine the hexadecimal value of the character or characters that are not being displayed

correctly.

You can obtain this information for a column `column_name` in the table `table_name` using the following query:

```
SELECT HEX(column_name)
FROM table_name;
```

`3F` is the encoding for the ? character; this means that ? is the character actually stored in the column. This most often happens because of a problem converting a particular character from your client character set to the target character set.

- Make sure that a round trip is possible. When you select `literal` (or `_introducer`

`hexadecimal-value`), do you obtain `literal` as a result?

For example, the Japanese Katakana character Pe (ペ') exists in all CJK character sets, and has the code point value (hexadecimal coding) `0x30da`. To test a round trip for this character, use this query:

```
SELECT 'ペ' AS `ペ`;         /* or SELECT _ucs2 0x30da; */
```

If the result is not also ペ, the round trip failed.

For bug reports regarding such failures, we might ask you to follow up with `SELECT``HEX('`ペ`');`. Then we can determine whether the client encoding is correct.

- Make sure that the problem is not with the browser or other application, rather than with MySQL.

Use the `mysql` client program to accomplish this task. If `mysql` displays characters correctly but your application does not, your problem is probably due to system settings.

To determine your settings, use the `SHOW VARIABLES` statement, whose output should resemble what is shown here:

```
mysql> SHOW VARIABLES LIKE 'char%';
+--------------------------+----------------------------------------+
| Variable_name            | Value                                  |
+--------------------------+----------------------------------------+
| character_set_client     | utf8                                   |
| character_set_connection | utf8                                   |
| character_set_database   | latin1                                 |
| character_set_filesystem | binary                                 |
| character_set_results    | utf8                                   |
| character_set_server     | latin1                                 |
| character_set_system     | utf8                                   |
```

MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean Character Sets

```
| character_sets_dir       | /usr/local/mysql/share/mysql/charsets/ |
+--------------------------+----------------------------------------+
```

These are typical character-set settings for an international-oriented client (notice the use of `utf8`Unicode) connected to a server in the West (`latin1` is a West Europe character set).

Although Unicode (usually the `utf8` variant on Unix, and the `ucs2` variant on Windows) is preferable to Latin, it is often not what your operating system utilities support best. Many Windows users find that a Microsoft character set, such as `cp932` for Japanese Windows, is suitable.

If you cannot control the server settings, and you have no idea what setting your underlying computer uses, try changing to a common character set for the country that you're in (`euckr` =Korea; `gb18030`, `gb2312` or `gbk` = People's Republic of China; `big5` = Taiwan; `sjis`, `ujis`,`cp932`, or `eucjpms` = Japan; `ucs2` or `utf8` = anywhere). Usually it is necessary to change only the client and connection and results settings. The `SET NAMES`. statement changes all three at once. For example:

```
SET NAMES 'big5';
```

Once the setting is correct, you can make it permanent by editing `my.cnf` or `my.ini`. For example you might add lines looking like these:

```
[mysqld]
character-set-server=big5
[client]
default-character-set=big5
```

It is also possible that there are issues with the API configuration setting being used in your application; see Why does my GUI front end or browser not display CJK characters correctly...?

for more information.

> A.11.3.What problems should I be aware of when working with the Big5 Chinese character set?

MySQL supports the Big5 character set which is common in Hong Kong and Taiwan (Republic of China). The MySQL `big5` character set is in reality Microsoft code page 950, which is very similar to the original `big5` character set.

A feature request for adding `HKSCS` extensions has been filed. People who need this extension may find the suggested patch for Bug #13577 to be of interest.

> A.11.4.Why do Japanese character set conversions fail?

MySQL supports the `sjis`, `ujis`, `cp932`, and `eucjpms` character sets, as well as Unicode. A common need is to convert between character sets. For example, there might be a Unix server(typically with `sjis` or `ujis`) and a Windows client (typically with `cp932`).

In the following conversion table, the `ucs2` column represents the source, and the `sjis`, `cp932`,`ujis`, and `eucjpms` columns represent the destinations; that is, the last 4 columns provide the hexadecimal result when we use `CONVERT(ucs2)` or we assign a `ucs2` column containing the value to an `sjis`, `cp932`, `ujis`, or `eucjpms` column.

Character ucs2 sjis cp932 ujis eucjpms Name BROKEN BAR 00A6 3F 3F 8FA2C3 3F FULLWIDTH FFE4 3F FA55 3F 8FA2 BROKEN BAR MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean Character Sets Character ucs2 sjis cp932 ujis eucjpms Name YEN SIGN 00A5 3F 3F 20 3F FULLWIDTH FFE5 818F 818F A1EF 3F YEN SIGN TILDE 007E 7E 7E 7E 7E OVERLINE 203E 3F 3F 20 3F HORIZONTAL 2015 815C 815C A1BD A1BD BAR EM DASH 2014 3F 3F 3F 3F REVERSE 005C 815F 5C 5C 5C SOLIDUS FULLWIDTH FF3C 3F 815F 3F A1C0 REVERSE SOLIDUS WAVE DASH 301C 8160 3F A1C1 3F FULLWIDTH FF5E 3F 8160 3F A1C1 TILDE DOUBLE 2016 8161 3F A1C2 3F VERTICAL LINE PARALLEL TO 2225 3F 8161 3F A1C2 MINUS SIGN 2212 817C 3F A1DD 3F FULLWIDTH FF0D 3F 817C 3F A1DD HYPHEN-MINUS CENT SIGN 00A2 8191 3F A1F1 3F FULLWIDTH FFE0 3F 8191 3F A1F1 CENT SIGN POUND SIGN 00A3 8192 3F A1F2 3F FULLWIDTH FFE1 3F 8192 3F A1F2 POUND SIGN NOT SIGN 00AC 81CA 3F A2CC 3F FULLWIDTH FFE2 3F 81CA 3F A2CC NOT SIGN Now consider the following portion of the table.

ucs2 sjis cp932 NOT SIGN 00AC 81CA 3F FULLWIDTH NOT FFE2 3F 81CA SIGN MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean Character Sets This means that MySQL converts the `NOT SIGN` (Unicode `U+00AC`) to `sjis` code point `0x81CA`and to `cp932` code point `3F`. (`3F` is the question mark (“?”. This is what is always used when the conversion cannot be performed.)A.11.5.What should I do if I want to convert SJIS `81CA` to `cp932`?

Our answer is: “?”. There are disadvantages to this, and many people would prefer a “loose”conversion, so that `81CA (NOT SIGN)` in `sjis` becomes `81CA (FULLWIDTH NOT SIGN)` in

```
cp932.
```

> A.11.6.How does MySQL represent the Yen (¥) sign?

A problem arises because some versions of Japanese character sets (both `sjis` and `euc`) treat `5C`as a reverse solidus (\, also known as a backslash), whereas others treat it as a yen sign (¥).

MySQL follows only one version of the JIS (Japanese Industrial Standards) standard description. In MySQL, `5C` is always the reverse solidus (\).

> A.11.7.Of what issues should I be aware when working with Korean character sets in MySQL?

In theory, while there have been several versions of the `euckr` (Extended Unix Code Korea)character set, only one problem has been noted. We use the “ASCII” variant of EUC-KR, in which the code point `0x5c` is REVERSE SOLIDUS, that is \, instead of the “KS-Roman” variant of EUC-KR, in which the code point `0x5c` is `WON SIGN` (₩). This means that you cannot convert Unicode U

```
+20A9 to euckr:
mysql> SELECT
CONVERT('₩' USING euckr) AS euckr,
HEX(CONVERT('₩' USING euckr)) AS hexeuckr;
+-------+----------+
| euckr | hexeuckr |
+-------+----------+
| ?     | 3F       |
+-------+----------+
```

> A.11.8.Why do I get `Incorrect string value` error messages?

To see the problem, create a table with one Unicode (`ucs2`) column and one Chinese (`gb2312`)column.

```
mysql> CREATE TABLE ch
(ucs2 CHAR(3) CHARACTER SET ucs2,
gb2312 CHAR(3) CHARACTER SET gb2312);
```

In nonstrict SQL mode, try to place the rare character 汌 in both columns.

```
mysql> SET sql_mode = '';
mysql> INSERT INTO ch VALUES ('A汌B','A汌B');
Query OK, 1 row affected, 1 warning (0.00 sec)
```

The `INSERT` produces a warning. Use the following statement to see what it is:

```
mysql> SHOW WARNINGS\G
*************************** 1. row ***************************
Level: Warning
Code: 1366
Message: Incorrect string value: '\xE6\xB1\x8CB' for column 'gb2312' at row 1
```

So it is a warning about the `gb2312` column only.

```
mysql> SELECT ucs2,HEX(ucs2),gb2312,HEX(gb2312) FROM ch;
```

MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean Character Sets

```
+-------+--------------+--------+-------------+
| ucs2  | HEX(ucs2)    | gb2312 | HEX(gb2312) |
+-------+--------------+--------+-------------+
| A汌B | 00416C4C0042 | A?B    | 413F42      |
+-------+--------------+--------+-------------+
```

Several things need explanation here:

1. The 汌 character is not in the `gb2312` character set, as described earlier.
2. If you are using an old version of MySQL, you may see a different message.
3. A warning occurs rather than an error because MySQL is not set to use strict SQL mode. In

nonstrict mode, MySQL tries to do what it can, to get the best fit, rather than give up. With strict SQL mode, the `Incorrect string value` message occurs as an error rather than a warning, and the `INSERT` fails.

A.11.9.Why does my GUI front end or browser display CJK characters incorrectly in my application using Access, PHP, or another API?

Obtain a direct connection to the server using the `mysql` client, and try the same query there. If`mysql` responds correctly, the trouble may be that your application interface requires initialization.

Use `mysql` to tell you what character set or sets it uses with the statement `SHOW VARIABLES``LIKE 'char%';`. If you are using Access, you are most likely connecting with Connector/ODBC.

In this case, you should check Configuring Connector/ODBC. If, for example, you use `big5`, you would enter `SET NAMES 'big5'`. (In this case, no ; character is required.) If you are using ASP,you might need to add `SET NAMES` in the code. Here is an example that has worked in the past:

```
<%
Session.CodePage=0
Dim strConnection
Dim Conn
strConnection="driver={MySQL ODBC 3.51 Driver};server=server;uid=username;" \
& "pwd=password;database=database;stmt=SET NAMES 'big5';"
Set Conn = Server.CreateObject("ADODB.Connection")
Conn.Open strConnection
%>
```

In much the same way, if you are using any character set other than `latin1` with Connector/NET,you must specify the character set in the connection string. See Connector/NET Connections, for more information.

If you are using PHP, try this:

```
<?php
$link = new mysqli($host, $usr, $pwd, $db);
if( mysqli_connect_errno() )
{
printf("Connect failed: %s\n", mysqli_connect_error());
exit();
}
$link->query("SET NAMES 'utf8'");
?>
```

In this case, we used `SET NAMES` to change `character_set_client`,

```
character_set_connection, and character_set_results.
```

Another issue often encountered in PHP applications has to do with assumptions made by the browser. Sometimes adding or changing a `<meta>` tag suffices to correct the problem: for MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean Character Sets example, to insure that the user agent interprets page content as `UTF-8`, include `<meta http-`

```
equiv="Content-Type" content="text/html; charset=utf-8"> in the <head> section
```

of the HTML page.

If you are using Connector/J, see Using Character Sets and Unicode.

A.11.10.I've upgraded to MySQL 5.6. How can I revert to behavior like that in MySQL 4.0 with regard to character sets?

In MySQL Version 4.0, there was a single “global” character set for both server and client, and the decision as to which character to use was made by the server administrator. This changed starting with MySQL Version 4.1. What happens now is a “handshake”, as described in Section 10.4,“Connection Character Sets and Collations”:When a client connects, it sends to the server the name of the character set that it wants to use. The server uses the name to set the `character_set_client`,

```
character_set_results, and character_set_connection system
```

variables. In effect, the server performs a `SET NAMES` operation using the character set name.

The effect of this is that you cannot control the client character set by starting `mysqld` with `--``character-set-server=utf8`. However, some Asian customers prefer the MySQL 4.0 behavior. To make it possible to retain this behavior, we added a `mysqld` switch, `--character-``set-client-handshake`, which can be turned off with `--skip-character-set-client-``handshake`. If you start `mysqld` with `--skip-character-set-client-handshake`, then,when a client connects, it sends to the server the name of the character set that it wants to use.

However, the server ignores this request from the client.

By way of example, suppose that your favorite server character set is `latin1`. Suppose further that the client uses `utf8` because this is what the client's operating system supports. Start the server with `latin1` as its default character set:

```
mysqld --character-set-server=latin1
```

And then start the client with the default character set `utf8`:

```
mysql --default-character-set=utf8
```

The resulting settings can be seen by viewing the output of `SHOW VARIABLES`:

```
mysql> SHOW VARIABLES LIKE 'char%';
+--------------------------+----------------------------------------+
| Variable_name            | Value                                  |
+--------------------------+----------------------------------------+
| character_set_client     | utf8                                   |
| character_set_connection | utf8                                   |
| character_set_database   | latin1                                 |
| character_set_filesystem | binary                                 |
| character_set_results    | utf8                                   |
| character_set_server     | latin1                                 |
| character_set_system     | utf8                                   |
| character_sets_dir       | /usr/local/mysql/share/mysql/charsets/ |
+--------------------------+----------------------------------------+
```

Now stop the client, and stop the server using `mysqladmin`. Then start the server again, but this time tell it to skip the handshake like so:

```
mysqld --character-set-server=utf8 --skip-character-set-client-handshake
```

MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean Character Sets Start the client with `utf8` once again as the default character set, then display the resulting settings:

```
mysql> SHOW VARIABLES LIKE 'char%';
+--------------------------+----------------------------------------+
| Variable_name            | Value                                  |
+--------------------------+----------------------------------------+
| character_set_client     | latin1                                 |
| character_set_connection | latin1                                 |
| character_set_database   | latin1                                 |
| character_set_filesystem | binary                                 |
| character_set_results    | latin1                                 |
| character_set_server     | latin1                                 |
| character_set_system     | utf8                                   |
| character_sets_dir       | /usr/local/mysql/share/mysql/charsets/ |
+--------------------------+----------------------------------------+
```

As you can see by comparing the differing results from `SHOW VARIABLES`, the server ignores the client's initial settings if the `--skip-character-set-client-handshake` option is used.

> A.11.11.Why do some `LIKE` and `FULLTEXT` searches with CJK characters fail?

For `LIKE` searches, there is a very simple problem with binary string column types such as `BINARY`and `BLOB`: we must know where characters end. With multibyte character sets, different characters might have different octet lengths. For example, in `utf8`, A requires one byte but ペ requires three bytes, as shown here:

```
+-------------------------+---------------------------+
| OCTET_LENGTH(_utf8 'A') | OCTET_LENGTH(_utf8 'ペ') |
+-------------------------+---------------------------+
|                       1 |                         3 |
+-------------------------+---------------------------+
```

If we do not know where the first character in a string ends, we do not know where the second character begins, in which case even very simple searches such as `LIKE '_A%'` fail. The solution is to use a nonbinary string column type defined to have the proper CJK character set. For example:`mycol TEXT CHARACTER SET sjis`. Alternatively, convert to a CJK character set before comparing.

This is one reason why MySQL cannot permit encodings of nonexistent characters. If it is not strict about rejecting bad input, it has no way of knowing where characters end.

For `FULLTEXT` searches, we must know where words begin and end. With Western languages, this is rarely a problem because most (if not all) of these use an easy-to-identify word boundary: the space character. However, this is not usually the case with Asian writing. We could use arbitrary halfway measures, like assuming that all Han characters represent words, or (for Japanese)depending on changes from Katakana to Hiragana due to grammatical endings. However, the only sure solution requires a comprehensive word list, which means that we would have to include a dictionary in the server for each Asian language supported. This is simply not feasible.

> A.11.12.How do I know whether character X is available in all character sets?

The majority of simplified Chinese and basic nonhalfwidth Japanese Kana characters appear in all CJK character sets. The following stored procedure accepts a `UCS-2` Unicode character, converts it to other character sets, and displays the results in hexadecimal.

```
DELIMITER //
CREATE PROCEDURE p_convert(ucs2_char CHAR(1) CHARACTER SET ucs2)
BEGIN
```

MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean Character Sets

```
CREATE TABLE tj
(ucs2 CHAR(1) character set ucs2,
utf8 CHAR(1) character set utf8,
big5 CHAR(1) character set big5,
cp932 CHAR(1) character set cp932,
eucjpms CHAR(1) character set eucjpms,
euckr CHAR(1) character set euckr,
gb2312 CHAR(1) character set gb2312,
gbk CHAR(1) character set gbk,
sjis CHAR(1) character set sjis,
ujis CHAR(1) character set ujis);
INSERT INTO tj (ucs2) VALUES (ucs2_char);
UPDATE tj SET utf8=ucs2,
big5=ucs2,
cp932=ucs2,
eucjpms=ucs2,
euckr=ucs2,
gb2312=ucs2,
gbk=ucs2,
sjis=ucs2,
ujis=ucs2;
/* If there are conversion problems, UPDATE produces warnings. */
SELECT hex(ucs2) AS ucs2,
hex(utf8) AS utf8,
hex(big5) AS big5,
hex(cp932) AS cp932,
hex(eucjpms) AS eucjpms,
hex(euckr) AS euckr,
hex(gb2312) AS gb2312,
hex(gbk) AS gbk,
hex(sjis) AS sjis,
hex(ujis) AS ujis
FROM tj;
DROP TABLE tj;
END//
DELIMITER ;
```

The input can be any single `ucs2` character, or it can be the code value (hexadecimal representation) of that character. For example, from Unicode's list of `ucs2` encodings and names(http://www.unicode.org/Public/UNIDATA/UnicodeData.txt), we know that the Katakana character Pe appears in all CJK character sets, and that its code value is `X'30DA'`. If we use this value as the argument to `p_convert()`, the result is as shown here:

```
mysql> CALL p_convert(X'30DA');
+------+--------+------+-------+---------+-------+--------+------+------+------+
| ucs2 | utf8   | big5 | cp932 | eucjpms | euckr | gb2312 | gbk  | sjis | ujis |
+------+--------+------+-------+---------+-------+--------+------+------+------+
| 30DA | E3839A | C772 | 8379  | A5DA    | ABDA  | A5DA   | A5DA | 8379 | A5DA |
+------+--------+------+-------+---------+-------+--------+------+------+------+
```

Since none of the column values is `3F` (that is, the question mark character, ?), we know that every conversion worked.

A.11.13.Why do CJK strings sort incorrectly in Unicode? (I)MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean Character Sets Note The CJK sorting problems described here can occur for MySQL versions prior to MySQL 8.0. As of MySQL 8.0, they can be solved by using the`utf8mb4` character set and the `utf8mb4_ja_0900_as_cs` collation.

Sometimes people observe that the result of a `utf8_unicode_ci` or `ucs2_unicode_ci` search,or of an `ORDER BY` sort is not what they think a native would expect. Although we never rule out the possibility that there is a bug, we have found in the past that many people do not correctly read the standard table of weights for the Unicode Collation Algorithm. MySQL uses the tables found under http://www.unicode.org/Public/UCA/:

- UCA 4.0.0 table: http://www.unicode.org/Public/UCA/4.0.0/allkeys-4.0.0.txt

This includes `xxx_unicode_ci` collations with no version number in the collation name.

- UCA 5.2.0 table: http://www.unicode.org/Public/UCA/5.2.0/allkeys.txt

This includes collations with `_520_` in the collation name.

- UCA 9.0.0 table: http://www.unicode.org/Public/UCA/9.0.0/allkeys.txt

This includes collations with `_0900_` in the collation name.

To handle newer UCA versions, we create new collations. We are very wary about changing ordering of existing collations because that affects indexes, which can bring about situations such as that reported in Bug #16526, illustrated as follows:

```
mysql> CREATE TABLE tj (s1 CHAR(1) CHARACTER SET utf8 COLLATE utf8_unicode_ci);
Query OK, 0 rows affected (0.05 sec)
mysql> INSERT INTO tj VALUES ('が'),('か');
Query OK, 2 rows affected (0.00 sec)
Records: 2  Duplicates: 0  Warnings: 0
mysql> SELECT * FROM tj WHERE s1 = 'か';
+------+
| s1   |
+------+
```

| が || か |

```
+------+
```

The character in the first result row is not the one that we searched for. Why did MySQL retrieve it? First we look for the Unicode code point value, which is possible by reading the hexadecimal number for the `ucs2` version of the characters:

```
mysql> SELECT s1, HEX(CONVERT(s1 USING ucs2)) FROM tj;
+------+-----------------------------+
| s1   | HEX(CONVERT(s1 USING ucs2)) |
+------+-----------------------------+
| が  | 304C                        |
| か  | 304B                        |
+------+-----------------------------+
```

Now we search for `304B` and `304C` in the `4.0.0 allkeys` table, and find these lines:

```
304B  ; [.1E57.0020.000E.304B] # HIRAGANA LETTER KA
304C  ; [.1E57.0020.000E.304B][.0000.0140.0002.3099] # HIRAGANA LETTER GA; QQCM
```

MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean Character Sets The official Unicode names (following the “#” mark) tell us the Japanese syllabary (Hiragana),the informal classification (letter, digit, or punctuation mark), and the Western identifier (`KA` or `GA`,which happen to be voiced and unvoiced components of the same letter pair). More importantly,the primary weight (the first hexadecimal number inside the square brackets) is `1E57` on both lines.

For comparisons in both searching and sorting, MySQL pays attention to the primary weight only,ignoring all the other numbers. This means that we are sorting が and か correctly according to the Unicode specification. If we wanted to distinguish them, we'd have to use a non-UCA (Unicode Collation Algorithm) collation (`utf8_bin` or `utf8_general_ci`), or to compare the `HEX()` values,or use `ORDER BY CONVERT(s1 USING sjis)`. Being correct “according to Unicode” is not enough, of course: the person who submitted the bug was equally correct. To solve this, we need another collation for Japanese according to the JIS X 4061 standard, in which voiced/unvoiced letter pairs like `KA`/`GA` are distinguishable for ordering purposes.

A.11.14.Why do CJK strings sort incorrectly in Unicode? (II)Note The CJK sorting problems described here can occur for MySQL versions prior to MySQL 8.0. As of MySQL 8.0, they can be solved by using the`utf8mb4` character set and the `utf8mb4_ja_0900_as_cs` collation.

If you are using Unicode (`ucs2` or `utf8`), and you know what the Unicode sort order is (see Section A.11, “MySQL 5.6 FAQ: MySQL Chinese, Japanese, and Korean Character Sets”), but MySQL still seems to sort your table incorrectly, first verify the character set in the table definition:

```
mysql> SHOW CREATE TABLE t\G
******************** 1. row ******************
Table: t
Create Table: CREATE TABLE `t` (
`s1` char(1) CHARACTER SET ucs2 DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1
```

Since the character set for the column `s1` appears to be correct (`ucs2`), check what information the`INFORMATION_SCHEMA.COLUMNS` table can provide about this column:

```
mysql> SELECT COLUMN_NAME, CHARACTER_SET_NAME, COLLATION_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE COLUMN_NAME = 's1'
AND TABLE_NAME = 't';
+-------------+--------------------+-----------------+
| COLUMN_NAME | CHARACTER_SET_NAME | COLLATION_NAME  |
+-------------+--------------------+-----------------+
| s1          | ucs2               | ucs2_general_ci |
+-------------+--------------------+-----------------+
```

(See Section 21.3.5, “The INFORMATION_SCHEMA COLUMNS Table”, for more information.)You can see that the collation is `ucs2_general_ci` instead of `ucs2_unicode_ci`. The reason why this is so can be found using `SHOW CHARACTER SET`, as shown here:

```
mysql> SHOW CHARSET LIKE 'ucs2%';
+---------+---------------+-------------------+--------+
| Charset | Description   | Default collation | Maxlen |
+---------+---------------+-------------------+--------+
| ucs2    | UCS-2 Unicode | ucs2_general_ci   |      2 |
+---------+---------------+-------------------+--------+
```

For `ucs2` and `utf8`, the default collation is “general”. To specify a Unicode UCA collation, use`COLLATE ucs2_unicode_ci`, as shown in the preceding item.

MySQL 5.6 FAQ: Connectors & APIs A.11.15.Why are my supplementary characters rejected by MySQL?

Supplementary characters lie outside the Unicode Basic Multilingual Plane / Plane 0. BMP characters have code point values between `U+0000` and `U+FFFF`. Supplementary characters have code point values between `U+10000` and `U+10FFFF`.

To store supplementary characters, you must use a character set that permits them:

- The `utf8` and `ucs2` character sets support BMP characters only.

The `utf8` character set permits only `UTF-8` characters that take up to three bytes. This has led to reports such as that found in Bug #12600, which we rejected as “not a bug”. With `utf8`, MySQL must truncate an input string when it encounters bytes that it does no understand. Otherwise, it is unknown how long the bad multibyte character is.

One possible workaround is to use `ucs2` instead of `utf8`, in which case the “bad” characters are changed to question marks. However, no truncation takes place. You can also change the data type to `BLOB` or `BINARY`, which perform no validity checking.

- The `utf8mb4`, `utf16`, `utf16le`, and `utf32` character sets support BMP characters, as well as

supplementary characters outside the BMP.

> A.11.16.Should “CJK” be “CJKV”?

No. The term “CJKV” (Chinese Japanese Korean Vietnamese) refers to Vietnamese character sets which contain Han (originally Chinese) characters. MySQL supports the modern Vietnamese script with Western characters, but does not support the old Vietnamese script using Han characters.

As of MySQL 5.6, there are Vietnamese collations for Unicode character sets, as described in Section 10.10.1, “Unicode Character Sets”.

> A.11.17.Does MySQL permit CJK characters to be used in database and table names?

Yes.

> A.11.18.Where can I find translations of the MySQL Manual into Chinese, Japanese, and Korean?

The Japanese translation of the MySQL 5.6 manual can be downloaded from https://dev.mysql.com/doc/.

> A.11.19.Where can I get help with CJK and related issues in MySQL?

The following resources are available:

- A listing of MySQL user groups can be found at https://wikis.oracle.com/display/mysql/List+of

+MySQL+User+Groups.

- View feature requests relating to character set issues at http://tinyurl.com/y6xcuf.
- Visit the MySQL Character Sets, Collation, Unicode Forum. http://forums.mysql.com/ also

provides foreign-language forums.

## A.12 MySQL 5.6 FAQ: Connectors & APIs

For common questions, issues, and answers relating to the MySQL Connectors and other APIs, see the following areas of the Manual:

- Using C API Features

MySQL 5.6 FAQ: C API, libmysql

- Connector/ODBC Notes and Tips
- Connector/NET Programming
- MySQL Connector/J 8.0 Developer Guide

## A.13 MySQL 5.6 FAQ: C API, libmysql

Frequently asked questions about MySQL C API and libmysql.

A.13.1 What is “MySQL Native C API”? What are typical benefits and use cases? ........................... 3542 A.13.2 Which version of libmysql should I use? ............................................................................. 3542 A.13.3 What if I want to use the “NoSQL” X DevAPI? .................................................................... 3542 A.13.4 How to I download libmysql? .............................................................................................. 3542 A.13.5 Where is the documentation? ............................................................................................. 3542 A.13.6 How do I report bugs? ....................................................................................................... 3542 A.13.7 Is it possible to compile the library myself? ......................................................................... 3542 A.13.1.What is “MySQL Native C API”? What are typical benefits and use cases?

libmysql is a C-based API that you can use in C applications to connect with the MySQL database server. It is also itself used as the foundation for drivers for standard database APIs like ODBC,Perl's DBI, and Python's DB API.

> A.13.2.Which version of libmysql should I use?

For MySQL 8.0, 5.7, 5.6, and 5.5, we recommend libmysql 8.0.

> A.13.3.What if I want to use the “NoSQL” X DevAPI?

For C-language and X DevApi Document Store for MySQL 8.0, we recommend MySQL Connector/C++. Connector/C++ 8.0 has compatible C headers. (This is not applicable to MySQL 5.7 or before.)A.13.4.How to I download libmysql?

- Linux: The Client Utilities Package is available from the MySQL Community Server download

page.

- Repos: The Client Utilities Package is available from the Yum, APT, SuSE repositories.
- Windows: The Client Utilities Package is available from Windows Installer.

> A.13.5.Where is the documentation?

See MySQL 5.6 C API Developer Guide.

> A.13.6.How do I report bugs?

Please report any bugs or inconsistencies you observe to our Bugs Database. Select the C API Client as shown.

> A.13.7.Is it possible to compile the library myself?

Compiling MySQL Server also compiles libmysqlclient; there is not a way to only compile libmysqlclient. For related information, see MySQL C API Implementations.

## A.14 MySQL 5.6 FAQ: Replication

MySQL 5.6 FAQ: Replication In the following section, we provide answers to questions that are most frequently asked about MySQL Replication.

A.14.1 Must the replica be connected to the source all the time? .................................................... 3543 A.14.2 Must I enable networking on my source and replica to enable replication? ............................. 3543 A.14.3 How do I know how late a replica is compared to the source? In other words, how do I know the date of the last statement replicated by the replica? ....................................................... 3543 A.14.4 How do I force the source to block updates until the replica catches up? ............................... 3544 A.14.5 What issues should I be aware of when setting up two-way replication? ................................ 3544 A.14.6 How can I use replication to improve performance of my system? ........................................ 3544 A.14.7 What should I do to prepare client code in my own applications to use performance-enhancing replication? ......................................................................................................................... 3545 A.14.8 When and how much can MySQL replication improve the performance of my system? ........... 3545 A.14.9 How can I use replication to provide redundancy or high availability? .................................... 3546 A.14.10 How do I tell whether a replication source server is using statement-based or row-based binary logging format? ........................................................................................................ 3546 A.14.11 How do I tell a replica to use row-based replication? ......................................................... 3546 A.14.12 How do I prevent `GRANT` and `REVOKE` statements from replicating to replica machines? ....... 3546 A.14.13 Does replication work on mixed operating systems (for example, the source runs on Linux while replicas run on macOS and Windows)? ...................................................................... 3546 A.14.14 Does replication work on mixed hardware architectures (for example, the source runs on a 64-bit machine while replicas run on 32-bit machines)? ........................................................ 3546 A.14.1.Must the replica be connected to the source all the time?

No, it does not. The replica can go down or stay disconnected for hours or even days, and then reconnect and catch up on updates. For example, you can set up a source/replica relationship over a dial-up link where the link is up only sporadically and for short periods of time. The implication of this is that, at any given time, the replica is not guaranteed to be in synchrony with the source unless you take some special measures.

To ensure that catchup can occur for a replica that has been disconnected, you must not remove binary log files from the source that contain information that has not yet been replicated to the replicas. Asynchronous replication can work only if the replica is able to continue reading the binary log from the point where it last read events.

> A.14.2.Must I enable networking on my source and replica to enable replication?

Yes, networking must be enabled on the source and replica. If networking is not enabled, the replica cannot connect to the source and transfer the binary log. Verify that the `skip_networking` system variable has not been enabled in the configuration file for either server.

A.14.3.How do I know how late a replica is compared to the source? In other words, how do I know the date of the last statement replicated by the replica?

Check the `Seconds_Behind_Master` column in the output from `SHOW REPLICA | SLAVE``STATUS`. See Section 17.1.5.1, “Checking Replication Status”.

When the replication SQL thread executes an event read from the source, it modifies its own time to the event timestamp. (This is why `TIMESTAMP` is well replicated.) In the `Time` column in the output of `SHOW PROCESSLIST`, the number of seconds displayed for the replication SQL thread is the number of seconds between the timestamp of the last replicated event and the real time of the replica machine. You can use this to determine the date of the last replicated event. Note that if your replica has been disconnected from the source for one hour, and then reconnects,you may immediately see large `Time` values such as 3600 for the replication SQL thread in `SHOW`MySQL 5.6 FAQ: Replication`PROCESSLIST`. This is because the replica is executing statements that are one hour old. See Section 17.2.1, “Replication Threads”.

> A.14.4.How do I force the source to block updates until the replica catches up?

Use the following procedure:

1. On the source, execute these statements:

```
mysql> FLUSH TABLES WITH READ LOCK;
mysql> SHOW MASTER STATUS;
```

Record the replication coordinates (the current binary log file name and position) from the output of the `SHOW` statement.

2. On the replica, issue the following statement, where the arguments to the

`SOURCE_POS_WAIT()` or `MASTER_POS_WAIT()` function are the replication coordinate values obtained in the previous step:

```
mysql> SELECT MASTER_POS_WAIT('log_name', log_pos);
Or from MySQL 8.0.26:
mysql> SELECT SOURCE_POS_WAIT('log_name', log_pos);
```

The `SELECT` statement blocks until the replica reaches the specified log file and position. At that point, the replica is in synchrony with the source and the statement returns.

3. On the source, issue the following statement to enable the source to begin processing updates

again:

```
mysql> UNLOCK TABLES;
```

> A.14.5.What issues should I be aware of when setting up two-way replication?

MySQL replication currently does not support any locking protocol between source and replica to guarantee the atomicity of a distributed (cross-server) update. In other words, it is possible for client A to make an update to co-source 1, and in the meantime, before it propagates to co-source 2,client B could make an update to co-source 2 that makes the update of client A work differently than it did on co-source 1. Thus, when the update of client A makes it to co-source 2, it produces tables that are different from what you have on co-source 1, even after all the updates from co-source 2 have also propagated. This means that you should not chain two servers together in a two-way replication relationship unless you are sure that your updates can safely happen in any order, or unless you take care of mis-ordered updates somehow in the client code.

You should also realize that two-way replication actually does not improve performance very much(if at all) as far as updates are concerned. Each server must do the same number of updates, just as you would have a single server do. The only difference is that there is a little less lock contention because the updates originating on another server are serialized in one replication thread. Even this benefit might be offset by network delays.

> A.14.6.How can I use replication to improve performance of my system?

Set up one server as the source and direct all writes to it. Then configure as many replicas as you have the budget and rackspace for, and distribute the reads among the source and the replicas. You can also start the replicas with the `--skip-innodb` option, enable the`low_priority_updates` system variable, and set the `delay_key_write` system variable to`ALL` to get speed improvements on the replica end. In this case, the replica uses nontransactional`MyISAM` tables instead of `InnoDB` tables to get more speed by eliminating transactional overhead.

MySQL 5.6 FAQ: Replication A.14.7.What should I do to prepare client code in my own applications to use performance-enhancing replication?

See the guide to using replication as a scale-out solution, Section 17.3.4, “Using Replication for Scale-Out”.

> A.14.8.When and how much can MySQL replication improve the performance of my system?

MySQL replication is most beneficial for a system that processes frequent reads and infrequent writes. In theory, by using a single-source/multiple-replica setup, you can scale the system by adding more replicas until you either run out of network bandwidth, or your update load grows to the point that the source cannot handle it.

To determine how many replicas you can use before the added benefits begin to level out, and how much you can improve performance of your site, you must know your query patterns, and determine empirically by benchmarking the relationship between the throughput for reads and writes on a typical source and a typical replica. The example here shows a rather simplified calculation of what you can get with replication for a hypothetical system. Let `reads` and `writes` denote the number of reads and writes per second, respectively.

Let's say that system load consists of 10% writes and 90% reads, and we have determined by benchmarking that `reads` is 1200 - 2 * `writes`. In other words, the system can do 1,200 reads per second with no writes, the average write is twice as slow as the average read, and the relationship is linear. Suppose that the source and each replica have the same capacity, and that we have one source and N replicas. Then we have for each server (source or replica):`reads` = 1200 - 2 * `writes``reads` = 9 * `writes` / (N + 1) (reads are split, but writes replicated to all replicas)9 * `writes` / (N + 1) + 2 * `writes` = 1200`writes` = 1200 / (2 + 9/(N + 1))The last equation indicates the maximum number of writes for N replicas, given a maximum possible read rate of 1,200 per second and a ratio of nine reads per write.

This analysis yields the following conclusions:

- If N = 0 (which means we have no replication), our system can handle about 1200/11 = 109 writes

per second.

- If N = 1, we get up to 184 writes per second.
- If N = 8, we get up to 400 writes per second.
- If N = 17, we get up to 480 writes per second.
- Eventually, as N approaches infinity (and our budget negative infinity), we can get very close to

600 writes per second, increasing system throughput about 5.5 times. However, with only eight servers, we increase it nearly four times.

These computations assume infinite network bandwidth and neglect several other factors that could be significant on your system. In many cases, you may not be able to perform a computation similar to the one just shown that accurately predicts what happens on your system if you add N replicas.

However, answering the following questions should help you decide whether and by how much replication may improve the performance of your system:MySQL 5.6 FAQ: MySQL Enterprise Thread Pool

- What is the read/write ratio on your system?
- How much more write load can one server handle if you reduce the reads?
- For how many replicas do you have bandwidth available on your network?

> A.14.9.How can I use replication to provide redundancy or high availability?

How you implement redundancy is entirely dependent on your application and circumstances. High-availability solutions (with automatic failover) require active monitoring and either custom scripts or third party tools to provide the failover support from the original MySQL server to the replica.

To handle the process manually, you should be able to switch from a failed source to a pre-configured replica by altering your application to talk to the new server or by adjusting the DNS for the MySQL server from the failed server to the new server.

For more information and some example solutions, see Section 17.3.7, “Switching Sources During Failover”.

A.14.10.How do I tell whether a replication source server is using statement-based or row-based binary logging format?

Check the value of the `binlog_format` system variable:

```
mysql> SHOW VARIABLES LIKE 'binlog_format';
```

The value shown is always one of `STATEMENT`, `ROW`, or `MIXED`. For `MIXED` mode, statement-based logging is used by default but replication switches automatically to row-based logging under certain conditions, such as unsafe statements. For information about when this may occur, see Section 5.4.4.3, “Mixed Binary Logging Format”.

> A.14.11.How do I tell a replica to use row-based replication?

Replicas automatically know which format to use.

> A.14.12.How do I prevent `GRANT` and `REVOKE` statements from replicating to replica machines?

Start the server with the `--replicate-wild-ignore-table=mysql.%` option to ignore replication for tables in the `mysql` database.

A.14.13.Does replication work on mixed operating systems (for example, the source runs on Linux while replicas run on macOS and Windows)?

Yes.

A.14.14.Does replication work on mixed hardware architectures (for example, the source runs on a 64-bit machine while replicas run on 32-bit machines)?

Yes.

## A.15 MySQL 5.6 FAQ: MySQL Enterprise Thread Pool

A.15.1 What is the Thread Pool and what problem does it solve? ................................................... 3547 A.15.2 How does the Thread Pool limit and manage concurrent sessions and transactions for optimal performance and throughput? .............................................................................................. 3547 A.15.3 How is the Thread Pool different from the client side Connection Pool? ................................. 3547 A.15.4 When should I use the Thread Pool? .................................................................................. 3547 MySQL 5.6 FAQ: MySQL Enterprise Thread Pool A.15.5 Are there recommended Thread Pool configurations? .......................................................... 3548 A.15.1.What is the Thread Pool and what problem does it solve?

The MySQL Thread Pool is a MySQL server plugin that extends the default connection-handling capabilities of the MySQL server to limit the number of concurrently executing statements/queries and transactions to ensure that each has sufficient CPU and memory resources to fulfill its task. For MySQL 5.6, the Thread Pool plugin is included in MySQL Enterprise Edition, a commercial product.

The default thread-handling model in MySQL Server executes statements using one thread per client connection. As more clients connect to the server and execute statements, overall performance degrades. The Thread Pool plugin provides an alternative thread-handling model designed to reduce overhead and improve performance. The Thread Pool plugin increases server performance by efficiently managing statement execution threads for large numbers of client connections, especially on modern multi-CPU/Core systems.

For more information, see Section 5.5.3, “MySQL Enterprise Thread Pool”.

A.15.2.How does the Thread Pool limit and manage concurrent sessions and transactions for optimal performance and throughput?

The Thread Pool uses a “divide and conquer” approach to limiting and balancing concurrency.

Unlike the default connection handling of the MySQL Server, the Thread Pool separates connections and threads, so there is no fixed relationship between connections and the threads that execute statements received from those connections. The Thread Pool then manages client connections within configurable thread groups, where they are prioritized and queued based on the nature of the work they were submitted to accomplish.

For more information, see Section 5.5.3.3, “Thread Pool Operation”.

> A.15.3.How is the Thread Pool different from the client side Connection Pool?

The MySQL Connection Pool operates on the client side to ensure that a MySQL client does not constantly connect to and disconnect from the MySQL server. It is designed to cache idle connections in the MySQL client for use by other users as they are needed. This minimizes the overhead and expense of establishing and tearing down connections as queries are submitted to the MySQL server. The MySQL Connection Pool has no visibility as to the query handling capabilities or load of the back-end MySQL server. By contrast, the Thread Pool operates on the MySQL server side and is designed to manage the execution of inbound concurrent connections and queries as they are received from the client connections accessing the back-end MySQL database. Because of the separation of duties, the MySQL Connection Pool and Thread Pool are orthogonal and can be used independent of each other.

MySQL Connection Pooling via the MySQL Connectors is covered in Chapter 23, Connectors and APIs.

> A.15.4.When should I use the Thread Pool?

There are a few rules of thumb to consider for optimal Thread Pool use cases:The MySQL `Threads_running` variable keeps track of the number of concurrent statements currently executing in the MySQL Server. If this variable consistently exceeds a region where the server won't operate optimally (usually going beyond 40 for InnoDB workloads), the Thread Pool should be beneficial, especially in extreme parallel overload situations.

If you are using the `innodb_thread_concurrency` to limit the number of concurrently executing statements, you should find that the Thread Pool solves the same problem, only better, by assigning MySQL 5.6 FAQ: InnoDB Change Buffer connections to thread groups, then queuing executions based on transactional content, user defined designations, and so forth.

Lastly, if your workload comprises mainly short queries, the Thread Pool should be beneficial.

To learn more, see Section 5.5.3.4, “Thread Pool Tuning”.

> A.15.5.Are there recommended Thread Pool configurations?

The Thread Pool has a number of user case driven configuration parameters that affect its performance. To learn about these and tips on tuning, see Section 5.5.3.4, “Thread Pool Tuning”.

## A.16 MySQL 5.6 FAQ: InnoDB Change Buffer

A.16.1 What types of operations modify secondary indexes and result in change buffering? .............. 3548 A.16.2 What is the benefit of the `InnoDB` change buffer? ............................................................... 3548 A.16.3 Does the change buffer support other types of indexes? ...................................................... 3548 A.16.4 How much space does `InnoDB` use for the change buffer? ................................................. 3548 A.16.5 How do I determine the current size of the change buffer? ................................................... 3549 A.16.6 When does change buffer merging occur? .......................................................................... 3549 A.16.7 When is the change buffer flushed? ................................................................................... 3549 A.16.8 When should the change buffer be used? ........................................................................... 3549 A.16.9 When should the change buffer not be used? ..................................................................... 3549 A.16.10 Where can I find additional information about the change buffer? ........................................ 3550 A.16.1.What types of operations modify secondary indexes and result in change buffering?

`INSERT`, `UPDATE`, and `DELETE` operations can modify secondary indexes. If an affected index page is not in the buffer pool, the changes can be buffered in the change buffer.

> A.16.2.What is the benefit of the `InnoDB` change buffer?

Buffering secondary index changes when secondary index pages are not in the buffer pool avoids expensive random access I/O operations that would be required to immediately read in affected index pages from disk. Buffered changes can be applied later, in batches, as pages are read into the buffer pool by other read operations.

> A.16.3.Does the change buffer support other types of indexes?

No. The change buffer only supports secondary indexes. Clustered indexes, full-text indexes, and spatial indexes are not supported. Full-text indexes have their own caching mechanism.

> A.16.4.How much space does `InnoDB` use for the change buffer?

Prior to the introduction of the `innodb_change_buffer_max_size` configuration option in MySQL 5.6, the maximum size of the on-disk change buffer in the system tablespace was 1/3 of the`InnoDB` buffer pool size.

In MySQL 5.6 and later, the `innodb_change_buffer_max_size` configuration option defines the maximum size of the change buffer as a percentage of the total buffer pool size. By default,`innodb_change_buffer_max_size` is set to 25. The maximum setting is 50.

`InnoDB` does not buffer an operation if it would cause the on-disk change buffer to exceed the defined limit.

Change buffer pages are not required to persist in the buffer pool and may be evicted by LRU operations.

MySQL 5.6 FAQ: InnoDB Change Buffer A.16.5.How do I determine the current size of the change buffer?

The current size of the change buffer is reported by `SHOW ENGINE INNODB STATUS \G`, under the `INSERT BUFFER AND ADAPTIVE HASH INDEX` heading. For example:

```
-------------------------------------
INSERT BUFFER AND ADAPTIVE HASH INDEX
-------------------------------------
Ibuf: size 1, free list len 0, seg size 2, 0 merges
```

Relevant data points include:

- `size`: The number of pages used within the change buffer. Change buffer size is equal to `seg`

`size - (1 + free list len)`. The `1 +` value represents the change buffer header page.

- `seg size`: The size of the change buffer, in pages.

For information about monitoring change buffer status, see Section 14.5.2, “Change Buffer”.

> A.16.6.When does change buffer merging occur?

- When a page is read into the buffer pool, buffered changes are merged upon completion of the

read, before the page is made available.

- Change buffer merging is performed as a background task. The `innodb_io_capacity`

parameter sets an upper limit on the I/O activity performed by `InnoDB` background tasks such as merging data from the change buffer.

- A change buffer merge is performed during crash recovery. Changes are applied from the change

buffer (in the system tablespace) to leaf pages of secondary indexes as index pages are read into the buffer pool.

- The change buffer is fully durable and can survive a system crash. Upon restart, change buffer

merge operations resume as part of normal operations.

- A full merge of the change buffer can be forced as part of a slow server shutdown using `--`

```
innodb-fast-shutdown=0.
```

> A.16.7.When is the change buffer flushed?

Updated pages are flushed by the same flushing mechanism that flushes the other pages that occupy the buffer pool.

> A.16.8.When should the change buffer be used?

The change buffer is a feature designed to reduce random I/O to secondary indexes as indexes grow larger and no longer fit in the `InnoDB` buffer pool. Generally, the change buffer should be used when the entire data set does not fit into the buffer pool, when there is substantial DML activity that modifies secondary index pages, or when there are lots of secondary indexes that are regularly changed by DML activity.

> A.16.9.When should the change buffer not be used?

You might consider disabling the change buffer if the entire data set fits within the `InnoDB` buffer pool, if you have relatively few secondary indexes, or if you are using solid-state storage, where random reads are about as fast as sequential reads. Before making configuration changes, it is recommended that you run tests using a representative workload to determine if disabling the change buffer provides any benefit.

MySQL 5.6 FAQ: Virtualization Support A.16.10.Where can I find additional information about the change buffer?

See Section 14.5.2, “Change Buffer”.

## A.17 MySQL 5.6 FAQ: Virtualization Support

A.17.1 Is MySQL supported on virtualized environments such as Oracle VM, VMWare, Docker,Microsoft Hyper-V, or others? .............................................................................................. 3550 A.17.1.Is MySQL supported on virtualized environments such as Oracle VM, VMWare, Docker, Microsoft Hyper-V, or others?

MySQL is supported on virtualized environments, but is certified only for Oracle VM. Contact Oracle Support for more information.

Be aware of potential problems when using virtualization software. The usual ones are related to performance, performance degradations, slowness, or unpredictability of disk, I/O, network, and memory.
