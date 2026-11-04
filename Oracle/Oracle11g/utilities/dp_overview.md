---
title: Overview of Oracle Data Pump
book: Utilities
doc_id: E22490-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_overview.htm
tags:
  - oracle
  - 11g
  - utilities
---

## 1 Overview of Oracle Data Pump

Oracle Data Pump technology enables very high-speed movement of data and metadata from one database to another.

This chapter discusses the following topics:

## Data Pump Components

Oracle Data Pump is made up of three distinct parts:

- The command-line clients, `expdp` and `impdp`
- The `DBMS_DATAPUMP` PL/SQL package (also known as the Data Pump API)
- The `DBMS_METADATA` PL/SQL package (also known as the Metadata API)

The Data Pump clients, `expdp` and `impdp`, invoke the Data Pump Export utility and Data Pump Import utility, respectively.

The `expdp` and `impdp` clients use the procedures provided in the `DBMS_DATAPUMP` PL/SQL package to execute export and import commands, using the parameters entered at the command line. These parameters enable the exporting and importing of data and metadata for a complete database or for subsets of a database.

When metadata is moved, Data Pump uses functionality provided by the `DBMS_METADATA` PL/SQL package. The `DBMS_METADATA` package provides a centralized facility for the extraction, manipulation, and re-creation of dictionary metadata.

The `DBMS_DATAPUMP` and `DBMS_METADATA` PL/SQL packages can be used independently of the Data Pump clients.

Note:

All Data Pump Export and Import processing, including the reading and writing of dump files, is done on the system (server) selected by the specified database connect string. This means that for unprivileged users, the database administrator (DBA) must create directory objects for the Data Pump files that are read and written on that server file system. (For security reasons, DBAs must ensure that only approved users are allowed access to directory objects.) For privileged users, a default directory object is available. See "Default Locations for Dump, Log, and SQL Files" for more information about directory objects.

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for descriptions of the `DBMS_DATAPUMP` and `DBMS_METADATA` packages
- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/adlob_bfile_ops.htm#ADLOB45842) for information about guidelines to consider when creating directory objects

## How Does Data Pump Move Data?

For information about how Data Pump moves data in and out of databases, see the following sections:

- Using Data File Copying to Move Data
- Using Direct Path to Move Data
- Using External Tables to Move Data
- Using Conventional Path to Move Data
- Using Network Link Import to Move Data

Note:

Data Pump does not load tables with disabled unique indexes. To load data into the table, the indexes must be either dropped or reenabled.

The following sections briefly explain how and when each of these data movement mechanisms is used.

### Using Data File Copying to Move Data

The fastest method of moving data is to copy the database data files to the target database without interpreting or altering the data. With this method, Data Pump Export is used to unload only structural information (metadata) into the dump file. This method is used in the following situations:

- The `TRANSPORT_TABLESPACES` parameter is used to specify a transportable mode export. Only metadata for the specified tablespaces is exported.
- The `TRANSPORTABLE=ALWAYS` parameter is supplied on a table mode export (specified with the `TABLES` parameter). Only metadata for the tables, partitions, and subpartitions specified on the `TABLES` parameter is exported.

When an export operation uses data file copying, the corresponding import job always also uses data file copying. During the ensuing import operation, both the data files and the export dump file must be loaded.

When data is moved by using data file copying, the character sets must be identical on both the source and target databases.

In addition to copying the data, you may need to prepare it by using the Recovery Manager (RMAN) `CONVERT` command to perform some data conversions. You can do this at either the source or target database.

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta012.htm#RCMRF192) for information about the RMAN `CONVERT` command
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tspaces.htm#ADMIN10140) for a description and example (including how to convert the data) of transporting tablespaces between databases

### Using Direct Path to Move Data

After data file copying, direct path is the fastest method of moving data. In this method, the SQL layer of the database is bypassed and rows are moved to and from the dump file with only minimal interpretation. Data Pump automatically uses the direct path method for loading and unloading data when the structure of a table allows it. For example, if a table contains a column of type `BFILE`, then direct path cannot be used to load that table and external tables is used instead.

The following sections describe situations in which direct path cannot be used for loading and unloading:

- Situations in Which Direct Path Load Is Not Used
- Situations in Which Direct Path Unload Is Not Used

Situations in Which Direct Path Load Is Not Used

If any of the following conditions exist for a table, then Data Pump uses external tables rather than direct path to load the data for that table:

- A global index on multipartition tables exists during a single-partition load. This includes object tables that are partitioned.
- A domain index exists for a LOB column.
- A table is in a cluster.
- There is an active trigger on a preexisting table.
- Fine-grained access control is enabled in insert mode on a preexisting table.
- A table contains `BFILE` columns or columns of opaque types.
- A referential integrity constraint is present on a preexisting table.
- A table contains `VARRAY` columns with an embedded opaque type.
- The table has encrypted columns.
- The table into which data is being imported is a preexisting table and at least one of the following conditions exists:
	- There is an active trigger
		- The table is partitioned
		- Fine-grained access control is in insert mode
		- A referential integrity constraint exists
		- A unique index exists
- Supplemental logging is enabled and the table has at least one LOB column.
- The Data Pump command for the specified table used the `QUERY`, `SAMPLE`, or `REMAP_DATA` parameter.
- A table contains a column (including a `VARRAY` column) with a `TIMESTAMP WITH TIME ZONE` datatype and the version of the time zone data file is different between the export and import systems.

Situations in Which Direct Path Unload Is Not Used

If any of the following conditions exist for a table, then Data Pump uses the external table method to unload data, rather than the direct path method:

- Fine-grained access control for `SELECT` is enabled.
- The table is a queue table.
- The table contains one or more columns of type `BFILE` or opaque, or an object type containing opaque columns.
- The table contains encrypted columns.
- The table contains a column of an evolved type that needs upgrading.
- The table contains a column of type `LONG` or `LONG RAW` that is not last.
- The Data Pump command for the specified table used the `QUERY`, `SAMPLE`, or `REMAP_DATA` parameter.

### Using External Tables to Move Data

When data file copying is not selected and the data cannot be moved using direct path, the external table mechanism is used. The external table mechanism creates an external table that maps to the dump file data for the database table. The SQL engine is then used to move the data. If possible, the `APPEND` hint is used on import to speed the copying of the data into the database. The representation of data for direct path data and external table data is the same in a dump file. Therefore, Data Pump might use the direct path mechanism at export time, but use external tables when the data is imported into the target database. Similarly, Data Pump might use external tables for the export, but use direct path for the import.

In particular, Data Pump uses external tables in the following situations:

- Loading and unloading very large tables and partitions in situations where it is advantageous to use parallel SQL capabilities
- Loading tables with global or domain indexes defined on them, including partitioned object tables
- Loading tables with active triggers or clustered tables
- Loading and unloading tables with encrypted columns
- Loading tables with fine-grained access control enabled for inserts
- Loading tables that are partitioned differently at load time and unload time
- Loading a table not created by the import operation (the table exists before the import starts)

Note:

When Data Pump uses external tables as the data access mechanism, it uses the `ORACLE_DATAPUMP` access driver. However, it is important to understand that the files that Data Pump creates when it uses external tables are not compatible with files created when you manually create an external table using the SQL `CREATE TABLE ... ORGANIZATION EXTERNAL` statement.

See Also:

- [Chapter 15, "The ORACLE\_DATAPUMP Access Driver"](et_dp_driver.md)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for information about using the `APPEND` hint

### Using Conventional Path to Move Data

In situations where there are conflicting table attributes, Data Pump is not able to load data into a table using either direct path or external tables. In such cases, conventional path is used, which can affect performance.

### Using Network Link Import to Move Data

When the Import `NETWORK_LINK` parameter is used to specify a network link for an import operation, SQL is directly used to move the data using an `INSERT SELECT` statement. The `SELECT` clause retrieves the data from the remote database over the network link. The `INSERT` clause uses SQL to insert the data into the target database. There are no dump files involved.

When the Export `NETWORK_LINK` parameter is used to specify a network link for an export operation, the data from the remote database is written to dump files on the target database. (Note that to export from a read-only database, the `NETWORK_LINK` parameter is required.)

Because the link can identify a remotely networked database, the terms database link and network link are used interchangeably.

Because reading over a network is generally slower than reading from a disk, network link is the slowest of the four access methods used by Data Pump and may be undesirable for very large jobs.

Supported Link Types

The following types of database links are supported for use with Data Pump Export and Import:

- Public (both public and shared)
- Fixed user
- Connected user

Unsupported Link Types

The database link type, Current User, is not supported for use with Data Pump Export or Import.

See Also:

- The Export [NETWORK\_LINK](dp_export.md) parameter for information about performing exports over a database link
- The Import [NETWORK\_LINK](dp_import.md) parameter for information about performing imports over a database link
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for information about database links

## Required Roles for Data Pump Export and Import Operations

Many Data Pump Export and Import operations require the user to have the `DATAPUMP_EXP_FULL_DATABASE` role and/or the `DATAPUMP_IMP_FULL_DATABASE` role. These roles are automatically defined for Oracle databases when you run the standard scripts that are part of database creation. (Note that although the names of these roles contain the word FULL, these roles are actually required for all export and import modes, not only Full mode.)

The `DATAPUMP_EXP_FULL_DATABASE` role affects only export operations. The `DATAPUMP_IMP_FULL_DATABASE` role affects import operations and operations that use the Import `SQLFILE` parameter. These roles allow users performing exports and imports to do the following:

- Perform the operation outside the scope of their schema
- Monitor jobs that were initiated by another user
- Export objects (such as tablespace definitions) and import objects (such as directory definitions) that unprivileged users cannot reference

These are powerful roles. Database administrators should use caution when granting these roles to users.

Although the `SYS` schema does not have either of these roles assigned to it, all security checks performed by Data Pump that require these roles also grant access to the `SYS` schema.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authorization.htm#DBSEG4414) for more information about predefined roles in an Oracle Database installation

## What Happens During Execution of a Data Pump Job?

Data Pump jobs use a master table, a master process, and worker processes to perform the work and keep track of progress.

### Coordination of a Job

For every Data Pump Export job and Data Pump Import job, a master process is created. The master process controls the entire job, including communicating with the clients, creating and controlling a pool of worker processes, and performing logging operations.

### Tracking Progress Within a Job

While the data and metadata are being transferred, a master table is used to track the progress within a job. The master table is implemented as a user table within the database. The specific function of the master table for export and import jobs is as follows:

- For export jobs, the master table records the location of database objects within a dump file set. Export builds and maintains the master table for the duration of the job. At the end of an export job, the content of the master table is written to a file in the dump file set.
- For import jobs, the master table is loaded from the dump file set and is used to control the sequence of operations for locating objects that need to be imported into the target database.

The master table is created in the schema of the current user performing the export or import operation. Therefore, that user must have the `CREATE TABLE` system privilege and a sufficient tablespace quota for creation of the master table. The name of the master table is the same as the name of the job that created it. Therefore, you cannot explicitly give a Data Pump job the same name as a preexisting table or view.

For all operations, the information in the master table is used to restart a job.

The master table is either retained or dropped, depending on the circumstances, as follows:

- Upon successful job completion, the master table is dropped.
- If a job is stopped using the `STOP_JOB` interactive command, then the master table is retained for use in restarting the job.
- If a job is killed using the `KILL_JOB` interactive command, then the master table is dropped and the job cannot be restarted.
- If a job terminates unexpectedly, then the master table is retained. You can delete it if you do not intend to restart the job.
- If a job stops before it starts running (that is, before any database objects have been copied), then the master table is dropped.

See Also:

["JOB\_NAME"](dp_export.md) for more information about how job names are formed

### Filtering Data and Metadata During a Job

Within the master table, specific objects are assigned attributes such as name or owning schema. Objects also belong to a class of objects (such as `TABLE`, `INDEX,` or `DIRECTORY`). The class of an object is called its object type. You can use the `EXCLUDE` and `INCLUDE` parameters to restrict the types of objects that are exported and imported. The objects can be based upon the name of the object or the name of the schema that owns the object. You can also specify data-specific filters to restrict the rows that are exported and imported.

See Also:

- ["Filtering During Export Operations"](dp_export.md)
- ["Filtering During Import Operations"](dp_import.md)

### Transforming Metadata During a Job

When you are moving data from one database to another, it is often useful to perform transformations on the metadata for remapping storage between tablespaces or redefining the owner of a particular set of objects. This is done using the following Data Pump Import parameters: `REMAP_DATAFILE`, `REMAP_SCHEMA`, `REMAP_TABLE,REMAP_TABLESPACE`, `TRANSFORM,` and `PARTITION_OPTIONS`.

### Maximizing Job Performance

Data Pump can employ multiple worker processes, running in parallel, to increase job performance. Use the `PARALLEL` parameter to set a degree of parallelism that takes maximum advantage of current conditions. For example, to limit the effect of a job on a production system, the database administrator (DBA) might want to restrict the parallelism. The degree of parallelism can be reset at any time during a job. For example, `PARALLEL` could be set to 2 during production hours to restrict a particular job to only two degrees of parallelism, and during nonproduction hours it could be reset to 8. The parallelism setting is enforced by the master process, which allocates work to be executed to worker processes that perform the data and metadata processing within an operation. These worker processes operate in parallel. In general, the degree of parallelism should be set to no more than twice the number of CPUs on an instance.

Note:

The ability to adjust the degree of parallelism is available only in the Enterprise Edition of Oracle Database.

### Loading and Unloading of Data

The worker processes unload and load metadata and table data. During import they also rebuild indexes. Some of these operations may be done in parallel: unloading and loading table data, rebuilding indexes, and loading package bodies. Worker processes are created as needed until the number of worker processes equals the value supplied for the `PARALLEL` command-line parameter. The number of active worker processes can be reset throughout the life of a job. Worker processes can be started on different nodes in an Oracle Real Application Clusters (Oracle RAC) environment.

Note:

The value of `PARALLEL` is restricted to 1 in the Standard Edition of Oracle Database.

When a worker process is assigned the task of loading or unloading a very large table or partition, it may choose to use the external tables access method to make maximum use of parallel execution. In such a case, the worker process becomes a parallel execution coordinator. The actual loading and unloading work is divided among some number of parallel I/O execution processes (sometimes called slaves) allocated from a pool of available processes in an Oracle RAC environment.

See Also:

- The Export [PARALLEL](dp_export.md) parameter
- The Import [PARALLEL](dp_import.md) parameter

## Monitoring Job Status

The Data Pump Export and Import utilities can attach to a job in either logging mode or interactive-command mode.

In logging mode, real-time detailed status about the job is automatically displayed during job execution. The information displayed can include the job and parameter descriptions, an estimate of the amount of data to be exported, a description of the current operation or item being processed, files used during the job, any errors encountered, and the final job state (Stopped or Completed).

See Also:

- The Export [STATUS](dp_export.md) parameter for information about changing the frequency of the status display in command-line Export
- The Import [STATUS](dp_import.md) parameter for information about changing the frequency of the status display in command-line Import

In interactive-command mode, job status can be displayed on request. The information displayed can include the job description and state, a description of the current operation or item being processed, files being written, and a cumulative status.

See Also:

- The interactive Export [STATUS](dp_export.md) command
- The interactive Import [STATUS](dp_import.md) command

A log file can also be optionally written during the execution of a job. The log file summarizes the progress of the job, lists any errors that were encountered during execution of the job, and records the completion status of the job.

See Also:

- The Export [LOGFILE](dp_export.md) parameter for information on how to set the file specification for an export log file
- The Import [LOGFILE](dp_import.md) parameter for information on how to set the file specification for a import log file

An alternative way to determine job status or to get other information about Data Pump jobs, would be to query the `DBA_DATAPUMP_JOBS`, `USER_DATAPUMP_JOBS`, or `DBA_DATAPUMP_SESSIONS` views. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for descriptions of these views.

### Monitoring the Progress of Executing Jobs

Data Pump operations that transfer table data (export and import) maintain an entry in the `V$SESSION_LONGOPS` dynamic performance view indicating the job progress (in megabytes of table data transferred). The entry contains the estimated transfer size and is periodically updated to reflect the actual amount of data transferred.

Use of the `COMPRESSION`, `ENCRYPTION`, `ENCRYPTION_ALGORITHM`, `ENCRYPTION_MODE`, `ENCRYPTION_PASSWORD`, `QUERY`, and `REMAP_DATA` parameters are not reflected in the determination of estimate values.

The usefulness of the estimate value for export operations depends on the type of estimation requested when the operation was initiated, and it is updated as required if exceeded by the actual transfer amount. The estimate value for import operations is exact.

The `V$SESSION_LONGOPS` columns that are relevant to a Data Pump job are as follows:

- `USERNAME` - job owner
- `OPNAME` - job name
- `TARGET_DESC` - job operation
- `SOFAR` - megabytes transferred thus far during the job
- `TOTALWORK` - estimated number of megabytes in the job
- `UNITS` - megabytes (MB)
- `MESSAGE` - a formatted status message of the form:
	```
	'job_name: operation_name : nnn out of mmm MB done'
	```

## File Allocation

Data Pump jobs manage the following types of files:

- Dump files to contain the data and metadata that is being moved.
- Log files to record the messages associated with an operation.
- SQL files to record the output of a SQLFILE operation. A SQLFILE operation is invoked using the Data Pump Import `SQLFILE` parameter and results in all the SQL DDL that Import would be executing based on other parameters, being written to a SQL file.
- Files specified by the `DATA_FILES` parameter during a transportable import.

An understanding of how Data Pump allocates and handles these files will help you to use Export and Import to their fullest advantage.

### Specifying Files and Adding Additional Dump Files

For export operations, you can specify dump files at the time the job is defined, and also at a later time during the operation. For example, if you discover that space is running low during an export operation, then you can add additional dump files by using the Data Pump Export `ADD_FILE` command in interactive mode.

For import operations, all dump files must be specified at the time the job is defined.

Log files and SQL files overwrite previously existing files. For dump files, you can use the Export `REUSE_DUMPFILES` parameter to specify whether to overwrite a preexisting dump file.

### Default Locations for Dump, Log, and SQL Files

Because Data Pump is server-based rather than client-based, dump files, log files, and SQL files are accessed relative to server-based directory paths. Data Pump requires that directory paths be specified as directory objects. A directory object maps a name to a directory path on the file system. DBAs must ensure that only approved users are allowed access to the directory object associated with the directory path.

The following example shows a SQL statement that creates a directory object named `dpump_dir1` that is mapped to a directory located at `/usr/apps/datafiles.`

```
SQL> CREATE DIRECTORY dpump_dir1 AS '/usr/apps/datafiles';
```

The reason that a directory object is required is to ensure data security and integrity. For example:

- If you were allowed to specify a directory path location for an input file, then you might be able to read data that the server has access to, but to which you should not.
- If you were allowed to specify a directory path location for an output file, then the server might overwrite a file that you might not normally have privileges to delete.

On UNIX and Windows NT systems, a default directory object, `DATA_PUMP_DIR`, is created at database creation or whenever the database dictionary is upgraded. By default, it is available only to privileged users. (The user `SYSTEM` has read and write access to the `DATA_PUMP_DIR` directory, by default.)

If you are not a privileged user, then before you can run Data Pump Export or Data Pump Import, a directory object must be created by a database administrator (DBA) or by any user with the `CREATE` `ANY` `DIRECTORY` privilege.

After a directory is created, the user creating the directory object must grant `READ` or `WRITE` permission on the directory to other users. For example, to allow the Oracle database to read and write files on behalf of user `hr` in the directory named by `dpump_dir1`, the DBA must execute the following command:

```
SQL> GRANT READ, WRITE ON DIRECTORY dpump_dir1 TO hr;
```

Note that `READ` or `WRITE` permission to a directory object only means that the Oracle database reads or writes that file on your behalf. You are not given direct access to those files outside of the Oracle database unless you have the appropriate operating system privileges. Similarly, the Oracle database requires permission from the operating system to read and write files in the directories.

Data Pump Export and Import use the following order of precedence to determine a file's location:

1. If a directory object is specified as part of the file specification, then the location specified by that directory object is used. (The directory object must be separated from the file name by a colon.)
2. If a directory object is not specified as part of the file specification, then the directory object named by the `DIRECTORY` parameter is used.
3. If a directory object is not specified as part of the file specification, and if no directory object is named by the `DIRECTORY` parameter, then the value of the environment variable, `DATA_PUMP_DIR`, is used. This environment variable is defined using operating system commands on the client system where the Data Pump Export and Import utilities are run. The value assigned to this client-based environment variable must be the name of a server-based directory object, which must first be created on the server system by a DBA. For example, the following SQL statement creates a directory object on the server system. The name of the directory object is `DUMP_FILES1`, and it is located at `'/usr/apps/dumpfiles1'`.
	```
	SQL> CREATE DIRECTORY DUMP_FILES1 AS '/usr/apps/dumpfiles1';
	```
	Then, a user on a UNIX-based client system using `csh` can assign the value `DUMP_FILES1` to the environment variable `DATA_PUMP_DIR`. The `DIRECTORY` parameter can then be omitted from the command line. The dump file `employees.dmp`, and the log file `export.log`, are written to `'/usr/apps/dumpfiles1'`.
	```
	%setenv DATA_PUMP_DIR DUMP_FILES1
	%expdp hr TABLES=employees DUMPFILE=employees.dmp
	```
4. If none of the previous three conditions yields a directory object and you are a privileged user, then Data Pump attempts to use the value of the default server-based directory object, `DATA_PUMP_DIR`. This directory object is automatically created at database creation or when the database dictionary is upgraded. You can use the following SQL query to see the path definition for `DATA_PUMP_DIR`:
	```
	SQL> SELECT directory_name, directory_path FROM dba_directories
	2 WHERE directory_name='DATA_PUMP_DIR';
	```
	If you are not a privileged user, then access to the `DATA_PUMP_DIR` directory object must have previously been granted to you by a DBA.
	Do not confuse the default `DATA_PUMP_DIR` directory object with the client-based environment variable of the same name.

#### Oracle RAC Considerations

Keep the following considerations in mind when working in an Oracle RAC environment.

- To use Data Pump or external tables in an Oracle RAC configuration, you must ensure that the directory object path is on a cluster-wide file system.
	The directory object must point to shared physical storage that is visible to, and accessible from, all instances where Data Pump and/or external tables processes may run.
- The default Data Pump behavior is that worker processes can run on any instance in an Oracle RAC configuration. Therefore, workers on those Oracle RAC instances must have physical access to the location defined by the directory object, such as shared storage media. If the configuration does not have shared storage for this purpose, but you still require parallelism, then you can use the `CLUSTER=no` parameter to constrain all worker processes to the instance where the Data Pump job was started.
- Under certain circumstances, Data Pump uses parallel query slaves to load or unload data. In an Oracle RAC environment, Data Pump does not control where these slaves run, and they may run on other instances in the Oracle RAC, regardless of what is specified for `CLUSTER` and `SERVICE_NAME` for the Data Pump job. Controls for parallel query operations are independent of Data Pump. When parallel query slaves run on other instances as part of a Data Pump job, they also require access to the physical storage of the dump file set.

#### Using Directory Objects When Oracle Automatic Storage Management Is Enabled

If you use Data Pump Export or Import with Oracle Automatic Storage Management (Oracle ASM) enabled, then you must define the directory object used for the dump file so that the Oracle ASM disk group name is used (instead of an operating system directory path). A separate directory object, which points to an operating system directory path, should be used for the log file. For example, you would create a directory object for the Oracle ASM dump file as follows:

```
SQL> CREATE or REPLACE DIRECTORY dpump_dir as '+DATAFILES/';
```

Then you would create a separate directory object for the log file:

```
SQL> CREATE or REPLACE DIRECTORY dpump_log as '/homedir/user1/';
```

To enable user `hr` to have access to these directory objects, you would assign the necessary privileges, for example:

```
SQL> GRANT READ, WRITE ON DIRECTORY dpump_dir TO hr;
SQL> GRANT READ, WRITE ON DIRECTORY dpump_log TO hr;
```

You would then use the following Data Pump Export command (you will be prompted for a password):

```
> expdp hr DIRECTORY=dpump_dir DUMPFILE=hr.dmp LOGFILE=dpump_log:hr.log
```

See Also:

- The Export [DIRECTORY](dp_export.md) parameter
- The Import [DIRECTORY](dp_import.md) parameter
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for information about the `CREATE` `DIRECTORY` command
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for more information about Oracle ASM

### Using Substitution Variables

Instead of, or in addition to, listing specific file names, you can use the `DUMPFILE` parameter during export operations to specify multiple dump files, by using a substitution variable (`%U`) in the file name. This is called a dump file template. The new dump files are created as they are needed, beginning with `01` for `%U`, then using `02`, `03`, and so on. Enough dump files are created to allow all processes specified by the current setting of the `PARALLEL` parameter to be active. If one of the dump files becomes full because its size has reached the maximum size specified by the `FILESIZE` parameter, then it is closed and a new dump file (with a new generated name) is created to take its place.

If multiple dump file templates are provided, they are used to generate dump files in a round-robin fashion. For example, if `expa%U`, `expb%U,` and `expc%U` were all specified for a job having a parallelism of 6, then the initial dump files created would be `expa01`.`dmp`, `expb01`.`dmp`, `expc01`.`dmp`, `expa02`.`dmp`, `expb02`.`dmp`, and `expc02`.`dmp`.

For import and SQLFILE operations, if dump file specifications `expa%U`, `expb%U,` and `expc%U` are specified, then the operation begins by attempting to open the dump files `expa01`.`dmp`, `expb01`.`dmp`, and `expc01`.`dmp`. It is possible for the master table to span multiple dump files, so until all pieces of the master table are found, dump files continue to be opened by incrementing the substitution variable and looking up the new file names (for example, `expa02`.`dmp`, `expb02`.`dmp`, and `expc02`.`dmp`). If a dump file does not exist, then the operation stops incrementing the substitution variable for the dump file specification that was in error. For example, if `expb01`.`dmp` and `expb02`.`dmp` are found but `expb03`.`dmp` is not found, then no more files are searched for using the `expb%U` specification. Once the entire master table is found, it is used to determine whether all dump files in the dump file set have been located.

## Moving Data Between Different Database Releases

Because most Data Pump operations are performed on the server side, if you are using any release of the database other than `COMPATIBLE`, then you must provide the server with the specific release information. Otherwise, errors may occur. To specify release information, use the `VERSION` parameter.

See Also:

- The Export [VERSION](dp_export.md) parameter
- The Import [VERSION](dp_import.md) parameter

Keep the following information in mind when you are using Data Pump Export and Import to move data between different database releases:

- If you specify a database release that is older than the current database release, then certain features may be unavailable. For example, specifying `VERSION=10.1` causes an error if data compression is also specified for the job because compression was not supported in Oracle Database 10g release 1 (10.1).
- On a Data Pump export, if you specify a database release that is older than the current database release, then a dump file set is created that you can import into that older release of the database. However, the dump file set does not contain any objects that the older database release does not support.
- Data Pump Import can always read dump file sets created by older releases of the database.
- Data Pump Import cannot read dump file sets created by a database release that is newer than the current database release, unless those dump file sets were created with the `VERSION` parameter set to the release of the target database. Therefore, the best way to perform a downgrade is to perform your Data Pump export with the `VERSION` parameter set to the release of the target database.
- When operating across a network link, Data Pump requires that the source and target databases differ by no more than one version. For example, if one database is Oracle Database 11g, then the other database must be either 11g or 10g. Note that Data Pump checks only the major version number (for example, 10g and 11g), not specific release numbers (for example, 10.1, 10.2, 11.1, or 11.2).

## SecureFiles LOB Considerations

When you use Data Pump Export to export SecureFiles LOBs, the resulting behavior depends on several things, including the value of the Export `VERSION` parameter, whether ContentType is present, and whether the LOB is archived and data is cached. The following scenarios cover different combinations of these variables:

- If a table contains SecureFiles LOBs with ContentType and the Export `VERSION` parameter is set to a value earlier than `11.2.0.0.0`, then the ContentType is not exported.
- If a table contains SecureFiles LOBs with ContentType and the Export `VERSION` parameter is set to a value of `11.2.0.0.0` or later, then the ContentType is exported and restored on a subsequent import.
- If a table contains a SecureFiles LOB that is currently archived and the data is cached, and the Export `VERSION` parameter is set to a value earlier than `11.2.0.0.0`, then the SecureFiles LOB data is exported and the archive metadata is dropped. In this scenario, if `VERSION` is set to `11.1` or later, then the SecureFiles LOB becomes a vanilla SecureFiles LOB. But if `VERSION` is set to a value earlier than `11.1`, then the SecureFiles LOB becomes a BasicFiles LOB.
- If a table contains a SecureFiles LOB that is currently archived but the data is not cached, and the Export `VERSION` parameter is set to a value earlier than `11.2.0.0.0`, then an ORA-45001 error is returned.
- If a table contains a SecureFiles LOB that is currently archived and the data is cached, and the Export `VERSION` parameter is set to a value of `11.2.0.0.0` or later, then both the cached data and the archive metadata is exported.

See Also:

[Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/adlob_smart.htm#ADLOB4444) for more information about SecureFiles

## Data Pump Exit Codes

Oracle Data Pump provides the results of export and import operations immediately upon completion. In addition to recording the results in a log file, Data Pump may also report the outcome in a process exit code. This allows you to check the outcome of a Data Pump job from the command line or a script.

Table 1-1 describes the Data Pump exit codes for Unix and Windows NT.

Table 1-1 Data Pump Exit Codes

| Exit Code | Meaning |
| --- | --- |
| `EX_SUCC 0` | The export or import job completed successfully. No errors are displayed to the output device or recorded in the log file, if there is one. |
| `EX_SUCC_ERR 5` | The export or import job completed successfully but there were errors encountered during the job. The errors are displayed to the output device and recorded in the log file, if there is one. |
| `EX_FAIL 1` | The export or import job encountered one or more fatal errors, including the following:  - Errors on the command line or in command syntax - Oracle database errors from which export or import cannot recover - Operating system errors (such as malloc) - Invalid parameter values that prevent the job from starting (for example, an invalid directory object specified in the `DIRECTORY` parameter)  A fatal error is displayed to the output device but may not be recorded in the log file. Whether it is recorded in the log file can depend on several factors, including:  - Was a log file specified at the start of the job? - Did the processing of the job proceed far enough for a log file to be opened? |