---
title: "SQL*Loader Command-Line Reference"
book: Utilities
doc_id: E22490-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e22490/ldr_params.htm
tags:
  - oracle
  - 11g
  - utilities
---

## 8 SQL\*Loader Command-Line Reference

This chapter describes the command-line parameters used to invoke SQL\*Loader. The following topics are discussed:

## Invoking SQL\*Loader

This section describes how to invoke SQL\*Loader and specify parameters. It contains the following sections:

- Specifying Parameters on the Command Line
- Alternative Ways to Specify Parameters
- Loading Data Across a Network

### Specifying Parameters on the Command Line

When you invoke SQL\*Loader, you specify parameters to establish session characteristics. You can separate the parameters by commas, if you want to.

```
> sqlldr CONTROL=ulcase1.ctl
Username: scott
Password: password
```

Specifying by position means that you enter a value, but not the parameter name. In the following example, the username `scott` is provided and then the name of the control file, `ulcase1.ctl`. You are prompted for the password:

```
> sqlldr scott ulcase1.ctl
Password: password
```

Once a keyword specification is used, no positional specification is allowed after that. For example, the following command line would result in an error even though the position of `ulcase1.log` is correct:

```
> sqlldr scott CONTROL=ulcase1.ctl ulcase1.log
```

If you invoke SQL\*Loader without specifying any parameters, then SQL\*Loader displays a help screen that lists the available parameters and their default values.

See Also:

"Command-Line Parameters" for descriptions of all the command-line parameters

### Alternative Ways to Specify Parameters

If the length of the command line exceeds the size of the maximum command line on your system, then you can put certain command-line parameters in the control file by using the `OPTIONS` clause.

You can also group parameters together in a parameter file. You specify the name of this file on the command line using the `PARFILE` parameter when you invoke SQL\*Loader.

These alternative ways of specifying parameters are useful when you often use the same parameters with the same values.

Parameter values specified on the command line override parameter values specified in either a parameter file or in the `OPTIONS` clause.

See Also:

- ["OPTIONS Clause"](ldr_control_file.md)
- "PARFILE (parameter file)"

### Loading Data Across a Network

To use SQL\*Loader to load data across a network connection, you can specify a connect identifier in the connect string when you invoke the SQL\*Loader utility. This identifier can specify a database instance that is different from the current instance identified by the current Oracle System ID (SID). The connect identifier can be an Oracle Net connect descriptor or a net service name (usually defined in the `tnsnames.ora` file) that maps to a connect descriptor. Use of a connect identifier requires that you have Oracle Net Listener running (to start the default listener, enter `lsnrctl start`). The following example invokes SQL\*Loader for user `scott` using the connect identifier `inst1`:

```
> sqlldr CONTROL=ulcase1.ctl
Username: scott@inst1
Password: password
```

The local SQL\*Loader client connects to the database instance defined by the connect identifier `inst1` (a net service name), and loads the data, as specified in the `ulcase1.ctl` control file.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for more information about connect identifiers and Oracle Net Listener

## Command-Line Parameters

This section describes each SQL\*Loader command-line parameter. The defaults and maximum values listed for these parameters are for UNIX-based systems. They may be different on your operating system. Refer to your Oracle operating system-specific documentation for more information.

### BAD (bad file)

Default: The name of the data file, with an extension of.`bad`.

`BAD` specifies the name of the bad file created by SQL\*Loader to store records that cause errors during insert or that are improperly formatted. If you do not specify a file name, then the default is used. A bad file is not automatically created if there are no rejected records.

A bad file name specified on the command line becomes the bad file associated with the first `INFILE` statement in the control file.

Note that the name of the bad file can also be specified in the SQL\*Loader control file, using the `BADFILE` clause. If the bad file name is specified in the control file as well as on the command line, then the command line value takes precedence.

See Also:

["Specifying the Bad File"](ldr_control_file.md) for information about the format of bad files

### BINDSIZE (maximum size)

Default: To see the default value for this parameter, invoke SQL\*Loader without any parameters, as described in "Invoking SQL\*Loader".

`BINDSIZE` specifies the maximum size (bytes) of the bind array. The size of the bind array given by `BINDSIZE` overrides the default size (which is system dependent) and any size determined by `ROWS.`

See Also:

- ["Bind Arrays and Conventional Path Loads"](ldr_control_file.md)
- "READSIZE (read buffer size)"

### COLUMNARRAYROWS

Default: To see the default value for this parameter, invoke SQL\*Loader without any parameters, as described in "Invoking SQL\*Loader".

Specifies the number of rows to allocate for direct path column arrays. The value for this parameter is not calculated by SQL\*Loader. You must either specify it or accept the default.

### CONTROL (control file)

Default: none

`CONTROL` specifies the name of the SQL\*Loader control file that describes how to load the data. If a file extension or file type is not specified, then it defaults to.`ctl`. If the file name is omitted, then SQL\*Loader prompts you for it.

If the name of your SQL\*Loader control file contains special characters, then your operating system may require that they be preceded by an escape character. Also, if your operating system uses backslashes in its file system paths, then you may need to use multiple escape characters or to enclose the path in quotation marks. See your Oracle operating system-specific documentation for more information.

See Also:

[Chapter 9](ldr_control_file.md) for a detailed description of the SQL\*Loader control file

### DATA (data file)

Default: The name of the control file, with an extension of.`dat`.

`DATA` specifies the name of the data file containing the data to be loaded. If you do not specify a file extension or file type, then the default is.`dat.`

If you specify a data file on the command line and also specify data files in the control file with `INFILE,` then the data specified on the command line is processed first. The first data file specified in the control file is ignored. All other data files specified in the control file are processed.

If you specify a file processing option when loading data from the control file, then a warning message will be issued.

### DATE\_CACHE

Default: Enabled (for `1000` elements). To completely disable the date cache feature, set it to `0`.

The date cache is used to store the results of conversions from text strings to internal date format. The cache is useful because the cost of looking up dates is much less than converting from text format to date format. If the same dates occur repeatedly in the data file, then using the date cache can improve the speed of a direct path load.

`DATE_CACHE` specifies the date cache size (in entries). For example,  
`DATE_CACHE=5000` specifies that each date cache created can contain a maximum of 5000 unique date entries. Every table has its own date cache, if one is needed. A date cache is created only if at least one date or timestamp value is loaded that requires datatype conversion in order to be stored in the table.

The date cache feature is only available for direct path loads. It is enabled by default. The default date cache size is 1000 elements. If the default size is used and the number of unique input values loaded exceeds 1000, then the date cache feature is automatically disabled for that table. However, if you override the default and specify a nonzero date cache size and that size is exceeded, then the cache is not disabled.

You can use the date cache statistics (entries, hits, and misses) contained in the log file to tune the size of the cache for future similar loads.

See Also:

["Specifying a Value for the Date Cache"](ldr_modes.md)

### DIRECT (data path)

Default: `false`

`DIRECT` specifies the data path, that is, the load method to use, either conventional path or direct path. A value of `true` specifies a direct path load. A value of `false` specifies a conventional path load.

See Also:

[Chapter 12, "Conventional and Direct Path Loads"](ldr_modes.md)

### DISCARD (file name)

Default: The name of the data file, with an extension of `.dsc`.

`DISCARD` specifies a discard file (optional) to be created by SQL\*Loader to store records that are neither inserted into a table nor rejected.

A discard file specified on the command line becomes the discard file associated with the first `INFILE` statement in the control file. If the discard file is also specified in the control file, then the command-line value overrides it.

See Also:

["Discarded and Rejected Records"](ldr_concepts.md) for information about the format of discard files

### DISCARDMAX (integer)

Default: `ALL`

`DISCARDMAX` specifies the number of discard records to allow before data loading is terminated. To stop on the first discarded record, specify one (1).

### ERRORS (errors to allow)

Default: To see the default value for this parameter, invoke SQL\*Loader without any parameters, as described in "Invoking SQL\*Loader".

`ERRORS` specifies the maximum number of insert errors to allow. If the number of errors exceeds the value specified for `ERRORS`, then SQL\*Loader terminates the load. To permit no errors at all, set `ERRORS=0.` To specify that all errors be allowed, use a very high number.

On a single-table load, SQL\*Loader terminates the load when errors exceed this error limit. Any data inserted up that point, however, is committed.

SQL\*Loader maintains the consistency of records across all tables. Therefore, multitable loads do not terminate immediately if errors exceed the error limit. When SQL\*Loader encounters the maximum number of errors for a multitable load, it continues to load rows to ensure that valid rows previously loaded into tables are loaded into all tables and rejected rows are filtered out of all tables.

In all cases, SQL\*Loader writes erroneous records to the bad file.

### EXTERNAL\_TABLE

Default: `NOT_USED`

`EXTERNAL_TABLE` instructs SQL\*Loader whether to load data using the external tables option. There are three possible values:

- `NOT_USED` - the default value. It means the load is performed using either conventional or direct path mode.
- `GENERATE_ONLY` - places all the SQL statements needed to do the load using external tables, as described in the control file, in the SQL\*Loader log file. These SQL statements can be edited and customized. The actual load can be done later without the use of SQL\*Loader by executing these statements in SQL\*Plus.
- `EXECUTE` - attempts to execute the SQL statements that are needed to do the load using external tables. However, if any of the SQL statements returns an error, then the attempt to load stops. Statements are placed in the log file as they are executed. This means that if a SQL statement returns an error, then the remaining SQL statements required for the load will not be placed in the log file.
	If you use `EXTERNAL_TABLE` = `EXECUTE` and also use the `SEQUENCE` parameter in your SQL\*Loader control file, then SQL\*Loader creates a database sequence, loads the table using that sequence, and then deletes the sequence. The results of doing the load this way will be different than if the load were done with conventional or direct path. (For more information about creating sequences, see `CREATE` `SEQUENCE` in [Oracle Database SQL Language Reference.)](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm)

Note:

When the `EXTERNAL_TABLE` parameter is specified, any datetime data types (for example, `TIMESTAMP`) in a SQL\*Loader control file are automatically converted to a `CHAR` data type and use the external tables `date_format_spec` clause. See ["date\_format\_spec"](et_params.md).

Note that the external table option uses directory objects in the database to indicate where all data files are stored and to indicate where output files, such as bad files and discard files, are created. You must have `READ` access to the directory objects containing the data files, and you must have `WRITE` access to the directory objects where the output files are created. If there are no existing directory objects for the location of a data file or output file, then SQL\*Loader will generate the SQL statement to create one. Therefore, when the `EXECUTE` option is specified, you must have the `CREATE` `ANY` `DIRECTORY` privilege. If you want the directory object to be deleted at the end of the load, then you must also have the `DELETE` `ANY` `DIRECTORY` privilege.

Note:

The `EXTERNAL_TABLE=` `EXECUTE` qualifier tells SQL\*Loader to create an external table that can be used to load data and then execute the `INSERT` statement to load the data. All files in the external table must be identified as being in a directory object. SQL\*Loader attempts to use directory objects that already exist and that you have privileges to access. However, if SQL\*Loader does not find the matching directory object, then it attempts to create a temporary directory object. If you do not have privileges to create new directory objects, then the operation fails.

To work around this, use `EXTERNAL_TABLE=` `GENERATE_ONLY` to create the SQL statements that SQL\*Loader would try to execute. Extract those SQL statements and change references to directory objects to be the directory object that you have privileges to access. Then, execute those SQL statements.

When using a multitable load, SQL\*Loader does the following:

1. Creates a table in the database that describes all fields in the data file that will be loaded into any table.
2. Creates an `INSERT` statement to load this table from an external table description of the data.
3. Executes one `INSERT` statement for every table in the control file.

To see an example of this, run case study 5, but add the `EXTERNAL_TABLE=GENERATE_ONLY` parameter. To guarantee unique names in the external table, SQL\*Loader uses generated names for all fields. This is because the field names may not be unique across the different tables in the control file.

See Also:

- ["SQL\*Loader Case Studies"](ldr_concepts.md) for information on how to access case studies
- [Chapter 13, "External Tables Concepts"](et_concepts.md)
- [Chapter 14, "The ORACLE\_LOADER Access Driver"](et_params.md)

#### Restrictions When Using EXTERNAL\_TABLE

The following restrictions apply when you use the `EXTERNAL_TABLE` qualifier:

- Julian dates cannot be used when you insert data into a database table from an external table through SQL\*Loader. To work around this, use `TO_DATE` and `TO_CHAR` to convert the Julian date format, as shown in the following example:
	```
	TO_CHAR(TO_DATE(:COL1, 'MM-DD-YYYY'), 'J')
	```
- Built-in functions and SQL strings cannot be used for object elements when you insert data into a database table from an external table.

### FILE (tablespace file to load into)

Default: none

`FILE` specifies the database file to allocate extents from. It is used only for direct path parallel loads. By varying the value of the `FILE` parameter for different SQL\*Loader processes, data can be loaded onto a system with minimal disk contention.

See Also:

["Parallel Data Loading Models"](ldr_modes.md)

### LOAD (number of records to load)

Default: All records are loaded.

`LOAD` specifies the maximum number of logical records to load (after skipping the specified number of records). No error occurs if fewer than the maximum number of records are found.

### LOG (log file)

Default: The name of the control file, with an extension of.`log`.

`LOG` specifies the log file that SQL\*Loader will create to store logging information about the loading process.

### MULTITHREADING

Default: `true` on multiple-CPU systems, `false` on single-CPU systems

This parameter is available only for direct path loads.

By default, the multithreading option is always enabled (set to `true`) on multiple-CPU systems. In this case, the definition of a multiple-CPU system is a single system that has more than one CPU.

On single-CPU systems, multithreading is set to `false` by default. To use multithreading between two single-CPU systems, you must enable multithreading; it will not be on by default. This will allow stream building on the client system to be done in parallel with stream loading on the server system.

Multithreading functionality is operating system-dependent. Not all operating systems support multithreading.

See Also:

["Optimizing Direct Path Loads on Multiple-CPU Systems"](ldr_modes.md)

### NO\_INDEX\_ERRORS

Default: none

When `NO_INDEX_ERRORS` is specified on the command line, indexes will not be set unusable at any time during the load. If any index errors are detected, then the load is aborted. That is, no rows are loaded and the indexes are left as is.

The `NO_INDEX_ERRORS` parameter is valid only for direct path loads. If specified for conventional path loads, then it is ignored.

### PARALLEL (parallel load)

Default: `false`

`PARALLEL` specifies whether direct loads can operate in multiple concurrent sessions to load data into the same table.

See Also:

["Parallel Data Loading Models"](ldr_modes.md)

### PARFILE (parameter file)

Default: none

`PARFILE` specifies the name of a file that contains commonly used command-line parameters. For example, a parameter file named `daily_report.par` might have the following contents:

```
USERID=scott
CONTROL=daily_report.ctl
ERRORS=9999
LOG=daily_report.log
```

For security reasons, you should not include your `USERID` password in a parameter file. SQL\*Loader will prompt you for the password after you specify the parameter file at the command line, for example:

```
sqlldr PARFILE=daily_report.par
Password: password
```

Note:

Although it is not usually important, on some systems it may be necessary to have no spaces around the equal sign (=) in the parameter specifications.

### READSIZE (read buffer size)

Default: To see the default value for this parameter, invoke SQL\*Loader without any parameters, as described in "Invoking SQL\*Loader".

The `READSIZE` parameter is used only when reading data from data files. When reading records from a control file, a value of 64 kilobytes (KB) is always used as the `READSIZE`.

The `READSIZE` parameter lets you specify (in bytes) the size of the read buffer, if you choose not to use the default. The maximum size allowed is platform dependent.

In the conventional path method, the bind array is limited by the size of the read buffer. Therefore, the advantage of a larger read buffer is that more data can be read before a commit operation is required.

For example, setting `READSIZE` to 1000000 enables SQL\*Loader to perform reads from the external data file in chunks of 1,000,000 bytes before a commit is required.

Note:

If the `READSIZE` value specified is smaller than the `BINDSIZE` value, then the `READSIZE` value will be increased.

The `READSIZE` parameter has no effect on LOBs. The size of the LOB read buffer is fixed at 64 kilobytes (KB).

See "BINDSIZE (maximum size)".

### RESUMABLE

Default: `false`

The `RESUMABLE` parameter is used to enable and disable resumable space allocation. Because this parameter is disabled by default, you must set `RESUMABLE=true` to use its associated parameters, `RESUMABLE_NAME` and `RESUMABLE_TIMEOUT`.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm)
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm)

### RESUMABLE\_NAME

Default: `'User USERNAME (USERID), Session SESSIONID, Instance INSTANCEID'`

The value for this parameter identifies the statement that is resumable. This value is a user-defined text string that is inserted in either the `USER_RESUMABLE` or `DBA_RESUMABLE` view to help you identify a specific resumable statement that has been suspended.

This parameter is ignored unless the `RESUMABLE` parameter is set to `true` to enable resumable space allocation.

### RESUMABLE\_TIMEOUT

Default: `7200` seconds (2 hours)

The value of the parameter specifies the time period during which an error must be fixed. If the error is not fixed within the timeout period, then execution of the statement is terminated, without finishing.

This parameter is ignored unless the `RESUMABLE` parameter is set to `true` to enable resumable space allocation.

### ROWS (rows per commit)

Default: To see the default value for this parameter, invoke SQL\*Loader without any parameters, as described in "Invoking SQL\*Loader".

Keep in mind that if you specify a low value for `ROWS` and then attempt to compress data using table compression, then your compression ratio will probably be degraded. Oracle recommends that you either specify a high value or accept the default value when compressing data.

Conventional path loads only: The `ROWS` parameter specifies the number of rows in the bind array. The maximum number of rows is 65534. See ["Bind Arrays and Conventional Path Loads"](ldr_control_file.md).

Direct path loads only: The `ROWS` parameter identifies the number of rows you want to read from the data file before a data save. The default is to read all rows and save data once at the end of the load. See ["Using Data Saves to Protect Against Data Loss"](ldr_modes.md). The actual number of rows loaded into a table on a save is approximately the value of `ROWS` minus the number of discarded and rejected records since the last save.

Note:

The `ROWS` parameter is ignored for direct path loads when data is loaded into an Index Organized Table (IOT) or into a table containing VARRAYs, XML columns, or LOBs. This means that the load will still take place, but no save points will be done.

### SILENT (feedback mode)

When SQL\*Loader begins, information about the SQL\*Loader version being used appears on the screen and is placed in the log file. As SQL\*Loader executes, you also see feedback messages on the screen, for example:

```
Commit point reached - logical record count 20
```

SQL\*Loader may also display data error messages similar to the following:

```
Record 4: Rejected - Error on table EMP
ORA-00001: unique constraint <name> violated
```

You can suppress these messages by specifying `SILENT` with one or more values.

For example, you can suppress the header and feedback messages that normally appear on the screen with the following command-line argument:

```
SILENT=(HEADER, FEEDBACK)
```

Use the appropriate values to suppress one or more of the following:

- `HEADER` - Suppresses the SQL\*Loader header messages that normally appear on the screen. Header messages still appear in the log file.
- `FEEDBACK` - Suppresses the "commit point reached" feedback messages that normally appear on the screen.
- `ERRORS` - Suppresses the data error messages in the log file that occur when a record generates an Oracle error that causes it to be written to the bad file. A count of rejected records still appears.
- `DISCARDS` - Suppresses the messages in the log file for each record written to the discard file.
- `PARTITIONS` - Disables writing the per-partition statistics to the log file during a direct load of a partitioned table.
- `ALL` - Implements all of the suppression values: `HEADER,` `FEEDBACK,` `ERRORS,` `DISCARDS,` and `PARTITIONS.`

### SKIP (records to skip)

Default: No records are skipped.

`SKIP` specifies the number of logical records from the beginning of the file that should not be loaded.

This parameter continues loads that have been interrupted for some reason. It is used for all conventional loads, for single-table direct loads, and for multiple-table direct loads when the same number of records was loaded into each table. It is not used for multiple-table direct loads when a different number of records was loaded into each table.

If a `WHEN` clause is also present and the load involves secondary data, then the secondary data is skipped only if the `WHEN` clause succeeds for the record in the primary data file.

See Also:

["Interrupted Loads"](ldr_control_file.md)

### SKIP\_INDEX\_MAINTENANCE

Default: `false`

The `SKIP_INDEX_MAINTENANCE` parameter stops index maintenance for direct path loads but does not apply to conventional path loads. It causes the index partitions that would have had index keys added to them to be marked Index Unusable instead, because the index segment is inconsistent with respect to the data it indexes. Index segments that are not affected by the load retain the Index Unusable state they had before the load.

The `SKIP_INDEX_MAINTENANCE` parameter:

- Applies to both local and global indexes
- Can be used (with the `PARALLEL` parameter) to do parallel loads on an object that has indexes
- Can be used (with the `PARTITION` parameter on the `INTO TABLE` clause) to do a single partition load to a table that has global indexes
- Puts a list (in the SQL\*Loader log file) of the indexes and index partitions that the load set into Index Unusable state

### SKIP\_UNUSABLE\_INDEXES

Default: The value of the Oracle database configuration parameter, `SKIP_UNUSABLE_INDEXES`, as specified in the initialization parameter file. The default database setting is `TRUE`.

Both SQL\*Loader and the Oracle database provide a `SKIP_UNUSABLE_INDEXES` parameter. The SQL\*Loader `SKIP_UNUSABLE_INDEXES` parameter is specified at the SQL\*Loader command line. The Oracle database `SKIP_UNUSABLE_INDEXES` parameter is specified as a configuration parameter in the initialization parameter file. It is important to understand how they affect each other.

If you specify a value for `SKIP_UNUSABLE_INDEXES` at the SQL\*Loader command line, then it overrides the value of the `SKIP_UNUSABLE_INDEXES` configuration parameter in the initialization parameter file.

If you do not specify a value for `SKIP_UNUSABLE_INDEXES` at the SQL\*Loader command line, then SQL\*Loader uses the database setting for the `SKIP_UNUSABLE_INDEXES` configuration parameter, as specified in the initialization parameter file. If the initialization parameter file does not specify a database setting for `SKIP_UNUSABLE_INDEXES`, then the default database setting is `TRUE`.

A value of `TRUE` for `SKIP_UNUSABLE_INDEXES` means that if an index in an Index Unusable state is encountered, it is skipped and the load operation continues. This allows SQL\*Loader to load a table with indexes that are in an Unusable state prior to the beginning of the load. Indexes that are not in an Unusable state at load time will be maintained by SQL\*Loader. Indexes that are in an Unusable state at load time will not be maintained but will remain in an Unusable state at load completion.

Note:

Indexes that are unique and marked Unusable are not allowed to skip index maintenance. This rule is enforced by DML operations, and enforced by the direct path load to be consistent with DML.

The `SKIP_UNUSABLE_INDEXES` parameter applies to both conventional and direct path loads.

### STREAMSIZE

Default: To see the default value for this parameter, invoke SQL\*Loader without any parameters, as described in "Invoking SQL\*Loader".

Specifies the size, in bytes, for direct path streams.

See Also:

["Specifying the Number of Column Array Rows and Size of Stream Buffers"](ldr_modes.md)

### USERID (username/password)

Default: none

`USERID` is used to provide your Oracle username and password. If it is omitted, then you are prompted for it. If only a slash is used, then `USERID` defaults to your operating system login.

If you connect as user `SYS`, then you must also specify `AS SYSDBA` in the connect string.

Note:

Because the string, `AS SYSDBA,` contains a blank, some operating systems may require that the entire connect string be placed in quotation marks or marked as a literal by some method. Some operating systems also require that quotation marks on the command line be preceded by an escape character, such as backslashes.

See your Oracle operating system-specific documentation for information about special and reserved characters on your system.

## Exit Codes for Inspection and Display

Oracle SQL\*Loader provides the results of a SQL\*Loader run immediately upon completion. In addition to recording the results in a log file, SQL\*Loader may also report the outcome in a process exit code. This Oracle SQL\*Loader functionality allows for checking the outcome of a SQL\*Loader invocation from the command line or a script. Table 8-1 shows the exit codes for various results.

Table 8-1 Exit Codes for SQL\*Loader

| Result | Exit Code |
| --- | --- |
| All rows loaded successfully | `EX_SUCC` |
| All or some rows rejected | `EX_WARN` |
| All or some rows discarded | `EX_WARN` |
| Discontinued load | `EX_WARN` |
| Command-line or syntax errors | `EX_FAIL` |
| Oracle errors nonrecoverable for SQL\*Loader | `EX_FAIL` |
| Operating system errors (such as file open/close and malloc) | `EX_FTL` |

For UNIX, the exit codes are as follows:

```
EX_SUCC 0
EX_FAIL 1
EX_WARN 2
EX_FTL  3
```

For Windows NT, the exit codes are as follows:

```
EX_SUCC 0
EX_FAIL 1
EX_WARN 2
EX_FTL  4
```

If SQL\*Loader returns any exit code other than zero, then you should consult your system log files and SQL\*Loader log files for more detailed diagnostic information.

In UNIX, you can check the exit code from the shell to determine the outcome of a load.