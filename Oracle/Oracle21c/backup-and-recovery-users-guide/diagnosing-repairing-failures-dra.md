---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/diagnosing-repairing-failures-dra.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

### 15.1 Overview of Data Recovery Advisor

The Data Recovery Advisor is a tool that helps reduce database recovery time by determining the best automated repair option for database failures.

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

#### 15.1.1 Purpose of Data Recovery Advisor

Data Recovery Advisor is an Oracle Database tool that automatically diagnoses data failures, determines and presents appropriate repair options, and executes repairs at the user's request.

In this context, a data failure is a corruption or loss of persistent data on disk. By providing a centralized tool for automated data repair, Data Recovery Advisor improves the manageability and reliability of an Oracle database and thus helps reduce the [MTTR](glossary.md).

Diagnosing a data failure and devising an optimal strategy for repair requires a high degree of training and experience. Data Recovery Advisor provides the following advantages over traditional repair techniques:

- Data Recovery Advisor can potentially detect, analyze, and repair data failures before a database process discovers the corruption and signals an error. Early warnings help limit damage caused by corruption.
- Manually assessing symptoms of data failures and correlating them into a problem statement can be complex, error-prone, and time-consuming. Data Recovery Advisor automatically diagnoses failures, assesses their impact, and reports these findings to the user.
- Traditionally, users must manually determine repair options along with the repair impact. If multiple failures are present, then users must determine the right sequence of repair execution and try to consolidate repairs. In contrast, Data Recovery Advisor automatically determines the best repair options and runs checks to ensure that these options are feasible in your environment.
- Execution of a data repair can be complex and error-prone. If you choose an automated repair option, then Data Recovery Advisor executes the repair and verifies its success.

#### 15.1.2 Basic Concepts of Data Recovery Advisor

You must familiarize yourself with a few concepts before using the Data Recovery Advisor.

A failure is detected either automatically by the database or through a manual check such as the `VALIDATE` command. You can use the `LIST                 FAILURE` command to view problem statements for failures and the effect of these failures on database operations. Each failure is uniquely identified by a failure number. In the same RMAN session, you can then use the `ADVISE FAILURE` command to view repair options, which typically include both automated and manual options.

After executing `ADVISE FAILURE`, you can either repair failures manually or run the `REPAIR FAILURE` command to repair the failures automatically. A repair is an action that fixes one or more failures. Examples of repairs include block media recovery, data file media recovery, and Oracle Flashback Database. When you choose an automated repair option, Data Recovery Advisor verifies the repair success and closes the relevant repaired failures.

Note:

Data Recovery Advisor can only be used to diagnose and repair data corruptions in a multitenant container database (CDB). You cannot diagnose data failures and execute repairs for individual pluggable databases (PDBs) within a CDB.

Note:

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

##### 15.1.2.1 User Interfaces to Data Recovery Advisor

Data Recovery Advisor has both a command-line and GUI interface. The GUI interface is available in Oracle Enterprise Manager Cloud Control.

In the RMAN command-line interface, the Data Recovery Advisor commands are `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR FAILURE`, and `CHANGE FAILURE`.

##### 15.1.2.2 About Data Integrity Checks

A checker is a diagnostic operation or procedure registered with the Health Monitor to assess the health of the database or its components.

The health assessment is known as a [data integrity check](glossary.md) and can be invoked reactively or proactively.

Failures are normally detected reactively. A database operation involving corrupted data results in an error, which automatically invokes a data integrity check that searches the database for failures related to the error. If failures are diagnosed, then they are recorded in the [Automatic Diagnostic Repository (ADR)](glossary.md), which is a directory structure stored outside of the database. You can use Data Recovery Advisor to generate repair advice and repair failures only after failures have been detected by the database and stored in ADR.

You can also invoke a data integrity check proactively. You can execute the check through the Health Monitor, which detects and stores failures in the same way as when the checks are invoked reactively. You can also check for block corruption with the `VALIDATE` and `BACKUP VALIDATE` commands, as explained in " Checking for Block Corruptions by Validating the Database ".

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN11269) to learn how to use the Health Monitor

##### 15.1.2.3 About Failures

A failure is a persistent data corruption that is detected by a data integrity check.

A failure can manifest itself as observable symptoms such as error messages and alerts, but a failure is different from a symptom because it represents a diagnosed [problem](glossary.md). After a problem is diagnosed by the database as a failure, you can obtain information about the failure and potentially repair it with Data Recovery Advisor.

Because failure information is not stored in the database itself, the database does not need to be open or mounted for you to access it. You can view failures when the database is started in `NOMOUNT` mode. Thus, the availability of the control file and [recovery catalog](glossary.md) does not affect the ability to view detected failures, although it may affect the feasibility of some repairs.

Data Recovery Advisor can diagnose failures such as the following:

- Components such as data files and control files that are not accessible because they do not exist, do not have the correct access permissions, have been taken offline, and so on
- Physical corruptions such as block checksum failures and invalid block header field values
- Inconsistencies such as a data file that is older than other database files
- I/O failures such as hardware errors, operating system driver failures, and exceeding operating system resource limits (for example, the number of open files)

The Data Recovery Advisor may detect or handle some logical corruptions. In general, corruptions of this type require help from Oracle Support Services.

Note:

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

See Also:

###### 15.1.2.3.1 About the Failure Status

Every failure has a failure status: `OPEN` or `CLOSED`.

The status of a failure is `OPEN` until the appropriate repair action is invoked. The status changes to `CLOSED` after the failure is repaired.

Every time you execute `LIST FAILURE`, Data Recovery Advisor revalidates all open failures and closes failures that no longer exist. Thus, if you fixed some failures as part of a separate procedure, or if the failures were transient problems that disappeared by themselves, running `LIST FAILURE` automatically closes them.

You can use `CHANGE FAILURE` to change the status of an open failure to `CLOSED` if you have fixed it manually. However, it makes sense to use `CHANGE FAILURE ... CLOSED` only if for some reason the failure was not closed automatically. If a failure still exists when you use `CHANGE` to close it manually, then Data Recover Advisor re-creates it with a different failure ID when the appropriate data integrity check is executed.

###### 15.1.2.3.2 About Failure Priority

Every failure has a failure priority: `CRITICAL`, `HIGH`, or `LOW`. Data Recovery Advisor only assigns `CRITICAL` or `HIGH` priority to diagnosed failures.

Failures with `CRITICAL` priority require immediate attention because they make the whole database unavailable. For example, a disk containing a current control file may fail. Failures with `HIGH` priority make a database partly unavailable or unrecoverable and usually have to be repaired quickly. Examples include block corruptions and missing archived redo logs.

If a failure was assigned a `HIGH` priority, but the failure has little impact on database availability and recoverability, then you can downgrade the priority to `LOW`. A `LOW` priority indicates that a failure can be ignored until more important failures are fixed.

By default `LIST FAILURE` displays only failures with `CRITICAL` and `HIGH` priority. You can use the `CHANGE` command to change the status for `LOW` and `HIGH` failures, but you cannot change the status of `CRITICAL` failures. The main reason for changing a priority to `LOW` is to reduce the `LIST FAILURE` output. If a failure cannot be revalidated at this time (for example, because of another failure), then `LIST FAILURE` shows the failure as open.

###### 15.1.2.3.3 About Failure Grouping

For clarity, Data Recovery Advisor groups related failures together.

For example, if 20 different blocks in a file are corrupted, then these failures are grouped under a single parent failure. By default, Data Recovery Advisor lists information about the group of failures, although you can specify the `DETAIL` option to list information about the individual subfailures.

A subfailure has the same format as a failure. You can get advice on a subfailure and repair it separately or in combination with any other failure.

##### 15.1.2.4 About Manual Actions and Automatic Repair Options

The `ADVISE FAILURE` command can present both manual and automatic repair options. Data Recovery Advisor categorizes manual actions as either mandatory or optional.

In some cases, the only possible actions are manual. Suppose that no backups exist for a lost control file. In this case, the manual action is to execute the `CREATE CONTROLFILE` statement. Data Recovery Advisor presents this manual action as mandatory because no automatic repair is available. In contrast, suppose that RMAN backups exist for a missing data file. In this case, the `REPAIR FAILURE` command can perform the repair automatically by restoring and recovering the data file. An optional manual action is to restore the data file if it was unintentionally renamed or moved. Data Recovery Advisor suggests optional manual actions if they might prevent a more extreme form of repair such as data file restore and recovery.

In contrast to manual actions, automated repairs can be performed by Data Recovery Advisor. The `ADVISE FAILURE` command presents an option ID for each automated repair option and summarizes the action.

Data Recovery Advisor performs feasibility checks before recommending an automated repair. For example, Data Recovery Advisor checks that all backups and archived redo logs needed for media recovery are present and consistent. Data Recovery Advisor may need specific backups and archived redo logs. If the files needed for recovery are not available, then recovery is not possible.

Note:

For performance reasons, Data Recovery Advisor does not exhaustively check every byte in every file. Thus, a feasible repair may still fail because of a corrupted backup or archived redo log file.

Note:

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

###### 15.1.2.4.1 About Consolidated Repairs

When possible, Data Recovery Advisor consolidates repairs to fix multiple failures into a single repair. A consolidated repair may contain multiple steps.

Sometimes a consolidated repair is not possible, as when one failure prevents the creation of repairs for other failures. For example, the feasibility of a data file repair cannot be determined when the control file is missing. In such cases, Data Recovery Advisor generates a repair option for failures that can be repaired and prints a message stating that some selected failures cannot be repaired at this time. After executing the proposed repair, you can repeat the `LIST`, `ADVISE`, and `REPAIR` sequence to repair remaining failures.

###### 15.1.2.4.2 About Repair Scripts

Whenever Data Recovery Advisor generates an automated repair option, it creates a script that explains which commands RMAN intends to use to repair the failure. Data Recovery Advisor prints the location of this script, which is a text file residing on the operating system.

Example 15-1 shows a sample repair script, which shows how Data Recovery Advisor plans to repair the loss of data file `27`.

Example 15-1 Sample Repair Script

```
# restore and recover data file
ALTER DATABASE DATAFILE 27 OFFLINE;
restore datafile 27;
recover datafile 27;
ALTER DATABASE DATAFILE 27 ONLINE;
```

If you do not want Data Recovery Advisor to automatically repair the failure, then you can copy the script, edit it, and execute it manually.

##### 15.1.2.5 About Supported Database Configurations for Data Recovery Advisor

Data Recovery Advisor is supported only on some database configurations.

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

###### 15.1.2.5.1 About Data Recovery Advisor and Oracle Real Application Clusters

Data Recovery Advisor only supports single-instance databases. Oracle Real Application Clusters (Oracle RAC) databases are not supported.

If a data failure occurs that brings down all Oracle RAC instances, then you can mount the database in single-instance mode and use Data Recovery Advisor to detect and repair control file, `SYSTEM` data file, and data dictionary failures. You can also invoke data recovery checks proactively to test other database components for data failures. This approach does not detect data failures that are local to other cluster instances, for example, an inaccessible data file.

###### 15.1.2.5.2 About Data Recovery Advisor and Oracle Data Guard

There are some limitations with Data Recovery Advisor in an Oracle Data Guard environment.

In a Data Guard environment, Data Recovery Advisor cannot do the following:

- Use files transferred from a [physical standby database](glossary.md) to repair failures on a primary database
- Diagnose and repair failures on a standby database

However, if the primary database is unavailable, then Data Recovery Advisor may recommend a failover to a standby database. After the failover you can repair the old primary database. If you are using Enterprise Manager Cloud Control in a Data Guard configuration, then you can initiate a failover through the Data Recovery Advisor recommendations page.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SBYDB04700) to learn how to use RMAN in a Data Guard configuration

### 15.2 Basic Steps of Diagnosing and Repairing Failures

The Data Recovery Advisor workflow begins when you either suspect or discover a failure. You can discover failures in many ways, including error messages, alerts, trace files, and failed data integrity checks.

The database can automatically diagnose failures when errors occur. To respond to failures, start an RMAN session and perform all of the following steps in the same session and in the order they are listed:

1. List failures by running the `LIST FAILURE` command.
	This task is explained in " Listing Failures ".
2. If you suspect that failures exist that have not been automatically diagnosed by the database, then run `VALIDATE DATABASE` to check for corrupt blocks and missing files.
	If `VALIDATE` detects a problem, then RMAN triggers execution of a failure assessment. If a failure is detected, then RMAN logs it into the Automated Diagnostic Repository, where is can be accessed by Data Recovery Advisor.
	This task is explained in " Checking for Block Corruptions by Validating the Database ".
3. Determine repair options by running the `ADVISE FAILURE` command.
	This task is explained in " Determining Repair Options ".
4. Choose a repair option. You can repair the failures manually or run the `REPAIR FAILURE` command to fix them automatically.
	This task is explained in " Repairing Failures ".
5. Return to the first step to confirm that all failures were repaired or determine which failures remain.

Performing the steps for diagnosing and repairing failures in an order that is different from the one listed in this section may result in errors.

If appropriate, you can use `CHANGE FAILURE` command at any time in the Data Recovery Advisor workflow to change the priority of a failure from `LOW` to `HIGH` or `HIGH` to `LOW`, or close a failure that has been fixed manually.

See Also:

- Changing Failure Status and Priority for information about changing failure status
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF90269) for a complete example on recovering a database using the Data Recovery Advisor

Note:

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

### 15.3 Listing Failures

Use the `LIST FAILURE` command to obtain information about failures, if you suspect or know that one or more database failures have occurred.

You can list all or a subset of failures and restrict output in various ways. Failures are uniquely identified by failure numbers. These numbers are not consecutive, so gaps between failure numbers have no significance.

The `LIST FAILURE` command does not execute data integrity checks to diagnose new failures; rather, it lists the results of previously executed assessments. Thus, repeatedly executing `LIST FAILURE` reveals new failures only if the database automatically diagnosed them in response to errors that occurred in between command executions. However, executing `LIST FAILURE` causes Data Recovery Advisor to revalidate all existing failures. If a user fixed failures manually, or if transient failures disappeared, then Data Recovery Advisor removes these failures from the `LIST FAILURE` output. If a failure cannot be revalidated at this moment (for example, because of another failure), `LIST FAILURE` shows the failure as open.

Note:

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

#### 15.3.1 Listing All Failures

The easiest way to determine problems that your database is encountering is to use the `LIST FAILURE` command.

To list all failures:

1. Start RMAN and connect to the root of the target database as a user with the `SYSDBA` or `SYSBACKUP` privilege. The target database instance must be started.
2. Execute the `LIST FAILURE` command.
	The following example reports all failures known to Data Recovery Advisor (the output has been reformatted to fit on the page).
	```
	RMAN> LIST FAILURE;
	List of Database Failures
	=========================
	 
	Failure ID Priority Status    Time Detected Summary
	---------- -------- --------- ------------- -------
	142        HIGH     OPEN      23-APR-13     One or more non-system datafiles are missing
	101        HIGH     OPEN      23-APR-13     Datafile 1: '/disk1/oradata/prod/system01.dbf' contains one or more corrupt blocks
	```
	In this example, RMAN reports two different failures: a group of missing data files and a data file with corrupt blocks. The output indicates the unique identifier for each failure (142 and 101), the priority, status, and detection time.
3. Optionally, execute `LIST FAILURE ... DETAIL` to list failures individually.
	Data Recovery Advisor consolidates failures when possible. Specify the `DETAIL` option to list failures individually. For example, if multiple block corruptions exist in a file, then specifying the `DETAIL` option lists each of the block corruptions. The following example lists detailed information about failure 101.
	```
	RMAN> LIST FAILURE 101 DETAIL;
	List of Database Failures
	=========================
	 
	Failure ID Priority Status    Time Detected Summary
	---------- -------- --------- ------------- -------
	101        HIGH     OPEN      23-APR-13     Datafile 1: '/disk1/oradata/prod/system01.dbf' contains one or more corrupt blocks
	  List of child failures for parent failure ID 101
	  Failure ID Priority Status    Time Detected Summary
	  ---------- -------- --------- ------------- -------
	  104        HIGH     OPEN      23-APR-13     Block 56416 in datafile 1: '/disk1/oradata/prod/system01.dbf' is media corrupt
	    Impact: Object BLKTEST owned by SYS might be unavailable
	```
4. Proceed to determine how to repair the failures displayed by the `LIST FAILURE` command as described in " Determining Repair Options ".

#### 15.3.2 Listing a Subset of Failures

Besides providing more verbose output, `LIST FAILURE` also enables you to restrict output.

For example, you can execute `LIST FAILURE` with the `CRITICAL`, `HIGH`, `LOW`, or `CLOSED` options to list only failures with a particular status or priority. You can also exclude specified failures from the output by specifying `EXCLUDE FAILURE`.

To list a subset of failures:

1. Start RMAN and connect to the root of the target database as a user with the `SYSDBA` or `SYSBACKUP` privilege. The target database instance must be started.
2. Execute `LIST FAILURE` with the desired options.
	The following examples illustrate some `LIST FAILURE` commands:
	```
	LIST FAILURE LOW;
	LIST FAILURE CLOSED;
	LIST FAILURE EXCLUDE FAILURE 234234;
	```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF132) to learn about the `LIST FAILURE` command

### 15.4 Checking for Block Corruptions by Validating the Database

The database invokes data integrity checks reactively when a user transaction is trying to access corrupted data. In some cases, latent failures can go undetected.

For example, when a data block corruption error occurs, the database reactively execute a data integrity check that validates the block on which the error occurred and other blocks in its immediate vicinity. However, blocks outside of the vicinity may be corrupted. Also, corrupted blocks that are never read by the database are never detected by a reactive data integrity check.

One effective way to execute a data integrity check proactively is to run the `VALIDATE` or `BACKUP VALIDATE` commands in RMAN. These commands can check data files and control files for physical and logical corruption. If RMAN discovers block corruptions, then it logs them into the Automatic Diagnostic Repository and creates one or more failures. You can then use Data Recovery Advisor to list information about the failures and repair them.

To validate the database:

1. Start RMAN and connect to a target database. The target database must be mounted.
2. The following example uses `VALIDATE DATABASE` to check for physical and logical corruption in the whole database (partial sample output included). Because " Listing Failures " indicates that some data files are missing, the `SKIP INACCESSIBLE` clause is specified. The output shows that the `system01.dbf` database file has one newly corrupt block (Blocks Failing) and no blocks previously marked corrupt by the database (Marked Corrupt).
	```
	RMAN> VALIDATE CHECK LOGICAL SKIP INACCESSIBLE DATABASE;
	 
	Starting validate at 23-APR-13
	allocated channel: ORA_DISK_1
	channel ORA_DISK_1: SID=103 device type=DISK
	could not access datafile 28
	skipping inaccessible file 28
	RMAN-06060: WARNING: skipping datafile compromises tablespace USERS recoverability
	RMAN-06060: WARNING: skipping datafile compromises tablespace USERS recoverability
	channel ORA_DISK_1: starting validation of datafile
	channel ORA_DISK_1: specifying datafile(s) for validation
	input datafile file number=00001 name=/disk1/oradata/prod/system01.dbf
	input datafile file number=00002 name=/disk1/oradata/prod/sysaux01.dbf
	input datafile file number=00022 name=/disk1/oradata/prod/undotbs01.dbf
	input datafile file number=00023 name=/disk1/oradata/prod/cwmlite01.dbf
	input datafile file number=00024 name=/disk1/oradata/prod/drsys01.dbf
	input datafile file number=00025 name=/disk1/oradata/prod/example01.dbf
	input datafile file number=00026 name=/disk1/oradata/prod/indx01.dbf
	input datafile file number=00027 name=/disk1/oradata/prod/tools01.dbf
	channel ORA_DISK_1: validation complete, elapsed time: 00:00:25
	List of Datafiles
	=================
	File Status Marked Corrupt Empty Blocks Blocks Examined High SCN
	---- ------ -------------- ------------ --------------- ----------
	1    FAILED 0              3536         57600           637711
	  File Name: /disk1/oradata/prod/system01.dbf
	  Block Type Blocks Failing Blocks Processed
	  ---------- -------------- ----------------
	  Data       1              41876
	  Index      0              7721
	  Other      0              4467
	.
	.
	. 
	File Status Marked Corrupt Empty Blocks Blocks Examined High SCN
	---- ------ -------------- ------------ --------------- ----------
	27   OK     0              1272         1280            400914
	  File Name: /disk1/oradata/prod/tools01.dbf
	  Block Type Blocks Failing Blocks Processed
	  ---------- -------------- ----------------
	  Data       0              0
	  Index      0              0
	  Other      0              8
	validate found one or more corrupt blocks
	See trace file /disk1/oracle/log/diag/rdbms/prod/prod/trace/prod_ora_2596.trc
	 for details
	channel ORA_DISK_1: starting validation of datafile
	channel ORA_DISK_1: specifying datafile(s) for validation
	including current control file for validation
	including current SPFILE in backup set
	channel ORA_DISK_1: validation complete, elapsed time: 00:00:01
	List of Control File and SPFILE
	===============================
	File Type    Status Blocks Failing Blocks Examined
	------------ ------ -------------- ---------------
	SPFILE       OK     0              2
	Control File OK     0              512
	Finished validate at 23-APR-13
	```

See Also:

- About Data Integrity Checks
- [Validating Database Files and Backups](validating-database-files-backups.md)
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF162) to learn about the `VALIDATE` command
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN11007) to learn about how Oracle Database manages diagnostic data

### 15.5 Determining Repair Options

Use the `ADVISE FAILURE` command to display repair options after running `LIST FAILURE` in an RMAN session. This command prints a summary of the failures and implicitly closes all open failures that are repaired.

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

Where appropriate, the `ADVISE FAILURE` command presents a list of manual and automated repair options. Manual options, which are categorized as either mandatory or optional, appear first. In some cases, an optional manual fix can avoid more extreme actions such as restoring and recovering data files. As a rule, use the repair technique that has the least effect on the database and the least possibility for error.

See Also:

- Determining Repair Options for All Failures
- Determining Repair Options for a Subset of Failures

#### 15.5.1 Determining Repair Options for All Failures

If one or more failures exist, then you typically use `LIST FAILURE` to show information about the failures and then `ADVISE FAILURE` in the same RMAN session to obtain a report of your repair options.

To determine repair options for all failures:

1. List failures as described in " Listing All Failures ".
2. In the same RMAN session, execute `ADVISE FAILURE`.
	The following example requests repair options for all failures known to Data Recovery Advisor and includes sample output (reformatted to fit the page).
	```
	RMAN> ADVISE FAILURE;
	 
	List of Database Failures
	=========================
	 
	Failure ID Priority Status    Time Detected Summary
	---------- -------- --------- ------------- -------
	142        HIGH     OPEN      23-APR-13     One or more non-system datafiles 
	                                            are missing
	101        HIGH     OPEN      23-APR-13     Datafile 1: '/disk1/oradata/prod/system01.dbf' contains one or more corrupt blocks
	 
	analyzing automatic repair options; this may take some time
	using channel ORA_DISK_1
	analyzing automatic repair options complete
	 
	Mandatory Manual Actions
	========================
	no manual actions available
	 
	Optional Manual Actions
	=======================
	1. If file /disk1/oradata/prod/users01.dbf was unintentionally renamed or moved, restore it
	 
	Automated Repair Options
	========================
	Option Repair Description
	------ ------------------
	1      Restore and recover datafile 28; Perform block media recovery of 
	       block 56416 in file 1
	  Strategy: The repair includes complete media recovery with no data loss
	  Repair script: /disk1/oracle/log/diag/rdbms/prod/prod/hm/reco_660500184.hm
	```
	In the preceding example, `ADVISE FAILURE` reports two failures: a missing data file and a data file with corrupt blocks. The command does not list mandatory manual actions, but it suggests making sure that the missing data file was not accidentally renamed or removed. The automated repair option involves [block media recovery](glossary.md) and restoring and recovering the missing data file. `ADVISE FAILURE` lists the location of the repair script.
	The following variation of the same example shows the output when the RMAN backups or archived redo logs needed for the automated repair are not available. The command `ADVISE FAILURE` now shows mandatory manual actions.
	```
	RMAN> ADVISE FAILURE;
	 
	List of Database Failures
	=========================
	 
	Failure ID Priority Status    Time Detected Summary
	---------- -------- --------- ------------- -------
	142        HIGH     OPEN      23-APR-13     One or more non-system datafiles 
	                                            are missing
	101        HIGH     OPEN      23-APR-13     Datafile 1:
	 '/disk1/oradata/prod/system01.dbf' contains one or more corrupt blocks
	 
	analyzing automatic repair options; this may take some time
	allocated channel: ORA_DISK_1
	channel ORA_DISK_1: SID=103 device type=DISK
	analyzing automatic repair options complete
	 
	Mandatory Manual Actions
	========================
	1. If file /disk1/oradata/prod/users01.dbf was unintentionally renamed or
	 moved, restore it
	2. Contact Oracle Support Services if the preceding recommendations cannot be
	 used, or if they do not fix the failures selected for repair
	 
	Optional Manual Actions
	=======================
	no manual actions available
	 
	Automated Repair Options
	========================
	Option Repair Description
	------ ------------------
	1      Perform block media recovery of block 56416 in file 1
	  Strategy: The repair includes complete media recovery with no data loss
	  Repair script: /disk1/oracle/log/diag/rdbms/prod/prod/hm/reco_1863891774.hm
	```
3. Proceed to " Repairing Failures " to determine how to repair the failures shown in the `LIST FAILURE` output.

#### 15.5.2 Determining Repair Options for a Subset of Failures

You can also request repair options for specific failures. You can specify failures by status (`CRITICAL`, `HIGH`, or `LOW`) or by failure number. You can also use `EXCLUDE FAILURE` to exclude one or more failures from the report.

To determine repair options for a subset of failures:

1. List failures as described in " Listing All Failures ".
2. In the same RMAN session, execute `ADVISE FAILURE` with the desired options.
	The following example requests repair options for failure 101 only.
	```
	RMAN> ADVISE FAILURE 101;
	 
	List of Database Failures
	=========================
	 
	Failure ID Priority Status    Time Detected Summary
	---------- -------- --------- ------------- -------
	101        HIGH     OPEN      23-APR-13     Datafile 1: '/disk1/oradata/prod/system01.dbf' contains one or more corrupt blocks
	 
	analyzing automatic repair options; this may take some time
	using channel ORA_DISK_1
	analyzing automatic repair options complete
	 
	Mandatory Manual Actions
	========================
	no manual actions available
	 
	Optional Manual Actions
	=======================
	no manual actions available
	 
	Automated Repair Options
	========================
	Option Repair Description
	------ ------------------
	1      Perform block media recovery of block 56416 in file 1
	  Strategy: The repair includes complete media recovery with no data loss
	  Repair script: /disk1/oracle/log/diag/rdbms/prod/prod/hm/reco_708819503.htm
	```
3. Proceed to " Repairing Failures " to determine how to repair the failures displayed by the `LIST FAILURE` command.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF166) to learn about the `ADVISE FAILURE` command

### 15.6 Repairing Failures

You can use Data Recovery Advisor to repair failures automatically.

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

This section contains the following topics:

- About Repairing Failures
- Repairing a Failure

#### 15.6.1 About Repairing Failures

If `ADVISE FAILURE` suggests manual repairs, then try these first. If manual repairs are not possible, or if they do not repair all failures, then you can use `REPAIR FAILURE` to automatically fix failures suggested in the most recent `ADVISE FAILURE` command in your current RMAN session.

By default, `REPAIR FAILURE` prompts for confirmation before it begins executing. You can suppress the confirmation prompt by specifying the `NOPROMPT` option. After it starts executing, the command indicates the current phase of repair. Depending on the circumstances, RMAN may prompt for a response. After executing a repair, RMAN reevaluates all existing failures on the chance that they may have been fixed during this repair.

While repairing a failure, wherever possible, RMAN takes a file online, restores and recovers it, and then brings it back online again. You can repair failures for a selected database, tablespace, or data file.

Before performing a repair, it is typically advisable to preview it by specifying the `PREVIEW` option. RMAN does not make any repairs and generates a script with all repair actions and comments. If you do not specify a particular repair option, then RMAN uses the first repair option of the most recent `ADVISE FAILURE` command in the current session. By default the repair script is displayed to standard output. You can use the `SPOOL` command to write the script to an editable file.

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF199) to learn about the `REPAIR FAILURE` command
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF156) to learn about the `SPOOL` command

#### 15.6.2 Repairing a Failure

By default the script is displayed to standard output. You can use the `SPOOL` command to write the script to an editable file.

To repair a failure:

1. List failures as described in " Listing All Failures ".
2. Display repair options as described in " Determining Repair Options ".
3. Optionally, execute `REPAIR FAILURE PREVIEW`.
	The following example previews the first repair options displayed by the previous `ADVISE FAILURE` command in the RMAN session.
	```
	RMAN> REPAIR FAILURE PREVIEW;
	 
	Strategy: The repair includes complete media recovery with no data loss
	Repair script: /disk1/oracle/log/diag/rdbms/prod/prod/hm/reco_475549922.hm
	contents of repair script:
	   # restore and recover datafile
	   sql 'alter database datafile 28 offline';
	   restore datafile 28;
	   recover datafile 28;
	   sql 'alter database datafile 28 online';
	   # block media recovery
	   recover datafile 1 block 56416;
	```
4. Execute `REPAIR FAILURE`.
	The following repair restores and recovers one data file and performs block media recovery on one corrupt block. RMAN prompts for confirmation that it should perform the repair. The user-entered text is in bold.
	```
	RMAN> REPAIR FAILURE;
	 
	Strategy: The repair includes complete media recovery with no data loss
	Repair script: /disk1/oracle/log/diag/rdbms/prod/prod/hm/reco_475549922.hm
	contents of repair script:
	   # restore and recover data file
	   sql 'alter database datafile 28 offline';
	   restore datafile 28;
	   recover datafile 28;
	   sql 'alter database datafile 28 online';
	   # block media recovery
	   recover datafile 1 block 56416;
	 
	Do you really want to execute the above repair (enter YES or NO)? YES
	executing repair script
	 
	sql statement: alter database datafile 28 offline
	 
	Starting restore at 23-APR-13
	using channel ORA_DISK_1
	 
	channel ORA_DISK_1: starting datafile backup set restore
	channel ORA_DISK_1: specifying datafile(s) to restore from backup set
	channel ORA_DISK_1: restoring datafile 00028 to /disk1/oradata/prod/users01.dbf
	channel ORA_DISK_1: reading from backup piece /disk2/PROD/backupset/2013_04_18/o1_mf_nnndf_TAG20130418T182042_32fjzd3z_.bkp
	channel ORA_DISK_1: piece handle=/disk2/PROD/backupset/2013_04_18/o1_mf_nnndf_TAG20130418T182042_32fjzd3z_.bkp tag=TAG20130418T182042
	channel ORA_DISK_1: restored backup piece 1
	channel ORA_DISK_1: restore complete, elapsed time: 00:00:03
	Finished restore at 23-APR-13
	 
	Starting recover at 23-APR-13
	using channel ORA_DISK_1
	 
	starting media recovery
	media recovery complete, elapsed time: 00:00:01
	 
	Finished recover at 23-APR-13
	 
	sql statement: alter database datafile 28 online
	 
	Starting recover at 23-APR-13
	using channel ORA_DISK_1
	searching flashback logs for block images until SCN 429690
	finished flashback log search, restored 1 blocks
	 
	starting media recovery
	media recovery complete, elapsed time: 00:00:03
	 
	Finished recover at 23-APR-13
	repair failure complete
	```
5. Optionally, execute `LIST FAILURE` to confirm

### 15.7 Changing Failure Status and Priority

In some situations, you may want to use the `CHANGE FAILURE` command to alter the status or priority of a failure.

For example, if a block corruption has `HIGH` priority, you may want to change it to `LOW` temporarily if the block is in a little-used tablespace.

If you repair a failure by a means other than the `REPAIR FAILURE` command, then Data Recovery Advisor closes it implicitly the next time you execute `LIST FAILURE`. For this reason, you do not normally need to execute the `CHANGE FAILURE ... CLOSED` command. You need to use this command only if the automatic failure revalidation fails, but you believe the failure no longer exists. If you use `CHANGE FAILURE` to close a failure that still exists, then Data Recovery Advisor re-creates it with a different failure ID when the appropriate data integrity check is executed.

Typically, you specify the failures to change by failure number. You can also change failures in bulk by specifying `ALL`, `CRITICAL`, `HIGH`, or `LOW`. You can change a failure to `CLOSED` or to `PRIORITY HIGH` or `PRIORITY LOW`.

Note:

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

To change the status or priority of a failure:

1. List failures as described in " Listing All Failures ".
	The following example lists one failure involving corrupt data blocks.
	```
	RMAN> LIST FAILURE;
	 
	List of Database Failures
	=========================
	 
	Failure ID Priority Status    Time Detected Summary
	---------- -------- --------- ------------- -------
	142        HIGH     OPEN      23-APR-13     One or more non-system datafiles 
	                                            are missing
	101        HIGH     OPEN      23-APR-13     Datafile 25: '/disk1/oradata/prod/example01.dbf' contains one or more corrupt blocks
	```
2. Execute `CHANGE FAILURE` with the desired options.
	The following example changes the priority of a block corruption failure from `HIGH` to `LOW`.
	```
	RMAN> CHANGE FAILURE 101 PRIORITY LOW;
	 
	List of Database Failures
	=========================
	 
	Failure ID Priority Status    Time Detected Summary
	---------- -------- --------- ------------- -------
	101        HIGH     OPEN      23-APR-13     Datafile 25: '/disk1/oradata/prod/example01.dbf' contains one or more corrupt blocks
	 
	Do you really want to change the above failures (enter YES or NO)? YES
	changed 1 failures to LOW priority
	```
3. Optionally, execute `LIST FAILURE ALL` to view the change.
	If you execute `LIST FAILURE` without `ALL`, then the command lists failures with `LOW` priority only if no `CRITICAL` or `HIGH` priority failures exist.
	```
	RMAN> LIST FAILURE ALL;
	 
	List of Database Failures
	=========================
	 
	Failure ID Priority Status    Time Detected Summary
	---------- -------- --------- ------------- -------
	142        HIGH     OPEN      23-APR-13     One or more non-system datafiles 
	                                            are missing
	101        LOW      OPEN      23-APR-13     Datafile 25: '/disk1/oradata/prod/example01.dbf' contains one or more corrupt blocks
	```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF110) to learn about the `CHANGE` command