---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/RECOVER.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
RECOVER {general | managed | BEGIN BACKUP | END BACKUP}
```

where the general clause has the following syntax:

```
[AUTOMATIC] [FROM location]
{ {full_database_recovery  | partial_database_recovery  | LOGFILE filename}
[ {TEST | ALLOW integer CORRUPTION | parallel_clause }  [TEST 
| ALLOW integer CORRUPTION | parallel_clause  ]...]| CONTINUE [DEFAULT] | CANCEL}
```

where the full\_database\_recovery clause has the following syntax:

```
[STANDBY] DATABASE
 [ {UNTIL {CANCEL | TIME date | CHANGE integer} | USING BACKUP CONTROLFILE 
 | SNAPSHOT TIME date}...]
```

where the partial\_database\_recovery clause has the following syntax:

```
{TABLESPACE tablespace [, tablespace]...  
  | DATAFILE {filename | filenumber} [, filename | filenumber]...
  | STANDBY {TABLESPACE tablespace [, tablespace]...
  | DATAFILE {filename | filenumber} [, filename | filenumber]...}
    UNTIL [CONSISTENT WITH] CONTROLFILE }
```

where the parallel clause has the following syntax:

```
{ NOPARALLEL | PARALLEL [ integer ] }
```

where the managed clause has the following syntax:

```
MANAGED STANDBY DATABASE recover_clause | cancel_clause | finish_clause
```
```
where the recover_clause has the following syntax:
```
```
{ { DISCONNECT [ FROM SESSION ]  | { TIMEOUT integer | NOTIMEOUT }  }
  | { NODELAY | DEFAULT DELAY | DELAY integer } 
  | NEXT integer  | { EXPIRE integer | NO EXPIRE } 
  | parallel_clause | USING CURRENT LOGFILE | UNTIL CHANGE integer
  | THROUGH { [ THREAD integer ] SEQUENCE integer
  | ALL ARCHIVELOG  | { ALL | LAST | NEXT } SWITCHOVER}} ...
```

where the cancel\_clause has the following syntax:

```
CANCEL [IMMEDIATE] [WAIT | NOWAIT]
```

where the finish\_clause has the following syntax:

```
[ DISCONNECT [ FROM SESSION ] ] [ parallel_clause ]
FINISH [ SKIP [ STANDBY LOGFILE ] ] [ WAIT | NOWAIT ]
```

where the parallel\_clause has the following syntax:

```
{ NOPARALLEL | PARALLEL [ integer ] }
```

Performs media recovery on one or more tablespaces, one or more datafiles, or the entire database. For more information on the RECOVER command, see the [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN), the ALTER DATABASE RECOVER command in the [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=SQLRF), and the [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=BRADV) guide.

Terms

```
AUTOMATIC
```

Automatically generates the name of the next archived redo log file needed to continue the recovery operation. Oracle Database uses the LOG\_ARCHIVE\_DEST (or LOG\_ARCHIVE\_DEST\_ 1) and LOG\_ARCHIVE\_FORMAT parameters (or their defaults) to generate the target redo log filename. If the file is found, the redo contained in that file is applied. If the file is not found, SQL\*Plus prompts you for a filename, displaying a generated filename as a suggestion.

If you do not specify either AUTOMATIC or LOGFILE, SQL\*Plus prompts you for a filename, suggesting the generated filename. You can either accept the generated filename or replace it with a fully qualified filename. You can save time by using the LOGFILE clause to specify the filename if you know the archived filename differs from the filename Oracle Database would generate.

```
FROM location
```

Specifies the location from which the archived redo log file group is read. The value of location must be a fully specified file location. If you omit this parameter, SQL\*Plus assumes the archived redo log file group is in the location specified by the initialization parameter LOG\_ARCHIVE\_DEST or LOG\_ARCHIVE\_DEST\_1. Do not specify FROM if you have set a file with SET LOGSOURCE.

```
full_database_recovery
```

Enables you to specify the recovery of a full database.

```
partial_database_recovery
```

Enables you to specify the recovery of individual tablespaces and datafiles.

```
LOGFILE
```

Continues media recovery by applying the specified redo log file. In interactive recovery mode (AUTORECOVERY OFF), if a bad log name is entered, errors for the bad log name are displayed and you are prompted to enter a new log name.

```
TEST
```

Specifies a trial recovery to detect possible problems. Redo is applied normally, but no changes are written to disk, and changes are rolled back at the end of the trial recovery. You can only use the TEST clause for a trial recovery if you have restored a backup. In the event of logfile corruption, specifies the number of corrupt blocks that can be tolerated while allowing recovery to proceed. During normal recovery, integer cannot exceed 1.

```
ALLOW integer CORRUPTION
```

In the event of logfile corruption, specifies the number of corrupt blocks that can be tolerated while allowing recovery to proceed.

```
parallel _clause
```

Enables you to specify the degree of parallel processing to use during the recovery operation.

```
CONTINUE
```

Continues multi-instance recovery after it has been interrupted to disable a thread.

```
CONTINUE DEFAULT
```

Continues recovery using the redo log file generated automatically by Oracle Database if no other logfile is specified. This is equivalent to specifying AUTOMATIC, except that Oracle Database does not prompt for a filename.

```
CANCEL
```

Terminates cancel-based recovery.

```
SNAPSHOT TIME date
```

Recovers the database with a storage snapshot using Storage snapshot Optimization.

```
STANDBY DATABASE
```

Recovers the standby database using the control file and archived redo log files copied from the primary database. The standby database must be mounted but not open.

```
DATABASE
```

Recovers the entire database.

```
UNTIL CANCEL
```

Specifies an incomplete, cancel-based recovery. Recovery proceeds by prompting you with suggested filenames of archived redo log files, and recovery completes when you specify CANCEL instead of a filename.

```
UNTIL TIME
```

Specifies an incomplete, time-based recovery. Use single quotes, and the following format:

```
'YYYY-MM-DD:HH24:MI:SS'
```
```
UNTIL CHANGE
```

Specifies an incomplete, change-based recovery. integer is the number of the System Change Number (SCN) following the last change you wish to recover. For example, if you want to restore your database up to the transaction with an SCN of 9, you would specify UNTIL CHANGE 10.

```
USING BACKUP CONTROLFILE
```

Specifies that a backup of the control file be used instead of the current control file.

```
TABLESPACE
```

Recovers a particular tablespace. tablespace is the name of a tablespace in the current database. You may recover up to 16 tablespaces in one statement.

```
DATAFILE
```

Recovers a particular datafile. You can specify any number of datafiles.

```
STANDBY TABLESPACE
```

Reconstructs a lost or damaged tablespace in the standby database using archived redo log files copied from the primary database and a control file.

```
STANDBY DATAFILE
```

Reconstructs a lost or damaged datafile in the standby database using archived redo log files copied from the primary database and a control file.

```
UNTIL CONSISTENT WITH CONTROLFILE
```

Specifies that the recovery of an old standby datafile or tablespace uses the current standby database control file.

```
PARALLEL [integer]
```

This is the default. SQL\*Plus selects a degree of parallelism equal to the number of CPUs available on all participating instances times the value of the PARALLEL\_THREADS\_PER\_CPU initialization parameter.

The PARALLEL keyword overrides the RECOVERY\_PARALLELISM initialization parameter. For more information about the PARALLEL keyword see the [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=RACAD) guide.

Use integer to specify the degree of parallelism, which is the number of parallel threads used in the parallel operation. Each parallel thread may use one or two parallel execution processes.

```
NOPARALLEL
```

Specifies serial recovery processing.

```
MANAGED STANDBY DATABASE
```

Specifies sustained standby recovery mode. This mode assumes that the standby database is an active component of an overall standby database architecture. A primary database actively archives its redo log files to the standby site. As these archived redo logs arrive at the standby site, they become available for use by a managed standby recovery operation. Sustained standby recovery is restricted to media recovery.

For more information on the parameters of this clause, see the [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=BRADV).

```
DISCONNECT
```

Indicates that the managed redo process (MRP) should apply archived redo files as a detached background process. Doing so leaves the current session available.

```
TIMEOUT
```

Specifies in minutes the wait period of the sustained recovery operation. The recovery process waits for integer minutes for a requested archived log redo to be available for writing to the standby database. If the redo log file does not become available within that time, the recovery process terminates with an error message. You can then issue the statement again to return to sustained standby recovery mode.

If you do not specify this clause, or if you specify NOTIMEOUT, the database remains in sustained standby recovery mode until you reissue the statement with the RECOVER CANCEL clause or until instance shutdown or failure.

```
NODELAY
```

Applies a delayed archivelog immediately to the standby database overriding any DELAY setting in the LOG\_ARCHIVE\_DEST\_n parameter on the primary database. If you omit this clause, application of the archivelog is delayed according to the parameter setting. If DELAY was not specified in the parameter, the archivelog is applied immediately.

```
DEFAULT DELAY
```

Waits the default number of minutes specified in the LOG\_ARCHIVE\_DEST\_n initialization parameter before applying the archived redo logs.

```
DELAY integer
```

Waits integer minutes before applying the archived redo logs.

```
NEXT integer
```

Applies the specified number of archived redo logs as soon as possible after they have been archived. It temporarily overrides any DELAY setting in the LOG\_ARCHIVE\_DEST\_n parameter on the primary database, and any delay values set in an earlier SQL\*Plus RECOVER command or an ALTER DATABASE RECOVER command.

```
EXPIRE integer
```

Specifies the number of minutes from the current time after which managed recovery terminates automatically.

```
NO EXPIRE
```

Disables a previously specified EXPIRE integer option.

```
USING CURRENT LOGFILE
```

Recovers redo from standby online logs as they are being filled, without requiring them to be archived in the standby database first.

```
UNTIL CHANGE integer
```

Processes managed recovery up to but not including the specified system change number (SCN).

```
THROUGH THREAD integer SEQUENCE integer
```

Terminates managed recovery based on archivelog thread number and sequence number. Managed recovery terminates when the corresponding archivelog has been applied. If omitted, THREAD defaults to 1.

```
THROUGH ALL ARCHIVELOG
```

Continues managed standby until all archivelogs have been recovered. You can use this statement to override a THROUGH THREAD integer SEQUENCE integer clause issued in an earlier statement. If the THROUGH clause is omitted, this is the default.

```
THROUGH ALL SWITCHOVER
```

Keeps managed standby recovery running through all switchover operations.

```
THROUGH LAST  SWITCHOVER
```

Terminates managed standby recovery after the final end-of-redo archival indicator.

```
THROUGH NEXT  SWITCHOVER
```

Terminates managed standby recovery after recovering the next end-of-redo archival indicator.

```
CANCEL (managed clause)
```

Terminates managed standby recovery after applying the current archived redo file. Session control returns when the recovery process terminates.

```
CANCEL IMMEDIATE
```

Terminates managed standby recovery after applying the current archived redo file, or after the next redo log file read, whichever comes first. Session control returns when the recovery process terminates.

```
CANCEL IMMEDIATE WAIT
```

Terminates managed standby recovery after applying the current archived redo file or after the next redo log file read, whichever comes first. Session control returns when the managed standby recovery terminates.

CANCEL IMMEDIATE cannot be issued from the same session that issued the RECOVER MANAGED STANDBY DATABASE statement.

```
CANCEL IMMEDIATE NOWAIT
```

Terminates managed standby recovery after applying the current archived redo file, or after the next redo log file read, whichever comes first. Session control returns immediately.

```
CANCEL NOWAIT
```

Terminates managed standby recovery after the next redo log file read and returns session control immediately.

```
FINISH
```

Recovers the current standby online logfiles of the standby database. This clause may be useful if the primary database fails. It overrides any delays specified for archivelogs, so that logs are applied immediately.

FINISH cannot be issued if you have also specified TIMEOUT, DELAY, EXPIRE or NEXT clauses.

Usage

You must have the OSDBA role enabled. You cannot use the RECOVER command when connected through the multi-threaded server.

To perform media recovery on an entire database (all tablespaces), the database must be mounted and closed, and all tablespaces requiring recovery must be online.

To perform media recovery on a tablespace, the database must be mounted or open, and the tablespace must be offline.

To perform media recovery on a datafile, the database can remain open and mounted with the damaged datafiles offline (unless the file is part of the SYSTEM tablespace).

Before using the RECOVER command you must have restored copies of the damaged datafiles from a previous backup. Be sure you can access all archived and online redo log files dating back to when that backup was made.

When another log file is required during recovery, a prompt suggests the names of files that are needed. The name is derived from the values specified in the initialization parameters LOG\_ARCHIVE\_DEST and LOG\_ARCHIVE\_FORMAT. You should restore copies of the archived redo log files needed for recovery to the destination specified in LOG\_ARCHIVE\_DEST, if necessary. You can override the initialization parameters by setting the LOGSOURCE variable with the SET LOGSOURCE command.

During recovery you can accept the suggested log name by pressing return, cancel recovery by entering CANCEL instead of a log name, or enter AUTO at the prompt for automatic file selection without further prompting.

If you have enabled autorecovery (that is, SET AUTORECOVERY ON), recovery proceeds without prompting you with filenames. Status messages are displayed when each log file is applied. When normal media recovery is done, a completion status is returned.

Examples

To recover the entire database, enter

```
RECOVER DATABASE
```

To recover the database until a specified time, enter

```
RECOVER DATABASE UNTIL TIME 01-JAN-2001:04:32:00
```

To recover the two tablespaces ts\_one and ts\_two from the database, enter

```
RECOVER TABLESPACE ts_one, ts_two
```

To recover the datafile data1.db from the database, enter

```
RECOVER DATAFILE 'data1.db'
```