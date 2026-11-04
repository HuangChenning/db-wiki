---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/validating-database-files-backups.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

Use the RMAN `VALIDATE` command to check the integrity of database files and backups.

### 16.1 Overview of RMAN Validation

Validation enables you to check the integrity of your backups.

#### 16.1.1 Purpose of RMAN Validation

The main purpose of RMAN validation is to check for corrupt blocks and missing files. You can also use RMAN to determine whether backups can be restored.

You can use the following RMAN commands to perform validation:

- `VALIDATE`
- `BACKUP ... VALIDATE`
- `RESTORE ... VALIDATE`

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF162) for `VALIDATE` syntax
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF149) for `RESTORE ... VALIDATE` syntax

#### 16.1.2 Basic Concepts of RMAN Validation

The database prevents operations that result in unusable backup files or corrupted restored data files.

The database automatically does the following:

- Blocks access to data files while they are being restored or recovered
- Permits only one restore operation for each data file at a time
- Ensures that incremental backups are applied in the correct order
- Stores information in backup files to allow detection of corruption
- Checks a block every time it is read or written in an attempt to report a corruption as soon as it has been detected

##### 16.1.2.1 About Checksums and Corrupt Blocks

A corrupt block is a block that has been changed so that it differs from what Oracle Database expects to find.

Block corruptions can be caused by several different failures including, but not limited to the following:

- Faulty disks and disk controllers
- Faulty memory
- Oracle Database software defects

`DB_BLOCK_CHECKSUM` is a database initialization parameter that controls the writing of checksums for the blocks in data files and online redo log files in the database (not backups). If `DB_BLOCK_CHECKSUM` is `typical`, then the database computes a checksum for each block during normal operations and stores it in the header of the block before writing it to disk. When the database reads the block from disk later, it recomputes the checksum and compares it to the stored value. If the values do not match, then the block is corrupt.

By default, the `BACKUP` command computes a checksum for each block and stores it in the backup. The `BACKUP` command ignores the values of `DB_BLOCK_CHECKSUM` because this initialization parameter applies to data files in the database, not backups.

##### 16.1.2.2 About Physical and Logical Block Corruption

In a physical corruption, which is also called a media corruption, the database does not recognize the block at all: the checksum is invalid, the block contains all zeros, or the header and footer of the block do not match.

Note:

By default, the `BACKUP` command computes a checksum for each block and stores it in the backup. If you specify the `NOCHECKSUM` option, then RMAN does not perform a checksum of the blocks when creating the backup.

In a [logical corruption](glossary.md), the contents of the block are logically inconsistent. Examples of logical corruption include corruption of a row piece or index entry. If RMAN detects logical corruption, then it logs the block in the alert log and server session trace file.

By default, RMAN does not check for logical corruption. If you specify `CHECK LOGICAL` on the `BACKUP` command, however, then RMAN tests data and index blocks for logical corruption, such as corruption of a row piece or index entry, and log them in the alert log located in the [Automatic Diagnostic Repository (ADR)](glossary.md). If you use RMAN with the following configuration when backing up or restoring files, then it detects all types of block corruption that are possible to detect:

- In the initialization parameter file of a database, set `DB_BLOCK_CHECKSUM=typical` so that the database calculates data file checksums automatically (not for backups, but for data files in use by the database)
- Do not precede the `BACKUP` command with `SET MAXCORRUPT` so that RMAN does not tolerate any unmarked block corruptions.
- In a `BACKUP` command, do not specify the `NOCHECKSUM` option so that RMAN calculates a checksum when writing backups
- In `BACKUP` and `RESTORE` commands, specify the `CHECK` `LOGICAL` option so that RMAN checks for logical and physical corruption

##### 16.1.2.3 About Limits for Corrupt Blocks in RMAN Backups

You can use the `SET MAXCORRUPT` command to set the total number of unmarked corruptions permitted in a file for RMAN backups. The default is zero, meaning that RMAN does not tolerate unmarked corrupt blocks of any kind.

If the `MAXCORRUPT` limit is exceeded when RMAN encounters an unmarked corrupt block during a backup, then RMAN terminates the backup. Otherwise, RMAN writes the newly detected corrupt block to the backup with a special header indicating that the block is marked corrupt. You can use the `VALIDATE` command to determine which blocks are marked as corrupt and to find any unmarked corrupt blocks.

Because RMAN allows marked corrupt blocks in a backup, and because RMAN can be instructed to allow unmarked corrupt blocks to be marked as corrupt in the backup (when `MAXCORRUPT` is used), it is possible to restore a data file that has several blocks marked as corrupt. If you backup this restored data file (assuming no new corruptions have happened), even without `MAXCORRUPT` setting, the backup succeeds. This is because the previously marked corruptions do not stop RMAN from completing the backup.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF153) for `SET MAXCORRUPT` syntax

##### 16.1.2.4 About Detecting Block Corruption

Oracle Database supports different techniques for detecting, repairing, and monitoring block corruption.

The technique depends on whether the corruption is [interblock corruption](glossary.md) or [intrablock corruption](glossary.md). In intrablock corruption, the corruption occurs within the block itself. This corruption can be either physical or logical. In an interblock corruption, the corruption occurs between blocks and can only be logical.

For example, the [`V$DATABASE_BLOCK_CORRUPTION`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=REFRN30048) view records intrablock corruptions, while the [Automatic Diagnostic Repository (ADR)](glossary.md) tracks all types of corruptions. Table 16-1 summarizes how the database treats different types of block corruption.

Table 16-1 Detection, Repair, and Monitoring of Block Corruption

| Response | Intrablock Corruption | Interblock Corruption |
| --- | --- | --- |
| Detection | All database utilities detect intrablock corruption, including RMAN (for example, the `BACKUP` command) and the DBVERIFY utility. If a database process can encounter the `ORA-1578` error, then it can detect the corruption and monitor it. | Only DBVERIFY and the `ANALYZE` statement detect interblock corruption. |
| Tracking | The `V$DATABASE_BLOCK_CORRUPTION` view displays blocks marked corrupt by Oracle Database components such as RMAN commands, `ANALYZE`, SQL queries, and so on. Any process that encounters an intrablock corruption records the block corruption in this view and in ADR. | The database monitors this type of block corruption in ADR. |
| Repair | Repair techniques include [block media recovery](glossary.md), restoring data files, recovering with incremental backups, and block newing. Block media recovery can repair physical corruptions.  However, block media recovery may not be able to repair all logical block corruptions. In these cases, alternate recovery methods, such as tablespace point-in-time recovery, or dropping and re-creating the affected objects, may repair the corruption.  Any RMAN command that fixes or detects that a block is repaired updates `V$DATABASE_BLOCK_CORRUPTION`. For example, RMAN updates the repository at end of successful block media recovery. If a `BACKUP`, `RESTORE`, or `VALIDATE` command detects that a block is no longer corrupted, then it removes the repaired block from the view. | You must fix interblock corruption using manual techniques such as dropping an object, rebuilding an index, and so on. |

See Also:

- [Performing Complete Database Recovery](rman-complete-database-recovery.md)
- [Performing Block Media Recovery](rman-block-media-recovery.md)
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN11257) to learn about ADR

### 16.2 Checking for Block Corruption with the VALIDATE Command

You can use the `VALIDATE` command to manually check for physical and logical corruptions in database files.

This command performs the same types of checks as `BACKUP VALIDATE`, but `VALIDATE` can check a larger selection of objects. For example, you can validate individual blocks with the `VALIDATE DATAFILE ... BLOCK` command.

To specify a copy number for the backup piece being validated, run the `VALIDATE FROM COPY NUMBER` command.

When validating whole files, RMAN checks every block of the input files. If the backup validation discovers previously unmarked corrupt blocks, then RMAN updates the `V$DATABASE_BLOCK_CORRUPTION` view with rows describing the corruptions.

Use `VALIDATE BACKUPSET` when you suspect that one or more backup pieces in a backup set are missing or have been damaged. This command checks every block in a backup set to ensure that the backup can be restored. If RMAN finds block corruption, then it issues an error and terminates the validation. The command `VALIDATE BACKUPSET` enables you to choose which backups to check, whereas the `VALIDATE` option of the `RESTORE` command lets RMAN choose.

To use VALIDATE to check database files and backups:

1. Start RMAN and connect to the root of the target database as a common user with the `SYSBACKUP` or `SYSDBA` privilege, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
2. Execute the `VALIDATE` command with the desired options.
	For example, to validate all data files and control files (and the server parameter file if one is in use) in the database, execute the following command at the RMAN prompt:
	```
	RMAN> VALIDATE DATABASE;
	```
	Alternatively, you can validate a particular backup set by using the form of the command shown in the following example (sample output included).
	```
	RMAN> VALIDATE BACKUPSET 22;
	Starting validate at 17-AUG-13
	using channel ORA_DISK_1
	allocated channel: ORA_SBT_TAPE_1
	channel ORA_SBT_TAPE_1: SID=89 device type=SBT_TAPE
	channel ORA_SBT_TAPE_1: Oracle Secure Backup
	channel ORA_DISK_1: starting validation of datafile backup set
	channel ORA_DISK_1: reading from backup piece
	/disk1/oracle/work/orcva/RDBMS/backupset/2013_08_16/o1_mf_nnndf_
	TAG20130816T153034_2g774bt2_.bkp
	channel ORA_DISK_1: piece
	handle=/disk1/oracle/work/orcva/RDBMS/backupset/2013_08_16/o1_mf_nnndf_
	TAG20130816T153034_2g774bt2_.bkp tag=TAG20130816T153034
	channel ORA_DISK_1: restored backup piece 1
	channel ORA_DISK_1: validation complete, elapsed time: 00:00:01
	Finished validate at 17-AUG-13
	```
	The following example illustrates how you can check individual data blocks within a data file for corruption.
	```
	RMAN> VALIDATE DATAFILE 1 BLOCK 10;
	 
	Starting validate at 17-AUG-13
	using channel ORA_DISK_1
	channel ORA_DISK_1: starting validation of datafile
	channel ORA_DISK_1: specifying datafile(s) for validation
	input datafile file number=00001 name=/disk1/oracle/dbs/tbs_01.f
	channel ORA_DISK_1: validation complete, elapsed time: 00:00:01
	List of Datafiles
	=================
	File Status Marked Corrupt Empty Blocks Blocks Examined High SCN
	---- ------ -------------- ------------ --------------- ----------
	1    OK     0              2            127             481907
	  File Name: /disk1/oracle/dbs/tbs_01.f
	  Block Type Blocks Failing Blocks Processed
	  ---------- -------------- ----------------
	  Data       0              36
	  Index      0              31
	  Other      0              58
	Finished validate at 17-AUG-13
	```

Make Parallel the Validation of a Data File

If you must validate a large data file, then RMAN can make the work parallel by dividing the file into sections and processing each [file section](glossary.md) in parallel. If multiple channels are configured or allocated, and if you want the channels to make parallel the validation, then specify the `SECTION SIZE` parameter of the `VALIDATE` command.

If you specify a section size that is larger than the size of the file, then RMAN does not create file sections. If you specify a small section size that would produce more than 256 sections, then RMAN increases the section size to a value that results in exactly 256 sections.

To make parallel the validation of a data file:

1. Start RMAN and connect to the root of the target database as a common user with the `SYSBACKUP` or `SYSDBA` privilege. The target database must be mounted or open.
2. Run `VALIDATE` with the `SECTION SIZE` parameter.
	The following example allocates two channels and validates a large data file. The section size is 1200 MB.
	```
	RUN
	{
	  ALLOCATE CHANNEL c1 DEVICE TYPE DISK;
	  ALLOCATE CHANNEL c2 DEVICE TYPE DISK;
	  VALIDATE DATAFILE 1 SECTION SIZE 1200M;
	}
	```

See Also:

- [Dividing the Backup of a Large Data File into Sections](backing-up-database-advanced.md)
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF162) to learn about the `VALIDATE` command

#### 16.2.1 Validating PDBs

There are multiple methods to validate PDBs.

Use one of the following techniques to validate PDBs:

- Connect to the root and use the `VALIDATE PLUGGABLE DATABASE` or `RESTORE PLUGGABLE DATABASE VALIDATE` command. This enables you to validate one or more PDBs.
	The following command, when connected to the root, validates the PDBs `hr_pdb` and `sales_pdb`.
	```
	VALIDATE PLUGGABLE DATABASE hr_pdb, sales_pdb;
	```
- Connect to the PDB and use the `VALIDATE DATABASE` and `RESTORE                             DATABASE VALIDATE` commands to validate only one PDB. The commands used here are the same commands that you would use for a whole database.
	The following command, when connected to a PDB, validates the restore of the database.
	```
	RESTORE DATABASE VALIDATE;
	```

See Also:

" [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) "

### 16.3 Validating Database Files with BACKUP VALIDATE

You can also use the `BACKUP VALIDATE` command to perform validation.

This command can perform the following tasks:

- Check data files for physical and logical block corruption
- Confirm that all database files exist and are in the correct locations

When you run `BACKUP VALIDATE`, RMAN reads the files to be backed up in their entirety, as it does during a real backup. RMAN does not, however, actually produce any backup sets or image copies.

You cannot use the `BACKUPSET`, `MAXCORRUPT`, or `PROXY` parameters with `BACKUP VALIDATE`. To validate specific backup sets, run the `VALIDATE` command.

To validate files with the BACKUP VALIDATE command:

1. Start RMAN and connect to a target database and recovery catalog (if used).
2. Run the `BACKUP VALIDATE` command.
	For example, you can validate that all database files and archived logs can be backed up by running a command as shown in the following example. This command checks for physical corruptions only.
	```
	BACKUP VALIDATE 
	  DATABASE 
	  ARCHIVELOG ALL;
	```
	To check for logical corruptions in addition to physical corruptions, run the following variation of the preceding command:
	```
	BACKUP VALIDATE 
	  CHECK LOGICAL 
	  DATABASE 
	  ARCHIVELOG ALL;
	```
	In the preceding examples, the RMAN client displays the same output as when really backing up the files. If RMAN cannot back up one or more of the files, then it issues an error message. For example, RMAN may show output similar to the following:
	```
	RMAN-00571: ===========================================================
	RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============
	RMAN-00571: ===========================================================
	RMAN-03002: failure of backup command at 08/29/2013 14:33:47
	ORA-19625: error identifying file /oracle/oradata/trgt/arch/archive1_6.dbf
	ORA-27037: unable to obtain file status
	SVR4 Error: 2: No such file or directory
	Additional information: 3
	```

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) for `BACKUP` syntax
- [Performing Block Media Recovery](rman-block-media-recovery.md) to learn how to repair corrupt blocks discovered by `BACKUP` `VALIDATE`

### 16.4 Validating Backups Before Restoring Them

You can run `RESTORE...VALIDATE` to test whether RMAN can restore a specific file or set of files from a backup. RMAN chooses which backups to use.

The database must be mounted or open for this command. You do not have to take data files offline when validating the restore of data files, because validation of backups of the data files only reads the backups and does not affect the production data files.

When validating files on disk or tape, RMAN reads all blocks in the backup piece or image copy. RMAN also validates offsite backups. The validation is identical to a real restore operation except that RMAN does not write output files.

RMAN also allows to specify a copy number for the backup pieces being validated.

Note:

As an additional test measure, you can perform a [trial recovery](glossary.md) with the `RECOVER ... TEST` command. A trial recovery applies redo in a way similar to normal recovery, but it is in memory only and it rolls back its changes after the trial.

To validate backups with the RESTORE command:

1. Start RMAN and connect to the root of the target database as a common user with the `SYSBACKUP` or `SYSDBA` privilege, as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".
2. Run the `RESTORE` command with the `VALIDATE` option.
	This following example illustrates validating the restore of the database and all archived redo logs:
	```
	RESTORE DATABASE VALIDATE;
	RESTORE ARCHIVELOG ALL VALIDATE;
	```
	If you do not see an RMAN error stack, then skip the subsequent steps. The lack of error messages means that RMAN had confirmed that it can use these backups successfully during a real restore and recovery.
3. If you see error messages in the output and the `RMAN-06026` message, then investigate the cause of the problem. If possible, correct the problem that is preventing RMAN from validating the backups and retry the validation.
	The following error means that RMAN cannot restore one or more of the specified files from your available backups:
	```
	RMAN-06026: some targets not found - aborting restore
	```
	The following sample output shows that RMAN encountered a problem reading the specified backup:
	```
	RMAN-03009: failure of restore command on c1 channel at 12-DEC-12 23:22:30
	ORA-19505: failed to identify file "oracle/dbs/1fafv9gl_1_1"
	ORA-27037: unable to obtain file status
	SVR4 Error: 2: No such file or directory
	Additional information: 3
	```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF149) to learn about the `RESTORE...VALIDATE` command