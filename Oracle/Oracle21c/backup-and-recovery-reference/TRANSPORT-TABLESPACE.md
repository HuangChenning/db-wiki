---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/TRANSPORT-TABLESPACE.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

Purpose

Use the `TRANSPORT TABLESPACE` command to create transportable tablespace sets from RMAN backups instead of the live data files of the source database.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV05141) to learn how to transport tablespaces with RMAN

Prerequisites

The limitations on creating transportable tablespace sets described in [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=ADMIN01101) apply to transporting tablespaces from backup, except the requirement to make the tablespaces read-only.

The `SYSAUX` tablespace must not be part of the recovery set, which is the set of tablespaces to be transported. RMAN enforces inclusion of the `SYSAUX` tablespace in the auxiliary set, which contains data files and other files required for the tablespace transport.

`TRANSPORT TABLESPACE` does not convert endian formats. If the target platform has a different endian format, then after running `TRANSPORT TABLESPACE` use the `CONVERT` command to convert the endian format of the transportable set data files.

If you drop a tablespace, then you cannot later use `TRANSPORT TABLESPACE` to include this tablespace in a transportable tablespace set, even if the SCN for `TRANSPORT TABLESPACE` is earlier than the SCN at which the table was dropped. If you rename a tablespace, then you cannot use `TRANSPORT TABLESPACE` to create a transportable tablespace set as of a point in time before the tablespace was renamed.

Backups and Backup Metadata

You must have a backup of all needed tablespaces (including those in the auxiliary set) and archived redo log files needed to recover to the target point in time.

If you do not use a recovery catalog, and if the database has re-used control file records containing metadata about required backups, then the command fails because RMAN cannot locate the backups. You may be able to use `CATALOG` to add backups to the RMAN repository, but if the database is overwriting control file records, you may lose records of other backups.

Data Pump Export and Import

Because the RMAN uses the Data Pump Export and Import utilities, you cannot use `TRANSPORT TABLESPACE` if the tablespaces to be transported use `XMLType`. In this case you must use the procedure in [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=ADMIN01101).

If a file under the name of the export dump file exists in the tablespace destination, then `TRANSPORT TABLESPACE` fails when it calls Data Pump Export. If you are repeating a previous `TRANSPORT TABLESPACE` job, then make sure to delete the previous output files, including the export dump file.

Tablespace and Column Encryption

The following database encryption features both use the Oracle software keystore: Transparent Data Encryption (TDE) column encryption, which functions at the column level, and TDE tablespace encryption. Note the following restrictions for tablespaces that are encrypted or contain encrypted columns:

- If you are transporting an encrypted tablespace and if the destination database does not have a keystore, then you must manually copy the keystore to the destination database.
- If the destination database has an existing keystore, then you must ensure to export the master keys from the source database and import the keys into the existing keystore on the destination database. See [Exporting a TDE Master Encryption Key](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=ASOAG-GUID-1F87839D-4D04-4752-A62E-399EFAD7E46E) in the Oracle Database Advanced Security Guide to learn more.
	Alternatively, you can also merge the software keystore from the source database to the destination database. See [Merging One TDE Wallet into an Existing TDE Wallet](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=ASOAG-GUID-31237A4D-B35D-4EC7-92A1-957A193A3E23) in the Oracle Database Advanced Security Guide to learn more.

See Also:

[Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=ASOAG10139) to learn about TDE

Usage Notes

Because RMAN creates the automatic auxiliary instance used for restore and recovery on the same node as the source instance, there is some performance overhead during the operation of the `TRANSPORT TABLESPACE` command.

If RMAN is not part of the backup strategy for your database, then you can still use `TRANSPORT TABLESPACE` if the needed data file copies and archived redo log files are available on disk. Use the `CATALOG` command to record the data file copies and archived redo log files in the RMAN repository. You can then use `TRANSPORT TABLESPACE`. You also have the option of using RMAN to back up your database specifically so you can use `TRANSPORT TABLESPACE`.

Semantics

transpt\_tbs

| Syntax Element | Description |
| --- | --- |
| `tablespace_name` | Specifies the name of each tablespace to transport.  You must have a backup of all needed tablespaces (including those in the auxiliary set) and archived redo log files available for use by RMAN that can be recovered to the target time for the `TRANSPORT TABLESPACE` operation. |

transpt\_tbs\_optlist

This subclause specifies optional parameters that affect the tablespace transport.

| Syntax Element | Description |
| --- | --- |
| `AUXILIARY DESTINATION` `'` `location` `'` | Specifies the location for files for the auxiliary instance.  You can use `SET` `NEWNAME` and `CONFIGURE` `AUXNAME` to override this argument for individual files. If using your own initialization parameter file to customize the auxiliary instance, then you can use the `DB_FILE_NAME_CONVERT` and `LOG_FILE_NAME_CONVERT` initialization parameters instead of `AUXILIARY DESTINATION`.  See Also: [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV39711) for details on the interactions among the different techniques for naming the auxiliary instance files |
| `DATAPUMP DIRECTORY` `datapump_directory` | Specifies a database directory object where Data Pump Export outputs are created (see Example 3-80). If not specified, then RMAN creates files in the location specified by `TABLESPACE ` `DESTINATION`.  See Also: [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=SUTIL-GUID-5F7380CE-A619-4042-8D13-1F7DDE429991) for more details on Data Pump Export and database directory objects |
| `DUMP FILE` `'` `filename` `'` | Specifies where to create the Data Pump Export dump file. If not specified, the export dump file is named `dmpfile.dmp` and stored in the location specified by the `DATAPUMP DIRECTORY` clause or in the tablespace destination.  Note: If a file under the name of the export dump file exists in the tablespace destination, then `TRANSPORT TABLESPACE` fails when it calls Data Pump Export. If you are repeating a previous `TRANSPORT TABLESPACE` job, then make sure to delete the previous output files, including the export dump file. |
| `EXPORT LOG` `'` `filename` `'` | Specifies the location of the log generated by Data Pump Export. If omitted, the export log is named `explog.log` and stored in the location specified by the `DATAPUMP DIRECTORY` clause or in the tablespace destination. |
| `IMPORT SCRIPT` `'` `filename` `'` | Specifies the file name for the sample input script generated by RMAN for use in plugging in the transported tablespace at the destination database. If omitted, the import script is named `impscript.sql`. The script is stored in the tablespace destination. |
| `TABLESPACE DESTINATION` `tablespace_destination` | Specifies the location of the data files for the transported tablespaces after the tablespace transport operation completes. |
| `TO RESTORE POINT` `restore_point_name` | Specifies a restore point for tablespace restore and recovery, with the SCN at which the restore point was created as the upper, inclusive limit. Because the limit is inclusive, RMAN selects only files that it can use to restore or recover tablespaces up to and including the SCN corresponding to the restore point. |
| `untilClause` | Specifies a past time, SCN, or log sequence number (see Example 3-79). If specified, RMAN restores and recovers the tablespaces at the auxiliary instance to their contents at that past point in time before export.  If you rename a tablespace, then you cannot use this command to create a transportable tablespace set as of a point in time before the tablespace was renamed. RMAN has no knowledge of the previous name of the tablespace.  Tablespaces including undo segments as of the `UNTIL` time or SCN for `TRANSPORT TABLESPACE` must be part of the auxiliary set. The control file only contains a record of tablespaces that include undo segments at the current time. If the set of tablespaces with undo segments was different at the `UNTIL` time or SCN, then `TRANSPORT TABLESPACE` fails. Thus, if you use RMAN in `NOCATALOG` mode and specify `UNTIL`, then the set of tablespaces with undo segments at the time `TRANSPORT TABLESPACE` executes must equal the set of tablespaces with undo segments at the `UNTIL` time or SCN. |

Examples

Example 3-79 Using TRANSPORT TABLESPACE with a Past Time

In this example, the tablespaces for the transportable set are `example` and `tools`, the transportable set files are to be stored at `/disk1/transport_dest`, and the transportable tablespaces are to be recovered to a time 15 minutes ago:

```
TRANSPORT TABLESPACE example, tools
  TABLESPACE DESTINATION '/disk1/transportdest'
  AUXILIARY DESTINATION '/disk1/auxdest'
  UNTIL TIME 'SYSDATE-15/1440';
```

Partial sample output follows:

```
Creating automatic instance, with SID='egnr'
 
initialization parameters used for automatic instance:
db_name=PROD
compatible=11.0.0
db_block_size=8192
.
.
.
starting up automatic instance PROD
.
.
. 
executing Memory Script
 
executing command: SET until clause
 
Starting restore at 07-JUN-13
allocated channel: ORA_AUX_DISK_1
channel ORA_AUX_DISK_1: SID=44 device type=DISK
 
channel ORA_AUX_DISK_1: starting datafile backup set restore
channel ORA_AUX_DISK_1: restoring control file
.
.
.
output file name=/disk1/auxdest/cntrl_tspitr_PROD_egnr.f
Finished restore at 07-JUN-13
 
sql statement: alter database mount clone database
 
sql statement: alter system archive log current
 
sql statement: begin dbms_backup_restore.AutoBackupFlag(FALSE); end;
 
starting full resync of recovery catalog
full resync complete
.
.
.
executing Memory Script
.
.
.
 
Starting restore at 07-JUN-13
using channel ORA_AUX_DISK_1
 
channel ORA_AUX_DISK_1: starting datafile backup set restore
channel ORA_AUX_DISK_1: specifying datafile(s) to restore from backup set
channel ORA_AUX_DISK_1: restoring datafile 00001 to /disk1/auxdest/TSPITR_PROD_EGNR/datafile/o1_mf_system_%u_.dbf
datafile 1 switched to datafile copy
.
.
.
starting media recovery
.
.
. 
Finished recover at 07-JUN-13
 
database opened
.
.
.
executing Memory Script
.
.
.
sql statement: alter tablespace EXAMPLE read only
Removing automatic instance
shutting down automatic instance
Oracle instance shut down
Automatic instance removed
auxiliary instance file /disk1/auxdest/cntrl_tspitr_PROD_egnr.f deleted
.
.
.
```

Example 3-80 Using TRANSPORT TABLESPACE with Customized File Locations

This example illustrates the use of the optional arguments that control the locations of Data Pump-related files such as the dump file. The `DATAPUMP DIRECTORY` must refer to an object that exists in the target database. Use the `CREATE DIRECTORY` SQL statement to create a directory object.

```
TRANSPORT TABLESPACE example
  TABLESPACE DESTINATION '/disk1/transportdest'
  AUXILIARY DESTINATION '/disk1/auxdest'
  DATAPUMP DIRECTORY mypumpdir
  DUMP FILE 'mydumpfile.dmp'
  IMPORT SCRIPT 'myimportscript.sql'
  EXPORT LOG 'myexportlog.log';
```