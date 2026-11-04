---
title: External Tables Concepts
book: Utilities
doc_id: E22490-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e22490/et_concepts.htm
tags:
  - oracle
  - 11g
  - utilities
---

## 13 External Tables Concepts

The external tables feature is a complement to existing SQL\*Loader functionality. It enables you to access data in external sources as if it were in a table in the database.

Note that SQL\*Loader may be the better choice in data loading situations that require additional indexing of the staging table. See ["Behavior Differences Between SQL\*Loader and External Tables"](ldr_concepts.md) for more information about how load behavior differs between SQL\*Loader and external tables.

This chapter discusses the following topics:

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tables.htm#ADMIN01507) for additional information about creating and managing external tables

## How Are External Tables Created?

External tables are created using the SQL `CREATE` `TABLE...ORGANIZATION EXTERNAL` statement. When you create an external table, you specify the following attributes:

- `TYPE` - specifies the type of external table. The two available types are the `ORACLE_LOADER` type and the `ORACLE_DATAPUMP` type. Each type of external table is supported by its own access driver.
	- The `ORACLE_LOADER` access driver is the default. It loads data from external tables to internal tables. The data must come from text data files. (The `ORACLE_LOADER` access driver cannot perform unloads; that is, it cannot move data from an internal table to an external table.)
		- The `ORACLE_DATAPUMP` access driver can perform both loads and unloads. The data must come from binary dump files. Loads to internal tables from external tables are done by fetching from the binary dump files. Unloads from internal tables to external tables are done by populating the binary dump files of the external table. The `ORACLE_DATAPUMP` access driver can write dump files only as part of creating an external table with the SQL `CREATE TABLE AS SELECT` statement. Once the dump file is created, it can be read any number of times, but it cannot be modified (that is, no DML operations can be performed).
- `DEFAULT` `DIRECTORY` - specifies the default directory to use for all input and output files that do not explicitly name a directory object. The location is specified with a directory object, not a directory path. You must create the directory object before you create the external table; otherwise, an error is generated. See "Location of Data Files and Output Files" for more information.
- `ACCESS` `PARAMETERS` - describe the external data source and implements the type of external table that was specified. Each type of external table has its own access driver that provides access parameters unique to that type of external table. Access parameters are optional. See "Access Parameters".
- `LOCATION` - specifies the data files for the external table. The files are named in the form `directory:file`. The `directory` portion is optional. If it is missing, then the default directory is used as the directory for the file.

The following example shows the use of each of these attributes (it assumes that the default directory `def_dir1` already exists):

```
SQL> CREATE TABLE emp_load
  2    (employee_number      CHAR(5),
  3     employee_dob         CHAR(20),
  4     employee_last_name   CHAR(20),
  5     employee_first_name  CHAR(15),
  6     employee_middle_name CHAR(15),
  7     employee_hire_date   DATE)
  8  ORGANIZATION EXTERNAL
  9    (TYPE ORACLE_LOADER
 10     DEFAULT DIRECTORY def_dir1
 11     ACCESS PARAMETERS
 12       (RECORDS DELIMITED BY NEWLINE
 13        FIELDS (employee_number      CHAR(2),
 14                employee_dob         CHAR(20),
 15                employee_last_name   CHAR(18),
 16                employee_first_name  CHAR(11),
 17                employee_middle_name CHAR(11),
 18                employee_hire_date   CHAR(10) date_format DATE mask "mm/dd/yyyy"
 19               )
 20       )
 21     LOCATION ('info.dat')
 22    );
 
Table created.
```

The information you provide through the access driver ensures that data from the data source is processed so that it matches the definition of the external table. The fields listed after `CREATE` `TABLE` `emp_load` are actually defining the metadata for the data in the `info`.`dat` source file.

See Also:

["Example: Creating and Loading an External Table Using ORACLE\_LOADER"](et_params.md)

### Location of Data Files and Output Files

The access driver runs inside the database server. This is different from SQL\*Loader, which is a client program that sends the data to be loaded over to the server. This difference has the following implications:

- The server must have access to any files to be loaded by the access driver.
- The server must create and write the output files created by the access driver: the log file, bad file, discard file, and also any dump files created by the `ORACLE_DATAPUMP` access driver.

The access driver requires that a directory object be used to specify the location from which to read and write files. A directory object maps a name to a directory name on the file system. For example, the following statement creates a directory object named `ext_tab_dir` that is mapped to a directory located at `/usr/apps/datafiles.`

```
CREATE DIRECTORY ext_tab_dir AS '/usr/apps/datafiles';
```

Directory objects can be created by DBAs or by any user with the `CREATE` `ANY` `DIRECTORY` privilege.

Note:

To use external tables in an Oracle Real Applications Cluster (Oracle RAC) configuration, you must ensure that the directory object path is on a cluster-wide file system.

After a directory is created, the user creating the directory object needs to grant `READ` and `WRITE` privileges on the directory to other users. These privileges must be explicitly granted, rather than assigned through the use of roles. For example, to allow the server to read files on behalf of user `scott` in the directory named by `ext_tab_dir`, the user who created the directory object must execute the following command:

```
GRANT READ ON DIRECTORY ext_tab_dir TO scott;
```

The `SYS` user is the only user that can own directory objects, but the `SYS` user can grant other users the privilege to create directory objects. Note that `READ` or `WRITE` permission to a directory object means only that the Oracle database will read or write that file on your behalf. You are not given direct access to those files outside of the Oracle database unless you have the appropriate operating system privileges. Similarly, the Oracle database requires permission from the operating system to read and write files in the directories.

### Access Parameters

When you create an external table of a particular type, you can specify access parameters to modify the default behavior of the access driver. Each access driver has its own syntax for access parameters. Oracle provides two access drivers for use with external tables: `ORACLE_LOADER` and `ORACLE_DATAPUMP`.

Note:

These access parameters are collectively referred to as the `opaque_format_spec` in the SQL `CREATE TABLE...ORGANIZATION EXTERNAL` statement.

See Also:

- [Chapter 14, "The ORACLE\_LOADER Access Driver"](et_params.md)
- [Chapter 15, "The ORACLE\_DATAPUMP Access Driver"](et_dp_driver.md)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_7002.htm#SQLRF01402) for information about specifying `opaque_format_spec` when using the SQL `CREATE TABLE` statement

## Datatype Conversion During External Table Use

When data is moved into or out of an external table, it is possible that the same column will have a different datatype in each of the following three places:

- The database: This is the source when data is unloaded into an external table and it is the destination when data is loaded from an external table.
- The external table: When data is unloaded into an external table, the data from the database is converted, if necessary, to match the datatype of the column in the external table. Also, you can apply SQL operators to the source data to change its datatype before the data gets moved to the external table. Similarly, when loading from the external table into a database, the data from the external table is automatically converted to match the datatype of the column in the database. Again, you can perform other conversions by using SQL operators in the SQL statement that is selecting from the external table. For better performance, the datatypes in the external table should match those in the database.
- The data file: When you unload data into an external table, the datatypes for fields in the data file exactly match the datatypes of fields in the external table. However, when you load data from the external table, the datatypes in the data file may not match the datatypes in the external table. In this case, the data from the data file is converted to match the datatypes of the external table. If there is an error converting a column, then the record containing that column is not loaded. For better performance, the datatypes in the data file should match the datatypes in the external table.

Any conversion errors that occur between the data file and the external table cause the row with the error to be ignored. Any errors between the external table and the column in the database (including conversion errors and constraint violations) cause the entire operation to terminate unsuccessfully.

When data is unloaded into an external table, data conversion occurs if the datatype of a column in the source table does not match the datatype of the column in the external table. If a conversion error occurs, then the data file may not contain all the rows that were processed up to that point and the data file will not be readable. To avoid problems with conversion errors causing the operation to fail, the datatype of the column in the external table should match the datatype of the column in the database. This is not always possible, because external tables do not support all datatypes. In these cases, the unsupported datatypes in the source table must be converted into a datatype that the external table can support. For example, if a source table named `LONG_TAB` has a `LONG` column, then the corresponding column in the external table being created, `LONG_TAB_XT`, must be a `CLOB` and the `SELECT` subquery that is used to populate the external table must use the `TO_LOB` operator to load the column:

```
CREATE TABLE LONG_TAB_XT (LONG_COL CLOB) ORGANIZATION EXTERNAL...SELECT TO_LOB(LONG_COL) FROM LONG_TAB;
```

## External Table Restrictions

This section lists what the external tables feature does not do and also describes some processing restrictions.

- Exporting and importing of external tables with encrypted columns is not supported.
- An external table does not describe any data that is stored in the database.
- An external table does not describe how data is stored in the external source. This is the function of the access parameters.
- Column processing: By default, the external tables feature fetches all columns defined for an external table. This guarantees a consistent result set for all queries. However, for performance reasons you can decide to process only the referenced columns of an external table, thus minimizing the amount of data conversion and data handling required to execute a query. In this case, a row that is rejected because a column in the row causes a datatype conversion error will not get rejected in a different query if the query does not reference that column. You can change this column-processing behavior with the `ALTER TABLE` command.
- An external table cannot load data into a `LONG` column.
- SQL strings cannot be specified in access parameters for the `ORACLE_LOADER` access driver. As a workaround, you can use the `DECODE` clause in the `SELECT` clause of the statement that is reading the external table. Alternatively, you can create a view of the external table that uses the `DECODE` clause and select from that view rather than the external table.
- When identifiers (for example, column or table names) are specified in the external table access parameters, certain values are considered to be reserved words by the access parameter parser. If a reserved word is used as an identifier, then it must be enclosed in double quotation marks.