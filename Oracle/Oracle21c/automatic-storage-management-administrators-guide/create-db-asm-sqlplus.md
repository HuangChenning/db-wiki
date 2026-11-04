---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/create-db-asm-sqlplus.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

Oracle Automatic Storage Management (Oracle ASM) can be deployed using SQL\*Plus.

This section contains the following topics:

### Creating a Database that Uses Oracle ASM

The recommended method of creating your database is to use Database Configuration Assistant (DBCA). However, if you create your database manually using the `CREATE DATABASE` statement, then Oracle ASM enables you to create a database and all of its underlying files with a minimum of input.

The following example shows the use of the `CREATE DATABASE` statement, where database files are created and managed automatically by Oracle ASM. This example creates a database with the following Oracle ASM files:

- A `SYSTEM` tablespace data file in disk group `data`.
- A `SYSAUX` tablespace data file in disk group `data`. The tablespace is locally managed with automatic segment-space management.
- A multiplexed online redo log with two online log groups, one member of each in `data` and `fra` (fast recovery area).
- If automatic undo management mode is enabled, then an undo tablespace data file in directory `data`.
- If you do not specify a value for the `CONTROL_FILES` initialization parameter, then two control files, one in `data` and another in `fra` (fast recovery area). The control file in `data` is the primary control file.

The following initialization parameter settings are included in the initialization parameter file:

```
DB_CREATE_FILE_DEST = +data
DB_RECOVERY_FILE_DEST = +fra
DB_RECOVERY_FILE_DEST_SIZE = 10G
```

The following statement can be run at the SQL prompt:

```
SQL> CREATE DATABASE orcl;
```

### Creating Tablespaces in Oracle ASM

When Oracle ASM creates a data file for a permanent tablespace (or a temporary file for a temporary tablespace), the data file is set to auto-extensible with an unlimited maximum size and 100 MB default size. You can use the `AUTOEXTEND` clause to override this default extensibility and the `SIZE` clause to override the default size.

Oracle ASM applies attributes to the data file, as specified in the system default template for a data file as shown in the table in " [Managing Disk Group Templates](asm-files-directories-templates.md) ". You can also create and specify your own template.

Files in a tablespace might be in both Oracle ASM files and non-Oracle ASM files due to the tablespace history. RMAN commands enable non-Oracle ASM files to be relocated to an Oracle ASM disk group and enable Oracle ASM files to be relocated as non-Oracle ASM files.

For example, if there is a disk group named `data`, then you can create a tablespace `tblspace` in that disk group with the following SQL statement:

```
SQL> CREATE TABLESPACE tblspace DATAFILE '+data';
```

The following example illustrates the usage of Oracle ASM with defaults. This example enables Oracle ASM to create and manage the tablespace data file for you, using Oracle supplied defaults that are adequate for most situations.

Assume the following initialization parameter setting:

```
DB_CREATE_FILE_DEST = +data
```

The following statement creates the tablespace and its data file:

```
SQL> CREATE TABLESPACE tblspace;
```

### Creating Redo Logs in Oracle ASM

Online redo logs can be created in multiple disk groups, either implicitly in an initialization parameter file or explicitly in an `ALTER DATABASE...ADD LOGFILE` statement. Each online log should have one log member in multiple disk groups. The file names for log file members are automatically generated. All partially created redo log files, created because of a system error, are automatically deleted.

For example, if there are disk groups named `data1` and `data2`, you can create a log file with a member in each disk group with the following SQL statement:

```
SQL> ALTER DATABASE ADD LOGFILE ('+data1','+data2');
```

The following example creates a log file with a member in each of the disk groups `data1` and `data2`. These parameter settings are included in the initialization parameter file:

```
DB_CREATE_ONLINE_LOG_DEST_1 = +data1
DB_CREATE_ONLINE_LOG_DEST_2 = +data2
```

The following statement can be run at the SQL prompt:

```
SQL> ALTER DATABASE ADD LOGFILE;
```

### Creating Control Files in Oracle ASM

Control files can be explicitly created in multiple disk groups. The file names for control files are automatically generated.

If you must specify a control file by name, then you can use alias file names to reference Oracle ASM files and use easy to understand names. Using aliases in the specification of a control file during its creation enables you to later refer to the control file with a user-specified name. An alias can also be specified as a control file name in the `CONTROL_FILES` initialization parameter.

When creating a control file, data files and log files that are stored in Oracle ASM disk groups should be given to the `CREATE` `CONTROLFILE` command using the file reference form of their Oracle ASM file names. However, the use of the `RESETLOGS` option requires the use of a file creation form for the specification of the log files.

Example 13-1 Creating control files in Oracle ASM using NORESETLOGS

The SQL statement in the following example is generated by an `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `TRACE` command for a database with data files and log files created on disk groups `data` and `fra`:

```
CREATE CONTROLFILE REUSE DATABASE "ORCL" NORESETLOGS  ARCHIVELOG
    MAXLOGFILES 16
    MAXLOGMEMBERS 3
    MAXDATAFILES 100
    MAXINSTANCES 8
    MAXLOGHISTORY 292
LOGFILE
  GROUP 1 (
    '+DATA/orcl/onlinelog/group_1.261.685366203',
    '+FRA/orcl/onlinelog/group_1.257.685366205'
  ) SIZE 50M BLOCKSIZE 512,
  GROUP 2 (
    '+DATA/orcl/onlinelog/group_2.262.685366207',
    '+FRA/orcl/onlinelog/group_2.258.685366211'
  ) SIZE 50M BLOCKSIZE 512,
  GROUP 3 (
    '+DATA/orcl/onlinelog/group_3.263.685366213',
    '+FRA/orcl/onlinelog/group_3.259.685366215'
  ) SIZE 50M BLOCKSIZE 512
-- STANDBY LOGFILE
DATAFILE
  '+DATA/orcl/datafile/system.256.685366089',
  '+DATA/orcl/datafile/sysaux.257.685366089',
  '+DATA/orcl/datafile/undotbs1.258.685366091',
  '+DATA/orcl/datafile/users.259.685366091'
CHARACTER SET WE8MSWIN1252
;
```

Example 13-2 Creating control files in Oracle ASM using RESETLOGS

The following example is a `CREATE` `CONTROLFILE` SQL statement for a database with data files, but uses a `RESETLOGS` clause, which uses the creation form for log files:

```
CREATE CONTROLFILE REUSE DATABASE "ORCL" RESETLOGS  ARCHIVELOG
    MAXLOGFILES 16
    MAXLOGMEMBERS 3
    MAXDATAFILES 100
    MAXINSTANCES 8
    MAXLOGHISTORY 292
LOGFILE
  GROUP 1 (
    '+DATA/orcl/onlinelog/group_1.261.685366203',
    '+FRA/orcl/onlinelog/group_1.257.685366205'
  ) SIZE 50M BLOCKSIZE 512,
  GROUP 2 (
    '+DATA/orcl/onlinelog/group_2.262.685366207',
    '+FRA/orcl/onlinelog/group_2.258.685366211'
  ) SIZE 50M BLOCKSIZE 512,
  GROUP 3 (
    '+DATA/orcl/onlinelog/group_3.263.685366213',
    '+FRA/orcl/onlinelog/group_3.259.685366215'
  ) SIZE 50M BLOCKSIZE 512
-- STANDBY LOGFILE
DATAFILE
  '+DATA/orcl/datafile/system.256.685366089',
  '+DATA/orcl/datafile/sysaux.257.685366089',
  '+DATA/orcl/datafile/undotbs1.258.685366091',
  '+DATA/orcl/datafile/users.259.685366091'
CHARACTER SET WE8MSWIN1252
;
```

### Creating Archive Log Files in Oracle ASM

Disk groups can be specified as archive log destinations in the `LOG_ARCHIVE_DEST` and `LOG_ARCHIVE_DEST_n` initialization parameters. When destinations are specified in this manner, the archive log file names are created in default subdirectories with unique names. However, all `LOG_ARCHIVE_DEST_n` parameters must have a unique string. To enter the same disk group more than once, subdirectories must be used. For example, you can set `LOG_ARCHIVE_DEST_n` as follows:

```
LOG_ARCHIVE_DEST_1 = 'LOCATION=+FRA/orcl/arc_1'
LOG_ARCHIVE_DEST_2 = 'LOCATION=+FRA/orcl/arc_2'
...
```

If `LOG_ARCHIVE_DEST` is set to a disk group name, `LOG_ARCHIVE_FORMAT` is ignored. Unique filenames for archived logs are automatically created by Oracle Database under default subdirectories. If `LOG_ARCHIVE_DEST` is set to a directory in a disk group, `LOG_ARCHIVE_FORMAT` has its normal semantics for the file alias. The underlying file is still generated in the default directories for the disk group with a system generated name.

You can also set the `DB_RECOVERY_FILE_DEST` initialization parameter to a disk group destination. In Example 13-3, archive log files are generated with `ARCHIVELOG` mode enabled, `DB_RECOVERY_FILE_DEST` set to the `+FRA` disk group, and `ORCL` is the value of the `DB_UNIQUE_NAME` parameter.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN008) for information about managing archived redo log files

Example 13-3 Archived log files in an Oracle ASM disk group

```
SQL> SHOW PARAMETER DB_RECOVERY_FILE_DEST

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
db_recovery_file_dest                string      +FRA

SQL> SELECT SUBSTR(name,1,64) name FROM V$ARCHIVED_LOG;
 
NAME
----------------------------------------------------------------
+FRA/ORCL/ARCHIVELOG/2013_06_24/thread_1_seq_112.260.818960623
+FRA/ORCL/ARCHIVELOG/2013_06_24/thread_1_seq_113.261.818978423
+FRA/ORCL/ARCHIVELOG/2013_06_25/thread_1_seq_114.262.818993031
+FRA/ORCL/ARCHIVELOG/2013_06_25/thread_1_seq_115.263.819032439
+FRA/ORCL/ARCHIVELOG/2013_06_25/thread_1_seq_116.264.819047121
+FRA/ORCL/ARCHIVELOG/2013_06_25/thread_1_seq_117.265.819064815
+FRA/ORCL/ARCHIVELOG/2013_06_26/thread_1_seq_118.266.819079417
...
```