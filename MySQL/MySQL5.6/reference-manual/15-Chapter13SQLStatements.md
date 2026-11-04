---
title: Chapter 13 SQL Statements
book: MySQL 5.6 Reference Manual
version: "5.6"
source: "MySQL/MySQL5.6/sources/refman-5.6-en.pdf#page=1661"
tags:
  - mysql
  - mysql-5.6
  - reference-manual
---

## Table of Contents

13.1 Data Definition Statements .................................................................................................... 1634

13.1.1 ALTER DATABASE Statement ................................................................................... 1634

13.1.2 ALTER EVENT Statement .......................................................................................... 1635

13.1.3 ALTER FUNCTION Statement .................................................................................... 1637

13.1.4 ALTER LOGFILE GROUP Statement .......................................................................... 1637

13.1.5 ALTER PROCEDURE Statement ................................................................................ 1639

13.1.6 ALTER SERVER Statement ........................................................................................ 1639

13.1.7 ALTER TABLE Statement ........................................................................................... 1639

13.1.8 ALTER TABLESPACE Statement ............................................................................... 1660

13.1.9 ALTER VIEW Statement ............................................................................................. 1661

13.1.10 CREATE DATABASE Statement ............................................................................... 1661

13.1.11 CREATE EVENT Statement ...................................................................................... 1662

13.1.12 CREATE FUNCTION Statement ............................................................................... 1667

13.1.13 CREATE INDEX Statement ...................................................................................... 1667

13.1.14 CREATE LOGFILE GROUP Statement ..................................................................... 1672

13.1.15 CREATE PROCEDURE and CREATE FUNCTION Statements ................................... 1674

13.1.16 CREATE SERVER Statement ................................................................................... 1679

13.1.17 CREATE TABLE Statement ...................................................................................... 1681

13.1.18 CREATE TABLESPACE Statement ........................................................................... 1718

13.1.19 CREATE TRIGGER Statement ................................................................................. 1720

13.1.20 CREATE VIEW Statement ........................................................................................ 1722

13.1.21 DROP DATABASE Statement ................................................................................... 1726

13.1.22 DROP EVENT Statement ......................................................................................... 1727

13.1.23 DROP FUNCTION Statement ................................................................................... 1727

13.1.24 DROP INDEX Statement .......................................................................................... 1727

13.1.25 DROP LOGFILE GROUP Statement ......................................................................... 1728

13.1.26 DROP PROCEDURE and DROP FUNCTION Statements .......................................... 1728

13.1.27 DROP SERVER Statement ....................................................................................... 1729

13.1.28 DROP TABLE Statement .......................................................................................... 1729

13.1.29 DROP TABLESPACE Statement ............................................................................... 1730

13.1.30 DROP TRIGGER Statement ..................................................................................... 1730

13.1.31 DROP VIEW Statement ............................................................................................ 1731

13.1.32 RENAME TABLE Statement ..................................................................................... 1731

13.1.33 TRUNCATE TABLE Statement ................................................................................. 1732

13.2 Data Manipulation Statements ............................................................................................... 1733

13.2.1 CALL Statement ......................................................................................................... 1733

13.2.2 DELETE Statement .................................................................................................... 1735

13.2.3 DO Statement ............................................................................................................ 1739

13.2.4 HANDLER Statement ................................................................................................. 1739

13.2.5 INSERT Statement ..................................................................................................... 1741

13.2.6 LOAD DATA Statement .............................................................................................. 1750

13.2.7 LOAD XML Statement ................................................................................................ 1762

13.2.8 REPLACE Statement .................................................................................................. 1769

13.2.9 SELECT Statement .................................................................................................... 1772

13.2.10 Subqueries ............................................................................................................... 1788

13.2.11 UPDATE Statement .................................................................................................. 1801

13.3 Transactional and Locking Statements ................................................................................... 1804

13.3.1 START TRANSACTION, COMMIT, and ROLLBACK Statements .................................. 1804 Data Definition Statements

13.3.2 Statements That Cannot Be Rolled Back ..................................................................... 1807

13.3.3 Statements That Cause an Implicit Commit ................................................................. 1808

13.3.4 SAVEPOINT, ROLLBACK TO SAVEPOINT, and RELEASE SAVEPOINT Statements .... 1809

13.3.5 LOCK TABLES and UNLOCK TABLES Statements ..................................................... 1809

13.3.6 SET TRANSACTION Statement .................................................................................. 1815

13.3.7 XA Transactions ......................................................................................................... 1818

13.4 Replication Statements .......................................................................................................... 1822

13.4.1 SQL Statements for Controlling Replication Source Servers .......................................... 1822

13.4.2 SQL Statements for Controlling Replica Servers .......................................................... 1825

13.5 Prepared Statements ............................................................................................................ 1835

13.5.1 PREPARE Statement ................................................................................................. 1839

13.5.2 EXECUTE Statement ................................................................................................. 1840

13.5.3 DEALLOCATE PREPARE Statement .......................................................................... 1840

13.6 Compound Statements .......................................................................................................... 1840

13.6.1 BEGIN ... END Compound Statement .......................................................................... 1840

13.6.2 Statement Labels ....................................................................................................... 1841

13.6.3 DECLARE Statement ................................................................................................. 1842

13.6.4 Variables in Stored Programs ..................................................................................... 1842

13.6.5 Flow Control Statements ............................................................................................ 1844

13.6.6 Cursors ...................................................................................................................... 1848

13.6.7 Condition Handling ..................................................................................................... 1850

13.7 Database Administration Statements ...................................................................................... 1875

13.7.1 Account Management Statements ............................................................................... 1875

13.7.2 Table Maintenance Statements ................................................................................... 1895

13.7.3 Plugin and Loadable Function Statements ................................................................... 1906

13.7.4 SET Statements ......................................................................................................... 1909

13.7.5 SHOW Statements ..................................................................................................... 1914

13.7.6 Other Administrative Statements ................................................................................. 1964

13.8 Utility Statements .................................................................................................................. 1975

13.8.1 DESCRIBE Statement ................................................................................................ 1975

13.8.2 EXPLAIN Statement ................................................................................................... 1975

13.8.3 HELP Statement ........................................................................................................ 1977

13.8.4 USE Statement .......................................................................................................... 1979 This chapter describes the syntax for the SQL statements supported by MySQL.

## 13.1 Data Definition Statements

### 13.1.1 ALTER DATABASE Statement

```
ALTER {DATABASE | SCHEMA} [db_name]
alter_option ...
ALTER {DATABASE | SCHEMA} db_name
UPGRADE DATA DIRECTORY NAME
alter_option: {
[DEFAULT] CHARACTER SET [=] charset_name
| [DEFAULT] COLLATE [=] collation_name
}
```

`ALTER DATABASE` enables you to change the overall characteristics of a database. These characteristics are stored in the `db.opt` file in the database directory. This statement requires the `ALTER` privilege on the database. `ALTER SCHEMA` is a synonym for `ALTER DATABASE`.

The database name can be omitted from the first syntax, in which case the statement applies to the default database. An error occurs if there is no default database.

ALTER EVENT Statement

- Character Set and Collation Options
- Upgrading from Versions Older than MySQL 5.1

> Character Set and Collation Options

The `CHARACTER SET` clause changes the default database character set. The `COLLATE` clause changes the default database collation. For information about character set and collation names, see Chapter 10,Character Sets, Collations, Unicode.

To see the available character sets and collations, use the `SHOW CHARACTER SET` and `SHOW``COLLATION` statements, respectively. See Section 13.7.5.4, “SHOW CHARACTER SET Statement”, and Section 13.7.5.5, “SHOW COLLATION Statement”.

A stored routine that uses the database defaults when the routine is created includes those defaults as part of its definition. (In a stored routine, variables with character data types use the database defaults if the character set or collation are not specified explicitly. See Section 13.1.15, “CREATE PROCEDURE and CREATE FUNCTION Statements”.) If you change the default character set or collation for a database, any stored routines that are to use the new defaults must be dropped and recreated.

> Upgrading from Versions Older than MySQL 5.1

The syntax that includes the `UPGRADE DATA DIRECTORY NAME` clause updates the name of the directory associated with the database to use the encoding implemented in MySQL 5.1 for mapping database names to database directory names (see Section 9.2.4, “Mapping of Identifiers to File Names”). This clause is for use under these conditions:

- It is intended when upgrading MySQL to 5.1 or later from older versions.
- It is intended to update a database directory name to the current encoding format if the name contains

special characters that need encoding.

- The statement is used by `mysqlcheck` (as invoked by `mysql_upgrade`).

For example, if a database in MySQL 5.0 has the name `a-b-c`, the name contains instances of the -(dash) character. In MySQL 5.0, the database directory is also named `a-b-c`, which is not necessarily safe for all file systems. In MySQL 5.1 and later, the same database name is encoded as `a@002db@002dc` to produce a file system-neutral directory name.

When a MySQL installation is upgraded to MySQL 5.1 or later from an older version,the server displays a name such as `a-b-c` (which is in the old format) as `#mysql50#a-b-c`, and you must refer to the name using the `#mysql50#` prefix. Use `UPGRADE DATA DIRECTORY NAME` in this case to explicitly tell the server to re-encode the database directory name to the current encoding format:

```
ALTER DATABASE `#mysql50#a-b-c` UPGRADE DATA DIRECTORY NAME;
```

After executing this statement, you can refer to the database as `a-b-c` without the special `#mysql50#`prefix.

### 13.1.2 ALTER EVENT Statement

```
ALTER
[DEFINER = user]
EVENT event_name
[ON SCHEDULE schedule]
[ON COMPLETION [NOT] PRESERVE]
[RENAME TO new_event_name]
```

ALTER EVENT Statement

```
[ENABLE | DISABLE | DISABLE ON SLAVE]
[COMMENT 'string']
[DO event_body]
```

The `ALTER EVENT` statement changes one or more of the characteristics of an existing event without the need to drop and recreate it. The syntax for each of the `DEFINER`, `ON SCHEDULE`, `ON COMPLETION`,`COMMENT`, `ENABLE` / `DISABLE`, and `DO` clauses is exactly the same as when used with `CREATE EVENT`.

(See Section 13.1.11, “CREATE EVENT Statement”.)Any user can alter an event defined on a database for which that user has the `EVENT` privilege. When a user executes a successful `ALTER EVENT` statement, that user becomes the definer for the affected event.

`ALTER EVENT` works only with an existing event:

```
mysql> ALTER EVENT no_such_event
>     ON SCHEDULE
>       EVERY '2:3' DAY_HOUR;
ERROR 1517 (HY000): Unknown event 'no_such_event'
```

In each of the following examples, assume that the event named `myevent` is defined as shown here:

```
CREATE EVENT myevent
ON SCHEDULE
EVERY 6 HOUR
COMMENT 'A sample comment.'
DO
UPDATE myschema.mytable SET mycol = mycol + 1;
```

The following statement changes the schedule for `myevent` from once every six hours starting immediately to once every twelve hours, starting four hours from the time the statement is run:

```
ALTER EVENT myevent
ON SCHEDULE
EVERY 12 HOUR
STARTS CURRENT_TIMESTAMP + INTERVAL 4 HOUR;
```

It is possible to change multiple characteristics of an event in a single statement. This example changes the SQL statement executed by `myevent` to one that deletes all records from `mytable`; it also changes the schedule for the event such that it executes once, one day after this `ALTER EVENT` statement is run.

```
ALTER EVENT myevent
ON SCHEDULE
AT CURRENT_TIMESTAMP + INTERVAL 1 DAY
DO
TRUNCATE TABLE myschema.mytable;
```

Specify the options in an `ALTER EVENT` statement only for those characteristics that you want to change;

omitted options keep their existing values. This includes any default values for `CREATE EVENT` such as

```
ENABLE.
```

To disable `myevent`, use this `ALTER EVENT` statement:

```
ALTER EVENT myevent
DISABLE;
```

The `ON SCHEDULE` clause may use expressions involving built-in MySQL functions and user variables to obtain any of the `timestamp` or `interval` values which it contains. You cannot use stored routines or loadable functions in such expressions, and you cannot use any table references; however, you can use`SELECT FROM DUAL`. This is true for both `ALTER EVENT` and `CREATE EVENT` statements. References to stored routines, loadable functions, and tables in such cases are specifically not permitted, and fail with an error (see Bug #22830).

ALTER FUNCTION Statement Although an `ALTER EVENT` statement that contains another `ALTER EVENT` statement in its `DO` clause appears to succeed, when the server attempts to execute the resulting scheduled event, the execution fails with an error.

To rename an event, use the `ALTER EVENT` statement's `RENAME TO` clause. This statement renames the event `myevent` to `yourevent`:

```
ALTER EVENT myevent
RENAME TO yourevent;
```

You can also move an event to a different database using `ALTER EVENT ... RENAME TO ...` and`db_name.event_name` notation, as shown here:

```
ALTER EVENT olddb.myevent
RENAME TO newdb.myevent;
```

To execute the previous statement, the user executing it must have the `EVENT` privilege on both the `olddb`and `newdb` databases.

Note There is no `RENAME EVENT` statement.

The value `DISABLE ON SLAVE` is used on a replica instead of `ENABLE` or `DISABLE` to indicate an event that was created on the source and replicated to the replica, but that is not executed on the replica.

Normally, `DISABLE ON SLAVE` is set automatically as required; however, there are some circumstances under which you may want or need to change it manually. See Section 17.4.1.16, “Replication of Invoked Features”, for more information.

### 13.1.3 ALTER FUNCTION Statement

```
ALTER FUNCTION func_name [characteristic ...]
characteristic: {
COMMENT 'string'
| LANGUAGE SQL
| { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
| SQL SECURITY { DEFINER | INVOKER }
}
```

This statement can be used to change the characteristics of a stored function. More than one change may be specified in an `ALTER FUNCTION` statement. However, you cannot change the parameters or body of a stored function using this statement; to make such changes, you must drop and re-create the function

```
using DROP FUNCTION and CREATE FUNCTION.
```

You must have the `ALTER ROUTINE` privilege for the function. (That privilege is granted automatically to the function creator.) If binary logging is enabled, the `ALTER FUNCTION` statement might also require the`SUPER` privilege, as described in Section 20.7, “Stored Program Binary Logging”.

### 13.1.4 ALTER LOGFILE GROUP Statement

```
ALTER LOGFILE GROUP logfile_group
ADD UNDOFILE 'file_name'
[INITIAL_SIZE [=] size]
[WAIT]
ENGINE [=] engine_name
```

This statement adds an `UNDO` file named '`file_name`' to an existing log file group `logfile_group`. An`ALTER LOGFILE GROUP` statement has one and only one `ADD UNDOFILE` clause. No `DROP UNDOFILE`clause is currently supported.

ALTER LOGFILE GROUP Statement Note All NDB Cluster Disk Data objects share the same namespace. This means that each Disk Data object must be uniquely named (and not merely each Disk Data object of a given type). For example, you cannot have a tablespace and an undo log file with the same name, or an undo log file and a data file with the same name.

The optional `INITIAL_SIZE` parameter sets the `UNDO` file's initial size in bytes; if not specified, the initial size defaults to 134217728 (128 MB). Prior to MySQL NDB Cluster 7.3.2, this value was required to be specified using digits; in MySQL NDB Cluster 7.3.2 and later, you may optionally follow `size` with a one-letter abbreviation for an order of magnitude, similar to those used in `my.cnf`. Generally, this is one of the letters M (megabytes) or G (gigabytes). (Bug #13116514, Bug #16104705, Bug #62858)On 32-bit systems, the maximum supported value for `INITIAL_SIZE` is 4294967296 (4 GB). (Bug#29186)The minimum allowed value for `INITIAL_SIZE` is 1048576 (1 MB). (Bug #29574)Note`WAIT` is parsed but otherwise ignored. This keyword currently has no effect, and is intended for future expansion.

The `ENGINE` parameter (required) determines the storage engine which is used by this log file group,with `engine_name` being the name of the storage engine. Currently, the only accepted values for`engine_name` are “`NDBCLUSTER`” and “`NDB`”. The two values are equivalent.

Here is an example, which assumes that the log file group `lg_3` has already been created using `CREATE``LOGFILE GROUP` (see Section 13.1.14, “CREATE LOGFILE GROUP Statement”):

```
ALTER LOGFILE GROUP lg_3
ADD UNDOFILE 'undo_10.dat'
INITIAL_SIZE=32M
ENGINE=NDBCLUSTER;
```

When `ALTER LOGFILE GROUP` is used with `ENGINE = NDBCLUSTER` (alternatively, `ENGINE = NDB`), an`UNDO` log file is created on each NDB Cluster data node. You can verify that the `UNDO` files were created and obtain information about them by querying the Information Schema `FILES` table. For example:

```
mysql> SELECT FILE_NAME, LOGFILE_GROUP_NUMBER, EXTRA
-> FROM INFORMATION_SCHEMA.FILES
-> WHERE LOGFILE_GROUP_NAME = 'lg_3';
+-------------+----------------------+----------------+
| FILE_NAME   | LOGFILE_GROUP_NUMBER | EXTRA          |
+-------------+----------------------+----------------+
| newdata.dat |                    0 | CLUSTER_NODE=3 |
| newdata.dat |                    0 | CLUSTER_NODE=4 |
| undo_10.dat |                   11 | CLUSTER_NODE=3 |
| undo_10.dat |                   11 | CLUSTER_NODE=4 |
+-------------+----------------------+----------------+
4 rows in set (0.01 sec)
```

(See Section 21.5.1, “The INFORMATION_SCHEMA FILES Table”.)Memory used for `UNDO_BUFFER_SIZE` comes from the global pool whose size is determined by the value of the `SharedGlobalMemory` data node configuration parameter. This includes any default value implied for this option by the setting of the `InitialLogFileGroup` data node configuration parameter.

`ALTER LOGFILE GROUP` is useful only with Disk Data storage for NDB Cluster. For more information, see Section 18.6.11, “NDB Cluster Disk Data Tables”.

ALTER PROCEDURE Statement

### 13.1.5 ALTER PROCEDURE Statement

```
ALTER PROCEDURE proc_name [characteristic ...]
characteristic: {
COMMENT 'string'
| LANGUAGE SQL
| { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
| SQL SECURITY { DEFINER | INVOKER }
}
```

This statement can be used to change the characteristics of a stored procedure. More than one change may be specified in an `ALTER PROCEDURE` statement. However, you cannot change the parameters or body of a stored procedure using this statement; to make such changes, you must drop and re-create the procedure using `DROP PROCEDURE` and `CREATE PROCEDURE`.

You must have the `ALTER ROUTINE` privilege for the procedure. By default, that privilege is granted automatically to the procedure creator. This behavior can be changed by disabling the`automatic_sp_privileges` system variable. See Section 20.2.2, “Stored Routines and MySQL Privileges”.

### 13.1.6 ALTER SERVER Statement

```
ALTER SERVER  server_name
OPTIONS (option [, option] ...)
```

Alters the server information for `server_name`, adjusting any of the options permitted in the `CREATE``SERVER` statement. The corresponding fields in the `mysql.servers` table are updated accordingly. This statement requires the `SUPER` privilege.

For example, to update the `USER` option:

```
ALTER SERVER s OPTIONS (USER 'sally');
```

`ALTER SERVER` causes an implicit commit. See Section 13.3.3, “Statements That Cause an Implicit Commit”.

`ALTER SERVER` is not written to the binary log, regardless of the logging format that is in use.

In MySQL 5.6.11 only, `gtid_next` must be set to `AUTOMATIC` before issuing this statement. (Bug#16062608, Bug #16715809, Bug #69045)

### 13.1.7 ALTER TABLE Statement

```
ALTER [ONLINE | OFFLINE] [IGNORE] TABLE tbl_name
[alter_option [, alter_option] ...]
[partition_options]
alter_option: {
table_options
| ADD [COLUMN] col_name column_definition
[FIRST | AFTER col_name]
| ADD [COLUMN] (col_name column_definition,...)
| ADD {INDEX | KEY} [index_name]
[index_type] (key_part,...) [index_option] ...
| ADD {FULLTEXT | SPATIAL} [INDEX | KEY] [index_name]
(key_part,...) [index_option] ...
| ADD [CONSTRAINT [symbol]] PRIMARY KEY
[index_type] (key_part,...)
[index_option] ...
| ADD [CONSTRAINT [symbol]] UNIQUE [INDEX | KEY]
[index_name] [index_type] (key_part,...)
[index_option] ...
```

ALTER TABLE Statement

```
| ADD [CONSTRAINT [symbol]] FOREIGN KEY
[index_name] (col_name,...)
reference_definition
| ADD CHECK (expr)
| ALGORITHM [=] {DEFAULT | INPLACE | COPY}
| ALTER [COLUMN] col_name {
SET DEFAULT {literal | (expr)}
| DROP DEFAULT
}
| CHANGE [COLUMN] old_col_name new_col_name column_definition
[FIRST | AFTER col_name]
| [DEFAULT] CHARACTER SET [=] charset_name [COLLATE [=] collation_name]
| CONVERT TO CHARACTER SET charset_name [COLLATE collation_name]
| {DISABLE | ENABLE} KEYS
| {DISCARD | IMPORT} TABLESPACE
| DROP [COLUMN] col_name
| DROP {INDEX | KEY} index_name
| DROP PRIMARY KEY
| DROP FOREIGN KEY fk_symbol
| FORCE
| LOCK [=] {DEFAULT | NONE | SHARED | EXCLUSIVE}
| MODIFY [COLUMN] col_name column_definition
[FIRST | AFTER col_name]
| ORDER BY col_name [, col_name] ...
| RENAME [TO | AS] new_tbl_name
}
partition_options:
partition_option [partition_option] ...
partition_option: {
ADD PARTITION (partition_definition)
| DROP PARTITION partition_names
| TRUNCATE PARTITION {partition_names | ALL}
| COALESCE PARTITION number
| REORGANIZE PARTITION partition_names INTO (partition_definitions)
| EXCHANGE PARTITION partition_name WITH TABLE tbl_name
| ANALYZE PARTITION {partition_names | ALL}
| CHECK PARTITION {partition_names | ALL}
| OPTIMIZE PARTITION {partition_names | ALL}
| REBUILD PARTITION {partition_names | ALL}
| REPAIR PARTITION {partition_names | ALL}
| REMOVE PARTITIONING
}
key_part:
col_name [(length)] [ASC | DESC]
index_type:
USING {BTREE | HASH}
index_option: {
KEY_BLOCK_SIZE [=] value
| index_type
| WITH PARSER parser_name
| COMMENT 'string'
}
table_options:
table_option [[,] table_option] ...
table_option: {
AUTO_INCREMENT [=] value
| AVG_ROW_LENGTH [=] value
| [DEFAULT] CHARACTER SET [=] charset_name
| CHECKSUM [=] {0 | 1}
| [DEFAULT] COLLATE [=] collation_name
```

ALTER TABLE Statement

```
| COMMENT [=] 'string'
| CONNECTION [=] 'connect_string'
| {DATA | INDEX} DIRECTORY [=] 'absolute path to directory'
| DELAY_KEY_WRITE [=] {0 | 1}
| ENGINE [=] engine_name
| INSERT_METHOD [=] { NO | FIRST | LAST }
| KEY_BLOCK_SIZE [=] value
| MAX_ROWS [=] value
| MIN_ROWS [=] value
| PACK_KEYS [=] {0 | 1 | DEFAULT}
| PASSWORD [=] 'string'
| ROW_FORMAT [=] {DEFAULT | DYNAMIC | FIXED | COMPRESSED | REDUNDANT | COMPACT}
| STATS_AUTO_RECALC [=] {DEFAULT | 0 | 1}
| STATS_PERSISTENT [=] {DEFAULT | 0 | 1}
| STATS_SAMPLE_PAGES [=] value
| TABLESPACE tablespace_name [STORAGE {DISK | MEMORY}]
| UNION [=] (tbl_name[,tbl_name]...)
}
```

`ALTER TABLE` changes the structure of a table. For example, you can add or delete columns, create or destroy indexes, change the type of existing columns, or rename columns or the table itself. You can also change characteristics such as the storage engine used for the table or the table comment.

- To use `ALTER TABLE`, you need `ALTER`, `CREATE`, and `INSERT` privileges for the table. Renaming a

table requires `ALTER` and `DROP` on the old table, `ALTER`, `CREATE`, and `INSERT` on the new table.

- Following the table name, specify the alterations to be made. If none are given, `ALTER TABLE` does

nothing.

- The syntax for many of the permissible alterations is similar to clauses of the `CREATE TABLE` statement.

`column_definition` clauses use the same syntax for `ADD` and `CHANGE` as for `CREATE TABLE`. For more information, see Section 13.1.17, “CREATE TABLE Statement”.

- The word `COLUMN` is optional and can be omitted.
- Multiple `ADD`, `ALTER`, `DROP`, and `CHANGE` clauses are permitted in a single `ALTER TABLE` statement,

separated by commas. This is a MySQL extension to standard SQL, which permits only one of each clause per `ALTER TABLE` statement. For example, to drop multiple columns in a single statement, do this:

```
ALTER TABLE t2 DROP COLUMN c, DROP COLUMN d;
```

- If a storage engine does not support an attempted `ALTER TABLE` operation, a warning may result.

Such warnings can be displayed with `SHOW WARNINGS`. See Section 13.7.5.41, “SHOW WARNINGS Statement”. For information on troubleshooting `ALTER TABLE`, see Section B.3.6.1, “Problems with ALTER TABLE”.

- For usage examples, see Section 13.1.7.2, “ALTER TABLE Examples”.
- With the `mysql_info()` C API function, you can find out how many rows were copied by `ALTER`

`TABLE`, and (when `IGNORE` is used) how many rows were deleted due to duplication of unique key values. See mysql_info().

There are several additional aspects to the `ALTER TABLE` statement, described under the following topics in this section:

- Table Options
- Performance and Space Requirements
- Concurrency Control

ALTER TABLE Statement

- Adding and Dropping Columns
- Renaming, Redefining, and Reordering Columns
- Primary Keys and Indexes
- Foreign Keys and Other Constraints
- Changing the Character Set
- Discarding and Importing InnoDB Tablespaces
- Row Order for MyISAM Tables
- Partitioning Options

> Table Options

`table_options` signifies table options of the kind that can be used in the `CREATE TABLE` statement,

```
such as ENGINE, AUTO_INCREMENT, AVG_ROW_LENGTH, MAX_ROWS, or ROW_FORMAT.
```

For descriptions of all table options, see Section 13.1.17, “CREATE TABLE Statement”. However, `ALTER``TABLE` ignores `DATA DIRECTORY` and `INDEX DIRECTORY` when given as table options. `ALTER TABLE`permits them only as partitioning options, and, as of MySQL 5.6.35, requires that you have the `FILE`privilege.

Use of table options with `ALTER TABLE` provides a convenient way of altering single table characteristics.

For example:

- If `t1` is currently not an `InnoDB` table, this statement changes its storage engine to `InnoDB`:

```
ALTER TABLE t1 ENGINE = InnoDB;
```

- See Section 14.6.1.5, “Converting Tables from MyISAM to InnoDB” for considerations when switching

tables to the `InnoDB` storage engine.

- When you specify an `ENGINE` clause, `ALTER TABLE` rebuilds the table. This is true even if the table

already has the specified storage engine.

- Running `ALTER TABLE tbl_name ENGINE=INNODB` on an existing `InnoDB` table performs a

“null” `ALTER TABLE` operation, which can be used to defragment an `InnoDB` table, as described in Section 14.12.4, “Defragmenting a Table”. Running `ALTER TABLE tbl_name FORCE` on an `InnoDB`table performs the same function.

- As of MySQL 5.6.17, `ALTER TABLE tbl_name ENGINE=INNODB` and `ALTER TABLE tbl_name`

`FORCE` use online DDL. For more information, see Section 14.13, “InnoDB and Online DDL”.

- The outcome of attempting to change the storage engine of a table is affected by whether the desired

storage engine is available and the setting of the `NO_ENGINE_SUBSTITUTION` SQL mode, as described in Section 5.1.10, “Server SQL Modes”.

- To prevent inadvertent loss of data, `ALTER TABLE` cannot be used to change the storage engine of a

table to `MERGE` or `BLACKHOLE`.

- To change the `InnoDB` table to use compressed row-storage format:

```
ALTER TABLE t1 ROW_FORMAT = COMPRESSED;
```

- To reset the current auto-increment value:

ALTER TABLE Statement

```
ALTER TABLE t1 AUTO_INCREMENT = 13;
```

You cannot reset the counter to a value less than or equal to the value that is currently in use. For both `InnoDB` and `MyISAM`, if the value is less than or equal to the maximum value currently in the`AUTO_INCREMENT` column, the value is reset to the current maximum `AUTO_INCREMENT` column value plus one.

- To change the default table character set:

```
ALTER TABLE t1 CHARACTER SET = utf8;
```

See also Changing the Character Set.

- To add (or change) a table comment:

```
ALTER TABLE t1 COMMENT = 'New table comment';
```

It is also possible to set `NDB_COMMENT` options for columns of `NDB` tables as part of an `ALTER TABLE`statement, like this one:

```
ALTER TABLE t1
CHANGE COLUMN c1 c1 BLOB
COMMENT = 'NDB_COLUMN=MAX_BLOB_PART_SIZE';
```

Bear in mind that `ALTER TABLE ... COMMENT ...` discards any existing comment for the table. See Setting NDB_TABLE options, for additional information and examples.

To verify that the table options were changed as intended, use `SHOW CREATE TABLE`, or query the Information Schema `TABLES` table.

> Performance and Space Requirements

`ALTER TABLE` operations are processed using one of the following algorithms:

- `COPY`: Operations are performed on a copy of the original table, and table data is copied from the original

table to the new table row by row. Concurrent DML is not permitted.

- `INPLACE`: Operations avoid copying table data but may rebuild the table in place. An exclusive metadata

lock on the table may be taken briefly during preparation and execution phases of the operation.

Typically, concurrent DML is supported.

For tables using the `NDB` storage engine, these algorithms work as follows:

- `COPY`: `NDB` creates a copy of the table and alters it; the NDB Cluster handler then copies the data

between the old and new versions of the table. Subsequently, `NDB` deletes the old table and renames the new one.

This is sometimes also referred to as a “copying” or “offline” `ALTER TABLE`.

- `INPLACE`: The data nodes make the required changes; the NDB Cluster handler does not copy data or

otherwise take part.

This is sometimes also referred to as a “non-copying” or “online” `ALTER TABLE`.

See Section 18.6.12, “Online Operations with ALTER TABLE in NDB Cluster”, for more information.

The `ALGORITHM` clause is optional. If the `ALGORITHM` clause is omitted (or if you specify`ALGORITHM=DEFAULT`), MySQL uses `ALGORITHM=INPLACE` for storage engines and `ALTER TABLE`clauses that support it. Otherwise, `ALGORITHM=COPY` is used.

ALTER TABLE Statement Note

```
ALGORITHM=DEFAULT, ALGORITHM=INPLACE, and ALGORITHM=COPY are not
```

supported for `ALTER TABLE` operations on partitioned tables. MySQL 5.6.11 and later supports `ALGORITHM=1` and `ALGORITHM=2` for use with upgrades and downgrades; see Section 13.1.7.1, “ALTER TABLE Partition Operations”, for more information.

Specifying an `ALGORITHM` clause requires the operation to use the specified algorithm for clauses and storage engines that support it, or fail with an error otherwise. Specifying `ALGORITHM=DEFAULT` is the same as omitting the `ALGORITHM` clause.

`ALTER TABLE` operations that use the `COPY` algorithm wait for other operations that are modifying the table to complete. After alterations are applied to the table copy, data is copied over, the original table is deleted, and the table copy is renamed to the name of the original table. While the `ALTER TABLE`operation executes, the original table is readable by other sessions (with the exception noted shortly).

Updates and writes to the table started after the `ALTER TABLE` operation begins are stalled until the new table is ready, then are automatically redirected to the new table. The temporary copy of the table is created in the database directory of the original table unless it is a `RENAME TO` operation that moves the table to a database that resides in a different directory.

The exception referred to earlier is that `ALTER TABLE` blocks reads (not just writes) at the point where it is ready to install a new version of the table `.frm` file, discard the old file, and clear outdated table structures from the table and table definition caches. At this point, it must acquire an exclusive lock. To do so, it waits for current readers to finish, and blocks new reads and writes.

An `ALTER TABLE` operation that uses the `COPY` algorithm prevents concurrent DML operations.

Concurrent queries are still allowed. That is, a table-copying operation always includes at least the concurrency restrictions of `LOCK=SHARED` (allow queries but not DML). You can further restrict concurrency for operations that support the `LOCK` clause by specifying `LOCK=EXCLUSIVE`, which prevents DML and queries. For more information, see Concurrency Control.

Note In MySQL 5.6, `LOCK` is not supported for `ALTER TABLE` operations on partitioned tables.

To force use of the `COPY` algorithm for an `ALTER TABLE` operation that would otherwise not use it, enable the `old_alter_table` system variable or specify `ALGORITHM=COPY`. If there is a conflict between the`old_alter_table` setting and an `ALGORITHM` clause with a value other than `DEFAULT`, the `ALGORITHM`clause takes precedence.

For `InnoDB` tables, an `ALTER TABLE` operation that uses the `COPY` algorithm on a table that resides in a shared tablespace such as the system tablespace can increase the amount of space used by the tablespace. Such operations require as much additional space as the data in the table plus indexes. For a table residing in a shared tablespace, the additional space used during the operation is not released back to the operating system as it is for a table that resides in a file-per-table tablespace.

For information about space requirements for online DDL operations, see Section 14.13.3, “Online DDL Space Requirements”.

`ALTER TABLE` operations that support the `INPLACE` algorithm include:

- `ALTER TABLE` operations supported by the `InnoDB` online DDL feature. See Section 14.13.1, “Online

DDL Operations”.

ALTER TABLE Statement

- Renaming a table. MySQL renames files that correspond to the table `tbl_name` without making a copy.

(You can also use the `RENAME TABLE` statement to rename tables. See Section 13.1.32, “RENAME TABLE Statement”.) Privileges granted specifically for the renamed table are not migrated to the new name. They must be changed manually.

- Operations that only modify table metadata. These operations are immediate because the server only

alters the table `.frm` file, not touch table contents. Metadata-only operations include:

- Renaming a column.
- Changing the default value of a column (except for `NDB` tables; see Limitations of NDB online

operations).

- Modifying the definition of an `ENUM` or `SET` column by adding new enumeration or set members to the

end of the list of valid member values, as long as the storage size of the data type does not change.

For example, adding a member to a `SET` column that has 8 members changes the required storage per value from 1 byte to 2 bytes; this requires a table copy. Adding members in the middle of the list causes renumbering of existing members, which requires a table copy.

- Adding or dropping a secondary index, for `InnoDB` and `NDB` tables. See Section 14.13, “InnoDB and

Online DDL”.

- For `NDB` tables, operations that add and drop indexes on variable-width columns. These operations

occur online, without table copying and without blocking concurrent DML actions for most of their duration. See Section 18.6.12, “Online Operations with ALTER TABLE in NDB Cluster”.

As of MySQL 5.6.16, `ALTER TABLE` upgrades MySQL 5.5 temporal columns to 5.6 format for `ADD``COLUMN`, `CHANGE COLUMN`, `MODIFY COLUMN`, `ADD INDEX`, and `FORCE` operations. This conversion cannot be done using the `INPLACE` algorithm because the table must be rebuilt, so specifying`ALGORITHM=INPLACE` in these cases results in an error. Specify `ALGORITHM=COPY` if necessary.

NDB Cluster supports online `ALTER TABLE` operations using the `ALGORITHM=INPLACE` syntax in MySQL NDB Cluster 7.3 and later. NDB Cluster also supports an older syntax specific to NDB that uses the`ONLINE` and `OFFLINE` keywords. These keywords are deprecated beginning with MySQL NDB Cluster

7.3; they continue to be supported in MySQL NDB Cluster 7.4, but are subject to removal in a future version of NDB Cluster. See Section 18.6.12, “Online Operations with ALTER TABLE in NDB Cluster”, for the exact syntax and other particulars.

If an `ALTER TABLE` operation on a multicolumn index used to partition a table by `KEY` changes the order of the columns, it can only be performed using `ALGORITHM=COPY`.

MySQL NDB Cluster 7.3 (and later) supports online operations using the same `ALGORITHM=INPLACE`syntax used with the standard MySQL Server. NDB Cluster 7.3 and 7.4 also continue to support online`ALTER TABLE` operations using the `ONLINE` and `OFFLINE` keywords for backwards compatibility, but these keywords are deprecated in NDB 7.3 and 7.4, and no longer supported as of NDB 7.5. `NDB` does not support changing a tablespace online. See Section 18.6.12, “Online Operations with ALTER TABLE in NDB Cluster”, for more information.

```
ALTER TABLE with ADD PARTITION, DROP PARTITION, COALESCE PARTITION, REBUILD
```

`PARTITION`, or `REORGANIZE PARTITION` does not create temporary tables (except when used with `NDB`tables); however, these operations can and do create temporary partition files.

`ADD` or `DROP` operations for `RANGE` or `LIST` partitions are immediate operations or nearly so. `ADD` or`COALESCE` operations for `HASH` or `KEY` partitions copy data between all partitions, unless `LINEAR HASH`or `LINEAR KEY` was used; this is effectively the same as creating a new table, although the `ADD` or`COALESCE` operation is performed partition by partition. `REORGANIZE` operations copy only changed partitions and do not touch unchanged ones.

ALTER TABLE Statement For `MyISAM` tables, you can speed up index re-creation (the slowest part of the alteration process) by setting the `myisam_sort_buffer_size` system variable to a high value.

> Concurrency Control

For `ALTER TABLE` operations that support it, you can use the `LOCK` clause to control the level of concurrent reads and writes on a table while it is being altered. Specifying a non-default value for this clause enables you to require a certain amount of concurrent access or exclusivity during the alter operation, and halts the operation if the requested degree of locking is not available. The parameters for the `LOCK` clause are:

```
- LOCK = DEFAULT
```

Maximum level of concurrency for the given `ALGORITHM` clause (if any) and `ALTER TABLE` operation:Permit concurrent reads and writes if supported. If not, permit concurrent reads if supported. If not,enforce exclusive access.

```
- LOCK = NONE
```

If supported, permit concurrent reads and writes. Otherwise, an error occurs.

```
- LOCK = SHARED
```

If supported, permit concurrent reads but block writes. Writes are blocked even if concurrent writes are supported by the storage engine for the given `ALGORITHM` clause (if any) and `ALTER TABLE` operation.

If concurrent reads are not supported, an error occurs.

```
- LOCK = EXCLUSIVE
```

Enforce exclusive access. This is done even if concurrent reads/writes are supported by the storage engine for the given `ALGORITHM` clause (if any) and `ALTER TABLE` operation.

Note Pending `INSERT DELAYED` statements are lost if a table is write locked and `ALTER``TABLE` is used to modify the table structure.

> Adding and Dropping Columns

Use `ADD` to add new columns to a table, and `DROP` to remove existing columns. `DROP col_name` is a MySQL extension to standard SQL.

To add a column at a specific position within a table row, use `FIRST` or `AFTER col_name`. The default is to add the column last.

If a table contains only one column, the column cannot be dropped. If what you intend is to remove the table, use the `DROP TABLE` statement instead.

If columns are dropped from a table, the columns are also removed from any index of which they are a part. If all columns that make up an index are dropped, the index is dropped as well.

> Renaming, Redefining, and Reordering Columns

The `CHANGE`, `MODIFY`, and `ALTER` clauses enable the names and definitions of existing columns to be altered. They have these comparative characteristics:

```
- CHANGE:
```

- Can rename a column and change its definition, or both.

ALTER TABLE Statement

- Has more capability than `MODIFY`, but at the expense of convenience for some operations. `CHANGE`

requires naming the column twice if not renaming it.

- With `FIRST` or `AFTER`, can reorder columns.

```
- MODIFY:
```

- Can change a column definition but not its name.
- More convenient than `CHANGE` to change a column definition without renaming it.
- With `FIRST` or `AFTER`, can reorder columns.
- `ALTER`: Used only to change a column default value.

`CHANGE` is a MySQL extension to standard SQL. `MODIFY` is a MySQL extension for Oracle compatibility.

To alter a column to change both its name and definition, use `CHANGE`, specifying the old and new names and the new definition. For example, to rename an `INT NOT NULL` column from a to b and change its definition to use the `BIGINT` data type while retaining the `NOT NULL` attribute, do this:

```
ALTER TABLE t1 CHANGE a b BIGINT NOT NULL;
```

To change a column definition but not its name, use `CHANGE` or `MODIFY`. With `CHANGE`, the syntax requires two column names, so you must specify the same name twice to leave the name unchanged. For example,to change the definition of column b, do this:

```
ALTER TABLE t1 CHANGE b b INT NOT NULL;
```

`MODIFY` is more convenient to change the definition without changing the name because it requires the column name only once:

```
ALTER TABLE t1 MODIFY b INT NOT NULL;
```

To change a column name but not its definition, use `CHANGE`. The syntax requires a column definition, so to leave the definition unchanged, you must respecify the definition the column currently has. For example,to rename an `INT NOT NULL` column from b to a, do this:

```
ALTER TABLE t1 CHANGE b a INT NOT NULL;
```

For column definition changes using `CHANGE` or `MODIFY`, the definition must include the data type and all attributes that should apply to the new column, other than index attributes such as `PRIMARY KEY`or `UNIQUE`. Attributes present in the original definition but not specified for the new definition are not carried forward. Suppose that a column `col1` is defined as `INT UNSIGNED DEFAULT 1 COMMENT 'my``column'` and you modify the column as follows, intending to change only `INT` to `BIGINT`:

```
ALTER TABLE t1 MODIFY col1 BIGINT;
```

That statement changes the data type from `INT` to `BIGINT`, but it also drops the `UNSIGNED`, `DEFAULT`,and `COMMENT` attributes. To retain them, the statement must include them explicitly:

```
ALTER TABLE t1 MODIFY col1 BIGINT UNSIGNED DEFAULT 1 COMMENT 'my column';
```

For data type changes using `CHANGE` or `MODIFY`, MySQL tries to convert existing column values to the new type as well as possible.

Warning This conversion may result in alteration of data. For example, if you shorten a string column, values may be truncated. To prevent the operation from succeeding if ALTER TABLE Statement conversions to the new data type would result in loss of data, enable strict SQL mode before using `ALTER TABLE` (see Section 5.1.10, “Server SQL Modes”).

If you use `CHANGE` or `MODIFY` to shorten a column for which an index exists on the column, and the resulting column length is less than the index length, MySQL shortens the index automatically.

For columns renamed by `CHANGE`, MySQL automatically renames these references to the renamed column:

- Indexes that refer to the old column, including indexes and disabled `MyISAM` indexes.
- Foreign keys that refer to the old column.

For columns renamed by `CHANGE`, MySQL does not automatically rename these references to the renamed column:

- Partition expressions that refer to the renamed column. You must use `CHANGE` to redefine such

expressions in the same `ALTER TABLE` statement as the one that renames the column.

- Views and stored programs that refer to the renamed column. You must manually alter the definition of

these objects to refer to the new column name.

To reorder columns within a table, use `FIRST` and `AFTER` in `CHANGE` or `MODIFY` operations.

`ALTER ... SET DEFAULT` or `ALTER ... DROP DEFAULT` specify a new default value for a column or remove the old default value, respectively. If the old default is removed and the column can be `NULL`,the new default is `NULL`. If the column cannot be `NULL`, MySQL assigns a default value as described in Section 11.5, “Data Type Default Values”.

> Primary Keys and Indexes

`DROP PRIMARY KEY` drops the primary key. If there is no primary key, an error occurs. For information about the performance characteristics of primary keys, especially for `InnoDB` tables, see Section 8.3.2,“Primary Key Optimization”.

If you add a `UNIQUE INDEX` or `PRIMARY KEY` to a table, MySQL stores it before any nonunique index to permit detection of duplicate keys as early as possible.

`IGNORE` is a MySQL extension to standard SQL. It controls how `ALTER TABLE` works if there are duplicates on unique keys in the new table or if warnings occur when strict mode is enabled. If `IGNORE` is not specified, the copy is aborted and rolled back if duplicate-key errors occur. If `IGNORE` is specified, only one row is used of rows with duplicates on a unique key. The other conflicting rows are deleted. Incorrect values are truncated to the closest matching acceptable value.

As of MySQL 5.6.17, the `IGNORE` clause is deprecated and its use generates a warning. `IGNORE` is removed in MySQL 5.7.

`DROP INDEX` removes an index. This is a MySQL extension to standard SQL. See Section 13.1.24,“DROP INDEX Statement”. To determine index names, use `SHOW INDEX FROM tbl_name`.

Some storage engines permit you to specify an index type when creating an index. The syntax for the`index_type` specifier is `USING type_name`. For details about `USING`, see Section 13.1.13, “CREATE INDEX Statement”. The preferred position is after the column list. Expect support for use of the option before the column list to be removed in a future MySQL release.

`index_option` values specify additional options for an index. For details about permissible`index_option` values, see Section 13.1.13, “CREATE INDEX Statement”.

ALTER TABLE Statement If you use `ALTER TABLE` on a `MyISAM` table, all nonunique indexes are created in a separate batch (as for`REPAIR TABLE`). This should make `ALTER TABLE` much faster when you have many indexes.

For `MyISAM` tables, key updating can be controlled explicitly. Use `ALTER TABLE ... DISABLE KEYS`to tell MySQL to stop updating nonunique indexes. Then use `ALTER TABLE ... ENABLE KEYS` to re-create missing indexes. `MyISAM` does this with a special algorithm that is much faster than inserting keys one by one, so disabling keys before performing bulk insert operations should give a considerable speedup. Using `ALTER TABLE ... DISABLE KEYS` requires the `INDEX` privilege in addition to the privileges mentioned earlier.

While the nonunique indexes are disabled, they are ignored for statements such as `SELECT` and `EXPLAIN`that otherwise would use them.

After an `ALTER TABLE` statement, it may be necessary to run `ANALYZE TABLE` to update index cardinality information. See Section 13.7.5.23, “SHOW INDEX Statement”.

> Foreign Keys and Other Constraints

The `FOREIGN KEY` and `REFERENCES` clauses are supported by the `InnoDB` and `NDB` storage engines, which implement `ADD [CONSTRAINT [symbol]] FOREIGN KEY [index_name] (...)``REFERENCES ... (...)`. See Section 13.1.17.5, “FOREIGN KEY Constraints”. For other storage engines, the clauses are parsed but ignored.

The `CHECK` constraint clause is parsed but ignored by all storage engines. See Section 13.1.17, “CREATE TABLE Statement”. The reason for accepting but ignoring syntax clauses is for compatibility, to make it easier to port code from other SQL servers, and to run applications that create tables with references. See Section 1.6.2, “MySQL Differences from Standard SQL”.

For `ALTER TABLE`, unlike `CREATE TABLE`, `ADD FOREIGN KEY` ignores `index_name` if given and uses an automatically generated foreign key name. As a workaround, include the `CONSTRAINT` clause to specify the foreign key name:

```
ADD CONSTRAINT name FOREIGN KEY (....) ...
```

Important MySQL silently ignores inline `REFERENCES` specifications, where the references are defined as part of the column specification. MySQL accepts only `REFERENCES`clauses defined as part of a separate `FOREIGN KEY` specification.

Note Partitioned `InnoDB` tables do not support foreign keys. This restriction does not apply to `NDB` tables, including those explicitly partitioned by `[LINEAR] KEY`. For more information, see Section 19.6.2, “Partitioning Limitations Relating to Storage Engines”.

The `InnoDB` and `NDB` storage engines support the use of `ALTER TABLE` to drop foreign keys:

```
ALTER TABLE tbl_name DROP FOREIGN KEY fk_symbol;
```

Adding and dropping a foreign key in the same `ALTER TABLE` statement is supported for `ALTER`

```
TABLE ... ALGORITHM=INPLACE but not for ALTER TABLE ... ALGORITHM=COPY.
```

The server prohibits changes to foreign key columns that have the potential to cause loss of referential integrity. A workaround is to use `ALTER TABLE ... DROP FOREIGN KEY` before changing the column definition and `ALTER TABLE ... ADD FOREIGN KEY` afterward. Examples of prohibited changes include:ALTER TABLE Statement

- Changes to the data type of foreign key columns that may be unsafe. For example, changing

`VARCHAR(20)` to `VARCHAR(30)` is permitted, but changing it to `VARCHAR(1024)` is not because that alters the number of length bytes required to store individual values.

- Changing a `NULL` column to `NOT NULL` in non-strict mode is prohibited to prevent converting `NULL`

values to default non-`NULL` values, for which there are no corresponding values in the referenced table.

The operation is permitted in strict mode, but an error is returned if any such conversion is required.

`ALTER TABLE tbl_name RENAME new_tbl_name` changes internally generated foreign key constraint names and user-defined foreign key constraint names that begin with the string “`tbl_name`_ibfk_” to reflect the new table name. `InnoDB` interprets foreign key constraint names that begin with the string“`tbl_name`_ibfk_” as internally generated names.

> Changing the Character Set

To change the table default character set and all character columns (`CHAR`, `VARCHAR`, `TEXT`) to a new character set, use a statement like this:

```
ALTER TABLE tbl_name
CONVERT TO CHARACTER SET charset_name [COLLATE collation_name];
```

The statement also changes the collation of all character columns. If you specify no `COLLATE` clause to indicate which collation to use, the statement uses default collation for the character set. If this collation is inappropriate for the intended table use (for example, if it would change from a case-sensitive collation to a case-insensitive collation), specify a collation explicitly.

For a column that has a data type of `VARCHAR` or one of the `TEXT` types, `CONVERT TO CHARACTER``SET` changes the data type as necessary to ensure that the new column is long enough to store as many characters as the original column. For example, a `TEXT` column has two length bytes, which store the byte-length of values in the column, up to a maximum of 65,535. For a `latin1` `TEXT` column, each character requires a single byte, so the column can store up to 65,535 characters. If the column is converted to`utf8`, each character might require up to three bytes, for a maximum possible length of 3 × 65,535 =196,605 bytes. That length does not fit in a `TEXT` column's length bytes, so MySQL converts the data type to `MEDIUMTEXT`, which is the smallest string type for which the length bytes can record a value of 196,605.

Similarly, a `VARCHAR` column might be converted to `MEDIUMTEXT`.

To avoid data type changes of the type just described, do not use `CONVERT TO CHARACTER SET`.

Instead, use `MODIFY` to change individual columns. For example:

```
ALTER TABLE t MODIFY latin1_text_col TEXT CHARACTER SET utf8;
ALTER TABLE t MODIFY latin1_varchar_col VARCHAR(M) CHARACTER SET utf8;
```

If you specify `CONVERT TO CHARACTER SET binary`, the `CHAR`, `VARCHAR`, and `TEXT` columns are converted to their corresponding binary string types (`BINARY`, `VARBINARY`, `BLOB`). This means that the columns no longer have a character set and a subsequent `CONVERT TO` operation does not apply to them.

If `charset_name` is `DEFAULT` in a `CONVERT TO CHARACTER SET` operation, the character set named by the `character_set_database` system variable is used.

Warning The `CONVERT TO` operation converts column values between the original and named character sets. This is not what you want if you have a column in one character set (like `latin1`) but the stored values actually use some other,incompatible character set (like `utf8`). In this case, you have to do the following for each such column:

```
ALTER TABLE t1 CHANGE c1 c1 BLOB;
```

ALTER TABLE Statement

```
ALTER TABLE t1 CHANGE c1 c1 TEXT CHARACTER SET utf8;
```

The reason this works is that there is no conversion when you convert to or from`BLOB` columns.

To change only the default character set for a table, use this statement:

```
ALTER TABLE tbl_name DEFAULT CHARACTER SET charset_name;
```

The word `DEFAULT` is optional. The default character set is the character set that is used if you do not specify the character set for columns that you add to a table later (for example, with `ALTER TABLE ...`

```
ADD column).
```

When the `foreign_key_checks` system variable is enabled, which is the default setting, character set conversion is not permitted on tables that include a character string column used in a foreign key constraint. The workaround is to disable `foreign_key_checks` before performing the character set conversion. You must perform the conversion on both tables involved in the foreign key constraint before re-enabling `foreign_key_checks`. If you re-enable `foreign_key_checks` after converting only one of the tables, an `ON DELETE CASCADE` or `ON UPDATE CASCADE` operation could corrupt data in the referencing table due to implicit conversion that occurs during these operations (Bug #45290, Bug#74816).

> Discarding and Importing InnoDB Tablespaces

An `InnoDB` table created in its own file-per-table tablespace can be imported from a backup or from another MySQL server instance using the `DISCARD TABLEPACE` and `IMPORT TABLESPACE` clauses. See Section 14.6.1.3, “Importing InnoDB Tables”.

> Row Order for MyISAM Tables

`ORDER BY` enables you to create the new table with the rows in a specific order. This option is useful primarily when you know that you query the rows in a certain order most of the time. By using this option after major changes to the table, you might be able to get higher performance. In some cases, it might make sorting easier for MySQL if the table is in order by the column that you want to order it by later.

Note The table does not remain in the specified order after inserts and deletes.

`ORDER BY` syntax permits one or more column names to be specified for sorting, each of which optionally can be followed by `ASC` or `DESC` to indicate ascending or descending sort order, respectively. The default is ascending order. Only column names are permitted as sort criteria; arbitrary expressions are not permitted.

This clause should be given last after any other clauses.

`ORDER BY` does not make sense for `InnoDB` tables because `InnoDB` always orders table rows according to the clustered index.

When used on a partitioned table, `ALTER TABLE ... ORDER BY` orders rows within each partition only.

> Partitioning Options

`partition_options` signifies options that can be used with partitioned tables for repartitioning, to add,drop, discard, merge, and split partitions, and to perform partitioning maintenance.

It is possible for an `ALTER TABLE` statement to contain a `PARTITION BY` or `REMOVE PARTITIONING`clause in an addition to other alter specifications, but the `PARTITION BY` or `REMOVE PARTITIONING`clause must be specified last after any other specifications. The `ADD PARTITION`, `DROP PARTITION`,

```
COALESCE PARTITION, REORGANIZE PARTITION, EXCHANGE PARTITION, ANALYZE PARTITION,
```

ALTER TABLE Statement`CHECK PARTITION`, and `REPAIR PARTITION` options cannot be combined with other alter specifications in a single `ALTER TABLE`, since the options just listed act on individual partitions.

For more information about partition options, see Section 13.1.17, “CREATE TABLE Statement”, and Section 13.1.7.1, “ALTER TABLE Partition Operations”. For information about and examples of `ALTER``TABLE ... EXCHANGE PARTITION` statements, see Section 19.3.3, “Exchanging Partitions and Subpartitions with Tables”.

#### 13.1.7.1 ALTER TABLE Partition Operations

Partitioning-related clauses for `ALTER TABLE` can be used with partitioned tables for repartitioning, to add,drop, discard, merge, and split partitions, and to perform partitioning maintenance.

- Simply using a `partition_options` clause with `ALTER TABLE` on a partitioned table repartitions

the table according to the partitioning scheme defined by the `partition_options`. This clause always begins with `PARTITION BY`, and follows the same syntax and other rules as apply to the`partition_options` clause for `CREATE TABLE` (for more detailed information, see Section 13.1.17,“CREATE TABLE Statement”), and can also be used to partition an existing table that is not already partitioned. For example, consider a (nonpartitioned) table defined as shown here:

```
CREATE TABLE t1 (
id INT,
year_col INT
);
```

This table can be partitioned by `HASH`, using the `id` column as the partitioning key, into 8 partitions by means of this statement:

```
ALTER TABLE t1
PARTITION BY HASH(id)
PARTITIONS 8;
```

MySQL 5.6.11 and later supports an `ALGORITHM` option with `[SUB]PARTITION BY [LINEAR] KEY`.

`ALGORITHM=1` causes the server to use the same key-hashing functions as MySQL 5.1 when computing the placement of rows in partitions; `ALGORITHM=2` means that the server employs the key-hashing functions implemented and used by default for new `KEY` partitioned tables in MySQL 5.5 and later.

(Partitioned tables created with the key-hashing functions employed in MySQL 5.5 and later cannot be used by a MySQL 5.1 server.) Not specifying the option has the same effect as using `ALGORITHM=2`.

This option is intended for use chiefly when upgrading or downgrading `[LINEAR] KEY` partitioned tables between MySQL 5.1 and later MySQL versions, or for creating tables partitioned by `KEY` or `LINEAR KEY`on a MySQL 5.5 or later server which can be used on a MySQL 5.1 server.

To upgrade a `KEY` partitioned table that was created in MySQL 5.1, first execute `SHOW CREATE TABLE`and note the exact columns and number of partitions shown. Now execute an `ALTER TABLE` statement using exactly the same column list and number of partitions as in the `CREATE TABLE` statement, while adding `ALGORITHM=2` immediately following the `PARTITION BY` keywords. (You should also include the `LINEAR` keyword if it was used for the original table definition.) An example from a session in the`mysql` client is shown here:

```
mysql> SHOW CREATE TABLE p\G
*************************** 1. row ***************************
Table: p
Create Table: CREATE TABLE `p` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`cd` datetime NOT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
/*!50100 PARTITION BY LINEAR KEY (id)
PARTITIONS 32 */
```

ALTER TABLE Statement

```
1 row in set (0.00 sec)
mysql> ALTER TABLE p PARTITION BY LINEAR KEY ALGORITHM=2 (id) PARTITIONS 32;
Query OK, 0 rows affected (5.34 sec)
Records: 0  Duplicates: 0  Warnings: 0
mysql> SHOW CREATE TABLE p\G
*************************** 1. row ***************************
Table: p
Create Table: CREATE TABLE `p` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`cd` datetime NOT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
/*!50100 PARTITION BY LINEAR KEY (id)
PARTITIONS 32 */
1 row in set (0.00 sec)
```

Downgrading a table created using the default key-hashing used in MySQL 5.5 and later to enable its use by a MySQL 5.1 server is similar, except in this case you should use `ALGORITHM=1` to force the table's partitions to be rebuilt using the MySQL 5.1 key-hashing functions. It is recommended that you not do this except when necessary for compatibility with a MySQL 5.1 server, as the improved `KEY`hashing functions used by default in MySQL 5.5 and later provide fixes for a number of issues found in the older implementation.

Note A table upgraded by means of `ALTER TABLE ... PARTITION BY``ALGORITHM=2 [LINEAR] KEY ...` can no longer be used by a MySQL 5.1 server. (Such a table would need to be downgraded with `ALTER TABLE ...``PARTITION BY ALGORITHM=1 [LINEAR] KEY ...` before it could be used again by a MySQL 5.1 server.)The table that results from using an `ALTER TABLE ... PARTITION BY` statement must follow the same rules as one created using `CREATE TABLE ... PARTITION BY`. This includes the rules governing the relationship between any unique keys (including any primary key) that the table might have, and the column or columns used in the partitioning expression, as discussed in Section 19.6.1,“Partitioning Keys, Primary Keys, and Unique Keys”. The `CREATE TABLE ... PARTITION BY` rules for specifying the number of partitions also apply to `ALTER TABLE ... PARTITION BY`.

The `partition_definition` clause for `ALTER TABLE ADD PARTITION` supports the same options as the clause of the same name for the `CREATE TABLE` statement. (See Section 13.1.17, “CREATE TABLE Statement”, for the syntax and description.) Suppose that you have the partitioned table created as shown here:

```
CREATE TABLE t1 (
id INT,
year_col INT
)
PARTITION BY RANGE (year_col) (
PARTITION p0 VALUES LESS THAN (1991),
PARTITION p1 VALUES LESS THAN (1995),
PARTITION p2 VALUES LESS THAN (1999)
```

ALTER TABLE Statement

```
);
```

You can add a new partition `p3` to this table for storing values less than 2002 as follows:

```
ALTER TABLE t1 ADD PARTITION (PARTITION p3 VALUES LESS THAN (2002));
```

`DROP PARTITION` can be used to drop one or more `RANGE` or `LIST` partitions. This statement cannot be used with `HASH` or `KEY` partitions; instead, use `COALESCE PARTITION` (see below). Any data that was stored in the dropped partitions named in the `partition_names` list is discarded. For example,given the table `t1` defined previously, you can drop the partitions named `p0` and `p1` as shown here:

```
ALTER TABLE t1 DROP PARTITION p0, p1;
```

Note`DROP PARTITION` does not work with tables that use the `NDB` storage engine.

See Section 19.3.1, “Management of RANGE and LIST Partitions”, and Section 18.2.7, “Known Limitations of NDB Cluster”.

`ADD PARTITION` and `DROP PARTITION` do not currently support `IF [NOT] EXISTS`.

Renames of partitioned tables are supported. You can rename individual partitions indirectly using`ALTER TABLE ... REORGANIZE PARTITION`; however, this operation copies the partition's data.

To delete rows from selected partitions, use the `TRUNCATE PARTITION` option. This option takes a list of one or more comma-separated partition names. For example, consider the table `t1` as defined here:

```
CREATE TABLE t1 (
id INT,
year_col INT
)
PARTITION BY RANGE (year_col) (
PARTITION p0 VALUES LESS THAN (1991),
PARTITION p1 VALUES LESS THAN (1995),
PARTITION p2 VALUES LESS THAN (1999),
PARTITION p3 VALUES LESS THAN (2003),
PARTITION p4 VALUES LESS THAN (2007)
);
```

To delete all rows from partition `p0`, use the following statement:

```
ALTER TABLE t1 TRUNCATE PARTITION p0;
```

The statement just shown has the same effect as the following `DELETE` statement:

```
DELETE FROM t1 WHERE year_col < 1991;
```

When truncating multiple partitions, the partitions do not have to be contiguous: This can greatly simplify delete operations on partitioned tables that would otherwise require very complex `WHERE` conditions if done with `DELETE` statements. For example, this statement deletes all rows from partitions `p1` and `p3`:

```
ALTER TABLE t1 TRUNCATE PARTITION p1, p3;
```

An equivalent `DELETE` statement is shown here:

```
DELETE FROM t1 WHERE
(year_col >= 1991 AND year_col < 1995)
OR
```

ALTER TABLE Statement

```
(year_col >= 2003 AND year_col < 2007);
```

If you use the `ALL` keyword in place of the list of partition names, the statement acts on all table partitions.

`TRUNCATE PARTITION` merely deletes rows; it does not alter the definition of the table itself, or of any of its partitions.

Note`TRUNCATE PARTITION` does not work with subpartitions.

To verify that the rows were dropped, check the `INFORMATION_SCHEMA.PARTITIONS` table, using a query such as this one:

```
SELECT PARTITION_NAME, TABLE_ROWS
FROM INFORMATION_SCHEMA.PARTITIONS
WHERE TABLE_NAME = 't1';
```

`TRUNCATE PARTITION` is supported only for partitioned tables that use the `MyISAM`, `InnoDB`, or`MEMORY` storage engine. It also works on `BLACKHOLE` tables (but has no effect). It is not supported for`ARCHIVE` tables.

`COALESCE PARTITION` can be used with a table that is partitioned by `HASH` or `KEY` to reduce the number of partitions by `number`. Suppose that you have created table `t2` as follows:

```
CREATE TABLE t2 (
name VARCHAR (30),
started DATE
)
PARTITION BY HASH( YEAR(started) )
PARTITIONS 6;
```

To reduce the number of partitions used by `t2` from 6 to 4, use the following statement:

```
ALTER TABLE t2 COALESCE PARTITION 2;
```

The data contained in the last `number` partitions is merged into the remaining partitions. In this case,partitions 4 and 5 are merged into the first 4 partitions (the partitions numbered 0, 1, 2, and 3).

To change some but not all the partitions used by a partitioned table, you can use `REORGANIZE``PARTITION`. This statement can be used in several ways:

- To merge a set of partitions into a single partition. This is done by naming several partitions in the

`partition_names` list and supplying a single definition for `partition_definition`.

- To split an existing partition into several partitions. Accomplish this by naming a single partition for

`partition_names` and providing multiple `partition_definitions`.

- To change the ranges for a subset of partitions defined using `VALUES LESS THAN` or the value lists

for a subset of partitions defined using `VALUES IN`.

- This statement may also be used without the `partition_names INTO`

`(partition_definitions)` option on tables that are automatically partitioned using `HASH`partitioning to force redistribution of data. (Currently, only `NDB` tables are automatically partitioned in this way.) This is useful in NDB Cluster where, after you have added new NDB Cluster data nodes online to an existing NDB Cluster, you wish to redistribute existing NDB Cluster table data to the new ALTER TABLE Statement data nodes. In such cases, you should invoke the statement with the `ONLINE` option; in other words,as shown here:

```
ALTER ONLINE TABLE table REORGANIZE PARTITION;
```

You cannot perform other DDL concurrently with online table reorganization—that is, no other DDL statements can be issued while an `ALTER ONLINE TABLE ... REORGANIZE PARTITION`statement is executing. For more information about adding NDB Cluster data nodes online, see Section 18.6.7, “Adding NDB Cluster Data Nodes Online”.

`ALTER ONLINE TABLE ... REORGANIZE PARTITION` does not work with tables which were created using the `MAX_ROWS` option, because it uses the constant `MAX_ROWS` value specified in the original `CREATE TABLE` statement to determine the number of partitions required, so no new partitions are created. Instead, you can use `ALTER ONLINE TABLE ... MAX_ROWS=rows` to increase the maximum number of rows for such a table; in this case, `ALTER ONLINE TABLE ... REORGANIZE``PARTITION` is not needed (and causes an error if executed). The value of `rows` must be greater than the value specified for `MAX_ROWS` in the original `CREATE TABLE` statement for this to work.

Attempting to use `REORGANIZE PARTITION` without the `partition_names INTO``(partition_definitions)` option on explicitly partitioned tables results in the error `REORGANIZE`

```
PARTITION without parameters can only be used on auto-partitioned tables
using HASH partitioning.
```

Note For partitions that have not been explicitly named, MySQL automatically provides the default names `p0`, `p1`, `p2`, and so on. The same is true with regard to subpartitions.

For more detailed information about and examples of `ALTER TABLE ... REORGANIZE PARTITION`statements, see Section 19.3.1, “Management of RANGE and LIST Partitions”.

- To exchange a table partition or subpartition with a table, use the `ALTER TABLE ... EXCHANGE`

`PARTITION` statement—that is, to move any existing rows in the partition or subpartition to the nonpartitioned table, and any existing rows in the nonpartitioned table to the table partition or subpartition.

For usage information and examples, see Section 19.3.3, “Exchanging Partitions and Subpartitions with Tables”.

- Several options provide partition maintenance and repair functionality analogous to that implemented

for nonpartitioned tables by statements such as `CHECK TABLE` and `REPAIR TABLE` (which are also supported for partitioned tables; for more information, see Section 13.7.2, “Table Maintenance Statements”). These include `ANALYZE PARTITION`, `CHECK PARTITION`, `OPTIMIZE PARTITION`,`REBUILD PARTITION`, and `REPAIR PARTITION`. Each of these options takes a `partition_names`clause consisting of one or more names of partitions, separated by commas. The partitions must already exist in the table to be altered. You can also use the `ALL` keyword in place of `partition_names`,in which case the statement acts on all table partitions. For more information and examples, see Section 19.3.4, “Maintenance of Partitions”.

Some MySQL storage engines, such as `InnoDB`, do not support per-partition optimization. For a partitioned table using such a storage engine, `ALTER TABLE ... OPTIMIZE PARTITION` causes ALTER TABLE Statement the entire table to rebuilt and analyzed, and an appropriate warning to be issued. (Bug #11751825, Bug#42822)To work around this problem, use the statements `ALTER TABLE ... REBUILD PARTITION` and

```
ALTER TABLE ... ANALYZE PARTITION instead.
The ANALYZE PARTITION, CHECK PARTITION, OPTIMIZE PARTITION, and REPAIR PARTITION
```

options are not permitted for tables which are not partitioned.

- `REMOVE PARTITIONING` enables you to remove a table's partitioning without otherwise affecting the

table or its data. This option can be combined with other `ALTER TABLE` options such as those used to add, drop, or rename columns or indexes.

- Using the `ENGINE` option with `ALTER TABLE` changes the storage engine used by the table without

affecting the partitioning.

```
When ALTER TABLE ... EXCHANGE PARTITION or ALTER TABLE ... TRUNCATE PARTITION is
```

run against a partitioned table that uses `MyISAM` (or another storage engine that makes use of table-level locking), only those partitions that are actually read from are locked. (This does not apply to partitioned tables using a storage enginethat employs row-level locking, such as `InnoDB`.) See Section 19.6.4,“Partitioning and Locking”.

It is possible for an `ALTER TABLE` statement to contain a `PARTITION BY` or `REMOVE PARTITIONING`clause in an addition to other alter specifications, but the `PARTITION BY` or `REMOVE PARTITIONING`clause must be specified last after any other specifications.

```
The ADD PARTITION, DROP PARTITION, COALESCE PARTITION, REORGANIZE PARTITION,
```

`ANALYZE PARTITION`, `CHECK PARTITION`, and `REPAIR PARTITION` options cannot be combined with other alter specifications in a single `ALTER TABLE`, since the options just listed act on individual partitions.

For more information, see Section 13.1.7.1, “ALTER TABLE Partition Operations”.

Only a single instance of any one of the following options can be used in a given `ALTER TABLE`

```
statement: PARTITION BY, ADD PARTITION, DROP PARTITION, TRUNCATE PARTITION, EXCHANGE
PARTITION, REORGANIZE PARTITION, or COALESCE PARTITION, ANALYZE PARTITION, CHECK
PARTITION, OPTIMIZE PARTITION, REBUILD PARTITION, REMOVE PARTITIONING.
```

For example, the following two statements are invalid:

```
ALTER TABLE t1 ANALYZE PARTITION p1, ANALYZE PARTITION p2;
ALTER TABLE t1 ANALYZE PARTITION p1, CHECK PARTITION p2;
```

In the first case, you can analyze partitions `p1` and `p2` of table `t1` concurrently using a single statement with a single `ANALYZE PARTITION` option that lists both of the partitions to be analyzed, like this:

```
ALTER TABLE t1 ANALYZE PARTITION p1, p2;
```

In the second case, it is not possible to perform `ANALYZE` and `CHECK` operations on different partitions of the same table concurrently. Instead, you must issue two separate statements, like this:

```
ALTER TABLE t1 ANALYZE PARTITION p1;
ALTER TABLE t1 CHECK PARTITION p2;
```

`ANALYZE`, `CHECK`, `OPTIMIZE`, `REBUILD`, `REPAIR`, and `TRUNCATE` operations are not supported for subpartitions.

#### 13.1.7.2 ALTER TABLE Examples

Begin with a table `t1` created as shown here:ALTER TABLE Statement

```
CREATE TABLE t1 (a INTEGER, b CHAR(10));
```

To rename the table from `t1` to `t2`:

```
ALTER TABLE t1 RENAME t2;
```

To change column a from `INTEGER` to `TINYINT NOT NULL` (leaving the name the same), and to change column b from `CHAR(10)` to `CHAR(20)` as well as renaming it from b to c:

```
ALTER TABLE t2 MODIFY a TINYINT NOT NULL, CHANGE b c CHAR(20);
```

To add a new `TIMESTAMP` column named d:

```
ALTER TABLE t2 ADD d TIMESTAMP;
```

To add an index on column d and a `UNIQUE` index on column a:

```
ALTER TABLE t2 ADD INDEX (d), ADD UNIQUE (a);
```

To remove column c:

```
ALTER TABLE t2 DROP COLUMN c;
```

To add a new `AUTO_INCREMENT` integer column named c:

```
ALTER TABLE t2 ADD c INT UNSIGNED NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (c);
```

We indexed c (as a `PRIMARY KEY`) because `AUTO_INCREMENT` columns must be indexed, and we declare c as `NOT NULL` because primary key columns cannot be `NULL`.

For `NDB` tables, it is also possible to change the storage type used for a table or column. For example,consider an `NDB` table created as shown here:

```
mysql> CREATE TABLE t1 (c1 INT) TABLESPACE ts_1 ENGINE NDB;
Query OK, 0 rows affected (1.27 sec)
```

To convert this table to disk-based storage, you can use the following `ALTER TABLE` statement:

```
mysql> ALTER TABLE t1 TABLESPACE ts_1 STORAGE DISK;
Query OK, 0 rows affected (2.99 sec)
Records: 0  Duplicates: 0  Warnings: 0
mysql> SHOW CREATE TABLE t1\G
*************************** 1. row ***************************
Table: t1
Create Table: CREATE TABLE `t1` (
`c1` int(11) DEFAULT NULL
) /*!50100 TABLESPACE ts_1 STORAGE DISK */
ENGINE=ndbcluster DEFAULT CHARSET=latin1
1 row in set (0.01 sec)
```

It is not necessary that the tablespace was referenced when the table was originally created; however, the tablespace must be referenced by the `ALTER TABLE`:

```
mysql> CREATE TABLE t2 (c1 INT) ts_1 ENGINE NDB;
Query OK, 0 rows affected (1.00 sec)
mysql> ALTER TABLE t2 STORAGE DISK;
ERROR 1005 (HY000): Can't create table 'c.#sql-1750_3' (errno: 140)
mysql> ALTER TABLE t2 TABLESPACE ts_1 STORAGE DISK;
Query OK, 0 rows affected (3.42 sec)
Records: 0  Duplicates: 0  Warnings: 0
mysql> SHOW CREATE TABLE t2\G
*************************** 1. row ***************************
Table: t1
```

ALTER TABLE Statement

```
Create Table: CREATE TABLE `t2` (
`c1` int(11) DEFAULT NULL
) /*!50100 TABLESPACE ts_1 STORAGE DISK */
ENGINE=ndbcluster DEFAULT CHARSET=latin1
1 row in set (0.01 sec)
```

To change the storage type of an individual column, you can use `ALTER TABLE ... MODIFY``[COLUMN]`. For example, suppose you create an NDB Cluster Disk Data table with two columns, using this`CREATE TABLE` statement:

```
mysql> CREATE TABLE t3 (c1 INT, c2 INT)
->     TABLESPACE ts_1 STORAGE DISK ENGINE NDB;
Query OK, 0 rows affected (1.34 sec)
```

To change column `c2` from disk-based to in-memory storage, include a STORAGE MEMORY clause in the column definition used by the ALTER TABLE statement, as shown here:

```
mysql> ALTER TABLE t3 MODIFY c2 INT STORAGE MEMORY;
Query OK, 0 rows affected (3.14 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

You can make an in-memory column into a disk-based column by using `STORAGE DISK` in a similar fashion.

Column `c1` uses disk-based storage, since this is the default for the table (determined by the table-level`STORAGE DISK` clause in the `CREATE TABLE` statement). However, column `c2` uses in-memory storage,as can be seen here in the output of SHOW `CREATE TABLE`:

```
mysql> SHOW CREATE TABLE t3\G
*************************** 1. row ***************************
Table: t3
Create Table: CREATE TABLE `t3` (
`c1` int(11) DEFAULT NULL,
`c2` int(11) /*!50120 STORAGE MEMORY */ DEFAULT NULL
) /*!50100 TABLESPACE ts_1 STORAGE DISK */ ENGINE=ndbcluster DEFAULT CHARSET=latin1
1 row in set (0.02 sec)
```

When you add an `AUTO_INCREMENT` column, column values are filled in with sequence numbers automatically. For `MyISAM` tables, you can set the first sequence number by executing `SET``INSERT_ID=value` before `ALTER TABLE` or by using the `AUTO_INCREMENT=value` table option.

With `MyISAM` tables, if you do not change the `AUTO_INCREMENT` column, the sequence number is not affected. If you drop an `AUTO_INCREMENT` column and then add another `AUTO_INCREMENT` column, the numbers are resequenced beginning with 1.

When replication is used, adding an `AUTO_INCREMENT` column to a table might not produce the same ordering of the rows on the replica and the source. This occurs because the order in which the rows are numbered depends on the specific storage engine used for the table and the order in which the rows were inserted. If it is important to have the same order on the source and replica, the rows must be ordered before assigning an `AUTO_INCREMENT` number. Assuming that you want to add an `AUTO_INCREMENT`column to the table `t1`, the following statements produce a new table `t2` identical to `t1` but with an`AUTO_INCREMENT` column:

```
CREATE TABLE t2 (id INT AUTO_INCREMENT PRIMARY KEY)
SELECT * FROM t1 ORDER BY col1, col2;
```

This assumes that the table `t1` has columns `col1` and `col2`.

This set of statements also produces a new table `t2` identical to `t1`, with the addition of an`AUTO_INCREMENT` column:

```
CREATE TABLE t2 LIKE t1;
ALTER TABLE t2 ADD id INT AUTO_INCREMENT PRIMARY KEY;
```

ALTER TABLESPACE Statement

```
INSERT INTO t2 SELECT * FROM t1 ORDER BY col1, col2;
```

Important To guarantee the same ordering on both source and replica, all columns of `t1` must be referenced in the `ORDER BY` clause.

Regardless of the method used to create and populate the copy having the `AUTO_INCREMENT` column, the final step is to drop the original table and then rename the copy:

```
DROP TABLE t1;
ALTER TABLE t2 RENAME t1;
```

### 13.1.8 ALTER TABLESPACE Statement

```
ALTER TABLESPACE tablespace_name
{ADD | DROP} DATAFILE 'file_name'
[INITIAL_SIZE [=] size]
[WAIT]
ENGINE [=] engine_name
```

This statement is used either to add a new data file, or to drop a data file from a tablespace.

The `ADD DATAFILE` variant enables you to specify an initial size using an `INITIAL_SIZE` clause, where`size` is measured in bytes; the default value is 134217728 (128 MB). Prior to MySQL NDB Cluster 7.3.2,this value was required to be specified using digits (Bug #13116514, Bug #16104705, Bug #62858); in MySQL NDB Cluster 7.3.2 and later, you may optionally follow `size` with a one-letter abbreviation for an order of magnitude, similar to those used in `my.cnf`. Generally, this is one of the letters M (megabytes) or G (gigabytes).

Note All NDB Cluster Disk Data objects share the same namespace. This means that each Disk Data object must be uniquely named (and not merely each Disk Data object of a given type). For example, you cannot have a tablespace and a data file with the same name, or an undo log file and a tablespace with the same name.

On 32-bit systems, the maximum supported value for `INITIAL_SIZE` is 4294967296 (4 GB). (Bug#29186)`INITIAL_SIZE` is rounded, explicitly, as for `CREATE TABLESPACE`.

Once a data file has been created, its size cannot be changed; however, you can add more data files to the tablespace using additional `ALTER TABLESPACE ... ADD DATAFILE` statements.

Using `DROP DATAFILE` with `ALTER TABLESPACE` drops the data file '`file_name`' from the tablespace.

You cannot drop a data file from a tablespace which is in use by any table; in other words, the data file must be empty (no extents used). See Section 18.6.11.1, “NDB Cluster Disk Data Objects”. In addition, any data file to be dropped must previously have been added to the tablespace with `CREATE TABLESPACE` or

```
ALTER TABLESPACE.
Both ALTER TABLESPACE ... ADD DATAFILE and ALTER TABLESPACE ... DROP DATAFILE
```

require an `ENGINE` clause which specifies the storage engine used by the tablespace. Currently, the only accepted values for `engine_name` are `NDB` and `NDBCLUSTER`.

`WAIT` is parsed but otherwise ignored, and so has no effect in MySQL 5.6. It is intended for future expansion.

When `ALTER TABLESPACE ... ADD DATAFILE` is used with `ENGINE = NDB`, a data file is created on each Cluster data node. You can verify that the data files were created and obtain information about them ALTER VIEW Statement by querying the Information Schema `FILES` table. For example, the following query shows all data files belonging to the tablespace named `newts`:

```
mysql> SELECT LOGFILE_GROUP_NAME, FILE_NAME, EXTRA
-> FROM INFORMATION_SCHEMA.FILES
-> WHERE TABLESPACE_NAME = 'newts' AND FILE_TYPE = 'DATAFILE';
+--------------------+--------------+----------------+
| LOGFILE_GROUP_NAME | FILE_NAME    | EXTRA          |
+--------------------+--------------+----------------+
| lg_3               | newdata.dat  | CLUSTER_NODE=3 |
| lg_3               | newdata.dat  | CLUSTER_NODE=4 |
| lg_3               | newdata2.dat | CLUSTER_NODE=3 |
| lg_3               | newdata2.dat | CLUSTER_NODE=4 |
+--------------------+--------------+----------------+
2 rows in set (0.03 sec)
```

See Section 21.5.1, “The INFORMATION_SCHEMA FILES Table”.

`ALTER TABLESPACE` is useful only with Disk Data storage for NDB Cluster. See Section 18.6.11, “NDB Cluster Disk Data Tables”.

### 13.1.9 ALTER VIEW Statement

```
ALTER
[ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
[DEFINER = user]
[SQL SECURITY { DEFINER | INVOKER }]
VIEW view_name [(column_list)]
AS select_statement
[WITH [CASCADED | LOCAL] CHECK OPTION]
```

This statement changes the definition of a view, which must exist. The syntax is similar to that for `CREATE``VIEW` see Section 13.1.20, “CREATE VIEW Statement”). This statement requires the `CREATE VIEW` and`DROP` privileges for the view, and some privilege for each column referred to in the `SELECT` statement.

`ALTER VIEW` is permitted only to the definer or users with the `SUPER` privilege.

### 13.1.10 CREATE DATABASE Statement

```
CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name
[create_option] ...
create_option: [DEFAULT] {
CHARACTER SET [=] charset_name
| COLLATE [=] collation_name
}
```

`CREATE DATABASE` creates a database with the given name. To use this statement, you need the `CREATE`privilege for the database. `CREATE SCHEMA` is a synonym for `CREATE DATABASE`.

An error occurs if the database exists and you did not specify `IF NOT EXISTS`.

`CREATE DATABASE` is not permitted within a session that has an active `LOCK TABLES` statement.

Each `create_option` specifies a database characteristic. Database characteristics are stored in the `db.opt` file in the database directory. The `CHARACTER SET` option specifies the default database character set. The `COLLATE` option specifies the default database collation. For information about character set and collation names, see Chapter 10, Character Sets, Collations, Unicode.

To see the available character sets and collations, use the `SHOW CHARACTER SET` and `SHOW``COLLATION` statements, respectively. See Section 13.7.5.4, “SHOW CHARACTER SET Statement”, and Section 13.7.5.5, “SHOW COLLATION Statement”.

CREATE EVENT Statement A database in MySQL is implemented as a directory containing files that correspond to tables in the database. Because there are no tables in a database when it is initially created, the `CREATE DATABASE`statement creates only a directory under the MySQL data directory and the `db.opt` file. Rules for permissible database names are given in Section 9.2, “Schema Object Names”. If a database name contains special characters, the name for the database directory contains encoded versions of those characters as described in Section 9.2.4, “Mapping of Identifiers to File Names”.

If you manually create a directory under the data directory (for example, with `mkdir`), the server considers it a database directory and it shows up in the output of `SHOW DATABASES`.

When you create a database, let the server manage the directory and the files in it. Manipulating database directories and files directly can cause inconsistencies and unexpected results.

MySQL has no limit on the number of databases. The underlying file system may have a limit on the number of directories.

You can also use the `mysqladmin` program to create databases. See Section 4.5.2, “mysqladmin — A MySQL Server Administration Program”.

### 13.1.11 CREATE EVENT Statement

```
CREATE
[DEFINER = user]
EVENT
[IF NOT EXISTS]
event_name
ON SCHEDULE schedule
[ON COMPLETION [NOT] PRESERVE]
[ENABLE | DISABLE | DISABLE ON SLAVE]
[COMMENT 'string']
DO event_body;
schedule: {
AT timestamp [+ INTERVAL interval] ...
| EVERY interval
[STARTS timestamp [+ INTERVAL interval] ...]
[ENDS timestamp [+ INTERVAL interval] ...]
}
interval:
quantity {YEAR | QUARTER | MONTH | DAY | HOUR | MINUTE |
WEEK | SECOND | YEAR_MONTH | DAY_HOUR | DAY_MINUTE |
DAY_SECOND | HOUR_MINUTE | HOUR_SECOND | MINUTE_SECOND}
```

This statement creates and schedules a new event. The event does not run unless the Event Scheduler is enabled. For information about checking Event Scheduler status and enabling it if necessary, see Section 20.4.2, “Event Scheduler Configuration”.

`CREATE EVENT` requires the `EVENT` privilege for the schema in which the event is to be created. If the `DEFINER` clause is present, the privileges required depend on the `user` value, as discussed in Section 20.6, “Stored Object Access Control”.

The minimum requirements for a valid `CREATE EVENT` statement are as follows:

- The keywords `CREATE EVENT` plus an event name, which uniquely identifies the event in a database

schema.

- An `ON SCHEDULE` clause, which determines when and how often the event executes.
- A `DO` clause, which contains the SQL statement to be executed by an event.

CREATE EVENT Statement This is an example of a minimal `CREATE EVENT` statement:

```
CREATE EVENT myevent
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR
DO
UPDATE myschema.mytable SET mycol = mycol + 1;
```

The previous statement creates an event named `myevent`. This event executes once—one hour following its creation—by running an SQL statement that increments the value of the `myschema.mytable` table's`mycol` column by 1.

The `event_name` must be a valid MySQL identifier with a maximum length of 64 characters. Event names are not case-sensitive, so you cannot have two events named `myevent` and `MyEvent` in the same schema. In general, the rules governing event names are the same as those for names of stored routines.

See Section 9.2, “Schema Object Names”.

An event is associated with a schema. If no schema is indicated as part of `event_name`, the default(current) schema is assumed. To create an event in a specific schema, qualify the event name with a schema using `schema_name.event_name` syntax.

The `DEFINER` clause specifies the MySQL account to be used when checking access privileges at event execution time. If the `DEFINER` clause is present, the `user` value should be a MySQL account specified as `'user_name'@'host_name'`, `CURRENT_USER`, or `CURRENT_USER()`. The permitted `user` values depend on the privileges you hold, as discussed in Section 20.6, “Stored Object Access Control”. Also see that section for additional information about event security.

If the `DEFINER` clause is omitted, the default definer is the user who executes the `CREATE EVENT`statement. This is the same as specifying `DEFINER = CURRENT_USER` explicitly.

Within an event body, the `CURRENT_USER` function returns the account used to check privileges at event execution time, which is the `DEFINER` user. For information about user auditing within events, see Section 6.2.15, “SQL-Based Account Activity Auditing”.

`IF NOT EXISTS` has the same meaning for `CREATE EVENT` as for `CREATE TABLE`: If an event named`event_name` already exists in the same schema, no action is taken, and no error results. (However, a warning is generated in such cases.)The `ON SCHEDULE` clause determines when, how often, and for how long the `event_body` defined for the event repeats. This clause takes one of two forms:

- `AT timestamp` is used for a one-time event. It specifies that the event executes one time only

at the date and time given by `timestamp`, which must include both the date and time, or must be an expression that resolves to a datetime value. You may use a value of either the `DATETIME` or`TIMESTAMP` type for this purpose. If the date is in the past, a warning occurs, as shown here:

```
mysql> SELECT NOW();
+---------------------+
| NOW()               |
+---------------------+
| 2006-02-10 23:59:01 |
+---------------------+
1 row in set (0.04 sec)
mysql> CREATE EVENT e_totals
->     ON SCHEDULE AT '2006-02-10 23:59:00'
->     DO INSERT INTO test.totals VALUES (NOW());
Query OK, 0 rows affected, 1 warning (0.00 sec)
mysql> SHOW WARNINGS\G
*************************** 1. row ***************************
Level: Note
```

CREATE EVENT Statement

```
Code: 1588
Message: Event execution time is in the past and ON COMPLETION NOT
PRESERVE is set. The event was dropped immediately after
creation.
```

`CREATE EVENT` statements which are themselves invalid—for whatever reason—fail with an error.

You may use `CURRENT_TIMESTAMP` to specify the current date and time. In such a case, the event acts as soon as it is created.

To create an event which occurs at some point in the future relative to the current date and time—such as that expressed by the phrase “three weeks from now”—you can use the optional clause `+ INTERVAL``interval`. The `interval` portion consists of two parts, a quantity and a unit of time, and follows the syntax rules described in Temporal Intervals, except that you cannot use any units keywords that involving microseconds when defining an event. With some interval types, complex time units may be used. For example, “two minutes and ten seconds” can be expressed as `+ INTERVAL '2:10'`

```
MINUTE_SECOND.
```

You can also combine intervals. For example, `AT CURRENT_TIMESTAMP + INTERVAL 3 WEEK +``INTERVAL 2 DAY` is equivalent to “three weeks and two days from now”. Each portion of such a clause must begin with `+ INTERVAL`.

- To repeat actions at a regular interval, use an `EVERY` clause. The `EVERY` keyword is followed by an

`interval` as described in the previous discussion of the `AT` keyword. (`+ INTERVAL` is not used with`EVERY`.) For example, `EVERY 6 WEEK` means “every six weeks”.

Although `+ INTERVAL` clauses are not permitted in an `EVERY` clause, you can use the same complex time units permitted in a `+ INTERVAL`.

An `EVERY` clause may contain an optional `STARTS` clause. `STARTS` is followed by a `timestamp` value that indicates when the action should begin repeating, and may also use `+ INTERVAL interval` to specify an amount of time “from now”. For example, `EVERY 3 MONTH STARTS CURRENT_TIMESTAMP``+ INTERVAL 1 WEEK` means “every three months, beginning one week from now”. Similarly, you can express “every two weeks, beginning six hours and fifteen minutes from now” as `EVERY 2 WEEK`

```
STARTS CURRENT_TIMESTAMP + INTERVAL '6:15' HOUR_MINUTE. Not specifying STARTS is
```

the same as using `STARTS CURRENT_TIMESTAMP`—that is, the action specified for the event begins repeating immediately upon creation of the event.

An `EVERY` clause may contain an optional `ENDS` clause. The `ENDS` keyword is followed by a `timestamp`value that tells MySQL when the event should stop repeating. You may also use `+ INTERVAL`

```
interval with ENDS; for instance, EVERY 12 HOUR STARTS CURRENT_TIMESTAMP + INTERVAL
```

`30 MINUTE ENDS CURRENT_TIMESTAMP + INTERVAL 4 WEEK` is equivalent to “every twelve hours,beginning thirty minutes from now, and ending four weeks from now”. Not using `ENDS` means that the event continues executing indefinitely.

`ENDS` supports the same syntax for complex time units as `STARTS` does.

You may use `STARTS`, `ENDS`, both, or neither in an `EVERY` clause.

If a repeating event does not terminate within its scheduling interval, the result may be multiple instances of the event executing simultaneously. If this is undesirable, you should institute a mechanism to prevent simultaneous instances. For example, you could use the `GET_LOCK()` function, or row or table locking.

The `ON SCHEDULE` clause may use expressions involving built-in MySQL functions and user variables to obtain any of the `timestamp` or `interval` values which it contains. You may not use stored functions or loadable functions in such expressions, nor may you use any table references; however, you may use`SELECT FROM DUAL`. This is true for both `CREATE EVENT` and `ALTER EVENT` statements. References to CREATE EVENT Statement stored functions, loadable functions, and tables in such cases are specifically not permitted, and fail with an error (see Bug #22830).

Times in the `ON SCHEDULE` clause are interpreted using the current session `time_zone` value. This becomes the event time zone; that is, the time zone that is used for event scheduling and is in effect within the event as it executes. These times are converted to UTC and stored along with the event time zone in the `mysql.event` table. This enables event execution to proceed as defined regardless of any subsequent changes to the server time zone or daylight saving time effects. For additional information about representation of event times, see Section 20.4.4, “Event Metadata”. See also Section 13.7.5.19,“SHOW EVENTS Statement”, and Section 21.3.8, “The INFORMATION_SCHEMA EVENTS Table”.

Normally, once an event has expired, it is immediately dropped. You can override this behavior by specifying `ON COMPLETION PRESERVE`. Using `ON COMPLETION NOT PRESERVE` merely makes the default nonpersistent behavior explicit.

You can create an event but prevent it from being active using the `DISABLE` keyword. Alternatively, you can use `ENABLE` to make explicit the default status, which is active. This is most useful in conjunction with`ALTER EVENT` (see Section 13.1.2, “ALTER EVENT Statement”).

A third value may also appear in place of `ENABLE` or `DISABLE`; `DISABLE ON SLAVE` is set for the status of an event on a replica to indicate that the event was created on the source and replicated to the replica,but is not executed on the replica. See Section 17.4.1.16, “Replication of Invoked Features”.

You may supply a comment for an event using a `COMMENT` clause. `comment` may be any string of up to 64 characters that you wish to use for describing the event. The comment text, being a string literal, must be surrounded by quotation marks.

The `DO` clause specifies an action carried by the event, and consists of an SQL statement. Nearly any valid MySQL statement that can be used in a stored routine can also be used as the action statement for a scheduled event. (See Section 20.8, “Restrictions on Stored Programs”.) For example, the following event `e_hourly` deletes all rows from the `sessions` table once per hour, where this table is part of the`site_activity` schema:

```
CREATE EVENT e_hourly
ON SCHEDULE
EVERY 1 HOUR
COMMENT 'Clears out sessions table each hour.'
DO
DELETE FROM site_activity.sessions;
```

MySQL stores the `sql_mode` system variable setting in effect when an event is created or altered, and always executes the event with this setting in force, regardless of the current server SQL mode when the event begins executing.

A `CREATE EVENT` statement that contains an `ALTER EVENT` statement in its `DO` clause appears to succeed; however, when the server attempts to execute the resulting scheduled event, the execution fails with an error.

Note Statements such as `SELECT` or `SHOW` that merely return a result set have no effect when used in an event; the output from these is not sent to the MySQL Monitor,nor is it stored anywhere. However, you can use statements such as `SELECT ...``INTO` and `INSERT INTO ... SELECT` that store a result. (See the next example in this section for an instance of the latter.)The schema to which an event belongs is the default schema for table references in the `DO` clause. Any references to tables in other schemas must be qualified with the proper schema name.

CREATE EVENT Statement As with stored routines, you can use compound-statement syntax in the `DO` clause by using the `BEGIN` and`END` keywords, as shown here:

```
delimiter |
CREATE EVENT e_daily
ON SCHEDULE
EVERY 1 DAY
COMMENT 'Saves total number of sessions then clears the table each day'
DO
BEGIN
INSERT INTO site_activity.totals (time, total)
SELECT CURRENT_TIMESTAMP, COUNT(*)
FROM site_activity.sessions;
DELETE FROM site_activity.sessions;
END |
delimiter ;
```

This example uses the `delimiter` command to change the statement delimiter. See Section 20.1,“Defining Stored Programs”.

More complex compound statements, such as those used in stored routines, are possible in an event. This example uses local variables, an error handler, and a flow control construct:

```
delimiter |
CREATE EVENT e
ON SCHEDULE
EVERY 5 SECOND
DO
BEGIN
DECLARE v INTEGER;
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION BEGIN END;
SET v = 0;
WHILE v < 5 DO
INSERT INTO t1 VALUES (0);
UPDATE t2 SET s1 = s1 + 1;
SET v = v + 1;
END WHILE;
END |
delimiter ;
```

There is no way to pass parameters directly to or from events; however, it is possible to invoke a stored routine with parameters within an event:

```
CREATE EVENT e_call_myproc
ON SCHEDULE
AT CURRENT_TIMESTAMP + INTERVAL 1 DAY
DO CALL myproc(5, 27);
```

If an event's definer has privileges sufficient to set global system variables (see Section 5.1.8.1, “System Variable Privileges”), the event can read and write global variables. As granting such privileges entails a potential for abuse, extreme care must be taken in doing so.

Generally, any statements that are valid in stored routines may be used for action statements executed by events. For more information about statements permitted within stored routines, see Section 20.2.1,“Stored Routine Syntax”. You can create an event as part of a stored routine, but an event cannot be created by another event.

CREATE FUNCTION Statement

### 13.1.12 CREATE FUNCTION Statement

The `CREATE FUNCTION` statement is used to create stored functions and loadable functions:

- For information about creating stored functions, see Section 13.1.15, “CREATE PROCEDURE and

CREATE FUNCTION Statements”.

- For information about creating loadable functions, see Section 13.7.3.1, “CREATE FUNCTION

Statement for Loadable Functions”.

### 13.1.13 CREATE INDEX Statement

```
CREATE [ONLINE | OFFLINE] [UNIQUE | FULLTEXT | SPATIAL] INDEX index_name
[index_type]
ON tbl_name (key_part,...)
[index_option]
[algorithm_option | lock_option] ...
key_part:
col_name [(length)] [ASC | DESC]
index_option: {
KEY_BLOCK_SIZE [=] value
| index_type
| WITH PARSER parser_name
| COMMENT 'string'
}
index_type:
USING {BTREE | HASH}
algorithm_option:
ALGORITHM [=] {DEFAULT | INPLACE | COPY}
lock_option:
LOCK [=] {DEFAULT | NONE | SHARED | EXCLUSIVE}
```

Normally, you create all indexes on a table at the time the table itself is created with `CREATE TABLE`. See Section 13.1.17, “CREATE TABLE Statement”. This guideline is especially important for `InnoDB` tables,where the primary key determines the physical layout of rows in the data file. `CREATE INDEX` enables you to add indexes to existing tables.

`CREATE INDEX` is mapped to an `ALTER TABLE` statement to create indexes. See Section 13.1.7, “ALTER TABLE Statement”. `CREATE INDEX` cannot be used to create a `PRIMARY KEY`; use `ALTER TABLE`instead. For more information about indexes, see Section 8.3.1, “How MySQL Uses Indexes”.

When the `innodb_stats_persistent` setting is enabled, run the `ANALYZE TABLE` statement for an`InnoDB` table after creating an index on that table.

An index specification of the form `(key_part1, key_part2, ...)` creates an index with multiple key parts. Index key values are formed by concatenating the values of the given key parts. For example`(col1, col2, col3)` specifies a multiple-column index with index keys consisting of values from `col1`,`col2`, and `col3`.

A `key_part` specification can end with `ASC` or `DESC`. These keywords are permitted for future extensions for specifying ascending or descending index value storage. Currently, they are parsed but ignored; index values are always stored in ascending order.

The following sections describe different aspects of the `CREATE INDEX` statement:

- Column Prefix Key Parts

CREATE INDEX Statement

- Unique Indexes
- Full-Text Indexes
- Spatial Indexes
- Index Options
- Table Copying and Locking Options

> Column Prefix Key Parts

For string columns, indexes can be created that use only the leading part of column values, using`col_name(length)` syntax to specify an index prefix length:

- Prefixes can be specified for `CHAR`, `VARCHAR`, `BINARY`, and `VARBINARY` key parts.
- Prefixes must be specified for `BLOB` and `TEXT` key parts. Additionally, `BLOB` and `TEXT` columns can be

indexed only for `InnoDB`, `MyISAM`, and `BLACKHOLE` tables.

- Prefix limits are measured in bytes. However, prefix lengths for index specifications in `CREATE TABLE`,

`ALTER TABLE`, and `CREATE INDEX` statements are interpreted as number of characters for nonbinary string types (`CHAR`, `VARCHAR`, `TEXT`) and number of bytes for binary string types (`BINARY`, `VARBINARY`,`BLOB`). Take this into account when specifying a prefix length for a nonbinary string column that uses a multibyte character set.

Prefix support and lengths of prefixes (where supported) are storage engine dependent. For example,a prefix can be up to 767 bytes long for `InnoDB` tables or 3072 bytes if the `innodb_large_prefix`option is enabled. For `MyISAM` tables, the prefix length limit is 1000 bytes. The `NDB` storage engine does not support prefixes (see Section 18.2.7.6, “Unsupported or Missing Features in NDB Cluster”).

The statement shown here creates an index using the first 10 characters of the `name` column (assuming that `name` has a nonbinary string type):

```
CREATE INDEX part_of_name ON customer (name(10));
```

If names in the column usually differ in the first 10 characters, lookups performed using this index should not be much slower than using an index created from the entire `name` column. Also, using column prefixes for indexes can make the index file much smaller, which could save a lot of disk space and might also speed up `INSERT` operations.

> Unique Indexes

A `UNIQUE` index creates a constraint such that all values in the index must be distinct. An error occurs if you try to add a new row with a key value that matches an existing row. If you specify a prefix value for a column in a `UNIQUE` index, the column values must be unique within the prefix length. A `UNIQUE` index permits multiple `NULL` values for columns that can contain `NULL`.

If a table has a `PRIMARY KEY` or `UNIQUE NOT NULL` index that consists of a single column that has an integer type, you can use `_rowid` to refer to the indexed column in `SELECT` statements, as follows:

- `_rowid` refers to the `PRIMARY KEY` column if there is a `PRIMARY KEY` consisting of a single integer

column. If there is a `PRIMARY KEY` but it does not consist of a single integer column, `_rowid` cannot be used.

- Otherwise, `_rowid` refers to the column in the first `UNIQUE NOT NULL` index if that index consists of a

single integer column. If the first `UNIQUE NOT NULL` index does not consist of a single integer column,`_rowid` cannot be used.

CREATE INDEX Statement

> Full-Text Indexes

`FULLTEXT` indexes are supported only for `InnoDB` and `MyISAM` tables and can include only `CHAR`,`VARCHAR`, and `TEXT` columns. Indexing always happens over the entire column; column prefix indexing is not supported and any prefix length is ignored if specified. See Section 12.10, “Full-Text Search Functions”, for details of operation.

> Spatial Indexes

The `MyISAM`, `InnoDB`, `NDB`, and `ARCHIVE` storage engines support spatial columns such as `POINT` and`GEOMETRY`. (Section 11.4, “Spatial Data Types”, describes the spatial data types.) However, support for spatial column indexing varies among engines. Spatial and nonspatial indexes on spatial columns are available according to the following rules.

Spatial indexes on spatial columns (created using `SPATIAL INDEX`) have these characteristics:

- Available only for `MyISAM` tables. Specifying `SPATIAL INDEX` for other storage engines results in an

error.

- Indexed columns must be `NOT NULL`.
- Column prefix lengths are prohibited. The full width of each column is indexed.

Nonspatial indexes on spatial columns (created with `INDEX`, `UNIQUE`, or `PRIMARY KEY`) have these characteristics:

- Permitted for any storage engine that supports spatial columns except `ARCHIVE`.
- Columns can be `NULL` unless the index is a primary key.
- For each spatial column in a non-`SPATIAL` index except `POINT` columns, a column prefix length must

be specified. (This is the same requirement as for indexed `BLOB` columns.) The prefix length is given in bytes.

- The index type for a non-`SPATIAL` index depends on the storage engine. Currently, B-tree is used.
- Permitted for a column that can have `NULL` values only for `InnoDB`, `MyISAM`, and `MEMORY` tables.

> Index Options

Following the key part list, index options can be given. An `index_option` value can be any of the following:

```
- KEY_BLOCK_SIZE [=] value
```

For `MyISAM` tables, `KEY_BLOCK_SIZE` optionally specifies the size in bytes to use for index key blocks.

The value is treated as a hint; a different size could be used if necessary. A `KEY_BLOCK_SIZE` value specified for an individual index definition overrides a table-level `KEY_BLOCK_SIZE` value.

`KEY_BLOCK_SIZE` is not supported at the index level for `InnoDB` tables. See Section 13.1.17, “CREATE TABLE Statement”.

```
- index_type
```

Some storage engines permit you to specify an index type when creating an index. For example:

```
CREATE TABLE lookup (id INT) ENGINE = MEMORY;
CREATE INDEX id_index ON lookup (id) USING BTREE;
```

CREATE INDEX Statement Table 13.1, “Index Types Per Storage Engine” shows the permissible index type values supported by different storage engines. Where multiple index types are listed, the first one is the default when no index type specifier is given. Storage engines not listed in the table do not support an `index_type` clause in index definitions.

> Table 13.1 Index Types Per Storage Engine Storage Engine Permissible Index Types

```
InnoDB  BTREE
MyISAM  BTREE
MEMORY/HEAP  HASH, BTREE
```

`NDB` `HASH`, `BTREE` (see note in text)The `index_type` clause cannot be used for `FULLTEXT INDEX` or `SPATIAL INDEX` specifications.

Full-text index implementation is storage engine dependent. Spatial indexes are implemented as R-tree indexes.

`BTREE` indexes are implemented by the `NDB` storage engine as T-tree indexes.

Note For indexes on `NDB` table columns, the `USING` option can be specified only for a unique index or primary key. `USING HASH` prevents the creation of an ordered index; otherwise, creating a unique index or primary key on an `NDB` table automatically results in the creation of both an ordered index and a hash index,each of which indexes the same set of columns.

For unique indexes that include one or more `NULL` columns of an `NDB` table,the hash index can be used only to look up literal values, which means that `IS``[NOT] NULL` conditions require a full scan of the table. One workaround is to make sure that a unique index using one or more `NULL` columns on such a table is always created in such a way that it includes the ordered index; that is, avoid employing `USING HASH` when creating the index.

If you specify an index type that is not valid for a given storage engine, but another index type is available that the engine can use without affecting query results, the engine uses the available type. The parser recognizes `RTREE` as a type name, but currently this cannot be specified for any storage engine.

Note Use of the `index_type` option before the `ON tbl_name` clause is deprecated;

expect support for use of the option in this position to be removed in a future CREATE INDEX Statement MySQL release. If an `index_type` option is given in both the earlier and later positions, the final option applies.

`TYPE type_name` is recognized as a synonym for `USING type_name`. However, `USING` is the preferred form.

The following tables show index characteristics for the storage engines that support the `index_type`option.

Table 13.2 InnoDB Storage Engine Index Characteristics Index Class Index Type Stores NULL Permits IS NULL Scan IS NOT NULL VALUES Multiple NULL Type Scan Type Values Primary key `BTREE` No No N/A N/A Unique `BTREE` Yes Yes Index Index Key `BTREE` Yes Yes Index Index`FULLTEXT` N/A Yes Yes Table Table Table 13.3 MyISAM Storage Engine Index Characteristics Index Class Index Type Stores NULL Permits IS NULL Scan IS NOT NULL VALUES Multiple NULL Type Scan Type Values Primary key `BTREE` No No N/A N/A Unique `BTREE` Yes Yes Index Index Key `BTREE` Yes Yes Index Index`FULLTEXT` N/A Yes Yes Table Table`SPATIAL` N/A No No N/A N/A Table 13.4 MEMORY Storage Engine Index Characteristics Index Class Index Type Stores NULL Permits IS NULL Scan IS NOT NULL VALUES Multiple NULL Type Scan Type Values Primary key `BTREE` No No N/A N/A Unique `BTREE` Yes Yes Index Index Key `BTREE` Yes Yes Index Index Primary key `HASH` No No N/A N/A Unique `HASH` Yes Yes Index Index Key `HASH` Yes Yes Index Index Table 13.5 NDB Storage Engine Index Characteristics Index Class Index Type Stores NULL Permits IS NULL Scan IS NOT NULL VALUES Multiple NULL Type Scan Type Values Primary key `BTREE` No No Index Index Unique `BTREE` Yes Yes Index Index CREATE LOGFILE GROUP Statement Index Class Index Type Stores NULL Permits IS NULL Scan IS NOT NULL VALUES Multiple NULL Type Scan Type Values Key `BTREE` Yes Yes Index Index Primary key `HASH` No No Table (see note Table (see note 1) 1)Unique `HASH` Yes Yes Table (see note Table (see note 1) 1)Key `HASH` Yes Yes Table (see note Table (see note 1) 1)Table note:

1. If `USING HASH` is specified that prevents creation of an implicit ordered index.

```
- WITH PARSER parser_name
```

This option can be used only with `FULLTEXT` indexes. It associates a parser plugin with the index if full-text indexing and searching operations need special handling. See The MySQL Plugin API, for details on creating plugins.

```
- COMMENT 'string'
```

Index definitions can include an optional comment of up to 1024 characters.

> Table Copying and Locking Options

`ALGORITHM` and `LOCK` clauses may be given to influence the table copying method and level of concurrency for reading and writing the table while its indexes are being modified. They have the same meaning as for the `ALTER TABLE` statement. For more information, see Section 13.1.7, “ALTER TABLE Statement”Indexes on variable-width columns of `NDBCLUSTER` tables are created online; that is, without any table copying. The table is not locked against access from other NDB Cluster API nodes, although it is locked against other operations on the same API node for the duration of the operation. This is done automatically by the server whenever it determines that it is possible to do so; you do not have to use any special SQL syntax or server options to cause it to happen.

In standard MySQL 5.6 releases, it is not possible to override the server when it determines that an index is to be created without table copying. In NDB Cluster, you can create indexes offline (which causes the table to be locked to all API nodes in the cluster) using the `OFFLINE` keyword. The rules and limitations governing `CREATE OFFLINE INDEX` and `CREATE ONLINE INDEX` are the same as for `ALTER OFFLINE``TABLE ... ADD INDEX` and `ALTER ONLINE TABLE ... ADD INDEX`. You cannot cause the noncopying creation of an index that would normally be created offline by using the `ONLINE` keyword: If it is not possible to perform the `CREATE INDEX` operation without table copying, the server ignores the`ONLINE` keyword. For more information, see Section 18.6.12, “Online Operations with ALTER TABLE in NDB Cluster”.

The `ONLINE` and `OFFLINE` keywords are available only in NDB Cluster; attempting to use these keywords in standard MySQL Server 5.6 releases results in a syntax error. The `ONLINE` and `OFFLINE` keywords are deprecated in MySQL NDB Cluster 7.3; they continue to be supported in MySQL NDB Cluster 7.4, but they are subject to removal in a future NDB Cluster release.

### 13.1.14 CREATE LOGFILE GROUP Statement

CREATE LOGFILE GROUP Statement

```
CREATE LOGFILE GROUP logfile_group
ADD UNDOFILE 'undo_file'
[INITIAL_SIZE [=] initial_size]
[UNDO_BUFFER_SIZE [=] undo_buffer_size]
[REDO_BUFFER_SIZE [=] redo_buffer_size]
[NODEGROUP [=] nodegroup_id]
[WAIT]
[COMMENT [=] 'string']
ENGINE [=] engine_name
```

This statement creates a new log file group named `logfile_group` having a single `UNDO` file named'`undo_file`'. A `CREATE LOGFILE GROUP` statement has one and only one `ADD UNDOFILE` clause. For rules covering the naming of log file groups, see Section 9.2, “Schema Object Names”.

Note All NDB Cluster Disk Data objects share the same namespace. This means that each Disk Data object must be uniquely named (and not merely each Disk Data object of a given type). For example, you cannot have a tablespace and a log file group with the same name, or a tablespace and a data file with the same name.

In MySQL NDB Cluster 7.3 and later, you can have only one log file group per Cluster at any given time.

(See Bug #16386)The optional `INITIAL_SIZE` parameter sets the `UNDO` file's initial size; if not specified, it defaults to`128M` (128 megabytes). The optional `UNDO_BUFFER_SIZE` parameter sets the size used by the `UNDO`buffer for the log file group; The default value for `UNDO_BUFFER_SIZE` is `8M` (eight megabytes); this value cannot exceed the amount of system memory available. Both of these parameters are specified in bytes.

In MySQL NDB Cluster 7.3.2 and later, you may optionally follow either or both of these with a one-letter abbreviation for an order of magnitude, similar to those used in `my.cnf`. Generally, this is one of the letters M (for megabytes) or G (for gigabytes). Prior to MySQL NDB Cluster 7.3.2, the values for these options could only be specified using digits. (Bug #13116514, Bug #16104705, Bug #62858)Memory used for `UNDO_BUFFER_SIZE` comes from the global pool whose size is determined by the value of the `SharedGlobalMemory` data node configuration parameter. This includes any default value implied for this option by the setting of the `InitialLogFileGroup` data node configuration parameter.

The maximum permitted for `UNDO_BUFFER_SIZE` is 629145600 (600 MB).

On 32-bit systems, the maximum supported value for `INITIAL_SIZE` is 4294967296 (4 GB). (Bug#29186)The minimum allowed value for `INITIAL_SIZE` is 1048576 (1 MB).

The `ENGINE` option determines the storage engine to be used by this log file group, with `engine_name`being the name of the storage engine. In MySQL 5.6, this must be `NDB` (or `NDBCLUSTER`). If `ENGINE` is not set, MySQL tries to use the engine specified by the `default_storage_engine` server system variable(formerly `storage_engine`). In any case, if the engine is not specified as `NDB` or `NDBCLUSTER`, the`CREATE LOGFILE GROUP` statement appears to succeed but actually fails to create the log file group, as shown here:

```
mysql> CREATE LOGFILE GROUP lg1
->     ADD UNDOFILE 'undo.dat' INITIAL_SIZE = 10M;
Query OK, 0 rows affected, 1 warning (0.00 sec)
mysql> SHOW WARNINGS;
+-------+------+-------------------------------------------------------------------------------------------
| Level | Code | Message
+-------+------+-------------------------------------------------------------------------------------------
```

CREATE PROCEDURE and CREATE FUNCTION Statements

```
| Error | 1478 | Table storage engine 'InnoDB' does not support the create option 'TABLESPACE or LOGFILE GROUP
+-------+------+----------------------------------------------------------------------------------------------
1 row in set (0.00 sec)
mysql> DROP LOGFILE GROUP lg1 ENGINE = NDB;
ERROR 1529 (HY000): Failed to drop LOGFILE GROUP
mysql> CREATE LOGFILE GROUP lg1
->     ADD UNDOFILE 'undo.dat' INITIAL_SIZE = 10M
->     ENGINE = NDB;
Query OK, 0 rows affected (2.97 sec)
```

The fact that the `CREATE LOGFILE GROUP` statement does not actually return an error when a non-`NDB`storage engine is named, but rather appears to succeed, is a known issue which we hope to address in a future release of NDB Cluster.

`REDO_BUFFER_SIZE`, `NODEGROUP`, `WAIT`, and `COMMENT` are parsed but ignored, and so have no effect in MySQL 5.6. These options are intended for future expansion.

When used with `ENGINE [=] NDB`, a log file group and associated `UNDO` log file are created on each Cluster data node. You can verify that the `UNDO` files were created and obtain information about them by querying the Information Schema `FILES` table. For example:

```
mysql> SELECT LOGFILE_GROUP_NAME, LOGFILE_GROUP_NUMBER, EXTRA
-> FROM INFORMATION_SCHEMA.FILES
-> WHERE FILE_NAME = 'undo_10.dat';
+--------------------+----------------------+----------------+
| LOGFILE_GROUP_NAME | LOGFILE_GROUP_NUMBER | EXTRA          |
+--------------------+----------------------+----------------+
| lg_3               |                   11 | CLUSTER_NODE=3 |
| lg_3               |                   11 | CLUSTER_NODE=4 |
+--------------------+----------------------+----------------+
2 rows in set (0.06 sec)
```

`CREATE LOGFILE GROUP` is useful only with Disk Data storage for NDB Cluster. See Section 18.6.11,“NDB Cluster Disk Data Tables”.

### 13.1.15 CREATE PROCEDURE and CREATE FUNCTION Statements

```
CREATE
[DEFINER = user]
PROCEDURE sp_name ([proc_parameter[,...]])
[characteristic ...] routine_body
CREATE
[DEFINER = user]
FUNCTION sp_name ([func_parameter[,...]])
RETURNS type
[characteristic ...] routine_body
proc_parameter:
[ IN | OUT | INOUT ] param_name type
func_parameter:
param_name type
type:
Any valid MySQL data type
characteristic: {
COMMENT 'string'
| LANGUAGE SQL
| [NOT] DETERMINISTIC
| { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
```

CREATE PROCEDURE and CREATE FUNCTION Statements

```
| SQL SECURITY { DEFINER | INVOKER }
}
routine_body:
Valid SQL routine statement
```

These statements are used to create a stored routine (a stored procedure or function). That is, the specified routine becomes known to the server. By default, a stored routine is associated with the default database. To associate the routine explicitly with a given database, specify the name as`db_name.sp_name` when you create it.

The `CREATE FUNCTION` statement is also used in MySQL to support loadable functions. See Section 13.7.3.1, “CREATE FUNCTION Statement for Loadable Functions”. A loadable function can be regarded as an external stored function. Stored functions share their namespace with loadable functions.

See Section 9.2.5, “Function Name Parsing and Resolution”, for the rules describing how the server interprets references to different kinds of functions.

To invoke a stored procedure, use the `CALL` statement (see Section 13.2.1, “CALL Statement”). To invoke a stored function, refer to it in an expression. The function returns a value during expression evaluation.

`CREATE PROCEDURE` and `CREATE FUNCTION` require the `CREATE ROUTINE` privilege. If the `DEFINER`clause is present, the privileges required depend on the `user` value, as discussed in Section 20.6,“Stored Object Access Control”. If binary logging is enabled, `CREATE FUNCTION` might require the `SUPER`privilege, as discussed in Section 20.7, “Stored Program Binary Logging”.

By default, MySQL automatically grants the `ALTER ROUTINE` and `EXECUTE` privileges to the routine creator. This behavior can be changed by disabling the `automatic_sp_privileges` system variable.

See Section 20.2.2, “Stored Routines and MySQL Privileges”.

The `DEFINER` and `SQL SECURITY` clauses specify the security context to be used when checking access privileges at routine execution time, as described later in this section.

If the routine name is the same as the name of a built-in SQL function, a syntax error occurs unless you use a space between the name and the following parenthesis when defining the routine or invoking it later.

For this reason, avoid using the names of existing SQL functions for your own stored routines.

The `IGNORE_SPACE` SQL mode applies to built-in functions, not to stored routines. It is always permissible to have spaces after a stored routine name, regardless of whether `IGNORE_SPACE` is enabled.

The parameter list enclosed within parentheses must always be present. If there are no parameters, an empty parameter list of `()` should be used. Parameter names are not case-sensitive.

Each parameter is an `IN` parameter by default. To specify otherwise for a parameter, use the keyword `OUT`or `INOUT` before the parameter name.

Note Specifying a parameter as `IN`, `OUT`, or `INOUT` is valid only for a `PROCEDURE`. For a`FUNCTION`, parameters are always regarded as `IN` parameters.

An `IN` parameter passes a value into a procedure. The procedure might modify the value, but the modification is not visible to the caller when the procedure returns. An `OUT` parameter passes a value from the procedure back to the caller. Its initial value is `NULL` within the procedure, and its value is visible to the caller when the procedure returns. An `INOUT` parameter is initialized by the caller, can be modified by the procedure, and any change made by the procedure is visible to the caller when the procedure returns.

For each `OUT` or `INOUT` parameter, pass a user-defined variable in the `CALL` statement that invokes the procedure so that you can obtain its value when the procedure returns. If you are calling the procedure CREATE PROCEDURE and CREATE FUNCTION Statements from within another stored procedure or function, you can also pass a routine parameter or local routine variable as an `OUT` or `INOUT` parameter. If you are calling the procedure from within a trigger, you can also pass `NEW.col_name` as an `OUT` or `INOUT` parameter.

For information about the effect of unhandled conditions on procedure parameters, see Section 13.6.7.8,“Condition Handling and OUT or INOUT Parameters”.

Routine parameters cannot be referenced in statements prepared within the routine; see Section 20.8,“Restrictions on Stored Programs”.

The following example shows a simple stored procedure that, given a country code, counts the number of cities for that country that appear in the `city` table of the `world` database. The country code is passed using an `IN` parameter, and the city count is returned using an `OUT` parameter:

```
mysql> delimiter //
mysql> CREATE PROCEDURE citycount (IN country CHAR(3), OUT cities INT)
BEGIN
SELECT COUNT(*) INTO cities FROM world.city
WHERE CountryCode = country;
END//
Query OK, 0 rows affected (0.01 sec)
mysql> delimiter ;
mysql> CALL citycount('JPN', @cities); -- cities in Japan
Query OK, 1 row affected (0.00 sec)
mysql> SELECT @cities;
+---------+
| @cities |
+---------+
|     248 |
+---------+
1 row in set (0.00 sec)
mysql> CALL citycount('FRA', @cities); -- cities in France
Query OK, 1 row affected (0.00 sec)
mysql> SELECT @cities;
+---------+
| @cities |
+---------+
|      40 |
+---------+
1 row in set (0.00 sec)
```

The example uses the `mysql` client `delimiter` command to change the statement delimiter from ; to `//`while the procedure is being defined. This enables the ; delimiter used in the procedure body to be passed through to the server rather than being interpreted by `mysql` itself. See Section 20.1, “Defining Stored Programs”.

The `RETURNS` clause may be specified only for a `FUNCTION`, for which it is mandatory. It indicates the return type of the function, and the function body must contain a `RETURN value` statement. If the `RETURN`statement returns a value of a different type, the value is coerced to the proper type. For example, if a function specifies an `ENUM` or `SET` value in the `RETURNS` clause, but the `RETURN` statement returns an integer, the value returned from the function is the string for the corresponding `ENUM` member of set of `SET`members.

The following example function takes a parameter, performs an operation using an SQL function, and returns the result. In this case, it is unnecessary to use `delimiter` because the function definition contains no internal ; statement delimiters:CREATE PROCEDURE and CREATE FUNCTION Statements

```
mysql> CREATE FUNCTION hello (s CHAR(20))
mysql> RETURNS CHAR(50) DETERMINISTIC
RETURN CONCAT('Hello, ',s,'!');
Query OK, 0 rows affected (0.00 sec)
mysql> SELECT hello('world');
+----------------+
| hello('world') |
+----------------+
| Hello, world!  |
+----------------+
1 row in set (0.00 sec)
```

Parameter types and function return types can be declared to use any valid data type. The `COLLATE`attribute can be used if preceded by a `CHARACTER SET` specification.

The `routine_body` consists of a valid SQL routine statement. This can be a simple statement such as`SELECT` or `INSERT`, or a compound statement written using `BEGIN` and `END`. Compound statements can contain declarations, loops, and other control structure statements. The syntax for these statements is described in Section 13.6, “Compound Statements”. In practice, stored functions tend to use compound statements, unless the body consists of a single `RETURN` statement.

MySQL permits routines to contain DDL statements, such as `CREATE` and `DROP`. MySQL also permits stored procedures (but not stored functions) to contain SQL transaction statements such as `COMMIT`.

Stored functions may not contain statements that perform explicit or implicit commit or rollback. Support for these statements is not required by the SQL standard, which states that each DBMS vendor may decide whether to permit them.

Statements that return a result set can be used within a stored procedure but not within a stored function.

This prohibition includes `SELECT` statements that do not have an `INTO var_list` clause and other statements such as `SHOW`, `EXPLAIN`, and `CHECK TABLE`. For statements that can be determined at function definition time to return a result set, a `Not allowed to return a result set from a``function` error occurs (`ER_SP_NO_RETSET`). For statements that can be determined only at runtime to return a result set, a `PROCEDURE %s can't return a result set in the given context` error occurs (`ER_SP_BADSELECT`).

`USE` statements within stored routines are not permitted. When a routine is invoked, an implicit `USE``db_name` is performed (and undone when the routine terminates). The causes the routine to have the given default database while it executes. References to objects in databases other than the routine default database should be qualified with the appropriate database name.

For additional information about statements that are not permitted in stored routines, see Section 20.8,“Restrictions on Stored Programs”.

For information about invoking stored procedures from within programs written in a language that has a MySQL interface, see Section 13.2.1, “CALL Statement”.

MySQL stores the `sql_mode` system variable setting in effect when a routine is created or altered, and always executes the routine with this setting in force, regardless of the current server SQL mode when the routine begins executing.

The switch from the SQL mode of the invoker to that of the routine occurs after evaluation of arguments and assignment of the resulting values to routine parameters. If you define a routine in strict SQL mode but invoke it in nonstrict mode, assignment of arguments to routine parameters does not take place in strict mode. If you require that expressions passed to a routine be assigned in strict SQL mode, you should invoke the routine with strict mode in effect.

The `COMMENT` characteristic is a MySQL extension, and may be used to describe the stored routine. This information is displayed by the `SHOW CREATE PROCEDURE` and `SHOW CREATE FUNCTION` statements.

CREATE PROCEDURE and CREATE FUNCTION Statements The `LANGUAGE` characteristic indicates the language in which the routine is written. The server ignores this characteristic; only SQL routines are supported.

A routine is considered “deterministic” if it always produces the same result for the same input parameters,and “not deterministic” otherwise. If neither `DETERMINISTIC` nor `NOT DETERMINISTIC` is given in the routine definition, the default is `NOT DETERMINISTIC`. To declare that a function is deterministic, you must specify `DETERMINISTIC` explicitly.

Assessment of the nature of a routine is based on the “honesty” of the creator: MySQL does not check that a routine declared `DETERMINISTIC` is free of statements that produce nondeterministic results. However,misdeclaring a routine might affect results or affect performance. Declaring a nondeterministic routine as`DETERMINISTIC` might lead to unexpected results by causing the optimizer to make incorrect execution plan choices. Declaring a deterministic routine as `NONDETERMINISTIC` might diminish performance by causing available optimizations not to be used.

If binary logging is enabled, the `DETERMINISTIC` characteristic affects which routine definitions MySQL accepts. See Section 20.7, “Stored Program Binary Logging”.

A routine that contains the `NOW()` function (or its synonyms) or `RAND()` is nondeterministic, but it might still be replication-safe. For `NOW()`, the binary log includes the timestamp and replicates correctly. `RAND()`also replicates correctly as long as it is called only a single time during the execution of a routine. (You can consider the routine execution timestamp and random number seed as implicit inputs that are identical on the source and replica.)Several characteristics provide information about the nature of data use by the routine. In MySQL, these characteristics are advisory only. The server does not use them to constrain what kinds of statements a routine is permitted to execute.

- `CONTAINS SQL` indicates that the routine does not contain statements that read or write data. This is the

default if none of these characteristics is given explicitly. Examples of such statements are `SET @x = 1`or `DO RELEASE_LOCK('abc')`, which execute but neither read nor write data.

- `NO SQL` indicates that the routine contains no SQL statements.
- `READS SQL DATA` indicates that the routine contains statements that read data (for example, `SELECT`),

but not statements that write data.

- `MODIFIES SQL DATA` indicates that the routine contains statements that may write data (for example,

```
INSERT or DELETE).
```

The `SQL SECURITY` characteristic can be `DEFINER` or `INVOKER` to specify the security context; that is,whether the routine executes using the privileges of the account named in the routine `DEFINER` clause or the user who invokes it. This account must have permission to access the database with which the routine is associated. The default value is `DEFINER`. The user who invokes the routine must have the `EXECUTE`privilege for it, as must the `DEFINER` account if the routine executes in definer security context.

The `DEFINER` clause specifies the MySQL account to be used when checking access privileges at routine execution time for routines that have the `SQL SECURITY DEFINER` characteristic.

If the `DEFINER` clause is present, the `user` value should be a MySQL account specified as`'user_name'@'host_name'`, `CURRENT_USER`, or `CURRENT_USER()`. The permitted `user` values depend on the privileges you hold, as discussed in Section 20.6, “Stored Object Access Control”. Also see that section for additional information about stored routine security.

If the `DEFINER` clause is omitted, the default definer is the user who executes the `CREATE PROCEDURE` or`CREATE FUNCTION` statement. This is the same as specifying `DEFINER = CURRENT_USER` explicitly.

CREATE SERVER Statement Within the body of a stored routine that is defined with the `SQL SECURITY DEFINER` characteristic, the`CURRENT_USER` function returns the routine's `DEFINER` value. For information about user auditing within stored routines, see Section 6.2.15, “SQL-Based Account Activity Auditing”.

Consider the following procedure, which displays a count of the number of MySQL accounts listed in the`mysql.user` system table:

```
CREATE DEFINER = 'admin'@'localhost' PROCEDURE account_count()
BEGIN
SELECT 'Number of accounts:', COUNT(*) FROM mysql.user;
END;
```

The procedure is assigned a `DEFINER` account of `'admin'@'localhost'` no matter which user defines it. It executes with the privileges of that account no matter which user invokes it (because the default security characteristic is `DEFINER`). The procedure succeeds or fails depending on whether invoker has the `EXECUTE` privilege for it and `'admin'@'localhost'` has the `SELECT` privilege for the `mysql.user`system table.

Now suppose that the procedure is defined with the `SQL SECURITY INVOKER` characteristic:

```
CREATE DEFINER = 'admin'@'localhost' PROCEDURE account_count()
SQL SECURITY INVOKER
BEGIN
SELECT 'Number of accounts:', COUNT(*) FROM mysql.user;
END;
```

The procedure still has a `DEFINER` of `'admin'@'localhost'`, but in this case, it executes with the privileges of the invoking user. Thus, the procedure succeeds or fails depending on whether the invoker has the `EXECUTE` privilege for it and the `SELECT` privilege for the `mysql.user` table.

The server handles the data type of a routine parameter, local routine variable created with `DECLARE`, or function return value as follows:

- Assignments are checked for data type mismatches and overflow. Conversion and overflow problems

result in warnings, or errors in strict SQL mode.

- Only scalar values can be assigned. For example, a statement such as `SET x = (SELECT 1, 2)` is

invalid.

- For character data types, if `CHARACTER SET` is includedd in the declaration, the specified character set

and its default collation is used. If the `COLLATE` attribute is also present, that collation is used rather than the default collation.

If `CHARACTER SET` and `COLLATE` are not present, the database character set and collation in effect at routine creation time are used. To avoid having the server use the database character set and collation,provide an explicit `CHARACTER SET` and a `COLLATE` attribute for character data parameters.

If you alter the database default character set or collation, stored routines that are to use the new database defaults must be dropped and recreated.

The database character set and collation are given by the value of the `character_set_database`and `collation_database` system variables. For more information, see Section 10.3.3, “Database Character Set and Collation”.

### 13.1.16 CREATE SERVER Statement

```
CREATE SERVER server_name
FOREIGN DATA WRAPPER wrapper_name
```

CREATE SERVER Statement

```
OPTIONS (option [, option] ...)
option: {
HOST character-literal
| DATABASE character-literal
| USER character-literal
| PASSWORD character-literal
| SOCKET character-literal
| OWNER character-literal
| PORT numeric-literal
}
```

This statement creates the definition of a server for use with the `FEDERATED` storage engine. The `CREATE``SERVER` statement creates a new row in the `servers` table in the `mysql` database. This statement requires the `SUPER` privilege.

The `server_name` should be a unique reference to the server. Server definitions are global within the scope of the server, it is not possible to qualify the server definition to a specific database. `server_name`has a maximum length of 64 characters (names longer than 64 characters are silently truncated), and is case-insensitive. You may specify the name as a quoted string.

The `wrapper_name` is an identifier and may be quoted with single quotation marks.

For each `option` you must specify either a character literal or numeric literal. Character literals are UTF-8,support a maximum length of 64 characters and default to a blank (empty) string. String literals are silently truncated to 64 characters. Numeric literals must be a number between 0 and 9999, default value is 0.

Note The `OWNER` option is currently not applied, and has no effect on the ownership or operation of the server connection that is created.

The `CREATE SERVER` statement creates an entry in the `mysql.servers` table that can later be used with the `CREATE TABLE` statement when creating a `FEDERATED` table. The options that you specify are used to populate the columns in the `mysql.servers` table. The table columns are `Server_name`, `Host`, `Db`,

```
Username, Password, Port and Socket.
```

For example:

```
CREATE SERVER s
FOREIGN DATA WRAPPER mysql
OPTIONS (USER 'Remote', HOST '198.51.100.106', DATABASE 'test');
```

Be sure to specify all options necessary to establish a connection to the server. The user name, host name, and database name are mandatory. Other options might be required as well, such as password.

The data stored in the table can be used when creating a connection to a `FEDERATED` table:

```
CREATE TABLE t (s1 INT) ENGINE=FEDERATED CONNECTION='s';
```

For more information, see Section 15.8, “The FEDERATED Storage Engine”.

`CREATE SERVER` causes an implicit commit. See Section 13.3.3, “Statements That Cause an Implicit Commit”.

`CREATE SERVER` is not written to the binary log, regardless of the logging format that is in use.

In MySQL 5.6.11 only, `gtid_next` must be set to `AUTOMATIC` before issuing this statement. (Bug#16062608, Bug #16715809, Bug #69045)CREATE TABLE Statement

### 13.1.17 CREATE TABLE Statement

```
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
(create_definition,...)
[table_options]
[partition_options]
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
[(create_definition,...)]
[table_options]
[partition_options]
[IGNORE | REPLACE]
[AS] query_expression
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
{ LIKE old_tbl_name | (LIKE old_tbl_name) }
create_definition: {
col_name column_definition
| {INDEX | KEY} [index_name] [index_type] (key_part,...)
[index_option] ...
| {FULLTEXT | SPATIAL} [INDEX | KEY] [index_name] (key_part,...)
[index_option] ...
| [CONSTRAINT [symbol]] PRIMARY KEY
[index_type] (key_part,...)
[index_option] ...
| [CONSTRAINT [symbol]] UNIQUE [INDEX | KEY]
[index_name] [index_type] (key_part,...)
[index_option] ...
| [CONSTRAINT [symbol]] FOREIGN KEY
[index_name] (col_name,...)
reference_definition
| CHECK (expr)
}
column_definition:
data_type [NOT NULL | NULL] [DEFAULT default_value]
[AUTO_INCREMENT] [UNIQUE [KEY]] [[PRIMARY] KEY]
[COMMENT 'string']
[COLLATE collation_name]
[COLUMN_FORMAT {FIXED | DYNAMIC | DEFAULT}]
[STORAGE {DISK | MEMORY}]
[reference_definition]
data_type:
(see Chapter 11, Data Types)
key_part:
col_name [(length)] [ASC | DESC]
index_type:
USING {BTREE | HASH}
index_option: {
KEY_BLOCK_SIZE [=] value
| index_type
| WITH PARSER parser_name
| COMMENT 'string'
}
reference_definition:
REFERENCES tbl_name (key_part,...)
[MATCH FULL | MATCH PARTIAL | MATCH SIMPLE]
[ON DELETE reference_option]
[ON UPDATE reference_option]
```

CREATE TABLE Statement

```
reference_option:
RESTRICT | CASCADE | SET NULL | NO ACTION | SET DEFAULT
table_options:
table_option [[,] table_option] ...
table_option: {
AUTO_INCREMENT [=] value
| AVG_ROW_LENGTH [=] value
| [DEFAULT] CHARACTER SET [=] charset_name
| CHECKSUM [=] {0 | 1}
| [DEFAULT] COLLATE [=] collation_name
| COMMENT [=] 'string'
| CONNECTION [=] 'connect_string'
| {DATA | INDEX} DIRECTORY [=] 'absolute path to directory'
| DELAY_KEY_WRITE [=] {0 | 1}
| ENGINE [=] engine_name
| INSERT_METHOD [=] { NO | FIRST | LAST }
| KEY_BLOCK_SIZE [=] value
| MAX_ROWS [=] value
| MIN_ROWS [=] value
| PACK_KEYS [=] {0 | 1 | DEFAULT}
| PASSWORD [=] 'string'
| ROW_FORMAT [=] {DEFAULT | DYNAMIC | FIXED | COMPRESSED | REDUNDANT | COMPACT}
| STATS_AUTO_RECALC [=] {DEFAULT | 0 | 1}
| STATS_PERSISTENT [=] {DEFAULT | 0 | 1}
| STATS_SAMPLE_PAGES [=] value
| tablespace_option
| UNION [=] (tbl_name[,tbl_name]...)
}
partition_options:
PARTITION BY
{ [LINEAR] HASH(expr)
| [LINEAR] KEY [ALGORITHM={1 | 2}] (column_list)
| RANGE{(expr) | COLUMNS(column_list)}
| LIST{(expr) | COLUMNS(column_list)} }
[PARTITIONS num]
[SUBPARTITION BY
{ [LINEAR] HASH(expr)
| [LINEAR] KEY [ALGORITHM={1 | 2}] (column_list) }
[SUBPARTITIONS num]
]
[(partition_definition [, partition_definition] ...)]
partition_definition:
PARTITION partition_name
[VALUES
{LESS THAN {(expr | value_list) | MAXVALUE}
|
IN (value_list)}]
[[STORAGE] ENGINE [=] engine_name]
[COMMENT [=] 'string' ]
[DATA DIRECTORY [=] 'data_dir']
[INDEX DIRECTORY [=] 'index_dir']
[MAX_ROWS [=] max_number_of_rows]
[MIN_ROWS [=] min_number_of_rows]
[TABLESPACE [=] tablespace_name]
[NODEGROUP [=] node_group_id]
[(subpartition_definition [, subpartition_definition] ...)]
subpartition_definition:
SUBPARTITION logical_name
[[STORAGE] ENGINE [=] engine_name]
[COMMENT [=] 'string' ]
[DATA DIRECTORY [=] 'data_dir']
[INDEX DIRECTORY [=] 'index_dir']
```

CREATE TABLE Statement

```
[MAX_ROWS [=] max_number_of_rows]
[MIN_ROWS [=] min_number_of_rows]
[TABLESPACE [=] tablespace_name]
[NODEGROUP [=] node_group_id]
tablespace_option:
TABLESPACE tablespace_name [STORAGE DISK]
| [TABLESPACE tablespace_name] STORAGE MEMORY
query_expression:
SELECT ...   (Some valid select or union statement)
```

`CREATE TABLE` creates a table with the given name. You must have the `CREATE` privilege for the table.

By default, tables are created in the default database, using the `InnoDB` storage engine. An error occurs if the table exists, if there is no default database, or if the database does not exist.

MySQL has no limit on the number of tables. The underlying file system may have a limit on the number of files that represent tables. Individual storage engines may impose engine-specific constraints. `InnoDB`permits up to 4 billion tables.

For information about the physical representation of a table, see Section 13.1.17.1, “Files Created by CREATE TABLE”.

There are several aspects to the `CREATE TABLE` statement, described under the following topics in this section:

- Table Name
- Temporary Tables
- Table Cloning and Copying
- Column Data Types and Attributes
- Indexes and Foreign Keys
- Table Options
- Table Partitioning

> Table Name

```
- tbl_name
```

The table name can be specified as `db_name.tbl_name` to create the table in a specific database.

This works regardless of whether there is a default database, assuming that the database exists.

If you use quoted identifiers, quote the database and table names separately. For example, write

```
`mydb`.`mytbl`, not `mydb.mytbl`.
```

Rules for permissible table names are given in Section 9.2, “Schema Object Names”.

```
- IF NOT EXISTS
```

Prevents an error from occurring if the table exists. However, there is no verification that the existing table has a structure identical to that indicated by the `CREATE TABLE` statement.

CREATE TABLE Statement

> Temporary Tables

You can use the `TEMPORARY` keyword when creating a table. A `TEMPORARY` table is visible only within the current session, and is dropped automatically when the session is closed. For more information, see Section 13.1.17.2, “CREATE TEMPORARY TABLE Statement”.

> Table Cloning and Copying

```
- LIKE
```

Use `CREATE TABLE ... LIKE` to create an empty table based on the definition of another table,including any column attributes and indexes defined in the original table:

```
CREATE TABLE new_tbl LIKE orig_tbl;
```

For more information, see Section 13.1.17.3, “CREATE TABLE ... LIKE Statement”.

```
- [AS] query_expression
```

To create one table from another, add a `SELECT` statement at the end of the `CREATE TABLE` statement:

```
CREATE TABLE new_tbl AS SELECT * FROM orig_tbl;
```

For more information, see Section 13.1.17.4, “CREATE TABLE ... SELECT Statement”.

```
- IGNORE | REPLACE
```

The `IGNORE` and `REPLACE` options indicate how to handle rows that duplicate unique key values when copying a table using a `SELECT` statement.

For more information, see Section 13.1.17.4, “CREATE TABLE ... SELECT Statement”.

> Column Data Types and Attributes

There is a hard limit of 4096 columns per table, but the effective maximum may be less for a given table and depends on the factors discussed in Section 8.4.7, “Limits on Table Column Count and Row Size”.

```
- data_type
```

`data_type` represents the data type in a column definition. For a full description of the syntax available for specifying column data types, as well as information about the properties of each type, see Chapter 11, Data Types.

- Some attributes do not apply to all data types. `AUTO_INCREMENT` applies only to integer and floating-

point types. `DEFAULT` does not apply to the `BLOB` or `TEXT` types.

- Character data types (`CHAR`, `VARCHAR`, the `TEXT` types, `ENUM`, `SET`, and any synonyms) can include

`CHARACTER SET` to specify the character set for the column. `CHARSET` is a synonym for `CHARACTER``SET`. A collation for the character set can be specified with the `COLLATE` attribute, along with any other attributes. For details, see Chapter 10, Character Sets, Collations, Unicode. Example:

```
CREATE TABLE t (c CHAR(20) CHARACTER SET utf8 COLLATE utf8_bin);
```

MySQL 5.6 interprets length specifications in character column definitions in characters. Lengths for`BINARY` and `VARBINARY` are in bytes.

- For `CHAR`, `VARCHAR`, `BINARY`, and `VARBINARY` columns, indexes can be created that use only the

leading part of column values, using `col_name(length)` syntax to specify an index prefix length.

`BLOB` and `TEXT` columns also can be indexed, but a prefix length must be given. Prefix lengths are CREATE TABLE Statement given in characters for nonbinary string types and in bytes for binary string types. That is, index entries consist of the first `length` characters of each column value for `CHAR`, `VARCHAR`, and `TEXT` columns,and the first `length` bytes of each column value for `BINARY`, `VARBINARY`, and `BLOB` columns.

Indexing only a prefix of column values like this can make the index file much smaller. For additional information about index prefixes, see Section 13.1.13, “CREATE INDEX Statement”.

Only the `InnoDB` and `MyISAM` storage engines support indexing on `BLOB` and `TEXT` columns. For example:

```
CREATE TABLE test (blob_col BLOB, INDEX(blob_col(10)));
- NOT NULL | NULL
```

If neither `NULL` nor `NOT NULL` is specified, the column is treated as though `NULL` had been specified.

In MySQL 5.6, only the `InnoDB`, `MyISAM`, and `MEMORY` storage engines support indexes on columns that can have `NULL` values. In other cases, you must declare indexed columns as `NOT NULL` or an error results.

```
- DEFAULT
```

Specifies a default value for a column. For more information about default value handling, including the case that a column definition includes no explicit `DEFAULT` value, see Section 11.5, “Data Type Default Values”.

If the `NO_ZERO_DATE` or `NO_ZERO_IN_DATE` SQL mode is enabled and a date-valued default is not correct according to that mode, `CREATE TABLE` produces a warning if strict SQL mode is not enabled and an error if strict mode is enabled. For example, with `NO_ZERO_IN_DATE` enabled, `c1 DATE``DEFAULT '2010-00-00'` produces a warning.

```
- AUTO_INCREMENT
```

An integer or floating-point column can have the additional attribute `AUTO_INCREMENT`. When you insert a value of `NULL` (recommended) or 0 into an indexed `AUTO_INCREMENT` column, the column is set to the next sequence value. Typically this is `value+1`, where `value` is the largest value for the column currently in the table. `AUTO_INCREMENT` sequences begin with 1.

To retrieve an `AUTO_INCREMENT` value after inserting a row, use the `LAST_INSERT_ID()` SQL function or the `mysql_insert_id()` C API function. See Section 12.16, “Information Functions”, and mysql_insert_id().

If the `NO_AUTO_VALUE_ON_ZERO` SQL mode is enabled, you can store 0 in `AUTO_INCREMENT` columns as 0 without generating a new sequence value. See Section 5.1.10, “Server SQL Modes”.

There can be only one `AUTO_INCREMENT` column per table, it must be indexed, and it cannot have a`DEFAULT` value. An `AUTO_INCREMENT` column works properly only if it contains only positive values.

Inserting a negative number is regarded as inserting a very large positive number. This is done to avoid CREATE TABLE Statement precision problems when numbers “wrap” over from positive to negative and also to ensure that you do not accidentally get an `AUTO_INCREMENT` column that contains 0.

For `MyISAM` tables, you can specify an `AUTO_INCREMENT` secondary column in a multiple-column key.

See Section 3.6.9, “Using AUTO_INCREMENT”.

To make MySQL compatible with some ODBC applications, you can find the `AUTO_INCREMENT` value for the last inserted row with the following query:

```
SELECT * FROM tbl_name WHERE auto_col IS NULL
```

This method requires that `sql_auto_is_null` variable is not set to 0. See Section 5.1.7, “Server System Variables”.

For information about `InnoDB` and `AUTO_INCREMENT`, see Section 14.6.1.6, “AUTO_INCREMENT Handling in InnoDB”. For information about `AUTO_INCREMENT` and MySQL Replication, see Section 17.4.1.1, “Replication and AUTO_INCREMENT”.

```
- COMMENT
```

A comment for a column can be specified with the `COMMENT` option, up to 1024 characters long. The comment is displayed by the `SHOW CREATE TABLE` and `SHOW FULL COLUMNS` statements. It is also shown in the `COLUMN_COMMENT` column of the Information Schema `COLUMNS` table.

```
- COLUMN_FORMAT
```

In NDB Cluster, it is also possible to specify a data storage format for individual columns of `NDB` tables using `COLUMN_FORMAT`. Permissible column formats are `FIXED`, `DYNAMIC`, and `DEFAULT`. `FIXED` is used to specify fixed-width storage, `DYNAMIC` permits the column to be variable-width, and `DEFAULT`causes the column to use fixed-width or variable-width storage as determined by the column's data type(possibly overridden by a `ROW_FORMAT` specifier).

For `NDB` tables, the default value for `COLUMN_FORMAT` is `DEFAULT`.

In NDB Cluster, the maximum possible offset for a column defined with `COLUMN_FORMAT=FIXED` is 8188 bytes. For more information and possible workarounds, see Section 18.2.7.5, “Limits Associated with Database Objects in NDB Cluster”.

`COLUMN_FORMAT` currently has no effect on columns of tables using storage engines other than `NDB`. In MySQL 5.6 and later, `COLUMN_FORMAT` is silently ignored.

```
- STORAGE
```

For `NDB` tables, it is possible to specify whether the column is stored on disk or in memory by using a `STORAGE` clause. `STORAGE DISK` causes the column to be stored on disk, and `STORAGE MEMORY`causes in-memory storage to be used. The `CREATE TABLE` statement used must still include a`TABLESPACE` clause:

```
mysql> CREATE TABLE t1 (
->     c1 INT STORAGE DISK,
->     c2 INT STORAGE MEMORY
-> ) ENGINE NDB;
ERROR 1005 (HY000): Can't create table 'c.t1' (errno: 140)
mysql> CREATE TABLE t1 (
->     c1 INT STORAGE DISK,
->     c2 INT STORAGE MEMORY
-> ) TABLESPACE ts_1 ENGINE NDB;
Query OK, 0 rows affected (1.06 sec)
```

CREATE TABLE Statement For `NDB` tables, `STORAGE DEFAULT` is equivalent to `STORAGE MEMORY`.

The `STORAGE` clause has no effect on tables using storage engines other than `NDB`. The `STORAGE`keyword is supported only in the build of `mysqld` that is supplied with NDB Cluster; it is not recognized in any other version of MySQL, where any attempt to use the `STORAGE` keyword causes a syntax error.

> Indexes and Foreign Keys

Several keywords apply to creation of indexes and foreign keys. For general background in addition to the following descriptions, see Section 13.1.13, “CREATE INDEX Statement”, and Section 13.1.17.5,“FOREIGN KEY Constraints”.

```
- CONSTRAINT symbol
```

The `CONSTRAINT symbol` clause may be given to name a constraint. If the clause is not given, or a `symbol` is not included following the `CONSTRAINT` keyword, MySQL automatically generates a constraint name. The `symbol` value, if used, must be unique per schema (database), per constraint type. A duplicate `symbol` results in an error. See also the discussion about length limits of generated constraint identifiers at Section 9.2.1, “Identifier Length Limits”.

The SQL standard specifies that all types of constraints (primary key, unique index, foreign key, check)belong to the same namespace. In MySQL, each constraint type has its own namespace per schema.

Consequently, names for each type of constraint must be unique per schema.

```
- PRIMARY KEY
```

A unique index where all key columns must be defined as `NOT NULL`. If they are not explicitly declared as `NOT NULL`, MySQL declares them so implicitly (and silently). A table can have only one `PRIMARY``KEY`. The name of a `PRIMARY KEY` is always `PRIMARY`, which thus cannot be used as the name for any other kind of index.

If you do not have a `PRIMARY KEY` and an application asks for the `PRIMARY KEY` in your tables,MySQL returns the first `UNIQUE` index that has no `NULL` columns as the `PRIMARY KEY`.

In `InnoDB` tables, keep the `PRIMARY KEY` short to minimize storage overhead for secondary indexes.

Each secondary index entry contains a copy of the primary key columns for the corresponding row. (See Section 14.6.2.1, “Clustered and Secondary Indexes”.)In the created table, a `PRIMARY KEY` is placed first, followed by all `UNIQUE` indexes, and then the nonunique indexes. This helps the MySQL optimizer to prioritize which index to use and also more quickly to detect duplicated `UNIQUE` keys.

A `PRIMARY KEY` can be a multiple-column index. However, you cannot create a multiple-column index using the `PRIMARY KEY` key attribute in a column specification. Doing so only marks that single column as primary. You must use a separate `PRIMARY KEY(key_part, ...)` clause.

If a table has a `PRIMARY KEY` or `UNIQUE NOT NULL` index that consists of a single column that has an integer type, you can use `_rowid` to refer to the indexed column in `SELECT` statements, as described in Unique Indexes.

In MySQL, the name of a `PRIMARY KEY` is `PRIMARY`. For other indexes, if you do not assign a name,the index is assigned the same name as the first indexed column, with an optional suffix (`_2`, `_3`, `...`)to make it unique. You can see index names for a table using `SHOW INDEX FROM tbl_name`. See Section 13.7.5.23, “SHOW INDEX Statement”.

```
- KEY | INDEX
```

CREATE TABLE Statement`KEY` is normally a synonym for `INDEX`. The key attribute `PRIMARY KEY` can also be specified as just`KEY` when given in a column definition. This was implemented for compatibility with other database systems.

```
- UNIQUE
```

A `UNIQUE` index creates a constraint such that all values in the index must be distinct. An error occurs if you try to add a new row with a key value that matches an existing row. For all engines, a `UNIQUE`index permits multiple `NULL` values for columns that can contain `NULL`. If you specify a prefix value for a column in a `UNIQUE` index, the column values must be unique within the prefix length.

If a table has a `PRIMARY KEY` or `UNIQUE NOT NULL` index that consists of a single column that has an integer type, you can use `_rowid` to refer to the indexed column in `SELECT` statements, as described in Unique Indexes.

```
- FULLTEXT
```

A `FULLTEXT` index is a special type of index used for full-text searches. Only the `InnoDB` and `MyISAM`storage engines support `FULLTEXT` indexes. They can be created only from `CHAR`, `VARCHAR`, and `TEXT`columns. Indexing always happens over the entire column; column prefix indexing is not supported and any prefix length is ignored if specified. See Section 12.10, “Full-Text Search Functions”, for details of operation. A `WITH PARSER` clause can be specified as an `index_option` value to associate a parser plugin with the index if full-text indexing and searching operations need special handling. This clause is valid only for `FULLTEXT` indexes. See The MySQL Plugin API, for details on creating plugins.

```
- SPATIAL
```

You can create `SPATIAL` indexes on spatial data types. Spatial types are supported only for `MyISAM`tables and indexed columns must be declared as `NOT NULL`. See Section 11.4, “Spatial Data Types”.

```
- FOREIGN KEY
```

MySQL supports foreign keys, which let you cross-reference related data across tables, and foreign key constraints, which help keep this spread-out data consistent. For definition and option information, see

```
reference_definition, and reference_option.
```

Partitioned tables employing the `InnoDB` storage engine do not support foreign keys. See Section 19.6,“Restrictions and Limitations on Partitioning”, for more information.

```
- CHECK
```

The `CHECK` clause is parsed but ignored by all storage engines.

```
- key_part
```

- A `key_part` specification can end with `ASC` or `DESC`. These keywords are permitted for future

extensions for specifying ascending or descending index value storage. Currently, they are parsed but ignored; index values are always stored in ascending order.

- Prefixes, defined by the `length` attribute, can be up to 767 bytes long for `InnoDB` tables or 3072

bytes if the `innodb_large_prefix` option is enabled. For MyISAM tables, the prefix length limit is 1000 bytes.

Prefix limits are measured in bytes. However, prefix lengths for index specifications in `CREATE``TABLE`, `ALTER TABLE`, and `CREATE INDEX` statements are interpreted as number of characters for nonbinary string types (`CHAR`, `VARCHAR`, `TEXT`) and number of bytes for binary string types (`BINARY`,CREATE TABLE Statement`VARBINARY`, `BLOB`). Take this into account when specifying a prefix length for a nonbinary string column that uses a multibyte character set.

```
- index_type
```

Some storage engines permit you to specify an index type when creating an index. The syntax for the`index_type` specifier is `USING type_name`.

Example:

```
CREATE TABLE lookup
(id INT, INDEX USING BTREE (id))
ENGINE = MEMORY;
```

The preferred position for `USING` is after the index column list. It can be given before the column list, but support for use of the option in that position is deprecated; expect it to be removed in a future MySQL release.

```
- index_option
```

`index_option` values specify additional options for an index.

```
- KEY_BLOCK_SIZE
```

For `MyISAM` tables, `KEY_BLOCK_SIZE` optionally specifies the size in bytes to use for index key blocks. The value is treated as a hint; a different size could be used if necessary. A `KEY_BLOCK_SIZE`value specified for an individual index definition overrides the table-level `KEY_BLOCK_SIZE` value.

For information about the table-level `KEY_BLOCK_SIZE` attribute, see Table Options.

```
- WITH PARSER
```

A `WITH PARSER` clause can be specified as an `index_option` value to associate a parser plugin with the index if full-text indexing and searching operations need special handling. This clause is valid only for `FULLTEXT` indexes. See The MySQL Plugin API, for details on creating plugins.

```
- COMMENT
```

Index definitions can include an optional comment of up to 1024 characters.

For more information about permissible `index_option` values, see Section 13.1.13, “CREATE INDEX Statement”. For more information about indexes, see Section 8.3.1, “How MySQL Uses Indexes”.

```
- reference_definition
```

For `reference_definition` syntax details and examples, see Section 13.1.17.5, “FOREIGN KEY Constraints”.

`InnoDB` and `NDB` tables support checking of foreign key constraints. The columns of the referenced table must always be explicitly named. Both `ON DELETE` and `ON UPDATE` actions on foreign keys CREATE TABLE Statement are supported. For more detailed information and examples, see Section 13.1.17.5, “FOREIGN KEY Constraints”.

For other storage engines, MySQL Server parses and ignores the `FOREIGN KEY` syntax in `CREATE``TABLE` statements.

Important For users familiar with the ANSI/ISO SQL Standard, please note that no storage engine, including `InnoDB`, recognizes or enforces the `MATCH` clause used in referential integrity constraint definitions. Use of an explicit `MATCH` clause does not have the specified effect, and also causes `ON DELETE` and `ON UPDATE`clauses to be ignored. For these reasons, specifying `MATCH` should be avoided.

The `MATCH` clause in the SQL standard controls how `NULL` values in a composite(multiple-column) foreign key are handled when comparing to a primary key.

`InnoDB` essentially implements the semantics defined by `MATCH SIMPLE`, which permit a foreign key to be all or partially `NULL`. In that case, the (child table) row containing such a foreign key is permitted to be inserted, and does not match any row in the referenced (parent) table. It is possible to implement other semantics using triggers.

Additionally, MySQL requires that the referenced columns be indexed for performance. However, it does not enforce any requirement that the referenced columns be declared `UNIQUE` or `NOT NULL`. The handling of foreign key references to nonunique keys or keys that contain `NULL` values is not well defined for operations such as `UPDATE` or `DELETE CASCADE`. You are advised to use foreign keys that reference only keys that are both `UNIQUE` (or `PRIMARY`) and

```
NOT NULL.
```

MySQL parses but ignores “inline `REFERENCES` specifications” (as defined in the SQL standard) where the references are defined as part of the column specification. MySQL accepts `REFERENCES` clauses only when specified as part of a separate `FOREIGN KEY` specification. For more information, see Section 1.6.2.3, “FOREIGN KEY Constraint Differences”.

```
- reference_option
```

For information about the `RESTRICT`, `CASCADE`, `SET NULL`, `NO ACTION`, and `SET DEFAULT` options,see Section 13.1.17.5, “FOREIGN KEY Constraints”.

> Table Options

Table options are used to optimize the behavior of the table. In most cases, you do not have to specify any of them. These options apply to all storage engines unless otherwise indicated. Options that do not apply to a given storage engine may be accepted and remembered as part of the table definition. Such options then apply if you later use `ALTER TABLE` to convert the table to use a different storage engine.

```
- ENGINE
```

Specifies the storage engine for the table, using one of the names shown in the following table. The engine name can be unquoted or quoted. The quoted name `'DEFAULT'` is recognized but ignored.

Storage Engine Description`InnoDB` Transaction-safe tables with row locking and foreign keys. The default storage engine for new CREATE TABLE Statement Storage Engine Description tables. See Chapter 14, The InnoDB Storage Engine, and in particular Section 14.1, “Introduction to InnoDB” if you have MySQL experience but are new to `InnoDB`.

`MyISAM` The binary portable storage engine that is primarily used for read-only or read-mostly workloads. See Section 15.2, “The MyISAM Storage Engine”.

`MEMORY` The data for this storage engine is stored only in memory. See Section 15.3, “The MEMORY Storage Engine”.

`CSV` Tables that store rows in comma-separated values format. See Section 15.4, “The CSV Storage Engine”.

`ARCHIVE` The archiving storage engine. See Section 15.5,“The ARCHIVE Storage Engine”.

`EXAMPLE` An example engine. See Section 15.9, “The EXAMPLE Storage Engine”.

`FEDERATED` Storage engine that accesses remote tables. See Section 15.8, “The FEDERATED Storage Engine”.

`HEAP` This is a synonym for `MEMORY`.

`MERGE` A collection of `MyISAM` tables used as one table.

Also known as `MRG_MyISAM`. See Section 15.7,“The MERGE Storage Engine”.

`NDB` Clustered, fault-tolerant, memory-based tables,supporting transactions and foreign keys. Also known as `NDBCLUSTER`. See Chapter 18, MySQL NDB Cluster 7.3 and NDB Cluster 7.4.

If a storage engine is specified that is not available, MySQL uses the default engine instead. Normally,this is `MyISAM`. For example, if a table definition includes the `ENGINE=INNODB` option but the MySQL server does not support `INNODB` tables, the table is created as a `MyISAM` table. This makes it possible to have a replication setup where you have transactional tables on the source but tables created on the replica are nontransactional (to get more speed). In MySQL 5.6, a warning occurs if the storage engine specification is not honored.

Engine substitution can be controlled by the setting of the `NO_ENGINE_SUBSTITUTION` SQL mode, as described in Section 5.1.10, “Server SQL Modes”.

Note The older `TYPE` option that was synonymous with `ENGINE` was removed in MySQL 5.5. When upgrading to MySQL 5.5 or later, you must convert existing applications that rely on `TYPE` to use `ENGINE` instead.

```
- AUTO_INCREMENT
```

The initial `AUTO_INCREMENT` value for the table. In MySQL 5.6, this works for `MyISAM`, `MEMORY`,`InnoDB`, and `ARCHIVE` tables. To set the first auto-increment value for engines that do not support the CREATE TABLE Statement`AUTO_INCREMENT` table option, insert a “dummy” row with a value one less than the desired value after creating the table, and then delete the dummy row.

For engines that support the `AUTO_INCREMENT` table option in `CREATE TABLE` statements, you can also use `ALTER TABLE tbl_name AUTO_INCREMENT = N` to reset the `AUTO_INCREMENT` value. The value cannot be set lower than the maximum value currently in the column.

```
- AVG_ROW_LENGTH
```

An approximation of the average row length for your table. You need to set this only for large tables with variable-size rows.

When you create a `MyISAM` table, MySQL uses the product of the `MAX_ROWS` and `AVG_ROW_LENGTH`options to decide how big the resulting table is. If you don't specify either option, the maximum size for `MyISAM` data and index files is 256TB by default. (If your operating system does not support files that large, table sizes are constrained by the file size limit.) If you want to keep down the pointer sizes to make the index smaller and faster and you don't really need big files, you can decrease the default pointer size by setting the `myisam_data_pointer_size` system variable. (See Section 5.1.7, “Server System Variables”.) If you want all your tables to be able to grow above the default limit and are willing to have your tables slightly slower and larger than necessary, you can increase the default pointer size by setting this variable. Setting the value to 7 permits table sizes up to 65,536TB.

```
- [DEFAULT] CHARACTER SET
```

Specifies a default character set for the table. `CHARSET` is a synonym for `CHARACTER SET`. If the character set name is `DEFAULT`, the database character set is used.

```
- CHECKSUM
```

Set this to 1 if you want MySQL to maintain a live checksum for all rows (that is, a checksum that MySQL updates automatically as the table changes). This makes the table a little slower to update, but also makes it easier to find corrupted tables. The `CHECKSUM TABLE` statement reports the checksum.

(`MyISAM` only.)

```
- [DEFAULT] COLLATE
```

Specifies a default collation for the table.

```
- COMMENT
```

A comment for the table, up to 2048 characters long.

```
- CONNECTION
```

The connection string for a `FEDERATED` table.

Note Older versions of MySQL used a `COMMENT` option for the connection string.

```
- DATA DIRECTORY, INDEX DIRECTORY
```

For `InnoDB`, the `DATA DIRECTORY='directory'` clause permits creating a table outside of the data directory. The `innodb_file_per_table` variable must be enabled to use the `DATA DIRECTORY`CREATE TABLE Statement clause. The full directory path must be specified. For more information, see Section 14.6.1.2, “Creating Tables Externally”.

When creating `MyISAM` tables, you can use the `DATA DIRECTORY='directory'` clause, the `INDEX``DIRECTORY='directory'` clause, or both. They specify where to put a `MyISAM` table's data file and index file, respectively. Unlike `InnoDB` tables, MySQL does not create subdirectories that correspond to the database name when creating a `MyISAM` table with a `DATA DIRECTORY` or `INDEX DIRECTORY`option. Files are created in the directory that is specified.

As of MySQL 5.6.35, you must have the `FILE` privilege to use the `DATA DIRECTORY` or `INDEX``DIRECTORY` table option.

Important Table-level `DATA DIRECTORY` and `INDEX DIRECTORY` options are ignored for partitioned tables. (Bug #32091)These options work only when you are not using the `--skip-symbolic-links` option. Your operating system must also have a working, thread-safe `realpath()` call. See Section 8.12.3.2, “Using Symbolic Links for MyISAM Tables on Unix”, for more complete information.

If a `MyISAM` table is created with no `DATA DIRECTORY` option, the `.MYD` file is created in the database directory. By default, if `MyISAM` finds an existing `.MYD` file in this case, it overwrites it. The same applies to `.MYI` files for tables created with no `INDEX DIRECTORY` option. To suppress this behavior, start the server with the `--keep_files_on_create` option, in which case `MyISAM` does not overwrite existing files and returns an error instead.

If a `MyISAM` table is created with a `DATA DIRECTORY` or `INDEX DIRECTORY` option and an existing`.MYD` or `.MYI` file is found, MyISAM always returns an error. It does not overwrite a file in the specified directory.

Important You cannot use path names that contain the MySQL data directory with `DATA``DIRECTORY` or `INDEX DIRECTORY`. This includes partitioned tables and individual table partitions. (See Bug #32167.)

```
- DELAY_KEY_WRITE
```

Set this to 1 if you want to delay key updates for the table until the table is closed. See the description of the `delay_key_write` system variable in Section 5.1.7, “Server System Variables”. (`MyISAM` only.)

```
- INSERT_METHOD
```

If you want to insert data into a `MERGE` table, you must specify with `INSERT_METHOD` the table into which the row should be inserted. `INSERT_METHOD` is an option useful for `MERGE` tables only. Use a value of `FIRST` or `LAST` to have inserts go to the first or last table, or a value of `NO` to prevent inserts. See Section 15.7, “The MERGE Storage Engine”.

```
- KEY_BLOCK_SIZE
```

For `MyISAM` tables, `KEY_BLOCK_SIZE` optionally specifies the size in bytes to use for index key blocks.

The value is treated as a hint; a different size could be used if necessary. A `KEY_BLOCK_SIZE` value specified for an individual index definition overrides the table-level `KEY_BLOCK_SIZE` value.

For `InnoDB` tables, `KEY_BLOCK_SIZE` specifies the page size in kilobytes to use for compressed`InnoDB` tables. The `KEY_BLOCK_SIZE` value is treated as a hint; a different size could CREATE TABLE Statement be used by `InnoDB` if necessary. `KEY_BLOCK_SIZE` can only be less than or equal to the`innodb_page_size` value. A value of 0 represents the default compressed page size, which is half of the `innodb_page_size` value. Depending on `innodb_page_size`, possible `KEY_BLOCK_SIZE`values include 0, 1, 2, 4, 8, and 16. See InnoDB Table Compression for more information.

Oracle recommends enabling `innodb_strict_mode` when specifying `KEY_BLOCK_SIZE` for `InnoDB`tables. When `innodb_strict_mode` is enabled, specifying an invalid `KEY_BLOCK_SIZE` value returns an error. If `innodb_strict_mode` is disabled, an invalid `KEY_BLOCK_SIZE` value results in a warning,and the `KEY_BLOCK_SIZE` option is ignored.

The `Create_options` column in response to `SHOW TABLE STATUS` reports the originally specified`KEY_BLOCK_SIZE` option, as does `SHOW CREATE TABLE`.

`InnoDB` only supports `KEY_BLOCK_SIZE` at the table level.

```
- MAX_ROWS
```

The maximum number of rows you plan to store in the table. This is not a hard limit, but rather a hint to the storage engine that the table must be able to store at least this many rows.

The `NDB` storage engine treats this value as a maximum. If you plan to create very large NDB Cluster tables (containing millions of rows), you should use this option to insure that `NDB` allocates sufficient number of index slots in the hash table used for storing hashes of the table's primary keys by setting`MAX_ROWS = 2 * rows`, where `rows` is the number of rows that you expect to insert into the table.

The maximum `MAX_ROWS` value is 4294967295; larger values are truncated to this limit.

```
- MIN_ROWS
```

The minimum number of rows you plan to store in the table. The `MEMORY` storage engine uses this option as a hint about memory use.

```
- PACK_KEYS
```

Takes effect only with `MyISAM` tables. Set this option to 1 if you want to have smaller indexes.

This usually makes updates slower and reads faster. Setting the option to 0 disables all packing of keys. Setting it to `DEFAULT` tells the storage engine to pack only long `CHAR`, `VARCHAR`, `BINARY`, or`VARBINARY` columns.

If you do not use `PACK_KEYS`, the default is to pack strings, but not numbers. If you use `PACK_KEYS=1`,numbers are packed as well.

When packing binary number keys, MySQL uses prefix compression:

- Every key needs one extra byte to indicate how many bytes of the previous key are the same for the

next key.

- The pointer to the row is stored in high-byte-first order directly after the key, to improve compression.

This means that if you have many equal keys on two consecutive rows, all following “same” keys usually only take two bytes (including the pointer to the row). Compare this to the ordinary case where the following keys takes `storage_size_for_key + pointer_size` (where the pointer size is usually 4). Conversely, you get a significant benefit from prefix compression only if you have many numbers that are the same. If all keys are totally different, you use one byte more per key, if the key is not a key that can have `NULL` values. (In this case, the packed key length is stored in the same byte that is used to mark if a key is `NULL`.)CREATE TABLE Statement

```
- PASSWORD
```

This option is unused. If you have a need to scramble your `.frm` files and make them unusable to any other MySQL server, please contact our sales department.

```
- ROW_FORMAT
```

Defines the physical format in which the rows are stored.

When creating a table with strict mode disabled, the storage engine's default row format is used if the specified row format is not supported. The actual row format of the table is reported in the `Row_format`column in response to `SHOW TABLE STATUS`. The `Create_options` column shows the row format that was specified in the `CREATE TABLE` statement, as does `SHOW CREATE TABLE`.

Row format choices differ depending on the storage engine used for the table.

For `InnoDB` tables:

- Rows are stored in compact format (`ROW_FORMAT=COMPACT`) by default.
- The noncompact format used in older versions of MySQL can still be requested by specifying

```
ROW_FORMAT=REDUNDANT.
```

- To enable compression for `InnoDB` tables, specify `ROW_FORMAT=COMPRESSED` and follow the

procedures in Section 14.9, “InnoDB Table Compression”.

- For more efficient `InnoDB` storage of data types, especially `BLOB` types, specify

`ROW_FORMAT=DYNAMIC` and follow the procedures in DYNAMIC Row Format. Both the`COMPRESSED` and `DYNAMIC` row formats require creating the table with the configuration settings

```
innodb_file_per_table=1 and innodb_file_format=barracuda.
```

- When you specify a non-default `ROW_FORMAT` clause, consider also enabling the

`innodb_strict_mode` configuration option.

- `ROW_FORMAT=FIXED` is not supported. If `ROW_FORMAT=FIXED` is specified while

`innodb_strict_mode` is disabled, `InnoDB` issues a warning and assumes `ROW_FORMAT=COMPACT`.

If `ROW_FORMAT=FIXED` is specified while `innodb_strict_mode` is enabled, `InnoDB` returns an error.

- For additional information about `InnoDB` row formats, see Section 14.11, “InnoDB Row Formats”.

For `MyISAM` tables, the option value can be `FIXED` or `DYNAMIC` for static or variable-length row format.

`myisampack` sets the type to `COMPRESSED`. See Section 15.2.3, “MyISAM Table Storage Formats”.

```
- STATS_AUTO_RECALC
```

Specifies whether to automatically recalculate persistent statistics for an `InnoDB` table. The value `DEFAULT` causes the persistent statistics setting for the table to be determined by the`innodb_stats_auto_recalc` configuration option. The value 1 causes statistics to be recalculated when 10% of the data in the table has changed. The value 0 prevents automatic recalculation for this table; with this setting, issue an `ANALYZE TABLE` statement to recalculate the statistics after making substantial changes to the table. For more information about the persistent statistics feature, see Section 14.8.11.1, “Configuring Persistent Optimizer Statistics Parameters”.

CREATE TABLE Statement

```
- STATS_PERSISTENT
```

Specifies whether to enable persistent statistics for an `InnoDB` table. The value `DEFAULT` causes the persistent statistics setting for the table to be determined by the `innodb_stats_persistent`configuration option. The value 1 enables persistent statistics for the table, while the value 0 turns off this feature. After enabling persistent statistics through a `CREATE TABLE` or `ALTER TABLE` statement,issue an `ANALYZE TABLE` statement to calculate the statistics, after loading representative data into the table. For more information about the persistent statistics feature, see Section 14.8.11.1, “Configuring Persistent Optimizer Statistics Parameters”.

```
- STATS_SAMPLE_PAGES
```

The number of index pages to sample when estimating cardinality and other statistics for an indexed column, such as those calculated by `ANALYZE TABLE`. For more information, see Section 14.8.11.1,“Configuring Persistent Optimizer Statistics Parameters”.

```
- TABLESPACE
```

The `TABLESPACE` and `STORAGE` table options are employed only with `NDB` tables.

`TABLESPACE ... STORAGE DISK` assigns a table to an NDB Cluster Disk Data tablespace. `STORAGE``DISK` cannot be used in `CREATE TABLE` unless preceded by `TABLESPACE` `tablespace_name`.

For `STORAGE MEMORY`, the tablespace name is optional, thus, you can use `TABLESPACE``tablespace_name STORAGE MEMORY` or simply `STORAGE MEMORY` to specify explicitly that the table is in-memory.

See Section 18.6.11, “NDB Cluster Disk Data Tables”, for more information.

```
- UNION
```

Used to access a collection of identical `MyISAM` tables as one. This works only with `MERGE` tables. See Section 15.7, “The MERGE Storage Engine”.

You must have `SELECT`, `UPDATE`, and `DELETE` privileges for the tables you map to a `MERGE` table.

Note Formerly, all tables used had to be in the same database as the `MERGE` table itself. This restriction no longer applies.

> Table Partitioning

`partition_options` can be used to control partitioning of the table created with `CREATE TABLE`.

Not all options shown in the syntax for `partition_options` at the beginning of this section are available for all partitioning types. Please see the listings for the following individual types for information specific to each type, and see Chapter 19, Partitioning, for more complete information about the workings of and uses for partitioning in MySQL, as well as additional examples of table creation and other statements relating to MySQL partitioning.

Partitions can be modified, merged, added to tables, and dropped from tables. For basic information about the MySQL statements to accomplish these tasks, see Section 13.1.7, “ALTER TABLE Statement”. For more detailed descriptions and examples, see Section 19.3, “Partition Management”.

```
- PARTITION BY
```

CREATE TABLE Statement If used, a `partition_options` clause begins with `PARTITION BY`. This clause contains the function that is used to determine the partition; the function returns an integer value ranging from 1 to `num`,where `num` is the number of partitions. (The maximum number of user-defined partitions which a table may contain is 1024; the number of subpartitions—discussed later in this section—is included in this maximum.)Note The expression (`expr`) used in a `PARTITION BY` clause cannot refer to any columns not in the table being created; such references are specifically not permitted and cause the statement to fail with an error. (Bug #29444)

```
- HASH(expr)
```

Hashes one or more columns to create a key for placing and locating rows. `expr` is an expression using one or more table columns. This can be any valid MySQL expression (including MySQL functions)that yields a single integer value. For example, these are both valid `CREATE TABLE` statements using

```
PARTITION BY HASH:
CREATE TABLE t1 (col1 INT, col2 CHAR(5))
PARTITION BY HASH(col1);
CREATE TABLE t1 (col1 INT, col2 CHAR(5), col3 DATETIME)
PARTITION BY HASH ( YEAR(col3) );
```

You may not use either `VALUES LESS THAN` or `VALUES IN` clauses with `PARTITION BY HASH`.

`PARTITION BY HASH` uses the remainder of `expr` divided by the number of partitions (that is, the modulus). For examples and additional information, see Section 19.2.4, “HASH Partitioning”.

The `LINEAR` keyword entails a somewhat different algorithm. In this case, the number of the partition in which a row is stored is calculated as the result of one or more logical `AND` operations. For discussion and examples of linear hashing, see Section 19.2.4.1, “LINEAR HASH Partitioning”.

```
- KEY(column_list)
```

This is similar to `HASH`, except that MySQL supplies the hashing function so as to guarantee an even data distribution. The `column_list` argument is simply a list of 1 or more table columns (maximum:16). This example shows a simple table partitioned by key, with 4 partitions:

```
CREATE TABLE tk (col1 INT, col2 CHAR(5), col3 DATE)
PARTITION BY KEY(col3)
PARTITIONS 4;
```

For tables that are partitioned by key, you can employ linear partitioning by using the `LINEAR` keyword.

This has the same effect as with tables that are partitioned by `HASH`. That is, the partition number is found using the & operator rather than the modulus (see Section 19.2.4.1, “LINEAR HASH Partitioning”,and Section 19.2.5, “KEY Partitioning”, for details). This example uses linear partitioning by key to distribute data between 5 partitions:

```
CREATE TABLE tk (col1 INT, col2 CHAR(5), col3 DATE)
PARTITION BY LINEAR KEY(col3)
PARTITIONS 5;
```

The `ALGORITHM={1 | 2}` option is supported with `[SUB]PARTITION BY [LINEAR] KEY` beginning with MySQL 5.6.11. `ALGORITHM=1` causes the server to use the same key-hashing functions as MySQL

5.1; `ALGORITHM=2` means that the server employs the key-hashing functions implemented and used by default for new `KEY` partitioned tables in MySQL 5.5 and later. (Partitioned tables created with the CREATE TABLE Statement key-hashing functions employed in MySQL 5.5 and later cannot be used by a MySQL 5.1 server.) Not specifying the option has the same effect as using `ALGORITHM=2`. This option is intended for use chiefly when upgrading or downgrading `[LINEAR] KEY` partitioned tables between MySQL 5.1 and later MySQL versions, or for creating tables partitioned by `KEY` or `LINEAR KEY` on a MySQL 5.5 or later server which can be used on a MySQL 5.1 server. For more information, see Section 13.1.7.1, “ALTER TABLE Partition Operations”.

`mysqldump` in MySQL 5.6.11 and later writes this option encased in versioned comments, like this:

```
CREATE TABLE t1 (a INT)
/*!50100 PARTITION BY KEY */ /*!50611 ALGORITHM = 1 */ /*!50100 ()
PARTITIONS 3 */
```

This causes MySQL 5.6.10 and earlier servers to ignore the option, which would otherwise cause a syntax error in those versions. If you plan to load a dump made on a MySQL 5.5.31 or later MySQL

5.5 server where you use tables that are partitioned or subpartitioned by `KEY` into a MySQL 5.6 server previous to version 5.6.11, be sure to consult Section 2.11.3, “Changes in MySQL 5.6”, before proceeding. (The information found there also applies if you are loading a dump containing `KEY`partitioned or subpartitioned tables made from a MySQL 5.6.11 or later server into a MySQL 5.5.30 or earlier server.)Also in MySQL 5.6.11 and later, `ALGORITHM=1` is shown when necessary in the output of `SHOW``CREATE TABLE` using versioned comments in the same manner as `mysqldump`. `ALGORITHM=2` is always omitted from `SHOW CREATE TABLE` output, even if this option was specified when creating the original table.

You may not use either `VALUES LESS THAN` or `VALUES IN` clauses with `PARTITION BY KEY`.

```
- RANGE(expr)
```

In this case, `expr` shows a range of values using a set of `VALUES LESS THAN` operators. When using range partitioning, you must define at least one partition using `VALUES LESS THAN`. You cannot use`VALUES IN` with range partitioning.

Note For tables partitioned by `RANGE`, `VALUES LESS THAN` must be used with either an integer literal value or an expression that evaluates to a single integer value.

In MySQL 5.6, you can overcome this limitation in a table that is defined using`PARTITION BY RANGE COLUMNS`, as described later in this section.

Suppose that you have a table that you wish to partition on a column containing year values, according to the following scheme.

Partition Number: Years Range:0 1990 and earlier 1 1991 to 1994 2 1995 to 1998 3 1999 to 2002 4 2003 to 2005 5 2006 and later A table implementing such a partitioning scheme can be realized by the `CREATE TABLE` statement shown here:CREATE TABLE Statement

```
CREATE TABLE t1 (
year_col  INT,
some_data INT
)
PARTITION BY RANGE (year_col) (
PARTITION p0 VALUES LESS THAN (1991),
PARTITION p1 VALUES LESS THAN (1995),
PARTITION p2 VALUES LESS THAN (1999),
PARTITION p3 VALUES LESS THAN (2002),
PARTITION p4 VALUES LESS THAN (2006),
PARTITION p5 VALUES LESS THAN MAXVALUE
);
```

`PARTITION ... VALUES LESS THAN ...` statements work in a consecutive fashion. `VALUES LESS``THAN MAXVALUE` works to specify “leftover” values that are greater than the maximum value otherwise specified.

`VALUES LESS THAN` clauses work sequentially in a manner similar to that of the `case` portions of a`switch ... case` block (as found in many programming languages such as C, Java, and PHP). That is, the clauses must be arranged in such a way that the upper limit specified in each successive `VALUES``LESS THAN` is greater than that of the previous one, with the one referencing `MAXVALUE` coming last of all in the list.

```
- RANGE COLUMNS(column_list)
```

This variant on `RANGE` facilitates partition pruning for queries using range conditions on multiple columns(that is, having conditions such as `WHERE a = 1 AND b < 10` or `WHERE a = 1 AND b = 10``AND c < 10`). It enables you to specify value ranges in multiple columns by using a list of columns in the `COLUMNS` clause and a set of column values in each `PARTITION ... VALUES LESS THAN``(value_list)` partition definition clause. (In the simplest case, this set consists of a single column.)The maximum number of columns that can be referenced in the `column_list` and `value_list` is 16.

The `column_list` used in the `COLUMNS` clause may contain only names of columns; each column in the list must be one of the following MySQL data types: the integer types; the string types; and time or date column types. Columns using `BLOB`, `TEXT`, `SET`, `ENUM`, `BIT`, or spatial data types are not permitted;

columns that use floating-point number types are also not permitted. You also may not use functions or arithmetic expressions in the `COLUMNS` clause.

The `VALUES LESS THAN` clause used in a partition definition must specify a literal value for each column that appears in the `COLUMNS()` clause; that is, the list of values used for each `VALUES LESS``THAN` clause must contain the same number of values as there are columns listed in the `COLUMNS`clause. An attempt to use more or fewer values in a `VALUES LESS THAN` clause than there are in the`COLUMNS` clause causes the statement to fail with the error `Inconsistency in usage of column``lists for partitioning...`. You cannot use `NULL` for any value appearing in `VALUES LESS``THAN`. It is possible to use `MAXVALUE` more than once for a given column other than the first, as shown in this example:

```
CREATE TABLE rc (
a INT NOT NULL,
b INT NOT NULL
)
PARTITION BY RANGE COLUMNS(a,b) (
PARTITION p0 VALUES LESS THAN (10,5),
PARTITION p1 VALUES LESS THAN (20,10),
PARTITION p2 VALUES LESS THAN (50,MAXVALUE),
PARTITION p3 VALUES LESS THAN (65,MAXVALUE),
PARTITION p4 VALUES LESS THAN (MAXVALUE,MAXVALUE)
```

CREATE TABLE Statement

```
);
```

Each value used in a `VALUES LESS THAN` value list must match the type of the corresponding column exactly; no conversion is made. For example, you cannot use the string `'1'` for a value that matches a column that uses an integer type (you must use the numeral 1 instead), nor can you use the numeral 1 for a value that matches a column that uses a string type (in such a case, you must use a quoted string:`'1'`).

For more information, see Section 19.2.1, “RANGE Partitioning”, and Section 19.4, “Partition Pruning”.

```
- LIST(expr)
```

This is useful when assigning partitions based on a table column with a restricted set of possible values,such as a state or country code. In such a case, all rows pertaining to a certain state or country can be assigned to a single partition, or a partition can be reserved for a certain set of states or countries. It is similar to `RANGE`, except that only `VALUES IN` may be used to specify permissible values for each partition.

`VALUES IN` is used with a list of values to be matched. For instance, you could create a partitioning scheme such as the following:

```
CREATE TABLE client_firms (
id   INT,
name VARCHAR(35)
)
PARTITION BY LIST (id) (
PARTITION r0 VALUES IN (1, 5, 9, 13, 17, 21),
PARTITION r1 VALUES IN (2, 6, 10, 14, 18, 22),
PARTITION r2 VALUES IN (3, 7, 11, 15, 19, 23),
PARTITION r3 VALUES IN (4, 8, 12, 16, 20, 24)
);
```

When using list partitioning, you must define at least one partition using `VALUES IN`. You cannot use

```
VALUES LESS THAN with PARTITION BY LIST.
```

Note For tables partitioned by `LIST`, the value list used with `VALUES IN` must consist of integer values only. In MySQL 5.6, you can overcome this limitation using partitioning by `LIST COLUMNS`, which is described later in this section.

```
- LIST COLUMNS(column_list)
```

This variant on `LIST` facilitates partition pruning for queries using comparison conditions on multiple columns (that is, having conditions such as `WHERE a = 5 AND b = 5` or `WHERE a = 1 AND b =``10 AND c = 5`). It enables you to specify values in multiple columns by using a list of columns in the`COLUMNS` clause and a set of column values in each `PARTITION ... VALUES IN (value_list)`partition definition clause.

The rules governing regarding data types for the column list used in `LIST COLUMNS(column_list)`and the value list used in `VALUES IN(value_list)` are the same as those for the column list used in `RANGE COLUMNS(column_list)` and the value list used in `VALUES LESS THAN(value_list)`,respectively, except that in the `VALUES IN` clause, `MAXVALUE` is not permitted, and you may use `NULL`.

There is one important difference between the list of values used for `VALUES IN` with `PARTITION``BY LIST COLUMNS` as opposed to when it is used with `PARTITION BY LIST`. When used with`PARTITION BY LIST COLUMNS`, each element in the `VALUES IN` clause must be a set of column values; the number of values in each set must be the same as the number of columns used in the CREATE TABLE Statement`COLUMNS` clause, and the data types of these values must match those of the columns (and occur in the same order). In the simplest case, the set consists of a single column. The maximum number of columns that can be used in the `column_list` and in the elements making up the `value_list` is 16.

The table defined by the following `CREATE TABLE` statement provides an example of a table using `LIST``COLUMNS` partitioning:

```
CREATE TABLE lc (
a INT NULL,
b INT NULL
)
PARTITION BY LIST COLUMNS(a,b) (
PARTITION p0 VALUES IN( (0,0), (NULL,NULL) ),
PARTITION p1 VALUES IN( (0,1), (0,2), (0,3), (1,1), (1,2) ),
PARTITION p2 VALUES IN( (1,0), (2,0), (2,1), (3,0), (3,1) ),
PARTITION p3 VALUES IN( (1,3), (2,2), (2,3), (3,2), (3,3) )
);
- PARTITIONS num
```

The number of partitions may optionally be specified with a `PARTITIONS num` clause, where `num` is the number of partitions. If both this clause and any `PARTITION` clauses are used, `num` must be equal to the total number of any partitions that are declared using `PARTITION` clauses.

Note Whether or not you use a `PARTITIONS` clause in creating a table that is partitioned by `RANGE` or `LIST`, you must still include at least one `PARTITION``VALUES` clause in the table definition (see below).

```
- SUBPARTITION BY
```

A partition may optionally be divided into a number of subpartitions. This can be indicated by using the optional `SUBPARTITION BY` clause. Subpartitioning may be done by `HASH` or `KEY`. Either of these may be `LINEAR`. These work in the same way as previously described for the equivalent partitioning types. (It is not possible to subpartition by `LIST` or `RANGE`.)The number of subpartitions can be indicated using the `SUBPARTITIONS` keyword followed by an integer value.

- Rigorous checking of the value used in `PARTITIONS` or `SUBPARTITIONS` clauses is applied and this

value must adhere to the following rules:

- The value must be a positive, nonzero integer.
- No leading zeros are permitted.
- The value must be an integer literal, and cannot not be an expression. For example, `PARTITIONS`

`0.2E+01` is not permitted, even though `0.2E+01` evaluates to 2. (Bug #15890)CREATE TABLE Statement

```
- partition_definition
```

Each partition may be individually defined using a `partition_definition` clause. The individual parts making up this clause are as follows:

```
- PARTITION partition_name
```

Specifies a logical name for the partition.

```
- VALUES
```

For range partitioning, each partition must include a `VALUES LESS THAN` clause; for list partitioning,you must specify a `VALUES IN` clause for each partition. This is used to determine which rows are to be stored in this partition. See the discussions of partitioning types in Chapter 19, Partitioning, for syntax examples.

```
- [STORAGE] ENGINE
```

The partitioning handler accepts a `[STORAGE] ENGINE` option for both `PARTITION` and`SUBPARTITION`. Currently, the only way in which this can be used is to set all partitions or all subpartitions to the same storage engine, and an attempt to set different storage engines for partitions or subpartitions in the same table raises the error `ERROR 1469 (HY000): The mix of`

```
handlers in the partitions is not permitted in this version of MySQL. We
```

expect to lift this restriction on partitioning in a future MySQL release.

```
- COMMENT
```

An optional `COMMENT` clause may be used to specify a string that describes the partition. Example:

```
COMMENT = 'Data for the years previous to 1999'
```

The maximum length for a partition comment is 1024 characters.

```
- DATA DIRECTORY and INDEX DIRECTORY
```

`DATA DIRECTORY` and `INDEX DIRECTORY` may be used to indicate the directory where, respectively,the data and indexes for this partition are to be stored. Both the `data_dir` and the `index_dir` must be absolute system path names.

As of MySQL 5.6.35, you must have the `FILE` privilege to use the `DATA DIRECTORY` or `INDEX``DIRECTORY` partition option.

Example:

```
CREATE TABLE th (id INT, name VARCHAR(30), adate DATE)
PARTITION BY LIST(YEAR(adate))
(
PARTITION p1999 VALUES IN (1995, 1999, 2003)
DATA DIRECTORY = '/var/appdata/95/data'
INDEX DIRECTORY = '/var/appdata/95/idx',
PARTITION p2000 VALUES IN (1996, 2000, 2004)
DATA DIRECTORY = '/var/appdata/96/data'
INDEX DIRECTORY = '/var/appdata/96/idx',
PARTITION p2001 VALUES IN (1997, 2001, 2005)
DATA DIRECTORY = '/var/appdata/97/data'
INDEX DIRECTORY = '/var/appdata/97/idx',
PARTITION p2002 VALUES IN (1998, 2002, 2006)
DATA DIRECTORY = '/var/appdata/98/data'
INDEX DIRECTORY = '/var/appdata/98/idx'
```

CREATE TABLE Statement

```
);
```

`DATA DIRECTORY` and `INDEX DIRECTORY` behave in the same way as in the `CREATE TABLE`statement's `table_option` clause as used for `MyISAM` tables.

One data directory and one index directory may be specified per partition. If left unspecified, the data and indexes are stored by default in the table's database directory.

On Windows, the `DATA DIRECTORY` and `INDEX DIRECTORY` options are not supported for individual partitions or subpartitions of `MyISAM` tables, and the `INDEX DIRECTORY` option is not supported for individual partitions or subpartitions of `InnoDB` tables. These options are ignored on Windows, except that a warning is generated. (Bug #30459)Note The `DATA DIRECTORY` and `INDEX DIRECTORY` options are ignored for creating partitioned tables if `NO_DIR_IN_CREATE` is in effect. (Bug #24633)

```
- MAX_ROWS and MIN_ROWS
```

May be used to specify, respectively, the maximum and minimum number of rows to be stored in the partition. The values for `max_number_of_rows` and `min_number_of_rows` must be positive integers. As with the table-level options with the same names, these act only as “suggestions” to the server and are not hard limits.

```
- TABLESPACE
```

May be used to designate a tablespace for the partition. Used for NDB Cluster only.

```
- subpartition_definition
```

The partition definition may optionally contain one or more `subpartition_definition` clauses.

Each of these consists at a minimum of the `SUBPARTITION name`, where `name` is an identifier for the subpartition. Except for the replacement of the `PARTITION` keyword with `SUBPARTITION`, the syntax for a subpartition definition is identical to that for a partition definition.

Subpartitioning must be done by `HASH` or `KEY`, and can be done only on `RANGE` or `LIST` partitions. See Section 19.2.6, “Subpartitioning”.

#### 13.1.17.1 Files Created by CREATE TABLE

MySQL represents each table by an `.frm` table format (definition) file in the database directory. The storage engine for the table might create other files as well.

For `InnoDB` tables, the file storage is controlled by the `innodb_file_per_table` configuration option.

For each `InnoDB` table created when this option is turned on, the table data and all associated indexes are stored in a .ibd file located inside the database directory. When this option is turned off, all `InnoDB` tables and indexes are stored in the system tablespace, represented by one or more ibdata* files.

For `MyISAM` tables, the storage engine creates data and index files. Thus, for each `MyISAM` table`tbl_name`, there are three disk files.

File Purpose`tbl_name.frm` Table format (definition) file`tbl_name.MYD` Data file CREATE TABLE Statement File Purpose`tbl_name.MYI` Index file Chapter 15, Alternative Storage Engines, describes what files each storage engine creates to represent tables. If a table name contains special characters, the names for the table files contain encoded versions of those characters as described in Section 9.2.4, “Mapping of Identifiers to File Names”.

Limits Imposed by .frm File Structure As described previously, each table has an `.frm` file that contains the table definition. The server uses the following expression to check some of the table information stored in the file against an upper limit of 64KB:

```
if (info_length+(ulong) create_fields.elements*FCOMP+288+
n_length+int_length+com_length > 65535L || int_count > 255)
```

The portion of the information stored in the `.frm` file that is checked against the expression cannot grow beyond the 64KB limit, so if the table definition reaches this size, no more columns can be added.

The relevant factors in the expression are:

- `info_length` is space needed for “screens.” This is related to MySQL's Unireg heritage.
- `create_fields.elements` is the number of columns.
- `FCOMP` is 17.
- `n_length` is the total length of all column names, including one byte per name as a separator.
- `int_length` is related to the list of values for `ENUM` and `SET` columns. In this context, “int” does not

mean “integer.” It means “interval,” a term that refers collectively to `ENUM` and `SET` columns.

- `int_count` is the number of unique `ENUM` and `SET` definitions.
- `com_length` is the total length of column comments.

The expression just described has several implications for permitted table definitions:

- Using long column names can reduce the maximum number of columns, as can the inclusion of `ENUM` or

`SET` columns, or use of column comments.

- A table can have no more than 255 unique `ENUM` and `SET` definitions. Columns with identical element

lists are considered the same against this limt. For example, if a table contains these two columns, they count as one (not two) toward this limit because the definitions are identical:

```
e1 ENUM('a','b','c')
e2 ENUM('a','b','c')
```

- The sum of the length of element names in the unique `ENUM` and `SET` definitions counts toward the 64KB

limit, so although the theoretical limit on number of elements in a given `ENUM` column is 65,535, the practical limit is less than 3000.

#### 13.1.17.2 CREATE TEMPORARY TABLE Statement

You can use the `TEMPORARY` keyword when creating a table. A `TEMPORARY` table is visible only within the current session, and is dropped automatically when the session is closed. This means that two different sessions can use the same temporary table name without conflicting with each other or with an CREATE TABLE Statement existing non-`TEMPORARY` table of the same name. (The existing table is hidden until the temporary table is dropped.)`CREATE TABLE` causes an implicit commit, except when used with the `TEMPORARY` keyword. See Section 13.3.3, “Statements That Cause an Implicit Commit”.

`TEMPORARY` tables have a very loose relationship with databases (schemas). Dropping a database does not automatically drop any `TEMPORARY` tables created within that database. Also, you can create a`TEMPORARY` table in a nonexistent database if you qualify the table name with the database name in the`CREATE TABLE` statement. In this case, all subsequent references to the table must be qualified with the database name.

To create a temporary table, you must have the `CREATE TEMPORARY TABLES` privilege. After a session has created a temporary table, the server performs no further privilege checks on the table. The creating session can perform any operation on the table, such as `DROP TABLE`, `INSERT`, `UPDATE`, or `SELECT`.

One implication of this behavior is that a session can manipulate its temporary tables even if the current user has no privilege to create them. Suppose that the current user does not have the `CREATE``TEMPORARY TABLES` privilege but is able to execute a definer-context stored procedure that executes with the privileges of a user who does have `CREATE TEMPORARY TABLES` and that creates a temporary table.

While the procedure executes, the session uses the privileges of the defining user. After the procedure returns, the effective privileges revert to those of the current user, which can still see the temporary table and perform any operation on it.

#### 13.1.17.3 CREATE TABLE ... LIKE Statement

Use `CREATE TABLE ... LIKE` to create an empty table based on the definition of another table,including any column attributes and indexes defined in the original table:

```
CREATE TABLE new_tbl LIKE orig_tbl;
```

The copy is created using the same version of the table storage format as the original table. The `SELECT`privilege is required on the original table.

`LIKE` works only for base tables, not for views.

Important You cannot execute `CREATE TABLE` or `CREATE TABLE ... LIKE` while a `LOCK``TABLES` statement is in effect.

`CREATE TABLE ... LIKE` makes the same checks as `CREATE TABLE` and does not just copy the `.frm` file. This means that if the current SQL mode is different from the mode in effect when the original table was created, the table definition might be considered invalid for the new mode and the statement fails.

`CREATE TABLE ... LIKE` does not preserve any `DATA DIRECTORY` or `INDEX DIRECTORY` table options that were specified for the original table, or any foreign key definitions.

If the original table is a `TEMPORARY` table, `CREATE TABLE ... LIKE` does not preserve `TEMPORARY`. To create a `TEMPORARY` destination table, use `CREATE TEMPORARY TABLE ... LIKE`.

#### 13.1.17.4 CREATE TABLE ... SELECT Statement

You can create one table from another by adding a `SELECT` statement at the end of the `CREATE TABLE`statement:CREATE TABLE Statement

```
CREATE TABLE new_tbl [AS] SELECT * FROM orig_tbl;
```

MySQL creates new columns for all elements in the `SELECT`. For example:

```
mysql> CREATE TABLE test (a INT NOT NULL AUTO_INCREMENT,
->        PRIMARY KEY (a), KEY(b))
->        ENGINE=InnoDB SELECT b,c FROM test2;
```

This creates an `InnoDB` table with three columns, a, b, and c. The `ENGINE` option is part of the `CREATE``TABLE` statement, and should not be used following the `SELECT`; this would result in a syntax error. The same is true for other `CREATE TABLE` options such as `CHARSET`.

Notice that the columns from the `SELECT` statement are appended to the right side of the table, not overlapped onto it. Take the following example:

```
mysql> SELECT * FROM foo;
+---+
| n |
+---+
| 1 |
+---+
mysql> CREATE TABLE bar (m INT) SELECT n FROM foo;
Query OK, 1 row affected (0.02 sec)
Records: 1  Duplicates: 0  Warnings: 0
mysql> SELECT * FROM bar;
+------+---+
| m    | n |
+------+---+
| NULL | 1 |
+------+---+
1 row in set (0.00 sec)
```

For each row in table `foo`, a row is inserted in `bar` with the values from `foo` and default values for the new columns.

In a table resulting from `CREATE TABLE ... SELECT`, columns named only in the `CREATE TABLE` part come first. Columns named in both parts or only in the `SELECT` part come after that. The data type of`SELECT` columns can be overridden by also specifying the column in the `CREATE TABLE` part.

If any errors occur while copying the data to the table, it is automatically dropped and not created.

You can precede the `SELECT` by `IGNORE` or `REPLACE` to indicate how to handle rows that duplicate unique key values. With `IGNORE`, rows that duplicate an existing row on a unique key value are discarded. With`REPLACE`, new rows replace rows that have the same unique key value. If neither `IGNORE` nor `REPLACE` is specified, duplicate unique key values result in an error.

Because the ordering of the rows in the underlying `SELECT` statements cannot always be determined,

```
CREATE TABLE ... IGNORE SELECT and CREATE TABLE ... REPLACE SELECT statements are
```

flagged as unsafe for statement-based replication. Such statements produce a warning in the error log when using statement-based mode and are written to the binary log using the row-based format when using `MIXED` mode. See also Section 17.1.2.1, “Advantages and Disadvantages of Statement-Based and Row-Based Replication”.

`CREATE TABLE ... SELECT` does not automatically create any indexes for you. This is done intentionally to make the statement as flexible as possible. If you want to have indexes in the created table,you should specify these before the `SELECT` statement:

```
mysql> CREATE TABLE bar (UNIQUE (n)) SELECT n FROM foo;
```

CREATE TABLE Statement Some conversion of data types might occur. For example, the `AUTO_INCREMENT` attribute is not preserved, and `VARCHAR` columns can become `CHAR` columns. Retrained attributes are `NULL` (or `NOT``NULL`) and, for those columns that have them, `CHARACTER SET`, `COLLATION`, `COMMENT`, and the`DEFAULT` clause.

When creating a table with `CREATE TABLE ... SELECT`, make sure to alias any function calls or expressions in the query. If you do not, the `CREATE` statement might fail or result in undesirable column names.

```
CREATE TABLE artists_and_works
SELECT artist.name, COUNT(work.artist_id) AS number_of_works
FROM artist LEFT JOIN work ON artist.id = work.artist_id
GROUP BY artist.id;
```

You can also explicitly specify the data type for a column in the created table:

```
CREATE TABLE foo (a TINYINT NOT NULL) SELECT b+1 AS a FROM bar;
```

For `CREATE TABLE ... SELECT`, if `IF NOT EXISTS` is given and the destination table already exists,the result is version dependent. Before MySQL 5.5.6, MySQL handles the statement as follows:

- The table definition given in the `CREATE TABLE` part is ignored. No error occurs, even if the definition

does not match that of the existing table. MySQL attempts to insert the rows from the `SELECT` part anyway.

- If there is a mismatch between the number of columns in the table and the number of columns produced

by the `SELECT` part, the selected values are assigned to the rightmost columns. For example, if the table contains n columns and the `SELECT` produces m columns, where m < n, the selected values are assigned to the m rightmost columns in the table. Each of the initial n − m columns is assigned its default value, either that specified explicitly in the column definition or the implicit column data type default if the definition contains no default. If the `SELECT` part produces too many columns (m > n), an error occurs.

- If strict SQL mode is enabled and any of these initial columns do not have an explicit default value, the

statement fails with an error.

The following example illustrates `IF NOT EXISTS` handling:

```
mysql> CREATE TABLE t1 (i1 INT DEFAULT 0, i2 INT, i3 INT, i4 INT);
Query OK, 0 rows affected (0.05 sec)
mysql> CREATE TABLE IF NOT EXISTS t1 (c1 CHAR(10)) SELECT 1, 2;
Query OK, 1 row affected, 1 warning (0.01 sec)
Records: 1  Duplicates: 0  Warnings: 0
mysql> SELECT * FROM t1;
+------+------+------+------+
| i1   | i2   | i3   | i4   |
+------+------+------+------+
|    0 | NULL |    1 |    2 |
+------+------+------+------+
1 row in set (0.00 sec)
```

As of MySQL 5.5.6, handling of `CREATE TABLE IF NOT EXISTS ... SELECT` statements was changed for the case that the destination table already exists. This change also involves a change in MySQL 5.1 beginning with 5.1.51.

- Previously, for `CREATE TABLE IF NOT EXISTS ... SELECT`, MySQL produced a warning that

the table exists, but inserted the rows and wrote the statement to the binary log anyway. By contrast,`CREATE TABLE ... SELECT` (without `IF NOT EXISTS`) failed with an error, but MySQL inserted no rows and did not write the statement to the binary log.

CREATE TABLE Statement

- MySQL now handles both statements the same way when the destination table exists, in that neither

statement inserts rows or is written to the binary log. The difference between them is that MySQL produces a warning when `IF NOT EXISTS` is present and an error when it is not.

This change means that, for the preceding example, the `CREATE TABLE IF NOT EXISTS ... SELECT`statement inserts nothing into the destination table as of MySQL 5.5.6.

This change in handling of `IF NOT EXISTS` results in an incompatibility for statement-based replication from a MySQL 5.1 source with the original behavior and a MySQL 5.5 replica with the new behavior.

Suppose that `CREATE TABLE IF NOT EXISTS ... SELECT` is executed on the source and the destination table exists. The result is that rows are inserted on the source but not on the replica. (Row-based replication does not have this problem.)To address this issue, statement-based binary logging for `CREATE TABLE IF NOT EXISTS ...``SELECT` is changed in MySQL 5.1 as of 5.1.51:

- If the destination table does not exist, there is no change: The statement is logged as is.
- If the destination table does exist, the statement is logged as the equivalent pair of `CREATE TABLE`

`IF NOT EXISTS` and `INSERT ... SELECT` statements. (If the `SELECT` in the original statement is preceded by `IGNORE` or `REPLACE`, the `INSERT` becomes `INSERT IGNORE` or `REPLACE`, respectively.)This change provides forward compatibility for statement-based replication from MySQL 5.1 to 5.5 because when the destination table exists, the rows are inserted on both the source and replica. To take advantage of this compatibility measure, the 5.1 server must be at least 5.1.51 and the 5.5 server must be at least

5.5.6.

To upgrade an existing 5.1-to-5.5 replication scenario, upgrade the source first to 5.1.51 or higher. Note that this differs from the usual replication upgrade advice of upgrading the replica first.

A workaround for applications that wish to achieve the original effect (rows inserted regardless of whether the destination table exists) is to use `CREATE TABLE IF NOT EXISTS` and `INSERT ... SELECT`statements rather than `CREATE TABLE IF NOT EXISTS ... SELECT` statements.

Along with the change just described, the following related change was made: Previously, if an existing view was named as the destination table for `CREATE TABLE IF NOT EXISTS ... SELECT`, rows were inserted into the underlying base table and the statement was written to the binary log. As of MySQL 5.1.51 and 5.5.6, nothing is inserted or logged.

To ensure that the binary log can be used to re-create the original tables, MySQL does not permit concurrent inserts during `CREATE TABLE ... SELECT`.

Important You cannot use `FOR UPDATE` as part of the `SELECT` in a statement such as

```
CREATE TABLE new_table SELECT ... FROM old_table .... If you
```

attempt to do so, the statement fails. This represents a change in behavior from MySQL 5.5 and earlier, which permitted `CREATE TABLE ... SELECT` statements to make changes in tables other than the table being created.

This change can also have implications for statement-based replication from an older source to a MySQL 5.6 or higher replica. See Section 17.4.1.7, “Replication of CREATE TABLE ... SELECT Statements”, for more information.

#### 13.1.17.5 FOREIGN KEY Constraints

MySQL supports foreign keys, which permit cross-referencing related data across tables, and foreign key constraints, which help keep the related data consistent.

CREATE TABLE Statement A foreign key relationship involves a parent table that holds the initial column values, and a child table with column values that reference the parent column values. A foreign key constraint is defined on the child table.

The essential syntax for a defining a foreign key constraint in a `CREATE TABLE` or `ALTER TABLE`statement includes the following:

```
[CONSTRAINT [symbol]] FOREIGN KEY
[index_name] (col_name, ...)
REFERENCES tbl_name (col_name,...)
[ON DELETE reference_option]
[ON UPDATE reference_option]
reference_option:
RESTRICT | CASCADE | SET NULL | NO ACTION | SET DEFAULT
```

Foreign key constraint usage is described under the following topics in this section:

- Identifiers
- Conditions and Restrictions
- Referential Actions
- Foreign Key Constraint Examples
- Adding Foreign Key Constraints
- Dropping Foreign Key Constraints
- Foreign Key Checks
- Foreign Key Definitions and Metadata
- Foreign Key Errors

Identifiers Foreign key constraint naming is governed by the following rules:

- The `CONSTRAINT` `symbol` value is used, if defined.
- If the `CONSTRAINT` `symbol` clause is not defined, or a symbol is not included following the `CONSTRAINT`

keyword:

- For `InnoDB` tables, a constraint name is generated automatically.
- For `NDB` tables, the `FOREIGN KEY` `index_name` value is used, if defined. Otherwise, a constraint

name is generated automatically.

- The `CONSTRAINT symbol` value, if defined, must be unique in the database. A duplicate

`symbol` results in an error similar to: `ERROR 1005 (HY000): Can't create table`

```
'test.fk1' (errno: 121).
```

Table and column identifiers in a `FOREIGN KEY ... REFERENCES` clause can be quoted within backticks(`). Alternatively, double quotation marks (") can be used if the `ANSI_QUOTES` SQL mode is enabled. The`lower_case_table_names` system variable setting is also taken into account.

Conditions and Restrictions Foreign key constraints are subject to the following conditions and restrictions:CREATE TABLE Statement

- Parent and child tables must use the same storage engine, and they cannot be defined as temporary

tables.

- Creating a foreign key constraint requires at least one of the `SELECT`, `INSERT`, `UPDATE`, `DELETE`, or

`REFERENCES` privileges on the parent table as of 5.6.22.

- Corresponding columns in the foreign key and the referenced key must have similar data types. The size

and sign of fixed precision types such as `INTEGER` and `DECIMAL` must be the same. The length of string types need not be the same. For nonbinary (character) string columns, the character set and collation must be the same.

- MySQL supports foreign key references between one column and another within a table. (A column

cannot have a foreign key reference to itself.) In these cases, a “child table record” refers to a dependent record within the same table.

- MySQL requires indexes on foreign keys and referenced keys so that foreign key checks can be fast

and not require a table scan. In the referencing table, there must be an index where the foreign key columns are listed as the first columns in the same order. Such an index is created on the referencing table automatically if it does not exist. This index might be silently dropped later if you create another index that can be used to enforce the foreign key constraint. `index_name`, if given, is used as described previously.

- `InnoDB` permits a foreign key to reference any index column or group of columns. However, in the

referenced table, there must be an index where the referenced columns are the first columns in the same order. Hidden columns that `InnoDB` adds to an index are also considered (see Section 14.6.2.1,“Clustered and Secondary Indexes”).

`NDB` requires an explicit unique key (or primary key) on any column referenced as a foreign key. `InnoDB`does not, which is an extension of standard SQL.

- Index prefixes on foreign key columns are not supported. Consequently, `BLOB` and `TEXT` columns

cannot be included in a foreign key because indexes on those columns must always include a prefix length.

- `InnoDB` does not currently support foreign keys for tables with user-defined partitioning. This includes

both parent and child tables.

This restriction does not apply for `NDB` tables that are partitioned by `KEY` or `LINEAR KEY` (the only user partitioning types supported by the `NDB` storage engine); these may have foreign key references or be the targets of such references.

- A table in a foreign key relationship cannot be altered to use another storage engine. To change the

storage engine, you must drop any foreign key constraints first.

For information about how the MySQL implementation of foreign key constraints differs from the SQL standard, see Section 1.6.2.3, “FOREIGN KEY Constraint Differences”.

Referential Actions When an `UPDATE` or `DELETE` operation affects a key value in the parent table that has matching rows in the child table, the result depends on the referential action specified by `ON UPDATE` and `ON DELETE`subclauses of the `FOREIGN KEY` clause. Referential actions include:

- `CASCADE`: Delete or update the row from the parent table and automatically delete or update the

matching rows in the child table. Both `ON DELETE CASCADE` and `ON UPDATE CASCADE` are supported.

Between two tables, do not define several `ON UPDATE CASCADE` clauses that act on the same column in the parent table or in the child table.

CREATE TABLE Statement Note Cascaded foreign key actions do not activate triggers.

- `SET NULL`: Delete or update the row from the parent table and set the foreign key column or columns

in the child table to `NULL`. Both `ON DELETE SET NULL` and `ON UPDATE SET NULL` clauses are supported.

If you specify a `SET NULL` action, make sure that you have not declared the columns in the child table as `NOT NULL`.

- `RESTRICT`: Rejects the delete or update operation for the parent table. Specifying `RESTRICT` (or `NO`

`ACTION`) is the same as omitting the `ON DELETE` or `ON UPDATE` clause.

- `NO ACTION`: A keyword from standard SQL. In MySQL, equivalent to `RESTRICT`. The MySQL Server

rejects the delete or update operation for the parent table if there is a related foreign key value in the referenced table. Some database systems have deferred checks, and `NO ACTION` is a deferred check.

In MySQL, foreign key constraints are checked immediately, so `NO ACTION` is the same as `RESTRICT`.

- `SET DEFAULT`: This action is recognized by the MySQL parser, but both `InnoDB` and `NDB` reject table

definitions containing `ON DELETE SET DEFAULT` or `ON UPDATE SET DEFAULT` clauses.

For storage engines that support foreign keys, MySQL rejects any `INSERT` or `UPDATE` operation that attempts to create a foreign key value in a child table if there is no matching candidate key value in the parent table.

For an `ON DELETE` or `ON UPDATE` that is not specified, the default action is always `RESTRICT`.

For `NDB` tables, `ON UPDATE CASCADE` is not supported where the reference is to the parent table's primary key.

As of NDB 7.3.25 and NDB 7.4.24: For `NDB` tables, `ON DELETE CASCADE` is not supported where the child table contains one or more columns of any of the `TEXT` or `BLOB` types. (Bug #89511, Bug #27484882)`InnoDB` performs cascading operations using a depth-first search algorithm on the records of the index that corresponds to the foreign key constraint.

Foreign Key Constraint Examples This simple example relates `parent` and `child` tables through a single-column foreign key:

```
CREATE TABLE parent (
id INT NOT NULL,
PRIMARY KEY (id)
) ENGINE=INNODB;
CREATE TABLE child (
id INT,
parent_id INT,
INDEX par_ind (parent_id),
FOREIGN KEY (parent_id)
REFERENCES parent(id)
ON DELETE CASCADE
) ENGINE=INNODB;
```

This is a more complex example in which a `product_order` table has foreign keys for two other tables.

One foreign key references a two-column index in the `product` table. The other references a single-column index in the `customer` table:CREATE TABLE Statement

```
CREATE TABLE product (
category INT NOT NULL, id INT NOT NULL,
price DECIMAL,
PRIMARY KEY(category, id)
)   ENGINE=INNODB;
CREATE TABLE customer (
id INT NOT NULL,
PRIMARY KEY (id)
)   ENGINE=INNODB;
CREATE TABLE product_order (
no INT NOT NULL AUTO_INCREMENT,
product_category INT NOT NULL,
product_id INT NOT NULL,
customer_id INT NOT NULL,
PRIMARY KEY(no),
INDEX (product_category, product_id),
INDEX (customer_id),
FOREIGN KEY (product_category, product_id)
REFERENCES product(category, id)
ON UPDATE CASCADE ON DELETE RESTRICT,
FOREIGN KEY (customer_id)
REFERENCES customer(id)
)   ENGINE=INNODB;
```

Adding Foreign Key Constraints You can add a foreign key constraint to an existing table using the following `ALTER TABLE` syntax:

```
ALTER TABLE tbl_name
ADD [CONSTRAINT [symbol]] FOREIGN KEY
[index_name] (col_name, ...)
REFERENCES tbl_name (col_name,...)
[ON DELETE reference_option]
[ON UPDATE reference_option]
```

The foreign key can be self referential (referring to the same table). When you add a foreign key constraint to a table using `ALTER TABLE`, remember to first create an index on the column(s) referenced by the foreign key.

Dropping Foreign Key Constraints You can drop a foreign key constraint using the following `ALTER TABLE` syntax:

```
ALTER TABLE tbl_name DROP FOREIGN KEY fk_symbol;
```

If the `FOREIGN KEY` clause defined a `CONSTRAINT` name when you created the constraint, you can refer to that name to drop the foreign key constraint. Otherwise, a constraint name was generated internally, and you must use that value. To determine the foreign key constraint name, use `SHOW CREATE TABLE`:

```
mysql> SHOW CREATE TABLE child\G
*************************** 1. row ***************************
Table: child
Create Table: CREATE TABLE `child` (
`id` int(11) DEFAULT NULL,
`parent_id` int(11) DEFAULT NULL,
KEY `par_ind` (`parent_id`),
CONSTRAINT `child_ibfk_1` FOREIGN KEY (`parent_id`)
REFERENCES `parent` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

CREATE TABLE Statement

```
mysql> ALTER TABLE child DROP FOREIGN KEY `child_ibfk_1`;
```

Adding and dropping a foreign key in the same `ALTER TABLE` statement is supported for `ALTER``TABLE ... ALGORITHM=INPLACE`. It is not supported for `ALTER TABLE ... ALGORITHM=COPY`.

Foreign Key Checks In MySQL, InnoDB and NDB tables support checking of foreign key constraints. Foreign key checking is controlled by the `foreign_key_checks` variable, which is enabled by default. Typically, you leave this variable enabled during normal operation to enforce referential integrity. Beginning with MySQL NDB Cluster 7.3.2, the `foreign_key_checks` variable has the same effect on `NDB` tables as it does for`InnoDB` tables. Previously, the setting was ignored for NDB tables and all such checks were enforced (Bug#14095855).

The `foreign_key_checks` variable is dynamic and supports both global and session scopes. For information about using system variables, see Section 5.1.8, “Using System Variables”.

Disabling foreign key checking is useful when:

- Dropping a table that is referenced by a foreign key constraint. A referenced table can only be dropped

after `foreign_key_checks` is disabled. When you drop a table, constraints defined on the table are also dropped.

- Reloading tables in different order than required by their foreign key relationships. For example,

`mysqldump` produces correct definitions of tables in the dump file, including foreign key constraints for child tables. To make it easier to reload dump files for tables with foreign key relationships, `mysqldump`automatically includes a statement in the dump output that disables `foreign_key_checks`. This enables you to import the tables in any order in case the dump file contains tables that are not correctly ordered for foreign keys. Disabling `foreign_key_checks` also speeds up the import operation by avoiding foreign key checks.

- Executing `LOAD DATA` operations, to avoid foreign key checking.
- Performing an `ALTER TABLE` operation on a table that has a foreign key relationship.

When `foreign_key_checks` is disabled, foreign key constraints are ignored, with the following exceptions:

- Recreating a table that was previously dropped returns an error if the table definition does not conform

to the foreign key constraints that reference the table. The table must have the correct column names and types. It must also have indexes on the referenced keys. If these requirements are not satisfied,MySQL returns Error 1005 that refers to errno: 150 in the error message, which means that a foreign key constraint was not correctly formed.

- Altering a table returns an error (errno: 150) if a foreign key definition is incorrectly formed for the altered

table.

- Dropping an index required by a foreign key constraint. The foreign key constraint must be removed

before dropping the index.

- Creating a foreign key constraint where a column references a nonmatching column type.

Disabling `foreign_key_checks` has these additional implications:

- It is permitted to drop a database that contains tables with foreign keys that are referenced by tables

outside the database.

- It is permitted to drop a table with foreign keys referenced by other tables.

CREATE TABLE Statement

- Enabling `foreign_key_checks` does not trigger a scan of table data, which means that rows

added to a table while `foreign_key_checks` is disabled are not checked for consistency when`foreign_key_checks` is re-enabled.

Foreign Key Definitions and Metadata To view a foreign key definition, use `SHOW CREATE TABLE`:

```
mysql> SHOW CREATE TABLE child\G
*************************** 1. row ***************************
Table: child
Create Table: CREATE TABLE `child` (
`id` int(11) DEFAULT NULL,
`parent_id` int(11) DEFAULT NULL,
KEY `par_ind` (`parent_id`),
CONSTRAINT `child_ibfk_1` FOREIGN KEY (`parent_id`)
REFERENCES `parent` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

You can obtain information about foreign keys from the Information Schema `KEY_COLUMN_USAGE` table.

An example of a query against this table is shown here:

```
mysql> SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE REFERENCED_TABLE_SCHEMA IS NOT NULL;
+--------------+------------+-------------+-----------------+
| TABLE_SCHEMA | TABLE_NAME | COLUMN_NAME | CONSTRAINT_NAME |
+--------------+------------+-------------+-----------------+
| test         | child      | parent_id   | child_ibfk_1    |
+--------------+------------+-------------+-----------------+
```

You can obtain information specific to `InnoDB` foreign keys from the `INNODB_SYS_FOREIGN` and`INNODB_SYS_FOREIGN_COLS` tables. Example queries are show here:

```
mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_FOREIGN \G
*************************** 1. row ***************************
ID: test/child_ibfk_1
FOR_NAME: test/child
REF_NAME: test/parent
N_COLS: 1
TYPE: 1
mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_FOREIGN_COLS \G
*************************** 1. row ***************************
ID: test/child_ibfk_1
FOR_COL_NAME: parent_id
REF_COL_NAME: id
POS: 0
```

Foreign Key Errors In the event of a foreign key error involving `InnoDB` tables (usually Error 150 in the MySQL Server),information about the latest foreign key error can be obtained by checking `SHOW ENGINE INNODB``STATUS` output.

```
mysql> SHOW ENGINE INNODB STATUS\G
...
------------------------
LATEST FOREIGN KEY ERROR
------------------------
2014-10-17 09:51:31 7f47bcde6700 Transaction:
TRANSACTION 436786, ACTIVE 0 sec inserting
mysql tables in use 1, locked 1
4 lock struct(s), heap size 1184, 3 row lock(s), undo log entries 3
```

CREATE TABLE Statement

```
MySQL thread id 1, OS thread handle 0x7f47bcde6700, query id 96 localhost
root update
INSERT INTO child VALUES
(NULL, 1)
, (NULL, 2)
, (NULL, 3)
, (NULL, 4)
, (NULL, 5)
, (NULL, 6)
Foreign key constraint fails for table `mysql`.`child`:
,
CONSTRAINT `child_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `parent`
(`id`)
ON DELETE CASCADE ON UPDATE CASCADE
Trying to add in child table, in index `par_ind` tuple:
DATA TUPLE: 2 fields;
0: len 4; hex 80000003; asc     ;;
1: len 4; hex 80000003; asc     ;;
But in parent table `mysql`.`parent`, in index `PRIMARY`,
the closest match we can find is record:
PHYSICAL RECORD: n_fields 3; compact format; info bits 0
0: len 4; hex 80000004; asc     ;;
1: len 6; hex 00000006aa26; asc      &;;
2: len 7; hex 9d000001610137; asc     a 7;;
------------------------
LATEST DETECTED DEADLOCK
------------------------
2014-10-17 09:52:38 7f47bcde6700
*** (1) TRANSACTION:
TRANSACTION 436801, ACTIVE 12 sec starting index read
mysql tables in use 1, locked 1
LOCK WAIT 2 lock struct(s), heap size 360, 1 row lock(s)
MySQL thread id 2, OS thread handle 0x7f47bcda5700, query id 102 localhost
root updating
DELETE FROM t WHERE i = 1
*** (1) WAITING FOR THIS LOCK TO BE GRANTED:
RECORD LOCKS space id 3693 page no 3 n bits 72 index `GEN_CLUST_INDEX` of
table `mysql`.`t` trx id 436801 lock_mode X waiting
Record lock, heap no 2 PHYSICAL RECORD: n_fields 4; compact format; info
bits 0
0: len 6; hex 000000003a00; asc     : ;;
1: len 6; hex 00000006aa3f; asc      ?;;
2: len 7; hex ad0000021d0110; asc        ;;
3: len 4; hex 80000001; asc     ;;
...
```

Warning`ER_NO_REFERENCED_ROW_2` and `ER_ROW_IS_REFERENCED_2` error messages for foreign key operations expose information about parent tables, even if the user has no parent table access privileges. To hide information about parent tables,include the appropriate condition handlers in application code and stored programs.

#### 13.1.17.6 Silent Column Specification Changes

In some cases, MySQL silently changes column specifications from those given in a `CREATE TABLE` or`ALTER TABLE` statement. These might be changes to a data type, to attributes associated with a data type, or to an index specification.

All changes are subject to the internal row-size limit of 65,535 bytes, which may cause some attempts at data type changes to fail. See Section 8.4.7, “Limits on Table Column Count and Row Size”.

- Columns that are part of a `PRIMARY KEY` are made `NOT NULL` even if not declared that way.

CREATE TABLE Statement

- Trailing spaces are automatically deleted from `ENUM` and `SET` member values when the table is created.
- MySQL maps certain data types used by other SQL database vendors to MySQL types. See

Section 11.8, “Using Data Types from Other Database Engines”.

- If you include a `USING` clause to specify an index type that is not permitted for a given storage engine,

but there is another index type available that the engine can use without affecting query results, the engine uses the available type.

- If strict SQL mode is not enabled, a `VARCHAR` column with a length specification greater than 65535

is converted to `TEXT`, and a `VARBINARY` column with a length specification greater than 65535 is converted to `BLOB`. Otherwise, an error occurs in either of these cases.

- Specifying the `CHARACTER SET binary` attribute for a character data type causes the column

to be created as the corresponding binary data type: `CHAR` becomes `BINARY`, `VARCHAR` becomes`VARBINARY`, and `TEXT` becomes `BLOB`. For the `ENUM` and `SET` data types, this does not occur; they are created as declared. Suppose that you specify a table using this definition:

```
CREATE TABLE t
(
c1 VARCHAR(10) CHARACTER SET binary,
c2 TEXT CHARACTER SET binary,
c3 ENUM('a','b','c') CHARACTER SET binary
);
```

The resulting table has this definition:

```
CREATE TABLE t
(
c1 VARBINARY(10),
c2 BLOB,
c3 ENUM('a','b','c') CHARACTER SET binary
);
```

To see whether MySQL used a data type other than the one you specified, issue a `DESCRIBE` or `SHOW``CREATE TABLE` statement after creating or altering the table.

Certain other data type changes can occur if you compress a table using `myisampack`. See Section 15.2.3.3, “Compressed Table Characteristics”.

#### 13.1.17.7 Setting NDB Comment Options

In NDB Cluster, a column comment in a `CREATE TABLE` or `ALTER TABLE` statement can also be used to specify an `NDB_COLUMN` option. NDB 7.3 and 7.4 support a single column comment option`MAX_BLOB_PART_SIZE`; syntax for this option is shown here:

```
COMMENT 'NDB_COLUMN=MAX_BLOB_PART_SIZE[={0|1}]'
```

The = sign and the value following it are optional. Using any value other than 0 or 1 results in a syntax error.

The effect of this option is to set the blob part size of a `TEXT` or `BLOB` column to the maximum number of bytes supported for this by `NDB` (13948). This option can be applied to any blob column type supported by MySQL except `TINYBLOB` or `TINYTEXT` (`BLOB`, `MEDIUMBLOB`, `LONGBLOB`, `TEXT`, `MEDIUMTEXT`, or

```
LONGTEXT).
```

To see the effects of this option, we first run the following SQL statement in the `mysql` client to create a table with two `BLOB` columns, one (`c1`) with no extra options, and another (`c2`) with

```
MAX_BLOB_PART_SIZE:
```

CREATE TABLE Statement

```
mysql> CREATE TABLE test.t (
->   p INT PRIMARY KEY,
->   c1 BLOB,
->   c2 BLOB COMMENT 'NDB_COLUMN=MAX_BLOB_PART_SIZE'
-> ) ENGINE NDB;
Query OK, 0 rows affected (0.32 sec)
```

From the system shell, run the `ndb_desc` utility to obtain information about the table just created, as shown in this example:

```
$> ndb_desc -d test t
-- t --
Version: 1
Fragment type: HashMapPartition
K Value: 6
Min load factor: 78
Max load factor: 80
Temporary table: no
Number of attributes: 3
Number of primary keys: 1
Length of frm data: 324
Row Checksum: 1
Row GCI: 1
SingleUserMode: 0
ForceVarPart: 1
FragmentCount: 2
ExtraRowGciBits: 0
ExtraRowAuthorBits: 0
TableStatus: Retrieved
HashMap: DEFAULT-HASHMAP-3840-2
-- Attributes --
p Int PRIMARY KEY DISTRIBUTION KEY AT=FIXED ST=MEMORY
c1 Blob(256,2000,0) NULL AT=MEDIUM_VAR ST=MEMORY BV=2 BT=NDB$BLOB_22_1
c2 Blob(256,13948,0) NULL AT=MEDIUM_VAR ST=MEMORY BV=2 BT=NDB$BLOB_22_2
-- Indexes --
PRIMARY KEY(p) - UniqueHashIndex
PRIMARY(p) - OrderedIndex
```

Column information in the output is listed under `Attributes`; for columns `c1` and `c2` it is displayed here in emphasized text. For `c1`, the blob part size is 2000, the default value; for `c2`, it is 13948, as set by

```
MAX_BLOB_PART_SIZE.
```

You can change the blob part size for a given blob column of an `NDB` table using an `ALTER TABLE`statement such as this one, and verifying the changes afterwards using `SHOW CREATE TABLE`:

```
mysql> ALTER TABLE test.t
->    DROP COLUMN c1,
->     ADD COLUMN c1 BLOB COMMENT 'NDB_COLUMN=MAX_BLOB_PART_SIZE',
->     CHANGE COLUMN c2 c2 BLOB AFTER c1;
Query OK, 0 rows affected (0.47 sec)
Records: 0  Duplicates: 0  Warnings: 0
mysql> SHOW CREATE TABLE test.t\G
*************************** 1. row ***************************
Table: t
Create Table: CREATE TABLE `t` (
`p` int(11) NOT NULL,
`c1` blob COMMENT 'NDB_COLUMN=MAX_BLOB_PART_SIZE',
`c2` blob,
PRIMARY KEY (`p`)
) ENGINE=ndbcluster DEFAULT CHARSET=latin1
1 row in set (0.00 sec)
mysql> EXIT
Bye
```

CREATE TABLESPACE Statement The output of `ndb_desc` shows that the blob part sizes of the columns have been changed as expected:

```
$> ndb_desc -d test t
-- t --
Version: 16777220
Fragment type: HashMapPartition
K Value: 6
Min load factor: 78
Max load factor: 80
Temporary table: no
Number of attributes: 3
Number of primary keys: 1
Length of frm data: 324
Row Checksum: 1
Row GCI: 1
SingleUserMode: 0
ForceVarPart: 1
FragmentCount: 2
ExtraRowGciBits: 0
ExtraRowAuthorBits: 0
TableStatus: Retrieved
HashMap: DEFAULT-HASHMAP-3840-2
-- Attributes --
p Int PRIMARY KEY DISTRIBUTION KEY AT=FIXED ST=MEMORY
c1 Blob(256,13948,0) NULL AT=MEDIUM_VAR ST=MEMORY BV=2 BT=NDB$BLOB_26_1
c2 Blob(256,2000,0) NULL AT=MEDIUM_VAR ST=MEMORY BV=2 BT=NDB$BLOB_26_2
-- Indexes --
PRIMARY KEY(p) - UniqueHashIndex
PRIMARY(p) - OrderedIndex
NDBT_ProgramExit: 0 - OK
```

Changing a column's blob part size must be done using a copying `ALTER TABLE`; this operation cannot be performed online (see Section 18.6.12, “Online Operations with ALTER TABLE in NDB Cluster”).

For more information about how `NDB` stores columns of blob types, see String Type Storage Requirements.

### 13.1.18 CREATE TABLESPACE Statement

```
CREATE TABLESPACE tablespace_name
ADD DATAFILE 'file_name'
USE LOGFILE GROUP logfile_group
[EXTENT_SIZE [=] extent_size]
[INITIAL_SIZE [=] initial_size]
[AUTOEXTEND_SIZE [=] autoextend_size]
[MAX_SIZE [=] max_size]
[NODEGROUP [=] nodegroup_id]
[WAIT]
[COMMENT [=] comment_text]
ENGINE [=] engine_name
```

This statement is used to create a tablespace, which can contain one or more data files, providing storage space for tables. One data file is created and added to the tablespace using this statement. Additional data files may be added to the tablespace by using the `ALTER TABLESPACE` statement (see Section 13.1.8,“ALTER TABLESPACE Statement”). For rules covering the naming of tablespaces, see Section 9.2,“Schema Object Names”.

Note All NDB Cluster Disk Data objects share the same namespace. This means that each Disk Data object must be uniquely named (and not merely each Disk Data object of a given type). For example, you cannot have a tablespace and a log file group with the same name, or a tablespace and a data file with the same name.

CREATE TABLESPACE Statement A log file group of one or more `UNDO` log files must be assigned to the tablespace to be created with the`USE LOGFILE GROUP` clause. `logfile_group` must be an existing log file group created with `CREATE``LOGFILE GROUP` (see Section 13.1.14, “CREATE LOGFILE GROUP Statement”). Multiple tablespaces may use the same log file group for `UNDO` logging.

The `EXTENT_SIZE` sets the size, in bytes, of the extents used by any files belonging to the tablespace.

The default value is 1M. The minimum size is 32K, and theoretical maximum is 2G, although the practical maximum size depends on a number of factors. In most cases, changing the extent size does not have any measurable effect on performance, and the default value is recommended for all but the most unusual situations.

An extent is a unit of disk space allocation. One extent is filled with as much data as that extent can contain before another extent is used. In theory, up to 65,535 (64K) extents may used per data file; however, the recommended maximum is 32,768 (32K). The recommended maximum size for a single data file is 32G—that is, 32K extents × 1 MB per extent. In addition, once an extent is allocated to a given partition, it cannot be used to store data from a different partition; an extent cannot store data from more than one partition.

This means, for example that a tablespace having a single datafile whose `INITIAL_SIZE` is 256 MB and whose `EXTENT_SIZE` is 128M has just two extents, and so can be used to store data from at most two different disk data table partitions.

You can see how many extents remain free in a given data file by querying the Information Schema `FILES`table, and so derive an estimate for how much space remains free in the file. For further discussion and examples, see Section 21.5.1, “The INFORMATION_SCHEMA FILES Table”.

The `INITIAL_SIZE` parameter sets the data file's total size in bytes. Once the file has been created,its size cannot be changed; however, you can add more data files to the tablespace using `ALTER``TABLESPACE ... ADD DATAFILE`. See Section 13.1.8, “ALTER TABLESPACE Statement”.

`INITIAL_SIZE` is optional; its default value is 134217728 (128 MB).

On 32-bit systems, the maximum supported value for `INITIAL_SIZE` is 4294967296 (4 GB). (Bug#29186)When setting `EXTENT_SIZE`, you may optionally follow the number with a one-letter abbreviation for an order of magnitude, similar to those used in `my.cnf`. Generally, this is one of the letters M (for megabytes)or G (for gigabytes). In MySQL NDB Cluster 7.3.2 and later, these abbreviations are also supported when specifying `INITIAL_SIZE` as well. (Bug #13116514, Bug #16104705, Bug #62858)`INITIAL_SIZE`, `EXTENT_SIZE`, and `UNDO_BUFFER_SIZE` are subject to rounding as follows:

- `EXTENT_SIZE` and `UNDO_BUFFER_SIZE` are each rounded up to the nearest whole multiple of 32K.
- `INITIAL_SIZE` is rounded down to the nearest whole multiple of 32K.

For data files, INITIAL_SIZE is subject to further rounding; the result just obtained is rounded up to the nearest whole multiple of `EXTENT_SIZE` (after any rounding).

The rounding just described is done explicitly, and a warning is issued by the MySQL Server when any such rounding is performed. The rounded values are also used by the NDB kernel for calculating`INFORMATION_SCHEMA.FILES` column values and other purposes. However, to avoid an unexpected result, we suggest that you always use whole multiples of 32K in specifying these options.

`AUTOEXTEND_SIZE`, `MAX_SIZE`, `NODEGROUP`, `WAIT`, and `COMMENT` are parsed but ignored, and so currently have no effect. These options are intended for future expansion.

The `ENGINE` parameter determines the storage engine which uses this tablespace, with `engine_name`being the name of the storage engine. Currently, `engine_name` must be one of the values `NDB` or

```
NDBCLUSTER.
```

CREATE TRIGGER Statement When `CREATE TABLESPACE` is used with `ENGINE = NDB`, a tablespace and associated data file are created on each Cluster data node. You can verify that the data files were created and obtain information about them by querying the Information Schema `FILES` table. For example:

```
mysql> SELECT LOGFILE_GROUP_NAME, FILE_NAME, EXTRA
-> FROM INFORMATION_SCHEMA.FILES
-> WHERE TABLESPACE_NAME = 'newts' AND FILE_TYPE = 'DATAFILE';
+--------------------+-------------+----------------+
| LOGFILE_GROUP_NAME | FILE_NAME   | EXTRA          |
+--------------------+-------------+----------------+
| lg_3               | newdata.dat | CLUSTER_NODE=3 |
| lg_3               | newdata.dat | CLUSTER_NODE=4 |
+--------------------+-------------+----------------+
2 rows in set (0.01 sec)
```

(See Section 21.5.1, “The INFORMATION_SCHEMA FILES Table”.)`CREATE TABLESPACE` is useful only with Disk Data storage for NDB Cluster. See Section 18.6.11, “NDB Cluster Disk Data Tables”.

### 13.1.19 CREATE TRIGGER Statement

```
CREATE
[DEFINER = user]
TRIGGER trigger_name
trigger_time trigger_event
ON tbl_name FOR EACH ROW
trigger_body
trigger_time: { BEFORE | AFTER }
trigger_event: { INSERT | UPDATE | DELETE }
```

This statement creates a new trigger. A trigger is a named database object that is associated with a table,and that activates when a particular event occurs for the table. The trigger becomes associated with the table named `tbl_name`, which must refer to a permanent table. You cannot associate a trigger with a`TEMPORARY` table or a view.

Trigger names exist in the schema namespace, meaning that all triggers must have unique names within a schema. Triggers in different schemas can have the same name.

This section describes `CREATE TRIGGER` syntax. For additional discussion, see Section 20.3.1, “Trigger Syntax and Examples”.

`CREATE TRIGGER` requires the `TRIGGER` privilege for the table associated with the trigger. If the `DEFINER`clause is present, the privileges required depend on the `user` value, as discussed in Section 20.6, “Stored Object Access Control”. If binary logging is enabled, `CREATE TRIGGER` might require the `SUPER` privilege,as discussed in Section 20.7, “Stored Program Binary Logging”.

The `DEFINER` clause determines the security context to be used when checking access privileges at trigger activation time, as described later in this section.

`trigger_time` is the trigger action time. It can be `BEFORE` or `AFTER` to indicate that the trigger activates before or after each row to be modified.

Basic column value checks occur prior to trigger activation, so you cannot use `BEFORE` triggers to convert values inappropriate for the column type to valid values.

`trigger_event` indicates the kind of operation that activates the trigger. These `trigger_event` values are permitted:CREATE TRIGGER Statement

- `INSERT`: The trigger activates whenever a new row is inserted into the table (for example, through

`INSERT`, `LOAD DATA`, and `REPLACE` statements).

- `UPDATE`: The trigger activates whenever a row is modified (for example, through `UPDATE` statements).
- `DELETE`: The trigger activates whenever a row is deleted from the table (for example, through `DELETE`

and `REPLACE` statements). `DROP TABLE` and `TRUNCATE TABLE` statements on the table do not activate this trigger, because they do not use `DELETE`. Dropping a partition does not activate `DELETE` triggers,either.

The `trigger_event` does not represent a literal type of SQL statement that activates the trigger so much as it represents a type of table operation. For example, an `INSERT` trigger activates not only for `INSERT`statements but also `LOAD DATA` statements because both statements insert rows into a table.

A potentially confusing example of this is the `INSERT INTO ... ON DUPLICATE KEY UPDATE ...`syntax: a `BEFORE INSERT` trigger activates for every row, followed by either an `AFTER INSERT` trigger or both the `BEFORE UPDATE` and `AFTER UPDATE` triggers, depending on whether there was a duplicate key for the row.

Note Cascaded foreign key actions do not activate triggers.

There cannot be multiple triggers for a given table that have the same trigger event and action time. For example, you cannot have two `BEFORE UPDATE` triggers for a table. But you can have a `BEFORE UPDATE`and a `BEFORE INSERT` trigger, or a `BEFORE UPDATE` and an `AFTER UPDATE` trigger.

`trigger_body` is the statement to execute when the trigger activates. To execute multiple statements,use the `BEGIN ... END` compound statement construct. This also enables you to use the same statements that are permissible within stored routines. See Section 13.6.1, “BEGIN ... END Compound Statement”. Some statements are not permitted in triggers; see Section 20.8, “Restrictions on Stored Programs”.

Within the trigger body, you can refer to columns in the subject table (the table associated with the trigger)by using the aliases `OLD` and `NEW`. `OLD.col_name` refers to a column of an existing row before it is updated or deleted. `NEW.col_name` refers to the column of a new row to be inserted or an existing row after it is updated.

MySQL stores the `sql_mode` system variable setting in effect when a trigger is created, and always executes the trigger body with this setting in force, regardless of the current server SQL mode when the trigger begins executing.

The `DEFINER` clause specifies the MySQL account to be used when checking access privileges at trigger activation time. If the `DEFINER` clause is present, the `user` value should be a MySQL account specified as `'user_name'@'host_name'`, `CURRENT_USER`, or `CURRENT_USER()`. The permitted `user` values depend on the privileges you hold, as discussed in Section 20.6, “Stored Object Access Control”. Also see that section for additional information about trigger security.

If the `DEFINER` clause is omitted, the default definer is the user who executes the `CREATE TRIGGER`statement. This is the same as specifying `DEFINER = CURRENT_USER` explicitly.

MySQL takes the `DEFINER` user into account when checking trigger privileges as follows:

- At `CREATE TRIGGER` time, the user who issues the statement must have the `TRIGGER` privilege.
- At trigger activation time, privileges are checked against the `DEFINER` user. This user must have these

privileges:CREATE VIEW Statement

- The `TRIGGER` privilege for the subject table.
- The `SELECT` privilege for the subject table if references to table columns occur using `OLD.col_name`

or `NEW.col_name` in the trigger body.

- The `UPDATE` privilege for the subject table if table columns are targets of `SET NEW.col_name =`

`value` assignments in the trigger body.

- Whatever other privileges normally are required for the statements executed by the trigger.

Within a trigger body, the `CURRENT_USER` function returns the account used to check privileges at trigger activation time. This is the `DEFINER` user, not the user whose actions caused the trigger to be activated.

For information about user auditing within triggers, see Section 6.2.15, “SQL-Based Account Activity Auditing”.

If you use `LOCK TABLES` to lock a table that has triggers, the tables used within the trigger are also locked,as described in LOCK TABLES and Triggers.

For additional discussion of trigger use, see Section 20.3.1, “Trigger Syntax and Examples”.

### 13.1.20 CREATE VIEW Statement

```
CREATE
[OR REPLACE]
[ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
[DEFINER = user]
[SQL SECURITY { DEFINER | INVOKER }]
VIEW view_name [(column_list)]
AS select_statement
[WITH [CASCADED | LOCAL] CHECK OPTION]
```

The `CREATE VIEW` statement creates a new view, or replaces an existing view if the `OR REPLACE` clause is given. If the view does not exist, `CREATE OR REPLACE VIEW` is the same as `CREATE VIEW`. If the view does exist, `CREATE OR REPLACE VIEW` replaces it.

For information about restrictions on view use, see Section 20.9, “Restrictions on Views”.

The `select_statement` is a `SELECT` statement that provides the definition of the view. (Selecting from the view selects, in effect, using the `SELECT` statement.) The `select_statement` can select from base tables or other views.

The view definition is “frozen” at creation time and is not affected by subsequent changes to the definitions of the underlying tables. For example, if a view is defined as `SELECT *` on a table, new columns added to the table later do not become part of the view, and columns dropped from the table result in an error when selecting from the view.

The `ALGORITHM` clause affects how MySQL processes the view. The `DEFINER` and `SQL SECURITY`clauses specify the security context to be used when checking access privileges at view invocation time. The `WITH CHECK OPTION` clause can be given to constrain inserts or updates to rows in tables referenced by the view. These clauses are described later in this section.

The `CREATE VIEW` statement requires the `CREATE VIEW` privilege for the view, and some privilege for each column selected by the `SELECT` statement. For columns used elsewhere in the `SELECT` statement,you must have the `SELECT` privilege. If the `OR REPLACE` clause is present, you must also have the `DROP`privilege for the view. If the `DEFINER` clause is present, the privileges required depend on the `user` value,as discussed in Section 20.6, “Stored Object Access Control”.

CREATE VIEW Statement When a view is referenced, privilege checking occurs as described later in this section.

A view belongs to a database. By default, a new view is created in the default database. To create the view explicitly in a given database, use `db_name.view_name` syntax to qualify the view name with the database name:

```
CREATE VIEW test.v AS SELECT * FROM t;
```

Unqualified table or view names in the `SELECT` statement are also interpreted with respect to the default database. A view can refer to tables or views in other databases by qualifying the table or view name with the appropriate database name.

Within a database, base tables and views share the same namespace, so a base table and a view cannot have the same name.

Columns retrieved by the `SELECT` statement can be simple references to table columns, or expressions that use functions, constant values, operators, and so forth.

A view must have unique column names with no duplicates, just like a base table. By default, the names of the columns retrieved by the `SELECT` statement are used for the view column names. To define explicit names for the view columns, specify the optional `column_list` clause as a list of comma-separated identifiers. The number of names in `column_list` must be the same as the number of columns retrieved by the `SELECT` statement.

A view can be created from many kinds of `SELECT` statements. It can refer to base tables or other views. It can use joins, `UNION`, and subqueries. The `SELECT` need not even refer to any tables:

```
CREATE VIEW v_today (today) AS SELECT CURRENT_DATE;
```

The following example defines a view that selects two columns from another table as well as an expression calculated from those columns:

```
mysql> CREATE TABLE t (qty INT, price INT);
mysql> INSERT INTO t VALUES(3, 50);
mysql> CREATE VIEW v AS SELECT qty, price, qty*price AS value FROM t;
mysql> SELECT * FROM v;
+------+-------+-------+
| qty  | price | value |
+------+-------+-------+
|    3 |    50 |   150 |
+------+-------+-------+
```

A view definition is subject to the following restrictions:

- The `SELECT` statement cannot contain a subquery in the `FROM` clause.
- The `SELECT` statement cannot refer to system variables or user-defined variables.
- Within a stored program, the `SELECT` statement cannot refer to program parameters or local variables.
- The `SELECT` statement cannot refer to prepared statement parameters.
- Any table or view referred to in the definition must exist. If, after the view has been created, a table or

view that the definition refers to is dropped, use of the view results in an error. To check a view definition for problems of this kind, use the `CHECK TABLE` statement.

- The definition cannot refer to a `TEMPORARY` table, and you cannot create a `TEMPORARY` view.
- You cannot associate a trigger with a view.

CREATE VIEW Statement

- Aliases for column names in the `SELECT` statement are checked against the maximum column length of

64 characters (not the maximum alias length of 256 characters).

`ORDER BY` is permitted in a view definition, but it is ignored if you select from a view using a statement that has its own `ORDER BY` or filtering or grouping. When `ORDER BY` is combined with `LIMIT` or `OFFSET` in a view definition, the ordering is always enforced before the query result is used by the outer query, but it does not guarantee that the same ordering is used in the end result. As a workaround, add an `ORDER BY`clause to the outer query.

For other options or clauses in the definition, they are added to the options or clauses of the statement that references the view, but the effect is undefined. For example, if a view definition includes a `LIMIT` clause,and you select from the view using a statement that has its own `LIMIT` clause, it is undefined which limit applies. This same principle applies to options such as `ALL`, `DISTINCT`, or `SQL_SMALL_RESULT` that follow the `SELECT` keyword, and to clauses such as `INTO`, `FOR UPDATE`, `LOCK IN SHARE MODE`, and

```
PROCEDURE.
```

The results obtained from a view may be affected if you change the query processing environment by changing system variables:

```
mysql> CREATE VIEW v (mycol) AS SELECT 'abc';
Query OK, 0 rows affected (0.01 sec)
mysql> SET sql_mode = '';
Query OK, 0 rows affected (0.00 sec)
mysql> SELECT "mycol" FROM v;
+-------+
| mycol |
+-------+
| mycol |
+-------+
1 row in set (0.01 sec)
mysql> SET sql_mode = 'ANSI_QUOTES';
Query OK, 0 rows affected (0.00 sec)
mysql> SELECT "mycol" FROM v;
+-------+
| mycol |
+-------+
| abc   |
+-------+
1 row in set (0.00 sec)
```

The `DEFINER` and `SQL SECURITY` clauses determine which MySQL account to use when checking access privileges for the view when a statement is executed that references the view. The valid `SQL``SECURITY` characteristic values are `DEFINER` (the default) and `INVOKER`. These indicate that the required privileges must be held by the user who defined or invoked the view, respectively.

If the `DEFINER` clause is present, the `user` value should be a MySQL account specified as`'user_name'@'host_name'`, `CURRENT_USER`, or `CURRENT_USER()`. The permitted `user` values depend on the privileges you hold, as discussed in Section 20.6, “Stored Object Access Control”. Also see that section for additional information about view security.

If the `DEFINER` clause is omitted, the default definer is the user who executes the `CREATE VIEW`statement. This is the same as specifying `DEFINER = CURRENT_USER` explicitly.

Within a view definition, the `CURRENT_USER` function returns the view's `DEFINER` value by default. For views defined with the `SQL SECURITY INVOKER` characteristic, `CURRENT_USER` returns the account for the view's invoker. For information about user auditing within views, see Section 6.2.15, “SQL-Based Account Activity Auditing”.

CREATE VIEW Statement Within a stored routine that is defined with the `SQL SECURITY DEFINER` characteristic, `CURRENT_USER`returns the routine's `DEFINER` value. This also affects a view defined within such a routine, if the view definition contains a `DEFINER` value of `CURRENT_USER`.

MySQL checks view privileges like this:

- At view definition time, the view creator must have the privileges needed to use the top-level objects

accessed by the view. For example, if the view definition refers to table columns, the creator must have some privilege for each column in the select list of the definition, and the `SELECT` privilege for each column used elsewhere in the definition. If the definition refers to a stored function, only the privileges needed to invoke the function can be checked. The privileges required at function invocation time can be checked only as it executes: For different invocations, different execution paths within the function might be taken.

- The user who references a view must have appropriate privileges to access it (`SELECT` to select from it,

`INSERT` to insert into it, and so forth.)

- When a view has been referenced, privileges for objects accessed by the view are checked against the

privileges held by the view `DEFINER` account or invoker, depending on whether the `SQL SECURITY`characteristic is `DEFINER` or `INVOKER`, respectively.

- If reference to a view causes execution of a stored function, privilege checking for statements executed

within the function depend on whether the function `SQL SECURITY` characteristic is `DEFINER` or`INVOKER`. If the security characteristic is `DEFINER`, the function runs with the privileges of the `DEFINER`account. If the characteristic is `INVOKER`, the function runs with the privileges determined by the view's`SQL SECURITY` characteristic.

Example: A view might depend on a stored function, and that function might invoke other stored routines.

For example, the following view invokes a stored function `f()`:

```
CREATE VIEW v AS SELECT * FROM t WHERE t.id = f(t.name);
```

Suppose that `f()` contains a statement such as this:

```
IF name IS NULL then
CALL p1();
ELSE
CALL p2();
END IF;
```

The privileges required for executing statements within `f()` need to be checked when `f()` executes. This might mean that privileges are needed for `p1()` or `p2()`, depending on the execution path within `f()`.

Those privileges must be checked at runtime, and the user who must possess the privileges is determined by the `SQL SECURITY` values of the view v and the function `f()`.

The `DEFINER` and `SQL SECURITY` clauses for views are extensions to standard SQL. In standard SQL,views are handled using the rules for `SQL SECURITY DEFINER`. The standard says that the definer of the view, which is the same as the owner of the view's schema, gets applicable privileges on the view (for example, `SELECT`) and may grant them. MySQL has no concept of a schema “owner”, so MySQL adds a clause to identify the definer. The `DEFINER` clause is an extension where the intent is to have what the standard has; that is, a permanent record of who defined the view. This is why the default `DEFINER` value is the account of the view creator.

The optional `ALGORITHM` clause is a MySQL extension to standard SQL. It affects how MySQL processes the view. `ALGORITHM` takes three values: `MERGE`, `TEMPTABLE`, or `UNDEFINED`. The default algorithm is `UNDEFINED` if no `ALGORITHM` clause is present. For more information, see Section 20.5.2, “View Processing Algorithms”, as well as Section 8.2.2.4, “Optimizing Derived Tables”.

DROP DATABASE Statement Some views are updatable. That is, you can use them in statements such as `UPDATE`, `DELETE`, or `INSERT`to update the contents of the underlying table. For a view to be updatable, there must be a one-to-one relationship between the rows in the view and the rows in the underlying table. There are also certain other constructs that make a view nonupdatable.

The `WITH CHECK OPTION` clause can be given for an updatable view to prevent inserts or updates to rows except those for which the `WHERE` clause in the `select_statement` is true.

In a `WITH CHECK OPTION` clause for an updatable view, the `LOCAL` and `CASCADED` keywords determine the scope of check testing when the view is defined in terms of another view. The `LOCAL` keyword restricts the `CHECK OPTION` only to the view being defined. `CASCADED` causes the checks for underlying views to be evaluated as well. When neither keyword is given, the default is `CASCADED`.

For more information about updatable views and the `WITH CHECK OPTION` clause, see Section 20.5.3,“Updatable and Insertable Views”, and Section 20.5.4, “The View WITH CHECK OPTION Clause”.

### 13.1.21 DROP DATABASE Statement

```
DROP {DATABASE | SCHEMA} [IF EXISTS] db_name
```

`DROP DATABASE` drops all tables in the database and deletes the database. Be very careful with this statement! To use `DROP DATABASE`, you need the `DROP` privilege on the database. `DROP SCHEMA` is a synonym for `DROP DATABASE`.

Important When a database is dropped, privileges granted specifically for the database are not automatically dropped. They must be dropped manually. See Section 13.7.1.4,“GRANT Statement”.

`IF EXISTS` is used to prevent an error from occurring if the database does not exist.

If the default database is dropped, the default database is unset (the `DATABASE()` function returns `NULL`).

If you use `DROP DATABASE` on a symbolically linked database, both the link and the original database are deleted.

`DROP DATABASE` returns the number of tables that were removed. This corresponds to the number of`.frm` files removed.

The `DROP DATABASE` statement removes from the given database directory those files and directories that MySQL itself may create during normal operation:

- All files with the following extensions:

```
- .frm
- .BAK
- .DAT
- .HSH
- .MRG
- .MYD
- .MYI
```

DROP EVENT Statement

```
- .TRG
- .TRN
- .db
- .ibd
- .ndb
- .par
```

- The `db.opt` file, if it exists.

If other files or directories remain in the database directory after MySQL removes those just listed, the database directory cannot be removed. In this case, you must remove any remaining files or directories manually and issue the `DROP DATABASE` statement again.

Dropping a database does not remove any `TEMPORARY` tables that were created in that database.

`TEMPORARY` tables are automatically removed when the session that created them ends. See Section 13.1.17.2, “CREATE TEMPORARY TABLE Statement”.

You can also drop databases with `mysqladmin`. See Section 4.5.2, “mysqladmin — A MySQL Server Administration Program”.

### 13.1.22 DROP EVENT Statement

```
DROP EVENT [IF EXISTS] event_name
```

This statement drops the event named `event_name`. The event immediately ceases being active, and is deleted completely from the server.

If the event does not exist, the error `ERROR 1517 (HY000): Unknown event 'event_name'` results.

You can override this and cause the statement to generate a warning for nonexistent events instead using

```
IF EXISTS.
```

This statement requires the `EVENT` privilege for the schema to which the event to be dropped belongs.

### 13.1.23 DROP FUNCTION Statement

The `DROP FUNCTION` statement is used to drop stored functions and loadable functions:

- For information about dropping stored functions, see Section 13.1.26, “DROP PROCEDURE and DROP

FUNCTION Statements”.

- For information about dropping loadable functions, see Section 13.7.3.2, “DROP FUNCTION Statement

for Loadable Functions”.

### 13.1.24 DROP INDEX Statement

```
DROP INDEX [ONLINE | OFFLINE] index_name ON tbl_name
[algorithm_option | lock_option] ...
algorithm_option:
ALGORITHM [=] {DEFAULT | INPLACE | COPY}
lock_option:
```

DROP LOGFILE GROUP Statement

```
LOCK [=] {DEFAULT | NONE | SHARED | EXCLUSIVE}
```

`DROP INDEX` drops the index named `index_name` from the table `tbl_name`. This statement is mapped to an `ALTER TABLE` statement to drop the index. See Section 13.1.7, “ALTER TABLE Statement”.

To drop a primary key, the index name is always `PRIMARY`, which must be specified as a quoted identifier because `PRIMARY` is a reserved word:

```
DROP INDEX `PRIMARY` ON t;
```

Indexes on variable-width columns of `NDB` tables are dropped online; that is, without any table copying.

The table is not locked against access from other NDB Cluster API nodes, although it is locked against other operations on the same API node for the duration of the operation. This is done automatically by the server whenever it determines that it is possible to do so; you do not have to use any special SQL syntax or server options to cause it to happen.

In NDB Cluster, you can drop indexes offline (which causes the table to be locked for all API nodes in the cluster) using the `OFFLINE` keyword. The rules and limitations governing `DROP OFFLINE INDEX`and `DROP ONLINE INDEX` are the same as for `ALTER OFFLINE TABLE ... DROP INDEX` and`ALTER ONLINE TABLE ... DROP INDEX`. You cannot cause the noncopying dropping of an index that would normally be dropped offline by using the `ONLINE` keyword: If it is not possible to perform the`DROP` operation without table copying, the server ignores the `ONLINE` keyword. For more information, see Section 18.6.12, “Online Operations with ALTER TABLE in NDB Cluster”.

The `ONLINE` and `OFFLINE` keywords are available only in NDB Cluster; attempting to use these keywords in standard MySQL Server 5.6 releases results in a syntax error. The `ONLINE` and `OFFLINE` keywords are deprecated in MySQL NDB Cluster 7.3; they continue to be supported in MySQL NDB Cluster 7.4, but are scheduled for removal in a future NDB Cluster release.

`ALGORITHM` and `LOCK` clauses may be given to influence the table copying method and level of concurrency for reading and writing the table while its indexes are being modified. They have the same meaning as for the `ALTER TABLE` statement. For more information, see Section 13.1.7, “ALTER TABLE Statement”

### 13.1.25 DROP LOGFILE GROUP Statement

```
DROP LOGFILE GROUP logfile_group
ENGINE [=] engine_name
```

This statement drops the log file group named `logfile_group`. The log file group must already exist or an error results. (For information on creating log file groups, see Section 13.1.14, “CREATE LOGFILE GROUP Statement”.)Important Before dropping a log file group, you must drop all tablespaces that use that log file group for `UNDO` logging.

The required `ENGINE` clause provides the name of the storage engine used by the log file group to be dropped. Currently, the only permitted values for `engine_name` are `NDB` and `NDBCLUSTER`.

`DROP LOGFILE GROUP` is useful only with Disk Data storage for NDB Cluster. See Section 18.6.11, “NDB Cluster Disk Data Tables”.

### 13.1.26 DROP PROCEDURE and DROP FUNCTION Statements

```
DROP {PROCEDURE | FUNCTION} [IF EXISTS] sp_name
```

DROP SERVER Statement These statements are used to drop a stored routine (a stored procedure or function). That is, the specified routine is removed from the server. (`DROP FUNCTION` is also used to drop loadable functions; see Section 13.7.3.2, “DROP FUNCTION Statement for Loadable Functions”.)To drop a stored routine, you must have the `ALTER ROUTINE` privilege for it. (If the`automatic_sp_privileges` system variable is enabled, that privilege and `EXECUTE` are granted automatically to the routine creator when the routine is created and dropped from the creator when the routine is dropped. See Section 20.2.2, “Stored Routines and MySQL Privileges”.)The `IF EXISTS` clause is a MySQL extension. It prevents an error from occurring if the procedure or function does not exist. A warning is produced that can be viewed with `SHOW WARNINGS`.

`DROP FUNCTION` is also used to drop loadable functions (see Section 13.7.3.2, “DROP FUNCTION Statement for Loadable Functions”).

### 13.1.27 DROP SERVER Statement

```
DROP SERVER [ IF EXISTS ] server_name
```

Drops the server definition for the server named `server_name`. The corresponding row in the`mysql.servers` table is deleted. This statement requires the `SUPER` privilege.

Dropping a server for a table does not affect any `FEDERATED` tables that used this connection information when they were created. See Section 13.1.16, “CREATE SERVER Statement”.

`DROP SERVER` causes an implicit commit. See Section 13.3.3, “Statements That Cause an Implicit Commit”.

`DROP SERVER` is not written to the binary log, regardless of the logging format that is in use.

In MySQL 5.6.11 only, `gtid_next` must be set to `AUTOMATIC` before issuing this statement. (Bug#16062608, Bug #16715809, Bug #69045)

### 13.1.28 DROP TABLE Statement

```
DROP [TEMPORARY] TABLE [IF EXISTS]
tbl_name [, tbl_name] ...
[RESTRICT | CASCADE]
```

`DROP TABLE` removes one or more tables. You must have the `DROP` privilege for each table.

Be careful with this statement! For each table, it removes the table definition and all table data. If the table is partitioned, the statement removes the table definition, all its partitions, all data stored in those partitions,and all partition definitions associated with the dropped table.

Dropping a table also drops any triggers for the table.

`DROP TABLE` causes an implicit commit, except when used with the `TEMPORARY` keyword. See Section 13.3.3, “Statements That Cause an Implicit Commit”.

Important When a table is dropped, privileges granted specifically for the table are not automatically dropped. They must be dropped manually. See Section 13.7.1.4,“GRANT Statement”.

If any tables named in the argument list do not exist, `DROP TABLE` behavior depends on whether the `IF``EXISTS` clause is given:DROP TABLESPACE Statement

- Without `IF EXISTS`, the statement drops all named tables that do exist, and returns an error indicating

which nonexisting tables it was unable to drop.

- With `IF EXISTS`, no error occurs for nonexisting tables. The statement drops all named tables that do

exist, and generates a `NOTE` diagnostic for each nonexistent table. These notes can be displayed with`SHOW WARNINGS`. See Section 13.7.5.41, “SHOW WARNINGS Statement”.

`IF EXISTS` can also be useful for dropping tables in unusual circumstances under which there is an `.frm`file but no table managed by the storage engine. (For example, if an abnormal server exit occurs after removal of the table from the storage engine but before `.frm` file removal.)The `TEMPORARY` keyword has the following effects:

- The statement drops only `TEMPORARY` tables.
- The statement does not cause an implicit commit.
- No access rights are checked. A `TEMPORARY` table is visible only with the session that created it, so no

check is necessary.

Including the `TEMPORARY` keyword is a good way to prevent accidentally dropping non-`TEMPORARY` tables.

The `RESTRICT` and `CASCADE` keywords do nothing. They are permitted to make porting easier from other database systems.

`DROP TABLE` is not supported with all `innodb_force_recovery` settings. See Section 14.21.2, “Forcing InnoDB Recovery”.

### 13.1.29 DROP TABLESPACE Statement

```
DROP TABLESPACE tablespace_name
ENGINE [=] engine_name
```

This statement drops a tablespace that was previously created using `CREATE TABLESPACE` (see Section 13.1.18, “CREATE TABLESPACE Statement”).

Important The tablespace to be dropped must not contain any data files; in other words,before you can drop a tablespace, you must first drop each of its data files using`ALTER TABLESPACE ... DROP DATAFILE` (see Section 13.1.8, “ALTER TABLESPACE Statement”).

The `ENGINE` clause (required) specifies the storage engine used by the tablespace. Currently, the only accepted values for `engine_name` are `NDB` and `NDBCLUSTER`.

`DROP TABLESPACE` is useful only with Disk Data storage for NDB Cluster. See Section 18.6.11, “NDB Cluster Disk Data Tables”.

### 13.1.30 DROP TRIGGER Statement

```
DROP TRIGGER [IF EXISTS] [schema_name.]trigger_name
```

This statement drops a trigger. The schema (database) name is optional. If the schema is omitted, the trigger is dropped from the default schema. `DROP TRIGGER` requires the `TRIGGER` privilege for the table associated with the trigger.

Use `IF EXISTS` to prevent an error from occurring for a trigger that does not exist. A `NOTE` is generated for a nonexistent trigger when using `IF EXISTS`. See Section 13.7.5.41, “SHOW WARNINGS Statement”.

DROP VIEW Statement Triggers for a table are also dropped if you drop the table.

### 13.1.31 DROP VIEW Statement

```
DROP VIEW [IF EXISTS]
view_name [, view_name] ...
[RESTRICT | CASCADE]
```

`DROP VIEW` removes one or more views. You must have the `DROP` privilege for each view.

If any views named in the argument list do not exist, the statement returns an error indicating by name which nonexisting views it was unable to drop, but also drops all views in the list that do exist.

The `IF EXISTS` clause prevents an error from occurring for views that don't exist. When this clause is given, a `NOTE` is generated for each nonexistent view. See Section 13.7.5.41, “SHOW WARNINGS Statement”.

`RESTRICT` and `CASCADE`, if given, are parsed and ignored.

### 13.1.32 RENAME TABLE Statement

```
RENAME TABLE
tbl_name TO new_tbl_name
[, tbl_name2 TO new_tbl_name2] ...
```

`RENAME TABLE` renames one or more tables. You must have `ALTER` and `DROP` privileges for the original table, and `CREATE` and `INSERT` privileges for the new table.

For example, to rename a table named `old_table` to `new_table`, use this statement:

```
RENAME TABLE old_table TO new_table;
```

That statement is equivalent to the following `ALTER TABLE` statement:

```
ALTER TABLE old_table RENAME new_table;
```

`RENAME TABLE`, unlike `ALTER TABLE`, can rename multiple tables within a single statement:

```
RENAME TABLE old_table1 TO new_table1,
old_table2 TO new_table2,
old_table3 TO new_table3;
```

Renaming operations are performed left to right. Thus, to swap two table names, do this (assuming that a table with the intermediary name `tmp_table` does not already exist):

```
RENAME TABLE old_table TO tmp_table,
new_table TO old_table,
tmp_table TO new_table;
```

Metadata locks on tables are acquired in name order, which in some cases can make a difference in operation outcome when multiple transactions execute concurrently. See Section 8.11.4, “Metadata Locking”.

To execute `RENAME TABLE`, there must be no active transactions or tables locked with `LOCK TABLES`.

With the transaction table locking conditions satisfied, the rename operation is done atomically; no other session can access any of the tables while the rename is in progress.

If any errors occur during a `RENAME TABLE`, the statement fails and no changes are made.

You can use `RENAME TABLE` to move a table from one database to another:TRUNCATE TABLE Statement

```
RENAME TABLE current_db.tbl_name TO other_db.tbl_name;
```

Using this method to move all tables from one database to a different one in effect renames the database(an operation for which MySQL has no single statement), except that the original database continues to exist, albeit with no tables.

Like `RENAME TABLE`, `ALTER TABLE ... RENAME` can also be used to move a table to a different database. Regardless of the statement used, if the rename operation would move the table to a database located on a different file system, the success of the outcome is platform specific and depends on the underlying operating system calls used to move table files.

If a table has triggers, attempts to rename the table into a different database fail with a `Trigger in`

```
wrong schema (ER_TRG_IN_WRONG_SCHEMA) error.
```

To rename `TEMPORARY` tables, `RENAME TABLE` does not work. Use `ALTER TABLE` instead.

`RENAME TABLE` works for views, except that views cannot be renamed into a different database.

Any privileges granted specifically for a renamed table or view are not migrated to the new name. They must be changed manually.

`RENAME TABLE tbl_name TO new_tbl_name` changes internally generated foreign key constraint names and user-defined foreign key constraint names that begin with the string “`tbl_name`_ibfk_” to reflect the new table name. `InnoDB` interprets foreign key constraint names that begin with the string“`tbl_name`_ibfk_” as internally generated names.

Foreign key constraint names that point to the renamed table are automatically updated unless there is a conflict, in which case the statement fails with an error. A conflict occurs if the renamed constraint name already exists. In such cases, you must drop and re-create the foreign keys for them to function properly.

### 13.1.33 TRUNCATE TABLE Statement

```
TRUNCATE [TABLE] tbl_name
```

`TRUNCATE TABLE` empties a table completely. It requires the `DROP` privilege.

Logically, `TRUNCATE TABLE` is similar to a `DELETE` statement that deletes all rows, or a sequence of `DROP``TABLE` and `CREATE TABLE` statements. To achieve high performance, it bypasses the DML method of deleting data. Thus, it cannot be rolled back, it does not cause `ON DELETE` triggers to fire, and it cannot be performed for `InnoDB` tables with parent-child foreign key relationships.

Although `TRUNCATE TABLE` is similar to `DELETE`, it is classified as a DDL statement rather than a DML statement. It differs from `DELETE` in the following ways:

- Truncate operations drop and re-create the table, which is much faster than deleting rows one by one,

particularly for large tables.

- Truncate operations cause an implicit commit, and so cannot be rolled back. See Section 13.3.3,

“Statements That Cause an Implicit Commit”.

- Truncation operations cannot be performed if the session holds an active table lock.
- `TRUNCATE TABLE` fails for an `InnoDB` table or `NDB` table if there are any `FOREIGN KEY` constraints

from other tables that reference the table. Foreign key constraints between columns of the same table are permitted.

- Truncation operations do not return a meaningful value for the number of deleted rows. The usual result

is “0 rows affected,” which should be interpreted as “no information.”Data Manipulation Statements

- As long as the table format file `tbl_name.frm` is valid, the table can be re-created as an empty table

with `TRUNCATE TABLE`, even if the data or index files have become corrupted.

- Any `AUTO_INCREMENT` value is reset to its start value. This is true even for `MyISAM` and `InnoDB`, which

normally do not reuse sequence values.

- When used with partitioned tables, `TRUNCATE TABLE` preserves the partitioning; that is, the data and

index files are dropped and re-created, while the partition definitions (`.par`) file is unaffected.

- The `TRUNCATE TABLE` statement does not invoke `ON DELETE` triggers.

`TRUNCATE TABLE` for a table closes all handlers for the table that were opened with `HANDLER OPEN`.

`TRUNCATE TABLE` is treated for purposes of binary logging and replication as `DROP TABLE` followed by`CREATE TABLE`—that is, as DDL rather than DML. This is due to the fact that, when using `InnoDB` and other transactional storage engines where the transaction isolation level does not permit statement-based logging (`READ COMMITTED` or `READ UNCOMMITTED`), the statement was not logged and replicated when using `STATEMENT` or `MIXED` logging mode. (Bug #36763) However, it is still applied on replicas using`InnoDB` in the manner described previously.

On a system with a large `InnoDB` buffer pool and `innodb_adaptive_hash_index` enabled, `TRUNCATE``TABLE` operations may cause a temporary drop in system performance due to an LRU scan that occurs when removing an `InnoDB` table's adaptive hash index entries. The problem was addressed for `DROP``TABLE` in MySQL 5.5.23 (Bug #13704145, Bug #64284) but remains a known issue for `TRUNCATE TABLE`(Bug #68184).

`TRUNCATE TABLE` can be used with Performance Schema summary tables, but the effect is to reset the summary columns to 0 or `NULL`, not to remove rows. See Section 22.12.9, “Performance Schema Summary Tables”.

## 13.2 Data Manipulation Statements

### 13.2.1 CALL Statement

```
CALL sp_name([parameter[,...]])
CALL sp_name[()]
```

The `CALL` statement invokes a stored procedure that was defined previously with `CREATE PROCEDURE`.

Stored procedures that take no arguments can be invoked without parentheses. That is, `CALL p()` and`CALL p` are equivalent.

`CALL` can pass back values to its caller using parameters that are declared as `OUT` or `INOUT` parameters.

When the procedure returns, a client program can also obtain the number of rows affected for the final statement executed within the routine: At the SQL level, call the `ROW_COUNT()` function; from the C API,call the `mysql_affected_rows()` function.

For information about the effect of unhandled conditions on procedure parameters, see Section 13.6.7.8,“Condition Handling and OUT or INOUT Parameters”.

To get back a value from a procedure using an `OUT` or `INOUT` parameter, pass the parameter by means of a user variable, and then check the value of the variable after the procedure returns. (If you are calling the procedure from within another stored procedure or function, you can also pass a routine parameter or local routine variable as an `IN` or `INOUT` parameter.) For an `INOUT` parameter, initialize its value before passing it to the procedure. The following procedure has an `OUT` parameter that the procedure sets to the current server version, and an `INOUT` value that the procedure increments by one from its current value:CALL Statement

```
DELIMITER //
CREATE PROCEDURE p (OUT ver_param VARCHAR(25), INOUT incr_param INT)
BEGIN
# Set value of OUT parameter
SELECT VERSION() INTO ver_param;
# Increment value of INOUT parameter
SET incr_param = incr_param + 1;
END //
DELIMITER ;
```

Before calling the procedure, initialize the variable to be passed as the `INOUT` parameter. After calling the procedure, the values of the two variables have been set or modified:

```
mysql> SET @increment = 10;
mysql> CALL p(@version, @increment);
mysql> SELECT @version, @increment;
+----------+------------+
| @version | @increment |
+----------+------------+
| 5.6.51   |         11 |
+----------+------------+
```

In prepared `CALL` statements used with `PREPARE` and `EXECUTE`, placeholders can be used for `IN`parameters, `OUT`, and `INOUT` parameters. These types of parameters can be used as follows:

```
mysql> SET @increment = 10;
mysql> PREPARE s FROM 'CALL p(?, ?)';
mysql> EXECUTE s USING @version, @increment;
mysql> SELECT @version, @increment;
+----------+------------+
| @version | @increment |
+----------+------------+
| 5.6.51   |         11 |
+----------+------------+
```

To write C programs that use the `CALL` SQL statement to execute stored procedures that produce result sets, the `CLIENT_MULTI_RESULTS` flag must be enabled. This is because each `CALL` returns a result to indicate the call status, in addition to any result sets that might be returned by statements executed within the procedure. `CLIENT_MULTI_RESULTS` must also be enabled if `CALL` is used to execute any stored procedure that contains prepared statements. It cannot be determined when such a procedure is loaded whether those statements produce result sets, so it is necessary to assume that they do so.

`CLIENT_MULTI_RESULTS` can be enabled when you call `mysql_real_connect()`, either explicitly by passing the `CLIENT_MULTI_RESULTS` flag itself, or implicitly by passing `CLIENT_MULTI_STATEMENTS`(which also enables `CLIENT_MULTI_RESULTS`). `CLIENT_MULTI_RESULTS` is enabled by default.

To process the result of a `CALL` statement executed using `mysql_query()` or `mysql_real_query()`,use a loop that calls `mysql_next_result()` to determine whether there are more results. For an example, see Multiple Statement Execution Support.

C programs can use the prepared-statement interface to execute `CALL` statements and access `OUT` and`INOUT` parameters. This is done by processing the result of a `CALL` statement using a loop that calls`mysql_stmt_next_result()` to determine whether there are more results. For an example, see Prepared CALL Statement Support. Languages that provide a MySQL interface can use prepared `CALL`statements to directly retrieve `OUT` and `INOUT` procedure parameters.

Metadata changes to objects referred to by stored programs are detected and cause automatic reparsing of the affected statements when the program is next executed. For more information, see Section 8.10.4,“Caching of Prepared Statements and Stored Programs”.

DELETE Statement

### 13.2.2 DELETE Statement

`DELETE` is a DML statement that removes rows from a table.

> Single-Table Syntax

```
DELETE [LOW_PRIORITY] [QUICK] [IGNORE] FROM tbl_name
[PARTITION (partition_name [, partition_name] ...)]
[WHERE where_condition]
[ORDER BY ...]
[LIMIT row_count]
```

The `DELETE` statement deletes rows from `tbl_name` and returns the number of deleted rows. To check the number of deleted rows, call the `ROW_COUNT()` function described in Section 12.16, “Information Functions”.

> Main Clauses

The conditions in the optional `WHERE` clause identify which rows to delete. With no `WHERE` clause, all rows are deleted.

`where_condition` is an expression that evaluates to true for each row to be deleted. It is specified as described in Section 13.2.9, “SELECT Statement”.

If the `ORDER BY` clause is specified, the rows are deleted in the order that is specified. The `LIMIT` clause places a limit on the number of rows that can be deleted. These clauses apply to single-table deletes, but not multi-table deletes.

> Multiple-Table Syntax

```
DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
tbl_name[.*] [, tbl_name[.*]] ...
FROM table_references
[WHERE where_condition]
DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
FROM tbl_name[.*] [, tbl_name[.*]] ...
USING table_references
[WHERE where_condition]
```

> Privileges

You need the `DELETE` privilege on a table to delete rows from it. You need only the `SELECT` privilege for any columns that are only read, such as those named in the `WHERE` clause.

> Performance

When you do not need to know the number of deleted rows, the `TRUNCATE TABLE` statement is a faster way to empty a table than a `DELETE` statement with no `WHERE` clause. Unlike `DELETE`, `TRUNCATE TABLE`cannot be used within a transaction or if you have a lock on the table. See Section 13.1.33, “TRUNCATE TABLE Statement” and Section 13.3.5, “LOCK TABLES and UNLOCK TABLES Statements”.

The speed of delete operations may also be affected by factors discussed in Section 8.2.4.3, “Optimizing DELETE Statements”.

To ensure that a given `DELETE` statement does not take too much time, the MySQL-specific `LIMIT``row_count` clause for `DELETE` specifies the maximum number of rows to be deleted. If the number of rows to delete is larger than the limit, repeat the `DELETE` statement until the number of affected rows is less than the `LIMIT` value.

DELETE Statement

> Subqueries

You cannot delete from a table and select from the same table in a subquery.

> Partitioned Table Support

`DELETE` supports explicit partition selection using the `PARTITION` clause, which takes a list of the comma-separated names of one or more partitions or subpartitions (or both) from which to select rows to be dropped. Partitions not included in the list are ignored. Given a partitioned table t with a partition named`p0`, executing the statement `DELETE FROM t PARTITION (p0)` has the same effect on the table as executing `ALTER TABLE t TRUNCATE PARTITION (p0)`; in both cases, all rows in partition `p0` are dropped.

`PARTITION` can be used along with a `WHERE` condition, in which case the condition is tested only on rows in the listed partitions. For example, `DELETE FROM t PARTITION (p0) WHERE c < 5` deletes rows only from partition `p0` for which the condition `c < 5` is true; rows in any other partitions are not checked and thus not affected by the `DELETE`.

The `PARTITION` clause can also be used in multiple-table `DELETE` statements. You can use up to one such option per table named in the `FROM` option.

For more information and examples, see Section 19.5, “Partition Selection”.

> Auto-Increment Columns

If you delete the row containing the maximum value for an `AUTO_INCREMENT` column, the value is not reused for a `MyISAM` or `InnoDB` table. If you delete all rows in the table with `DELETE FROM tbl_name`(without a `WHERE` clause) in `autocommit` mode, the sequence starts over for all storage engines except`InnoDB` and `MyISAM`. There are some exceptions to this behavior for `InnoDB` tables, as discussed in Section 14.6.1.6, “AUTO_INCREMENT Handling in InnoDB”.

For `MyISAM` tables, you can specify an `AUTO_INCREMENT` secondary column in a multiple-column key.

In this case, reuse of values deleted from the top of the sequence occurs even for `MyISAM` tables. See Section 3.6.9, “Using AUTO_INCREMENT”.

> Modifiers

The `DELETE` statement supports the following modifiers:

- If you specify the `LOW_PRIORITY` modifier, the server delays execution of the `DELETE` until no other

clients are reading from the table. This affects only storage engines that use only table-level locking(such as `MyISAM`, `MEMORY`, and `MERGE`).

- For `MyISAM` tables, if you use the `QUICK` modifier, the storage engine does not merge index leaves

during delete, which may speed up some kinds of delete operations.

- The `IGNORE` modifier causes MySQL to ignore errors during the process of deleting rows. (Errors

encountered during the parsing stage are processed in the usual manner.) Errors that are ignored due to the use of `IGNORE` are returned as warnings.

> Order of Deletion

If the `DELETE` statement includes an `ORDER BY` clause, rows are deleted in the order specified by the clause. This is useful primarily in conjunction with `LIMIT`. For example, the following statement finds rows matching the `WHERE` clause, sorts them by `timestamp_column`, and deletes the first (oldest) one:

```
DELETE FROM somelog WHERE user = 'jcole'
```

DELETE Statement

```
ORDER BY timestamp_column LIMIT 1;
```

`ORDER BY` also helps to delete rows in an order required to avoid referential integrity violations.

> InnoDB Tables

If you are deleting many rows from a large table, you may exceed the lock table size for an `InnoDB` table.

To avoid this problem, or simply to minimize the time that the table remains locked, the following strategy(which does not use `DELETE` at all) might be helpful:

1. Select the rows not to be deleted into an empty table that has the same structure as the original table:

```
INSERT INTO t_copy SELECT * FROM t WHERE ... ;
```

2. Use `RENAME TABLE` to atomically move the original table out of the way and rename the copy to the

original name:

```
RENAME TABLE t TO t_old, t_copy TO t;
```

3. Drop the original table:

```
DROP TABLE t_old;
```

No other sessions can access the tables involved while `RENAME TABLE` executes, so the rename operation is not subject to concurrency problems. See Section 13.1.32, “RENAME TABLE Statement”.

> MyISAM Tables

In `MyISAM` tables, deleted rows are maintained in a linked list and subsequent `INSERT` operations reuse old row positions. To reclaim unused space and reduce file sizes, use the `OPTIMIZE TABLE` statement or the `myisamchk` utility to reorganize tables. `OPTIMIZE TABLE` is easier to use, but `myisamchk` is faster.

See Section 13.7.2.4, “OPTIMIZE TABLE Statement”, and Section 4.6.3, “myisamchk — MyISAM Table-Maintenance Utility”.

The `QUICK` modifier affects whether index leaves are merged for delete operations. `DELETE QUICK` is most useful for applications where index values for deleted rows are replaced by similar index values from rows inserted later. In this case, the holes left by deleted values are reused.

`DELETE QUICK` is not useful when deleted values lead to underfilled index blocks spanning a range of index values for which new inserts occur again. In this case, use of `QUICK` can lead to wasted space in the index that remains unreclaimed. Here is an example of such a scenario:

1. Create a table that contains an indexed `AUTO_INCREMENT` column.
2. Insert many rows into the table. Each insert results in an index value that is added to the high end of

the index.

3. Delete a block of rows at the low end of the column range using `DELETE QUICK`.

In this scenario, the index blocks associated with the deleted index values become underfilled but are not merged with other index blocks due to the use of `QUICK`. They remain underfilled when new inserts occur,because new rows do not have index values in the deleted range. Furthermore, they remain underfilled even if you later use `DELETE` without `QUICK`, unless some of the deleted index values happen to lie in index blocks within or adjacent to the underfilled blocks. To reclaim unused index space under these circumstances, use `OPTIMIZE TABLE`.

If you are going to delete many rows from a table, it might be faster to use `DELETE QUICK` followed by`OPTIMIZE TABLE`. This rebuilds the index rather than performing many index block merge operations.

DELETE Statement

> Multi-Table Deletes

You can specify multiple tables in a `DELETE` statement to delete rows from one or more tables depending on the condition in the `WHERE` clause. You cannot use `ORDER BY` or `LIMIT` in a multiple-table `DELETE`.

The `table_references` clause lists the tables involved in the join, as described in Section 13.2.9.2,“JOIN Clause”.

For the first multiple-table syntax, only matching rows from the tables listed before the `FROM` clause are deleted. For the second multiple-table syntax, only matching rows from the tables listed in the `FROM` clause(before the `USING` clause) are deleted. The effect is that you can delete rows from many tables at the same time and have additional tables that are used only for searching:

```
DELETE t1, t2 FROM t1 INNER JOIN t2 INNER JOIN t3
WHERE t1.id=t2.id AND t2.id=t3.id;
```

Or:

```
DELETE FROM t1, t2 USING t1 INNER JOIN t2 INNER JOIN t3
WHERE t1.id=t2.id AND t2.id=t3.id;
```

These statements use all three tables when searching for rows to delete, but delete matching rows only from tables `t1` and `t2`.

The preceding examples use `INNER JOIN`, but multiple-table `DELETE` statements can use other types of join permitted in `SELECT` statements, such as `LEFT JOIN`. For example, to delete rows that exist in `t1`that have no match in `t2`, use a `LEFT JOIN`:

```
DELETE t1 FROM t1 LEFT JOIN t2 ON t1.id=t2.id WHERE t2.id IS NULL;
```

The syntax permits `.*` after each `tbl_name` for compatibility with `Access`.

If you use a multiple-table `DELETE` statement involving `InnoDB` tables for which there are foreign key constraints, the MySQL optimizer might process tables in an order that differs from that of their parent/child relationship. In this case, the statement fails and rolls back. Instead, you should delete from a single table and rely on the `ON DELETE` capabilities that `InnoDB` provides to cause the other tables to be modified accordingly.

Note If you declare an alias for a table, you must use the alias when referring to the table:

```
DELETE t1 FROM test AS t1, test2 WHERE ...
```

Table aliases in a multiple-table `DELETE` should be declared only in the `table_references` part of the statement. Elsewhere, alias references are permitted but not alias declarations.

Correct:

```
DELETE a1, a2 FROM t1 AS a1 INNER JOIN t2 AS a2
WHERE a1.id=a2.id;
DELETE FROM a1, a2 USING t1 AS a1 INNER JOIN t2 AS a2
WHERE a1.id=a2.id;
```

Incorrect:

```
DELETE t1 AS a1, t2 AS a2 FROM t1 INNER JOIN t2
WHERE a1.id=a2.id;
DELETE FROM t1 AS a1, t2 AS a2 USING t1 INNER JOIN t2
WHERE a1.id=a2.id;
```

DO Statement

### 13.2.3 DO Statement

```
DO expr [, expr] ...
```

`DO` executes the expressions but does not return any results. In most respects, `DO` is shorthand for `SELECT``expr, ...`, but has the advantage that it is slightly faster when you do not care about the result.

`DO` is useful primarily with functions that have side effects, such as `RELEASE_LOCK()`.

Example: This `SELECT` statement pauses, but also produces a result set:

```
mysql> SELECT SLEEP(5);
+----------+
| SLEEP(5) |
+----------+
|        0 |
+----------+
1 row in set (5.02 sec)
```

`DO`, on the other hand, pauses without producing a result set.:

```
mysql> DO SLEEP(5);
Query OK, 0 rows affected (4.99 sec)
```

This could be useful, for example in a stored function or trigger, which prohibit statements that produce result sets.

`DO` only executes expressions. It cannot be used in all cases where `SELECT` can be used. For example, `DO``id FROM t1` is invalid because it references a table.

### 13.2.4 HANDLER Statement

```
HANDLER tbl_name OPEN [ [AS] alias]
HANDLER tbl_name READ index_name { = | <= | >= | < | > } (value1,value2,...)
[ WHERE where_condition ] [LIMIT ... ]
HANDLER tbl_name READ index_name { FIRST | NEXT | PREV | LAST }
[ WHERE where_condition ] [LIMIT ... ]
HANDLER tbl_name READ { FIRST | NEXT }
[ WHERE where_condition ] [LIMIT ... ]
HANDLER tbl_name CLOSE
```

The `HANDLER` statement provides direct access to table storage engine interfaces. It is available for`InnoDB` and `MyISAM` tables.

The `HANDLER ... OPEN` statement opens a table, making it accessible using subsequent `HANDLER ...``READ` statements. This table object is not shared by other sessions and is not closed until the session calls`HANDLER ... CLOSE` or the session terminates.

If you open the table using an alias, further references to the open table with other `HANDLER` statements must use the alias rather than the table name. If you do not use an alias, but open the table using a table name qualified by the database name, further references must use the unqualified table name. For example, for a table opened using `mydb.mytable`, further references must use `mytable`.

The first `HANDLER ... READ` syntax fetches a row where the index specified satisfies the given values and the `WHERE` condition is met. If you have a multiple-column index, specify the index column values as a comma-separated list. Either specify values for all the columns in the index, or specify values for a leftmost prefix of the index columns. Suppose that an index `my_idx` includes three columns named `col_a`, `col_b`,and `col_c`, in that order. The `HANDLER` statement can specify values for all three columns in the index, or for the columns in a leftmost prefix. For example:HANDLER Statement

```
HANDLER ... READ my_idx = (col_a_val,col_b_val,col_c_val) ...
HANDLER ... READ my_idx = (col_a_val,col_b_val) ...
HANDLER ... READ my_idx = (col_a_val) ...
```

To employ the `HANDLER` interface to refer to a table's `PRIMARY KEY`, use the quoted identifier

```
`PRIMARY`:
HANDLER tbl_name READ `PRIMARY` ...
```

The second `HANDLER ... READ` syntax fetches a row from the table in index order that matches the`WHERE` condition.

The third `HANDLER ... READ` syntax fetches a row from the table in natural row order that matches the`WHERE` condition. It is faster than `HANDLER tbl_name READ index_name` when a full table scan is desired. Natural row order is the order in which rows are stored in a `MyISAM` table data file. This statement works for `InnoDB` tables as well, but there is no such concept because there is no separate data file.

Without a `LIMIT` clause, all forms of `HANDLER ... READ` fetch a single row if one is available. To return a specific number of rows, include a `LIMIT` clause. It has the same syntax as for the `SELECT` statement.

See Section 13.2.9, “SELECT Statement”.

`HANDLER ... CLOSE` closes a table that was opened with `HANDLER ... OPEN`.

There are several reasons to use the `HANDLER` interface instead of normal `SELECT` statements:

- `HANDLER` is faster than `SELECT`:
- A designated storage engine handler object is allocated for the `HANDLER ... OPEN`. The object is

reused for subsequent `HANDLER` statements for that table; it need not be reinitialized for each one.

- There is less parsing involved.
- There is no optimizer or query-checking overhead.
- The handler interface does not have to provide a consistent look of the data (for example, dirty reads

are permitted), so the storage engine can use optimizations that `SELECT` does not normally permit.

- `HANDLER` makes it easier to port to MySQL applications that use a low-level `ISAM`-like interface. (See

Section 14.20, “InnoDB memcached Plugin” for an alternative way to adapt applications that use the key-value store paradigm.)

- `HANDLER` enables you to traverse a database in a manner that is difficult (or even impossible) to

accomplish with `SELECT`. The `HANDLER` interface is a more natural way to look at data when working with applications that provide an interactive user interface to the database.

`HANDLER` is a somewhat low-level statement. For example, it does not provide consistency. That is,`HANDLER ... OPEN` does not take a snapshot of the table, and does not lock the table. This means that after a `HANDLER ... OPEN` statement is issued, table data can be modified (by the current session or other sessions) and these modifications might be only partially visible to `HANDLER ... NEXT` or`HANDLER ... PREV` scans.

An open handler can be closed and marked for reopen, in which case the handler loses its position in the table. This occurs when both of the following circumstances are true:

- Any session executes `FLUSH TABLES` or DDL statements on the handler's table.
- The session in which the handler is open executes non-`HANDLER` statements that use tables.

`TRUNCATE TABLE` for a table closes all handlers for the table that were opened with `HANDLER OPEN`.

INSERT Statement If a table is flushed with `FLUSH TABLES tbl_name WITH READ LOCK` was opened with `HANDLER`, the handler is implicitly flushed and loses its position.

`HANDLER` is not supported with partitioned tables.

### 13.2.5 INSERT Statement

```
INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
[INTO] tbl_name
[PARTITION (partition_name [, partition_name] ...)]
[(col_name [, col_name] ...)]
{VALUES | VALUE} (value_list) [, (value_list)] ...
[ON DUPLICATE KEY UPDATE assignment_list]
INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
[INTO] tbl_name
[PARTITION (partition_name [, partition_name] ...)]
SET assignment_list
[ON DUPLICATE KEY UPDATE assignment_list]
INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
[INTO] tbl_name
[PARTITION (partition_name [, partition_name] ...)]
[(col_name [, col_name] ...)]
SELECT ...
[ON DUPLICATE KEY UPDATE assignment_list]
value:
{expr | DEFAULT}
value_list:
value [, value] ...
assignment:
col_name = value
assignment_list:
assignment [, assignment] ...
```

`INSERT` inserts new rows into an existing table. The `INSERT ... VALUES` and `INSERT ... SET` forms of the statement insert rows based on explicitly specified values. The `INSERT ... SELECT` form inserts rows selected from another table or tables. `INSERT` with an `ON DUPLICATE KEY UPDATE` clause enables existing rows to be updated if a row to be inserted would cause a duplicate value in a `UNIQUE` index or

```
PRIMARY KEY.
```

For additional information about `INSERT ... SELECT` and `INSERT ... ON DUPLICATE KEY``UPDATE`, see Section 13.2.5.1, “INSERT ... SELECT Statement”, and Section 13.2.5.2, “INSERT ... ON DUPLICATE KEY UPDATE Statement”.

Inserting into a table requires the `INSERT` privilege for the table. If the `ON DUPLICATE KEY UPDATE`clause is used and a duplicate key causes an `UPDATE` to be performed instead, the statement requires the`UPDATE` privilege for the columns to be updated. For columns that are read but not modified you need only the `SELECT` privilege (such as for a column referenced only on the right hand side of an `col_name`=`expr`assignment in an `ON DUPLICATE KEY UPDATE` clause).

When inserting into a partitioned table, you can control which partitions and subpartitions accept new rows. The `PARTITION` clause takes a list of the comma-separated names of one or more partitions or subpartitions (or both) of the table. If any of the rows to be inserted by a given `INSERT` statement do not match one of the partitions listed, the `INSERT` statement fails with the error `Found a row not``matching the given partition set`. For more information and examples, see Section 19.5,“Partition Selection”.

INSERT Statement`tbl_name` is the table into which rows should be inserted. Specify the columns for which the statement provides values as follows:

- Provide a parenthesized list of comma-separated column names following the table name. In this case, a

value for each named column must be provided by the `VALUES` list or the `SELECT` statement.

- If you do not specify a list of column names for `INSERT ... VALUES` or `INSERT ... SELECT`, values

for every column in the table must be provided by the `VALUES` list or the `SELECT` statement. If you do not know the order of the columns in the table, use `DESCRIBE tbl_name` to find out.

- A `SET` clause indicates columns explicitly by name, together with the value to assign each one.

Column values can be given in several ways:

- If strict SQL mode is not enabled, any column not explicitly given a value is set to its default (explicit or

implicit) value. For example, if you specify a column list that does not name all the columns in the table,unnamed columns are set to their default values. Default value assignment is described in Section 11.5,“Data Type Default Values”. See also Section 1.6.3.3, “Constraints on Invalid Data”.

If strict SQL mode is enabled, an `INSERT` statement generates an error if it does not specify an explicit value for every column that has no default value. See Section 5.1.10, “Server SQL Modes”.

- If both the column list and the `VALUES` list are empty, `INSERT` creates a row with each column set to its

default value:

```
INSERT INTO tbl_name () VALUES();
```

If strict mode is not enabled, MySQL uses the implicit default value for any column that has no explicitly defined default. If strict mode is enabled, an error occurs if any column has no default value.

- Use the keyword `DEFAULT` to set a column explicitly to its default value. This makes it easier to write

`INSERT` statements that assign values to all but a few columns, because it enables you to avoid writing an incomplete `VALUES` list that does not include a value for each column in the table. Otherwise, you must provide the list of column names corresponding to each value in the `VALUES` list.

- In expressions, you can use `DEFAULT(col_name)` to produce the default value for column `col_name`.
- Type conversion of an expression `expr` that provides a column value might occur if the expression data

type does not match the column data type. Conversion of a given value can result in different inserted values depending on the column type. For example, inserting the string `'1999.0e-2'` into an `INT`,`FLOAT`, `DECIMAL(10,6)`, or `YEAR` column inserts the value 1999, `19.9921`, `19.992100`, or 1999,respectively. The value stored in the `INT` and `YEAR` columns is 1999 because the string-to-number conversion looks only at as much of the initial part of the string as may be considered a valid integer or year. For the `FLOAT` and `DECIMAL` columns, the string-to-number conversion considers the entire string a valid numeric value.

- An expression `expr` can refer to any column that was set earlier in a value list. For example, you can do

this because the value for `col2` refers to `col1`, which has previously been assigned:

```
INSERT INTO tbl_name (col1,col2) VALUES(15,col1*2);
```

But the following is not legal, because the value for `col1` refers to `col2`, which is assigned after `col1`:

```
INSERT INTO tbl_name (col1,col2) VALUES(col2*2,15);
```

An exception occurs for columns that contain `AUTO_INCREMENT` values. Because `AUTO_INCREMENT`values are generated after other value assignments, any reference to an `AUTO_INCREMENT` column in the assignment returns a 0.

INSERT Statement`INSERT` statements that use `VALUES` syntax can insert multiple rows. To do this, include multiple lists of comma-separated column values, with lists enclosed within parentheses and separated by commas.

Example:

```
INSERT INTO tbl_name (a,b,c) VALUES(1,2,3),(4,5,6),(7,8,9);
```

Each values list must contain exactly as many values as are to be inserted per row. The following statement is invalid because it contains one list of nine values, rather than three lists of three values each:

```
INSERT INTO tbl_name (a,b,c) VALUES(1,2,3,4,5,6,7,8,9);
```

`VALUE` is a synonym for `VALUES` in this context. Neither implies anything about the number of values lists,nor about the number of values per list. Either may be used whether there is a single values list or multiple lists, and regardless of the number of values per list.

The affected-rows value for an `INSERT` can be obtained using the `ROW_COUNT()` SQL function or the `mysql_affected_rows()` C API function. See Section 12.16, “Information Functions”, and mysql_affected_rows().

If you use an `INSERT ... VALUES` statement with multiple value lists or `INSERT ... SELECT`, the statement returns an information string in this format:

```
Records: N1 Duplicates: N2 Warnings: N3
```

If you are using the C API, the information string can be obtained by invoking the `mysql_info()` function.

See mysql_info().

`Records` indicates the number of rows processed by the statement. (This is not necessarily the number of rows actually inserted because `Duplicates` can be nonzero.) `Duplicates` indicates the number of rows that could not be inserted because they would duplicate some existing unique index value. `Warnings`indicates the number of attempts to insert column values that were problematic in some way. Warnings can occur under any of the following conditions:

- Inserting `NULL` into a column that has been declared `NOT NULL`. For multiple-row `INSERT` statements or

`INSERT INTO ... SELECT` statements, the column is set to the implicit default value for the column data type. This is 0 for numeric types, the empty string (`''`) for string types, and the “zero” value for date and time types. `INSERT INTO ... SELECT` statements are handled the same way as multiple-row inserts because the server does not examine the result set from the `SELECT` to see whether it returns a single row. (For a single-row `INSERT`, no warning occurs when `NULL` is inserted into a `NOT NULL`column. Instead, the statement fails with an error.)

- Setting a numeric column to a value that lies outside the column range. The value is clipped to the

closest endpoint of the range.

- Assigning a value such as `'10.34 a'` to a numeric column. The trailing nonnumeric text is stripped off

and the remaining numeric part is inserted. If the string value has no leading numeric part, the column is set to 0.

- Inserting a string into a string column (`CHAR`, `VARCHAR`, `TEXT`, or `BLOB`) that exceeds the column

maximum length. The value is truncated to the column maximum length.

- Inserting a value into a date or time column that is illegal for the data type. The column is set to the

appropriate zero value for the type.

- For `INSERT` examples involving `AUTO_INCREMENT` column values, see Section 3.6.9, “Using

AUTO_INCREMENT”.

INSERT Statement If `INSERT` inserts a row into a table that has an `AUTO_INCREMENT` column, you can find the value used for that column by using the `LAST_INSERT_ID()` SQL function or the `mysql_insert_id()` C API function.

Note These two functions do not always behave identically. The behavior of `INSERT`statements with respect to `AUTO_INCREMENT` columns is discussed further in Section 12.16, “Information Functions”, and mysql_insert_id().

The `INSERT` statement supports the following modifiers:

- If you use the `DELAYED` modifier, the server puts the row or rows to be inserted into a buffer, and the

client issuing the `INSERT DELAYED` statement can then continue immediately. If the table is in use, the server holds the rows. When the table is free, the server begins inserting rows, checking periodically to see whether there are any new read requests for the table. If there are, the delayed row queue is suspended until the table becomes free again. See Section 13.2.5.3, “INSERT DELAYED Statement”.

```
DELAYED is ignored with INSERT ... SELECT or INSERT ... ON DUPLICATE KEY UPDATE.
```

`DELAYED` is also disregarded for an `INSERT` that uses functions accessing tables or triggers, or that is called from a function or a trigger.

Note As of MySQL 5.6.6, `INSERT DELAYED` is deprecated; expect it to be removed in a future release. Use `INSERT` (without `DELAYED`) instead.

- If you use the `LOW_PRIORITY` modifier, execution of the `INSERT` is delayed until no other clients are

reading from the table. This includes other clients that began reading while existing clients are reading,and while the `INSERT LOW_PRIORITY` statement is waiting. It is possible, therefore, for a client that issues an `INSERT LOW_PRIORITY` statement to wait for a very long time (or even forever) in a read-heavy environment. (This is in contrast to `INSERT DELAYED`, which lets the client continue at once.)`LOW_PRIORITY` affects only storage engines that use only table-level locking (such as `MyISAM`,`MEMORY`, and `MERGE`).

Note`LOW_PRIORITY` should normally not be used with `MyISAM` tables because doing so disables concurrent inserts. See Section 8.11.3, “Concurrent Inserts”.

- If you specify `HIGH_PRIORITY`, it overrides the effect of the `--low-priority-updates` option if the

server was started with that option. It also causes concurrent inserts not to be used. See Section 8.11.3,“Concurrent Inserts”.

`HIGH_PRIORITY` affects only storage engines that use only table-level locking (such as `MyISAM`,`MEMORY`, and `MERGE`).

- If you use the `IGNORE` modifier, errors that occur while executing the `INSERT` statement are ignored. For

example, without `IGNORE`, a row that duplicates an existing `UNIQUE` index or `PRIMARY KEY` value in the table causes a duplicate-key error and the statement is aborted. With `IGNORE`, the row is discarded and no error occurs. Ignored errors may generate warnings instead, although duplicate-key errors do not.

`IGNORE` has a similar effect on inserts into partitioned tables where no partition matching a given value is found. Without `IGNORE`, such `INSERT` statements are aborted with an error. When `INSERT IGNORE`INSERT Statement is used, the insert operation fails silently for rows containing the unmatched value, but inserts rows that are matched. For an example, see Section 19.2.2, “LIST Partitioning”.

Data conversions that would trigger errors abort the statement if `IGNORE` is not specified. With `IGNORE`,invalid values are adjusted to the closest values and inserted; warnings are produced but the statement does not abort. You can determine with the `mysql_info()` C API function how many rows were actually inserted into the table.

You can use `REPLACE` instead of `INSERT` to overwrite old rows. `REPLACE` is the counterpart to `INSERT``IGNORE` in the treatment of new rows that contain unique key values that duplicate old rows: The new rows replace the old rows rather than being discarded. See Section 13.2.8, “REPLACE Statement”.

- If you specify `ON DUPLICATE KEY UPDATE`, and a row is inserted that would cause a duplicate value

in a `UNIQUE` index or `PRIMARY KEY`, an `UPDATE` of the old row occurs. The affected-rows value per row is 1 if the row is inserted as a new row, 2 if an existing row is updated, and 0 if an existing row is set to its current values. If you specify the `CLIENT_FOUND_ROWS` flag to the `mysql_real_connect()` C API function when connecting to `mysqld`, the affected-rows value is 1 (not 0) if an existing row is set to its current values. See Section 13.2.5.2, “INSERT ... ON DUPLICATE KEY UPDATE Statement”.

An `INSERT` statement affecting a partitioned table using a storage engine such as `MyISAM` that employs table-level locks locks only those partitions into which rows are actually inserted. (For storage engines such as `InnoDB` that employ row-level locking, no locking of partitions takes place.) For more information, see Section 19.6.4, “Partitioning and Locking”.

#### 13.2.5.1 INSERT ... SELECT Statement

```
INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
[INTO] tbl_name
[PARTITION (partition_name [, partition_name] ...)]
[(col_name [, col_name] ...)]
SELECT ...
[ON DUPLICATE KEY UPDATE assignment_list]
value:
{expr | DEFAULT}
assignment:
col_name = value
assignment_list:
assignment [, assignment] ...
```

With `INSERT ... SELECT`, you can quickly insert many rows into a table from the result of a `SELECT`statement, which can select from one or many tables. For example:

```
INSERT INTO tbl_temp2 (fld_id)
SELECT tbl_temp1.fld_order_id
FROM tbl_temp1 WHERE tbl_temp1.fld_order_id > 100;
```

The following conditions hold for `INSERT ... SELECT` statements:

- Specify `IGNORE` to ignore rows that would cause duplicate-key violations.
- `DELAYED` is ignored with `INSERT ... SELECT`.
- The target table of the `INSERT` statement may appear in the `FROM` clause of the `SELECT` part of the

query. However, you cannot insert into a table and select from the same table in a subquery.

When selecting from and inserting into the same table, MySQL creates an internal temporary table to hold the rows from the `SELECT` and then inserts those rows into the target table. However, you INSERT Statement cannot use `INSERT INTO t ... SELECT ... FROM t` when t is a `TEMPORARY` table, because`TEMPORARY` tables cannot be referred to twice in the same statement. See Section 8.4.4, “Internal Temporary Table Use in MySQL”, and Section B.3.6.2, “TEMPORARY Table Problems”.

- `AUTO_INCREMENT` columns work as usual.
- To ensure that the binary log can be used to re-create the original tables, MySQL does not permit

concurrent inserts for `INSERT ... SELECT` statements (see Section 8.11.3, “Concurrent Inserts”).

- To avoid ambiguous column reference problems when the `SELECT` and the `INSERT` refer to the same

table, provide a unique alias for each table used in the `SELECT` part, and qualify column names in that part with the appropriate alias.

You can explicitly select which partitions or subpartitions (or both) of the source or target table (or both) are to be used with a `PARTITION` clause following the name of the table. When `PARTITION` is used with the name of the source table in the `SELECT` portion of the statement, rows are selected only from the partitions or subpartitions named in its partition list. When `PARTITION` is used with the name of the target table for the `INSERT` portion of the statement, it must be possible to insert all rows selected into the partitions or subpartitions named in the partition list following the option. Otherwise, the `INSERT ... SELECT`statement fails. For more information and examples, see Section 19.5, “Partition Selection”.

For `INSERT ... SELECT` statements, see Section 13.2.5.2, “INSERT ... ON DUPLICATE KEY UPDATE Statement” for conditions under which the `SELECT` columns can be referred to in an `ON DUPLICATE KEY``UPDATE` clause.

The order in which a `SELECT` statement with no `ORDER BY` clause returns rows is nondeterministic. This means that, when using replication, there is no guarantee that such a `SELECT` returns rows in the same order on the source and the replica, which can lead to inconsistencies between them. To prevent this from occurring, always write `INSERT ... SELECT` statements that are to be replicated using an `ORDER``BY` clause that produces the same row order on the source and the replica. See also Section 17.4.1.17,“Replication and LIMIT”.

Due to this issue, `INSERT ... SELECT ON DUPLICATE KEY UPDATE` and `INSERT IGNORE ...``SELECT` statements are flagged as unsafe for statement-based replication. Such statements produce a warning in the error log when using statement-based mode and are written to the binary log using the row-based format when using `MIXED` mode. (Bug #11758262, Bug #50439)See also Section 17.1.2.1, “Advantages and Disadvantages of Statement-Based and Row-Based Replication”.

An `INSERT ... SELECT` statement affecting partitioned tables using a storage engine such as `MyISAM`that employs table-level locks locks all partitions of the target table; however, only those partitions that are actually read from the source table are locked. (This does not occur with tables using storage engines such as `InnoDB` that employ row-level locking.) For more information, see Section 19.6.4, “Partitioning and Locking”.

#### 13.2.5.2 INSERT ... ON DUPLICATE KEY UPDATE Statement

If you specify an `ON DUPLICATE KEY UPDATE` clause and a row to be inserted would cause a duplicate value in a `UNIQUE` index or `PRIMARY KEY`, an `UPDATE` of the old row occurs. For example, if column a is declared as `UNIQUE` and contains the value 1, the following two statements have similar effect:

```
INSERT INTO t1 (a,b,c) VALUES (1,2,3)
ON DUPLICATE KEY UPDATE c=c+1;
UPDATE t1 SET c=c+1 WHERE a=1;
```

INSERT Statement The effects are not quite identical: For an `InnoDB` table where a is an auto-increment column, the `INSERT`statement increases the auto-increment value but the `UPDATE` does not.

If column b is also unique, the `INSERT` is equivalent to this `UPDATE` statement instead:

```
UPDATE t1 SET c=c+1 WHERE a=1 OR b=2 LIMIT 1;
```

If `a=1 OR b=2` matches several rows, only one row is updated. In general, you should try to avoid using an `ON DUPLICATE KEY UPDATE` clause on tables with multiple unique indexes.

With `ON DUPLICATE KEY UPDATE`, the affected-rows value per row is 1 if the row is inserted as a new row, 2 if an existing row is updated, and 0 if an existing row is set to its current values. If you specify the`CLIENT_FOUND_ROWS` flag to the `mysql_real_connect()` C API function when connecting to `mysqld`,the affected-rows value is 1 (not 0) if an existing row is set to its current values.

If a table contains an `AUTO_INCREMENT` column and `INSERT ... ON DUPLICATE KEY UPDATE` inserts or updates a row, the `LAST_INSERT_ID()` function returns the `AUTO_INCREMENT` value.

The `ON DUPLICATE KEY UPDATE` clause can contain multiple column assignments, separated by commas.

In assignment value expressions in the `ON DUPLICATE KEY UPDATE` clause, you can use the`VALUES(col_name)` function to refer to column values from the `INSERT` portion of the `INSERT ...``ON DUPLICATE KEY UPDATE` statement. In other words, `VALUES(col_name)` in the `ON DUPLICATE``KEY UPDATE` clause refers to the value of `col_name` that would be inserted, had no duplicate-key conflict occurred. This function is especially useful in multiple-row inserts. The `VALUES()` function is meaningful only in the `ON DUPLICATE KEY UPDATE` clause or `INSERT` statements and returns `NULL` otherwise.

Example:

```
INSERT INTO t1 (a,b,c) VALUES (1,2,3),(4,5,6)
ON DUPLICATE KEY UPDATE c=VALUES(a)+VALUES(b);
```

That statement is identical to the following two statements:

```
INSERT INTO t1 (a,b,c) VALUES (1,2,3)
ON DUPLICATE KEY UPDATE c=3;
INSERT INTO t1 (a,b,c) VALUES (4,5,6)
ON DUPLICATE KEY UPDATE c=9;
```

The `DELAYED` option is ignored when you use `ON DUPLICATE KEY UPDATE`.

For `INSERT ... SELECT` statements, these rules apply regarding acceptable forms of `SELECT` query expressions that you can refer to in an `ON DUPLICATE KEY UPDATE` clause:

- References to columns from queries on a single table, which may be a derived table.
- References to columns from queries on a join over multiple tables.
- References to columns from `DISTINCT` queries.
- References to columns in other tables, as long as the `SELECT` does not use `GROUP BY`. One side effect

is that you must qualify references to nonunique column names.

References to columns from a `UNION` do not work reliably. To work around this restriction, rewrite the`UNION` as a derived table so that its rows can be treated as a single-table result set. For example, this statement can produce incorrect results:

```
INSERT INTO t1 (a, b)
SELECT c, d FROM t2
UNION
```

INSERT Statement

```
SELECT e, f FROM t3
ON DUPLICATE KEY UPDATE b = b + c;
```

Instead, use an equivalent statement that rewrites the `UNION` as a derived table:

```
INSERT INTO t1 (a, b)
SELECT * FROM
(SELECT c, d FROM t2
UNION
SELECT e, f FROM t3) AS dt
ON DUPLICATE KEY UPDATE b = b + c;
```

The technique of rewriting a query as a derived table also enables references to columns from `GROUP BY`queries.

Because the results of `INSERT ... SELECT` statements depend on the ordering of rows from the`SELECT` and this order cannot always be guaranteed, it is possible when logging `INSERT ... SELECT``ON DUPLICATE KEY UPDATE` statements for the source and the replica to diverge. Thus, `INSERT ...``SELECT ON DUPLICATE KEY UPDATE` statements are flagged as unsafe for statement-based replication.

Such statements produce a warning in the error log when using statement-based mode and are written to the binary log using the row-based format when using `MIXED` mode. An `INSERT ... ON DUPLICATE``KEY UPDATE` statement against a table having more than one unique or primary key is also marked as unsafe. (Bug #11765650, Bug #58637)See also Section 17.1.2.1, “Advantages and Disadvantages of Statement-Based and Row-Based Replication”.

An `INSERT ... ON DUPLICATE KEY UPDATE` on a partitioned table using a storage engine such as`MyISAM` that employs table-level locks locks any partitions of the table in which a partitioning key column is updated. (This does not occur with tables using storage engines such as `InnoDB` that employ row-level locking.) For more information, see Section 19.6.4, “Partitioning and Locking”.

#### 13.2.5.3 INSERT DELAYED Statement

```
INSERT DELAYED ...
```

The `DELAYED` option for the `INSERT` statement is a MySQL extension to standard SQL that can be used for certain kinds of tables (such as `MyISAM`). When a client uses `INSERT DELAYED`, it gets an okay from the server at once, and the row is queued to be inserted when the table is not in use by any other thread.

Note`INSERT DELAYED` is slower than a normal `INSERT` if the table is not otherwise in use. There is also the additional overhead for the server to handle a separate thread for each table for which there are delayed rows. This means that you should use `INSERT DELAYED` only when you are really sure that you need it.

As of MySQL 5.6.6, `INSERT DELAYED` is deprecated; expect it to be removed in a future release. Use `INSERT` (without `DELAYED`) instead.

The queued rows are held only in memory until they are inserted into the table. This means that if you terminate `mysqld` forcibly (for example, with `kill -9`) or if `mysqld` dies unexpectedly, any queued rows that have not been written to disk are lost.

There are some constraints on the use of `DELAYED`:

- `INSERT DELAYED` works only with `MyISAM`, `MEMORY`, `ARCHIVE`, and `BLACKHOLE` tables. For engines

that do not support `DELAYED`, an error occurs.

INSERT Statement

- An error occurs for `INSERT DELAYED` if used with a table that has been locked with `LOCK TABLES`

because the insert must be handled by a separate thread, not by the session that holds the lock.

- For `MyISAM` tables, if there are no free blocks in the middle of the data file, concurrent `SELECT` and

`INSERT` statements are supported. Under these circumstances, you very seldom need to use `INSERT``DELAYED` with `MyISAM`.

- `INSERT DELAYED` should be used only for `INSERT` statements that specify value lists. The server

```
ignores DELAYED for INSERT ... SELECT or INSERT ... ON DUPLICATE KEY UPDATE
```

statements.

- Because the `INSERT DELAYED` statement returns immediately, before the rows are inserted, you cannot

use `LAST_INSERT_ID()` to get the `AUTO_INCREMENT` value that the statement might generate.

- `DELAYED` rows are not visible to `SELECT` statements until they actually have been inserted.
- `INSERT DELAYED` is handled as a simple `INSERT` (that is, without the `DELAYED` option) whenever the

value of `binlog_format` is `STATEMENT` or `MIXED`. (In the latter case, the statement does not trigger a switch to row-based logging, and so is logged using the statement-based format.)This does not apply when using row-based binary logging mode (`binlog_format` set to `ROW`), in which`INSERT DELAYED` statements are always executed using the `DELAYED` option as specified, and logged as row-update events.

- `DELAYED` is ignored on replica servers, so that `INSERT DELAYED` is treated as a normal `INSERT` on

replicas. This is because `DELAYED` could cause the slave to have different data than the source.

- Pending `INSERT DELAYED` statements are lost if a table is write locked and `ALTER TABLE` is used to

modify the table structure.

- `INSERT DELAYED` is not supported for views.
- `INSERT DELAYED` is not supported for partitioned tables.

The following describes in detail what happens when you use the `DELAYED` option to `INSERT` or `REPLACE`.

In this description, the “thread” is the thread that received an `INSERT DELAYED` statement and “handler” is the thread that handles all `INSERT DELAYED` statements for a particular table.

- When a thread executes a `DELAYED` statement for a table, a handler thread is created to process all

`DELAYED` statements for the table, if no such handler already exists.

- The thread checks whether the handler has previously acquired a `DELAYED` lock; if not, it tells the

handler thread to do so. The `DELAYED` lock can be obtained even if other threads have a `READ` or `WRITE`lock on the table. However, the handler waits for all `ALTER TABLE` locks or `FLUSH TABLES` statements to finish, to ensure that the table structure is up to date.

- The thread executes the `INSERT` statement, but instead of writing the row to the table, it puts a copy of

the final row into a queue that is managed by the handler thread. Any syntax errors are noticed by the thread and reported to the client program.

- The client cannot obtain from the server the number of duplicate rows or the `AUTO_INCREMENT` value for

the resulting row, because the `INSERT` returns before the insert operation has been completed. (If you use the C API, the `mysql_info()` function does not return anything meaningful, for the same reason.)

- The binary log is updated by the handler thread when the row is inserted into the table. In case of

multiple-row inserts, the binary log is updated when the first row is inserted.

- Each time that `delayed_insert_limit` rows are written, the handler checks whether any `SELECT`

statements are still pending. If so, it permits these to execute before continuing.

LOAD DATA Statement

- When the handler has no more rows in its queue, the table is unlocked. If no new `INSERT DELAYED`

statements are received within `delayed_insert_timeout` seconds, the handler terminates.

- If more than `delayed_queue_size` rows are pending in a specific handler queue, the thread

requesting `INSERT DELAYED` waits until there is room in the queue. This is done to ensure that `mysqld`does not use all memory for the delayed memory queue.

- The handler thread shows up in the MySQL process list with `delayed_insert` in the `Command` column.

It is killed if you execute a `FLUSH TABLES` statement or kill it with `KILL thread_id`. However, before exiting, it first stores all queued rows into the table. During this time it does not accept any new `INSERT`statements from other threads. If you execute an `INSERT DELAYED` statement after this, a new handler thread is created.

This means that `INSERT DELAYED` statements have higher priority than normal `INSERT` statements if there is an `INSERT DELAYED` handler running. Other update statements have to wait until the`INSERT DELAYED` queue is empty, someone terminates the handler thread (with `KILL thread_id`), or someone executes a `FLUSH TABLES`.

- The following status variables provide information about `INSERT DELAYED` statements.

Status Variable Meaning`Delayed_insert_threads` Number of handler threads`Delayed_writes` Number of rows written with `INSERT DELAYED``Not_flushed_delayed_rows` Number of rows waiting to be written You can view these variables by issuing a `SHOW STATUS` statement or by executing a `mysqladmin``extended-status` command.

### 13.2.6 LOAD DATA Statement

```
LOAD DATA
[LOW_PRIORITY | CONCURRENT] [LOCAL]
INFILE 'file_name'
[REPLACE | IGNORE]
INTO TABLE tbl_name
[PARTITION (partition_name [, partition_name] ...)]
[CHARACTER SET charset_name]
[{FIELDS | COLUMNS}
[TERMINATED BY 'string']
[[OPTIONALLY] ENCLOSED BY 'char']
[ESCAPED BY 'char']
]
[LINES
[STARTING BY 'string']
[TERMINATED BY 'string']
]
[IGNORE number {LINES | ROWS}]
[(col_name_or_user_var
[, col_name_or_user_var] ...)]
[SET col_name={expr | DEFAULT}
[, col_name={expr | DEFAULT}] ...]
```

The `LOAD DATA` statement reads rows from a text file into a table at a very high speed. The file can be read from the server host or the client host, depending on whether the `LOCAL` modifier is given. `LOCAL` also affects data interpretation and error handling.

`LOAD DATA` is the complement of `SELECT ... INTO OUTFILE`. (See Section 13.2.9.1, “SELECT ...

INTO Statement”.) To write data from a table to a file, use `SELECT ... INTO OUTFILE`. To read the LOAD DATA Statement file back into a table, use `LOAD DATA`. The syntax of the `FIELDS` and `LINES` clauses is the same for both statements.

The `mysqlimport` utility provides another way to load data files; it operates by sending a `LOAD DATA`statement to the server. See Section 4.5.5, “mysqlimport — A Data Import Program”.

For information about the efficiency of `INSERT` versus `LOAD DATA` and speeding up `LOAD DATA`, see Section 8.2.4.1, “Optimizing INSERT Statements”.

- Non-LOCAL Versus LOCAL Operation
- Input File Character Set
- Input File Location
- Security Requirements
- Duplicate-Key and Error Handling
- Index Handling
- Field and Line Handling
- Column List Specification
- Input Preprocessing
- Column Value Assignment
- Partitioned Table Support
- Concurrency Considerations
- Statement Result Information
- Replication Considerations
- Miscellaneous Topics

> Non-LOCAL Versus LOCAL Operation

The `LOCAL` modifier affects these aspects of `LOAD DATA`, compared to non-`LOCAL` operation:

- It changes the expected location of the input file; see Input File Location.
- It changes the statement security requirements; see Security Requirements.
- It has the same effect as the `IGNORE` modifier on the interpretation of input file contents and error

handling; see Duplicate-Key and Error Handling, and Column Value Assignment.

`LOCAL` works only if the server and your client both have been configured to permit it. For example, if`mysqld` was started with the `local_infile` system variable disabled, `LOCAL` produces an error. See Section 6.1.6, “Security Considerations for LOAD DATA LOCAL”.

> Input File Character Set

The file name must be given as a literal string. On Windows, specify backslashes in path names as forward slashes or doubled backslashes. The server interprets the file name using the character set indicated by the `character_set_filesystem` system variable.

LOAD DATA Statement By default, the server interprets the file contents using the character set indicated by the`character_set_database` system variable. If the file contents use a character set different from this default, it is a good idea to specify that character set by using the `CHARACTER SET` clause. A character set of `binary` specifies “no conversion.”`SET NAMES` and the setting of `character_set_client` do not affect interpretation of file contents.

`LOAD DATA` interprets all fields in the file as having the same character set, regardless of the data types of the columns into which field values are loaded. For proper interpretation of the file, you must ensure that it was written with the correct character set. For example, if you write a data file with `mysqldump -T` or by issuing a `SELECT ... INTO OUTFILE` statement in `mysql`, be sure to use a `--default-character-``set` option to write output in the character set to be used when the file is loaded with `LOAD DATA`.

Note It is not possible to load data files that use the `ucs2`, `utf16`, `utf16le`, or `utf32`character set.

> Input File Location

These rules determine the `LOAD DATA` input file location:

- If `LOCAL` is not specified, the file must be located on the server host. The server reads the file directly,

locating it as follows:

- If the file name is an absolute path name, the server uses it as given.
- If the file name is a relative path name with leading components, the server looks for the file relative to

its data directory.

- If the file name has no leading components, the server looks for the file in the database directory of the

default database.

- If `LOCAL` is specified, the file must be located on the client host. The client program reads the file,

locating it as follows:

- If the file name is an absolute path name, the client program uses it as given.
- If the file name is a relative path name, the client program looks for the file relative to its invocation

directory.

When `LOCAL` is used, the client program reads the file and sends its contents to the server. The server creates a copy of the file in the directory where it stores temporary files. See Section B.3.3.5, “Where MySQL Stores Temporary Files”. Lack of sufficient space for the copy in this directory can cause the`LOAD DATA LOCAL` statement to fail.

The non-`LOCAL` rules mean that the server reads a file named as `./myfile.txt` relative to its data directory, whereas it reads a file named as `myfile.txt` from the database directory of the default database. For example, if the following `LOAD DATA` statement is executed while `db1` is the default database, the server reads the file `data.txt` from the database directory for `db1`, even though the statement explicitly loads the file into a table in the `db2` database:

```
LOAD DATA INFILE 'data.txt' INTO TABLE db2.my_table;
```

> Security Requirements

For a non-`LOCAL` load operation, the server reads a text file located on the server host, so these security requirements must be satisified:LOAD DATA Statement

- You must have the `FILE` privilege. See Section 6.2.2, “Privileges Provided by MySQL”.
- The operation is subject to the `secure_file_priv` system variable setting:
- If the variable value is a nonempty directory name, the file must be located in that directory.
- If the variable value is empty (which is insecure), the file need only be readable by the server.

For a `LOCAL` load operation, the client program reads a text file located on the client host. Because the file contents are sent over the connection by the client to the server, using `LOCAL` is a bit slower than when the server accesses the file directly. On the other hand, you do not need the `FILE` privilege, and the file can be located in any directory the client program can access.

> Duplicate-Key and Error Handling

The `REPLACE` and `IGNORE` modifiers control handling of new (input) rows that duplicate existing table rows on unique key values (`PRIMARY KEY` or `UNIQUE` index values):

- With `REPLACE`, new rows that have the same value as a unique key value in an existing row replace the

existing row. See Section 13.2.8, “REPLACE Statement”.

- With `IGNORE`, new rows that duplicate an existing row on a unique key value are discarded.

The `LOCAL` modifier has the same effect as `IGNORE`. This occurs because the server has no way to stop transmission of the file in the middle of the operation.

If none of `REPLACE`, `IGNORE`, or `LOCAL` is specified, an error occurs when a duplicate key value is found,and the rest of the text file is ignored.

In addition to affecting duplicate-key handling as just described, `IGNORE` and `LOCAL` also affect error handling:

- With neither `IGNORE` nor `LOCAL`, data-interpretation errors terminate the operation.
- With `IGNORE` or `LOCAL`, data-interpretation errors become warnings and the load operation continues,

even if the SQL mode is restrictive. For examples, see Column Value Assignment.

> Index Handling

To ignore foreign key constraints during the load operation, execute a `SET foreign_key_checks = 0`statement before executing `LOAD DATA`.

If you use `LOAD DATA` on an empty `MyISAM` table, all nonunique indexes are created in a separate batch(as for `REPAIR TABLE`). Normally, this makes `LOAD DATA` much faster when you have many indexes. In some extreme cases, you can create the indexes even faster by turning them off with `ALTER TABLE ...``DISABLE KEYS` before loading the file into the table and re-creating the indexes with `ALTER TABLE ...``ENABLE KEYS` after loading the file. See Section 8.2.4.1, “Optimizing INSERT Statements”.

> Field and Line Handling

For both the `LOAD DATA` and `SELECT ... INTO OUTFILE` statements, the syntax of the `FIELDS`and `LINES` clauses is the same. Both clauses are optional, but `FIELDS` must precede `LINES` if both are specified.

If you specify a `FIELDS` clause, each of its subclauses (`TERMINATED BY`, `[OPTIONALLY] ENCLOSED``BY`, and `ESCAPED BY`) is also optional, except that you must specify at least one of them. Arguments to these clauses are permitted to contain only ASCII characters.

LOAD DATA Statement If you specify no `FIELDS` or `LINES` clause, the defaults are the same as if you had written this:

```
FIELDS TERMINATED BY '\t' ENCLOSED BY '' ESCAPED BY '\\'
LINES TERMINATED BY '\n' STARTING BY ''
```

Backslash is the MySQL escape character within strings in SQL statements. Thus, to specify a literal backslash, you must specify two backslashes for the value to be interpreted as a single backslash. The escape sequences `'\t'` and `'\n'` specify tab and newline characters, respectively.

In other words, the defaults cause `LOAD DATA` to act as follows when reading input:

- Look for line boundaries at newlines.
- Do not skip any line prefix.
- Break lines into fields at tabs.
- Do not expect fields to be enclosed within any quoting characters.
- Interpret characters preceded by the escape character \ as escape sequences. For example, `\t`, `\n`,

and `\\` signify tab, newline, and backslash, respectively. See the discussion of `FIELDS ESCAPED BY`later for the full list of escape sequences.

Conversely, the defaults cause `SELECT ... INTO OUTFILE` to act as follows when writing output:

- Write tabs between fields.
- Do not enclose fields within any quoting characters.
- Use \ to escape instances of tab, newline, or \ that occur within field values.
- Write newlines at the ends of lines.

Note For a text file generated on a Windows system, proper file reading might require`LINES TERMINATED BY '\r\n'` because Windows programs typically use two characters as a line terminator. Some programs, such as `WordPad`, might use `\r`as a line terminator when writing files. To read such files, use `LINES TERMINATED`

```
BY '\r'.
```

If all the input lines have a common prefix that you want to ignore, you can use `LINES STARTING BY``'prefix_string'` to skip the prefix and anything before it. If a line does not include the prefix, the entire line is skipped. Suppose that you issue the following statement:

```
LOAD DATA INFILE '/tmp/test.txt' INTO TABLE test
FIELDS TERMINATED BY ','  LINES STARTING BY 'xxx';
```

If the data file looks like this:

```
xxx"abc",1
something xxx"def",2
"ghi",3
```

The resulting rows are `("abc",1)` and `("def",2)`. The third row in the file is skipped because it does not contain the prefix.

The `IGNORE number LINES` clause can be used to ignore lines at the start of the file. For example, you can use `IGNORE 1 LINES` to skip an initial header line containing column names:LOAD DATA Statement

```
LOAD DATA INFILE '/tmp/test.txt' INTO TABLE test IGNORE 1 LINES;
```

When you use `SELECT ... INTO OUTFILE` in tandem with `LOAD DATA` to write data from a database into a file and then read the file back into the database later, the field- and line-handling options for both statements must match. Otherwise, `LOAD DATA` does not interpret the contents of the file properly.

Suppose that you use `SELECT ... INTO OUTFILE` to write a file with fields delimited by commas:

```
SELECT * INTO OUTFILE 'data.txt'
FIELDS TERMINATED BY ','
FROM table2;
```

To read the comma-delimited file, the correct statement is:

```
LOAD DATA INFILE 'data.txt' INTO TABLE table2
FIELDS TERMINATED BY ',';
```

If instead you tried to read the file with the statement shown following, it would not work because it instructs`LOAD DATA` to look for tabs between fields:

```
LOAD DATA INFILE 'data.txt' INTO TABLE table2
FIELDS TERMINATED BY '\t';
```

The likely result is that each input line would be interpreted as a single field.

`LOAD DATA` can be used to read files obtained from external sources. For example, many programs can export data in comma-separated values (CSV) format, such that lines have fields separated by commas and enclosed within double quotation marks, with an initial line of column names. If the lines in such a file are terminated by carriage return/newline pairs, the statement shown here illustrates the field- and line-handling options you would use to load the file:

```
LOAD DATA INFILE 'data.txt' INTO TABLE tbl_name
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;
```

If the input values are not necessarily enclosed within quotation marks, use `OPTIONALLY` before the`ENCLOSED BY` option.

Any of the field- or line-handling options can specify an empty string (`''`). If not empty, the `FIELDS``[OPTIONALLY] ENCLOSED BY` and `FIELDS ESCAPED BY` values must be a single character. The`FIELDS TERMINATED BY`, `LINES STARTING BY`, and `LINES TERMINATED BY` values can be more than one character. For example, to write lines that are terminated by carriage return/linefeed pairs, or to read a file containing such lines, specify a `LINES TERMINATED BY '\r\n'` clause.

To read a file containing jokes that are separated by lines consisting of `%%`, you can do this

```
CREATE TABLE jokes
(a INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
joke TEXT NOT NULL);
LOAD DATA INFILE '/tmp/jokes.txt' INTO TABLE jokes
FIELDS TERMINATED BY ''
LINES TERMINATED BY '\n%%\n' (joke);
```

`FIELDS [OPTIONALLY] ENCLOSED BY` controls quoting of fields. For output (`SELECT ... INTO``OUTFILE`), if you omit the word `OPTIONALLY`, all fields are enclosed by the `ENCLOSED BY` character. An example of such output (using a comma as the field delimiter) is shown here:

```
"1","a string","100.20"
"2","a string containing a , comma","102.20"
"3","a string containing a \" quote","102.20"
```

LOAD DATA Statement

```
"4","a string containing a \", quote and comma","102.20"
```

If you specify `OPTIONALLY`, the `ENCLOSED BY` character is used only to enclose values from columns that have a string data type (such as `CHAR`, `BINARY`, `TEXT`, or `ENUM`):

```
1,"a string",100.20
2,"a string containing a , comma",102.20
3,"a string containing a \" quote",102.20
4,"a string containing a \", quote and comma",102.20
```

Occurrences of the `ENCLOSED BY` character within a field value are escaped by prefixing them with the`ESCAPED BY` character. Also, if you specify an empty `ESCAPED BY` value, it is possible to inadvertently generate output that cannot be read properly by `LOAD DATA`. For example, the preceding output just shown would appear as follows if the escape character is empty. Observe that the second field in the fourth line contains a comma following the quote, which (erroneously) appears to terminate the field:

```
1,"a string",100.20
2,"a string containing a , comma",102.20
3,"a string containing a " quote",102.20
4,"a string containing a ", quote and comma",102.20
```

For input, the `ENCLOSED BY` character, if present, is stripped from the ends of field values. (This is true regardless of whether `OPTIONALLY` is specified; `OPTIONALLY` has no effect on input interpretation.)Occurrences of the `ENCLOSED BY` character preceded by the `ESCAPED BY` character are interpreted as part of the current field value.

If the field begins with the `ENCLOSED BY` character, instances of that character are recognized as terminating a field value only if followed by the field or line `TERMINATED BY` sequence. To avoid ambiguity, occurrences of the `ENCLOSED BY` character within a field value can be doubled and are interpreted as a single instance of the character. For example, if `ENCLOSED BY '"'` is specified,quotation marks are handled as shown here:

```
"The ""BIG"" boss"  -> The "BIG" boss
The "BIG" boss      -> The "BIG" boss
The ""BIG"" boss    -> The ""BIG"" boss
```

`FIELDS ESCAPED BY` controls how to read or write special characters:

- For input, if the `FIELDS ESCAPED BY` character is not empty, occurrences of that character are stripped

and the following character is taken literally as part of a field value. Some two-character sequences that are exceptions, where the first character is the escape character. These sequences are shown in the following table (using \ for the escape character). The rules for `NULL` handling are described later in this section.

Character Escape Sequence`\0` An ASCII NUL (`X'00'`) character`\b` A backspace character`\n` A newline (linefeed) character`\r` A carriage return character`\t` A tab character.

`\Z` ASCII 26 (Control+Z)`\N` NULL For more information about \-escape syntax, see Section 9.1.1, “String Literals”.

If the `FIELDS ESCAPED BY` character is empty, escape-sequence interpretation does not occur.

LOAD DATA Statement

- For output, if the `FIELDS ESCAPED BY` character is not empty, it is used to prefix the following

characters on output:

- The `FIELDS ESCAPED BY` character.
- The `FIELDS [OPTIONALLY] ENCLOSED BY` character.
- The first character of the `FIELDS TERMINATED BY` and `LINES TERMINATED BY` values, if the

`ENCLOSED BY` character is empty or unspecified.

- ASCII 0 (what is actually written following the escape character is ASCII 0, not a zero-valued byte).

If the `FIELDS ESCAPED BY` character is empty, no characters are escaped and `NULL` is output as`NULL`, not `\N`. It is probably not a good idea to specify an empty escape character, particularly if field values in your data contain any of the characters in the list just given.

In certain cases, field- and line-handling options interact:

- If `LINES TERMINATED BY` is an empty string and `FIELDS TERMINATED BY` is nonempty, lines are

also terminated with `FIELDS TERMINATED BY`.

- If the `FIELDS TERMINATED BY` and `FIELDS ENCLOSED BY` values are both empty (`''`), a fixed-row

(nondelimited) format is used. With fixed-row format, no delimiters are used between fields (but you can still have a line terminator). Instead, column values are read and written using a field width wide enough to hold all values in the field. For `TINYINT`, `SMALLINT`, `MEDIUMINT`, `INT`, and `BIGINT`, the field widths are 4, 6, 8, 11, and 20, respectively, no matter what the declared display width is.

`LINES TERMINATED BY` is still used to separate lines. If a line does not contain all fields, the rest of the columns are set to their default values. If you do not have a line terminator, you should set this to `''`. In this case, the text file must contain all fields for each row.

Fixed-row format also affects handling of `NULL` values, as described later.

Note Fixed-size format does not work if you are using a multibyte character set.

Handling of `NULL` values varies according to the `FIELDS` and `LINES` options in use:

- For the default `FIELDS` and `LINES` values, `NULL` is written as a field value of `\N` for output, and a field

value of `\N` is read as `NULL` for input (assuming that the `ESCAPED BY` character is \).

- If `FIELDS ENCLOSED BY` is not empty, a field containing the literal word `NULL` as its value is read as a

`NULL` value. This differs from the word `NULL` enclosed within `FIELDS ENCLOSED BY` characters, which is read as the string `'NULL'`.

- If `FIELDS ESCAPED BY` is empty, `NULL` is written as the word `NULL`.
- With fixed-row format (which is used when `FIELDS TERMINATED BY` and `FIELDS ENCLOSED BY` are

both empty), `NULL` is written as an empty string. This causes both `NULL` values and empty strings in the table to be indistinguishable when written to the file because both are written as empty strings. If you need to be able to tell the two apart when reading the file back in, you should not use fixed-row format.

An attempt to load `NULL` into a `NOT NULL` column produces either a warning or an error according to the rules described in Column Value Assignment.

Some cases are not supported by `LOAD DATA`:LOAD DATA Statement

- Fixed-size rows (`FIELDS TERMINATED BY` and `FIELDS ENCLOSED BY` both empty) and `BLOB` or

`TEXT` columns.

- If you specify one separator that is the same as or a prefix of another, `LOAD DATA` cannot interpret the

input properly. For example, the following `FIELDS` clause would cause problems:

```
FIELDS TERMINATED BY '"' ENCLOSED BY '"'
```

- If `FIELDS ESCAPED BY` is empty, a field value that contains an occurrence of `FIELDS ENCLOSED`

`BY` or `LINES TERMINATED BY` followed by the `FIELDS TERMINATED BY` value causes `LOAD DATA`to stop reading a field or line too early. This happens because `LOAD DATA` cannot properly determine where the field or line value ends.

> Column List Specification

The following example loads all columns of the `persondata` table:

```
LOAD DATA INFILE 'persondata.txt' INTO TABLE persondata;
```

By default, when no column list is provided at the end of the `LOAD DATA` statement, input lines are expected to contain a field for each table column. If you want to load only some of a table's columns,specify a column list:

```
LOAD DATA INFILE 'persondata.txt' INTO TABLE persondata
(col_name_or_user_var [, col_name_or_user_var] ...);
```

You must also specify a column list if the order of the fields in the input file differs from the order of the columns in the table. Otherwise, MySQL cannot tell how to match input fields with table columns.

> Input Preprocessing

Each instance of `col_name_or_user_var` in `LOAD DATA` syntax is either a column name or a user variable. With user variables, the `SET` clause enables you to perform preprocessing transformations on their values before assigning the result to columns.

User variables in the `SET` clause can be used in several ways. The following example uses the first input column directly for the value of `t1.column1`, and assigns the second input column to a user variable that is subjected to a division operation before being used for the value of `t1.column2`:

```
LOAD DATA INFILE 'file.txt'
INTO TABLE t1
(column1, @var1)
SET column2 = @var1/100;
```

The `SET` clause can be used to supply values not derived from the input file. The following statement sets`column3` to the current date and time:

```
LOAD DATA INFILE 'file.txt'
INTO TABLE t1
(column1, column2)
SET column3 = CURRENT_TIMESTAMP;
```

You can also discard an input value by assigning it to a user variable and not assigning the variable to any table column:

```
LOAD DATA INFILE 'file.txt'
INTO TABLE t1
(column1, @dummy, column2, @dummy, column3);
```

LOAD DATA Statement Use of the column/variable list and `SET` clause is subject to the following restrictions:

- Assignments in the `SET` clause should have only column names on the left hand side of assignment

operators.

- You can use subqueries in the right hand side of `SET` assignments. A subquery that returns a value to be

assigned to a column may be a scalar subquery only. Also, you cannot use a subquery to select from the table that is being loaded.

- Lines ignored by an `IGNORE number LINES` clause are not processed for the column/variable list or

`SET` clause.

- User variables cannot be used when loading data with fixed-row format because user variables do not

have a display width.

> Column Value Assignment

To process an input line, `LOAD DATA` splits it into fields and uses the values according to the column/variable list and the `SET` clause, if they are present. Then the resulting row is inserted into the table. If there are `BEFORE INSERT` or `AFTER INSERT` triggers for the table, they are activated before or after inserting the row, respectively.

Interpretation of field values and assignment to table columns depends on these factors:

- The SQL mode (the value of the `sql_mode` system variable). The mode can be nonstrictive, or

restrictive in various ways. For example, strict SQL mode can be enabled, or the mode can include values such as `NO_ZERO_DATE` or `NO_ZERO_IN_DATE`.

- Presence or absence of the `IGNORE` and `LOCAL` modifiers.

Those factors combine to produce restrictive or nonrestrictive data interpretation by `LOAD DATA`:

- Data interpretation is restrictive if the SQL mode is restrictive and neither the `IGNORE` nor the `LOCAL`

modifier is specified. Errors terminate the load operation.

- Data interpretation is nonrestrictive if the SQL mode is nonrestrictive or the `IGNORE` or `LOCAL` modifier

is specified. (In particular, either modifier if specified overrides a restrictive SQL mode.) Errors become warnings and the load operation continues.

Restrictive data interpretation uses these rules:

- Too many or too few fields results an error.
- Assigning `NULL` (that is, `\N`) to a non-`NULL` column results in an error.
- A value that is out of range for the column data type results in an error.
- Invalid values produce errors. For example, a value such as `'x'` for a numeric column results in an

error, not conversion to 0.

By contrast, nonrestrictive data interpretation uses these rules:

- If an input line has too many fields, the extra fields are ignored and the number of warnings is

incremented.

- If an input line has too few fields, the columns for which input fields are missing are assigned their

default values. Default value assignment is described in Section 11.5, “Data Type Default Values”.

LOAD DATA Statement

- Assigning `NULL` (that is, `\N`) to a non-`NULL` column results in assignment of the implicit default value for

the column data type. Implicit default values are described in Section 11.5, “Data Type Default Values”.

- Invalid values produce warnings rather than errors, and are converted to the “closest” valid value for the

column data type. Examples:

- A value such as `'x'` for a numeric column results in conversion to 0.
- An out-of-range numeric or temporal value is clipped to the closest endpoint of the range for the

column data type.

- An invalid value for a `DATETIME`, `DATE`, or `TIME` column is inserted as the implicit default value,

regardless of the SQL mode `NO_ZERO_DATE` setting. The implicit default is the appropriate “zero”value for the type (`'0000-00-00 00:00:00'`, `'0000-00-00'`, or `'00:00:00'`). See Section 11.2,“Date and Time Data Types”.

- `LOAD DATA` interprets an empty field value differently from a missing field:
- For string types, the column is set to the empty string.
- For numeric types, the column is set to 0.
- For date and time types, the column is set to the appropriate “zero” value for the type. See

Section 11.2, “Date and Time Data Types”.

These are the same values that result if you assign an empty string explicitly to a string, numeric, or date or time type explicitly in an `INSERT` or `UPDATE` statement.

`TIMESTAMP` columns are set to the current date and time only if there is a `NULL` value for the column (that is, `\N`) and the column is not declared to permit `NULL` values, or if the `TIMESTAMP` column default value is the current timestamp and it is omitted from the field list when a field list is specified.

`LOAD DATA` regards all input as strings, so you cannot use numeric values for `ENUM` or `SET` columns the way you can with `INSERT` statements. All `ENUM` and `SET` values must be specified as strings.

`BIT` values cannot be loaded directly using binary notation (for example, `b'011010'`). To work around this, use the `SET` clause to strip off the leading `b'` and trailing ' and perform a base-2 to base-10 conversion so that MySQL loads the values into the `BIT` column properly:

```
$> cat /tmp/bit_test.txt
b'10'
b'1111111'
$> mysql test
mysql> LOAD DATA INFILE '/tmp/bit_test.txt'
INTO TABLE bit_test (@var1)
SET b = CAST(CONV(MID(@var1, 3, LENGTH(@var1)-3), 2, 10) AS UNSIGNED);
Query OK, 2 rows affected (0.00 sec)
Records: 2  Deleted: 0  Skipped: 0  Warnings: 0
mysql> SELECT BIN(b+0) FROM bit_test;
+----------+
| BIN(b+0) |
+----------+
| 10       |
| 1111111  |
+----------+
2 rows in set (0.00 sec)
```

For `BIT` values in `0b` binary notation (for example, `0b011010`), use this `SET` clause instead to strip off the leading `0b`:LOAD DATA Statement

```
SET b = CAST(CONV(MID(@var1, 3, LENGTH(@var1)-2), 2, 10) AS UNSIGNED)
```

> Partitioned Table Support

`LOAD DATA` supports explicit partition selection using the `PARTITION` clause with a list of one or more comma-separated names of partitions, subpartitions, or both. When this clause is used, if any rows from the file cannot be inserted into any of the partitions or subpartitions named in the list, the statement fails with the error `Found a row not matching the given partition set`. For more information and examples, see Section 19.5, “Partition Selection”.

For partitioned tables using storage engines that employ table locks, such as `MyISAM`, `LOAD DATA` cannot prune any partition locks. This does not apply to tables using storage engines that employ row-level locking, such as `InnoDB`. For more information, see Section 19.6.4, “Partitioning and Locking”.

> Concurrency Considerations

With the `LOW_PRIORITY` modifier, execution of the `LOAD DATA` statement is delayed until no other clients are reading from the table. This affects only storage engines that use only table-level locking (such as`MyISAM`, `MEMORY`, and `MERGE`).

With the `CONCURRENT` modifier and a `MyISAM` table that satisfies the condition for concurrent inserts (that is, it contains no free blocks in the middle), other threads can retrieve data from the table while `LOAD DATA`is executing. This modifier affects the performance of `LOAD DATA` a bit, even if no other thread is using the table at the same time.

> Statement Result Information

When the `LOAD DATA` statement finishes, it returns an information string in the following format:

```
Records: 1  Deleted: 0  Skipped: 0  Warnings: 0
```

Warnings occur under the same circumstances as when values are inserted using the `INSERT` statement(see Section 13.2.5, “INSERT Statement”), except that `LOAD DATA` also generates warnings when there are too few or too many fields in the input row.

You can use `SHOW WARNINGS` to get a list of the first `max_error_count` warnings as information about what went wrong. See Section 13.7.5.41, “SHOW WARNINGS Statement”.

If you are using the C API, you can get information about the statement by calling the `mysql_info()`function. See mysql_info().

> Replication Considerations

For information about `LOAD DATA` in relation to replication, see Section 17.4.1.18, “Replication and LOAD DATA”.

> Miscellaneous Topics

On Unix, if you need `LOAD DATA` to read from a pipe, you can use the following technique (the example loads a listing of the / directory into the table `db1.t1`):

```
mkfifo /mysql/data/db1/ls.dat
chmod 666 /mysql/data/db1/ls.dat
find / -ls > /mysql/data/db1/ls.dat &
mysql -e "LOAD DATA INFILE 'ls.dat' INTO TABLE t1" db1
```

LOAD XML Statement Here you must run the command that generates the data to be loaded and the `mysql` commands either on separate terminals, or run the data generation process in the background (as shown in the preceding example). If you do not do this, the pipe blocks until data is read by the `mysql` process.

### 13.2.7 LOAD XML Statement

```
LOAD XML
[LOW_PRIORITY | CONCURRENT] [LOCAL]
INFILE 'file_name'
[REPLACE | IGNORE]
INTO TABLE [db_name.]tbl_name
[CHARACTER SET charset_name]
[ROWS IDENTIFIED BY '<tagname>']
[IGNORE number {LINES | ROWS}]
[(field_name_or_user_var
[, field_name_or_user_var] ...)]
[SET col_name={expr | DEFAULT}
[, col_name={expr | DEFAULT}] ...]
```

The `LOAD XML` statement reads data from an XML file into a table. The `file_name` must be given as a literal string. The `tagname` in the optional `ROWS IDENTIFIED BY` clause must also be given as a literal string, and must be surrounded by angle brackets (< and >).

`LOAD XML` acts as the complement of running the `mysql` client in XML output mode (that is, starting the client with the `--xml` option). To write data from a table to an XML file, you can invoke the `mysql` client with the `--xml` and `-e` options from the system shell, as shown here:

```
$> mysql --xml -e 'SELECT * FROM mydb.mytable' > file.xml
```

To read the file back into a table, use `LOAD XML`. By default, the `<row>` element is considered to be the equivalent of a database table row; this can be changed using the `ROWS IDENTIFIED BY` clause.

This statement supports three different XML formats:

- Column names as attributes and column values as attribute values:

```
<row column1="value1" column2="value2" .../>
```

- Column names as tags and column values as the content of these tags:

```
<row>
<column1>value1</column1>
<column2>value2</column2>
</row>
```

- Column names are the `name` attributes of `<field>` tags, and values are the contents of these tags:

```
<row>
<field name='column1'>value1</field>
<field name='column2'>value2</field>
</row>
```

This is the format used by other MySQL tools, such as `mysqldump`.

All three formats can be used in the same XML file; the import routine automatically detects the format for each row and interprets it correctly. Tags are matched based on the tag or attribute name and the column name.

Prior to MySQL 5.6.27, `LOAD XML` did not handle empty XML elements in the form `<element/>` correctly.

(Bug #67542, Bug #16171518)LOAD XML Statement In MySQL 5.6, `LOAD XML` does not support `CDATA` sections in the source XML. This limitation is removed in MySQL 8.0. (Bug #30753708, Bug #98199)The following clauses work essentially the same way for `LOAD XML` as they do for `LOAD DATA`:

```
- LOW_PRIORITY or CONCURRENT
- LOCAL
- REPLACE or IGNORE
- CHARACTER SET
- SET
```

See Section 13.2.6, “LOAD DATA Statement”, for more information about these clauses.

`(field_name_or_user_var, ...)` is a list of one or more comma-separated XML fields or user variables. The name of a user variable used for this purpose must match the name of a field from the XML file, prefixed with @. You can use field names to select only desired fields. User variables can be employed to store the corresponding field values for subsequent re-use.

The `IGNORE number LINES` or `IGNORE number ROWS` clause causes the first `number` rows in the XML file to be skipped. It is analogous to the `LOAD DATA` statement's `IGNORE ... LINES` clause.

Suppose that we have a table named `person`, created as shown here:

```
USE test;
CREATE TABLE person (
person_id INT NOT NULL PRIMARY KEY,
fname VARCHAR(40) NULL,
lname VARCHAR(40) NULL,
created TIMESTAMP
);
```

Suppose further that this table is initially empty.

Now suppose that we have a simple XML file `person.xml`, whose contents are as shown here:

```
<list>
<person person_id="1" fname="Kapek" lname="Sainnouine"/>
<person person_id="2" fname="Sajon" lname="Rondela"/>
<person person_id="3"><fname>Likame</fname><lname>Örrtmons</lname></person>
<person person_id="4"><fname>Slar</fname><lname>Manlanth</lname></person>
<person><field name="person_id">5</field><field name="fname">Stoma</field>
<field name="lname">Milu</field></person>
<person><field name="person_id">6</field><field name="fname">Nirtam</field>
<field name="lname">Sklöd</field></person>
<person person_id="7"><fname>Sungam</fname><lname>Dulbåd</lname></person>
<person person_id="8" fname="Sraref" lname="Encmelt"/>
</list>
```

Each of the permissible XML formats discussed previously is represented in this example file.

To import the data in `person.xml` into the `person` table, you can use this statement:

```
mysql> LOAD XML LOCAL INFILE 'person.xml'
->   INTO TABLE person
->   ROWS IDENTIFIED BY '<person>';
Query OK, 8 rows affected (0.00 sec)
Records: 8  Deleted: 0  Skipped: 0  Warnings: 0
```

LOAD XML Statement Here, we assume that `person.xml` is located in the MySQL data directory. If the file cannot be found, the following error results:

```
ERROR 2 (HY000): File '/person.xml' not found (Errcode: 2)
```

The `ROWS IDENTIFIED BY '<person>'` clause means that each `<person>` element in the XML file is considered equivalent to a row in the table into which the data is to be imported. In this case, this is the`person` table in the `test` database.

As can be seen by the response from the server, 8 rows were imported into the `test.person` table. This can be verified by a simple `SELECT` statement:

```
mysql> SELECT * FROM person;
+-----------+--------+------------+---------------------+
| person_id | fname  | lname      | created             |
+-----------+--------+------------+---------------------+
|         1 | Kapek  | Sainnouine | 2007-07-13 16:18:47 |
|         2 | Sajon  | Rondela    | 2007-07-13 16:18:47 |
|         3 | Likame | Örrtmons   | 2007-07-13 16:18:47 |
|         4 | Slar   | Manlanth   | 2007-07-13 16:18:47 |
|         5 | Stoma  | Nilu       | 2007-07-13 16:18:47 |
|         6 | Nirtam | Sklöd      | 2007-07-13 16:18:47 |
|         7 | Sungam | Dulbåd     | 2007-07-13 16:18:47 |
|         8 | Sreraf | Encmelt    | 2007-07-13 16:18:47 |
+-----------+--------+------------+---------------------+
8 rows in set (0.00 sec)
```

This shows, as stated earlier in this section, that any or all of the 3 permitted XML formats may appear in a single file and be read using `LOAD XML`.

The inverse of the import operation just shown—that is, dumping MySQL table data into an XML file—can be accomplished using the `mysql` client from the system shell, as shown here:

```
$> mysql --xml -e "SELECT * FROM test.person" > person-dump.xml
$> cat person-dump.xml
<?xml version="1.0"?>
<resultset statement="SELECT * FROM test.person" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<row>
<field name="person_id">1</field>
<field name="fname">Kapek</field>
<field name="lname">Sainnouine</field>
</row>
<row>
<field name="person_id">2</field>
<field name="fname">Sajon</field>
<field name="lname">Rondela</field>
</row>
<row>
<field name="person_id">3</field>
<field name="fname">Likema</field>
<field name="lname">Örrtmons</field>
</row>
<row>
<field name="person_id">4</field>
<field name="fname">Slar</field>
<field name="lname">Manlanth</field>
</row>
<row>
<field name="person_id">5</field>
```

LOAD XML Statement

```
<field name="fname">Stoma</field>
<field name="lname">Nilu</field>
</row>
<row>
<field name="person_id">6</field>
<field name="fname">Nirtam</field>
<field name="lname">Sklöd</field>
</row>
<row>
<field name="person_id">7</field>
<field name="fname">Sungam</field>
<field name="lname">Dulbåd</field>
</row>
<row>
<field name="person_id">8</field>
<field name="fname">Sreraf</field>
<field name="lname">Encmelt</field>
</row>
</resultset>
```

Note The `--xml` option causes the `mysql` client to use XML formatting for its output; the`-e` option causes the client to execute the SQL statement immediately following the option. See Section 4.5.1, “mysql — The MySQL Command-Line Client”.

You can verify that the dump is valid by creating a copy of the `person` table and importing the dump file into the new table, like this:

```
mysql> USE test;
mysql> CREATE TABLE person2 LIKE person;
Query OK, 0 rows affected (0.00 sec)
mysql> LOAD XML LOCAL INFILE 'person-dump.xml'
->   INTO TABLE person2;
Query OK, 8 rows affected (0.01 sec)
Records: 8  Deleted: 0  Skipped: 0  Warnings: 0
mysql> SELECT * FROM person2;
+-----------+--------+------------+---------------------+
| person_id | fname  | lname      | created             |
+-----------+--------+------------+---------------------+
|         1 | Kapek  | Sainnouine | 2007-07-13 16:18:47 |
|         2 | Sajon  | Rondela    | 2007-07-13 16:18:47 |
|         3 | Likema | Örrtmons   | 2007-07-13 16:18:47 |
|         4 | Slar   | Manlanth   | 2007-07-13 16:18:47 |
|         5 | Stoma  | Nilu       | 2007-07-13 16:18:47 |
|         6 | Nirtam | Sklöd      | 2007-07-13 16:18:47 |
|         7 | Sungam | Dulbåd     | 2007-07-13 16:18:47 |
|         8 | Sreraf | Encmelt    | 2007-07-13 16:18:47 |
+-----------+--------+------------+---------------------+
8 rows in set (0.00 sec)
```

There is no requirement that every field in the XML file be matched with a column in the corresponding table. Fields which have no corresponding columns are skipped. You can see this by first emptying the`person2` table and dropping the `created` column, then using the same `LOAD XML` statement we just employed previously, like this:

```
mysql> TRUNCATE person2;
Query OK, 8 rows affected (0.26 sec)
mysql> ALTER TABLE person2 DROP COLUMN created;
```

LOAD XML Statement

```
Query OK, 0 rows affected (0.52 sec)
Records: 0  Duplicates: 0  Warnings: 0
mysql> SHOW CREATE TABLE person2\G
*************************** 1. row ***************************
Table: person2
Create Table: CREATE TABLE `person2` (
`person_id` int(11) NOT NULL,
`fname` varchar(40) DEFAULT NULL,
`lname` varchar(40) DEFAULT NULL,
PRIMARY KEY (`person_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.00 sec)
mysql> LOAD XML LOCAL INFILE 'person-dump.xml'
->   INTO TABLE person2;
Query OK, 8 rows affected (0.01 sec)
Records: 8  Deleted: 0  Skipped: 0  Warnings: 0
mysql> SELECT * FROM person2;
+-----------+--------+------------+
| person_id | fname  | lname      |
+-----------+--------+------------+
|         1 | Kapek  | Sainnouine |
|         2 | Sajon  | Rondela    |
|         3 | Likema | Örrtmons   |
|         4 | Slar   | Manlanth   |
|         5 | Stoma  | Nilu       |
|         6 | Nirtam | Sklöd      |
|         7 | Sungam | Dulbåd     |
|         8 | Sreraf | Encmelt    |
+-----------+--------+------------+
8 rows in set (0.00 sec)
```

The order in which the fields are given within each row of the XML file does not affect the operation of`LOAD XML`; the field order can vary from row to row, and is not required to be in the same order as the corresponding columns in the table.

As mentioned previously, you can use a `(field_name_or_user_var, ...)` list of one or more XML fields (to select desired fields only) or user variables (to store the corresponding field values for later use). User variables can be especially useful when you want to insert data from an XML file into table columns whose names do not match those of the XML fields. To see how this works, we first create a table named `individual` whose structure matches that of the `person` table, but whose columns are named differently:

```
mysql> CREATE TABLE individual (
->     individual_id INT NOT NULL PRIMARY KEY,
->     name1 VARCHAR(40) NULL,
->     name2 VARCHAR(40) NULL,
->     made TIMESTAMP
-> );
Query OK, 0 rows affected (0.42 sec)
```

In this case, you cannot simply load the XML file directly into the table, because the field and column names do not match:

```
mysql> LOAD XML INFILE '../bin/person-dump.xml' INTO TABLE test.individual;
ERROR 1263 (22004): Column set to default value; NULL supplied to NOT NULL column 'individual_id' at row 1
```

This happens because the MySQL server looks for field names matching the column names of the target table. You can work around this problem by selecting the field values into user variables, then setting the target table's columns equal to the values of those variables using `SET`. You can perform both of these operations in a single statement, as shown here:LOAD XML Statement

```
mysql> LOAD XML INFILE '../bin/person-dump.xml'
->     INTO TABLE test.individual (@person_id, @fname, @lname, @created)
->     SET individual_id=@person_id, name1=@fname, name2=@lname, made=@created;
Query OK, 8 rows affected (0.05 sec)
Records: 8  Deleted: 0  Skipped: 0  Warnings: 0
mysql> SELECT * FROM individual;
+---------------+--------+------------+---------------------+
| individual_id | name1  | name2      | made                |
+---------------+--------+------------+---------------------+
|             1 | Kapek  | Sainnouine | 2007-07-13 16:18:47 |
|             2 | Sajon  | Rondela    | 2007-07-13 16:18:47 |
|             3 | Likema | Örrtmons   | 2007-07-13 16:18:47 |
|             4 | Slar   | Manlanth   | 2007-07-13 16:18:47 |
|             5 | Stoma  | Nilu       | 2007-07-13 16:18:47 |
|             6 | Nirtam | Sklöd      | 2007-07-13 16:18:47 |
|             7 | Sungam | Dulbåd     | 2007-07-13 16:18:47 |
|             8 | Srraf  | Encmelt    | 2007-07-13 16:18:47 |
+---------------+--------+------------+---------------------+
8 rows in set (0.00 sec)
```

The names of the user variables must match those of the corresponding fields from the XML file, with the addition of the required @ prefix to indicate that they are variables. The user variables need not be listed or assigned in the same order as the corresponding fields.

Using a `ROWS IDENTIFIED BY '<tagname>'` clause, it is possible to import data from the same XML file into database tables with different definitions. For this example, suppose that you have a file named`address.xml` which contains the following XML:

```
<?xml version="1.0"?>
<list>
<person person_id="1">
<fname>Robert</fname>
<lname>Jones</lname>
<address address_id="1" street="Mill Creek Road" zip="45365" city="Sidney"/>
<address address_id="2" street="Main Street" zip="28681" city="Taylorsville"/>
</person>
<person person_id="2">
<fname>Mary</fname>
<lname>Smith</lname>
<address address_id="3" street="River Road" zip="80239" city="Denver"/>
<!-- <address address_id="4" street="North Street" zip="37920" city="Knoxville"/> -->
</person>
</list>
```

You can again use the `test.person` table as defined previously in this section, after clearing all the existing records from the table and then showing its structure as shown here:

```
mysql< TRUNCATE person;
Query OK, 0 rows affected (0.04 sec)
mysql< SHOW CREATE TABLE person\G
*************************** 1. row ***************************
Table: person
Create Table: CREATE TABLE `person` (
`person_id` int(11) NOT NULL,
`fname` varchar(40) DEFAULT NULL,
`lname` varchar(40) DEFAULT NULL,
`created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`person_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1
1 row in set (0.00 sec)
```

LOAD XML Statement Now create an `address` table in the `test` database using the following `CREATE TABLE` statement:

```
CREATE TABLE address (
address_id INT NOT NULL PRIMARY KEY,
person_id INT NULL,
street VARCHAR(40) NULL,
zip INT NULL,
city VARCHAR(40) NULL,
created TIMESTAMP
);
```

To import the data from the XML file into the `person` table, execute the following `LOAD XML` statement,which specifies that rows are to be specified by the `<person>` element, as shown here;

```
mysql> LOAD XML LOCAL INFILE 'address.xml'
->   INTO TABLE person
->   ROWS IDENTIFIED BY '<person>';
Query OK, 2 rows affected (0.00 sec)
Records: 2  Deleted: 0  Skipped: 0  Warnings: 0
```

You can verify that the records were imported using a `SELECT` statement:

```
mysql> SELECT * FROM person;
+-----------+--------+-------+---------------------+
| person_id | fname  | lname | created             |
+-----------+--------+-------+---------------------+
|         1 | Robert | Jones | 2007-07-24 17:37:06 |
|         2 | Mary   | Smith | 2007-07-24 17:37:06 |
+-----------+--------+-------+---------------------+
2 rows in set (0.00 sec)
```

Since the `<address>` elements in the XML file have no corresponding columns in the `person` table, they are skipped.

To import the data from the `<address>` elements into the `address` table, use the `LOAD XML` statement shown here:

```
mysql> LOAD XML LOCAL INFILE 'address.xml'
->   INTO TABLE address
->   ROWS IDENTIFIED BY '<address>';
Query OK, 3 rows affected (0.00 sec)
Records: 3  Deleted: 0  Skipped: 0  Warnings: 0
```

You can see that the data was imported using a `SELECT` statement such as this one:

```
mysql> SELECT * FROM address;
+------------+-----------+-----------------+-------+--------------+---------------------+
| address_id | person_id | street          | zip   | city         | created             |
+------------+-----------+-----------------+-------+--------------+---------------------+
|          1 |         1 | Mill Creek Road | 45365 | Sidney       | 2007-07-24 17:37:37 |
|          2 |         1 | Main Street     | 28681 | Taylorsville | 2007-07-24 17:37:37 |
|          3 |         2 | River Road      | 80239 | Denver       | 2007-07-24 17:37:37 |
+------------+-----------+-----------------+-------+--------------+---------------------+
3 rows in set (0.00 sec)
```

The data from the `<address>` element that is enclosed in XML comments is not imported. However, since there is a `person_id` column in the `address` table, the value of the `person_id` attribute from the parent`<person>` element for each `<address>` is imported into the `address` table.

Security Considerations. As with the `LOAD DATA` statement, the transfer of the XML file from the client host to the server host is initiated by the MySQL server. In theory, a patched server could be built that would tell the client program to transfer a file of the server's choosing rather than the file named by the REPLACE Statement client in the `LOAD XML` statement. Such a server could access any file on the client host to which the client user has read access.

In a Web environment, clients usually connect to MySQL from a Web server. A user that can run any command against the MySQL server can use `LOAD XML LOCAL` to read any files to which the Web server process has read access. In this environment, the client with respect to the MySQL server is actually the Web server, not the remote program being run by the user who connects to the Web server.

You can disable loading of XML files from clients by starting the server with `--local-infile=0` or `--``local-infile=OFF`. This option can also be used when starting the `mysql` client to disable `LOAD XML`for the duration of the client session.

To prevent a client from loading XML files from the server, do not grant the `FILE` privilege to the corresponding MySQL user account, or revoke this privilege if the client user account already has it.

Important Revoking the `FILE` privilege (or not granting it in the first place) keeps the user only from executing the `LOAD XML` statement (as well as the `LOAD_FILE()` function;

it does not prevent the user from executing `LOAD XML LOCAL`. To disallow this statement, you must start the server or the client with `--local-infile=OFF`.

In other words, the `FILE` privilege affects only whether the client can read files on the server; it has no bearing on whether the client can read files on the local file system.

For partitioned tables using storage engines that employ table locks, such as `MyISAM`, any locks caused by`LOAD XML` perform locks on all partitions of the table. This does not apply to tables using storage engines which employ row-level locking, such as `InnoDB`. For more information, see Section 19.6.4, “Partitioning and Locking”.

### 13.2.8 REPLACE Statement

```
REPLACE [LOW_PRIORITY | DELAYED]
[INTO] tbl_name
[PARTITION (partition_name [, partition_name] ...)]
[(col_name [, col_name] ...)]
{VALUES | VALUE} (value_list) [, (value_list)] ...
REPLACE [LOW_PRIORITY | DELAYED]
[INTO] tbl_name
[PARTITION (partition_name [, partition_name] ...)]
SET assignment_list
REPLACE [LOW_PRIORITY | DELAYED]
[INTO] tbl_name
[PARTITION (partition_name [, partition_name] ...)]
[(col_name [, col_name] ...)]
SELECT ...
value:
{expr | DEFAULT}
value_list:
value [, value] ...
assignment:
col_name = value
assignment_list:
```

REPLACE Statement

```
assignment [, assignment] ...
```

`REPLACE` works exactly like `INSERT`, except that if an old row in the table has the same value as a new row for a `PRIMARY KEY` or a `UNIQUE` index, the old row is deleted before the new row is inserted. See Section 13.2.5, “INSERT Statement”.

`REPLACE` is a MySQL extension to the SQL standard. It either inserts, or deletes and inserts. For another MySQL extension to standard SQL—that either inserts or updates—see Section 13.2.5.2, “INSERT ... ON DUPLICATE KEY UPDATE Statement”.

Note`REPLACE` makes sense only if a table has a `PRIMARY KEY` or `UNIQUE` index.

Otherwise, it becomes equivalent to `INSERT`, because there is no index to be used to determine whether a new row duplicates another.

Values for all columns are taken from the values specified in the `REPLACE` statement. Any missing columns are set to their default values, just as happens for `INSERT`. You cannot refer to values from the current row and use them in the new row. If you use an assignment such as `SET col_name = col_name +`1, the reference to the column name on the right hand side is treated as `DEFAULT(col_name)`, so the assignment is equivalent to `SET col_name = DEFAULT(col_name) + 1`.

To use `REPLACE`, you must have both the `INSERT` and `DELETE` privileges for the table.

`REPLACE` supports explicit partition selection using the `PARTITION` clause with a list of comma-separated names of partitions, subpartitions, or both. As with `INSERT`, if it is not possible to insert the new row into any of these partitions or subpartitions, the `REPLACE` statement fails with the error `Found a row``not matching the given partition set`. For more information and examples, see Section 19.5,“Partition Selection”.

The `REPLACE` statement returns a count to indicate the number of rows affected. This is the sum of the rows deleted and inserted. If the count is 1 for a single-row `REPLACE`, a row was inserted and no rows were deleted. If the count is greater than 1, one or more old rows were deleted before the new row was inserted. It is possible for a single row to replace more than one old row if the table contains multiple unique indexes and the new row duplicates values for different old rows in different unique indexes.

The affected-rows count makes it easy to determine whether `REPLACE` only added a row or whether it also replaced any rows: Check whether the count is 1 (added) or greater (replaced).

If you are using the C API, the affected-rows count can be obtained using the `mysql_affected_rows()`function.

You cannot replace into a table and select from the same table in a subquery.

MySQL uses the following algorithm for `REPLACE` (and `LOAD DATA ... REPLACE`):

1. Try to insert the new row into the table
2. While the insertion fails because a duplicate-key error occurs for a primary key or unique index:

a. Delete from the table the conflicting row that has the duplicate key value b. Try again to insert the new row into the table It is possible that in the case of a duplicate-key error, a storage engine may perform the `REPLACE` as an update rather than a delete plus insert, but the semantics are the same. There are no user-visible effects other than a possible difference in how the storage engine increments `Handler_xxx` status variables.

REPLACE Statement Because the results of `REPLACE ... SELECT` statements depend on the ordering of rows from the`SELECT` and this order cannot always be guaranteed, it is possible when logging these statements for the source and the slave to diverge. For this reason, `REPLACE ... SELECT` statements are flagged as unsafe for statement-based replication. such statements produce a warning in the error log when using statement-based mode and are written to the binary log using the row-based format when using `MIXED`mode. See also Section 17.1.2.1, “Advantages and Disadvantages of Statement-Based and Row-Based Replication”.

When modifying an existing table that is not partitioned to accommodate partitioning, or, when modifying the partitioning of an already partitioned table, you may consider altering the table's primary key (see Section 19.6.1, “Partitioning Keys, Primary Keys, and Unique Keys”). You should be aware that, if you do this, the results of `REPLACE` statements may be affected, just as they would be if you modified the primary key of a nonpartitioned table. Consider the table created by the following `CREATE TABLE` statement:

```
CREATE TABLE test (
id INT UNSIGNED NOT NULL AUTO_INCREMENT,
data VARCHAR(64) DEFAULT NULL,
ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id)
);
```

When we create this table and run the statements shown in the mysql client, the result is as follows:

```
mysql> REPLACE INTO test VALUES (1, 'Old', '2014-08-20 18:47:00');
Query OK, 1 row affected (0.04 sec)
mysql> REPLACE INTO test VALUES (1, 'New', '2014-08-20 18:47:42');
Query OK, 2 rows affected (0.04 sec)
mysql> SELECT * FROM test;
+----+------+---------------------+
| id | data | ts                  |
+----+------+---------------------+
|  1 | New  | 2014-08-20 18:47:42 |
+----+------+---------------------+
1 row in set (0.00 sec)
```

Now we create a second table almost identical to the first, except that the primary key now covers 2 columns, as shown here (emphasized text):

```
CREATE TABLE test2 (
id INT UNSIGNED NOT NULL AUTO_INCREMENT,
data VARCHAR(64) DEFAULT NULL,
ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id, ts)
);
```

When we run on `test2` the same two `REPLACE` statements as we did on the original `test` table, we obtain a different result:

```
mysql> REPLACE INTO test2 VALUES (1, 'Old', '2014-08-20 18:47:00');
Query OK, 1 row affected (0.05 sec)
mysql> REPLACE INTO test2 VALUES (1, 'New', '2014-08-20 18:47:42');
Query OK, 1 row affected (0.06 sec)
mysql> SELECT * FROM test2;
+----+------+---------------------+
| id | data | ts                  |
+----+------+---------------------+
|  1 | Old  | 2014-08-20 18:47:00 |
|  1 | New  | 2014-08-20 18:47:42 |
+----+------+---------------------+
```

SELECT Statement

```
2 rows in set (0.00 sec)
```

This is due to the fact that, when run on `test2`, both the `id` and `ts` column values must match those of an existing row for the row to be replaced; otherwise, a row is inserted.

A `REPLACE` statement affecting a partitioned table using a storage engine such as `MyISAM` that employs table-level locks locks only those partitions containing rows that match the `REPLACE` statement `WHERE`clause, as long as none of the table partitioning columns are updated; otherwise the entire table is locked.

(For storage engines such as `InnoDB` that employ row-level locking, no locking of partitions takes place.)For more information, see Section 19.6.4, “Partitioning and Locking”.

### 13.2.9 SELECT Statement

```
SELECT
[ALL | DISTINCT | DISTINCTROW ]
[HIGH_PRIORITY]
[STRAIGHT_JOIN]
[SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT]
[SQL_CACHE | SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]
select_expr [, select_expr] ...
[into_option]
[FROM table_references
[PARTITION partition_list]]
[WHERE where_condition]
[GROUP BY {col_name | expr | position}
[ASC | DESC], ... [WITH ROLLUP]]
[HAVING where_condition]
[ORDER BY {col_name | expr | position}
[ASC | DESC], ...]
[LIMIT {[offset,] row_count | row_count OFFSET offset}]
[PROCEDURE procedure_name(argument_list)]
[into_option]
[FOR UPDATE | LOCK IN SHARE MODE]
into_option: {
INTO OUTFILE 'file_name'
[CHARACTER SET charset_name]
export_options
| INTO DUMPFILE 'file_name'
| INTO var_name [, var_name] ...
}
```

`SELECT` is used to retrieve rows selected from one or more tables, and can include `UNION` statements and subqueries. See Section 13.2.9.3, “UNION Clause”, and Section 13.2.10, “Subqueries”.

The most commonly used clauses of `SELECT` statements are these:

- Each `select_expr` indicates a column that you want to retrieve. There must be at least one

```
select_expr.
```

- `table_references` indicates the table or tables from which to retrieve rows. Its syntax is described in

Section 13.2.9.2, “JOIN Clause”.

- `SELECT` supports explicit partition selection using the `PARTITION` clause with a list of partitions or

subpartitions (or both) following the name of the table in a `table_reference` (see Section 13.2.9.2,“JOIN Clause”). In this case, rows are selected only from the partitions listed, and any other partitions of the table are ignored. For more information and examples, see Section 19.5, “Partition Selection”.

`SELECT ... PARTITION` from tables using storage engines such as `MyISAM` that perform table-level locks (and thus partition locks) lock only the partitions or subpartitions named by the `PARTITION` option.

For more information, see Section 19.6.4, “Partitioning and Locking”.

SELECT Statement

- The `WHERE` clause, if given, indicates the condition or conditions that rows must satisfy to be selected.

`where_condition` is an expression that evaluates to true for each row to be selected. The statement selects all rows if there is no `WHERE` clause.

In the `WHERE` expression, you can use any of the functions and operators that MySQL supports, except for aggregate (group) functions. See Section 9.5, “Expressions”, and Chapter 12, Functions and Operators.

`SELECT` can also be used to retrieve rows computed without reference to any table.

For example:

```
mysql> SELECT 1 + 1;
-> 2
```

You are permitted to specify `DUAL` as a dummy table name in situations where no tables are referenced:

```
mysql> SELECT 1 + 1 FROM DUAL;
-> 2
```

`DUAL` is purely for the convenience of people who require that all `SELECT` statements should have `FROM`and possibly other clauses. MySQL may ignore the clauses. MySQL does not require `FROM DUAL` if no tables are referenced.

In general, clauses used must be given in exactly the order shown in the syntax description. For example,a `HAVING` clause must come after any `GROUP BY` clause and before any `ORDER BY` clause. The`INTO` clause, if present, can appear in any position indicated by the syntax description, but within a given statement can appear only once, not in multiple positions. For more information about `INTO`, see Section 13.2.9.1, “SELECT ... INTO Statement”.

The list of `select_expr` terms comprises the select list that indicates which columns to retrieve. Terms specify a column or expression or can use *-shorthand:

- A select list consisting only of a single unqualified * can be used as shorthand to select all columns from

all tables:

```
SELECT * FROM t1 INNER JOIN t2 ...
```

- `tbl_name.*` can be used as a qualified shorthand to select all columns from the named table:

```
SELECT t1.*, t2.* FROM t1 INNER JOIN t2 ...
```

- Use of an unqualified * with other items in the select list may produce a parse error. To avoid this

problem, use a qualified `tbl_name.*` reference:

```
SELECT AVG(score), t1.* FROM t1 ...
```

The following list provides additional information about other `SELECT` clauses:

- A `select_expr` can be given an alias using `AS alias_name`. The alias is used as the expression's

column name and can be used in `GROUP BY`, `ORDER BY`, or `HAVING` clauses. For example:

```
SELECT CONCAT(last_name,', ',first_name) AS full_name
FROM mytable ORDER BY full_name;
```

The `AS` keyword is optional when aliasing a `select_expr` with an identifier. The preceding example could have been written like this:

```
SELECT CONCAT(last_name,', ',first_name) full_name
FROM mytable ORDER BY full_name;
```

SELECT Statement However, because the `AS` is optional, a subtle problem can occur if you forget the comma between two `select_expr` expressions: MySQL interprets the second as an alias name. For example, in the following statement, `columnb` is treated as an alias name:

```
SELECT columna columnb FROM mytable;
```

For this reason, it is good practice to be in the habit of using `AS` explicitly when specifying column aliases.

It is not permissible to refer to a column alias in a `WHERE` clause, because the column value might not yet be determined when the `WHERE` clause is executed. See Section B.3.4.4, “Problems with Column Aliases”.

- The `FROM table_references` clause indicates the table or tables from which to retrieve rows.

If you name more than one table, you are performing a join. For information on join syntax, see Section 13.2.9.2, “JOIN Clause”. For each table specified, you can optionally specify an alias.

```
tbl_name [[AS] alias] [index_hint]
```

The use of index hints provides the optimizer with information about how to choose indexes during query processing. For a description of the syntax for specifying these hints, see Section 8.9.3, “Index Hints”.

You can use `SET max_seeks_for_key=value` as an alternative way to force MySQL to prefer key scans instead of table scans. See Section 5.1.7, “Server System Variables”.

- You can refer to a table within the default database as `tbl_name`, or as `db_name`.`tbl_name` to

specify a database explicitly. You can refer to a column as `col_name`, `tbl_name`.`col_name`, or`db_name`.`tbl_name`.`col_name`. You need not specify a `tbl_name` or `db_name`.`tbl_name` prefix for a column reference unless the reference would be ambiguous. See Section 9.2.2, “Identifier Qualifiers”, for examples of ambiguity that require the more explicit column reference forms.

- A table reference can be aliased using `tbl_name AS alias_name` or `tbl_name alias_name`.

These statements are equivalent:

```
SELECT t1.name, t2.salary FROM employee AS t1, info AS t2
WHERE t1.name = t2.name;
SELECT t1.name, t2.salary FROM employee t1, info t2
WHERE t1.name = t2.name;
```

- Columns selected for output can be referred to in `ORDER BY` and `GROUP BY` clauses using column

names, column aliases, or column positions. Column positions are integers and begin with 1:

```
SELECT college, region, seed FROM tournament
ORDER BY region, seed;
SELECT college, region AS r, seed AS s FROM tournament
ORDER BY r, s;
SELECT college, region, seed FROM tournament
ORDER BY 2, 3;
```

To sort in reverse order, add the `DESC` (descending) keyword to the name of the column in the `ORDER``BY` clause that you are sorting by. The default is ascending order; this can be specified explicitly using the `ASC` keyword.

If `ORDER BY` occurs within a parenthesized query expression and also is applied in the outer query, the results are undefined and may change in a future MySQL version.

SELECT Statement Use of column positions is deprecated because the syntax has been removed from the SQL standard.

- MySQL extends the `GROUP BY` clause so that you can also specify `ASC` and `DESC` after columns named

in the clause:

```
SELECT a, COUNT(b) FROM test_table GROUP BY a DESC;
```

- If you use `GROUP BY`, output rows are sorted according to the `GROUP BY` columns as if you had an

`ORDER BY` for the same columns. To avoid the overhead of sorting that `GROUP BY` produces, add

```
ORDER BY NULL:
SELECT a, COUNT(b) FROM test_table GROUP BY a ORDER BY NULL;
```

Relying on implicit `GROUP BY` sorting (that is, sorting in the absence of `ASC` or `DESC` designators) is deprecated. To produce a given sort order, use explicit `ASC` or `DESC` designators for `GROUP BY` columns or provide an `ORDER BY` clause.

- When you use `ORDER BY` or `GROUP BY` to sort a column in a `SELECT`, the server sorts values using

only the initial number of bytes indicated by the `max_sort_length` system variable.

- MySQL extends the use of `GROUP BY` to permit selecting fields that are not mentioned in the `GROUP BY`

clause. If you are not getting the results that you expect from your query, please read the description of`GROUP BY` found in Section 12.19, “Aggregate Functions”.

- `GROUP BY` permits a `WITH ROLLUP` modifier. See Section 12.19.2, “GROUP BY Modifiers”.
- The `HAVING` clause, like the `WHERE` clause, specifies selection conditions. The `WHERE` clause specifies

conditions on columns in the select list, but cannot refer to aggregate functions. The `HAVING` clause specifies conditions on groups, typically formed by the `GROUP BY` clause. The query result includes only groups satisfying the `HAVING` conditions. (If no `GROUP BY` is present, all rows implicitly form a single aggregate group.)The `HAVING` clause is applied nearly last, just before items are sent to the client, with no optimization.

(`LIMIT` is applied after `HAVING`.)The SQL standard requires that `HAVING` must reference only columns in the `GROUP BY` clause or columns used in aggregate functions. However, MySQL supports an extension to this behavior, and permits `HAVING` to refer to columns in the `SELECT` list and columns in outer subqueries as well.

If the `HAVING` clause refers to a column that is ambiguous, a warning occurs. In the following statement,`col2` is ambiguous because it is used as both an alias and a column name:

```
SELECT COUNT(col1) AS col2 FROM t GROUP BY col2 HAVING col2 = 2;
```

Preference is given to standard SQL behavior, so if a `HAVING` column name is used both in `GROUP BY`and as an aliased column in the select column list, preference is given to the column in the `GROUP BY`column.

- Do not use `HAVING` for items that should be in the `WHERE` clause. For example, do not write the

following:

```
SELECT col_name FROM tbl_name HAVING col_name > 0;
```

Write this instead:

```
SELECT col_name FROM tbl_name WHERE col_name > 0;
```

- The `HAVING` clause can refer to aggregate functions, which the `WHERE` clause cannot:

SELECT Statement

```
SELECT user, MAX(salary) FROM users
GROUP BY user HAVING MAX(salary) > 10;
```

(This did not work in some older versions of MySQL.)

- MySQL permits duplicate column names. That is, there can be more than one `select_expr` with

the same name. This is an extension to standard SQL. Because MySQL also permits `GROUP BY` and`HAVING` to refer to `select_expr` values, this can result in an ambiguity:

```
SELECT 12 AS a, a FROM t GROUP BY a;
```

In that statement, both columns have the name a. To ensure that the correct column is used for grouping, use different names for each `select_expr`.

- MySQL resolves unqualified column or alias references in `ORDER BY` clauses by searching in the

`select_expr` values, then in the columns of the tables in the `FROM` clause. For `GROUP BY` or `HAVING`clauses, it searches the `FROM` clause before searching in the `select_expr` values. (For `GROUP BY` and`HAVING`, this differs from the pre-MySQL 5.0 behavior that used the same rules as for `ORDER BY`.)

- The `LIMIT` clause can be used to constrain the number of rows returned by the `SELECT` statement.

`LIMIT` takes one or two numeric arguments, which must both be nonnegative integer constants, with these exceptions:

- Within prepared statements, `LIMIT` parameters can be specified using ? placeholder markers.
- Within stored programs, `LIMIT` parameters can be specified using integer-valued routine parameters

or local variables.

With two arguments, the first argument specifies the offset of the first row to return, and the second specifies the maximum number of rows to return. The offset of the initial row is 0 (not 1):

```
SELECT * FROM tbl LIMIT 5,10;  # Retrieve rows 6-15
```

To retrieve all rows from a certain offset up to the end of the result set, you can use some large number for the second parameter. This statement retrieves all rows from the 96th row to the last:

```
SELECT * FROM tbl LIMIT 95,18446744073709551615;
```

With one argument, the value specifies the number of rows to return from the beginning of the result set:

```
SELECT * FROM tbl LIMIT 5;     # Retrieve first 5 rows
```

In other words, `LIMIT row_count` is equivalent to `LIMIT 0, row_count`.

For prepared statements, you can use placeholders. The following statements return one row from the`tbl` table:

```
SET @a=1;
PREPARE STMT FROM 'SELECT * FROM tbl LIMIT ?';
EXECUTE STMT USING @a;
```

The following statements return the second to sixth row from the `tbl` table:

```
SET @skip=1; SET @numrows=5;
PREPARE STMT FROM 'SELECT * FROM tbl LIMIT ?, ?';
EXECUTE STMT USING @skip, @numrows;
```

For compatibility with PostgreSQL, MySQL also supports the `LIMIT row_count OFFSET offset`syntax.

SELECT Statement If `LIMIT` occurs within a parenthesized query expression and also is applied in the outer query, the results are undefined and may change in a future MySQL version.

- A `PROCEDURE` clause names a procedure that should process the data in the result set. For an example,

see Section 8.4.2.4, “Using PROCEDURE ANALYSE”, which describes `ANALYSE`, a procedure that can be used to obtain suggestions for optimal column data types that may help reduce table sizes.

A `PROCEDURE` clause is not permitted in a `UNION` statement.

- The `SELECT ... INTO` form of `SELECT` enables the query result to be written to a file or stored in

variables. For more information, see Section 13.2.9.1, “SELECT ... INTO Statement”.

- If you use `FOR UPDATE` with a storage engine that uses page or row locks, rows examined by the

query are write-locked until the end of the current transaction. Using `LOCK IN SHARE MODE` sets a shared lock that permits other transactions to read the examined rows but not to update or delete them.

See Section 14.7.2.4, “Locking Reads”.

In addition, you cannot use `FOR UPDATE` as part of the `SELECT` in a statement such as `CREATE TABLE``new_table SELECT ... FROM old_table ...`. (If you attempt to do so, the statement is rejected

```
with the error Can't update table 'old_table' while 'new_table' is being created.)
```

This is a change in behavior from MySQL 5.5 and earlier, which permitted `CREATE TABLE ...``SELECT` statements to make changes in tables other than the table being created.

Following the `SELECT` keyword, you can use a number of modifiers that affect the operation of the statement. `HIGH_PRIORITY`, `STRAIGHT_JOIN`, and modifiers beginning with `SQL_` are MySQL extensions to standard SQL.

- The `ALL` and `DISTINCT` modifiers specify whether duplicate rows should be returned. `ALL` (the default)

specifies that all matching rows should be returned, including duplicates. `DISTINCT` specifies removal of duplicate rows from the result set. It is an error to specify both modifiers. `DISTINCTROW` is a synonym for

```
DISTINCT.
```

- `HIGH_PRIORITY` gives the `SELECT` higher priority than a statement that updates a table. You should

use this only for queries that are very fast and must be done at once. A `SELECT HIGH_PRIORITY`query that is issued while the table is locked for reading runs even if there is an update statement waiting for the table to be free. This affects only storage engines that use only table-level locking (such as`MyISAM`, `MEMORY`, and `MERGE`).

`HIGH_PRIORITY` cannot be used with `SELECT` statements that are part of a `UNION`.

- `STRAIGHT_JOIN` forces the optimizer to join the tables in the order in which they are listed in the

`FROM` clause. You can use this to speed up a query if the optimizer joins the tables in nonoptimal order.

`STRAIGHT_JOIN` also can be used in the `table_references` list. See Section 13.2.9.2, “JOIN Clause”.

`STRAIGHT_JOIN` does not apply to any table that the optimizer treats as a `const` or `system` table.

Such a table produces a single row, is read during the optimization phase of query execution, and references to its columns are replaced with the appropriate column values before query execution proceeds. These tables appear first in the query plan displayed by `EXPLAIN`. See Section 8.8.1,“Optimizing Queries with EXPLAIN”. This exception may not apply to `const` or `system` tables that are used on the `NULL`-complemented side of an outer join (that is, the right-side table of a `LEFT JOIN` or the left-side table of a `RIGHT JOIN`.

- `SQL_BIG_RESULT` or `SQL_SMALL_RESULT` can be used with `GROUP BY` or `DISTINCT` to tell the

optimizer that the result set has many rows or is small, respectively. For `SQL_BIG_RESULT`, MySQL directly uses disk-based temporary tables if they are created, and prefers sorting to using a temporary SELECT Statement table with a key on the `GROUP BY` elements. For `SQL_SMALL_RESULT`, MySQL uses in-memory temporary tables to store the resulting table instead of using sorting. This should not normally be needed.

- `SQL_BUFFER_RESULT` forces the result to be put into a temporary table. This helps MySQL free the

table locks early and helps in cases where it takes a long time to send the result set to the client. This modifier can be used only for top-level `SELECT` statements, not for subqueries or following `UNION`.

- `SQL_CALC_FOUND_ROWS` tells MySQL to calculate how many rows there would be in the result

set, disregarding any `LIMIT` clause. The number of rows can then be retrieved with `SELECT``FOUND_ROWS()`. See Section 12.16, “Information Functions”.

- The `SQL_CACHE` and `SQL_NO_CACHE` modifiers affect caching of query results in the query cache (see

Section 8.10.3, “The MySQL Query Cache”). `SQL_CACHE` tells MySQL to store the result in the query cache if it is cacheable and the value of the `query_cache_type` system variable is 2 or `DEMAND`. With`SQL_NO_CACHE`, the server does not use the query cache. It neither checks the query cache to see whether the result is already cached, nor does it cache the query result. (Due to a limitation in the parser,a space character must precede and follow the `SQL_NO_CACHE` keyword; a nonspace such as a newline causes the server to check the query cache to see whether the result is already cached.)These two modifiers are mutually exclusive and an error occurs if they are both specified. Also, these modifiers are not permitted in subqueries (including subqueries in the `FROM` clause), and `SELECT`statements in unions other than the first `SELECT`.

For views, `SQL_NO_CACHE` applies if it appears in any `SELECT` in the query. For a cacheable query,`SQL_CACHE` applies if it appears in the first `SELECT` of a view referred to by the query.

A `SELECT` from a partitioned table using a storage engine such as `MyISAM` that employs table-level locks locks only those partitions containing rows that match the `SELECT` statement `WHERE` clause. (This does not occur with storage engines such as `InnoDB` that employ row-level locking.) For more information, see Section 19.6.4, “Partitioning and Locking”.

#### 13.2.9.1 SELECT ... INTO Statement

The `SELECT ... INTO` form of `SELECT` enables a query result to be stored in variables or written to a file:

- `SELECT ... INTO var_list` selects column values and stores them into variables.
- `SELECT ... INTO OUTFILE` writes the selected rows to a file. Column and line terminators can be

specified to produce a specific output format.

- `SELECT ... INTO DUMPFILE` writes a single row to a file without any formatting.

A given `SELECT` statement can contain at most one `INTO` clause, although as shown by the `SELECT`syntax description (see Section 13.2.9, “SELECT Statement”), the `INTO` can appear in different positions:

- Before `FROM`. Example:

```
SELECT * INTO @myvar FROM t1;
```

- Before a trailing locking clause. Example:

```
SELECT * FROM t1 INTO @myvar FOR UPDATE;
```

An `INTO` clause should not be used in a nested `SELECT` because such a `SELECT` must return its result to the outer context. There are also constraints on the use of `INTO` within `UNION` statements; see Section 13.2.9.3, “UNION Clause”.

SELECT Statement For the `INTO var_list` variant:

- `var_list` names a list of one or more variables, each of which can be a user-defined variable, stored

procedure or function parameter, or stored program local variable. (Within a prepared `SELECT ...``INTO var_list` statement, only user-defined variables are permitted; see Section 13.6.4.2, “Local Variable Scope and Resolution”.)

- The selected values are assigned to the variables. The number of variables must match the number of

columns. The query should return a single row. If the query returns no rows, a warning with error code 1329 occurs (`No data`), and the variable values remain unchanged. If the query returns multiple rows,error 1172 occurs (`Result consisted of more than one row`). If it is possible that the statement may retrieve multiple rows, you can use `LIMIT 1` to limit the result set to a single row.

```
SELECT id, data INTO @x, @y FROM test.t1 LIMIT 1;
```

User variable names are not case-sensitive. See Section 9.4, “User-Defined Variables”.

The `SELECT ... INTO OUTFILE 'file_name'` form of `SELECT` writes the selected rows to a file. The file is created on the server host, so you must have the `FILE` privilege to use this syntax.

`file_name` cannot be an existing file, which among other things prevents files such as `/etc/passwd` and database tables from being modified. The `character_set_filesystem` system variable controls the interpretation of the file name.

The `SELECT ... INTO OUTFILE` statement is intended to enable dumping a table to a text file on the server host. To create the resulting file on some other host, `SELECT ... INTO OUTFILE` normally is unsuitable because there is no way to write a path to the file relative to the server host file system, unless the location of the file on the remote host can be accessed using a network-mapped path on the server host file system.

Alternatively, if the MySQL client software is installed on the remote host, you can use a client command such as `mysql -e "SELECT ..." > file_name` to generate the file on that host.

`SELECT ... INTO OUTFILE` is the complement of `LOAD DATA`. Column values are written converted to the character set specified in the `CHARACTER SET` clause. If no such clause is present, values are dumped using the `binary` character set. In effect, there is no character set conversion. If a result set contains columns in several character sets, so does the output data file, and it may not be possible to reload the file correctly.

The syntax for the `export_options` part of the statement consists of the same `FIELDS` and `LINES`clauses that are used with the `LOAD DATA` statement. For information about the `FIELDS` and `LINES`clauses, including their default values and permissible values, see Section 13.2.6, “LOAD DATA Statement”.

`FIELDS ESCAPED BY` controls how to write special characters. If the `FIELDS ESCAPED BY` character is not empty, it is used when necessary to avoid ambiguity as a prefix that precedes following characters on output:

- The `FIELDS ESCAPED BY` character
- The `FIELDS [OPTIONALLY] ENCLOSED BY` character
- The first character of the `FIELDS TERMINATED BY` and `LINES TERMINATED BY` values
- ASCII `NUL` (the zero-valued byte; what is actually written following the escape character is ASCII 0, not a

zero-valued byte)

```
The FIELDS TERMINATED BY, ENCLOSED BY, ESCAPED BY, or LINES TERMINATED BY characters
```

must be escaped so that you can read the file back in reliably. ASCII `NUL` is escaped to make it easier to view with some pagers.

SELECT Statement The resulting file need not conform to SQL syntax, so nothing else need be escaped.

If the `FIELDS ESCAPED BY` character is empty, no characters are escaped and `NULL` is output as `NULL`,not `\N`. It is probably not a good idea to specify an empty escape character, particularly if field values in your data contain any of the characters in the list just given.

Here is an example that produces a file in the comma-separated values (CSV) format used by many programs:

```
SELECT a,b,a+b INTO OUTFILE '/tmp/result.txt'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM test_table;
```

If you use `INTO DUMPFILE` instead of `INTO OUTFILE`, MySQL writes only one row into the file, without any column or line termination and without performing any escape processing. This is useful for selecting a`BLOB` value and storing it in a file.

Note Any file created by `INTO OUTFILE` or `INTO DUMPFILE` is writable by all users on the server host. The reason for this is that the MySQL server cannot create a file that is owned by anyone other than the user under whose account it is running.

(You should never run `mysqld` as `root` for this and other reasons.) The file thus must be world-writable so that you can manipulate its contents.

If the `secure_file_priv` system variable is set to a nonempty directory name,the file to be written must be located in that directory.

In the context of `SELECT ... INTO` statements that occur as part of events executed by the Event Scheduler, diagnostics messages (not only errors, but also warnings) are written to the error log, and, on Windows, to the application event log. For additional information, see Section 20.4.5, “Event Scheduler Status”.

#### 13.2.9.2 JOIN Clause

MySQL supports the following `JOIN` syntax for the `table_references` part of `SELECT` statements and multiple-table `DELETE` and `UPDATE` statements:

```
table_references:
escaped_table_reference [, escaped_table_reference] ...
escaped_table_reference: {
table_reference
| { OJ table_reference }
}
table_reference: {
table_factor
| joined_table
}
table_factor: {
tbl_name [PARTITION (partition_names)]
[[AS] alias] [index_hint_list]
| table_subquery [AS] alias
| ( table_references )
}
joined_table: {
```

SELECT Statement

```
table_reference [INNER | CROSS] JOIN table_factor [join_specification]
| table_reference STRAIGHT_JOIN table_factor
| table_reference STRAIGHT_JOIN table_factor ON search_condition
| table_reference {LEFT|RIGHT} [OUTER] JOIN table_reference join_specification
| table_reference NATURAL [{LEFT|RIGHT} [OUTER]] JOIN table_factor
}
join_specification: {
ON search_condition
| USING (join_column_list)
}
join_column_list:
column_name [, column_name] ...
index_hint_list:
index_hint [, index_hint] ...
index_hint: {
USE {INDEX|KEY}
[FOR {JOIN|ORDER BY|GROUP BY}] ([index_list])
| {IGNORE|FORCE} {INDEX|KEY}
[FOR {JOIN|ORDER BY|GROUP BY}] (index_list)
}
index_list:
index_name [, index_name] ...
```

A table reference is also known as a join expression.

A table reference (when it refers to a partitioned table) may contain a `PARTITION` clause, including a list of comma-separated partitions, subpartitions, or both. This option follows the name of the table and precedes any alias declaration. The effect of this option is that rows are selected only from the listed partitions or subpartitions. Any partitions or subpartitions not named in the list are ignored. For more information and examples, see Section 19.5, “Partition Selection”.

The syntax of `table_factor` is extended in MySQL in comparison with standard SQL. The standard accepts only `table_reference`, not a list of them inside a pair of parentheses.

This is a conservative extension if each comma in a list of `table_reference` items is considered as equivalent to an inner join. For example:

```
SELECT * FROM t1 LEFT JOIN (t2, t3, t4)
ON (t2.a = t1.a AND t3.b = t1.b AND t4.c = t1.c)
```

is equivalent to:

```
SELECT * FROM t1 LEFT JOIN (t2 CROSS JOIN t3 CROSS JOIN t4)
ON (t2.a = t1.a AND t3.b = t1.b AND t4.c = t1.c)
```

In MySQL, `JOIN`, `CROSS JOIN`, and `INNER JOIN` are syntactic equivalents (they can replace each other).

In standard SQL, they are not equivalent. `INNER JOIN` is used with an `ON` clause, `CROSS JOIN` is used otherwise.

In general, parentheses can be ignored in join expressions containing only inner join operations. MySQL also supports nested joins. See Section 8.2.1.7, “Nested Join Optimization”.

Index hints can be specified to affect how the MySQL optimizer makes use of indexes. For more information, see Section 8.9.3, “Index Hints”. The `optimizer_switch` system variable is another way to influence optimizer use of indexes. See Section 8.9.2, “Switchable Optimizations”.

The following list describes general factors to take into account when writing joins:SELECT Statement

- A table reference can be aliased using `tbl_name AS alias_name` or `tbl_name alias_name`:

```
SELECT t1.name, t2.salary
FROM employee AS t1 INNER JOIN info AS t2 ON t1.name = t2.name;
SELECT t1.name, t2.salary
FROM employee t1 INNER JOIN info t2 ON t1.name = t2.name;
```

- A `table_subquery` is also known as a derived table or subquery in the `FROM` clause. See

Section 13.2.10.8, “Derived Tables”. Such subqueries must include an alias to give the subquery result a table name. A trivial example follows:

```
SELECT * FROM (SELECT 1, 2, 3) AS t1;
```

- The maximum number of tables that can be referenced in a single join is 61.
- `INNER JOIN` and , (comma) are semantically equivalent in the absence of a join condition: both

produce a Cartesian product between the specified tables (that is, each and every row in the first table is joined to each and every row in the second table).

However, the precedence of the comma operator is less than that of `INNER JOIN`, `CROSS JOIN`, `LEFT``JOIN`, and so on. If you mix comma joins with the other join types when there is a join condition, an error of the form `Unknown column 'col_name' in 'on clause'` may occur. Information about dealing with this problem is given later in this section.

- The `search_condition` used with `ON` is any conditional expression of the form that can be used in

a `WHERE` clause. Generally, the `ON` clause serves for conditions that specify how to join tables, and the`WHERE` clause restricts which rows to include in the result set.

- If there is no matching row for the right table in the `ON` or `USING` part in a `LEFT JOIN`, a row with all

columns set to `NULL` is used for the right table. You can use this fact to find rows in a table that have no counterpart in another table:

```
SELECT left_tbl.*
FROM left_tbl LEFT JOIN right_tbl ON left_tbl.id = right_tbl.id
WHERE right_tbl.id IS NULL;
```

This example finds all rows in `left_tbl` with an `id` value that is not present in `right_tbl` (that is,all rows in `left_tbl` with no corresponding row in `right_tbl`). See Section 8.2.1.8, “Outer Join Optimization”.

- The `USING(join_column_list)` clause names a list of columns that must exist in both tables. If

tables a and b both contain columns `c1`, `c2`, and `c3`, the following join compares corresponding columns from the two tables:

```
a LEFT JOIN b USING (c1, c2, c3)
```

- The `NATURAL [LEFT] JOIN` of two tables is defined to be semantically equivalent to an `INNER JOIN`

or a `LEFT JOIN` with a `USING` clause that names all columns that exist in both tables.

- `RIGHT JOIN` works analogously to `LEFT JOIN`. To keep code portable across databases, it is

recommended that you use `LEFT JOIN` instead of `RIGHT JOIN`.

- The `{ OJ ... }` syntax shown in the join syntax description exists only for compatibility with ODBC.

The curly braces in the syntax should be written literally; they are not metasyntax as used elsewhere in syntax descriptions.

```
SELECT left_tbl.*
FROM { OJ left_tbl LEFT OUTER JOIN right_tbl
ON left_tbl.id = right_tbl.id }
```

SELECT Statement

```
WHERE right_tbl.id IS NULL;
```

You can use other types of joins within `{ OJ ... }`, such as `INNER JOIN` or `RIGHT OUTER JOIN`.

This helps with compatibility with some third-party applications, but is not official ODBC syntax.

- `STRAIGHT_JOIN` is similar to `JOIN`, except that the left table is always read before the right table. This

can be used for those (few) cases for which the join optimizer processes the tables in a suboptimal order.

Some join examples:

```
SELECT * FROM table1, table2;
SELECT * FROM table1 INNER JOIN table2 ON table1.id = table2.id;
SELECT * FROM table1 LEFT JOIN table2 ON table1.id = table2.id;
SELECT * FROM table1 LEFT JOIN table2 USING (id);
SELECT * FROM table1 LEFT JOIN table2 ON table1.id = table2.id
LEFT JOIN table3 ON table2.id = table3.id;
```

Natural joins and joins with `USING`, including outer join variants, are processed according to the SQL:2003 standard:

- Redundant columns of a `NATURAL` join do not appear. Consider this set of statements:

```
CREATE TABLE t1 (i INT, j INT);
CREATE TABLE t2 (k INT, j INT);
INSERT INTO t1 VALUES(1, 1);
INSERT INTO t2 VALUES(1, 1);
SELECT * FROM t1 NATURAL JOIN t2;
SELECT * FROM t1 JOIN t2 USING (j);
```

In the first `SELECT` statement, column j appears in both tables and thus becomes a join column, so,according to standard SQL, it should appear only once in the output, not twice. Similarly, in the second SELECT statement, column j is named in the `USING` clause and should appear only once in the output,not twice.

Thus, the statements produce this output:

```
+------+------+------+
| j    | i    | k    |
+------+------+------+
|    1 |    1 |    1 |
+------+------+------+
+------+------+------+
| j    | i    | k    |
+------+------+------+
|    1 |    1 |    1 |
+------+------+------+
```

Redundant column elimination and column ordering occurs according to standard SQL, producing this display order:

- First, coalesced common columns of the two joined tables, in the order in which they occur in the first

table

- Second, columns unique to the first table, in order in which they occur in that table
- Third, columns unique to the second table, in order in which they occur in that table

SELECT Statement The single result column that replaces two common columns is defined using the coalesce operation.

That is, for two `t1.a` and `t2.a` the resulting single join column a is defined as `a = COALESCE(t1.a,``t2.a)`, where:

```
COALESCE(x, y) = (CASE WHEN x IS NOT NULL THEN x ELSE y END)
```

If the join operation is any other join, the result columns of the join consist of the concatenation of all columns of the joined tables.

A consequence of the definition of coalesced columns is that, for outer joins, the coalesced column contains the value of the non-`NULL` column if one of the two columns is always `NULL`. If neither or both columns are `NULL`, both common columns have the same value, so it doesn't matter which one is chosen as the value of the coalesced column. A simple way to interpret this is to consider that a coalesced column of an outer join is represented by the common column of the inner table of a `JOIN`.

Suppose that the tables `t1(a, b)` and `t2(a, c)` have the following contents:

```
t1    t2
----  ----
1 x   2 z
2 y   3 w
```

Then, for this join, column a contains the values of `t1.a`:

```
mysql> SELECT * FROM t1 NATURAL LEFT JOIN t2;
+------+------+------+
| a    | b    | c    |
+------+------+------+
|    1 | x    | NULL |
|    2 | y    | z    |
+------+------+------+
```

By contrast, for this join, column a contains the values of `t2.a`.

```
mysql> SELECT * FROM t1 NATURAL RIGHT JOIN t2;
+------+------+------+
| a    | c    | b    |
+------+------+------+
|    2 | z    | y    |
|    3 | w    | NULL |
+------+------+------+
```

Compare those results to the otherwise equivalent queries with `JOIN ... ON`:

```
mysql> SELECT * FROM t1 LEFT JOIN t2 ON (t1.a = t2.a);
+------+------+------+------+
| a    | b    | a    | c    |
+------+------+------+------+
|    1 | x    | NULL | NULL |
|    2 | y    |    2 | z    |
+------+------+------+------+
mysql> SELECT * FROM t1 RIGHT JOIN t2 ON (t1.a = t2.a);
+------+------+------+------+
| a    | b    | a    | c    |
+------+------+------+------+
|    2 | y    |    2 | z    |
| NULL | NULL |    3 | w    |
+------+------+------+------+
```

SELECT Statement

- A `USING` clause can be rewritten as an `ON` clause that compares corresponding columns. However,

although `USING` and `ON` are similar, they are not quite the same. Consider the following two queries:

```
a LEFT JOIN b USING (c1, c2, c3)
a LEFT JOIN b ON a.c1 = b.c1 AND a.c2 = b.c2 AND a.c3 = b.c3
```

With respect to determining which rows satisfy the join condition, both joins are semantically identical.

With respect to determining which columns to display for `SELECT *` expansion, the two joins are not semantically identical. The `USING` join selects the coalesced value of corresponding columns, whereas the `ON` join selects all columns from all tables. For the `USING` join, `SELECT *` selects these values:

```
COALESCE(a.c1, b.c1), COALESCE(a.c2, b.c2), COALESCE(a.c3, b.c3)
```

For the `ON` join, `SELECT *` selects these values:

```
a.c1, a.c2, a.c3, b.c1, b.c2, b.c3
```

With an inner join, `COALESCE(a.c1, b.c1)` is the same as either `a.c1` or `b.c1` because both columns have the same value. With an outer join (such as `LEFT JOIN`), one of the two columns can be`NULL`. That column is omitted from the result.

- An `ON` clause can refer only to its operands.

Example:

```
CREATE TABLE t1 (i1 INT);
CREATE TABLE t2 (i2 INT);
CREATE TABLE t3 (i3 INT);
SELECT * FROM t1 JOIN t2 ON (i1 = i3) JOIN t3;
```

The statement fails with an `Unknown column 'i3' in 'on clause'` error because `i3` is a column in `t3`, which is not an operand of the `ON` clause. To enable the join to be processed, rewrite the statement as follows:

```
SELECT * FROM t1 JOIN t2 JOIN t3 ON (i1 = i3);
```

- `JOIN` has higher precedence than the comma operator (,), so the join expression `t1, t2 JOIN t3`

is interpreted as `(t1, (t2 JOIN t3))`, not as `((t1, t2) JOIN t3)`. This affects statements that use an `ON` clause because that clause can refer only to columns in the operands of the join, and the precedence affects interpretation of what those operands are.

Example:

```
CREATE TABLE t1 (i1 INT, j1 INT);
CREATE TABLE t2 (i2 INT, j2 INT);
CREATE TABLE t3 (i3 INT, j3 INT);
INSERT INTO t1 VALUES(1, 1);
INSERT INTO t2 VALUES(1, 1);
INSERT INTO t3 VALUES(1, 1);
```

SELECT Statement

```
SELECT * FROM t1, t2 JOIN t3 ON (t1.i1 = t3.i3);
```

The `JOIN` takes precedence over the comma operator, so the operands for the `ON` clause are `t2` and`t3`. Because `t1.i1` is not a column in either of the operands, the result is an `Unknown column`

```
't1.i1' in 'on clause' error.
```

To enable the join to be processed, use either of these strategies:

- Group the first two tables explicitly with parentheses so that the operands for the `ON` clause are `(t1,`

`t2)` and `t3`:

```
SELECT * FROM (t1, t2) JOIN t3 ON (t1.i1 = t3.i3);
```

- Avoid the use of the comma operator and use `JOIN` instead:

```
SELECT * FROM t1 JOIN t2 JOIN t3 ON (t1.i1 = t3.i3);
```

The same precedence interpretation also applies to statements that mix the comma operator with `INNER``JOIN`, `CROSS JOIN`, `LEFT JOIN`, and `RIGHT JOIN`, all of which have higher precedence than the comma operator.

- A MySQL extension compared to the SQL:2003 standard is that MySQL permits you to qualify the

common (coalesced) columns of `NATURAL` or `USING` joins, whereas the standard disallows that.

#### 13.2.9.3 UNION Clause

```
SELECT ...
UNION [ALL | DISTINCT] SELECT ...
[UNION [ALL | DISTINCT] SELECT ...]
```

`UNION` combines the result from multiple `SELECT` statements into a single result set.

- Result Set Column Names and Data Types
- UNION DISTINCT and UNION ALL
- ORDER BY and LIMIT in Unions
- UNION Restrictions

Result Set Column Names and Data Types The result set column names are taken from the column names of the first `SELECT` statement.

Selected columns listed in corresponding positions of each `SELECT` statement should have the same data type. For example, the first column selected by the first statement should have the same type as the first column selected by the other statements. If the data types of corresponding `SELECT` columns do not match, the types and lengths of the columns in the `UNION` result take into account the values retrieved by all the `SELECT` statements. For example, consider the following, where the column length is not constrained to the length of the value from the first `SELECT`:

```
mysql> SELECT REPEAT('a',1) UNION SELECT REPEAT('b',20);
+----------------------+
| REPEAT('a',1)        |
+----------------------+
| a                    |
| bbbbbbbbbbbbbbbbbbbb |
+----------------------+
```

SELECT Statement UNION DISTINCT and UNION ALL By default, duplicate rows are removed from `UNION` results. The optional `DISTINCT` keyword has the same effect but makes it explicit. With the optional `ALL` keyword, duplicate-row removal does not occur and the result includes all matching rows from all the `SELECT` statements.

You can mix `UNION ALL` and `UNION DISTINCT` in the same query. Mixed `UNION` types are treated such that a `DISTINCT` union overrides any `ALL` union to its left. A `DISTINCT` union can be produced explicitly by using `UNION DISTINCT` or implicitly by using `UNION` with no following `DISTINCT` or `ALL` keyword.

ORDER BY and LIMIT in Unions To apply an `ORDER BY` or `LIMIT` clause to an individual `SELECT`, parenthesize the `SELECT` and place the clause inside the parentheses:

```
(SELECT a FROM t1 WHERE a=10 AND B=1 ORDER BY a LIMIT 10)
UNION
(SELECT a FROM t2 WHERE a=11 AND B=2 ORDER BY a LIMIT 10);
```

Use of `ORDER BY` for individual `SELECT` statements implies nothing about the order in which the rows appear in the final result because `UNION` by default produces an unordered set of rows. Therefore, `ORDER``BY` in this context typically is used in conjunction with `LIMIT`, to determine the subset of the selected rows to retrieve for the `SELECT`, even though it does not necessarily affect the order of those rows in the final`UNION` result. If `ORDER BY` appears without `LIMIT` in a `SELECT`, it is optimized away because it has no effect.

To use an `ORDER BY` or `LIMIT` clause to sort or limit the entire `UNION` result, parenthesize the individual`SELECT` statements and place the `ORDER BY` or `LIMIT` after the last one:

```
(SELECT a FROM t1 WHERE a=10 AND B=1)
UNION
(SELECT a FROM t2 WHERE a=11 AND B=2)
ORDER BY a LIMIT 10;
```

A statement without parentheses is equivalent to one parenthesized as just shown.

This kind of `ORDER BY` cannot use column references that include a table name (that is, names in`tbl_name`.`col_name` format). Instead, provide a column alias in the first `SELECT` statement and refer to the alias in the `ORDER BY`. (Alternatively, refer to the column in the `ORDER BY` using its column position.

However, use of column positions is deprecated.)Also, if a column to be sorted is aliased, the `ORDER BY` clause must refer to the alias, not the column name. The first of the following statements is permitted, but the second fails with an `Unknown column`

```
'a' in 'order clause' error:
(SELECT a AS b FROM t) UNION (SELECT ...) ORDER BY b;
(SELECT a AS b FROM t) UNION (SELECT ...) ORDER BY a;
```

To cause rows in a `UNION` result to consist of the sets of rows retrieved by each `SELECT` one after the other, select an additional column in each `SELECT` to use as a sort column and add an `ORDER BY` that sorts on that column following the last `SELECT`:

```
(SELECT 1 AS sort_col, col1a, col1b, ... FROM t1)
UNION
(SELECT 2, col2a, col2b, ... FROM t2) ORDER BY sort_col;
```

To additionally maintain sort order within individual `SELECT` results, add a secondary column to the `ORDER``BY` clause:Subqueries

```
(SELECT 1 AS sort_col, col1a, col1b, ... FROM t1)
UNION
(SELECT 2, col2a, col2b, ... FROM t2) ORDER BY sort_col, col1a;
```

Use of an additional column also enables you to determine which `SELECT` each row comes from. Extra columns can provide other identifying information as well, such as a string that indicates a table name.

UNION Restrictions In a `UNION`, the `SELECT` statements are normal select statements, but with the following restrictions:

- `HIGH_PRIORITY` in the first `SELECT` has no effect. `HIGH_PRIORITY` in any subsequent `SELECT`

produces a syntax error.

- Only the last `SELECT` statement can use an `INTO` clause. However, the entire `UNION` result is written to

the `INTO` output destination.

### 13.2.10 Subqueries

A subquery is a `SELECT` statement within another statement.

All subquery forms and operations that the SQL standard requires are supported, as well as a few features that are MySQL-specific.

Here is an example of a subquery:

```
SELECT * FROM t1 WHERE column1 = (SELECT column1 FROM t2);
```

In this example, `SELECT * FROM t1 ...` is the outer query (or outer statement), and `(SELECT``column1 FROM t2)` is the subquery. We say that the subquery is nested within the outer query, and in fact it is possible to nest subqueries within other subqueries, to a considerable depth. A subquery must always appear within parentheses.

The main advantages of subqueries are:

- They allow queries that are structured so that it is possible to isolate each part of a statement.
- They provide alternative ways to perform operations that would otherwise require complex joins and

unions.

- Many people find subqueries more readable than complex joins or unions. Indeed, it was the innovation

of subqueries that gave people the original idea of calling the early SQL “Structured Query Language.”Here is an example statement that shows the major points about subquery syntax as specified by the SQL standard and supported in MySQL:

```
DELETE FROM t1
WHERE s11 > ANY
(SELECT COUNT(*) /* no hint */ FROM t2
WHERE NOT EXISTS
(SELECT * FROM t3
WHERE ROW(5*t2.s1,77)=
(SELECT 50,11*s1 FROM t4 UNION SELECT 50,77 FROM
(SELECT * FROM t5) AS t5)));
```

A subquery can return a scalar (a single value), a single row, a single column, or a table (one or more rows of one or more columns). These are called scalar, column, row, and table subqueries. Subqueries that Subqueries return a particular kind of result often can be used only in certain contexts, as described in the following sections.

There are few restrictions on the type of statements in which subqueries can be used. A subquery can contain many of the keywords or clauses that an ordinary `SELECT` can contain: `DISTINCT`, `GROUP BY`,`ORDER BY`, `LIMIT`, joins, index hints, `UNION` constructs, comments, functions, and so on.

A subquery's outer statement can be any one of: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `SET`, or `DO`.

In MySQL, you cannot modify a table and select from the same table in a subquery. This applies to statements such as `DELETE`, `INSERT`, `REPLACE`, `UPDATE`, and (because subqueries can be used in the`SET` clause) `LOAD DATA`.

For information about how the optimizer handles subqueries, see Section 8.2.2, “Optimizing Subqueries and Derived Tables”. For a discussion of restrictions on subquery use, including performance issues for certain forms of subquery syntax, see Section 13.2.10.12, “Restrictions on Subqueries”.

#### 13.2.10.1 The Subquery as Scalar Operand

In its simplest form, a subquery is a scalar subquery that returns a single value. A scalar subquery is a simple operand, and you can use it almost anywhere a single column value or literal is legal, and you can expect it to have those characteristics that all operands have: a data type, a length, an indication that it can be `NULL`, and so on. For example:

```
CREATE TABLE t1 (s1 INT, s2 CHAR(5) NOT NULL);
INSERT INTO t1 VALUES(100, 'abcde');
SELECT (SELECT s2 FROM t1);
```

The subquery in this `SELECT` returns a single value (`'abcde'`) that has a data type of `CHAR`, a length of 5,a character set and collation equal to the defaults in effect at `CREATE TABLE` time, and an indication that the value in the column can be `NULL`. Nullability of the value selected by a scalar subquery is not copied because if the subquery result is empty, the result is `NULL`. For the subquery just shown, if `t1` were empty,the result would be `NULL` even though `s2` is `NOT NULL`.

There are a few contexts in which a scalar subquery cannot be used. If a statement permits only a literal value, you cannot use a subquery. For example, `LIMIT` requires literal integer arguments, and `LOAD``DATA` requires a literal string file name. You cannot use subqueries to supply these values.

When you see examples in the following sections that contain the rather spartan construct `(SELECT``column1 FROM t1)`, imagine that your own code contains much more diverse and complex constructions.

Suppose that we make two tables:

```
CREATE TABLE t1 (s1 INT);
INSERT INTO t1 VALUES (1);
CREATE TABLE t2 (s1 INT);
INSERT INTO t2 VALUES (2);
```

Then perform a `SELECT`:

```
SELECT (SELECT s1 FROM t2) FROM t1;
```

The result is 2 because there is a row in `t2` containing a column `s1` that has a value of 2.

A scalar subquery can be part of an expression, but remember the parentheses, even if the subquery is an operand that provides an argument for a function. For example:Subqueries

```
SELECT UPPER((SELECT s1 FROM t1)) FROM t2;
```

#### 13.2.10.2 Comparisons Using Subqueries

The most common use of a subquery is in the form:

```
non_subquery_operand comparison_operator (subquery)
```

Where `comparison_operator` is one of these operators:

```
=  >  <  >=  <=  <>  !=  <=>
```

For example:

```
... WHERE 'a' = (SELECT column1 FROM t1)
```

MySQL also permits this construct:

```
non_subquery_operand LIKE (subquery)
```

At one time the only legal place for a subquery was on the right side of a comparison, and you might still find some old DBMSs that insist on this.

Here is an example of a common-form subquery comparison that you cannot do with a join. It finds all the rows in table `t1` for which the `column1` value is equal to a maximum value in table `t2`:

```
SELECT * FROM t1
WHERE column1 = (SELECT MAX(column2) FROM t2);
```

Here is another example, which again is impossible with a join because it involves aggregating for one of the tables. It finds all rows in table `t1` containing a value that occurs twice in a given column:

```
SELECT * FROM t1 AS t
WHERE 2 = (SELECT COUNT(*) FROM t1 WHERE t1.id = t.id);
```

For a comparison of the subquery to a scalar, the subquery must return a scalar. For a comparison of the subquery to a row constructor, the subquery must be a row subquery that returns a row with the same number of values as the row constructor. See Section 13.2.10.5, “Row Subqueries”.

#### 13.2.10.3 Subqueries with ANY, IN, or SOME

Syntax:

```
operand comparison_operator ANY (subquery)
operand IN (subquery)
operand comparison_operator SOME (subquery)
```

Where `comparison_operator` is one of these operators:

```
=  >  <  >=  <=  <>  !=
```

The `ANY` keyword, which must follow a comparison operator, means “return `TRUE` if the comparison is`TRUE` for `ANY` of the values in the column that the subquery returns.” For example:

```
SELECT s1 FROM t1 WHERE s1 > ANY (SELECT s1 FROM t2);
```

Suppose that there is a row in table `t1` containing `(10)`. The expression is `TRUE` if table `t2` contains`(21,14,7)` because there is a value 7 in `t2` that is less than 10. The expression is `FALSE` if table `t2`Subqueries contains `(20,10)`, or if table `t2` is empty. The expression is unknown (that is, `NULL`) if table `t2` contains

```
(NULL,NULL,NULL).
```

When used with a subquery, the word `IN` is an alias for `= ANY`. Thus, these two statements are the same:

```
SELECT s1 FROM t1 WHERE s1 = ANY (SELECT s1 FROM t2);
SELECT s1 FROM t1 WHERE s1 IN    (SELECT s1 FROM t2);
```

`IN` and `= ANY` are not synonyms when used with an expression list. `IN` can take an expression list, but =`ANY` cannot. See Section 12.4.2, “Comparison Functions and Operators”.

`NOT IN` is not an alias for `<> ANY`, but for `<> ALL`. See Section 13.2.10.4, “Subqueries with ALL”.

The word `SOME` is an alias for `ANY`. Thus, these two statements are the same:

```
SELECT s1 FROM t1 WHERE s1 <> ANY  (SELECT s1 FROM t2);
SELECT s1 FROM t1 WHERE s1 <> SOME (SELECT s1 FROM t2);
```

Use of the word `SOME` is rare, but this example shows why it might be useful. To most people, the English phrase “a is not equal to any b” means “there is no b which is equal to a,” but that is not what is meant by the SQL syntax. The syntax means “there is some b to which a is not equal.” Using `<> SOME` instead helps ensure that everyone understands the true meaning of the query.

#### 13.2.10.4 Subqueries with ALL

Syntax:

```
operand comparison_operator ALL (subquery)
```

The word `ALL`, which must follow a comparison operator, means “return `TRUE` if the comparison is `TRUE` for`ALL` of the values in the column that the subquery returns.” For example:

```
SELECT s1 FROM t1 WHERE s1 > ALL (SELECT s1 FROM t2);
```

Suppose that there is a row in table `t1` containing `(10)`. The expression is `TRUE` if table `t2` contains`(-5,0,+5)` because 10 is greater than all three values in `t2`. The expression is `FALSE` if table `t2`contains `(12,6,NULL,-100)` because there is a single value 12 in table `t2` that is greater than 10. The expression is unknown (that is, `NULL`) if table `t2` contains `(0,NULL,1)`.

Finally, the expression is `TRUE` if table `t2` is empty. So, the following expression is `TRUE` when table `t2` is empty:

```
SELECT * FROM t1 WHERE 1 > ALL (SELECT s1 FROM t2);
```

But this expression is `NULL` when table `t2` is empty:

```
SELECT * FROM t1 WHERE 1 > (SELECT s1 FROM t2);
```

In addition, the following expression is `NULL` when table `t2` is empty:

```
SELECT * FROM t1 WHERE 1 > ALL (SELECT MAX(s1) FROM t2);
```

In general, tables containing `NULL` values and empty tables are “edge cases.” When writing subqueries,always consider whether you have taken those two possibilities into account.

`NOT IN` is an alias for `<> ALL`. Thus, these two statements are the same:

```
SELECT s1 FROM t1 WHERE s1 <> ALL (SELECT s1 FROM t2);
```

Subqueries

```
SELECT s1 FROM t1 WHERE s1 NOT IN (SELECT s1 FROM t2);
```

#### 13.2.10.5 Row Subqueries

Scalar or column subqueries return a single value or a column of values. A row subquery is a subquery variant that returns a single row and can thus return more than one column value. Legal operators for row subquery comparisons are:

```
=  >  <  >=  <=  <>  !=  <=>
```

Here are two examples:

```
SELECT * FROM t1
WHERE (col1,col2) = (SELECT col3, col4 FROM t2 WHERE id = 10);
SELECT * FROM t1
WHERE ROW(col1,col2) = (SELECT col3, col4 FROM t2 WHERE id = 10);
```

For both queries, if the table `t2` contains a single row with `id = 10`, the subquery returns a single row.

If this row has `col3` and `col4` values equal to the `col1` and `col2` values of any rows in `t1`, the `WHERE`expression is `TRUE` and each query returns those `t1` rows. If the `t2` row `col3` and `col4` values are not equal the `col1` and `col2` values of any `t1` row, the expression is `FALSE` and the query returns an empty result set. The expression is unknown (that is, `NULL`) if the subquery produces no rows. An error occurs if the subquery produces multiple rows because a row subquery can return at most one row.

For information about how each operator works for row comparisons, see Section 12.4.2, “Comparison Functions and Operators”.

The expressions `(1,2)` and `ROW(1,2)` are sometimes called row constructors. The two are equivalent.

The row constructor and the row returned by the subquery must contain the same number of values.

A row constructor is used for comparisons with subqueries that return two or more columns. When a subquery returns a single column, this is regarded as a scalar value and not as a row, so a row constructor cannot be used with a subquery that does not return at least two columns. Thus, the following query fails with a syntax error:

```
SELECT * FROM t1 WHERE ROW(1) = (SELECT column1 FROM t2)
```

Row constructors are legal in other contexts. For example, the following two statements are semantically equivalent (and are handled in the same way by the optimizer):

```
SELECT * FROM t1 WHERE (column1,column2) = (1,1);
SELECT * FROM t1 WHERE column1 = 1 AND column2 = 1;
```

The following query answers the request, “find all rows in table `t1` that also exist in table `t2`”:

```
SELECT column1,column2,column3
FROM t1
WHERE (column1,column2,column3) IN
(SELECT column1,column2,column3 FROM t2);
```

For more information about the optimizer and row constructors, see Section 8.2.1.18, “Row Constructor Expression Optimization”

#### 13.2.10.6 Subqueries with EXISTS or NOT EXISTS

If a subquery returns any rows at all, `EXISTS subquery` is `TRUE`, and `NOT EXISTS subquery` is`FALSE`. For example:Subqueries

```
SELECT column1 FROM t1 WHERE EXISTS (SELECT * FROM t2);
```

Traditionally, an `EXISTS` subquery starts with `SELECT *`, but it could begin with `SELECT 5` or `SELECT``column1` or anything at all. MySQL ignores the `SELECT` list in such a subquery, so it makes no difference.

For the preceding example, if `t2` contains any rows, even rows with nothing but `NULL` values, the `EXISTS`condition is `TRUE`. This is actually an unlikely example because a `[NOT] EXISTS` subquery almost always contains correlations. Here are some more realistic examples:

- What kind of store is present in one or more cities?

```
SELECT DISTINCT store_type FROM stores
WHERE EXISTS (SELECT * FROM cities_stores
WHERE cities_stores.store_type = stores.store_type);
```

- What kind of store is present in no cities?

```
SELECT DISTINCT store_type FROM stores
WHERE NOT EXISTS (SELECT * FROM cities_stores
WHERE cities_stores.store_type = stores.store_type);
```

- What kind of store is present in all cities?

```
SELECT DISTINCT store_type FROM stores s1
WHERE NOT EXISTS (
SELECT * FROM cities WHERE NOT EXISTS (
SELECT * FROM cities_stores
WHERE cities_stores.city = cities.city
AND cities_stores.store_type = stores.store_type));
```

The last example is a double-nested `NOT EXISTS` query. That is, it has a `NOT EXISTS` clause within a `NOT EXISTS` clause. Formally, it answers the question “does a city exist with a store that is not in`Stores`”? But it is easier to say that a nested `NOT EXISTS` answers the question “is x `TRUE` for all y?”

#### 13.2.10.7 Correlated Subqueries

A correlated subquery is a subquery that contains a reference to a table that also appears in the outer query. For example:

```
SELECT * FROM t1
WHERE column1 = ANY (SELECT column1 FROM t2
WHERE t2.column2 = t1.column2);
```

Notice that the subquery contains a reference to a column of `t1`, even though the subquery's `FROM` clause does not mention a table `t1`. So, MySQL looks outside the subquery, and finds `t1` in the outer query.

Suppose that table `t1` contains a row where `column1 = 5` and `column2 = 6`; meanwhile, table `t2`contains a row where `column1 = 5` and `column2 = 7`. The simple expression `... WHERE column1``= ANY (SELECT column1 FROM t2)` would be `TRUE`, but in this example, the `WHERE` clause within the subquery is `FALSE` (because `(5,6)` is not equal to `(5,7)`), so the expression as a whole is `FALSE`.

> Scoping rule: MySQL evaluates from inside to outside. For example:

```
SELECT column1 FROM t1 AS x
WHERE x.column1 = (SELECT column1 FROM t2 AS x
WHERE x.column1 = (SELECT column1 FROM t3
WHERE x.column2 = t3.column1));
```

In this statement, `x.column2` must be a column in table `t2` because `SELECT column1 FROM t2 AS``x ...` renames `t2`. It is not a column in table `t1` because `SELECT column1 FROM t1 ...` is an outer query that is farther out.

Subqueries For subqueries in `HAVING` or `ORDER BY` clauses, MySQL also looks for column names in the outer select list.

For certain cases, a correlated subquery is optimized. For example:

```
val IN (SELECT key_val FROM tbl_name WHERE correlated_condition)
```

Otherwise, they are inefficient and likely to be slow. Rewriting the query as a join might improve performance.

Aggregate functions in correlated subqueries may contain outer references, provided the function contains nothing but outer references, and provided the function is not contained in another function or expression.

#### 13.2.10.8 Derived Tables

A derived table is an expression that generates a table within the scope of a query `FROM` clause. For example, a subquery in a `SELECT` statement `FROM` clause is a derived table:

```
SELECT ... FROM (subquery) [AS] tbl_name ...
```

The `[AS] tbl_name` clause is mandatory because every table in a `FROM` clause must have a name. Any columns in the derived table must have unique names.

For the sake of illustration, assume that you have this table:

```
CREATE TABLE t1 (s1 INT, s2 CHAR(5), s3 FLOAT);
```

Here is how to use a subquery in the `FROM` clause, using the example table:

```
INSERT INTO t1 VALUES (1,'1',1.0);
INSERT INTO t1 VALUES (2,'2',2.0);
SELECT sb1,sb2,sb3
FROM (SELECT s1 AS sb1, s2 AS sb2, s3*2 AS sb3 FROM t1) AS sb
WHERE sb1 > 1;
```

Result:

```
+------+------+------+
| sb1  | sb2  | sb3  |
+------+------+------+
|    2 | 2    |    4 |
+------+------+------+
```

Here is another example: Suppose that you want to know the average of a set of sums for a grouped table.

This does not work:

```
SELECT AVG(SUM(column1)) FROM t1 GROUP BY column1;
```

However, this query provides the desired information:

```
SELECT AVG(sum_column1)
FROM (SELECT SUM(column1) AS sum_column1
FROM t1 GROUP BY column1) AS t1;
```

Notice that the column name used within the subquery (`sum_column1`) is recognized in the outer query.

A derived table can return a scalar, column, row, or table.

Derived tables are subject to these restrictions:Subqueries

- A derived table cannot be a correlated subquery.
- A derived table cannot contain references to other tables of the same `SELECT`.
- A derived table cannot contain outer references. This is a MySQL restriction, not a restriction of the SQL

standard.

The optimizer determines information about derived tables in such a way that `EXPLAIN` does not need to materialize them. See Section 8.2.2.4, “Optimizing Derived Tables”.

It is possible under certain circumstances that using `EXPLAIN SELECT` modifies table data. This can occur if the outer query accesses any tables and an inner query invokes a stored function that changes one or more rows of a table. Suppose that there are two tables `t1` and `t2` in database `d1`, and a stored function`f1` that modifies `t2`, created as shown here:

```
CREATE DATABASE d1;
USE d1;
CREATE TABLE t1 (c1 INT);
CREATE TABLE t2 (c1 INT);
CREATE FUNCTION f1(p1 INT) RETURNS INT
BEGIN
INSERT INTO t2 VALUES (p1);
RETURN p1;
END;
```

Referencing the function directly in an `EXPLAIN SELECT` has no effect on `t2`, as shown here:

```
mysql> SELECT * FROM t2;
Empty set (0.02 sec)
mysql> EXPLAIN SELECT f1(5)\G
*************************** 1. row ***************************
id: 1
select_type: SIMPLE
table: NULL
type: NULL
possible_keys: NULL
key: NULL
key_len: NULL
ref: NULL
rows: NULL
Extra: No tables used
1 row in set (0.01 sec)
mysql> SELECT * FROM t2;
Empty set (0.01 sec)
```

This is because the `SELECT` statement did not reference any tables, as can be seen in the `table` and`Extra` columns of the output. This is also true of the following nested `SELECT`:

```
mysql> EXPLAIN SELECT NOW() AS a1, (SELECT f1(5)) AS a2\G
*************************** 1. row ***************************
id: 1
select_type: SIMPLE
table: NULL
type: NULL
possible_keys: NULL
key: NULL
key_len: NULL
ref: NULL
rows: NULL
filtered: NULL
Extra: No tables used
1 row in set, 1 warning (0.00 sec)
```

Subqueries

```
mysql> SHOW WARNINGS;
+-------+------+------------------------------------------+
| Level | Code | Message                                  |
+-------+------+------------------------------------------+
| Note  | 1249 | Select 2 was reduced during optimization |
+-------+------+------------------------------------------+
1 row in set (0.00 sec)
mysql> SELECT * FROM t2;
Empty set (0.00 sec)
```

However, if the outer `SELECT` references any tables, the optimizer executes the statement in the subquery as well, with the result that `t2` is modified:

```
mysql> EXPLAIN SELECT * FROM t1 AS a1, (SELECT f1(5)) AS a2\G
*************************** 1. row ***************************
id: 1
select_type: PRIMARY
table: <derived2>
type: system
possible_keys: NULL
key: NULL
key_len: NULL
ref: NULL
rows: 1
Extra: NULL
*************************** 2. row ***************************
id: 1
select_type: PRIMARY
table: a1
type: ALL
possible_keys: NULL
key: NULL
key_len: NULL
ref: NULL
rows: 1
Extra: NULL
*************************** 3. row ***************************
id: 2
select_type: DERIVED
table: NULL
type: NULL
possible_keys: NULL
key: NULL
key_len: NULL
ref: NULL
rows: NULL
Extra: No tables used
3 rows in set (0.00 sec)
mysql> SELECT * FROM t2;
+------+
| c1   |
+------+
|    5 |
+------+
1 row in set (0.00 sec)
```

#### 13.2.10.9 Subquery Errors

There are some errors that apply only to subqueries. This section describes them.

- Unsupported subquery syntax:

```
ERROR 1235 (ER_NOT_SUPPORTED_YET)
SQLSTATE = 42000
```

Subqueries

```
Message = "This version of MySQL doesn't yet support
'LIMIT & IN/ALL/ANY/SOME subquery'"
```

This means that MySQL does not support statements of the following form:

```
SELECT * FROM t1 WHERE s1 IN (SELECT s2 FROM t2 ORDER BY s1 LIMIT 1)
```

- Incorrect number of columns from subquery:

```
ERROR 1241 (ER_OPERAND_COL)
SQLSTATE = 21000
Message = "Operand should contain 1 column(s)"
```

This error occurs in cases like this:

```
SELECT (SELECT column1, column2 FROM t2) FROM t1;
```

You may use a subquery that returns multiple columns, if the purpose is row comparison. In other contexts, the subquery must be a scalar operand. See Section 13.2.10.5, “Row Subqueries”.

- Incorrect number of rows from subquery:

```
ERROR 1242 (ER_SUBSELECT_NO_1_ROW)
SQLSTATE = 21000
Message = "Subquery returns more than 1 row"
```

This error occurs for statements where the subquery must return at most one row but returns multiple rows. Consider the following example:

```
SELECT * FROM t1 WHERE column1 = (SELECT column1 FROM t2);
```

If `SELECT column1 FROM t2` returns just one row, the previous query works. If the subquery returns more than one row, error 1242 occurs. In that case, the query should be rewritten as:

```
SELECT * FROM t1 WHERE column1 = ANY (SELECT column1 FROM t2);
```

- Incorrectly used table in subquery:

```
Error 1093 (ER_UPDATE_TABLE_USED)
SQLSTATE = HY000
Message = "You can't specify target table 'x'
for update in FROM clause"
```

This error occurs in cases such as the following, which attempts to modify a table and select from the same table in the subquery:

```
UPDATE t1 SET column2 = (SELECT MAX(column1) FROM t1);
```

You can use a subquery for assignment within an `UPDATE` statement because subqueries are legal in`UPDATE` and `DELETE` statements as well as in `SELECT` statements. However, you cannot use the same table (in this case, table `t1`) for both the subquery `FROM` clause and the update target.

For transactional storage engines, the failure of a subquery causes the entire statement to fail. For nontransactional storage engines, data modifications made before the error was encountered are preserved.

#### 13.2.10.10 Optimizing Subqueries

Development is ongoing, so no optimization tip is reliable for the long term. The following list provides some interesting tricks that you might want to play with. See also Section 8.2.2, “Optimizing Subqueries and Derived Tables”.

Subqueries

- Use subquery clauses that affect the number or order of the rows in the subquery. For example:

```
SELECT * FROM t1 WHERE t1.column1 IN
(SELECT column1 FROM t2 ORDER BY column1);
SELECT * FROM t1 WHERE t1.column1 IN
(SELECT DISTINCT column1 FROM t2);
SELECT * FROM t1 WHERE EXISTS
(SELECT * FROM t2 LIMIT 1);
```

- Replace a join with a subquery. For example, try this:

```
SELECT DISTINCT column1 FROM t1 WHERE t1.column1 IN (
SELECT column1 FROM t2);
```

Instead of this:

```
SELECT DISTINCT t1.column1 FROM t1, t2
WHERE t1.column1 = t2.column1;
```

- Some subqueries can be transformed to joins for compatibility with older versions of MySQL that do not

support subqueries. However, in some cases, converting a subquery to a join may improve performance.

See Section 13.2.10.11, “Rewriting Subqueries as Joins”.

- Move clauses from outside to inside the subquery. For example, use this query:

```
SELECT * FROM t1
WHERE s1 IN (SELECT s1 FROM t1 UNION ALL SELECT s1 FROM t2);
```

Instead of this query:

```
SELECT * FROM t1
WHERE s1 IN (SELECT s1 FROM t1) OR s1 IN (SELECT s1 FROM t2);
```

For another example, use this query:

```
SELECT (SELECT column1 + 5 FROM t1) FROM t2;
```

Instead of this query:

```
SELECT (SELECT column1 FROM t1) + 5 FROM t2;
```

- Use a row subquery instead of a correlated subquery. For example, use this query:

```
SELECT * FROM t1
WHERE (column1,column2) IN (SELECT column1,column2 FROM t2);
```

Instead of this query:

```
SELECT * FROM t1
WHERE EXISTS (SELECT * FROM t2 WHERE t2.column1=t1.column1
AND t2.column2=t1.column2);
```

- Use `NOT (a = ANY (...))` rather than `a <> ALL (...)`.
- Use `x = ANY (table containing (1,2))` rather than `x=1 OR x=2`.
- Use `= ANY` rather than `EXISTS`.
- For uncorrelated subqueries that always return one row, `IN` is always slower than =. For example, use

this query:

```
SELECT * FROM t1
WHERE t1.col_name = (SELECT a FROM t2 WHERE b = some_const);
```

Subqueries Instead of this query:

```
SELECT * FROM t1
WHERE t1.col_name IN (SELECT a FROM t2 WHERE b = some_const);
```

These tricks might cause programs to go faster or slower. Using MySQL facilities like the `BENCHMARK()`function, you can get an idea about what helps in your own situation. See Section 12.16, “Information Functions”.

Some optimizations that MySQL itself makes are:

- MySQL executes uncorrelated subqueries only once. Use `EXPLAIN` to make sure that a given subquery

really is uncorrelated.

- MySQL rewrites `IN`, `ALL`, `ANY`, and `SOME` subqueries in an attempt to take advantage of the possibility

that the select-list columns in the subquery are indexed.

- MySQL replaces subqueries of the following form with an index-lookup function, which `EXPLAIN`

describes as a special join type (`unique_subquery` or `index_subquery`):

```
... IN (SELECT indexed_column FROM single_table ...)
```

- MySQL enhances expressions of the following form with an expression involving `MIN()` or `MAX()`,

unless `NULL` values or empty sets are involved:

```
value {ALL|ANY|SOME} {> | < | >= | <=} (uncorrelated subquery)
```

For example, this `WHERE` clause:

```
WHERE 5 > ALL (SELECT x FROM t)
```

might be treated by the optimizer like this:

```
WHERE 5 > (SELECT MAX(x) FROM t)
```

See also MySQL Internals: How MySQL Transforms Subqueries.

#### 13.2.10.11 Rewriting Subqueries as Joins

Sometimes there are other ways to test membership in a set of values than by using a subquery. Also, on some occasions, it is not only possible to rewrite a query without a subquery, but it can be more efficient to make use of some of these techniques rather than to use subqueries. One of these is the `IN()` construct:For example, this query:

```
SELECT * FROM t1 WHERE id IN (SELECT id FROM t2);
```

Can be rewritten as:

```
SELECT DISTINCT t1.* FROM t1, t2 WHERE t1.id=t2.id;
```

The queries:

```
SELECT * FROM t1 WHERE id NOT IN (SELECT id FROM t2);
SELECT * FROM t1 WHERE NOT EXISTS (SELECT id FROM t2 WHERE t1.id=t2.id);
```

Can be rewritten as:

```
SELECT table1.*
FROM table1 LEFT JOIN table2 ON table1.id=table2.id
WHERE table2.id IS NULL;
```

Subqueries A `LEFT [OUTER] JOIN` can be faster than an equivalent subquery because the server might be able to optimize it better—a fact that is not specific to MySQL Server alone. Prior to SQL-92, outer joins did not exist, so subqueries were the only way to do certain things. Today, MySQL Server and many other modern database systems offer a wide range of outer join types.

MySQL Server supports multiple-table `DELETE` statements that can be used to efficiently delete rows based on information from one table or even from many tables at the same time. Multiple-table `UPDATE`statements are also supported. See Section 13.2.2, “DELETE Statement”, and Section 13.2.11, “UPDATE Statement”.

#### 13.2.10.12 Restrictions on Subqueries

- In general, you cannot modify a table and select from the same table in a subquery. For example, this

limitation applies to statements of the following forms:

```
DELETE FROM t WHERE ... (SELECT ... FROM t ...);
UPDATE t ... WHERE col = (SELECT ... FROM t ...);
{INSERT|REPLACE} INTO t (SELECT ... FROM t ...);
```

Exception: The preceding prohibition does not apply if for the modified table you are using a derived table and that derived table is materialized rather than merged into the outer query. Example:

```
UPDATE t ... WHERE col = (SELECT * FROM (SELECT ... FROM t...) AS _t ...);
```

Here the result from the derived table is materialized as a temporary table, so the relevant rows in t have already been selected by the time the update to t takes place.

- Row comparison operations are only partially supported:
- For `expr [NOT] IN subquery`, `expr` can be an n-tuple (specified using row constructor syntax)

and the subquery can return rows of n-tuples. The permitted syntax is therefore more specifically

```
expressed as row_constructor [NOT] IN table_subquery
```

- For `expr op {ALL|ANY|SOME} subquery`, `expr` must be a scalar value and the subquery must

be a column subquery; it cannot return multiple-column rows.

In other words, for a subquery that returns rows of n-tuples, this is supported:

```
(expr_1, ..., expr_n) [NOT] IN table_subquery
```

But this is not supported:

```
(expr_1, ..., expr_n) op {ALL|ANY|SOME} subquery
```

The reason for supporting row comparisons for `IN` but not for the others is that `IN` is implemented by rewriting it as a sequence of = comparisons and `AND` operations. This approach cannot be used for `ALL`,`ANY`, or `SOME`.

- Subqueries in the `FROM` clause cannot be correlated subqueries. They are materialized in whole

(evaluated to produce a result set) during query execution, so they cannot be evaluated per row of the outer query. Before MySQL 5.6.3, materialization takes place before evaluation of the outer query. As of

5.6.3, the optimizer delays materialization until the result is needed, which may permit materialization to be avoided. See Section 8.2.2.4, “Optimizing Derived Tables”.

- MySQL does not support `LIMIT` in subqueries for certain subquery operators:

```
mysql> SELECT * FROM t1
WHERE s1 IN (SELECT s2 FROM t2 ORDER BY s1 LIMIT 1);
ERROR 1235 (42000): This version of MySQL doesn't yet support
```

UPDATE Statement

```
'LIMIT & IN/ALL/ANY/SOME subquery'
```

- MySQL permits a subquery to refer to a stored function that has data-modifying side effects such as

inserting rows into a table. For example, if `f()` inserts rows, the following query can modify data:

```
SELECT ... WHERE x IN (SELECT f() ...);
```

This behavior is an extension to the SQL standard. In MySQL, it can produce nondeterministic results because `f()` might be executed a different number of times for different executions of a given query depending on how the optimizer chooses to handle it.

For statement-based or mixed-format replication, one implication of this indeterminism is that such a query can produce different results on the source and its slaves.

- Before MySQL 5.6.3, a subquery in the `FROM` clause is evaluated by materializing the result into a

temporary table, and this table does not use indexes. As of 5.6.3, the optimizer creates an index on the materialized table if this results in faster query execution. See Section 8.2.2.4, “Optimizing Derived Tables”.

### 13.2.11 UPDATE Statement

`UPDATE` is a DML statement that modifies rows in a table.

Single-table syntax:

```
UPDATE [LOW_PRIORITY] [IGNORE] table_reference
SET assignment_list
[WHERE where_condition]
[ORDER BY ...]
[LIMIT row_count]
value:
{expr | DEFAULT}
assignment:
col_name = value
assignment_list:
assignment [, assignment] ...
```

Multiple-table syntax:

```
UPDATE [LOW_PRIORITY] [IGNORE] table_references
SET assignment_list
[WHERE where_condition]
```

For the single-table syntax, the `UPDATE` statement updates columns of existing rows in the named table with new values. The `SET` clause indicates which columns to modify and the values they should be given.

Each value can be given as an expression, or the keyword `DEFAULT` to set a column explicitly to its default value. The `WHERE` clause, if given, specifies the conditions that identify which rows to update. With no`WHERE` clause, all rows are updated. If the `ORDER BY` clause is specified, the rows are updated in the order that is specified. The `LIMIT` clause places a limit on the number of rows that can be updated.

For the multiple-table syntax, `UPDATE` updates rows in each table named in `table_references` that satisfy the conditions. Each matching row is updated once, even if it matches the conditions multiple times.

For multiple-table syntax, `ORDER BY` and `LIMIT` cannot be used.

For partitioned tables, both the single-single and multiple-table forms of this statement support the use of a `PARTITION` clause as part of a table reference. This option takes a list of one or more partitions or subpartitions (or both). Only the partitions (or subpartitions) listed are checked for matches, and a row that UPDATE Statement is not in any of these partitions or subpartitions is not updated, whether it satisfies the `where_condition`or not.

Note Unlike the case when using `PARTITION` with an `INSERT` or `REPLACE` statement, an otherwise valid `UPDATE ... PARTITION` statement is considered successful even if no rows in the listed partitions (or subpartitions) match the `where_condition`.

For more information and examples, see Section 19.5, “Partition Selection”.

`where_condition` is an expression that evaluates to true for each row to be updated. For expression syntax, see Section 9.5, “Expressions”.

`table_references` and `where_condition` are specified as described in Section 13.2.9, “SELECT Statement”.

You need the `UPDATE` privilege only for columns referenced in an `UPDATE` that are actually updated. You need only the `SELECT` privilege for any columns that are read but not modified.

The `UPDATE` statement supports the following modifiers:

- With the `LOW_PRIORITY` modifier, execution of the `UPDATE` is delayed until no other clients are reading

from the table. This affects only storage engines that use only table-level locking (such as `MyISAM`,`MEMORY`, and `MERGE`).

- With the `IGNORE` modifier, the update statement does not abort even if errors occur during the update.

Rows for which duplicate-key conflicts occur on a unique key value are not updated. Rows updated to values that would cause data conversion errors are updated to the closest valid values instead.

`UPDATE IGNORE` statements, including those having an `ORDER BY` clause, are flagged as unsafe for statement-based replication. (This is because the order in which the rows are updated determines which rows are ignored.) Such statements produce a warning in the error log when using statement-based mode and are written to the binary log using the row-based format when using `MIXED` mode. (Bug #11758262,Bug #50439) See Section 17.1.2.3, “Determination of Safe and Unsafe Statements in Binary Logging”, for more information.

If you access a column from the table to be updated in an expression, `UPDATE` uses the current value of the column. For example, the following statement sets `col1` to one more than its current value:

```
UPDATE t1 SET col1 = col1 + 1;
```

The second assignment in the following statement sets `col2` to the current (updated) `col1` value, not the original `col1` value. The result is that `col1` and `col2` have the same value. This behavior differs from standard SQL.

```
UPDATE t1 SET col1 = col1 + 1, col2 = col1;
```

Single-table `UPDATE` assignments are generally evaluated from left to right. For multiple-table updates,there is no guarantee that assignments are carried out in any particular order.

If you set a column to the value it currently has, MySQL notices this and does not update it.

If you update a column that has been declared `NOT NULL` by setting to `NULL`, an error occurs if strict SQL mode is enabled; otherwise, the column is set to the implicit default value for the column data type and the warning count is incremented. The implicit default value is 0 for numeric types, the empty string (`''`) for string types, and the “zero” value for date and time types. See Section 11.5, “Data Type Default Values”.

UPDATE Statement`UPDATE` returns the number of rows that were actually changed. The `mysql_info()` C API function returns the number of rows that were matched and updated and the number of warnings that occurred during the `UPDATE`.

You can use `LIMIT row_count` to restrict the scope of the `UPDATE`. A `LIMIT` clause is a rows-matched restriction. The statement stops as soon as it has found `row_count` rows that satisfy the `WHERE` clause,whether or not they actually were changed.

If an `UPDATE` statement includes an `ORDER BY` clause, the rows are updated in the order specified by the clause. This can be useful in certain situations that might otherwise result in an error. Suppose that a table t contains a column `id` that has a unique index. The following statement could fail with a duplicate-key error, depending on the order in which rows are updated:

```
UPDATE t SET id = id + 1;
```

For example, if the table contains 1 and 2 in the `id` column and 1 is updated to 2 before 2 is updated to 3,an error occurs. To avoid this problem, add an `ORDER BY` clause to cause the rows with larger `id` values to be updated before those with smaller values:

```
UPDATE t SET id = id + 1 ORDER BY id DESC;
```

You can also perform `UPDATE` operations covering multiple tables. However, you cannot use `ORDER BY` or`LIMIT` with a multiple-table `UPDATE`. The `table_references` clause lists the tables involved in the join.

Its syntax is described in Section 13.2.9.2, “JOIN Clause”. Here is an example:

```
UPDATE items,month SET items.price=month.price
WHERE items.id=month.id;
```

The preceding example shows an inner join that uses the comma operator, but multiple-table `UPDATE`statements can use any type of join permitted in `SELECT` statements, such as `LEFT JOIN`.

If you use a multiple-table `UPDATE` statement involving `InnoDB` tables for which there are foreign key constraints, the MySQL optimizer might process tables in an order that differs from that of their parent/child relationship. In this case, the statement fails and rolls back. Instead, update a single table and rely on the`ON UPDATE` capabilities that `InnoDB` provides to cause the other tables to be modified accordingly. See Section 13.1.17.5, “FOREIGN KEY Constraints”.

You cannot update a table and select directly from the same table in a subquery. You can work around this by using a multi-table update in which one of the tables is derived from the table that you actually wish to update, and referring to the derived table using an alias. Suppose you wish to update a table named`items` which is defined using the statement shown here:

```
CREATE TABLE items (
id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
wholesale DECIMAL(6,2) NOT NULL DEFAULT 0.00,
retail DECIMAL(6,2) NOT NULL DEFAULT 0.00,
quantity BIGINT NOT NULL DEFAULT 0
);
```

To reduce the retail price of any items for which the markup is 30% or greater and of which you have fewer than one hundred in stock, you might try to use an `UPDATE` statement such as the one following, which uses a subquery in the `WHERE` clause. As shown here, this statement does not work:

```
mysql> UPDATE items
> SET retail = retail * 0.9
> WHERE id IN
>     (SELECT id FROM items
>         WHERE retail / wholesale >= 1.3 AND quantity > 100);
ERROR 1093 (HY000): You can't specify target table 'items' for update in FROM clause
```

Transactional and Locking Statements Instead, you can employ a multi-table update in which the subquery is moved into the list of tables to be updated, using an alias to reference it in the outermost `WHERE` clause, like this:

```
UPDATE items,
(SELECT id FROM items
WHERE id IN
(SELECT id FROM items
WHERE retail / wholesale >= 1.3 AND quantity < 100))
AS discounted
SET items.retail = items.retail * 0.9
WHERE items.id = discounted.id;
```

Because the optimizer tries by default to merge the derived table `discounted` into the outermost query block, this works only if you force materialization of the derived table. You can do this by setting the`derived_merge` flag of the `optimizer_switch` system variable to `off` before running the update, or by using the `NO_MERGE` optimizer hint, as shown here:

```
UPDATE /*+ NO_MERGE(discounted) */ items,
(SELECT id FROM items
WHERE retail / wholesale >= 1.3 AND quantity < 100)
AS discounted
SET items.retail = items.retail * 0.9
WHERE items.id = discounted.id;
```

The advantage of using the optimizer hint in such a case is that it applies only within the query block where it is used, so that it is not necessary to change the value of `optimizer_switch` again after executing the

```
UPDATE.
```

Another possibility is to rewrite the subquery so that it does not use `IN` or `EXISTS`, like this:

```
UPDATE items,
(SELECT id, retail / wholesale AS markup, quantity FROM items)
AS discounted
SET items.retail = items.retail * 0.9
WHERE discounted.markup >= 1.3
AND discounted.quantity < 100
AND items.id = discounted.id;
```

In this case, the subquery is materialized by default rather than merged, so it is not necessary to disable merging of the derived table.

An `UPDATE` on a partitioned table using a storage engine such as `MyISAM` that employs table-level locks locks only those partitions containing rows that match the `UPDATE` statement `WHERE` clause, as long as none of the table partitioning columns are updated. (For storage engines such as `InnoDB` that employ row-level locking, no locking of partitions takes place.) For more information, see Section 19.6.4, “Partitioning and Locking”.

## 13.3 Transactional and Locking Statements

MySQL supports local transactions (within a given client session) through statements such as `SET``autocommit`, `START TRANSACTION`, `COMMIT`, and `ROLLBACK`. See Section 13.3.1, “START TRANSACTION, COMMIT, and ROLLBACK Statements”. XA transaction support enables MySQL to participate in distributed transactions as well. See Section 13.3.7, “XA Transactions”.

### 13.3.1 START TRANSACTION, COMMIT, and ROLLBACK Statements

```
START TRANSACTION
[transaction_characteristic [, transaction_characteristic] ...]
transaction_characteristic: {
WITH CONSISTENT SNAPSHOT
```

START TRANSACTION, COMMIT, and ROLLBACK Statements

```
| READ WRITE
| READ ONLY
}
BEGIN [WORK]
COMMIT [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
ROLLBACK [WORK] [AND [NO] CHAIN] [[NO] RELEASE]
SET autocommit = {0 | 1}
```

These statements provide control over use of transactions:

- `START TRANSACTION` or `BEGIN` start a new transaction.
- `COMMIT` commits the current transaction, making its changes permanent.
- `ROLLBACK` rolls back the current transaction, canceling its changes.
- `SET autocommit` disables or enables the default autocommit mode for the current session.

By default, MySQL runs with autocommit mode enabled. This means that, when not otherwise inside a transaction, each statement is atomic, as if it were surrounded by `START TRANSACTION` and `COMMIT`.

You cannot use `ROLLBACK` to undo the effect; however, if an error occurs during statement execution, the statement is rolled back.

To disable autocommit mode implicitly for a single series of statements, use the `START TRANSACTION`statement:

```
START TRANSACTION;
SELECT @A:=SUM(salary) FROM table1 WHERE type=1;
UPDATE table2 SET summary=@A WHERE type=1;
COMMIT;
```

With `START TRANSACTION`, autocommit remains disabled until you end the transaction with `COMMIT` or`ROLLBACK`. The autocommit mode then reverts to its previous state.

`START TRANSACTION` permits several modifiers that control transaction characteristics. To specify multiple modifiers, separate them by commas.

- The `WITH CONSISTENT SNAPSHOT` modifier starts a consistent read for storage engines that are

capable of it. This applies only to `InnoDB`. The effect is the same as issuing a `START TRANSACTION`followed by a `SELECT` from any `InnoDB` table. See Section 14.7.2.3, “Consistent Nonlocking Reads”.

The `WITH CONSISTENT SNAPSHOT` modifier does not change the current transaction isolation level,so it provides a consistent snapshot only if the current isolation level is one that permits a consistent read. The only isolation level that permits a consistent read is `REPEATABLE READ`. For all other isolation levels, the `WITH CONSISTENT SNAPSHOT` clause is ignored.

- The `READ WRITE` and `READ ONLY` modifiers set the transaction access mode. They permit or prohibit

changes to tables used in the transaction. The `READ ONLY` restriction prevents the transaction from modifying or locking both transactional and nontransactional tables that are visible to other transactions;

the transaction can still modify or lock temporary tables. These modifiers are available as of MySQL

5.6.5.

MySQL enables extra optimizations for queries on `InnoDB` tables when the transaction is known to be read-only. Specifying `READ ONLY` ensures these optimizations are applied in cases where the read-only status cannot be determined automatically. See Section 8.5.3, “Optimizing InnoDB Read-Only Transactions” for more information.

If no access mode is specified, the default mode applies. Unless the default has been changed, it is read/write. It is not permitted to specify both `READ WRITE` and `READ ONLY` in the same statement.

START TRANSACTION, COMMIT, and ROLLBACK Statements In read-only mode, it remains possible to change tables created with the `TEMPORARY` keyword using DML statements. Changes made with DDL statements are not permitted, just as with permanent tables.

For additional information about transaction access mode, including ways to change the default mode,see Section 13.3.6, “SET TRANSACTION Statement”.

If the `read_only` system variable is enabled, explicitly starting a transaction with `START TRANSACTION``READ WRITE` requires the `SUPER` privilege.

Important Many APIs used for writing MySQL client applications (such as JDBC) provide their own methods for starting transactions that can (and sometimes should) be used instead of sending a `START TRANSACTION` statement from the client. See Chapter 23, Connectors and APIs, or the documentation for your API, for more information.

To disable autocommit mode explicitly, use the following statement:

```
SET autocommit=0;
```

After disabling autocommit mode by setting the `autocommit` variable to zero, changes to transaction-safe tables (such as those for `InnoDB` or `NDB`) are not made permanent immediately. You must use `COMMIT` to store your changes to disk or `ROLLBACK` to ignore the changes.

`autocommit` is a session variable and must be set for each session. To disable autocommit mode for each new connection, see the description of the `autocommit` system variable at Section 5.1.7, “Server System Variables”.

`BEGIN` and `BEGIN WORK` are supported as aliases of `START TRANSACTION` for initiating a transaction.

`START TRANSACTION` is standard SQL syntax, is the recommended way to start an ad-hoc transaction,and permits modifiers that `BEGIN` does not.

The `BEGIN` statement differs from the use of the `BEGIN` keyword that starts a `BEGIN ... END` compound statement. The latter does not begin a transaction. See Section 13.6.1, “BEGIN ... END Compound Statement”.

Note Within all stored programs (stored procedures and functions, triggers, and events),the parser treats `BEGIN [WORK]` as the beginning of a `BEGIN ... END` block.

Begin a transaction in this context with `START TRANSACTION` instead.

The optional `WORK` keyword is supported for `COMMIT` and `ROLLBACK`, as are the `CHAIN` and `RELEASE`clauses. `CHAIN` and `RELEASE` can be used for additional control over transaction completion. The value of the `completion_type` system variable determines the default completion behavior. See Section 5.1.7,“Server System Variables”.

The `AND CHAIN` clause causes a new transaction to begin as soon as the current one ends, and the new transaction has the same isolation level as the just-terminated transaction. The new transaction also uses the same access mode (`READ WRITE` or `READ ONLY`) as the just-terminated transaction. The`RELEASE` clause causes the server to disconnect the current client session after terminating the current transaction. Including the `NO` keyword suppresses `CHAIN` or `RELEASE` completion, which can be useful if the `completion_type` system variable is set to cause chaining or release completion by default.

Beginning a transaction causes any pending transaction to be committed. See Section 13.3.3, “Statements That Cause an Implicit Commit”, for more information.

Statements That Cannot Be Rolled Back Beginning a transaction also causes table locks acquired with `LOCK TABLES` to be released, as though you had executed `UNLOCK TABLES`. Beginning a transaction does not release a global read lock acquired

```
with FLUSH TABLES WITH READ LOCK.
```

For best results, transactions should be performed using only tables managed by a single transaction-safe storage engine. Otherwise, the following problems can occur:

- If you use tables from more than one transaction-safe storage engine (such as `InnoDB`), and the

transaction isolation level is not `SERIALIZABLE`, it is possible that when one transaction commits,another ongoing transaction that uses the same tables sees only some of the changes made by the first transaction. That is, the atomicity of transactions is not guaranteed with mixed engines and inconsistencies can result. (If mixed-engine transactions are infrequent, you can use `SET``TRANSACTION ISOLATION LEVEL` to set the isolation level to `SERIALIZABLE` on a per-transaction basis as necessary.)

- If you use tables that are not transaction-safe within a transaction, changes to those tables are stored at

once, regardless of the status of autocommit mode.

- If you issue a `ROLLBACK` statement after updating a nontransactional table within a transaction, an

`ER_WARNING_NOT_COMPLETE_ROLLBACK` warning occurs. Changes to transaction-safe tables are rolled back, but not changes to nontransaction-safe tables.

Each transaction is stored in the binary log in one chunk, upon `COMMIT`. Transactions that are rolled back are not logged. (Exception: Modifications to nontransactional tables cannot be rolled back. If a transaction that is rolled back includes modifications to nontransactional tables, the entire transaction is logged with a`ROLLBACK` statement at the end to ensure that modifications to the nontransactional tables are replicated.)See Section 5.4.4, “The Binary Log”.

You can change the isolation level or access mode for transactions with the `SET TRANSACTION`statement. See Section 13.3.6, “SET TRANSACTION Statement”.

Rolling back can be a slow operation that may occur implicitly without the user having explicitly asked for it (for example, when an error occurs). Because of this, `SHOW PROCESSLIST` displays `Rolling back` in the `State` column for the session, not only for explicit rollbacks performed with the `ROLLBACK` statement but also for implicit rollbacks.

Note In MySQL 5.6, `BEGIN`, `COMMIT`, and `ROLLBACK` are not affected by `--replicate-`

```
do-db or --replicate-ignore-db rules.
```

When `InnoDB` performs a complete rollback of a transaction, all locks set by the transaction are released.

If a single SQL statement within a transaction rolls back as a result of an error, such as a duplicate key error, locks set by the statement are preserved while the transaction remains active. This happens because `InnoDB` stores row locks in a format such that it cannot know afterward which lock was set by which statement.

If a `SELECT` statement within a transaction calls a stored function, and a statement within the stored function fails, that statement rolls back. If `ROLLBACK` is executed for the transaction subsequently, the entire transaction rolls back.

### 13.3.2 Statements That Cannot Be Rolled Back

Some statements cannot be rolled back. In general, these include data definition language (DDL)statements, such as those that create or drop databases, those that create, drop, or alter tables or stored routines.

Statements That Cause an Implicit Commit You should design your transactions not to include such statements. If you issue a statement early in a transaction that cannot be rolled back, and then another statement later fails, the full effect of the transaction cannot be rolled back in such cases by issuing a `ROLLBACK` statement.

### 13.3.3 Statements That Cause an Implicit Commit

The statements listed in this section (and any synonyms for them) implicitly end any transaction active in the current session, as if you had done a `COMMIT` before executing the statement.

Most of these statements also cause an implicit commit after executing. The intent is to handle each such statement in its own special transaction because it cannot be rolled back anyway. Transaction-control and locking statements are exceptions: If an implicit commit occurs before execution, another does not occur after.

- Data definition language (DDL) statements that define or modify database objects. `ALTER`

```
DATABASE ... UPGRADE DATA DIRECTORY NAME, ALTER EVENT, ALTER PROCEDURE, ALTER
SERVER, ALTER TABLE, ALTER TABLESPACE, ALTER VIEW, CREATE DATABASE, CREATE EVENT,
CREATE INDEX, CREATE PROCEDURE, CREATE SERVER, CREATE TABLE, CREATE TABLESPACE,
CREATE TRIGGER, CREATE VIEW, DROP DATABASE, DROP EVENT, DROP INDEX, DROP PROCEDURE,
DROP SERVER, DROP TABLE, DROP TABLESPACE, DROP TRIGGER, DROP VIEW, RENAME TABLE,
TRUNCATE TABLE.
```

`ALTER FUNCTION`, `CREATE FUNCTION` and `DROP FUNCTION` also cause an implicit commit when used with stored functions, but not with loadable functions. (`ALTER FUNCTION` can only be used with stored functions.)`CREATE TABLE` and `DROP TABLE` statements do not commit a transaction if the `TEMPORARY` keyword is used. (This does not apply to other operations on temporary tables such as `ALTER TABLE` and`CREATE INDEX`, which do cause a commit.) However, although no implicit commit occurs, neither can the statement be rolled back, which means that the use of such statements causes transactional atomicity to be violated. For example, if you use `CREATE TEMPORARY TABLE` and then roll back the transaction, the table remains in existence.

The `CREATE TABLE` statement in `InnoDB` is processed as a single transaction. This means that a `ROLLBACK` from the user does not undo `CREATE TABLE` statements the user made during that transaction.

`CREATE TABLE ... SELECT` causes an implicit commit before and after the statement is executed when you are creating nontemporary tables. (No commit occurs for `CREATE TEMPORARY TABLE ...`

```
SELECT.)
```

- Statements that implicitly use or modify tables in the `mysql` database. `ALTER USER`, `CREATE`

```
USER, DROP USER, GRANT, RENAME USER, REVOKE, SET PASSWORD.
```

- Transaction-control and locking statements. `BEGIN`, `LOCK TABLES`, `SET autocommit = 1` (if the

value is not already 1), `START TRANSACTION`, `UNLOCK TABLES`.

`UNLOCK TABLES` commits a transaction only if any tables currently have been locked with `LOCK``TABLES` to acquire nontransactional table locks. A commit does not occur for `UNLOCK TABLES` following`FLUSH TABLES WITH READ LOCK` because the latter statement does not acquire table-level locks.

Transactions cannot be nested. This is a consequence of the implicit commit performed for any current transaction when you issue a `START TRANSACTION` statement or one of its synonyms.

Statements that cause an implicit commit cannot be used in an XA transaction while the transaction is in an `ACTIVE` state.

SAVEPOINT, ROLLBACK TO SAVEPOINT, and RELEASE SAVEPOINT Statements The `BEGIN` statement differs from the use of the `BEGIN` keyword that starts a `BEGIN ... END`compound statement. The latter does not cause an implicit commit. See Section 13.6.1, “BEGIN ... END Compound Statement”.

- Data loading statements. `LOAD DATA`. `LOAD DATA` causes an implicit commit only for tables using the

`NDB` storage engine.

- Administrative statements. `ANALYZE TABLE`, `CACHE INDEX`, `CHECK TABLE`, `FLUSH`, `LOAD INDEX`

```
INTO CACHE, OPTIMIZE TABLE, REPAIR TABLE, RESET.
```

- Replication control statements. `START SLAVE`, `STOP SLAVE`, `RESET SLAVE`, `CHANGE MASTER TO`.

> 13.3.4 SAVEPOINT, ROLLBACK TO SAVEPOINT, and RELEASE SAVEPOINT Statements

```
SAVEPOINT identifier
ROLLBACK [WORK] TO [SAVEPOINT] identifier
RELEASE SAVEPOINT identifier
```

`InnoDB` supports the SQL statements `SAVEPOINT`, `ROLLBACK TO SAVEPOINT`, `RELEASE SAVEPOINT`and the optional `WORK` keyword for `ROLLBACK`.

The `SAVEPOINT` statement sets a named transaction savepoint with a name of `identifier`. If the current transaction has a savepoint with the same name, the old savepoint is deleted and a new one is set.

The `ROLLBACK TO SAVEPOINT` statement rolls back a transaction to the named savepoint without terminating the transaction. Modifications that the current transaction made to rows after the savepoint was set are undone in the rollback, but `InnoDB` does not release the row locks that were stored in memory after the savepoint. (For a new inserted row, the lock information is carried by the transaction ID stored in the row; the lock is not separately stored in memory. In this case, the row lock is released in the undo.)Savepoints that were set at a later time than the named savepoint are deleted.

If the `ROLLBACK TO SAVEPOINT` statement returns the following error, it means that no savepoint with the specified name exists:

```
ERROR 1305 (42000): SAVEPOINT identifier does not exist
```

The `RELEASE SAVEPOINT` statement removes the named savepoint from the set of savepoints of the current transaction. No commit or rollback occurs. It is an error if the savepoint does not exist.

All savepoints of the current transaction are deleted if you execute a `COMMIT`, or a `ROLLBACK` that does not name a savepoint.

A new savepoint level is created when a stored function is invoked or a trigger is activated. The savepoints on previous levels become unavailable and thus do not conflict with savepoints on the new level. When the function or trigger terminates, any savepoints it created are released and the previous savepoint level is restored.

### 13.3.5 LOCK TABLES and UNLOCK TABLES Statements

```
LOCK TABLES
tbl_name [[AS] alias] lock_type
[, tbl_name [[AS] alias] lock_type] ...
lock_type: {
READ [LOCAL]
```

LOCK TABLES and UNLOCK TABLES Statements

```
| [LOW_PRIORITY] WRITE
}
UNLOCK TABLES
```

MySQL enables client sessions to acquire table locks explicitly for the purpose of cooperating with other sessions for access to tables, or to prevent other sessions from modifying tables during periods when a session requires exclusive access to them. A session can acquire or release locks only for itself. One session cannot acquire locks for another session or release locks held by another session.

Locks may be used to emulate transactions or to get more speed when updating tables. This is explained in more detail in Table-Locking Restrictions and Conditions.

`LOCK TABLES` explicitly acquires table locks for the current client session. Table locks can be acquired for base tables or views. You must have the `LOCK TABLES` privilege, and the `SELECT` privilege for each object to be locked.

For view locking, `LOCK TABLES` adds all base tables used in the view to the set of tables to be locked and locks them automatically. As of MySQL 5.6.50, `LOCK TABLES` checks that the view definer has the proper privileges on the tables underlying the view.

If you lock a table explicitly with `LOCK TABLES`, any tables used in triggers are also locked implicitly, as described in LOCK TABLES and Triggers.

`UNLOCK TABLES` explicitly releases any table locks held by the current session. `LOCK TABLES` implicitly releases any table locks held by the current session before acquiring new locks.

Another use for `UNLOCK TABLES` is to release the global read lock acquired with the `FLUSH TABLES``WITH READ LOCK` statement, which enables you to lock all tables in all databases. See Section 13.7.6.3,“FLUSH Statement”. (This is a very convenient way to get backups if you have a file system such as Veritas that can take snapshots in time.)A table lock protects only against inappropriate reads or writes by other sessions. A session holding a`WRITE` lock can perform table-level operations such as `DROP TABLE` or `TRUNCATE TABLE`. For sessions holding a `READ` lock, `DROP TABLE` and `TRUNCATE TABLE` operations are not permitted.

The following discussion applies only to non-`TEMPORARY` tables. `LOCK TABLES` is permitted (but ignored)for a `TEMPORARY` table. The table can be accessed freely by the session within which it was created,regardless of what other locking may be in effect. No lock is necessary because no other session can see the table.

- Table Lock Acquisition
- Table Lock Release
- Interaction of Table Locking and Transactions
- LOCK TABLES and Triggers
- Table-Locking Restrictions and Conditions

> Table Lock Acquisition

To acquire table locks within the current session, use the `LOCK TABLES` statement, which acquires metadata locks (see Section 8.11.4, “Metadata Locking”).

The following lock types are available:LOCK TABLES and UNLOCK TABLES Statements`READ [LOCAL]` lock:

- The session that holds the lock can read the table (but not write it).
- Multiple sessions can acquire a `READ` lock for the table at the same time.
- Other sessions can read the table without explicitly acquiring a `READ` lock.
- The `LOCAL` modifier enables nonconflicting `INSERT` statements (concurrent inserts) by other sessions

to execute while the lock is held. (See Section 8.11.3, “Concurrent Inserts”.) However, `READ LOCAL`cannot be used if you are going to manipulate the database using processes external to the server while you hold the lock. For `InnoDB` tables, `READ LOCAL` is the same as `READ`.

```
[LOW_PRIORITY] WRITE lock:
```

- The session that holds the lock can read and write the table.
- Only the session that holds the lock can access the table. No other session can access it until the lock is

released.

- Lock requests for the table by other sessions block while the `WRITE` lock is held.
- The `LOW_PRIORITY` modifier has no effect. In previous versions of MySQL, it affected locking behavior,

but this is no longer true. It is now deprecated and its use produces a warning. Use `WRITE` without`LOW_PRIORITY` instead.

`WRITE` locks normally have higher priority than `READ` locks to ensure that updates are processed as soon as possible. This means that if one session obtains a `READ` lock and then another session requests a `WRITE` lock, subsequent `READ` lock requests wait until the session that requested the `WRITE` lock has obtained the lock and released it. (An exception to this policy can occur for small values of the`max_write_lock_count` system variable; see Section 8.11.4, “Metadata Locking”.)If the `LOCK TABLES` statement must wait due to locks held by other sessions on any of the tables, it blocks until all locks can be acquired.

A session that requires locks must acquire all the locks that it needs in a single `LOCK TABLES` statement.

While the locks thus obtained are held, the session can access only the locked tables. For example, in the following sequence of statements, an error occurs for the attempt to access `t2` because it was not locked in the `LOCK TABLES` statement:

```
mysql> LOCK TABLES t1 READ;
mysql> SELECT COUNT(*) FROM t1;
+----------+
| COUNT(*) |
+----------+
|        3 |
+----------+
mysql> SELECT COUNT(*) FROM t2;
ERROR 1100 (HY000): Table 't2' was not locked with LOCK TABLES
```

Tables in the `INFORMATION_SCHEMA` database are an exception. They can be accessed without being locked explicitly even while a session holds table locks obtained with `LOCK TABLES`.

You cannot refer to a locked table multiple times in a single query using the same name. Use aliases instead, and obtain a separate lock for the table and each alias:

```
mysql> LOCK TABLE t WRITE, t AS t1 READ;
mysql> INSERT INTO t SELECT * FROM t;
ERROR 1100: Table 't' was not locked with LOCK TABLES
mysql> INSERT INTO t SELECT * FROM t AS t1;
```

LOCK TABLES and UNLOCK TABLES Statements The error occurs for the first `INSERT` because there are two references to the same name for a locked table. The second `INSERT` succeeds because the references to the table use different names.

If your statements refer to a table by means of an alias, you must lock the table using that same alias. It does not work to lock the table without specifying the alias:

```
mysql> LOCK TABLE t READ;
mysql> SELECT * FROM t AS myalias;
ERROR 1100: Table 'myalias' was not locked with LOCK TABLES
```

Conversely, if you lock a table using an alias, you must refer to it in your statements using that alias:

```
mysql> LOCK TABLE t AS myalias READ;
mysql> SELECT * FROM t;
ERROR 1100: Table 't' was not locked with LOCK TABLES
mysql> SELECT * FROM t AS myalias;
```

Note`LOCK TABLES` or `UNLOCK TABLES`, when applied to a partitioned table, always locks or unlocks the entire table; these statements do not support partition lock pruning. See Section 19.6.4, “Partitioning and Locking”.

> Table Lock Release

When the table locks held by a session are released, they are all released at the same time. A session can release its locks explicitly, or locks may be released implicitly under certain conditions.

- A session can release its locks explicitly with `UNLOCK TABLES`.
- If a session issues a `LOCK TABLES` statement to acquire a lock while already holding locks, its existing

locks are released implicitly before the new locks are granted.

- If a session begins a transaction (for example, with `START TRANSACTION`), an implicit `UNLOCK`

`TABLES` is performed, which causes existing locks to be released. (For additional information about the interaction between table locking and transactions, see Interaction of Table Locking and Transactions.)If the connection for a client session terminates, whether normally or abnormally, the server implicitly releases all table locks held by the session (transactional and nontransactional). If the client reconnects,the locks are no longer be in effect. In addition, if the client had an active transaction, the server rolls back the transaction upon disconnect, and if reconnect occurs, the new session begins with autocommit enabled. For this reason, clients may wish to disable auto-reconnect. With auto-reconnect in effect, the client is not notified if reconnect occurs but any table locks or current transaction are lost. With auto-reconnect disabled, if the connection drops, an error occurs for the next statement issued. The client can detect the error and take appropriate action such as reacquiring the locks or redoing the transaction. See Automatic Reconnection Control.

Note If you use `ALTER TABLE` on a locked table, it may become unlocked. For example,if you attempt a second `ALTER TABLE` operation, the result may be an error `Table``'tbl_name' was not locked with LOCK TABLES`. To handle this, lock the table again prior to the second alteration. See also Section B.3.6.1, “Problems with ALTER TABLE”.

> Interaction of Table Locking and Transactions

`LOCK TABLES` and `UNLOCK TABLES` interact with the use of transactions as follows:LOCK TABLES and UNLOCK TABLES Statements

- `LOCK TABLES` is not transaction-safe and implicitly commits any active transaction before attempting to

lock the tables.

- `UNLOCK TABLES` implicitly commits any active transaction, but only if `LOCK TABLES` has been used

to acquire table locks. For example, in the following set of statements, `UNLOCK TABLES` releases the global read lock but does not commit the transaction because no table locks are in effect:

```
FLUSH TABLES WITH READ LOCK;
START TRANSACTION;
SELECT ... ;
UNLOCK TABLES;
```

- Beginning a transaction (for example, with `START TRANSACTION`) implicitly commits any current

transaction and releases existing table locks.

- `FLUSH TABLES WITH READ LOCK` acquires a global read lock and not table locks, so it is not

subject to the same behavior as `LOCK TABLES` and `UNLOCK TABLES` with respect to table locking and implicit commits. For example, `START TRANSACTION` does not release the global read lock. See Section 13.7.6.3, “FLUSH Statement”.

- Other statements that implicitly cause transactions to be committed do not release existing table locks.

For a list of such statements, see Section 13.3.3, “Statements That Cause an Implicit Commit”.

- The correct way to use `LOCK TABLES` and `UNLOCK TABLES` with transactional tables, such as `InnoDB`

tables, is to begin a transaction with `SET autocommit = 0` (not `START TRANSACTION`) followed by`LOCK TABLES`, and to not call `UNLOCK TABLES` until you commit the transaction explicitly. For example,if you need to write to table `t1` and read from table `t2`, you can do this:

```
SET autocommit=0;
LOCK TABLES t1 WRITE, t2 READ, ...;
... do something with tables t1 and t2 here ...
COMMIT;
UNLOCK TABLES;
```

When you call `LOCK TABLES`, `InnoDB` internally takes its own table lock, and MySQL takes its own table lock. `InnoDB` releases its internal table lock at the next commit, but for MySQL to release its table lock, you have to call `UNLOCK TABLES`. You should not have `autocommit = 1`, because then `InnoDB`releases its internal table lock immediately after the call of `LOCK TABLES`, and deadlocks can very easily happen. `InnoDB` does not acquire the internal table lock at all if `autocommit = 1`, to help old applications avoid unnecessary deadlocks.

- `ROLLBACK` does not release table locks.

> LOCK TABLES and Triggers

If you lock a table explicitly with `LOCK TABLES`, any tables used in triggers are also locked implicitly:

- The locks are taken as the same time as those acquired explicitly with the `LOCK TABLES` statement.
- The lock on a table used in a trigger depends on whether the table is used only for reading. If so, a read

lock suffices. Otherwise, a write lock is used.

- If a table is locked explicitly for reading with `LOCK TABLES`, but needs to be locked for writing because it

might be modified within a trigger, a write lock is taken rather than a read lock. (That is, an implicit write lock needed due to the table's appearance within a trigger causes an explicit read lock request for the table to be converted to a write lock request.)Suppose that you lock two tables, `t1` and `t2`, using this statement:LOCK TABLES and UNLOCK TABLES Statements

```
LOCK TABLES t1 WRITE, t2 READ;
```

If `t1` or `t2` have any triggers, tables used within the triggers are also locked. Suppose that `t1` has a trigger defined like this:

```
CREATE TRIGGER t1_a_ins AFTER INSERT ON t1 FOR EACH ROW
BEGIN
UPDATE t4 SET count = count+1
WHERE id = NEW.id AND EXISTS (SELECT a FROM t3);
INSERT INTO t2 VALUES(1, 2);
END;
```

The result of the `LOCK TABLES` statement is that `t1` and `t2` are locked because they appear in the statement, and `t3` and `t4` are locked because they are used within the trigger:

- `t1` is locked for writing per the `WRITE` lock request.
- `t2` is locked for writing, even though the request is for a `READ` lock. This occurs because `t2` is inserted

into within the trigger, so the `READ` request is converted to a `WRITE` request.

- `t3` is locked for reading because it is only read from within the trigger.
- `t4` is locked for writing because it might be updated within the trigger.

> Table-Locking Restrictions and Conditions

You can safely use `KILL` to terminate a session that is waiting for a table lock. See Section 13.7.6.4, “KILL Statement”.

Do not lock any tables that you are using with `INSERT DELAYED`. An `INSERT DELAYED` in this case results in an error because the insert must be handled by a separate thread, not by the session which holds the lock.

`LOCK TABLES` and `UNLOCK TABLES` cannot be used within stored programs.

Tables in the `performance_schema` database cannot be locked with `LOCK TABLES`, except the`setup_xxx` tables.

The scope of a lock generated by `LOCK TABLES` is a single MySQL server. It is not compatible with NDB Cluster, which has no way of enforcing an SQL-level lock across multiple instances of `mysqld`. You can enforce locking in an API application instead. See Section 18.2.7.10, “Limitations Relating to Multiple NDB Cluster Nodes”, for more information.

The following statements are prohibited while a `LOCK TABLES` statement is in effect: `CREATE TABLE`,`CREATE TABLE ... LIKE`, `CREATE VIEW`, `DROP VIEW`, and DDL statements on stored functions and procedures and events.

For some operations, system tables in the `mysql` database must be accessed. For example, the `HELP`statement requires the contents of the server-side help tables, and `CONVERT_TZ()` might need to read the time zone tables. The server implicitly locks the system tables for reading as necessary so that you need not lock them explicitly. These tables are treated as just described:

```
mysql.help_category
mysql.help_keyword
mysql.help_relation
mysql.help_topic
mysql.proc
mysql.time_zone
mysql.time_zone_leap_second
mysql.time_zone_name
mysql.time_zone_transition
```

SET TRANSACTION Statement

```
mysql.time_zone_transition_type
```

If you want to explicitly place a `WRITE` lock on any of those tables with a `LOCK TABLES` statement, the table must be the only one locked; no other table can be locked with the same statement.

Normally, you do not need to lock tables, because all single `UPDATE` statements are atomic; no other session can interfere with any other currently executing SQL statement. However, there are a few cases when locking tables may provide an advantage:

- If you are going to run many operations on a set of `MyISAM` tables, it is much faster to lock the tables you

are going to use. Locking `MyISAM` tables speeds up inserting, updating, or deleting on them because MySQL does not flush the key cache for the locked tables until `UNLOCK TABLES` is called. Normally, the key cache is flushed after each SQL statement.

The downside to locking the tables is that no session can update a `READ`-locked table (including the one holding the lock) and no session can access a `WRITE`-locked table other than the one holding the lock.

- If you are using tables for a nontransactional storage engine, you must use `LOCK TABLES` if you want

to ensure that no other session modifies the tables between a `SELECT` and an `UPDATE`. The example shown here requires `LOCK TABLES` to execute safely:

```
LOCK TABLES trans READ, customer WRITE;
SELECT SUM(value) FROM trans WHERE customer_id=some_id;
UPDATE customer
SET total_value=sum_from_previous_statement
WHERE customer_id=some_id;
UNLOCK TABLES;
```

Without `LOCK TABLES`, it is possible that another session might insert a new row in the `trans` table between execution of the `SELECT` and `UPDATE` statements.

You can avoid using `LOCK TABLES` in many cases by using relative updates (`UPDATE customer SET``value=value+new_value`) or the `LAST_INSERT_ID()` function.

You can also avoid locking tables in some cases by using the user-level advisory lock functions`GET_LOCK()` and `RELEASE_LOCK()`. These locks are saved in a hash table in the server and implemented with `pthread_mutex_lock()` and `pthread_mutex_unlock()` for high speed. See Section 12.15, “Locking Functions”.

See Section 8.11.1, “Internal Locking Methods”, for more information on locking policy.

### 13.3.6 SET TRANSACTION Statement

```
SET [GLOBAL | SESSION] TRANSACTION
transaction_characteristic [, transaction_characteristic] ...
transaction_characteristic: {
ISOLATION LEVEL level
| access_mode
}
level: {
REPEATABLE READ
| READ COMMITTED
| READ UNCOMMITTED
| SERIALIZABLE
}
access_mode: {
READ WRITE
| READ ONLY
```

SET TRANSACTION Statement

```
}
```

This statement specifies transaction characteristics. It takes a list of one or more characteristic values separated by commas. Each characteristic value sets the transaction isolation level or access mode. The isolation level is used for operations on `InnoDB` tables. The access mode specifies whether transactions operate in read/write or read-only mode.

In addition, `SET TRANSACTION` can include an optional `GLOBAL` or `SESSION` keyword to indicate the scope of the statement.

- Transaction Isolation Levels
- Transaction Access Mode
- Transaction Characteristic Scope

> Transaction Isolation Levels

To set the transaction isolation level, use an `ISOLATION LEVEL level` clause. It is not permitted to specify multiple `ISOLATION LEVEL` clauses in the same `SET TRANSACTION` statement.

The default isolation level is `REPEATABLE READ`. Other permitted values are `READ COMMITTED`, `READ``UNCOMMITTED`, and `SERIALIZABLE`. For information about these isolation levels, see Section 14.7.2.1,“Transaction Isolation Levels”.

> Transaction Access Mode

To set the transaction access mode, use a `READ WRITE` or `READ ONLY` clause. It is not permitted to specify multiple access-mode clauses in the same `SET TRANSACTION` statement.

By default, a transaction takes place in read/write mode, with both reads and writes permitted to tables used in the transaction. This mode may be specified explicitly using `SET TRANSACTION` with an access mode of `READ WRITE`.

If the transaction access mode is set to `READ ONLY`, changes to tables are prohibited. This may enable storage engines to make performance improvements that are possible when writes are not permitted.

In read-only mode, it remains possible to change tables created with the `TEMPORARY` keyword using DML statements. Changes made with DDL statements are not permitted, just as with permanent tables.

The `READ WRITE` and `READ ONLY` access modes also may be specified for an individual transaction using the `START TRANSACTION` statement.

> Transaction Characteristic Scope

You can set transaction characteristics globally, for the current session, or for the next transaction only:

- With the `GLOBAL` keyword:
- The statement applies globally for all subsequent sessions.
- Existing sessions are unaffected.
- With the `SESSION` keyword:
- The statement applies to all subsequent transactions performed within the current session.
- The statement is permitted within transactions, but does not affect the current ongoing transaction.

SET TRANSACTION Statement

- If executed between transactions, the statement overrides any preceding statement that sets the next-

transaction value of the named characteristics.

- Without any `SESSION` or `GLOBAL` keyword:
- The statement applies only to the next single transaction performed within the session.
- Subsequent transactions revert to using the session value of the named characteristics.
- The statement is not permitted within transactions:

```
mysql> START TRANSACTION;
Query OK, 0 rows affected (0.02 sec)
mysql> SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
ERROR 1568 (25001): Transaction characteristics can't be changed
while a transaction is in progress
```

A change to global transaction characteristics requires the `SUPER` privilege. Any session is free to change its session characteristics (even in the middle of a transaction), or the characteristics for its next transaction(prior to the start of that transaction).

To set the global isolation level at server startup, use the `--transaction-isolation=level` option on the command line or in an option file. Values of `level` for this option use dashes rather than spaces,so the permissible values are `READ-UNCOMMITTED`, `READ-COMMITTED`, `REPEATABLE-READ`, or

```
SERIALIZABLE.
```

Similarly, to set the global transaction access mode at server startup, use the `--transaction-read-``only` option. The default is `OFF` (read/write mode) but the value can be set to `ON` for a mode of read only.

For example, to set the isolation level to `REPEATABLE READ` and the access mode to `READ WRITE`, use these lines in the `[mysqld]` section of an option file:

```
[mysqld]
transaction-isolation = REPEATABLE-READ
transaction-read-only = OFF
```

At runtime, characteristics at the global, session, and next-transaction scope levels can be set indirectly using the `SET TRANSACTION` statement, as described previously. They can also be set directly using the`SET` statement to assign values to the `tx_isolation` and `tx_read_only` system variables:

- `SET TRANSACTION` permits optional `GLOBAL` and `SESSION` keywords for setting transaction

characteristics at different scope levels.

- The `SET` statement for assigning values to the `tx_isolation` and `tx_read_only` system variables

has syntaxes for setting these variables at different scope levels.

The following tables show the characteristic scope level set by each `SET TRANSACTION` and variable-assignment syntax.

> Table 13.6 SET TRANSACTION Syntax for Transaction Characteristics Syntax Affected Characteristic Scope

```
SET GLOBAL TRANSACTION  Global
transaction_characteristic
SET SESSION TRANSACTION  Session
transaction_characteristic
```

XA Transactions Syntax Affected Characteristic Scope`SET TRANSACTION` Next transaction only

```
transaction_characteristic
```

> Table 13.7 SET Syntax for Transaction Characteristics Syntax Affected Characteristic Scope

```
SET GLOBAL var_name = value  Global
SET @@GLOBAL.var_name = value  Global
SET PERSIST var_name = value  Global
SET @@PERSIST.var_name = value  Global
```

`SET PERSIST_ONLY var_name = value` No runtime effect`SET @@PERSIST_ONLY.var_name = value` No runtime effect

```
SET SESSION var_name = value  Session
SET @@SESSION.var_name = value  Session
```

`SET var_name = value` Session`SET @@var_name = value` Next transaction only It is possible to check the global and session values of transaction characteristics at runtime:

```
SELECT @@GLOBAL.tx_isolation, @@GLOBAL.tx_read_only;
SELECT @@SESSION.tx_isolation, @@SESSION.tx_read_only;
```

### 13.3.7 XA Transactions

Support for XA transactions is available for the `InnoDB` storage engine. The MySQL XA implementation is based on the X/Open CAE document Distributed Transaction Processing: The XA Specification. This document is published by The Open Group and available at http://www.opengroup.org/public/pubs/catalog/c193.htm. Limitations of the current XA implementation are described in Section 13.3.7.3, “Restrictions on XA Transactions”.

On the client side, there are no special requirements. The XA interface to a MySQL server consists of SQL statements that begin with the `XA` keyword. MySQL client programs must be able to send SQL statements and to understand the semantics of the XA statement interface. They do not need be linked against a recent client library. Older client libraries also work.

Among the MySQL Connectors, MySQL Connector/J 5.0.0 and higher supports XA directly, by means of a class interface that handles the XA SQL statement interface for you.

XA supports distributed transactions, that is, the ability to permit multiple separate transactional resources to participate in a global transaction. Transactional resources often are RDBMSs but may be other kinds of resources.

A global transaction involves several actions that are transactional in themselves, but that all must either complete successfully as a group, or all be rolled back as a group. In essence, this extends ACID properties “up a level” so that multiple ACID transactions can be executed in concert as components of a global operation that also has ACID properties. (As with nondistributed transactions, `SERIALIZABLE`may be preferred if your applications are sensitive to read phenomena. `REPEATABLE READ` may not be sufficient for distributed transactions.)Some examples of distributed transactions:XA Transactions

- An application may act as an integration tool that combines a messaging service with an RDBMS.

The application makes sure that transactions dealing with message sending, retrieval, and processing that also involve a transactional database all happen in a global transaction. You can think of this as“transactional email.”

- An application performs actions that involve different database servers, such as a MySQL server and an

Oracle server (or multiple MySQL servers), where actions that involve multiple servers must happen as part of a global transaction, rather than as separate transactions local to each server.

- A bank keeps account information in an RDBMS and distributes and receives money through automated

teller machines (ATMs). It is necessary to ensure that ATM actions are correctly reflected in the accounts, but this cannot be done with the RDBMS alone. A global transaction manager integrates the ATM and database resources to ensure overall consistency of financial transactions.

Applications that use global transactions involve one or more Resource Managers and a Transaction Manager:

- A Resource Manager (RM) provides access to transactional resources. A database server is one kind of

resource manager. It must be possible to either commit or roll back transactions managed by the RM.

- A Transaction Manager (TM) coordinates the transactions that are part of a global transaction. It

communicates with the RMs that handle each of these transactions. The individual transactions within a global transaction are “branches” of the global transaction. Global transactions and their branches are identified by a naming scheme described later.

The MySQL implementation of XA enables a MySQL server to act as a Resource Manager that handles XA transactions within a global transaction. A client program that connects to the MySQL server acts as the Transaction Manager.

To carry out a global transaction, it is necessary to know which components are involved, and bring each component to a point when it can be committed or rolled back. Depending on what each component reports about its ability to succeed, they must all commit or roll back as an atomic group. That is, either all components must commit, or all components must roll back. To manage a global transaction, it is necessary to take into account that any component or the connecting network might fail.

The process for executing a global transaction uses two-phase commit (2PC). This takes place after the actions performed by the branches of the global transaction have been executed.

1. In the first phase, all branches are prepared. That is, they are told by the TM to get ready to commit.

Typically, this means each RM that manages a branch records the actions for the branch in stable storage. The branches indicate whether they are able to do this, and these results are used for the second phase.

2. In the second phase, the TM tells the RMs whether to commit or roll back. If all branches indicated

when they were prepared that they are able to commit, all branches are told to commit. If any branch indicated when it was prepared that it was not able to commit, all branches are told to roll back.

In some cases, a global transaction might use one-phase commit (1PC). For example, when a Transaction Manager finds that a global transaction consists of only one transactional resource (that is, a single branch), that resource can be told to prepare and commit at the same time.

#### 13.3.7.1 XA Transaction SQL Statements

To perform XA transactions in MySQL, use the following statements:

```
XA {START|BEGIN} xid [JOIN|RESUME]
```

XA Transactions

```
XA END xid [SUSPEND [FOR MIGRATE]]
XA PREPARE xid
XA COMMIT xid [ONE PHASE]
XA ROLLBACK xid
XA RECOVER
```

For `XA START`, the `JOIN` and `RESUME` clauses are recognized but have no effect.

For `XA END` the `SUSPEND [FOR MIGRATE]` clause is recognized but has no effect.

Each XA statement begins with the `XA` keyword, and most of them require an `xid` value. An `xid` is an XA transaction identifier. It indicates which transaction the statement applies to. `xid` values are supplied by the client, or generated by the MySQL server. An `xid` value has from one to three parts:

```
xid: gtrid [, bqual [, formatID ]]
```

`gtrid` is a global transaction identifier, `bqual` is a branch qualifier, and `formatID` is a number that identifies the format used by the `gtrid` and `bqual` values. As indicated by the syntax, `bqual` and`formatID` are optional. The default `bqual` value is `''` if not given. The default `formatID` value is 1 if not given.

`gtrid` and `bqual` must be string literals, each up to 64 bytes (not characters) long. `gtrid` and `bqual` can be specified in several ways. You can use a quoted string (`'ab'`), hex string (`X'6162'`, `0x6162`), or bit value (`b'nnnn'`).

`formatID` is an unsigned integer.

The `gtrid` and `bqual` values are interpreted in bytes by the MySQL server's underlying XA support routines. However, while an SQL statement containing an XA statement is being parsed, the server works with some specific character set. To be safe, write `gtrid` and `bqual` as hex strings.

`xid` values typically are generated by the Transaction Manager. Values generated by one TM must be different from values generated by other TMs. A given TM must be able to recognize its own `xid` values in a list of values returned by the `XA RECOVER` statement.

`XA START xid` starts an XA transaction with the given `xid` value. Each XA transaction must have a unique `xid` value, so the value must not currently be used by another XA transaction. Uniqueness is assessed using the `gtrid` and `bqual` values. All following XA statements for the XA transaction must be specified using the same `xid` value as that given in the `XA START` statement. If you use any of those statements but specify an `xid` value that does not correspond to some existing XA transaction, an error occurs.

One or more XA transactions can be part of the same global transaction. All XA transactions within a given global transaction must use the same `gtrid` value in the `xid` value. For this reason, `gtrid` values must be globally unique so that there is no ambiguity about which global transaction a given XA transaction is part of. The `bqual` part of the `xid` value must be different for each XA transaction within a global transaction. (The requirement that `bqual` values be different is a limitation of the current MySQL XA implementation. It is not part of the XA specification.)The `XA RECOVER` statement returns information for those XA transactions on the MySQL server that are in the `PREPARED` state. (See Section 13.3.7.2, “XA Transaction States”.) The output includes a row for each such XA transaction on the server, regardless of which client started it.

`XA RECOVER` output rows look like this (for an example `xid` value consisting of the parts `'abc'`, `'def'`,and 7):XA Transactions

```
mysql> XA RECOVER;
+----------+--------------+--------------+--------+
| formatID | gtrid_length | bqual_length | data   |
+----------+--------------+--------------+--------+
|        7 |            3 |            3 | abcdef |
+----------+--------------+--------------+--------+
```

The output columns have the following meanings:

- `formatID` is the `formatID` part of the transaction `xid`
- `gtrid_length` is the length in bytes of the `gtrid` part of the `xid`
- `bqual_length` is the length in bytes of the `bqual` part of the `xid`
- `data` is the concatenation of the `gtrid` and `bqual` parts of the `xid`

#### 13.3.7.2 XA Transaction States

An XA transaction progresses through the following states:

1. Use `XA START` to start an XA transaction and put it in the `ACTIVE` state.
2. For an `ACTIVE` XA transaction, issue the SQL statements that make up the transaction, and then issue

an `XA END` statement. `XA END` puts the transaction in the `IDLE` state.

3. For an `IDLE` XA transaction, you can issue either an `XA PREPARE` statement or an `XA COMMIT ...`

`ONE PHASE` statement:

- `XA PREPARE` puts the transaction in the `PREPARED` state. An `XA RECOVER` statement at this point

includes the transaction's `xid` value in its output, because `XA RECOVER` lists all XA transactions that are in the `PREPARED` state.

- `XA COMMIT ... ONE PHASE` prepares and commits the transaction. The `xid` value is not listed by

`XA RECOVER` because the transaction terminates.

4. For a `PREPARED` XA transaction, you can issue an `XA COMMIT` statement to commit and terminate the

transaction, or `XA ROLLBACK` to roll back and terminate the transaction.

Here is a simple XA transaction that inserts a row into a table as part of a global transaction:

```
mysql> XA START 'xatest';
Query OK, 0 rows affected (0.00 sec)
mysql> INSERT INTO mytable (i) VALUES(10);
Query OK, 1 row affected (0.04 sec)
mysql> XA END 'xatest';
Query OK, 0 rows affected (0.00 sec)
mysql> XA PREPARE 'xatest';
Query OK, 0 rows affected (0.00 sec)
mysql> XA COMMIT 'xatest';
Query OK, 0 rows affected (0.00 sec)
```

Within the context of a given client connection, XA transactions and local (non-XA) transactions are mutually exclusive. For example, if `XA START` has been issued to begin an XA transaction, a local transaction cannot be started until the XA transaction has been committed or rolled back. Conversely, if a local transaction has been started with `START TRANSACTION`, no XA statements can be used until the transaction has been committed or rolled back.

Replication Statements If an XA transaction is in the `ACTIVE` state, you cannot issue any statements that cause an implicit commit.

That would violate the XA contract because you could not roll back the XA transaction. You receive the following error if you try to execute such a statement:

```
ERROR 1399 (XAE07): XAER_RMFAIL: The command cannot be executed
when global transaction is in the ACTIVE state
```

Statements to which the preceding remark applies are listed at Section 13.3.3, “Statements That Cause an Implicit Commit”.

#### 13.3.7.3 Restrictions on XA Transactions

XA transaction support is limited to the `InnoDB` storage engine.

For “external XA,” a MySQL server acts as a Resource Manager and client programs act as Transaction Managers. For “Internal XA”, storage engines within a MySQL server act as RMs, and the server itself acts as a TM. Internal XA support is limited by the capabilities of individual storage engines. Internal XA is required for handling XA transactions that involve more than one storage engine. The implementation of internal XA requires that a storage engine support two-phase commit at the table handler level, and currently this is true only for `InnoDB`.

For `XA START`, the `JOIN` and `RESUME` clauses are recognized but have no effect.

For `XA END` the `SUSPEND [FOR MIGRATE]` clause is recognized but has no effect.

The requirement that the `bqual` part of the `xid` value be different for each XA transaction within a global transaction is a limitation of the current MySQL XA implementation. It is not part of the XA specification.

If an XA transaction has reached the `PREPARED` state and the MySQL server is killed (for example, with`kill -9` on Unix) or shuts down abnormally, the transaction can be continued after the server restarts.

However, if the client reconnects and commits the transaction, the transaction is absent from the binary log even though it has been committed. This means the data and the binary log have gone out of synchrony.

An implication is that XA cannot be used safely together with replication.

It is possible that the server rolls back a pending XA transaction, even one that has reached the `PREPARED`state. This happens if a client connection terminates and the server continues to run, or if clients are connected and the server shuts down gracefully. (In the latter case, the server marks each connection to be terminated, and then rolls back the `PREPARED` XA transaction associated with it.) It should be possible to commit or roll back a `PREPARED` XA transaction, but this cannot be done without changes to the binary logging mechanism.

`FLUSH TABLES WITH READ LOCK` is not compatible with XA transactions.

## 13.4 Replication Statements

Replication can be controlled through the SQL interface using the statements described in this section.

One group of statements controls replication source servers, the other controls replicas.

### 13.4.1 SQL Statements for Controlling Replication Source Servers

This section discusses statements for managing replication source servers. Section 13.4.2, “SQL Statements for Controlling Replica Servers”, discusses statements for managing replica servers.

In addition to the statements described here, the following `SHOW` statements are used with replication source servers. For information about these statements, see Section 13.7.5, “SHOW Statements”.

```
- SHOW BINARY LOGS
```

SQL Statements for Controlling Replication Source Servers

```
- SHOW BINLOG EVENTS
- SHOW MASTER STATUS
- SHOW SLAVE HOSTS
```

#### 13.4.1.1 PURGE BINARY LOGS Statement

```
PURGE { BINARY | MASTER } LOGS {
TO 'log_name'
| BEFORE datetime_expr
}
```

The binary log is a set of files that contain information about data modifications made by the MySQL server. The log consists of a set of binary log files, plus an index file (see Section 5.4.4, “The Binary Log”).

The `PURGE BINARY LOGS` statement deletes all the binary log files listed in the log index file prior to the specified log file name or date. `BINARY` and `MASTER` are synonyms. Deleted log files also are removed from the list recorded in the index file, so that the given log file becomes the first in the list.

This statement has no effect if the server was not started with the `--log-bin` option to enable binary logging.

Examples:

```
PURGE BINARY LOGS TO 'mysql-bin.010';
PURGE BINARY LOGS BEFORE '2019-04-02 22:46:26';
```

The `BEFORE` variant's `datetime_expr` argument should evaluate to a `DATETIME` value (a value in`'YYYY-MM-DD hh:mm:ss'` format).

This statement is safe to run while replicas are replicating. You need not stop them. If you have an active replica that currently is reading one of the log files you are trying to delete, this statement does not delete the log file that is in use or any log files later than that one, but it deletes any earlier log files. In MySQL

5.6.12 and later, a warning message is issued in this situation. (Bug #13727933) However, if a replica is not connected and you happen to purge one of the log files it has yet to read, the replica cannot replicate after it reconnects.

To safely purge binary log files, follow this procedure:

1. On each replica server, use `SHOW SLAVE STATUS` to check which log file it is reading.
2. Obtain a listing of the binary log files on the source with `SHOW BINARY LOGS`.
3. Determine the earliest log file among all the replicas. This is the target file. If all the replicas are up to

date, this is the last log file on the list.

4. Make a backup of all the log files you are about to delete. (This step is optional, but always advisable.)
5. Purge all log files up to but not including the target file.

You can also set the `expire_logs_days` system variable to expire binary log files automatically after a given number of days (see Section 5.1.7, “Server System Variables”). If you are using replication, you should set the variable no lower than the maximum number of days your replicas might lag behind the source.

`PURGE BINARY LOGS TO` and `PURGE BINARY LOGS BEFORE` both fail with an error when binary log files listed in the `.index` file had been removed from the system by some other means (such as using SQL Statements for Controlling Replication Source Servers`rm` on Linux). (Bug #18199, Bug #18453) To handle such errors, edit the `.index` file (which is a simple text file) manually to ensure that it lists only the binary log files that are actually present, then run again the`PURGE BINARY LOGS` statement that failed.

#### 13.4.1.2 RESET MASTER Statement

```
RESET MASTER
```

Deletes all binary log files listed in the index file, resets the binary log index file to be empty, and creates a new binary log file.

`RESET MASTER` also clears the values of the `gtid_purged` system variable as well as the global value of the `gtid_executed` system variable (but not its session value); that is, executing this statement sets each of these values to an empty string (`''`).

This statement is intended to be used only when the source is started for the first time.

Important The effects of `RESET MASTER` differ from those of `PURGE BINARY LOGS` in 2 key ways:

1. `RESET MASTER` removes all binary log files that are listed in the index file,

leaving only a single, empty binary log file with a numeric suffix of `.000001`,whereas the numbering is not reset by `PURGE BINARY LOGS`.

2. `RESET MASTER` is not intended to be used while any replicas are running. The

behavior of `RESET MASTER` when used while replicas are running is undefined(and thus unsupported), whereas `PURGE BINARY LOGS` may be safely used while replicas are running.

See also Section 13.4.1.1, “PURGE BINARY LOGS Statement”.

`RESET MASTER` can prove useful when you first set up the source and the replica, so that you can verify the setup as follows:

1. Start the source and replica, and start replication (see Section 17.1.1, “How to Set Up Replication”).
2. Execute a few test queries on the source.
3. Check that the queries were replicated to the replica.
4. When replication is running correctly, issue `STOP SLAVE` followed by `RESET SLAVE` on the replica,

then verify that any unwanted data no longer exists on the replica.

5. Issue `RESET MASTER` on the source to clean up the test queries.

After verifying the setup and getting rid of any unwanted and log files generated by testing, you can start the replica and begin replicating.

#### 13.4.1.3 SET sql_log_bin Statement

```
SET sql_log_bin = {OFF|ON}
```

The `sql_log_bin` variable controls whether logging to the binary log is enabled for the current session(assuming that the binary log itself is enabled). The default value is `ON`. To disable or enable binary logging for the current session, set the session `sql_log_bin` variable to `OFF` or `ON`.

SQL Statements for Controlling Replica Servers Set this variable to `OFF` for a session to temporarily disable binary logging while making changes to the source you do not want replicated to the replica.

Setting the session value of this system variable is a restricted operation. The session user must have privileges sufficient to set restricted session variables. See Section 5.1.8.1, “System Variable Privileges”.

It is not possible to set the session value of `sql_log_bin` within a transaction or subquery.

Setting this variable to `OFF` prevents GTIDs from being assigned to transactions in the binary log. If you are using GTIDs for replication, this means that, even when binary logging is later enabled once again, the GTIDs written into the log from this point do not account for any transactions that occurred in the meantime—in effect, those transactions are lost.

As of MySQL 5.6.22, the global `sql_log_bin` variable is read only and cannot be modified. The global scope is deprecated; expect it to be removed in a future MySQL release. Prior to 5.6.22, `sql_log_bin`can be set as a global or session variable. Setting `sql_log_bin` globally is only detected when a new session is started. Any sessions previously running are not impacted when setting `sql_log_bin` globally.

Warning Incorrect use of `sql_log_bin` with a global scope means any changes made in an already running session are still being recorded to the binary log and therefore replicated. Exercise extreme caution using `sql_log_bin` with a global scope as the above situation could cause unexpected results including replication failure.

### 13.4.2 SQL Statements for Controlling Replica Servers

This section discusses statements for managing replica servers. Section 13.4.1, “SQL Statements for Controlling Replication Source Servers”, discusses statements for managing source servers.

In addition to the statements described here, `SHOW SLAVE STATUS` and `SHOW RELAYLOG EVENTS` are also used with replicas. For information about these statements, see Section 13.7.5.35, “SHOW SLAVE STATUS Statement”, and Section 13.7.5.33, “SHOW RELAYLOG EVENTS Statement”.

#### 13.4.2.1 CHANGE MASTER TO Statement

```
CHANGE MASTER TO option [, option] ...
option: {
MASTER_BIND = 'interface_name'
| MASTER_HOST = 'host_name'
| MASTER_USER = 'user_name'
| MASTER_PASSWORD = 'password'
| MASTER_PORT = port_num
| MASTER_CONNECT_RETRY = interval
| MASTER_RETRY_COUNT = count
| MASTER_DELAY = interval
| MASTER_HEARTBEAT_PERIOD = interval
| MASTER_LOG_FILE = 'source_log_name'
| MASTER_LOG_POS = source_log_pos
| MASTER_AUTO_POSITION = {0|1}
| RELAY_LOG_FILE = 'relay_log_name'
| RELAY_LOG_POS = relay_log_pos
| MASTER_SSL = {0|1}
| MASTER_SSL_CA = 'ca_file_name'
| MASTER_SSL_CAPATH = 'ca_directory_name'
| MASTER_SSL_CERT = 'cert_file_name'
| MASTER_SSL_CRL = 'crl_file_name'
| MASTER_SSL_CRLPATH = 'crl_directory_name'
| MASTER_SSL_KEY = 'key_file_name'
| MASTER_SSL_CIPHER = 'cipher_list'
```

SQL Statements for Controlling Replica Servers

```
| MASTER_SSL_VERIFY_SERVER_CERT = {0|1}
| IGNORE_SERVER_IDS = (server_id_list)
}
server_id_list:
[server_id [, server_id] ... ]
```

`CHANGE MASTER TO` changes the parameters that the replica uses for connecting to the replication source server, for reading the source's binary log, and reading the replica's relay log. It also updates the contents of the replication metadata repositories (see Section 17.2.2, “Relay Log and Replication Metadata Repositories”). `CHANGE MASTER TO` requires the `SUPER` privilege.

To use `CHANGE MASTER TO`, the replication threads must be stopped (use `STOP SLAVE` if necessary). In MySQL 5.6.11 and later, `gtid_next` must also be set to `AUTOMATIC` (Bug #16062608).

Options not specified retain their value, except as indicated in the following discussion. Thus, in most cases, there is no need to specify options that do not change. For example, if the password to connect to your MySQL source has changed, issue these statements to tell the replica about the new password:

```
STOP SLAVE; -- if replication was running
CHANGE MASTER TO MASTER_PASSWORD='new3cret';
START SLAVE; -- if you want to restart replication
```

`MASTER_HOST`, `MASTER_USER`, `MASTER_PASSWORD`, and `MASTER_PORT` provide information to the replica about how to connect to its source:

- `MASTER_HOST` and `MASTER_PORT` are the host name (or IP address) of the source host and its TCP/IP

port.

Note Replication cannot use Unix socket files. You must be able to connect to the source MySQL server using TCP/IP.

If you specify the `MASTER_HOST` or `MASTER_PORT` option, the replica assumes that the source server is different from before (even if the option value is the same as its current value). In this case, the old values for the source's binary log file name and position are considered no longer applicable, so if you do not specify `MASTER_LOG_FILE` and `MASTER_LOG_POS` in the statement, `MASTER_LOG_FILE=''` and`MASTER_LOG_POS=4` are silently appended to it.

Setting `MASTER_HOST=''` (that is, setting its value explicitly to an empty string) is not the same as not setting `MASTER_HOST` at all. Beginning with MySQL 5.5, trying to set `MASTER_HOST` to an empty string fails with an error. Previously, setting `MASTER_HOST` to an empty string caused `START SLAVE`subsequently to fail. (Bug #28796)In MySQL 5.6.5 and later, values used for `MASTER_HOST` and other `CHANGE MASTER TO` options are checked for linefeed (`\n` or `0x0A`) characters; the presence of such characters in these values causes the statement to fail with `ER_MASTER_INFO`. (Bug #11758581, Bug #50801)

- `MASTER_USER` and `MASTER_PASSWORD` are the user name and password of the account to use for

connecting to the source. If you specify `MASTER_PASSWORD`, `MASTER_USER` is also required. The password used for a replication user account in a `CHANGE MASTER TO` statement is limited to 32 characters in length; if the password is longer, the statement succeeds, but any excess characters are silently truncated. This is an issue specific to MySQL Replication, which is fixed in MySQL 5.7. (Bug#11752299, Bug #43439)It is possible to set an empty user name by specifying `MASTER_USER=''`, but the replication channel cannot be started with an empty user name. Only set an empty `MASTER_USER` user name if you need to SQL Statements for Controlling Replica Servers clear previously used credentials from the replica's repositories for security purposes, and do not attempt to use the channel afterwards. (Bug #13427949)The text of a running `CHANGE MASTER TO` statement, including values for `MASTER_USER` and`MASTER_PASSWORD`, can be seen in the output of a concurrent `SHOW PROCESSLIST` statement. (The complete text of a `START SLAVE` statement is also visible to `SHOW PROCESSLIST`.)The `MASTER_SSL_xxx` options provide information about using SSL for the connection. They correspond to the `--ssl-xxx` options described in Command Options for Encrypted Connections, and Section 17.3.8,“Setting Up Replication to Use Encrypted Connections”. These options can be changed even on replicas that are compiled without SSL support. They are saved to the connection metadata repository, but are ignored if the replica does not have SSL support enabled. `MASTER_SSL_CRL` and `MASTER_SSL_CRLPATH`were added in MySQL 5.6.3.

Important To help prevent sophisticated man-in-the-middle attacks, it is important for the replica to verify the server’s identity. With the additional `MASTER_SSL_xxx` settings,the replica checks that the server’s certificate is valid. To implement this level of verification, you must first ensure that the CA certificate for the server is reliably available to the replica, otherwise availability issues will result.

`MASTER_CONNECT_RETRY` specifies how many seconds to wait between connect retries. The default is 60.

`MASTER_RETRY_COUNT`, added in MySQL 5.6.1, limits the number of reconnection attempts and updates the value of the `Master_Retry_Count` column in the output of `SHOW SLAVE STATUS` (also added in MySQL 5.6.1). The default value is 24 * 3600 = 86400. `MASTER_RETRY_COUNT` is intended to replace the older `--master-retry-count` server option, and is now the preferred method for setting this limit.

You are encouraged not to rely on `--master-retry-count` in new applications and, when upgrading to MySQL 5.6.1 or later from earlier versions of MySQL, to update any existing applications that rely on it, so that they use `CHANGE MASTER TO ... MASTER_RETRY_COUNT` instead.

`MASTER_DELAY` specifies how many seconds behind the source the replica must lag. An event received from the source is not executed until at least `interval` seconds later than its execution on the source.

The default is 0. An error occurs if `interval` is not a nonnegative integer in the range from 0 to 231−1. For more information, see Section 17.3.10, “Delayed Replication”. This option was added in MySQL 5.6.0.

`MASTER_BIND` is for use on replicas having multiple network interfaces, and determines which of the replica's network interfaces is chosen for connecting to the source.

The address configured with this option, if any, can be seen in the `Master_Bind` column of the output from `SHOW SLAVE STATUS`. If you are using tables for the replication metadata repositories (the server was started with `master_info_repository=TABLE`), the value can also be seen as the `Master_bind`column of the `mysql.slave_master_info` table.

The ability to bind a replica to a specific network interface was added in MySQL 5.6.2. This is also supported in MySQL NDB Cluster 7.3 and later.

`MASTER_HEARTBEAT_PERIOD` sets the interval in seconds between replication heartbeats. Whenever the source's binary log is updated with an event, the waiting period for the next heartbeat is reset. `interval`is a decimal value having the range 0 to 4294967 seconds and a resolution in milliseconds; the smallest nonzero value is 0.001. Heartbeats are sent by the source only if there are no unsent events in the binary log file for a period longer than `interval`.

If you are logging source connection information to tables, `MASTER_HEARTBEAT_PERIOD` can be seen as the value of the `Heartbeat` column of the `mysql.slave_master_info` table.

SQL Statements for Controlling Replica Servers Setting `interval` to 0 disables heartbeats altogether. The default value for `interval` is equal to the value of `slave_net_timeout` divided by 2.

Setting `@@GLOBAL.slave_net_timeout` to a value less than that of the current heartbeat interval results in a warning being issued. The effect of issuing `RESET SLAVE` on the heartbeat interval is to reset it to the default value.

`MASTER_LOG_FILE` and `MASTER_LOG_POS` are the coordinates at which the replication I/O thread should begin reading from the source the next time the thread starts. `RELAY_LOG_FILE` and `RELAY_LOG_POS`are the coordinates at which the replication SQL thread should begin reading from the relay log the next time the thread starts. If you specify either of `MASTER_LOG_FILE` or `MASTER_LOG_POS`, you cannot specify `RELAY_LOG_FILE` or `RELAY_LOG_POS`. In MySQL 5.6.5 and later, if you specify either of `MASTER_LOG_FILE` or `MASTER_LOG_POS`, you also cannot specify `MASTER_AUTO_POSITION =`1 (described later in this section). If neither of `MASTER_LOG_FILE` or `MASTER_LOG_POS` is specified,the replica uses the last coordinates of the replication SQL thread before `CHANGE MASTER TO` was issued. This ensures that there is no discontinuity in replication, even if the replication SQL thread was late compared to the replication I/O thread, when you merely want to change, say, the password to use.

`MASTER_AUTO_POSITION` was added in MySQL 5.6.5. If `MASTER_AUTO_POSITION = 1` is used with`CHANGE MASTER TO`, the replica attempts to connect to the source using the GTID-based replication protocol.

When using GTIDs, the replica tells the source which transactions it has already received, executed,or both. To compute this set, it reads the global value of `gtid_executed` and the value of the`Retrieved_gtid_set` column from `SHOW SLAVE STATUS`. Since the GTID of the last transmitted transaction is included in `Retrieved_gtid_set` even if the transaction was only partially transmitted, the last received GTID is subtracted from this set. Thus, the replica computes the following set:

```
UNION(@@GLOBAL.gtid_executed, Retrieved_gtid_set - last_received_GTID)
```

This set is sent to the source as part of the initial handshake, and the source sends back all transactions that it has executed which are not part of the set. If any of these transactions have been already purged from the source's binary log, the source sends the error `ER_MASTER_HAS_PURGED_REQUIRED_GTIDS` to the replica, and replication does not start.

When GTID-based replication is employed, the coordinates represented by `MASTER_LOG_FILE` and`MASTER_LOG_POS` are not used, and global transaction identifiers are used instead. Thus the use of either or both of these options together with `MASTER_AUTO_POSITION` causes an error.

Beginning with MySQL 5.6.10, you can see whether replication is running with autopositioning enabled by checking the output of `SHOW SLAVE STATUS`. (Bug #15992220)`gtid_mode` must also be enabled before issuing `CHANGE MASTER TO ... MASTER_AUTO_POSITION``= 1`. Otherwise, the statement fails with an error.

To revert to the older file-based replication protocol after using GTIDs, you can issue a new `CHANGE``MASTER TO` statement that specifies `MASTER_AUTO_POSITION = 0`, as well as at least one of

```
MASTER_LOG_FILE or MASTER_LOG_POS.
```

`CHANGE MASTER TO` deletes all relay log files and starts a new one, unless you specify`RELAY_LOG_FILE` or `RELAY_LOG_POS`. In that case, relay log files are kept; the `relay_log_purge`global variable is set silently to 0.

Prior to MySQL 5.6.2, `RELAY_LOG_FILE` required an absolute path. Beginning with MySQL 5.6.2, the path can be relative, in which case it is assumed to be relative to the replica's data directory. (Bug #12190)SQL Statements for Controlling Replica Servers`IGNORE_SERVER_IDS` takes a comma-separated list of 0 or more server IDs. Events originating from the corresponding servers are ignored, with the exception of log rotation and deletion events, which are still recorded in the relay log.

In circular replication, the originating server normally acts as the terminator of its own events, so that they are not applied more than once. Thus, this option is useful in circular replication when one of the servers in the circle is removed. Suppose that you have a circular replication setup with 4 servers, having server IDs 1, 2, 3, and 4, and server 3 fails. When bridging the gap by starting replication from server 2 to server 4, you can include `IGNORE_SERVER_IDS = (3)` in the `CHANGE MASTER TO` statement that you issue on server 4 to tell it to use server 2 as its source instead of server 3. Doing so causes it to ignore and not to propagate any statements that originated with the server that is no longer in use.

When a `CHANGE MASTER TO` statement is issued without any `IGNORE_SERVER_IDS` option, any existing list is preserved. To clear the list of ignored servers, it is necessary to use the option with an empty list:

```
CHANGE MASTER TO IGNORE_SERVER_IDS = ();
```

`RESET SLAVE ALL` has no effect on the server ID list. This issue is fixed in MySQL 5.7. (Bug #18816897)If `IGNORE_SERVER_IDS` contains the server's own ID and the server was started with the `--replicate-``same-server-id` option enabled, an error results.

In MySQL 5.6, the connection metadata repository and the output of `SHOW SLAVE STATUS` provide the list of servers that are currently ignored. For more information, see Section 17.2.2.2, “Replication Metadata Repositories”, and Section 13.7.5.35, “SHOW SLAVE STATUS Statement”.

In MySQL 5.6, invoking `CHANGE MASTER TO` causes the previous values for `MASTER_HOST`,`MASTER_PORT`, `MASTER_LOG_FILE`, and `MASTER_LOG_POS` to be written to the error log, along with other information about the replica's state prior to execution.

In MySQL 5.6.7 and later, `CHANGE MASTER TO` causes an implicit commit of an ongoing transaction. See Section 13.3.3, “Statements That Cause an Implicit Commit”.

`CHANGE MASTER TO` is useful for setting up a replica when you have the snapshot of the source and have recorded the source binary log coordinates corresponding to the time of the snapshot. After loading the snapshot into the replica to synchronize it with the source, you can run `CHANGE MASTER``TO MASTER_LOG_FILE='log_name', MASTER_LOG_POS=log_pos` on the replica to specify the coordinates at which the replica should begin reading the source's binary log.

The following example changes the source server the replica uses and establishes the source's binary log coordinates from which the replica begins reading. This is used when you want to set up the replica to replicate the source:

```
CHANGE MASTER TO
MASTER_HOST='source2.example.com',
MASTER_USER='replication',
MASTER_PASSWORD='bigs3cret',
MASTER_PORT=3306,
MASTER_LOG_FILE='source2-bin.001',
MASTER_LOG_POS=4,
MASTER_CONNECT_RETRY=10;
```

The next example shows an operation that is less frequently employed. It is used when the replica has relay log files that you want it to execute again for some reason. To do this, the source need not be reachable. You need only use `CHANGE MASTER TO` and start the SQL thread (`START SLAVE`

```
SQL_THREAD):
CHANGE MASTER TO
RELAY_LOG_FILE='replica-relay-bin.006',
```

SQL Statements for Controlling Replica Servers

```
RELAY_LOG_POS=4025;
```

The following table shows the maximum permissible length for the string-valued options.

> Option Maximum Length

```
MASTER_HOST  60
MASTER_USER  16
MASTER_PASSWORD  32
MASTER_LOG_FILE  255
RELAY_LOG_FILE  255
MASTER_SSL_CA  255
MASTER_SSL_CAPATH  255
MASTER_SSL_CERT  255
MASTER_SSL_CRL  255
MASTER_SSL_CRLPATH  255
MASTER_SSL_KEY  255
MASTER_SSL_CIPHER  511
```

#### 13.4.2.2 MASTER_POS_WAIT() Statement

```
SELECT MASTER_POS_WAIT('source_log_file', source_log_pos [, timeout])
```

This is actually a function, not a statement. It is used to ensure that the replica has read and executed events up to a given position in the source's binary log. See Section 12.20, “Miscellaneous Functions”, for a full description.

#### 13.4.2.3 RESET SLAVE Statement

```
RESET SLAVE [ALL]
```

`RESET SLAVE` makes the replica forget its replication position in the source's binary log. This statement is meant to be used for a clean start: It clears the replication metadata repositories, deletes all the relay log files, and starts a new relay log file. It also resets to 0 the replication delay specified with the `MASTER_DELAY` option to `CHANGE MASTER TO`. `RESET SLAVE` does not change the values of`gtid_executed` or `gtid_purged`. To use `RESET SLAVE`, the replication threads must be stopped, so on a running replica use `STOP SLAVE` before issuing `RESET SLAVE`.

Note All relay log files are deleted, even if they have not been completely executed by the replication SQL thread. (This is a condition likely to exist on a replica if you have issued a `STOP SLAVE` statement or if the replica is highly loaded.)In MySQL 5.6 (unlike the case in MySQL 5.1 and earlier), `RESET SLAVE` does not change any replication connection parameters such as the source's host name and port or the replication user account name and password, which are retained in memory. This means that `START SLAVE` can be issued without requiring a`CHANGE MASTER TO` statement following `RESET SLAVE`.

Connection parameters are reset if the replica `mysqld` is shut down following `RESET SLAVE`. In MySQL

5.6.3 and later, you can instead use `RESET SLAVE ALL` to reset these connection parameters (Bug#11809016).

SQL Statements for Controlling Replica Servers`RESET SLAVE ALL` does not clear the `IGNORE_SERVER_IDS` list set by `CHANGE MASTER TO`. This issue is fixed in MySQL 5.7. (Bug #18816897)In MySQL 5.6.7 and later, `RESET SLAVE` causes an implicit commit of an ongoing transaction. See Section 13.3.3, “Statements That Cause an Implicit Commit”.

If the replication SQL thread was in the middle of replicating temporary tables when it was stopped, and`RESET SLAVE` is issued, these replicated temporary tables are deleted on the replica.

Note When used on an NDB Cluster replica SQL node, `RESET SLAVE` clears the`mysql.ndb_apply_status` table. You should keep in mind when using this statement that `ndb_apply_status` uses the `NDB` storage engine and so is shared by all SQL nodes attached to the replica cluster.

Beginning with MySQL NDB Cluster 7.4.9, you can override this behavior by issuing`SET` `GLOBAL @@ndb_clear_apply_status=OFF` prior to executing `RESET``SLAVE`, which keeps the replica from purging the `ndb_apply_status` table in such cases.

#### 13.4.2.4 SET GLOBAL sql_slave_skip_counter Statement

```
SET GLOBAL sql_slave_skip_counter = N
```

This statement skips the next N events from the source. This is useful for recovering from replication stops caused by a statement.

This statement is valid only when the replication threads are not running. Otherwise, it produces an error.

When using this statement, it is important to understand that the binary log is actually organized as a sequence of groups known as event groups. Each event group consists of a sequence of events.

- For transactional tables, an event group corresponds to a transaction.
- For nontransactional tables, an event group corresponds to a single SQL statement.

Note A single transaction can contain changes to both transactional and nontransactional tables.

When you use `SET GLOBAL sql_slave_skip_counter` to skip events and the result is in the middle of a group, the replica continues to skip events until it reaches the end of the group. Execution then starts with the next event group.

#### 13.4.2.5 START SLAVE Statement

```
START SLAVE [thread_types] [until_option] [connection_options]
thread_types:
[thread_type [, thread_type] ... ]
thread_type:
IO_THREAD | SQL_THREAD
until_option:
UNTIL {   {SQL_BEFORE_GTIDS | SQL_AFTER_GTIDS} = gtid_set
```

SQL Statements for Controlling Replica Servers

```
|   MASTER_LOG_FILE = 'log_name', MASTER_LOG_POS = log_pos
|   RELAY_LOG_FILE = 'log_name', RELAY_LOG_POS = log_pos
|   SQL_AFTER_MTS_GAPS  }
connection_options:
[USER='user_name'] [PASSWORD='user_pass'] [DEFAULT_AUTH='plugin_name'] [PLUGIN_DIR='plugin_dir']
gtid_set:
uuid_set [, uuid_set] ...
| ''
uuid_set:
uuid:interval[:interval]...
uuid:
hhhhhhhh-hhhh-hhhh-hhhh-hhhhhhhhhhhh
h:
[0-9,A-F]
interval:
n[-n]
(n >= 1)
```

`START SLAVE` with no `thread_type` options starts both of the replication threads. The I/O thread reads events from the replication source server and stores them in the relay log. The SQL thread reads events from the relay log and executes them. `START SLAVE` requires the `SUPER` privilege.

If `START SLAVE` succeeds in starting the replication threads, it returns without any error. However, even in that case, it might be that the replication threads start and then later stop (for example, because they do not manage to connect to the source or read its binary log, or some other problem). `START SLAVE`does not warn you about this. You must check the replica's error log for error messages generated by the replication threads, or check that they are running satisfactorily with `SHOW SLAVE STATUS`.

`START SLAVE` causes an implicit commit of an ongoing transaction. See Section 13.3.3, “Statements That Cause an Implicit Commit”.

Beginning with MySQL 5.6.11, `gtid_next` must be set to `AUTOMATIC` before issuing this statement (Bug#16062608).

`START SLAVE` supports pluggable user-password authentication with the `USER`, `PASSWORD`,`DEFAULT_AUTH` and `PLUGIN_DIR` options, as described in the following list:

- `USER`: User name. Cannot be set to an empty or null string, or left unset if `PASSWORD` is used.
- `PASSWORD`: Password.
- `DEFAULT_AUTH`: Name of plugin; default is MySQL native authentication.
- `PLUGIN_DIR`: Location of plugin.

You cannot use the `SQL_THREAD` option when specifying any of `USER`, `PASSWORD`, `DEFAULT_AUTH`, or`PLUGIN_DIR`, unless the `IO_THREAD` option is also provided.

For more information, see Section 6.2.11, “Pluggable Authentication”.

If an insecure connection is used with any these options, the server issues the warning `Sending`

```
passwords in plain text without SSL/TLS is extremely insecure.
```

SQL Statements for Controlling Replica Servers`START SLAVE ... UNTIL` supports two additional options for use with global transaction identifiers(GTIDs) (see Section 17.1.3, “Replication with Global Transaction Identifiers”). Each of these takes a set of one or more global transaction identifiers `gtid_set` as an argument (see GTID Sets, for more information).

When no `thread_type` is specified, `START SLAVE UNTIL SQL_BEFORE_GTIDS` causes the replication SQL thread to process transactions until it has reached the first transaction whose GTID is listed in the`gtid_set`. `START SLAVE UNTIL SQL_AFTER_GTIDS` causes the replication threads to process all transactions until the `last` transaction in the `gtid_set` has been processed by both threads. In other words, `START SLAVE UNTIL SQL_BEFORE_GTIDS` causes the replication SQL thread to process all transactions occurring before the first GTID in the `gtid_set` is reached, and `START SLAVE UNTIL``SQL_AFTER_GTIDS` causes the replication threads to handle all transactions, including those whose GTIDs are found in `gtid_set`, until each has encountered a transaction whose GTID is not part of the set.

`SQL_BEFORE_GTIDS` and `SQL_AFTER_GTIDS` each support the `SQL_THREAD` and `IO_THREAD` options,although using `IO_THREAD` with them currently has no effect.

```
For example, START SLAVE SQL_THREAD UNTIL SQL_BEFORE_GTIDS =
```

`3E11FA47-71CA-11E1-9E33-C80AA9429562:11-56` causes the replication SQL thread to process all transactions originating from the source whose `server_uuid` is `3E11FA47-71CA-11E1-9E33-``C80AA9429562` until it encounters the transaction having sequence number 11; it then stops without processing this transaction. In other words, all transactions up to and including the transaction with sequence number 10 are processed. Executing `START SLAVE SQL_THREAD UNTIL`

```
SQL_AFTER_GTIDS = 3E11FA47-71CA-11E1-9E33-C80AA9429562:11-56, on the other hand,
```

would cause the replication SQL thread to obtain all transactions just mentioned from the source, including all of the transactions having the sequence numbers 11 through 56, and then to stop without processing any additional transactions; that is, the transaction having sequence number 56 would be the last transaction fetched by the replication SQL thread.

Prior to MySQL 5.6.14, `SQL_AFTER_GTIDS` did not stop the replica once the indicated transaction was completed, but waited until another GTID event was received (Bug #14767986).

Use the `START SLAVE UNTIL SQL_AFTER_MTS_GAPS` statement to cause a multithreaded replica's SQL threads to run until no more gaps are found in the relay log, and then to stop. This statement can take an `SQL_THREAD` option, but the effects of the statement remain unchanged. It has no effect on the replication I/O thread (and cannot be used with the `IO_THREAD` option). `START SLAVE UNTIL``SQL_AFTER_MTS_GAPS` should be used before switching the replica from multithreaded mode to single-threaded mode (that is, when resetting `slave_parallel_workers` back to 0 from a positive, nonzero value) after the replica has failed with errors in multithreaded mode.

To change a failed multithreaded replica to single-threaded mode, you can issue the following series of statements, in the order shown:

```
START SLAVE UNTIL SQL_AFTER_MTS_GAPS;
SET @@GLOBAL.slave_parallel_workers = 0;
START SLAVE SQL_THREAD;
```

If you were running the failed multithreaded replica with `relay_log_recovery` enabled, then you must issue `START SLAVE UNTIL SQL_AFTER_MTS_GAPS` prior to executing `CHANGE MASTER TO`. Otherwise the latter statement fails.

Note It is possible to view the entire text of a running `START SLAVE ...`statement, including any `USER` or `PASSWORD` values used, in the output of SQL Statements for Controlling Replica Servers`SHOW PROCESSLIST`. This is also true for the text of a running `CHANGE``MASTER TO` statement, including any values it employs for `MASTER_USER` or

```
MASTER_PASSWORD.
```

`START SLAVE` sends an acknowledgment to the user after both the I/O thread and the SQL thread have started. However, the I/O thread may not yet have connected. For this reason, a successful `START SLAVE`causes `SHOW SLAVE STATUS` to show `Slave_SQL_Running=Yes`, but this does not guarantee that`Slave_IO_Running=Yes` (because `Slave_IO_Running=Yes` only if the I/O thread is running and connected). For more information, see Section 13.7.5.35, “SHOW SLAVE STATUS Statement”, and Section 17.1.5.1, “Checking Replication Status”.

You can add `IO_THREAD` and `SQL_THREAD` options to the statement to name which of the threads to start. The `SQL_THREAD` option is disallowed when specifying any of `USER`, `PASSWORD`, `DEFAULT_AUTH`, or`PLUGIN_DIR`, unless the `IO_THREAD` option is also provided.

An `UNTIL` clause (`until_option`, in the preceding grammar) may be added to specify that the replica should start and run until the SQL thread reaches a given point in the source's binary log, specified by the`MASTER_LOG_POS` and `MASTER_LOG_FILE` options, or a given point in the replica's relay log, indicated with the `RELAY_LOG_POS` and `RELAY_LOG_FILE` options. When the SQL thread reaches the point specified, it stops. If the `SQL_THREAD` option is specified in the statement, it starts only the SQL thread.

Otherwise, it starts both replication threads. If the SQL thread is running, the `UNTIL` clause is ignored and a warning is issued. You cannot use an `UNTIL` clause with the `IO_THREAD` option.

It is also possible with `START SLAVE UNTIL` to specify a stop point relative to a given GTID or set of GTIDs using one of the options `SQL_BEFORE_GTIDS` or `SQL_AFTER_GTIDS`, as explained previously in this section. When using one of these options, you can specify `SQL_THREAD`, `IO_THREAD`, both of these,or neither of them. If you specify only `SQL_THREAD`, then only the replication SQL thread is affected by the statement; if only `IO_THREAD` is used, then only the replication I/O thread is affected. If both `SQL_THREAD`and `IO_THREAD` are used, or if neither of them is used, then both the replication threads are affected by the statement.

The `UNTIL` clause is not supported for multithreaded replicas except when also using

```
SQL_AFTER_MTS_GAPS.
```

For an `UNTIL` clause, you must specify any one of the following:

- Both a log file name and a position in that file
- Either of `SQL_BEFORE_GTIDS` or `SQL_AFTER_GTIDS`

```
- SQL_AFTER_MTS_GAPS
```

Do not mix binary log and relay log options. Do not mix log file options with GTID options.

Any `UNTIL` condition is reset by a subsequent `STOP SLAVE` statement, a `START SLAVE` statement that includes no `UNTIL` clause, or a server restart.

When specifying a log file and position, you can use the `IO_THREAD` option with `START SLAVE ...``UNTIL` even though only the SQL thread is affected by this statement. The `IO_THREAD` option is ignored in such cases. The preceding restriction does not apply when using one of the GTID options(`SQL_BEFORE_GTIDS` and `SQL_AFTER_GTIDS`); the GTID options support both `SQL_THREAD` and`IO_THREAD`, as explained previously in this section.

The `UNTIL` clause can be useful for debugging replication, or to cause replication to proceed until just before the point where you want to avoid having the replica replicate an event. For example, if an unwise`DROP TABLE` statement was executed on the source, you can use `UNTIL` to tell the replica to execute up Prepared Statements to that point but no farther. To find what the event is, use `mysqlbinlog` with the source's binary log or the replica's relay log, or by using a `SHOW BINLOG EVENTS` statement.

If you are using `UNTIL` to have the replica process replicated queries in sections, it is recommended that you start the replica with the `--skip-slave-start` option to prevent the SQL thread from running when the replica server starts. It is probably best to use this option in an option file rather than on the command line, so that an unexpected server restart does not cause it to be forgotten.

The `SHOW SLAVE STATUS` statement includes output fields that display the current values of the `UNTIL`condition.

#### 13.4.2.6 STOP SLAVE Statement

```
STOP SLAVE [thread_types]
thread_types:
[thread_type [, thread_type] ... ]
thread_type: IO_THREAD | SQL_THREAD
```

Stops the replication threads. `STOP SLAVE` requires the `SUPER` privilege. Recommended best practice is to execute `STOP SLAVE` on the replica before stopping the replica server (see Section 5.1.15, “The Server Shutdown Process”, for more information).

When using the row-based logging format: You should execute `STOP SLAVE` or `STOP SLAVE``SQL_THREAD` on the replica prior to shutting down the replica server if you are replicating any tables that use a nontransactional storage engine (see the Note later in this section).

Like `START SLAVE`, this statement may be used with the `IO_THREAD` and `SQL_THREAD` options to name the thread or threads to be stopped.

`STOP SLAVE` causes an implicit commit of an ongoing transaction. See Section 13.3.3, “Statements That Cause an Implicit Commit”.

Beginning with MySQL 5.6.11, `gtid_next` must be set to `AUTOMATIC` before issuing this statement (Bug#16062608).

In MySQL 5.6.13 and later, you can control how long `STOP SLAVE` waits before timing out by setting the `rpl_stop_slave_timeout` system variable. This can be used to avoid deadlocks between `STOP``SLAVE` and other SQL statements using different client connections to the replica. When the timeout value is reached, the issuing client returns an error message and stops waiting, but the `STOP SLAVE` instruction remains in effect. Once the replication threads are no longer busy, the `STOP SLAVE` statement is executed and the replica stops. (Bug #16856735)If the current replication event group has modified one or more nontransactional tables, `STOP SLAVE`waits for up to 60 seconds for the event group to complete, unless you issue a `KILL QUERY` or `KILL``CONNECTION` statement for the replication SQL thread. If the event group remains incomplete after the timeout, an error message is logged. (Bug #319, Bug #38205)In old versions of MySQL (before 4.0.5), this statement was called `SLAVE STOP`. That syntax is no longer accepted as of MySQL 5.6.1.

## 13.5 Prepared Statements

MySQL 5.6 provides support for server-side prepared statements. This support takes advantage of the efficient client/server binary protocol. Using prepared statements with placeholders for parameter values has the following benefits:Prepared Statements in Application Programs

- Less overhead for parsing the statement each time it is executed. Typically, database applications

process large volumes of almost-identical statements, with only changes to literal or variable values in clauses such as `WHERE` for queries and deletes, `SET` for updates, and `VALUES` for inserts.

- Protection against SQL injection attacks. The parameter values can contain unescaped SQL quote and

delimiter characters.

The following sections provide an overview of the characteristics of prepared statements:

- Prepared Statements in Application Programs
- Prepared Statements in SQL Scripts
- PREPARE, EXECUTE, and DEALLOCATE PREPARE Statements
- SQL Syntax Permitted in Prepared Statements

> Prepared Statements in Application Programs

You can use server-side prepared statements through client programming interfaces, including the MySQL C API client library for C programs, MySQL Connector/J for Java programs, and MySQL Connector/NET for programs using .NET technologies. For example, the C API provides a set of function calls that make up its prepared statement API. See C API Prepared Statement Interface. Other language interfaces can provide support for prepared statements that use the binary protocol by linking in the C client library, one example being the `mysqli` extension, available in PHP 5.0 and higher.

> Prepared Statements in SQL Scripts

An alternative SQL interface to prepared statements is available. This interface is not as efficient as using the binary protocol through a prepared statement API, but requires no programming because it is available directly at the SQL level:

- You can use it when no programming interface is available to you.
- You can use it from any program that can send SQL statements to the server to be executed, such as

the `mysql` client program.

- You can use it even if the client is using an old version of the client library.

SQL syntax for prepared statements is intended to be used for situations such as these:

- To test how prepared statements work in your application before coding it.
- To use prepared statements when you do not have access to a programming API that supports them.
- To interactively troubleshoot application issues with prepared statements.
- To create a test case that reproduces a problem with prepared statements, so that you can file a bug

report.

> PREPARE, EXECUTE, and DEALLOCATE PREPARE Statements

SQL syntax for prepared statements is based on three SQL statements:

- `PREPARE` prepares a statement for execution (see Section 13.5.1, “PREPARE Statement”).
- `EXECUTE` executes a prepared statement (see Section 13.5.2, “EXECUTE Statement”).

PREPARE, EXECUTE, and DEALLOCATE PREPARE Statements

- `DEALLOCATE PREPARE` releases a prepared statement (see Section 13.5.3, “DEALLOCATE PREPARE

Statement”).

The following examples show two equivalent ways of preparing a statement that computes the hypotenuse of a triangle given the lengths of the two sides.

The first example shows how to create a prepared statement by using a string literal to supply the text of the statement:

```
mysql> PREPARE stmt1 FROM 'SELECT SQRT(POW(?,2) + POW(?,2)) AS hypotenuse';
mysql> SET @a = 3;
mysql> SET @b = 4;
mysql> EXECUTE stmt1 USING @a, @b;
+------------+
| hypotenuse |
+------------+
|          5 |
+------------+
mysql> DEALLOCATE PREPARE stmt1;
```

The second example is similar, but supplies the text of the statement as a user variable:

```
mysql> SET @s = 'SELECT SQRT(POW(?,2) + POW(?,2)) AS hypotenuse';
mysql> PREPARE stmt2 FROM @s;
mysql> SET @a = 6;
mysql> SET @b = 8;
mysql> EXECUTE stmt2 USING @a, @b;
+------------+
| hypotenuse |
+------------+
|         10 |
+------------+
mysql> DEALLOCATE PREPARE stmt2;
```

Here is an additional example that demonstrates how to choose the table on which to perform a query at runtime, by storing the name of the table as a user variable:

```
mysql> USE test;
mysql> CREATE TABLE t1 (a INT NOT NULL);
mysql> INSERT INTO t1 VALUES (4), (8), (11), (32), (80);
mysql> SET @table = 't1';
mysql> SET @s = CONCAT('SELECT * FROM ', @table);
mysql> PREPARE stmt3 FROM @s;
mysql> EXECUTE stmt3;
+----+
| a  |
+----+
|  4 |
|  8 |
| 11 |
| 32 |
| 80 |
+----+
mysql> DEALLOCATE PREPARE stmt3;
```

A prepared statement is specific to the session in which it was created. If you terminate a session without deallocating a previously prepared statement, the server deallocates it automatically.

A prepared statement is also global to the session. If you create a prepared statement within a stored routine, it is not deallocated when the stored routine ends.

SQL Syntax Permitted in Prepared Statements To guard against too many prepared statements being created simultaneously, set the`max_prepared_stmt_count` system variable. To prevent the use of prepared statements, set the value to 0.

> SQL Syntax Permitted in Prepared Statements

The following SQL statements can be used as prepared statements:

```
ALTER TABLE
ALTER USER
ANALYZE TABLE
CACHE INDEX
CALL
CHANGE MASTER
CHECKSUM {TABLE | TABLES}
COMMIT
{CREATE | RENAME | DROP} DATABASE
{CREATE | DROP} INDEX
{CREATE | RENAME | DROP} TABLE
{CREATE | RENAME | DROP} USER
{CREATE | DROP} VIEW
DELETE
DO
FLUSH {TABLE | TABLES | TABLES WITH READ LOCK | HOSTS | PRIVILEGES
| LOGS | STATUS | MASTER | SLAVE | DES_KEY_FILE | USER_RESOURCES}
GRANT
INSERT
INSTALL PLUGIN
KILL
LOAD INDEX INTO CACHE
OPTIMIZE TABLE
REPAIR TABLE
REPLACE
RESET {MASTER | SLAVE | QUERY CACHE}
REVOKE
SELECT
SET
SHOW {AUTHORS | CONTRIBUTORS | WARNINGS | ERRORS}
SHOW BINLOG EVENTS
SHOW CREATE {PROCEDURE | FUNCTION | EVENT | TABLE | VIEW}
SHOW {MASTER | BINARY} LOGS
SHOW {MASTER | SLAVE} STATUS
SLAVE {START | STOP}
TRUNCATE TABLE
UNINSTALL PLUGIN
UPDATE
```

Other statements are not supported.

Generally, statements not permitted in SQL prepared statements are also not permitted in stored programs. Exceptions are noted in Section 20.8, “Restrictions on Stored Programs”.

Metadata changes to tables or views referred to by prepared statements are detected and cause automatic repreparation of the statement when it is next executed. For more information, see Section 8.10.4,“Caching of Prepared Statements and Stored Programs”.

Placeholders can be used for the arguments of the `LIMIT` clause when using prepared statements. See Section 13.2.9, “SELECT Statement”.

In prepared `CALL` statements used with `PREPARE` and `EXECUTE`, placeholder support for `OUT` and `INOUT`parameters is available beginning with MySQL 5.6. See Section 13.2.1, “CALL Statement”, for an example and a workaround for earlier versions. Placeholders can be used for `IN` parameters regardless of version.

PREPARE Statement SQL syntax for prepared statements cannot be used in nested fashion. That is, a statement passed to`PREPARE` cannot itself be a `PREPARE`, `EXECUTE`, or `DEALLOCATE PREPARE` statement.

SQL syntax for prepared statements is distinct from using prepared statement API calls. For example,you cannot use the `mysql_stmt_prepare()` C API function to prepare a `PREPARE`, `EXECUTE`, or`DEALLOCATE PREPARE` statement.

SQL syntax for prepared statements can be used within stored procedures, but not in stored functions or triggers. However, a cursor cannot be used for a dynamic statement that is prepared and executed with`PREPARE` and `EXECUTE`. The statement for a cursor is checked at cursor creation time, so the statement cannot be dynamic.

SQL syntax for prepared statements does not support multi-statements (that is, multiple statements within a single string separated by ; characters).

Prepared statements use the query cache under the conditions described in Section 8.10.3.1, “How the Query Cache Operates”.

To write C programs that use the `CALL` SQL statement to execute stored procedures that contain prepared statements, the `CLIENT_MULTI_RESULTS` flag must be enabled. This is because each `CALL` returns a result to indicate the call status, in addition to any result sets that might be returned by statements executed within the procedure.

`CLIENT_MULTI_RESULTS` can be enabled when you call `mysql_real_connect()`, either explicitly by passing the `CLIENT_MULTI_RESULTS` flag itself, or implicitly by passing `CLIENT_MULTI_STATEMENTS`(which also enables `CLIENT_MULTI_RESULTS`). For additional information, see Section 13.2.1, “CALL Statement”.

### 13.5.1 PREPARE Statement

```
PREPARE stmt_name FROM preparable_stmt
```

The `PREPARE` statement prepares a SQL statement and assigns it a name, `stmt_name`, by which to refer to the statement later. The prepared statement is executed with `EXECUTE` and released with `DEALLOCATE``PREPARE`. For examples, see Section 13.5, “Prepared Statements”.

Statement names are not case-sensitive. `preparable_stmt` is either a string literal or a user variable that contains the text of the SQL statement. The text must represent a single statement, not multiple statements. Within the statement, ? characters can be used as parameter markers to indicate where data values are to be bound to the query later when you execute it. The ? characters should not be enclosed within quotation marks, even if you intend to bind them to string values. Parameter markers can be used only where data values should appear, not for SQL keywords, identifiers, and so forth.

If a prepared statement with the given name already exists, it is deallocated implicitly before the new statement is prepared. This means that if the new statement contains an error and cannot be prepared, an error is returned and no statement with the given name exists.

The scope of a prepared statement is the session within which it is created, which as several implications:

- A prepared statement created in one session is not available to other sessions.
- When a session ends, whether normally or abnormally, its prepared statements no longer exist. If auto-

reconnect is enabled, the client is not notified that the connection was lost. For this reason, clients may wish to disable auto-reconnect. See Automatic Reconnection Control.

- A prepared statement created within a stored program continues to exist after the program finishes

executing and can be executed outside the program later.

EXECUTE Statement

- A statement prepared in stored program context cannot refer to stored procedure or function parameters

or local variables because they go out of scope when the program ends and would be unavailable were the statement to be executed later outside the program. As a workaround, refer instead to user-defined variables, which also have session scope; see Section 9.4, “User-Defined Variables”.

### 13.5.2 EXECUTE Statement

```
EXECUTE stmt_name
[USING @var_name [, @var_name] ...]
```

After preparing a statement with `PREPARE`, you execute it with an `EXECUTE` statement that refers to the prepared statement name. If the prepared statement contains any parameter markers, you must supply a `USING` clause that lists user variables containing the values to be bound to the parameters.

Parameter values can be supplied only by user variables, and the `USING` clause must name exactly as many variables as the number of parameter markers in the statement.

You can execute a given prepared statement multiple times, passing different variables to it or setting the variables to different values before each execution.

For examples, see Section 13.5, “Prepared Statements”.

### 13.5.3 DEALLOCATE PREPARE Statement

```
{DEALLOCATE | DROP} PREPARE stmt_name
```

To deallocate a prepared statement produced with `PREPARE`, use a `DEALLOCATE PREPARE` statement that refers to the prepared statement name. Attempting to execute a prepared statement after deallocating it results in an error. If too many prepared statements are created and not deallocated by either the`DEALLOCATE PREPARE` statement or the end of the session, you might encounter the upper limit enforced by the `max_prepared_stmt_count` system variable.

For examples, see Section 13.5, “Prepared Statements”.

## 13.6 Compound Statements

This section describes the syntax for the `BEGIN ... END` compound statement and other statements that can be used in the body of stored programs: Stored procedures and functions, triggers, and events. These objects are defined in terms of SQL code that is stored on the server for later invocation (see Chapter 20,Stored Objects).

A compound statement is a block that can contain other blocks; declarations for variables, condition handlers, and cursors; and flow control constructs such as loops and conditional tests.

### 13.6.1 BEGIN ... END Compound Statement

```
[begin_label:] BEGIN
[statement_list]
END [end_label]
```

`BEGIN ... END` syntax is used for writing compound statements, which can appear within stored programs (stored procedures and functions, triggers, and events). A compound statement can contain multiple statements, enclosed by the `BEGIN` and `END` keywords. `statement_list` represents a list of one or more statements, each terminated by a semicolon (;) statement delimiter. The `statement_list` itself is optional, so the empty compound statement (`BEGIN END`) is legal.

`BEGIN ... END` blocks can be nested.

Statement Labels Use of multiple statements requires that a client is able to send statement strings containing the ;

statement delimiter. In the `mysql` command-line client, this is handled with the `delimiter` command.

Changing the ; end-of-statement delimiter (for example, to `//`) permit ; to be used in a program body. For an example, see Section 20.1, “Defining Stored Programs”.

A `BEGIN ... END` block can be labeled. See Section 13.6.2, “Statement Labels”.

The optional `[NOT] ATOMIC` clause is not supported. This means that no transactional savepoint is set at the start of the instruction block and the `BEGIN` clause used in this context has no effect on the current transaction.

Note Within all stored programs, the parser treats `BEGIN [WORK]` as the beginning of a `BEGIN ... END` block. To begin a transaction in this context, use `START``TRANSACTION` instead.

### 13.6.2 Statement Labels

```
[begin_label:] BEGIN
[statement_list]
END [end_label]
[begin_label:] LOOP
statement_list
END LOOP [end_label]
[begin_label:] REPEAT
statement_list
UNTIL search_condition
END REPEAT [end_label]
[begin_label:] WHILE search_condition DO
statement_list
END WHILE [end_label]
```

Labels are permitted for `BEGIN ... END` blocks and for the `LOOP`, `REPEAT`, and `WHILE` statements. Label use for those statements follows these rules:

- `begin_label` must be followed by a colon.
- `begin_label` can be given without `end_label`. If `end_label` is present, it must be the same as

```
begin_label.
```

- `end_label` cannot be given without `begin_label`.
- Labels at the same nesting level must be distinct.
- Labels can be up to 16 characters long.

To refer to a label within the labeled construct, use an `ITERATE` or `LEAVE` statement. The following example uses those statements to continue iterating or terminate the loop:

```
CREATE PROCEDURE doiterate(p1 INT)
BEGIN
label1: LOOP
SET p1 = p1 + 1;
IF p1 < 10 THEN ITERATE label1; END IF;
LEAVE label1;
END LOOP label1;
```

DECLARE Statement

```
END;
```

The scope of a block label does not include the code for handlers declared within the block. For details,see Section 13.6.7.2, “DECLARE ... HANDLER Statement”.

### 13.6.3 DECLARE Statement

The `DECLARE` statement is used to define various items local to a program:

- Local variables. See Section 13.6.4, “Variables in Stored Programs”.
- Conditions and handlers. See Section 13.6.7, “Condition Handling”.
- Cursors. See Section 13.6.6, “Cursors”.

`DECLARE` is permitted only inside a `BEGIN ... END` compound statement and must be at its start, before any other statements.

Declarations must follow a certain order. Cursor declarations must appear before handler declarations.

Variable and condition declarations must appear before cursor or handler declarations.

### 13.6.4 Variables in Stored Programs

System variables and user-defined variables can be used in stored programs, just as they can be used outside stored-program context. In addition, stored programs can use `DECLARE` to define local variables,and stored routines (procedures and functions) can be declared to take parameters that communicate values between the routine and its caller.

- To declare local variables, use the `DECLARE` statement, as described in Section 13.6.4.1, “Local Variable

DECLARE Statement”.

- Variables can be set directly with the `SET` statement. See Section 13.7.4.1, “SET Syntax for Variable

Assignment”.

- Results from queries can be retrieved into local variables using `SELECT ... INTO var_list` or by

opening a cursor and using `FETCH ... INTO var_list`. See Section 13.2.9.1, “SELECT ... INTO Statement”, and Section 13.6.6, “Cursors”.

For information about the scope of local variables and how MySQL resolves ambiguous names, see Section 13.6.4.2, “Local Variable Scope and Resolution”.

It is not permitted to assign the value `DEFAULT` to stored procedure or function parameters or stored program local variables (for example with a `SET var_name = DEFAULT` statement). As of MySQL 5.6.6,this results in a syntax error.

#### 13.6.4.1 Local Variable DECLARE Statement

```
DECLARE var_name [, var_name] ... type [DEFAULT value]
```

This statement declares local variables within stored programs. To provide a default value for a variable,include a `DEFAULT` clause. The value can be specified as an expression; it need not be a constant. If the`DEFAULT` clause is missing, the initial value is `NULL`.

Local variables are treated like stored routine parameters with respect to data type and overflow checking.

See Section 13.1.15, “CREATE PROCEDURE and CREATE FUNCTION Statements”.

Variable declarations must appear before cursor or handler declarations.

Variables in Stored Programs Local variable names are not case-sensitive. Permissible characters and quoting rules are the same as for other identifiers, as described in Section 9.2, “Schema Object Names”.

The scope of a local variable is the `BEGIN ... END` block within which it is declared. The variable can be referred to in blocks nested within the declaring block, except those blocks that declare a variable with the same name.

For examples of variable declarations, see Section 13.6.4.2, “Local Variable Scope and Resolution”.

#### 13.6.4.2 Local Variable Scope and Resolution

The scope of a local variable is the `BEGIN ... END` block within which it is declared. The variable can be referred to in blocks nested within the declaring block, except those blocks that declare a variable with the same name.

Because local variables are in scope only during stored program execution, references to them are not permitted in prepared statements created within a stored program. Prepared statement scope is the current session, not the stored program, so the statement could be executed after the program ends, at which point the variables would no longer be in scope. For example, `SELECT ... INTO local_var` cannot be used as a prepared statement. This restriction also applies to stored procedure and function parameters.

See Section 13.5.1, “PREPARE Statement”.

A local variable should not have the same name as a table column. If an SQL statement, such as a`SELECT ... INTO` statement, contains a reference to a column and a declared local variable with the same name, MySQL currently interprets the reference as the name of a variable. Consider the following procedure definition:

```
CREATE PROCEDURE sp1 (x VARCHAR(5))
BEGIN
DECLARE xname VARCHAR(5) DEFAULT 'bob';
DECLARE newname VARCHAR(5);
DECLARE xid INT;
SELECT xname, id INTO newname, xid
FROM table1 WHERE xname = xname;
SELECT newname;
END;
```

MySQL interprets `xname` in the `SELECT` statement as a reference to the `xname` variable rather than the`xname` column. Consequently, when the procedure `sp1()`is called, the `newname` variable returns the value`'bob'` regardless of the value of the `table1.xname` column.

Similarly, the cursor definition in the following procedure contains a `SELECT` statement that refers to`xname`. MySQL interprets this as a reference to the variable of that name rather than a column reference.

```
CREATE PROCEDURE sp2 (x VARCHAR(5))
BEGIN
DECLARE xname VARCHAR(5) DEFAULT 'bob';
DECLARE newname VARCHAR(5);
DECLARE xid INT;
DECLARE done TINYINT DEFAULT 0;
DECLARE cur1 CURSOR FOR SELECT xname, id FROM table1;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
OPEN cur1;
read_loop: LOOP
FETCH FROM cur1 INTO newname, xid;
IF done THEN LEAVE read_loop; END IF;
SELECT newname;
END LOOP;
```

Flow Control Statements

```
CLOSE cur1;
END;
```

See also Section 20.8, “Restrictions on Stored Programs”.

### 13.6.5 Flow Control Statements

MySQL supports the `IF`, `CASE`, `ITERATE`, `LEAVE` `LOOP`, `WHILE`, and `REPEAT` constructs for flow control within stored programs. It also supports `RETURN` within stored functions.

Many of these constructs contain other statements, as indicated by the grammar specifications in the following sections. Such constructs may be nested. For example, an `IF` statement might contain a `WHILE`loop, which itself contains a `CASE` statement.

MySQL does not support `FOR` loops.

#### 13.6.5.1 CASE Statement

```
CASE case_value
WHEN when_value THEN statement_list
[WHEN when_value THEN statement_list] ...
[ELSE statement_list]
END CASE
```

Or:

```
CASE
WHEN search_condition THEN statement_list
[WHEN search_condition THEN statement_list] ...
[ELSE statement_list]
END CASE
```

The `CASE` statement for stored programs implements a complex conditional construct.

Note There is also a `CASE` operator, which differs from the `CASE` statement described here. See Section 12.5, “Flow Control Functions”. The `CASE` statement cannot have an `ELSE NULL` clause, and it is terminated with `END CASE` instead of `END`.

For the first syntax, `case_value` is an expression. This value is compared to the `when_value`expression in each `WHEN` clause until one of them is equal. When an equal `when_value` is found, the corresponding `THEN` clause `statement_list` executes. If no `when_value` is equal, the `ELSE` clause`statement_list` executes, if there is one.

This syntax cannot be used to test for equality with `NULL` because `NULL = NULL` is false. See Section 3.3.4.6, “Working with NULL Values”.

For the second syntax, each `WHEN` clause `search_condition` expression is evaluated until one is true,at which point its corresponding `THEN` clause `statement_list` executes. If no `search_condition` is equal, the `ELSE` clause `statement_list` executes, if there is one.

If no `when_value` or `search_condition` matches the value tested and the `CASE` statement contains no`ELSE` clause, a `Case not found for CASE statement` error results.

Each `statement_list` consists of one or more SQL statements; an empty `statement_list` is not permitted.

Flow Control Statements To handle situations where no value is matched by any `WHEN` clause, use an `ELSE` containing an empty`BEGIN ... END` block, as shown in this example. (The indentation used here in the `ELSE` clause is for purposes of clarity only, and is not otherwise significant.)

```
DELIMITER |
CREATE PROCEDURE p()
BEGIN
DECLARE v INT DEFAULT 1;
CASE v
WHEN 2 THEN SELECT v;
WHEN 3 THEN SELECT 0;
ELSE
BEGIN
END;
END CASE;
END;
|
```

#### 13.6.5.2 IF Statement

```
IF search_condition THEN statement_list
[ELSEIF search_condition THEN statement_list] ...
[ELSE statement_list]
END IF
```

The `IF` statement for stored programs implements a basic conditional construct.

Note There is also an `IF()` function, which differs from the `IF` statement described here.

See Section 12.5, “Flow Control Functions”. The `IF` statement can have `THEN`,`ELSE`, and `ELSEIF` clauses, and it is terminated with `END IF`.

If a given `search_condition` evaluates to true, the corresponding `THEN` or `ELSEIF` clause`statement_list` executes. If no `search_condition` matches, the `ELSE` clause `statement_list`executes.

Each `statement_list` consists of one or more SQL statements; an empty `statement_list` is not permitted.

An `IF ... END IF` block, like all other flow-control blocks used within stored programs, must be terminated with a semicolon, as shown in this example:

```
DELIMITER //
CREATE FUNCTION SimpleCompare(n INT, m INT)
RETURNS VARCHAR(20)
BEGIN
DECLARE s VARCHAR(20);
IF n > m THEN SET s = '>';
ELSEIF n = m THEN SET s = '=';
ELSE SET s = '<';
END IF;
SET s = CONCAT(n, ' ', s, ' ', m);
RETURN s;
END //
```

Flow Control Statements

```
DELIMITER ;
```

As with other flow-control constructs, `IF ... END IF` blocks may be nested within other flow-control constructs, including other `IF` statements. Each `IF` must be terminated by its own `END IF` followed by a semicolon. You can use indentation to make nested flow-control blocks more easily readable by humans(although this is not required by MySQL), as shown here:

```
DELIMITER //
CREATE FUNCTION VerboseCompare (n INT, m INT)
RETURNS VARCHAR(50)
BEGIN
DECLARE s VARCHAR(50);
IF n = m THEN SET s = 'equals';
ELSE
IF n > m THEN SET s = 'greater';
ELSE SET s = 'less';
END IF;
SET s = CONCAT('is ', s, ' than');
END IF;
SET s = CONCAT(n, ' ', s, ' ', m, '.');
RETURN s;
END //
DELIMITER ;
```

In this example, the inner `IF` is evaluated only if n is not equal to m.

#### 13.6.5.3 ITERATE Statement

```
ITERATE label
```

`ITERATE` can appear only within `LOOP`, `REPEAT`, and `WHILE` statements. `ITERATE` means “start the loop again.”For an example, see Section 13.6.5.5, “LOOP Statement”.

#### 13.6.5.4 LEAVE Statement

```
LEAVE label
```

This statement is used to exit the flow control construct that has the given label. If the label is for the outermost stored program block, `LEAVE` exits the program.

`LEAVE` can be used within `BEGIN ... END` or loop constructs (`LOOP`, `REPEAT`, `WHILE`).

For an example, see Section 13.6.5.5, “LOOP Statement”.

#### 13.6.5.5 LOOP Statement

```
[begin_label:] LOOP
statement_list
END LOOP [end_label]
```

`LOOP` implements a simple loop construct, enabling repeated execution of the statement list, which consists of one or more statements, each terminated by a semicolon (;) statement delimiter. The statements within Flow Control Statements the loop are repeated until the loop is terminated. Usually, this is accomplished with a `LEAVE` statement.

Within a stored function, `RETURN` can also be used, which exits the function entirely.

Neglecting to include a loop-termination statement results in an infinite loop.

A `LOOP` statement can be labeled. For the rules regarding label use, see Section 13.6.2, “Statement Labels”.

Example:

```
CREATE PROCEDURE doiterate(p1 INT)
BEGIN
label1: LOOP
SET p1 = p1 + 1;
IF p1 < 10 THEN
ITERATE label1;
END IF;
LEAVE label1;
END LOOP label1;
SET @x = p1;
END;
```

#### 13.6.5.6 REPEAT Statement

```
[begin_label:] REPEAT
statement_list
UNTIL search_condition
END REPEAT [end_label]
```

The statement list within a `REPEAT` statement is repeated until the `search_condition` expression is true. Thus, a `REPEAT` always enters the loop at least once. `statement_list` consists of one or more statements, each terminated by a semicolon (;) statement delimiter.

A `REPEAT` statement can be labeled. For the rules regarding label use, see Section 13.6.2, “Statement Labels”.

Example:

```
mysql> delimiter //
mysql> CREATE PROCEDURE dorepeat(p1 INT)
BEGIN
SET @x = 0;
REPEAT
SET @x = @x + 1;
UNTIL @x > p1 END REPEAT;
END
//
Query OK, 0 rows affected (0.00 sec)
mysql> CALL dorepeat(1000)//
Query OK, 0 rows affected (0.00 sec)
mysql> SELECT @x//
+------+
| @x   |
+------+
| 1001 |
+------+
1 row in set (0.00 sec)
```

#### 13.6.5.7 RETURN Statement

```
RETURN expr
```

Cursors The `RETURN` statement terminates execution of a stored function and returns the value `expr` to the function caller. There must be at least one `RETURN` statement in a stored function. There may be more than one if the function has multiple exit points.

This statement is not used in stored procedures, triggers, or events. The `LEAVE` statement can be used to exit a stored program of those types.

#### 13.6.5.8 WHILE Statement

```
[begin_label:] WHILE search_condition DO
statement_list
END WHILE [end_label]
```

The statement list within a `WHILE` statement is repeated as long as the `search_condition` expression is true. `statement_list` consists of one or more SQL statements, each terminated by a semicolon (;)statement delimiter.

A `WHILE` statement can be labeled. For the rules regarding label use, see Section 13.6.2, “Statement Labels”.

Example:

```
CREATE PROCEDURE dowhile()
BEGIN
DECLARE v1 INT DEFAULT 5;
WHILE v1 > 0 DO
...
SET v1 = v1 - 1;
END WHILE;
END;
```

### 13.6.6 Cursors

MySQL supports cursors inside stored programs. The syntax is as in embedded SQL. Cursors have these properties:

- Asensitive: The server may or may not make a copy of its result table
- Read only: Not updatable
- Nonscrollable: Can be traversed only in one direction and cannot skip rows

Cursor declarations must appear before handler declarations and after variable and condition declarations.

Example:

```
CREATE PROCEDURE curdemo()
BEGIN
DECLARE done INT DEFAULT FALSE;
DECLARE a CHAR(16);
DECLARE b, c INT;
DECLARE cur1 CURSOR FOR SELECT id,data FROM test.t1;
DECLARE cur2 CURSOR FOR SELECT i FROM test.t2;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
OPEN cur1;
OPEN cur2;
read_loop: LOOP
FETCH cur1 INTO a, b;
```

Cursors

```
FETCH cur2 INTO c;
IF done THEN
LEAVE read_loop;
END IF;
IF b < c THEN
INSERT INTO test.t3 VALUES (a,b);
ELSE
INSERT INTO test.t3 VALUES (a,c);
END IF;
END LOOP;
CLOSE cur1;
CLOSE cur2;
END;
```

#### 13.6.6.1 Cursor CLOSE Statement

```
CLOSE cursor_name
```

This statement closes a previously opened cursor. For an example, see Section 13.6.6, “Cursors”.

An error occurs if the cursor is not open.

If not closed explicitly, a cursor is closed at the end of the `BEGIN ... END` block in which it was declared.

#### 13.6.6.2 Cursor DECLARE Statement

```
DECLARE cursor_name CURSOR FOR select_statement
```

This statement declares a cursor and associates it with a `SELECT` statement that retrieves the rows to be traversed by the cursor. To fetch the rows later, use a `FETCH` statement. The number of columns retrieved by the `SELECT` statement must match the number of output variables specified in the `FETCH` statement.

The `SELECT` statement cannot have an `INTO` clause.

Cursor declarations must appear before handler declarations and after variable and condition declarations.

A stored program may contain multiple cursor declarations, but each cursor declared in a given block must have a unique name. For an example, see Section 13.6.6, “Cursors”.

For information available through `SHOW` statements, it is possible in many cases to obtain equivalent information by using a cursor with an `INFORMATION_SCHEMA` table.

#### 13.6.6.3 Cursor FETCH Statement

```
FETCH [[NEXT] FROM] cursor_name INTO var_name [, var_name] ...
```

This statement fetches the next row for the `SELECT` statement associated with the specified cursor (which must be open), and advances the cursor pointer. If a row exists, the fetched columns are stored in the named variables. The number of columns retrieved by the `SELECT` statement must match the number of output variables specified in the `FETCH` statement.

If no more rows are available, a No Data condition occurs with SQLSTATE value `'02000'`. To detect this condition, you can set up a handler for it (or for a `NOT FOUND` condition). For an example, see Section 13.6.6, “Cursors”.

Be aware that another operation, such as a `SELECT` or another `FETCH`, may also cause the handler to execute by raising the same condition. If it is necessary to distinguish which operation raised the condition,place the operation within its own `BEGIN ... END` block so that it can be associated with its own handler.

Condition Handling

#### 13.6.6.4 Cursor OPEN Statement

```
OPEN cursor_name
```

This statement opens a previously declared cursor. For an example, see Section 13.6.6, “Cursors”.

#### 13.6.6.5 Restrictions on Server-Side Cursors

Server-side cursors are implemented in the C API using the `mysql_stmt_attr_set()` function. The same implementation is used for cursors in stored routines. A server-side cursor enables a result set to be generated on the server side, but not transferred to the client except for those rows that the client requests.

For example, if a client executes a query but is only interested in the first row, the remaining rows are not transferred.

In MySQL, a server-side cursor is materialized into an internal temporary table. Initially, this is a`MEMORY` table, but is converted to a `MyISAM` table when its size exceeds the minimum value of the`max_heap_table_size` and `tmp_table_size` system variables. The same restrictions apply to internal temporary tables created to hold the result set for a cursor as for other uses of internal temporary tables.

See Section 8.4.4, “Internal Temporary Table Use in MySQL”. One limitation of the implementation is that for a large result set, retrieving its rows through a cursor might be slow.

Cursors are read only; you cannot use a cursor to update rows.

`UPDATE WHERE CURRENT OF` and `DELETE WHERE CURRENT OF` are not implemented, because updatable cursors are not supported.

Cursors are nonholdable (not held open after a commit).

Cursors are asensitive.

Cursors are nonscrollable.

Cursors are not named. The statement handler acts as the cursor ID.

You can have open only a single cursor per prepared statement. If you need several cursors, you must prepare several statements.

You cannot use a cursor for a statement that generates a result set if the statement is not supported in prepared mode. This includes statements such as `CHECK TABLE`, `HANDLER READ`, and `SHOW BINLOG`

```
EVENTS.
```

### 13.6.7 Condition Handling

Conditions may arise during stored program execution that require special handling, such as exiting the current program block or continuing execution. Handlers can be defined for general conditions such as warnings or exceptions, or for specific conditions such as a particular error code. Specific conditions can be assigned names and referred to that way in handlers.

To name a condition, use the `DECLARE ... CONDITION` statement. To declare a handler, use the`DECLARE ... HANDLER` statement. See Section 13.6.7.1, “DECLARE ... CONDITION Statement”, and Section 13.6.7.2, “DECLARE ... HANDLER Statement”. For information about how the server chooses handlers when a condition occurs, see Section 13.6.7.6, “Scope Rules for Handlers”.

To raise a condition, use the `SIGNAL` statement. To modify condition information within a condition handler,use `RESIGNAL`. See Section 13.6.7.1, “DECLARE ... CONDITION Statement”, and Section 13.6.7.2,“DECLARE ... HANDLER Statement”.

Condition Handling To retrieve information from the diagnostics area, use the `GET DIAGNOSTICS` statement (see Section 13.6.7.3, “GET DIAGNOSTICS Statement”). For information about the diagnostics area, see Section 13.6.7.7, “The MySQL Diagnostics Area”.

#### 13.6.7.1 DECLARE ... CONDITION Statement

```
DECLARE condition_name CONDITION FOR condition_value
condition_value: {
mysql_error_code
| SQLSTATE [VALUE] sqlstate_value
}
```

The `DECLARE ... CONDITION` statement declares a named error condition, associating a name with a condition that needs specific handling. The name can be referred to in a subsequent `DECLARE ...``HANDLER` statement (see Section 13.6.7.2, “DECLARE ... HANDLER Statement”).

Condition declarations must appear before cursor or handler declarations.

The `condition_value` for `DECLARE ... CONDITION` indicates the specific condition or class of conditions to associate with the condition name. It can take the following forms:

- `mysql_error_code`: An integer literal indicating a MySQL error code.

Do not use MySQL error code 0 because that indicates success rather than an error condition. For a list of MySQL error codes, see Server Error Message Reference.

- SQLSTATE [VALUE] `sqlstate_value`: A 5-character string literal indicating an SQLSTATE value.

Do not use SQLSTATE values that begin with `'00'` because those indicate success rather than an error condition. For a list of SQLSTATE values, see Server Error Message Reference.

Condition names referred to in `SIGNAL` or use `RESIGNAL` statements must be associated with SQLSTATE values, not MySQL error codes.

Using names for conditions can help make stored program code clearer. For example, this handler applies to attempts to drop a nonexistent table, but that is apparent only if you know that 1051 is the MySQL error code for “unknown table”:

```
DECLARE CONTINUE HANDLER FOR 1051
BEGIN
-- body of handler
END;
```

By declaring a name for the condition, the purpose of the handler is more readily seen:

```
DECLARE no_such_table CONDITION FOR 1051;
DECLARE CONTINUE HANDLER FOR no_such_table
BEGIN
-- body of handler
END;
```

Here is a named condition for the same condition, but based on the corresponding SQLSTATE value rather than the MySQL error code:

```
DECLARE no_such_table CONDITION FOR SQLSTATE '42S02';
DECLARE CONTINUE HANDLER FOR no_such_table
BEGIN
-- body of handler
END;
```

Condition Handling

#### 13.6.7.2 DECLARE ... HANDLER Statement

```
DECLARE handler_action HANDLER
FOR condition_value [, condition_value] ...
statement
handler_action: {
CONTINUE
| EXIT
| UNDO
}
condition_value: {
mysql_error_code
| SQLSTATE [VALUE] sqlstate_value
| condition_name
| SQLWARNING
| NOT FOUND
| SQLEXCEPTION
}
```

The `DECLARE ... HANDLER` statement specifies a handler that deals with one or more conditions.

If one of these conditions occurs, the specified `statement` executes. `statement` can be a simple statement such as `SET var_name = value`, or a compound statement written using `BEGIN` and `END`(see Section 13.6.1, “BEGIN ... END Compound Statement”).

Handler declarations must appear after variable or condition declarations.

The `handler_action` value indicates what action the handler takes after execution of the handler statement:

- `CONTINUE`: Execution of the current program continues.
- `EXIT`: Execution terminates for the `BEGIN ... END` compound statement in which the handler is

declared. This is true even if the condition occurs in an inner block.

- `UNDO`: Not supported.

The `condition_value` for `DECLARE ... HANDLER` indicates the specific condition or class of conditions that activates the handler. It can take the following forms:

- `mysql_error_code`: An integer literal indicating a MySQL error code, such as 1051 to specify

“unknown table”:

```
DECLARE CONTINUE HANDLER FOR 1051
BEGIN
-- body of handler
END;
```

Do not use MySQL error code 0 because that indicates success rather than an error condition. For a list of MySQL error codes, see Server Error Message Reference.

- SQLSTATE [VALUE] `sqlstate_value`: A 5-character string literal indicating an SQLSTATE value,

such as `'42S01'` to specify “unknown table”:

```
DECLARE CONTINUE HANDLER FOR SQLSTATE '42S02'
BEGIN
-- body of handler
END;
```

Do not use SQLSTATE values that begin with `'00'` because those indicate success rather than an error condition. For a list of SQLSTATE values, see Server Error Message Reference.

Condition Handling

- `condition_name`: A condition name previously specified with `DECLARE ... CONDITION`. A

condition name can be associated with a MySQL error code or SQLSTATE value. See Section 13.6.7.1,“DECLARE ... CONDITION Statement”.

- `SQLWARNING`: Shorthand for the class of SQLSTATE values that begin with `'01'`.

```
DECLARE CONTINUE HANDLER FOR SQLWARNING
BEGIN
-- body of handler
END;
```

- `NOT FOUND`: Shorthand for the class of SQLSTATE values that begin with `'02'`. This is relevant within

the context of cursors and is used to control what happens when a cursor reaches the end of a data set.

If no more rows are available, a No Data condition occurs with SQLSTATE value `'02000'`. To detect this condition, you can set up a handler for it or for a `NOT FOUND` condition.

```
DECLARE CONTINUE HANDLER FOR NOT FOUND
BEGIN
-- body of handler
END;
```

For another example, see Section 13.6.6, “Cursors”. The `NOT FOUND` condition also occurs for`SELECT ... INTO var_list` statements that retrieve no rows.

- `SQLEXCEPTION`: Shorthand for the class of SQLSTATE values that do not begin with `'00'`, `'01'`, or

```
'02'.
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
BEGIN
-- body of handler
END;
```

For information about how the server chooses handlers when a condition occurs, see Section 13.6.7.6,“Scope Rules for Handlers”.

If a condition occurs for which no handler has been declared, the action taken depends on the condition class:

- For `SQLEXCEPTION` conditions, the stored program terminates at the statement that raised the condition,

as if there were an `EXIT` handler. If the program was called by another stored program, the calling program handles the condition using the handler selection rules applied to its own handlers.

- For `SQLWARNING` conditions, the program continues executing, as if there were a `CONTINUE` handler.
- For `NOT FOUND` conditions, if the condition was raised normally, the action is `CONTINUE`. If it was raised

by `SIGNAL` or `RESIGNAL`, the action is `EXIT`.

The following example uses a handler for `SQLSTATE '23000'`, which occurs for a duplicate-key error:

```
mysql> CREATE TABLE test.t (s1 INT, PRIMARY KEY (s1));
Query OK, 0 rows affected (0.00 sec)
mysql> delimiter //
mysql> CREATE PROCEDURE handlerdemo ()
BEGIN
DECLARE CONTINUE HANDLER FOR SQLSTATE '23000' SET @x2 = 1;
SET @x = 1;
INSERT INTO test.t VALUES (1);
SET @x = 2;
INSERT INTO test.t VALUES (1);
SET @x = 3;
```

Condition Handling

```
END;
//
Query OK, 0 rows affected (0.00 sec)
mysql> CALL handlerdemo()//
Query OK, 0 rows affected (0.00 sec)
mysql> SELECT @x//
+------+
| @x   |
+------+
| 3    |
+------+
1 row in set (0.00 sec)
```

Notice that `@x` is 3 after the procedure executes, which shows that execution continued to the end of the procedure after the error occurred. If the `DECLARE ... HANDLER` statement had not been present,MySQL would have taken the default action (`EXIT`) after the second `INSERT` failed due to the `PRIMARY``KEY` constraint, and `SELECT @x` would have returned 2.

To ignore a condition, declare a `CONTINUE` handler for it and associate it with an empty block. For example:

```
DECLARE CONTINUE HANDLER FOR SQLWARNING BEGIN END;
```

The scope of a block label does not include the code for handlers declared within the block. Therefore,the statement associated with a handler cannot use `ITERATE` or `LEAVE` to refer to labels for blocks that enclose the handler declaration. Consider the following example, where the `REPEAT` block has a label of

```
retry:
CREATE PROCEDURE p ()
BEGIN
DECLARE i INT DEFAULT 3;
retry:
REPEAT
BEGIN
DECLARE CONTINUE HANDLER FOR SQLWARNING
BEGIN
ITERATE retry;    # illegal
END;
IF i < 0 THEN
LEAVE retry;        # legal
END IF;
SET i = i - 1;
END;
UNTIL FALSE END REPEAT;
END;
```

The `retry` label is in scope for the `IF` statement within the block. It is not in scope for the `CONTINUE`handler, so the reference there is invalid and results in an error:

```
ERROR 1308 (42000): LEAVE with no matching label: retry
```

To avoid references to outer labels in handlers, use one of these strategies:

- To leave the block, use an `EXIT` handler. If no block cleanup is required, the `BEGIN ... END` handler

body can be empty:

```
DECLARE EXIT HANDLER FOR SQLWARNING BEGIN END;
```

Otherwise, put the cleanup statements in the handler body:

```
DECLARE EXIT HANDLER FOR SQLWARNING
```

Condition Handling

```
BEGIN
block cleanup statements
END;
```

- To continue execution, set a status variable in a `CONTINUE` handler that can be checked in the enclosing

block to determine whether the handler was invoked. The following example uses the variable `done` for this purpose:

```
CREATE PROCEDURE p ()
BEGIN
DECLARE i INT DEFAULT 3;
DECLARE done INT DEFAULT FALSE;
retry:
REPEAT
BEGIN
DECLARE CONTINUE HANDLER FOR SQLWARNING
BEGIN
SET done = TRUE;
END;
IF done OR i < 0 THEN
LEAVE retry;
END IF;
SET i = i - 1;
END;
UNTIL FALSE END REPEAT;
END;
```

#### 13.6.7.3 GET DIAGNOSTICS Statement

```
GET [CURRENT] DIAGNOSTICS {
statement_information_item
[, statement_information_item] ...
| CONDITION condition_number
condition_information_item
[, condition_information_item] ...
}
statement_information_item:
target = statement_information_item_name
condition_information_item:
target = condition_information_item_name
statement_information_item_name: {
NUMBER
| ROW_COUNT
}
condition_information_item_name: {
CLASS_ORIGIN
| SUBCLASS_ORIGIN
| RETURNED_SQLSTATE
| MESSAGE_TEXT
| MYSQL_ERRNO
| CONSTRAINT_CATALOG
| CONSTRAINT_SCHEMA
| CONSTRAINT_NAME
| CATALOG_NAME
| SCHEMA_NAME
| TABLE_NAME
| COLUMN_NAME
| CURSOR_NAME
}
condition_number, target:
(see following discussion)
```

Condition Handling SQL statements produce diagnostic information that populates the diagnostics area. The `GET``DIAGNOSTICS` statement enables applications to inspect this information. It is available as of MySQL 5.6.4.

(You can also use `SHOW WARNINGS` or `SHOW ERRORS` to see conditions or errors.)No special privileges are required to execute `GET DIAGNOSTICS`.

The keyword `CURRENT` means to retrieve information from the current diagnostics area. In MySQL, it has no effect because that is the default behavior.

`GET DIAGNOSTICS` is typically used in a handler within a stored program, but it is a MySQL extension that it is permitted outside handler context to check the execution of any SQL statement. For example, if you invoke the `mysql` client program, you can enter these statements at the prompt:

```
mysql> DROP TABLE test.no_such_table;
ERROR 1051 (42S02): Unknown table 'test.no_such_table'
mysql> GET DIAGNOSTICS CONDITION 1
@p1 = RETURNED_SQLSTATE, @p2 = MESSAGE_TEXT;
mysql> SELECT @p1, @p2;
+-------+------------------------------------+
| @p1   | @p2                                |
+-------+------------------------------------+
| 42S02 | Unknown table 'test.no_such_table' |
+-------+------------------------------------+
```

For a description of the diagnostics area, see Section 13.6.7.7, “The MySQL Diagnostics Area”. Briefly, it contains two kinds of information:

- Statement information, such as the number of conditions that occurred or the affected-rows count.
- Condition information, such as the error code and message. If a statement raises multiple conditions,

this part of the diagnostics area has a condition area for each one. If a statement raises no conditions,this part of the diagnostics area is empty.

For a statement that produces three conditions, the diagnostics area contains statement and condition information like this:

```
Statement information:
row count
... other statement information items ...
Condition area list:
Condition area 1:
error code for condition 1
error message for condition 1
... other condition information items ...
Condition area 2:
error code for condition 2:
error message for condition 2
... other condition information items ...
Condition area 3:
error code for condition 3
error message for condition 3
... other condition information items ...
```

`GET DIAGNOSTICS` can obtain either statement or condition information, but not both in the same statement:

- To obtain statement information, retrieve the desired statement items into target variables. This instance

of `GET DIAGNOSTICS` assigns the number of available conditions and the rows-affected count to the user variables `@p1` and `@p2`:

```
GET DIAGNOSTICS @p1 = NUMBER, @p2 = ROW_COUNT;
```

Condition Handling

- To obtain condition information, specify the condition number and retrieve the desired condition items

into target variables. This instance of `GET DIAGNOSTICS` assigns the SQLSTATE value and error message to the user variables `@p3` and `@p4`:

```
GET DIAGNOSTICS CONDITION 1
@p3 = RETURNED_SQLSTATE, @p4 = MESSAGE_TEXT;
```

The retrieval list specifies one or more `target = item_name` assignments, separated by commas.

Each assignment names a target variable and either a `statement_information_item_name` or`condition_information_item_name` designator, depending on whether the statement retrieves statement or condition information.

Valid `target` designators for storing item information can be stored procedure or function parameters,stored program local variables declared with `DECLARE`, or user-defined variables.

Valid `condition_number` designators can be stored procedure or function parameters, stored program local variables declared with `DECLARE`, user-defined variables, system variables, or literals. A character literal may include a `_charset` introducer. A warning occurs if the condition number is not in the range from 1 to the number of condition areas that have information. In this case, the warning is added to the diagnostics area without clearing it.

When a condition occurs, MySQL does not populate all condition items recognized by `GET DIAGNOSTICS`.

For example:

```
mysql> GET DIAGNOSTICS CONDITION 1
@p5 = SCHEMA_NAME, @p6 = TABLE_NAME;
mysql> SELECT @p5, @p6;
+------+------+
| @p5  | @p6  |
+------+------+
|      |      |
+------+------+
```

In standard SQL, if there are multiple conditions, the first condition relates to the `SQLSTATE` value returned for the previous SQL statement. In MySQL, this is not guaranteed. To get the main error, you cannot do this:

```
GET DIAGNOSTICS CONDITION 1 @errno = MYSQL_ERRNO;
```

Instead, retrieve the condition count first, then use it to specify which condition number to inspect:

```
GET DIAGNOSTICS @cno = NUMBER;
GET DIAGNOSTICS CONDITION @cno @errno = MYSQL_ERRNO;
```

For information about permissible statement and condition information items, and which ones are populated when a condition occurs, see Diagnostics Area Information Items.

Here is an example that uses `GET DIAGNOSTICS` and an exception handler in stored procedure context to assess the outcome of an insert operation. If the insert was successful, the procedure uses `GET``DIAGNOSTICS` to get the rows-affected count. This shows that you can use `GET DIAGNOSTICS` multiple times to retrieve information about a statement as long as the diagnostics area has not been cleared.

```
CREATE PROCEDURE do_insert(value INT)
BEGIN
-- Declare variables to hold diagnostics area information
DECLARE code CHAR(5) DEFAULT '00000';
DECLARE msg TEXT;
DECLARE nrows INT;
DECLARE result TEXT;
-- Declare exception handler for failed insert
```

Condition Handling

```
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
BEGIN
GET DIAGNOSTICS CONDITION 1
code = RETURNED_SQLSTATE, msg = MESSAGE_TEXT;
END;
-- Perform the insert
INSERT INTO t1 (int_col) VALUES(value);
-- Check whether the insert was successful
IF code = '00000' THEN
GET DIAGNOSTICS nrows = ROW_COUNT;
SET result = CONCAT('insert succeeded, row count = ',nrows);
ELSE
SET result = CONCAT('insert failed, error = ',code,', message = ',msg);
END IF;
-- Say what happened
SELECT result;
END;
```

Suppose that `t1.int_col` is an integer column that is declared as `NOT NULL`. The procedure produces these results when invoked to insert non-`NULL` and `NULL` values, respectively:

```
mysql> CALL do_insert(1);
+---------------------------------+
| result                          |
+---------------------------------+
| insert succeeded, row count = 1 |
+---------------------------------+
mysql> CALL do_insert(NULL);
+-------------------------------------------------------------------------+
| result                                                                  |
+-------------------------------------------------------------------------+
| insert failed, error = 23000, message = Column 'int_col' cannot be null |
+-------------------------------------------------------------------------+
```

Within a condition handler, `GET DIAGNOSTICS` should be used before other statements that might clear the diagnostics area and cause information to be lost about the condition that activated the handler.

For information about when the diagnostics area is set and cleared, see Section 13.6.7.7, “The MySQL Diagnostics Area”.

#### 13.6.7.4 RESIGNAL Statement

```
RESIGNAL [condition_value]
[SET signal_information_item
[, signal_information_item] ...]
condition_value: {
SQLSTATE [VALUE] sqlstate_value
| condition_name
}
signal_information_item:
condition_information_item_name = simple_value_specification
condition_information_item_name: {
CLASS_ORIGIN
| SUBCLASS_ORIGIN
| MESSAGE_TEXT
| MYSQL_ERRNO
| CONSTRAINT_CATALOG
| CONSTRAINT_SCHEMA
| CONSTRAINT_NAME
| CATALOG_NAME
| SCHEMA_NAME
```

Condition Handling

```
| TABLE_NAME
| COLUMN_NAME
| CURSOR_NAME
}
condition_name, simple_value_specification:
(see following discussion)
```

`RESIGNAL` passes on the error condition information that is available during execution of a condition handler within a compound statement inside a stored procedure or function, trigger, or event. `RESIGNAL`may change some or all information before passing it on. `RESIGNAL` is related to `SIGNAL`, but instead of originating a condition as `SIGNAL` does, `RESIGNAL` relays existing condition information, possibly after modifying it.

`RESIGNAL` makes it possible to both handle an error and return the error information. Otherwise, by executing an SQL statement within the handler, information that caused the handler's activation is destroyed. `RESIGNAL` also can make some procedures shorter if a given handler can handle part of a situation, then pass the condition “up the line” to another handler.

No privileges are required to execute the `RESIGNAL` statement.

All forms of `RESIGNAL` require that the current context be a condition handler. Otherwise, `RESIGNAL` is illegal and a `RESIGNAL when handler not active` error occurs.

To retrieve information from the diagnostics area, use the `GET DIAGNOSTICS` statement (see Section 13.6.7.3, “GET DIAGNOSTICS Statement”). For information about the diagnostics area, see Section 13.6.7.7, “The MySQL Diagnostics Area”.

- RESIGNAL Overview
- RESIGNAL Alone
- RESIGNAL with New Signal Information
- RESIGNAL with a Condition Value and Optional New Signal Information
- RESIGNAL Requires Condition Handler Context

RESIGNAL Overview For `condition_value` and `signal_information_item`, the definitions and rules are the same for `RESIGNAL` as for `SIGNAL`. For example, the `condition_value` can be an `SQLSTATE` value, and the value can indicate errors, warnings, or “not found.” For additional information, see Section 13.6.7.5,“SIGNAL Statement”.

The `RESIGNAL` statement takes `condition_value` and `SET` clauses, both of which are optional. This leads to several possible uses:

- `RESIGNAL` alone:

```
RESIGNAL;
```

- `RESIGNAL` with new signal information:

```
RESIGNAL SET signal_information_item [, signal_information_item] ...;
```

- `RESIGNAL` with a condition value and possibly new signal information:

```
RESIGNAL condition_value
```

Condition Handling

```
[SET signal_information_item [, signal_information_item] ...];
```

These use cases all cause changes to the diagnostics and condition areas:

- A diagnostics area contains one or more condition areas.
- A condition area contains condition information items, such as the `SQLSTATE` value, `MYSQL_ERRNO`, or

```
MESSAGE_TEXT.
```

The maximum number of condition areas in a diagnostics area is determined by the value of the`max_error_count` system variable. See Diagnostics Area-Related System Variables.

RESIGNAL Alone A simple `RESIGNAL` alone means “pass on the error with no change.” It restores the last diagnostics area and makes it the current diagnostics area. That is, it “pops” the diagnostics area stack.

Within a condition handler that catches a condition, one use for `RESIGNAL` alone is to perform some other actions, and then pass on without change the original condition information (the information that existed before entry into the handler).

Example:

```
DROP TABLE IF EXISTS xx;
delimiter //
CREATE PROCEDURE p ()
BEGIN
DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
SET @error_count = @error_count + 1;
IF @a = 0 THEN RESIGNAL; END IF;
END;
DROP TABLE xx;
END//
delimiter ;
SET @error_count = 0;
SET @a = 0;
CALL p();
```

Suppose that the `DROP TABLE xx` statement fails. The diagnostics area stack looks like this:

```
DA 1. ERROR 1051 (42S02): Unknown table 'xx'
```

Then execution enters the `EXIT` handler. It starts by pushing a diagnostics area to the top of the stack,which now looks like this:

```
DA 1. ERROR 1051 (42S02): Unknown table 'xx'
DA 2. ERROR 1051 (42S02): Unknown table 'xx'
```

At this point, the contents of the first (current) and second (stacked) diagnostics areas are the same. The first diagnostics area may be modified by statements executing subsequently within the handler.

Usually a procedure statement clears the first diagnostics area. `BEGIN` is an exception, it does not clear,it does nothing. `SET` is not an exception, it clears, performs the operation, and produces a result of“success.” The diagnostics area stack now looks like this:

```
DA 1. ERROR 0000 (00000): Successful operation
DA 2. ERROR 1051 (42S02): Unknown table 'xx'
```

At this point, if `@a = 0`, `RESIGNAL` pops the diagnostics area stack, which now looks like this:Condition Handling

```
DA 1. ERROR 1051 (42S02): Unknown table 'xx'
```

And that is what the caller sees.

If `@a` is not 0, the handler simply ends, which means that there is no more use for the current diagnostics area (it has been “handled”), so it can be thrown away, causing the stacked diagnostics area to become the current diagnostics area again. The diagnostics area stack looks like this:

```
DA 1. ERROR 0000 (00000): Successful operation
```

The details make it look complex, but the end result is quite useful: Handlers can execute without destroying information about the condition that caused activation of the handler.

RESIGNAL with New Signal Information`RESIGNAL` with a `SET` clause provides new signal information, so the statement means “pass on the error with changes”:

```
RESIGNAL SET signal_information_item [, signal_information_item] ...;
```

As with `RESIGNAL` alone, the idea is to pop the diagnostics area stack so that the original information goes out. Unlike `RESIGNAL` alone, anything specified in the `SET` clause changes.

Example:

```
DROP TABLE IF EXISTS xx;
delimiter //
CREATE PROCEDURE p ()
BEGIN
DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
SET @error_count = @error_count + 1;
IF @a = 0 THEN RESIGNAL SET MYSQL_ERRNO = 5; END IF;
END;
DROP TABLE xx;
END//
delimiter ;
SET @error_count = 0;
SET @a = 0;
CALL p();
```

Remember from the previous discussion that `RESIGNAL` alone results in a diagnostics area stack like this:

```
DA 1. ERROR 1051 (42S02): Unknown table 'xx'
```

The `RESIGNAL SET MYSQL_ERRNO = 5` statement results in this stack instead, which is what the caller sees:

```
DA 1. ERROR 5 (42S02): Unknown table 'xx'
```

In other words, it changes the error number, and nothing else.

The `RESIGNAL` statement can change any or all of the signal information items, making the first condition area of the diagnostics area look quite different.

RESIGNAL with a Condition Value and Optional New Signal Information`RESIGNAL` with a condition value means “push a condition into the current diagnostics area.” If the `SET`clause is present, it also changes the error information.

```
RESIGNAL condition_value
```

Condition Handling

```
[SET signal_information_item [, signal_information_item] ...];
```

This form of `RESIGNAL` restores the last diagnostics area and makes it the current diagnostics area. That is, it “pops” the diagnostics area stack, which is the same as what a simple `RESIGNAL` alone would do.

However, it also changes the diagnostics area depending on the condition value or signal information.

Example:

```
DROP TABLE IF EXISTS xx;
delimiter //
CREATE PROCEDURE p ()
BEGIN
DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
SET @error_count = @error_count + 1;
IF @a = 0 THEN RESIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=5; END IF;
END;
DROP TABLE xx;
END//
delimiter ;
SET @error_count = 0;
SET @a = 0;
SET @@max_error_count = 2;
CALL p();
SHOW ERRORS;
```

This is similar to the previous example, and the effects are the same, except that if `RESIGNAL` happens,the current condition area looks different at the end. (The reason the condition adds to rather than replaces the existing condition is the use of a condition value.)The `RESIGNAL` statement includes a condition value (`SQLSTATE '45000'`), so it adds a new condition area, resulting in a diagnostics area stack that looks like this:

```
DA 1. (condition 2) ERROR 1051 (42S02): Unknown table 'xx'
(condition 1) ERROR 5 (45000) Unknown table 'xx'
```

The result of `CALL p()` and `SHOW ERRORS` for this example is:

```
mysql> CALL p();
ERROR 5 (45000): Unknown table 'xx'
mysql> SHOW ERRORS;
+-------+------+----------------------------------+
| Level | Code | Message                          |
+-------+------+----------------------------------+
| Error | 1051 | Unknown table 'xx'               |
| Error |    5 | Unknown table 'xx'               |
+-------+------+----------------------------------+
```

RESIGNAL Requires Condition Handler Context All forms of `RESIGNAL` require that the current context be a condition handler. Otherwise, `RESIGNAL` is illegal and a `RESIGNAL when handler not active` error occurs. For example:

```
mysql> CREATE PROCEDURE p () RESIGNAL;
Query OK, 0 rows affected (0.00 sec)
mysql> CALL p();
ERROR 1645 (0K000): RESIGNAL when handler not active
```

Here is a more difficult example:

```
delimiter //
CREATE FUNCTION f () RETURNS INT
```

Condition Handling

```
BEGIN
RESIGNAL;
RETURN 5;
END//
CREATE PROCEDURE p ()
BEGIN
DECLARE EXIT HANDLER FOR SQLEXCEPTION SET @a=f();
SIGNAL SQLSTATE '55555';
END//
delimiter ;
CALL p();
```

`RESIGNAL` occurs within the stored function `f()`. Although `f()` itself is invoked within the context of the`EXIT` handler, execution within `f()` has its own context, which is not handler context. Thus, `RESIGNAL`within `f()` results in a “handler not active” error.

In MySQL 5.5, handler scope rules are less developed. `f()` is considered to execute within handler context and `RESIGNAL` within `f()` is legal.

#### 13.6.7.5 SIGNAL Statement

```
SIGNAL condition_value
[SET signal_information_item
[, signal_information_item] ...]
condition_value: {
SQLSTATE [VALUE] sqlstate_value
| condition_name
}
signal_information_item:
condition_information_item_name = simple_value_specification
condition_information_item_name: {
CLASS_ORIGIN
| SUBCLASS_ORIGIN
| MESSAGE_TEXT
| MYSQL_ERRNO
| CONSTRAINT_CATALOG
| CONSTRAINT_SCHEMA
| CONSTRAINT_NAME
| CATALOG_NAME
| SCHEMA_NAME
| TABLE_NAME
| COLUMN_NAME
| CURSOR_NAME
}
condition_name, simple_value_specification:
(see following discussion)
```

`SIGNAL` is the way to “return” an error. `SIGNAL` provides error information to a handler, to an outer portion of the application, or to the client. Also, it provides control over the error's characteristics (error number,`SQLSTATE` value, message). Without `SIGNAL`, it is necessary to resort to workarounds such as deliberately referring to a nonexistent table to cause a routine to return an error.

No privileges are required to execute the `SIGNAL` statement.

To retrieve information from the diagnostics area, use the `GET DIAGNOSTICS` statement (see Section 13.6.7.3, “GET DIAGNOSTICS Statement”). For information about the diagnostics area, see Section 13.6.7.7, “The MySQL Diagnostics Area”.

- SIGNAL Overview

Condition Handling

- Signal Condition Information Items
- Effect of Signals on Handlers, Cursors, and Statements

SIGNAL Overview The `condition_value` in a `SIGNAL` statement indicates the error value to be returned. It can be an`SQLSTATE` value (a 5-character string literal) or a `condition_name` that refers to a named condition previously defined with `DECLARE ... CONDITION` (see Section 13.6.7.1, “DECLARE ... CONDITION Statement”).

An `SQLSTATE` value can indicate errors, warnings, or “not found.” The first two characters of the value indicate its error class, as discussed in Signal Condition Information Items. Some signal values cause statement termination; see Effect of Signals on Handlers, Cursors, and Statements.

The `SQLSTATE` value for a `SIGNAL` statement should not start with `'00'` because such values indicate success and are not valid for signaling an error. This is true whether the `SQLSTATE` value is specified directly in the `SIGNAL` statement or in a named condition referred to in the statement. If the value is invalid,a `Bad SQLSTATE` error occurs.

To signal a generic `SQLSTATE` value, use `'45000'`, which means “unhandled user-defined exception.”The `SIGNAL` statement optionally includes a `SET` clause that contains multiple signal items, in a list of`condition_information_item_name` = `simple_value_specification` assignments, separated by commas.

Each `condition_information_item_name` may be specified only once in the `SET` clause. Otherwise,a `Duplicate condition information item` error occurs.

Valid `simple_value_specification` designators can be specified using stored procedure or function parameters, stored program local variables declared with `DECLARE`, user-defined variables, system variables, or literals. A character literal may include a `_charset` introducer.

For information about permissible `condition_information_item_name` values, see Signal Condition Information Items.

The following procedure signals an error or warning depending on the value of `pval`, its input parameter:

```
CREATE PROCEDURE p (pval INT)
BEGIN
DECLARE specialty CONDITION FOR SQLSTATE '45000';
IF pval = 0 THEN
SIGNAL SQLSTATE '01000';
ELSEIF pval = 1 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'An error occurred';
ELSEIF pval = 2 THEN
SIGNAL specialty
SET MESSAGE_TEXT = 'An error occurred';
ELSE
SIGNAL SQLSTATE '01000'
SET MESSAGE_TEXT = 'A warning occurred', MYSQL_ERRNO = 1000;
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'An error occurred', MYSQL_ERRNO = 1001;
END IF;
END;
```

If `pval` is 0, `p()` signals a warning because `SQLSTATE` values that begin with `'01'` are signals in the warning class. The warning does not terminate the procedure, and can be seen with `SHOW WARNINGS`after the procedure returns.

Condition Handling If `pval` is 1, `p()` signals an error and sets the `MESSAGE_TEXT` condition information item. The error terminates the procedure, and the text is returned with the error information.

If `pval` is 2, the same error is signaled, although the `SQLSTATE` value is specified using a named condition in this case.

If `pval` is anything else, `p()` first signals a warning and sets the message text and error number condition information items. This warning does not terminate the procedure, so execution continues and `p()` then signals an error. The error does terminate the procedure. The message text and error number set by the warning are replaced by the values set by the error, which are returned with the error information.

`SIGNAL` is typically used within stored programs, but it is a MySQL extension that it is permitted outside handler context. For example, if you invoke the `mysql` client program, you can enter any of these statements at the prompt:

```
SIGNAL SQLSTATE '77777';
CREATE TRIGGER t_bi BEFORE INSERT ON t
FOR EACH ROW SIGNAL SQLSTATE '77777';
CREATE EVENT e ON SCHEDULE EVERY 1 SECOND
DO SIGNAL SQLSTATE '77777';
```

`SIGNAL` executes according to the following rules:If the `SIGNAL` statement indicates a particular `SQLSTATE` value, that value is used to signal the condition specified. Example:

```
CREATE PROCEDURE p (divisor INT)
BEGIN
IF divisor = 0 THEN
SIGNAL SQLSTATE '22012';
END IF;
END;
```

If the `SIGNAL` statement uses a named condition, the condition must be declared in some scope that applies to the `SIGNAL` statement, and must be defined using an `SQLSTATE` value, not a MySQL error number. Example:

```
CREATE PROCEDURE p (divisor INT)
BEGIN
DECLARE divide_by_zero CONDITION FOR SQLSTATE '22012';
IF divisor = 0 THEN
SIGNAL divide_by_zero;
END IF;
END;
```

If the named condition does not exist in the scope of the `SIGNAL` statement, an `Undefined CONDITION`error occurs.

If `SIGNAL` refers to a named condition that is defined with a MySQL error number rather than an

```
SQLSTATE value, a SIGNAL/RESIGNAL can only use a CONDITION defined with SQLSTATE
```

error occurs. The following statements cause that error because the named condition is associated with a MySQL error number:

```
DECLARE no_such_table CONDITION FOR 1051;
SIGNAL no_such_table;
```

If a condition with a given name is declared multiple times in different scopes, the declaration with the most local scope applies. Consider the following procedure:Condition Handling

```
CREATE PROCEDURE p (divisor INT)
BEGIN
DECLARE my_error CONDITION FOR SQLSTATE '45000';
IF divisor = 0 THEN
BEGIN
DECLARE my_error CONDITION FOR SQLSTATE '22012';
SIGNAL my_error;
END;
END IF;
SIGNAL my_error;
END;
```

If `divisor` is 0, the first `SIGNAL` statement executes. The innermost `my_error` condition declaration applies, raising `SQLSTATE` `'22012'`.

If `divisor` is not 0, the second `SIGNAL` statement executes. The outermost `my_error` condition declaration applies, raising `SQLSTATE` `'45000'`.

For information about how the server chooses handlers when a condition occurs, see Section 13.6.7.6,“Scope Rules for Handlers”.

Signals can be raised within exception handlers:

```
CREATE PROCEDURE p ()
BEGIN
DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
SIGNAL SQLSTATE VALUE '99999'
SET MESSAGE_TEXT = 'An error occurred';
END;
DROP TABLE no_such_table;
END;
```

`CALL p()` reaches the `DROP TABLE` statement. There is no table named `no_such_table`, so the error handler is activated. The error handler destroys the original error (“no such table”) and makes a new error with `SQLSTATE` `'99999'` and message `An error occurred`.

Signal Condition Information Items The following table lists the names of diagnostics area condition information items that can be set in a`SIGNAL` (or `RESIGNAL`) statement. All items are standard SQL except `MYSQL_ERRNO`, which is a MySQL extension. For more information about these items see Section 13.6.7.7, “The MySQL Diagnostics Area”.

```
Item Name             Definition
---------             ----------
CLASS_ORIGIN          VARCHAR(64)
SUBCLASS_ORIGIN       VARCHAR(64)
CONSTRAINT_CATALOG    VARCHAR(64)
CONSTRAINT_SCHEMA     VARCHAR(64)
CONSTRAINT_NAME       VARCHAR(64)
CATALOG_NAME          VARCHAR(64)
SCHEMA_NAME           VARCHAR(64)
TABLE_NAME            VARCHAR(64)
COLUMN_NAME           VARCHAR(64)
CURSOR_NAME           VARCHAR(64)
MESSAGE_TEXT          VARCHAR(128)
MYSQL_ERRNO           SMALLINT UNSIGNED
```

The character set for character items is UTF-8.

It is illegal to assign `NULL` to a condition information item in a `SIGNAL` statement.

Condition Handling A `SIGNAL` statement always specifies an `SQLSTATE` value, either directly, or indirectly by referring to a named condition defined with an `SQLSTATE` value. The first two characters of an `SQLSTATE` value are its class, and the class determines the default value for the condition information items:

- Class = `'00'` (success)

Illegal. `SQLSTATE` values that begin with `'00'` indicate success and are not valid for `SIGNAL`.

- Class = `'01'` (warning)

```
MESSAGE_TEXT = 'Unhandled user-defined warning condition';
MYSQL_ERRNO = ER_SIGNAL_WARN
```

- Class = `'02'` (not found)

```
MESSAGE_TEXT = 'Unhandled user-defined not found condition';
MYSQL_ERRNO = ER_SIGNAL_NOT_FOUND
```

- Class > `'02'` (exception)

```
MESSAGE_TEXT = 'Unhandled user-defined exception condition';
MYSQL_ERRNO = ER_SIGNAL_EXCEPTION
```

For legal classes, the other condition information items are set as follows:

```
CLASS_ORIGIN = SUBCLASS_ORIGIN = '';
CONSTRAINT_CATALOG = CONSTRAINT_SCHEMA = CONSTRAINT_NAME = '';
CATALOG_NAME = SCHEMA_NAME = TABLE_NAME = COLUMN_NAME = '';
CURSOR_NAME = '';
```

The error values that are accessible after `SIGNAL` executes are the `SQLSTATE` value raised by the `SIGNAL`statement and the `MESSAGE_TEXT` and `MYSQL_ERRNO` items. These values are available from the C API:

- `mysql_sqlstate()` returns the `SQLSTATE` value.
- `mysql_errno()` returns the `MYSQL_ERRNO` value.
- `mysql_error()` returns the `MESSAGE_TEXT` value.

At the SQL level, the output from `SHOW WARNINGS` and `SHOW ERRORS` indicates the `MYSQL_ERRNO` and`MESSAGE_TEXT` values in the `Code` and `Message` columns.

To retrieve information from the diagnostics area, use the `GET DIAGNOSTICS` statement (see Section 13.6.7.3, “GET DIAGNOSTICS Statement”). For information about the diagnostics area, see Section 13.6.7.7, “The MySQL Diagnostics Area”.

Effect of Signals on Handlers, Cursors, and Statements Signals have different effects on statement execution depending on the signal class. The class determines how severe an error is. MySQL ignores the value of the `sql_mode` system variable; in particular, strict SQL mode does not matter. MySQL also ignores `IGNORE`: The intent of `SIGNAL` is to raise a user-generated error explicitly, so a signal is never ignored.

In the following descriptions, “unhandled” means that no handler for the signaled `SQLSTATE` value has been defined with `DECLARE ... HANDLER`.

- Class = `'00'` (success)

Illegal. `SQLSTATE` values that begin with `'00'` indicate success and are not valid for `SIGNAL`.

- Class = `'01'` (warning)

Condition Handling The value of the `warning_count` system variable goes up. `SHOW WARNINGS` shows the signal.

`SQLWARNING` handlers catch the signal.

Warnings cannot be returned from stored functions because the `RETURN` statement that causes the function to return clears the diagnostic area. The statement thus clears any warnings that may have been present there (and resets `warning_count` to 0).

- Class = `'02'` (not found)

`NOT FOUND` handlers catch the signal. There is no effect on cursors. If the signal is unhandled in a stored function, statements end.

- Class > `'02'` (exception)

`SQLEXCEPTION` handlers catch the signal. If the signal is unhandled in a stored function, statements end.

- Class = `'40'`

Treated as an ordinary exception.

#### 13.6.7.6 Scope Rules for Handlers

A stored program may include handlers to be invoked when certain conditions occur within the program.

The applicability of each handler depends on its location within the program definition and on the condition or conditions that it handles:

- A handler declared in a `BEGIN ... END` block is in scope only for the SQL statements following the

handler declarations in the block. If the handler itself raises a condition, it cannot handle that condition,nor can any other handlers declared in the block. In the following example, handlers `H1` and `H2` are in scope for conditions raised by statements `stmt1` and `stmt2`. But neither `H1` nor `H2` are in scope for conditions raised in the body of `H1` or `H2`.

```
BEGIN -- outer block
DECLARE EXIT HANDLER FOR ...;  -- handler H1
DECLARE EXIT HANDLER FOR ...;  -- handler H2
stmt1;
stmt2;
END;
```

- A handler is in scope only for the block in which it is declared, and cannot be activated for conditions

occurring outside that block. In the following example, handler `H1` is in scope for `stmt1` in the inner block, but not for `stmt2` in the outer block:

```
BEGIN -- outer block
BEGIN -- inner block
DECLARE EXIT HANDLER FOR ...;  -- handler H1
stmt1;
END;
stmt2;
END;
```

- A handler can be specific or general. A specific handler is for a MySQL error code, `SQLSTATE` value,

or condition name. A general handler is for a condition in the `SQLWARNING`, `SQLEXCEPTION`, or `NOT``FOUND` class. Condition specificity is related to condition precedence, as described later.

Multiple handlers can be declared in different scopes and with different specificities. For example, there might be a specific MySQL error code handler in an outer block, and a general `SQLWARNING` handler in Condition Handling an inner block. Or there might be handlers for a specific MySQL error code and the general `SQLWARNING`class in the same block.

Whether a handler is activated depends not only on its own scope and condition value, but on what other handlers are present. When a condition occurs in a stored program, the server searches for applicable handlers in the current scope (current `BEGIN ... END` block). If there are no applicable handlers, the search continues outward with the handlers in each successive containing scope (block). When the server finds one or more applicable handlers at a given scope, it chooses among them based on condition precedence:

- A MySQL error code handler takes precedence over an `SQLSTATE` value handler.
- An `SQLSTATE` value handler takes precedence over general `SQLWARNING`, `SQLEXCEPTION`, or `NOT`

`FOUND` handlers.

- An `SQLEXCEPTION` handler takes precedence over an `SQLWARNING` handler.
- It is possible to have several applicable handlers with the same precedence. For example, a statement

could generate multiple warnings with different error codes, for each of which an error-specific handler exists. In this case, the choice of which handler the server activates is nondeterministic, and may change depending on the circumstances under which the condition occurs.

One implication of the handler selection rules is that if multiple applicable handlers occur in different scopes, handlers with the most local scope take precedence over handlers in outer scopes, even over those for more specific conditions.

If there is no appropriate handler when a condition occurs, the action taken depends on the class of the condition:

- For `SQLEXCEPTION` conditions, the stored program terminates at the statement that raised the condition,

as if there were an `EXIT` handler. If the program was called by another stored program, the calling program handles the condition using the handler selection rules applied to its own handlers.

- For `SQLWARNING` conditions, the program continues executing, as if there were a `CONTINUE` handler.
- For `NOT FOUND` conditions, if the condition was raised normally, the action is `CONTINUE`. If it was raised

by `SIGNAL` or `RESIGNAL`, the action is `EXIT`.

The following examples demonstrate how MySQL applies the handler selection rules.

This procedure contains two handlers, one for the specific `SQLSTATE` value (`'42S02'`) that occurs for attempts to drop a nonexistent table, and one for the general `SQLEXCEPTION` class:

```
CREATE PROCEDURE p1()
BEGIN
DECLARE CONTINUE HANDLER FOR SQLSTATE '42S02'
SELECT 'SQLSTATE handler was activated' AS msg;
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
SELECT 'SQLEXCEPTION handler was activated' AS msg;
DROP TABLE test.t;
END;
```

Both handlers are declared in the same block and have the same scope. However, `SQLSTATE` handlers take precedence over `SQLEXCEPTION` handlers, so if the table t is nonexistent, the `DROP TABLE`statement raises a condition that activates the `SQLSTATE` handler:

```
mysql> CALL p1();
+--------------------------------+
| msg                            |
```

Condition Handling

```
+--------------------------------+
| SQLSTATE handler was activated |
+--------------------------------+
```

This procedure contains the same two handlers. But this time, the `DROP TABLE` statement and`SQLEXCEPTION` handler are in an inner block relative to the `SQLSTATE` handler:

```
CREATE PROCEDURE p2()
BEGIN -- outer block
DECLARE CONTINUE HANDLER FOR SQLSTATE '42S02'
SELECT 'SQLSTATE handler was activated' AS msg;
BEGIN -- inner block
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
SELECT 'SQLEXCEPTION handler was activated' AS msg;
DROP TABLE test.t; -- occurs within inner block
END;
END;
```

In this case, the handler that is more local to where the condition occurs takes precedence. The`SQLEXCEPTION` handler activates, even though it is more general than the `SQLSTATE` handler:

```
mysql> CALL p2();
+------------------------------------+
| msg                                |
+------------------------------------+
| SQLEXCEPTION handler was activated |
+------------------------------------+
```

In this procedure, one of the handlers is declared in a block inner to the scope of the `DROP TABLE`statement:

```
CREATE PROCEDURE p3()
BEGIN -- outer block
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
SELECT 'SQLEXCEPTION handler was activated' AS msg;
BEGIN -- inner block
DECLARE CONTINUE HANDLER FOR SQLSTATE '42S02'
SELECT 'SQLSTATE handler was activated' AS msg;
END;
DROP TABLE test.t; -- occurs within outer block
END;
```

Only the `SQLEXCEPTION` handler applies because the other one is not in scope for the condition raised by the `DROP TABLE`:

```
mysql> CALL p3();
+------------------------------------+
| msg                                |
+------------------------------------+
| SQLEXCEPTION handler was activated |
+------------------------------------+
```

In this procedure, both handlers are declared in a block inner to the scope of the `DROP TABLE` statement:

```
CREATE PROCEDURE p4()
BEGIN -- outer block
BEGIN -- inner block
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
SELECT 'SQLEXCEPTION handler was activated' AS msg;
DECLARE CONTINUE HANDLER FOR SQLSTATE '42S02'
SELECT 'SQLSTATE handler was activated' AS msg;
END;
DROP TABLE test.t; -- occurs within outer block
```

Condition Handling

```
END;
```

Neither handler applies because they are not in scope for the `DROP TABLE`. The condition raised by the statement goes unhandled and terminates the procedure with an error:

```
mysql> CALL p4();
ERROR 1051 (42S02): Unknown table 'test.t'
```

#### 13.6.7.7 The MySQL Diagnostics Area

SQL statements produce diagnostic information that populates the diagnostics area. Standard SQL has a diagnostics area stack, containing a diagnostics area for each nested execution context. Standard SQL also supports `GET STACKED DIAGNOSTICS` syntax for referring to the second diagnostics area during condition handler execution. MySQL does not support the `STACKED` keyword until MySQL 5.7. In MySQL

5.6, there is a single diagnostics area containing information from the most recent statement that wrote to it.

The following discussion describes the structure of the diagnostics area in MySQL, the information items recognized by MySQL and how statements clear and set the diagnostics area.

- Diagnostics Area Structure
- Diagnostics Area Information Items
- How the Diagnostics Area is Cleared and Populated
- Diagnostics Area-Related System Variables

Diagnostics Area Structure The diagnostics area contains two kinds of information:

- Statement information, such as the number of conditions that occurred or the affected-rows count.
- Condition information, such as the error code and message. If a statement raises multiple conditions,

this part of the diagnostics area has a condition area for each one. If a statement raises no conditions,this part of the diagnostics area is empty.

For a statement that produces three conditions, the diagnostics area contains statement and condition information like this:

```
Statement information:
row count
... other statement information items ...
Condition area list:
Condition area 1:
error code for condition 1
error message for condition 1
... other condition information items ...
Condition area 2:
error code for condition 2:
error message for condition 2
... other condition information items ...
Condition area 3:
error code for condition 3
error message for condition 3
... other condition information items ...
```

Diagnostics Area Information Items The diagnostics area contains statement and condition information items. Numeric items are integers. The character set for character items is UTF-8. No item can be `NULL`. If a statement or condition item is not Condition Handling set by a statement that populates the diagnostics area, its value is 0 or the empty string, depending on the item data type.

The statement information part of the diagnostics area contains these items:

- `NUMBER`: An integer indicating the number of condition areas that have information.
- `ROW_COUNT`: An integer indicating the number of rows affected by the statement. `ROW_COUNT` has the

same value as the `ROW_COUNT()` function (see Section 12.16, “Information Functions”).

The condition information part of the diagnostics area contains a condition area for each condition.

Condition areas are numbered from 1 to the value of the `NUMBER` statement condition item. If `NUMBER` is 0,there are no condition areas.

Each condition area contains the items in the following list. All items are standard SQL except`MYSQL_ERRNO`, which is a MySQL extension. The definitions apply for conditions generated other than by a signal (that is, by a `SIGNAL` or `RESIGNAL` statement). For nonsignal conditions, MySQL populates only those condition items not described as always empty. The effects of signals on the condition area are described later.

- `CLASS_ORIGIN`: A string containing the class of the `RETURNED_SQLSTATE` value. If the

`RETURNED_SQLSTATE` value begins with a class value defined in SQL standards document ISO 9075-2(section 24.1, SQLSTATE), `CLASS_ORIGIN` is `'ISO 9075'`. Otherwise, `CLASS_ORIGIN` is `'MySQL'`.

- `SUBCLASS_ORIGIN`: A string containing the subclass of the `RETURNED_SQLSTATE` value. If

```
CLASS_ORIGIN is 'ISO 9075' or RETURNED_SQLSTATE ends with '000', SUBCLASS_ORIGIN is
```

`'ISO 9075'`. Otherwise, `SUBCLASS_ORIGIN` is `'MySQL'`.

- `RETURNED_SQLSTATE`: A string that indicates the `SQLSTATE` value for the condition.
- `MESSAGE_TEXT`: A string that indicates the error message for the condition.
- `MYSQL_ERRNO`: An integer that indicates the MySQL error code for the condition.
- `CONSTRAINT_CATALOG`, `CONSTRAINT_SCHEMA`, `CONSTRAINT_NAME`: Strings that indicate the catalog,

schema, and name for a violated constraint. They are always empty.

- `CATALOG_NAME`, `SCHEMA_NAME`, `TABLE_NAME`, `COLUMN_NAME`: Strings that indicate the catalog,

schema, table, and column related to the condition. They are always empty.

- `CURSOR_NAME`: A string that indicates the cursor name. This is always empty.

For the `RETURNED_SQLSTATE`, `MESSAGE_TEXT`, and `MYSQL_ERRNO` values for particular errors, see Server Error Message Reference.

If a `SIGNAL` (or `RESIGNAL`) statement populates the diagnostics area, its `SET` clause can assign to any condition information item except `RETURNED_SQLSTATE` any value that is legal for the item data type.

`SIGNAL` also sets the `RETURNED_SQLSTATE` value, but not directly in its `SET` clause. That value comes from the `SIGNAL` statement `SQLSTATE` argument.

`SIGNAL` also sets statement information items. It sets `NUMBER` to 1. It sets `ROW_COUNT` to −1 for errors and 0 otherwise.

How the Diagnostics Area is Cleared and Populated Most nondiagnostic SQL statements populate the diagnostics area automatically, and its contents can be set explicitly with the `SIGNAL` and `RESIGNAL` statements. The diagnostics area can be examined with `GET`Condition Handling`DIAGNOSTICS` to extract specific items, or with `SHOW WARNINGS` or `SHOW ERRORS` to see conditions or errors.

SQL statements clear and set the diagnostics area as follows:

- When the server starts executing a statement after parsing it, it clears the diagnostics area for

nondiagnostic statements that use tables. Diagnostic statements do not clear the diagnostics area.

These statements are diagnostic:

```
- GET DIAGNOSTICS
- SHOW ERRORS
- SHOW WARNINGS
```

- If a statement raises a condition, the diagnostics area is cleared of conditions that belong to earlier

statements. The exception is that conditions raised by `GET DIAGNOSTICS` and `RESIGNAL` are added to the diagnostics area without clearing it.

Thus, even a statement that does not normally clear the diagnostics area when it begins executing clears it if the statement raises a condition.

The following example shows the effect of various statements on the diagnostics area, using `SHOW``WARNINGS` to display information about conditions stored there.

This `DROP TABLE` statement uses a table, so it clears the diagnostics area and populates it when the condition occurs:

```
mysql> DROP TABLE IF EXISTS test.no_such_table;
Query OK, 0 rows affected, 1 warning (0.01 sec)
mysql> SHOW WARNINGS;
+-------+------+------------------------------------+
| Level | Code | Message                            |
+-------+------+------------------------------------+
| Note  | 1051 | Unknown table 'test.no_such_table' |
+-------+------+------------------------------------+
1 row in set (0.00 sec)
```

This `SET` statement does not use tables and does not generate warnings, so it leaves the diagnostics area unchanged:

```
mysql> SET @x = 1;
Query OK, 0 rows affected (0.00 sec)
mysql> SHOW WARNINGS;
+-------+------+------------------------------------+
| Level | Code | Message                            |
+-------+------+------------------------------------+
| Note  | 1051 | Unknown table 'test.no_such_table' |
+-------+------+------------------------------------+
1 row in set (0.00 sec)
```

This `SET` statement generates an error, so it clears and populates the diagnostics area:

```
mysql> SET @x = @@x;
ERROR 1193 (HY000): Unknown system variable 'x'
mysql> SHOW WARNINGS;
+-------+------+-----------------------------+
| Level | Code | Message                     |
+-------+------+-----------------------------+
| Error | 1193 | Unknown system variable 'x' |
```

Condition Handling

```
+-------+------+-----------------------------+
1 row in set (0.00 sec)
```

The previous `SET` statement produced a single condition, so 1 is the only valid condition number for `GET``DIAGNOSTICS` at this point. The following statement uses a condition number of 2, which produces a warning that is added to the diagnostics area without clearing it:

```
mysql> GET DIAGNOSTICS CONDITION 2 @p = MESSAGE_TEXT;
Query OK, 0 rows affected, 1 warning (0.00 sec)
mysql> SHOW WARNINGS;
+-------+------+------------------------------+
| Level | Code | Message                      |
+-------+------+------------------------------+
| Error | 1193 | Unknown system variable 'xx' |
| Error | 1753 | Invalid condition number     |
+-------+------+------------------------------+
2 rows in set (0.00 sec)
```

Now there are two conditions in the diagnostics area, so the same `GET DIAGNOSTICS` statement succeeds:

```
mysql> GET DIAGNOSTICS CONDITION 2 @p = MESSAGE_TEXT;
Query OK, 0 rows affected (0.00 sec)
mysql> SELECT @p;
+--------------------------+
| @p                       |
+--------------------------+
| Invalid condition number |
+--------------------------+
1 row in set (0.01 sec)
```

Diagnostics Area-Related System Variables Certain system variables control or are related to some aspects of the diagnostics area:

- `max_error_count` controls the number of condition areas in the diagnostics area. If more conditions

than this occur, MySQL silently discards information for the excess conditions. (Conditions added by`RESIGNAL` are always added, with older conditions being discarded as necessary to make room.)

- `warning_count` indicates the number of conditions that occurred. This includes errors, warnings, and

notes. Normally, `NUMBER` and `warning_count` are the same. However, as the number of conditions generated exceeds `max_error_count`, the value of `warning_count` continues to rise whereas`NUMBER` remains capped at `max_error_count` because no additional conditions are stored in the diagnostics area.

- `error_count` indicates the number of errors that occurred. This value includes “not found” and

exception conditions, but excludes warnings and notes. Like `warning_count`, its value can exceed

```
max_error_count.
```

- If the `sql_notes` system variable is set to 0, notes are not stored and do not increment

```
warning_count.
```

Example: If `max_error_count` is 10, the diagnostics area can contain a maximum of 10 condition areas.

Suppose that a statement raises 20 conditions, 12 of which are errors. In that case, the diagnostics area contains the first 10 conditions, `NUMBER` is 10, `warning_count` is 20, and `error_count` is 12.

Changes to the value of `max_error_count` have no effect until the next attempt to modify the diagnostics area. If the diagnostics area contains 10 condition areas and `max_error_count` is set to 5, that has no immediate effect on the size or content of the diagnostics area.

Database Administration Statements Before MySQL 5.6, statement information items are not available directly. `ROW_COUNT` can be obtained by calling the `ROW_COUNT()` function. `NUMBER` is approximated by the value of the `warning_count` system variable. However, whereas `NUMBER` is capped to the value of `max_error_count`, `warning_count` is not.

#### 13.6.7.8 Condition Handling and OUT or INOUT Parameters

If a stored procedure exits with an unhandled exception, modified values of `OUT` and `INOUT` parameters are not propogated back to the caller.

If an exception is handled by a `CONTINUE` or `EXIT` handler that contains a `RESIGNAL` statement,execution of `RESIGNAL` pops the Diagnostics Area stack, thus signalling the exception (that is, the information that existed before entry into the handler). If the exception is an error, the values of `OUT` and`INOUT` parameters are not propogated back to the caller.

#### 13.6.7.9 Restrictions on Condition Handling

`SIGNAL`, `RESIGNAL`, and `GET DIAGNOSTICS` are not permissible as prepared statements. For example,this statement is invalid:

```
PREPARE stmt1 FROM 'SIGNAL SQLSTATE "02000"';
```

`SQLSTATE` values in class `'04'` are not treated specially. They are handled the same as other exceptions.

Standard SQL has a diagnostics area stack, containing a diagnostics area for each nested execution context. Standard SQL syntax includes `GET STACKED DIAGNOSTICS` for referring to stacked areas.

MySQL does not support the `STACKED` keyword because there is a single diagnostics area containing information from the most recent statement that wrote to it. See also Section 13.6.7.7, “The MySQL Diagnostics Area”.

In standard SQL, the first condition relates to the `SQLSTATE` value returned for the previous SQL statement. In MySQL, this is not guaranteed, so to get the main error, you cannot do this:

```
GET DIAGNOSTICS CONDITION 1 @errno = MYSQL_ERRNO;
```

Instead, do this:

```
GET DIAGNOSTICS @cno = NUMBER;
GET DIAGNOSTICS CONDITION @cno @errno = MYSQL_ERRNO;
```

## 13.7 Database Administration Statements

### 13.7.1 Account Management Statements

MySQL account information is stored in the tables of the `mysql` system database. This database and the access control system are discussed extensively in Chapter 5, MySQL Server Administration, which you should consult for additional details.

Important Some MySQL releases introduce changes to the grant tables to add new privileges or features. To make sure that you can take advantage of any new capabilities,update your grant tables to the current structure whenever you upgrade MySQL.

See Section 2.11, “Upgrading MySQL”.

When the `read_only` system variable is enabled, account-management statements require the `SUPER`privilege, in addition to any other required privileges. This is because they modify tables in the `mysql`system database.

Account Management Statements

#### 13.7.1.1 ALTER USER Statement

```
ALTER USER user_specification [, user_specification] ...
user_specification:
user PASSWORD EXPIRE
```

The `ALTER USER` statement modifies MySQL accounts. An error occurs if you try to modify a nonexistent account.

To use `ALTER USER`, you must have the global `CREATE USER` privilege or the `UPDATE` privilege for the`mysql` system database. When the `read_only` system variable is enabled, `ALTER USER` additionally requires the `SUPER` privilege.

Each account name uses the format described in Section 6.2.4, “Specifying Account Names”. The host name part of the account name, if omitted, defaults to `'%'`. It is also possible to specify `CURRENT_USER` or`CURRENT_USER()` to refer to the account associated with the current session.

For each account, `ALTER USER` expires its password. For example:

```
ALTER USER 'jeffrey'@'localhost' PASSWORD EXPIRE;
```

Password expiration for an account affects the corresponding row of the `mysql.user` system table: The server sets the `password_expired` column to `'Y'`.

A client session operates in restricted mode if the account password has been expired. In restricted mode, operations performed within the session result in an error until the user establishes a new account password:

```
mysql> SELECT 1;
ERROR 1820 (HY000): You must SET PASSWORD before executing this statement
mysql> SET PASSWORD = PASSWORD('new_password');
Query OK, 0 rows affected (0.01 sec)
mysql> SELECT 1;
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.00 sec)
```

This restricted mode of operation permits `SET` statements, which is useful if the account password has a hashing format that requires `old_passwords` to be set to a value different from its default before using

```
SET PASSWORD.
```

It is possible for an administrative user to reset the account password, but any existing sessions for the account remain restricted. A client using the account must disconnect and reconnect before statements can be executed successfully.

Note Although it is possible to “reset” an expired password by setting it to its current value, it is preferable, as a matter of good policy, to choose a different password.

#### 13.7.1.2 CREATE USER Statement

```
CREATE USER
user [auth_option] [, user [auth_option]] ...
```

Account Management Statements

```
user:
(see Section 6.2.4, “Specifying Account Names”)
auth_option: {
IDENTIFIED BY [PASSWORD] 'auth_string'
| IDENTIFIED WITH auth_plugin [AS 'auth_string']
}
```

The `CREATE USER` statement creates new MySQL accounts. An error occurs if you try to create an account that already exists.

To use `CREATE USER`, you must have the global `CREATE USER` privilege, or the `INSERT` privilege for the`mysql` system database. When the `read_only` system variable is enabled, `CREATE USER` additionally requires the `SUPER` privilege.

Important Under some circumstances, `CREATE USER` may be recorded in server logs or on the client side in a history file such as `~/.mysql_history`, which means that cleartext passwords may be read by anyone having read access to that information.

For information about the conditions under which this occurs for the server logs and how to control it, see Section 6.1.2.3, “Passwords and Logging”. For similar information about client-side logging, see Section 4.5.1.3, “mysql Client Logging”.

For each account, `CREATE USER` creates a new row in the `mysql.user` system table with no privileges and assigns the account an authentication plugin. Depending on the syntax used, `CREATE USER` may also assign the account a password.

An account when first created has no privileges. To assign privileges, use the `GRANT` statement.

Each `user` value naming an account may be followed by an optional `auth_option` value that specifies how authentication occurs for clients that use the account. This part of `CREATE USER` syntax is shared with`GRANT`, so the description here applies to `GRANT` as well.

Each account name uses the format described in Section 6.2.4, “Specifying Account Names”. For example:

```
CREATE USER 'jeffrey'@'localhost' IDENTIFIED BY 'password';
```

The host name part of the account name, if omitted, defaults to `'%'`.

The server assigns an authentication plugin and password to each account as follows, depending on whether the user specification clause includes `IDENTIFIED BY` or `IDENTIFIED WITH` to specify authentication information:

- With `IDENTIFIED BY`, the server assigns the plugin implicitly. The `'auth_string'` value is cleartext

and is passed to the plugin for possible hashing. The result returned by the plugin is stored as the password. A plugin may use the value as specified, in which case no hashing occurs. If the optional`PASSWORD` keyword is given, the behavior is the same except that if the plugin requires a hashed string,the string is assumed to be already hashed in the format the plugin requires, and is stored as is as the password.

- With `IDENTIFIED WITH`, the server assigns the specified plugin and the account has no password. If

the optional `AS 'auth_string'` clause is given, the string is stored as is as the password. If the plugin requires a hashed string, the string is assumed to be already hashed in the format the plugin requires.

- With neither `IDENTIFIED BY` nor `IDENTIFIED WITH`, the server assigns the plugin implicitly and the

account has no password.

Account Management Statements If the account has no password, the password information in the account row in the `mysql.user` table remains empty, which is insecure. To set the password, use `SET PASSWORD`. See Section 13.7.1.7, “SET PASSWORD Statement”.

For implicit plugin assignment, the default plugin becomes the value of the `plugin` column in the account's`mysql.user` system table row. The default plugin is `mysql_native_password` unless the `--default-``authentication-plugin` option is set otherwise at server startup.

For client connections that use a given account, the server invokes the authentication plugin assigned to the account and the client must provide credentials as required by the authentication method that the plugin implements. If the server cannot find the plugin, either at account-creation time or connect time, an error occurs.

If an account's `mysql.user` table row has a nonempty `plugin` column:

- The server authenticates client connection attempts using the named plugin.
- Changes to the account password using `SET PASSWORD` with `PASSWORD()` must be made with

the `old_passwords` system variable set to the value required by the authentication plugin, so that`PASSWORD()` uses the appropriate password hashing method. If the plugin is `mysql_old_password`,the password can also be changed using `SET PASSWORD` with `OLD_PASSWORD()`, which uses pre-4.1 password hashing regardless of the value of `old_passwords`.

If an account's `mysql.user` table row has an empty `plugin` column:

- The server authenticates client connection attempts using the `mysql_native_password` or

`mysql_old_password` authentication plugin, depending on the hash format of the password stored in the `Password` column.

- Changes to the account password using `SET PASSWORD` can be made with `PASSWORD()`,

with `old_passwords` set to 0 or 1 for 4.1 or pre-4.1 password hashing, respectively, or with`OLD_PASSWORD()`, which uses pre-4.1 password hashing regardless of the value of `old_passwords`.

`CREATE USER` examples:

- To specify an authentication plugin for an account, use `IDENTIFIED WITH auth_plugin`. The plugin

name can be a quoted string literal or an unquoted name. `'auth_string'` is an optional quoted string literal to pass to the plugin. The plugin interprets the meaning of the string, so its format is plugin specific and it is stored in the `authentication_string` column as given. (This value is meaningful only for plugins that use that column.) Consult the documentation for a given plugin for information about the authentication string values it accepts, if any.

```
CREATE USER 'jeffrey'@'localhost' IDENTIFIED WITH mysql_native_password;
```

The server assigns the given authentication plugin to the account but no password. Clients must provide no password when they connect. However, an account with no password is insecure. To ensure that an account uses a specific authentication plugin and has a password with the corresponding hash format,specify the plugin explicitly with `IDENTIFIED WITH`, then use `SET PASSWORD` to set the password:

```
CREATE USER 'jeffrey'@'localhost' IDENTIFIED WITH mysql_native_password;
SET old_passwords = 0;
SET PASSWORD FOR 'jeffrey'@'localhost' = PASSWORD('password');
```

Changes to the account password using `SET PASSWORD` with `PASSWORD()` must be made with the `old_passwords` system variable set to the value required by the account's authentication plugin, so that `PASSWORD()` uses the appropriate password hashing method. Therefore, to use the`sha256_password` or `mysql_old_password` plugin instead, name that plugin in the `CREATE USER`statement and set `old_passwords` to 2 or 1, respectively, before using `SET PASSWORD`. (Use of Account Management Statements`mysql_old_password` is not recommended. It is deprecated; expect support for it to removed in a future MySQL release.)

- To specify a password for an account at account-creation time, use `IDENTIFIED BY` with the literal

cleartext password value:

```
CREATE USER 'jeffrey'@'localhost' IDENTIFIED BY 'password';
```

The server assigns an authentication plugin to the account implicitly, as described previously, and assigns the given password. Clients must provide the given password when they connect.

If the implicitly assigned plugin is `mysql_native_password`, the `old_passwords` system variable must be set to 0. Otherwise, `CREATE USER` does not hash the password in the format required by the plugin and an error occurs:

```
mysql> SET old_passwords = 1;
mysql> CREATE USER 'jeffrey'@'localhost' IDENTIFIED BY 'password';
ERROR 1827 (HY000): The password hash doesn't have the expected
format. Check if the correct password algorithm is being used with
the PASSWORD() function.
mysql> SET old_passwords = 0;
mysql> CREATE USER 'jeffrey'@'localhost' IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.00 sec)
```

- To avoid specifying the cleartext password if you know its hash value (the value that `PASSWORD()` would

return for the password), specify the hash value preceded by the keyword `PASSWORD`:

```
CREATE USER 'jeffrey'@'localhost'
IDENTIFIED BY PASSWORD '*90E462C37378CED12064BB3388827D2BA3A9B689';
```

The server assigns an authentication plugin to the account implicitly, as described previously, and assigns the given password. The password hash must be in the format required by the assigned plugin.

Clients must provide the password when they connect.

- To enable the user to connect with no password, include no `IDENTIFIED BY` clause:

```
CREATE USER 'jeffrey'@'localhost';
```

The server assigns an authentication plugin to the account implicitly, as described previously, but no password. Clients must provide no password when they connect. However, an account with no password is insecure. To avoid this, use `SET PASSWORD` to set the account password.

As mentioned previously, implicit plugin assignment depends on the default authentication plugin.

Permitted values of `--default-authentication-plugin` are `mysql_native_plugin` and`sha256_password`, but not `mysql_old_password`. This means it is not possible to set the default plugin so as to be able to create an account that uses `mysql_old_password` with `CREATE USER ...``IDENTIFIED BY` syntax. To create an account that uses `mysql_old_password`, use `CREATE``USER ... IDENTIFIED WITH` to name the plugin explicitly, then set the password:

```
CREATE USER 'jeffrey'@'localhost' IDENTIFIED WITH mysql_old_password;
SET old_passwords = 1;
SET PASSWORD FOR 'jeffrey'@'localhost' = PASSWORD('password');
```

However, the preceding procedure is not recommended because `mysql_old_password` is deprecated.

For additional information about setting passwords and authentication plugins, see Section 6.2.9,“Assigning Account Passwords”, and Section 6.2.11, “Pluggable Authentication”.

#### 13.7.1.3 DROP USER Statement

Account Management Statements

```
DROP USER user [, user] ...
```

The `DROP USER` statement removes one or more MySQL accounts and their privileges. It removes privilege rows for the account from all grant tables. An error occurs for accounts that do not exist.

To use `DROP USER`, you must have the global `CREATE USER` privilege, or the `DELETE` privilege for the`mysql` system database. When the `read_only` system variable is enabled, `DROP USER` additionally requires the `SUPER` privilege.

Each account name uses the format described in Section 6.2.4, “Specifying Account Names”. For example:

```
DROP USER 'jeffrey'@'localhost';
```

The host name part of the account name, if omitted, defaults to `'%'`.

Important`DROP USER` does not automatically close any open user sessions. Rather, in the event that a user with an open session is dropped, the statement does not take effect until that user's session is closed. Once the session is closed, the user is dropped, and that user's next attempt to log in fails. This is by design.

`DROP USER` does not automatically drop or invalidate databases or objects within them that the old user created. This includes stored programs or views for which the `DEFINER` attribute names the dropped user.

Attempts to access such objects may produce an error if they execute in definer security context. (For information about security context, see Section 20.6, “Stored Object Access Control”.)

#### 13.7.1.4 GRANT Statement

```
GRANT
priv_type [(column_list)]
[, priv_type [(column_list)]] ...
ON [object_type] priv_level
TO user [auth_option] [, user [auth_option]] ...
[REQUIRE {NONE | tls_option [[AND] tls_option] ...}]
[WITH {GRANT OPTION | resource_option} ...]
GRANT PROXY ON user
TO user [, user] ...
[WITH GRANT OPTION]
object_type: {
TABLE
| FUNCTION
| PROCEDURE
}
priv_level: {
*
| *.*
| db_name.*
| db_name.tbl_name
| tbl_name
| db_name.routine_name
}
user:
(see Section 6.2.4, “Specifying Account Names”)
auth_option: {
IDENTIFIED BY [PASSWORD] 'auth_string'
```

Account Management Statements

```
| IDENTIFIED WITH auth_plugin
| IDENTIFIED WITH auth_plugin AS 'auth_string'
}
tls_option: {
SSL
| X509
| CIPHER 'cipher'
| ISSUER 'issuer'
| SUBJECT 'subject'
}
resource_option: {
| MAX_QUERIES_PER_HOUR count
| MAX_UPDATES_PER_HOUR count
| MAX_CONNECTIONS_PER_HOUR count
| MAX_USER_CONNECTIONS count
}
```

The `GRANT` statement grants privileges to MySQL user accounts. There are several aspects to the `GRANT`statement, described under the following topics:

- GRANT General Overview
- Object Quoting Guidelines
- Account Names and Passwords
- Privileges Supported by MySQL
- Global Privileges
- Database Privileges
- Table Privileges
- Column Privileges
- Stored Routine Privileges
- Proxy User Privileges
- Implicit Account Creation
- Other Account Characteristics
- MySQL and Standard SQL Versions of GRANT

GRANT General Overview The `GRANT` statement grants privileges to MySQL user accounts. `GRANT` also serves to specify other account characteristics such as use of secure connections and limits on access to server resources.

To grant a privilege with `GRANT`, you must have the `GRANT OPTION` privilege, and you must have the privileges that you are granting. (Alternatively, if you have the `UPDATE` privilege for the grant tables in the`mysql` system database, you can grant any account any privilege.) When the `read_only` system variable is enabled, `GRANT` additionally requires the `SUPER` privilege.

The `REVOKE` statement is related to `GRANT` and enables administrators to remove account privileges. See Section 13.7.1.6, “REVOKE Statement”.

Account Management Statements Each account name uses the format described in Section 6.2.4, “Specifying Account Names”. For example:

```
GRANT ALL ON db1.* TO 'jeffrey'@'localhost';
```

The host name part of the account, if omitted, defaults to `'%'`.

Normally, a database administrator first uses `CREATE USER` to create an account, then `GRANT` to define its privileges and characteristics. For example:

```
CREATE USER 'jeffrey'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON db1.* TO 'jeffrey'@'localhost';
GRANT SELECT ON db2.invoice TO 'jeffrey'@'localhost';
GRANT USAGE ON *.* TO 'jeffrey'@'localhost' WITH MAX_QUERIES_PER_HOUR 90;
```

Note Examples shown here include no `IDENTIFIED` clause. It is assumed that you establish passwords with `CREATE USER` at account-creation time to avoid creating insecure accounts.

If an account named in a `GRANT` statement does not already exist, `GRANT` may create it under the conditions described later in the discussion of the `NO_AUTO_CREATE_USER` SQL mode.

From the `mysql` program, `GRANT` responds with `Query OK, 0 rows affected` when executed successfully. To determine what privileges result from the operation, use `SHOW GRANTS`. See Section 13.7.5.22, “SHOW GRANTS Statement”.

Important Under some circumstances, `GRANT` may be recorded in server logs or on the client side in a history file such as `~/.mysql_history`, which means that cleartext passwords may be read by anyone having read access to that information. For information about the conditions under which this occurs for the server logs and how to control it, see Section 6.1.2.3, “Passwords and Logging”. For similar information about client-side logging, see Section 4.5.1.3, “mysql Client Logging”.

`GRANT` supports host names up to 60 characters long. User names can be up to 16 characters. Database,table, column, and routine names can be up to 64 characters.

Warning Do not attempt to change the permissible length for user names by altering the`mysql.user` system table. Doing so results in unpredictable behavior which may even make it impossible for users to log in to the MySQL server. Never alter the structure of tables in the `mysql` system database in any manner except by means of the procedure described in Section 2.11, “Upgrading MySQL”.

Object Quoting Guidelines Several objects within `GRANT` statements are subject to quoting, although quoting is optional in many cases: Account, database, table, column, and routine names. For example, if a `user_name` or `host_name`value in an account name is legal as an unquoted identifier, you need not quote it. However, quotation marks are necessary to specify a `user_name` string containing special characters (such as -), or a`host_name` string containing special characters or wildcard characters such as % (for example, `'test-``user'@'%.com'`). Quote the user name and host name separately.

To specify quoted values:Account Management Statements

- Quote database, table, column, and routine names as identifiers.
- Quote user names and host names as identifiers or as strings.
- Quote passwords as strings.

For string-quoting and identifier-quoting guidelines, see Section 9.1.1, “String Literals”, and Section 9.2,“Schema Object Names”.

The _ and % wildcards are permitted when specifying database names in `GRANT` statements that grant privileges at the database level (`GRANT ... ON db_name.*`). This means, for example, that to use a _ character as part of a database name, specify it using the \ escape character as `\_` in the `GRANT`statement, to prevent the user from being able to access additional databases matching the wildcard pattern (for example, `GRANT ... ON `foo\_bar`.* TO ...`).

When a database name is not used to grant privileges at the database level, but as a qualifier for granting privileges to some other object such as a table or routine (for example, `GRANT ... ON``db_name.tbl_name`), MySQL interprets wildcard characters as literal characters.

Account Names and Passwords A `user` value in a `GRANT` statement indicates a MySQL account to which the statement applies. To accommodate granting rights to users from arbitrary hosts, MySQL supports specifying the `user` value in the form `'user_name'@'host_name'`.

You can specify wildcards in the host name. For example, `'user_name'@'%.example.com'` applies to`user_name` for any host in the `example.com` domain, and `'user_name'@'198.51.100.%'` applies to`user_name` for any host in the `198.51.100` class C subnet.

The simple form `'user_name'` is a synonym for `'user_name'@'%'`.

MySQL does not support wildcards in user names. To refer to an anonymous user, specify an account with an empty user name with the `GRANT` statement:

```
GRANT ALL ON test.* TO ''@'localhost' ...;
```

In this case, any user who connects from the local host with the correct password for the anonymous user is permitted access, with the privileges associated with the anonymous-user account.

For additional information about user name and host name values in account names, see Section 6.2.4,“Specifying Account Names”.

Warning If you permit local anonymous users to connect to the MySQL server, you should also grant privileges to all local users as `'user_name'@'localhost'`. Otherwise,the anonymous user account for `localhost` in the `mysql.user` system table(created during MySQL installation) is used when named users try to log in to the MySQL server from the local machine. For details, see Section 6.2.5, “Access Control, Stage 1: Connection Verification”.

To determine whether this issue applies to you, execute the following query, which lists any anonymous users:

```
SELECT Host, User FROM mysql.user WHERE User='';
```

To avoid the problem just described, delete the local anonymous user account using this statement:Account Management Statements

```
DROP USER ''@'localhost';
```

For `GRANT` syntax that permits an `auth_option` value to follow a `user` value, `auth_option` begins with`IDENTIFIED` and indicates how the account authenticates by specifying an account authentication plugin,credentials (for example, a password), or both. Syntax of the `auth_option` clause is the same as for the`CREATE USER` statement. For details, see Section 13.7.1.2, “CREATE USER Statement”.

When `IDENTIFIED` is present and you have the global grant privilege (`GRANT OPTION`), any password specified becomes the new password for the account, even if the account exists and already has a password. Without `IDENTIFIED`, the account password remains unchanged.

Privileges Supported by MySQL The following table summarizes the permissible `priv_type` privilege types that can be specified for the`GRANT` and `REVOKE` statements, and the levels at which each privilege can be granted. For additional information about each privilege, see Section 6.2.2, “Privileges Provided by MySQL”.

Table 13.8 Permissible Privileges for GRANT and REVOKE Privilege Meaning and Grantable Levels`ALL [PRIVILEGES]` Grant all privileges at specified access level except

```
GRANT OPTION and PROXY.
```

`ALTER` Enable use of `ALTER TABLE`. Levels: Global,database, table.

`ALTER ROUTINE` Enable stored routines to be altered or dropped.

Levels: Global, database, routine.

`CREATE` Enable database and table creation. Levels: Global,database, table.

`CREATE ROUTINE` Enable stored routine creation. Levels: Global,database.

`CREATE TABLESPACE` Enable tablespaces and log file groups to be created, altered, or dropped. Level: Global.

```
CREATE TEMPORARY TABLES  Enable use of CREATE TEMPORARY TABLE.
```

Levels: Global, database.

`CREATE USER` Enable use of `CREATE USER`, `DROP USER`, `RENAME``USER`, and `REVOKE ALL PRIVILEGES`. Level:Global.

`CREATE VIEW` Enable views to be created or altered. Levels:Global, database, table.

`DELETE` Enable use of `DELETE`. Level: Global, database,table.

`DROP` Enable databases, tables, and views to be dropped.

Levels: Global, database, table.

`EVENT` Enable use of events for the Event Scheduler.

Levels: Global, database.

`EXECUTE` Enable the user to execute stored routines. Levels:Global, database, routine.

Account Management Statements Privilege Meaning and Grantable Levels`FILE` Enable the user to cause the server to read or write files. Level: Global.

`GRANT OPTION` Enable privileges to be granted to or removed from other accounts. Levels: Global, database, table,routine, proxy.

`INDEX` Enable indexes to be created or dropped. Levels:Global, database, table.

`INSERT` Enable use of `INSERT`. Levels: Global, database,table, column.

`LOCK TABLES` Enable use of `LOCK TABLES` on tables for which you have the `SELECT` privilege. Levels: Global,database.

`PROCESS` Enable the user to see all processes with `SHOW``PROCESSLIST`. Level: Global.

`PROXY` Enable user proxying. Level: From user to user.

`REFERENCES` Enable foreign key creation. Levels: Global,database, table, column.

`RELOAD` Enable use of `FLUSH` operations. Level: Global.

`REPLICATION CLIENT` Enable the user to ask where source or replica servers are. Level: Global.

`REPLICATION SLAVE` Enable replicas to read binary log events from the source. Level: Global.

`SELECT` Enable use of `SELECT`. Levels: Global, database,table, column.

`SHOW DATABASES` Enable `SHOW DATABASES` to show all databases.

Level: Global.

`SHOW VIEW` Enable use of `SHOW CREATE VIEW`. Levels: Global,database, table.

`SHUTDOWN` Enable use of `mysqladmin shutdown`. Level:Global.

`SUPER` Enable use of other administrative operations such

```
as CHANGE MASTER TO, KILL, PURGE BINARY
LOGS, SET GLOBAL, and mysqladmin debug
```

command. Level: Global.

`TRIGGER` Enable trigger operations. Levels: Global, database,table.

`UPDATE` Enable use of `UPDATE`. Levels: Global, database,table, column.

`USAGE` Synonym for “no privileges”A trigger is associated with a table. To create or drop a trigger, you must have the `TRIGGER` privilege for the table, not the trigger.

In `GRANT` statements, the `ALL [PRIVILEGES]` or `PROXY` privilege must be named by itself and cannot be specified along with other privileges. `ALL [PRIVILEGES]` stands for all privileges available for the level at which privileges are to be granted except for the `GRANT OPTION` and `PROXY` privileges.

Account Management Statements`USAGE` can be specified to create a user that has no privileges, or to specify the `REQUIRE` or `WITH` clauses for an account without changing its existing privileges.

MySQL account information is stored in the tables of the `mysql` system database. For additional details,consult Section 6.2, “Access Control and Account Management”, which discusses the `mysql` system database and the access control system extensively.

If the grant tables hold privilege rows that contain mixed-case database or table names and the`lower_case_table_names` system variable is set to a nonzero value, `REVOKE` cannot be used to revoke these privileges. It is necessary to manipulate the grant tables directly. (`GRANT` does not create such rows when `lower_case_table_names` is set, but such rows might have been created prior to setting that variable.)Privileges can be granted at several levels, depending on the syntax used for the `ON` clause. For `REVOKE`,the same `ON` syntax specifies which privileges to remove.

For the global, database, table, and routine levels, `GRANT ALL` assigns only the privileges that exist at the level you are granting. For example, `GRANT ALL ON db_name.*` is a database-level statement, so it does not grant any global-only privileges such as `FILE`. Granting `ALL` does not assign the `GRANT OPTION`or `PROXY` privilege.

The `object_type` clause, if present, should be specified as `TABLE`, `FUNCTION`, or `PROCEDURE` when the following object is a table, a stored function, or a stored procedure.

The privileges that a user holds for a database, table, column, or routine are formed additively as the logical `OR` of the account privileges at each of the privilege levels, including the global level. It is not possible to deny a privilege granted at a higher level by absence of that privilege at a lower level. For example, this statement grants the `SELECT` and `INSERT` privileges globally:

```
GRANT SELECT, INSERT ON *.* TO u1;
```

The globally granted privileges apply to all databases, tables, and columns, even though not granted at any of those lower levels.

Details of the privilege-checking procedure are presented in Section 6.2.6, “Access Control, Stage 2:Request Verification”.

If you are using table, column, or routine privileges for even one user, the server examines table, column,and routine privileges for all users and this slows down MySQL a bit. Similarly, if you limit the number of queries, updates, or connections for any users, the server must monitor these values.

MySQL enables you to grant privileges on databases or tables that do not exist. For tables, the privileges to be granted must include the `CREATE` privilege. This behavior is by design, and is intended to enable the database administrator to prepare user accounts and privileges for databases or tables that are to be created at a later time.

Important MySQL does not automatically revoke any privileges when you drop a database or table. However, if you drop a routine, any routine-level privileges granted for that routine are revoked.

Global Privileges Global privileges are administrative or apply to all databases on a given server. To assign global privileges,use `ON *.*` syntax:Account Management Statements

```
GRANT ALL ON *.* TO 'someuser'@'somehost';
GRANT SELECT, INSERT ON *.* TO 'someuser'@'somehost';
The CREATE TABLESPACE, CREATE USER, FILE, PROCESS, RELOAD, REPLICATION CLIENT,
```

`REPLICATION SLAVE`, `SHOW DATABASES`, `SHUTDOWN`, and `SUPER` privileges are administrative and can only be granted globally.

Other privileges can be granted globally or at more specific levels.

`GRANT OPTION` granted at the global level for any global privilege applies to all global privileges.

MySQL stores global privileges in the `mysql.user` system table.

Database Privileges Database privileges apply to all objects in a given database. To assign database-level privileges, use `ON``db_name.*` syntax:

```
GRANT ALL ON mydb.* TO 'someuser'@'somehost';
GRANT SELECT, INSERT ON mydb.* TO 'someuser'@'somehost';
```

If you use `ON *` syntax (rather than `ON *.*`), privileges are assigned at the database level for the default database. An error occurs if there is no default database.

The `CREATE`, `DROP`, `EVENT`, `GRANT OPTION`, `LOCK TABLES`, and `REFERENCES` privileges can be specified at the database level. Table or routine privileges also can be specified at the database level, in which case they apply to all tables or routines in the database.

MySQL stores database privileges in the `mysql.db` system table.

Table Privileges Table privileges apply to all columns in a given table. To assign table-level privileges, use `ON``db_name.tbl_name` syntax:

```
GRANT ALL ON mydb.mytbl TO 'someuser'@'somehost';
GRANT SELECT, INSERT ON mydb.mytbl TO 'someuser'@'somehost';
```

If you specify `tbl_name` rather than `db_name.tbl_name`, the statement applies to `tbl_name` in the default database. An error occurs if there is no default database.

The permissible `priv_type` values at the table level are `ALTER`, `CREATE VIEW`, `CREATE`, `DELETE`, `DROP`,

```
GRANT OPTION, INDEX, INSERT, REFERENCES, SELECT, SHOW VIEW, TRIGGER, and UPDATE.
```

Table-level privileges apply to base tables and views. They do not apply to tables created with `CREATE``TEMPORARY TABLE`, even if the table names match. For information about `TEMPORARY` table privileges,see Section 13.1.17.2, “CREATE TEMPORARY TABLE Statement”.

MySQL stores table privileges in the `mysql.tables_priv` system table.

Column Privileges Column privileges apply to single columns in a given table. Each privilege to be granted at the column level must be followed by the column or columns, enclosed within parentheses.

```
GRANT SELECT (col1), INSERT (col1, col2) ON mydb.mytbl TO 'someuser'@'somehost';
```

The permissible `priv_type` values for a column (that is, when you use a `column_list` clause) are

```
INSERT, REFERENCES, SELECT, and UPDATE.
```

Account Management Statements MySQL stores column privileges in the `mysql.columns_priv` system table.

Stored Routine Privileges The `ALTER ROUTINE`, `CREATE ROUTINE`, `EXECUTE`, and `GRANT OPTION` privileges apply to stored routines (procedures and functions). They can be granted at the global and database levels. Except for`CREATE ROUTINE`, these privileges can be granted at the routine level for individual routines.

```
GRANT CREATE ROUTINE ON mydb.* TO 'someuser'@'somehost';
GRANT EXECUTE ON PROCEDURE mydb.myproc TO 'someuser'@'somehost';
```

The permissible `priv_type` values at the routine level are `ALTER ROUTINE`, `EXECUTE`, and `GRANT``OPTION`. `CREATE ROUTINE` is not a routine-level privilege because you must have the privilege at the global or database level to create a routine in the first place.

MySQL stores routine-level privileges in the `mysql.procs_priv` system table.

Proxy User Privileges The `PROXY` privilege enables one user to be a proxy for another. The proxy user impersonates or takes the identity of the proxied user; that is, it assumes the privileges of the proxied user.

```
GRANT PROXY ON 'localuser'@'localhost' TO 'externaluser'@'somehost';
```

When `PROXY` is granted, it must be the only privilege named in the `GRANT` statement, the `REQUIRE` clause cannot be given, and the only permitted `WITH` option is `WITH GRANT OPTION`.

Proxying requires that the proxy user authenticate through a plugin that returns the name of the proxied user to the server when the proxy user connects, and that the proxy user have the `PROXY` privilege for the proxied user. For details and examples, see Section 6.2.12, “Proxy Users”.

MySQL stores proxy privileges in the `mysql.proxies_priv` system table.

Implicit Account Creation If an account named in a `GRANT` statement does not exist, the action taken depends on the`NO_AUTO_CREATE_USER` SQL mode:

- If `NO_AUTO_CREATE_USER` is not enabled, `GRANT` creates the account. This is very insecure unless you

specify a nonempty password using `IDENTIFIED BY`.

- If `NO_AUTO_CREATE_USER` is enabled, `GRANT` fails and does not create the account, unless you specify

a nonempty password using `IDENTIFIED BY` or name an authentication plugin using `IDENTIFIED`

```
WITH.
```

As of MySQL 5.6.12, if the account already exists, `IDENTIFIED WITH` is prohibited because it is intended only for use when creating new accounts.

Other Account Characteristics MySQL can check X.509 certificate attributes in addition to the usual authentication that is based on the user name and credentials. For background information on the use of SSL with MySQL, see Section 6.3,“Using Encrypted Connections”.

The optional `REQUIRE` clause specifies SSL-related options for a MySQL account, using one or more`tls_option` values.

Account Management Statements Order of `REQUIRE` options does not matter, but no option can be specified twice. The `AND` keyword is optional between `REQUIRE` options.

`GRANT` permits these `tls_option` values:

```
- NONE
```

Indicates that the account has no SSL or X.509 requirements.

```
GRANT ALL PRIVILEGES ON test.* TO 'root'@'localhost'
REQUIRE NONE;
```

Unencrypted connections are permitted if the user name and password are valid. Encrypted connections can be used, at the client's option, if the client has the proper certificate and key files. That is, the client need not specify any SSL command options, in which case the connection is unencrypted. To use an encrypted connection, the client must specify either the `--ssl-ca` option, or all three of the `--ssl-ca`,`--ssl-key`, and `--ssl-cert` options.

`NONE` is the default if no SSL-related `REQUIRE` options are specified.

```
- SSL
```

Tells the server to permit only encrypted connections for the account.

```
GRANT ALL PRIVILEGES ON test.* TO 'root'@'localhost'
REQUIRE SSL;
```

To connect, the client must specify the `--ssl-ca` option to authenticate the server certificate, and may additionally specify the `--ssl-key` and `--ssl-cert` options. If neither the `--ssl-ca` option nor `--``ssl-capath` option is specified, the client does not authenticate the server certificate.

```
- X509
```

Requires that clients present a valid certificate, but the exact certificate, issuer, and subject do not matter. The only requirement is that it should be possible to verify its signature with one of the CA certificates. Use of X.509 certificates always implies encryption, so the `SSL` option is unnecessary in this case.

```
GRANT ALL PRIVILEGES ON test.* TO 'root'@'localhost'
REQUIRE X509;
```

For accounts with `REQUIRE X509`, clients must specify the `--ssl-key` and `--ssl-cert` options to connect. (It is recommended but not required that `--ssl-ca` also be specified so that the public certificate provided by the server can be verified.) This is true for `ISSUER` and `SUBJECT` as well because those `REQUIRE` options imply the requirements of `X509`.

```
- ISSUER 'issuer'
```

Requires that clients present a valid X.509 certificate issued by CA `'issuer'`. If a client presents a certificate that is valid but has a different issuer, the server rejects the connection. Use of X.509 certificates always implies encryption, so the `SSL` option is unnecessary in this case.

```
GRANT ALL PRIVILEGES ON test.* TO 'root'@'localhost'
REQUIRE ISSUER '/C=SE/ST=Stockholm/L=Stockholm/
O=MySQL/CN=CA/emailAddress=ca@example.com';
```

Because `ISSUER` implies the requirements of `X509`, clients must specify the `--ssl-key` and `--ssl-``cert` options to connect. (It is recommended but not required that `--ssl-ca` also be specified so that the public certificate provided by the server can be verified.)Account Management Statements Note If MySQL is linked against a version of OpenSSL older than 0.9.6h, use `Email`rather than `emailAddress` in the `'issuer'` value.

```
- SUBJECT 'subject'
```

Requires that clients present a valid X.509 certificate containing the subject `subject`. If a client presents a certificate that is valid but has a different subject, the server rejects the connection. Use of X.509 certificates always implies encryption, so the `SSL` option is unnecessary in this case.

```
GRANT ALL PRIVILEGES ON test.* TO 'root'@'localhost'
REQUIRE SUBJECT '/C=SE/ST=Stockholm/L=Stockholm/
O=MySQL demo client certificate/
CN=client/emailAddress=client@example.com';
```

MySQL does a simple string comparison of the `'subject'` value to the value in the certificate, so lettercase and component ordering must be given exactly as present in the certificate.

Note Regarding `emailAddress`, see the note in the description of `REQUIRE ISSUER`.

Because `SUBJECT` implies the requirements of `X509`, clients must specify the `--ssl-key` and `--ssl-``cert` options to connect. (It is recommended but not required that `--ssl-ca` also be specified so that the public certificate provided by the server can be verified.)

```
- CIPHER 'cipher'
```

Requires a specific cipher method for encrypting connections. This option is needed to ensure that ciphers and key lengths of sufficient strength are used. SSL itself can be weak if old algorithms using short encryption keys are used.

```
GRANT ALL PRIVILEGES ON test.* TO 'root'@'localhost'
REQUIRE CIPHER 'EDH-RSA-DES-CBC3-SHA';
```

The `SUBJECT`, `ISSUER`, and `CIPHER` options can be combined in the `REQUIRE` clause like this:

```
GRANT ALL PRIVILEGES ON test.* TO 'root'@'localhost'
REQUIRE SUBJECT '/C=SE/ST=Stockholm/L=Stockholm/
O=MySQL demo client certificate/
CN=client/emailAddress=client@example.com'
AND ISSUER '/C=SE/ST=Stockholm/L=Stockholm/
O=MySQL/CN=CA/emailAddress=ca@example.com'
AND CIPHER 'EDH-RSA-DES-CBC3-SHA';
```

The optional `WITH` clause is used for these purposes:

- To enable a user to grant privileges to other users
- To specify resource limits for a user

The `WITH GRANT OPTION` clause gives the user the ability to give to other users any privileges the user has at the specified privilege level.

To grant the `GRANT OPTION` privilege to an account without otherwise changing its privileges, do this:

```
GRANT USAGE ON *.* TO 'someuser'@'somehost' WITH GRANT OPTION;
```

Account Management Statements Be careful to whom you give the `GRANT OPTION` privilege because two users with different privileges may be able to combine privileges!

You cannot grant another user a privilege which you yourself do not have; the `GRANT OPTION` privilege enables you to assign only those privileges which you yourself possess.

Be aware that when you grant a user the `GRANT OPTION` privilege at a particular privilege level, any privileges the user possesses (or may be given in the future) at that level can also be granted by that user to other users. Suppose that you grant a user the `INSERT` privilege on a database. If you then grant the`SELECT` privilege on the database and specify `WITH GRANT OPTION`, that user can give to other users not only the `SELECT` privilege, but also `INSERT`. If you then grant the `UPDATE` privilege to the user on the database, the user can grant `INSERT`, `SELECT`, and `UPDATE`.

For a nonadministrative user, you should not grant the `ALTER` privilege globally or for the `mysql` system database. If you do that, the user can try to subvert the privilege system by renaming tables!

For additional information about security risks associated with particular privileges, see Section 6.2.2,“Privileges Provided by MySQL”.

It is possible to place limits on use of server resources by an account, as discussed in Section 6.2.13,“Setting Account Resource Limits”. To do so, use a `WITH` clause that specifies one or more`resource_option` values. Limits not specified retain their current values.

Order of `WITH` options does not matter, except that if a given resource limit is specified multiple times, the last instance takes precedence.

`GRANT` permits these `resource_option` values:

```
- MAX_QUERIES_PER_HOUR count, MAX_UPDATES_PER_HOUR count,
MAX_CONNECTIONS_PER_HOUR count
```

These options restrict how many queries, updates, and connections to the server are permitted to this account during any given one-hour period. (Queries for which results are served from the query cache do not count against the `MAX_QUERIES_PER_HOUR` limit.) If `count` is 0 (the default), this means that there is no limitation for the account.

```
- MAX_USER_CONNECTIONS count
```

Restricts the maximum number of simultaneous connections to the server by the account. A nonzero `count` specifies the limit for the account explicitly. If `count` is 0 (the default), the server determines the number of simultaneous connections for the account from the global value of the`max_user_connections` system variable. If `max_user_connections` is also zero, there is no limit for the account.

To specify resource limits for an existing user without affecting existing privileges, use `GRANT USAGE` at the global level (`ON *.*`) and name the limits to be changed. For example:

```
GRANT USAGE ON *.* TO ...
WITH MAX_QUERIES_PER_HOUR 500 MAX_UPDATES_PER_HOUR 100;
```

MySQL and Standard SQL Versions of GRANT The biggest differences between the MySQL and standard SQL versions of `GRANT` are:

- MySQL associates privileges with the combination of a host name and user name and not with only a

user name.

Account Management Statements

- Standard SQL does not have global or database-level privileges, nor does it support all the privilege

types that MySQL supports.

- MySQL does not support the standard SQL `UNDER` privilege.
- Standard SQL privileges are structured in a hierarchical manner. If you remove a user, all privileges

the user has been granted are revoked. This is also true in MySQL if you use `DROP USER`. See Section 13.7.1.3, “DROP USER Statement”.

- In standard SQL, when you drop a table, all privileges for the table are revoked. In standard SQL, when

you revoke a privilege, all privileges that were granted based on that privilege are also revoked. In MySQL, privileges can be dropped with `DROP USER` or `REVOKE` statements.

- In MySQL, it is possible to have the `INSERT` privilege for only some of the columns in a table. In this

case, you can still execute `INSERT` statements on the table, provided that you insert values only for those columns for which you have the `INSERT` privilege. The omitted columns are set to their implicit default values if strict SQL mode is not enabled. In strict mode, the statement is rejected if any of the omitted columns have no default value. (Standard SQL requires you to have the `INSERT` privilege on all columns.) For information about strict SQL mode and implicit default values, see Section 5.1.10, “Server SQL Modes”, and Section 11.5, “Data Type Default Values”.

#### 13.7.1.5 RENAME USER Statement

```
RENAME USER old_user TO new_user
[, old_user TO new_user] ...
```

The `RENAME USER` statement renames existing MySQL accounts. An error occurs for old accounts that do not exist or new accounts that already exist.

To use `RENAME USER`, you must have the global `CREATE USER` privilege, or the `UPDATE` privilege for the`mysql` system database. When the `read_only` system variable is enabled, `RENAME USER` additionally requires the `SUPER` privilege.

Each account name uses the format described in Section 6.2.4, “Specifying Account Names”. For example:

```
RENAME USER 'jeffrey'@'localhost' TO 'jeff'@'127.0.0.1';
```

The host name part of the account name, if omitted, defaults to `'%'`.

`RENAME USER` causes the privileges held by the old user to be those held by the new user. However,`RENAME USER` does not automatically drop or invalidate databases or objects within them that the old user created. This includes stored programs or views for which the `DEFINER` attribute names the old user.

Attempts to access such objects may produce an error if they execute in definer security context. (For information about security context, see Section 20.6, “Stored Object Access Control”.)The privilege changes take effect as indicated in Section 6.2.8, “When Privilege Changes Take Effect”.

#### 13.7.1.6 REVOKE Statement

```
REVOKE
priv_type [(column_list)]
[, priv_type [(column_list)]] ...
ON [object_type] priv_level
FROM user [, user] ...
REVOKE ALL [PRIVILEGES], GRANT OPTION
FROM user [, user] ...
REVOKE PROXY ON user
```

Account Management Statements

```
FROM user [, user] ...
```

The `REVOKE` statement enables system administrators to revoke privileges from MySQL accounts.

For details on the levels at which privileges exist, the permissible `priv_type`, `priv_level`, and`object_type` values, and the syntax for specifying users and passwords, see Section 13.7.1.4, “GRANT Statement”.

When the `read_only` system variable is enabled, `REVOKE` requires the `SUPER` privilege in addition to any other required privileges described in the following discussion.

Each account name uses the format described in Section 6.2.4, “Specifying Account Names”. For example:

```
REVOKE INSERT ON *.* FROM 'jeffrey'@'localhost';
```

The host name part of the account name, if omitted, defaults to `'%'`.

To use the first `REVOKE` syntax, you must have the `GRANT OPTION` privilege, and you must have the privileges that you are revoking.

To revoke all privileges, use the second syntax, which drops all global, database, table, column, and routine privileges for the named user or users:

```
REVOKE ALL PRIVILEGES, GRANT OPTION FROM user [, user] ...
```

To use this `REVOKE` syntax, you must have the global `CREATE USER` privilege, or the `UPDATE` privilege for the `mysql` system database.

User accounts from which privileges are to be revoked must exist, but the privileges to be revoked need not be currently granted to them.

`REVOKE` removes privileges, but does not remove rows from the `mysql.user` system table. To remove a user account entirely, use `DROP USER`. See Section 13.7.1.3, “DROP USER Statement”.

If the grant tables hold privilege rows that contain mixed-case database or table names and the`lower_case_table_names` system variable is set to a nonzero value, `REVOKE` cannot be used to revoke these privileges. It is necessary to manipulate the grant tables directly. (`GRANT` does not create such rows when `lower_case_table_names` is set, but such rows might have been created prior to setting the variable.)When successfully executed from the `mysql` program, `REVOKE` responds with `Query OK, 0``rows affected`. To determine what privileges remain after the operation, use `SHOW GRANTS`. See Section 13.7.5.22, “SHOW GRANTS Statement”.

#### 13.7.1.7 SET PASSWORD Statement

```
SET PASSWORD [FOR user] = password_option
password_option: {
PASSWORD('auth_string')
| OLD_PASSWORD('auth_string')
| 'hash_string'
}
```

The `SET PASSWORD` statement assigns a password to a MySQL user account, specified as either a cleartext (unencrypted) or encrypted value:

- `'auth_string'` represents a cleartext password.
- `'hash_string'` represents an encrypted password.

Account Management Statements Important Under some circumstances, `SET PASSWORD` may be recorded in server logs or on the client side in a history file such as `~/.mysql_history`, which means that cleartext passwords may be read by anyone having read access to that information.

For information about the conditions under which this occurs for the server logs and how to control it, see Section 6.1.2.3, “Passwords and Logging”. For similar information about client-side logging, see Section 4.5.1.3, “mysql Client Logging”.

`SET PASSWORD` can be used with or without a `FOR` clause that explicitly names a user account:

- With a `FOR user` clause, the statement sets the password for the named account, which must exist:

```
SET PASSWORD FOR 'jeffrey'@'localhost' = password_option;
```

- With no `FOR user` clause, the statement sets the password for the current user:

```
SET PASSWORD = password_option;
```

Any client who connects to the server using a nonanonymous account can change the password for that account. (In particular, you can change your own password.) To see which account the server authenticated you as, invoke the `CURRENT_USER()` function:

```
SELECT CURRENT_USER();
```

If a `FOR user` clause is given, the account name uses the format described in Section 6.2.4, “Specifying Account Names”. For example:

```
SET PASSWORD FOR 'bob'@'%.example.org' = PASSWORD('auth_string');
```

The host name part of the account name, if omitted, defaults to `'%'`.

Setting the password for a named account (with a `FOR` clause) requires the `UPDATE` privilege for the `mysql`system database. Setting the password for yourself (for a nonanonymous account with no `FOR` clause)requires no special privileges. When the `read_only` system variable is enabled, `SET PASSWORD` requires the `SUPER` privilege in addition to any other required privileges.

The password can be specified in these ways:

- Use the `PASSWORD()` function

The `PASSWORD()` argument is the cleartext (unencrypted) password. `PASSWORD()` hashes the password and returns the encrypted password string for storage in the account row in the `mysql.user`system table.

The `PASSWORD()` function hashes the password using the hashing method determined by the value of the `old_passwords` system variable value. If `SET PASSWORD` rejects the hashed password value returned by `PASSWORD()` as not being in the correct format, it may be necessary to change `old_passwords` to change the hashing method. For example, if the account uses the`mysql_native_password` plugin, the `old_passwords` value must be 0:

```
SET old_passwords = 0;
SET PASSWORD FOR 'jeffrey'@'localhost' = PASSWORD('password');
```

If the `old_passwords` value differs from that required by the authentication plugin, the hashed password value returned by `PASSWORD()` is not acceptable for that plugin, and attempts to set the password produce an error. For example:

```
mysql> SET old_passwords = 1;
```

Table Maintenance Statements

```
mysql> SET PASSWORD FOR 'jeffrey'@'localhost' = PASSWORD('password');
ERROR 1372 (HY000): Password hash should be a 41-digit hexadecimal number
```

Permitted `old_passwords` values are described later in this section.

- Use the `OLD_PASSWORD()` function:

The `'auth_string'` function argument is the cleartext (unencrypted) password. `OLD_PASSWORD()`hashes the password using pre-4.1 hashing and returns the encrypted password string for storage in the account row in the `mysql.user` system table. This hashing method is appropriate only for accounts that use the `mysql_old_password` authentication plugin.

- Use an already encrypted password string

The password is specified as a string literal. It must represent the already encrypted password value, in the hash format required by the authentication method used for the account.

The following table shows, for each password hashing method, the permitted value of `old_passwords`and which authentication plugins use the hashing method.

Password Hashing Method old_passwords Value Associated Authentication Plugin MySQL 4.1 native hashing 0 `mysql_native_password`Pre-4.1 (“old”) hashing 1 `mysql_old_password`SHA-256 hashing 2 `sha256_password`Caution If you are connecting to a MySQL 4.1 or later server using a pre-4.1 client program,do not change your password without first reading Section 6.1.2.4, “Password Hashing in MySQL”. The default password hashing format changed in MySQL 4.1,and if you change your password, it might be stored using a hashing format that pre-4.1 clients cannot generate, thus preventing you from connecting to the server afterward.

For additional information about setting passwords and authentication plugins, see Section 6.2.9,“Assigning Account Passwords”, and Section 6.2.11, “Pluggable Authentication”.

### 13.7.2 Table Maintenance Statements

#### 13.7.2.1 ANALYZE TABLE Statement

```
ANALYZE [NO_WRITE_TO_BINLOG | LOCAL]
TABLE tbl_name [, tbl_name] ...
```

`ANALYZE TABLE` performs a key distribution analysis and stores the distribution for the named table or tables. For `MyISAM` tables, this statement is equivalent to using `myisamchk --analyze`.

This statement requires `SELECT` and `INSERT` privileges for the table.

`ANALYZE TABLE` works with `InnoDB`, `NDB`, and `MyISAM` tables. It does not work with views.

`ANALYZE TABLE` is supported for partitioned tables, and you can use `ALTER TABLE ... ANALYZE``PARTITION` to analyze one or more partitions; for more information, see Section 13.1.7, “ALTER TABLE Statement”, and Section 19.3.4, “Maintenance of Partitions”.

During the analysis, the table is locked with a read lock for `InnoDB` and `MyISAM`.

Table Maintenance Statements`ANALYZE TABLE` removes the table from the table definition cache, which requires a flush lock. If there are long running statements or transactions still using the table, subsequent statements and transactions must wait for those operations to finish before the flush lock is released. Because `ANALYZE TABLE` itself typically finishes quickly, it may not be apparent that delayed transactions or statements involving the same table are due to the remaining flush lock.

By default, the server writes `ANALYZE TABLE` statements to the binary log so that they replicate to replicas. To suppress logging, specify the optional `NO_WRITE_TO_BINLOG` keyword or its alias `LOCAL`.

- ANALYZE TABLE Output
- Key Distribution Analysis
- Other Considerations

ANALYZE TABLE Output`ANALYZE TABLE` returns a result set with the columns shown in the following table.

Column Value`Table` The table name`Op` Always `analyze`

```
Msg_type  status, error, info, note, or warning
```

`Msg_text` An informational message Key Distribution Analysis If the table has not changed since the last key distribution analysis, the table is not analyzed again.

MySQL uses the stored key distribution to decide the table join order for joins on something other than a constant. In addition, key distributions can be used when deciding which indexes to use for a specific table within a query.

To check the stored key distribution cardinality, use the `SHOW INDEX` statement or the`INFORMATION_SCHEMA` `STATISTICS` table. See Section 13.7.5.23, “SHOW INDEX Statement”, and Section 21.3.22, “The INFORMATION_SCHEMA STATISTICS Table”.

For `InnoDB` tables, `ANALYZE TABLE` determines index cardinality by performing random dives on each of the index trees and updating index cardinality estimates accordingly. Because these are only estimates,repeated runs of `ANALYZE TABLE` could produce different numbers. This makes `ANALYZE TABLE` fast on`InnoDB` tables but not 100% accurate because it does not take all rows into account.

You can make the statistics collected by `ANALYZE TABLE` more precise and more stable by enabling`innodb_stats_persistent`, as explained in Section 14.8.11.1, “Configuring Persistent Optimizer Statistics Parameters”. When `innodb_stats_persistent` is enabled, it is important to run `ANALYZE``TABLE` after major changes to index column data, as statistics are not recalculated periodically (such as after a server restart).

If `innodb_stats_persistent` is enabled, you can change the number of random dives by modifying the `innodb_stats_persistent_sample_pages` system variable. If `innodb_stats_persistent` is disabled, modify `innodb_stats_transient_sample_pages` instead.

For more information about key distribution analysis in `InnoDB`, see Section 14.8.11.1, “Configuring Persistent Optimizer Statistics Parameters”, and Section 14.8.11.3, “Estimating ANALYZE TABLE Complexity for InnoDB Tables”.

Table Maintenance Statements MySQL uses index cardinality estimates in join optimization. If a join is not optimized in the right way, try running `ANALYZE TABLE`. In the few cases that `ANALYZE TABLE` does not produce values good enough for your particular tables, you can use `FORCE INDEX` with your queries to force the use of a particular index, or set the `max_seeks_for_key` system variable to ensure that MySQL prefers index lookups over table scans. See Section B.3.5, “Optimizer-Related Issues”.

Other Considerations`ANALYZE TABLE` clears table statistics from the Information Schema `INNODB_SYS_TABLESTATS` table and sets the `STATS_INITIALIZED` column to `Uninitialized`. Statistics are collected again the next time the table is accessed.

In MySQL 5.6.11 only, `gtid_next` must be set to `AUTOMATIC` before issuing this statement. (Bug#16062608, Bug #16715809, Bug #69045)

#### 13.7.2.2 CHECK TABLE Statement

```
CHECK TABLE tbl_name [, tbl_name] ... [option] ...
option: {
FOR UPGRADE
| QUICK
| FAST
| MEDIUM
| EXTENDED
| CHANGED
}
```

`CHECK TABLE` checks a table or tables for errors. For `MyISAM` tables, the key statistics are updated as well. `CHECK TABLE` can also check views for problems, such as tables that are referenced in the view definition that no longer exist.

To check a table, you must have some privilege for it.

`CHECK TABLE` works for `InnoDB`, `MyISAM`, `ARCHIVE`, and `CSV` tables.

Before running `CHECK TABLE` on `InnoDB` tables, see CHECK TABLE Usage Notes for InnoDB Tables.

`CHECK TABLE` is supported for partitioned tables, and you can use `ALTER TABLE ... CHECK``PARTITION` to check one or more partitions; for more information, see Section 13.1.7, “ALTER TABLE Statement”, and Section 19.3.4, “Maintenance of Partitions”.

In MySQL 5.6.11 only, `gtid_next` must be set to `AUTOMATIC` before issuing this statement. (Bug#16062608, Bug #16715809, Bug #69045)

- CHECK TABLE Output
- Checking Version Compatibility
- Checking Data Consistency
- CHECK TABLE Usage Notes for InnoDB Tables

CHECK TABLE Output`CHECK TABLE` returns a result set with the columns shown in the following table.

Column Value`Table` The table name Table Maintenance Statements Column Value`Op` Always `check`

```
Msg_type  status, error, info, note, or warning
```

`Msg_text` An informational message The statement might produce many rows of information for each checked table. The last row has a`Msg_type` value of `status` and the `Msg_text` normally should be `OK`. For a `MyISAM` table, if you don't get `OK` or `Table is already up to date`, you should normally run a repair of the table. See Section 7.6, “MyISAM Table Maintenance and Crash Recovery”. `Table is already up to date`means that the storage engine for the table indicated that there was no need to check the table.

Checking Version Compatibility The `FOR UPGRADE` option checks whether the named tables are compatible with the current version of MySQL. With `FOR UPGRADE`, the server checks each table to determine whether there have been any incompatible changes in any of the table's data types or indexes since the table was created. If not, the check succeeds. Otherwise, if there is a possible incompatibility, the server runs a full check on the table(which might take some time). If the full check succeeds, the server marks the table's `.frm` file with the current MySQL version number. Marking the `.frm` file ensures that further checks for the table with the same version of the server are fast.

Incompatibilities might occur because the storage format for a data type has changed or because its sort order has changed. Our aim is to avoid these changes, but occasionally they are necessary to correct problems that would be worse than an incompatibility between releases.

`FOR UPGRADE` discovers these incompatibilities:

- The indexing order for end-space in `TEXT` columns for `InnoDB` and `MyISAM` tables changed between

MySQL 4.1 and 5.0.

- The storage method of the new `DECIMAL` data type changed between MySQL 5.0.3 and 5.0.5.
- If your table was created by a different version of the MySQL server than the one you are currently

running, `FOR UPGRADE` indicates that the table has an `.frm` file with an incompatible version. In this case, the result set returned by `CHECK TABLE` contains a line with a `Msg_type` value of `error` and a

```
Msg_text value of Table upgrade required. Please do "REPAIR TABLE `tbl_name`" to
fix it!
```

- Changes are sometimes made to character sets or collations that require table indexes to be rebuilt.

For details about such changes, see Section 2.11.3, “Changes in MySQL 5.6”. For information about rebuilding tables, see Section 2.11.10, “Rebuilding or Repairing Tables or Indexes”.

- The `YEAR(2)` data type is deprecated as of MySQL 5.6.6. For tables containing `YEAR(2)` columns,

`CHECK TABLE` recommends `REPAIR TABLE`, which converts 2-digit `YEAR(2)` columns to 4-digit `YEAR`columns.

- As of MySQL 5.6.4, MySQL permits fractional seconds for `TIME`, `DATETIME`, and `TIMESTAMP` column

values. As a result, encoding and storage requirements for these temporal column types differ in tables created in MySQL 5.6.4 and later. This incompatible change is described in Section 2.11.3,“Changes in MySQL 5.6”. When upgrading to MySQL 5.6.4 or later, be aware that `CHECK TABLE ...``FOR UPGRADE` does not report temporal columns that use the pre-MySQL 5.6.4 format (Bug #73008,Bug #18985579). In MySQL 5.6.24, two new system variables, `avoid_temporal_upgrade` and`show_old_temporals`, were added to provide control over temporal column upgrades (Bug #72997,Bug #18985760).

Table Maintenance Statements Checking Data Consistency The following table shows the other check options that can be given. These options are passed to the storage engine, which may use or ignore them.

Type Meaning`QUICK` Do not scan the rows to check for incorrect links.

Applies to `InnoDB` and `MyISAM` tables and views.

`FAST` Check only tables that have not been closed properly. Applies only to `MyISAM` tables and views;

ignored for `InnoDB`.

`CHANGED` Check only tables that have been changed since the last check or that have not been closed properly.

Applies only to `MyISAM` tables and views; ignored for `InnoDB`.

`MEDIUM` Scan rows to verify that deleted links are valid. This also calculates a key checksum for the rows and verifies this with a calculated checksum for the keys.

Applies only to `MyISAM` tables and views; ignored for `InnoDB`.

`EXTENDED` Do a full key lookup for all keys for each row. This ensures that the table is 100% consistent, but takes a long time. Applies only to `MyISAM` tables and views; ignored for `InnoDB`.

If none of the options `QUICK`, `MEDIUM`, or `EXTENDED` are specified, the default check type for dynamic-format `MyISAM` tables is `MEDIUM`. This has the same result as running `myisamchk --medium-check``tbl_name` on the table. The default check type also is `MEDIUM` for static-format `MyISAM` tables, unless`CHANGED` or `FAST` is specified. In that case, the default is `QUICK`. The row scan is skipped for `CHANGED`and `FAST` because the rows are very seldom corrupted.

You can combine check options, as in the following example that does a quick check on the table to determine whether it was closed properly:

```
CHECK TABLE test_table FAST QUICK;
```

Note If `CHECK TABLE` finds no problems with a table that is marked as “corrupted” or “not closed properly”, `CHECK TABLE` may remove the mark.

If a table is corrupted, the problem is most likely in the indexes and not in the data part. All of the preceding check types check the indexes thoroughly and should thus find most errors.

To check a table that you assume is okay, use no check options or the `QUICK` option. The latter should be used when you are in a hurry and can take the very small risk that `QUICK` does not find an error in the data file. (In most cases, under normal usage, MySQL should find any error in the data file. If this happens, the table is marked as “corrupted” and cannot be used until it is repaired.)`FAST` and `CHANGED` are mostly intended to be used from a script (for example, to be executed from `cron`)to check tables periodically. In most cases, `FAST` is to be preferred over `CHANGED`. (The only case when it is not preferred is when you suspect that you have found a bug in the `MyISAM` code.)Table Maintenance Statements`EXTENDED` is to be used only after you have run a normal check but still get errors from a table when MySQL tries to update a row or find a row by key. This is very unlikely if a normal check has succeeded.

Use of `CHECK TABLE ... EXTENDED` might influence execution plans generated by the query optimizer.

Some problems reported by `CHECK TABLE` cannot be corrected automatically:

```
- Found row where the auto_increment column has the value 0.
```

This means that you have a row in the table where the `AUTO_INCREMENT` index column contains the value 0. (It is possible to create a row where the `AUTO_INCREMENT` column is 0 by explicitly setting the column to 0 with an `UPDATE` statement.)This is not an error in itself, but could cause trouble if you decide to dump the table and restore it or do an `ALTER TABLE` on the table. In this case, the `AUTO_INCREMENT` column changes value according to the rules of `AUTO_INCREMENT` columns, which could cause problems such as a duplicate-key error.

To get rid of the warning, execute an `UPDATE` statement to set the column to some value other than 0.

CHECK TABLE Usage Notes for InnoDB Tables The following notes apply to `InnoDB` tables:

- If `CHECK TABLE` encounters a corrupt page, the server exits to prevent error propagation (Bug #10132).

If the corruption occurs in a secondary index but table data is readable, running `CHECK TABLE` can still cause a server exit.

- If `CHECK TABLE` encounters a corrupted `DB_TRX_ID` or `DB_ROLL_PTR` field in a clustered index, `CHECK`

`TABLE` can cause `InnoDB` to access an invalid undo log record, resulting in an MVCC-related server exit.

- If `CHECK TABLE` encounters errors in `InnoDB` tables or indexes, it reports an error, and usually marks

the index and sometimes marks the table as corrupted, preventing further use of the index or table. Such errors include an incorrect number of entries in a secondary index or incorrect links.

- If `CHECK TABLE` finds an incorrect number of entries in a secondary index, it reports an error but does

not cause a server exit or prevent access to the file.

- `CHECK TABLE` surveys the index page structure, then surveys each key entry. It does not validate the

key pointer to a clustered record or follow the path for `BLOB` pointers.

- When an `InnoDB` table is stored in its own `.ibd` file, the first 3 pages of the `.ibd` file contain

header information rather than table or index data. The `CHECK TABLE` statement does not detect inconsistencies that affect only the header data. To verify the entire contents of an `InnoDB` `.ibd` file,use the `innochecksum` command.

- When running `CHECK TABLE` on large `InnoDB` tables, other threads may be blocked during `CHECK`

`TABLE` execution. To avoid timeouts, the semaphore wait threshold (600 seconds) is extended by 2 hours (7200 seconds) for `CHECK TABLE` operations. If `InnoDB` detects semaphore waits of 240 seconds or more, it starts printing `InnoDB` monitor output to the error log. If a lock request extends beyond the semaphore wait threshold, `InnoDB` aborts the process. To avoid the possibility of a semaphore wait timeout entirely, run `CHECK TABLE QUICK` instead of `CHECK TABLE`.

#### 13.7.2.3 CHECKSUM TABLE Statement

```
CHECKSUM TABLE tbl_name [, tbl_name] ... [QUICK | EXTENDED]
```

Table Maintenance Statements`CHECKSUM TABLE` reports a checksum for the contents of a table. You can use this statement to verify that the contents are the same before and after a backup, rollback, or other operation that is intended to put the data back to a known state.

This statement requires the `SELECT` privilege for the table.

This statement is not supported for views. If you run `CHECKSUM TABLE` against a view, the `Checksum`value is always `NULL`, and a warning is returned.

For a nonexistent table, `CHECKSUM TABLE` returns `NULL` and generates a warning.

During the checksum operation, the table is locked with a read lock for `InnoDB` and `MyISAM`.

Performance Considerations By default, the entire table is read row by row and the checksum is calculated. For large tables, this could take a long time, thus you would only perform this operation occasionally. This row-by-row calculation is what you get with the `EXTENDED` clause, with `InnoDB` and all other storage engines other than `MyISAM`,and with `MyISAM` tables not created with the `CHECKSUM=1` clause.

For `MyISAM` tables created with the `CHECKSUM=1` clause, `CHECKSUM TABLE` or `CHECKSUM TABLE ...``QUICK` returns the “live” table checksum that can be returned very fast. If the table does not meet all these conditions, the `QUICK` method returns `NULL`. The `QUICK` method is not supported with `InnoDB` tables. See Section 13.1.17, “CREATE TABLE Statement” for the syntax of the `CHECKSUM` clause.

The checksum value depends on the table row format. If the row format changes, the checksum also changes. For example, the change in storage format for temporal types such as `TIME`, `DATETIME`, and`TIMESTAMP` just described mean that, if a 5.5 table is upgraded to MySQL 5.6, the checksum value may change.

Important If the checksums for two tables are different, then it is almost certain that the tables are different in some way. However, because the hashing function used by`CHECKSUM TABLE` is not guaranteed to be collision-free, there is a slight chance that two tables which are not identical can produce the same checksum.

#### 13.7.2.4 OPTIMIZE TABLE Statement

```
OPTIMIZE [NO_WRITE_TO_BINLOG | LOCAL]
TABLE tbl_name [, tbl_name] ...
```

`OPTIMIZE TABLE` reorganizes the physical storage of table data and associated index data, to reduce storage space and improve I/O efficiency when accessing the table. The exact changes made to each table depend on the storage engine used by that table.

Use `OPTIMIZE TABLE` in these cases, depending on the type of table:

- After doing substantial insert, update, or delete operations on an `InnoDB` table that has its own .ibd file

because it was created with the `innodb_file_per_table` option enabled. The table and indexes are reorganized, and disk space can be reclaimed for use by the operating system.

- After doing substantial insert, update, or delete operations on columns that are part of a `FULLTEXT` index

in an `InnoDB` table. Set the configuration option `innodb_optimize_fulltext_only=1` first. To keep the index maintenance period to a reasonable time, set the `innodb_ft_num_word_optimize` option Table Maintenance Statements to specify how many words to update in the search index, and run a sequence of `OPTIMIZE TABLE`statements until the search index is fully updated.

- After deleting a large part of a `MyISAM` or `ARCHIVE` table, or making many changes to a `MyISAM` or

`ARCHIVE` table with variable-length rows (tables that have `VARCHAR`, `VARBINARY`, `BLOB`, or `TEXT`columns). Deleted rows are maintained in a linked list and subsequent `INSERT` operations reuse old row positions. You can use `OPTIMIZE TABLE` to reclaim the unused space and to defragment the data file.

After extensive changes to a table, this statement may also improve performance of statements that use the table, sometimes significantly.

This statement requires `SELECT` and `INSERT` privileges for the table.

`OPTIMIZE TABLE` works for `InnoDB`, `MyISAM`, and `ARCHIVE` tables. `OPTIMIZE TABLE` is also supported for dynamic columns of in-memory `NDB` tables. It does not work for fixed-width columns of in-memory tables, nor does it work for Disk Data tables. The performance of `OPTIMIZE` on NDB Cluster tables can be tuned using `--ndb-optimization-delay`, which controls the length of time to wait between processing batches of rows by `OPTIMIZE TABLE`. For more information, see Section 18.2.7.11, “Previous NDB Cluster Issues Resolved in NDB Cluster 7.3”.

For NDB Cluster tables, `OPTIMIZE TABLE` can be interrupted by (for example) killing the SQL thread performing the `OPTIMIZE` operation.

By default, `OPTIMIZE TABLE` does not work for tables created using any other storage engine and returns a result indicating this lack of support. You can make `OPTIMIZE TABLE` work for other storage engines by starting `mysqld` with the `--skip-new` option. In this case, `OPTIMIZE TABLE` is just mapped to `ALTER`

```
TABLE.
```

This statement does not work with views.

`OPTIMIZE TABLE` is supported for partitioned tables. For information about using this statement with partitioned tables and table partitions, see Section 19.3.4, “Maintenance of Partitions”.

By default, the server writes `OPTIMIZE TABLE` statements to the binary log so that they replicate to replicas. To suppress logging, specify the optional `NO_WRITE_TO_BINLOG` keyword or its alias `LOCAL`.

In MySQL 5.6.11 only, `gtid_next` must be set to `AUTOMATIC` before issuing this statement. (Bug#16062608, Bug #16715809, Bug #69045)

- OPTIMIZE TABLE Output
- InnoDB Details
- MyISAM Details
- Other Considerations

OPTIMIZE TABLE Output`OPTIMIZE TABLE` returns a result set with the columns shown in the following table.

Column Value`Table` The table name`Op` Always `optimize`

```
Msg_type  status, error, info, note, or warning
```

Table Maintenance Statements Column Value`Msg_text` An informational message`OPTIMIZE TABLE` table catches and throws any errors that occur while copying table statistics from the old file to the newly created file. For example. if the user ID of the owner of the `.frm`, `.MYD`, or `.MYI`file is different from the user ID of the `mysqld` process, `OPTIMIZE TABLE` generates a "cannot change ownership of the file" error unless `mysqld` is started by the `root` user.

InnoDB Details For `InnoDB` tables, `OPTIMIZE TABLE` is mapped to `ALTER TABLE ... FORCE`, which rebuilds the table to update index statistics and free unused space in the clustered index. This is displayed in the output of`OPTIMIZE TABLE` when you run it on an `InnoDB` table, as shown here:

```
mysql> OPTIMIZE TABLE foo;
+----------+----------+----------+-------------------------------------------------------------------+
| Table    | Op       | Msg_type | Msg_text                                                          |
+----------+----------+----------+-------------------------------------------------------------------+
| test.foo | optimize | note     | Table does not support optimize, doing recreate + analyze instead |
| test.foo | optimize | status   | OK                                                                |
+----------+----------+----------+-------------------------------------------------------------------+
```

Prior to Mysql 5.6.17, `OPTIMIZE TABLE` does not use online DDL. Consequently, concurrent DML(`INSERT`, `UPDATE`, `DELETE`) is not permitted on a table while `OPTIMIZE TABLE` is running, and secondary indexes are not created as efficiently.

As of MySQL 5.6.17, `OPTIMIZE TABLE` uses online DDL for regular and partitioned `InnoDB` tables, which reduces downtime for concurrent DML operations. The table rebuild triggered by `OPTIMIZE TABLE` is completed in place. An exclusive table lock is only taken briefly during the prepare phase and the commit phase of the operation. During the prepare phase, metadata is updated and an intermediate table is created. During the commit phase, table metadata changes are committed.

`OPTIMIZE TABLE` rebuilds the table using the table copy method under the following conditions:

- When the `old_alter_table` system variable is enabled.
- When the server is started with the `--skip-new` option.

`OPTIMIZE TABLE` using online DDL is not supported for `InnoDB` tables that contain `FULLTEXT` indexes.

The table copy method is used instead.

`InnoDB` stores data using a page-allocation method and does not suffer from fragmentation in the same way that legacy storage engines (such as `MyISAM`) do. When considering whether or not to run optimize,consider the workload of transactions that your server is expected to process:

- Some level of fragmentation is expected. `InnoDB` only fills pages 93% full, to leave room for updates

without having to split pages.

- Delete operations might leave gaps that leave pages less filled than desired, which could make it

worthwhile to optimize the table.

- Updates to rows usually rewrite the data within the same page, depending on the data type and row

format, when sufficient space is available. See Section 14.9.5, “How Compression Works for InnoDB Tables” and Section 14.11, “InnoDB Row Formats”.

- High-concurrency workloads might leave gaps in indexes over time, as `InnoDB` retains multiple versions

of the same data due through its MVCC mechanism. See Section 14.3, “InnoDB Multi-Versioning”.

Table Maintenance Statements MyISAM Details For `MyISAM` tables, `OPTIMIZE TABLE` works as follows:

1. If the table has deleted or split rows, repair the table.
2. If the index pages are not sorted, sort them.
3. If the table's statistics are not up to date (and the repair could not be accomplished by sorting the

index), update them.

Other Considerations For `InnoDB` tables prior to 5.6.17 and other table types, MySQL locks the table during the time `OPTIMIZE``TABLE` is running. As of MySQL 5.6.17, `OPTIMIZE TABLE` is performed online for regular and partitioned`InnoDB` tables.

`OPTIMIZE TABLE` does not sort R-tree indexes, such as spatial indexes on `POINT` columns. (Bug#23578)

#### 13.7.2.5 REPAIR TABLE Statement

```
REPAIR [NO_WRITE_TO_BINLOG | LOCAL]
TABLE tbl_name [, tbl_name] ...
[QUICK] [EXTENDED] [USE_FRM]
```

`REPAIR TABLE` repairs a possibly corrupted table, for certain storage engines only.

This statement requires `SELECT` and `INSERT` privileges for the table.

Although normally you should never have to run `REPAIR TABLE`, if disaster strikes, this statement is very likely to get back all your data from a `MyISAM` table. If your tables become corrupted often, try to find the reason for it, to eliminate the need to use `REPAIR TABLE`. See Section B.3.3.3, “What to Do If MySQL Keeps Crashing”, and Section 15.2.4, “MyISAM Table Problems”.

`REPAIR TABLE` checks the table to see whether an upgrade is required. If so, it performs the upgrade,following the same rules as `CHECK TABLE ... FOR UPGRADE`. See Section 13.7.2.2, “CHECK TABLE Statement”, for more information.

> Important

- Make a backup of a table before performing a table repair operation; under some

circumstances the operation might cause data loss. Possible causes include but are not limited to file system errors. See Chapter 7, Backup and Recovery.

- If the server exits during a `REPAIR TABLE` operation, it is essential after

restarting it that you immediately execute another `REPAIR TABLE` statement for the table before performing any other operations on it. In the worst case, you might have a new clean index file without information about the data file, and then the next operation you perform could overwrite the data file. This is an unlikely but possible scenario that underscores the value of making a backup first.

- In the event that a table on the source becomes corrupted and you run `REPAIR`

`TABLE` on it, any resulting changes to the original table are not propagated to replicas.

- In MySQL 5.6.11 only, `gtid_next` must be set to `AUTOMATIC` before issuing this

statement. (Bug #16062608, Bug #16715809, Bug #69045)Table Maintenance Statements

- REPAIR TABLE Storage Engine and Partitioning Support
- REPAIR TABLE Options
- REPAIR TABLE Output
- Table Repair Considerations

REPAIR TABLE Storage Engine and Partitioning Support`REPAIR TABLE` works for `MyISAM`, `ARCHIVE`, and `CSV` tables. For `MyISAM` tables, it has the same effect as `myisamchk --recover tbl_name` by default. This statement does not work with views.

`REPAIR TABLE` is supported for partitioned tables. However, the `USE_FRM` option cannot be used with this statement on a partitioned table.

You can use `ALTER TABLE ... REPAIR PARTITION` to repair one or more partitions; for more information, see Section 13.1.7, “ALTER TABLE Statement”, and Section 19.3.4, “Maintenance of Partitions”.

> REPAIR TABLE Options

```
- NO_WRITE_TO_BINLOG or LOCAL
```

By default, the server writes `REPAIR TABLE` statements to the binary log so that they replicate to replicas. To suppress logging, specify the optional `NO_WRITE_TO_BINLOG` keyword or its alias `LOCAL`.

```
- QUICK
```

If you use the `QUICK` option, `REPAIR TABLE` tries to repair only the index file, and not the data file. This type of repair is like that done by `myisamchk --recover --quick`.

```
- EXTENDED
```

If you use the `EXTENDED` option, MySQL creates the index row by row instead of creating one index at a time with sorting. This type of repair is like that done by `myisamchk --safe-recover`.

```
- USE_FRM
```

The `USE_FRM` option is available for use if the `.MYI` index file is missing or if its header is corrupted.

This option tells MySQL not to trust the information in the `.MYI` file header and to re-create it using information from the `.frm` file. This kind of repair cannot be done with `myisamchk`.

Caution Use the `USE_FRM` option only if you cannot use regular `REPAIR` modes. Telling the server to ignore the `.MYI` file makes important table metadata stored in the `.MYI` unavailable to the repair process, which can have deleterious consequences:

- The current `AUTO_INCREMENT` value is lost.
- The link to deleted records in the table is lost, which means that free space for

deleted records remains unoccupied thereafter.

- The `.MYI` header indicates whether the table is compressed. If the server

ignores this information, it cannot tell that a table is compressed and repair Plugin and Loadable Function Statements can cause change or loss of table contents. This means that `USE_FRM` should not be used with compressed tables. That should not be necessary, anyway:Compressed tables are read only, so they should not become corrupt.

If you use `USE_FRM` for a table that was created by a different version of the MySQL server than the one you are currently running, `REPAIR TABLE` does not attempt to repair the table. In this case, the result set returned by `REPAIR``TABLE` contains a line with a `Msg_type` value of `error` and a `Msg_text` value

```
of Failed repairing incompatible .FRM file.
```

If `USE_FRM` is used, `REPAIR TABLE` does not check the table to see whether an upgrade is required.

REPAIR TABLE Output`REPAIR TABLE` returns a result set with the columns shown in the following table.

Column Value`Table` The table name`Op` Always `repair`

```
Msg_type  status, error, info, note, or warning
```

`Msg_text` An informational message The `REPAIR TABLE` statement might produce many rows of information for each repaired table. The last row has a `Msg_type` value of `status` and `Msg_test` normally should be `OK`. For a `MyISAM` table, if you do not get `OK`, you should try repairing it with `myisamchk --safe-recover`. (`REPAIR TABLE` does not implement all the options of `myisamchk`. With `myisamchk --safe-recover`, you can also use options that `REPAIR TABLE` does not support, such as `--max-record-length`.)`REPAIR TABLE` table catches and throws any errors that occur while copying table statistics from the old corrupted file to the newly created file. For example. if the user ID of the owner of the `.frm`, `.MYD`, or`.MYI` file is different from the user ID of the `mysqld` process, `REPAIR TABLE` generates a "cannot change ownership of the file" error unless `mysqld` is started by the `root` user.

Table Repair Considerations You may be able to increase `REPAIR TABLE` performance by setting certain system variables. See Section 8.6.3, “Optimizing REPAIR TABLE Statements”.

### 13.7.3 Plugin and Loadable Function Statements

#### 13.7.3.1 CREATE FUNCTION Statement for Loadable Functions

```
CREATE [AGGREGATE] FUNCTION function_name
RETURNS {STRING|INTEGER|REAL|DECIMAL}
SONAME shared_library_name
```

This statement loads the loadable function named `function_name`. (`CREATE FUNCTION` is also used to created stored functions; see Section 13.1.15, “CREATE PROCEDURE and CREATE FUNCTION Statements”.)A loadable function is a way to extend MySQL with a new function that works like a native (built-in) MySQL function such as `ABS()` or `CONCAT()`. See Adding a Loadable Function.

Plugin and Loadable Function Statements`function_name` is the name that should be used in SQL statements to invoke the function. The `RETURNS`clause indicates the type of the function's return value. `DECIMAL` is a legal value after `RETURNS`, but currently `DECIMAL` functions return string values and should be written like `STRING` functions.

The `AGGREGATE` keyword, if given, signifies that the function is an aggregate (group) function. An aggregate function works exactly like a native MySQL aggregate function such as `SUM()` or `COUNT()`.

`shared_library_name` is the base name of the shared library file containing the code that implements the function. The file must be located in the plugin directory. This directory is given by the value of the`plugin_dir` system variable. For more information, see Section 5.6.1, “Installing and Uninstalling Loadable Functions”.

`CREATE FUNCTION` requires the `INSERT` privilege for the `mysql` system database because it adds a row to the `mysql.func` system table to register the function.

During the normal startup sequence, the server loads functions registered in the `mysql.func` table. If the server is started with the `--skip-grant-tables` option, functions registered in the table are not loaded and are unavailable.

Note To upgrade the shared library associated with a loadable function, issue a `DROP``FUNCTION` statement, upgrade the shared library, and then issue a `CREATE``FUNCTION` statement. If you upgrade the shared library first and then use `DROP``FUNCTION`, the server may unexpectedly shut down.

#### 13.7.3.2 DROP FUNCTION Statement for Loadable Functions

```
DROP FUNCTION [IF EXISTS] function_name
```

This statement drops the loadable function named `function_name`. (`DROP FUNCTION` is also used to drop stored functions; see Section 13.1.26, “DROP PROCEDURE and DROP FUNCTION Statements”.)`DROP FUNCTION` is the complement of `CREATE FUNCTION`. It requires the `DELETE` privilege for the`mysql` system database because it removes the row from the `mysql.func` system table that registers the function.

During the normal startup sequence, the server loads functions registered in the `mysql.func` table.

Because `DROP FUNCTION` removes the `mysql.func` row for the dropped function, the server does not load the function during subsequent restarts.

Note To upgrade the shared library associated with a loadable function, issue a `DROP``FUNCTION` statement, upgrade the shared library, and then issue a `CREATE``FUNCTION` statement. If you upgrade the shared library first and then use `DROP``FUNCTION`, the server may unexpectedly shut down.

#### 13.7.3.3 INSTALL PLUGIN Statement

```
INSTALL PLUGIN plugin_name SONAME 'shared_library_name'
```

This statement installs a server plugin. It requires the `INSERT` privilege for the `mysql.plugin` system table because it adds a row to that table to register the plugin.

`plugin_name` is the name of the plugin as defined in the plugin descriptor structure contained in the library file (see Plugin Data Structures). Plugin names are not case-sensitive. For maximal compatibility,Plugin and Loadable Function Statements plugin names should be limited to ASCII letters, digits, and underscore because they are used in C source files, shell command lines, M4 and Bourne shell scripts, and SQL environments.

`shared_library_name` is the name of the shared library that contains the plugin code. The name includes the file name extension (for example, `libmyplugin.so`, `libmyplugin.dll`, or

```
libmyplugin.dylib).
```

The shared library must be located in the plugin directory (the directory named by the `plugin_dir` system variable). The library must be in the plugin directory itself, not in a subdirectory. By default, `plugin_dir`is the `plugin` directory under the directory named by the `pkglibdir` configuration variable, but it can be changed by setting the value of `plugin_dir` at server startup. For example, set its value in a `my.cnf` file:

```
[mysqld]
plugin_dir=/path/to/plugin/directory
```

If the value of `plugin_dir` is a relative path name, it is taken to be relative to the MySQL base directory(the value of the `basedir` system variable).

`INSTALL PLUGIN` loads and initializes the plugin code to make the plugin available for use. A plugin is initialized by executing its initialization function, which handles any setup that the plugin must perform before it can be used. When the server shuts down, it executes the deinitialization function for each plugin that is loaded so that the plugin has a chance to perform any final cleanup.

`INSTALL PLUGIN` also registers the plugin by adding a line that indicates the plugin name and library file name to the `mysql.plugin` system table. During the normal startup sequence, the server loads and initializes plugins registered in `mysql.plugin`. This means that a plugin is installed with `INSTALL``PLUGIN` only once, not every time the server starts. If the server is started with the `--skip-grant-``tables` option, plugins registered in the `mysql.plugin` table are not loaded and are unavailable.

A plugin library can contain multiple plugins. For each of them to be installed, use a separate `INSTALL``PLUGIN` statement. Each statement names a different plugin, but all of them specify the same library name.

`INSTALL PLUGIN` causes the server to read option (`my.cnf`) files just as during server startup. This enables the plugin to pick up any relevant options from those files. It is possible to add plugin options to an option file even before loading a plugin (if the `loose` prefix is used). It is also possible to uninstall a plugin,edit `my.cnf`, and install the plugin again. Restarting the plugin this way enables it to the new option values without a server restart.

For options that control individual plugin loading at server startup, see Section 5.5.1, “Installing and Uninstalling Plugins”. If you need to load plugins for a single server startup when the `--skip-grant-``tables` option is given (which tells the server not to read system tables), use the `--plugin-load` option.

See Section 5.1.6, “Server Command Options”.

To remove a plugin, use the `UNINSTALL PLUGIN` statement.

For additional information about plugin loading, see Section 5.5.1, “Installing and Uninstalling Plugins”.

To see what plugins are installed, use the `SHOW PLUGINS` statement or query the `INFORMATION_SCHEMA`the `PLUGINS` table.

If you recompile a plugin library and need to reinstall it, you can use either of the following methods:

- Use `UNINSTALL PLUGIN` to uninstall all plugins in the library, install the new plugin library file in the

plugin directory, and then use `INSTALL PLUGIN` to install all plugins in the library. This procedure has the advantage that it can be used without stopping the server. However, if the plugin library contains many plugins, you must issue many `INSTALL PLUGIN` and `UNINSTALL PLUGIN` statements.

SET Statements

- Stop the server, install the new plugin library file in the plugin directory, and restart the server.

#### 13.7.3.4 UNINSTALL PLUGIN Statement

```
UNINSTALL PLUGIN plugin_name
```

This statement removes an installed server plugin. `UNINSTALL PLUGIN` is the complement of `INSTALL``PLUGIN`. It requires the `DELETE` privilege for the `mysql.plugin` system table because it removes the row from that table that registers the plugin.

`plugin_name` must be the name of some plugin that is listed in the `mysql.plugin` table. The server executes the plugin's deinitialization function and removes the row for the plugin from the `mysql.plugin`system table, so that subsequent server restarts do not load and initialize the plugin. `UNINSTALL PLUGIN`does not remove the plugin's shared library file.

You cannot uninstall a plugin if any table that uses it is open.

Plugin removal has implications for the use of associated tables. For example, if a full-text parser plugin is associated with a `FULLTEXT` index on the table, uninstalling the plugin makes the table unusable. Any attempt to access the table results in an error. The table cannot even be opened, so you cannot drop an index for which the plugin is used. This means that uninstalling a plugin is something to do with care unless you do not care about the table contents. If you are uninstalling a plugin with no intention of reinstalling it later and you care about the table contents, you should dump the table with `mysqldump` and remove the`WITH PARSER` clause from the dumped `CREATE TABLE` statement so that you can reload the table later.

If you do not care about the table, `DROP TABLE` can be used even if any plugins associated with the table are missing.

For additional information about plugin loading, see Section 5.5.1, “Installing and Uninstalling Plugins”.

### 13.7.4 SET Statements

The `SET` statement has several forms. Descriptions for those forms that are not associated with a specific server capability appear in subsections of this section:

- `SET var_name = value` enables you to assign values to variables that affect the operation of the

server or clients. See Section 13.7.4.1, “SET Syntax for Variable Assignment”.

- `SET CHARACTER SET` and `SET NAMES` assign values to character set and collation variables

associated with the current connection to the server. See Section 13.7.4.2, “SET CHARACTER SET Statement”, and Section 13.7.4.3, “SET NAMES Statement”.

Descriptions for the other forms appear elsewhere, grouped with other statements related to the capability they help implement:

- `SET PASSWORD` assigns account passwords. See Section 13.7.1.7, “SET PASSWORD Statement”.
- `SET TRANSACTION ISOLATION LEVEL` sets the isolation level for transaction processing. See

Section 13.3.6, “SET TRANSACTION Statement”.

#### 13.7.4.1 SET Syntax for Variable Assignment

```
SET variable = expr [, variable = expr] ...
variable: {
user_var_name
| param_name
| local_var_name
```

SET Statements

```
| {GLOBAL | @@GLOBAL.} system_var_name
| [SESSION | @@SESSION. | @@] system_var_name
}
SET ONE_SHOT system_var_name = expr
```

`SET` syntax for variable assignment enables you to assign values to different types of variables that affect the operation of the server or clients:

- User-defined variables. See Section 9.4, “User-Defined Variables”.
- Stored procedure and function parameters, and stored program local variables. See Section 13.6.4,

“Variables in Stored Programs”.

- System variables. See Section 5.1.7, “Server System Variables”. System variables also can be set at

server startup, as described in Section 5.1.8, “Using System Variables”.

A `SET` statement that assigns variable values is not written to the binary log, so in replication scenarios it affects only the host on which you execute it. To affect all replication hosts, execute the statement on each host.

The following sections describe `SET` syntax for setting variables. They use the = assignment operator, but the `:=` assignment operator is also permitted for this purpose.

- User-Defined Variable Assignment
- Parameter and Local Variable Assignment
- System Variable Assignment
- SET Error Handling
- Multiple Variable Assignment
- System Variable References in Expressions
- ONE_SHOT Assignment

User-Defined Variable Assignment User-defined variables are created locally within a session and exist only within the context of that session;

see Section 9.4, “User-Defined Variables”.

A user-defined variable is written as `@var_name` and is assigned an expression value as follows:

```
SET @var_name = expr;
```

Examples:

```
SET @name = 43;
SET @total_tax = (SELECT SUM(tax) FROM taxable_transactions);
```

As demonstrated by those statements, `expr` can range from simple (a literal value) to more complex (the value returned by a scalar subquery).

Parameter and Local Variable Assignment`SET` applies to parameters and local variables in the context of the stored object within which they are defined. The following procedure uses the `increment` procedure parameter and `counter` local variable:SET Statements

```
CREATE PROCEDURE p(increment INT)
BEGIN
DECLARE counter INT DEFAULT 0;
WHILE counter < 10 DO
-- ... do work ...
SET counter = counter + increment;
END WHILE;
END;
```

System Variable Assignment The MySQL server maintains system variables that configure its operation. A system variable can have a global value that affects server operation as a whole, a session value that affects the current session, or both. Many system variables are dynamic and can be changed at runtime using the `SET` statement to affect operation of the current server instance. (To make a global system variable setting permanent so that it applies across server restarts, you should also set it in an option file.)If you change a session system variable, the value remains in effect within your session until you change the variable to a different value or the session ends. The change has no effect on other sessions.

If you change a global system variable, the value is remembered and used to initialize the session value for new sessions until you change the variable to a different value or the server exits. The change is visible to any client that accesses the global value. However, the change affects the corresponding session value only for clients that connect after the change. The global variable change does not affect the session value for any current client sessions (not even the session within which the global value change occurs).

Note Setting a global system variable value always requires special privileges. Setting a session system variable value normally requires no special privileges and can be done by any user, although there are exceptions. For more information, see Section 5.1.8.1, “System Variable Privileges”.

The following discussion describes the syntax options for setting system variables:

- To assign a value to a global system variable, precede the variable name by the `GLOBAL` keyword or the

`@@GLOBAL.` qualifier:

```
SET GLOBAL max_connections = 1000;
SET @@GLOBAL.max_connections = 1000;
```

- To assign a value to a session system variable, precede the variable name by the `SESSION` or `LOCAL`

keyword, by the `@@SESSION.`, `@@LOCAL.`, or `@@` qualifier, or by no keyword or no modifier at all:

```
SET SESSION sql_mode = 'TRADITIONAL';
SET LOCAL sql_mode = 'TRADITIONAL';
SET @@SESSION.sql_mode = 'TRADITIONAL';
SET @@LOCAL.sql_mode = 'TRADITIONAL';
SET @@sql_mode = 'TRADITIONAL';
SET sql_mode = 'TRADITIONAL';
```

A client can change its own session variables, but not those of any other client.

To set a global system variable value to the compiled-in MySQL default value or a session system variable to the current corresponding global value, set the variable to the value `DEFAULT`. For example, the following two statements are identical in setting the session value of `max_join_size` to the current global value:

```
SET @@SESSION.max_join_size = DEFAULT;
```

SET Statements

```
SET @@SESSION.max_join_size = @@GLOBAL.max_join_size;
```

To display system variable names and values:

- Use the `SHOW VARIABLES` statement; see Section 13.7.5.40, “SHOW VARIABLES Statement”.
- Several `INFORMATION_SCHEMA` tables provide system variable information. See Section 21.3.10, “The

INFORMATION_SCHEMA GLOBAL_VARIABLES and SESSION_VARIABLES Tables”.

SET Error Handling If any variable assignment in a `SET` statement fails, the entire statement fails and no variables are changed.

`SET` produces an error under the circumstances described here. Most of the examples show `SET`statements that use keyword syntax (for example, `GLOBAL` or `SESSION`), but the principles are also true for statements that use the corresponding modifiers (for example, `@@GLOBAL.` or `@@SESSION.`).

- Use of `SET` (any variant) to set a read-only variable:

```
mysql> SET GLOBAL version = 'abc';
ERROR 1238 (HY000): Variable 'version' is a read only variable
```

- Use of `GLOBAL` to set a variable that has only a session value:

```
mysql> SET GLOBAL sql_log_bin = ON;
ERROR 1231 (42000): Variable 'sql_log_bin' can't be
set to the value of 'ON'
```

- Use of `SESSION` to set a variable that has only a global value:

```
mysql> SET SESSION max_connections = 1000;
ERROR 1229 (HY000): Variable 'max_connections' is a
GLOBAL variable and should be set with SET GLOBAL
```

- Omission of `GLOBAL` to set a variable that has only a global value:

```
mysql> SET max_connections = 1000;
ERROR 1229 (HY000): Variable 'max_connections' is a
GLOBAL variable and should be set with SET GLOBAL
```

- The `@@GLOBAL.`, `@@SESSION.`, and `@@` modifiers apply only to system variables. An error occurs for

attempts to apply them to user-defined variables, stored procedure or function parameters, or stored program local variables.

- Not all system variables can be set to `DEFAULT`. In such cases, assigning `DEFAULT` results in an error.
- An error occurs for attempts to assign `DEFAULT` to user-defined variables, stored procedure or function

parameters, or stored program local variables.

Multiple Variable Assignment A `SET` statement can contain multiple variable assignments, separated by commas. This statement assigns a value to a user-defined variable and a system variable:

```
SET @x = 1, SESSION sql_mode = '';
```

If you set multiple system variables in a single statement, the most recent `GLOBAL` or `SESSION` keyword in the statement is used for following assignments that have no keyword specified.

SET Statements Examples of multiple-variable assignment:

```
SET GLOBAL sort_buffer_size = 1000000, SESSION sort_buffer_size = 1000000;
SET @@GLOBAL.sort_buffer_size = 1000000, @@LOCAL.sort_buffer_size = 1000000;
SET GLOBAL max_connections = 1000, sort_buffer_size = 1000000;
```

The `@@GLOBAL.`, `@@SESSION.`, and `@@` modifiers apply only to the immediately following system variable,not any remaining system variables. This statement sets the `sort_buffer_size` global value to 50000 and the session value to 1000000:

```
SET @@GLOBAL.sort_buffer_size = 50000, sort_buffer_size = 1000000;
```

System Variable References in Expressions To refer to the value of a system variable in expressions, use one of the `@@`-modifiers. For example, you can retrieve system variable values in a `SELECT` statement like this:

```
SELECT @@GLOBAL.sql_mode, @@SESSION.sql_mode, @@sql_mode;
```

Note A reference to a system variable in an expression as `@@var_name` (with `@@` rather than `@@GLOBAL.` or `@@SESSION.`) returns the session value if it exists and the global value otherwise. This differs from `SET @@var_name = expr`, which always refers to the session value.

ONE_SHOT Assignment The `SET ONE_SHOT` syntax is for internal use only, has been deprecated since MySQL 5.0, and was removed in MySQL 5.6.1.

#### 13.7.4.2 SET CHARACTER SET Statement

```
SET {CHARACTER SET | CHARSET}
{'charset_name' | DEFAULT}
```

This statement maps all strings sent between the server and the current client with the given mapping.

`SET CHARACTER SET` sets three session system variables: `character_set_client` and`character_set_results` are set to the given character set, and `character_set_connection` to the value of `character_set_database`. See Section 10.4, “Connection Character Sets and Collations”.

`charset_name` may be quoted or unquoted.

The default character set mapping can be restored by using the value `DEFAULT`. The default depends on the server configuration.

Some character sets cannot be used as the client character set. Attempting to use them with `SET``CHARACTER SET` produces an error. See Impermissible Client Character Sets.

#### 13.7.4.3 SET NAMES Statement

```
SET NAMES {'charset_name'
[COLLATE 'collation_name'] | DEFAULT}
```

This statement sets the three session system variables `character_set_client`,`character_set_connection`, and `character_set_results` to the given character set. Setting SHOW Statements`character_set_connection` to `charset_name` also sets `collation_connection` to the default collation for `charset_name`. See Section 10.4, “Connection Character Sets and Collations”.

The optional `COLLATE` clause may be used to specify a collation explicitly. If given, the collation must one of the permitted collations for `charset_name`.

`charset_name` and `collation_name` may be quoted or unquoted.

The default mapping can be restored by using a value of `DEFAULT`. The default depends on the server configuration.

Some character sets cannot be used as the client character set. Attempting to use them with `SET NAMES`produces an error. See Impermissible Client Character Sets.

### 13.7.5 SHOW Statements

`SHOW` has many forms that provide information about databases, tables, columns, or status information about the server. This section describes those following:

```
SHOW AUTHORS
SHOW {BINARY | MASTER} LOGS
SHOW BINLOG EVENTS [IN 'log_name'] [FROM pos] [LIMIT [offset,] row_count]
SHOW {CHARACTER SET | CHARSET} [like_or_where]
SHOW COLLATION [like_or_where]
SHOW [FULL] COLUMNS FROM tbl_name [FROM db_name] [like_or_where]
SHOW CONTRIBUTORS
SHOW CREATE DATABASE db_name
SHOW CREATE EVENT event_name
SHOW CREATE FUNCTION func_name
SHOW CREATE PROCEDURE proc_name
SHOW CREATE TABLE tbl_name
SHOW CREATE TRIGGER trigger_name
SHOW CREATE VIEW view_name
SHOW DATABASES [like_or_where]
SHOW ENGINE engine_name {STATUS | MUTEX}
SHOW [STORAGE] ENGINES
SHOW ERRORS [LIMIT [offset,] row_count]
SHOW EVENTS
SHOW FUNCTION CODE func_name
SHOW FUNCTION STATUS [like_or_where]
SHOW GRANTS FOR user
SHOW INDEX FROM tbl_name [FROM db_name]
SHOW MASTER STATUS
SHOW OPEN TABLES [FROM db_name] [like_or_where]
SHOW PLUGINS
SHOW PROCEDURE CODE proc_name
SHOW PROCEDURE STATUS [like_or_where]
SHOW PRIVILEGES
SHOW [FULL] PROCESSLIST
SHOW PROFILE [types] [FOR QUERY n] [OFFSET n] [LIMIT n]
SHOW PROFILES
SHOW RELAYLOG EVENTS [IN 'log_name'] [FROM pos] [LIMIT [offset,] row_count]
SHOW SLAVE HOSTS
SHOW SLAVE STATUS
SHOW [GLOBAL | SESSION] STATUS [like_or_where]
SHOW TABLE STATUS [FROM db_name] [like_or_where]
SHOW [FULL] TABLES [FROM db_name] [like_or_where]
SHOW TRIGGERS [FROM db_name] [like_or_where]
SHOW [GLOBAL | SESSION] VARIABLES [like_or_where]
SHOW WARNINGS [LIMIT [offset,] row_count]
like_or_where: {
LIKE 'pattern'
```

SHOW Statements

```
| WHERE expr
}
```

If the syntax for a given `SHOW` statement includes a `LIKE 'pattern'` part, `'pattern'` is a string that can contain the SQL % and _ wildcard characters. The pattern is useful for restricting statement output to matching values.

Several `SHOW` statements also accept a `WHERE` clause that provides more flexibility in specifying which rows to display. See Section 21.9, “Extensions to SHOW Statements”.

Many MySQL APIs (such as PHP) enable you to treat the result returned from a `SHOW` statement as you would a result set from a `SELECT`; see Chapter 23, Connectors and APIs, or your API documentation for more information. In addition, you can work in SQL with results from queries on tables in the`INFORMATION_SCHEMA` database, which you cannot easily do with results from `SHOW` statements. See Chapter 21, INFORMATION_SCHEMA Tables.

#### 13.7.5.1 SHOW AUTHORS Statement

```
SHOW AUTHORS
```

The `SHOW AUTHORS` statement displays information about the people who work on MySQL. For each author, it displays `Name`, `Location`, and `Comment` values.

This statement is removed as of MySQL 5.6.8.

#### 13.7.5.2 SHOW BINARY LOGS Statement

```
SHOW BINARY LOGS
SHOW MASTER LOGS
```

Lists the binary log files on the server. This statement is used as part of the procedure described in Section 13.4.1.1, “PURGE BINARY LOGS Statement”, that shows how to determine which logs can be purged.

```
mysql> SHOW BINARY LOGS;
+---------------+-----------+
| Log_name      | File_size |
+---------------+-----------+
| binlog.000015 |    724935 |
| binlog.000016 |    733481 |
+---------------+-----------+
```

`SHOW MASTER LOGS` is equivalent to `SHOW BINARY LOGS`.

A user with the `SUPER` or `REPLICATION CLIENT` privilege may execute this statement.

#### 13.7.5.3 SHOW BINLOG EVENTS Statement

```
SHOW BINLOG EVENTS
[IN 'log_name']
[FROM pos]
[LIMIT [offset,] row_count]
```

Shows the events in the binary log. If you do not specify `'log_name'`, the first binary log is displayed.

The `LIMIT` clause has the same syntax as for the `SELECT` statement. See Section 13.2.9, “SELECT Statement”.

SHOW Statements Note Issuing a `SHOW BINLOG EVENTS` with no `LIMIT` clause could start a very time-and resource-consuming process because the server returns to the client the complete contents of the binary log (which includes all statements executed by the server that modify data). As an alternative to `SHOW BINLOG EVENTS`, use the`mysqlbinlog` utility to save the binary log to a text file for later examination and analysis. See Section 4.6.8, “mysqlbinlog — Utility for Processing Binary Log Files”.

`SHOW BINLOG EVENTS` displays the following fields for each event in the binary log:

```
- Log_name
```

The name of the file that is being listed.

```
- Pos
```

The position at which the event occurs.

```
- Event_type
```

An identifier that describes the event type.

```
- Server_id
```

The server ID of the server on which the event originated.

```
- End_log_pos
```

The position at which the next event begins, which is equal to `Pos` plus the size of the event.

```
- Info
```

More detailed information about the event type. The format of this information depends on the event type.

Note Some events relating to the setting of user and system variables are not included in the output from `SHOW BINLOG EVENTS`. To get complete coverage of events within a binary log, use `mysqlbinlog`.

Note`SHOW BINLOG EVENTS` does not work with relay log files. You can use `SHOW``RELAYLOG EVENTS` for this purpose.

#### 13.7.5.4 SHOW CHARACTER SET Statement

```
SHOW {CHARACTER SET | CHARSET}
[LIKE 'pattern' | WHERE expr]
```

The `SHOW CHARACTER SET` statement shows all available character sets. The `LIKE` clause, if present,indicates which character set names to match. The `WHERE` clause can be given to select rows using more general conditions, as discussed in Section 21.9, “Extensions to SHOW Statements”. For example:

```
mysql> SHOW CHARACTER SET LIKE 'latin%';
+---------+-----------------------------+-------------------+--------+
```

SHOW Statements

```
| Charset | Description                 | Default collation | Maxlen |
+---------+-----------------------------+-------------------+--------+
| latin1  | cp1252 West European        | latin1_swedish_ci |      1 |
| latin2  | ISO 8859-2 Central European | latin2_general_ci |      1 |
| latin5  | ISO 8859-9 Turkish          | latin5_turkish_ci |      1 |
| latin7  | ISO 8859-13 Baltic          | latin7_general_ci |      1 |
+---------+-----------------------------+-------------------+--------+
```

`SHOW CHARACTER SET` output has these columns:

```
- Charset
```

The character set name.

```
- Description
```

A description of the character set.

```
- Default collation
```

The default collation for the character set.

```
- Maxlen
```

The maximum number of bytes required to store one character.

The `filename` character set is for internal use only; consequently, `SHOW CHARACTER SET` does not display it.

Character set information is also available from the `INFORMATION_SCHEMA` `CHARACTER_SETS` table.

#### 13.7.5.5 SHOW COLLATION Statement

```
SHOW COLLATION
[LIKE 'pattern' | WHERE expr]
```

This statement lists collations supported by the server. By default, the output from `SHOW COLLATION`includes all available collations. The `LIKE` clause, if present, indicates which collation names to match. The`WHERE` clause can be given to select rows using more general conditions, as discussed in Section 21.9,“Extensions to SHOW Statements”. For example:

```
mysql> SHOW COLLATION WHERE Charset = 'latin1';
+-------------------+---------+----+---------+----------+---------+
| Collation         | Charset | Id | Default | Compiled | Sortlen |
+-------------------+---------+----+---------+----------+---------+
| latin1_german1_ci | latin1  |  5 |         | Yes      |       1 |
| latin1_swedish_ci | latin1  |  8 | Yes     | Yes      |       1 |
| latin1_danish_ci  | latin1  | 15 |         | Yes      |       1 |
| latin1_german2_ci | latin1  | 31 |         | Yes      |       2 |
| latin1_bin        | latin1  | 47 |         | Yes      |       1 |
| latin1_general_ci | latin1  | 48 |         | Yes      |       1 |
| latin1_general_cs | latin1  | 49 |         | Yes      |       1 |
| latin1_spanish_ci | latin1  | 94 |         | Yes      |       1 |
+-------------------+---------+----+---------+----------+---------+
```

`SHOW COLLATION` output has these columns:

```
- Collation
```

The collation name.

SHOW Statements

```
- Charset
```

The name of the character set with which the collation is associated.

- `Id`

The collation ID.

```
- Default
```

Whether the collation is the default for its character set.

```
- Compiled
```

Whether the character set is compiled into the server.

```
- Sortlen
```

This is related to the amount of memory required to sort strings expressed in the character set.

To see the default collation for each character set, use the following statement. `Default` is a reserved word, so to use it as an identifier, it must be quoted as such:

```
mysql> SHOW COLLATION WHERE `Default` = 'Yes';
+---------------------+----------+----+---------+----------+---------+
| Collation           | Charset  | Id | Default | Compiled | Sortlen |
+---------------------+----------+----+---------+----------+---------+
| big5_chinese_ci     | big5     |  1 | Yes     | Yes      |       1 |
| dec8_swedish_ci     | dec8     |  3 | Yes     | Yes      |       1 |
| cp850_general_ci    | cp850    |  4 | Yes     | Yes      |       1 |
| hp8_english_ci      | hp8      |  6 | Yes     | Yes      |       1 |
| koi8r_general_ci    | koi8r    |  7 | Yes     | Yes      |       1 |
| latin1_swedish_ci   | latin1   |  8 | Yes     | Yes      |       1 |
...
```

Collation information is also available from the `INFORMATION_SCHEMA` `COLLATIONS` table. See Section 21.3.3, “The INFORMATION_SCHEMA COLLATIONS Table”.

#### 13.7.5.6 SHOW COLUMNS Statement

```
SHOW [FULL] {COLUMNS | FIELDS}
{FROM | IN} tbl_name
[{FROM | IN} db_name]
[LIKE 'pattern' | WHERE expr]
```

`SHOW COLUMNS` displays information about the columns in a given table. It also works for views. `SHOW``COLUMNS` displays information only for those columns for which you have some privilege.

```
mysql> SHOW COLUMNS FROM City;
+-------------+----------+------+-----+---------+----------------+
| Field       | Type     | Null | Key | Default | Extra          |
+-------------+----------+------+-----+---------+----------------+
| ID          | int(11)  | NO   | PRI | NULL    | auto_increment |
| Name        | char(35) | NO   |     |         |                |
| CountryCode | char(3)  | NO   | MUL |         |                |
| District    | char(20) | NO   |     |         |                |
| Population  | int(11)  | NO   |     | 0       |                |
+-------------+----------+------+-----+---------+----------------+
```

An alternative to `tbl_name FROM db_name` syntax is `db_name.tbl_name`. These two statements are equivalent:SHOW Statements

```
SHOW COLUMNS FROM mytable FROM mydb;
SHOW COLUMNS FROM mydb.mytable;
```

The optional `FULL` keyword causes the output to include the column collation and comments, as well as the privileges you have for each column.

The `LIKE` clause, if present, indicates which column names to match. The `WHERE` clause can be given to select rows using more general conditions, as discussed in Section 21.9, “Extensions to SHOW Statements”.

The data types may differ from what you expect them to be based on a `CREATE TABLE` statement because MySQL sometimes changes data types when you create or alter a table. The conditions under which this occurs are described in Section 13.1.17.6, “Silent Column Specification Changes”.

`SHOW COLUMNS` displays the following values for each table column:

```
- Field
```

The column name.

```
- Type
```

The column data type.

```
- Collation
```

The collation for nonbinary string columns, or `NULL` for other columns. This value is displayed only if you use the `FULL` keyword.

```
- Null
```

The column nullability. The value is `YES` if `NULL` values can be stored in the column, `NO` if not.

```
- Key
```

Whether the column is indexed:

- If `Key` is empty, the column either is not indexed or is indexed only as a secondary column in a

multiple-column, nonunique index.

- If `Key` is `PRI`, the column is a `PRIMARY KEY` or is one of the columns in a multiple-column `PRIMARY`

```
KEY.
```

- If `Key` is `UNI`, the column is the first column of a `UNIQUE` index. (A `UNIQUE` index permits multiple

`NULL` values, but you can tell whether the column permits `NULL` by checking the `Null` field.)

- If `Key` is `MUL`, the column is the first column of a nonunique index in which multiple occurrences of a

given value are permitted within the column.

If more than one of the `Key` values applies to a given column of a table, `Key` displays the one with the highest priority, in the order `PRI`, `UNI`, `MUL`.

A `UNIQUE` index may be displayed as `PRI` if it cannot contain `NULL` values and there is no `PRIMARY``KEY` in the table. A `UNIQUE` index may display as `MUL` if several columns form a composite `UNIQUE`index; although the combination of the columns is unique, each column can still hold multiple occurrences of a given value.

```
- Default
```

SHOW Statements The default value for the column. This is `NULL` if the column has an explicit default of `NULL`, or if the column definition includes no `DEFAULT` clause.

```
- Extra
```

Any additional information that is available about a given column. The value is nonempty in these cases: `auto_increment` for columns that have the `AUTO_INCREMENT` attribute; `on``update CURRENT_TIMESTAMP` for `TIMESTAMP` or `DATETIME` columns that have the `ON UPDATE``CURRENT_TIMESTAMP` attribute.

```
- Privileges
```

The privileges you have for the column. This value is displayed only if you use the `FULL` keyword.

```
- Comment
```

Any comment included in the column definition. This value is displayed only if you use the `FULL`keyword.

Table column information is also available from the `INFORMATION_SCHEMA` `COLUMNS` table. See Section 21.3.5, “The INFORMATION_SCHEMA COLUMNS Table”.

You can list a table's columns with the `mysqlshow db_name tbl_name` command.

The `DESCRIBE` statement provides information similar to `SHOW COLUMNS`. See Section 13.8.1,“DESCRIBE Statement”.

The `SHOW CREATE TABLE`, `SHOW TABLE STATUS`, and `SHOW INDEX` statements also provide information about tables. See Section 13.7.5, “SHOW Statements”.

#### 13.7.5.7 SHOW CONTRIBUTORS Statement

```
SHOW CONTRIBUTORS
```

The `SHOW CONTRIBUTORS` statement displays information about the people who contribute to MySQL source or to causes that we support. For each contributor, it displays `Name`, `Location`, and `Comment`values.

This statement is removed as of MySQL 5.6.8.

#### 13.7.5.8 SHOW CREATE DATABASE Statement

```
SHOW CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name
```

Shows the `CREATE DATABASE` statement that creates the named database. If the `SHOW` statement includes an `IF NOT EXISTS` clause, the output too includes such a clause. `SHOW CREATE SCHEMA` is a synonym for `SHOW CREATE DATABASE`.

```
mysql> SHOW CREATE DATABASE test\G
*************************** 1. row ***************************
Database: test
Create Database: CREATE DATABASE `test`
/*!40100 DEFAULT CHARACTER SET latin1 */
mysql> SHOW CREATE SCHEMA test\G
*************************** 1. row ***************************
```

SHOW Statements

```
Database: test
Create Database: CREATE DATABASE `test`
/*!40100 DEFAULT CHARACTER SET latin1 */
```

`SHOW CREATE DATABASE` quotes table and column names according to the value of the`sql_quote_show_create` option. See Section 5.1.7, “Server System Variables”.

#### 13.7.5.9 SHOW CREATE EVENT Statement

```
SHOW CREATE EVENT event_name
```

This statement displays the `CREATE EVENT` statement needed to re-create a given event. It requires the`EVENT` privilege for the database from which the event is to be shown. For example (using the same event`e_daily` defined and then altered in Section 13.7.5.19, “SHOW EVENTS Statement”):

```
mysql> SHOW CREATE EVENT myschema.e_daily\G
*************************** 1. row ***************************
Event: e_daily
sql_mode: NO_ENGINE_SUBSTITUTION
time_zone: SYSTEM
Create Event: CREATE DEFINER=`jon`@`ghidora` EVENT `e_daily`
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_TIMESTAMP + INTERVAL 6 HOUR
ON COMPLETION NOT PRESERVE
ENABLE
COMMENT 'Saves total number of sessions then
clears the table each day'
DO BEGIN
INSERT INTO site_activity.totals (time, total)
SELECT CURRENT_TIMESTAMP, COUNT(*)
FROM site_activity.sessions;
DELETE FROM site_activity.sessions;
END
character_set_client: utf8
collation_connection: utf8_general_ci
Database Collation: latin1_swedish_ci
```

`character_set_client` is the session value of the `character_set_client` system variable when the event was created. `collation_connection` is the session value of the `collation_connection`system variable when the event was created. `Database Collation` is the collation of the database with which the event is associated.

The output reflects the current status of the event (`ENABLE`) rather than the status with which it was created.

#### 13.7.5.10 SHOW CREATE FUNCTION Statement

```
SHOW CREATE FUNCTION func_name
```

This statement is similar to `SHOW CREATE PROCEDURE` but for stored functions. See Section 13.7.5.11,“SHOW CREATE PROCEDURE Statement”.

#### 13.7.5.11 SHOW CREATE PROCEDURE Statement

```
SHOW CREATE PROCEDURE proc_name
```

This statement is a MySQL extension. It returns the exact string that can be used to re-create the named stored procedure. A similar statement, `SHOW CREATE FUNCTION`, displays information about stored functions (see Section 13.7.5.10, “SHOW CREATE FUNCTION Statement”).

SHOW Statements To use either statement, you must be the user named in the routine `DEFINER` clause or have `SELECT`access to the `mysql.proc` table. If you do not have privileges for the routine itself, the value displayed for the `Create Procedure` or `Create Function` column is `NULL`.

```
mysql> SHOW CREATE PROCEDURE test.citycount\G
*************************** 1. row ***************************
Procedure: citycount
sql_mode: STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION
Create Procedure: CREATE DEFINER=`me`@`localhost`
PROCEDURE `citycount`(IN country CHAR(3), OUT cities INT)
BEGIN
SELECT COUNT(*) INTO cities FROM world.city
WHERE CountryCode = country;
END
character_set_client: utf8
collation_connection: utf8_general_ci
Database Collation: latin1_swedish_ci
mysql> SHOW CREATE FUNCTION test.hello\G
*************************** 1. row ***************************
Function: hello
sql_mode: STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION
Create Function: CREATE DEFINER=`me`@`localhost`
FUNCTION `hello`(s CHAR(20))
RETURNS char(50) CHARSET latin1
DETERMINISTIC
RETURN CONCAT('Hello, ',s,'!')
character_set_client: utf8
collation_connection: utf8_general_ci
Database Collation: latin1_swedish_ci
```

`character_set_client` is the session value of the `character_set_client` system variable when the routine was created. `collation_connection` is the session value of the `collation_connection`system variable when the routine was created. `Database Collation` is the collation of the database with which the routine is associated.

#### 13.7.5.12 SHOW CREATE TABLE Statement

```
SHOW CREATE TABLE tbl_name
```

Shows the `CREATE TABLE` statement that creates the named table. To use this statement, you must have some privilege for the table. This statement also works with views.

```
mysql> SHOW CREATE TABLE t\G
*************************** 1. row ***************************
Table: t
Create Table: CREATE TABLE `t` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`s` char(60) DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

`SHOW CREATE TABLE` quotes table and column names according to the value of the`sql_quote_show_create` option. See Section 5.1.7, “Server System Variables”.

When altering the storage engine of a table, table options that are not applicable to the new storage engine are retained in the table definition to enable reverting the table with its previously defined options to the original storage engine, if necessary. For example, when changing the storage engine from InnoDB to MyISAM, InnoDB-specific options such as `ROW_FORMAT=COMPACT` are retained.

```
mysql> CREATE TABLE t1 (c1 INT PRIMARY KEY) ROW_FORMAT=COMPACT ENGINE=InnoDB;
mysql> ALTER TABLE t1 ENGINE=MyISAM;
```

SHOW Statements

```
mysql> SHOW CREATE TABLE t1\G
*************************** 1. row ***************************
Table: t1
Create Table: CREATE TABLE `t1` (
`c1` int(11) NOT NULL,
PRIMARY KEY (`c1`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT
```

When creating a table with strict mode disabled, the storage engine's default row format is used if the specified row format is not supported. The actual row format of the table is reported in the `Row_format`column in response to `SHOW TABLE STATUS`. `SHOW CREATE TABLE` shows the row format that was specified in the `CREATE TABLE` statement.

#### 13.7.5.13 SHOW CREATE TRIGGER Statement

```
SHOW CREATE TRIGGER trigger_name
```

This statement shows the `CREATE TRIGGER` statement that creates the named trigger. This statement requires the `TRIGGER` privilege for the table associated with the trigger.

```
mysql> SHOW CREATE TRIGGER ins_sum\G
*************************** 1. row ***************************
Trigger: ins_sum
sql_mode: NO_ENGINE_SUBSTITUTION
SQL Original Statement: CREATE DEFINER=`me`@`localhost` TRIGGER ins_sum
BEFORE INSERT ON account
FOR EACH ROW SET @sum = @sum + NEW.amount
character_set_client: utf8
collation_connection: utf8_general_ci
Database Collation: latin1_swedish_ci
```

`SHOW CREATE TRIGGER` output has these columns:

- `Trigger`: The trigger name.
- `sql_mode`: The SQL mode in effect when the trigger executes.
- `SQL Original Statement`: The `CREATE TRIGGER` statement that defines the trigger.
- `character_set_client`: The session value of the `character_set_client` system variable when

the trigger was created.

- `collation_connection`: The session value of the `collation_connection` system variable when

the trigger was created.

- `Database Collation`: The collation of the database with which the trigger is associated.

Trigger information is also available from the `INFORMATION_SCHEMA` `TRIGGERS` table. See Section 21.3.27, “The INFORMATION_SCHEMA TRIGGERS Table”.

#### 13.7.5.14 SHOW CREATE VIEW Statement

```
SHOW CREATE VIEW view_name
```

This statement shows the `CREATE VIEW` statement that creates the named view.

```
mysql> SHOW CREATE VIEW v\G
*************************** 1. row ***************************
View: v
Create View: CREATE ALGORITHM=UNDEFINED
DEFINER=`bob`@`localhost`
```

SHOW Statements

```
SQL SECURITY DEFINER VIEW
`v` AS select 1 AS `a`,2 AS `b`
character_set_client: utf8
collation_connection: utf8_general_ci
```

`character_set_client` is the session value of the `character_set_client` system variable when the view was created. `collation_connection` is the session value of the `collation_connection`system variable when the view was created.

Use of `SHOW CREATE VIEW` requires the `SHOW VIEW` privilege, and the `SELECT` privilege for the view in question.

View information is also available from the `INFORMATION_SCHEMA` `VIEWS` table. See Section 21.3.29,“The INFORMATION_SCHEMA VIEWS Table”.

MySQL lets you use different `sql_mode` settings to tell the server the type of SQL syntax to support. For example, you might use the `ANSI` SQL mode to ensure MySQL correctly interprets the standard SQL concatenation operator, the double bar (`||`), in your queries. If you then create a view that concatenates items, you might worry that changing the `sql_mode` setting to a value different from `ANSI` could cause the view to become invalid. But this is not the case. No matter how you write out a view definition, MySQL always stores it the same way, in a canonical form. Here is an example that shows how the server changes a double bar concatenation operator to a `CONCAT()` function:

```
mysql> SET sql_mode = 'ANSI';
Query OK, 0 rows affected (0.00 sec)
mysql> CREATE VIEW test.v AS SELECT 'a' || 'b' as col1;
Query OK, 0 rows affected (0.01 sec)
mysql> SHOW CREATE VIEW test.v\G
*************************** 1. row ***************************
View: v
Create View: CREATE VIEW "v" AS select concat('a','b') AS "col1"
...
1 row in set (0.00 sec)
```

The advantage of storing a view definition in canonical form is that changes made later to the value of`sql_mode` does not affect the results from the view. However an additional consequence is that comments prior to `SELECT` are stripped from the definition by the server.

#### 13.7.5.15 SHOW DATABASES Statement

```
SHOW {DATABASES | SCHEMAS}
[LIKE 'pattern' | WHERE expr]
```

`SHOW DATABASES` lists the databases on the MySQL server host. `SHOW SCHEMAS` is a synonym for `SHOW``DATABASES`. The `LIKE` clause, if present, indicates which database names to match. The `WHERE` clause can be given to select rows using more general conditions, as discussed in Section 21.9, “Extensions to SHOW Statements”.

You see only those databases for which you have some kind of privilege, unless you have the global `SHOW``DATABASES` privilege. You can also get this list using the `mysqlshow` command.

If the server was started with the `--skip-show-database` option, you cannot use this statement at all unless you have the `SHOW DATABASES` privilege.

MySQL implements databases as directories in the data directory, so this statement simply lists directories in that location. However, the output may include names of directories that do not correspond to actual databases.

SHOW Statements Database information is also available from the `INFORMATION_SCHEMA` `SCHEMATA` table. See Section 21.3.20, “The INFORMATION_SCHEMA SCHEMATA Table”.

Caution Because a global privilege is considered a privilege for all databases, any global privilege enables a user to see all database names with `SHOW DATABASES` or by examining the `INFORMATION_SCHEMA` `SCHEMATA` table.

#### 13.7.5.16 SHOW ENGINE Statement

```
SHOW ENGINE engine_name {STATUS | MUTEX}
```

`SHOW ENGINE` displays operational information about a storage engine. It requires the `PROCESS` privilege.

The statement has these variants:

```
SHOW ENGINE INNODB STATUS
SHOW ENGINE INNODB MUTEX
SHOW ENGINE {NDB | NDBCLUSTER} STATUS
SHOW ENGINE PERFORMANCE_SCHEMA STATUS
```

`SHOW ENGINE INNODB STATUS` displays extensive information from the standard `InnoDB` Monitor about the state of the `InnoDB` storage engine. For information about the standard monitor and other `InnoDB`Monitors that provide information about `InnoDB` processing, see Section 14.17, “InnoDB Monitors”.

`SHOW ENGINE INNODB MUTEX` displays `InnoDB` mutex and rw-lock statistics.

Note Most `SHOW ENGINE INNODB MUTEX` output is removed in 5.6.14. `SHOW ENGINE``INNODB MUTEX` output is removed entirely in MySQL 5.7.2. `InnoDB` mutexes can be monitored using Performance Schema tables. For an example, see Section 14.16.1, “Monitoring InnoDB Mutex Waits Using Performance Schema”.

```
- Type
```

Always `InnoDB`.

```
- Name
```

The source file where the mutex is implemented, and the line number in the file where the mutex is created. The line number is specific to your version of MySQL.

```
- Status
```

The mutex status. This field displays several values if `WITH_DEBUG` was defined at MySQL compilation time. If `WITH_DEBUG` was not defined, the statement displays only the `os_waits` value. In the latter case (without `WITH_DEBUG`), the information on which the output is based is insufficient to distinguish regular mutexes and mutexes that protect rw-locks (which permit multiple readers or a single writer).

Consequently, the output may appear to contain multiple rows for the same mutex.

- `count` indicates how many times the mutex was requested.
- `spin_waits` indicates how many times the spinlock had to run.
- `spin_rounds` indicates the number of spinlock rounds. (`spin_rounds` divided by `spin_waits`

provides the average round count.)SHOW Statements

- `os_waits` indicates the number of operating system waits. This occurs when the spinlock did not

work (the mutex was not locked during the spinlock and it was necessary to yield to the operating system and wait).

- `os_yields` indicates the number of times a thread trying to lock a mutex gave up its timeslice and

yielded to the operating system (on the presumption that permitting other threads to run frees the mutex so that it can be locked).

- `os_wait_times` indicates the amount of time (in ms) spent in operating system waits. In MySQL 5.6

timing is disabled and this value is always 0.

`SHOW ENGINE INNODB MUTEX` does not list mutexes and rw-locks for each buffer pool block, as the amount of output would be overwhelming on systems with a large buffer pool. `SHOW ENGINE INNODB``MUTEX` does, however, print aggregate `BUF_BLOCK_MUTEX` spin, wait, and call values for buffer pool block mutexes and rw-locks. `SHOW ENGINE INNODB MUTEX` also does not list any mutexes or rw-locks that have never been waited on (`os_waits=0`). Thus, `SHOW ENGINE INNODB MUTEX` only displays information about mutexes and rw-locks outside of the buffer pool that have caused at least one OS-level wait.

`SHOW ENGINE INNODB MUTEX` information can be used to diagnose system problems. For example,large values of `spin_waits` and `spin_rounds` may indicate scalability problems.

Use `SHOW ENGINE PERFORMANCE_SCHEMA STATUS` to inspect the internal operation of the Performance Schema code:

```
mysql> SHOW ENGINE PERFORMANCE_SCHEMA STATUS\G
...
*************************** 3. row ***************************
Type: performance_schema
Name: events_waits_history.row_size
Status: 76
*************************** 4. row ***************************
Type: performance_schema
Name: events_waits_history.row_count
Status: 10000
*************************** 5. row ***************************
Type: performance_schema
Name: events_waits_history.memory
Status: 760000
...
*************************** 57. row ***************************
Type: performance_schema
Name: performance_schema.memory
Status: 26459600
...
```

This statement is intended to help the DBA understand the effects that different Performance Schema options have on memory requirements.

`Name` values consist of two parts, which name an internal buffer and a buffer attribute, respectively.

Interpret buffer names as follows:

- An internal buffer that is not exposed as a table is named within parentheses. Examples:

```
(pfs_cond_class).row_size, (pfs_mutex_class).memory.
```

- An internal buffer that is exposed as a table in the `performance_schema` database is named

after the table, without parentheses. Examples: `events_waits_history.row_size`,

```
mutex_instances.row_count.
```

SHOW Statements

- A value that applies to the Performance Schema as a whole begins with `performance_schema`.

Example: `performance_schema.memory`.

Buffer attributes have these meanings:

- `row_size` is the size of the internal record used by the implementation, such as the size of a row in a

table. `row_size` values cannot be changed.

- `row_count` is the number of internal records, such as the number of rows in a table. `row_count` values

can be changed using Performance Schema configuration options.

- For a table, `tbl_name.memory` is the product of `row_size` and `row_count`. For the Performance

Schema as a whole, `performance_schema.memory` is the sum of all the memory used (the sum of all other `memory` values).

In some cases, there is a direct relationship between a Performance Schema configuration parameter and a `SHOW ENGINE` value. For example, `events_waits_history_long.row_count`corresponds to `performance_schema_events_waits_history_long_size`. In other cases, the relationship is more complex. For example, `events_waits_history.row_count` corresponds to`performance_schema_events_waits_history_size` (the number of rows per thread) multiplied by`performance_schema_max_thread_instances` ( the number of threads).

SHOW ENGINE NDB STATUS. If the server has the `NDB` storage engine enabled, `SHOW ENGINE``NDB STATUS` displays cluster status information such as the number of connected data nodes, the cluster connectstring, and cluster binary log epochs, as well as counts of various Cluster API objects created by the MySQL Server when connected to the cluster. Sample output from this statement is shown here:

```
mysql> SHOW ENGINE NDB STATUS;
+------------+-----------------------+--------------------------------------------------+
| Type       | Name                  | Status                                           |
+------------+-----------------------+--------------------------------------------------+
| ndbcluster | connection            | cluster_node_id=7,
connected_host=198.51.100.103, connected_port=1186, number_of_data_nodes=4,
number_of_ready_data_nodes=3, connect_count=0                                         |
| ndbcluster | NdbTransaction        | created=6, free=0, sizeof=212                    |
| ndbcluster | NdbOperation          | created=8, free=8, sizeof=660                    |
| ndbcluster | NdbIndexScanOperation | created=1, free=1, sizeof=744                    |
| ndbcluster | NdbIndexOperation     | created=0, free=0, sizeof=664                    |
| ndbcluster | NdbRecAttr            | created=1285, free=1285, sizeof=60               |
| ndbcluster | NdbApiSignal          | created=16, free=16, sizeof=136                  |
| ndbcluster | NdbLabel              | created=0, free=0, sizeof=196                    |
| ndbcluster | NdbBranch             | created=0, free=0, sizeof=24                     |
| ndbcluster | NdbSubroutine         | created=0, free=0, sizeof=68                     |
| ndbcluster | NdbCall               | created=0, free=0, sizeof=16                     |
| ndbcluster | NdbBlob               | created=1, free=1, sizeof=264                    |
| ndbcluster | NdbReceiver           | created=4, free=0, sizeof=68                     |
| ndbcluster | binlog                | latest_epoch=155467, latest_trans_epoch=148126,
latest_received_binlog_epoch=0, latest_handled_binlog_epoch=0,
latest_applied_binlog_epoch=0                                                         |
+------------+-----------------------+--------------------------------------------------+
```

The `Status` column in each of these rows provides information about the MySQL server's connection to the cluster and about the cluster binary log's status, respectively. The `Status` information is in the form of comma-delimited set of name/value pairs.

The `connection` row's `Status` column contains the name/value pairs described in the following table.

Name Value`cluster_node_id` The node ID of the MySQL server in the cluster SHOW Statements Name Value`connected_host` The host name or IP address of the cluster management server to which the MySQL server is connected`connected_port` The port used by the MySQL server to connect to the management server (`connected_host`)`number_of_data_nodes` The number of data nodes configured for the cluster(that is, the number of `[ndbd]` sections in the cluster `config.ini` file)`number_of_ready_data_nodes` The number of data nodes in the cluster that are actually running`connect_count` The number of times this `mysqld` has connected or reconnected to cluster data nodes The `binlog` row's `Status` column contains information relating to NDB Cluster Replication. The name/value pairs it contains are described in the following table.

Name Value`latest_epoch` The most recent epoch most recently run on this MySQL server (that is, the sequence number of the most recent transaction run on the server)`latest_trans_epoch` The most recent epoch processed by the cluster's data nodes`latest_received_binlog_epoch` The most recent epoch received by the binary log thread`latest_handled_binlog_epoch` The most recent epoch processed by the binary log thread (for writing to the binary log)`latest_applied_binlog_epoch` The most recent epoch actually written to the binary log See Section 18.7, “NDB Cluster Replication”, for more information.

The remaining rows from the output of `SHOW ENGINE NDB STATUS` which are most likely to prove useful in monitoring the cluster are listed here by `Name`:

- `NdbTransaction`: The number and size of `NdbTransaction` objects that have been created. An

`NdbTransaction` is created each time a table schema operation (such as `CREATE TABLE` or `ALTER``TABLE`) is performed on an `NDB` table.

- `NdbOperation`: The number and size of `NdbOperation` objects that have been created.
- `NdbIndexScanOperation`: The number and size of `NdbIndexScanOperation` objects that have

been created.

- `NdbIndexOperation`: The number and size of `NdbIndexOperation` objects that have been created.
- `NdbRecAttr`: The number and size of `NdbRecAttr` objects that have been created. In general, one of

these is created each time a data manipulation statement is performed by an SQL node.

- `NdbBlob`: The number and size of `NdbBlob` objects that have been created. An `NdbBlob` is created for

each new operation involving a `BLOB` column in an `NDB` table.

SHOW Statements

- `NdbReceiver`: The number and size of any `NdbReceiver` object that have been created. The number

in the `created` column is the same as the number of data nodes in the cluster to which the MySQL server has connected.

Note`SHOW ENGINE NDB STATUS` returns an empty result if no operations involving`NDB` tables have been performed during the current session by the MySQL client accessing the SQL node on which this statement is run.

#### 13.7.5.17 SHOW ENGINES Statement

```
SHOW [STORAGE] ENGINES
```

`SHOW ENGINES` displays status information about the server's storage engines. This is particularly useful for checking whether a storage engine is supported, or to see what the default engine is.

For information about MySQL storage engines, see Chapter 14, The InnoDB Storage Engine, and Chapter 15, Alternative Storage Engines.

```
mysql> SHOW ENGINES\G
*************************** 1. row ***************************
Engine: FEDERATED
Support: NO
Comment: Federated MySQL storage engine
Transactions: NULL
XA: NULL
Savepoints: NULL
*************************** 2. row ***************************
Engine: MRG_MYISAM
Support: YES
Comment: Collection of identical MyISAM tables
Transactions: NO
XA: NO
Savepoints: NO
*************************** 3. row ***************************
Engine: MyISAM
Support: YES
Comment: MyISAM storage engine
Transactions: NO
XA: NO
Savepoints: NO
*************************** 4. row ***************************
Engine: BLACKHOLE
Support: YES
Comment: /dev/null storage engine (anything you write to it disappears)
Transactions: NO
XA: NO
Savepoints: NO
*************************** 5. row ***************************
Engine: CSV
Support: YES
Comment: CSV storage engine
Transactions: NO
XA: NO
Savepoints: NO
*************************** 6. row ***************************
Engine: MEMORY
Support: YES
Comment: Hash based, stored in memory, useful for temporary tables
Transactions: NO
XA: NO
Savepoints: NO
*************************** 7. row ***************************
```

SHOW Statements

```
Engine: ARCHIVE
Support: YES
Comment: Archive storage engine
Transactions: NO
XA: NO
Savepoints: NO
*************************** 8. row ***************************
Engine: InnoDB
Support: DEFAULT
Comment: Supports transactions, row-level locking, and foreign keys
Transactions: YES
XA: YES
Savepoints: YES
*************************** 9. row ***************************
Engine: PERFORMANCE_SCHEMA
Support: YES
Comment: Performance Schema
Transactions: NO
XA: NO
Savepoints: NO
```

The output from `SHOW ENGINES` may vary according to the MySQL version used and other factors.

`SHOW ENGINES` output has these columns:

```
- Engine
```

The name of the storage engine.

```
- Support
```

The server's level of support for the storage engine, as shown in the following table.

Value Meaning`YES` The engine is supported and is active`DEFAULT` Like `YES`, plus this is the default engine`NO` The engine is not supported`DISABLED` The engine is supported but has been disabled A value of `NO` means that the server was compiled without support for the engine, so it cannot be enabled at runtime.

A value of `DISABLED` occurs either because the server was started with an option that disables the engine, or because not all options required to enable it were given. In the latter case, the error log should contain a reason indicating why the option is disabled. See Section 5.4.2, “The Error Log”.

You might also see `DISABLED` for a storage engine if the server was compiled to support it, but was started with a `--skip-engine_name` option. For the `NDB` storage engine, `DISABLED` means the server was compiled with support for NDB Cluster, but was not started with the `--ndbcluster` option.

All MySQL servers support `MyISAM` tables. It is not possible to disable `MyISAM`.

```
- Comment
```

A brief description of the storage engine.

```
- Transactions
```

Whether the storage engine supports transactions.

SHOW Statements

- `XA`

Whether the storage engine supports XA transactions.

```
- Savepoints
```

Whether the storage engine supports savepoints.

Storage engine information is also available from the `INFORMATION_SCHEMA` `ENGINES` table. See Section 21.3.7, “The INFORMATION_SCHEMA ENGINES Table”.

#### 13.7.5.18 SHOW ERRORS Statement

```
SHOW ERRORS [LIMIT [offset,] row_count]
SHOW COUNT(*) ERRORS
```

`SHOW ERRORS` is a diagnostic statement that is similar to `SHOW WARNINGS`, except that it displays information only for errors, rather than for errors, warnings, and notes.

The `LIMIT` clause has the same syntax as for the `SELECT` statement. See Section 13.2.9, “SELECT Statement”.

The `SHOW COUNT(*) ERRORS` statement displays the number of errors. You can also retrieve this number from the `error_count` variable:

```
SHOW COUNT(*) ERRORS;
SELECT @@error_count;
```

`SHOW ERRORS` and `error_count` apply only to errors, not warnings or notes. In other respects, they are similar to `SHOW WARNINGS` and `warning_count`. In particular, `SHOW ERRORS` cannot display information for more than `max_error_count` messages, and `error_count` can exceed the value of`max_error_count` if the number of errors exceeds `max_error_count`.

For more information, see Section 13.7.5.41, “SHOW WARNINGS Statement”.

#### 13.7.5.19 SHOW EVENTS Statement

```
SHOW EVENTS
[{FROM | IN} schema_name]
[LIKE 'pattern' | WHERE expr]
```

This statement displays information about Event Manager events, which are discussed in Section 20.4,“Using the Event Scheduler”. It requires the `EVENT` privilege for the database from which the events are to be shown.

In its simplest form, `SHOW EVENTS` lists all of the events in the current schema:

```
mysql> SELECT CURRENT_USER(), SCHEMA();
+----------------+----------+
| CURRENT_USER() | SCHEMA() |
+----------------+----------+
| jon@ghidora    | myschema |
+----------------+----------+
1 row in set (0.00 sec)
mysql> SHOW EVENTS\G
*************************** 1. row ***************************
Db: myschema
Name: e_daily
Definer: jon@ghidora
Time zone: SYSTEM
```

SHOW Statements

```
Type: RECURRING
Execute at: NULL
Interval value: 1
Interval field: DAY
Starts: 2018-08-08 11:06:34
Ends: NULL
Status: ENABLED
Originator: 1
character_set_client: utf8
collation_connection: utf8_general_ci
Database Collation: latin1_swedish_ci
```

To see events for a specific schema, use the `FROM` clause. For example, to see events for the `test`schema, use the following statement:

```
SHOW EVENTS FROM test;
```

The `LIKE` clause, if present, indicates which event names to match. The `WHERE` clause can be given to select rows using more general conditions, as discussed in Section 21.9, “Extensions to SHOW Statements”.

`SHOW EVENTS` output has these columns:

- `Db`

The name of the schema (database) to which the event belongs.

```
- Name
```

The name of the event.

```
- Definer
```

The account of the user who created the event, in `'user_name'@'host_name'` format.

```
- Time zone
```

The event time zone, which is the time zone used for scheduling the event and that is in effect within the event as it executes. The default value is `SYSTEM`.

```
- Type
```

The event repetition type, either `ONE TIME` (transient) or `RECURRING` (repeating).

```
- Execute At
```

For a one-time event, this is the `DATETIME` value specified in the `AT` clause of the `CREATE EVENT`statement used to create the event, or of the last `ALTER EVENT` statement that modified the event. The value shown in this column reflects the addition or subtraction of any `INTERVAL` value included in the event's `AT` clause. For example, if an event is created using `ON SCHEDULE AT CURRENT_TIMESTAMP``+ '1:6' DAY_HOUR`, and the event was created at 2018-02-09 14:05:30, the value shown in this column would be `'2018-02-10 20:05:30'`. If the event's timing is determined by an `EVERY` clause instead of an `AT` clause (that is, if the event is recurring), the value of this column is `NULL`.

```
- Interval Value
```

For a recurring event, the number of intervals to wait between event executions. For a transient event,the value of this column is always `NULL`.

```
- Interval Field
```

SHOW Statements The time units used for the interval which a recurring event waits before repeating. For a transient event,the value of this column is always `NULL`.

```
- Starts
```

The start date and time for a recurring event. This is displayed as a `DATETIME` value, and is `NULL` if no start date and time are defined for the event. For a transient event, this column is always `NULL`. For a recurring event whose definition includes a `STARTS` clause, this column contains the corresponding`DATETIME` value. As with the `Execute At` column, this value resolves any expressions used. If there is no `STARTS` clause affecting the timing of the event, this column is `NULL`

```
- Ends
```

For a recurring event whose definition includes a `ENDS` clause, this column contains the corresponding`DATETIME` value. As with the `Execute At` column, this value resolves any expressions used. If there is no `ENDS` clause affecting the timing of the event, this column is `NULL`.

```
- Status
```

The event status. One of `ENABLED`, `DISABLED`, or `SLAVESIDE_DISABLED`. `SLAVESIDE_DISABLED`indicates that the creation of the event occurred on another MySQL server acting as a replication source and replicated to the current MySQL server which is acting as a replica, but the event is not presently being executed on the replica. For more information, see Section 17.4.1.16, “Replication of Invoked Features”. information.

```
- Originator
```

The server ID of the MySQL server on which the event was created; used in replication. This value may be updated by `ALTER EVENT` to the server ID of the server on which that statement occurs, if executed on a source server. The default value is 0.

```
- character_set_client
```

The session value of the `character_set_client` system variable when the event was created.

```
- collation_connection
```

The session value of the `collation_connection` system variable when the event was created.

```
- Database Collation
```

The collation of the database with which the event is associated.

For more information about `SLAVESIDE_DISABLED` and the `Originator` column, see Section 17.4.1.16,“Replication of Invoked Features”.

Times displayed by `SHOW EVENTS` are given in the event time zone, as discussed in Section 20.4.4, “Event Metadata”.

Event information is also available from the `INFORMATION_SCHEMA` `EVENTS` table. See Section 21.3.8,“The INFORMATION_SCHEMA EVENTS Table”.

The event action statement is not shown in the output of `SHOW EVENTS`. Use `SHOW CREATE EVENT` or the

```
INFORMATION_SCHEMA EVENTS table.
```

#### 13.7.5.20 SHOW FUNCTION CODE Statement

```
SHOW FUNCTION CODE func_name
```

SHOW Statements This statement is similar to `SHOW PROCEDURE CODE` but for stored functions. See Section 13.7.5.28,“SHOW PROCEDURE CODE Statement”.

#### 13.7.5.21 SHOW FUNCTION STATUS Statement

```
SHOW FUNCTION STATUS
[LIKE 'pattern' | WHERE expr]
```

This statement is similar to `SHOW PROCEDURE STATUS` but for stored functions. See Section 13.7.5.29,“SHOW PROCEDURE STATUS Statement”.

#### 13.7.5.22 SHOW GRANTS Statement

```
SHOW GRANTS [FOR user]
```

This statement displays the privileges that are assigned to a MySQL user account, in the form of `GRANT`statements that must be executed to duplicate the privilege assignments.

`SHOW GRANTS` requires the `SELECT` privilege for the `mysql` system database, except to display privileges for the current user. For output that includes an `IDENTIFIED BY PASSWORD` clause displaying an account password hash value, the `SUPER` privilege is required to see the actual hash value. Otherwise, the value displays as `<secret>`.

To name the account for `SHOW GRANTS`, use the same format as for the `GRANT` statement (for example,

```
'jeffrey'@'localhost'):
mysql> SHOW GRANTS FOR 'jeffrey'@'localhost';
+------------------------------------------------------------------+
| Grants for jeffrey@localhost                                     |
+------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `jeffrey`@`localhost`                      |
| GRANT SELECT, INSERT, UPDATE ON `db1`.* TO `jeffrey`@`localhost` |
+------------------------------------------------------------------+
```

The host part, if omitted, defaults to `'%'`. For additional information about specifying account names, see Section 6.2.4, “Specifying Account Names”.

To display the privileges granted to the current user (the account you are using to connect to the server),you can use any of the following statements:

```
SHOW GRANTS;
SHOW GRANTS FOR CURRENT_USER;
SHOW GRANTS FOR CURRENT_USER();
```

If `SHOW GRANTS FOR CURRENT_USER` (or any equivalent syntax) is used in definer context, such as within a stored procedure that executes with definer rather than invoker privileges, the grants displayed are those of the definer and not the invoker.

`SHOW GRANTS` does not display privileges that are available to the named account but are granted to a different account. For example, if an anonymous account exists, the named account might be able to use its privileges, but `SHOW GRANTS` does not display them.

#### 13.7.5.23 SHOW INDEX Statement

```
SHOW {INDEX | INDEXES | KEYS}
{FROM | IN} tbl_name
[{FROM | IN} db_name]
[WHERE expr]
```

`SHOW INDEX` returns table index information. The format resembles that of the `SQLStatistics` call in ODBC. This statement requires some privilege for any column in the table.

SHOW Statements

```
mysql> SHOW INDEX FROM City\G
*************************** 1. row ***************************
Table: city
Non_unique: 0
Key_name: PRIMARY
Seq_in_index: 1
Column_name: ID
Collation: A
Cardinality: 4188
Sub_part: NULL
Packed: NULL
Null:
Index_type: BTREE
Comment:
Index_comment:
*************************** 2. row ***************************
Table: city
Non_unique: 1
Key_name: CountryCode
Seq_in_index: 1
Column_name: CountryCode
Collation: A
Cardinality: 4188
Sub_part: NULL
Packed: NULL
Null:
Index_type: BTREE
Comment:
Index_comment:
```

An alternative to `tbl_name FROM db_name` syntax is `db_name`.`tbl_name`. These two statements are equivalent:

```
SHOW INDEX FROM mytable FROM mydb;
SHOW INDEX FROM mydb.mytable;
```

The `WHERE` clause can be given to select rows using more general conditions, as discussed in Section 21.9, “Extensions to SHOW Statements”.

`SHOW INDEX` returns the following fields:

```
- Table
```

The name of the table.

```
- Non_unique
```

0 if the index cannot contain duplicates, 1 if it can.

```
- Key_name
```

The name of the index. If the index is the primary key, the name is always `PRIMARY`.

```
- Seq_in_index
```

The column sequence number in the index, starting with 1.

```
- Column_name
```

The name of the column.

```
- Collation
```

How the column is sorted in the index. This can have values A (ascending) or `NULL` (not sorted).

SHOW Statements

```
- Cardinality
```

An estimate of the number of unique values in the index. To update this number, run `ANALYZE TABLE`or (for `MyISAM` tables) `myisamchk -a`.

`Cardinality` is counted based on statistics stored as integers, so the value is not necessarily exact even for small tables. The higher the cardinality, the greater the chance that MySQL uses the index when doing joins.

```
- Sub_part
```

The index prefix. That is, the number of indexed characters if the column is only partly indexed, `NULL` if the entire column is indexed.

Note Prefix limits are measured in bytes. However, prefix lengths for index specifications in `CREATE TABLE`, `ALTER TABLE`, and `CREATE INDEX`statements are interpreted as number of characters for nonbinary string types(`CHAR`, `VARCHAR`, `TEXT`) and number of bytes for binary string types (`BINARY`,`VARBINARY`, `BLOB`). Take this into account when specifying a prefix length for a nonbinary string column that uses a multibyte character set.

For additional information about index prefixes, see Section 8.3.4, “Column Indexes”, and Section 13.1.13, “CREATE INDEX Statement”.

```
- Packed
```

Indicates how the key is packed. `NULL` if it is not.

```
- Null
```

Contains `YES` if the column may contain `NULL` values and `''` if not.

```
- Index_type
```

The index method used (`BTREE`, `FULLTEXT`, `HASH`, `RTREE`).

```
- Comment
```

Information about the index not described in its own column, such as `disabled` if the index is disabled.

```
- Index_comment
```

Any comment provided for the index with a `COMMENT` attribute when the index was created.

Information about table indexes is also available from the `INFORMATION_SCHEMA` `STATISTICS` table. See Section 21.3.22, “The INFORMATION_SCHEMA STATISTICS Table”.

You can list a table's indexes with the `mysqlshow -k db_name tbl_name` command.

#### 13.7.5.24 SHOW MASTER STATUS Statement

```
SHOW MASTER STATUS
```

This statement provides status information about the binary log files of the source. It requires either the`SUPER` or `REPLICATION CLIENT` privilege.

Example:SHOW Statements

```
mysql> SHOW MASTER STATUS\G
*************************** 1. row ***************************
File: source-bin.000002
Position: 1307
Binlog_Do_DB: test
Binlog_Ignore_DB: manual, mysql
Executed_Gtid_Set: 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5
1 row in set (0.00 sec)
```

When global transaction IDs are in use, this column shows the set of GTIDs for transactions that have been executed on the source. This is the same as the value for the `gtid_executed` system variable on this server, as well as the value for `Executed_Gtid_Set` in the output of `SHOW SLAVE STATUS` on this server.

#### 13.7.5.25 SHOW OPEN TABLES Statement

```
SHOW OPEN TABLES
[{FROM | IN} db_name]
[LIKE 'pattern' | WHERE expr]
```

`SHOW OPEN TABLES` lists the non-`TEMPORARY` tables that are currently open in the table cache. See Section 8.4.3.1, “How MySQL Opens and Closes Tables”. The `FROM` clause, if present, restricts the tables shown to those present in the `db_name` database. The `LIKE` clause, if present, indicates which table names to match. The `WHERE` clause can be given to select rows using more general conditions, as discussed in Section 21.9, “Extensions to SHOW Statements”.

`SHOW OPEN TABLES` output has these columns:

```
- Database
```

The database containing the table.

```
- Table
```

The table name.

```
- In_use
```

The number of table locks or lock requests there are for the table. For example, if one client acquires a lock for a table using `LOCK TABLE t1 WRITE`, `In_use` is 1. If another client issues `LOCK TABLE``t1 WRITE` while the table remains locked, the client blocks waiting for the lock, but the lock request causes `In_use` to be 2. If the count is zero, the table is open but not currently being used. `In_use` is also increased by the `HANDLER ... OPEN` statement and decreased by `HANDLER ... CLOSE`.

```
- Name_locked
```

Whether the table name is locked. Name locking is used for operations such as dropping or renaming tables.

If you have no privileges for a table, it does not show up in the output from `SHOW OPEN TABLES`.

#### 13.7.5.26 SHOW PLUGINS Statement

```
SHOW PLUGINS
```

`SHOW PLUGINS` displays information about server plugins.

Example of `SHOW PLUGINS` output:

```
mysql> SHOW PLUGINS\G
```

SHOW Statements

```
*************************** 1. row ***************************
Name: binlog
Status: ACTIVE
Type: STORAGE ENGINE
Library: NULL
License: GPL
*************************** 2. row ***************************
Name: CSV
Status: ACTIVE
Type: STORAGE ENGINE
Library: NULL
License: GPL
*************************** 3. row ***************************
Name: MEMORY
Status: ACTIVE
Type: STORAGE ENGINE
Library: NULL
License: GPL
*************************** 4. row ***************************
Name: MyISAM
Status: ACTIVE
Type: STORAGE ENGINE
Library: NULL
License: GPL
...
```

`SHOW PLUGINS` output has these columns:

```
- Name
```

The name used to refer to the plugin in statements such as `INSTALL PLUGIN` and `UNINSTALL`

```
PLUGIN.
- Status
```

The plugin status, one of `ACTIVE`, `INACTIVE`, `DISABLED`, or `DELETED`.

```
- Type
```

The type of plugin, such as `STORAGE ENGINE`, `INFORMATION_SCHEMA`, or `AUTHENTICATION`.

```
- Library
```

The name of the plugin shared library file. This is the name used to refer to the plugin file in statements such as `INSTALL PLUGIN` and `UNINSTALL PLUGIN`. This file is located in the directory named by the `plugin_dir` system variable. If the library name is `NULL`, the plugin is compiled in and cannot be uninstalled with `UNINSTALL PLUGIN`.

```
- License
```

How the plugin is licensed (for example, `GPL`).

For plugins installed with `INSTALL PLUGIN`, the `Name` and `Library` values are also registered in the`mysql.plugin` system table.

For information about plugin data structures that form the basis of the information displayed by `SHOW``PLUGINS`, see The MySQL Plugin API.

Plugin information is also available from the `INFORMATION_SCHEMA` `.PLUGINS` table. See Section 21.3.15, “The INFORMATION_SCHEMA PLUGINS Table”.

#### 13.7.5.27 SHOW PRIVILEGES Statement

SHOW Statements

```
SHOW PRIVILEGES
```

`SHOW PRIVILEGES` shows the list of system privileges that the MySQL server supports. The exact list of privileges depends on the version of your server.

```
mysql> SHOW PRIVILEGES\G
*************************** 1. row ***************************
Privilege: Alter
Context: Tables
Comment: To alter the table
*************************** 2. row ***************************
Privilege: Alter routine
Context: Functions,Procedures
Comment: To alter or drop stored functions/procedures
*************************** 3. row ***************************
Privilege: Create
Context: Databases,Tables,Indexes
Comment: To create new databases and tables
*************************** 4. row ***************************
Privilege: Create routine
Context: Databases
Comment: To use CREATE FUNCTION/PROCEDURE
*************************** 5. row ***************************
Privilege: Create temporary tables
Context: Databases
Comment: To use CREATE TEMPORARY TABLE
...
```

Privileges belonging to a specific user are displayed by the `SHOW GRANTS` statement. See Section 13.7.5.22, “SHOW GRANTS Statement”, for more information.

#### 13.7.5.28 SHOW PROCEDURE CODE Statement

```
SHOW PROCEDURE CODE proc_name
```

This statement is a MySQL extension that is available only for servers that have been built with debugging support. It displays a representation of the internal implementation of the named stored procedure. A similar statement, `SHOW FUNCTION CODE`, displays information about stored functions (see Section 13.7.5.20, “SHOW FUNCTION CODE Statement”).

To use either statement, you must be the owner of the routine or have `SELECT` access to the `mysql.proc`table.

If the named routine is available, each statement produces a result set. Each row in the result set corresponds to one “instruction” in the routine. The first column is `Pos`, which is an ordinal number beginning with 0. The second column is `Instruction`, which contains an SQL statement (usually changed from the original source), or a directive which has meaning only to the stored-routine handler.

```
mysql> DELIMITER //
mysql> CREATE PROCEDURE p1 ()
BEGIN
DECLARE fanta INT DEFAULT 55;
DROP TABLE t2;
LOOP
INSERT INTO t3 VALUES (fanta);
END LOOP;
END//
Query OK, 0 rows affected (0.01 sec)
mysql> SHOW PROCEDURE CODE p1//
+-----+----------------------------------------+
| Pos | Instruction                            |
+-----+----------------------------------------+
```

SHOW Statements

```
|   0 | set fanta@0 55                         |
|   1 | stmt 9 "DROP TABLE t2"                 |
|   2 | stmt 5 "INSERT INTO t3 VALUES (fanta)" |
|   3 | jump 2                                 |
+-----+----------------------------------------+
4 rows in set (0.00 sec)
mysql> CREATE FUNCTION test.hello (s CHAR(20))
RETURNS CHAR(50) DETERMINISTIC
RETURN CONCAT('Hello, ',s,'!');
Query OK, 0 rows affected (0.00 sec)
mysql> SHOW FUNCTION CODE test.hello;
+-----+---------------------------------------+
| Pos | Instruction                           |
+-----+---------------------------------------+
|   0 | freturn 254 concat('Hello, ',s@0,'!') |
+-----+---------------------------------------+
1 row in set (0.00 sec)
```

In this example, the nonexecutable `BEGIN` and `END` statements have disappeared, and for the `DECLARE``variable_name` statement, only the executable part appears (the part where the default is assigned). For each statement that is taken from source, there is a code word `stmt` followed by a type (9 means `DROP`, 5 means `INSERT`, and so on). The final row contains an instruction `jump 2`, meaning `GOTO instruction``#2`.

#### 13.7.5.29 SHOW PROCEDURE STATUS Statement

```
SHOW PROCEDURE STATUS
[LIKE 'pattern' | WHERE expr]
```

This statement is a MySQL extension. It returns characteristics of a stored procedure, such as the database, name, type, creator, creation and modification dates, and character set information. A similar statement, `SHOW FUNCTION STATUS`, displays information about stored functions (see Section 13.7.5.21,“SHOW FUNCTION STATUS Statement”).

To use either statement, you must be the owner of the routine or have `SELECT` access to the `mysql.proc`table.

The `LIKE` clause, if present, indicates which procedure or function names to match. The `WHERE` clause can be given to select rows using more general conditions, as discussed in Section 21.9, “Extensions to SHOW Statements”.

```
mysql> SHOW PROCEDURE STATUS LIKE 'sp1'\G
*************************** 1. row ***************************
Db: test
Name: sp1
Type: PROCEDURE
Definer: testuser@localhost
Modified: 2018-08-08 13:54:11
Created: 2018-08-08 13:54:11
Security_type: DEFINER
Comment:
character_set_client: utf8
collation_connection: utf8_general_ci
Database Collation: latin1_swedish_ci
mysql> SHOW FUNCTION STATUS LIKE 'hello'\G
*************************** 1. row ***************************
Db: test
Name: hello
Type: FUNCTION
Definer: testuser@localhost
```

SHOW Statements

```
Modified: 2020-03-10 11:14:27
Created: 2020-03-10 11:14:27
Security_type: DEFINER
Comment:
character_set_client: utf8
collation_connection: utf8_general_ci
Database Collation: latin1_swedish_ci
```

`character_set_client` is the session value of the `character_set_client` system variable when the routine was created. `collation_connection` is the session value of the `collation_connection`system variable when the routine was created. `Database Collation` is the collation of the database with which the routine is associated.

Stored routine information is also available from the `INFORMATION_SCHEMA` `PARAMETERS` and `ROUTINES`tables. See Section 21.3.13, “The INFORMATION_SCHEMA PARAMETERS Table”, and Section 21.3.19,“The INFORMATION_SCHEMA ROUTINES Table”.

#### 13.7.5.30 SHOW PROCESSLIST Statement

```
SHOW [FULL] PROCESSLIST
```

The MySQL process list indicates the operations currently being performed by the set of threads executing within the server. The `SHOW PROCESSLIST` statement is one source of process information. For a comparison of this statement with other sources, see Sources of Process Information.

If you have the `PROCESS` privilege, you can see all threads, even those belonging to other users. Otherwise(without the `PROCESS` privilege), nonanonymous users have access to information about their own threads but not threads for other users, and anonymous users have no access to thread information.

Without the `FULL` keyword, `SHOW PROCESSLIST` displays only the first 100 characters of each statement in the `Info` field.

The `SHOW PROCESSLIST` statement is very useful if you get the “too many connections” error message and want to find out what is going on. MySQL reserves one extra connection to be used by accounts that have the `SUPER` privilege, to ensure that administrators should always be able to connect and check the system (assuming that you are not giving this privilege to all your users).

Threads can be killed with the `KILL` statement. See Section 13.7.6.4, “KILL Statement”.

Example of `SHOW PROCESSLIST` output:

```
mysql> SHOW FULL PROCESSLIST\G
*************************** 1. row ***************************
Id: 1
User: system user
Host:
db: NULL
Command: Connect
Time: 1030455
State: Waiting for master to send event
Info: NULL
*************************** 2. row ***************************
Id: 2
User: system user
Host:
db: NULL
Command: Connect
Time: 1004
State: Has read all relay log; waiting for the slave
I/O thread to update it
Info: NULL
*************************** 3. row ***************************
```

SHOW Statements

```
Id: 3112
User: replikator
Host: artemis:2204
db: NULL
Command: Binlog Dump
Time: 2144
State: Has sent all binlog to slave; waiting for binlog to be updated
Info: NULL
*************************** 4. row ***************************
Id: 3113
User: replikator
Host: iconnect2:45781
db: NULL
Command: Binlog Dump
Time: 2086
State: Has sent all binlog to slave; waiting for binlog to be updated
Info: NULL
*************************** 5. row ***************************
Id: 3123
User: stefan
Host: localhost
db: apollon
Command: Query
Time: 0
State: NULL
Info: SHOW FULL PROCESSLIST
```

`SHOW PROCESSLIST` output has these columns:

- `Id`

The connection identifier. This is the same value displayed in the `ID` column of the`INFORMATION_SCHEMA` `PROCESSLIST` table, displayed in the `PROCESSLIST_ID` column of the Performance Schema `threads` table, and returned by the `CONNECTION_ID()` function within the thread.

```
- User
```

The MySQL user who issued the statement. A value of `system user` refers to a nonclient thread spawned by the server to handle tasks internally, for example, a delayed-row handler thread or an I/O or SQL thread used on replica hosts. For `system user`, there is no host specified in the `Host` column.

`unauthenticated user` refers to a thread that has become associated with a client connection but for which authentication of the client user has not yet occurred. `event_scheduler` refers to the thread that monitors scheduled events (see Section 20.4, “Using the Event Scheduler”).

```
- Host
```

The host name of the client issuing the statement (except for `system user`, for which there is no host).

The host name for TCP/IP connections is reported in `host_name:client_port` format to make it easier to determine which client is doing what.

- `db`

The default database for the thread, or `NULL` if none has been selected.

```
- Command
```

The type of command the thread is executing on behalf of the client, or `Sleep` if the session is idle. For descriptions of thread commands, see Section 8.14, “Examining Server Thread (Process) Information”.

The value of this column corresponds to the `COM_xxx` commands of the client/server protocol and`Com_xxx` status variables. See Section 5.1.9, “Server Status Variables”.

SHOW Statements

```
- Time
```

The time in seconds that the thread has been in its current state. For a replica SQL thread, the value is the number of seconds between the timestamp of the last replicated event and the real time of the replica host. See Section 17.2.1, “Replication Threads”.

```
- State
```

An action, event, or state that indicates what the thread is doing. For descriptions of `State` values, see Section 8.14, “Examining Server Thread (Process) Information”.

Most states correspond to very quick operations. If a thread stays in a given state for many seconds,there might be a problem that needs to be investigated.

```
- Info
```

The statement the thread is executing, or `NULL` if it is executing no statement. The statement might be the one sent to the server, or an innermost statement if the statement executes other statements. For example, if a `CALL` statement executes a stored procedure that is executing a `SELECT` statement, the`Info` value shows the `SELECT` statement.

#### 13.7.5.31 SHOW PROFILE Statement

```
SHOW PROFILE [type [, type] ... ]
[FOR QUERY n]
[LIMIT row_count [OFFSET offset]]
type: {
ALL
| BLOCK IO
| CONTEXT SWITCHES
| CPU
| IPC
| MEMORY
| PAGE FAULTS
| SOURCE
| SWAPS
}
```

The `SHOW PROFILE` and `SHOW PROFILES` statements display profiling information that indicates resource usage for statements executed during the course of the current session.

Note These statements are deprecated as of MySQL 5.6.7; expect them to be removed in a future MySQL release. Use the Performance Schema instead; see Section 22.18.1, “Query Profiling Using Performance Schema”.

To control profiling, use the `profiling` session variable, which has a default value of 0 (`OFF`). Enable profiling by setting `profiling` to 1 or `ON`:

```
mysql> SET profiling = 1;
```

`SHOW PROFILES` displays a list of the most recent statements sent to the server. The size of the list is controlled by the `profiling_history_size` session variable, which has a default value of 15. The maximum value is 100. Setting the value to 0 has the practical effect of disabling profiling.

All statements are profiled except `SHOW PROFILE` and `SHOW PROFILES`, so you find neither of those statements in the profile list. Malformed statements are profiled. For example, `SHOW PROFILING` is an illegal statement, and a syntax error occurs if you try to execute it, but it shows up in the profiling list.

SHOW Statements`SHOW PROFILE` displays detailed information about a single statement. Without the `FOR QUERY n` clause,the output pertains to the most recently executed statement. If `FOR QUERY n` is included, `SHOW PROFILE`displays information for statement n. The values of n correspond to the `Query_ID` values displayed by

```
SHOW PROFILES.
```

The `LIMIT row_count` clause may be given to limit the output to `row_count` rows. If `LIMIT` is given,`OFFSET offset` may be added to begin the output `offset` rows into the full set of rows.

By default, `SHOW PROFILE` displays `Status` and `Duration` columns. The `Status` values are like the`State` values displayed by `SHOW PROCESSLIST`, although there might be some minor differences in interpretion for the two statements for some status values (see Section 8.14, “Examining Server Thread(Process) Information”).

Optional `type` values may be specified to display specific additional types of information:

- `ALL` displays all information
- `BLOCK IO` displays counts for block input and output operations
- `CONTEXT SWITCHES` displays counts for voluntary and involuntary context switches
- `CPU` displays user and system CPU usage times
- `IPC` displays counts for messages sent and received
- `MEMORY` is not currently implemented
- `PAGE FAULTS` displays counts for major and minor page faults
- `SOURCE` displays the names of functions from the source code, together with the name and line number

of the file in which the function occurs

- `SWAPS` displays swap counts

Profiling is enabled per session. When a session ends, its profiling information is lost.

```
mysql> SELECT @@profiling;
+-------------+
| @@profiling |
+-------------+
|           0 |
+-------------+
1 row in set (0.00 sec)
mysql> SET profiling = 1;
Query OK, 0 rows affected (0.00 sec)
mysql> DROP TABLE IF EXISTS t1;
Query OK, 0 rows affected, 1 warning (0.00 sec)
mysql> CREATE TABLE T1 (id INT);
Query OK, 0 rows affected (0.01 sec)
mysql> SHOW PROFILES;
+----------+----------+--------------------------+
| Query_ID | Duration | Query                    |
+----------+----------+--------------------------+
|        0 | 0.000088 | SET PROFILING = 1        |
|        1 | 0.000136 | DROP TABLE IF EXISTS t1  |
|        2 | 0.011947 | CREATE TABLE t1 (id INT) |
+----------+----------+--------------------------+
3 rows in set (0.00 sec)
```

SHOW Statements

```
mysql> SHOW PROFILE;
+----------------------+----------+
| Status               | Duration |
+----------------------+----------+
| checking permissions | 0.000040 |
| creating table       | 0.000056 |
| After create         | 0.011363 |
| query end            | 0.000375 |
| freeing items        | 0.000089 |
| logging slow query   | 0.000019 |
| cleaning up          | 0.000005 |
+----------------------+----------+
7 rows in set (0.00 sec)
mysql> SHOW PROFILE FOR QUERY 1;
+--------------------+----------+
| Status             | Duration |
+--------------------+----------+
| query end          | 0.000107 |
| freeing items      | 0.000008 |
| logging slow query | 0.000015 |
| cleaning up        | 0.000006 |
+--------------------+----------+
4 rows in set (0.00 sec)
mysql> SHOW PROFILE CPU FOR QUERY 2;
+----------------------+----------+----------+------------+
| Status               | Duration | CPU_user | CPU_system |
+----------------------+----------+----------+------------+
| checking permissions | 0.000040 | 0.000038 |   0.000002 |
| creating table       | 0.000056 | 0.000028 |   0.000028 |
| After create         | 0.011363 | 0.000217 |   0.001571 |
| query end            | 0.000375 | 0.000013 |   0.000028 |
| freeing items        | 0.000089 | 0.000010 |   0.000014 |
| logging slow query   | 0.000019 | 0.000009 |   0.000010 |
| cleaning up          | 0.000005 | 0.000003 |   0.000002 |
+----------------------+----------+----------+------------+
7 rows in set (0.00 sec)
```

Note Profiling is only partially functional on some architectures. For values that depend on the `getrusage()` system call, `NULL` is returned on systems such as Windows that do not support the call. In addition, profiling is per process and not per thread.

This means that activity on threads within the server other than your own may affect the timing information that you see.

Profiling information is also available from the `INFORMATION_SCHEMA` `PROFILING` table. See Section 21.3.17, “The INFORMATION_SCHEMA PROFILING Table”. For example, the following queries are equivalent:

```
SHOW PROFILE FOR QUERY 2;
SELECT STATE, FORMAT(DURATION, 6) AS DURATION
FROM INFORMATION_SCHEMA.PROFILING
WHERE QUERY_ID = 2 ORDER BY SEQ;
```

#### 13.7.5.32 SHOW PROFILES Statement

```
SHOW PROFILES
```

The `SHOW PROFILES` statement, together with `SHOW PROFILE`, displays profiling information that indicates resource usage for statements executed during the course of the current session. For more information, see Section 13.7.5.31, “SHOW PROFILE Statement”.

SHOW Statements Note These statements are deprecated as of MySQL 5.6.7; expect them to be removed in a future MySQL release. Use the Performance Schema instead; see Chapter 22,MySQL Performance Schema.

#### 13.7.5.33 SHOW RELAYLOG EVENTS Statement

```
SHOW RELAYLOG EVENTS
[IN 'log_name']
[FROM pos]
[LIMIT [offset,] row_count]
```

Shows the events in the relay log of a replica. If you do not specify `'log_name'`, the first relay log is displayed. This statement has no effect on the source.

The `LIMIT` clause has the same syntax as for the `SELECT` statement. See Section 13.2.9, “SELECT Statement”.

Note Issuing a `SHOW RELAYLOG EVENTS` with no `LIMIT` clause could start a very time- and resource-consuming process because the server returns to the client the complete contents of the relay log (including all statements modifying data that have been received by the replica).

`SHOW RELAYLOG EVENTS` displays the following fields for each event in the relay log:

```
- Log_name
```

The name of the file that is being listed.

```
- Pos
```

The position at which the event occurs.

```
- Event_type
```

An identifier that describes the event type.

```
- Server_id
```

The server ID of the server on which the event originated.

```
- End_log_pos
```

The value of `End_log_pos` for this event in the source's binary log.

```
- Info
```

More detailed information about the event type. The format of this information depends on the event type.

Note Some events relating to the setting of user and system variables are not included in the output from `SHOW RELAYLOG EVENTS`. To get complete coverage of events within a relay log, use `mysqlbinlog`.

SHOW Statements

#### 13.7.5.34 SHOW SLAVE HOSTS Statement

```
SHOW SLAVE HOSTS
```

Displays a list of replicas currently registered with the source.

`SHOW SLAVE HOSTS` should be executed on a server that acts as a replication source. The statement displays information about servers that are or have been connected as replicas, with each row of the result corresponding to one replica server, as shown here:

```
mysql> SHOW SLAVE HOSTS;
+------------+-----------+------+-----------+--------------------------------------+
| Server_id  | Host      | Port | Master_id | Slave_UUID                           |
+------------+-----------+------+-----------+--------------------------------------+
|  192168010 | iconnect2 | 3306 | 192168011 | 14cb6624-7f93-11e0-b2c0-c80aa9429562 |
| 1921680101 | athena    | 3306 | 192168011 | 07af4990-f41f-11df-a566-7ac56fdaf645 |
+------------+-----------+------+-----------+--------------------------------------+
```

- `Server_id`: The unique server ID of the replica server, as configured in the replica server's option file,

or on the command line with `--server-id=value`.

- `Host`: The host name of the replica server as specified on the replica with the `--report-host` option.

This can differ from the machine name as configured in the operating system.

- `User`: The replica server user name as, specified on the replica with the `--report-user` option.

Statement output includes this column only if the source server is started with the `--show-slave-``auth-info` option.

- `Password`: The replica server password as, specified on the replica with the `--report-password`

option. Statement output includes this column only if the source server is started with the `--show-``slave-auth-info` option.

- `Port`: The port on the source to which the replica server is listening, as specified on the replica with the

`--report-port` option.

A zero in this column means that the replica port (`--report-port`) was not set.

- `Master_id`: The unique server ID of the source server that the replica server is replicating from. This is

the server ID of the server on which `SHOW SLAVE HOSTS` is executed, so this same value is listed for each row in the result.

- `Slave_UUID`: The globally unique ID of this replica, as generated on the replica and found in the

replica's `auto.cnf` file.

#### 13.7.5.35 SHOW SLAVE STATUS Statement

```
SHOW SLAVE STATUS
```

This statement provides status information on essential parameters of the replica threads. It requires either the `SUPER` or `REPLICATION CLIENT` privilege.

If you issue this statement using the `mysql` client, you can use a `\G` statement terminator rather than a semicolon to obtain a more readable vertical layout:

```
mysql> SHOW SLAVE STATUS\G
*************************** 1. row ***************************
Slave_IO_State: Waiting for master to send event
Master_Host: localhost
Master_User: root
Master_Port: 13000
Connect_Retry: 60
```

SHOW Statements

```
Master_Log_File: source-bin.000002
Read_Master_Log_Pos: 1307
Relay_Log_File: replica-relay-bin.000003
Relay_Log_Pos: 1508
Relay_Master_Log_File: source-bin.000002
Slave_IO_Running: Yes
Slave_SQL_Running: Yes
Replicate_Do_DB:
Replicate_Ignore_DB:
Replicate_Do_Table:
Replicate_Ignore_Table:
Replicate_Wild_Do_Table:
Replicate_Wild_Ignore_Table:
Last_Errno: 0
Last_Error:
Skip_Counter: 0
Exec_Master_Log_Pos: 1307
Relay_Log_Space: 1858
Until_Condition: None
Until_Log_File:
Until_Log_Pos: 0
Master_SSL_Allowed: No
Master_SSL_CA_File:
Master_SSL_CA_Path:
Master_SSL_Cert:
Master_SSL_Cipher:
Master_SSL_Key:
Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
Last_IO_Errno: 0
Last_IO_Error:
Last_SQL_Errno: 0
Last_SQL_Error:
Replicate_Ignore_Server_Ids:
Master_Server_Id: 1
Master_UUID: 3e11fa47-71ca-11e1-9e33-c80aa9429562
Master_Info_File: /var/mysqld.2/data/master.info
SQL_Delay: 0
SQL_Remaining_Delay: NULL
Slave_SQL_Running_State: Reading event from the relay log
Master_Retry_Count: 10
Master_Bind:
Last_IO_Error_Timestamp:
Last_SQL_Error_Timestamp:
Master_SSL_Crl:
Master_SSL_Crlpath:
Retrieved_Gtid_Set: 3e11fa47-71ca-11e1-9e33-c80aa9429562:1-5
Executed_Gtid_Set: 3e11fa47-71ca-11e1-9e33-c80aa9429562:1-5
Auto_Position: 1
```

The following list describes the fields returned by `SHOW SLAVE STATUS`. For additional information about interpreting their meanings, see Section 8.14.7, “Replication Replica I/O Thread States”.

```
- Slave_IO_State
```

A copy of the `State` field of the `SHOW PROCESSLIST` output for the replica I/O thread. This tells you what the thread is doing: trying to connect to the source, waiting for events from the source,reconnecting to the source, and so on. For a listing of possible states, see Section 8.14.7, “Replication Replica I/O Thread States”.

```
- Master_Host
```

The source host that the replica is connected to.

```
- Master_User
```

SHOW Statements The user name of the account used to connect to the source.

```
- Master_Port
```

The port used to connect to the source.

```
- Connect_Retry
```

The number of seconds between connect retries (default 60). This can be set with the `CHANGE MASTER``TO` statement.

```
- Master_Log_File
```

The name of the source binary log file from which the I/O thread is currently reading.

```
- Read_Master_Log_Pos
```

The position in the current source binary log file up to which the I/O thread has read.

```
- Relay_Log_File
```

The name of the relay log file from which the SQL thread is currently reading and executing.

```
- Relay_Log_Pos
```

The position in the current relay log file up to which the SQL thread has read and executed.

```
- Relay_Master_Log_File
```

The name of the source binary log file containing the most recent event executed by the SQL thread.

```
- Slave_IO_Running
```

Whether the I/O thread is started and has connected successfully to the source. Internally, the state of this thread is represented by one of the following three values:

- MYSQL_SLAVE_NOT_RUN. The replica I/O thread is not running. For this state,

```
Slave_IO_Running is No.
```

- MYSQL_SLAVE_RUN_NOT_CONNECT. The replica I/O thread is running, but is not connected to

a replication source. For this state, `Slave_IO_Running` is `Connecting`.

- MYSQL_SLAVE_RUN_CONNECT. The replica I/O thread is running, and is connected to a

replication source. For this state, `Slave_IO_Running` is `Yes`.

The value of the `Slave_running` system status variable corresponds with this value.

```
- Slave_SQL_Running
```

Whether the SQL thread is started.

```
- Replicate_Do_DB, Replicate_Ignore_DB
```

The lists of databases that were specified with the `--replicate-do-db` and `--replicate-ignore-``db` options, if any.

```
- Replicate_Do_Table, Replicate_Ignore_Table, Replicate_Wild_Do_Table,
Replicate_Wild_Ignore_Table
```

SHOW Statements The lists of tables that were specified with the `--replicate-do-table`, `--replicate-ignore-``table`, `--replicate-wild-do-table`, and `--replicate-wild-ignore-table` options, if any.

```
- Last_Errno, Last_Error
```

These columns are aliases for `Last_SQL_Errno` and `Last_SQL_Error`.

Issuing `RESET MASTER` or `RESET SLAVE` resets the values shown in these columns.

Note When the replica SQL thread receives an error, it reports the error first, then stops the SQL thread. This means that there is a small window of time during which `SHOW SLAVE STATUS` shows a nonzero value for `Last_SQL_Errno` even though `Slave_SQL_Running` still displays `Yes`.

```
- Skip_Counter
```

The current value of the `sql_slave_skip_counter` system variable. See Section 13.4.2.4, “SET GLOBAL sql_slave_skip_counter Statement”.

```
- Exec_Master_Log_Pos
```

The position in the current source binary log file to which the SQL thread has read and executed,marking the start of the next transaction or event to be processed. You can use this value with the `CHANGE MASTER TO` statement's `MASTER_LOG_POS` option when starting a new replica from an existing replica, so that the new replica reads from this point. The coordinates given by(`Relay_Master_Log_File`, `Exec_Master_Log_Pos`) in the source's binary log correspond to the coordinates given by (`Relay_Log_File`, `Relay_Log_Pos`) in the relay log.

When using a multithreaded replica (by setting `slave_parallel_workers` to a nonzero value), the value in this column actually represents a “low-water” mark, before which no uncommitted transactions remain. Because the current implementation allows execution of transactions on different databases in a different order on the replica than on the source, this is not necessarily the position of the most recently executed transaction.

```
- Relay_Log_Space
```

The total combined size of all existing relay log files.

```
- Until_Condition, Until_Log_File, Until_Log_Pos
```

The values specified in the `UNTIL` clause of the `START SLAVE` statement.

`Until_Condition` has these values:

- `None` if no `UNTIL` clause was specified
- `Master` if the replica is reading until a given position in the source's binary log
- `Relay` if the replica is reading until a given position in its relay log
- `SQL_BEFORE_GTIDS` if the replica SQL thread is processing transactions until it has reached the first

transaction whose GTID is listed in the `gtid_set`.

- `SQL_AFTER_GTIDS` if the replica threads are processing all transactions until the last transaction in

the `gtid_set` has been processed by both threads.

SHOW Statements

- `SQL_AFTER_MTS_GAPS` if a multithreaded replica's SQL threads are running until no more gaps are

found in the relay log.

`Until_Log_File` and `Until_Log_Pos` indicate the log file name and position that define the coordinates at which the SQL thread stops executing.

For more information on `UNTIL` clauses, see Section 13.4.2.5, “START SLAVE Statement”.

```
- Master_SSL_Allowed, Master_SSL_CA_File, Master_SSL_CA_Path, Master_SSL_Cert,
Master_SSL_Cipher, Master_SSL_CRL_File, Master_SSL_CRL_Path, Master_SSL_Key,
Master_SSL_Verify_Server_Cert
```

These fields show the SSL parameters used by the replica to connect to the source, if any.

`Master_SSL_Allowed` has these values:

- `Yes` if an SSL connection to the source is permitted
- `No` if an SSL connection to the source is not permitted
- `Ignored` if an SSL connection is permitted but the replica server does not have SSL support enabled

The values of the other SSL-related fields correspond to the values of the `MASTER_SSL_CA`,

```
MASTER_SSL_CAPATH, MASTER_SSL_CERT, MASTER_SSL_CIPHER, MASTER_SSL_CRL,
MASTER_SSL_CRLPATH, MASTER_SSL_KEY, and MASTER_SSL_VERIFY_SERVER_CERT options to the
```

`CHANGE MASTER TO` statement. See Section 13.4.2.1, “CHANGE MASTER TO Statement”.

```
- Seconds_Behind_Master
```

This field is an indication of how “late” the replica is:

- When the replica is actively processing updates, this field shows the difference between the current

timestamp on the replica and the original timestamp logged on the source for the event currently being processed on the replica.

- When no event is currently being processed on the replica, this value is 0.

In essence, this field measures the time difference in seconds between the replica SQL thread and the replica I/O thread. If the network connection between source and replica is fast, the replica I/O thread is very close to the source, so this field is a good approximation of how late the replica SQL thread is compared to the source. If the network is slow, this is not a good approximation; the replica SQL thread may quite often be caught up with the slow-reading replica I/O thread, so `Seconds_Behind_Master`often shows a value of 0, even if the I/O thread is late compared to the source. In other words, this column is useful only for fast networks.

This time difference computation works even if the source and replica do not have identical clock times, provided that the difference, computed when the replica I/O thread starts, remains constant from then on. Any changes—including NTP updates—can lead to clock skews that can make calculation of`Seconds_Behind_Master` less reliable.

In MySQL 5.6.9 and later, this field is `NULL` (undefined or unknown) if the replica SQL thread is not running, or if the SQL thread has consumed all of the relay log and the replica I/O thread is not running.

Previously, this field was `NULL` if the replica SQL thread or the replica I/O thread was not running or was not connected to the source. (Bug #12946333) For example, if (prior to MySQL 5.6.9) the replica I/O thread was running but was not connected to the source and was sleeping for the number of seconds given by the `CHANGE MASTER TO` statement or `--master-connect-retry` option (default 60) before SHOW Statements reconnecting, the value was `NULL`. Now in such cases, the connection to the source is not tested;

instead, if the I/O thread is running but the relay log is exhausted, `Seconds_Behind_Master` is set to

0.

The value of `Seconds_Behind_Master` is based on the timestamps stored in events, which are preserved through replication. This means that if a source M1 is itself a replica of M0, any event from M1's binary log that originates from M0's binary log has M0's timestamp for that event. This enables MySQL to replicate `TIMESTAMP` successfully. However, the problem for `Seconds_Behind_Master`is that if M1 also receives direct updates from clients, the `Seconds_Behind_Master` value randomly fluctuates because sometimes the last event from M1 originates from M0 and sometimes is the result of a direct update on M1.

When using a multithreaded replica, you should keep in mind that this value is based on`Exec_Master_Log_Pos`, and so may not reflect the position of the most recently committed transaction.

```
- Last_IO_Errno, Last_IO_Error
```

The error number and error message of the most recent error that caused the I/O thread to stop. An error number of 0 and message of the empty string mean “no error.” If the `Last_IO_Error` value is not empty, the error values also appear in the replica's error log.

I/O error information includes a timestamp showing when the most recent I/O thread error occurred. This timestamp uses the format `YYMMDD hh:mm:ss`, and appears in the `Last_IO_Error_Timestamp`column.

Issuing `RESET MASTER` or `RESET SLAVE` resets the values shown in these columns.

```
- Last_SQL_Errno, Last_SQL_Error
```

The error number and error message of the most recent error that caused the SQL thread to stop. An error number of 0 and message of the empty string mean “no error.” If the `Last_SQL_Error` value is not empty, the error values also appear in the replica's error log.

SQL error information includes a timestamp showing when the most recent SQL thread error occurred. This timestamp uses the format `YYMMDD hh:mm:ss`, and appears in the

```
Last_SQL_Error_Timestamp column.
```

Issuing `RESET MASTER` or `RESET SLAVE` resets the values shown in these columns.

```
- Replicate_Ignore_Server_Ids
```

In MySQL 5.6, you set a replica to ignore events from 0 or more sources using the`IGNORE_SERVER_IDS` option of the `CHANGE MASTER TO` statement. By default this is blank, and is usually modified only when using a circular or other multi-source replication setup. The message shown for `Replicate_Ignore_Server_Ids` when not blank consists of a comma-delimited list of one or more numbers, indicating the server IDs to be ignored. For example:

```
Replicate_Ignore_Server_Ids: 2, 6, 9
```

Note`Ignored_server_ids` also shows the server IDs to be ignored, but is a space-delimited list, which is preceded by the total number of server IDs to be ignored. For example, if a `CHANGE MASTER TO` statement containing the`IGNORE_SERVER_IDS = (2,6,9)` option has been issued to tell a replica to ignore sources having the server ID 2, 6, or 9, that information appears as:SHOW Statements

```
Ignored_server_ids: 3 2 6 9
```

where 3 is the total number of server IDs being ignored.

`Replicate_Ignore_Server_Ids` filtering is performed by the I/O thread, rather than by the SQL thread, which means that events which are filtered out are not written to the relay log. This differs from the filtering actions taken by server options such `--replicate-do-table`, which apply to the SQL thread.

```
- Master_Server_Id
```

The `server_id` value from the source.

```
- Master_UUID
```

The `server_uuid` value from the source.

```
- Master_Info_File
```

The location of the `master.info` file.

```
- SQL_Delay
```

The number of seconds that the replica must lag the source.

```
- SQL_Remaining_Delay
When Slave_SQL_Running_State is Waiting until MASTER_DELAY seconds after master
```

`executed event`, this field contains the number of delay seconds remaining. At other times, this field is

```
NULL.
- Slave_SQL_Running_State
```

The state of the SQL thread (analogous to `Slave_IO_State`). The value is identical to the `State`value of the SQL thread as displayed by `SHOW PROCESSLIST`; Section 8.14.8, “Replication Replica SQL Thread States”, provides a listing of possible states.

```
- Master_Retry_Count
```

The number of times the replica can attempt to reconnect to the source in the event of a lost connection.

This value can be set using the `MASTER_RETRY_COUNT` option of the `CHANGE MASTER TO` statement(preferred) or the older `--master-retry-count` server option (still supported for backward compatibility).

```
- Master_Bind
```

The network interface that the replica is bound to, if any. This is set using the `MASTER_BIND` option for the `CHANGE MASTER TO` statement.

```
- Last_IO_Error_Timestamp
```

A timestamp in `YYMMDD hh:mm:ss` format that shows when the most recent I/O error took place.

```
- Last_SQL_Error_Timestamp
```

A timestamp in `YYMMDD hh:mm:ss` format that shows when the most recent SQL error occurred.

```
- Retrieved_Gtid_Set
```

SHOW Statements The set of global transaction IDs corresponding to all transactions received by this replica. Empty if GTIDs are not in use.

This is the set of all GTIDs that exist or have existed in the relay logs. Each GTID is added as soon as the `Gtid_log_event` is received. This can cause partially transmitted transactions to have their GTIDs included in the set.

When all relay logs are lost due to executing `RESET SLAVE` or `CHANGE MASTER TO`, or due to the effects of the `--relay-log-recovery` option, the set is cleared. When `relay_log_purge = 1`, the newest relay log is always kept, and the set is not cleared.

```
- Executed_Gtid_Set
```

The set of global transaction IDs written in the binary log. This is the same as the value for the global`gtid_executed` system variable on this server, as well as the value for `Executed_Gtid_Set` in the output of `SHOW MASTER STATUS` on this server. Empty if GTIDs are not in use. See GTID Sets for more information.

```
- Auto_Position
```

1 if autopositioning is in use; otherwise 0.

#### 13.7.5.36 SHOW STATUS Statement

```
SHOW [GLOBAL | SESSION] STATUS
[LIKE 'pattern' | WHERE expr]
```

`SHOW STATUS` provides server status information (see Section 5.1.9, “Server Status Variables”). This statement does not require any privilege. It requires only the ability to connect to the server.

Status variable information is also available from these sources:

- The `GLOBAL_STATUS` and `SESSION_STATUS` tables. See Section 21.3.9, “The

INFORMATION_SCHEMA GLOBAL_STATUS and SESSION_STATUS Tables”.

- The `mysqladmin extended-status` command. See Section 4.5.2, “mysqladmin — A MySQL Server

Administration Program”.

For `SHOW STATUS`, a `LIKE` clause, if present, indicates which variable names to match. A `WHERE` clause can be given to select rows using more general conditions, as discussed in Section 21.9, “Extensions to SHOW Statements”.

`SHOW STATUS` accepts an optional `GLOBAL` or `SESSION` variable scope modifier:

- With a `GLOBAL` modifier, the statement displays the global status values. A global status variable

may represent status for some aspect of the server itself (for example, `Aborted_connects`), or the aggregated status over all connections to MySQL (for example, `Bytes_received` and `Bytes_sent`). If a variable has no global value, the session value is displayed.

- With a `SESSION` modifier, the statement displays the status variable values for the current connection. If

a variable has no session value, the global value is displayed. `LOCAL` is a synonym for `SESSION`.

- If no modifier is present, the default is `SESSION`.

The scope for each status variable is listed at Section 5.1.9, “Server Status Variables”.

SHOW Statements Each invocation of the `SHOW STATUS` statement uses an internal temporary table and increments the global `Created_tmp_tables` value.

Partial output is shown here. The list of names and values may differ for your server. The meaning of each variable is given in Section 5.1.9, “Server Status Variables”.

```
mysql> SHOW STATUS;
+--------------------------+------------+
| Variable_name            | Value      |
+--------------------------+------------+
| Aborted_clients          | 0          |
| Aborted_connects         | 0          |
| Bytes_received           | 155372598  |
| Bytes_sent               | 1176560426 |
| Connections              | 30023      |
| Created_tmp_disk_tables  | 0          |
| Created_tmp_tables       | 8340       |
| Created_tmp_files        | 60         |
...
| Open_tables              | 1          |
| Open_files               | 2          |
| Open_streams             | 0          |
| Opened_tables            | 44600      |
| Questions                | 2026873    |
...
| Table_locks_immediate    | 1920382    |
| Table_locks_waited       | 0          |
| Threads_cached           | 0          |
| Threads_created          | 30022      |
| Threads_connected        | 1          |
| Threads_running          | 1          |
| Uptime                   | 80380      |
+--------------------------+------------+
```

With a `LIKE` clause, the statement displays only rows for those variables with names that match the pattern:

```
mysql> SHOW STATUS LIKE 'Key%';
+--------------------+----------+
| Variable_name      | Value    |
+--------------------+----------+
| Key_blocks_used    | 14955    |
| Key_read_requests  | 96854827 |
| Key_reads          | 162040   |
| Key_write_requests | 7589728  |
| Key_writes         | 3813196  |
+--------------------+----------+
```

#### 13.7.5.37 SHOW TABLE STATUS Statement

```
SHOW TABLE STATUS
[{FROM | IN} db_name]
[LIKE 'pattern' | WHERE expr]
```

`SHOW TABLE STATUS` works likes `SHOW TABLES`, but provides a lot of information about each non-`TEMPORARY` table. You can also get this list using the `mysqlshow --status db_name` command.

The `LIKE` clause, if present, indicates which table names to match. The `WHERE` clause can be given to select rows using more general conditions, as discussed in Section 21.9, “Extensions to SHOW Statements”.

This statement also displays information about views.

`SHOW TABLE STATUS` output has these columns:

```
- Name
```

SHOW Statements The name of the table.

```
- Engine
```

The storage engine for the table. See Chapter 14, The InnoDB Storage Engine, and Chapter 15,Alternative Storage Engines.

For partitioned tables, `Engine` shows the name of the storage engine used by all partitions.

```
- Version
```

The version number of the table's `.frm` file.

```
- Row_format
```

The row-storage format (`Fixed`, `Dynamic`, `Compressed`, `Redundant`, `Compact`). For `MyISAM` tables,`Dynamic` corresponds to what `myisamchk -dvv` reports as `Packed`. `InnoDB` table format is either`Redundant` or `Compact` when using the `Antelope` file format, or `Compressed` or `Dynamic` when using the `Barracuda` file format.

```
- Rows
```

The number of rows. Some storage engines, such as `MyISAM`, store the exact count. For other storage engines, such as `InnoDB`, this value is an approximation, and may vary from the actual value by as much as 40% to 50%. In such cases, use `SELECT COUNT(*)` to obtain an accurate count.

The `Rows` value is `NULL` for `INFORMATION_SCHEMA` tables.

For `InnoDB` tables, the row count is only a rough estimate used in SQL optimization. (This is also true if the `InnoDB` table is partitioned.)

```
- Avg_row_length
```

The average row length.

Refer to the notes at the end of this section for related information.

```
- Data_length
```

For `MyISAM`, `Data_length` is the length of the data file, in bytes.

For `InnoDB`, `Data_length` is the approximate amount of space allocated for the clustered index, in bytes. Specifically, it is the clustered index size, in pages, multiplied by the `InnoDB` page size.

Refer to the notes at the end of this section for information regarding other storage engines.

```
- Max_data_length
```

For `MyISAM`, `Max_data_length` is maximum length of the data file. This is the total number of bytes of data that can be stored in the table, given the data pointer size used.

Unused for `InnoDB`.

Refer to the notes at the end of this section for information regarding other storage engines.

```
- Index_length
```

For `MyISAM`, `Index_length` is the length of the index file, in bytes.

SHOW Statements For `InnoDB`, `Index_length` is the approximate amount of space allocated for non-clustered indexes,in bytes. Specifically, it is the sum of non-clustered index sizes, in pages, multiplied by the `InnoDB` page size.

Refer to the notes at the end of this section for information regarding other storage engines.

```
- Data_free
```

The number of allocated but unused bytes.

`InnoDB` tables report the free space of the tablespace to which the table belongs. For a table located in the shared tablespace, this is the free space of the shared tablespace. If you are using multiple tablespaces and the table has its own tablespace, the free space is for only that table. Free space means the number of bytes in completely free extents minus a safety margin. Even if free space displays as 0, it may be possible to insert rows as long as new extents need not be allocated.

For NDB Cluster, `Data_free` shows the space allocated on disk for, but not used by, a Disk Data table or fragment on disk. (In-memory data resource usage is reported by the `Data_length` column.)For partitioned tables, this value is only an estimate and may not be absolutely correct. A more accurate method of obtaining this information in such cases is to query the `INFORMATION_SCHEMA` `PARTITIONS`table, as shown in this example:

```
SELECT SUM(DATA_FREE)
FROM  INFORMATION_SCHEMA.PARTITIONS
WHERE TABLE_SCHEMA = 'mydb'
AND   TABLE_NAME   = 'mytable';
```

For more information, see Section 21.3.14, “The INFORMATION_SCHEMA PARTITIONS Table”.

```
- Auto_increment
```

The next `AUTO_INCREMENT` value.

```
- Create_time
```

When the table was created.

Prior to MySQL 5.6.25, for partitioned `InnoDB` tables, the `Create_time` column shows `NULL`.

This column shows the correct table creation time for such tables in MySQL 5.6.25 and later. (Bug#17299181, Bug #69990)

```
- Update_time
```

When the data file was last updated. For some storage engines, this value is `NULL`. For example,`InnoDB` stores multiple tables in its system tablespace and the data file timestamp does not apply. Even with file-per-table mode with each `InnoDB` table in a separate `.ibd` file, change buffering can delay the write to the data file, so the file modification time is different from the time of the last insert, update, or delete. For `MyISAM`, the data file timestamp is used; however, on Windows the timestamp is not updated by updates, so the value is inaccurate.

For partitioned `InnoDB` tables, `Update_time` is always `NULL`.

```
- Check_time
```

When the table was last checked. Not all storage engines update this time, in which case, the value is always `NULL`.

SHOW Statements For partitioned `InnoDB` tables, `Check_time` is always `NULL`.

```
- Collation
```

The table default collation. The output does not explicitly list the table default character set, but the collation name begins with the character set name.

```
- Checksum
```

The live checksum value, if any.

```
- Create_options
```

Extra options used with `CREATE TABLE`.

`Create_options` shows `partitioned` for partitioned tables.

When creating a table with strict mode disabled, the storage engine's default row format is used if the specified row format is not supported. The actual row format of the table is reported in the `Row_format`column. `Create_options` shows the row format that was specified in the `CREATE TABLE` statement.

When altering the storage engine of a table, table options that are not applicable to the new storage engine are retained in the table definition to enable reverting the table with its previously defined options to the original storage engine, if necessary. `Create_options` may show retained options.

```
- Comment
```

The comment used when creating the table (or information as to why MySQL could not access the table information).

> Notes

- For `InnoDB` tables, `SHOW TABLE STATUS` does not give accurate statistics except for the physical size

reserved by the table. The row count is only a rough estimate used in SQL optimization.

- For `NDB` tables, the output of this statement shows appropriate values for the `Avg_row_length` and

`Data_length` columns, with the exception that `BLOB` columns are not taken into account.

- For `NDB` tables, `Data_length` includes data stored in main memory only; the `Max_data_length` and

`Data_free` columns apply to Disk Data.

- For NDB Cluster Disk Data tables, `Max_data_length` shows the space allocated for the disk part of a

Disk Data table or fragment. (In-memory data resource usage is reported by the `Data_length` column.)

- For `MEMORY` tables, the `Data_length`, `Max_data_length`, and `Index_length` values approximate

the actual amount of allocated memory. The allocation algorithm reserves memory in large amounts to reduce the number of allocation operations.

- For views, all columns displayed by `SHOW TABLE STATUS` are `NULL` except that `Name` indicates the

view name and `Comment` says `VIEW`.

Table information is also available from the `INFORMATION_SCHEMA` `TABLES` table. See Section 21.3.23,“The INFORMATION_SCHEMA TABLES Table”.

#### 13.7.5.38 SHOW TABLES Statement

```
SHOW [FULL] TABLES
[{FROM | IN} db_name]
```

SHOW Statements

```
[LIKE 'pattern' | WHERE expr]
```

`SHOW TABLES` lists the non-`TEMPORARY` tables in a given database. You can also get this list using the`mysqlshow db_name` command. The `LIKE` clause, if present, indicates which table names to match. The`WHERE` clause can be given to select rows using more general conditions, as discussed in Section 21.9,“Extensions to SHOW Statements”.

Matching performed by the `LIKE` clause is dependent on the setting of the `lower_case_table_names`system variable.

This statement also lists any views in the database. The optional `FULL` modifier causes `SHOW TABLES` to display a second output column with values of `BASE TABLE` for a table, `VIEW` for a view, or `SYSTEM VIEW`for an `INFORMATION_SCHEMA` table.

If you have no privileges for a base table or view, it does not show up in the output from `SHOW TABLES` or

```
mysqlshow db_name.
```

Table information is also available from the `INFORMATION_SCHEMA` `TABLES` table. See Section 21.3.23,“The INFORMATION_SCHEMA TABLES Table”.

#### 13.7.5.39 SHOW TRIGGERS Statement

```
SHOW TRIGGERS
[{FROM | IN} db_name]
[LIKE 'pattern' | WHERE expr]
```

`SHOW TRIGGERS` lists the triggers currently defined for tables in a database (the default database unless a`FROM` clause is given). This statement returns results only for databases and tables for which you have the`TRIGGER` privilege. The `LIKE` clause, if present, indicates which table names (not trigger names) to match and causes the statement to display triggers for those tables. The `WHERE` clause can be given to select rows using more general conditions, as discussed in Section 21.9, “Extensions to SHOW Statements”.

For the `ins_sum` trigger defined in Section 20.3, “Using Triggers”, the output of `SHOW TRIGGERS` is as shown here:

```
mysql> SHOW TRIGGERS LIKE 'acc%'\G
*************************** 1. row ***************************
Trigger: ins_sum
Event: INSERT
Table: account
Statement: SET @sum = @sum + NEW.amount
Timing: BEFORE
Created: NULL
sql_mode: NO_ENGINE_SUBSTITUTION
Definer: me@localhost
character_set_client: utf8
collation_connection: utf8_general_ci
Database Collation: latin1_swedish_ci
```

`SHOW TRIGGERS` output has these columns:

```
- Trigger
```

The name of the trigger.

```
- Event
```

The trigger event. This is the type of operation on the associated table for which the trigger activates.

The value is `INSERT` (a row was inserted), `DELETE` (a row was deleted), or `UPDATE` (a row was modified).

SHOW Statements

```
- Table
```

The table for which the trigger is defined.

```
- Statement
```

The trigger body; that is, the statement executed when the trigger activates.

```
- Timing
```

Whether the trigger activates before or after the triggering event. The value is `BEFORE` or `AFTER`.

```
- Created
```

The value of this column is always `NULL`.

```
- sql_mode
```

The SQL mode in effect when the trigger was created, and under which the trigger executes. For the permitted values, see Section 5.1.10, “Server SQL Modes”.

```
- Definer
```

The account of the user who created the trigger, in `'user_name'@'host_name'` format.

```
- character_set_client
```

The session value of the `character_set_client` system variable when the trigger was created.

```
- collation_connection
```

The session value of the `collation_connection` system variable when the trigger was created.

```
- Database Collation
```

The collation of the database with which the trigger is associated.

Trigger information is also available from the `INFORMATION_SCHEMA` `TRIGGERS` table. See Section 21.3.27, “The INFORMATION_SCHEMA TRIGGERS Table”.

#### 13.7.5.40 SHOW VARIABLES Statement

```
SHOW [GLOBAL | SESSION] VARIABLES
[LIKE 'pattern' | WHERE expr]
```

`SHOW VARIABLES` shows the values of MySQL system variables (see Section 5.1.7, “Server System Variables”). This statement does not require any privilege. It requires only the ability to connect to the server.

System variable information is also available from these sources:

- The `GLOBAL_VARIABLES` and `SESSION_VARIABLES` tables. See Section 21.3.10, “The

INFORMATION_SCHEMA GLOBAL_VARIABLES and SESSION_VARIABLES Tables”.

- The `mysqladmin variables` command. See Section 4.5.2, “mysqladmin — A MySQL Server

Administration Program”.

For `SHOW VARIABLES`, a `LIKE` clause, if present, indicates which variable names to match. A `WHERE`clause can be given to select rows using more general conditions, as discussed in Section 21.9,“Extensions to SHOW Statements”.

SHOW Statements`SHOW VARIABLES` accepts an optional `GLOBAL` or `SESSION` variable scope modifier:

- With a `GLOBAL` modifier, the statement displays global system variable values. These are the values

used to initialize the corresponding session variables for new connections to MySQL. If a variable has no global value, no value is displayed.

- With a `SESSION` modifier, the statement displays the system variable values that are in effect for the

current connection. If a variable has no session value, the global value is displayed. `LOCAL` is a synonym for `SESSION`.

- If no modifier is present, the default is `SESSION`.

The scope for each system variable is listed at Section 5.1.7, “Server System Variables”.

`SHOW VARIABLES` is subject to a version-dependent display-width limit. For variables with very long values that are not completely displayed, use `SELECT` as a workaround. For example:

```
SELECT @@GLOBAL.innodb_data_file_path;
```

Most system variables can be set at server startup (read-only variables such as `version_comment` are exceptions). Many can be changed at runtime with the `SET` statement. See Section 5.1.8, “Using System Variables”, and Section 13.7.4.1, “SET Syntax for Variable Assignment”.

Partial output is shown here. The list of names and values may differ for your server. Section 5.1.7, “Server System Variables”, describes the meaning of each variable, and Section 5.1.1, “Configuring the Server”,provides information about tuning them.

```
mysql> SHOW VARIABLES;
+-----------------------------------------+---------------------------+
| Variable_name                           | Value                     |
+-----------------------------------------+---------------------------+
| auto_increment_increment                | 1                         |
| auto_increment_offset                   | 1                         |
| autocommit                              | ON                        |
| automatic_sp_privileges                 | ON                        |
| back_log                                | 50                        |
| basedir                                 | /home/jon/bin/mysql-5.5   |
| big_tables                              | OFF                       |
| binlog_cache_size                       | 32768                     |
| binlog_direct_non_transactional_updates | OFF                       |
| binlog_format                           | STATEMENT                 |
| binlog_stmt_cache_size                  | 32768                     |
| bulk_insert_buffer_size                 | 8388608                   |
...
| max_allowed_packet                      | 4194304                   |
| max_binlog_cache_size                   | 18446744073709547520      |
| max_binlog_size                         | 1073741824                |
| max_binlog_stmt_cache_size              | 18446744073709547520      |
| max_connect_errors                      | 100                       |
| max_connections                         | 151                       |
| max_delayed_threads                     | 20                        |
| max_error_count                         | 64                        |
| max_heap_table_size                     | 16777216                  |
| max_insert_delayed_threads              | 20                        |
| max_join_size                           | 18446744073709551615      |
...
| thread_handling                         | one-thread-per-connection |
| thread_stack                            | 262144                    |
| time_format                             | %H:%i:%s                  |
| time_zone                               | SYSTEM                    |
| timed_mutexes                           | OFF                       |
| timestamp                               | 1316689732                |
```

SHOW Statements

```
| tmp_table_size                          | 16777216                  |
| tmpdir                                  | /tmp                      |
| transaction_alloc_block_size            | 8192                      |
| transaction_prealloc_size               | 4096                      |
| tx_isolation                            | REPEATABLE-READ           |
| unique_checks                           | ON                        |
| updatable_views_with_limit              | YES                       |
| version                                 | 5.5.17-log                |
| version_comment                         | Source distribution       |
| version_compile_machine                 | x86_64                    |
| version_compile_os                      | Linux                     |
| wait_timeout                            | 28800                     |
| warning_count                           | 0                         |
+-----------------------------------------+---------------------------+
```

With a `LIKE` clause, the statement displays only rows for those variables with names that match the pattern. To obtain the row for a specific variable, use a `LIKE` clause as shown:

```
SHOW VARIABLES LIKE 'max_join_size';
SHOW SESSION VARIABLES LIKE 'max_join_size';
```

To get a list of variables whose name match a pattern, use the % wildcard character in a `LIKE` clause:

```
SHOW VARIABLES LIKE '%size%';
SHOW GLOBAL VARIABLES LIKE '%size%';
```

Wildcard characters can be used in any position within the pattern to be matched. Strictly speaking,because _ is a wildcard that matches any single character, you should escape it as `\_` to match it literally.

In practice, this is rarely necessary.

#### 13.7.5.41 SHOW WARNINGS Statement

```
SHOW WARNINGS [LIMIT [offset,] row_count]
SHOW COUNT(*) WARNINGS
```

`SHOW WARNINGS` is a diagnostic statement that displays information about the conditions (errors,warnings, and notes) resulting from executing a statement in the current session. Warnings are generated for DML statements such as `INSERT`, `UPDATE`, and `LOAD DATA` as well as DDL statements such as

```
CREATE TABLE and ALTER TABLE.
```

The `LIMIT` clause has the same syntax as for the `SELECT` statement. See Section 13.2.9, “SELECT Statement”.

`SHOW WARNINGS` is also used following `EXPLAIN EXTENDED`, to display the extra information generated by `EXPLAIN` when the `EXTENDED` keyword is used. See Section 8.8.3, “Extended EXPLAIN Output Format”.

`SHOW WARNINGS` displays information about the conditions resulting from the most recent statement in the current session that generated messages. It shows nothing if the most recent statement used a table and generated no messages. (That is, statements that use a table but generate no messages clear the message list.) Statements that do not use tables and do not generate messages have no effect on the message list.

The `SHOW COUNT(*) WARNINGS` diagnostic statement displays the total number of errors, warnings, and notes. You can also retrieve this number from the `warning_count` system variable:

```
SHOW COUNT(*) WARNINGS;
SELECT @@warning_count;
```

A related diagnostic statement, `SHOW ERRORS`, shows only error conditions (it excludes warnings and notes), and `SHOW COUNT(*) ERRORS` statement displays the total number of errors. See SHOW Statements Section 13.7.5.18, “SHOW ERRORS Statement”. `GET DIAGNOSTICS` can be used to examine information for individual conditions. See Section 13.6.7.3, “GET DIAGNOSTICS Statement”.

Here is a simple example that shows data-conversion warnings for `INSERT`. The example assumes that strict SQL mode is disabled. With strict mode enabled, the warnings would become errors and terminate the `INSERT`.

```
mysql> CREATE TABLE t1 (a TINYINT NOT NULL, b CHAR(4));
Query OK, 0 rows affected (0.05 sec)
mysql> INSERT INTO t1 VALUES(10,'mysql'), (NULL,'test'), (300,'xyz');
Query OK, 3 rows affected, 3 warnings (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 3
mysql> SHOW WARNINGS\G
*************************** 1. row ***************************
Level: Warning
Code: 1265
Message: Data truncated for column 'b' at row 1
*************************** 2. row ***************************
Level: Warning
Code: 1048
Message: Column 'a' cannot be null
*************************** 3. row ***************************
Level: Warning
Code: 1264
Message: Out of range value for column 'a' at row 3
3 rows in set (0.00 sec)
```

The `max_error_count` system variable controls the maximum number of error, warning, and note messages for which the server stores information, and thus the number of messages that `SHOW``WARNINGS` displays. To change the number of messages the server can store, change the value of`max_error_count`. The default is 64.

`max_error_count` controls only how many messages are stored, not how many are counted. The value of `warning_count` is not limited by `max_error_count`, even if the number of messages generated exceeds `max_error_count`. The following example demonstrates this. The `ALTER TABLE`statement produces three warning messages (strict SQL mode is disabled for the example to prevent an error from occuring after a single conversion issue). Only one message is stored and displayed because `max_error_count` has been set to 1, but all three are counted (as shown by the value of

```
warning_count):
mysql> SHOW VARIABLES LIKE 'max_error_count';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_error_count | 64    |
+-----------------+-------+
1 row in set (0.00 sec)
mysql> SET max_error_count=1, sql_mode = '';
Query OK, 0 rows affected (0.00 sec)
mysql> ALTER TABLE t1 MODIFY b CHAR;
Query OK, 3 rows affected, 3 warnings (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 3
mysql> SHOW WARNINGS;
+---------+------+----------------------------------------+
| Level   | Code | Message                                |
+---------+------+----------------------------------------+
| Warning | 1263 | Data truncated for column 'b' at row 1 |
+---------+------+----------------------------------------+
1 row in set (0.00 sec)
```

Other Administrative Statements

```
mysql> SELECT @@warning_count;
+-----------------+
| @@warning_count |
+-----------------+
|               3 |
+-----------------+
1 row in set (0.01 sec)
```

To disable message storage, set `max_error_count` to 0. In this case, `warning_count` still indicates how many warnings occurred, but messages are not stored and cannot be displayed.

The `sql_notes` system variable controls whether note messages increment `warning_count` and whether the server stores them. By default, `sql_notes` is 1, but if set to 0, notes do not increment`warning_count` and the server does not store them:

```
mysql> SET sql_notes = 1;
mysql> DROP TABLE IF EXISTS test.no_such_table;
Query OK, 0 rows affected, 1 warning (0.00 sec)
mysql> SHOW WARNINGS;
+-------+------+------------------------------------+
| Level | Code | Message                            |
+-------+------+------------------------------------+
| Note  | 1051 | Unknown table 'test.no_such_table' |
+-------+------+------------------------------------+
1 row in set (0.00 sec)
mysql> SET sql_notes = 0;
mysql> DROP TABLE IF EXISTS test.no_such_table;
Query OK, 0 rows affected (0.00 sec)
mysql> SHOW WARNINGS;
Empty set (0.00 sec)
```

The MySQL server sends to each client a count indicating the total number of errors, warnings, and notes resulting from the most recent statement executed by that client. From the C API, this value can be obtained by calling `mysql_warning_count()`. See mysql_warning_count().

In the `mysql` client, you can enable and disable automatic warnings display using the `warnings` and`nowarning` commands, respectively, or their shortcuts, `\W` and `\w` (see Section 4.5.1.2, “mysql Client Commands”). For example:

```
mysql> \W
Show warnings enabled.
mysql> SELECT 1/0;
+------+
| 1/0  |
+------+
| NULL |
+------+
1 row in set, 1 warning (0.03 sec)
Warning (Code 1365): Division by 0
mysql> \w
Show warnings disabled.
```

### 13.7.6 Other Administrative Statements

#### 13.7.6.1 BINLOG Statement

```
BINLOG 'str'
```

`BINLOG` is an internal-use statement. It is generated by the `mysqlbinlog` program as the printable representation of certain events in binary log files. (See Section 4.6.8, “mysqlbinlog — Utility for Processing Other Administrative Statements Binary Log Files”.) The `'str'` value is a base 64-encoded string the that server decodes to determine the data change indicated by the corresponding event. This statement requires the `SUPER` privilege.

This statement can execute only format description events and row events.

#### 13.7.6.2 CACHE INDEX Statement

```
CACHE INDEX {
tbl_index_list [, tbl_index_list] ...
| tbl_name PARTITION (partition_list)
}
IN key_cache_name
tbl_index_list:
tbl_name [{INDEX|KEY} (index_name[, index_name] ...)]
partition_list: {
partition_name[, partition_name] ...
| ALL
}
```

The `CACHE INDEX` statement assigns table indexes to a specific key cache. It applies only to `MyISAM`tables, including partitioned `MyISAM` tables. After the indexes have been assigned, they can be preloaded into the cache if desired with `LOAD INDEX INTO CACHE`.

The following statement assigns indexes from the tables `t1`, `t2`, and `t3` to the key cache named

```
hot_cache:
mysql> CACHE INDEX t1, t2, t3 IN hot_cache;
+---------+--------------------+----------+----------+
| Table   | Op                 | Msg_type | Msg_text |
+---------+--------------------+----------+----------+
| test.t1 | assign_to_keycache | status   | OK       |
| test.t2 | assign_to_keycache | status   | OK       |
| test.t3 | assign_to_keycache | status   | OK       |
+---------+--------------------+----------+----------+
```

The syntax of `CACHE INDEX` enables you to specify that only particular indexes from a table should be assigned to the cache. However, the implementation assigns all the table's indexes to the cache, so there is no reason to specify anything other than the table name.

The key cache referred to in a `CACHE INDEX` statement can be created by setting its size with a parameter setting statement or in the server parameter settings. For example:

```
SET GLOBAL keycache1.key_buffer_size=128*1024;
```

Key cache parameters are accessed as members of a structured system variable. See Section 5.1.8.3,“Structured System Variables”.

A key cache must exist before you assign indexes to it, or an error occurs:

```
mysql> CACHE INDEX t1 IN non_existent_cache;
ERROR 1284 (HY000): Unknown key cache 'non_existent_cache'
```

By default, table indexes are assigned to the main (default) key cache created at the server startup. When a key cache is destroyed, all indexes assigned to it are reassigned to the default key cache.

Index assignment affects the server globally: If one client assigns an index to a given cache, this cache is used for all queries involving the index, no matter which client issues the queries.

`CACHE INDEX` is supported for partitioned `MyISAM` tables. You can assign one or more indexes for one,several, or all partitions to a given key cache. For example, you can do the following:Other Administrative Statements

```
CREATE TABLE pt (c1 INT, c2 VARCHAR(50), INDEX i(c1))
ENGINE=MyISAM
PARTITION BY HASH(c1)
PARTITIONS 4;
SET GLOBAL kc_fast.key_buffer_size = 128 * 1024;
SET GLOBAL kc_slow.key_buffer_size = 128 * 1024;
CACHE INDEX pt PARTITION (p0) IN kc_fast;
CACHE INDEX pt PARTITION (p1, p3) IN kc_slow;
```

The previous set of statements performs the following actions:

- Creates a partitioned table with 4 partitions; these partitions are automatically named `p0`, ..., `p3`; this

table has an index named i on column `c1`.

- Creates 2 key caches named `kc_fast` and `kc_slow`
- Assigns the index for partition `p0` to the `kc_fast` key cache and the index for partitions `p1` and `p3` to the

`kc_slow` key cache; the index for the remaining partition (`p2`) uses the server's default key cache.

If you wish instead to assign the indexes for all partitions in table `pt` to a single key cache named `kc_all`,you can use either of the following two statements:

```
CACHE INDEX pt PARTITION (ALL) IN kc_all;
CACHE INDEX pt IN kc_all;
```

The two statements just shown are equivalent, and issuing either one has exactly the same effect. In other words, if you wish to assign indexes for all partitions of a partitioned table to the same key cache, the`PARTITION (ALL)` clause is optional.

When assigning indexes for multiple partitions to a key cache, the partitions need not be contiguous, and you need not list their names in any particular order. Indexes for any partitions not explicitly assigned to a key cache automatically use the server default key cache.

Index preloading is also supported for partitioned `MyISAM` tables. For more information, see Section 13.7.6.5, “LOAD INDEX INTO CACHE Statement”.

In MySQL 5.6.11 only, `gtid_next` must be set to `AUTOMATIC` before issuing this statement. (Bug#16062608, Bug #16715809, Bug #69045)

#### 13.7.6.3 FLUSH Statement

```
FLUSH [NO_WRITE_TO_BINLOG | LOCAL] {
flush_option [, flush_option] ...
| tables_option
}
flush_option: {
BINARY LOGS
| DES_KEY_FILE
| ENGINE LOGS
| ERROR LOGS
| GENERAL LOGS
| HOSTS
| LOGS
| PRIVILEGES
| QUERY CACHE
| RELAY LOGS
| SLOW LOGS
| STATUS
| USER_RESOURCES
```

Other Administrative Statements

```
}
tables_option: {
TABLES
| TABLES tbl_name [, tbl_name] ...
| TABLES WITH READ LOCK
| TABLES tbl_name [, tbl_name] ... WITH READ LOCK
| TABLES tbl_name [, tbl_name] ... FOR EXPORT
}
```

The `FLUSH` statement has several variant forms that clear or reload various internal caches, flush tables, or acquire locks. To execute `FLUSH`, you must have the `RELOAD` privilege. Specific flush options might require additional privileges, as indicated in the option descriptions.

Note It is not possible to issue `FLUSH` statements within stored functions or triggers.

However, you may use `FLUSH` in stored procedures, so long as these are not called from stored functions or triggers. See Section 20.8, “Restrictions on Stored Programs”.

By default, the server writes `FLUSH` statements to the binary log so that they replicate to replicas. To suppress logging, specify the optional `NO_WRITE_TO_BINLOG` keyword or its alias `LOCAL`.

> Note

```
FLUSH LOGS, FLUSH BINARY LOGS, FLUSH TABLES WITH READ LOCK (with
```

or without a table list), and `FLUSH TABLES tbl_name ... FOR EXPORT` are not written to the binary log in any case because they would cause problems if replicated to a replica.

The `FLUSH` statement causes an implicit commit. See Section 13.3.3, “Statements That Cause an Implicit Commit”.

The `mysqladmin` utility provides a command-line interface to some flush operations, using commands

```
such as flush-hosts, flush-logs, flush-privileges, flush-status, and flush-tables. See
```

Section 4.5.2, “mysqladmin — A MySQL Server Administration Program”.

Sending a `SIGHUP` signal to the server causes several flush operations to occur that are similar to various forms of the `FLUSH` statement. Signals can be sent by the `root` system account or the system account that owns the server process. This enables the flush operations to be performed without having to connect to the server, which requires a MySQL account that has privileges sufficient for those operations. See Section 4.10, “Unix Signal Handling in MySQL”.

The `RESET` statement is similar to `FLUSH`. See Section 13.7.6.6, “RESET Statement”, for information about using `RESET` with replication.

The following list describes the permitted `FLUSH` statement `flush_option` values. For descriptions of the permitted `tables_option` values, see FLUSH TABLES Syntax.

```
- FLUSH BINARY LOGS
```

Closes and reopens any binary log file to which the server is writing. If binary logging is enabled, the sequence number of the binary log file is incremented by one relative to the previous file.

This operation has no effect on tables used for the binary and relay logs (as controlled by the`master_info_repository` and `relay_log_info_repository` system variables).

```
- FLUSH DES_KEY_FILE
```

Other Administrative Statements Reloads the DES keys from the file that was specified with the `--des-key-file` option at server startup time.

```
- FLUSH ENGINE LOGS
```

Closes and reopens any flushable logs for installed storage engines. This causes `InnoDB` to flush its logs to disk.

```
- FLUSH ERROR LOGS
```

Closes and reopens any error log file to which the server is writing.

```
- FLUSH GENERAL LOGS
```

Closes and reopens any general query log file to which the server is writing.

This operation has no effect on tables used for the general query log (see Section 5.4.1, “Selecting General Query Log and Slow Query Log Output Destinations”).

```
- FLUSH HOSTS
```

Empties the host cache and the Performance Schema `host_cache` table that exposes the cache contents, and unblocks any blocked hosts.

For information about why host cache flushing might be advisable or desirable, see Section 5.1.11.2,“DNS Lookups and the Host Cache”.

> Note

```
The statement TRUNCATE TABLE performance_schema.host_cache,
```

unlike `FLUSH HOSTS`, is not written to the binary log. To obtain the same behavior from the latter, specify `NO_WRITE_TO_BINLOG` or `LOCAL` as part of the`FLUSH HOSTS` statement.

```
- FLUSH LOGS
```

Closes and reopens any log file to which the server is writing.

The effect of this operation is equivalent to the combined effects of these operations:

```
FLUSH BINARY LOGS
FLUSH ENGINE LOGS
FLUSH ERROR LOGS
FLUSH GENERAL LOGS
FLUSH RELAY LOGS
FLUSH SLOW LOGS
- FLUSH PRIVILEGES
```

Re-reads the privileges from the grant tables in the `mysql` system database.

Reloading the grant tables is necessary to enable updates to MySQL privileges and users only if you make such changes directly to the grant tables; it is not needed for account management statements such as `GRANT` or `REVOKE`, which take effect immediately. See Section 6.2.8, “When Privilege Changes Take Effect”, for more information.

If the `--skip-grant-tables` option was specified at server startup to disable the MySQL privilege system, `FLUSH PRIVILEGES` provides a way to enable the privilege system at runtime.

Other Administrative Statements Frees memory cached by the server as a result of `GRANT`, `CREATE USER`, `CREATE SERVER`, and`INSTALL PLUGIN` statements. This memory is not released by the corresponding `REVOKE`, `DROP``USER`, `DROP SERVER`, and `UNINSTALL PLUGIN` statements, so for a server that executes many instances of the statements that cause caching, there is likely to be an increase in cached memory use unless it is freed with `FLUSH PRIVILEGES`.

```
- FLUSH QUERY CACHE
```

Defragment the query cache to better utilize its memory. `FLUSH QUERY CACHE` does not remove any queries from the cache, unlike `FLUSH TABLES` or `RESET QUERY CACHE`.

```
- FLUSH RELAY LOGS
```

Closes and reopens any relay log file to which the server is writing. If relay logging is enabled, the sequence number of the relay log file is incremented by one relative to the previous file.

This operation has no effect on tables used for the binary and relay logs (as controlled by the`master_info_repository` and `relay_log_info_repository` system variables).

```
- FLUSH SLOW LOGS
```

Closes and reopens any slow query log file to which the server is writing.

This operation has no effect on tables used for the slow query log (see Section 5.4.1, “Selecting General Query Log and Slow Query Log Output Destinations”).

```
- FLUSH STATUS
```

Flushes status indicators.

This operation adds the current thread's session status variable values to the global values and resets the session values to zero. Some global variables may be reset to zero as well. It also resets the counters for key caches (default and named) to zero and sets `Max_used_connections` to the current number of open connections. This information may be of use when debugging a query. See Section 1.5,“How to Report Bugs or Problems”.

`FLUSH STATUS` is unaffected by `read_only` or `super_read_only`, and is always written to the binary log.

```
- FLUSH USER_RESOURCES
```

Resets all per-hour user resource indicators to zero.

Resetting resource indicators enables clients that have reached their hourly connection, query, or update limits to resume activity immediately. `FLUSH USER_RESOURCES` does not apply to the limit on maximum simultaneous connections that is controlled by the `max_user_connections` system variable. See Section 6.2.13, “Setting Account Resource Limits”.

In MySQL 5.6.11 only, `gtid_next` must be set to `AUTOMATIC` before issuing this statement. (Bug#16062608, Bug #16715809, Bug #69045)FLUSH TABLES Syntax`FLUSH TABLES` flushes tables, and, depending on the variant used, acquires locks. Any `TABLES` variant used in a `FLUSH` statement must be the only option used. `FLUSH TABLE` is a synonym for `FLUSH`

```
TABLES.
```

Other Administrative Statements Note The descriptions here that indicate tables are flushed by closing them apply differently for `InnoDB`, which flushes table contents to disk but leaves them open.

This still permits table files to be copied while the tables are open, as long as other activity does not modify them.

```
- FLUSH TABLES
```

Closes all open tables, forces all tables in use to be closed, and flushes the query cache and prepared statement cache. `FLUSH TABLES` also removes all query results from the query cache, like the `RESET``QUERY CACHE` statement. For information about query caching and prepared statement caching, see Section 8.10.3, “The MySQL Query Cache”. and Section 8.10.4, “Caching of Prepared Statements and Stored Programs”.

`FLUSH TABLES` is not permitted when there is an active `LOCK TABLES ... READ`. To flush and lock tables, use `FLUSH TABLES tbl_name ... WITH READ LOCK` instead.

```
- FLUSH TABLES tbl_name [, tbl_name] ...
```

With a list of one or more comma-separated table names, this operation is like `FLUSH TABLES` with no names except that the server flushes only the named tables. If a named table does not exist, no error occurs.

```
- FLUSH TABLES WITH READ LOCK
```

Closes all open tables and locks all tables for all databases with a global read lock.

This operation is a very convenient way to get backups if you have a file system such as Veritas or ZFS that can take snapshots in time. Use `UNLOCK TABLES` to release the lock.

`FLUSH TABLES WITH READ LOCK` acquires a global read lock rather than table locks, so it is not subject to the same behavior as `LOCK TABLES` and `UNLOCK TABLES` with respect to table locking and implicit commits:

- `UNLOCK TABLES` implicitly commits any active transaction only if any tables currently have been

locked with `LOCK TABLES`. The commit does not occur for `UNLOCK TABLES` following `FLUSH``TABLES WITH READ LOCK` because the latter statement does not acquire table locks.

- Beginning a transaction causes table locks acquired with `LOCK TABLES` to be released, as though you

had executed `UNLOCK TABLES`. Beginning a transaction does not release a global read lock acquired

```
with FLUSH TABLES WITH READ LOCK.
```

`FLUSH TABLES WITH READ LOCK` is not compatible with XA transactions.

`FLUSH TABLES WITH READ LOCK` does not prevent the server from inserting rows into the log tables(see Section 5.4.1, “Selecting General Query Log and Slow Query Log Output Destinations”).

```
- FLUSH TABLES tbl_name [, tbl_name] ... WITH READ LOCK
```

Flushes and acquires read locks for the named tables.

Because this operation acquires table locks, it requires the `LOCK TABLES` privilege for each table, in addition to the `RELOAD` privilege.

The operation first acquires exclusive metadata locks for the tables, so it waits for transactions that have those tables open to complete. Then the operation flushes the tables from the table cache, reopens Other Administrative Statements the tables, acquires table locks (like `LOCK TABLES ... READ`), and downgrades the metadata locks from exclusive to shared. After the operation acquires locks and downgrades the metadata locks, other sessions can read but not modify the tables.

This operation applies only to existing base (non-`TEMPORARY)` tables. If a name refers to a base table, that table is used. If it refers to a `TEMPORARY` table, it is ignored. If a name applies to a view, an`ER_WRONG_OBJECT` error occurs. Otherwise, an `ER_NO_SUCH_TABLE` error occurs.

Use `UNLOCK TABLES` to release the locks, `LOCK TABLES` to release the locks and acquire other locks,or `START TRANSACTION` to release the locks and begin a new transaction.

This `FLUSH TABLES` variant enables tables to be flushed and locked in a single operation. It provides a workaround for the restriction that `FLUSH TABLES` is not permitted when there is an active `LOCK`

```
TABLES ... READ.
```

This operation does not perform an implicit `UNLOCK TABLES`, so an error results if you perform the operation while there is any active `LOCK TABLES` or use it a second time without first releasing the locks acquired.

If a flushed table was opened with `HANDLER`, the handler is implicitly flushed and loses its position.

```
- FLUSH TABLES tbl_name [, tbl_name] ... FOR EXPORT
```

This `FLUSH TABLES` variant applies to `InnoDB` tables. It ensures that changes to the named tables have been flushed to disk so that binary table copies can be made while the server is running.

Because the `FLUSH TABLES ... FOR EXPORT` operation acquires locks on tables in preparation for exporting them, it requires the `LOCK TABLES` and `SELECT` privileges for each table, in addition to the`RELOAD` privilege.

The operation works like this:

1. It acquires shared metadata locks for the named tables. The operation blocks as long as other

sessions have active transactions that have modified those tables or hold table locks for them. When the locks have been acquired, the operation blocks transactions that attempt to update the tables,while permitting read-only operations to continue.

2. It checks whether all storage engines for the tables support `FOR EXPORT`. If any do not, an

`ER_ILLEGAL_HA` error occurs and the operation fails.

3. The operation notifies the storage engine for each table to make the table ready for export. The

storage engine must ensure that any pending changes are written to disk.

4. The operation puts the session in lock-tables mode so that the metadata locks acquired earlier are

not released when the `FOR EXPORT` operation completes.

This operation applies only to existing base (non-`TEMPORARY`) tables. If a name refers to a base table, that table is used. If it refers to a `TEMPORARY` table, it is ignored. If a name applies to a view, an`ER_WRONG_OBJECT` error occurs. Otherwise, an `ER_NO_SUCH_TABLE` error occurs.

`InnoDB` supports `FOR EXPORT` for tables that have their own `.ibd` file file (that is, tables created with the `innodb_file_per_table` setting enabled). `InnoDB` ensures when notified by the `FOR EXPORT`operation that any changes have been flushed to disk. This permits a binary copy of table contents to be made while the `FOR EXPORT` operation is in effect because the `.ibd` file is transaction consistent and Other Administrative Statements can be copied while the server is running. `FOR EXPORT` does not apply to `InnoDB` system tablespace files, or to `InnoDB` tables that have `FULLTEXT` indexes.

`FLUSH TABLES ...FOR EXPORT` does not work with partitioned `InnoDB` tables prior to MySQL 5.6.17,but is supported for such tables in MySQL 5.6.17 and higher.

When notified by `FOR EXPORT`, `InnoDB` writes to disk certain kinds of data that is normally held in memory or in separate disk buffers outside the tablespace files. For each table, `InnoDB` also produces a file named `table_name.cfg` in the same database directory as the table. The `.cfg` file contains metadata needed to reimport the tablespace files later, into the same or different server.

When the `FOR EXPORT` operation completes, `InnoDB` has flushed all dirty pages to the table data files.

Any change buffer entries are merged prior to flushing. At this point, the tables are locked and quiescent:The tables are in a transactionally consistent state on disk and you can copy the `.ibd` tablespace files along with the corresponding `.cfg` files to get a consistent snapshot of those tables.

For the procedure to reimport the copied table data into a MySQL instance, see Section 14.6.1.3,“Importing InnoDB Tables”.

After you are done with the tables, use `UNLOCK TABLES` to release the locks, `LOCK TABLES` to release the locks and acquire other locks, or `START TRANSACTION` to release the locks and begin a new transaction.

While any of these statements is in effect within the session, attempts to use `FLUSH TABLES ... FOR``EXPORT` produce an error:

```
FLUSH TABLES ... WITH READ LOCK
FLUSH TABLES ... FOR EXPORT
LOCK TABLES ... READ
LOCK TABLES ... WRITE
```

While `FLUSH TABLES ... FOR EXPORT` is in effect within the session, attempts to use any of these statements produce an error:

```
FLUSH TABLES WITH READ LOCK
FLUSH TABLES ... WITH READ LOCK
FLUSH TABLES ... FOR EXPORT
```

#### 13.7.6.4 KILL Statement

```
KILL [CONNECTION | QUERY] processlist_id
```

Each connection to `mysqld` runs in a separate thread. You can kill a thread with the `KILL``processlist_id` statement.

Thread processlist identifiers can be determined from the `ID` column of the `INFORMATION_SCHEMA``PROCESSLIST` table, the `Id` column of `SHOW PROCESSLIST` output, and the `PROCESSLIST_ID`column of the Performance Schema `threads` table. The value for the current thread is returned by the`CONNECTION_ID()` function.

`KILL` permits an optional `CONNECTION` or `QUERY` modifier:

- `KILL CONNECTION` is the same as `KILL` with no modifier: It terminates the connection associated with

the given `processlist_id`, after terminating any statement the connection is executing.

- `KILL QUERY` terminates the statement the connection is currently executing, but leaves the connection

itself intact.

The ability to see which threads are available to be killed depends on the `PROCESS` privilege:Other Administrative Statements

- Without `PROCESS`, you can see only your own threads.
- With `PROCESS`, you can see all threads.

The ability to kill threads and statements depends on the `SUPER` privilege:

- Without `SUPER`, you can kill only your own threads and statements.
- With `SUPER`, you can kill all threads and statements.

You can also use the `mysqladmin processlist` and `mysqladmin kill` commands to examine and kill threads.

Note You cannot use `KILL` with the Embedded MySQL Server library because the embedded server merely runs inside the threads of the host application. It does not create any connection threads of its own.

When you use `KILL`, a thread-specific kill flag is set for the thread. In most cases, it might take some time for the thread to die because the kill flag is checked only at specific intervals:

- During `SELECT` operations, for `ORDER BY` and `GROUP BY` loops, the flag is checked after reading a

block of rows. If the kill flag is set, the statement is aborted.

- `ALTER TABLE` operations that make a table copy check the kill flag periodically for each few copied rows

read from the original table. If the kill flag was set, the statement is aborted and the temporary table is deleted.

The `KILL` statement returns without waiting for confirmation, but the kill flag check aborts the operation within a reasonably small amount of time. Aborting the operation to perform any necessary cleanup also takes some time.

- During `UPDATE` or `DELETE` operations, the kill flag is checked after each block read and after each

updated or deleted row. If the kill flag is set, the statement is aborted. If you are not using transactions,the changes are not rolled back.

- `GET_LOCK()` aborts and returns `NULL`.
- An `INSERT DELAYED` thread quickly flushes (inserts) all rows it has in memory and then terminates.
- If the thread is in the table lock handler (state: `Locked`), the table lock is quickly aborted.
- If the thread is waiting for free disk space in a write call, the write is aborted with a “disk full” error

message.

Warning Killing a `REPAIR TABLE` or `OPTIMIZE TABLE` operation on a `MyISAM` table results in a table that is corrupted and unusable. Any reads or writes to such a table fail until you optimize or repair it again (without interruption).

#### 13.7.6.5 LOAD INDEX INTO CACHE Statement

```
LOAD INDEX INTO CACHE
tbl_index_list [, tbl_index_list] ...
tbl_index_list:
tbl_name
```

Other Administrative Statements

```
[PARTITION (partition_list)]
[{INDEX|KEY} (index_name[, index_name] ...)]
[IGNORE LEAVES]
partition_list: {
partition_name[, partition_name] ...
| ALL
}
```

The `LOAD INDEX INTO CACHE` statement preloads a table index into the key cache to which it has been assigned by an explicit `CACHE INDEX` statement, or into the default key cache otherwise.

`LOAD INDEX INTO CACHE` applies only to `MyISAM` tables, including partitioned `MyISAM` tables. In addition, indexes on partitioned tables can be preloaded for one, several, or all partitions.

The `IGNORE LEAVES` modifier causes only blocks for the nonleaf nodes of the index to be preloaded.

`IGNORE LEAVES` is also supported for partitioned `MyISAM` tables.

The following statement preloads nodes (index blocks) of indexes for the tables `t1` and `t2`:

```
mysql> LOAD INDEX INTO CACHE t1, t2 IGNORE LEAVES;
+---------+--------------+----------+----------+
| Table   | Op           | Msg_type | Msg_text |
+---------+--------------+----------+----------+
| test.t1 | preload_keys | status   | OK       |
| test.t2 | preload_keys | status   | OK       |
+---------+--------------+----------+----------+
```

This statement preloads all index blocks from `t1`. It preloads only blocks for the nonleaf nodes from `t2`.

The syntax of `LOAD INDEX INTO CACHE` enables you to specify that only particular indexes from a table should be preloaded. However, the implementation preloads all the table's indexes into the cache, so there is no reason to specify anything other than the table name.

In MySQL 5.6.11 only, `gtid_next` must be set to `AUTOMATIC` before issuing this statement. (Bug#16062608, Bug #16715809, Bug #69045)It is possible to preload indexes on specific partitions of partitioned `MyISAM` tables. For example, of the following 2 statements, the first preloads indexes for partition `p0` of a partitioned table `pt`, while the second preloads the indexes for partitions `p1` and `p3` of the same table:

```
LOAD INDEX INTO CACHE pt PARTITION (p0);
LOAD INDEX INTO CACHE pt PARTITION (p1, p3);
```

To preload the indexes for all partitions in table `pt`, you can use either of the following two statements:

```
LOAD INDEX INTO CACHE pt PARTITION (ALL);
LOAD INDEX INTO CACHE pt;
```

The two statements just shown are equivalent, and issuing either one has exactly the same effect. In other words, if you wish to preload indexes for all partitions of a partitioned table, the `PARTITION (ALL)` clause is optional.

When preloading indexes for multiple partitions, the partitions need not be contiguous, and you need not list their names in any particular order.

`LOAD INDEX INTO CACHE ... IGNORE LEAVES` fails unless all indexes in a table have the same block size. To determine index block sizes for a table, use `myisamchk -dv` and check the `Blocksize`column.

Utility Statements

#### 13.7.6.6 RESET Statement

```
RESET reset_option [, reset_option] ...
reset_option: {
MASTER
| QUERY CACHE
| SLAVE
}
```

The `RESET` statement is used to clear the state of various server operations. You must have the `RELOAD`privilege to execute `RESET`.

`RESET` acts as a stronger version of the `FLUSH` statement. See Section 13.7.6.3, “FLUSH Statement”.

The `RESET` statement causes an implicit commit. See Section 13.3.3, “Statements That Cause an Implicit Commit”.

In MySQL 5.6.11 only, `gtid_next` must be set to `AUTOMATIC` before issuing this statement. (Bug#16062608, Bug #16715809, Bug #69045)The following list describes the permitted `RESET` statement `reset_option` values:

```
- RESET MASTER
```

Deletes all binary logs listed in the index file, resets the binary log index file to be empty, and creates a new binary log file.

```
- RESET QUERY CACHE
```

Removes all query results from the query cache.

```
- RESET SLAVE
```

Makes the replica forget its replication position in the source binary logs. Also resets the relay log by deleting any existing relay log files and beginning a new one.

## 13.8 Utility Statements

### 13.8.1 DESCRIBE Statement

The `DESCRIBE` and `EXPLAIN` statements are synonyms, used either to obtain information about table structure or query execution plans. For more information, see Section 13.7.5.6, “SHOW COLUMNS Statement”, and Section 13.8.2, “EXPLAIN Statement”.

### 13.8.2 EXPLAIN Statement

```
{EXPLAIN | DESCRIBE | DESC}
tbl_name [col_name | wild]
{EXPLAIN | DESCRIBE | DESC}
[explain_type]
explainable_stmt
explain_type: {
EXTENDED
| PARTITIONS
| FORMAT = format_name
}
```

EXPLAIN Statement

```
format_name: {
TRADITIONAL
| JSON
}
explainable_stmt: {
SELECT statement
| DELETE statement
| INSERT statement
| REPLACE statement
| UPDATE statement
}
```

The `DESCRIBE` and `EXPLAIN` statements are synonyms. In practice, the `DESCRIBE` keyword is more often used to obtain information about table structure, whereas `EXPLAIN` is used to obtain a query execution plan (that is, an explanation of how MySQL would execute a query).

The following discussion uses the `DESCRIBE` and `EXPLAIN` keywords in accordance with those uses, but the MySQL parser treats them as completely synonymous.

- Obtaining Table Structure Information
- Obtaining Execution Plan Information

> Obtaining Table Structure Information

`DESCRIBE` provides information about the columns in a table:

```
mysql> DESCRIBE City;
+------------+----------+------+-----+---------+----------------+
| Field      | Type     | Null | Key | Default | Extra          |
+------------+----------+------+-----+---------+----------------+
| Id         | int(11)  | NO   | PRI | NULL    | auto_increment |
| Name       | char(35) | NO   |     |         |                |
| Country    | char(3)  | NO   | UNI |         |                |
| District   | char(20) | YES  | MUL |         |                |
| Population | int(11)  | NO   |     | 0       |                |
+------------+----------+------+-----+---------+----------------+
```

`DESCRIBE` is a shortcut for `SHOW COLUMNS`. These statements also display information for views. The description for `SHOW COLUMNS` provides more information about the output columns. See Section 13.7.5.6,“SHOW COLUMNS Statement”.

By default, `DESCRIBE` displays information about all columns in the table. `col_name`, if given, is the name of a column in the table. In this case, the statement displays information only for the named column. `wild`,if given, is a pattern string. It can contain the SQL % and _ wildcard characters. In this case, the statement displays output only for the columns with names matching the string. There is no need to enclose the string within quotation marks unless it contains spaces or other special characters.

The `DESCRIBE` statement is provided for compatibility with Oracle.

The `SHOW CREATE TABLE`, `SHOW TABLE STATUS`, and `SHOW INDEX` statements also provide information about tables. See Section 13.7.5, “SHOW Statements”.

> Obtaining Execution Plan Information

The `EXPLAIN` statement provides information about how MySQL executes statements:

- `EXPLAIN` works with `SELECT`, `DELETE`, `INSERT`, `REPLACE`, and `UPDATE` statements.

HELP Statement

- When `EXPLAIN` is used with an explainable statement, MySQL displays information from the optimizer

about the statement execution plan. That is, MySQL explains how it would process the statement,including information about how tables are joined and in which order. For information about using`EXPLAIN` to obtain execution plan information, see Section 8.8.2, “EXPLAIN Output Format”.

- `EXPLAIN EXTENDED` produces additional execution plan information that can be displayed using `SHOW`

`WARNINGS`. See Section 8.8.3, “Extended EXPLAIN Output Format”.

- `EXPLAIN PARTITIONS` is useful for examining queries involving partitioned tables. See Section 19.3.5,

“Obtaining Information About Partitions”.

- The `FORMAT` option can be used to select the output format. `TRADITIONAL` presents the output in

tabular format. This is the default if no `FORMAT` option is present. `JSON` format displays the information in JSON format. With `FORMAT = JSON`, the output includes extended and partition information.

`EXPLAIN` requires the same privileges required to execute the explained statement. Additionally, `EXPLAIN`also requires the `SHOW VIEW` privilege for any explained view.

With the help of `EXPLAIN`, you can see where you should add indexes to tables so that the statement executes faster by using indexes to find rows. You can also use `EXPLAIN` to check whether the optimizer joins the tables in an optimal order. To give a hint to the optimizer to use a join order corresponding to the order in which the tables are named in a `SELECT` statement, begin the statement with `SELECT``STRAIGHT_JOIN` rather than just `SELECT`. (See Section 13.2.9, “SELECT Statement”.)If you have a problem with indexes not being used when you believe that they should be, run `ANALYZE``TABLE` to update table statistics, such as cardinality of keys, that can affect the choices the optimizer makes. See Section 13.7.2.1, “ANALYZE TABLE Statement”.

Note MySQL Workbench has a Visual Explain capability that provides a visual representation of `EXPLAIN` output. See Tutorial: Using Explain to Improve Query Performance.

### 13.8.3 HELP Statement

```
HELP 'search_string'
```

The `HELP` statement returns online information from the MySQL Reference Manual. Its proper operation requires that the help tables in the `mysql` database be initialized with help topic information (see Section 5.1.14, “Server-Side Help Support”).

The `HELP` statement searches the help tables for the given search string and displays the result of the search. The search string is not case-sensitive.

The search string can contain the wildcard characters % and _. These have the same meaning as for pattern-matching operations performed with the `LIKE` operator. For example, `HELP 'rep%'` returns a list of topics that begin with `rep`.

The HELP statement understands several types of search strings:

- At the most general level, use `contents` to retrieve a list of the top-level help categories:

```
HELP 'contents'
```

- For a list of topics in a given help category, such as `Data Types`, use the category name:

```
HELP 'data types'
```

HELP Statement

- For help on a specific help topic, such as the `ASCII()` function or the `CREATE TABLE` statement, use

the associated keyword or keywords:

```
HELP 'ascii'
HELP 'create table'
```

In other words, the search string matches a category, many topics, or a single topic. You cannot necessarily tell in advance whether a given search string returns a list of items or the help information for a single help topic. However, you can tell what kind of response `HELP` returned by examining the number of rows and columns in the result set.

The following descriptions indicate the forms that the result set can take. Output for the example statements is shown using the familiar “tabular” or “vertical” format that you see when using the `mysql`client.

Note The `mysql` itself reformats `HELP` result sets in a different way.

- Empty result set

No match could be found for the search string.

- Result set containing a single row with three columns

This means that the search string yielded a hit for the help topic. The result has three columns:

- `name`: The topic name.
- `description`: Descriptive help text for the topic.
- `example`: Usage example or examples. This column might be blank.

Example: `HELP 'replace'`Yields:

```
name: REPLACE
description: Syntax:
REPLACE(str,from_str,to_str)
Returns the string str with all occurrences of the string from_str
replaced by the string to_str. REPLACE() performs a case-sensitive
match when searching for from_str.
example: mysql> SELECT REPLACE('www.mysql.com', 'w', 'Ww');
-> 'WwWwWw.mysql.com'
```

- Result set containing multiple rows with two columns

This means that the search string matched many help topics. The result set indicates the help topic names:

- `name`: The help topic name.
- `is_it_category`: Y if the name represents a help category, N if it does not. If it does not, the `name`

value when specified as the argument to the `HELP` statement should yield a single-row result set containing a description for the named item.

Example: `HELP 'status'`USE Statement Yields:

```
+-----------------------+----------------+
| name                  | is_it_category |
+-----------------------+----------------+
| SHOW                  | N              |
| SHOW ENGINE           | N              |
| SHOW MASTER STATUS    | N              |
| SHOW PROCEDURE STATUS | N              |
| SHOW SLAVE STATUS     | N              |
| SHOW STATUS           | N              |
| SHOW TABLE STATUS     | N              |
+-----------------------+----------------+
```

- Result set containing multiple rows with three columns

This means the search string matches a category. The result set contains category entries:

- `source_category_name`: The help category name.
- `name`: The category or topic name
- `is_it_category`: Y if the name represents a help category, N if it does not. If it does not, the `name`

value when specified as the argument to the `HELP` statement should yield a single-row result set containing a description for the named item.

Example: `HELP 'functions'`Yields:

```
+----------------------+-------------------------+----------------+
| source_category_name | name                    | is_it_category |
+----------------------+-------------------------+----------------+
| Functions            | CREATE FUNCTION         | N              |
| Functions            | DROP FUNCTION           | N              |
| Functions            | Bit Functions           | Y              |
| Functions            | Comparison operators    | Y              |
| Functions            | Control flow functions  | Y              |
| Functions            | Date and Time Functions | Y              |
| Functions            | Encryption Functions    | Y              |
| Functions            | Information Functions   | Y              |
| Functions            | Logical operators       | Y              |
| Functions            | Miscellaneous Functions | Y              |
| Functions            | Numeric Functions       | Y              |
| Functions            | String Functions        | Y              |
+----------------------+-------------------------+----------------+
```

### 13.8.4 USE Statement

```
USE db_name
```

The `USE` statement tells MySQL to use the named database as the default (current) database for subsequent statements. This statement requires some privilege for the database or some object within it.

The named database remains the default until the end of the session or another `USE` statement is issued:

```
USE db1;
SELECT COUNT(*) FROM mytable;   # selects from db1.mytable
USE db2;
SELECT COUNT(*) FROM mytable;   # selects from db2.mytable
```

The database name must be specified on a single line. Newlines in database names are not supported.

USE Statement Making a particular database the default by means of the `USE` statement does not preclude accessing tables in other databases. The following example accesses the `author` table from the `db1` database and the `editor` table from the `db2` database:

```
USE db1;
SELECT author_name,editor_name FROM author,db2.editor
WHERE author.editor_id = db2.editor.editor_id;
```
