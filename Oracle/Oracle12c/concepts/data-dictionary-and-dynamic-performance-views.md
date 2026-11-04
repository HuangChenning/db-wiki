---
title: Database Concepts
book: Database Concepts
doc_id: E85769-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/cncpt/data-dictionary-and-dynamic-performance-views.html
tags:
  - oracle
  - 12c
  - concepts
---

The central set of read-only reference tables and views of each Oracle database is known collectively as the data dictionary. The dynamic performance views are special views that are continuously updated while a database is open and in use.

This chapter contains the following sections:

### Overview of the Data Dictionary

An important part of an Oracle database is its data dictionary, which is a read-only set of tables that provides administrative metadata about the database.

A data dictionary contains information such as the following:

- The definitions of every [schema object](glossary.md) in the database, including default values for columns and integrity constraint information
- The amount of space allocated for and currently used by the schema objects
- The names of Oracle Database users, privileges and roles granted to users, and auditing information related to users

The data dictionary is a central part of data management for every Oracle database. For example, the database performs the following actions:

- Accesses the data dictionary to find information about users, schema objects, and storage structures
- Modifies the data dictionary every time that a DDL statement is issued

Because Oracle Database stores data dictionary data in tables, just like other data, users can [query](glossary.md) the data with SQL. For example, users can run `SELECT` statements to determine their privileges, which tables exist in their schema, which columns are in these tables, whether indexes are built on these columns, and so on.

See Also:

- " [Introduction to Schema Objects](tables-and-table-clusters.md) "
- " [User Accounts](topics-for-database-administrators-and-developers.md) "
- " [Data Definition Language (DDL) Statements](sql.md) "

#### Contents of the Data Dictionary

The data dictionary consists of base tables and views.

These objects are defined as follows:

- Base tables
	These store information about the database. Only Oracle Database should write to and read these tables. Users rarely access the base tables directly because they are normalized and most data is stored in a cryptic format.
- Views
	These decode the base table data into useful information, such as user or table names, using joins and `WHERE` clauses to simplify the information. The views contain the names and description of all objects in the data dictionary. Some views are accessible to all database users, whereas others are intended for administrators only.

Typically, data dictionary views are grouped in sets. In many cases, a set consists of three views containing similar information and distinguished from each other by their prefixes, as shown in the following table. By querying the appropriate views, you can access only the information relevant for you.

Table 6-1 Data Dictionary View Sets

| Prefix | User Access | Contents | Notes |
| --- | --- | --- | --- |
| `DBA_` | Database administrators | All objects | Some `DBA_` views have additional columns containing information useful to the administrator. |
| `ALL_` | All users | Objects to which user has privileges | Includes objects owned by user. These views obey the current set of enabled roles. |
| `USER_` | All users | Objects owned by user | Views with the prefix `USER_` usually exclude the column `OWNER`. This column is implied in the `USER_` views to be the user issuing the query. |

Not all views sets have three members. For example, the data dictionary contains a `DBA_LOCK` view but no `ALL_LOCK` view.

The system-supplied `DICTIONARY` view contains the names and abbreviated descriptions of all data dictionary views. The following query of this view includes partial sample output:

```
SQL> SELECT * FROM DICTIONARY
  2  ORDER BY TABLE_NAME;

TABLE_NAME                     COMMENTS
------------------------------ ----------------------------------------
ALL_ALL_TABLES                 Description of all object and relational
                               tables accessible to the user
 
ALL_APPLY                      Details about each apply process that
                               dequeues from the queue visible to the
                               current user
.
.
.
```

See Also:

- " [Overview of Views](partitions-views-and-other-schema-objects.md) "
- [Oracle Database Reference](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/cncpt&id=GUID-8865F65B-EF6D-44A5-B0A1-3179EFF0C36A) for a complete list of data dictionary views and their columns

##### Views with the Prefix DBA\_

Views with the prefix `DBA_` show all relevant information in the entire database. `DBA_` views are intended only for administrators.

The following sample query shows information about all objects in the database:

```
SELECT OWNER, OBJECT_NAME, OBJECT_TYPE
FROM   DBA_OBJECTS
ORDER BY OWNER, OBJECT_NAME;
```

See Also:

[Oracle Database Administrator’s Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/cncpt&id=ADMIN11047) for detailed information on administrative privileges

##### Views with the Prefix ALL\_

Views with the prefix `ALL_` refer to the user's overall perspective of the database.

These views return information about schema objects to which the user has access through public or explicit grants of privileges and roles, in addition to schema objects that the user owns.

For example, the following query returns information about all the objects to which you have access:

```
SELECT OWNER, OBJECT_NAME, OBJECT_TYPE 
FROM   ALL_OBJECTS
ORDER BY OWNER, OBJECT_NAME;
```

Because the `ALL_` views obey the current set of enabled roles, query results depend on which roles are enabled, as shown in the following example:

```
SQL> SET ROLE ALL;
 
Role set.
 
SQL> SELECT COUNT(*) FROM ALL_OBJECTS;
 
COUNT(*)
----------
68295
 
SQL> SET ROLE NONE;
 
Role set.
 
SQL> SELECT COUNT(*) FROM ALL_OBJECTS;
 
COUNT(*)
----------
53771
```

Application developers should be cognizant of the effect of roles when using `ALL_` views in a [stored procedure](glossary.md), where roles are not enabled by default.

##### Views with the Prefix USER\_

The views most likely to be of interest to typical database users are those with the prefix `USER_`.

These views:

- Refer to the user's private environment in the database, including metadata about schema objects created by the user, grants made by the user, and so on
- Display only rows pertinent to the user, returning a subset of the information in the `ALL_` views
- Has columns identical to the other views, except that the column `OWNER` is implied
- Can have abbreviated `PUBLIC` synonyms for convenience

For example, the following query returns all the objects contained in your schema:

```
SELECT OBJECT_NAME, OBJECT_TYPE 
FROM   USER_OBJECTS
ORDER BY OBJECT_NAME;
```

##### The DUAL Table

`DUAL` is a small table in the data dictionary that Oracle Database and user-written programs can reference to guarantee a known result.

The dual table is useful when a value must be returned only once, for example, the current date and time. All database users have access to `DUAL`.

The `DUAL` table has one column called `DUMMY` and one row containing the value `X`. The following example queries `DUAL` to perform an arithmetical operation:

```
SQL> SELECT ((3*4)+5)/3 FROM DUAL;
 
((3*4)+5)/3
-----------
 5.66666667
```

See Also:

[Oracle Database SQL Language Reference](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/cncpt&id=SQLRF20036) for more information about the `DUAL` table

#### Storage of the Data Dictionary

The data dictionary base tables are the first objects created in any Oracle database.

All data dictionary tables and views for a database are stored in the `SYSTEM` tablespace. Because the `SYSTEM` tablespace is always online when the database is open, the data dictionary is always available when the database is open.

See Also:

" [The SYSTEM Tablespace](logical-storage-structures.md) " for more information about the `SYSTEM` tablespace

#### How Oracle Database Uses the Data Dictionary

The Oracle Database user account `SYS` owns all base tables and user-accessible views of the data dictionary.

During database operation, Oracle Database reads the data dictionary to ascertain that schema objects exist and that users have proper access to them. Oracle Database updates the data dictionary continuously to reflect changes in database structures, auditing, grants, and data.

For example, if user `hr` creates a table named `interns`, then the database adds new rows to the data dictionary that reflect the new table, columns, segment, extents, and the privileges that `hr` has on the table. This new information is visible the next time the dictionary views are queried.

Data in the base tables of the data dictionary is necessary for Oracle Database to function. Only Oracle Database should write or change data dictionary information. No Oracle Database user should ever alter rows or schema objects contained in the `SYS` schema because such activity can compromise [data integrity](glossary.md). The security administrator must keep strict control of this central account.

WARNING:

Altering or manipulating the data in data dictionary tables can permanently and detrimentally affect database operation.

See Also:

" [SYS and SYSTEM Schemas](tables-and-table-clusters.md) "

##### Public Synonyms for Data Dictionary Views

Oracle Database creates public synonyms for many data dictionary views so users can access them conveniently.

The security administrator can also create additional public synonyms for schema objects that are used systemwide. Oracle recommends against using the same name for a private schema object and a public synonym.

See Also:

" [Overview of Synonyms](partitions-views-and-other-schema-objects.md) "

##### Data Dictionary Cache

Much of the data dictionary information is in the data dictionary cache because the database constantly requires the information to validate user access and verify the state of schema objects..

The caches typically contain the parsing information. The `COMMENTS` columns describing the tables and their columns are not cached in the dictionary cache, but may be cached in the database buffer cache

See Also:

" [Data Dictionary Cache](memory-architecture.md) "

##### Other Programs and the Data Dictionary

Other Oracle Database products can reference existing views and create additional data dictionary tables or views of their own.

Oracle recommends that application developers who write programs referring to the data dictionary use the public synonyms rather than the underlying tables. Synonyms are less likely to change between releases.

### Overview of the Dynamic Performance Views

Throughout its operation, Oracle Database maintains a set of virtual tables that record current database activity.

These views are dynamic because they are continuously updated while a database is open and in use. The views are sometimes called V$ views because their names begin with `V$`.

Dynamic performance views contain information such as the following:

- System and [session](glossary.md) parameters
- Memory usage and allocation
- File states (including [RMAN](glossary.md) backup files)
- Progress of jobs and tasks
- SQL execution
- Statistics and metrics

The dynamic performance views have the following primary uses:

- [Oracle Enterprise Manager](glossary.md) uses the views to obtain information about the database.
- Administrators can use the views for performance monitoring and debugging.

See Also:

- " [Oracle Enterprise Manager](concepts-for-database-administrators.md) "
- [Oracle Database Reference](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/cncpt&id=REFRN003) for a complete list of the dynamic performance views

#### Contents of the Dynamic Performance Views

Dynamic performance views are called fixed views because they cannot be altered or removed by a database administrator. However, database administrators can query and create views on the tables and grant access to these views to other users.

`SYS` owns the dynamic performance tables, whose names begin with `V_$`. Views are created on these tables, and then public synonyms prefixed with `V$`. For example, the `V$DATAFILE` view contains information about data files. The `V$FIXED_TABLE` view contains information about all of the dynamic performance tables and views.

For almost every `V$` view, a corresponding `GV$` view exists. In Oracle Real Application Clusters (Oracle RAC), querying a `GV$` view retrieves the `V$` view information from all qualified database instances.

When you use the Database Configuration Assistant (DBCA) to create a database, Oracle automatically creates the data dictionary. Oracle Database automatically runs the `catalog.sql` script, which contains definitions of the views and public synonyms for the dynamic performance views. You must run `catalog.sql` to create these views and synonyms.

See Also:

- " [Database Server Grid](topics-for-database-administrators-and-developers.md) "
- " [Tools for Database Installation and Configuration](concepts-for-database-administrators.md) " to learn about DBCA
- [Oracle Database Administrator’s Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/cncpt&id=ADMIN11082) to learn how to run `catalog.sql` manually
- [Oracle Real Application Clusters Administration and Deployment Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/cncpt&id=RACAD718) to learn about using performance views in Oracle RAC

#### Storage of the Dynamic Performance Views

Dynamic performance views are based on virtual tables built from database memory structures.

The views are not conventional tables stored in the database. Read consistency is not guaranteed for the views because the data is updated dynamically.

Because the dynamic performance views are not true tables, the data depends on the state of the database and [database instance](glossary.md). For example, you can query `V$INSTANCE` and `V$BGPROCESS` when the database is started but not mounted. However, you cannot query `V$DATAFILE` until the database has been mounted.

See Also:

" [Data Concurrency and Consistency](data-concurrency-and-consistency.md) "

### Database Object Metadata

The `DBMS_METADATA` package provides interfaces for extracting complete definitions of database objects.

The definitions can be expressed either as XML or as SQL DDL. Oracle Database provides two styles of interface: a flexible, sophisticated interface for programmatic control, and a simplified interface for ad hoc querying.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/cncpt&id=ARPLS026) for more information about `DBMS_METADATA`