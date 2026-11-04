---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/CATALOG.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

Purpose

Use the `CATALOG` command to do the following:

- Add backup pieces and image copies on disk to the RMAN repository
- Record a data file copy as a level 0 incremental backup in the RMAN repository, which enables you to use it as part of an incremental backup strategy

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV8007) to learn how to manage target database records stored in the catalog

Prerequisites

You must be connected to the target database, which must be mounted or open. If RMAN is connected to a recovery catalog, then the catalog database must be open.

The file that you are cataloging must meet the following conditions:

- It must not exist on an SBT device.
- If it is a user-managed copy, then it must be a data file copy, control file copy, archived redo log, or backup piece.

Usage Notes

RMAN considers all user-managed backups as image copies. While cataloging, RMAN does not check whether the file was correctly copied by the operating system utility: it just checks the header.

A recovery catalog is required when using RMAN in a Data Guard environment. The recovery catalog supports a unified file namespace for all primary and standby databases with the same DBID but different `DB_UNIQUE_NAME` values. Thus, the recovery catalog keeps track of database file names for all primary and standby databases, and also where online redo logs, standby redo logs, temp files, archived redo log files, backup sets, and image copies were created.

" [RMAN Backups in a Data Guard Environment](BACKUP.md) " explains how RMAN handles backups made on a different primary and standby databases. In general, tape backups made on one database are accessible to any database in the environment, whereas disk backups are accessible only to the database that created them.

If backups are accessible to the connected target database, RMAN commands such as `RESTORE` and `RECOVER` behave transparently across different databases. You can manually transfer a disk backup from one host in the environment to another host and then catalog the backup. If a backup is on shared disk, then you can use `CHANGE` `RESET DB_UNIQUE_NAME` to associate the backup with a new database.

Syntax

catalog::=

![catalog](img/catalog.gif)

> CATALOG {\[PREPLUGIN\] { {ARCHIVELOG | BACKUPPIECE} ' filename ' \[, ' filename '\]... | BACKUPPIECE FROM FILE ' filename ' | DEVICE TYPE deviceSpecifier {BACKUPPIECE ' filename ' \[, ' filename '\]... | BACKUPPIECE FROM FILE ' filename '} | CONTROLFILECOPY ' filename ' \[, ' filename '\]...} | DATAFILECOPY ' filename ' \[, ' filename '\]... \[ { {LEVEL integer | TAG \['\] tag\_name \['\]}}...\] | { {RECOVERY AREA | DB\_RECOVERY\_FILE\_DEST} | START WITH ' string\_pattern '} \[NOPROMPT\]}


Semantics

| Syntax Element | Description |
| --- | --- |
| `PREPLUGIN ARCHIVELOG` | Specifies the names of preplugin archived redo logs that must be added to the RMAN repository. Use a comma-separated list to specify multiple names. This command is used to catalog preplugin backups that were created on a source database and subsequently moved to a different backup location.  The CDB must be open in read-write mode and you must be connected to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.  Note: You cannot catalog preplugin backups created on standby databases. To restore standby data files, you must copy the data files from the primary using `RESTORE...FROM SERVICE` command. |
| `PREPLUGIN BACKUPPIECE` | This clause is not supported in the current release. |
| `PREPLUGIN CONTROLFILECOPY` | This clause is not supported in the current release. |
| `ARCHIVELOG` `'` `filename` `'` | Specifies the file name of an archived redo log to be added to the RMAN repository.  Note: This command does not catalog foreign archived redo log files, which are redo logs received by a logical standby database for a LogMiner session. Unlike normal archived redo log files, foreign archived redo log files have a different DBID. |
| `BACKUPPIECE` `'` `filename` `'` | Specifies the name of a backup piece to be added to the RMAN repository (see Example 2-40).  The backup piece must be on disk. RMAN verifies the backup piece header before cataloging it. RMAN can catalog a backup piece from a previous database incarnation.  You may choose to catalog backup pieces in the following situations:  - You copy or move a backup piece with an operating system utility and want it to be usable by RMAN. - The RMAN metadata for the backup piece was removed, but the backup piece still exists. This situation can occur if you ran the `DELETE` command on a backup piece that was only temporarily unavailable. - You make a `NOCATALOG` backup on one database host in a Data Guard environment and move the backup piece to the same location on a different database host. In this case, the recovery catalog has no record of the original backup piece. - You do not use a recovery catalog and must re-create the control file, thereby losing all RMAN repository data. Cataloging your backups makes them available again. - When control file autobackup is disabled, you back up the control file and then back up the archived redo log files. You can restore and mount the control file, but must catalog the backup pieces containing the archived redo log files backed up after the control file.  If you specify a list of backup pieces, then RMAN attempts to catalog all pieces in the given list even if some of them fail. Cataloging a backup piece creates a new row in `V$BACKUP_PIECE`. A backup set is only usable when all backup pieces are cataloged because otherwise it is only in a partially available state.  Note: If RMAN creates a server parameter file backup when the `COMPATIBLE` parameter of the database is set to 11.0.0 or higher, then the backup is associated with this database. In this case, even if you connect RMAN to a different database and explicitly catalog the backup piece, the `DB_UNIQUE_NAME` associated with this backup does not change. For example, if RMAN backs up the server parameter file of the database with `DB_UNIQUE_NAME 'NEWYORK'` when `COMPATIBLE` is 11.0.0, then RMAN cannot use the server parameter file backup created at database `NEWYORK` to restore the server parameter file on database `BOSTON`. |
| `BACKUPPIECE FROM FILE` `'` `filename` `'` | Specifies the name of the XML file that contains the list of backup piece names to be added to the RMAN repository.  If the backup piece names are stored in an XML file, then use the `BACKUPPIECE` `FROM FILE` clause to specify the location of the XML file using `filename`.  For example: `CATALOG BACKUPPIECE FROM FILE` ' `home/oracle/OPC/metadata.xml` '  See [Extracting Backup Metadata from a Storage Bucket or a Container](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=CSDBB-GUID-43CE8E6C-1F2B-4D0E-ADBD-AE8EDC4AAD22) in Using Oracle Database Backup Cloud Service to learn how to construct an XML file for backups stored in Oracle Cloud.  Example 2-44 includes the sample contents of an XML file that contains the backup piece names. |
| `CONTROLFILECOPY` `'` `filename` `'` | Specifies the file name of a control file copy to be added to the RMAN repository. The control file copy can be a normal or standby control file copy created by one of the following commands:  - RMAN: `BACKUP` `AS COPY CURRENT CONTROLFILE` - SQL: `ALTER DATABASE BACKUP CONTROLFILE` - SQL: `ALTER DATABASE CREATE STANDBY CONTROLFILE`  Note: RMAN can automatically convert a primary database control file backup to a standby control file during a restore operation. |
| `DATAFILECOPY` `'` `filename` `'` | Specifies the file name of a data file copy to be added to the RMAN repository (see Example 2-40). You can create data file copies with the RMAN `BACKUP` `AS COPY` command or with operating system utilities used with `ALTER TABLESPACE BEGIN/END BACKUP`. |
| `   LEVEL` `integer` | Records the data file copy as a level 0 incremental backup (`0` is the only valid value of `LEVEL`).  You can perform incremental backups by using this data file copy as the base level 0 backup. |
| `   TAG` `tagname` | Specifies a tag for the data file copy. |
| `RECOVERY AREA` | Catalogs all valid backup sets, data file copies, and archived redo log files in the fast recovery area (see Example 2-42).  RMAN must be connected to a database as `TARGET`. The target database must be mounted or open. The keywords `RECOVERY AREA` and `DB_RECOVERY_FILE_DEST` are exact synonyms.  Note: This command also catalogs foreign archived redo log files, which are archived redo log files received by logical standby for a LogMiner session, if they exist in the fast recovery area. |
| `DB_RECOVERY_FILE_DEST` | The keywords `RECOVERY AREA` and `DB_RECOVERY_FILE_DEST` are exact synonyms. |
| `START WITH` `'` `string_pattern` `'` | Catalogs all valid backup sets, data file and control file copies, and archived redo log files whose name start with `string_pattern`. The string pattern can be an ASM disk group, Oracle-managed files directory, or part of a file name (see Example 2-41).  RMAN reports any files in the disk location that it cannot catalog. RMAN must be connected to a mounted target database.  If the string pattern specifies a file name, then it matches the left part of the file name pattern. For example, `/tmp/arc` matches everything in directories `/tmp/arc_dest` and ` /tmp/archive/january`, and file `/tmp/arc.cpy`.  Note: You cannot use wildcard characters in the string pattern, only a strict prefix. |
| `   NOPROMPT` | Suppresses the confirmation prompt. By default, RMAN prompts after every match. |

Examples

Example 2-40 Cataloging a Data File Copy as an Incremental Backup

Assume that you used a Linux utility to back up the `users01.dbf` data file to `/disk2/backup/users01.bak`. This example catalogs the data file copy as an incremental level 0 backup and then lists all copies.

```
CATALOG DATAFILECOPY '/disk2/backup/users01.bak' LEVEL 0;
LIST COPY;
```

Example 2-41 Cataloging Multiple Copies in a Directory

This example catalogs a directory full of archived redo log files that were copied into the `/disk2/archlog` directory with an operating system utility. The example includes sample output.

```
CATALOG START WITH '/disk2/archlog' NOPROMPT; 

searching for all files that match the pattern /disk2/archlog
 
List of Files Unknown to the Database
=====================================
File Name: /disk2/archlog/o1_mf_1_10_24trtc7s_.arc
File Name: /disk2/archlog/o1_mf_1_11_24trtg7s_.arc
File Name: /disk2/archlog/o1_mf_1_12_24trtk84_.arc
File Name: /disk2/archlog/o1_mf_1_13_24trtn85_.arc
File Name: /disk2/archlog/o1_mf_1_14_24trtq84_.arc
File Name: /disk2/archlog/o1_mf_1_15_24trtt84_.arc
File Name: /disk2/archlog/o1_mf_1_16_24trtx84_.arc
File Name: /disk2/archlog/o1_mf_1_17_24trv085_.arc
File Name: /disk2/archlog/o1_mf_1_18_24trv385_.arc
File Name: /disk2/archlog/o1_mf_1_19_24trv685_.arc
cataloging files...
cataloging done
 
List of Cataloged Files
=======================
File Name: /disk2/archlog/o1_mf_1_10_24trtc7s_.arc
File Name: /disk2/archlog/o1_mf_1_11_24trtg7s_.arc
File Name: /disk2/archlog/o1_mf_1_12_24trtk84_.arc
File Name: /disk2/archlog/o1_mf_1_13_24trtn85_.arc
File Name: /disk2/archlog/o1_mf_1_14_24trtq84_.arc
File Name: /disk2/archlog/o1_mf_1_15_24trtt84_.arc
File Name: /disk2/archlog/o1_mf_1_16_24trtx84_.arc
File Name: /disk2/archlog/o1_mf_1_17_24trv085_.arc
File Name: /disk2/archlog/o1_mf_1_18_24trv385_.arc
File Name: /disk2/archlog/o1_mf_1_19_24trv685_.arc
```

Example 2-42 Cataloging Files in the Fast Recovery Area

This example catalogs all files in the currently enabled fast recovery area without prompting the user for each one. As shown in the sample output, RMAN displays a message if it finds no files to catalog.

```
CATALOG RECOVERY AREA;
 
searching for all files in the recovery area
no files found to be unknown to the database
```

Example 2-43 Cataloging a Backup Piece

Assume that you use an operating system utility to copy a backup piece from one location to another. This example catalogs the backup piece in the new location (sample output included):

```
CATALOG BACKUPPIECE '/disk1/c-874220581-20131128-01';

using target database control file instead of recovery catalog
cataloged backup piece
backup piece handle=/disk1/c-874220581-20131128-01 RECID=12 STAMP=607695990
```

Example 2-44 Sample of a Backup Metadata XML File

The `metadata.xml` file stores the metadata of a backup piece.

```
<MetaData>
   <File>
      <Filename>6GJ28IEKFL_07CEC18D372F4D29E06379624664E053</Filename>
      <SetStamp>1150345378</SetStamp>
      <IsSpfile>NO</IsSpfile>
      <IsControlFile>NO</IsControlFile>  
      <PieceNo>1</PieceNo>
      <Dbname>SALESDB</Dbname>
      <Dbid>3483424530</Dbid>          
   </File>
<File>
      <Filename>6GJ28IEKFL_07CEC1A6254D4D36E0637962466444CD</Filename>
      <SetStamp>1150345451</SetStamp>
      <IsSpfile>NO</IsSpfile>
      <IsControlFile>NO</IsControlFile>  
      <PieceNo>1</PieceNo>
      <Dbname>SALESDB</Dbname>
      <Dbid>3483424530</Dbid>          
   </File>
</MetaData>
```