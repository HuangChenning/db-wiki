---
title: Original Export
book: Utilities
doc_id: E22490-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e22490/original_export.htm
tags:
  - oracle
  - 11g
  - utilities
---

## 21 Original Export

This chapter describes how to use the original Export utility (`exp`) to write data from an Oracle database into an operating system file in binary format. This file is stored outside the database, and it can be read into another Oracle database using the original Import utility.

Note:

Original Export is desupported for general use as of Oracle Database 11g. The only supported use of original Export in Oracle Database 11g is backward migration of XMLType data to Oracle Database 10g release 2 (10.2) or earlier. Therefore, Oracle recommends that you use the new Data Pump Export and Import utilities, except in the following situations which require original Export and Import:
- You want to import files that were created using the original Export utility (`exp`).
- You want to export files that will be imported using the original Import utility (`imp`). An example of this would be if you wanted to export data from Oracle Database 10g and then import it into an earlier database release.

The following topics are discussed in this chapter:

## What is the Export Utility?

The Export utility provides a simple way for you to transfer data objects between Oracle databases, even if they reside on platforms with different hardware and software configurations.

When you run Export against an Oracle database, objects (such as tables) are extracted, followed by their related objects (such as indexes, comments, and grants), if any.

An Export file is an Oracle binary-format dump file that is typically located on disk or tape. The dump files can be transferred using FTP or physically transported (in the case of tape) to a different site. The files can then be used with the Import utility to transfer data between databases that are on systems not connected through a network. The files can also be used as backups in addition to normal backup procedures.

Export dump files can only be read by the Oracle Import utility. The version of the Import utility cannot be earlier than the version of the Export utility used to create the dump file.

You can also display the contents of an export file without actually performing an import. To do this, use the Import SHOW parameter. See ["SHOW"](original_import.md) for more information.To load data from ASCII fixed-format or delimited files, use the SQL\*Loader utility.

## Before Using Export

Before you begin using Export, be sure you take care of the following items (described in detail in the following sections):

- If you created your database manually, ensure that the `catexp.sql` or `catalog.sql` script has been run. If you created your database using the Database Configuration Assistant (DBCA), it is not necessary to run these scripts.
- Ensure there is sufficient disk or tape storage to write the export file
- Verify that you have the required access privileges

### Running catexp.sql or catalog.sql

To use Export, you must run the script `catexp.sql` or `catalog.sql` (which runs `catexp.sql`) after the database has been created or migrated to a newer release.

The `catexp.sql` or `catalog.sql` script needs to be run only once on a database. The script performs the following tasks to prepare the database for export and import operations:

- Creates the necessary export and import views in the data dictionary
- Creates the `EXP_FULL_DATABASE` and `IMP_FULL_DATABASE` roles
- Assigns all necessary privileges to the `EXP_FULL_DATABASE` and `IMP_FULL_DATABASE` roles
- Assigns `EXP_FULL_DATABASE` and `IMP_FULL_DATABASE` to the `DBA` role
- Records the version of `catexp.sql` that has been installed

The `EXP_FULL_DATABASE` and `IMP_FULL_DATABASE` roles are powerful. Database administrators should use caution when granting these roles to users.

### Ensuring Sufficient Disk Space for Export Operations

Before you run Export, ensure that there is sufficient disk or tape storage space to write the export file. If there is not enough space, then Export terminates with a write-failure error.

You can use table sizes to estimate the maximum space needed. You can find table sizes in the `USER_SEGMENTS` view of the Oracle data dictionary. The following query displays disk usage for all tables:

```
SELECT SUM(BYTES) FROM USER_SEGMENTS WHERE SEGMENT_TYPE='TABLE';
```

The result of the query does not include disk space used for data stored in LOB (large object) or `VARRAY` columns or in partitioned tables.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for more information about dictionary views

### Verifying Access Privileges for Export and Import Operations

To use Export, you must have the `CREATE SESSION` privilege on an Oracle database. This privilege belongs to the `CONNECT` role established during database creation. To export tables owned by another user, you must have the `EXP_FULL_DATABASE` role enabled. This role is granted to all database administrators (DBAs).

If you do not have the system privileges contained in the `EXP_FULL_DATABASE` role, then you cannot export objects contained in another user's schema. For example, you cannot export a table in another user's schema, even if you created a synonym for it.

Several system schemas cannot be exported because they are not user schemas; they contain Oracle-managed data and metadata. Examples of schemas that are not exported include `SYS`, `ORDSYS`, and `MDSYS`.

## Invoking Export

You can invoke Export and specify parameters by using any of the following methods:

- Command-line entries
- Parameter files
- Interactive mode

Before you use one of these methods, be sure to read the descriptions of the available parameters. See "Export Parameters".

### Invoking Export as SYSDBA

`SYSDBA` is used internally and has specialized functions; its behavior is not the same as for generalized users. Therefore, you should not typically need to invoke Export `as SYSDBA` except in the following situations:

- At the request of Oracle technical support
- When importing a transportable tablespace set

### Command-Line Entries

You can specify all valid parameters and their values from the command line using the following syntax (you will then be prompted for a username and password):

```
exp PARAMETER=value
```

or

```
exp PARAMETER=(value1,value2,...,valuen)
```

The number of parameters cannot exceed the maximum length of a command line on the system.

### Parameter Files

You can specify all valid parameters and their values in a parameter file. Storing the parameters in a file allows them to be easily modified or reused, and is the recommended method for invoking Export. If you use different parameters for different databases, then you can have multiple parameter files.

Create the parameter file using any flat file text editor. The command-line option `PARFILE=` `filename` tells Export to read the parameters from the specified file rather than from the command line. For example:

The syntax for parameter file specifications is one of the following:

```
PARAMETER=value
PARAMETER=(value)
PARAMETER=(value1, value2, ...)
```

The following example shows a partial parameter file listing:

```
FULL=y
FILE=dba.dmp
GRANTS=y
INDEXES=y
CONSISTENT=y
```

Note:

The maximum size of the parameter file may be limited by the operating system. The name of the parameter file is subject to the file-naming conventions of the operating system.

You can add comments to the parameter file by preceding them with the pound (#) sign. Export ignores all characters to the right of the pound (#) sign.

You can specify a parameter file at the same time that you are entering parameters on the command line. In fact, you can specify the same parameter in both places. The position of the `PARFILE` parameter and other parameters on the command line determines which parameters take precedence. For example, assume the parameter file `params.dat` contains the parameter `INDEXES=y` and Export is invoked with the following line:

```
exp PARFILE=params.dat INDEXES=n
```

In this case, because `INDEXES=n` occurs after `PARFILE=params.dat`, `INDEXES=n` overrides the value of the `INDEXES` parameter in the parameter file.

### Interactive Mode

If you prefer to be prompted for the value of each parameter, then you can simply specify either `exp` at the command line. You will be prompted for a username and password.

Commonly used parameters are then displayed. You can accept the default value, if one is provided, or enter a different value. The command-line interactive method does not provide prompts for all functionality and is provided only for backward compatibility. If you want to use an interactive interface, then Oracle recommends that you use the Oracle Enterprise Manager Export Wizard.

#### Restrictions When Using Export's Interactive Method

Keep in mind the following points when you use the interactive method:

- In user mode, Export prompts for all usernames to be included in the export before exporting any data. To indicate the end of the user list and begin the current Export session, press Enter.
- In table mode, if you do not specify a schema prefix, then Export defaults to the exporter's schema or the schema containing the last table exported in the current session.
	For example, if `beth` is a privileged user exporting in table mode, then Export assumes that all tables are in the `beth` schema until another schema is specified. Only a privileged user (someone with the `EXP_FULL_DATABASE` role) can export tables in another user's schema.
- If you specify a null table list to the prompt "Table to be exported," then the Export utility exits.

### Getting Online Help

Export provides online help. Enter `exp help=y` on the command line to invoke Export help.

## Export Modes

The Export utility supports four modes of operation:

- Full: Exports a full database. Only users with the `EXP_FULL_DATABASE` role can use this mode. Use the `FULL` parameter to specify this mode.
- Tablespace: Enables a privileged user to move a set of tablespaces from one Oracle database to another. Use the `TRANSPORT_TABLESPACE` parameter to specify this mode.
- User: Enables you to export all objects that belong to you (such as tables, grants, indexes, and procedures). A privileged user importing in user mode can import all objects in the schemas of a specified set of users. Use the `OWNER` parameter to specify this mode in Export.
- Table: Enables you to export specific tables and partitions. A privileged user can qualify the tables by specifying the schema that contains them. For any table for which a schema name is not specified, Export defaults to the exporter's schema name. Use the `TABLES` parameter to specify this mode.

See Table 21-1 for a list of objects that are exported and imported in each mode.

Note:

The original Export utility does not export any table that was created with deferred segment creation and has not had a segment created for it. The most common way for a segment to be created is to store a row into the table, though other operations such as `ALTER TABLE ALLOCATE EXTENTS` will also create a segment. If a segment does exist for the table and the table is exported, then the `SEGMENT CREATION DEFERRED` clause is not included in the `CREATE TABLE` statement that is executed by the original Import utility.

You can use conventional path Export or direct path Export to export in any mode except tablespace mode.The differences between conventional path Export and direct path Export are described in "Conventional Path Export Versus Direct Path Export".

Table 21-1 Objects Exported in Each Mode

| Object | Table Mode | User Mode | Full Database Mode | Tablespace Mode |
| --- | --- | --- | --- | --- |
| Analyze cluster | No | Yes | Yes | No |
| Analyze tables/statistics | Yes | Yes | Yes | Yes |
| Application contexts | No | No | Yes | No |
| Auditing information | Yes | Yes | Yes | No |
| B-tree, bitmap, domain function-based indexes | Yes <sup>Foot 1</sup> | Yes | Yes | Yes |
| Cluster definitions | No | Yes | Yes | Yes |
| Column and table comments | Yes | Yes | Yes | Yes |
| Database links | No | Yes | Yes | No |
| Default roles | No | No | Yes | No |
| Dimensions | No | Yes | Yes | No |
| Directory aliases | No | No | Yes | No |
| External tables (without data) | Yes | Yes | Yes | No |
| Foreign function libraries | No | Yes | Yes | No |
| Indexes owned by users other than table owner | Yes (Privileged users only) | Yes | Yes | Yes |
| Index types | No | Yes | Yes | No |
| Java resources and classes | No | Yes | Yes | No |
| Job queues | No | Yes | Yes | No |
| Nested table data | Yes | Yes | Yes | Yes |
| Object grants | Yes (Only for tables and indexes) | Yes | Yes | Yes |
| Object type definitions used by table | Yes | Yes | Yes | Yes |
| Object types | No | Yes | Yes | No |
| Operators | No | Yes | Yes | No |
| Password history | No | No | Yes | No |
| Postinstance actions and objects | No | No | Yes | No |
| Postschema procedural actions and objects | No | Yes | Yes | No |
| Posttable actions | Yes | Yes | Yes | Yes |
| Posttable procedural actions and objects | Yes | Yes | Yes | Yes |
| Preschema procedural objects and actions | No | Yes | Yes | No |
| Pretable actions | Yes | Yes | Yes | Yes |
| Pretable procedural actions | Yes | Yes | Yes | Yes |
| Private synonyms | No | Yes | Yes | No |
| Procedural objects | No | Yes | Yes | No |
| Profiles | No | No | Yes | No |
| Public synonyms | No | No | Yes | No |
| Referential integrity constraints | Yes | Yes | Yes | No |
| Refresh groups | No | Yes | Yes | No |
| Resource costs | No | No | Yes | No |
| Role grants | No | No | Yes | No |
| Roles | No | No | Yes | No |
| Rollback segment definitions | No | No | Yes | No |
| Security policies for table | Yes | Yes | Yes | Yes |
| Sequence numbers | No | Yes | Yes | No |
| Snapshot logs | No | Yes | Yes | No |
| Snapshots and materialized views | No | Yes | Yes | No |
| System privilege grants | No | No | Yes | No |
| Table constraints (primary, unique, check) | Yes | Yes | Yes | Yes |
| Table data | Yes | Yes | Yes | Yes |
| Table definitions | Yes | Yes | Yes | Yes |
| Tablespace definitions | No | No | Yes | No |
| Tablespace quotas | No | No | Yes | No |
| Triggers | Yes | Yes <sup>Foot 2</sup> | Yes <sup>Foot 3</sup> | Yes |
| Triggers owned by other users | Yes (Privileged users only) | No | No | No |
| User definitions | No | No | Yes | No |
| User proxies | No | No | Yes | No |
| User views | No | Yes | Yes | No |
| User-stored procedures, packages, and functions | No | Yes | Yes | No |

<sup>Footnote 1</sup> Nonprivileged users can export and import only indexes they own on tables they own. They cannot export indexes they own that are on tables owned by other users, nor can they export indexes owned by other users on their own tables. Privileged users can export and import indexes on the specified users' tables, even if the indexes are owned by other users. Indexes owned by the specified user on other users' tables are not included, unless those other users are included in the list of users to export.

<sup>Footnote 2</sup> Nonprivileged and privileged users can export and import all triggers owned by the user, even if they are on tables owned by other users.

<sup>Footnote 3</sup> A full export does not export triggers owned by schema SYS. You must manually re-create SYS triggers either before or after the full import. Oracle recommends that you re-create them after the import in case they define actions that would impede progress of the import.

### Table-Level and Partition-Level Export

You can export tables, partitions, and subpartitions in the following ways:

- Table-level Export: exports all data from the specified tables
- Partition-level Export: exports only data from the specified source partitions or subpartitions

In all modes, partitioned data is exported in a format such that partitions or subpartitions can be imported selectively.

#### Table-Level Export

In table-level Export, you can export an entire table (partitioned or nonpartitioned) along with its indexes and other table-dependent objects. If the table is partitioned, then all of its partitions and subpartitions are also exported. This applies to both direct path Export and conventional path Export. You can perform a table-level export in any Export mode.

#### Partition-Level Export

In partition-level Export, you can export one or more specified partitions or subpartitions of a table. You can only perform a partition-level export in table mode.

For information about how to specify table-level and partition-level Exports, see "TABLES".

## Export Parameters

This section contains descriptions of the Export command-line parameters.

### BUFFER

Default: operating system-dependent. See your Oracle operating system-specific documentation to determine the default value for this parameter.

Specifies the size, in bytes, of the buffer used to fetch rows. As a result, this parameter determines the maximum number of rows in an array fetched by Export. Use the following formula to calculate the buffer size:

```
buffer_size = rows_in_array * maximum_row_size
```

If you specify zero, then the Export utility fetches only one row at a time.

Tables with columns of type LOBs, `LONG`, `BFILE`, `REF`, `ROWID`, `LOGICAL` `ROWID`, or `DATE` are fetched one row at a time.

Note:

The `BUFFER` parameter applies only to conventional path Export. It has no effect on a direct path Export. For direct path Exports, use the `RECORDLENGTH` parameter to specify the size of the buffer that Export uses for writing to the export file.

#### Example: Calculating Buffer Size

This section shows an example of how to calculate buffer size.

The following table is created:

```
CREATE TABLE sample (name varchar(30), weight number);
```

The maximum size of the `name` column is 30, plus 2 bytes for the indicator. The maximum size of the `weight` column is 22 (the size of the internal representation for Oracle numbers), plus 2 bytes for the indicator.

Therefore, the maximum row size is 56 (30+2+22+2).

To perform array operations for 100 rows, a buffer size of 5600 should be specified.

### COMPRESS

Default: `y`

Specifies how Export and Import manage the initial extent for table data.

The default, `COMPRESS=y,` causes Export to flag table data for consolidation into one initial extent upon import. If extent sizes are large (for example, because of the `PCTINCREASE` parameter), then the allocated space will be larger than the space required to hold the data.

If you specify `COMPRESS=n,` then Export uses the current storage parameters, including the values of initial extent size and next extent size. The values of the parameters may be the values specified in the `CREATE TABLE` or `ALTER TABLE` statements or the values modified by the database system. For example, the `NEXT` extent size value may be modified if the table grows and if the `PCTINCREASE` parameter is nonzero.

The `COMPRESS` parameter does not work with bitmapped tablespaces.

Note:

Although the actual consolidation is performed upon import, you can specify the `COMPRESS` parameter only when you export, not when you import. The Export utility, not the Import utility, generates the data definitions, including the storage parameter definitions. Therefore, if you specify `COMPRESS=y` when you export, then you can import the data in consolidated form only.

Note:

Neither LOB data nor subpartition data is compressed. Rather, values of initial extent size and next extent size at the time of export are used.

### CONSISTENT

Default: `n`

Specifies whether Export uses the `SET TRANSACTION READ ONLY` statement to ensure that the data seen by Export is consistent to a single point in time and does not change during the execution of the `exp` command. You should specify `CONSISTENT=y` when you anticipate that other applications will be updating the target data after an export has started.

If you use `CONSISTENT=n`, then each table is usually exported in a single transaction. However, if a table contains nested tables, then the outer table and each inner table are exported as separate transactions. If a table is partitioned, then each partition is exported as a separate transaction.

Therefore, if nested tables and partitioned tables are being updated by other applications, then the data that is exported could be inconsistent. To minimize this possibility, export those tables at a time when updates are not being done.

Table 21-2 shows a sequence of events by two users: `user1` exports partitions in a table and `user2` updates data in that table.

Table 21-2 Sequence of Events During Updates by Two Users

| TIme Sequence | user1 | user2 |
| --- | --- | --- |
| 1 | Begins export of TAB:P1 | No activity |
| 2 | No activity | Updates TAB:P2   Updates TAB:P1   Commits transaction |
| 3 | Ends export of TAB:P1 | No activity |
| 4 | Exports TAB:P2 | No activity |

If the export uses `CONSISTENT=y,` then none of the updates by `user2` are written to the export file.

If the export uses `CONSISTENT=n,` then the updates to TAB:P1 are not written to the export file. However, the updates to TAB:P2 are written to the export file, because the update transaction is committed before the export of TAB:P2 begins. As a result, the `user2` transaction is only partially recorded in the export file, making it inconsistent.

If you use `CONSISTENT=y` and the volume of updates is large, then the rollback segment usage will be large. In addition, the export of each table will be slower, because the rollback segment must be scanned for uncommitted transactions.

Keep in mind the following points about using `CONSISTENT=y:`

- `CONSISTENT=y` is unsupported for exports that are performed when you are connected as user `SYS` or you are using `AS SYSDBA,` or both.
- Export of certain metadata may require the use of the `SYS` schema within recursive SQL. In such situations, the use of `CONSISTENT=y` will be ignored. Oracle recommends that you avoid making metadata changes during an export process in which `CONSISTENT=y` is selected.
- To minimize the time and space required for such exports, you should export tables that need to remain consistent separately from those that do not. For example, export the `emp` and `dept` tables together in a consistent export, and then export the remainder of the database in a second pass.
- A "snapshot too old" error occurs when rollback space is used up, and space taken up by committed transactions is reused for new transactions. Reusing space in the rollback segment allows database integrity to be preserved with minimum space requirements, but it imposes a limit on the amount of time that a read-consistent image can be preserved.
	If a committed transaction has been overwritten and the information is needed for a read-consistent view of the database, then a "snapshot too old" error results.
	To avoid this error, you should minimize the time taken by a read-consistent export. (Do this by restricting the number of objects exported and, if possible, by reducing the database transaction rate.) Also, make the rollback segment as large as possible.
	Note:
	Rollback segments will be deprecated in a future Oracle database release. Oracle recommends that you use automatic undo management instead.
	See Also:
	"OBJECT\_CONSISTENT"

### CONSTRAINTS

Default: `y`

Specifies whether the Export utility exports table constraints.

### DIRECT

Default: `n`

Specifies the use of direct path Export.

Specifying `DIRECT=y` causes Export to extract data by reading the data directly, bypassing the SQL command-processing layer (evaluating buffer). This method can be much faster than a conventional path Export.

For information about direct path Exports, including security and performance considerations, see "Invoking a Direct Path Export".

### FEEDBACK

Default: `0` (zero)

Specifies that Export should display a progress meter in the form of a period for `n` number of rows exported. For example, if you specify `FEEDBACK=10`, then Export displays a period each time 10 rows are exported. The `FEEDBACK` value applies to all tables being exported; it cannot be set individually for each table.

### FILE

Default: `expdat.dmp`

Specifies the names of the export dump files. The default extension is.`dmp`, but you can specify any extension. Because Export supports multiple export files, you can specify multiple file names to be used. For example:

```
exp scott FILE = dat1.dmp, dat2.dmp, dat3.dmp FILESIZE=2048
```

When Export reaches the value you have specified for the maximum `FILESIZE,` Export stops writing to the current file, opens another export file with the next name specified by the `FILE` parameter, and continues until complete or the maximum value of `FILESIZE` is again reached. If you do not specify sufficient export file names to complete the export, then Export prompts you to provide additional file names.

### FILESIZE

Default: Data is written to one file until the maximum size, as specified in Table 21-3, is reached.

Export supports writing to multiple export files, and Import can read from multiple export files. If you specify a value (byte limit) for the `FILESIZE` parameter, then Export will write only the number of bytes you specify to each dump file.

When the amount of data Export must write exceeds the maximum value you specified for `FILESIZE,` it will get the name of the next export file from the `FILE` parameter (see "FILE" for more information) or, if it has used all the names specified in the `FILE` parameter, then it will prompt you to provide a new export file name. If you do not specify a value for `FILESIZE` (note that a value of 0 is equivalent to not specifying `FILESIZE`), then Export will write to only one file, regardless of the number of files specified in the `FILE` parameter.

Note:

If the space requirements of your export file exceed the available disk space, then Export will terminate, and you will have to repeat the Export after making sufficient disk space available.

The `FILESIZE` parameter has a maximum value equal to the maximum value that can be stored in 64 bits.

Table 21-3 shows that the maximum size for dump files depends on the operating system you are using and on the release of the Oracle database that you are using.

Table 21-3 Maximum Size for Dump Files

| Operating System | Release of Oracle Database | Maximum Size |
| --- | --- | --- |
| Any | Before 8.1.5 | 2 gigabytes |
| 32-bit | 8.1.5 | 2 gigabytes |
| 64-bit | 8.1.5 and later | Unlimited |
| 32-bit with 32-bit files | Any | 2 gigabytes |
| 32-bit with 64-bit files | 8.1.6 and later | Unlimited |

The maximum value that can be stored in a file is dependent on your operating system. You should verify this maximum value in your Oracle operating system-specific documentation before specifying `FILESIZE`. You should also ensure that the file size you specify for Export is supported on the system on which Import will run.

The `FILESIZE` value can also be specified as a number followed by KB (number of kilobytes). For example, `FILESIZE=2KB` is the same as `FILESIZE=2048.` Similarly, MB specifies megabytes (1024 \* 1024) and GB specifies gigabytes (1024\*\*3). B remains the shorthand for bytes; the number is not multiplied to obtain the final file size (`FILESIZE=2048B` is the same as `FILESIZE=2048`).

### FLASHBACK\_SCN

Default: none

Specifies the system change number (SCN) that Export will use to enable flashback. The export operation is performed with data consistent as of this specified SCN.

See Also:

[Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm) for more information about using flashback

The following is an example of specifying an SCN. When the export is performed, the data will be consistent as of SCN `3482971`.

```
> exp FILE=exp.dmp FLASHBACK_SCN=3482971
```

### FLASHBACK\_TIME

Default: none

Enables you to specify a timestamp. Export finds the SCN that most closely matches the specified timestamp. This SCN is used to enable flashback. The export operation is performed with data consistent as of this SCN.

You can specify the time in any format that the `DBMS_FLASHBACK`.`ENABLE_AT_TIME` procedure accepts. This means that you can specify it in either of the following ways:

```
> exp FILE=exp.dmp FLASHBACK_TIME="TIMESTAMP '2006-05-01 11:00:00'"

> exp FILE=exp.dmp FLASHBACK_TIME="TO_TIMESTAMP('12-02-2005 14:35:00', 'DD-MM-YYYY HH24:MI:SS')"
```

Also, the old format, as shown in the following example, will continue to be accepted to ensure backward compatibility:

```
> exp FILE=exp.dmp FLASHBACK_TIME="'2006-05-01 11:00:00'"
```

See Also:

- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm) for more information about using flashback
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for more information about the `DBMS_FLASHBACK` package

### FULL

Default: `n`

Indicates that the export is a full database mode export (that is, it exports the entire database). Specify `FULL=y` to export in full database mode. You need to have the `EXP_FULL_DATABASE` role to export in this mode.

#### Points to Consider for Full Database Exports and Imports

A full database export and import can be a good way to replicate or clean up a database. However, to avoid problems be sure to keep the following points in mind:

- A full export does not export triggers owned by schema `SYS`. You must manually re-create `SYS` triggers either before or after the full import. Oracle recommends that you re-create them after the import in case they define actions that would impede progress of the import.
- A full export also does not export the default profile. If you have modified the default profile in the source database (for example, by adding a password verification function owned by schema `SYS`), then you must manually pre-create the function and modify the default profile in the target database after the import completes.
- If possible, before beginning, make a physical copy of the exported database and the database into which you intend to import. This ensures that any mistakes are reversible.
- Before you begin the export, it is advisable to produce a report that includes the following information:
	- A list of tablespaces and data files
		- A list of rollback segments
		- A count, by user, of each object type such as tables, indexes, and so on
	This information lets you ensure that tablespaces have already been created and that the import was successful.
- If you are creating a completely new database from an export, then remember to create an extra rollback segment in `SYSTEM` and to make it available in your initialization parameter file (`init`.`ora)` before proceeding with the import.
- When you perform the import, ensure you are pointing at the correct instance. This is very important because on some UNIX systems, just the act of entering a subshell can change the database against which an import operation was performed.
- Do not perform a full import on a system that has more than one database unless you are certain that all tablespaces have already been created. A full import creates any undefined tablespaces using the same data file names as the exported database. This can result in problems in the following situations:
	- If the data files belong to any other database, then they will become corrupted. This is especially true if the exported database is on the same system, because its data files will be reused by the database into which you are importing.
		- If the data files have names that conflict with existing operating system files.

### GRANTS

Default: `y`

Specifies whether the Export utility exports object grants. The object grants that are exported depend on whether you use full database mode or user mode. In full database mode, all grants on a table are exported. In user mode, only those granted by the owner of the table are exported. System privilege grants are always exported.

### HELP

Default: none

Displays a description of the Export parameters. Enter `exp` `help=y` on the command line to invoke it.

### INDEXES

Default: `y`

Specifies whether the Export utility exports indexes.

### LOG

Default: none

Specifies a file name (for example, export.log) to receive informational and error messages.

If you specify this parameter, then messages are logged in the log file and displayed to the terminal display.

### OBJECT\_CONSISTENT

Default: `n`

Specifies whether the Export utility uses the `SET` `TRANSACTION` `READ` `ONLY` statement to ensure that the data exported is consistent to a single point in time and does not change during the export. If `OBJECT_CONSISTENT` is set to `y`, then each object is exported in its own read-only transaction, even if it is partitioned. In contrast, if you use the `CONSISTENT` parameter, then there is only one read-only transaction.

See Also:

"CONSISTENT"

### OWNER

Default: none

Indicates that the export is a user-mode export and lists the users whose objects will be exported. If the user initiating the export is the database administrator (DBA), then multiple users can be listed.

User-mode exports can be used to back up one or more database users. For example, a DBA may want to back up the tables of deleted users for a period of time. User mode is also appropriate for users who want to back up their own data or who want to move objects from one owner to another.

### PARFILE

Default: none

Specifies a file name for a file that contains a list of Export parameters. For more information about using a parameter file, see "Invoking Export".

### QUERY

Default: none

This parameter enables you to select a subset of rows from a set of tables when doing a table mode export. The value of the query parameter is a string that contains a `WHERE` clause for a SQL `SELECT` statement that will be applied to all tables (or table partitions) listed in the `TABLES` parameter.

For example, if user `scott` wants to export only those employees whose job title is `SALESMAN` and whose salary is less than 1600, then he could do the following (this example is UNIX-based):

```
exp scott TABLES=emp QUERY=\"WHERE job=\'SALESMAN\' and sal \<1600\"
```

Note:

Because the value of the `QUERY` parameter contains blanks, most operating systems require that the entire string `WHERE job=\'SALESMAN\'` and `sal\<1600` be placed in double quotation marks or marked as a literal by some method. Operating system reserved characters also need to be preceded by an escape character. See your Oracle operating system-specific documentation for information about special and reserved characters on your system.

When executing this query, Export builds a SQL `SELECT` statement similar to the following:

```
SELECT * FROM emp WHERE job='SALESMAN' and sal <1600;
```

The values specified for the `QUERY` parameter are applied to all tables (or table partitions) listed in the `TABLES` parameter. For example, the following statement will unload rows in both `emp` and `bonus` that match the query:

```
exp scott TABLES=emp,bonus QUERY=\"WHERE job=\'SALESMAN\' and sal\<1600\"
```

Again, the SQL statements that Export executes are similar to the following:

```
SELECT * FROM emp WHERE job='SALESMAN' and sal <1600;

SELECT * FROM bonus WHERE job='SALESMAN' and sal <1600;
```

If a table is missing the columns specified in the `QUERY` clause, then an error message will be produced, and no rows will be exported for the offending table.

#### Restrictions When Using the QUERY Parameter

- The `QUERY` parameter cannot be specified for full, user, or tablespace-mode exports.
- The `QUERY` parameter must be applicable to all specified tables.
- The `QUERY` parameter cannot be specified in a direct path Export (`DIRECT=y`)
- The `QUERY` parameter cannot be specified for tables with inner nested tables.
- You cannot determine from the contents of the export file whether the data is the result of a `QUERY` export.

### RECORDLENGTH

Default: operating system-dependent

Specifies the length, in bytes, of the file record. The `RECORDLENGTH` parameter is necessary when you must transfer the export file to another operating system that uses a different default value.

If you do not define this parameter, then it defaults to your platform-dependent value for buffer size.

You can set `RECORDLENGTH` to any value equal to or greater than your system's buffer size. (The highest value is 64 KB.) Changing the `RECORDLENGTH` parameter affects only the size of data that accumulates before writing to the disk. It does not affect the operating system file block size.

Note:

You can use this parameter to specify the size of the Export I/O buffer.

### RESUMABLE

Default: `n`

The `RESUMABLE` parameter is used to enable and disable resumable space allocation. Because this parameter is disabled by default, you must set `RESUMABLE=y` to use its associated parameters, `RESUMABLE_NAME` and `RESUMABLE_TIMEOUT`.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm)
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information about resumable space allocation

### RESUMABLE\_NAME

Default: `'User USERNAME (USERID), Session SESSIONID, Instance INSTANCEID'`

The value for this parameter identifies the statement that is resumable. This value is a user-defined text string that is inserted in either the `USER_RESUMABLE` or `DBA_RESUMABLE` view to help you identify a specific resumable statement that has been suspended.

This parameter is ignored unless the `RESUMABLE` parameter is set to `y` to enable resumable space allocation.

### RESUMABLE\_TIMEOUT

Default: `7200` seconds (2 hours)

The value of the parameter specifies the time period during which an error must be fixed. If the error is not fixed within the timeout period, then execution of the statement is terminated.

This parameter is ignored unless the `RESUMABLE` parameter is set to `y` to enable resumable space allocation.

### ROWS

Default: `y`

Specifies whether the rows of table data are exported.

### STATISTICS

Default: `ESTIMATE`

Specifies the type of database optimizer statistics to generate when the exported data is imported. Options are `ESTIMATE,` `COMPUTE,` and `NONE.`

In some cases, Export will place the precalculated statistics in the export file, and also the `ANALYZE` statements to regenerate the statistics.

However, the precalculated optimizer statistics will not be used at export time if a table has columns with system-generated names.

The precalculated optimizer statistics are flagged as questionable at export time if:

- There are row errors while exporting
- The client character set or `NCHAR` character set does not match the server character set or `NCHAR` character set
- A `QUERY` clause is specified
- Only certain partitions or subpartitions are exported
	Note:
	Specifying `ROWS=n` does not preclude saving the precalculated statistics in the export file. This enables you to tune plan generation for queries in a nonproduction database using statistics from a production database.

### TABLES

Default: none

Specifies that the export is a table-mode export and lists the table names and partition and subpartition names to export. You can specify the following when you specify the name of the table:

- `schemaname` specifies the name of the user's schema from which to export the table or partition. If a schema name is not specified, then the exporter's schema is used as the default. System schema names such as `ORDSYS,` `MDSYS,` `CTXSYS,` `LBACSYS`, and `ORDPLUGINS` are reserved by Export.
- `tablename` specifies the name of the table or tables to be exported. Table-level export lets you export entire partitioned or nonpartitioned tables. If a table in the list is partitioned and you do not specify a partition name, then all its partitions and subpartitions are exported.
	The table name can contain any number of '%' pattern matching characters, which can each match zero or more characters in the table name against the table objects in the database. All the tables in the relevant schema that match the specified pattern are selected for export, as if the respective table names were explicitly specified in the parameter.
- `partition_name` indicates that the export is a partition-level Export. Partition-level Export lets you export one or more specified partitions or subpartitions within a table.

The syntax you use to specify the preceding is in the form:

```
schemaname.tablename:partition_name
schemaname.tablename:subpartition_name
```

If you use `tablename``:``partition_name``,` then the specified table must be partitioned, and `partition_name` must be the name of one of its partitions or subpartitions. If the specified table is not partitioned, then the `partition_name` is ignored and the entire table is exported.

See "Example Export Session Using Partition-Level Export" for several examples of partition-level Exports.

#### Table Name Restrictions

The following restrictions apply to table names:

- By default, table names in a database are stored as uppercase. If you have a table name in mixed-case or lowercase, and you want to preserve case-sensitivity for the table name, then you must enclose the name in quotation marks. The name must exactly match the table name stored in the database.
	Some operating systems require that quotation marks on the command line be preceded by an escape character. The following are examples of how case-sensitivity can be preserved in the different Export modes.
	- In command-line mode:
		```
		TABLES='\"Emp\"'
		```
		- In interactive mode:
		```
		Table(T) to be exported: "Emp"
		```
		- In parameter file mode:
		```
		TABLES='"Emp"'
		```
- Table names specified on the command line cannot include a pound (#) sign, unless the table name is enclosed in quotation marks. Similarly, in the parameter file, if a table name includes a pound (#) sign, then the Export utility interprets the rest of the line as a comment, unless the table name is enclosed in quotation marks.
	For example, if the parameter file contains the following line, then Export interprets everything on the line after `emp#` as a comment and does not export the tables `dept` and `mydata:`
	```
	TABLES=(emp#, dept, mydata)
	```
	However, given the following line, the Export utility exports all three tables, because `emp#` is enclosed in quotation marks:
	```
	TABLES=("emp#", dept, mydata)
	```
	Note:
	Some operating systems require single quotation marks rather than double quotation marks, or the reverse. Different operating systems also have other restrictions on table naming.

### TABLESPACES

Default: none

The `TABLESPACES` parameter specifies that all tables in the specified tablespace be exported to the Export dump file. This includes all tables contained in the list of tablespaces and all tables that have a partition located in the list of tablespaces. Indexes are exported with their tables, regardless of where the index is stored.

You must have the `EXP_FULL_DATABASE` role to use `TABLESPACES` to export all tables in the tablespace.

When `TABLESPACES` is used in conjunction with `TRANSPORT_TABLESPACE=y,` you can specify a limited list of tablespaces to be exported from the database to the export file.

### TRANSPORT\_TABLESPACE

Default: `n`

When specified as `y`, this parameter enables the export of transportable tablespace metadata.

Encrypted columns are not supported in transportable tablespace mode.

Note:

You cannot export transportable tablespaces and then import them into a database at a lower release level. The target database must be at the same or higher release level as the source database.

See Also:

- "Transportable Tablespaces"
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm)
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm)

### TRIGGERS

Default: `y`

Specifies whether the Export utility exports triggers.

### TTS\_FULL\_CHECK

Default: `n`

When `TTS_FULL_CHECK` is set to `y,` Export verifies that a recovery set (set of tablespaces to be recovered) has no dependencies (specifically, `IN` pointers) on objects outside the recovery set, and the reverse.

### USERID (username/password)

Default: none

Specifies the username, password, and optional connect string of the user performing the export. If you omit the password, then Export will prompt you for it.

If you connect as user `SYS,` then you must also specify `AS SYSDBA` in the connect string. Your operating system may require you to treat `AS SYSDBA` as a special string, in which case the entire string would be enclosed in quotation marks.

See Also:

- [Oracle Database Heterogeneous Connectivity User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11050/toc.htm)
- The user's guide for your Oracle Net protocol for information about specifying a connect string for Oracle Net

### VOLSIZE

Default: none

Specifies the maximum number of bytes in an export file on each volume of tape.

The `VOLSIZE` parameter has a maximum value equal to the maximum value that can be stored in 64 bits on your platform.

The `VOLSIZE` value can be specified as a number followed by KB (number of kilobytes). For example, `VOLSIZE=2KB` is the same as `VOLSIZE=2048.` Similarly, MB specifies megabytes (1024 \* 1024) and GB specifies gigabytes (1024\*\*3). B remains the shorthand for bytes; the number is not multiplied to get the final file size (`VOLSIZE=2048B` is the same as `VOLSIZE=2048)`.

## Example Export Sessions

This section provides examples of the following types of Export sessions:

- Example Export Session in Full Database Mode
- Example Export Session in User Mode
- Example Export Sessions in Table Mode
- Example Export Session Using Partition-Level Export

In each example, you are shown how to use both the command-line method and the parameter file method. Some examples use vertical ellipses to indicate sections of example output that were too long to include.

### Example Export Session in Full Database Mode

Only users with the `DBA` role or the `EXP_FULL_DATABASE` role can export in full database mode. In this example, an entire database is exported to the file `dba.dmp` with all `GRANTS` and all data.

Parameter File Method

```
> exp PARFILE=params.dat
```

The `params.dat` file contains the following information:

```
FILE=dba.dmp
GRANTS=y
FULL=y
ROWS=y
```

Command-Line Method

```
> exp FULL=y FILE=dba.dmp GRANTS=y ROWS=y
```

Export Messages

Information is displayed about the release of Export you are using and the release of Oracle Database that you are connected to. Status messages are written out as the entire database is exported. A final completion message is returned when the export completes successfully, without warnings.

### Example Export Session in User Mode

User-mode exports can be used to back up one or more database users. For example, a DBA may want to back up the tables of deleted users for a period of time. User mode is also appropriate for users who want to back up their own data or who want to move objects from one owner to another. In this example, user `scott` is exporting his own tables.

Parameter File Method

```
> exp scott PARFILE=params.dat
```

The `params.dat` file contains the following information:

```
FILE=scott.dmp
OWNER=scott
GRANTS=y
ROWS=y
COMPRESS=y
```

Command-Line Method

```
> exp scott FILE=scott.dmp OWNER=scott GRANTS=y ROWS=y COMPRESS=y
```

Export Messages

Information is displayed about the release of Export you are using and the release of Oracle Database that you are connected to. Then, status messages similar to the following are shown:

```
.
.
. about to export SCOTT's tables via Conventional Path ...
. . exporting table                          BONUS          0 rows exported
. . exporting table                           DEPT          4 rows exported
. . exporting table                            EMP         14 rows exported
. . exporting table                       SALGRADE          5 rows exported
.
.
.
Export terminated successfully without warnings.
```

### Example Export Sessions in Table Mode

In table mode, you can export table data or the table definitions. (If no rows are exported, then the `CREATE TABLE` statement is placed in the export file, with grants and indexes, if they are specified.)

A user with the `EXP_FULL_DATABASE` role can use table mode to export tables from any user's schema by specifying `TABLES=schemaname.tablename.`

If `schemaname` is not specified, then Export defaults to the exporter's schema name. In the following example, Export defaults to the `SYSTEM` schema for table `a` and table `c`:

```
> exp TABLES=(a, scott.b, c, mary.d)
```

A user with the `EXP_FULL_DATABASE` role can also export dependent objects that are owned by other users. A nonprivileged user can export only dependent objects for the specified tables that the user owns.

Exports in table mode do not include cluster definitions. As a result, the data is exported as unclustered tables. Thus, you can use table mode to uncluster tables.

#### Example 1: DBA Exporting Tables for Two Users

In this example, a DBA exports specified tables for two users.

Parameter File Method

```
> exp PARFILE=params.dat
```

The `params.dat` file contains the following information:

```
FILE=expdat.dmp
TABLES=(scott.emp,blake.dept)
GRANTS=y
INDEXES=y
```

Command-Line Method

```
> exp FILE=expdat.dmp TABLES=(scott.emp,blake.dept) GRANTS=y INDEXES=y
```

Export Messages

Information is displayed about the release of Export you are using and the release of Oracle Database that you are connected to. Then, status messages similar to the following are shown:

```
.
.
.
About to export specified tables via Conventional Path ...
Current user changed to SCOTT
. . exporting table                            EMP         14 rows exported
Current user changed to BLAKE
. . exporting table                           DEPT          8 rows exported
Export terminated successfully without warnings.
```

#### Example 2: User Exports Tables That He Owns

In this example, user `blake` exports selected tables that he owns.

Parameter File Method

```
> exp blake PARFILE=params.dat
```

The `params.dat` file contains the following information:

```
FILE=blake.dmp
TABLES=(dept,manager)
ROWS=y
COMPRESS=y
```

Command-Line Method

```
> exp blake FILE=blake.dmp TABLES=(dept, manager) ROWS=y COMPRESS=y
```

Export Messages

Information is displayed about the release of Export you are using and the release of Oracle Database that you are connected to. Then, status messages similar to the following are shown:

```
.
.
.

About to export specified tables via Conventional Path ...
. . exporting table                           DEPT          8 rows exported
. . exporting table                        MANAGER          4 rows exported
Export terminated successfully without warnings.
```

#### Example 3: Using Pattern Matching to Export Various Tables

In this example, pattern matching is used to export various tables for users `scott` and `blake`.

Parameter File Method

```
> exp PARFILE=params.dat
```

The `params.dat` file contains the following information:

```
FILE=misc.dmp
TABLES=(scott.%P%,blake.%,scott.%S%)
```

Command-Line Method

```
> exp FILE=misc.dmp TABLES=(scott.%P%,blake.%,scott.%S%)
```

Export Messages

Information is displayed about the release of Export you are using and the release of Oracle Database that you are connected to. Then, status messages similar to the following are shown:

```
.
.
.
About to export specified tables via Conventional Path ...
Current user changed to SCOTT
. . exporting table                           DEPT          4 rows exported
. . exporting table                            EMP         14 rows exported
Current user changed to BLAKE
. . exporting table                           DEPT          8 rows exported
. . exporting table                        MANAGER          4 rows exported
Current user changed to SCOTT
. . exporting table                          BONUS          0 rows exported
. . exporting table                       SALGRADE          5 rows exported
Export terminated successfully without warnings.
```

### Example Export Session Using Partition-Level Export

In partition-level Export, you can specify the partitions and subpartitions of a table that you want to export.

#### Example 1: Exporting a Table Without Specifying a Partition

Assume `emp` is a table that is partitioned on employee name. There are two partitions, `m` and `z.` As this example shows, if you export the table without specifying a partition, then all of the partitions are exported.

Parameter File Method

```
> exp scott PARFILE=params.dat
```

The `params.dat` file contains the following:

```
TABLES=(emp)
ROWS=y
```

Command-Line Method

```
> exp scott TABLES=emp rows=y
```

Export Messages

Information is displayed about the release of Export you are using and the release of Oracle Database that you are connected to. Then, status messages similar to the following are shown:

```
.
.
.
About to export specified tables via Conventional Path ...
. . exporting table                            EMP
. . exporting partition                              M          8 rows exported
. . exporting partition                              Z          6 rows exported
Export terminated successfully without warnings.
```

#### Example 2: Exporting a Table with a Specified Partition

Assume `emp` is a table that is partitioned on employee name. There are two partitions, `m` and `z.` As this example shows, if you export the table and specify a partition, then only the specified partition is exported.

Parameter File Method

```
> exp scott PARFILE=params.dat
```

The `params.dat` file contains the following:

```
TABLES=(emp:m)
ROWS=y
```

Command-Line Method

```
> exp scott TABLES=emp:m rows=y
```

Export Messages

Information is displayed about the release of Export you are using and the release of Oracle Database that you are connected to. Then, status messages similar to the following are shown:

```
.
.
.
About to export specified tables via Conventional Path ...
. . exporting table                            EMP
. . exporting partition                              M          8 rows exported
Export terminated successfully without warnings.
```

#### Example 3: Exporting a Composite Partition

Assume `emp` is a partitioned table with two partitions, `m` and `z.` Table `emp` is partitioned using the composite method. Partition `m` has subpartitions `sp1` and `sp2,` and partition `z` has subpartitions `sp3` and `sp4.` As the example shows, if you export the composite partition `m,` then all its subpartitions (`sp1` and `sp2`) will be exported. If you export the table and specify a subpartition (`sp4`), then only the specified subpartition is exported.

Parameter File Method

```
> exp scott PARFILE=params.dat
```

The `params.dat` file contains the following:

```
TABLES=(emp:m,emp:sp4)
ROWS=y
```

Command-Line Method

```
> exp scott TABLES=(emp:m, emp:sp4) ROWS=y
```

Export Messages

Information is displayed about the release of Export you are using and the release of Oracle Database that you are connected to. Then, status messages similar to the following are shown:

```
.
.
.
About to export specified tables via Conventional Path ...
. . exporting table                            EMP
. . exporting composite partition                    M
. . exporting subpartition                         SP1          1 rows exported
. . exporting subpartition                         SP2          3 rows exported
. . exporting composite partition                    Z
. . exporting subpartition                         SP4          1 rows exported
Export terminated successfully without warnings.
```

## Warning, Error, and Completion Messages

This section describes the different types of messages issued by Export and how to save them in a log file.

### Log File

You can capture all Export messages in a log file, either by using the `LOG` parameter or, for those systems that permit it, by redirecting the output to a file. A log of detailed information is written about successful unloads and any errors that may have occurred.

### Warning Messages

Export does not terminate after recoverable errors. For example, if an error occurs while exporting a table, then Export displays (or logs) an error message, skips to the next table, and continues processing. These recoverable errors are known as warnings.

Export also issues warnings when invalid objects are encountered.

For example, if a nonexistent table is specified as part of a table-mode Export, then the Export utility exports all other tables. Then it issues a warning and terminates successfully.

### Nonrecoverable Error Messages

Some errors are nonrecoverable and terminate the Export session. These errors typically occur because of an internal problem or because a resource, such as memory, is not available or has been exhausted. For example, if the `catexp.sql` script is not executed, then Export issues the following nonrecoverable error message:

```
EXP-00024: Export views not installed, please notify your DBA
```

### Completion Messages

When an export completes without errors, a message to that effect is displayed, for example:

```
Export terminated successfully without warnings
```

If one or more recoverable errors occurs but the job continues to completion, then a message similar to the following is displayed:

```
Export terminated successfully with warnings
```

If a nonrecoverable error occurs, then the job terminates immediately and displays a message stating so, for example:

```
Export terminated unsuccessfully
```

## Exit Codes for Inspection and Display

Export provides the results of an operation immediately upon completion. Depending on the platform, the outcome may be reported in a process exit code and the results recorded in the log file. This enables you to check the outcome from the command line or script. Table 21-4 shows the exit codes that get returned for various results.

Table 21-4 Exit Codes for Export

| Result | Exit Code |
| --- | --- |
| Export terminated successfully without warnings  Import terminated successfully without warnings | `EX_SUCC` |
| Export terminated successfully with warnings  Import terminated successfully with warnings | `EX_OKWARN` |
| Export terminated unsuccessfully  Import terminated unsuccessfully | `EX_FAIL` |

For UNIX, the exit codes are as follows:

```
EX_SUCC   0
EX_OKWARN 0
EX_FAIL   1
```

## Conventional Path Export Versus Direct Path Export

Export provides two methods for exporting table data:

- Conventional path Export
- Direct path Export

Conventional path Export uses the SQL `SELECT` statement to extract data from tables. Data is read from disk into a buffer cache, and rows are transferred to the evaluating buffer. The data, after passing expression evaluation, is transferred to the Export client, which then writes the data into the export file.

Direct path Export is much faster than conventional path Export because data is read from disk into the buffer cache and rows are transferred directly to the Export client. The evaluating buffer (that is, the SQL command-processing layer) is bypassed. The data is already in the format that Export expects, thus avoiding unnecessary data conversion. The data is transferred to the Export client, which then writes the data into the export file.

## Invoking a Direct Path Export

To use direct path Export, specify the `DIRECT=y` parameter on the command line or in the parameter file. The default is `DIRECT=n,` which extracts the table data using the conventional path. The rest of this section discusses the following topics:

- Security Considerations for Direct Path Exports
- Performance Considerations for Direct Path Exports
- Restrictions for Direct Path Exports

### Security Considerations for Direct Path Exports

Oracle Virtual Private Database (VPD) and Oracle Label Security are not enforced during direct path Exports.

The following users are exempt from Virtual Private Database and Oracle Label Security enforcement regardless of the export mode, application, or utility used to extract data from the database:

- The database user `SYS`
- Database users granted the `EXEMPT` `ACCESS` `POLICY` privilege, either directly or through a database role

This means that any user who is granted the `EXEMPT` `ACCESS` `POLICY` privilege is completely exempt from enforcement of VPD and Oracle Label Security. This is a powerful privilege and should be carefully managed. This privilege does not affect the enforcement of traditional object privileges such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE`. These privileges are enforced even if a user has been granted the `EXEMPT` `ACCESS` `POLICY` privilege.

### Performance Considerations for Direct Path Exports

You may be able to improve performance by increasing the value of the `RECORDLENGTH` parameter when you invoke a direct path Export. Your exact performance gain depends upon the following factors:

- `DB_BLOCK_SIZE`
- The types of columns in your table
- Your I/O layout (The drive receiving the export file should be separate from the disk drive where the database files reside.)

The following values are generally recommended for `RECORDLENGTH:`

- Multiples of the file system I/O block size
- Multiples of `DB_BLOCK_SIZE`

An export file that is created using direct path Export will take the same amount of time to import as an export file created using conventional path Export.

### Restrictions for Direct Path Exports

Keep the following restrictions in mind when you are using direct path mode:

- To invoke a direct path Export, you must use either the command-line method or a parameter file. You cannot invoke a direct path Export using the interactive method.
- The Export parameter `BUFFER` applies only to conventional path Exports. For direct path Export, use the `RECORDLENGTH` parameter to specify the size of the buffer that Export uses for writing to the export file.
- You cannot use direct path when exporting in tablespace mode (`TRANSPORT_TABLESPACES` = `Y`).
- The `QUERY` parameter cannot be specified in a direct path Export.
- A direct path Export can only export data when the `NLS_LANG` environment variable of the session invoking the export equals the database character set. If `NLS_LANG` is not set or if it is different than the database character set, then a warning is displayed and the export is discontinued. The default value for the `NLS_LANG` environment variable is `AMERICAN_AMERICA.US7ASCII`.

## Network Considerations

This section describes factors to consider when using Export across a network.

### Transporting Export Files Across a Network

Because the export file is in binary format, use a protocol that supports binary transfers to prevent corruption of the file when you transfer it across a network. For example, use FTP or a similar file transfer protocol to transmit the file in binary mode. Transmitting export files in character mode causes errors when the file is imported.

### Exporting with Oracle Net

With Oracle Net, you can perform exports over a network. For example, if you run Export locally, then you can write data from a remote Oracle database into a local export file.

To use Export with Oracle Net, include the connection qualifier string `@` `connect_string` when entering the username and password in the `exp` command. For the exact syntax of this clause, see the user's guide for your Oracle Net protocol.

## Character Set and Globalization Support Considerations

The following sections describe the globalization support behavior of Export with respect to character set conversion of user data and data definition language (DDL).

### User Data

The Export utility always exports user data, including Unicode data, in the character sets of the Export server. (Character sets are specified at database creation.) If the character sets of the source database are different than the character sets of the import database, then a single conversion is performed to automatically convert the data to the character sets of the Import server.

#### Effect of Character Set Sorting Order on Conversions

If the export character set has a different sorting order than the import character set, then tables that are partitioned on character columns may yield unpredictable results. For example, consider the following table definition, which is produced on a database having an ASCII character set:

```
CREATE TABLE partlist 
   ( 
   part     VARCHAR2(10), 
   partno   NUMBER(2) 
   ) 
PARTITION BY RANGE (part) 
  ( 
  PARTITION part_low VALUES LESS THAN ('Z') 
    TABLESPACE tbs_1, 
  PARTITION part_mid VALUES LESS THAN ('z') 
    TABLESPACE tbs_2, 
  PARTITION part_high VALUES LESS THAN (MAXVALUE) 
    TABLESPACE tbs_3 
  );
```

This partitioning scheme makes sense because `z` comes after `Z` in ASCII character sets.

When this table is imported into a database based upon an EBCDIC character set, all of the rows in the `part_mid` partition will migrate to the `part_low` partition because `z` comes before `Z` in EBCDIC character sets. To obtain the desired results, the owner of `partlist` must repartition the table following the import.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm)

### Data Definition Language (DDL)

Up to three character set conversions may be required for data definition language (DDL) during an export/import operation:

1. Export writes export files using the character set specified in the `NLS_LANG` environment variable for the user session. A character set conversion is performed if the value of `NLS_LANG` differs from the database character set.
2. If the export file's character set is different than the import user session character set, then Import converts the character set to its user session character set. Import can only perform this conversion for single-byte character sets. This means that for multibyte character sets, the import file's character set must be identical to the export file's character set.
3. A final character set conversion may be performed if the target database's character set is different from the character set used by the import user session.

To minimize data loss due to character set conversions, ensure that the export database, the export user session, the import user session, and the import database all use the same character set.

### Single-Byte Character Sets and Export and Import

Some 8-bit characters can be lost (that is, converted to 7-bit equivalents) when you import an 8-bit character set export file. This occurs if the system on which the import occurs has a native 7-bit character set, or the `NLS_LANG` operating system environment variable is set to a 7-bit character set. Most often, this is apparent when accented characters lose the accent mark.

To avoid this unwanted conversion, you can set the `NLS_LANG` operating system environment variable to be that of the export file character set.

### Multibyte Character Sets and Export and Import

During character set conversion, any characters in the export file that have no equivalent in the target character set are replaced with a default character. (The default character is defined by the target character set.) To guarantee 100% conversion, the target character set must be a superset (or equivalent) of the source character set.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm)

Caution:

When the character set width differs between the Export server and the Import server, truncation of data can occur if conversion causes expansion of data. If truncation occurs, then Import displays a warning message.

## Using Instance Affinity with Export and Import

You can use instance affinity to associate jobs with instances in databases you plan to export and import. Be aware that there may be some compatibility issues if you are using a combination of releases.

## Considerations When Exporting Database Objects

The following sections describe points you should consider when you export particular database objects.

### Exporting Sequences

If transactions continue to access sequence numbers during an export, then sequence numbers might be skipped. The best way to ensure that sequence numbers are not skipped is to ensure that the sequences are not accessed during the export.

Sequence numbers can be skipped only when cached sequence numbers are in use. When a cache of sequence numbers has been allocated, they are available for use in the current database. The exported value is the next sequence number (after the cached values). Sequence numbers that are cached, but unused, are lost when the sequence is imported.

### Exporting LONG and LOB Datatypes

On export, `LONG` datatypes are fetched in sections. However, enough memory must be available to hold all of the contents of each row, including the LONG data.

`LONG` columns can be up to 2 gigabytes in length.

All data in a LOB column does not need to be held in memory at the same time. LOB data is loaded and unloaded in sections.

Note:

Oracle also recommends that you convert existing `LONG` columns to LOB columns. LOB columns are subject to far fewer restrictions than `LONG` columns. Further, LOB functionality is enhanced in every release, whereas LONG functionality has been static for several releases.

### Exporting Foreign Function Libraries

The contents of foreign function libraries are not included in the export file. Instead, only the library specification (name, location) is included in full database mode and user-mode export. You must move the library's executable files and update the library specification if the database is moved to a new location.

### Exporting Offline Locally Managed Tablespaces

If the data you are exporting contains offline locally managed tablespaces, then Export will not be able to export the complete tablespace definition and will display an error message. You can still import the data; however, you must create the offline locally managed tablespaces before importing to prevent DDL commands that may reference the missing tablespaces from failing.

### Exporting Directory Aliases

Directory alias definitions are included only in a full database mode export. To move a database to a new location, the database administrator must update the directory aliases to point to the new location.

Directory aliases are not included in user-mode or table-mode export. Therefore, you must ensure that the directory alias has been created on the target system before the directory alias is used.

### Exporting BFILE Columns and Attributes

The export file does not hold the contents of external files referenced by `BFILE` columns or attributes. Instead, only the names and directory aliases for files are copied on Export and restored on Import. If you move the database to a location where the old directories cannot be used to access the included files, then the database administrator (DBA) must move the directories containing the specified files to a new location where they can be accessed.

### Exporting External Tables

The contents of external tables are not included in the export file. Instead, only the table specification (name, location) is included in full database mode and user-mode export. You must manually move the external data and update the table specification if the database is moved to a new location.

### Exporting Object Type Definitions

In all Export modes, the Export utility includes information about object type definitions used by the tables being exported. The information, including object name, object identifier, and object geometry, is needed to verify that the object type on the target system is consistent with the object instances contained in the export file. This ensures that the object types needed by a table are created with the same object identifier at import time.

Note, however, that in table mode, user mode, and tablespace mode, the export file does not include a full object type definition needed by a table if the user running Export does not have execute access to the object type. In this case, only enough information is written to verify that the type exists, with the same object identifier and the same geometry, on the Import target system.

The user must ensure that the proper type definitions exist on the target system, either by working with the DBA to create them, or by importing them from full database mode or user-mode exports performed by the DBA.

It is important to perform a full database mode export regularly to preserve all object type definitions. Alternatively, if object type definitions from different schemas are used, then the DBA should perform a user mode export of the appropriate set of users. For example, if `table1` belonging to user `scott` contains a column on `blake` 's type `type1,` then the DBA should perform a user mode export of both `blake` and `scott` to preserve the type definitions needed by the table.

### Exporting Nested Tables

Inner nested table data is exported whenever the outer containing table is exported. Although inner nested tables can be named, they cannot be exported individually.

### Exporting Advanced Queue (AQ) Tables

Queues are implemented on tables. The export and import of queues constitutes the export and import of the underlying queue tables and related dictionary tables. You can export and import queues only at queue table granularity.

When you export a queue table, both the table definition information and queue data are exported. Because the queue table data and the table definition is exported, the user is responsible for maintaining application-level data integrity when queue table data is imported.

See Also:

[Oracle Streams Advanced Queuing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11013/toc.htm)

### Exporting Synonyms

You should be cautious when exporting compiled objects that reference a name used as a synonym and as another object. Exporting and importing these objects will force a recompilation that could result in changes to the object definitions.

The following example helps to illustrate this problem:

```
CREATE PUBLIC SYNONYM emp FOR scott.emp;

CONNECT blake/paper;
CREATE TRIGGER t_emp BEFORE INSERT ON emp BEGIN NULL; END;
CREATE VIEW emp AS SELECT * FROM dual;
```

If the database in the preceding example were exported, then the reference to `emp` in the trigger would refer to `blake` 's view rather than to `scott` 's table. This would cause an error when Import tried to reestablish the `t_emp` trigger.

### Support for Fine-Grained Access Control

You can export tables with fine-grained access control policies enabled. When doing so, consider the following:

- The user who imports from an export file containing such tables must have the appropriate privileges (specifically, the `EXECUTE` privilege on the `DBMS_RLS` package so that the tables' security policies can be reinstated). If a user without the correct privileges attempts to export a table with fine-grained access policies enabled, then only those rows that the exporter is privileged to read will be exported.
- If fine-grained access control is enabled on a `SELECT` statement, then conventional path Export may not export the entire table because fine-grained access may rewrite the query.
- Only user SYS, or a user with the `EXP_FULL_DATABASE` role enabled or who has been granted `EXEMPT ACCESS POLICY`, can perform direct path Exports on tables having fine-grained access control.

## Transportable Tablespaces

The transportable tablespace feature enables you to move a set of tablespaces from one Oracle database to another.

Note:

You cannot export transportable tablespaces and then import them into a database at a lower release level. The target database must be at the same or higher release level as the source database.

To move or copy a set of tablespaces, you must make the tablespaces read-only, copy the data files of these tablespaces, and use Export and Import to move the database information (metadata) stored in the data dictionary. Both the data files and the metadata export file must be copied to the target database. The transport of these files can be done using any facility for copying flat binary files, such as the operating system copying facility, binary-mode FTP, or publishing on CD-ROMs.

After copying the data files and exporting the metadata, you can optionally put the tablespaces in read/write mode.

Export and Import provide the following parameters to enable movement of transportable tablespace metadata.

- `TABLESPACES`
- `TRANSPORT_TABLESPACE`

See "TABLESPACES" and "TRANSPORT\_TABLESPACE" for more information about using these parameters during an export operation.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for details about managing transportable tablespaces
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for an introduction to transportable tablespaces

## Exporting From a Read-Only Database

To extract metadata from a source database, Export uses queries that contain ordering clauses (sort operations). For these queries to succeed, the user performing the export must be able to allocate sort segments. For these sort segments to be allocated in a read-only database, the user's temporary tablespace should be set to point at a temporary, locally managed tablespace.

## Using Export and Import to Partition a Database Migration

When you use the Export and Import utilities to migrate a large database, it may be more efficient to partition the migration into multiple export and import jobs. If you decide to partition the migration, then be aware of the following advantages and disadvantages.

### Advantages of Partitioning a Migration

Partitioning a migration has the following advantages:

- Time required for the migration may be reduced, because many of the subjobs can be run in parallel.
- The import can start as soon as the first export subjob completes, rather than waiting for the entire export to complete.

### Disadvantages of Partitioning a Migration

Partitioning a migration has the following disadvantages:

- The export and import processes become more complex.
- Support of cross-schema references for certain types of objects may be compromised. For example, if a schema contains a table with a foreign key constraint against a table in a different schema, then you may not have the required parent records when you import the table into the dependent schema.

### How to Use Export and Import to Partition a Database Migration

To perform a database migration in a partitioned manner, take the following steps:

1. For all top-level metadata in the database, issue the following commands:
	1. `exp FILE=full FULL=y CONSTRAINTS=n TRIGGERS=n ROWS=n INDEXES=n`
		2. `imp FILE=full FULL=y`
2. For each schema `n` in the database, issue the following commands:
	1. `exp OWNER=schema` `n` `FILE=schema` `n`
		2. `imp FILE=schema` `n` `FROMUSER=schema` `n` `TOUSER=schema` `n` `IGNORE=y`

All exports can be done in parallel. When the import of `full`.`dmp` completes, all remaining imports can also be done in parallel.

## Using Different Releases of Export and Import

This section describes compatibility issues that relate to using different releases of Export and the Oracle database.

Whenever you are moving data between different releases of the Oracle database, the following basic rules apply:

- The Import utility and the database to which data is being imported (the target database) must be the same release. For example, if you try to use the Import utility 9.2.0.7 to import into a 9.2.0.8 database, then you may encounter errors.
- The version of the Export utility must be equal to the release of either the source or target database, whichever is earlier.
	For example, to create an export file for an import into a later release database, use a version of the Export utility that equals the source database. Conversely, to create an export file for an import into an earlier release database, use a version of the Export utility that equals the release of the target database.
	- In general, you can use the Export utility from any Oracle8 release to export from an Oracle9i server and create an Oracle8 export file.

### Restrictions When Using Different Releases of Export and Import

The following restrictions apply when you are using different releases of Export and Import:

- Export dump files can be read only by the Import utility because they are stored in a special binary format.
- Any export dump file can be imported into a later release of the Oracle database.
- The Import utility cannot read export dump files created by the Export utility of a later maintenance release. For example, a release 9.2 export dump file cannot be imported by a release 9.0.1 Import utility.
- Whenever a lower version of the Export utility runs with a later release of the Oracle database, categories of database objects that did not exist in the earlier release are excluded from the export.
- Export files generated by Oracle9i Export, either direct path or conventional path, are incompatible with earlier releases of Import and can be imported only with Oracle9i Import. When backward compatibility is an issue, use the earlier release or version of the Export utility against the Oracle9i database.

### Examples of Using Different Releases of Export and Import

Table 21-5 shows some examples of which Export and Import releases to use when moving data between different releases of the Oracle database.

Table 21-5 Using Different Releases of Export and Import

| Export from->Import to | Use Export Release | Use Import Release |
| --- | --- | --- |
| 8.1.6 -> 8.1.6 | 8.1.6 | 8.1.6 |
| 8.1.5 -> 8.0.6 | 8.0.6 | 8.0.6 |
| 8.1.7 -> 8.1.6 | 8.1.6 | 8.1.6 |
| 9.0.1 -> 8.1.6 | 8.1.6 | 8.1.6 |
| 9.0.1 -> 9.0.2 | 9.0.1 | 9.0.2 |
| 9.0.2 -> 10.1.0 | 9.0.2 | 10.1.0 |
| 10.1.0 -> 9.0.2 | 9.0.2 | 9.0.2 |

Table 21-5 covers moving data only between the original Export and Import utilities. For Oracle Database 10g release 1 (10.1) or higher, Oracle recommends the Data Pump Export and Import utilities in most cases because these utilities provide greatly enhanced performance compared to the original Export and Import utilities.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/expimp.htm#UPGRD12560) for more information about exporting and importing data between different releases, including releases higher than 10.1