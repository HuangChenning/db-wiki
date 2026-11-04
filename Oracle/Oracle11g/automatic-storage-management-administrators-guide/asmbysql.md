---
title: "Creating Database Files in Oracle ASM Using SQL*Plus"
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmbysql.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

## A Creating Database Files in Oracle ASM Using SQL\*Plus

This appendix describes how to deploy Oracle Automatic Storage Management (Oracle ASM) using SQL\*Plus under the following topics:

## Creating a Database that Uses Oracle ASM

The recommended method of creating your database is to use Database Configuration Assistant (DBCA). However, if you create your database manually using the `CREATE DATABASE` statement, then Oracle ASM enables you to create a database and all of its underlying files with a minimum of input.

The following section describes an example of using the `CREATE DATABASE` statement, where database files are created and managed automatically by Oracle ASM.

### Creating a Database that Uses Oracle ASM: Example

This example creates a database with the following Oracle ASM files:

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

The following statement is run at the SQL prompt:

```
CREATE DATABASE orcl;
```

## Creating Tablespaces in Oracle ASM

When Oracle ASM creates a data file for a permanent tablespace (or a temporary file for a temporary tablespace), the data file is set to auto-extensible with an unlimited maximum size and 100 MB default size. You can use the `AUTOEXTEND` clause to override this default extensibility and the `SIZE` clause to override the default size.

Oracle ASM applies attributes to the data file, as specified in the system default template for a data file as shown in the table in ["Managing Disk Group Templates"](asmfiles.md). You can also create and specify your own template.

Files in a tablespace might be in both Oracle ASM files and non-Oracle ASM files due to the tablespace history. RMAN commands enable non-Oracle ASM files to be relocated to an Oracle ASM disk group and enable Oracle ASM files to be relocated as non-Oracle ASM files.

For example, if there is a disk group named `data`, then you can create a tablespace `tblspace` in that disk group with the following SQL statement:

```
CREATE TABLESPACE tblspace DATAFILE +data;
```

The following example illustrates the usage of Oracle ASM with defaults. This example enables Oracle ASM to create and manage the tablespace data file for you, using Oracle supplied defaults that are adequate for most situations.

Assume the following initialization parameter setting:

```
DB_CREATE_FILE_DEST = +data
```

The following statement creates the tablespace and its data file:

```
CREATE TABLESPACE tblspace;
```

## Creating Redo Logs in Oracle ASM

Online redo logs can be created in multiple disk groups, either implicitly in an initialization parameter file or explicitly in an `ALTER DATABASE...ADD LOGFILE` statement. Each online log should have one log member in multiple disk groups. The filenames for log file members are automatically generated. All partially created redo log files, created because of a system error, are automatically deleted.

For example, if there are disk groups named `data1` and `data2`, you can create a log file with a member in each disk group with the following SQL statement:

```
ALTER DATABASE ADD LOGFILE (+data1,+data2);
```

The following example creates a log file with a member in each of the disk groups `data1` and `data2`. The following parameter settings are included in the initialization parameter file:

```
DB_CREATE_ONLINE_LOG_DEST_1 = +data1
DB_CREATE_ONLINE_LOG_DEST_2 = +data2
```

The following statement is run at the SQL prompt:

```
ALTER DATABASE ADD LOGFILE;
```

## Creating Control Files in Oracle ASM

Control files can be explicitly created in multiple disk groups. The filenames for control files are automatically generated.

If you must specify a control file by name, then you can use alias filenames to reference Oracle ASM files and use easy to understand names. Using aliases in the specification of a control file during its creation enables you to later refer to the control file with a user-specified name. An alias can also be specified as a control file name in the `CONTROL_FILES` initialization parameter.

When creating a control file, data files and log files that are stored in Oracle ASM disk groups should be given to the `CREATE` `CONTROLFILE` command using the file reference form of their Oracle ASM filenames. However, the use of the `RESETLOGS` option requires the use of a file creation form for the specification of the log files.

### Creating Control Files in Oracle ASM: Example 1

The following `CREATE` `CONTROLFILE` statement is generated by an `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `TRACE` command for a database with data files and log files created on disk groups `data` and `fra`:

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

### Creating Control Files in Oracle ASM: Example 2

This example is a `CREATE` `CONTROLFILE` statement for a database with data files, but uses a `RESETLOGS` clause, and thus uses the creation form for log files:

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

## Creating Archive Log Files in Oracle ASM

Disk groups can be specified as archive log destinations in the `LOG_ARCHIVE_DEST` and `LOG_ARCHIVE_DEST_n` initialization parameters. When destinations are specified in this manner, the archive log filenames are unique, even if archived twice.

If `LOG_ARCHIVE_DEST` is set to a disk group name, `LOG_ARCHIVE_FORMAT` is ignored. Unique filenames for archived logs are automatically created by the Oracle database. If `LOG_ARCHIVE_DEST` is set to a directory in a disk group, `LOG_ARCHIVE_FORMAT` has its normal semantics.

The following sample archive log names might be generated with `DB_RECOVERY_FILE_DEST` set to `+data`. `ORCL` is the value of the `DB_UNIQUE_NAME` parameter:

```
+DATA/ORCL/ARCHIVELOG/2009_09_23/thread_1_seq_38.614.541956473
+DATA/ORCL/ARCHIVELOG/2009_09_23/thread_4_seq_35.609.541956477
+DATA/ORCL/ARCHIVELOG/2009_09_23/thread_2_seq_34.603.541956487
+DATA/ORCL/ARCHIVELOG/2009_09_25/thread_3_seq_100.621.541956497
+DATA/ORCL/ARCHIVELOG/2009_09_25/thread_1_seq_38.614.541956511
```