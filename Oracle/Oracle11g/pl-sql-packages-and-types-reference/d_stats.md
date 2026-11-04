---
title: DBMS_STATS
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_stats.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 142 DBMS\_STATS

With the `DBMS_STATS` package you can view and modify optimizer statistics gathered for database objects.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm)

This chapter contains the following topics:

- Using DBMS\_STATS
- Summary of DBMS\_STATS Subprograms

---

## Using DBMS\_STATS

This section contains topics which relate to using the `DBMS_STATS` package.

---

### Overview

The Oracle RDBMS allows you to collect statistics of many different kinds as an aid to improving performance. This package is concerned with optimizer statistics only. Given that Oracle sets automatic statistics collection of this kind on by default, this package is intended for only specialized cases.

The statistics of interest to be viewed or modified can reside in the dictionary or in a table created in the user's schema for this purpose. You can also collect and manage user-defined statistics for tables and domain indexes using this package.

For example, if the `DELETE_COLUMN_STATS` procedure is invoked on a column for which an association is defined, user-defined statistics for that column are deleted in addition to deletion of the standard statistics.

Only statistics stored in the dictionary have an impact on the cost-based optimizer. You can also use `DBMS_STATS` to gather statistics in parallel

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/stats.htm#PFGRF003) for more information about "Managing Optimizer Statistics".

---

### Types

Types for the minimum and maximum values and histogram endpoints include:

```
TYPE numarray  IS VARRAY(256) OF NUMBER;
TYPE datearray IS VARRAY(256) OF DATE;
TYPE chararray IS VARRAY(256) OF VARCHAR2(4000);
TYPE rawarray  IS VARRAY(256) OF RAW(2000);
TYPE fltarray IS VARRAY(256) OF BINARY_FLOAT;
TYPE dblarray IS VARRAY(256) OF BINARY_DOUBLE;
 
TYPE StatRec IS RECORD (
  epc    NUMBER,
  minval RAW(2000),
  maxval RAW(2000),
  bkvals NUMARRAY,
  novals NUMARRAY,
  chvals CHARARRAY,
  eavs   NUMBER);
```

Types for listing stale tables include:

```
TYPE ObjectElem IS RECORD (
  ownname     VARCHAR2(30),     -- owner
  objtype     VARCHAR2(6),      -- 'TABLE' or 'INDEX'
  objname     VARCHAR2(30),     -- table/index
  partname    VARCHAR2(30),     -- partition
  subpartname VARCHAR2(30));    -- subpartition
type ObjectTab is TABLE of ObjectElem;
```

Type for displaying statistics difference report:

```
TYPE DiffRepElem IS RECORD (
 report     CLOB,              -- stats difference report
 maxdiffpct number);           -- max stats difference (percentage)
type DiffRepTab is table of DiffRepElem;
```

---

### Constants

The `DBMS_STATS` package uses the constants shown in Table 142-1:

Table 142-1 DBMS\_STATS Constants

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `AUTO_CASCADE` | `BOOLEAN` | `NULL` | Lets Oracle decide whether to collect statistics for indexes or not |
| `AUTO_DEGREE` | `NUMBER` | `32768` | Lets Oracle select the degree of parallelism based on size of the object, number of CPUs and initialization parameters. For definition of default parallel degree, see " [Degree of Parallelism"](https://docs.oracle.com/cd/E11882_01/server.112/e25523/parallel002.htm#VLDBG0102) in [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/toc.htm). |
| `AUTO_INVALIDATE` | `BOOLEAN` | NULL | Lets Oracle decide when to invalidate dependent cursors |
| `AUTO_SAMPLE_SIZE` | `NUMBER` | `0` | Indicates that auto-sample size algorithms should be used |

---

### Operational Notes

The `DBMS_STATS` subprograms perform the following general operations:

- Gathering Optimizer Statistics
- Setting or Getting Statistics
- Deleting Statistics
- Transferring Statistics
- Locking or Unlocking Statistics
- Restoring and Purging Statistics History
- User-Defined Statistics
- Pending Statistics
- Comparing Statistics
- Extended Statistics

Most of the `DBMS_STATS` procedures include the three parameters `statown`, `stattab`, and `statid`. These parameters allow you to store statistics in your own tables (outside of the dictionary), which does not affect the optimizer. Therefore, you can maintain and experiment with sets of statistics.

The `stattab` parameter specifies the name of a table in which to hold statistics, and it is assumed that it resides in the same schema as the object for which statistics are collected (unless the `statown` parameter is specified). You can create multiple tables with different `stattab` identifiers to hold separate sets of statistics.

Additionally, you can maintain different sets of statistics within a single `stattab` by using the `statid` parameter, which avoids cluttering the user's schema.

For the `SET` and `GET` procedures, if `stattab` is not provided (that is, `NULL`), then the operation works directly on the dictionary statistics; therefore, you do not need to create these statistics tables if they only plan to modify the dictionary directly. However, if `stattab` is not `NULL`, then the `SET` or `GET` operation works on the specified user statistics table, and not the dictionary.

You can change the default values of some of the parameters of `DBMS_STATS` procedures using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure.

Most of the procedures in this package commit the current transaction, perform the operation, and then commit again.

Most of the procedures have a parameter, `force` which allows you to override any lock on statistics.Whenever statistics in dictionary are modified, old versions of statistics are saved automatically for future restoring.

Gathering Optimizer Statistics

Use the following subprograms to gather certain classes of optimizer statistics, with possible performance improvements over the `ANALYZE` command:

  
GATHER\_DATABASE\_STATS Procedures  
GATHER\_DICTIONARY\_STATS Procedure  
GATHER\_FIXED\_OBJECTS\_STATS Procedure  
GATHER\_INDEX\_STATS Procedure  
GATHER\_SCHEMA\_STATS Procedures  
GATHER\_SYSTEM\_STATS Procedure  
GATHER\_TABLE\_STATS Procedure  

The `GATHER_*` procedures also collect user-defined statistics for columns and domain indexes.

The `statown`, `stattab`, and `statid` parameters instruct the package to back up current statistics in the specified table before gathering new statistics.

Oracle also provides the following procedure for generating statistics for derived objects when you have sufficient statistics on related objects:

GENERATE\_STATS Procedure

Setting or Getting Statistics

Use the following subprograms to store and retrieve individual column-related, index-related, and table-related statistics:

  
PREPARE\_COLUMN\_VALUES Procedures  
PREPARE\_COLUMN\_VALUES\_NVARCHAR2 Procedure  
PREPARE\_COLUMN\_VALUES\_ROWID Procedure  
  
SEED\_COL\_USAGE Procedure  
SET\_INDEX\_STATS Procedures  
SET\_SYSTEM\_STATS Procedure  
SET\_TABLE\_STATS Procedure  
  
GET\_COLUMN\_STATS Procedures  
GET\_INDEX\_STATS Procedures  
GET\_SYSTEM\_STATS Procedure  
GET\_TABLE\_STATS Procedure  

In the special versions of the `SET_*_STATS` procedures for setting user-defined statistics, the following, if provided, are stored in the dictionary or external statistics table:

- User-defined statistics (`extstats`)
- The statistics type schema name (`statsschema`)
- The statistics type name (`statsname`)

The user-defined statistics and the corresponding statistics type are inserted into the `USTATS$` dictionary table. You can specify user-defined statistics without specifying the statistics type name.

The special versions of the `GET_*_STATS` procedures return user-defined statistics and the statistics type owner and name as `OUT` arguments corresponding to the schema object specified. If user-defined statistics are not collected, `NULL` values are returned.

Deleting Statistics

The `DELETE_*` procedures delete both user-defined statistics and the standard statistics for the given schema object.

  
DELETE\_COLUMN\_STATS Procedure  
DELETE\_DATABASE\_STATS Procedure  
DELETE\_DICTIONARY\_STATS Procedure  
DELETE\_FIXED\_OBJECTS\_STATS Procedure  
DELETE\_INDEX\_STATS Procedure  
DELETE\_SCHEMA\_STATS Procedure  
DELETE\_SYSTEM\_STATS Procedure  
DELETE\_TABLE\_STATS Procedure

Transferring Statistics

Use the following procedures for creating and dropping the user statistics table.

  
CREATE\_STAT\_TABLE Procedure  
DROP\_STAT\_TABLE Procedure  

Use the following procedures to transfer statistics

- from the dictionary to a user statistics table (`EXPORT_` \*)
- from a user statistics table to the dictionary (`IMPORT_` \*)
  
EXPORT\_COLUMN\_STATS Procedure  
EXPORT\_DATABASE\_STATS Procedure  
EXPORT\_DICTIONARY\_STATS Procedure  
EXPORT\_FIXED\_OBJECTS\_STATS Procedure  
EXPORT\_INDEX\_STATS Procedure  
EXPORT\_SCHEMA\_STATS Procedure  
EXPORT\_SYSTEM\_STATS Procedure  
EXPORT\_TABLE\_STATS Procedure  
  
IMPORT\_COLUMN\_STATS Procedure  
IMPORT\_DATABASE\_STATS Procedure  
IMPORT\_DICTIONARY\_STATS Procedure  
IMPORT\_FIXED\_OBJECTS\_STATS Procedure  
IMPORT\_INDEX\_STATS Procedure  
IMPORT\_SCHEMA\_STATS Procedure  
IMPORT\_SYSTEM\_STATS Procedure  
IMPORT\_TABLE\_STATS Procedure

Note:

Oracle does not support export or import of statistics across databases of different character sets.

Locking or Unlocking Statistics

Use the following procedures to lock and unlock statistics on objects.

  
LOCK\_SCHEMA\_STATS Procedure  
LOCK\_TABLE\_STATS Procedure  
  
UNLOCK\_SCHEMA\_STATS Procedure  
UNLOCK\_TABLE\_STATS Procedure  

The `LOCK_*` procedures either freeze the current set of the statistics or to keep the statistics empty (uncollected).When statistics on a table are locked, all the statistics depending on the table, including table statistics, column statistics, histograms and statistics on all dependent indexes, are considered to be locked.

Restoring and Purging Statistics History

Use the following procedures to restore statistics as of a specified timestamp. This is useful in case newly collected statistics leads to some sub-optimal execution plans and the administrator wants to revert to the previous set of statistics.

  
RESET\_GLOBAL\_PREF\_DEFAULTS Procedure  
RESTORE\_DICTIONARY\_STATS Procedure  
RESTORE\_FIXED\_OBJECTS\_STATS Procedure  
RESTORE\_SCHEMA\_STATS Procedure  
RESTORE\_SYSTEM\_STATS Procedure  
RESTORE\_TABLE\_STATS Procedure  

Whenever statistics in dictionary are modified, old versions of statistics are saved automatically for future restoring. The old statistics are purged automatically at regular intervals based on the statistics history retention setting and the time of recent statistics gathering performed in the system. Retention is configurable using the ALTER\_STATS\_HISTORY\_RETENTION Procedure.

The other `DBMS_STATS` procedures related to restoring statistics are:

- PURGE\_STATS Procedure: This procedure lets you manually purge old versions beyond a time stamp.
- GET\_STATS\_HISTORY\_RETENTION Function: This function gets the current statistics history retention value.
- GET\_STATS\_HISTORY\_AVAILABILITY Function: This function gets the oldest time stamp where statistics history is available. Users cannot restore statistics to a time stamp older than the oldest time stamp.

`RESTORE_*` operations are not supported for user defined statistics.

User-Defined Statistics

The `DBMS_STATS` package supports operations on user-defined statistics. When a domain index or column is associated with a statistics type (using the `associate` statement), operations on the index or column manipulate user-defined statistics. For example, gathering statistics for a domain index (for which an association with a statistics type exists) using the GET\_INDEX\_STATS Procedures invokes the user-defined statistics collection method of the associated statistics type. Similarly, delete, transfer, import, and export operations manipulate user-defined statistics.

`SET_*` and `GET_*` operations for user-defined statistics are also supported using a special version of the `SET` and `GET` interfaces for columns and indexes.

`EXPORT_*`, `IMPORT_*` and `RESTORE_*` operations are not supported for user defined statistics.

Pending Statistics

The package gather statistics and stores it in the dictionary by default. User's can store these statistics in the system's private area instead of the dictionary by turning the `PUBLISH` option to `FALSE` using the `SET*PREFS` procedures. The default value for `PUBLISH` is `TRUE`.The statistics stored in private area are not used by Cost Based Optimizer unless parameter `optimizer_use_pending_statistics` is set to `TRUE`. The default value of this parameter is `FALSE` and this boolean parameter can be set at the session/system level. Users can verify the impact of the new statistics on query plans by using the pending statistics on a session.

Pending statistics provide a mechanism to verify the impact of the new statistics on query plans before making them available for general use. There are two scenarios to verify the query plans:

- Export the pending statistics (use the EXPORT\_PENDING\_STATS Procedure) to a test system, then run the query workload and check the performance or plans.
- Set `optimizer_use_pending_statistics` to `TRUE` in a session on the system where pending statistics have been gathered, run the workload, and check the performance or plans.

Once the performance or query plans have been verified, the pending statistics can be published (run the PUBLISH\_PENDING\_STATS Procedure) if the performance is acceptable or delete (run the DELETE\_PENDING\_STATS Procedure) if not.

Pending statistics can be published, exported, or deleted. The following procedures are provided to manage pending statistics:

- DELETE\_PENDING\_STATS Procedure
- EXPORT\_PENDING\_STATS Procedure
- PUBLISH\_PENDING\_STATS Procedure

Comparing Statistics

The `DIFF_TABLE_STATS_` \* statistics can be used to compare statistics for a table from two different sources. The statistics can be from:

- two different user statistics tables
- a single user statistics table containing two sets of statistics that can be identified using statids
- a user statistics table and dictionary history
- pending statistics

The functions also compare the statistics of the dependent objects (indexes, columns, partitions). They displays statistics of the object(s) from both sources if the difference between those statistics exceeds a certain threshold (%). The threshold can be specified as an argument to the function, with a default of 10%. The statistics corresponding to the first source (`stattab1` or `time1`) will be used as basis for computing the differential percentage.

Extended Statistics

This package allows you to collect statistics for column groups and expressions (known as "statistics extensions"). The statistics collected for column groups and expressions are called "extended statistics".

Statistics on Column groups are used by optimizer for accounting correlation between columns. For example, if a query has predicates c1=1 and c2=1 and if there are statistics on (c1, c2), the optimizer will use this statistics for estimating the combined selectivity of the predicates.The expression statistics are used by optimizer for estimating selectivity of predicates on those expressions. The extended statistics are similar to column statistics and the procedures that take columns names will accept extension names in place of column names.

Related subprograms:

- CREATE\_EXTENDED\_STATS Function
- DROP\_EXTENDED\_STATS Procedure
- SHOW\_EXTENDED\_STATS\_NAME Function

---

### Examples

- Using Pending Statistics
- Gathering Daytime System Statistics

Using Pending Statistics

Assume many modifications have been made to the `employees` table since the last time statistics were gathered. To ensure that the cost-based optimizer is still picking the best plan, statistics should be gathered once again; however, the user is concerned that new statistics will cause the optimizer to choose bad plans when the current ones are acceptable. The user can do the following:

```
EXEC DBMS_STATS.SET_TABLE_PREFS('hr', 'employees', 'PUBLISH', 'false');
```

By setting the employees tables publish preference to `FALSE`, any statistics gather from now on will not be automatically published. The newly gathered statistics will be marked as pending.

```
EXEC DBMS_STATS.GATHER_TABLE_STATS ('hr', 'employees');
```

To test the newly gathered statistics, set `optimizer_pending_statistics` to `TRUE` in a session and run sample queries.

```
ALTER SESSION SET optimizer_use_pending_statistics = TRUE;
```

If the pending statistics generate sound execution plans, they can be published:

```
EXEC DBMS_STATS.PUBLISH_PENDING_STATS('hr', 'employees');
EXEC DBMS_STATS.SET_TABLE_PREF('hr', 'employees', 'PUBLISH', 'true');
```

Gathering Daytime System Statistics

Assume that you want to perform database application processing OLTP transactions during the day and run reports at night.

To collect daytime system statistics, gather statistics for 720 minutes. Store the statistics in the `MYSTATS` table.

```
BEGIN
   DBMS_STATS.GATHER_SYSTEM_STATS (
      interval => 720,
      stattab  => 'mystats',
      statid   => 'OLTP');
END;
```

To collect nighttime system statistics, gather statistics for 720 minutes. Store the statistics in the `MYSTATS` table.

```
BEGIN
   DBMS_STATS.GATHER_SYSTEM_STATS (
      interval => 720,
      stattab  => 'mystats',
      statid   => 'OLAP');
END;
```

Update the dictionary with the gathered statistics.

```
VARIABLE   jobno   number;
BEGIN
   DBMS_JOB.SUBMIT (:jobno, 'DBMS_STATS.IMPORT_SYSTEM_STATS
   (''mystats'',''OLTP'');'
   sysdate, 'sysdate + 1');
   COMMIT;
END;

BEGIN
   DBMS_JOB.SUBMIT (:jobno, 'DBMS_STATS.IMPORT_SYSTEM_STATS
   (''mystats'',''OLAP'');'
   sysdate + 0.5, 'sysdate + 1');
   COMMIT;
END;
```

---

## Summary of DBMS\_STATS Subprograms

Table 142-2 DBMS\_STATS Package Subprograms

| Subprogram | Description |
| --- | --- |
| ALTER\_STATS\_HISTORY\_RETENTION Procedure | Changes the statistics history retention value |
| CONVERT\_RAW\_VALUE Procedures | Convert the internal representation of a minimum or maximum value into a datatype-specific value |
| CONVERT\_RAW\_VALUE\_NVARCHAR Procedure | Convert the internal representation of a minimum or maximum value into a datatype-specific value |
| CONVERT\_RAW\_VALUE\_ROWID Procedure | Convert the internal representation of a minimum or maximum value into a datatype-specific value |
| COPY\_TABLE\_STATS Procedure | Copies the statistics of the source \[sub\] partition to the destination \[sub\] partition after scaling |
| CREATE\_EXTENDED\_STATS Function | Creates a virtual column for a user specified column group or an expression in a table |
| CREATE\_STAT\_TABLE Procedure | Creates a table with name `stattab` in ownname's schema which is capable of holding statistics |
| DELETE\_COLUMN\_STATS Procedure | Deletes column-related statistics |
| DELETE\_DATABASE\_PREFS Procedure | Deletes the statistics preferences of all the tables, excluding the tables owned by Oracle |
| DELETE\_DATABASE\_STATS Procedure | Deletes statistics for the entire database |
| DELETE\_DICTIONARY\_STATS Procedure | Deletes statistics for all dictionary schemas (' `SYS` ', ' `SYSTEM` ' and RDBMS component schemas) |
| DELETE\_FIXED\_OBJECTS\_STATS Procedure | Deletes statistics of all fixed tables |
| DELETE\_INDEX\_STATS Procedure | Deletes index-related statistics |
| DELETE\_PENDING\_STATS Procedure | Deletes the private statistics that have been collected but have not been published |
| DELETE\_SCHEMA\_PREFS Procedure | Deletes the statistics preferences of all the tables owned by the specified owner name |
| DELETE\_SCHEMA\_STATS Procedure | Deletes schema-related statistics |
| DELETE\_SYSTEM\_STATS Procedure | Deletes system statistics |
| DELETE\_TABLE\_PREFS Procedure | Deletes statistics preferences of the specified table in the specified schema |
| DELETE\_TABLE\_STATS Procedure | Deletes table-related statistics |
| DIFF\_TABLE\_STATS\_IN\_HISTORY Function | Compares statistics for a table from two timestamps in past and compare the statistics as of that timestamps |
| DIFF\_TABLE\_STATS\_IN\_PENDING Function | Compares pending statistics and statistics as of a timestamp or statistics from dictionary |
| DIFF\_TABLE\_STATS\_IN\_STATTAB Function | Compares statistics for a table from two different sources |
| DROP\_EXTENDED\_STATS Procedure | Drops the statistics entry that is created for the user specified extension |
| DROP\_STAT\_TABLE Procedure | Drops a user statistics table created by `CREATE_STAT_TABLE` |
| EXPORT\_COLUMN\_STATS Procedure | Retrieves statistics for a particular column and stores them in the user statistics table identified by `stattab` |
| EXPORT\_DATABASE\_PREFS Procedure | Exports the statistics preferences of all the tables, excluding the tables owned by Oracle |
| EXPORT\_DATABASE\_STATS Procedure | Retrieves statistics for all objects in the database and stores them in the user statistics table identified by `statown`.`stattab` |
| EXPORT\_DICTIONARY\_STATS Procedure | Retrieves statistics for all dictionary schemas (' `SYS` ', ' `SYSTEM` ' and RDBMS component schemas) and stores them in the user statistics table identified by `stattab` |
| EXPORT\_FIXED\_OBJECTS\_STATS Procedure | Retrieves statistics for fixed tables and stores them in the user statistics table identified by `stattab` |
| EXPORT\_INDEX\_STATS Procedure | Retrieves statistics for a particular index and stores them in the user statistics table identified by `stattab` |
| EXPORT\_PENDING\_STATS Procedure | Exports the statistics gathered and stored as pending |
| EXPORT\_SCHEMA\_PREFS Procedure | Exports the statistics preferences of all the tables owned by the specified owner name |
| EXPORT\_SCHEMA\_STATS Procedure | Retrieves statistics for all objects in the schema identified by ownname and stores them in the user statistics table identified by `stattab` |
| EXPORT\_SYSTEM\_STATS Procedure | Retrieves system statistics and stores them in the user statistics table |
| EXPORT\_TABLE\_PREFS Procedure | Exports statistics preferences of the specified table in the specified schema into the specified statistics table |
| EXPORT\_TABLE\_STATS Procedure | Retrieves statistics for a particular table and stores them in the user statistics table |
| FLUSH\_DATABASE\_MONITORING\_INFO Procedure | Flushes in-memory monitoring information for all the tables to the dictionary |
| GATHER\_DATABASE\_STATS Procedures | Gathers statistics for all objects in the database |
| GATHER\_DICTIONARY\_STATS Procedure | Gathers statistics for dictionary schemas ' `SYS` ', ' `SYSTEM` ' and schemas of RDBMS components |
| GATHER\_FIXED\_OBJECTS\_STATS Procedure | Gathers statistics of fixed objects |
| GATHER\_INDEX\_STATS Procedure | Gathers index statistics |
| GATHER\_SCHEMA\_STATS Procedures | Gathers statistics for all objects in a schema |
| GATHER\_SYSTEM\_STATS Procedure | Gathers system statistics |
| GATHER\_TABLE\_STATS Procedure | Gathers table and column (and index) statistics |
| GENERATE\_STATS Procedure | Generates object statistics from previously collected statistics of related objects |
| GET\_COLUMN\_STATS Procedures | Gets all column-related information |
| GET\_INDEX\_STATS Procedures | Gets all index-related information |
| GET\_PARAM Function | Gets the default value of parameters of `DBMS_STATS` procedures \see [Deprecated Subprograms \] |
| GET\_PREFS Function | Gets the default value of the specified preference |
| GET\_STATS\_HISTORY\_AVAILABILITY Function | Gets the oldest timestamp where statistics history is available |
| GET\_STATS\_HISTORY\_RETENTION Function | Returns the current retention value |
| GET\_SYSTEM\_STATS Procedure | Gets system statistics from stattab, or from the dictionary if stattab is `NULL` |
| GET\_TABLE\_STATS Procedure | Gets all table-related information |
| IMPORT\_COLUMN\_STATS Procedure | Retrieves statistics for a particular column from the user statistics table identified by `stattab` and stores them in the dictionary |
| IMPORT\_DATABASE\_PREFS Procedure | Imports the statistics preferences of all the tables, excluding the tables owned by Oracle |
| IMPORT\_DATABASE\_STATS Procedure | Retrieves statistics for all objects in the database from the user statistics table and stores them in the dictionary |
| IMPORT\_DICTIONARY\_STATS Procedure | Retrieves statistics for all dictionary schemas (' `SYS` ', ' `SYSTEM` ' and RDBMS component schemas) from the user statistics table and stores them in the dictionary |
| IMPORT\_FIXED\_OBJECTS\_STATS Procedure | Retrieves statistics for fixed tables from the user statistics table identified by `stattab` and stores them in the dictionary |
| IMPORT\_INDEX\_STATS Procedure | Retrieves statistics for a particular index from the user statistics table identified by `stattab` and stores them in the dictionary |
| IMPORT\_SCHEMA\_PREFS Procedure | Imports the statistics preferences of all the tables owned by the specified owner name |
| IMPORT\_SCHEMA\_STATS Procedure | Retrieves statistics for all objects in the schema identified by `ownname` from the user statistics table and stores them in the dictionary |
| IMPORT\_SYSTEM\_STATS Procedure | Retrieves system statistics from the user statistics table and stores them in the dictionary |
| IMPORT\_TABLE\_PREFS Procedure | Sets the statistics preferences of the specified table in the specified schema |
| IMPORT\_TABLE\_STATS Procedure | Retrieves statistics for a particular table from the user statistics table identified by `stattab` and stores them in the dictionary |
| LOCK\_PARTITION\_STATS Procedure | Locks statistics for a partition |
| LOCK\_SCHEMA\_STATS Procedure | Locks the statistics of all tables of a schema |
| LOCK\_TABLE\_STATS Procedure | Locks the statistics on the table |
| MERGE\_COL\_USAGE Procedure | Merges column usage information from a source database, by means of a dblink, into the local database |
| PREPARE\_COLUMN\_VALUES Procedures | Converts user-specified minimum, maximum, and histogram endpoint datatype-specific values into Oracle's internal representation for future storage using the SEED\_COL\_USAGE Procedure |
| PREPARE\_COLUMN\_VALUES\_NVARCHAR2 Procedure | Converts user-specified minimum, maximum, and histogram endpoint datatype-specific values into Oracle's internal representation for future storage using the SEED\_COL\_USAGE Procedure |
| PREPARE\_COLUMN\_VALUES\_ROWID Procedure | Converts user-specified minimum, maximum, and histogram endpoint datatype-specific values into Oracle's internal representation for future storage using the SEED\_COL\_USAGE Procedure |
| PUBLISH\_PENDING\_STATS Procedure | Publishes the statistics gathered and stored as pending |
| PURGE\_STATS Procedure | Purges old versions of statistics saved in the dictionary |
| REPORT\_COL\_USAGE Function | Reports the recorded column (group) usage information |
| RESET\_GLOBAL\_PREF\_DEFAULTS Procedure | Resets the default values of all parameters to Oracle recommended values |
| RESET\_PARAM\_DEFAULTS Procedure | Resets global preferences to default values \see [Deprecated Subprograms \] |
| RESTORE\_DICTIONARY\_STATS Procedure | Restores statistics of all dictionary tables (tables of ' `SYS` ', ' `SYSTEM` ' and RDBMS component schemas) as of a specified timestamp |
| RESTORE\_FIXED\_OBJECTS\_STATS Procedure | Restores statistics of all fixed tables as of a specified timestamp |
| RESTORE\_SCHEMA\_STATS Procedure | Restores statistics of all tables of a schema as of a specified timestamp |
| RESTORE\_SYSTEM\_STATS Procedure | Restores statistics of all tables of a schema as of a specified timestamp |
| RESTORE\_TABLE\_STATS Procedure | Restores statistics of a table as of a specified timestamp (as\_of\_timestamp), as well as statistics of associated indexes and columns |
| SEED\_COL\_USAGE Procedure | Iterates over the SQL statements in the specified SQL tuning set, compiles them and seeds column usage information for the columns that appear in these statements |
| SET\_COLUMN\_STATS Procedures | Sets column-related information |
| SET\_DATABASE\_PREFS Procedure | Sets the statistics preferences of all the tables, excluding the tables owned by Oracle |
| SET\_GLOBAL\_PREFS Procedure | Sets the global statistics preferences |
| SET\_INDEX\_STATS Procedures | Sets index-related information |
| SET\_PARAM Procedure | Sets default values for parameters of `DBMS_STATS` procedures \see [Deprecated Subprograms \] |
| SET\_SCHEMA\_PREFS Procedure | Sets the statistics preferences of all the tables owned by the specified owner name |
| SET\_SYSTEM\_STATS Procedure | Sets system statistics |
| SET\_TABLE\_PREFS Procedure | Sets the statistics preferences of the specified table in the specified schema |
| SET\_TABLE\_STATS Procedure | Sets table-related information |
| SHOW\_EXTENDED\_STATS\_NAME Function | Returns the name of the virtual column that is created for the user-specified extension |
| UNLOCK\_PARTITION\_STATS Procedure | Unlocks the statistics for a partition |
| UNLOCK\_SCHEMA\_STATS Procedure | Unlocks the statistics on all the table in a schema |
| UNLOCK\_TABLE\_STATS Procedure | Unlocks the statistics on the table |
| UPGRADE\_STAT\_TABLE Procedure | Upgrades user statistics on an older table |

---

### ALTER\_STATS\_HISTORY\_RETENTION Procedure

This procedure changes the statistics history retention value. Statistics history retention is used by both the automatic purge and PURGE\_STATS Procedure.

Syntax

```
DBMS_STATS.ALTER_STATS_HISTORY_RETENTION (
   retention       IN     NUMBER);
```

Parameters

Table 142-3 ALTER\_STATS\_HISTORY\_RETENTION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `retention` | The retention time in days. The statistics history will be retained for at least these many number of days.The valid range is \[1,365000\]. Also you can use the following values for special purposes:  - \-1:Statistics history is never purged by automatic purge - 0: Old statistics are never saved. The automatic purge will delete all statistics history - `NULL`: Change statistics history retention to default value |

Usage Notes

To run this procedure, you must have the `SYSDBA` or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privilege.

Exceptions

`ORA-20000`: Insufficient privileges

---

### CONVERT\_RAW\_VALUE Procedures

This procedure converts the internal representation of a minimum or maximum value into a datatype-specific value. The minval and maxval fields of the `StatRec` structure as filled in by `GET_COLUMN_STATS` or `PREPARE_COLUMN_VALUES` are appropriate values for input.

Syntax

```
DBMS_STATS.CONVERT_RAW_VALUE (
   rawval     RAW, 
   resval OUT BINARY_FLOAT);

DBMS_STATS.CONVERT_RAW_VALUE (
   rawval     RAW, 
   resval OUT BINARY_DOUBLE);

DBMS_STATS.CONVERT_RAW_VALUE (
   rawval     RAW, 
   resval OUT DATE);

DBMS_STATS.CONVERT_RAW_VALUE (
   rawval     RAW, 
   resval OUT NUMBER);

DBMS_STATS.CONVERT_RAW_VALUE (
   rawval     RAW, 
   resval OUT VARCHAR2);
```

Pragmas

```
pragma restrict_references(convert_raw_value, WNDS, RNDS, WNPS, RNPS);
```

Parameters

Table 142-4 CONVERT\_RAW\_VALUE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rawval` | The raw representation of a column minimum or maximum datatype-specific output parameters |
| `resval` | The converted, type-specific value |

Usage Notes

No special privilege or role is needed to invoke this procedure.

---

### CONVERT\_RAW\_VALUE\_NVARCHAR Procedure

This procedure converts the internal representation of a minimum or maximum value into a datatype-specific value. The minval and maxval fields of the `StatRec` structure as filled in by `GET_COLUMN_STATS` or `PREPARE_COLUMN_VALUES` are appropriate values for input.

Syntax

```
DBMS_STATS.CONVERT_RAW_VALUE_NVARCHAR (
   rawval     RAW, 
   resval OUT NVARCHAR2);
```

Pragmas

```
pragma restrict_references(convert_raw_value_nvarchar, WNDS, RNDS, WNPS, RNPS);
```

Parameters

Table 142-5 CONVERT\_RAW\_VALUE\_NVARCHAR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rawval` | The raw representation of a column minimum or maximum datatype-specific output parameters |
| `resval` | The converted, type-specific value |

Usage Notes

No special privilege or role is needed to invoke this procedure.

---

### CONVERT\_RAW\_VALUE\_ROWID Procedure

This procedure converts the internal representation of a minimum or maximum value into a datatype-specific value. The minval and maxval fields of the `StatRec` structure as filled in by `GET_COLUMN_STATS` or `PREPARE_COLUMN_VALUES` are appropriate values for input.

Syntax

```
DBMS_STATS.CONVERT_RAW_VALUE_ROWID (
   rawval     RAW, 
   resval OUT ROWID);
```

Pragmas

```
pragma restrict_references(convert_raw_value_rowid, WNDS, RNDS, WNPS, RNPS);
```

Parameters

Table 142-6 CONVERT\_RAW\_VALUE\_ROWID Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rawval` | The raw representation of a column minimum or maximum datatype-specific output parameters |
| `resval` | The converted, type-specific value |

Usage Notes

No special privilege or role is needed to invoke this procedure.

---

### COPY\_TABLE\_STATS Procedure

This procedure copies the statistics of the source \[sub\] partition to the destination \[sub\] partition.It also copies statistics of all dependent object such as columns and local indexes. If the statistics forsource are not available then nothing is copied. It can optionally scale the statistics (such as the number of blks, or number of rows) based on the given `scale_factor`.

Syntax

```
DBMS_STATS.COPY_TABLE_STATS (
   ownname          VARCHAR2, 
   tabname          VARCHAR2, 
   srcpartname      VARCHAR2,
   dstpartname      VARCHAR2, 
   scale_factor     VARCHAR2 DEFAULT 1,
   flags            NUMBER DEFAULT,
   force            BOOLEAN DEFAULT FALSE);
```

Parameters

Table 142-7 COPY\_TABLE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Schema of the table of source and destination \[sub\] partitions |
| `tabname` | Table name of source and destination \[sub\] partitions |
| `srcpartname` | Source \[sub\] partition |
| `dtspartname` | Destination \[sub\] partition |
| `scale_factor` | Scale factor to scale `nblks`, `nrows` etc. in `dstpartname` |
| `flags` | For internal Oracle use (should be left as `NULL`) |
| `force` | When value of this argument is `TRUE`, copy statistics even if locked |

Exceptions

`ORA-20000`: Invalid partition name

`ORA-20001`: Bad input value

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

This procedure updates the minimum and maximum values of destination partition for the first partitioning column as follows:

- If the partitioning type is `HASH` the minimum and maximum values of the destination partition are same as that of the source partition.
- If the partitioning type is `LIST` then
	- if the destination partition is a `NOT` `DEFAULT` paritition then
		- the minimum value of the destination partition is set to the minimum value of the value list that describes the destination partition
				- the maximum value of the destination partition is set to the maximum value of the value list that describes the destination partition
		- alternatively, if the destination partition is a `DEFAULT` paritition, then
		- the minimum value of the destination partition is set to the minimum value of the source partition
				- the maximum value of the destination partition is set to the maximum value of the source partition
- If the partitioning type is `RANGE` then
	- the minimum value of the destination partition is set to the high bound of previous partition
		- the maximum value of the destination partition is set to the high bound of the destination partition unless the high bound of the destination partition is `MAXVALUE`, in which case the maximum value of the destination partition is set to the high bound of the previous partition

Note that if the destination partition is the first partition then minimum values are equal to maximum values.

The procedure is is extended to handle the second and subsequent key columns with two additional rules (which do not apply to the first key column):

- If the source partition column's minimum value is equal to its maximum value, and both are equal to the source partition's lower bound, and it has a single distinct value, then the destination partition column's minimum and maximum values are both set to the destination partition's lower bound.
- IIf the above condition does not apply, the destination partition column's maximum value is set to the greater of the destination partition upper bound and the source partition column's maximum value, with the following exception: if the destination partition is D and its preceding partition is D-1 and the key column to be adjusted is Cn, the maximum value for Cn is set to the upper bound of D (ignoring the maximum value of the source partition column) provided that the upper bounds of the previous key column Cn-1 are the same in partitions D and D-1.

---

### CREATE\_EXTENDED\_STATS Function

This function creates a column statistics entry in the system for a user specified column group or an expression in a table. Statistics for this extension will be gathered when user or auto statistics gathering job gathers statistics for the table. We call statistics for such an extension, "extended statistics". This function returns the name of this newly created entry for the extension.

Syntax

```
DBMS_STATS.CREATE_EXTENDED_STATS (
   ownname    VARCHAR2, 
   tabname    VARCHAR2,
   extension  VARCHAR2)
 RETURN VARCHAR2;
```

Parameters

Table 142-8 CREATE\_EXTENDED\_STATS Function Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name of a table |
| `tabname` | Name of the table |
| `extension` | Can be either a column group or an expression. Suppose the specified table has two column `c1`, `c2`. An example column group can be "(`c1`, `c2`)" and an example expression can be "(`c1` + `c2`)". |

Return Values

This function returns the name of this newly created entry for the extension.

Exceptions

`ORA-20000`: Insufficient privileges / creating extension is not supported

`ORA-20001`: Error when processing extension

`ORA-20007`: Extension already exists

`ORA-20008`: Reached the upper limit on number of extensions

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

There are nine restrictions on the extension:

- The extension cannot contain a virtual column.
- Extensions cannot be created on tables owned by `SYS.`
- Extensions cannot be created on cluster tables, index organized tables, temporary tables or external tables.
- The total number of extensions in a table cannot be greater than a maximum of (20, 10% of number of non-virtual columns in the table).
- The number of columns in a column group must be in the range \[2, 32\].
- A column can not appear more than once in a column group.
- A column group can not contain expressions.
- An expression must contain at least one column.
- An expression can not contain a subquery.
- The `COMPATIBLE` parameter needs to be 11.0.0.0.0 or greater

---

### CREATE\_STAT\_TABLE Procedure

This procedure creates a table with name `stattab` in `ownname` 's schema which is capable of holding statistics. The columns and types that compose this table are not relevant as it should be accessed solely through the procedures in this package.

Syntax

```
DBMS_STATS.CREATE_STAT_TABLE (
   ownname  VARCHAR2, 
   stattab  VARCHAR2,
   tblspace VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-9 CREATE\_STAT\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `stattab` | Name of the table to create. This value should be passed as the `stattab` parameter to other procedures when the user does not want to modify the dictionary statistics directly. |
| `tblspace` | Tablespace in which to create the statistics tables. If none is specified, then they are created in the user's default tablespace. |

Exceptions

`ORA-20000`: Table already exists or insufficient privileges

`ORA-20001`: Tablespace does not exist

Usage Notes

To invoke this procedure you need whichever privileges are required for creating a table in the specified schema.

---

### DELETE\_COLUMN\_STATS Procedure

This procedure deletes column-related statistics.

Syntax

```
DBMS_STATS.DELETE_COLUMN_STATS (
   ownname        VARCHAR2, 
   tabname        VARCHAR2, 
   colname        VARCHAR2, 
   partname       VARCHAR2 DEFAULT NULL,
   stattab        VARCHAR2 DEFAULT NULL, 
   statid         VARCHAR2 DEFAULT NULL,
   cascade_parts  BOOLEAN  DEFAULT TRUE,
   statown        VARCHAR2 DEFAULT NULL,
   no_invalidate  BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   force          BOOLEAN  DEFAULT FALSE,
   col_stat_type  VARCHAR2 DEFAULT 'ALL');
```

Parameters

Table 142-10 DELETE\_COLUMN\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `tabname` | Name of the table to which this column belongs |
| `colname` | Name of the column or extension |
| `partname` | Name of the table partition for which to delete the statistics. If the table is partitioned and if `partname` is `NULL`, then global column statistics are deleted. |
| `stattab` | User statistics table identifier describing from where to delete the statistics. If `stattab` is `NULL`, then the statistics are deleted directly from the dictionary. |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` (Only pertinent if `stattab` is not `NULL`). |
| `cascade_parts` | If the table is partitioned and if `partname` is `NULL`, then setting this to true causes the deletion of statistics for this column for all underlying partitions as well. |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `force` | When value of this argument is `TRUE`, deletes column statistics even if locked |
| `col_stat_type` | Type of column statistics to be deleted.This argument takes the following values:  - `HISTOGRAM` - delete column histogram only - `ALL` - delete base column statistics and histogram |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20005`: Object statistics are locked

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

---

### DELETE\_DATABASE\_PREFS Procedure

This procedure is used to delete the statistics preferences of all the tables, excluding the tables owned by Oracle. These tables can by included by passing `TRUE` for the `add_sys` parameter.

Syntax

```
DBMS_STATS.DELETE_DATABASE_PREFS (
    pname            IN   VARCHAR2,
    add_sys          IN   BOOLEAN DEFAULT FALSE);
```

Parameters

Table 142-11 DELETE\_DATABASE\_PREFS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pname` | Preference name. The default value for following parameters can be deleted:  - `CASCADE` - `DEGREE` - `ESTIMATE_PERCENT` - `METHOD_OPT` - `NO_INVALIDATE` - `GRANULARITY` - `PUBLISH` - `INCREMENTAL` - `STALE_PERCENT` |
| . | `CASCADE` - The value determines whether or not index statistics are collected as part of gathering table statistics |
| . | `DEGREE` - The value determines degree of parallelism used for gathering statistics |
| . | `ESTIMATE_PERCENT` - The value determines the percentage of rows to estimate. The valid range is \[0.000001,100\]. Use the constant `DBMS_STATS`.`AUTO_SAMPLE_SIZE` to have Oracle determine the appropriate sample size for good statistics. This is the default. |
| . | `METHOD_OPT` - The value controls column statistics collection and histogram creation. It accepts either of the following options, or both in combination:  - `FOR ALL [INDEXED \| HIDDEN] COLUMNS` `[size_clause]` - `FOR COLUMNS [size clause] column [size_clause] [,column [size_clause]...]`  `size_clause` is defined as `size_clause := SIZE {integer \| REPEAT \| AUTO \| SKEWONLY}`  `column` is defined as `column := column_name \| extension name \| extension`     `- integer`: Number of histogram buckets. Must be in the range \[1,254\].   `- REPEAT`: Collects histograms only on the columns that already have histograms   `- AUTO`: Oracle determines the columns on which to collect histograms based on data distribution and the workload of the columns   `- SKEWONLY`: Oracle determines the columns on which to collect histograms based on the data distribution of the columns   \- `column_name`: name of a column   \- `extension :` can be either a column group in the format of `(column_name, colume_name [, ...])` or an expression  The default is `FOR ALL COLUMNS SIZE AUTO`. |
| . | `NO_INVALIDATE` - The value controls the invalidation of dependent cursors of the tables for which statistics are being gathered. Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE` to have Oracle decide when to invalidate dependent cursors. This is the default. |
| . | `GRANULARITY` - The value determines granularity of statistics to collect (only pertinent if the table is partitioned)  `'ALL'` - gathers all (subpartition, partition, and global) statistics  `'AUTO'` - determines the granularity based on the partitioning type. This is the default value.  `'DEFAULT'` - gathers global and partition-level statistics. This option is obsolete, and while currently supported, it is included in the documentation for legacy reasons only. You should use the ' `GLOBAL AND PARTITION` ' for this functionality. Note that the default value is now ' `AUTO` '.  `'GLOBAL'` - gathers global statistics  ' `GLOBAL AND PARTITION` ' - gathers the global and partition level statistics. No subpartition level statistics are gathered even if it is a composite partitioned object.  `'PARTITION` '- gathers partition-level statistics  `'SUBPARTITION'` - gathers subpartition-level statistics |
| . | `PUBLISH` - This value determines whether or not newly gathered statistics will be published once the gather job has completed. Prior to Oracle Database 11g, Release 1 (11.1), once a statistic gathering job completed the new statistics were automatically published into the dictionary tables. The user now has the ability to gather statistics but not publish them immediately. This allows the DBA to test the new statistics before publishing them. |
| . | `INCREMENTAL` - This value determines whether or not the global statistics of a partitioned table will be maintained without doing a full table scan. With partitioned tables it is very common to load new data into a new partition. As new partitions are added and data loaded, the global table statistics need to be kept up to date. Oracle will update the global table statistics by scanning only the partitions that have been changed instead of the entire table if the following conditions hold:  - the `INCREMENTAL` value for the partitioned table is set to `TRUE`; - the `PUBLISH` value for the partitioned table is set to `TRUE`; - the user specifies `AUTO_SAMPLE_SIZE` for `ESTIMATE_PERCENT` and `AUTO` for `GRANULARITY` when gathering statistics on the table.  If the `INCREMENTAL` value for the partitioned table was set to `FALSE` (default value), a full table scan is used to maintain the global statistics which is a much more resource intensive and time-consuming operation for large tables. |
| . | `STALE_PERCENT` - Determines the percentage of rows in a table that have to change before the statistics on that table are deemed stale and should be regathered. The valid domain for `stale_percent` is non-negative numbers.The default value is 10%. Note that if you set `stale_percent` to zero the `AUTO` `STATS` gathering job will gather statistics for this table every time a row in the table is modified. |
| `add_sys` | Value `TRUE` will include the Oracle-owned tables |

Exceptions

`ORA-20000`: Insufficient privileges

`ORA-20001`: Invalid or Illegal input values

Usage Notes

- To run this procedure, you need to have the `SYSDBA` role or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privileges.
- All `pname` arguments are of type `VARCHAR2` and values are enclosed in quotes, even when they represent numbers.

Examples

```
DBMS_STATS.DELETE_DATABASE_PREFS('CASCADE', FALSE);
DBMS_STATS.DELETE_DATABASE_PREFS('ESTIMATE_PERCENT',TRUE);
```

---

### DELETE\_DATABASE\_STATS Procedure

This procedure deletes statistics for all the tables in a database.

Syntax

```
DBMS_STATS.DELETE_DATABASE_STATS (
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   statown          VARCHAR2 DEFAULT NULL,
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   force            BOOLEAN  DEFAULT FALSE);
```

Parameters

Table 142-12 DELETE\_DATABASE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | User statistics table identifier describing from where to delete the statistics. If `stattab` is `NULL`, then the statistics are deleted directly in the dictionary. |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` (Only pertinent if `stattab` is not `NULL`) |
| `statown` | Schema containing `stattab` (if different from current schema) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `force` | When the value of this argument is `TRUE`, deletes statistics of tables in a database even if they are locked |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

Usage Notes

To run this procedure, you need to have the `SYSDBA` role or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privileges.

---

### DELETE\_DICTIONARY\_STATS Procedure

This procedure deletes statistics for all dictionary schemas (' `SYS` ', ' `SYSTEM` ' and RDBMS component schemas).

Syntax

```
DBMS_STATS.DELETE_DICTIONARY_STATS (
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   statown          VARCHAR2 DEFAULT NULL,
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   force            BOOLEAN  DEFAULT FALSE);
```

Parameters

Table 142-13 DELETE\_DICTIONARY\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | User statistics table identifier describing from where to delete the statistics. If `stattab` is `NULL`, then the statistics are deleted directly in the dictionary. |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` (Only pertinent if `stattab` is not `NULL`) |
| `statown` | Schema containing `stattab` (if different from current schema) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure |
| `force` | When the value of this argument is `TRUE`, deletes statistics of tables in a database even if they are locked |

Usage Notes

You must have the `SYSDBA` or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privilege to execute this procedure.

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20002`: Bad user statistics table, may need to upgrade it

---

### DELETE\_FIXED\_OBJECTS\_STATS Procedure

This procedure deletes statistics of all fixed tables.

Syntax

```
DBMS_STATS.DELETE_FIXED_OBJECTS_STATS (
   stattab        VARCHAR2 DEFAULT NULL,
   statid         VARCHAR2 DEFAULT NULL,
   statown        VARCHAR2 DEFAULT NULL, 
   no_invalidate  BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   force          BOOLEAN  DEFAULT FALSE);
```

Parameters

Table 142-14 DELETE\_FIXED\_OBJECTS\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | The user statistics table identifier describing from where to delete the current statistics. If `stattab` is `NULL`, the statistics will be deleted directly in the dictionary. |
| `statid` | The (optional) identifier to associate with these statistics within stattab. This only applies if `stattab` is not `NULL`. |
| `statown` | Schema containing `stattab` (if different from current schema) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure |
| `force` | Ignores the statistics lock on objects and deletes the statistics if set to `TRUE` |

Usage Notes

You must have the `SYSDBA` or `ANALYZE` `ANY` `DICTIONARY` system privilege to execute this procedure.

Exceptions

`ORA-20000`: Insufficient privileges

`ORA-20002`: Bad user statistics table, may need to upgrade it

---

### DELETE\_INDEX\_STATS Procedure

This procedure deletes index-related statistics.

Syntax

```
DBMS_STATS.DELETE_INDEX_STATS (
   ownname          VARCHAR2, 
   indname          VARCHAR2,
   partname         VARCHAR2 DEFAULT NULL,
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   cascade_parts    BOOLEAN  DEFAULT TRUE,
   statown          VARCHAR2 DEFAULT NULL,
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   force            BOOLEAN DEFAULT FALSE);
```

Parameters

Table 142-15 DELETE\_INDEX\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `indname` | Name of the index |
| `partname` | Name of the index partition for which to delete the statistics. If the index is partitioned and if `partname` is `NULL`, then index statistics are deleted at the global level. |
| `stattab` | User statistics table identifier describing from where to delete the statistics. If `stattab` is `NULL`, then the statistics are deleted directly from the dictionary. |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` (Only pertinent if `stattab` is not `NULL`) |
| `cascade_parts` | If the index is partitioned and if `partname` is `NULL`, then setting this to `TRUE` causes the deletion of statistics for this index for all underlying partitions as well |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `force` | When value of this argument is `TRUE`, deletes index statistics even if locked |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20005`: Object statistics are locked

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

---

### DELETE\_PENDING\_STATS Procedure

This procedure is used to delete the pending statistics that have been collected but have not been published.

Syntax

```
DBMS_STATS.DELETE_PENDING_STATS (
    ownname    IN  VARCHAR2  DEFAULT USER,
    tabname    IN  VARCHAR2);
```

Parameters

Table 142-16 DELETE\_PENDING\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name |
| `tabname` | Table name |

Exceptions

`ORA-20000`: Insufficient privileges

Usage Notes

- If the parameter `tabname` is `NULL` delete applies to all tables of the specified schema.
- The default owner/schema is the user who runs the procedure.
- To run this procedure, you need to have the same privilege for gathering statistics on the tables that will be touched by this procedure.

Examples

```
DBMS_STATS.DELETE_PENDING_STATS('SH', 'SALES');
```

---

### DELETE\_SCHEMA\_PREFS Procedure

This procedure is used to delete the statistics preferences of all the tables owned by the specified owner name.

Syntax

```
DBMS_STATS.DELETE_SCHEMA_PREFS (
    ownname   IN   VARCHAR2,
    pname     IN   VARCHAR2);
```

Parameters

Table 142-17 DELETE\_SCHEMA\_PREFS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name |
| `pname` | Preference name. The default value for following parameters can be deleted:  - `CASCADE` - `DEGREE` - `ESTIMATE_PERCENT` - `METHOD_OPT` - `NO_INVALIDATE` - `GRANULARITY` - `PUBLISH` - `INCREMENTAL` - `STALE_PERCENT` |
| . | `CASCADE` - Determines whether or not index statistics are collected as part of gathering table statistics |
| . | `DEGREE` - Determines degree of parallelism used for gathering statistics |
| . | `ESTIMATE_PERCENT` - Determines the percentage of rows to estimate. The valid range is \[0.000001,100\]. Use the constant `DBMS_STATS`.`AUTO_SAMPLE_SIZE` to have Oracle determine the appropriate sample size for good statistics. This is the default. |
| . | `METHOD_OPT` - Controls column statistics collection and histogram creation. It accepts either of the following options, or both in combination:  - `FOR ALL [INDEXED \| HIDDEN] COLUMNS` `[size_clause]` - `FOR COLUMNS [size clause] column [size_clause] [,column [size_clause]...]`  `size_clause` is defined as `size_clause := SIZE {integer \| REPEAT \| AUTO \| SKEWONLY}`  `column` is defined as `column := column_name \| extension name \| extension`     `- integer`: Number of histogram buckets. Must be in the range \[1,254\].   `- REPEAT`: Collects histograms only on the columns that already have histograms   `- AUTO`: Oracle determines the columns on which to collect histograms based on data distribution and the workload of the columns.   `- SKEWONLY`: Oracle determines the columns on which to collect histograms based on the data distribution of the columns   \- `column_name`: name of a column   \- `extension:` can be either a column group in the format of `(column_name, colume_name [, ...])` or an expression  The default is `FOR ALL COLUMNS SIZE AUTO`. |
| . | `NO_INVALIDATE` - Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| . | `GRANULARITY` - The value determines granularity of statistics to collect (only pertinent if the table is partitioned).  `'ALL'` - gathers all (subpartition, partition, and global) statistics  `'AUTO'` - determines the granularity based on the partitioning type. This is the default value.  `'DEFAULT'` - gathers global and partition-level statistics. This option is obsolete, and while currently supported, it is included in the documentation for legacy reasons only. You should use the ' `GLOBAL AND PARTITION` ' for this functionality. Note that the default value is now ' `AUTO` '.  `'GLOBAL'` - gathers global statistics  ' `GLOBAL AND PARTITION` ' - gathers the global and partition level statistics. No subpartition level statistics are gathered even if it is a composite partitioned object.  `'PARTITION` '- gathers partition-level statistics  `'SUBPARTITION'` - gathers subpartition-level statistics. |
| . | `PUBLISH` - This value determines whether or not newly gathered statistics will be published once the gather job has completed. Prior to Oracle Database 11g, Release 1 (11.1), once a statistic gathering job completed the new statistics were automatically published into the dictionary tables. The user now has the ability to gather statistics but not publish them immediately. This allows the DBA to test the new statistics before publishing them. |
| . | `INCREMENTAL` - This value determines whether or not the global statistics of a partitioned table will be maintained without doing a full table scan. With partitioned tables it is very common to load new data into a new partition. As new partitions are added and data loaded, the global table statistics need to be kept up to date. Oracle will update the global table statistics by scanning only the partitions that have been changed instead of the entire table if the following conditions hold:  - the `INCREMENTAL` value for the partitioned table is set to `TRUE` - the `PUBLISH` value for the partitioned table is set to `TRUE` - the user specifies `AUTO_SAMPLE_SIZE` for `ESTIMATE_PERCENT` and `AUTO` for `GRANULARITY` when gathering statistics on the table  If the `INCREMENTAL` value for the partitioned table was set to `FALSE` (default value), a full table scan is used to maintain the global statistics which is a much more resource intensive and time-consuming operation for large tables. |
| . | `STALE_PERCENT` - Determines the percentage of rows in a table that have to change before the statistics on that table are deemed stale and should be regathered. The valid domain for `stale_percent` is non-negative numbers.The default value is 10%. Note that if you set `stale_percent` to zero the `AUTO` `STATS` gathering job will gather statistics for this table every time a row in the table is modified. |

Exceptions

`ORA-20000`: Insufficient privileges / Schema "\<schema>" does not exist

`ORA-20001`: Invalid or Illegal input values

Usage Notes

- To run this procedure, you need to connect as owner, or have the `SYSDBA` privilege, or have the `ANALYZE` `ANY` system privilege.
- All arguments are of type `VARCHAR2` and values are enclosed in quotes, even when they represent numbers.

Examples

```
DBMS_STATS.DELETE_SCHEMA_PREFS('SH', 'CASCADE');
DBMS_STATS.DELETE_SCHEMA_PREFS('SH', 'ESTIMATE_PERCENT');
DBMS_STATS.DELETE_SCHEMA_PREFS('SH', 'DEGREE');
```

---

### DELETE\_SCHEMA\_STATS Procedure

This procedure deletes statistics for an entire schema.

Syntax

```
DBMS_STATS.DELETE_SCHEMA_STATS (
   ownname          VARCHAR2, 
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   statown          VARCHAR2 DEFAULT NULL,
   no_invalidate    BOOLEAN DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   force            BOOLEAN DEFAULT FALSE);
```

Parameters

Table 142-18 DELETE\_SCHEMA\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `stattab` | User statistics table identifier describing from where to delete the statistics. If `stattab` is `NULL`, then the statistics are deleted directly in the dictionary. |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` (Only pertinent if `stattab` is not `NULL`) |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `force` | When value of this argument is `TRUE`, deletes statistics of tables in a schema even if locked |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

---

### DELETE\_SYSTEM\_STATS Procedure

This procedure deletes workload statistics (collected using the ' `INTERVAL` ' or ' `START` ' and ' `STOP` ' options) and resets the default to `noworkload` statistics (collected using ' `NOWORKLOAD` ' option) if `stattab` is not specified. If `stattab` is specified, the subprogram deletes all system statistics with the associated `statid` from the `stattab`.

Syntax

```
DBMS_STATS.DELETE_SYSTEM_STATS (
   stattab       VARCHAR2 DEFAULT NULL, 
   statid        VARCHAR2 DEFAULT NULL,
   statown       VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-19 DELETE\_SYSTEM\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | Identifier of the user statistics table where the statistics will be saved |
| `statid` | Optional identifier associated with the statistics saved in the stattab |
| `statown` | Schema containing `stattab` (if different from current schema) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20002`: Bad user statistics table; may need to be upgraded

Usage Notes

To invoke this procedure you need the `GATHER_SYSTEM_STATISTICS` role.

---

### DELETE\_TABLE\_PREFS Procedure

This procedure is used to delete the statistics preferences of the specified table in the specified schema.

Syntax

```
DBMS_STATS.DELETE_TABLE_PREFS (
    ownname    IN  VARCHAR2,
    tabname    IN  VARCHAR2,
    pname      IN  VARCHAR2);
```

Parameters

Table 142-20 DELETE\_TABLE\_PREFS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name |
| `tabname` | Table name |
| `pname` | Preference name. The default value for following preferences can be deleted:  - `CASCADE` - `DEGREE` - `ESTIMATE_PERCENT` - `METHOD_OPT` - `NO_INVALIDATE` - `GRANULARITY` - `PUBLISH` - `INCREMENTAL` - `STALE_PERCENT` |
| . | `CASCADE` - Determines whether or not index statistics are collected as part of gathering table statistics |
| . | `DEGREE` - Determines degree of parallelism used for gathering statistics |
| . | `ESTIMATE_PERCENT` - Determines the percentage of rows to estimate. The valid range is \[0.000001,100\]. Use the constant `DBMS_STATS`.`AUTO_SAMPLE_SIZE` to have Oracle determine the appropriate sample size for good statistics. This is the default. |
| . | `METHOD_OPT` - The value controls column statistics collection and histogram creation. It accepts either of the following options, or both in combination:  - `FOR ALL [INDEXED \| HIDDEN] COLUMNS` `[size_clause]` - `FOR COLUMNS [size clause] column [size_clause] [,column [size_clause]...]`  `size_clause` is defined as `size_clause := SIZE {integer \| REPEAT \| AUTO \| SKEWONLY}`  `column` is defined as `column := column_name \| extension name \| extension`     `- integer`: Number of histogram buckets. Must be in the range \[1,254\].   `- REPEAT`: Collects histograms only on the columns that already have histograms.   `- AUTO`: Oracle determines the columns on which to collect histograms based on data distribution and the workload of the columns.   `- SKEWONLY`: Oracle determines the columns on which to collect histograms based on the data distribution of the columns.   \- `column_name`: name of a column   \- `extension :` can be either a column group in the format of `(column_name, colume_name [, ...])` or an expression  The default is `FOR ALL COLUMNS SIZE AUTO`. |
| . | `NO_INVALIDATE` - Controls the invalidation of dependent cursors of the tables for which statistics are being gathered. Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE` to have Oracle decide when to invalidate dependent cursors. This is the default. |
| . | `GRANULARITY` - Determines granularity of statistics to collect (only pertinent if the table is partitioned).  `'ALL'` - Gathers all (subpartition, partition, and global) statistics  `'AUTO'` - Determines the granularity based on the partitioning type. This is the default value.  `'DEFAULT'` - Gathers global and partition-level statistics. This option is obsolete, and while currently supported, it is included in the documentation for legacy reasons only. You should use the ' `GLOBAL AND PARTITION` ' for this functionality. Note that the default value is now ' `AUTO` '.  `'GLOBAL'` - Gathers global statistics  ' `GLOBAL AND PARTITION` ' - Gathers the global and partition level statistics. No subpartition level statistics are gathered even if it is a composite partitioned object.  `'PARTITION` '- Gathers partition-level statistics  `'SUBPARTITION'` - Gathers subpartition-level statistics. |
| . | `PUBLISH` - Determines whether or not newly gathered statistics will be published once the gather job has completed. Prior to Oracle Database 11g, Release 1 (11.1), once a statistic gathering job completed the new statistics were automatically published into the dictionary tables. The user now has the ability to gather statistics but not publish them immediately. This allows the DBA to test the new statistics before publishing them. |
| . | `INCREMENTAL` - Determines whether or not the global statistics of a partitioned table will be maintained without doing a full table scan. With partitioned tables it is very common to load new data into a new partition. As new partitions are added and data loaded, the global table statistics need to be kept up to date. Oracle will update the global table statistics by scanning only the partitions that have been changed instead of the entire table if the following conditions hold:  - `INCREMENTAL` value for the partitioned table is set to `TRUE` - `PUBLISH` value for the partitioned table is set to `TRUE`; - User specifies `AUTO_SAMPLE_SIZE` for `ESTIMATE_PERCENT` and `AUTO` for `GRANULARITY` when gathering statistics on the table.  If the `INCREMENTAL` value for the partitioned table was set to `FALSE` (default value), a full table scan is used to maintain the global statistics which is a much more resource intensive and time-consuming operation for large tables. |
| . | `STALE_PERCENT` - Determines the percentage of rows in a table that have to change before the statistics on that table are deemed stale and should be regathered. The valid domain for `stale_percent` is non-negative numbers. The default value is 10%. |
| pvalue | Preference value. If `NULL` is specified, it will set the Oracle default value. |

Exceptions

`ORA-20000`: Insufficient privileges

`ORA-20001`: Invalid or Illegal input values

Usage Notes

- To run this procedure, you need to connect as owner of the table, be granted `ANALYZE` privilege on the table, or `ANALYZE` `ANY` system privilege.
- All arguments are of type `VARCHAR2` and values are enclosed in quotes, even when they represent numbers.

Examples

```
DBMS_STATS.DELETE_TABLE_PREFS('SH', 'SALES', 'CASCADE');
DBMS_STATS.DELETE_TABLE_PREFS('SH', 'SALES', 'DEGREE');
```

---

### DELETE\_TABLE\_STATS Procedure

This procedure deletes table-related statistics.

Syntax

```
DBMS_STATS.DELETE_TABLE_STATS (
   ownname          VARCHAR2, 
   tabname          VARCHAR2, 
   partname         VARCHAR2 DEFAULT NULL,
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   cascade_parts    BOOLEAN  DEFAULT TRUE, 
   cascade_columns  BOOLEAN  DEFAULT TRUE,
   cascade_indexes  BOOLEAN  DEFAULT TRUE,
   statown          VARCHAR2 DEFAULT NULL,
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   force            BOOLEAN DEFAULT FALSE);
```

Parameters

Table 142-21 DELETE\_TABLE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `tabname` | Name of the table to which this column belongs |
| `partname` | Name of the table partition from which to get the statistics. If the table is partitioned and if `partname` is `NULL`, then the statistics are retrieved from the global table level. |
| `stattab` | User statistics table identifier describing from where to retrieve the statistics. If `stattab` is `NULL`, then the statistics are retrieved directly from the dictionary. |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` (Only pertinent if `stattab` is not `NULL`) |
| `cascade_parts` | If the table is partitioned and if `partname` is `NULL`, then setting this to `TRUE` causes the deletion of statistics for this table for all underlying partitions as well |
| `cascade_columns` | Indicates that `DELETE_COLUMN_STATS` should be called for all underlying columns (passing the `cascade_parts` parameter) |
| `cascade_indexes` | Indicates that `DELETE_INDEX_STATS` should be called for all underlying indexes (passing the `cascade_parts` parameter) |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `force` | When value of this argument is `TRUE`, deletes table statistics even if locked |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20002`: Bad user statistics table, may need to upgrade it

`ORA` - `20005`: Object statistics are locked

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

---

### DIFF\_TABLE\_STATS\_IN\_HISTORY Function

This function can be used to compare statistics for a table from two timestamps in past and compare the statistics as of that timestamps.

Syntax

```
DBMS_STATS.DIFF_TABLE_STATS_IN_HISTORY( 
      ownname        IN  VARCHAR2,
      tabname        IN  VARCHAR2,
      time1          IN  TIMESTAMP WITH TIME ZONE,
      time2          IN  TIMESTAMP WITH TIME ZONE DEFAULT NULL,
      pctthreshold   IN  NUMBER  DEFAULT 10)
   RETURN DiffRepTab pipelined;
```

Parameters

Table 142-22 DIFF\_TABLE\_STATS\_IN\_HISTORY Function Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner of the table. Specify `NULL` for current schema. |
| `tabname` | Table for which statistics are to be compared |
| `time1` | First timestamp 1 |
| `time2` | Second timestamp 2 |
| `pctthreshold` | The function reports difference in statistics only if it exceeds this limit. The default value is 10. |

Usage Notes

- To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- If the second timestamp is `NULL`, the function compares the current statistics in dictionary with the statistics as of the other timestamp.

---

### DIFF\_TABLE\_STATS\_IN\_PENDING Function

This function compares pending statistics and statistics as of a timestamp or statistics from dictionary.

Syntax

```
DBMS_STATS.DIFF_TABLE_STATS_IN_PENDING( 
      ownname        IN  VARCHAR2,
      tabname        IN  VARCHAR2,
      timestamp      IN  TIMESTAMP WITH TIME ZONE,
      pctthreshold   IN  NUMBER  DEFAULT 10)
   RETURN DiffRepTab pipelined;
```

Parameters

Table 142-23 DIFF\_TABLE\_STATS\_IN\_PENDING Function Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner of the table. Specify `NULL` for current schema. |
| `tabname` | Table for which statistics are to be compared |
| `timestamp` | Time stamp to get statistics from the history |
| `pctthreshold` | The function reports difference in statistics only if it exceeds this limit. The default value is 10. |

Usage Notes

- To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- If the second timestamp is `NULL`, the function compares the current statistics in dictionary with the statistics as of the other timestamp.

---

### DIFF\_TABLE\_STATS\_IN\_STATTAB Function

This function can be used to compare statistics for a table from two different sources. The statistics can be drawn from

- two different user statistics tables
- a single user statistics table containing 2 sets of statistics that can be identified using `statids`
- a user statistics table and dictionary

The function also compares the statistics of the dependent objects (indexes, columns, partitions) as well. It displays statistics of the object(s) from both sources if the difference between those statistics exceeds a certain threshold (%). The threshold can be specified as an argument to the function. The statistics corresponding to the first source (`stattab1` or `time1`) will be used as basis for computing the difference percentage.

Syntax

```
DBMS_STATS.DIFF_TABLE_STATS_IN_STATTAB( 
      ownname        IN  VARCHAR2,
      tabname        IN  VARCHAR2,
      stattab1       IN  VARCHAR2,
      stattab2       IN  VARCHAR2 DEFAULT NULL,      pctthreshold   IN  NUMBER  DEFAULT 10,      statid1        IN  VARCHAR2 DEFAULT NULL,      statid2        IN  VARCHAR2 DEFAULT NULL,      stattab1own    IN  VARCHAR2 DEFAULT NULL,      stattab2own    IN  VARCHAR2 DEFAULT NULL)   RETURN DiffRepTab pipelined;
```

Parameters

Table 142-24 DIFF\_TABLE\_STATS\_IN\_STATTAB Function Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner of the table. Specify `NULL` for current schema. |
| `tabname` | Table for which statistics are to be compared |
| `stattab1` | User statistics table 1 |
| `stattab2` | User statistics table 2. If `NULL`, statistics in `stattab1` is compared with current statistics in dictionary. This is the default. Specify same table as `stattab1` to compare two sets within the statistics table (see `statid` below). |
| `pctthreshold` | The function reports difference in statistics only if it exceeds this limit. The default value is 10. |
| `stadid1` | (optional) Identifies statistics set within `stattab1`. |
| `stadid2` | (optional) Identifies statistics set within `stattab2` |
| `stattab1own` | Schema containing `stattab1` (if other than `ownname`) |
| `stattab2own` | Schema containing `stattab2` (if other than `ownname`) |

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

---

### DROP\_EXTENDED\_STATS Procedure

This function drops the statistics entry that is created for the user specified extension. This cancels the effects of the CREATE\_EXTENDED\_STATS Function.

Syntax

```
DBMS_STATS.DROP_EXTENDED_STATS (
   ownname    VARCHAR2, 
   tabname    VARCHAR2,
   extension  VARCHAR2);
```

Parameters

Table 142-25 DROP\_EXTENDED\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name of a table |
| `tabname` | Name of the table |
| `extension` | Can be either a column group or an expression. Suppose the specified table has two column `c1`, `c2`. An example column group can be "(`c1`, `c2`)" and an example expression can be "(`c1` + `c2`)". |

Exceptions

- `ORA-20000`: Insufficient privileges or extension does not exist
- `ORA-20001`: Error when processing extension

Usage Notes

- To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- If no extended statistics set is created for the extension, this function throws an error.

---

### DROP\_STAT\_TABLE Procedure

This procedure drops a user statistics table.

Syntax

```
DBMS_STATS.DROP_STAT_TABLE (
   ownname VARCHAR2, 
   stattab VARCHAR2);
```

Parameters

Table 142-26 DROP\_STAT\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `stattab` | User statistics table identifier |

Exceptions

`ORA-20000`: Table does not exists or insufficient privileges.

Usage Notes

To invoke this procedure you need the privileges for dropping the specified table.

---

### EXPORT\_COLUMN\_STATS Procedure

This procedure retrieves statistics for a particular column and stores them in the user statistics table identified by `stattab`.

Syntax

```
DBMS_STATS.EXPORT_COLUMN_STATS (
   ownname  VARCHAR2, 
   tabname  VARCHAR2, 
   colname  VARCHAR2, 
   partname VARCHAR2 DEFAULT NULL,
   stattab  VARCHAR2, 
   statid   VARCHAR2 DEFAULT NULL,
   statown  VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-27 EXPORT\_COLUMN\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `tabname` | Name of the table to which this column belongs |
| `colname` | Name of the column or extension |
| `partname` | Name of the table partition. If the table is partitioned and if `partname` is `NULL`, then global and partition column statistics are exported. |
| `stattab` | User statistics table identifier describing where to store the statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `statown` | Schema containing `stattab` (if different than `ownname`) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

Usage Notes

- To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- Oracle does not support export or import of statistics across databases of different character sets.

---

### EXPORT\_DATABASE\_PREFS Procedure

This procedure is used to export the statistics preferences of all the tables, excluding the tables owned by Oracle. These tables can by included by passing `TRUE` for the `add_sys` parameter.

Syntax

```
DBMS_STATS.EXPORT_DATABASE_PREFS (
    stattab    IN  VARCHAR2,
    statid     IN  VARCHAR2 DEFAULT NULL,
    statown    IN  VARCHAR2 DEFAULT NULL
    add_sys    IN  BOOLEAN DEFAULT FALSE);
```

Parameters

Table 142-28 EXPORT\_DATABASE\_PREFS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | Statistics table name to where statistics should be exported |
| statid | (Optional) Identifier to associate with these statistics within `stattab` |
| statown | Schema containing `stattab` (if other than `ownname`) |
| `add_sys` | Value `TRUE` will include the Oracle-owned tables |

Exceptions

`ORA-20000`: Insufficient privileges

Usage Notes

- To run this procedure, you need to have the `SYSDBA` role, or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privileges.
- All arguments are of type `VARCHAR2` and values are enclosed in quotes.
- Oracle does not support export or import of statistics across databases of different character sets.

Examples

```
DBMS_STATS.EXPORT_DATABASE_PREFS('STATTAB', statown=>'SH');
```

---

### EXPORT\_DATABASE\_STATS Procedure

This procedure retrieves statistics for all objects in the database and stores them in the user statistics tables identified by `statown`.`stattab`.

Syntax

```
DBMS_STATS.EXPORT_DATABASE_STATS (
   stattab         VARCHAR2, 
   statid          VARCHAR2 DEFAULT NULL,
   statown         VARCHAR2 DEFAULT NULL,
   stat_category   VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY);
```

Parameters

Table 142-29 EXPORT\_DATABASE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | User statistics table identifier describing where to store the statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `statown` | Schema containing `stattab` (if different from current schema) |
| `stat_category` | Specifies what statistics to import, accepting multiple values separated by a comma. Values supported:  - `'OBJECT_STATS'` - table statistics, column statistics and index statistics (Default) - `'SYNOPSES'` - auxiliary statistics information gathered on a partitioned table when incremental is `TRUE` |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

Usage Notes

- To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- Oracle does not support export or import of statistics across databases of different character sets.

---

### EXPORT\_DICTIONARY\_STATS Procedure

This procedure retrieves statistics for all dictionary schemas (' `SYS` ', ' `SYSTEM` ' and RDBMS component schemas) and stores them in the user statistics table identified by `stattab`.

Syntax

```
DBMS_STATS.EXPORT_DICTIONARY_STATS (
   stattab         VARCHAR2, 
   statid          VARCHAR2 DEFAULT NULL,
   statown         VARCHAR2 DEFAULT NULL,
   stat_category   VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY);
```

Parameters

Table 142-30 EXPORT\_DICTIONARY\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | User statistics table identifier describing where to store the statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `statown` | Schema containing `stattab` (if different from current schema) |
| `stat_category` | Specifies what statistics to import, accepting multiple values separated by a comma. Values supported:  - `'OBJECT_STATS'` - table statistics, column statistics and index statistics (Default) - `'SYNOPSES'` - auxiliary statistics information gathered on a partitioned table when incremental is `TRUE` |

Usage Notes

- You must have the `SYSDBA` or `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privilege to execute this procedure.
- Oracle does not support export or import of statistics across databases of different character sets.

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20002`: Bad user statistics table, may need to upgrade it

---

### EXPORT\_FIXED\_OBJECTS\_STATS Procedure

This procedure retrieves statistics for fixed tables and stores them in the user statistics table identified by `stattab`.

Syntax

```
DBMS_STATS.EXPORT_FIXED_OBJECTS_STATS (
   stattab  VARCHAR2, 
   statid   VARCHAR2 DEFAULT NULL,
   statown  VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-31 EXPORT\_FIXED\_OBJECTS\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | User statistics table identifier describing where to store the statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `statown` | Schema containing `stattab` (if different from current schema) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20002`: Bad user statistics table, may need to upgrade it

Usage Notes

- To invoke this subprogram you need to be connected as `SYS` or have the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege
- Oracle does not support export or import of statistics across databases of different character sets.

---

### EXPORT\_INDEX\_STATS Procedure

This procedure retrieves statistics for a particular index and stores them in the user statistics table identified by `stattab`.

Syntax

```
DBMS_STATS.EXPORT_INDEX_STATS (
   ownname  VARCHAR2, 
   indname  VARCHAR2, 
   partname VARCHAR2 DEFAULT NULL,
   stattab  VARCHAR2, 
   statid   VARCHAR2 DEFAULT NULL,
   statown  VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-32 EXPORT\_INDEX\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `indname` | Name of the index |
| `partname` | Name of the index partition. If the index is partitioned and if `partname` is `NULL`, then global and partition index statistics are exported. |
| `stattab` | User statistics table identifier describing where to store the statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `statown` | Schema containing `stattab` (if different than `ownname`) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

Usage Notes

- To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- Oracle does not support export or import of statistics across databases of different character sets.

---

### EXPORT\_PENDING\_STATS Procedure

This procedure is used to export the statistics gathered and stored as pending.

Syntax

```
DBMS_STATS.EXPORT_PENDING_STATS (
    ownname    IN  VARCHAR2  DEFAULT USER,
    tabname    IN  VARCHAR2,
    stattab    IN  VARCHAR2,
    statid     IN  VARCHAR2 DEFAULT NULL,
    statown    IN  VARCHAR2 DEFAULT USER);
```

Parameters

Table 142-33 EXPORT\_PENDING\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name |
| `tabname` | Table name |
| `stattab` | Statistics table name to where to export the statistics |
| statid | (Optional) Identifier to associate with these statistics within `stattab` |
| statown | Schema containing `stattab` (if other than `ownname`) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

Usage Notes

- If the parameter `tabname` is `NULL` then export applies to all tables of the specified schema.
- The default owner/schema is the user who runs the procedure.
- To run this procedure, you need to have the same privilege for gathering statistics on the tables that will be touched by this procedure.
- All arguments are of type `VARCHAR2` and values are enclosed in quotes.
- Oracle does not support export or import of statistics across databases of different character sets.

Examples

```
DBMS_STATS.EXPORT_PENDING_STATS(NULL, NULL, 'MY_STAT_TABLE');
```

---

### EXPORT\_SCHEMA\_PREFS Procedure

This procedure is used to export the statistics preferences of all the tables owned by the specified owner name.

Syntax

```
DBMS_STATS.EXPORT_SCHEMA_PREFS (
    ownname    IN  VARCHAR2,
    stattab    IN  VARCHAR2,
    statid     IN  VARCHAR2 DEFAULT NULL,
    statown    IN  VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-34 EXPORT\_SCHEMA\_PREFS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name |
| `stattab` | Statistics table name to where to export the statistics |
| statid | (Optional) Identifier to associate with these statistics within `stattab` |
| statown | Schema containing `stattab` (if different than `ownname`) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

Usage Notes

- To run this procedure, you need to connect as owner, or have the `SYSDBA` privilege, or have the `ANALYZE` `ANY` system privilege.
- All arguments are of type `VARCHAR2` and values are enclosed in quotes.
- Oracle does not support export or import of statistics across databases of different character sets.

Examples

```
DBMS_STATS.EXPORT_SCHEMA_PREFS('SH', 'STAT');
```

---

### EXPORT\_SCHEMA\_STATS Procedure

This procedure retrieves statistics for all objects in the schema identified by `ownname` and stores them in the user statistics tables identified by `stattab`.

Syntax

```
DBMS_STATS.EXPORT_SCHEMA_STATS (
   ownname         VARCHAR2,
   stattab         VARCHAR2, 
   statid          VARCHAR2 DEFAULT NULL,
   statown         VARCHAR2 DEFAULT NULL,
   stat_category   VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY);
```

Parameters

Table 142-35 EXPORT\_SCHEMA\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `stattab` | User statistics table identifier describing where to store the statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `stat_category` | Specifies what statistics to import, accepting multiple values separated by a comma. Values supported:  - `'OBJECT_STATS'` - table statistics, column statistics and index statistics (Default) - `'SYNOPSES'` - auxiliary statistics information gathered on a partitioned table when incremental is `TRUE` |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

Usage Notes

- To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- Oracle does not support export or import of statistics across databases of different character sets.

---

### EXPORT\_SYSTEM\_STATS Procedure

This procedure retrieves system statistics and stores them in the user statistics table, identified by `stattab`.

Syntax

```
DBMS_STATS.EXPORT_SYSTEM_STATS (
   stattab       VARCHAR2, 
   statid        VARCHAR2 DEFAULT NULL,
   statown       VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-36 EXPORT\_SYSTEM\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | Identifier of the user statistics table that describes where the statistics will be stored |
| `statid` | Optional identifier associated with the statistics stored from the `stattab` |
| `statown` | Schema containing `stattab` (if different from current schema) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20002`: Bad user statistics table; may need to be upgraded

`ORA-20003`: Unable to export system statistics

Usage Notes

To run this procedure, you need the `GATHER_SYSTEM_STATISTICS` role.

Oracle does not support export or import of statistics across databases of different character sets.

---

### EXPORT\_TABLE\_PREFS Procedure

This procedure is used to export the statistics preferences of the specified table in the specified schema into the specified statistics table.

Syntax

```
DBMS_STATS.EXPORT_TABLE_PREFS (
    ownname    IN  VARCHAR2,
    tabname    IN  VARCHAR2,
    stattab    IN  VARCHAR2,
    statid     IN  VARCHAR2 DEFAULT NULL,
    statown    IN  VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-37 EXPORT\_TABLE\_PREFS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name |
| `tabname` | Table name |
| `stattab` | Statistics table name where to export the statistics |
| statid | Optional identifier to associate with these statistics within stattab |
| statown | Schema containing stattab (if other than `ownname`) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

Usage Notes

- To run this procedure, you need to connect as owner of the table, or have the `ANALYZE` `ANY` system privilege.
- All arguments are of type `VARCHAR2` and values are enclosed in quotes.
- Oracle does not support export or import of statistics across databases of different character sets.

Examples

```
DBMS_STATS.EXPORT_TABLE_PREFS('SH', 'SALES', 'STAT');
```

---

### EXPORT\_TABLE\_STATS Procedure

This procedure retrieves statistics for a particular table and stores them in the user statistics table. Cascade results in all index statistics associated with the specified table being exported as well.

Syntax

```
DBMS_STATS.EXPORT_TABLE_STATS (
   ownname         VARCHAR2, 
   tabname         VARCHAR2, 
   partname        VARCHAR2 DEFAULT NULL,
   stattab         VARCHAR2, 
   statid          VARCHAR2 DEFAULT NULL,
   cascade         BOOLEAN  DEFAULT TRUE,
   statown         VARCHAR2 DEFAULT NULL,
   stat_category   VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY);
```

Parameters

Table 142-38 EXPORT\_TABLE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `tabname` | Name of the table |
| `partname` | Name of the table partition. If the table is partitioned and if `partname` is `NULL`, then global and partition table statistics are exported. |
| `stattab` | User statistics table identifier describing where to store the statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `cascade` | If true, then column and index statistics for this table are also exported |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `stat_category` | Specifies what statistics to import, accepting multiple values separated by a comma. Values supported:  - `'OBJECT_STATS'` - table statistics, column statistics and index statistics (Default) - `'SYNOPSES'` - auxiliary statistics information gathered on a partitioned table when incremental is `TRUE` |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

Usage Notes

- To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- Oracle does not support export or import of statistics across databases of different character sets.

---

### FLUSH\_DATABASE\_MONITORING\_INFO Procedure

This procedure flushes in-memory monitoring information for all tables in the dictionary. Corresponding entries in the `*_TAB_MODIFICATIONS`, `*_TAB_STATISTICS` and `*_IND_STATISTICS` views are updated immediately, without waiting for the Oracle database to flush them periodically. This procedure is useful when you need up-to-date information in those views. Because the `GATHER_*_STATS` procedures internally flush monitoring information, it is not necessary to run this procedure before gathering the statistics.

Syntax

```
DBMS_STATS.FLUSH_DATABASE_MONITORING_INFO;
```

Exceptions

`ORA-20000`: Insufficient privileges

Usage Notes

The `ANALYZE_ANY` system privilege is required to run this procedure.

---

### GATHER\_DATABASE\_STATS Procedures

This procedure gathers statistics for all objects in the database.

Syntax

```
DBMS_STATS.GATHER_DATABASE_STATS (
   estimate_percent NUMBER   DEFAULT to_estimate_percent_type 
                                                (get_param('ESTIMATE_PERCENT')),
   block_sample     BOOLEAN  DEFAULT FALSE,
   method_opt       VARCHAR2 DEFAULT get_param('METHOD_OPT'),
   degree           NUMBER   DEFAULT to_degree_type(get_param('DEGREE')),
   granularity      VARCHAR2 DEFAULT GET_PARAM('GRANULARITY'), 
   cascade          BOOLEAN  DEFAULT to_cascade_type(get_param('CASCADE')),
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   options          VARCHAR2 DEFAULT 'GATHER',
   objlist          OUT      ObjectTab,
   statown          VARCHAR2 DEFAULT NULL,
   gather_sys       BOOLEAN  DEFAULT TRUE,
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   obj_filter_list ObjectTab DEFAULT NULL);

DBMS_STATS.GATHER_DATABASE_STATS (
   estimate_percent NUMBER   DEFAULT to_estimate_percent_type 
                                                (get_param('ESTIMATE_PERCENT')), 
   block_sample     BOOLEAN  DEFAULT FALSE,
   method_opt       VARCHAR2 DEFAULT get_param('METHOD_OPT'),
   degree           NUMBER   DEFAULT to_degree_type(get_param('DEGREE')),
   granularity      VARCHAR2 DEFAULT GET_PARAM('GRANULARITY'), 
   cascade          BOOLEAN  DEFAULT to_cascade_type(get_param('CASCADE')),
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   options          VARCHAR2 DEFAULT 'GATHER',
   statown          VARCHAR2 DEFAULT NULL,
   gather_sys       BOOLEAN  DEFAULT TRUE,
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   obj_filter_list ObjectTab DEFAULT NULL);
```

Parameters

Table 142-39 GATHER\_DATABASE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `estimate_percent` | Percentage of rows to estimate (`NULL` means compute): The valid range is \[0.000001,100\]. Use the constant `DBMS_STATS`.`AUTO_SAMPLE_SIZE` to have Oracle determine the appropriate sample size for good statistics. This is the default.The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `block_sample` | Whether or not to use random block sampling instead of random row sampling. Random block sampling is more efficient, but if the data is not randomly distributed on disk, then the sample values may be somewhat correlated. Only pertinent when doing an estimate statistics. |
| `method_opt` | Accepts:  - `FOR ALL [INDEXED \| HIDDEN] COLUMNS` `[size_clause]` - `FOR COLUMNS [size clause] column [size_clause] [,column [size_clause]...]`  `size_clause` is defined as `size_clause := SIZE {integer \| REPEAT \| AUTO \| SKEWONLY}`  `column` is defined as `column := column_name \| extension name \| extension`     `- integer`: Number of histogram buckets. Must be in the range \[1,254\].   `- REPEAT`: Collects histograms only on the columns that already have histograms.   `- AUTO`: Oracle determines the columns on which to collect histograms based on data distribution and the workload of the columns.   `- SKEWONLY`: Oracle determines the columns on which to collect histograms based on the data distribution of the columns.  The default is `FOR ALL COLUMNS SIZE AUTO`.The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `degree` | Degree of parallelism. The default for `degree` is `NULL`. The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. `NULL` means use the table default value specified by the `DEGREE` clause in the `CREATE TABLE` or `ALTER TABLE` statement. Use the constant `DBMS_STATS.DEFAULT_DEGREE` to specify the default value based on the initialization parameters. The `AUTO_DEGREE` value determines the degree of parallelism automatically. This is between `1` (serial execution) and `DEFAULT_DEGREE` (the system default value based on number of CPUs and initialization parameters) according to the size of the object. When using `DEGREE=>NULL`, `DEGREE=>n`, or `DEGREE=>DBMS_STATS.DEFAULT_DEGREE`, the current implementation of `DBMS_STATS` may use serial execution if the size of the object does not warrant parallel execution. |
| `granularity` | Granularity of statistics to collect (only pertinent if the table is partitioned).  `'ALL'` - Gathers all (subpartition, partition, and global) statistics  `'AUTO'` - Determines the granularity based on the partitioning type. This is the default value.  `'DEFAULT'` - Gathers global and partition-level statistics. This option is obsolete, and while currently supported, it is included in the documentation for legacy reasons only. You should use the ' `GLOBAL AND PARTITION` ' for this functionality. Note that the default value is now ' `AUTO` '.  `'GLOBAL'` - Gathers global statistics  ' `GLOBAL AND PARTITION` ' - Gathers the global and partition level statistics. No subpartition level statistics are gathered even if it is a composite partitioned object.  `'PARTITION` '- Gathers partition-level statistics  `'SUBPARTITION'` - Gathers subpartition-level statistics |
| `cascade` | Gather statistics on the indexes as well. Using this option is equivalent to running the GATHER\_INDEX\_STATS Procedure on each of the indexes in the database in addition to gathering table and column statistics. Use the constant `DBMS_STATS.AUTO_CASCADE` to have Oracle determine whether index statistics to be collected or not. This is the default. The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `stattab` | User statistics table identifier describing where to save the current statistics.  The statistics table is assumed to reside in the same schema as the object being analyzed, so there must be one such table in each schema to use this option. |
| `statid` | Identifier (optional) to associate with these statistics within `stattab`. |
| `options` | Further specification of which objects to gather statistics for:  `GATHER`: Gathers statistics on all objects in the schema.  `GATHER` `AUTO`: Gathers all necessary statistics automatically. Oracle implicitly determines which objects need new statistics, and determines how to gather those statistics. When `GATHER AUTO` is specified, the only additional valid parameters are `stattab`, `statid`, `objlist` and `statown`; all other parameter settings are ignored. Returns a list of processed objects.  `GATHER` `STALE`: Gathers statistics on stale objects as determined by looking at the \* `_tab_modifications` views. Also, return a list of objects found to be stale.  `GATHER` `EMPTY`: Gathers statistics on objects which currently have no statistics. Return a list of objects found to have no statistics.  `LIST AUTO`: Returns a list of objects to be processed with `GATHER AUTO`  `LIST` `STALE`: Returns a list of stale objects as determined by looking at the \* `_tab_modifications` views  `LIST` `EMPTY`: Returns a list of objects which currently have no statistics |
| `objlist` | List of objects found to be stale or empty |
| `statown` | Schema containing `stattab` (if different from current schema) |
| `gather_sys` | Gathers statistics on the objects owned by the `'SYS'` user |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `obj_filter_list` | A list of object filters. When provided, `GATHER_DATABASE_STATS` will gather statistics only on objects which satisfy at least one object filter in the list as needed. In a single object filter, we can specify the constraints on the object attributes. The attribute values specified in the object filter are case- insensitive unless double-quoted. Wildcard is allowed in the attribute values. Suppose non- `NULL` values s1, s2,... are specified for attributes a1, a2,... in one object filter. An object o is said to satisfy this object filter if (o.a1 like s1) and (o.a2 like s2) and... is true. See Applying an Object Filter List. |

Exceptions

`ORA-20000`: Insufficient privileges

`ORA-20001`: Bad input value

Usage Notes

To run this procedure, you need to have the `SYSDBA` role or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privileges.

---

### GATHER\_DICTIONARY\_STATS Procedure

This procedure gathers statistics for dictionary schemas ' `SYS` ', ' `SYSTEM` ' and schemas of RDBMS components.

Syntax

```
DBMS_STATS.GATHER_DICTIONARY_STATS (
   comp_id          VARCHAR2 DEFAULT NULL, 
   estimate_percent NUMBER   DEFAULT to_estimate_percent_type 
                                                (get_param('ESTIMATE_PERCENT')),
   block_sample     BOOLEAN  DEFAULT FALSE,
   method_opt       VARCHAR2 DEFAULT get_param('METHOD_OPT'),
   degree           NUMBER   DEFAULT to_degree_type(get_param('DEGREE')),
   granularity      VARCHAR2 DEFAULT GET_PARAM('GRANULARITY'),
   cascade          BOOLEAN  DEFAULT to_cascade_type(get_param('CASCADE')),
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   options          VARCHAR2 DEFAULT 'GATHER AUTO', 
   objlist    OUT   ObjectTab,
   statown          VARCHAR2 DEFAULT NULL,
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   obj_filter_list ObjectTab DEFAULT NULL);

DBMS_STATS.GATHER_DICTIONARY_STATS (
   comp_id           VARCHAR2 DEFAULT NULL,
   estimate_percent  NUMBER DEFAULT 
                          to_estimate_percent_type(GET_PARAM('ESTIMATE_PERCENT')),
   block_sample      BOOLEAN DEFAULT FALSE,
   method_opt        VARCHAR2 DEFAULT GET_PARAM('METHOD_OPT'),
   degree            NUMBER DEFAULT to_degree_type(GET_PARAM('DEGREE')),
   granularity       VARCHAR2 DEFAULT GET_PARAM('GRANULARITY'),
   cascade           BOOLEAN DEFAULT to_cascade_type(GET_PARAM('CASCADE')),
   stattab           VARCHAR2 DEFAULT NULL, 
   statid            VARCHAR2 DEFAULT NULL,
   options           VARCHAR2 DEFAULT 'GATHER AUTO', 
   statown           VARCHAR2 DEFAULT NULL,
   no_invalidate     BOOLEAN DEFAULT
                               to_no_invalidate_type(get_param('NO_INVALIDATE')),
   obj_filter_list   ObjectTab DEFAULT NULL);
```

Parameters

Table 142-40 GATHER\_DICTIONARY\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `comp_id` | Component id of the schema to analyze (`NULL` will result in analyzing schemas of all RDBMS components).Please refer to comp\_id column of DBA\_REGISTRY view. The procedure always gather statistics on ' `SYS` ' and ' `SYSTEM` ' schemas regardless of this argument. |
| `estimate_percent` | Percentage of rows to estimate (`NULL` means compute). The valid range is `[0.000001,100]`. Use the constant `DBMS_STATS`.`AUTO_SAMPLE_SIZE` to have Oracle determine the appropriate sample size for good statistics. This is the default.The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure`.` |
| `block_sample` | Determines whether or not to use random block sampling instead of random row sampling. Random block sampling is more efficient, but if the data is not randomly distributed on disk then the sample values may be somewhat correlated. Only pertinent when performing estimate statistics. |
| `method_opt` | Accepts:  - `FOR ALL [INDEXED \| HIDDEN] COLUMNS` `[size_clause]` - `FOR COLUMNS [size clause] column [size_clause] [,column [size_clause]...]`  `size_clause` is defined as `size_clause := SIZE {integer \| REPEAT \| AUTO \| SKEWONLY}`  `column` is defined as `column := column_name \| extension name \| extension`     `- integer`: Number of histogram buckets. Must be in the range \[1,254\].   `- REPEAT`: Collects histograms only on the columns that already have histograms.   `- AUTO`: Oracle determines the columns on which to collect histograms based on data distribution and the workload of the columns.   `- SKEWONLY`: Oracle determines the columns on which to collect histograms based on the data distribution of the columns.  The default is `FOR ALL COLUMNS SIZE AUTO`.The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `degree` | Degree of parallelism. The default for `degree` is `NULL`. The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. `NULL` means use the table default value specified by the `DEGREE` clause in the `CREATE TABLE` or `ALTER TABLE` statement. Use the constant `DBMS_STATS.DEFAULT_DEGREE` to specify the default value based on the initialization parameters. The `AUTO_DEGREE` value determines the degree of parallelism automatically. This is between `1` (serial execution) and `DEFAULT_DEGREE` (the system default value based on number of CPUs and initialization parameters) according to the size of the object. When using `DEGREE=>NULL`, `DEGREE=>n`, or `DEGREE=>DBMS_STATS.DEFAULT_DEGREE`, the current implementation of `DBMS_STATS` may use serial execution if the size of the object does not warrant parallel execution. |
| `granularity` | Granularity of statistics to collect (only pertinent if the table is partitioned).  `'ALL'` - Gathers all (subpartition, partition, and global) statistics  `'AUTO'` - Determines the granularity based on the partitioning type. This is the default value.  `'DEFAULT'` - Gathers global and partition-level statistics. This option is obsolete, and while currently supported, it is included in the documentation for legacy reasons only. You should use the ' `GLOBAL AND PARTITION` ' for this functionality. Note that the default value is now ' `AUTO` '.  `'GLOBAL'` - Gathers global statistics  ' `GLOBAL AND PARTITION` ' - Gathers the global and partition level statistics. No subpartition level statistics are gathered even if it is a composite partitioned object.  `'PARTITION` '- Gathers partition-level statistics  `'SUBPARTITION'` - gathers subpartition-level statistics |
| `cascade` | Gathers statistics on indexes also.Index statistics gathering will not be parallelized. Using this option is equivalent to running the GATHER\_INDEX\_STATS Procedure on each of the indexes in the schema in addition to gathering table and column statistics. Use the constant `DBMS_STATS.AUTO_CASCADE` to have Oracle determine whether index statistics to be collected or not. This is the default.The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `stattab` | User statistics table identifier describing where to save the current statistics |
| `statid` | The (optional) identifier to associate with these statistics within `stattab` |
| `options` | Further specification of objects for which to gather statistics:  - ' `GATHER` ' - Gathers statistics on all objects in the schema - ' `GATHER` `AUTO` ' - Gathers all necessary statistics automatically. Oracle implicitly determines which objects need new statistics and determines how to gather those statistics. When ' `GATHER` `AUTO` ' is specified, the only additional valid parameters are `comp_id`, `stattab`, `statid` and `statown`; all other parameter settings will be ignored. Also, returns a list of objects processed. - ' `GATHER` `STALE` ' - Gathers statistics on stale objects as determined by looking at the `*_tab` \_modifications views. Also, returns a list of objects found to be stale. - ' `GATHER` `EMPTY` ' - Gathers statistics on objects which currently have no statistics. Also, returns a list of objects found to have no statistics. - ' `LIST` `AUTO` ' - Returns list of objects to be processed with ' `GATHER` `AUTO` ' - ' `LIST` `STALE` ' - Returns list of stale objects as determined by looking at the `*_tab` \_modifications views - ' `LIST` `EMPTY` ' - Returns list of objects which currently have no statistics |
| `objlist` | The list of objects found to be stale or empty |
| `statown` | Schema containing `stattab` (if different from current schema) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `obj_filter_list` | A list of object filters. When provided, this will gather statistics only on objects which satisfy at least one object filter in the list as needed. In a single object filter, we can specify the constraints on the object attributes. The attribute values specified in the object filter are case- insensitive unless double-quoted. Wildcard is allowed in the attribute values. Suppose non- `NULL` values s1, s2,... are specified for attributes a1, a2,... in one object filter. An object o is said to satisfy this object filter if (o.a1 like s1) and (o.a2 like s2) and... is true. See Applying an Object Filter List. |

Usage Notes

You must have the `SYSDBA` or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privilege to execute this procedure.

Exceptions

`ORA-20000`: Index does not exist or insufficient privileges

`ORA-20001`: Bad input value

`ORA-20002`: Bad user statistics table, may need to upgrade it

---

### GATHER\_FIXED\_OBJECTS\_STATS Procedure

This procedure gathers statistics for all fixed objects (dynamic performance tables).

Syntax

```
DBMS_STATS.GATHER_FIXED_OBJECTS_STATS (
   stattab        VARCHAR2 DEFAULT NULL,
   statid         VARCHAR2 DEFAULT NULL,
   statown        VARCHAR2 DEFAULT NULL, 
   no_invalidate  BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')));
```

Parameters

Table 142-41 GATHER\_FIXED\_OBJECTS\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | User statistics table identifier describing where to save the current statistics |
| `statid` | Identifier to associate with these statistics within `stattab` (optional) |
| `statown` | Schema containing `stattab` (if different from current schema) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |

Usage Notes

You must have the `SYSDBA` or `ANALYZE` `ANY` `DICTIONARY` system privilege to execute this procedure.

Exceptions

`ORA-20000`: Insufficient privileges

`ORA-20001`: Bad input value

`ORA-20002`: Bad user statistics table, may need to upgrade it

---

### GATHER\_INDEX\_STATS Procedure

This procedure gathers index statistics. It attempts to parallelize as much of the work as possible. Restrictions are described in the individual parameters. This operation will not parallelize with certain types of indexes, including cluster indexes, domain indexes, and bitmap join indexes. The `granularity` and `no_invalidate` arguments are not relevant to these types of indexes.

Syntax

```
DBMS_STATS.GATHER_INDEX_STATS (
   ownname          VARCHAR2, 
   indname          VARCHAR2, 
   partname         VARCHAR2 DEFAULT NULL,
   estimate_percent NUMBER   DEFAULT to_estimate_percent_type 
                                                (GET_PARAM('ESTIMATE_PERCENT')),
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   statown          VARCHAR2 DEFAULT NULL,
   degree           NUMBER   DEFAULT to_degree_type(get_param('DEGREE')),
   granularity      VARCHAR2 DEFAULT GET_PARAM('GRANULARITY'),
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type 
                                               (GET_PARAM('NO_INVALIDATE')),
   force            BOOLEAN DEFAULT FALSE);
```

Parameters

Table 142-42 GATHER\_INDEX\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Schema of index to analyze |
| `indname` | Name of index |
| `partname` | Name of partition |
| `estimate_percent` | Percentage of rows to estimate (`NULL` means compute). The valid range is `[0.000001,100]`. Use the constant `DBMS_STATS`.`AUTO_SAMPLE_SIZE` to have Oracle determine the appropriate sample size for good statistics. This is the default.The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `stattab` | User statistics table identifier describing where to save the current statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `degree` | Degree of parallelism. The default for `degree` is `NULL`. The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. `NULL` means use the table default value specified by the `DEGREE` clause in the `CREATE TABLE` or `ALTER TABLE` statement. Use the constant `DBMS_STATS.DEFAULT_DEGREE` to specify the default value based on the initialization parameters. The `AUTO_DEGREE` value determines the degree of parallelism automatically. This is between `1` (serial execution) and `DEFAULT_DEGREE` (the system default value based on number of CPUs and initialization parameters) according to the size of the object. When using `DEGREE=>NULL`, `DEGREE=>n`, or `DEGREE=>DBMS_STATS.DEFAULT_DEGREE`, the current implementation of `DBMS_STATS` may use serial execution if the size of the object does not warrant parallel execution. |
| `granularity` | Granularity of statistics to collect (only pertinent if the table is partitioned).  `'ALL'` - Gathers all (subpartition, partition, and global) statistics  `'AUTO'` - Determines the granularity based on the partitioning type. This is the default value.  `'DEFAULT'` - Gathers global and partition-level statistics. This option is obsolete, and while currently supported, it is included in the documentation for legacy reasons only. You should use the ' `GLOBAL AND PARTITION` ' for this functionality. Note that the default value is now ' `AUTO` '.  `'GLOBAL'` - Gathers global statistics  ' `GLOBAL AND PARTITION` ' - Gathers the global and partition level statistics. No subpartition level statistics are gathered even if it is a composite partitioned object.  `'PARTITION` '- Gathers partition-level statistics  `'SUBPARTITION'` - Gathers subpartition-level statistics. |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `force` | Gather statistics on object even if it is locked |

Exceptions

`ORA-20000`: Index does not exist or insufficient privileges

`ORA-20001`: Bad input value

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

---

### GATHER\_SCHEMA\_STATS Procedures

This procedure gathers statistics for all objects in a schema.

Syntax

```
DBMS_STATS.GATHER_SCHEMA_STATS ( 
   ownname          VARCHAR2, 
   estimate_percent NUMBER   DEFAULT to_estimate_percent_type 
                                                (get_param('ESTIMATE_PERCENT')), 
   block_sample     BOOLEAN  DEFAULT FALSE, 
   method_opt       VARCHAR2 DEFAULT get_param('METHOD_OPT'),
   degree           NUMBER   DEFAULT to_degree_type(get_param('DEGREE')), 
   granularity      VARCHAR2 DEFAULT GET_PARAM('GRANULARITY'), 
   cascade          BOOLEAN  DEFAULT to_cascade_type(get_param('CASCADE')), 
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL, 
   options          VARCHAR2 DEFAULT 'GATHER', 
   objlist          OUT      ObjectTab,
   statown          VARCHAR2 DEFAULT NULL, 
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
  force             BOOLEAN DEFAULT FALSE,
  obj_filter_list  ObjectTab DEFAULT NULL);
   
DBMS_STATS.GATHER_SCHEMA_STATS ( 
   ownname          VARCHAR2, 
   estimate_percent NUMBER   DEFAULT to_estimate_percent_type 
                                                (get_param('ESTIMATE_PERCENT')), 
   block_sample     BOOLEAN  DEFAULT FALSE, 
   method_opt       VARCHAR2 DEFAULT get_param('METHOD_OPT'), 
   degree           NUMBER   DEFAULT to_degree_type(get_param('DEGREE')), 
   granularity      VARCHAR2 DEFAULT GET_PARAM('GRANULARITY'), 
   cascade          BOOLEAN  DEFAULT to_cascade_type(get_param('CASCADE')), 
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL, 
   options          VARCHAR2 DEFAULT 'GATHER', 
   statown          VARCHAR2 DEFAULT NULL, 
   no_invalidate    BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE'), 
   force            BOOLEAN DEFAULT FALSE,
   obj_filter_list  ObjectTab DEFAULT NULL);
```

Parameters

Table 142-43 GATHER\_SCHEMA\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Schema to analyze (`NULL` means current schema) |
| `estimate_percent` | Percentage of rows to estimate (`NULL` means compute): The valid range is \[0.000001,100\]. Use the constant `DBMS_STATS`.`AUTO_SAMPLE_SIZE` to have Oracle determine the appropriate sample size for good statistics. This is the default.The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `block_sample` | Whether or not to use random block sampling instead of random row sampling. Random block sampling is more efficient, but if the data is not randomly distributed on disk, then the sample values may be somewhat correlated. Only pertinent when doing an estimate statistics. |
| `method_opt` | Accepts:  - `FOR ALL [INDEXED \| HIDDEN] COLUMNS` `[size_clause]` - `FOR COLUMNS [size clause] column [size_clause] [,column [size_clause]...]`  `size_clause` is defined as `size_clause := SIZE {integer \| REPEAT \| AUTO \| SKEWONLY}`  `column` is defined as `column := column_name \| extension name \| extension`     `- integer`: Number of histogram buckets. Must be in the range \[1,254\].   `- REPEAT`: Collects histograms only on the columns that already have histograms   `- AUTO`: Oracle determines the columns on which to collect histograms based on data distribution and the workload of the columns.   `- SKEWONLY`: Oracle determines the columns on which to collect histograms based on the data distribution of the columns.  The default is `FOR ALL COLUMNS SIZE AUTO`.The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `degree` | Degree of parallelism. The default for `degree` is `NULL`. The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. `NULL` means use the table default value specified by the `DEGREE` clause in the `CREATE TABLE` or `ALTER TABLE` statement. Use the constant `DBMS_STATS.DEFAULT_DEGREE` to specify the default value based on the initialization parameters. The `AUTO_DEGREE` value determines the degree of parallelism automatically. This is between `1` (serial execution) and `DEFAULT_DEGREE` (the system default value based on number of CPUs and initialization parameters) according to the size of the object. When using `DEGREE=>NULL`, `DEGREE=>n`, or `DEGREE=>DBMS_STATS.DEFAULT_DEGREE`, the current implementation of `DBMS_STATS` may use serial execution if the size of the object does not warrant parallel execution. |
| `granularity` | Granularity of statistics to collect (only pertinent if the table is partitioned).  `'ALL'` - Gathers all (subpartition, partition, and global) statistics  `'AUTO'` - Determines the granularity based on the partitioning type. This is the default value.  `'DEFAULT'` - Gathers global and partition-level statistics. This option is obsolete, and while currently supported, it is included in the documentation for legacy reasons only. You should use the ' `GLOBAL AND PARTITION` ' for this functionality. Note that the default value is now ' `AUTO` '.  `'GLOBAL'` - Gathers global statistics  ' `GLOBAL AND PARTITION` ' - Gathers the global and partition level statistics. No subpartition level statistics are gathered even if it is a composite partitioned object.  `'PARTITION` '- Gathers partition-level statistics  `'SUBPARTITION'` - Gathers subpartition-level statistics. |
| `cascade` | Gather statistics on the indexes as well. Using this option is equivalent to running the GATHER\_INDEX\_STATS Procedure on each of the indexes in the schema in addition to gathering table and column statistics. Use the constant `DBMS_STATS.AUTO_CASCADE` to have Oracle determine whether index statistics to be collected or not. This is the default. The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `stattab` | User statistics table identifier describing where to save the current statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `options` | Further specification of which objects to gather statistics for:  `GATHER`: Gathers statistics on all objects in the schema.  `GATHER` `AUTO`: Gathers all necessary statistics automatically. Oracle implicitly determines which objects need new statistics, and determines how to gather those statistics. When `GATHER AUTO` is specified, the only additional valid parameters are `ownname`, `stattab`, `statid`, `objlist` and `statown`; all other parameter settings are ignored. Returns a list of processed objects.  `GATHER` `STALE`: Gathers statistics on stale objects as determined by looking at the \* `_tab_modifications` views. Also, return a list of objects found to be stale.  `GATHER` `EMPTY`: Gathers statistics on objects which currently have no statistics. also, return a list of objects found to have no statistics.  `LIST AUTO`: Returns a list of objects to be processed with `GATHER AUTO`.  `LIST` `STALE`: Returns list of stale objects as determined by looking at the \* `_tab_modifications` views.  `LIST` `EMPTY`: Returns list of objects which currently have no statistics. |
| `objlist` | List of objects found to be stale or empty |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `force` | Gather statistics on objects even if they are locked |
| `obj_filter_list` | A list of object filters. When provided, `GATHER_SCHEMA_STATS` will gather statistics only on objects which satisfy at least one object filter in the list as needed. In a single object filter, we can specify the constraints on the object attributes. The attribute values specified in the object filter are case- insensitive unless double-quoted. Wildcard is allowed in the attribute values. Suppose non- `NULL` values s1, s2,... are specified for attributes a1, a2,... in one object filter. An object o is said to satisfy this object filter if (o.a1 like s1) and (o.a2 like s2) and... is true. See Applying an Object Filter List. |

Exceptions

`ORA-20000`: Schema does not exist or insufficient privileges

`ORA-20001`: Bad input value

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

When you use a specific value for the sampling percentage, `DBMS_STATS` honors it except for when:

- The result is less than 2500 rows (too small a sample) and
- The specified percentage is more than the certain percentage.

Examples

Applying an Object Filter List

The following example specifies that any table with a " `T` " prefix in the `SAMPLE` schema and any table in the `SYS` schema, if stale, will have statistics gathered upon it.

```
DECLARE
   filter_lst  DBMS_STATS.OBJECTTAB := DBMS_STATS.OBJECTTAB();
BEGIN
   filter_lst.extend(2);
   filter_lst(1).ownname := 'SH';
   filter_lst(1).objname := 'SALES';
   filter_lst(2).ownname := 'SH';
   filter_lst(2).objname := 'COSTS';
   DBMS_STATS.GATHER_SCHEMA_STATS(ownname=>'SH',obj_filter_list=>filter_lst);
 END;
```

---

### GATHER\_SYSTEM\_STATS Procedure

This procedure gathers system statistics.

Syntax

```
DBMS_STATS.GATHER_SYSTEM_STATS (
   gathering_mode   VARCHAR2 DEFAULT 'NOWORKLOAD',
   interval         INTEGER  DEFAULT NULL,
   stattab          VARCHAR2 DEFAULT NULL,
   statid           VARCHAR2 DEFAULT NULL,
   statown          VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-44 GATHER\_SYSTEM\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `gathering_mode` | Mode values are:  `NOWORKLOAD`: Will capture characteristics of the I/O system. Gathering may take a few minutes and depends on the size of the database. During this period Oracle will estimate the average read seek time and transfer speed for the I/O system. This mode is suitable for the all workloads. Oracle recommends to run `GATHER_SYSTEM_STATS` ('noworkload') after creation of the database and tablespaces. To fine tune system statistics for the workload use ' `START` ' and ' `STOP` ' or ' `INTERVAL` ' options. If you gather both ' `NOWORKLOAD` ' and workload specific (statistics collected using ' `INTERVAL` ' or ' `START` ' and ' `STOP` ' ), the workload statistics will be used by optimizer. Collected components: `cpuspeednw,` `ioseektim,` `iotfrspeed`.  `INTERVAL`: Captures system activity during a specified interval. This works in combination with the `interval` parameter. You should provide an interval value in minutes, after which system statistics are created or updated in the dictionary or `stattab`. You can use `GATHER_SYSTEM_STATS (gathering_mode=>'STOP'`) to stop gathering earlier than scheduled. Collected components: `maxthr`, `slavethr`, `cpuspeed`, `sreadtim`, `mreadtim`, `mbrc`.  `START` \| `STOP`: Captures system activity during specified start and stop times and refreshes the dictionary or `stattab` with statistics for the elapsed period. `Interval` value is ignored. Collected components: `maxthr`, `slavethr`, `cpuspeed`, `sreadtim`, `mreadtim`, `mbrc`. |
| `interval` | Time, in minutes, to gather statistics. This parameter applies only when `gathering_mode='INTERVAL'` |
| `stattab` | Identifier of the user statistics table where the statistics will be saved |
| `statid` | Optional identifier associated with the statistics saved in the `stattab` |
| `statown` | Schema containing `stattab` (if different from current schema) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid input value

`ORA-20002`: Bad user statistics table; may need to be upgraded

`ORA-20003`: Unable to gather system statistics

`ORA-20004`: Error in the `INTERVAL` mode: system parameter `job_queue_processes` must be >0

Usage Notes

To run this procedure, you need the `GATHER_SYSTEM_STATISTICS` role.

---

### GATHER\_TABLE\_STATS Procedure

This procedure gathers table and column (and index) statistics. It attempts to parallelize as much of the work as possible, but there are some restrictions as described in the individual parameters.

Syntax

```
DBMS_STATS.GATHER_TABLE_STATS (
   ownname          VARCHAR2, 
   tabname          VARCHAR2, 
   partname         VARCHAR2 DEFAULT NULL,
   estimate_percent NUMBER   DEFAULT to_estimate_percent_type 
                                                (get_param('ESTIMATE_PERCENT')), 
   block_sample     BOOLEAN  DEFAULT FALSE,
   method_opt       VARCHAR2 DEFAULT get_param('METHOD_OPT'),
   degree           NUMBER   DEFAULT to_degree_type(get_param('DEGREE')),
   granularity      VARCHAR2 DEFAULT GET_PARAM('GRANULARITY'), 
   cascade          BOOLEAN  DEFAULT to_cascade_type(get_param('CASCADE')),
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   statown          VARCHAR2 DEFAULT NULL,
   no_invalidate    BOOLEAN  DEFAULT  to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   stattype         VARCHAR2 DEFAULT 'DATA',
   force            BOOLEAN  DEFAULT FALSE);
```

Parameters

Table 142-45 GATHER\_TABLE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Schema of table to analyze |
| `tabname` | Name of table |
| `partname` | Name of partition |
| `estimate_percent` | Percentage of rows to estimate (`NULL` means compute) The valid range is \[0.000001,100\]. Use the constant `DBMS_STATS`.`AUTO_SAMPLE_SIZE` to have Oracle determine the appropriate sample size for good statistics. This is the default.The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `block_sample` | Whether or not to use random block sampling instead of random row sampling. Random block sampling is more efficient, but if the data is not randomly distributed on disk, then the sample values may be somewhat correlated. Only pertinent when doing an estimate statistics. |
| `method_opt` | Accepts either of the following options, or both in combination:  - `FOR ALL [INDEXED \| HIDDEN] COLUMNS` `[size_clause]` - `FOR COLUMNS [size clause] column [size_clause] [,column [size_clause]...]`  `size_clause` is defined as `size_clause := SIZE {integer \| REPEAT \| AUTO \| SKEWONLY}`  `column` is defined as `column := column_name \| extension name \| extension`     `- integer`: Number of histogram buckets. Must be in the range \[1,254\].   `- REPEAT`: Collects histograms only on the columns that already have histograms   `- AUTO`: Oracle determines the columns on which to collect histograms based on data distribution and the workload of the columns.   `- SKEWONLY`: Oracle determines the columns on which to collect histograms based on the data distribution of the columns.   \- `column_name`: Name of a column   \- `extension :` can be either a column group in the format of (`column_name`, `Colume_name` \[,...\]) or an expression  The default is `FOR ALL COLUMNS SIZE AUTO`. The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `degree` | Degree of parallelism. The default for `degree` is `NULL`. The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. `NULL` means use the table default value specified by the `DEGREE` clause in the `CREATE TABLE` or `ALTER TABLE` statement. Use the constant `DBMS_STATS.DEFAULT_DEGREE` to specify the default value based on the initialization parameters. The `AUTO_DEGREE` value determines the degree of parallelism automatically. This is between `1` (serial execution) and `DEFAULT_DEGREE` (the system default value based on number of CPUs and initialization parameters) according to the size of the object. When using `DEGREE=>NULL`, `DEGREE=>n`, or `DEGREE=>DBMS_STATS.DEFAULT_DEGREE`, the current implementation of `DBMS_STATS` may use serial execution if the size of the object does not warrant parallel execution. |
| `granularity` | Granularity of statistics to collect (only pertinent if the table is partitioned).  `'ALL'` - Gathers all (subpartition, partition, and global) statistics  `'APPROX_GLOBAL AND PARTITION'` - similar to `'GLOBAL AND PARTITION'` but in this case the global statistics are aggregated from partition level statistics. This option will aggregate all statistics except the number of distinct values for columns and number of distinct keys of indexes. The existing histograms of the columns at the table level are also aggregated.The aggregation will use only partitions with statistics, so to get accurate global statistics, users should make sure to have statistics for all partitions. Global statistics are gathered if `partname` is `NULL` or if the aggregation cannot be performed (for example, if statistics for one of the partitions is missing).  `'AUTO'` - Determines the granularity based on the partitioning type. This is the default value.  `'DEFAULT'` - Gathers global and partition-level statistics. This option is obsolete, and while currently supported, it is included in the documentation for legacy reasons only. You should use the ' `GLOBAL AND PARTITION` ' for this functionality. Note that the default value is now ' `AUTO` '.  `'GLOBAL'` - Gathers global statistics  ' `GLOBAL AND PARTITION` ' - Gathers the global and partition level statistics. No subpartition level statistics are gathered even if it is a composite partitioned object.  `'PARTITION` '- Gathers partition-level statistics  `'SUBPARTITION'` - Gathers subpartition-level statistics. |
| `cascade` | Gathers statistics on the indexes for this table. Using this option is equivalent to running the GATHER\_INDEX\_STATS Procedure on each of the table's indexes. Use the constant `DBMS_STATS.AUTO_CASCADE` to have Oracle determine whether index statistics are to be collected or not. This is the default. The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure`.` |
| `stattab` | User statistics table identifier describing where to save the current statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `stattype` | Statistics type. The only value allowed is `DATA`. |
| `force` | Gather statistics of table even if it is locked |

Exceptions

`ORA-20000`: Table does not exist or insufficient privileges

`ORA-20001`: Bad input value

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

Index statistics collection can be parellelized except for cluster, domain and join indexes.

Examples

An extension can be either a column group (see Example 1) or an expression (see Example 2).

Example 1

```
DBMS_STATS.GATHER_TABLE_STATS(
    'SH', 'SALES', method_opt => 'FOR COLUMNS (empno, deptno)');
```

Example 2

```
DBMS_STATS.GATHER_TABLE_STATS(
    'SH', 'SALES', method_opt => 'FOR COLUMNS (sal+comm)');
```

---

### GENERATE\_STATS Procedure

This procedure generates object statistics from previously collected statistics of related objects. The currently supported objects are b-tree and bitmap indexes.

Syntax

```
DBMS_STATS.GENERATE_STATS (
   ownname    VARCHAR2, 
   objname    VARCHAR2,
   organized  NUMBER DEFAULT 7,
   force      BOOLEAN default FALSE);
```

Parameters

Table 142-46 GENERATE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Schema of object |
| `objname` | Name of object |
| `organized` | Amount of ordering associated between the index and its underlying table. A heavily organized index would have consecutive index keys referring to consecutive rows on disk for the table (the same block). A heavily disorganized index would have consecutive keys referencing different table blocks on disk.  This parameter is only used for b-tree indexes. The number can be in the range of 0-10, with 0 representing a completely organized index and 10 a completely disorganized one. |
| `force` | If `TRUE`, generates statistics for the target object even if it is locked |

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by SYS, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the SYSDBA privilege.

For fully populated schemas, the gather procedures should be used instead when more accurate statistics are desired.

Exceptions

`ORA-20000`: Unsupported object type of object does not exist

`ORA-20001`: Invalid option or invalid statistics

---

### GET\_COLUMN\_STATS Procedures

These procedures gets all column-related information. In the form of this procedure that deals with user-defined statistics, the statistics type returned is the type stored, in addition to the user-defined statistics.

Syntax

```
DBMS_STATS.GET_COLUMN_STATS (
   ownname     VARCHAR2, 
   tabname     VARCHAR2, 
   colname     VARCHAR2, 
   partname    VARCHAR2 DEFAULT NULL,
   stattab     VARCHAR2 DEFAULT NULL, 
   statid      VARCHAR2 DEFAULT NULL,
   distcnt OUT NUMBER, 
   density OUT NUMBER,
   nullcnt OUT NUMBER, 
   srec    OUT StatRec,
   avgclen OUT NUMBER,
   statown     VARCHAR2 DEFAULT NULL);
```

Use the following for user-defined statistics:

```
DBMS_STATS.GET_COLUMN_STATS (
   ownname          VARCHAR2, 
   tabname          VARCHAR2, 
   colname          VARCHAR2, 
   partname         VARCHAR2 DEFAULT NULL,
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   ext_stats   OUT  RAW,
   stattypown  OUT  VARCHAR2 DEFAULT NULL, 
   stattypname OUT  VARCHAR2 DEFAULT NULL, 
   statown          VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-47 GET\_COLUMN\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `tabname` | Name of the table to which this column belongs |
| `colname` | Name of the column or extension |
| `partname` | Name of the table partition from which to get the statistics. If the table is partitioned and if `partname` is `NULL`, statistics are retrieved from the global table level. |
| `stattab` | User statistics table identifier describing from where to retrieve the statistics. If `stattab` is `NULL`, statistics are retrieved directly from the dictionary. |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` (Only pertinent if `stattab` is not `NULL`) |
| `ext_stats` | The user-defined statistics |
| `stattypown` | Schema of the statistics type |
| `stattypname` | Name of the statistics type |
| `distcnt` | Number of distinct values |
| `density` | Column density |
| `nullcnt` | Number of `NULLs` |
| `srec` | Structure holding internal representation of column minimum, maximum, and histogram values |
| `avgclen` | Average length of the column (in bytes) |
| `statown` | Schema containing `stattab` (if different than `ownname`) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges or no statistics have been stored for requested object

Usage Notes

Before invoking this procedure, ensure that the table exists.

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

---

### GET\_INDEX\_STATS Procedures

These procedures get all index-related information. In the form of this procedure that deals with user-defined statistics, the statistics type returned is the type stored, in addition to the user-defined statistics.

Syntax

```
DBMS_STATS.GET_INDEX_STATS (
   ownname        VARCHAR2, 
   indname        VARCHAR2,
   partname       VARCHAR2 DEFAULT NULL,
   stattab        VARCHAR2 DEFAULT NULL, 
   statid         VARCHAR2 DEFAULT NULL,
   numrows    OUT NUMBER, 
   numlblks   OUT NUMBER,
   numdist    OUT NUMBER, 
   avglblk    OUT NUMBER,
   avgdblk    OUT NUMBER, 
   clstfct    OUT NUMBER,
   indlevel   OUT NUMBER,
   statown        VARCHAR2 DEFAULT NULL,
   cachedblk  OUT NUMBER,
   cachehit   OUT NUMBER);

DBMS_STATS.GET_INDEX_STATS (
   ownname        VARCHAR2, 
   indname        VARCHAR2,
   partname       VARCHAR2 DEFAULT NULL,
   stattab        VARCHAR2 DEFAULT NULL, 
   statid         VARCHAR2 DEFAULT NULL,
   numrows    OUT NUMBER, 
   numlblks   OUT NUMBER,
   numdist    OUT NUMBER, 
   avglblk    OUT NUMBER,
   avgdblk    OUT NUMBER, 
   clstfct    OUT NUMBER,
   indlevel   OUT NUMBER,
   statown        VARCHAR2 DEFAULT NULL,
   guessq     OUT NUMBER,
   cachedblk  OUT NUMBER,
   cachehit   OUT NUMBER);
```

Use the following for user-defined statistics:

```
DBMS_STATS.GET_INDEX_STATS (
   ownname          VARCHAR2, 
   indname          VARCHAR2,
   partname         VARCHAR2 DEFAULT NULL,
   stattab          VARCHAR2 DEFAULT NULL, 
   statid           VARCHAR2 DEFAULT NULL,
   ext_stats   OUT  RAW,
   stattypown  OUT  VARCHAR2 DEFAULT NULL, 
   stattypname OUT  VARCHAR2 DEFAULT NULL, 
   statown          VARCHAR2 DEFAULT NULL,
   cachedblk        OUT NUMBER,
   cachehit         OUT NUMBER);
```

Parameters

Table 142-48 GET\_INDEX\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `indname` | Name of the index |
| `partname` | Name of the index partition for which to get the statistics. If the index is partitioned and if `partname` is `NULL`, then the statistics are retrieved for the global index level. |
| `stattab` | User statistics table identifier describing from where to retrieve the statistics. If `stattab` is `NULL`, then the statistics are retrieved directly from the dictionary. |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` (Only pertinent if `stattab` is not `NULL`) |
| `ext_stats` | User-defined statistics |
| `stattypown` | Schema of the statistics type |
| `stattypname` | Name of the statistics type |
| `numrows` | Number of rows in the index (partition) |
| `numlblks` | Number of leaf blocks in the index (partition) |
| `numdist` | Number of distinct keys in the index (partition) |
| `avglblk` | Average integral number of leaf blocks in which each distinct key appears for this index (partition) |
| `avgdblk` | Average integral number of data blocks in the table pointed to by a distinct key for this index (partition) |
| `clstfct` | Clustering factor for the index (partition) |
| `indlevel` | Height of the index (partition) |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `guessq` | Guess quality for the index (partition) |
| `cachedblk` | The average number of blocks in the buffer cache for the segment (index/table/index partition/table partition) |
| `cachehit` | The average cache hit ratio for the segment (index/table/index partition/table partition) |

Usage Notes

- Before invoking this procedure, ensure that the table exists.
	To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- The Optimizer uses the cached data to estimate number of cached blocks for index or statistics table access. The total cost of the operation will be combined from the I/O cost of reading not cached blocks from disk, the CPU cost of getting cached blocks from the buffer cache, and the CPU cost of processing the data.
- Oracle maintains `cachedblk` and `cachehit` at all times but uses correspondent caching statistics for optimization as part of the table and index statistics only when the user calls `DBMS_STATS.GATHER_[TABLE/INDEX/SCHEMA/DATABASE]_STATS` procedure for auto mode or `DBMS_STATS.GATHER_SYSTEM_STATS` for manual mode. In order to prevent the user from utilizing inaccurate and unreliable data, the optimizer will compute a 'confidence factor' for each `cachehit` and a `cachedblk` for each object. If the 'confidence factor' for the value meets confidence criteria, this value will be used, otherwise the defaults will be used.
- The automatic maintenance algorithm for object caching statistics assumes that there is only one major workload for the system and adjusts statistics to this workload, ignoring other "minor" workloads. If this is not the case, you must use manual mode for maintaining object caching statistics.
- The object caching statistics maintenance algorithm for auto mode prevents you from using statistics in the following situations
	- When not enough data has been analyzed, such as when an object has been recently create
		- When the system does not have one major workload resulting in averages not corresponding to real values.

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges or no statistics have been stored for requested object

---

### GET\_PARAM Function

Note:

This subprogram has been replaced by improved technology and is maintained only for purposes of backward compatibility. In this case, use the GET\_PREFS Function.

See also Deprecated Subprograms.

This function returns the default value of parameters of `DBMS_STATS` procedures.

Syntax

```
DBMS_STATS.GET_PARAM (
   pname     IN   VARCHAR2)
 RETURN VARCHAR2;
```

Parameters

Table 142-49 GET\_PARAM Function Parameters

| Parameter | Description |
| --- | --- |
| `pname` | Parameter name |

Exceptions

`ORA-20001`: Invalid input values

---

### GET\_PREFS Function

This function returns the default value of the specified preference.

Syntax

```
DBMS_STATS.GET_PREFS (
   pname     IN   VARCHAR2,
   ownname   IN   VARCHAR2 DEFAULT NULL,
   tabname   IN   VARCHAR2 DEFAULT NULL)
 RETURN VARCHAR2;
```

Parameters

Table 142-50 GET\_PREFS Function Parameters

| Parameter | Description |
| --- | --- |
| `pname` | Preference name. The default value for following preferences can be retrieved:  - `AUTOSTATS_TARGET` - `CASCADE` - `DEGREE` - `ESTIMATE_PERCENT` - `METHOD_OPT` - `NO_INVALIDATE` - `GRANULARITY` - `PUBLISH` - `INCREMENTAL` - `STALE_PERCENT` |
|  | `AUTOSTATS_TARGET` - This preference is applicable only for auto statistics collection. The value of this parameter controls the objects considered for statistics collection. It takes the following values:  - `'ALL'` - Statistics collected for all objects in system - `'ORACLE'` - Statistics collected for all Oracle owned objects - `'AUTO'` - Oracle decides on which objects to collect statistics |
| . | `CASCADE` - Determines whether or not index statistics are collected as part of gathering table statistics`.` |
| . | `DEGREE` - Determines degree of parallelism used for gathering statistics. |
| . | `ESTIMATE_PERCENT` - Determines the percentage of rows to estimate. The valid range is \[0.000001,100\]. Use the constant `DBMS_STATS`.`AUTO_SAMPLE_SIZE` to have Oracle determine the appropriate sample size for good statistics. This is the default. |
| . | `METHOD_OPT` - Controls column statistics collection and histogram creation. It accepts either of the following options, or both in combination:  - `FOR ALL [INDEXED \| HIDDEN] COLUMNS` `[size_clause]` - `FOR COLUMNS [size clause] column [size_clause] [,column [size_clause]...]`  `size_clause` is defined as `size_clause := SIZE {integer \| REPEAT \| AUTO \| SKEWONLY}`  `column` is defined as `column := column_name \| extension name \| extension`     `- integer`: Number of histogram buckets. Must be in the range \[1,254\].   `- REPEAT`: Collects histograms only on the columns that already have histograms.   `- AUTO`: Oracle determines the columns on which to collect histograms based on data distribution and the workload of the columns.   `- SKEWONLY`: Oracle determines the columns on which to collect histograms based on the data distribution of the columns.   \- `column_name`: name of a column   \- `extension :` can be either a column group in the format of `(column_name, colume_name [, ...])` or an expression  The default is `FOR ALL COLUMNS SIZE AUTO`.The default value can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| . | `NO_INVALIDATE` - The value controls the invalidation of dependent cursors of the tables for which statistics are being gathered. Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE` to have Oracle decide when to invalidate dependent cursors. This is the default. |
| . | `GRANULARITY` - Determines granularity of statistics to collect (only pertinent if the table is partitioned).  `'ALL'` - Gathers all (subpartition, partition, and global) statistics  `'AUTO'` - Determines the granularity based on the partitioning type. This is the default value.  `'DEFAULT'` - Gathers global and partition-level statistics. This option is obsolete, and while currently supported, it is included in the documentation for legacy reasons only. You should use the ' `GLOBAL AND PARTITION` ' for this functionality. Note that the default value is now ' `AUTO` '.  `'GLOBAL'` - Gathers global statistics  ' `GLOBAL AND PARTITION` ' - Gathers the global and partition level statistics. No subpartition level statistics are gathered even if it is a composite partitioned object.  `'PARTITION` '- Gathers partition-level statistics  `'SUBPARTITION'` - Gathers subpartition-level statistics. |
| . | `PUBLISH` - Determines whether or not newly gathered statistics will be published once the gather job has completed. Prior to Oracle Database 11g, Release 1 (11.1), once a statistic gathering job completed the new statistics were automatically published into the dictionary tables. The user now has the ability to gather statistics but not publish them immediately. This allows the DBA to test the new statistics before publishing them. |
| . | `INCREMENTAL` - Determines whether or not the global statistics of a partitioned table will be maintained without doing a full table scan. With partitioned tables it is very common to load new data into a new partition. As new partitions are added and data loaded, the global table statistics need to be kept up to date. Oracle will update the global table statistics by scanning only the partitions that have been changed instead of the entire table if the following conditions hold:  - `INCREMENTAL` value for the partitioned table is set to `TRUE` - `PUBLISH` value for the partitioned table is set to `TRUE`; - User specifies `AUTO_SAMPLE_SIZE` for `ESTIMATE_PERCENT` and `AUTO` for `GRANULARITY` when gathering statistics on the table  If the `INCREMENTAL` value for the partitioned table was set to `FALSE` (default value), a full table scan is used to maintain the global statistics which is a much more resource intensive and time-consuming operation for large tables. |
| . | `STALE_PERCENT` - This value determines the percentage of rows in a table that have to change before the statistics on that table are deemed stale and should be regathered. The valid domain for `stale_percent` is non-negative numbers. The default value is 10%. |
| `ownname` | Owner name |
| `tabname` | Table name |

Exceptions

`ORA-20001`: Invalid input values

Usage Notes

If the ownname and tabname are provided and a preference has been entered for the table, the function returns the preference as specified for the table. In all other cases it returns the global preference if it has been specified, otherwise the default value is returned.

No special privilege or role is needed to invoke this procedure.

---

### GET\_STATS\_HISTORY\_AVAILABILITY Function

This function returns oldest timestamp where statistics history is available.Users cannot restore statistics to a timestamp older than this one.

Syntax

```
DBMS_STATS.GET_STATS_HISTORY_AVAILABILITY
 RETURN TIMESTAMP WITH TIMEZONE;
```

Usage Notes

No special privilege or role is needed to invoke this procedure.

---

### GET\_STATS\_HISTORY\_RETENTION Function

This function returns the current retention value.

Syntax

```
DBMS_STATS.GET_STATS_HISTORY_RETENTION
 RETURN NUMBER;
```

Usage Notes

No special privilege or role is needed to invoke this procedure.

---

### GET\_SYSTEM\_STATS Procedure

This procedure gets system statistics from `stattab`, or from the dictionary if `stattab` is `NULL`.

Syntax

```
DBMS_STATS.GET_SYSTEM_STATS (
   status    OUT  VARCHAR2,
   dstart    OUT  DATE,
   dstop     OUT  DATE,
   pname          VARCHAR2,
   pvalue    OUT  NUMBER,
   stattab   IN   VARCHAR2 DEFAULT NULL, 
   statid    IN   VARCHAR2 DEFAULT NULL,
   statown   IN   VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-51 GET\_SYSTEM\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `status` | Output is one of the following:  - `COMPLETED:` - `AUTOGATHERING:` - `MANUALGATHERING:` - `BADSTATS:` |
| `dstart` | Date when statistics gathering started.  If `status` = `MANUALGATHERING`, the start date is returned. |
| `dstop` | Date when statistics gathering stopped.  - If `status` = `COMPLETE`, the finish date is returned. - If `status` = `AUTOGATHERING`, the future finish date is returned. - If `status` = `BADSTATS`, the must-finished-by date is returned. |
| `pname` | The parameter name to get, which can have one of the following values:  - `iotfrspeed` - I/O transfer speed in bytes for each millisecond - `ioseektim` - seek time + latency time + operating system overhead time, in milliseconds - `sreadtim` - average time to read single block (random read), in milliseconds - `mreadtim` - average time to read an mbrc block at once (sequential read), in milliseconds - `cpuspeed` - average number of CPU cycles for each second, in millions, captured for the workload (statistics collected using ' `INTERVAL` ' or ' `START` ' and ' `STOP` ' options) - `cpuspeednw` - average number of CPU cycles for each second, in millions, captured for the noworkload (statistics collected using ' `NOWORKLOAD` ' option. - `mbrc` - average multiblock read count for sequential read, in blocks - `maxthr` - maximum I/O system throughput, in bytes/second - `slavethr` - average slave I/O throughput, in bytes/second |
| `pvalue` | Parameter value to get |
| `stattab` | Identifier of the user statistics table where the statistics will be obtained. If stattab is null, the statistics will be obtained from the dictionary. |
| `statid` | Optional identifier associated with the statistics saved in the `stattab` |
| `statown` | Schema containing `stattab` (if different from current schema) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20002`: Bad user statistics table; may need to be upgraded

`ORA-20003`: Unable to gather system statistics

`ORA-20004`: Parameter does not exist

Usage Notes

To run this procedure, you need the `GATHER_SYSTEM_STATISTICS` role.

---

### GET\_TABLE\_STATS Procedure

This procedure gets all table-related information.

Syntax

```
DBMS_STATS.GET_TABLE_STATS (
   ownname         VARCHAR2, 
   tabname         VARCHAR2, 
   partname        VARCHAR2 DEFAULT NULL,
   stattab         VARCHAR2 DEFAULT NULL,
   statid          VARCHAR2 DEFAULT NULL,
   numrows     OUT NUMBER, 
   numblks     OUT NUMBER,
   avgrlen     OUT NUMBER,
   statown         VARCHAR2 DEFAULT NULL,
   cachedblk   OUT NUMBER,
   cachehit    OUT NUMBER);
```

Parameters

Table 142-52 GET\_TABLE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `tabname` | Name of the table to which this column belongs |
| `partname` | Name of the table partition from which to get the statistics. If the table is partitioned and if `partname` is `NULL`, then the statistics are retrieved from the global table level. |
| `stattab` | User statistics table identifier describing from where to retrieve the statistics. If `stattab` is `NULL`, then the statistics are retrieved directly from the dictionary. |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` (Only pertinent if `stattab` is not `NULL`) |
| `numrows` | Number of rows in the table (partition) |
| `numblks` | Number of blocks the table (partition) occupies |
| `avgrlen` | Average row length for the table (partition) |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `cachedblk` | The average number of blocks in the buffer cache for the segment (index/table/index partition/table partition) |
| `cachehit` | The average cache hit ratio for the segment (index/table/index partition/table partition) |

Usage Notes

- Before invoking this procedure, ensure that the table exists.
	To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- The Optimizer uses the cached data to estimate number of cached blocks for index or statistics table access. The total cost of the operation will be combined from the I/O cost of reading not cached blocks from disk, the CPU cost of getting cached blocks from the buffer cache, and the CPU cost of processing the data.
- Oracle maintains `cachedblk` and `cachehit` at all times but uses correspondent caching statistics for optimization as part of the table and index statistics only when the user calls `DBMS_STATS.GATHER_[TABLE/INDEX/SCHEMA/DATABASE]_STATS` procedure for auto mode or `DBMS_STATS.GATHER_SYSTEM_STATS` for manual mode. In order to prevent the user from utilizing inaccurate and unreliable data, the optimizer will compute a 'confidence factor' for each `cachehit` and a `cachedblk` for each object. If the 'confidence factor' for the value meets confidence criteria, this value will be used, otherwise the defaults will be used.
- The automatic maintenance algorithm for object caching statistics assumes that there is only one major workload for the system and adjusts statistics to this workload, ignoring other "minor" workloads. If this is not the case, you must use manual mode for maintaining object caching statistics.
- The object caching statistics maintenance algorithm for auto mode prevents you from using statistics in the following situations
	- When not enough data has been analyzed, such as when an object has been recently create
		- When the system does not have one major workload resulting in averages not corresponding to real values.

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges or no statistics have been stored for requested object

Usage Notes

Oracle does not support export or import of statistics across databases of different character sets.

---

### IMPORT\_COLUMN\_STATS Procedure

This procedure retrieves statistics for a particular column from the user statistics table identified by `stattab` and stores them in the dictionary.

Syntax

```
DBMS_STATS.IMPORT_COLUMN_STATS (
   ownname       VARCHAR2, 
   tabname       VARCHAR2, 
   colname       VARCHAR2,
   partname      VARCHAR2 DEFAULT NULL,
   stattab       VARCHAR2, 
   statid        VARCHAR2 DEFAULT NULL,
   statown       VARCHAR2 DEFAULT NULL,
   no_invalidate BOOLEAN DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   force         BOOLEAN DEFAULT FALSE);
```

Parameters

Table 142-53 IMPORT\_COLUMN\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `tabname` | Name of the table to which this column belongs |
| `colname` | Name of the column or extension |
| `partname` | Name of the table partition. If the table is partitioned and if `partname` is `NULL`, then global and partition column statistics are imported. |
| `stattab` | User statistics table identifier describing from where to retrieve the statistics |
| `statid` | Identifier to associate with these statistics within `stattab` (optional) |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `force` | If set to `TRUE`, imports statistics even if statistics are locked |

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values in the user statistics table

`ORA-20005`: Object statistics are locked

Usage Notes

Oracle does not support export or import of statistics across databases of different character sets.

---

### IMPORT\_DATABASE\_STATS Procedure

This procedure retrieves statistics for all objects in the database from the user statistics table(s) and stores them in the dictionary.

Syntax

```
DBMS_STATS.IMPORT_DATABASE_STATS (
   stattab         VARCHAR2, 
   statid          VARCHAR2 DEFAULT NULL,
   statown         VARCHAR2 DEFAULT NULL,
   no_invalidate   BOOLEAN DEFAULT to_no_invalidate_type(
                                    get_param('NO_INVALIDATE')),
   force           BOOLEAN DEFAULT FALSE,
   stat_category   VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY);
```

Parameters

Table 142-54 IMPORT\_DATABASE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | User statistics table identifier describing from where to retrieve the statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `statown` | Schema containing `stattab` (if different from current schema) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `force` | Overrides statistics locked at the object (table) level:  - `TRUE` - Ignores the statistics lock and imports the statistics - `FALSE` - The statistics will be imported only if they are not locked |
| `stat_category` | Specifies what statistics to import, accepting multiple values separated by a comma. Values supported:  - `OBJECT_STATS` - table statistics, column statistics and index statistics (Default) - `SYNOPSES` - information to support incremental statistics |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values in the user statistics table

Usage Notes

- To run this procedure, you need to have the `SYSDBA` role or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privileges.
- Oracle does not support export or import of statistics across databases of different character sets.

---

### IMPORT\_DATABASE\_PREFS Procedure

This procedure is used to import the statistics preferences of all the tables, excluding the tables owned by Oracle. These tables can by included by passing `TRUE` for the `add_sys` parameter.

Syntax

```
DBMS_STATS.IMPORT_DATABASE_PREFS (
    stattab    IN  VARCHAR2,
    statid     IN  VARCHAR2 DEFAULT NULL,
    statown    IN  VARCHAR2 DEFAULT NULL
    add_sys    IN  BOOLEAN DEFAULT FALSE);
```

Parameters

Table 142-55 IMPORT\_DATABASE\_PREFS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | Statistics table name where to import the statistics |
| statid | Optional identifier to associate with these statistics within `stattab` |
| statown | Schema containing `stattab` (if different than `ownname`) |
| `add_sys` | Value `TRUE` will include the Oracle-owned tables |

Exceptions

`ORA-20000`: Insufficient privileges.

Usage Notes

- To run this procedure, you need to have the SYSDBA role, or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privileges.
- Oracle does not support export or import of statistics across databases of different character sets.

Examples

```
DBMS_STATS.IMPORT_DATABASE_PREFS('STATTAB', statown=>'SH');
```

---

### IMPORT\_DICTIONARY\_STATS Procedure

This procedure retrieves statistics for all dictionary schemas (' `SYS` ', ' `SYSTEM` ' and RDBMS component schemas) from the user statistics table and stores them in the dictionary.

Syntax

```
DBMS_STATS.IMPORT_DICTIONARY_STATS (
   stattab         VARCHAR2, 
   statid          VARCHAR2 DEFAULT NULL,
   statown         VARCHAR2 DEFAULT NULL,
   no_invalidate   BOOLEAN DEFAULT to_no_invalidate_type(
                                    get_param('NO_INVALIDATE')),
   force           BOOLEAN DEFAULT FALSE,
   stat_category   VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY);
```

Parameters

Table 142-56 IMPORT\_DICTIONARY\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | User statistics table identifier describing from where to retrieve the statistics |
| `statid` | The (optional) identifier to associate with these statistics within `stattab` |
| `statown` | Schema containing `stattab` (if different from current schema) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `force` | Overrides statistics lock at the object (table) level:  - `TRUE` - Ignores the statistics lock and imports the statistics. - `FALSE` - The statistics will be imported only if there is no lock. |
| `stat_category` | Specifies what statistics to import, accepting multiple values separated by a comma. Values supported:  - `'OBJECT_STATS'` - table statistics, column statistics and index statistics (Default) - `'SYNOPSES'` - auxiliary statistics information gathered on a partitioned table when incremental is `TRUE` |

Usage Notes

- You must have the `SYSDBA` or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privilege to execute this procedure.
- Oracle does not support export or import of statistics across databases of different character sets.

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values in the user statistics table

`ORA-20002`: Bad user statistics table, may need to upgrade it

---

### IMPORT\_FIXED\_OBJECTS\_STATS Procedure

This procedure retrieves statistics for fixed tables from the user statistics table(s) and stores them in the dictionary.

Syntax

```
DBMS_STATS.IMPORT_FIXED_OBJECTS_STATS (
   stattab       VARCHAR2, 
   statid        VARCHAR2 DEFAULT NULL,
   statown       VARCHAR2 DEFAULT NULL,
   no_invalidate BOOLEAN DEFAULT to_no_invalidate_type(
                                    get_param('NO_INVALIDATE')),
   force         BOOLEAN DEFAULT FALSE);
```

Parameters

Table 142-57 IMPORT\_FIXED\_OBJECTS\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | User statistics table identifier describing from where to retrieve the statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `statown` | Schema containing `stattab` (if different from current schema) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `force` | Overrides statistics lock:  - `TRUE` - Ignores the statistics lock and imports the statistics - `FALSE` - The statistics will be imported only if there is no lock |

Usage Notes

- You must have the `SYSDBA` or `ANALYZE` `ANY` `DICTIONARY` system privilege to execute this procedure.
- Oracle does not support export or import of statistics across databases of different character sets.

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values in the user statistics table

`ORA-20002`: Bad user statistics table, may need to upgrade it

---

### IMPORT\_INDEX\_STATS Procedure

This procedure retrieves statistics for a particular index from the user statistics table identified by `stattab` and stores them in the dictionary.

Syntax

```
DBMS_STATS.IMPORT_INDEX_STATS (
   ownname       VARCHAR2, 
   indname       VARCHAR2,
   partname      VARCHAR2 DEFAULT NULL,
   stattab       VARCHAR2, 
   statid        VARCHAR2 DEFAULT NULL,
   statown       VARCHAR2 DEFAULT NULL,
   no_invalidate BOOLEAN DEFAULT to_no_invalidate_type(
                                    get_param('NO_INVALIDATE')),
   force         BOOLEAN DEFAULT FALSE);
```

Parameters

Table 142-58 IMPORT\_INDEX\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `indname` | Name of the index |
| `partname` | Name of the index partition. If the index is partitioned and if `partname` is `NULL`, then global and partition index statistics are imported. |
| `stattab` | User statistics table identifier describing from where to retrieve the statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `force` | Imports statistics even if index statistics are locked |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values in the user statistics table

`ORA-20005`: Object statistics are locked

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

Oracle does not support export or import of statistics across databases of different character sets.

---

### IMPORT\_SCHEMA\_PREFS Procedure

This procedure is used to import the statistics preferences of all the tables owned by the specified owner name.

Syntax

```
DBMS_STATS.IMPORT_SCHEMA_PREFS (
    ownname    IN  VARCHAR2,
    stattab    IN  VARCHAR2,
    statid     IN  VARCHAR2 DEFAULT NULL,
    statown    IN  VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-59 IMPORT\_SCHEMA\_PREFS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name |
| `stattab` | Statistics table name from where to import the statistics |
| statid | (Optional) Identifier to associate with these statistics within `stattab` |
| statown | Schema containing `stattab` (if other than `ownname`) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

Usage Notes

- To run this procedure, you need to connect as owner, or have the `SYSDBA` privilege, or have the `ANALYZE` `ANY` system privilege.
- All arguments are of type `VARCHAR2` and values are enclosed in quotes.
- Oracle does not support export or import of statistics across databases of different character sets.

Examples

```
DBMS_STATS.IMPORT_SCHEMA_PREFS('SH', 'STAT');
```

---

### IMPORT\_SCHEMA\_STATS Procedure

This procedure retrieves statistics for all objects in the schema identified by ownname from the user statistics table and stores them in the dictionary.

Syntax

```
DBMS_STATS.IMPORT_SCHEMA_STATS (
   ownname         VARCHAR2,
   stattab         VARCHAR2, 
   statid          VARCHAR2 DEFAULT NULL,
   statown         VARCHAR2 DEFAULT NULL,
   no_invalidate   BOOLEAN DEFAULTto_no_invalidate_type(
                                    get_param('NO_INVALIDATE')),
   force           BOOLEAN DEFAULT FALSE,
   stat_category   VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY);
```

Parameters

Table 142-60 IMPORT\_SCHEMA\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `stattab` | User statistics table identifier describing from where to retrieve the statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `force` | Overrides statistics locked at the object (table) level:  - `TRUE` - Ignores the statistics lock and imports the statistics. - `FALSE` - Statistics will be imported only if there is no lock. |
| `stat_category` | Specifies what statistics to import, accepting multiple values separated by a comma. Values supported:  - `'OBJECT_STATS'` - table statistics, column statistics and index statistics (Default) - `'SYNOPSES'` - auxiliary statistics information gathered on a partitioned table when incremental is `TRUE` |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values in the user statistics table

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

Oracle does not support export or import of statistics across databases of different character sets.

---

### IMPORT\_SYSTEM\_STATS Procedure

This procedure retrieves system statistics from the user statistics table, identified by stattab, and stores the statistics in the dictionary.

Syntax

```
DBMS_STATS.IMPORT_SYSTEM_STATS (
   stattab       VARCHAR2, 
   statid        VARCHAR2 DEFAULT NULL,
   statown       VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-61 IMPORT\_SYSTEM\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `stattab` | Identifier of the user statistics table where the statistics will be retrieved |
| `statid` | Optional identifier associated with the statistics retrieved from the stattab |
| `statown` | Schema containing `stattab` (if different from current schema) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values in the user statistics table

`ORA-20002`: Bad user statistics table; may need to be upgraded

`ORA-20003`: Unable to import system statistics

Usage Notes

To run this procedure, you need the `GATHER_SYSTEM_STATISTICS` role.

Oracle does not support export or import of statistics across databases of different character sets.

---

### IMPORT\_TABLE\_PREFS Procedure

This procedure is used to set the statistics preferences of the specified table in the specified schema.

Syntax

```
DBMS_STATS.IMPORT_TABLE_PREFS (
    ownname    IN  VARCHAR2,
    tabname    IN  VARCHAR2,
    stattab    IN  VARCHAR2,
    statid     IN  VARCHAR2 DEFAULT NULL,
    statown    IN  VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-62 IMPORT\_TABLE\_PREFS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name |
| `tabname` | Table name |
| `stattab` | Statistics table name from where to import the statistics |
| statid | (Optional) Identifier to associate with these statistics within stattab |
| statown | Schema containing stattab (if other than ownname) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

Usage Notes

- To run this procedure, you need to connect as owner of the table, or have the `ANALYZE` `ANY` system privilege.
- All arguments are of type `VARCHAR2` and values are enclosed in quotes.
- Oracle does not support export or import of statistics across databases of different character sets.

Examples

```
DBMS_STATS.IMPORT_TABLE_PREFS('SH', 'SALES', 'STAT');
```

---

### IMPORT\_TABLE\_STATS Procedure

This procedure retrieves statistics for a particular table from the user statistics table identified by `stattab` and stores them in the dictionary. Cascade results in all index statistics associated with the specified table being imported as well.

Syntax

```
DBMS_STATS.IMPORT_TABLE_STATS (
   ownname         VARCHAR2, 
   tabname         VARCHAR2,
   partname        VARCHAR2 DEFAULT NULL,
   stattab         VARCHAR2, 
   statid          VARCHAR2 DEFAULT NULL,
   cascade         BOOLEAN  DEFAULT TRUE,
   statown         VARCHAR2 DEFAULT NULL,
   no_invalidate   BOOLEAN DEFAULT to_no_invalidate_type(
                                    get_param('NO_INVALIDATE')),
   force           BOOLEAN DEFAULT FALSE,
   stat_category   VARCHAR2 DEFAULT DEFAULT_STAT_CATEGORY);
```

Parameters

Table 142-63 IMPORT\_TABLE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `tabname` | Name of the table |
| `partname` | Name of the table partition. If the table is partitioned and if `partname` is `NULL`, then global and partition table statistics are imported. |
| `stattab` | User statistics table identifier describing from where to retrieve the statistics |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` |
| `cascade` | If true, column and index statistics for this table are also imported |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure |
| `force` | Imports statistics even if table statistics are locked |
| `stat_category` | Specifies what statistics to import, accepting multiple values separated by a comma. Values supported:  - `'OBJECT_STATS'` - table statistics, column statistics and index statistics (Default) - `'SYNOPSES'` - auxiliary statistics information gathered on a partitioned table when incremental is `TRUE` |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values in the user statistics table

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

Oracle does not support export or import of statistics across databases of different character sets.

---

### LOCK\_PARTITION\_STATS Procedure

This procedure enables the user to lock statistics for a partition.

Syntax

```
DBMS_STATS.LOCK_PARTITION_STATS (
    ownname    VARCHAR2,
    tabname    VARCHAR2,
    partname   VARCHAR2);
```

Parameters

Table 142-64 LOCK\_PARTITION\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema to lock |
| `tabname` | Name of the table |
| `partname` | Partition name |

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

---

### LOCK\_SCHEMA\_STATS Procedure

This procedure locks the statistics of all tables of a schema.

Syntax

```
DBMS_STATS.LOCK_SCHEMA_STATS (
   ownname    VARCHAR2);
```

Parameters

Table 142-65 LOCK\_SCHEMA\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema to lock |

Usage Notes

- To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- When statistics on a table are locked, all the statistics depending on the table, including table statistics, column statistics, histograms and statistics on all dependent indexes, are considered to be locked.
- The `SET_*,` `DELETE_*,` `IMPORT_*,` `GATHER_*` procedures that modify statistics in the dictionary of an individual table, index or column will raise an error if statistics of the object is locked.
- Procedures that operates on multiple objects (such as `GATHER_SCHEMA_STATS`) will skip modifying the statistics of an object if it is locked. Many procedures have force argument to override the lock.
- This procedure either freezes the current set of the statistics or keeps the statistics empty (uncollected) to use dynamic statistics.
- The locked or unlocked state is not exported along with the table statistics when using `EXPORT_*_STATS` procedures.
- Neither the UNLOCK\_SCHEMA\_STATS Procedure nor the UNLOCK\_TABLE\_STATS Procedure is designed to unlock statistics of corresponding partitions. When you invoke the LOCK\_TABLE\_STATS Procedure, it sets the statistics lock bit at the table level. In that case, you cannot gather statistics on dependent objects such as partitions and indexes. By the same token, if table statistics are locked, the dependents are locked and you do not need to explicitly invoke the LOCK\_PARTITION\_STATS Procedure.

---

### LOCK\_TABLE\_STATS Procedure

This procedure locks the statistics on the table.

Syntax

```
DBMS_STATS.LOCK_TABLE_STATS (
   ownname    VARCHAR2,
   tabname    VARCHAR2);
```

Parameters

Table 142-66 LOCK\_TABLE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | The name of the schema |
| `tabname` | The name of the table |

Usage Notes

- To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- When statistics on a table are locked, all the statistics depending on the table, including table statistics, column statistics, histograms and statistics on all dependent indexes, are considered to be locked.
- The `SET_*,` `DELETE_*,` `IMPORT_*,` `GATHER_*` procedures that modify statistics in the dictionary of an individual table, index or column will raise an error if statistics of the object is locked.
- Procedures that operates on multiple objects (such as `GATHER_SCHEMA_STATS`) will skip modifying the statistics of an object if it is locked. Many procedures have force argument to override the lock.
- This procedure either freezes the current set of the statistics or keeps the statistics empty (uncollected) to use Dynamic Sampling.
- The locked or unlocked state is not exported along with the table statistics when using `EXPORT_*_STATS` procedures.

---

### MERGE\_COL\_USAGE Procedure

This procedure merges column usage information from a source database by means of a dblink into the local database. If column usage information already exists for a given table or column `MERGE_COL_USAGE` will combine both the local and the remote information.

Syntax

```
DBMS_STATS.MERGE_COL_USAGE (
   dblink    IN    VARCHAR2);
```

Parameters

Table 142-67 MERGE\_COL\_USAGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `dblink` | Name of dblink |

Usage Notes

User must be `SYS` to execute this procedure.

Exceptions

ORA-20000: Insufficient privileges

ORA-20001: Parameter dblink cannot be `NULL`

ORA-20002: Unable to create a `TEMP` table

---

### PREPARE\_COLUMN\_VALUES Procedures

These procedures convert user-specified minimum, maximum, and histogram endpoint datatype-specific values into Oracle's internal representation for future storage using `SET_COLUMN_STATS`.

Syntax

```
DBMS_STATS.PREPARE_COLUMN_VALUES (
   srec     IN OUT StatRec, 
   charvals        CHARARRAY);

DBMS_STATS.PREPARE_COLUMN_VALUES (
   srec      IN OUT StatRec, 
   datevals         DATEARRAY);

DBMS_STATS.PREPARE_COLUMN_VALUES ( 
   srec     IN OUT StatRec, 
   dblvals         DBLARRAY);

DBMS_STATS.PREPARE_COLUMN_VALUES ( 
   srec     IN OUT StatRec, 
   fltvals         FLTARRAY);

DBMS_STATS.PREPARE_COLUMN_VALUES (
   srec     IN OUT StatRec, 
   numvals         NUMARRAY);

DBMS_STATS.PREPARE_COLUMN_VALUES ( 
   srec     IN OUT StatRec, 
   rawvals         RAWARRAY);
```

Pragmas

```
pragma restrict_references(prepare_column_values, WNDS, RNDS, WNPS, RNPS);
pragma restrict_references(prepare_column_values_nvarchar, WNDS, RNDS, WNPS, RNPS);
pragma restrict_references(prepare_column_values_rowid, WNDS, RNDS, WNPS, RNPS);
```

Parameters

Table 142-68 PREPARE\_COLUMN\_VALUES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `srec.epc` | Number of values specified in `charvals`, `datevals`, `dblvals`, `fltvals`, `numvals`, or `rawvals`. This value must be between 2 and 256, inclusive, and it should be set to `2` for procedures which do not allow histogram information (`nvarchar` and `rowid`).  The first corresponding array entry should hold the minimum value for the column, and the last entry should hold the maximum. If there are more than two entries, then all the others hold the remaining height-balanced or frequency histogram endpoint values (with in-between values ordered from next-smallest to next-largest). This value may be adjusted to account for compression, so the returned value should be left as is for a call to `SET_COLUMN_STATS`. |
| `srec.bkvals` | If you want a frequency distribution, this array contains the number of occurrences of each distinct value specified in `charvals`, `datevals`, `dblvals`, `fltvals`, `numvals`, or `rawvals`. Otherwise, it is merely an output parameter, and it must be set to `NULL` when this procedure is called. |

Datatype-specific input parameters (use one) are shown in Table 142-69.

Table 142-69 Datatype-Specific Input Parameters

| Type | Description |
| --- | --- |
| `charvals` | The array of values when the column type is character-based. Up to the first 32 bytes of each string should be provided. Arrays must have between 2 and 256 entries, inclusive. If the datatype is fixed `CHAR`, the strings must be space-padded to 15 characters for correct normalization. |
| `datevals` | Array of values when the column type is date-based |
| `dblvals` | Array of values when the column type is double-based |
| `fltvals` | Array of values when the column type is float-based |
| `numvals` | Array of values when the column type is numeric-based |
| `rawvals` | Array of values when the column type is `RAW`. Up to the first 32 bytes of each strings should be provided. |
| `nvmin, nvmax` | Minimum and maximum values when the column type is national character set based. No histogram information can be provided for a column of this type. If the datatype is fixed `CHAR`, the strings must be space-padded to 15 characters for correct normalization. |
| `rwmin, rwmax` | Minimum and maximum values when the column type is `rowid`. No histogram information is provided for a column of this type. |

Output Parameters

Table 142-70 PREPARE\_COLUMN\_VALUES Procedure Output Parameters

| Parameter | Description |
| --- | --- |
| `srec.minval` | Internal representation of the minimum suitable for use in a call to `SET_COLUMN_STATS` |
| `srec.maxval` | Internal representation of the maximum suitable for use in a call to `SET_COLUMN_STATS` |
| `srec.bkvals` | Array suitable for use in a call to `SET_COLUMN_STATS` |
| `srec.novals` | Array suitable for use in a call to `SET_COLUMN_STATS` |

Exceptions

`ORA-20001`: Invalid or inconsistent input values

Usage Notes

No special privilege or role is needed to invoke this procedure.

---

### PREPARE\_COLUMN\_VALUES\_NVARCHAR2 Procedure

This procedure converts user-specified minimum, maximum, and histogram endpoint datatype-specific values into Oracle's internal representation for future storage using `SET_COLUMN_STATS`.

Syntax

```
DBMS_STATS.PREPARE_COLUMN_VALUES_NVARCHAR2 (
   srec     IN OUT StatRec, 
   nvmin           NVARCHAR2, 
   nvmax           NVARCHAR2);
```

Pragmas

```
pragma restrict_references(prepare_column_values_nvarchar, WNDS, RNDS, WNPS, RNPS);
```

Parameters

Table 142-71 PREPARE\_COLUMN\_VALUES\_NVARCHAR2 Procedure Parameters

| Parameter | Description |
| --- | --- |
| `srec.epc` | Number of values specified in `charvals`, `datevals`, `dblvals`, `fltvals`, `numvals`, or `rawvals`. This value must be between 2 and 256, inclusive, and it should be set to `2` for procedures which do not allow histogram information (`nvarchar` and `rowid`).  The first corresponding array entry should hold the minimum value for the column, and the last entry should hold the maximum. If there are more than two entries, then all the others hold the remaining height-balanced or frequency histogram endpoint values (with in-between values ordered from next-smallest to next-largest). This value may be adjusted to account for compression, so the returned value should be left as is for a call to `SET_COLUMN_STATS`. |
| `srec.bkvals` | If you want a frequency distribution, then this array contains the number of occurrences of each distinct value specified in `charvals`, `datevals`, `dblvals`, `fltvals`, `numvals`, or `rawvals`. Otherwise, it is merely an output parameter, and it must be set to `NULL` when this procedure is called. |

Datatype-specific input parameters (use one) are shown in Table 142-69.

Table 142-72 Datatype-Specific Input Parameters

| Type | Description |
| --- | --- |
| `nvmin, nvmax` | The minimum and maximum values when the column type is national character set based. No histogram information can be provided for a column of this type. If the datatype is fixed `CHAR`, the strings must be space-padded to 15 characters for correct normalization. |

Output Parameters

Table 142-73 PREPARE\_COLUMN\_VALUES Procedure Output Parameters

| Parameter | Description |
| --- | --- |
| `srec.minval` | Internal representation of the minimum suitable for use in a call to `SET_COLUMN_STATS` |
| `srec.maxval` | Internal representation of the maximum suitable for use in a call to `SET_COLUMN_STATS` |
| `srec.bkvals` | Array suitable for use in a call to `SET_COLUMN_STATS`. |
| `srec.novals` | Array suitable for use in a call to `SET_COLUMN_STATS` |

Exceptions

`ORA-20001`: Invalid or inconsistent input values

Usage Notes

No special privilege or role is needed to invoke this procedure.

---

### PREPARE\_COLUMN\_VALUES\_ROWID Procedure

This procedure converts user-specified minimum, maximum, and histogram endpoint datatype-specific values into Oracle's internal representation for future storage using `SET_COLUMN_STATS`.

Syntax

```
DBMS_STATS.PREPARE_COLUMN_VALUES_ROWID (
   srec  IN OUT StatRec, 
   rwmin        ROWID, 
   rwmax        ROWID);
```

Pragmas

```
pragma restrict_references(prepare_column_values_rowid, WNDS, RNDS, WNPS, RNPS);
```

Parameters

Table 142-74 PREPARE\_COLUMN\_VALUES\_ROWID Procedure Parameters

| Parameter | Description |
| --- | --- |
| `srec.epc` | Number of values specified in `charvals`, `datevals`, `dblvals`, `fltvals`, `numvals`, or `rawvals`. This value must be between 2 and 256, inclusive, and it should be set to `2` for procedures which do not allow histogram information (`nvarchar` and `rowid`).  The first corresponding array entry should hold the minimum value for the column, and the last entry should hold the maximum. If there are more than two entries, then all the others hold the remaining height-balanced or frequency histogram endpoint values (with in-between values ordered from next-smallest to next-largest). This value may be adjusted to account for compression, so the returned value should be left as is for a call to `SET_COLUMN_STATS`. |
| `srec.bkvals` | If you want a frequency distribution, this array contains the number of occurrences of each distinct value specified in `charvals`, `datevals`, `dblvals`, `fltvals`, `numvals`, or `rawvals`. Otherwise, it is merely an output parameter, and it must be set to `NULL` when this procedure is called. |

Datatype-specific input parameters (use one) are shown in Table 142-69.

Table 142-75 Datatype-Specific Input Parameters

| Type | Description |
| --- | --- |
| `rwmin, rwmax` | Minimum and maximum values when the column type is `rowid`. No histogram information is provided for a column of this type. |

Output Parameters

Table 142-76 PREPARE\_COLUMN\_VALUES Procedure Output Parameters

| Parameter | Description |
| --- | --- |
| `srec.minval` | Internal representation of the minimum suitable for use in a call to `SET_COLUMN_STATS`. |
| `srec.maxval` | Internal representation of the maximum suitable for use in a call to `SET_COLUMN_STATS`. |
| `srec.bkvals` | Array suitable for use in a call to `SET_COLUMN_STATS`. |
| `srec.novals` | Array suitable for use in a call to `SET_COLUMN_STATS`. |

Exceptions

`ORA-20001`: Invalid or inconsistent input values

Usage Notes

No special privilege or role is needed to invoke this procedure.

---

### PUBLISH\_PENDING\_STATS Procedure

This procedure is used to publish the statistics gathered and stored as pending.

Syntax

```
DBMS_STATS.PUBLISH_PENDING_STATS (
    ownname         IN  VARCHAR2 DEFAULT USER,
    tabname         IN  VARCHAR2,
    no_invalidate   BOOLEAN DEFAULT 
       to_no_invalidate_type(get_param('NO_INVALIDATE')),
    force      IN  BOOLEAN DEFAULT FALSE);
```

Parameters

Table 142-77 PUBLISH\_PENDING\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name |
| tabname | Table name |
| no\_invalidate | Do not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE` to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| force | If `TRUE`, will override the lock |

Exceptions

`ORA-20000`: Insufficient privileges

Usage Notes

- If the parameter `tabname` is `NULL` then publish applies to all tables of the specified schema.
- The default owner/schema is the user who runs the procedure.
- To run this procedure, you need to have the same privilege for gathering statistics on the tables that will be touched by this procedure.

Examples

```
DBMS_STATS.PUBLISH_PENDING_STATS ('SH', null);
```

---

### PURGE\_STATS Procedure

This procedure purges old versions of statistics saved in the dictionary. To run this procedure, you must have the `SYSDBA` or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privilege.

Syntax

```
DBMS_STATS.PURGE_STATS( 
    before_timestamp       TIMESTAMP WITH TIME ZONE);
```

Parameters

Table 142-78 PURGE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `before_timestamp` | Versions of statistics saved before this timestamp are purged. If `NULL`, it uses the purging policy used by automatic purge. The automatic purge deletes all history older than the older of (current time - statistics history retention) and (time of recent analyze in the system - 1). The statistics history retention value can be changed using `ALTER_STATS_HISTORY_RETENTION` Procedure.The default is 31 days. |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values

Usage Notes

To invoke this procedure you need the `ANALYZE` `ANY` privilege and the `ANALYZE` `ANY` `DICTIONARY` privilege.

---

### REPORT\_COL\_USAGE Function

This function reports the recorded column (group) usage information.

Syntax

```
DBMS_STATS.REPORT_COL_USAGE (
   ownname    IN    VARCHAR2,
   tabname    IN    VARCHAR2)
RETURN CLOB;
```

Parameters

Table 142-79 REPORT\_COL\_USAGE Function Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name. If `NULL` it reports column usage information for tables in all schemas in the database. |
| `tabname` | Table name. If `NULL` it reports column usage information for all tables of `ownname`. |

Usage Notes

To run this procedure, you need to have the `SYSDBA` role or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privileges.

---

### RESET\_GLOBAL\_PREF\_DEFAULTS Procedure

This procedures sets global preference, such as `CASCADE`, `ESTIMATE_PERCENT` and `GRANULARITY`, to default values. This reverses the global preferences set by the SET\_GLOBAL\_PREFS Procedure.

Syntax

```
DBMS_STATS.RESET_GLOBAL_PREF_DEFAULTS;
```

Usage Notes

To invoke this procedure you need the `ANALYZE` `ANY` privilege and the `ANALYZE` `ANY` `DICTIONARY` privilege.

---

### RESET\_PARAM\_DEFAULTS Procedure

Note:

This subprogram has been replaced by improved technology and is maintained only for purposes of backward compatibility. In this case, use the RESET\_GLOBAL\_PREF\_DEFAULTS Procedure.

See also Deprecated Subprograms.

This procedure resets the default values of all parameters to Oracle recommended values.

Syntax

```
DBMS_STATS.RESET_PARAM_DEFAULTS;
```

---

### RESTORE\_DATABASE\_STATS Procedure

This procedure restores statistics of all tables of the database as of a specified timestamp (`as_of_timestamp`).

Syntax

```
DBMS_STATS.RESTORE_DATABSE_STATS( 
   as_of_timestamp        TIMESTAMP WITH TIME ZONE, 
   force                  BOOLEAN DEFAULT FALSE,
   no_invalidate          BOOLEAN DEFAULT to_no_invalidate_type
                                                    (GET_PARAM('NO_INVALIDATE')));
```

Parameters

Table 142-80 RESTORE\_DATABASE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `as_of_timestamp` | The timestamp to which to restore statistics |
| `force` | Restores statistics even if their statistics are locked |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values

`ORA-20006`: Unable to restore statistics, statistics history not available

---

### RESTORE\_DICTIONARY\_STATS Procedure

This procedure restores statistics of all dictionary tables (tables of ' `SYS` ', ' `SYSTEM` ' and RDBMS component schemas) as of a specified timestamp (`as_of_timestamp`).

Syntax

```
DBMS_STATS.RESTORE_DICTIONARY_STATS( 
   as_of_timestamp        TIMESTAMP WITH TIME ZONE, 
   force                  BOOLEAN DEFAULT FALSE,
   no_invalidate          BOOLEAN DEFAULT to_no_invalidate_type
                                                    (GET_PARAM('NO_INVALIDATE')));
```

Parameters

Table 142-81 RESTORE\_DICTIONARY\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `as_of_timestamp` | Tmestamp to which to restore statistics |
| `force` | Restores statistics even if their statistics are locked |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |

Usage Notes

To run this procedure, you must have the `SYSDBA` or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privilege.

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values

`ORA-20006`: Unable to restore statistics, statistics history not available

---

### RESTORE\_FIXED\_OBJECTS\_STATS Procedure

This procedure restores statistics of all fixed tables as of a specified timestamp (`as_of_timestamp`).

Syntax

```
DBMS_STATS.RESTORE_FIXED_OBJECTS_STATS( 
   as_of_timestamp        TIMESTAMP WITH TIME ZONE, 
   force                  BOOLEAN DEFAULT FALSE,
   no_invalidate          BOOLEAN DEFAULT to_no_invalidate_type
                                                    (GET_PARAM('NO_INVALIDATE')));
```

Parameters

Table 142-82 RESTORE\_FIXED\_OBJECTS\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `as_of_timestamp` | The timestamp to which to restore statistics |
| `force` | Restores statistics even if their statistics are locked |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |

Usage Notes

To run this procedure, you must have the `SYSDBA` or `ANALYZE` `ANY` `DICTIONARY` system privilege.

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values

`ORA-20006`: Unable to restore statistics, statistics history not available

---

### RESTORE\_SCHEMA\_STATS Procedure

This procedure restores statistics of all tables of a schema as of a specified timestamp (`as_of_timestamp`).

Syntax

```
DBMS_STATS.RESTORE_SCHEMA_STATS( 
   ownname                VARCHAR2, 
   as_of_timestamp        TIMESTAMP WITH TIME ZONE, 
   force                  BOOLEAN DEFAULT FALSE,
   no_invalidate          BOOLEAN DEFAULT to_no_invalidate_type
                                                    (GET_PARAM('NO_INVALIDATE')));
```

Parameters

Table 142-83 RESTORE\_SCHEMA\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Schema of the tables for which the statistics are to be restored |
| `as_of_timestamp` | The timestamp to which to restore statistics |
| `force` | Restores statistics even if their statistics are locked |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values

`ORA-20006`: Unable to restore statistics, statistics history not available

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

---

### RESTORE\_SYSTEM\_STATS Procedure

This procedure restores system statistics as of a specified timestamp (`as_of_timestamp`).

Syntax

```
DBMS_STATS.RESTORE_SCHEMA_STATS( 
   as_of_timestamp        TIMESTAMP WITH TIME ZONE);
```

Parameters

Table 142-84 RESTORE\_SYSTEM\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `as_of_timestamp` | The timestamp to which to restore statistics |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values

`ORA-20006`: Unable to restore statistics, statistics history not available

Usage Notes

To run this procedure, you need the `GATHER_SYSTEM_STATISTICS` role.

---

### RESTORE\_TABLE\_STATS Procedure

This procedure restores statistics of a table as of a specified timestamp (`as_of_timestamp`). The procedure will restore statistics of associated indexes and columns as well. If the table statistics were locked at the specified timestamp the procedure will lock the statistics. The procedure will not restore user defined statistics.

Syntax

```
DBMS_STATS.RESTORE_TABLE_STATS (
   ownname                   VARCHAR2, 
   tabname                   VARCHAR2, 
   as_of_timestamp           TIMESTAMP WITH TIME ZONE,
   restore_cluster_index     BOOLEAN DEFAULT FALSE,
   force                     BOOLEAN DEFAULT FALSE,
   no_invalidate             BOOLEAN DEFAULT to_no_invalidate_type
                                                    (GET_PARAM('NO_INVALIDATE')));
```

Parameters

Table 142-85 RESTORE\_TABLE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | The schema of the table for which the statistics are to be restored |
| `tabname` | The table name |
| `as_of_timestamp` | The timestamp to which to restore statistics |
| `restore_cluster_index` | If the table is part of a cluster, restore statistics of the cluster index if set to `TRUE` |
| `force` | Restores statistics even if the table statistics are locked. If the table statistics were not locked at the specified timestamp, it unlocks the statistics. |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent values

`ORA-20006`: Unable to restore statistics, statistics history not available

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

---

### SEED\_COL\_USAGE Procedure

This procedure iterates over the SQL statements in the specified SQL tuning set, compiles them and seeds column usage information for the columns that appear in these statements.

Syntax

```
DBMS_STATS.SEED_COL_USAGE (
   sqlset_name    IN    VARCHAR2,
   owner_name     IN    VARCHAR2,
   time_limit     IN    POSITIVE DEFAULT NULL);
```

Parameters

Table 142-86 SEED\_COL\_USAGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sqlset_name` | Name of the SQL tuning set |
| `owner_name` | Owner of the SQL tuning set |
| `time_limit` | Time limit (in seconds) |

Exceptions

`ORA-20000`: Insufficient privileges

Usage Notes

To invoke this procedure you need the `ANALYZE` `ANY` privilege and the `ANALYZE` `ANY` `DICTIONARY` privilege.

This procedure also records group of columns. Extensions for the recorded group of columns can be created using the CREATE\_EXTENDED\_STATS Function procedure. If `sqlset_name` and `owner_name` are `NULL`, it records the column (group) usage information for the statements executed in the system in next `time_limit` seconds.

---

### SET\_COLUMN\_STATS Procedures

This procedure sets column-related information. In the version of this procedure that deals with user-defined statistics, the statistics type specified is the type to store in the dictionary, in addition to the actual user-defined statistics. If this statistics type is `NULL`, the statistics type associated with the index or column is stored.

Syntax

```
DBMS_STATS.SET_COLUMN_STATS (
   ownname       VARCHAR2, 
   tabname       VARCHAR2, 
   colname       VARCHAR2, 
   partname      VARCHAR2 DEFAULT NULL,
   stattab       VARCHAR2 DEFAULT NULL, 
   statid        VARCHAR2 DEFAULT NULL,
   distcnt       NUMBER DEFAULT NULL,
   density       NUMBER DEFAULT NULL,
   nullcnt       NUMBER DEFAULT NULL,
   srec          StatRec DEFAULT NULL,
   avgclen       NUMBER DEFAULT NULL,
   flags         NUMBER DEFAULT NULL,
   statown       VARCHAR2 DEFAULT NULL,
   no_invalidate BOOLEAN DEFAULT to_no_invalidate_type(
                                    get_param('NO_INVALIDATE')),
   force         BOOLEAN DEFAULT FALSE);
```

Use the following for user-defined statistics:

```
DBMS_STATS.SET_COLUMN_STATS (
   ownname       VARCHAR2, 
   tabname       VARCHAR2, 
   colname       VARCHAR2, 
   partname      VARCHAR2 DEFAULT NULL,
   stattab       VARCHAR2 DEFAULT NULL, 
   statid        VARCHAR2 DEFAULT NULL,
   ext_stats     RAW,
   stattypown    VARCHAR2 DEFAULT NULL, 
   stattypname   VARCHAR2 DEFAULT NULL, 
   statown       VARCHAR2 DEFAULT NULL,
   no_invalidate BOOLEAN DEFAULT to_no_invalidate_type(
                                    get_param('NO_INVALIDATE')),
   force         BOOLEAN DEFAULT FALSE);
```

Parameters

Table 142-87 SET\_COLUMN\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema. |
| `tabname` | Name of the table to which this column belongs. |
| `colname` | Name of the column or extension |
| `partname` | Name of the table partition in which to store the statistics. If the table is partitioned and `partname` is `NULL`, then the statistics are stored at the global table level. |
| `stattab` | User statistics table identifier describing where to store the statistics. If `stattab` is `NULL`, then the statistics are stored directly in the dictionary. |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` (Only pertinent if `stattab` is not `NULL`) |
| `ext_stats` | User-defined statistics |
| `stattypown` | Schema of the statistics type |
| `stattypname` | Name of the statistics type |
| `distcnt` | Number of distinct values |
| `density` | Column density. If this value is `NULL` and if `distcnt` is not `NULL`, then density is derived from `distcnt`. |
| `nullcnt` | Number of `NULLs` |
| `srec` | `StatRec` structure filled in by a call to `PREPARE_COLUMN_VALUES` or `GET_COLUMN_STATS` |
| `avgclen` | Average length for the column (in bytes) |
| `flags` | For internal Oracle use (should be left as `NULL`) |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `force` | Sets the values even if statistics of the column are locked |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or inconsistent input values

`ORA-20005`: Object statistics are locked

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

---

### SET\_DATABASE\_PREFS Procedure

This procedure is used to set the statistics preferences of all the tables, excluding the tables owned by Oracle. These tables can by included by passing `TRUE` for the `add_sys` parameter.

Syntax

```
DBMS_STATS.SET_DATABASE_PREFS (
    pname            IN   VARCHAR2,
    pvalue           IN   VARCHAR2,
    add_sys          IN   BOOLEAN DEFAULT FALSE);
```

Parameters

Table 142-88 SET\_DATABASE\_PREFS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pname` | Preference name. The default value for following parameters can be set:  - `CASCADE` - `DEGREE` - `ESTIMATE_PERCENT` - `METHOD_OPT` - `NO_INVALIDATE` - `GRANULARITY` - `PUBLISH` - `INCREMENTAL` - `STALE_PERCENT` |
| . | `CASCADE` - Determines whether or not index statistics are collected as part of gathering table statistics`.` |
| . | `DEGREE` - Determines degree of parallelism used for gathering statistics. |
| . | `ESTIMATE_PERCENT` - Determines the percentage of rows to estimate. The valid range is \[0.000001,100\]. Use the constant `DBMS_STATS`.`AUTO_SAMPLE_SIZE` to have Oracle determine the appropriate sample size for good statistics. This is the default. |
| . | `METHOD_OPT` - Controls column statistics collection and histogram creation. It accepts either of the following options, or both in combination:  - `FOR ALL [INDEXED \| HIDDEN] COLUMNS` `[size_clause]` - `FOR COLUMNS [size clause] column [size_clause] [,column [size_clause]...]`  `size_clause` is defined as `size_clause := SIZE {integer \| REPEAT \| AUTO \| SKEWONLY}`  `column` is defined as `column := column_name \| extension name \| extension`     `- integer`: Number of histogram buckets. Must be in the range \[1,254\].   `- REPEAT`: Collects histograms only on the columns that already have histograms   `- AUTO`: Oracle determines the columns on which to collect histograms based on data distribution and the workload of the columns.   `- SKEWONLY`: Oracle determines the columns on which to collect histograms based on the data distribution of the columns.   \- `column_name`: Name of a column   \- `extension :` Can be either a column group in the format of `(column_name, colume_name [, ...])` or an expression  The default is `FOR ALL COLUMNS SIZE AUTO`. |
| . | `NO_INVALIDATE` - Controls the invalidation of dependent cursors of the tables for which statistics are being gathered. Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE` to have Oracle decide when to invalidate dependent cursors. This is the default. |
| . | `GRANULARITY` - Determines granularity of statistics to collect (only pertinent if the table is partitioned).  `'ALL'` - Gathers all (subpartition, partition, and global) statistics  `'AUTO'` - Determines the granularity based on the partitioning type. This is the default value.  `'DEFAULT'` - Gathers global and partition-level statistics. This option is obsolete, and while currently supported, it is included in the documentation for legacy reasons only. You should use the ' `GLOBAL AND PARTITION` ' for this functionality. Note that the default value is now ' `AUTO` '.  `'GLOBAL'` - Gathers global statistics  ' `GLOBAL AND PARTITION` ' - Gathers the global and partition level statistics. No subpartition level statistics are gathered even if it is a composite partitioned object.  `'PARTITION` '- Gathers partition-level statistics  `'SUBPARTITION'` - Gathers subpartition-level statistics. |
| . | `PUBLISH` - Determines whether or not newly gathered statistics will be published once the gather job has completed. Prior to Oracle Database 11g, Release 1 (11.1), once a statistic gathering job completed the new statistics were automatically published into the dictionary tables. The user now has the ability to gather statistics but not publish them immediately. This allows the DBA to test the new statistics before publishing them. |
| . | `INCREMENTAL` - Determines whether or not the global statistics of a partitioned table will be maintained without doing a full table scan. With partitioned tables it is very common to load new data into a new partition. As new partitions are added and data loaded, the global table statistics need to be kept up to date. Oracle will update the global table statistics by scanning only the partitions that have been changed instead of the entire table if the following conditions hold:  - the `INCREMENTAL` value for the partitioned table is set to `TRUE`; - the `PUBLISH` value for the partitioned table is set to `TRUE`; - the user specifies `AUTO_SAMPLE_SIZE` for `ESTIMATE_PERCENT` and `AUTO` for `GRANULARITY` when gathering statistics on the table.  If the `INCREMENTAL` value for the partitioned table was set to `FALSE` (default value), a full table scan is used to maintain the global statistics which is a much more resource intensive and time-consuming operation for large tables. |
| . | `STALE_PERCENT` - Determines the percentage of rows in a table that have to change before the statistics on that table are deemed stale and should be regathered. The valid domain for `stale_percent` is non-negative numbers. The default value is 10%. |
| `pvalue` | Preference value. If `NULL` is specified, it will set the Oracle default value.s |
| `add_sys` | Value `TRUE` will include the Oracle-owned tables |

Exceptions

`ORA-20000`: Insufficient privileges

`ORA-20001`: Invalid or illegal input values

Usage Notes

- To run this procedure, you need to have the `SYSDBA` role or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privileges.
- Both arguments are of type `VARCHAR2` and values are enclosed in quotes, even when they represent numbers.

Examples

```
DBMS_STATS.SET_DATABASE_PREFS('CASCADE', 'DBMS_STATS.AUTO_CASCADE');
DBMS_STATS.SET_DATABASE_PREFS('ESTIMATE_PERCENT','9');
DBMS_STATS.SET_DATABASE_PREFS('DEGREE','99');
```

---

### SET\_GLOBAL\_PREFS Procedure

This procedure is used to set the global statistics preferences.

Syntax

```
DBMS_STATS.SET_GLOBAL_PREFS (
    pname     IN   VARCHAR2,
    pvalue    IN   VARCHAR2);
```

Parameters

Table 142-89 SET\_GLOBAL\_PREFS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pname` | Preference name. The default value for the following preferences can be set:  - `AUTOSTATS_TARGET` - `CASCADE` - `DEGREE` - `ESTIMATE_PERCENT` - `METHOD_OPT` - `NO_INVALIDATE` - `GRANULARITY` - `PUBLISH` - `INCREMENTAL` - `STALE_PERCENT` |
|  | `AUTOSTATS_TARGET` - This preference is applicable only for auto statistics collection. The value of this parameter controls the objects considered for stats collection. It takes the following values:  - `'ALL'` - Statistics collected for all objects in system - `'ORACLE'` - Statistics collected for all Oracle owned objects - `'AUTO'` - Oracle decides on which objects to collect statistics |
| . | `CASCADE` - Determines whether or not index statistics are collected as part of gathering table statistics |
| . | `DEGREE` - Determines degree of parallelism used for gathering statistics |
| . | `ESTIMATE_PERCENT` - Determines the percentage of rows to estimate. The valid range is \[0.000001,100\]. Use the constant `DBMS_STATS`.`AUTO_SAMPLE_SIZE` to have Oracle determine the appropriate sample size for good statistics. This is the default. |
| . | `METHOD_OPT` - The value controls column statistics collection and histogram creation. It accepts either of the following options, or both in combination:  - `FOR ALL [INDEXED \| HIDDEN] COLUMNS` `[size_clause]` - `FOR COLUMNS [size clause] column [size_clause] [,column [size_clause]...]`  `size_clause` is defined as `size_clause := SIZE {integer \| REPEAT \| AUTO \| SKEWONLY}`  `column` is defined as `column := column_name \| extension name \| extension`     `- integer`: Number of histogram buckets. Must be in the range \[1,254\].   `- REPEAT`: Collects histograms only on the columns that already have histograms.   `- AUTO`: Oracle determines the columns on which to collect histograms based on data distribution and the workload of the columns.   `- SKEWONLY`: Oracle determines the columns on which to collect histograms based on the data distribution of the columns.   \- `column_name`: Name of a column   \- `extension :` Can be either a column group in the format of `(column_name, colume_name [, ...])` or an expression  The default is `FOR ALL COLUMNS SIZE AUTO`. |
| . | `NO_INVALIDATE` - Controls the invalidation of dependent cursors of the tables for which statistics are being gathered. Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE` to have Oracle decide when to invalidate dependent cursors. This is the default. |
| . | `GRANULARITY` - Determines granularity of statistics to collect (only pertinent if the table is partitioned).  `'ALL'` - Gathers all (subpartition, partition, and global) statistics  `'AUTO'` - Determines the granularity based on the partitioning type. This is the default value.  `'DEFAULT'` - gathers global and partition-level statistics. This option is obsolete, and while currently supported, it is included in the documentation for legacy reasons only. You should use the ' `GLOBAL AND PARTITION` ' for this functionality. Note that the default value is now ' `AUTO` '.  `'GLOBAL'` - Gathers global statistics  ' `GLOBAL AND PARTITION` ' - gathers the global and partition level statistics. No subpartition level statistics are gathered even if it is a composite partitioned object.  `'PARTITION` '- gathers partition-level statistics  `'SUBPARTITION'` - gathers subpartition-level statistics. |
| . | `PUBLISH` - This value determines whether or not newly gathered statistics will be published once the gather job has completed. Prior to Oracle Database 11g, Release 1 (11.1), once a statistic gathering job completed the new statistics were automatically published into the dictionary tables. The user now has the ability to gather statistics but not publish them immediately. This allows the DBA to test the new statistics before publishing them. |
| . | `INCREMENTAL` - This value determines whether or not the global statistics of a partitioned table will be maintained without doing a full table scan. With partitioned tables it is very common to load new data into a new partition. As new partitions are added and data loaded, the global table statistics need to be kept up to date. Oracle will update the global table statistics by scanning only the partitions that have been changed instead of the entire table if the following conditions hold:  - `INCREMENTAL` value for the partitioned table is set to `TRUE` - `PUBLISH` value for the partitioned table is set to `TRUE`; - User specifies `AUTO_SAMPLE_SIZE` for `ESTIMATE_PERCENT` and `AUTO` for `GRANULARITY` when gathering statistics on the table  If the `INCREMENTAL` value for the partitioned table was set to `FALSE` (default value), a full table scan is used to maintain the global statistics which is a much more resource intensive and time-consuming operation for large tables. |
| . | `STALE_PERCENT` - Determines the percentage of rows in a table that have to change before the statistics on that table are deemed stale and should be regathered. The valid domain for `stale_percent` is non-negative numbers. The default value is 10%. |
| `pvalue` | Preference value. If `NULL` is specified, it will set the Oracle default value.s |

Exceptions

`ORA-20000`: Insufficient privileges

`ORA-20001`: Invalid or illegal input values

Usage Notes

- This setting is honored only of there is no preference specified for the table to be analyzed.
- To run this procedure, you need to have the `SYSDBA` or both `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privilege.
- Both arguments are of type `VARCHAR2` and values are enclosed in quotes, even when they represent numbers.

Examples

```
DBMS_STATS.SET_GLOBAL_PREFS('ESTIMATE_PERCENT','9');
DBMS_STATS.SET_GLOBAL_PREFS('DEGREE','99');
```

---

### SET\_INDEX\_STATS Procedures

These procedures set index-related information. In the version of this procedure that deals with user-defined statistics, the statistics type specified is the type to store in the dictionary, in addition to the actual user-defined statistics. If this statistics type is NULL, the statistics type associated with the index or column is stored.

Syntax

```
DBMS_STATS.SET_INDEX_STATS (
   ownname       VARCHAR2, 
   indname       VARCHAR2,
   partname      VARCHAR2  DEFAULT NULL,
   stattab       VARCHAR2  DEFAULT NULL, 
   statid        VARCHAR2  DEFAULT NULL,
   numrows       NUMBER    DEFAULT NULL, 
   numlblks      NUMBER    DEFAULT NULL,
   numdist       NUMBER    DEFAULT NULL, 
   avglblk       NUMBER    DEFAULT NULL,
   avgdblk       NUMBER    DEFAULT NULL, 
   clstfct       NUMBER    DEFAULT NULL,
   indlevel      NUMBER    DEFAULT NULL, 
   flags         NUMBER    DEFAULT NULL,
   statown       VARCHAR2  DEFAULT NULL,
   no_invalidate BOOLEAN   DEFAULT to_no_invalidate_type(
                                    get_param('NO_INVALIDATE')),
   guessq        NUMBER    DEFAULT NULL,
   cachedblk     NUMBER    DEFAULT NULL,
   cachehit      NUMBER    DEFUALT NULL,
   force         BOOLEAN   DEFAULT FALSE);
```

Use the following for user-defined statistics:

```
DBMS_STATS.SET_INDEX_STATS (
   ownname       VARCHAR2, 
   indname       VARCHAR2,
   partname      VARCHAR2  DEFAULT NULL,
   stattab       VARCHAR2  DEFAULT NULL, 
   statid        VARCHAR2  DEFAULT NULL,
   ext_stats     RAW,
   stattypown    VARCHAR2 DEFAULT NULL, 
   stattypname   VARCHAR2 DEFAULT NULL, 
   statown       VARCHAR2 DEFAULT NULL,
   no_invalidate BOOLEAN DEFAULT to_no_invalidate_type(
                                    get_param('NO_INVALIDATE')),
   cachedblk     NUMBER    DEFAULT NULL,
   cachehit      NUMBER    DEFUALT NULL,
   force         BOOLEAN   DEFAULT FALSE);
```

Parameters

Table 142-90 SET\_INDEX\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `indname` | Name of the index |
| `partname` | Name of the index partition in which to store the statistics. If the index is partitioned and if `partname` is `NULL`, then the statistics are stored at the global index level. |
| `stattab` | User statistics table identifier describing where to store the statistics. If `stattab` is `NULL`, then the statistics are stored directly in the dictionary. |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` (Only pertinent if `stattab` is not `NULL`) |
| `ext_stats` | User-defined statistics |
| `stattypown` | Schema of the statistics type |
| `stattypname` | Name of the statistics type |
| `numrows` | Number of rows in the index (partition) |
| `numlblks` | Number of leaf blocks in the index (partition) |
| `numdist` | Number of distinct keys in the index (partition) |
| `avglblk` | Average integral number of leaf blocks in which each distinct key appears for this index (partition). If not provided, then this value is derived from `numlblks` and `numdist`. |
| `avgdblk` | Average integral number of data blocks in the table pointed to by a distinct key for this index (partition). If not provided, then this value is derived from `clstfct` and `numdist`. |
| `clstfct` | See `clustering_factor` column of the `all_indexes` view for a description |
| `indlevel` | Height of the index (partition) |
| `flags` | For internal Oracle use (should be left as `NULL`) |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `guessq` | Guess quality. See the `pct_direct_access` column of the `all_indexes` view for a description. |
| `cachedblk` | The average number of blocks in the buffer cache for the segment (index/table/index partition/table partition) |
| `cachehit` | The average cache hit ratio for the segment (index/table/index partition/table partition) |
| `force` | Sets the values even if statistics of the index are locked |

Usage Notes

- To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- The Optimizer uses the cached data to estimate number of cached blocks for index or statistics table access. The total cost of the operation will be combined from the I/O cost of reading not cached blocks from disk, the CPU cost of getting cached blocks from the buffer cache, and the CPU cost of processing the data.
- Oracle maintains `cachedblk` and `cachehit` at all times but uses correspondent caching statistics for optimization as part of the table and index statistics only when the user calls `DBMS_STATS.GATHER_[TABLE/INDEX/SCHEMA/DATABASE]_STATS` procedure for auto mode or `DBMS_STATS.GATHER_SYSTEM_STATS` for manual mode. In order to prevent the user from utilizing inaccurate and unreliable data, the optimizer will compute a 'confidence factor' for each `cachehit` and a `cachedblk` for each object. If the 'confidence factor' for the value meets confidence criteria, this value will be used, otherwise the defaults will be used.
- The automatic maintenance algorithm for object caching statistics assumes that there is only one major workload for the system and adjusts statistics to this workload, ignoring other "minor" workloads. If this is not the case, you must use manual mode for maintaining object caching statistics.
- The object caching statistics maintenance algorithm for auto mode prevents you from using statistics in the following situations
	- When not enough data has been analyzed, such as when an object has been recently create
		- When the system does not have one major workload resulting in averages not corresponding to real values.

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid input value

`ORA-20005`: Object statistics are locked

---

### SET\_PARAM Procedure

Note:

This subprogram has been replaced by improved technology and is maintained only for purposes of backward compatibility. In this case, use the SET\_GLOBAL\_PREFS Procedure.

See also Deprecated Subprograms.

This procedure sets default values for parameters of `DBMS_STATS` procedures. You can use the `GET_PARAM` `Function` to get the current default value of a parameter.

Syntax

```
DBMS_STATS.SET_PARAM (
   pname      IN    VARCHAR2, 
   pval       IN    VARCHAR2);
```

Parameters

Table 142-91 SET\_PARAM Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pname` | The parameter name The default value for following parameters can be set.  - `CASCADE` - The default value for `CASCADE` set by `SET_PARAM` is not used by export/import procedures.It is used only by gather procedures. - `DEGREE` - `ESTIMATE_PERCENT` - `METHOD_OPT` - `NO_INVALIDATE` - `GRANULARITY` - `AUTOSTATS_TARGET` - This parameter is applicable only for auto statistics collection. The value of this parameter controls the objects considered for statistics collection (see `pval`) |
| `pval` | The parameter value. If `NULL` is specified, it will set the default value determined by Oracle. When `pname` is `AUTOSTATS_TARGET`, the following are valid values:  - `'ALL'` - Statistics are collected for all objects in the system - `'ORACLE'` - Statistics are collected for all Oracle owned objects - `'AUTO'` - Oracle decides for which objects to collect statistics |

Usage Notes

- To run this procedure, you must have the `SYSDBA` or both the `ANALYZE` `ANY` `DICTIONARY` and `ANALYZE` `ANY` system privileges.
- Note that both arguments are of type `VARCHAR2` and the values need to be enclosed in quotes even when they represent numbers.
- Note also the difference between `NULL` and `'NULL'`:
	- When `NULL` is unquoted, this sets the parameter to the value Oracle recommends.
		- In the case of the quoted `'NULL'`, this sets the value of the parameter to `NULL`.

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or illegal input value

Examples

```
DBMS_STATS.SET_PARAM('CASCADE','DBMS_STATS.AUTO_CASCADE');
DBMS_STATS.SET_PARAM('ESTIMATE_PERCENT','5');
DBMS_STATS.SET_PARAM('DEGREE','NULL');
```

---

### SET\_SCHEMA\_PREFS Procedure

This procedure is used to set the statistics preferences of all the tables owned by the specified owner name.

Syntax

```
DBMS_STATS.SET_SCHEMA_PREFS (
    ownname   IN   VARCHAR2,
    pname     IN   VARCHAR2,
    pvalue    IN   VARCHAR2);
```

Parameters

Table 142-92 SET\_SCHEMA\_PREFS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name |
| `pname` | Preference name. The default value for following parameters can be set:  - `CASCADE` - `DEGREE` - `ESTIMATE_PERCENT` - `METHOD_OPT` - `NO_INVALIDATE` - `GRANULARITY` - `PUBLISH` - `INCREMENTAL` - `STALE_PERCENT` |
| `pvalue` | Preference value. If `NULL` is specified, it will set the Oracle default value.s |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or illegal input value

Usage Notes

- To run this procedure, you need to connect as owner, or have the `SYSDBA` privilege, or have the `ANALYZE` `ANY` system privilege.
- Both arguments are of type `VARCHAR2` and values are enclosed in quotes, even when they represent numbers.

Examples

```
DBMS_STATS.SET_SCHEMA_PREFS('SH','CASCADE', 'DBMS_STATS.AUTO_CASCADE');
DBMS_STATS.SET_SCHEMA_PREFS('SH' 'ESTIMATE_PERCENT','9');
DBMS_STATS.SET_SCHEMA_PREFS('SH', 'DEGREE','99');
```

---

### SET\_SYSTEM\_STATS Procedure

This procedure sets systems statistics.

Syntax

```
DBMS_STATS.SET_SYSTEM_STATS (
   pname          VARCHAR2,
   pvalue         NUMBER,
   stattab   IN   VARCHAR2 DEFAULT NULL, 
   statid    IN   VARCHAR2 DEFAULT NULL,
   statown   IN   VARCHAR2 DEFAULT NULL);
```

Parameters

Table 142-93 SET\_SYSTEM\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pname` | The parameter name to get, which can have one of the following values:  - `iotfrspeed` —I/O transfer speed in bytes for each millisecond - `ioseektim` - Seek time + latency time + operating system overhead time, in milliseconds - `sreadtim` - Average time to read single block (random read), in milliseconds - `mreadtim` - Average time to read an mbrc block at once (sequential read), in milliseconds - `cpuspeed` - Average number of CPU cycles for each second, in millions, captured for the workload (statistics collected using ' `INTERVAL` ' or ' `START` ' and ' `STOP` ' options) - `cpuspeednw` - Average number of CPU cycles for each second, in millions, captured for the noworkload (statistics collected using ' `NOWORKLOAD` ' option. - `mbrc` - Average multiblock read count for sequential read, in blocks - `maxthr` - Maximum I/O system throughput, in bytes/second - `slavethr` - Average slave I/O throughput, in bytes/second |
| `pvalue` | Parameter value to get |
| `stattab` | Identifier of the user statistics table where the statistics will be obtained. If stattab is null, the statistics will be obtained from the dictionary. |
| `statid` | Optional identifier associated with the statistics saved in the stattab |
| `statown` | Schema containing `stattab` (if different from current schema) |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid input value

`ORA-20002`: Bad user statistics table; may need to be upgraded

`ORA-20003`: Unable to set system statistics

`ORA-20004`: Parameter does not exist

Usage Notes

To run this procedure, you need the `GATHER_SYSTEM_STATISTICS` role.

---

### SET\_TABLE\_PREFS Procedure

This procedure is used to set the statistics preferences of the specified table in the specified schema.

Syntax

```
DBMS_STATS.SET_TABLE_PREFS (
    ownname    IN  VARCHAR2,
    tabname    IN  VARCHAR2,
    pname      IN  VARCHAR2,
    pvalue     IN  VARCHAR2);
```

Parameters

Table 142-94 SET\_TABLE\_PREFS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name |
| `tabname` | Table name |
| `pname` | Preference name. The default value for following preferences can be set:  - `CASCADE` - `DEGREE` - `ESTIMATE_PERCENT` - `METHOD_OPT` - `NO_INVALIDATE` - `GRANULARITY` - `PUBLISH` - `INCREMENTAL` - `STALE_PERCENT` |
| . | `CASCADE` - Determines whether or not index statistics are collected as part of gathering table statistics`.` |
| . | `DEGREE` - Determines degree of parallelism used for gathering statistics. |
| . | `ESTIMATE_PERCENT` - Determines the percentage of rows to estimate. The valid range is \[0.000001,100\]. Use the constant `DBMS_STATS`.`AUTO_SAMPLE_SIZE` to have Oracle determine the appropriate sample size for good statistics. This is the default. |
| . | `METHOD_OPT` - Controls column statistics collection and histogram creation. It accepts either of the following options, or both in combination:  - `FOR ALL [INDEXED \| HIDDEN] COLUMNS` `[size_clause]` - `FOR COLUMNS [size clause] column [size_clause] [,column [size_clause]...]`  `size_clause` is defined as `size_clause := SIZE {integer \| REPEAT \| AUTO \| SKEWONLY}`  `column` is defined as `column := column_name \| extension name \| extension`     `- integer`: Number of histogram buckets. Must be in the range \[1,254\].   `- REPEAT`: Collects histograms only on the columns that already have histograms   `- AUTO`: Oracle determines the columns on which to collect histograms based on data distribution and the workload of the columns.   `- SKEWONLY`: Oracle determines the columns on which to collect histograms based on the data distribution of the columns.   \- `column_name`: Name of a column   \- `extension :` Can be either a column group in the format of `(column_name, colume_name [, ...])` or an expression  The default is `FOR ALL COLUMNS SIZE AUTO`. |
| . | `NO_INVALIDATE` - The value controls the invalidation of dependent cursors of the tables for which statistics are being gathered. Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE` to have Oracle decide when to invalidate dependent cursors. This is the default. |
| . | `GRANULARITY` - Determines granularity of statistics to collect (only pertinent if the table is partitioned).  `'ALL'` - Gathers all (subpartition, partition, and global) statistics  `'AUTO'` - Determines the granularity based on the partitioning type. This is the default value.  `'DEFAULT'` - Gathers global and partition-level statistics. This option is obsolete, and while currently supported, it is included in the documentation for legacy reasons only. You should use the ' `GLOBAL AND PARTITION` ' for this functionality. Note that the default value is now ' `AUTO` '.  `'GLOBAL'` - Gathers global statistics  ' `GLOBAL AND PARTITION` ' - Gathers the global and partition level statistics. No subpartition level statistics are gathered even if it is a composite partitioned object.  `'PARTITION` '- Gathers partition-level statistics  `'SUBPARTITION'` - Gathers subpartition-level statistics. |
| . | `PUBLISH` - Determines whether or not newly gathered statistics will be published once the gather job has completed. Prior to Oracle Database 11g, Release 1 (11.1), once a statistic gathering job completed the new statistics were automatically published into the dictionary tables. The user now has the ability to gather statistics but not publish them immediately. This allows the DBA to test the new statistics before publishing them. |
| . | `INCREMENTAL` - Determines whether or not the global statistics of a partitioned table will be maintained without doing a full table scan. With partitioned tables it is very common to load new data into a new partition. As new partitions are added and data loaded, the global table statistics need to be kept up to date. Oracle will update the global table statistics by scanning only the partitions that have been changed instead of the entire table if the following conditions hold:  - `INCREMENTAL` value for the partitioned table is set to `TRUE`; - `PUBLISH` value for the partitioned table is set to `TRUE`; - User specifies `AUTO_SAMPLE_SIZE` for `ESTIMATE_PERCENT` and `AUTO` for `GRANULARITY` when gathering statistics on the table.  If the `INCREMENTAL` value for the partitioned table was set to `FALSE` (default value), a full table scan is used to maintain the global statistics which is a much more resource intensive and time-consuming operation for large tables. |
| . | `STALE_PERCENT` - Determines the percentage of rows in a table that have to change before the statistics on that table are deemed stale and should be regathered. The valid domain for `stale_percent` is non-negative numbers. The default value is 10%. |
| pvalue | Preference value. If `NULL` is specified, it will set the Oracle default value. |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid or illegal input values

Usage Notes

- To run this procedure, you need to connect as owner of the table or should have the `ANALYZE` `ANY` system privilege.
- All arguments are of type `VARCHAR2` and values are enclosed in quotes, even when they represent numbers.

Examples

```
DBMS_STATS.SET_TABLE_PREFS('SH', 'SALES', 'CASCADE', 'DBMS_STATS.AUTO_CASCADE');
DBMS_STATS.SET_TABLE_PREFS('SH', 'SALES','ESTIMATE_PERCENT','9');
DBMS_STATS.SET_TABLE_PREFS('SH', 'SALES', 'DEGREE','99');
```

---

### SET\_TABLE\_STATS Procedure

This procedure sets table-related information.

Syntax

```
DBMS_STATS.SET_TABLE_STATS (
   ownname       VARCHAR2, 
   tabname       VARCHAR2, 
   partname      VARCHAR2 DEFAULT NULL,
   stattab       VARCHAR2 DEFAULT NULL, 
   statid        VARCHAR2 DEFAULT NULL,
   numrows       NUMBER   DEFAULT NULL, 
   numblks       NUMBER   DEFAULT NULL,
   avgrlen       NUMBER   DEFAULT NULL, 
   flags         NUMBER   DEFAULT NULL,
   statown       VARCHAR2 DEFAULT NULL,
   no_invalidate BOOLEAN  DEFAULT to_no_invalidate_type (
                                     get_param('NO_INVALIDATE')),
   cachedblk     NUMBER    DEFAULT NULL,
   cachehit      NUMBER    DEFUALT NULL,
   force         BOOLEAN   DEFAULT FALSE);
```

Parameters

Table 142-95 SET\_TABLE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `tabname` | Name of the table |
| `partname` | Name of the table partition in which to store the statistics. If the table is partitioned and `partname` is `NULL`, then the statistics are stored at the global table level. |
| `stattab` | User statistics table identifier describing where to store the statistics. If `stattab` is `NULL`, then the statistics are stored directly in the dictionary. |
| `statid` | Identifier (optional) to associate with these statistics within `stattab` (Only pertinent if `stattab` is not `NULL`) |
| `numrows` | Number of rows in the table (partition) |
| `numblks` | Number of blocks the table (partition) occupies |
| `avgrlen` | Average row length for the table (partition) |
| `flags` | For internal Oracle use (should be left as `NULL`) |
| `statown` | Schema containing `stattab` (if different than `ownname`) |
| `no_invalidate` | Does not invalidate the dependent cursors if set to `TRUE`. The procedure invalidates the dependent cursors immediately if set to `FALSE`. Use `DBMS_STATS`.`AUTO_INVALIDATE`. to have Oracle decide when to invalidate dependent cursors. This is the default. The default can be changed using the SET\_DATABASE\_PREFS Procedure, SET\_GLOBAL\_PREFS Procedure, SET\_SCHEMA\_PREFS Procedure and SET\_TABLE\_PREFS Procedure. |
| `cachedblk` | The average number of blocks in the buffer cache for the segment (index/table/index partition/table partition) |
| `cachehit` | The average cache hit ratio for the segment (index/table/index partition/table partition) |
| `force` | Sets the values even if statistics of the table are locked |

Usage Notes

- To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- The Optimizer uses the cached data to estimate number of cached blocks for index or statistics table access. The total cost of the operation will be combined from the I/O cost of reading not cached blocks from disk, the CPU cost of getting cached blocks from the buffer cache, and the CPU cost of processing the data.
- Oracle maintains `cachedblk` and `cachehit` at all times but uses correspondent caching statistics for optimization as part of the table and index statistics only when the user calls `DBMS_STATS.GATHER_[TABLE/INDEX/SCHEMA/DATABASE]_STATS` procedure for auto mode or `DBMS_STATS.GATHER_SYSTEM_STATS` for manual mode. In order to prevent the user from utilizing inaccurate and unreliable data, the optimizer will compute a 'confidence factor' for each `cachehit` and a `cachedblk` for each object. If the 'confidence factor' for the value meets confidence criteria, this value will be used, otherwise the defaults will be used.
- The automatic maintenance algorithm for object caching statistics assumes that there is only one major workload for the system and adjusts statistics to this workload, ignoring other "minor" workloads. If this is not the case, you must use manual mode for maintaining object caching statistics.
- The object caching statistics maintenance algorithm for auto mode prevents you from using statistics in the following situations
	- When not enough data has been analyzed, such as when an object has been recently create
		- When the system does not have one major workload resulting in averages not corresponding to real values.

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Invalid input value

`ORA-20005`: Object statistics are locked

---

### SHOW\_EXTENDED\_STATS\_NAME Function

This function returns the name of the statistics entry that is created for the user-specified extension. It raises an error if no extension has been created.

Syntax

```
DBMS_STATS.SHOW_EXTENDED_STATS_NAME (
   ownname    VARCHAR2, 
   tabname    VARCHAR2,
   extension  VARCHAR2)
 RETURN VARCHAR2;
```

Parameters

Table 142-96 SHOW\_EXTENDED\_STATS\_NAME Function Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Owner name of a table |
| `tabname` | Name of the table |
| `extension` | Can be either a column group or an expression. Suppose the specified table has two column `c1`, `c2`. An example column group can be "(`c1`, `c2`)" and an example expression can be "(`c1` + `c2`)". |

Exceptions

`ORA-20000`: Object does not exist or insufficient privileges

`ORA-20001`: Error when processing extension

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

---

### UNLOCK\_PARTITION\_STATS Procedure

This procedure enables the user to unlock statistics for a partition.

Syntax

```
DBMS_STATS.UNLOCK_PARTITION_STATS (
    ownname    VARCHAR2,
    tabname    VARCHAR2,
    partname   VARCHAR2);
```

Parameters

Table 142-97 UNLOCK\_PARTITION\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema to unlock |
| `tabname` | Name of the table |
| `partname` | Partition name |

Usage Notes

To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.

---

### UNLOCK\_SCHEMA\_STATS Procedure

This procedure unlocks the statistics on all the tables in schema.

Syntax

```
DBMS_STATS.UNLOCK_SCHEMA_STATS (
   ownname    VARCHAR2);
```

Parameters

Table 142-98 UNLOCK\_SCHEMA\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | The name of the schema |

Usage Notes

- To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- When statistics on a table is locked, all the statistics depending on the table, including table statistics, column statistics, histograms and statistics on all dependent indexes, are considered to be locked.
- The `SET_*,` `DELETE_*,` `IMPORT_*,` `GATHER_*` procedures that modify statistics in the dictionary of an individual table, index or column will raise an error if statistics of the object is locked.
- Procedures that operates on multiple objects (such as `GATHER_SCHEMA_STATS`) will skip modifying the statistics of an object if it is locked. Many procedures have force argument to override the lock.

---

### UNLOCK\_TABLE\_STATS Procedure

This procedure unlocks the statistics on the table.

Syntax

```
DBMS_STATS.UNLOCK_TABLE_STATS (
   ownname    VARCHAR2,
   tabname    VARCHAR2);
```

Parameters

Table 142-99 UNLOCK\_TABLE\_STATS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | The name of the schema |
| `tabname` | The name of the table |

Usage Notes

- To invoke this procedure you must be owner of the table, or you need the `ANALYZE` `ANY` privilege. For objects owned by `SYS`, you need to be either the owner of the table, or you need the `ANALYZE` `ANY` `DICTIONARY` privilege or the `SYSDBA` privilege.
- When statistics on a table is locked, all the statistics depending on the table, including table statistics, column statistics, histograms and statistics on all dependent indexes, are considered to be locked.
- The `SET_*,` `DELETE_*,` `IMPORT_*,` `GATHER_*` procedures that modify statistics in the dictionary of an individual table, index or column will raise an error if statistics of the object is locked.
- Procedures that operates on multiple objects (such as `GATHER_SCHEMA_STATS`) will skip modifying the statistics of an object if it is locked. Many procedures have force argument to override the lock.

---

### UPGRADE\_STAT\_TABLE Procedure

This procedure upgrades a user statistics table from an older version.

Syntax

```
DBMS_STATS.UPGRADE_STAT_TABLE (
   ownname    VARCHAR2,
   stattab    VARCHAR2);
```

Parameters

Table 142-100 UPGRADE\_STAT\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownname` | Name of the schema |
| `stattab` | Name of the table |

Exceptions

`ORA-20000`: Unable to upgrade table

Usage Notes

To invoke this procedure you need the privileges to drop and create a table.