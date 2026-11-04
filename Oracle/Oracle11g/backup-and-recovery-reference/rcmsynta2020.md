---
title: SWITCH
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2020.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Purpose

Use the `SWITCH` command to perform either of the following operations:

- Update the file names for a database, tablespace, or data file to the latest image copies available for the specified files
- Update the file names for data files and temp files for which you have issued a `SET` `NEWNAME` command

A `SWITCH` is equivalent to the SQL statement `ALTER DATABASE RENAME FILE`: the names of the files in the RMAN repository are updated, but the database does not rename the files at the operating system level.

Prerequisites

RMAN must be connected to a target database. When switching tablespaces, data files, or temp files, the files must be offline. When switching the whole database, the database must not be open.

Usage Notes

The `SWITCH` command deletes the RMAN repository records for the data file copy from the recovery catalog and updates the control file records to status `DELETED`.

If RMAN is connected to a recovery catalog, and if the database is using a control file restored from backup, then `SWITCH` updates the control file with records of any data files known to the recovery catalog but missing from the control file.

Execute `SWITCH ... TO COPY` only at the RMAN prompt. Use `SWITCH` without `TO COPY` only within a `RUN` block.

Semantics

switch

This subclause switches file names for a database, tablespace, or data file to the latest image copies available for the specified files. By executing this command, you avoid restoring data files from backups. Execute `SWITCH ... TO COPY` only at the RMAN prompt.

| Syntax Element | Description |
| --- | --- |
| `DATABASE` | Renames the data files and control files to use the file names of image copies of these files. RMAN switches to the latest image copy of each database file.  After a database switch, RMAN considers the previous database files as data file copies. |
| `DATAFILE` `datafileSpec` | Switches the specified data files to the latest image copies.  After the switch, the control file no longer considers the specified data file as current. |
| `TABLESPACE` `tablespace_name` | Switches all data files within the specified tablespace, as with `SWITCH DATAFILE ... TO COPY` (see Example 3-55). |
| `   TO COPY` | Switches the specified active database files to image copies. |

switchFile

This subclause updates the names for data files and temp files for which you have issued a `SET` `NEWNAME` command. Use this clause only within a `RUN` block.

| Syntax Element | Description |
| --- | --- |
| `DATAFILE` `ALL` | Specifies that all data files for which a `SET` `NEWNAME FOR DATAFILE` command has been issued in this job are switched to their new name (see Example 3-56). |
| `DATAFILE` `datafileSpec` | Specifies the data file that are renaming. After the switch, the control file no longer considers the specified file as current. If you do not specify a `TO` option, then RMAN uses the file name specified on a prior `SET` `NEWNAME` command in the `RUN` block for this file as the switch target. |
| `   TO DATAFILECOPY`   `   {'` `filename` `'` `\|`   `    TAG` `tag_name` `}` | Specifies the input copy file for the switch, that is, the data file copy that you intend to rename (see Example 3-58). |
| `TEMPFILE ALL` | Specifies that all temp files for which a `SET` `NEWNAME FOR TEMPFILE` command has been issued in this job are switched to their new name. |
| `TEMPFILE` `tempfileSpec` | Specifies the temp file that you are renaming. If you do not specify a `TO` option, then RMAN uses the file name specified on a prior `SET` `NEWNAME` command in the `RUN` block for this file as the switch target. The target database must be mounted but not open. |
| `   TO` `'` `filename` `'` | Renames the temp file to the specified name (see Example 3-57). The target database must be mounted but not open. |

Examples

Example 3-55 Switching to Image Copies to Avoid Restoring from Backup

Assume that a disk fails, rendering all data files in the `users` tablespace inaccessible. Image copies of all data files in this tablespace exist in the fast recovery area. After starting RMAN and connecting to the database as `TARGET`, you can run `SWITCH` to point the control file to the new data files and then run `RECOVER` as follows:

```
SQL "ALTER TABLESPACE users OFFLINE IMMEDIATE";
SWITCH TABLESPACE users TO COPY;
RECOVER TABLESPACE users;
SQL "ALTER TABLESPACE users ONLINE";
```

Example 3-56 Switching Data File File Names After a Restore to a New Location

Assume that a disk fails, forcing you to restore a data file to a new disk location. After starting RMAN and connecting to the database as `TARGET`, you can use the `SET` `NEWNAME` command to rename the data file, then `RESTORE` to restore the missing data file. You run `SWITCH` to point the control file to the new data file and then `RECOVER`. This example allocates both disk and tape channels.

```
RUN
{
  ALLOCATE CHANNEL dev1 DEVICE TYPE DISK;
  ALLOCATE CHANNEL dev2 DEVICE TYPE sbt;
  SQL "ALTER TABLESPACE users OFFLINE IMMEDIATE";
  SET NEWNAME FOR DATAFILE '/disk1/oradata/prod/users01.dbf'
                        TO '/disk2/users01.dbf';
  RESTORE TABLESPACE users;
  SWITCH DATAFILE ALL;
  RECOVER TABLESPACE users;
  SQL "ALTER TABLESPACE users ONLINE";
}
```

Example 3-57 Renaming Temp Files Using SET NEWNAME and SWITCH TEMPFILE ALL

This example demonstrates using `SET NEWNAME` to specify new names for several temp files, and `SWITCH TEMPFILE ALL` to rename the temp files to the specified names. The database must be closed at the beginning of this procedure. The temp files are re-created at the new locations when the database is opened.

```
CONNECT TARGET /
STARTUP FORCE MOUNT
RUN
{  
  SET NEWNAME FOR TEMPFILE 1 TO '/disk2/temp01.dbf';
  SET NEWNAME FOR TEMPFILE 2 TO '/disk2/temp02.dbf';
  SET NEWNAME FOR TEMPFILE 3 TO '/disk2/temp03.dbf'; 
  SWITCH TEMPFILE ALL;  
  RESTORE DATABASE;  
  RECOVER DATABASE;  
  ALTER DATABASE OPEN;
}
```

Example 3-58 Switching to a Data File Copy

The following command switches the data file in the `tools` tablespace to the data file copy named `/disk2/tools.copy`:

```
RUN
{ 
  SQL "ALTER TABLESPACE tools OFFLINE IMMEDIATE";
  SWITCH DATAFILE '/disk1/oradata/prod/tools01.dbf' 
  TO DATAFILECOPY '/disk2/tools.copy'; 
  RECOVER TABLESPACE tools;
  SQL "ALTER TABLESPACE tools ONLINE";
}
```