---
title: Performing RMAN Tablespace Point-in-Time Recovery (TSPITR)
book: "Backup and Recovery User's Guide"
doc_id: E10642-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmtspit.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-users-guide
---

## 21 Performing RMAN Tablespace Point-in-Time Recovery (TSPITR)

This chapter explains how to perform RMAN tablespace point-in-time recovery. This chapter contains the following sections:

## Overview of RMAN TSPITR

To use RMAN [tablespace point-in-time recovery (TSPITR)](glossary.md) effectively, it is helpful to understand what types of problems it can resolve, its components, what RMAN does during TSPITR, and the various limitations and restrictions on when and how it can be run. This section explains the basic concepts, preparatory tasks, and modes of running RMAN TSPITR.

### Purpose of RMAN TSPITR

Recovery Manager (RMAN) TSPITR enables quick recovery of one or more tablespaces in a database to an earlier time without affecting the rest of the tablespaces and objects in the database.

RMAN TSPITR is most useful for the following situations:

- To recover a logical database to a point different from the rest of the physical database, when multiple logical databases exist in separate tablespaces of one physical database. For example, you maintain logical databases in the `orders` and `personnel` tablespaces. An incorrect batch job or data manipulation language (DML) statement corrupts the data in only one tablespace.
- To recover data lost after data definition language (DDL) operations that change the structure of tables. You cannot use Flashback Table to rewind a table to before the point of a structural change such as a truncate table operation.
- To recover a table after it has been dropped with the `PURGE` option.
- To recover from the logical corruption of a table.
- To recover dropped tablespaces. In fact, RMAN can perform TSPITR on dropped tablespaces even when a recovery catalog is not used.

You can also use Flashback Database to rewind data, but you must rewind the entire database rather than just a subset. Also, unlike TSPITR, the Flashback Database feature necessitates the overhead of maintaining flashback logs. The point in time to which you can flash back the database is more limited than the TSPITR window, which extends back to your earliest recoverable backup.

### Basic Concepts of RMAN TSPITR

The following sections explain RMAN TSPITR fundamentals:

- Common Terms
- Modes of RMAN TSPITR
- How RMAN TSPITR Works With an RMAN-Managed Auxiliary Instance

#### Common Terms

Table 21-1 defines some common entities that are used by RMAN TSPITR.

Table 21-1 RMAN TSPITR Entities

| Name | Explanation |
| --- | --- |
| Target instance | Contains the tablespace to be recovered to the target time |
| Target time | Point in time or SCN of the tablespace after TSPITR completes |
| Auxiliary instance | A database instance used in the recovery process to perform the work of recovery. The auxiliary instance has other files associated with it. See auxiliary set for a complete list. |
| Auxiliary destination | An optional disk location that RMAN uses to temporarily store the auxiliary set files. The auxiliary destination is used only with an RMAN-managed auxiliary instance. Specifying an auxiliary destination with a user-managed auxiliary instance results in an error.  All references to auxiliary destination in this chapter assume use of an RMAN-managed auxiliary instance. |
| Recovery set | Data files in the tablespaces that you intend to recover |
| Auxiliary set | Data files required for TSPITR that are not part of the recovery set. The auxiliary set typically includes:  - The `SYSTEM` and `SYSAUX` tablespaces. - Data files containing rollback or undo segments from the target database instance. - Temporary tablespaces. - Control file from source database. - Archived redo logs that must be restored to recover the auxiliary instance to specified point in time. - Online redo logs of the auxiliary instance. These are not the same logs as the online redo logs from the source database. They are created when the auxiliary instance is opened with the `RESETLOGS` option.  The auxiliary set does not include the parameter file, password file, or associated network files. |

#### Modes of RMAN TSPITR

You start RMAN TSPITR with the RMAN `RECOVER TABLESPACE` command. You have several options for running RMAN TSPITR. The difference between the various modes of operation corresponds to how much automation versus customization you require in your environment. There are three ways to run the utility:

- Fully Automated (the default)
	In this mode, RMAN manages the entire TSPITR process including the auxiliary instance. You specify the tablespaces of the recovery set, an auxiliary destination, the target time, and you allow RMAN to manage all other aspects of TSPITR.
	The default mode is recommended unless you specifically need more control over the location of recovery set files after TSPITR, auxiliary set files during TSPITR, channel settings and parameters or some other aspect of your auxiliary instance. For more information, see "Performing Fully Automated RMAN TSPITR".
- Automated: RMAN-Managed Auxiliary Instance with User Settings
	You can override some defaults of RMAN TSPITR while still using an RMAN-managed auxiliary instance and destination. This variation of the default mode enables you to benefit from some built-in management that RMAN TSITR provides while being able to specify:
	- Location of auxiliary set or recovery set files
		- Initialization parameters
	For more information, see "Overriding Defaults for RMAN TSPITR with an RMAN-Managed Auxiliary Instance".
- Non-Automated: TSPITR and User-Managed Auxiliary Instance
	This mode of RMAN TSPITR requires you to set up and manage all aspects of the auxiliary instance and some aspects of the TSPITR process. This mode may be appropriate if, for example, you must allocate a different number of channels or change the channel parameters for your user-managed auxiliary instance.
	For more information, see "Performing RMAN TSPITR Using Your Own Auxiliary Instance".

#### How RMAN TSPITR Works With an RMAN-Managed Auxiliary Instance

Having selected tablespaces from the recovery set, an auxiliary destination and a target time, you are now ready to perform Fully Automated RMAN TSPITR (default). The automated mode of RMAN TSPITR shares many of these high-level processing steps.

RMAN TSPITR automatically performs the following actions:

1. If the tablespaces in the recovery set have not been dropped, checks to see if they are self-contained by executing the `DBMS_TTS.TRANSPORT_SET_CHECK` for the recovery set tablespaces and then checking that the view `TRANSPORT_SET_VIOLATIONS` is empty. If the query returns rows, RMAN stops TSPITR processing. You must resolve any tablespace containment violations before TSPITR can proceed. Example 21-1 shows you how to set up and run the query before invoking RMAN TSPITR.
2. Checks to see if a connection to a user-managed auxiliary instance was provided. If it is, then RMAN TSPITR uses it. If not, RMAN TSPITR creates the auxiliary instance, starts it, and connects to it.
3. Takes the tablespaces to be recovered offline in the target database, if the tablespaces in the recovery set have not been dropped.
4. Restores a backup control file from a point in time before the target time to the auxiliary instance.
5. Restores the data files from the recovery set and the auxiliary set to the auxiliary instance.
	Files are restored either in the:
	- Locations that you specify for each file
		- Original location of the file (for recovery set data files)
		- Auxiliary destination (if you used the `AUXILIARY DESTINATION` argument of `RECOVER TABLESPACE` and an RMAN-managed auxiliary instance)
6. Recovers the restored data files in the auxiliary instance to the specified time.
7. Opens the auxiliary database with the `RESETLOGS` option.
8. Makes the recovery set tablespaces read-only in the auxiliary instance.
9. Exports the recovery set tablespaces from the auxiliary instance using the Data Pump utility to produce a transportable tablespace dump file.
10. Shuts down the auxiliary instance.
11. Drops the recovery set tablespaces from the target.
12. Data Pump utility reads the transportable tablespace dump file and plugs the recovery set tablespaces into the target.
13. Makes the tablespaces that were put in the target database read/write and immediately takes them offline.
14. Deletes all auxiliary set files.

At this point, RMAN TSPITR has finished. The recovery set data files are returned to their contents at the specified point in time, and belong to the target database.

The recovery set tablespaces are left offline for you to back up and then bring back online. These last steps follow Oracle's recommendation and best practice of backing up recovered tablespaces as soon as TSPITR completes.

## TSPITR Restrictions, Special Cases, and Limitations

Some database problems cannot be resolved with TSPITR. The following list explains when you cannot perform TSPITR:

- If there are no archived redo logs or if the database runs in `NOARCHIVELOG` mode.
- If TSPITR is used to recover a renamed tablespace to a point in time before it was renamed, you must use the previous name of the tablespace to perform the recovery operation.
	In this case when TSPITR completes, the target database contains two copies of the same tablespace, the original tablespace with the new name and the TSPITR tablespace with the old name. If this is not your goal, then you can drop the new tablespace with the new name.
- If constraints for the tables in tablespace `tbs1` are contained in tablespace `tbs2`, then you cannot recover `tbs1` without also recovering `tbs2`.
- If a table and its indexes are stored in different tablespaces, then the indexes must be dropped before performing TSPITR.
- You cannot use TSPITR to recover the current default tablespace.
- You cannot use TSPITR to recover tablespaces containing any of the following objects:
	- Objects with underlying objects (such as materialized views) or contained objects (such as partitioned tables) unless all of the underlying or contained objects are in the recovery set. Additionally, if the partitions of a partitioned table are stored in different tablespaces, then you must either drop the table before performing TSPITR or move all the partitions to the same tablespace before performing TSPITR.
		- Undo or rollback segments
		- Oracle8-compatible advanced queues with multiple recipients
		- Objects owned by the user `SYS`. Examples of these types of objects are: PL/SQL, Java classes, callout programs, views, synonyms, users, privileges, dimensions, directories, and sequences.

### Limitations of TSPITR

After TSPITR completes, RMAN recovers the data files in the recovery set to the target time. Note the following special cases:

- TSPITR does not recover query optimizer statistics for recovered objects.You must gather new statistics after TSPITR completes.
- If you run TSPITR on a tablespace and bring the tablespace online at time t, then backups of the tablespace created before time t are no longer usable for recovery with a current control file. You cannot use the current control file to recover the database to any time less than or equal to t.
- If one or more data files in the recovery set have Oracle Managed File (OMF) names and the compatibility in the target database is set to version 10.1 or earlier, RMAN cannot reuse the data file. This restriction is true even if no `SET NEWNAME` command is provided for the data file. A new OMF name is created for the recovery set data file. This action temporarily doubles the space requirements for the data file. This is because `DB_CREATE_FILE_DEST` has two copies of the data file (the original data file and the one used by TSPITR) until the tablespace is dropped in the target and the original data file is deleted.

RMAN uses the transportable tablespaces functionality to perform TSPITR. Therefore, any limitations on transportable tablespaces are also applicable to TSPITR.

See Also:

[Oracle Database Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=ADMIN13896) for information about limitations on transportable tablespaces

### Special Considerations When Not Using a Recovery Catalog

You should be aware of following precautions:

- Because RMAN has no historical record of the undo in the control file, RMAN assumes that the current set of tablespaces with rollback or undo segments were the same set present at the time when recovery was performed. If the tablespace set has changed since that time, then the current rollback or undo segments were the same segments present at the time to which recovery is performed. If the undo segments have changed since that time, then you can use `UNDO TABLESPACE` to indicate the correct set of tablespaces with undo at the point in time where the tablespaces are being recovered.
- TSPITR to a time that is too old may not succeed if Oracle Database has reused the control file records for needed backups. (In planning your database, set the `CONTROL_FILE_RECORD_KEEP_TIME` initialization parameter to a value large enough to ensure that control file records needed for TSPITR are kept.)
- To rerun TSPITR when you are not using a recovery catalog, you must first drop the tablespace to be used by TSPITR from the target database.

## Planning and Preparing for TSPITR

This section assumes that you have read "TSPITR Restrictions, Special Cases, and Limitations". You must complete the following steps when preparing for TSPITR:

- Step 1: Select the Right Target Time for TSPITR
- Step 2: Determine the Recovery Set
- Step 3: Identify and Preserve Objects That Are Lost After TSPITR

### Step 1: Select the Right Target Time for TSPITR

It is extremely important that you choose the right target time or SCN for your TSPITR. As noted in "TSPITR Restrictions, Special Cases, and Limitations", after you bring a tablespace online after TSPITR, you cannot use any backup from a time earlier than the moment you brought the tablespace online.

If you have a recovery catalog, then you can perform repeated TSPITR operations to different target times because the catalog contains tablespace history information. If RMAN uses only a control file, however, repeated TSPITR is only possible after dropping the tablespace because the control file does not have the tablespace history. In this case, RMAN only knows about the current set of tablespaces. The tablespace on which TSPITR was performed has a creation time equal to the time it was brought online.

To investigate past states of your data to identify the target time for TSPITR, you can use Flashback Query, Oracle Transaction Query, and Flashback Version Query to find the point in time when unwanted database changes occurred.

See Also:

[Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_flashback.htm#ADFNS1008) for more information on Flashback Query, Flashback Transaction Query, and Flashback Version Query

### Step 2: Determine the Recovery Set

Initially, your recovery set includes the data files for the tablespaces that you intend to recover. However, if objects in the tablespaces that you need have relationships (such as constraints) to objects in other tablespaces, then you must account for these relationships before you can perform TSPITR. You have the following choices when faced with such a relationship:

- Add the tablespace including the related objects to your recovery set
- Remove the relationship
- Suspend the relationship for the duration of TSPITR

#### Identify and Resolve Dependencies on the Primary Database

RMAN TSPITR requires that the tablespace be self-contained and that no SYS -owned objects reside in the tablespace. You can use the `DBMS_TTS.TRANSPORT_SET_CHECK` procedure to locate objects outside the tablespace and identify relationships between objects that span the recovery set boundaries. If the `TRANSPORT_SET_VIOLATIONS` view returns rows, you must investigate and correct the problem according to the choices mentioned earlier in this step.

Note:

If one or more of the tablespaces in the recovery set have been dropped, RMAN TSPITR cannot run the procedure `DBMS_TTS.TRANSPORT_SET_CHECK`. In this case, `DBMS_TTS.TRANSPORT_SET_CHECK` is run when the Data Pump export of the auxiliary instance occurs. Just like RMAN TSPITR, the export operation fails if it encounters any tablespaces that are not self-contained.

Record all actions performed during this step so that you can re-create any suspended or removed relationships after completing TSPITR. Proceed with TSPITR only when the `TRANSPORT_SET_VIOLATIONS` view is empty for the tablespaces in the recovery set.

The query in Example 21-1 illustrates how to use the `DBMS_TTS.TRANSPORT_SET_CHECK` procedure for an initial recovery set consisting of tablespaces `tools` and `users`. It queries the transportable tablespace violations table to manage any dependencies. No rows are returned from this query when all dependencies are managed.

Example 21-1 Querying DBMS\_TTS.TRANSPORT\_SET\_CHECK for a Subset of Tablespaces

```
BEGIN
   DBMS_TTS.TRANSPORT_SET_CHECK('USERS,TOOLS', TRUE,TRUE);
END;
/
SELECT * FROM  TRANSPORT_SET_VIOLATIONS;
```

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for more information about the `DBMS_TTS.TRANSPORT_SET_CHECK` procedure and corresponding view

### Step 3: Identify and Preserve Objects That Are Lost After TSPITR

When you perform RMAN TSPITR on a tablespace, objects created after the target recovery time are lost. You can preserve such objects after they are identified by exporting them before TSPITR with the Data Pump Export utility and reimporting them afterward with Data Pump Import.

To determine which objects are lost in TSPITR, query the `TS_PITR_OBJECTS_TO_BE_DROPPED` view on the primary database. Table 21-2 describes the contents of the view.

Table 21-2 TS\_PITR\_OBJECTS\_TO\_BE\_DROPPED View

| Column Name | Meaning |
| --- | --- |
| `OWNER` | Owner of the object to be dropped |
| `NAME` | The name of the object that is lost by undergoing TSPITR |
| `CREATION_TIME` | Creation time stamp for the object |
| `TABLESPACE_NAME` | Name of the tablespace containing the object |

Filter the view for objects whose `CREATION_TIME` is after the target time for TSPITR. For example, with a recovery set consisting of `users` and `tools`, and a recovery point in time of November 2, 2007, 7:03:11 am, issue the statement shown in Example 21-2.

Example 21-2 Querying TS\_PITR\_OBJECTS\_TO\_BE\_DROPPED

```
SELECT OWNER, NAME, TABLESPACE_NAME, 
       TO_CHAR(CREATION_TIME, 'YYYY-MM-DD:HH24:MI:SS') 
       FROM TS_PITR_OBJECTS_TO_BE_DROPPED 
WHERE TABLESPACE_NAME IN ('USERS','TOOLS') 
AND CREATION_TIME > TO_DATE('02-NOV-07:07:03:11','YY-MON-DD:HH24:MI:SS')
ORDER BY TABLESPACE_NAME, CREATION_TIME;
```

The `TO_CHAR` and `TO_DATE` functions are used to avoid issues with different national date formats. Of course, you can use local date formats in your own work.

Alternatively, if you have the SCN of the tablespaces, you can use conversion functions to determine the time stamp associated with the SCN and the objects that are dropped. For example, if the SCN to recover tablespaces `users` and `tools` is 1645870, use the statement outlined in Example 21-3 to determine the objects that are dropped.

Example 21-3 Using SCN and TS\_PITR\_OBJECTS\_TO\_BE\_DROPPED

```
SELECT OWNER, NAME, TABLESPACE_NAME,
       TO_CHAR(CREATION_TIME,'YYYY-MM-DD:HH24:MI:SS')
       FROM TS_PITR_OBJECTS_TO_BE_DROPPED
WHERE TABLESPACE_NAME IN ('USERS','TOOLS')
AND CREATION_TIME > TO_DATE(TO_CHAR(SCN_TO_TIMESTAMP(1645870),
'MM/DD/YYYY HH24:MI:SS'),
'MM/DD/YYYY HH24:MI:SS')
ORDER BY TABLESPACE_NAME, CREATION_TIME;
```

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for more information about the `TS_PITR_OBJECTS_TO_BE_DROPPED` view

## Performing Fully Automated RMAN TSPITR

In the default mode, RMAN bases as much of the configuration for TSPITR as possible on the target database. During TSPITR, the recovery set data files are written in their current locations on the target database (For OMF files, see "Limitations of TSPITR"). The same channel configurations for the target database are used on the auxiliary instance when restoring files from backup. Auxiliary set data files and other auxiliary instance files, however, are stored in the auxiliary destination.

Use the `AUXILIARY DESTINATION` parameter to set a location for RMAN to use for the auxiliary set data files. The auxiliary destination must be a location on disk with enough space to hold auxiliary set data files. Even if you use other techniques to rename some or all of the auxiliary set data files, specifying an `AUXILIARY DESTINATION` parameter provides a default location for auxiliary set data files for which names are not specified. TSPITR does not fail if you inadvertently omit some names of the auxiliary set data files.

To perform fully automated RMAN TSPITR, the user performing TSPITR should be able to connect as `SYSDBA` using operating system authentication.

To perform fully automated RMAN TSPITR:

1. Review the information in "TSPITR Restrictions, Special Cases, and Limitations".
2. Perform the tasks in "Planning and Preparing for TSPITR".
3. Start an RMAN session on the target database and, if applicable, connect to a recovery catalog.
	Note:
	Do not connect to an auxiliary instance when starting the RMAN client for automated TSPITR. If RMAN is connected to an auxiliary instance when you run `RECOVER TABLESPACE`, then RMAN assumes that you are trying to manage your own auxiliary instance, as described in "Performing RMAN TSPITR Using Your Own Auxiliary Instance", and tries to use the connected auxiliary for TSPITR.
4. Configure any channels required for TSPITR on the target instance.
	The auxiliary instance uses the same channel configuration as the target instance when performing TSPITR.
5. Run the `RECOVER TABLESPACE` command, specifying both the `UNTIL` clause and the `AUXILIARY DESTINATION` parameter.
	Example 21-4 returns the `users` and `tools` tablespaces to the end of log sequence number 1299, and stores the auxiliary set files in the `/disk1/auxdest` directory.
	Example 21-4 Performing TSPITR on Two Tablespaces
	```
	RECOVER TABLESPACE users, tools 
	  UNTIL LOGSEQ 1300 THREAD 1
	  AUXILIARY DESTINATION '/disk1/auxdest';
	```
	The next step depends on the results of the `RECOVER` command:
	- If no error occurs during TSPITR, then proceed to Step 6.
		The tablespaces are taken offline by RMAN, restored from backup and recovered to the desired point in time on the auxiliary instance, and then reimported to the target database. The tablespaces are left offline. All auxiliary set data files and other auxiliary instance files are cleaned up from the auxiliary destination.
		- If an error occurs during TSPITR, then proceed to "Troubleshooting RMAN TSPITR".
6. If TSPITR completes successfully, then back up the recovered tablespaces before bringing them online.
	For example, enter the following command:
	```
	BACKUP TABLESPACE users, tools;
	```
	After you perform TSPITR on a tablespace, you can no longer use previous backups of that tablespace once TSPITR successfully completes. If you use the recovered tablespaces without taking a backup, then you run your database without a usable backup of these tablespaces.
7. Bring the tablespaces back online.
	For example, enter the following command:
	```
	RMAN> SQL "ALTER TABLESPACE users, tools ONLINE";
	```
	Your recovered tablespaces are now ready for use.

## Overriding Defaults for RMAN TSPITR with an RMAN-Managed Auxiliary Instance

You can customize the following aspects of RMAN TSPITR while still mostly following the procedure described in "Performing Fully Automated RMAN TSPITR":

- Rename or relocate your recovery set data files so that the data files making up the recovered tablespaces are not stored in the original locations after TSPITR. This may be necessary if the disk that originally contained the tablespace is not usable.
	This task is described in "Renaming TSPITR Recovery Set Data Files with SET NEWNAME".
- Specify a location other than the auxiliary destination for some or all auxiliary set data files. You might choose this option if no single location on disk has enough space for all auxiliary set files.
	This task is described in "Naming TSPITR Auxiliary Set Data Files".
- Rename files in an Oracle Managed Files format.
	This task is described in "Considerations When Renaming OMF Auxiliary Set Files in TSPITR".
- Set up image copy backups of your auxiliary set data files in advance to avoid having to restore data files during TSPITR.
	This task is described in "Using Image Copies for Faster RMAN TSPITR Performance".
- Customize initialization parameters for your RMAN-managed auxiliary instance.
	This task is described in "Customizing Initialization Parameters for the Automatic Auxiliary Instance in TSPITR".

### Renaming TSPITR Recovery Set Data Files with SET NEWNAME

You may not want the recovery set data files restored and recovered in their original locations. The `SET NEWNAME` command enables you to specify a new destination. When you specify a new destination for the recovery set, RMAN does not remove the original data files of the tablespaces.

To specify new recovery set file names, create a `RUN` block and use `SET NEWNAME` commands within it. Be sure to assign names that do not conflict with each other or with the names of your current data files. Example 21-5 illustrates the basic technique.

Example 21-5 Renaming Recovery Set Files

```
RUN
{
   .
   .
   .
   SET NEWNAME FOR DATAFILE 'ORACLE_HOME/oradata/trgt/users01.dbf'
     TO '/newfs/users01.dbf';
   ...other SET NEWNAME commands...
   RECOVER TABLESPACE users, tools UNTIL SEQUENCE 1300 THREAD 1;
}
```

In this example, RMAN takes the following actions:

- Restores each specified data file to the new location during TSPITR.
- Uses the image copy if one exists at the specified location and its checkpoint is before the specified point in time. If this criteria is not met, then RMAN overwrites the image copy.
- Plugs the newly recovered data file into the target control file.

RMAN does not detect conflicts between names set with `SET NEWNAME` and current data file names on the target database until the actual recovery. If RMAN detects a conflict, then TSPITR fails and RMAN reports an error. The valid data file is not overwritten.

### Naming TSPITR Auxiliary Set Data Files

Unlike recovery set data files, which are usually stored in their original locations, auxiliary set data files must not overwrite the corresponding original files in the target database. If you do not specify an auxiliary set file location that is different from its original location, then TSPITR fails. The failure occurs when RMAN attempts to overwrite the corresponding file in the original database and discovers the file in use.

The simplest way to provide locations for auxiliary set data files is to specify an auxiliary destination for TSPITR. However, RMAN supports the following alternatives for controlling the location of auxiliary set data files, which are listed in order of precedence shown in Table 21-3.

Table 21-3 Order of Precedence for Naming Files

| Order | Technique | Section |
| --- | --- | --- |
| 1 | `SET` `NEWNAME` | "Using SET NEWNAME to Name Auxiliary Set Data Files" |
| 2 | `CONFIGURE` `AUXNAME` | "Using SET NEWNAME and CONFIGURE AUXNAME with Auxiliary Set Image Copies" |
| 3 | `DB_FILE_NAME_CONVERT` | "Using DB\_FILE\_NAME\_CONVERT to Name Auxiliary Set Data Files". If the target database uses OMF names for auxiliary set, then you cannot use `DB_FILE_NAME_CONVERT.` See "Considerations When Renaming OMF Auxiliary Set Files in TSPITR". |
| 4 | `AUXILIARY DESTINATION` argument to `RECOVER TABLESPACE` when using an RMAN-managed auxiliary instance |  |

Settings higher on the list override settings lower on the list in situations where both have been applied. For example, you might run `RECOVER TABLESPACE... AUXILIARY DESTINATION` on a target database when some auxiliary set data files have auxiliary names configured with `CONFIGURE AUXNAME`.

Even if you intend to use either of the preceding techniques to provide locations for specific files, Oracle recommends that you provide an `AUXILIARY DESTINATION` argument to `RECOVER TABLESPACE` when using an RMAN-managed auxiliary instance. If you overlook renaming some auxiliary set data files, then TSPITR still succeeds. Any files not otherwise renamed are placed in the auxiliary destination.

Note:

You can view any current `CONFIGURE` `AUXNAME` settings by running the `SHOW` `AUXNAME` command, which is described in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2015.htm#RCMRF154).

#### Considerations When Renaming OMF Auxiliary Set Files in TSPITR

Auxiliary set data files can have Oracle Managed Files (OMF) in the target and can use Automatic Storage Management (ASM) or non-ASM storage. TSPITR performs name conversion differently when the `DB_FILE_NAME_CONVERT` initialization parameter is set and the OMF files are in ASM or non-ASM storage.

##### Using ASM Storage

For Oracle Managed Files (OMF) that use ASM storage, the database converts only disk group names as in: +DISK1 to +DISK2.

You can use `DB_FILE_NAME_CONVERT` and `LOG_FILE_NAME_CONVERT` initialization parameters for the auxiliary instance to specify the conversion of the disk group. RMAN uses the pattern to convert the ASM disk group name and generates a valid OMF file name in the converted disk group. The following command demonstrates this point:

```
LOG_FILE_NAME_CONVERT='+onlinelogs','+tmpasm'
```

If the `DB_FILE_NAME_CONVERT` and `LOG_FILE_NAME_CONVERT` parameters change a substring other than the disk group name, the conversion is ignored and the resulting disk group name is used, for example:

```
DB_FILE_NAME_CONVERT='+DATAFILE/prod','+DATAFILE/tspitr'
```

The preceding command results in an invalid ASM OMF file name and the change is ignored. Instead, the files are created in disk group name +DATAFILE and the following message is issued:

```
WARNING: DB_FILE_NAME_CONVERT resulted in invalid ASM names; names changed to disk group only
```

If auxiliary set data files are stored in ASM disk groups, then you can use the `SET` `NEWNAME` command to redirect individual files to a specific disk group accessible from the auxiliary instance (and allow the database to generate the file name within the disk group). Example 21-6 shows how to do this.

Example 21-6 Redirecting ASM files

```
RUN
{
  SET NEWNAME FOR DATAFILE 1 TO "+DISK2";
  SET NEWNAME FOR DATAFILE 2 TO "+DISK3";
  RECOVER TABLESPACE users, tools 
    UNTIL LOGSEQ 1300 THREAD 1
    AUXILIARY DESTINATION '/disk1/auxdest';
}
```

##### Using Non-ASM Storage

The initialization parameters `DB_FILE_NAME_CONVERT` and `LOG_FILE_NAME_CONVERT` cannot be used to rename OMF (non-ASM) file names for the auxiliary instance because this method generates invalid OMF file names. If you must control the generation of new OMF file names that do not use ASM storage, you must rename them using one of the following alternate techniques. The various naming options are listed in order from most recommended to least recommended.

1. Use an auxiliary destination, as described in "Performing Fully Automated RMAN TSPITR".
2. Specify locations for new OMF files with one or more of the OMF initialization parameters for the auxiliary instance so that all of the necessary OMF files are handled:
	- `DB_CREATE_FILE_DEST` for the auxiliary set data files
		- `DB_CREATE_ONLINE_LOG_DEST_` `n` with `DB_CREATE_FILE_DEST` for the online redo logs of the auxiliary instance if the online logs are not created in the `DB_CREATE_FILE_DEST`

#### Using SET NEWNAME to Name Auxiliary Set Data Files

To specify a new name for an auxiliary set data file, you can enclose `RECOVER TABLESPACE` in a `RUN` command and use a `SET NEWNAME` command within the `RUN` block to rename the file. Example 21-7 illustrates the basic technique.

Example 21-7 Renaming Auxiliary Set Oracle Managed Files (OMF) in TSPITR

```
RUN
{
  SET NEWNAME FOR DATAFILE '?/oradata/prod/system01.dbf'
    TO '/disk1/auxdest/system01.dbf';
  SET NEWNAME FOR DATAFILE '?/oradata/prod/sysaux01.dbf'
    TO '/disk1/auxdest/sysaux01.dbf';
  SET NEWNAME FOR DATAFILE '?/oradata/prod/undotbs01.dbf'
    TO '/disk1/auxdest/undotbs01.dbf';
  RECOVER TABLESPACE users, tools 
    UNTIL LOGSEQ 1300 THREAD 1
    AUXILIARY DESTINATION '/disk1/auxdest';
}
```

The result depends on whether `/disk1/auxdest/system01.dbf` exists when `RECOVER TABLESPACE` is executed. If `?/oradata/system01.dbf` exists at the specified location and was created at an SCN before the `UNTIL` time for TSPITR, then the `DATAFILECOPY` is used and the restore operation is not necessary. For more information, see "Using SET NEWNAME and CONFIGURE AUXNAME with Auxiliary Set Image Copies". Otherwise, RMAN restores the auxiliary set data file to the `NEWNAME` instead of the default location. If your intention is to control where the auxiliary set data files are stored, then ensure that no file is stored at the location specified by `SET NEWNAME` before performing TSPITR.

#### Using DB\_FILE\_NAME\_CONVERT to Name Auxiliary Set Data Files

Assume that you do not want to use an auxiliary destination for all of your auxiliary set data files, but you also do not want to name every file individually. In this case, you can include a `DB_FILE_NAME_CONVERT` initialization parameter in the initialization parameter file used by the auxiliary instance. You can use this technique only in the following circumstances:

One of the following situations exists:

- \- You create your own initialization parameter file for an automatically managed auxiliary instance, as described in "Customizing Initialization Parameters for the Automatic Auxiliary Instance in TSPITR"
- \- You create your own auxiliary instance, as described in "Performing RMAN TSPITR Using Your Own Auxiliary Instance"

The `DB_FILE_NAME_CONVERT` initialization parameter in the auxiliary instance specifies how to derive names for files in the auxiliary instance from the original names of the corresponding files in the target database instance. The parameter consists of a list of pairs of strings. For any file name that contains the first string of a pair as a substring, the name of the corresponding file in the auxiliary instance is generated by substituting the second string of the pair into the original file name.

For example, assume that the target instance contains the following files:

- `?/oradata/trgt/system01.dbf` of the `SYSTEM` tablespace
- `?/oradata/trgt/sysaux01.dbf` of the `SYSAUX` tablespace
- `?/oradata/trgt/undotbs01.dbf` of the `undotbs` tablespace

To place the corresponding files of the auxiliary instance in `/bigtmp`, you would add the following line to the auxiliary instance parameter file:

```
DB_FILE_NAME_CONVERT=('?/oradata/trgt', '/bigtmp')
```

New file names for the corresponding auxiliary instance files would be `/bigtmp/trgt/system01.dbf`, `/bigtmp/trgt/sysaux01.dbf`, and `/bigtmp/trgt/undotbs01.dbf`.

The most important point to remember is that `DB_FILE_NAME_CONVERT` must be present in the auxiliary instance parameter file. If the auxiliary instance was manually created, then add `DB_FILE_NAME_CONVERT` to the auxiliary instance parameter file.

You can still rename individual auxiliary set data files with the `SET NEWNAME` or `CONFIGURE AUXNAME` command. Also, files that do not match the patterns provided in `DB_FILE_NAME_CONVERT` are not renamed. When using RMAN-managed auxiliary instance, you can use the `AUXILIARY DESTINATION` parameter of `RECOVER TABLESPACE` command to ensure that all auxiliary set data files are sent to some destination. If none of the renaming methods used provide a new name for a file at the auxiliary instance, then TSPITR fails.

##### Renaming Temp Files During TSPITR

Temp files are considered part of the auxiliary set for your database. When the auxiliary instance is instantiated, RMAN re-creates the temporary tablespaces of the target database and generates their names using the regular rules for the auxiliary data file names.

To rename temp files, you can use one of the following:

- `SET` `NEWNAME` `FOR` `TEMPFILE` command
- `DB_FILE_NAME_CONVERT` initialization parameter of the auxiliary instance. See the previous example. If the temporary files have non-ASM Oracle Managed File names, you cannot use this parameter option. See "Considerations When Renaming OMF Auxiliary Set Files in TSPITR".
- `AUXILIARY DESTINATION` clause of the `RECOVER` command when using an RMAN-managed auxiliary instance

### Using Image Copies for Faster RMAN TSPITR Performance

You can enhance TSPITR performance by redirecting RMAN to use existing image copies of the recovery set and auxiliary set data files. In this case, RMAN does not need to restore the data files from backup. You can use the following techniques to tell RMAN about the possible existence of an image copy of a data file:

- Use the `CONFIGURE AUXNAME` command with image copies of auxiliary set data files
- Use the `SET NEWNAME` command with image copies of recovery set data files or auxiliary set data files

In general, if a suitable image copy is available in the specified location, then RMAN uses the image copy to perform TSPITR, and the data file copy is uncataloged from the target control file.

#### Using SET NEWNAME with Recovery Set Image Copies

During TSPITR, RMAN looks in the specified `NEWNAME` location for the data file. RMAN checks whether an image copy backup of the data file exists with a [data file checkpoint](glossary.md) SCN early enough that it can be recovered to the target time. If RMAN finds a usable image copy, then RMAN uses it in TSPITR. Otherwise, RMAN restores the data file to the `NEWNAME` location. Any file in the location specified by the `NEWNAME` is overwritten. The specified `NEWNAME` becomes the name of the data file in the target database once TSPITR completes. Example 21-8 illustrates this technique.

Example 21-8 Using SET NEWNAME

```
RUN
{
SET NEWNAME FOR DATAFILE 'ORACLE_HOME/oradata/trgt/users01.dbf' 
  TO '/newfs/users1.dbf';
...other RMAN commands, if any...
RECOVER TABLESPACE users, tools UNTIL SEQUENCE 1300 THREAD 1;
}
```

#### Using SET NEWNAME and CONFIGURE AUXNAME with Auxiliary Set Image Copies

The `CONFIGURE AUXNAME` command sets a persistent alternative location for an auxiliary set data file image copy, whereas the `SET NEWNAME` command sets an alternative location for the duration of a `RUN` command.

Assume that you use `SET NEWNAME` or `CONFIGURE AUXNAME` to specify a new location for an auxiliary set data file. Also assume that there is an image copy at that location with an SCN that can be used in TSPITR. In this case, RMAN uses the image copy. If there is no usable image copy at that location, however, then RMAN restores a usable copy from backup. (If an image copy is present but the SCN is after the target time for TSPITR, then the data file is overwritten by the restored file.)

As with all auxiliary set files, the file is deleted after TSPITR. This behavior occurs regardless of whether it was an image copy created before TSPITR or restored by RMAN during TSPITR.

The primary use of `CONFIGURE AUXNAME` is to make TSPITR faster by eliminating restore times. If you anticipate performing TSPITR, then you can include in your backup routine the maintenance of a set of image copies of the auxiliary set data files, and update these periodically to the earliest point to which you expect to perform TSPITR. The recommended usage model is:

1. Configure the `AUXNAME` for the files once, when setting up this strategy.
2. Perform `BACKUP AS COPY DATAFILE` `n` `FORMAT` `auxname` regularly to maintain the updated image copy. For better performance, use an incrementally updated backup strategy to keep the image copies up-to-date without performing full backups of the data files.
3. When TSPITR is needed, specify a target time after the last update of the image copy.

#### Performing TSPITR with CONFIGURE AUXNAME and Image Copies: Scenario

Assume that you have enough disk space to save image copies of your entire database for use in TSPITR. In preparation for the possibility of TSPITR, you do the following:

- Configure an `AUXNAME` for each data file in the auxiliary set by using a command of the following form:
	```
	CONFIGURE AUXNAME FOR DATAFILE n TO auxname_n;
	```
- Take an image copy of the auxiliary set every Sunday by using a command of the following form:
	```
	BACKUP AS COPY DATAFILE n FORMAT auxname_n
	```
	If the image copies are all in the same location on disk, and if they are named similarly to the original data files, then you can avoid performing backups of every data file. Instead, you can use the `FORMAT` or `DB_FILE_NAME_CONVERT` options of the `BACKUP` command and use `BACKUP AS COPY DATABASE`. For example, if the configured auxiliary names are a translation of the location `maindisk` to `auxdisk`, then you use the following command:
	```
	BACKUP AS COPY 
	  DATABASE 
	  DB_FILE_NAME_CONVERT (maindisk, auxdisk);
	```
	Note:
	Because Oracle managed file names cannot generally be translated using a simple substitution, you cannot typically use `DB_FILE_NAME_CONVERT` to generate names for image copies stored in OMF.

After these steps, you are prepared for TSPITR without restoring the auxiliary set from backup. For example, if an erroneous batch job, started on November 15, 2007, at 19:00:00, incorrectly updates the tables in the tablespace `parts`, you use the following command to perform TSPITR on tablespace `parts`:

```
RECOVER TABLESPACE parts UNTIL TIME 'November 15 2007, 19:00:00';
```

Because `AUXNAME` locations are configured and refer to data file copies from an SCN before the TSPITR target time, the auxiliary set is not restored from backup. Instead, the data file copies are used in recovery, which reduces the restore overhead.

You can also prevent the recovery set from being restored. You must take frequent image copies of the tablespaces and use `SET NEWNAME` to specify the location of these copies. This method ensures that the recovery set is not restored, and the tablespace changes location after TSPITR successfully completes.

### Customizing Initialization Parameters for the Automatic Auxiliary Instance in TSPITR

The automatic auxiliary instance uses a set of default initialization parameters as shown in Table 21-4. It also looks for additional initialization parameters to complement the default parameters in a location that is operating system-dependent. For example, in UNIX this location is: `?/rdbms/admin/params_auxinst.ora`. RMAN always looks for this additional parameter file for an RMAN-automatic auxiliary instance when performing TSPITR. If the file is not found, then RMAN does not generate an error. Instead, RMAN uses the default parameters in Table 21-4 for the RMAN-managed automatic auxiliary instance.

Table 21-4 Default Initialization Parameters for the RMAN-Managed Auxiliary Instance

| Initialization Parameter | Value |
| --- | --- |
| `DB_NAME` | Same as `DB_NAME` of the source database |
| `COMPATIBLE` | Same as the `COMPATIBLE` setting of the target database |
| `DB_UNIQUE_NAME` | RMAN auto-generated unique value based on `DB_NAME` |
| `DB_BLOCK_SIZE` | Same as the `DB_BLOCK_SIZE` of the target database |
| `DB_CREATE_FILE_DEST` | Auxiliary destination (only if the `AUXILIARY DESTINATION` argument is specified when using an RMAN-managed auxiliary instance). RMAN creates Oracle Managed Files for the auxiliary set files in this location. |
| `LOG_ARCHIVE_DEST_1` | Auxiliary destination (only if the `AUXILIARY DESTINATION` clause is specified when using an RMAN-managed auxiliary instance). Archived logs needed for recovery are restored to this location. |
| `SGA_TARGET` | `280M` |
| `DB_FILES` | Same as `DB_FILES` of the target database |
| `PROCESSES` | `50` |

Usually it is not necessary to alter or add to the values of these initialization parameters, especially if you provide an `AUXILIARY DESTINATION` clause to the `RECOVER TABLESPACE` command when using a RMAN-managed auxiliary instance. If you override an initialization parameter in Table 21-4 with an inappropriate value, then TSPITR may fail due to problems with the auxiliary instance. Nevertheless, you can add other parameters besides these basic parameters if needed. For example, you can use `DB_FILE_NAME_CONVERT` to specify the names of the data files in the auxiliary and recovery sets.

To override or specify parameters for the automatic auxiliary instance, you can do either of the following:

- \- Place the initialization parameters in the operating system specific default auxiliary parameter file name. For example, in UNIX, the file name is `?/rdbms/admin/params_auxinst.ora`.
- Perform these steps:
	1. Place the initialization parameters in a file.
		2. Specify the location of this file with the `SET AUXILIARY INSTANCE PARAMETER FILE` command before executing TSPITR.

Regardless of the method that you choose, the parameters that you specify take precedence over defaults and can override the value of an `AUXILIARY DESTINATION` clause.

#### Specifying the Auxiliary Instance Control File Location in TSPITR

If you use an initialization parameter file, then you can specify your own location for the control file of your auxiliary instance. Set the `CONTROL_FILES` initialization parameter to specify a location for the control files.

If you do not explicitly specify a control file location, and if you use the `AUXILIARY DESTINATION` clause, then RMAN locates the control file in the auxiliary destination. If you do not use the `AUXILIARY DESTINATION` clause, then the auxiliary instance control files are stored in an operating system-specific location.

No matter where you store your auxiliary instance control file, it is removed at the end of the TSPITR operation. Because control files are relatively small, RMAN seldom encounters a problem creating an auxiliary control file. If there is not enough space to create the control file, however, then TSPITR fails.

#### Specifying the Auxiliary Instance Archived Logs in TSPITR

To perform recovery on the auxiliary and recovery sets after restoring them at the auxiliary instance, RMAN may need to restore archived logs. When an auxiliary destination is being used, the archived logs are restored to that location. In the absence of an auxiliary destination and any other initialization parameters, the archived logs are restored to an operating system specific location. For details, consult your operating system specific documentation. You can use the `LOG_ARCHIVE_DEST_1` initialization parameter to specify an alternative location where the archived logs are restored.

#### Specifying the Auxiliary Instance Online Log Location in TSPITR

If you specify the `LOG_FILE_NAME_CONVERT` initialization parameter in your auxiliary instance parameter file and the parameter successfully converts the names of the online redo logs of the target, then this parameter determines the online redo log location. The same restrictions that apply to OMF data files, apply to OMF online redo logs. For more information, see "Considerations When Renaming OMF Auxiliary Set Files in TSPITR". If RMAN is managing the auxiliary instance and an auxiliary destination is specified, RMAN creates the online redo log in the auxiliary destination.

Alternatively, you can use `DB_CREATE_FILE_DEST` or `DB_CREATE_FILE_DEST` and `DB_CREATE_ONLINE_LOG_1` to specify the location where the auxiliary instance redo logs are created. If you choose the latter option, you must use `DB_CREATE_ONLINE_LOG_1` with `DB_CREATE_FILE_DEST`.

TSPITR fails to create the online redo logs if you do not specify a location for them by using one of the following:

- `LOG_FILE_NAME_CONVERT`
- `DB_CREATE_FILE_DEST`
- `DB_CREATE_FILE_DEST` and `DB_CREATE_ONLINE_LOG_1`
- `AUXILIARY DESTINATION`

## Performing RMAN TSPITR Using Your Own Auxiliary Instance

Although Oracle recommends that you let RMAN manage all aspects of the auxiliary instance, there may be times when you must create and manage your own auxiliary instance. If you select this mode, you are responsible for setting up, starting, stopping and cleaning up the auxiliary instance used in TSPITR.

One reason that you might want to create your own instance is to exercise control of channels used in TSPITR. The automatic auxiliary instance uses the configured channels of the target database as the basis for the channels to configure on the auxiliary instance and to use during the restore operation. You may need different channel settings and may not want to use the `CONFIGURE` command to change the settings on the target database. In this case, you can operate your own auxiliary instance. By connecting to the auxiliary instance before invoking `RECOVER`, a run block can provide specific channel allocations using `the ALLOCATE AUXILIARY CHANNEL` command.

### Preparing Your Own Auxiliary Instance for RMAN TSPITR

Creating an Oracle instance suitable for use as an auxiliary instance requires that you complete all of the following steps:

- Step 1: Create an Oracle Password File for the Auxiliary Instance
- Step 2: Create an Initialization Parameter File for the Auxiliary Instance
- Step 3: Check Oracle Net Connectivity to the Auxiliary Instance

#### Step 1: Create an Oracle Password File for the Auxiliary Instance

For instructions on how to create and maintain Oracle password files, refer to [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN10241).

#### Step 2: Create an Initialization Parameter File for the Auxiliary Instance

Use a text editor to create an initialization parameter file for the auxiliary instance on the target database host. For this example, assume that your parameter file is placed at `/tmp/initAux.ora`. Set the parameters described in Table 21-5.

Note:

For TSPITR, the target and auxiliary database instances must be on the same host.

Table 21-5 Initialization Parameters in a User-Managed Auxiliary Instance

| Parameter | Mandatory? | Value |
| --- | --- | --- |
| `DB_NAME` | YES | The same name as the target database |
| `DB_UNIQUE_NAME` | YES | A value different from any database in the same Oracle home. For simplicity, specify `_` `dbname`. For example, if the target database name is `trgt`, then specify `_trgt`. |
| `REMOTE_LOGIN_PASSWORDFILE` | YES | Set to `EXCLUSIVE` when connecting to the auxiliary instance with a password file. Otherwise, set to `NONE`. |
| `COMPATIBLE` | YES | The same value as the parameter in the target database |
| `DB_BLOCK_SIZE` | YES | If this initialization parameter is set in the target database, then it must be set to the same value in the auxiliary instance. |
| `LOG_FILE_NAME_CONVERT` | NO | Patterns to generate file names for the online redo logs of the auxiliary database based on the online redo log names of the target database. Query `V$LOGFILE.MEMBER` to obtain target instance online redo log file names, and ensure that the conversion pattern matches the format of the file name shown in the view.  Note: Some platforms do not support ending patterns in a forward or backward slash (`\` or `/`).  See Also: "Specifying the Auxiliary Instance Online Log Location in TSPITR" for restrictions on possible values for `LOG_FILE_NAME_CONVERT` with OMF file names and "Considerations When Renaming OMF Auxiliary Set Files in TSPITR" |
| `DB_FILE_NAME_CONVERT` | NO | Patterns to convert file names for the data files of the auxiliary database. You can use this parameter to generate file names for those files that you did not name with `SET` `NEWNAME` or `CONFIGURE` `AUXNAME`. Obtain the data file names by querying `V$DATAFILE.NAME`, and ensure that the conversion pattern matches the format of the file name displayed in the view.  Note: Some platforms do not support ending patterns in a forward or backward slash (`\` or `/`).  See Also: "Using DB\_FILE\_NAME\_CONVERT to Name Auxiliary Set Data Files" and "Considerations When Renaming OMF Auxiliary Set Files in TSPITR". |
| `DB_CREATE_FILE_DEST` | NO | Use it to specify a location for all auxiliary set files. |
| `LOG_ARCHIVE_DEST_` `n` | NO | Use it to specify where archived logs required for recover are created. |
| `DB_CREATE_ONLINE_LOG_` `n` | NO | Use it with `DB_CREATE_FILE_DEST` to specify a different location where online redo logs are created. |
| `CONTROL_FILES` | NO | Filenames that do not conflict with the control file names of the target instance (or any other existing file). |
| `SGA_TARGET` | NO (Recommended) | `280M` |
| `STREAMS_POOL_SIZE` | NO  YES | If `SGA_TARGET` is set  If `SGA_TARGET` is not set |

Set other parameters as needed, including the parameters to specify how much memory the auxiliary instance uses.

The following example shows possible initialization parameter settings for an auxiliary instance for TSPITR:

```
DB_NAME=trgt
DB_UNIQUE_NAME=_trgt
CONTROL_FILES=/tmp/control01.ctl
DB_FILE_NAME_CONVERT=('/oracle/oradata/trgt/','/tmp/')
LOG_FILE_NAME_CONVERT=('/oracle/oradata/trgt/redo','/tmp/redo')
REMOTE_LOGIN_PASSWORDFILE=exclusive
COMPATIBLE =11.0.0
DB_BLOCK_SIZE=8192
```

Note:

After setting these initialization parameters, ensure that you do not overwrite the initialization settings for the production files at the target database.

#### Step 3: Check Oracle Net Connectivity to the Auxiliary Instance

The auxiliary instance must have a valid net service name. Before proceeding, use SQL\*Plus to ensure that you can establish a `SYSDBA` connection to the auxiliary instance.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for more information about Oracle Net

### Preparing RMAN Commands for TSPITR with Your Own Auxiliary Instance

If you run your own auxiliary instance, then it is possible for the sequence of commands required for TSPITR to be long. This situation can occur when you allocate a complex channel configuration for restoring from backup and you are not using `DB_CREATE_FILE_DEST` to determine file naming of auxiliary set files.

You may want to store the series of commands for TSPITR in an RMAN command file. Review the command file carefully to catch any errors. To read the command file into RMAN, use the `@` command (or the `CMDFILE` command-line argument when starting RMAN).

The following example runs the command file named `/tmp/tspitr.rman`:

```
@/tmp/tspitr.rman;
```

See Also:

["Using Command Files with RMAN"](rcmcnctg.md)

#### Planning Channels for TSPITR with Your Own Auxiliary Instance

When you run your own auxiliary instance, the default behavior is to use the automatic channel configuration of the target instance. If you decide to allocate your own channels with a different configuration (changing the number of channels or channel parameters), you can include `ALLOCATE AUXILIARY CHANNEL` commands in a `RUN` block along with the `RECOVER TABLESPACE` command for TSPITR. Plan out these commands, if necessary, and add them to the sequence of commands you run for TSPITR.

See Also:

"Performing TSPITR with Your Own Auxiliary Instance: Scenario" to learn how to include channel allocation in your TSPITR script

#### Planning Data File Names with Your Own Auxiliary Instance: SET NEWNAME

You may want to use `SET NEWNAME` commands to refer to existing image copies of auxiliary set files to improve TSPITR performance, or to assign new names to the recovery set files for after TSPITR. Plan these commands, if necessary, and add them to the sequence of commands that you run for TSPITR. For more information, see "Renaming TSPITR Recovery Set Data Files with SET NEWNAME".

### Executing TSPITR with Your Own Auxiliary Instance

With the preparations complete and your TSPITR commands completely planned, you are now ready to perform TSPITR. The following steps are required:

- Step 1: Start the Auxiliary Instance in NOMOUNT Mode
- Step 2: Connect the RMAN Client to Target and Auxiliary Instances
- Step 3: Execute the RECOVER TABLESPACE Command

#### Step 1: Start the Auxiliary Instance in NOMOUNT Mode

Before beginning RMAN TSPITR, start SQL\*Plus and connect to the auxiliary instance with `SYSOPER` privileges.

Start the auxiliary instance in `NOMOUNT` mode, specifying a parameter file if necessary. For example, enter the following SQL\*Plus command:

```
SQL> STARTUP NOMOUNT PFILE='/tmp/initAux.ora'
```

Remember that if you specify `PFILE`, then the path for the `PFILE` is a client-side path on the host from which you run SQL\*Plus.

Because the auxiliary instance does not yet have a control file, you can only start the instance in `NOMOUNT` mode. Do not create a control file or try to mount or open the auxiliary instance for TSPITR.

#### Step 2: Connect the RMAN Client to Target and Auxiliary Instances

Start RMAN and connect to the target database and the manually created auxiliary instance.

```
$rman target dba/dbapwd AUXILIARY aux/auxpwd@aux
```

#### Step 3: Execute the RECOVER TABLESPACE Command

In the simplest case, execute the `RECOVER TABLESPACE... UNTIL` command at the RMAN prompt:

```
RECOVER TABLESPACE ts1, ts2... UNTIL TIME 'time';
```

If you want to use the `ALLOCATE AUXILIARY CHANNEL` or `SET NEWNAME` commands, then include these commands before the `RECOVER TABLESPACE` command within a `RUN` command. The following example illustrates this technique:

```
RUN
{
   ALLOCATE AUXILIARY CHANNEL c1 DEVICE TYPE DISK;
   ALLOCATE AUXILIARY CHANNEL c2 DEVICE TYPE sbt;
  # and so on...
   RECOVER TABLESPACE ts1, ts2 UNTIL TIME 'time';
}
```

### Performing TSPITR with Your Own Auxiliary Instance: Scenario

This scenario shows the execution of a `RECOVER TABLESPACE... UNTIL` operation. This scenario illustrates the following features of RMAN TSPITR:

- Managing your own auxiliary instance
- Configuring channels for restore of backups from disk and [SBT](glossary.md) devices
- Using recoverable image copies for some auxiliary set data files using `SET NEWNAME`
- Specifying new names for recovery set data files using `SET NEWNAME`

To use TSPITR with your own auxiliary instance:

1. Prepare the auxiliary instance as described in "Preparing Your Own Auxiliary Instance for RMAN TSPITR". Specify a password for the auxiliary instance in the password file, and set up the auxiliary instance parameter file `/bigtmp/init_tspitr_prod.ora` with the following settings:
	```
	DB_NAME=PROD
	DB_UNIQUE_NAME=tspitr_PROD
	CONTROL_FILES=/bigtmp/tspitr_cntrl.dbf
	DB_CREATE_FILE_DEST=/bigtmp
	COMPATIBLE=11.0.0
	BLOCK_SIZE=8192
	REMOTE_LOGIN_PASSWORD=exclusive
	```
2. Create service name `pitprod` for the auxiliary instance, and check for connectivity.
3. Using SQL\*Plus, connect to the auxiliary instance with `SYSOPER` privileges. Start the instance in `NOMOUNT` mode:
	```
	SQL> STARTUP NOMOUNT PFILE=/bigtmp/init_tspitr_prod.ora
	```
4. Start RMAN and connect to the target and auxiliary database instances.
	```
	rman target / auxiliary sys/syspwd@pitprod
	```
5. Enter the following commands in a `RUN` block to set up and execute TSPITR:
	```
	RUN 
	{
	# Specify NEWNAME for recovery set data files
	  SET NEWNAME FOR TABLESPACE clients
	                        TO '?/oradata/prod/rec/%b';
	# Specify NEWNAMES for some auxiliary set 
	# data files that have a valid image copy to avoid restores:
	  SET NEWNAME FOR DATAFILE '?/oradata/prod/system01.dbf'
	                        TO '/backups/prod/system01_monday_noon.dbf';
	  SET NEWNAME FOR DATAFILE '?/oradata/prod/system02.dbf'
	                        TO '/backups/prod/system02_monday_noon.dbf';
	  SET NEWNAME FOR DATAFILE '?/oradata/prod/sysaux01.dbf'
	                        TO '/backups/prod/sysaux01_monday_noon.dbf';
	  SET NEWNAME FOR DATAFILE '?/oradata/prod/undo01.dbf'
	                        TO '/backups/prod/undo01_monday_noon.dbf';
	# Specify the types of channels to use
	  ALLOCATE AUXILIARY CHANNEL c1 DEVICE TYPE DISK;
	  ALLOCATE AUXILIARY CHANNEL t1 DEVICE TYPE sbt;
	# Recover the clients tablespace to 24 hours ago:
	  RECOVER TABLESPACE clients UNTIL TIME 'sysdate-1';
	}
	```

Consider storing this command sequence in a command file and executing the command file.

If the TSPITR operation is successful, then the results are:

- The recovery set data files are registered in the target database control file under the names specified with `SET NEWNAME`, with their contents as of the time specified time for TSPITR.
- The auxiliary files are removed by RMAN, including the control files, online logs, and auxiliary set data files of the auxiliary instance.
- The auxiliary instance is shut down.

If the TSPITR operation fails, the auxiliary set files are removed and the auxiliary instance is shut down. The recovery set files are left in the specified location and in an unresolved state from the failed TSPITR run.

## Troubleshooting RMAN TSPITR

A variety of problems can cause RMAN TSPITR to fail. This section lists possible areas to check and fix:

- Filename conflicts
- Mismatched or incorrect TSPITR target times for sets of tablespaces and undo segments
- Management issues with auxiliary instances not created by RMAN

### Troubleshooting Filename Conflicts

Name conflicts can occur between files already in the target database, file names assigned by the `SET NEWNAME` or `CONFIGURE AUXNAME` commands, and file names generated by the effect of the `DB_FILE_NAME_CONVERT` parameter.

Suppose that `SET NEWNAME`, `CONFIGURE AUXNAME`, and `DB_FILE_NAME_CONVERT` cause multiple files in the auxiliary or recovery sets to have the same name. In this case, RMAN reports an error during TSPITR. To correct the problem, use different values for these parameters.

### Troubleshooting the Identification of Tablespaces with Undo Segments

During TSPITR, RMAN needs information about which tablespaces had undo segments at the TSPITR target time. This information is usually available in the recovery catalog, if one is used.

If there is no recovery catalog or if the information is not found in the recovery catalog, RMAN assumes that the set of tablespaces with undo segments at the target time is the same as the set of tablespaces with undo segments at the present time. If this assumption is not correct, then TSPITR fails with an error. In this case, use the `UNDO` `TABLESPACE` clause to provide a list of tablespaces with undo segments at the target time.

### Troubleshooting the Restart of a Manual Auxiliary Instance After TSPITR Failure

If you are managing your own auxiliary instance and TSPITR fails, do not attempt to rerun TSPITR without resolving the errors and following this approach:

1. Identify and fix the problems that prevented TSPITR from a successful run.
2. Start the auxiliary instance in `NOMOUNT`.
3. Run TSPITR again.