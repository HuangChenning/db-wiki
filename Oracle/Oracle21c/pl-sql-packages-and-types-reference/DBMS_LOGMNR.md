---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_LOGMNR.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 106 DBMS\_LOGMNR

The `DBMS_LOGMNR` package, one of a set of LogMiner packages, contains the subprograms you use to initialize the LogMiner tool and to begin and end a LogMiner session.

Note:

The ability to create flat file dictionary dumps of pluggable databases (PDBs) is desupported in Oracle Database 21c.

In previous releases, using a flat file dictionary was one means of mining the redo logs for the changes associated with a specific PDB whose data dictionary was contained within the flat file. This feature is now desupported. Starting with Oracle Database 21c, Oracle recommends that you call `DBMS_LOGMNR.START_LOGMNR`, and supply the system change number (SCN) or time range that you want to mine. The SCN or time range options of `START_LOGMNR` are enhanced to support mining of individual PDBs.

The `CONTINUOUS_MINE` functionality of the LogMiner package is obsolete. It was deprecated in Oracle Database 12c release 2 (12.2). There is no replacement functionality.

This chapter contains the following topics:

See Also:

[Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SUTIL019) for information regarding LogMiner.

### 106.1 DBMS\_LOGMNR Overview

Oracle LogMiner, which is part of Oracle Database, enables you to query online and archived redo log files through a SQL interface. The `DBMS_LOGMNR` package provides the majority of the tools needed to start and stop LogMiner and specify the redo log files of interest.

All changes made to user data or to the database dictionary are recorded in the Oracle redo log files so that database recovery operations can be performed. You can take advantage of the data recorded in the redo log files to accomplish other tasks, such as:

- Pinpointing when a logical corruption to a database, such as errors made at the application level, may have begun
- Determining what actions you would have to take to perform fine-grained recovery at the transaction level.
- Performance tuning and capacity planning through trend analysis.
- Track any data manipulation language (DML) and data definition language (DDL) statements executed on the database, the order in which they were executed, and who executed them.

See Also:

[DBMS\_LOGMNR\_D](DBMS_LOGMNR_D.md) for information on the package subprograms that extract a LogMiner dictionary and re-create LogMiner tables in alternate tablespaces

### 106.2 DBMS\_LOGMNR Security Model

You must have the `EXECUTE_CATALOG_ROLE` role to use the `DBMS_LOGMNR` package.

### 106.3 DBMS\_LOGMNR Constants

The `DBMS_LOGMNR` package defines several enumerated constants for specifying parameter values. Enumerated constants must be prefixed with the package name, for example, `DBMS_LOGMNR.NEW`.

Note:

The `continuous_mine` option for the `dbms_logmnr.start_logmnr` package is desupported in Oracle Database 19c (19.1), and is no longer available.

The following table describes the constants for the `ADD_LOGFILE` `options` flag in the `DBMS_LOGMNR` package.

Table 106-1 Constants for ADD\_LOGFILE Options Flag

| Constant | Description |
| --- | --- |
| `NEW` | Implicitly calls the `DBMS_LOGMNR.END_LOGMNR` procedure to end the current LogMiner session and then creates a new session. The new session starts a new list of redo log files to be analyzed, beginning with the redo log file you specify. |
| `ADDFILE` | Adds the specified redo log file to the list of redo log files to be analyzed. Any attempt to add a duplicate file raises an exception (`ORA-01289`). This is the default if no options flag is specified. |

Table 106-2 describes the constants for the `START_LOGMNR` options flag in the `DBMS_LOGMNR` package.

Table 106-2 Constants for START\_LOGMNR Options Flag

| Constant | Description |
| --- | --- |
| `COMMITTED_DATA_ONLY` | If set, DML statements corresponding to committed transactions are returned. DML statements corresponding to a committed transaction are grouped together. Transactions are returned in their commit order. Transactions that are rolled back or in-progress are filtered out, as are internal redo records (those related to index operations, management, and so on).  If this option is not set, all rows for all transactions (committed, rolled back, and in-progress) are returned in the order in which they are found in the redo logs (in order of SCN values). |
| `SKIP_CORRUPTION` | Directs a select operation on the `V$LOGMNR_CONTENTS` view to skip any corruptions in the redo log file being analyzed and continue processing. This option works only when a block in the redo log file (and not the header of the redo log file) is corrupt. You should check the `INFO` column in the `V$LOGMNR_CONTENTS` view to determine the corrupt blocks skipped by LogMiner. When a corruption in the redo log file is skipped, the `OPERATION` column contains the value `CORRUPTED_BLOCKS`, and the `STATUS` column contains the value `1343.` |
| `DDL_DICT_TRACKING` | If the LogMiner dictionary in use is a flat file or in the redo log files, LogMiner updates its internal dictionary if a DDL event occurs. This ensures that correct `SQL_REDO` and `SQL_UNDO` information is maintained for objects that are modified after the LogMiner internal dictionary is built. The database to which LogMiner is connected must be open.  This option cannot be used in conjunction with the `DICT_FROM_ONLINE_CATALOG` option and cannot be used when the LogMiner dictionary being used is one that was extracted to a flat file prior to Oracle9i. |
| `DICT_FROM_ONLINE_CATALOG` | Directs LogMiner to use the current online database dictionary rather than a LogMiner dictionary contained in a flat file or in the redo log files being analyzed.  This option cannot be used in conjunction with the `DDL_DICT_TRACKING` option. The database to which LogMiner is connected must be the same one that generated the redo log files.  Expect to see a value of `2` in the `STATUS` column of the `V$LOGMNR_CONTENTS` view if the table definition in the database does not match the table definition in the redo log file. |
| `DICT_FROM_REDO_LOGS` | If set, LogMiner expects to find a LogMiner dictionary in the redo log files that were specified. The redo log files are specified with the `DBMS_LOGMNR.ADD_LOGFILE` procedure or with the `DBMS_LOGMNR.START_LOGMNR` procedure. |
| `NO_SQL_DELIMITER` | If set, the SQL delimiter (a semicolon) is not placed at the end of reconstructed SQL statements. This is helpful for applications that open a cursor and then execute the reconstructed statements. |
| `NO_ROWID_IN_STMT` | If set, the `ROWID` clause is not included in the reconstructed SQL statements. The redo log file may already contain logically unique identifiers for modified rows if supplemental logging is enabled.  When using this option, you must be sure that supplemental logging was enabled in the source database at the appropriate level and that no duplicate rows exist in the tables of interest. LogMiner does not make any guarantee regarding the uniqueness of logical row identifiers. |
| `PRINT_PRETTY_SQL` | If set, LogMiner formats the reconstructed SQL statements for ease of reading. These reconstructed SQL statements are not executable. |
| `STRING_LITERALS_IN_STMT` | If set, SQL\_REDO and SQL\_UNDO use literals for numbers and datetime and interval column types. |

To specify more than one option, use a plus sign (+) between them. For example:

```
EXECUTE DBMS_LOGMNR.START_LOGMNR(OPTIONS => -
   DBMS_LOGMNR.DDL_DICT_TRACKING + DBMS_LOGMNR.DICT_FROM_REDO_LOGS);
```

### 106.4 DBMS\_LOGMNR Views

The `DBMS_LOGMNR` package uses the views listed under Accessing Logminer Operational Information In Views in Oracle Database Utilities.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SUTIL1594)

### 106.5 DBMS\_LOGMNR Operational Notes

A LogMiner session begins with a call to `DBMS_LOGMNR.ADD_LOGFILE` or `DBMS_LOGMNR.START_LOGMNR` (the former if you plan to specify log files explicitly; the latter if you plan to use continuous mining). The session ends with a call to `DBMS_LOGMNR.END_LOGMNR`.

Within a LogMiner session, you can specify the redo log files to be analyzed and the SCN or time range of interest; then you can issue SQL `SELECT` statements against the `V$LOGMNR_CONTENTS` view to retrieve the data of interest.

`ADD_LOGFILE` Procedure must be invoked before `START_LOGMNR` Procedure.

Note:

You must add log files before filtering. Continuous logging is no longer supported. If logfiles have not been added that match the time or the SCN that you provide, then `DBMS_LOGMNR.START_LOGMNR` fails with the error `ORA-01291: missing logfile`.

### 106.6 Summary of DBMS\_LOGMNR Subprograms

This table lists the `DBMS_LOGMNR` subprograms and briefly describes them.

In a multitenant container database (CDB) some subprograms must be called from the root. There may be other differences as well. See the individual subprogram descriptions for details.

Table 106-3 DBMS\_LOGMNR Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_LOGFILE Procedure | Adds a redo log file to the existing or newly created list of redo log files for LogMiner to process, so that if a new list is created, this marks the beginning of a LogMiner session |
| COLUMN\_PRESENT Function | Call this function for any row returned from the `V$LOGMNR_CONTENTS` view to determine if undo or redo column values exist for the column specified by the `column_name` input parameter to this function |
| END\_LOGMNR Procedure | Finishes a LogMiner session |
| MINE\_VALUE Function | Call this function for any row returned from the `V$LOGMNR_CONTENTS` view to retrieve the undo or redo column value of the column specified by the `column_name` input parameter to this function |
| REMOVE\_LOGFILE Procedure | Removes a redo log file from the list of redo log files for LogMiner to process |
| START\_LOGMNR Procedure | Initializes the LogMiner utility and starts LogMiner (unless the session was already started with a call to `DBMS_LOGMNR.ADD_LOGFILE`) |

#### 106.6.1 ADD\_LOGFILE Procedure

This procedure adds a file to an existing or newly created list of log files for LogMiner to process.

Note:

The `continuous_mine` option for the `dbms_logmnr.start_logmnr` package is desupported in Oracle Database 19c (19.1), and is no longer available.

In a CDB, the `ADD_LOGFILE` procedure must be called from the root database. You must have the `LOGMINING` administrative privilege to use this procedure.

Syntax

```
DBMS_LOGMNR.ADD_LOGFILE ( 
   LogFileName     IN VARCHAR2,
   options         IN BINARY_INTEGER default ADDFILE );
```

Parameters

Table 106-4 ADD\_LOGFILE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `LogFileName` | Specifies the name of the redo log file to add to the list of redo log files to be analyzed during this session. |
| `options` | Does one of the following:  - Starts a new LogMiner session and a new list of redo log files for analysis (`DBMS_LOGMNR.NEW`) - Adds a file to an existing list of redo log files for analysis (`DBMS_LOGMNR.ADDFILE`)  See Table 106-1. |

Exceptions

Table 106-5 ADD\_LOGFILE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-01284` | Specified file cannot be opened. |
| `ORA-01287` | Specified file is from a different database incarnation. |
| `ORA-01289` | Specified file has already been added to the list. Duplicate redo log files cannot be added. |
| `ORA-01290` | Specified file is not in the current list and therefore cannot be removed from the list. |
| `ORA-01324` | Specified file cannot be added to the list because there is a DB\_ID mismatch. |

Usage Notes

- The `DBMS_LOGMNR.ADD_LOGFILE` call from a PDB connection is not supported for adhoc users and returns error `65040`.
- Dumping Flat File dictionary and mining using Flat File dictionary are not supported from a PDB connection.
- Before querying the `V$LOGMNR_CONTENTS` view, you must make a successful call to the `DBMS_LOGMNR.START_LOGMNR` procedure (within the current LogMiner session).
- The LogMiner session must be set up with a list of redo log files to be analyzed. Use the `ADD_LOGFILE` procedure to specify the list of redo log files to analyze.
- If you want to analyze more than one redo log file, you must call the `ADD_LOGFILE` procedure separately for each redo log file. The redo log files do not need to be registered in any particular order.
- Both archived and online redo log files can be mined.
- After you have added the first redo log file to the list, each additional redo log file that you add to the list must be associated with the same database and database `RESETLOGS` `SCN` as the first redo log file. (The database `RESETLOGS` `SCN` uniquely identifies each execution of an `ALTER` `DATABASE` `OPEN` `RESETLOGS` statement. When the online redo logs are reset, Oracle creates a new and unique incarnation of the database.)
- To analyze the redo log files from a different database (or a database incarnation with a different database `RESETLOGS SCN`) than that with which the current list of redo log files is associated, use the `END_LOGMNR` procedure to end the current LogMiner session, and then build a new list using the `ADD_LOGFILE` procedure.
- LogMiner matches redo log files by the log sequence number. Thus, two redo log files with different names but with the same log sequence number will return the ORA-01289 exception. For instance, the online counterpart of an archived redo log file has a different name from the archived redo log file, but attempting to register it with LogMiner after registering the archived counterpart will result in the ORA-01289 exception being returned.

#### 106.6.2 COLUMN\_PRESENT Function

This function is designed to be used in conjunction with the `MINE_VALUE` function.

If the `MINE_VALUE` function returns a `NULL` value, it can mean either:

- The specified column is not present in the redo or undo portion of the data.
- The specified column is present and has a `NULL` value.

To distinguish between these two cases, use the `COLUMN_PRESENT` function, which returns a `1` if the column is present in the redo or undo portion of the data. Otherwise, it returns a `0`.

Syntax

```
DBMS_LOGMNR.COLUMN_PRESENT (
     sql_redo_undo      IN  RAW,
     column_name        IN  VARCHAR2 default '') RETURN NUMBER;
```

Parameters

Table 106-6 COLUMN\_PRESENT Function Parameters

| Parameter | Description |
| --- | --- |
| `sql_redo_undo` | Specifies either the `REDO_VALUE` or the `UNDO_VALUE` column in the `V$LOGMNR_CONTENTS` view from which to extract data values. See the Usage Notes for more information. |
| `column_name` | Specifies the fully qualified name (`schema.table.column`) of the column for which this function will return information.  In a CDB, the column name is specified as follows:  `container_name:schema.table.column` |

Return Values

Table 106-7 describes the return values for the `COLUMN_PRESENT` function. The `COLUMN_PRESENT` function returns 1 if the self-describing record (the first parameter) contains the column specified in the second parameter. This can be used to determine the meaning of `NULL` values returned by the `DBMS_LOGMNR.MINE_VALUE` function.

Table 106-7 Return Values for COLUMN\_PRESENT Function

| Return | Description |
| --- | --- |
| `0` | Specified column is not present in this row of `V$LOGMNR_CONTENTS`. |
| `1` | Column is present in this row of `V$LOGMNR_CONTENTS`. |

Exceptions

Table 106-8 COLUMN\_PRESENT Function Exceptions

| Exception | Description |
| --- | --- |
| `ORA-01323` | Currently, a LogMiner dictionary is not associated with the LogMiner session. You must specify a LogMiner dictionary for the LogMiner session. |
| `ORA-00904` | Value specified for the `column_name` parameter is not a fully qualified column name. |

Usage Notes

- To use the `COLUMN_PRESENT` function, you must have successfully started LogMiner.
- The `COLUMN_PRESENT` function must be invoked in the context of a select operation on the `V$LOGMNR_CONTENTS` view.
- The `COLUMN_PRESENT` function does not support `LONG`, LOB, `ADT`, or `COLLECTION` datatypes.
- The value for the `sql_redo_undo` parameter depends on the operation performed and the data of interest:
	- If an update operation was performed and you want to know what the value was prior to the update operation, specify `UNDO_VALUE`.
		- If an update operation was performed and you want to know what the value is after the update operation, specify `REDO_VALUE`.
		- If an insert operation was performed, typically you would specify `REDO_VALUE` (because the value of a column prior to an insert operation will always be `NULL`).
		- If a delete operation was performed, typically you would specify `UNDO_VALUE` (because the value of a column after a delete operation will always be `NULL`).

#### 106.6.3 END\_LOGMNR Procedure

This procedure finishes a LogMiner session. Because this procedure performs cleanup operations that may not otherwise be done, you must use it to properly end a LogMiner session. This procedure is called automatically when you log out of a database session or when you call `DBMS_LOGMNR.ADD_LOGFILE` and specify the `NEW` option.

Syntax

```
DBMS_LOGMNR.END_LOGMNR;
```

Exceptions

Table 106-9 END\_LOGMNR Procedure Exception

| Exception | Description |
| --- | --- |
| `ORA-01307` | No LogMiner session is currently active. The `END_LOGMNR` procedure was called without adding any log files or before the `START_LOGMNR` procedure was called |

#### 106.6.4 MINE\_VALUE Function

This function facilitates queries based on a column's data value.

This function takes two arguments. The first one specifies whether to mine the redo (`REDO_VALUE`) or undo (`UNDO_VALUE`) portion of the data. The second argument is a string that specifies the fully qualified name of the column to be mined. The `MINE_VALUE` function always returns a string that can be converted back to the original datatype.

Syntax

```
DBMS_LOGMNR.MINE_VALUE (
     sql_redo_undo      IN  RAW,
     column_name        IN  VARCHAR2 default '') RETURN VARCHAR2;
```

Parameters

Table 106-10 MINE\_VALUE Function Parameters

| Parameter | Description |
| --- | --- |
| `sql_redo_undo` | Specifies either the `REDO_VALUE` or the `UNDO_VALUE` column in the `V$LOGMNR_CONTENTS` view from which to extract data values. See the Usage Notes for more information. |
| `column_name` | Specifies the fully qualified name (`schema.table.column`) of the column for which this function will return information.  In a CDB, the column name is specified as follows:  `container_name:schema.table.column` |

Return Values

Table 106-11 Return Values for MINE\_VALUE Function

| Return | Description |
| --- | --- |
| `NULL` | The column is not contained within the self-describing record, or the column value is `NULL`. To distinguish between the two different null possibilities, use the `DBMS_LOGMNR.COLUMN_PRESENT` function. |
| `NON-NULL` | The column is contained within the self-describing record; the value is returned in string format. |

Exceptions

Table 106-12 MINE\_VALUE Function Exceptions

| Exception | Description |
| --- | --- |
| `ORA-01323` | Invalid state. Currently, a LogMiner dictionary is not associated with the LogMiner session. You must specify a LogMiner dictionary for the LogMiner session. |
| `ORA-00904` | Invalid identifier. The value specified for the `column_name` parameter was not a fully qualified column name. |

Usage Notes

- To use the `MINE_VALUE` function, you must have successfully started LogMiner.
- The `MINE_VALUE` function must be invoked in the context of a select operation from the `V$LOGMNR_CONTENTS` view.
- The `MINE_VALUE` function does not support `LONG`, LOB, `ADT`, or `COLLECTION` datatypes.
- The value for the `sql_redo_undo` parameter depends on the operation performed and the data of interest:
	- If an update operation was performed and you want to know what the value was prior to the update operation, specify `UNDO_VALUE`.
		- If an update operation was performed and you want to know what the value is after the update operation, specify `REDO_VALUE`.
		- If an insert operation was performed, typically you would specify `REDO_VALUE` (because the value of a column prior to an insert operation will always be null).
		- If a delete operation was performed, typically you would specify `UNDO_VALUE` (because the value of a column after a delete operation will always be null).
- If the `DBMS_LOGMNR.MINE_VALUE` function is used to get an `NCHAR` value that includes characters not found in the database character set, then those characters are returned as the replacement character (for example, an inverted question mark) of the database character set.

#### 106.6.5 REMOVE\_LOGFILE Procedure

This procedure removes a redo log file from an existing list of redo log files for LogMiner to process.

In a CDB, the `REMOVE_LOGFILE` procedure must be called from the root database. You must have the `LOGMINING` administrative privilege to use this procedure.

Syntax

```
DBMS_LOGMNR.REMOVE_LOGFILE ( 
   LogFileName     IN VARCHAR2);
```

Parameters

Table 106-13 REMOVE\_LOGFILE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `LogFileName` | Specifies the name of the redo log file to be removed from the list of redo log files to be analyzed during this session. |

Exceptions

Table 106-14 REMOVE\_LOGFILE Procedure Exception

| Exception | Description |
| --- | --- |
| `ORA-01290` | Cannot remove unlisted log file |

Usage Notes

- Before querying the `V$LOGMNR_CONTENTS` view, you must make a successful call to the `DBMS_LOGMNR.START_LOGMNR` procedure (within the current LogMiner session).
- You can use this procedure to remove a redo log file from the list of redo log files for LogMiner to process if you know that redo log file does not contain any data of interest.
- Multiple redo log files can be removed by calling this procedure repeatedly.
- The redo log files do not need to be removed in any particular order.
- To start a new list of redo log files for analysis, use the `END_LOGMNR` procedure to end the current LogMiner session, and then build a new list using the `ADD_LOGFILE` procedure.
- Even if you remove all redo log files from the list, any subsequent calls you make to the `ADD_LOGFILE` procedure must match the database ID and `RESETLOGS` `SCN` of the removed redo log files. Therefore, to analyze the redo log files from a different database (or a database incarnation with a different database `RESETLOGS` `SCN`) than that with which the current list of redo log files is associated, use the `END_LOGMNR` procedure to end the current LogMiner session, and then build a new list using the `ADD_LOGFILE` procedure.

#### 106.6.6 START\_LOGMNR Procedure

This procedure starts LogMiner by loading the dictionary that LogMiner will use to translate internal schema object identifiers to names.

In a CDB, the `START_LOGMNR` procedure must be called from the root database. You must have the `LOGMINING` administrative privilege to use this procedure.

Note:

The ability to create flat file dictionary dumps of pluggable databases (PDBs) is desupported in Oracle Database 21c.

In previous releases, using a flat file dictionary was one means of mining the redo logs for the changes associated with a specific PDB whose data dictionary was contained within the flat file. This feature is now desupported. Starting with Oracle Database 21c, Oracle recommends that you call `DBMS_LOGMNR.START_LOGMNR`, and supply the system change number (SCN) or time range that you want to mine. The SCN or time range options of `START_LOGMNR` are enhanced to support mining of individual PDBs.

Syntax

```
DBMS_LOGMNR.START_LOGMNR ( 
   startScn           IN NUMBER default 0,
   endScn             IN NUMBER default 0,
   startTime          IN DATE default '01-jan-1988',
   endTime            IN DATE default '31-dec-2110',
   DictFileName       IN VARCHAR2 default '',
   Options            IN BINARY_INTEGER default 0 );
```

Parameters

Table 106-15 START\_LOGMNR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `startScn` | Directs LogMiner to return only redo records with an SCN greater than or equal to the `startScn` specified. This fails if there is no redo log file containing the specified `startScn` value. (You can query the `FILENAME`, `LOW_SCN,` and `NEXT_SCN` columns in the `V$LOGMNR_LOGS` view for each redo log file to determine the range of SCN values contained in each redo log file.) |
| `endScn` | Directs LogMiner to return only redo records with an SCN less than or equal to the `endScn` specified. If you specify an `endScn` value that is beyond the value in any redo log file, then LogMiner uses the greatest endScn value in the redo log file that contains the most recent changes. (You can query the `FILENAME,` `LOW_SCN,` and `NEXT_SCN` columns in the `V$LOGMNR_LOGS` view for each redo log file to determine the range of SCN values contained in each redo log file.) |
| `startTime` | Directs LogMiner to return only redo records with a timestamp greater than or equal to the `startTime` specified. This fails if there is no redo log file containing the specified `startTime` value. (You can query the `FILENAME`, `LOW_TIME,` and `HIGH_TIME` columns in the `V$LOGMNR_LOGS` view for each redo log file to determine the range of time covered in each redo log file.)  This parameter is ignored if `startScn` is specified. See the Usage Notes for additional information. |
| `endTime` | Directs LogMiner to return only redo records with a timestamp less than or equal to the `endTime` specified. If you specify an `endTime` value that is beyond the value in any redo log file, then LogMiner will use the greatest `endTime` in the redo log file that contains the most recent changes. You can query the `FILENAME,` `LOW_TIME,` and `HIGH_TIME` columns in the V$LOGMNR\_LOGS view for each redo log file to determine the range of time covered in each redo log file.)  This parameter is ignored if `endScn` is specified. See the Usage Notes for additional information. |
| `DictFileName` | Specifies the flat file that contains the LogMiner dictionary. It is used to reconstruct `SQL_REDO` and `SQL_UNDO` columns in `V$LOGMNR_CONTENTS`, as well as to fully translate `SEG_NAME`, `SEG_OWNER`, `SEG_TYPE_NAME,` `TABLE_NAME,` and `TABLE_SPACE` columns. The fully qualified path name for the LogMiner dictionary file must be specified. (This file must have been created previously through the `DBMS_LOGMNR_D`.`BUILD` procedure.)  You need to specify this parameter only if neither `DICT_FROM_REDO_LOGS` nor `DICT_FROM_ONLINE_CATALOG` is specified. |
| `options` | See Table 106-2. |

Exceptions

Table 106-16 START\_LOGMNR Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-01280` | Internal error encountered. |
| `ORA-01281` | `startScn` or `endScn` parameter value is not a valid SCN, or `endScn` is less than `startScn`. |
| `ORA-01282` | value for the `startTime` parameter was greater than the value specified for the `endTime` parameter, or there was no redo log file that was compatible with the date range specified with the `startTime` and `endTime` parameters. |
| `ORA-01283` | Options parameter specified is invalid. |
| `ORA-01284` | LogMiner dictionary file specified in the `DictFileName` parameter has a full path length greater than 256 characters, or the file cannot be opened. |
| `ORA-01285` | Error reading specified file. |
| `ORA-01291` | Redo log files that are needed to satisfy the user's requested SCN or time range are missing. |
| `ORA-01292` | No log file has been specified for the current LogMiner session. |
| `ORA-01293` | Mounted database required for specified LogMiner options. |
| `ORA-01294` | Error occurred while processing information in the specified dictionary file, possible corruption. |
| `ORA-01295` | Specified LogMiner dictionary does not correspond to the database that produced the log files being analyzed. |
| `ORA-01296` | Character set mismatch between specified LogMiner dictionary and log files. |
| `ORA-01297` | Redo version mismatch between LogMiner dictionary and log files. |
| `ORA-01299` | Specified LogMiner dictionary corresponds to a different database incarnation. |
| `ORA-01300` | Writable database required for specified LogMiner options. |

Usage Notes

Note:

The `continuous_mine` option for the `dbms_logmnr.start_logmnr` package is desupported in Oracle Database 19c (19.1), and is no longer available.

- The `DBMS_LOGMNR.ADD_LOGFILE` call from a PDB connection is not supported for adhoc users and returns error `65040`.
- Users can specify the SCN range or the time range. The required logfiles will be added programmatically.
- Dumping Flat File dictionary and mining using Flat File dictionary are not supported from a PDB connection.
- LogMiner can use a dictionary that you previously extracted to the redo log files or to a flat file, or you can specify that LogMiner use the online catalog if LogMiner is mining data from the source system.
- After executing the `START_LOGMNR` procedure, you can query the following views:
	- `V$LOGMNR_CONTENTS` - contains history of information in redo log files
		- `V$LOGMNR_DICTIONARY` - contains current information about the LogMiner dictionary file extracted to a flat file
		- `V$LOGMNR_PARAMETERS` - contains information about the LogMiner session
	(You can query the `V$LOGMNR_LOGS` view after a redo log file list has been added to the list of files that LogMiner is to mine.)
- Parameters and options are not persistent across calls to `DBMS_LOGMNR.START_LOGMNR`. You must specify all desired parameters and options (including SCN and time ranges) each time you call `DBMS_LOGMNR.START_LOGMNR`
- Be aware that specifying redo log files using a timestamp is not precise.
- Keep the following in mind regarding starting and ending times or SCN ranges:
	- If you specify neither a `startTime` nor a `startScn` parameter, LogMiner will set the `startScn` parameter to use the lowest SCN value from the redo log file that contains the oldest changes.
		- If you specify both time and SCN values, LogMiner uses the SCN value or values and ignores the time values.
		- If you specify starting and ending time or SCN values and they are found in the LogMiner redo log file list, then LogMiner mines the logs indicated by those values.
		- If you specify starting and ending times or SCN values that are not in the LogMiner redo log file list, and you specify `DBMS_LOGMNR.START_LOGMNR`, and you specify:
		- `0` for the `startTime` or `startScn` value, then the lowest SCN in the LogMiner redo log file list will be used as the `startScn`
				- A nonzero number for the `startTime` or `startScn` value, then an error is returned
				- `0` or a nonzero number for the `endTime` or `endScn` value, then the highest SCN in the LogMiner redo log file list will be used as the `endScn`
		- If you specify starting and ending times or SCN values and they are not found in the LogMiner redo log file list, and you specify `DBMS_LOGMNR.START_LOGMNR`, and you specify:
		- `0` for the `startTime` or `startScn` value, then an error is returned.
				- A `startTime` or `startScn` value that is greater than any value in the database's archived redo log files, then LogMiner starts mining in the online redo log file. LogMiner will continue to process the online redo log file until it finds a change at, or beyond, the requested starting point before it returns rows from the `V$LOGMNR_CONTENTS` view.
				- An `endTime` or `endScn` parameter value that indicates a time or SCN in the future, then LogMiner includes the online redo log files when it mines. When you query the `V$LOGMNR_CONTENTS` view, rows will be returned from this view as changes are made to the database, and will not stop until LogMiner sees a change beyond the requested ending point.
				- `0` for the `endTime` or `endScn` parameter value, then LogMiner includes the online redo log files when it mines. When you query the `V$LOGMNR_CONTENTS` view, rows will be returned from this view as changes are made to the database, and will not stop until you enter CTL+C or you terminate the PL/SQL cursor.