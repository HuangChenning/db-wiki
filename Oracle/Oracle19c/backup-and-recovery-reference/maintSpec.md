---
title: Backup and Recovery Reference
book: Oracle AI Database Backup and Recovery Reference
doc_id: E96242-15
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/rcmrf/maintSpec.html
tags:
  - oracle
  - 19c
  - backup-and-recovery-reference
---

## 4.16 maintSpec

Purpose

Use the `maintSpec` subclause to specify the backup files operated on by the `CHANGE`, `CROSSCHECK`, and `DELETE` commands.

Syntax

maintSpec::=

![maintspec](img/maintspec.gif)

> {BACKUP \[OF listObjList\] | {archivelogRecordSpecifier | COPY \[OF listObjList\] | foreignlogRecordSpecifier}} \[ {maintQualifier}...\] | recordSpec \[DEVICE TYPE deviceSpecifier \[, deviceSpecifier\]...\]
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2025, 2026, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


([listObjList::=](listObjList.md), [maintQualifier::=](maintQualifier.md), [archivelogRecordSpecifier::=](archivelogRecordSpecifier.md), [recordSpec::=](recordSpec.md), [deviceSpecifier::=](deviceSpecifier.md))

Semantics

maintSpec

| Syntax Element | Description |
| --- | --- |
| `BACKUP` | Processes backup sets. For processing image copies, use the option `COPY`.  If you do not use the `OF` clause with `CHANGE` `BACKUP`, then RMAN changes all backup sets recorded in the repository. If you do not use the `OF` clause with `CROSSCHECK` `BACKUP`, then RMAN crosschecks backups of the whole database. If you do not use the `OF` clause with `DELETE` `BACKUP`, then RMAN deletes backups of the whole database. |
| `   OF` `listObjList` | Restricts the list of files operated on to the object type specified in the `listObjList` clause.  See Also: `listObjList` |
| `archivelogRecordSpecifier` | Processes the specified archived redo log files.  If you specify `DELETE` `ARCHIVELOG` without the `BACKED UP` clause, then RMAN uses the configured settings to determine whether an archived log can be deleted (`CONFIGURE` `ARCHIVELOG DELETION POLICY TO BACKED UP`). If you specify `DELETE ARCHIVELOG` with the `BACKED UP` clause, then RMAN uses the `DELETE` settings to determine whether an archived log can be deleted. Use `FORCE` with `DELETE ARCHIVELOG` to override a configured deletion policy and any mismatches between media and repository.  See Also: `archivelogRecordSpecifier` |
| `COPY` | Processes data file copies, control file copies, and archived redo log files.  If you do not specify an option for `CHANGE` `COPY`, then the command operates on all image copies recorded in the repository. If you are using `CROSSCHECK` `COPY`, then by default the command checks all image copies of all files in the database with status `AVAILABLE` or `EXPIRED`. If you are using `DELETE` `COPY`, then by default `COPY` removes copies of all files in the database. Specify the `EXPIRED` option to remove only copies that are marked `EXPIRED` in the repository. |
| `   OF` `listObjList` | Restricts the list of objects operated on to the object type specified in the `listObjList` clause. If you do not specify an object, then the command defaults to all copies. `CHANGE` `COPY` `OF` `DATABASE` includes data files but not control files.  See Also: `listObjList` |
| `foreignlogRecordSpecifier` | Processes the specified foreign archived redo log files.  See Also: `foreignlogRecordSpecifier` |
| `maintQualifier` | Restricts the command based on the specified options.  See Also: `maintQualifier` |
| `recordSpec` | Specifies the file that you are performing maintenance on.  If you use the `BACKUPSET` parameter in `recordSpec`, then the keys identify backup sets for use with the `CHANGE`, `CROSSCHECK` and `DELETE` commands. For more details, see " [LIST Command Output](LIST.md) " for an explanation of the column headings of the `LIST` output tables. Use the `KEY` column of the output to obtain the primary key usable in the `CHANGE` and `DELETE` commands.  See Also: `recordSpec` |
| `DEVICE TYPE` `deviceSpecifier` | Allocates automatic channels for the specified device type only. This option is valid only if you have configured automatic channels and have not manually allocated channels. For example, if you configure automatic disk and tape channels and run `CROSSCHECK...DEVICE TYPE DISK`, then RMAN allocates only disk channels.  See Also: `deviceSpecifier` |

Examples

Example 4-32 Crosschecking Backups

The following command crosschecks backups of archived redo log files:

```
RMAN> CROSSCHECK BACKUP OF ARCHIVELOG ALL;
 
allocated channel: ORA_SBT_TAPE_1
channel ORA_SBT_TAPE_1: SID=103 device type=SBT_TAPE
channel ORA_SBT_TAPE_1: Oracle Secure Backup
using channel ORA_DISK_1
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=8cic4031_1_1 RECID=195 STAMP=616693857
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=8oic41ad_1_1 RECID=198 STAMP=616695118
crosschecked backup piece: found to be 'AVAILABLE'
backup piece handle=8qic41c3_1_1 RECID=200 STAMP=616695171
Crosschecked 3 objects
```

Note:

Oracle Secure Backup (OSB) 19.1 desupport was announced on May 1, 2026 with premier support end date on September 30, 2027. See My Oracle Support note [PNEWS3035](https://support.oracle.com/support/?documentId=PNEWS3035) for more information. Please refer to [Lifetime Support Policy: Oracle Technology Products](https://www.oracle.com/support/lifetime-support/) for updated support timeframes.

Oracle recommends that database backups to cloud take advantage of Oracle Database Zero Data Loss Cloud Protect, which uses Oracle Zero Data Loss Autonomous Recovery Service in OCI. Cloud Protect offers an efficient incremental forever backup strategy, real-time transaction protection, logically air-gapped immutable backups, and fast, point-in-time recovery.

For customers who require database backups to Amazon S3, Oracle Database Cloud Backup for Amazon S3 may be used. This offering is similar to Oracle Secure Backup Cloud Module in that it is fully integrated with Recovery Manager (RMAN) and enables you to back up your Oracle database to Amazon S3. You can exchange your Oracle Secure Backup license for an Oracle Database Cloud Backup for Amazon S3 license on a 1:1 basis. See [Oracle Database Cloud Backup for Amazon S3](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/rcmrf&id=BRADV-GUID-F187E3A0-EA0E-49DA-B075-4FE7C5846A32) for more information.