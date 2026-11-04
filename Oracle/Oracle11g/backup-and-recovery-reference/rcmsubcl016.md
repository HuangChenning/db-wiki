---
title: recordSpec
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl016.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Purpose

Use the `recordSpec` subclause to specify which backups or copies the `CHANGE`, `CROSSCHECK`, `DELETE`, and `LIST` commands should process.

Most `recordSpec` options allow you to specify a primary key. Use the output of the `LIST` command to obtain primary keys.

Semantics

| Syntax Element | Description |
| --- | --- |
| `ARCHIVELOG` | Specifies an archived redo log by either primary key or file name. |
| `BACKUPSET` | Specifies a backup set by primary key. |
| `BACKUPPIECE` | Specifies a backup piece by media handle, primary key, or tag name. |
| `PROXY` | Specifies a proxy copy by media handle, primary key, or tag name. |
| `CONTROLFILECOPY` | Specifies a control file copy by primary key, file name pattern (`'filename'`), or `TAG` `tag_name`. If you crosscheck a control file copy, then you must specify a file name rather than a primary key. |
| `DATAFILECOPY` | Specifies a data file copy by primary key, file name pattern (`'filename'`), tag (`TAG` `tag_name`), or matching string (`LIKE '` `string_pattern` `'`). Specify `ALL` to indicate all data file copies recorded in the RMAN repository. |
| `   NODUPLICATES` | Specifies that only one copy of the control file or data file copy specified by the rest of the clause is the target of the operation, even when there are multiple copies. |

Examples

Example 4-32 Crosschecking Backups

This example crosschecks backup sets specified by primary key:

```
RMAN> LIST BACKUP SUMMARY; 
 
List of Backups
===============
Key     TY LV S Device Type Completion Time #Pieces #Copies Compressed Tag
------- -- -- - ----------- --------------- ------- ------- ---------- ---
8504    B  A  A SBT_TAPE    08-MAR-07       1       1       NO         TAG20070308T155057
8558    B  F  A SBT_TAPE    08-MAR-07       1       1       NO         TAG20070308T155114
9872    B  F  A DISK        08-MAR-07       1       1       NO         TAG20070308T160830
9954    B  A  A SBT_TAPE    08-MAR-07       1       1       NO         TAG20070308T161157
9972    B  F  A SBT_TAPE    08-MAR-07       1       1       NO         TAG20070308T161224
10021   B  A  A SBT_TAPE    08-MAR-07       1       1       NO         TAG20070308T161251
10042   B  F  A SBT_TAPE    08-MAR-07       1       1       NO         TAG20070308T161308
10185   B  F  A DISK        08-MAR-07       1       1       NO         TAG20070308T170532
10210   B  F  A DISK        08-MAR-07       1       1       NO         TAG20070308T170535
 
RMAN> CROSSCHECK BACKUPSET 9872, 10185, 10210;
 
allocated channel: ORA_SBT_TAPE_1
channel ORA_SBT_TAPE_1: SID=103 device type=SBT_TAPE
channel ORA_SBT_TAPE_1: Oracle Secure Backup
using channel ORA_DISK_1
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/disk2/PROD/autobackup/2007_03_08/o1_mf_s_616694910_2z19d0wg_.bkp RECID=197 STAMP=616694912
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/disk2/PROD/backupset/2007_03_08/o1_mf_nnsnf_TAG20070308T170532_2z1dpwz6_.bkp RECID=202 STAMP=616698332
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=/disk2/PROD/autobackup/2007_03_08/o1_mf_s_616698335_2z1dq0d0_.bkp RECID=203 STAMP=616698336
Crosschecked 3 objects
```

Example 4-33 Deleting Data File Copies

This example deletes the specified data file copy:

```
RMAN> DELETE NOPROMPT DATAFILECOPY '/disk1/oradata/prod/users01.dbf';
```