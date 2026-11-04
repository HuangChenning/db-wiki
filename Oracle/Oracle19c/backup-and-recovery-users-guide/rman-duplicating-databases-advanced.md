---
title: "Duplicating Databases: Advanced Topics"
book: Backup and Recovery User Guide
doc_id: E96241-26
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-duplicating-databases-advanced.html
tags:
  - oracle
  - 19c
  - backup-and-recovery-users-guide
---

This chapter explains advanced forms of database duplication.

This chapter contains the following topics:

- Specifying Alternative Names for Duplicate Database Files
- Making Disk Backups Accessible Without Shared Disk

## Specifying Alternative Names for Duplicate Database Files

If the source database and duplicate database do not use the same names for database files, then you must choose an alternative naming strategy for the duplicate files.

Depending on whether the source and duplicate databases use Oracle Managed Files (OMF) or Oracle Automatic Storage Management (ASM), use one of the following strategies:

- Specifying Non-OMF or Non-ASM Alternative Names for Duplicate Database Files
- Using the CONFIGURE AUXNAME Command to Name File System Data Files and OMF or ASM Target Data Files
	If the source data files use OMF, then you cannot rename them by using the `DB_FILE_NAME_CONVERT` initialization parameter.[Using Non-ASM Storage](performing-rman-tspitr.md) discusses the details and options of OMF-managed data files.

### Specifying Non-OMF or Non-ASM Alternative Names for Duplicate Database Files

When the source and duplicate database either use different directory structures or use the same structure but you want to name the duplicate files differently, then you must specify how duplicate database files must be named. Table 26-1 summarizes the formats that are available for naming each type of file.

***Table 26-1 Substitution Variables for the SET NEWNAME Command***

| Variable | Description |
| --- | --- |
| `%b` | Specifies the file name stripped of directory paths. For example, if a data file is named `/oradata/prod/financial.dbf`, then `%b` results in `financial.dbf`. |
| `%f` | Specifies the absolute file number of the data file for which the new name is generated. For example, if data file 2 is duplicated, then `%f` generates the value 2. |
| `%I` | Specifies the DBID. |
| `%N` | Specifies the tablespace name. |
| `%U` | Specifies the following format: `data-D-%d_id-%I_TS-%N_FNO-%f` |

Use one of the following techniques to provide alternate names for non-OMF or non-ASM duplicate database files:

- Using the SET NEWNAME Command to Name File System Data Files and Temp Files
- Using the CONFIGURE AUXNAME Command to Name File System Data Files and OMF or ASM Target Data Files

#### Using the SET NEWNAME Command to Name File System Data Files and Temp Files

Use the `SET NEWNAME` command before you execute the `DUPLICATE` command to name duplicate data files.

RMAN supports the following commands, listed in order of precedence:

1. `SET NEWNAME FOR DATAFILE` and `SET NEWNAME FOR TEMPFILE`
2. `SET NEWNAME FOR TABLESPACE`
3. `SET NEWNAME FOR DATABASE`

The order of precedence means that the `SET NEWNAME FOR TABLESPACE` command specifies names for files that are not named by the `SET NEWNAME FOR DATAFILE` and `SET NEWNAME FOR TEMPFILE` commands, whereas the `SET NEWNAME FOR DATABASE` command specifies names for files that are not named by the `SET NEWNAME FOR TABLESPACE`, `SET NEWNAME FOR DATAFILE`, or `SET NEWNAME FOR TEMPFILE` commands.

When yo use the `SET NEWNAME FOR DATAFILE` command, you can specify a full path as a literal, as in `/oradata1/system01.dbf`. However, when you use the `SET` command with the `FOR DATABASE` or `FOR TABLESPACE` options, you must use at least one of these substitution variables, described in Table 26-1: `%b`, `%f`, `%U` (`%I` and `%N` are optional).

To use the `SET NEWNAME` command to specify new file names:

1. Ensure that the prerequisites for the selected duplication technique are met.
	See “ [Prerequisites for Duplicating a Database](rman-duplicating-databases.md) ”.
2. Complete the required planning tasks before you begin database duplication.
	See “ [Planning to Duplicate a Database](rman-duplicating-databases.md) ”.
3. Prepare the auxiliary instance that is used when you create the duplicate database.
	While duplicating an Oracle Real Application Clusters (Oracle RAC) database, set the `CLUSTER_DATABASE` initialization parameter on the auxiliary database to `FALSE`. This parameter can be reset to `TRUE` after the duplication process completes.
	See “ [Preparing the Auxiliary Instance](rman-duplicating-databases.md) ”.
4. Start RMAN and connect to required databases. Depending on your duplication technique, you may need to connect to one or more of the following: target database, auxiliary instance, or recovery catalog.
	See “ [Starting RMAN and Connecting to Databases](rman-duplicating-databases.md) ”.
5. Place the source database in a proper state, if necessary.
	See “ [Placing the Source Database in a Proper State](rman-duplicating-databases.md) ”.
6. (Optional) Configure RMAN channels to improve duplication performance. Channels perform the primary task of duplicating the database.
	See “ [Configuring RMAN Channels for Use in Duplication](rman-duplicating-databases.md) ”.
7. Within a `RUN` command, issue the `SET NEWNAME` command before you issue the `DUPLICATE` command.

***Example 26-1 Duplicating Databases with the SET NEWNAME FOR DATAFILE Command***

This example illustrates a script that specifies new names for data files 1 through 5 and temp file 1. The script does not set a new name for data file 6 because it is in the `TOOLS` tablespace, which is excluded from the duplicate database.

Assume the following:

- DBID is 87650928
- Database name is `PROD`

Use the following command to duplicate the database:

```md
RUN
{
SET NEWNAME FOR DATAFILE 1 TO '/oradata1/system01.dbf';
SET NEWNAME FOR DATAFILE 2 TO '/oradata2/sysaux01.dbf';
SET NEWNAME FOR DATAFILE 3 TO '/oradata3/undotbs01.dbf';
SET NEWNAME FOR DATAFILE 4 TO '/oradata4/users01.dbf';
SET NEWNAME FOR DATAFILE 5 TO '/oradata5/users02.dbf';
SET NEWNAME FOR TEMPFILE 1 TO '/oradatat/temp01.dbf';
DUPLICATE TARGET DATABASE TO dupdb
  SKIP TABLESPACE tools
  LOGFILE
     GROUP 1 ('/duplogs/redo01a.log','/duplogs/redo01b.log') SIZE 4M REUSE,
     GROUP 2 ('/duplogs/redo02a.log', '/duplogs/redo02b.log') SIZE 4M REUSE;
}
```

***Example 26-2 Duplicating Databases with the SET NEWNAME FOR DATAFILE and SET NEWNAME FOR TABLESPACE Commands***

This example is a variation of Example 26-1 and uses a single `SET NEWNAME` command to name all data files in the tablespace `users`. After the example completes, the file names for tablespace `users` are set to: `/oradata4/users01.dbf` and `/oradata5/users02.dbf`.

Use the following command to duplicate the database:

```md
{
SET NEWNAME FOR TABLESPACE users TO '/oradata%f/%b';
SET NEWNAME FOR DATAFILE 1 TO '/oradata1/system01.dbf';
SET NEWNAME FOR DATAFILE 2 TO '/oradata2/sysaux01.dbf';
SET NEWNAME FOR DATAFILE 3 TO '/oradata3/undotbs01.dbf';
SET NEWNAME FOR TEMPFILE 1 TO '/oradatat/temp01.dbf';
DUPLICATE TARGET DATABASE TO dupdb
SKIP TABLESPACE tools
LOGFILE
   GROUP 1 ('/duplogs/redo01a.log','/duplogs/redo01b.log') SIZE 4M REUSE,
   GROUP 2 ('/duplogs/redo02a.log','/duplogs/redo02b.log') SIZE 4M REUSE;
}
```

***Example 26-3 Duplicating Database with the SET NEWNAME FOR DATABASE Command***

This example is a variation of Example 26-1 and uses a single `SET` command to name all data files in the database.

Use the following command to duplicate the database:

```md
RUN
{
SET NEWNAME FOR DATABASE TO '/oradata/%U';
DUPLICATE TARGET DATABASE TO dupdb
  SKIP TABLESPACE tools
  LOGFILE
    GROUP 1 ('/duplogs/redo01a.log','/duplogs/redo01b.log') SIZE 4M REUSE,
    GROUP 2 ('/duplogs/redo02a.log','/duplogs/redo02b.log') SIZE 4M REUSE;
}
```

The following table shows the results from this example.

***Table 26-2 Results for the SET NEWNAME DATABASE Command***

| Before SET NEWNAME DATABASE | Tablespace Name | Data File Number | After SET NEWNAME DATABASE TO ‘/oradata/%U’; |
| --- | --- | --- | --- |
| `.../system01.dbf` | `SYSTEM` | 1 | `/oradata/data-D-PROD_id-87650928_TS-SYSTEM_FNO-1` |
| `.../sysaux01.dbf` | `SYSAUX` | 2 | `/oradata/data-D-PROD_id-87650928_TS-SYSAUX_FNO-2` |
| `.../undotbs01.dbf` | `UNDOTS` | 3 | `/oradata/data-D-PROD_id-87650928_TS-UNDOTS_FNO-3` |
| `.../users01.dbf` | `USERS` | 4 | `/oradata/data-D-PROD_id-87650928_TS-USERS_FNO-4` |
| `.../users02.dbf` | `USERS` | 5 | `/oradata/data-D-PROD_id-87650928_TS-USERS_FNO-5` |
| `.../temp01.dbf` | `TEMP` | 1 | `/oradata/data-D-PROD_id-87650928_TS-TEMP_FNO-1` |

**See Also:** [*Oracle Database Backup and Recovery Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=RCMRF-GUID-BC501B5C-4CD0-485D-AA18-27E2894024C3) for details on substitution variables usable in `SET NEWNAME`

#### Using the CONFIGURE AUXNAME Command to Name File System Data Files and OMF or ASM Target Data Files

The `CONFIGURE AUXNAME` command is an alternative to the `SET NEWNAME` command. The difference is that after you configure the auxiliary name the first time, additional `DUPLICATE` commands reuse the configured settings. In contrast, you must reissue the `SET NEWNAME` command every time you execute the `DUPLICATE` command.

To use the `CONFIGURE AUXNAME` command to specify names for duplicate data files:

1. Issue a `CONFIGURE AUXNAME` command for each file to name in the duplicate database.
	For example, enter the following commands at the RMAN prompt to specify names for files data files 1 through 5:
	```md
	CONFIGURE AUXNAME FOR DATAFILE 1 TO '/oradata1/system01.dbf';
	CONFIGURE AUXNAME FOR DATAFILE 2 TO '/oradata2/sysaux01.dbf';
	CONFIGURE AUXNAME FOR DATAFILE 3 TO '/oradata3/undotbs01.dbf';
	CONFIGURE AUXNAME FOR DATAFILE 4 TO '/oradata4/users01.dbf';
	CONFIGURE AUXNAME FOR DATAFILE 5 TO '/oradata5/users02.dbf';
	```
2. Issue a `DUPLICATE` command.
	For example, enter the following command at the RMAN prompt:
	```md
	SET NEWNAME FOR TEMPFILE 1 TO '/oradatat/temp01.dbf';
	DUPLICATE TARGET DATABASE
	  TO dupdb
	  SKIP TABLESPACE tools
	  LOGFILE
	     GROUP 1 ('/duplogs/redo01a.log','/duplogs/redo01b.log') SIZE 4M REUSE,
	     GROUP 2 ('/duplogs/redo02a.log','/duplogs/redo02b.log') SIZE 4M REUSE;
	```

**See Also:** [*Oracle Database Backup and Recovery Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=RCMRF-GUID-B5094E73-C26C-4FED-AE39-8C2E9540050A) for details on using `CONFIGURE AUXNAME`

### Specifying OMF or ASM Alternative Names for Duplicate Database Files

You must specify how to name duplicate database files when the source database and duplicate database do not use the same names for database files.

The following sections discuss requirements and procedures for creating a duplicate database when some or all files of the duplicate database use OMF or ASM:

- Settings and Restrictions for OMF Initialization Parameters
- Setting Initialization Parameters for ASM
- Examples: Duplicating Databases to ASM
- Using the SET NEWNAME Command to Create OMF or ASM Files
- Using the DB\_FILE\_NAME\_CONVERT Parameter to Generate Names for Non-OMF or ASM Data Files
- Using the LOG\_FILE\_NAME\_CONVERT Parameter to Generate Names for Non-OMF or ASM Log Files

**See Also:** *Oracle Automatic Storage Management Administrator’s Guide* for an introduction to ASM and OMF

#### Settings and Restrictions for OMF Initialization Parameters

When you create a duplicate database that uses OMF, you must set initialization parameters in the auxiliary instance. If you use the `SPFILE` option of the `DUPLICATE` command to name the files, then you can set initialization parameters in the `SPFILE` option. Table 26-3 describes the relevant parameters and recommended settings.

***Table 26-3 Initialization Parameters for Oracle Managed Files***

| Initialization Parameter | Purpose | Recommendation |
| --- | --- | --- |
| `DB_CREATE_FILE_DEST` | Specifies the default location for Oracle managed data files. This location is also the default location for Oracle managed control files and online logs if no `DB_CREATE_ONLINE_LOG_DEST` initialization parameters are specified. | Set this parameter to the location for OMF. Any database files that have no location specified are created in the directory specified by the `DB_CREATE_FILE_DEST` parameter. You can override the default for specific files by using the `SET NEWNAME` command, as described in “ Using the SET NEWNAME Command to Create OMF or ASM Files ”. |
| `DB_CREATE_ONLINE_LOG_DEST_n` | Specifies the default location for Oracle managed control files and online redo logs. If multiple parameters are set, then one control file and one online redo log is created in each location. | Set these parameters (\_1, \_2, and so on) only if you want to multiplex the control files and online redo log files in multiple locations. |
| `DB_RECOVERY_FILE_DEST` | Specifies the default location for the fast recovery area. The fast recovery area contains multiplexed copies of current control files and online redo log files. | Set this parameter if you want a multiplexed copy of the control file and online redo log file in the recovery area. |

Table 26-4 lists the restrictions on setting other initialization parameters.

***Table 26-4 Initialization Parameter Restrictions for Oracle Managed Files***

| Initialization Parameter | Purpose | Restriction |
| --- | --- | --- |
| `CONTROL_FILES` | Specifies one or more names of control files, separated by commas. | Do not set this parameter if you want the duplicate database control files in an OMF format. When you use control files in an OMF format, Oracle recommends that you use a server parameter file at the duplicate database. |
| `DB_FILE_NAME_CONVERT` | Converts the file name of a new data file on the primary database to a file name on the duplicate database. | Do not set this parameter. Omitting this parameter enables the database to generate valid Oracle managed file names for the duplicate data files. |
| `LOG_FILE_NAME_CONVERT` | Converts the file name of a new log file on the primary database to the file name of a log file on the standby database. | Do not set this parameter. Omitting this parameter allows the database to generate valid Oracle managed online redo log file names.  To direct duplicate database online redo log files to Oracle managed storage, you can use the `DB_CREATE_FILE_DEST`, `DB_RECOVERY_FILE_DEST`, or `DB_CREATE_ONLINE_LOG_DEST_n` initialization parameters to identify an Oracle managed location for the online logs. |

#### Setting Initialization Parameters for ASM

You must identify the initialization parameters that control the location where files are created and set these parameters to an ASM disk group.

The procedure for creating a duplicate database to an ASM location is similar to that of creating a duplicate database to OMF. For example, set the `DB_CREATE_FILE_DEST`, `DB_CREATE_ONLINE_DEST_n`, and `CONTROL_FILES` parameters to `+DISK1`.

**See Also:** Settings and Restrictions for OMF Initialization Parameters

#### Examples: Duplicating Databases to ASM

This section contains examples on duplicating databases to ASM.

***Example 26-4 Duplicating a Database from a File System to ASM***

In this example, you use active database duplication. If the source database uses a server parameter file (or a backup is available), then you can create a temporary initialization parameter file on the destination host and set only the `DB_NAME` parameter.

Assume that the source database `prod` is on `host1` and stores its data files in a non-ASM file system. The control files for `prod` are located in `/oracle/oradata/prod/`. You want to duplicate the source database to database `dupdb` on remote host `host2`. You want to store the duplicate database files in ASM disk group `+DISK1`.

After connecting RMAN to the target, duplicate, and recovery catalog databases, run the following RMAN script to duplicate the database.

```md
DUPLICATE TARGET DATABASE TO dupdb
FROM ACTIVE DATABASE
SPFILE
PARAMETER_VALUE_CONVERT '/oracle/oradata/prod/', '+DISK1'
SET DB_CREATE_FILE_DEST +DISK1;
```

When the `DUPLICATE` command completes, the duplicate database is created, with data files, online redo log files, and control files in ASM disk group `+DISK1`.

***Example 26-5 Duplicating a Database from ASM to ASM***

In this example, you use active database duplication. If the source database uses a server parameter file (or a backup is available), then you can create a temporary initialization parameter file on the destination host and set only the `DB_NAME` parameter.

Assume that the source database `prod` is on `host1` and stores its data files in ASM disk group `+DISK1`. You want to duplicate the target to database `dupdb` on remote host `host2`. You want to store the data files for `dupdb` in ASM. Specifically, you want to store the data files and control files in disk group `+DISK2`.

In the `DUPLICATE` command, set `PARAMETER_VALUE_CONVERT` to convert all directory locations from `+DISK1` to `+DISK2`. The new file names in `+DISK2` are generated by ASM and do not match the original file names in disk group `+DISK1`.

After connecting to the target, duplicate, and catalog databases, run the following RMAN script to duplicate the database.

```md
DUPLICATE TARGET DATABASE
TO dupdb
FROM ACTIVE DATABASE
SPFILE PARAMETER_VALUE_CONVERT '+DISK1','+DISK2'
SET DB_RECOVERY_FILE_DEST_SIZE='750G';
```

When the `DUPLICATE` command completes, the duplicate database is created, with data files, online redo logs, and control files in the larger ASM disk group `+DISK2`.

#### Using the SET NEWNAME Command to Create OMF or ASM Files

To name Oracle managed data files, you can use the `SET NEWNAME` command with the `TO NEW` option instead of the `TO 'filename'` option. RMAN creates the specified data files or temp files with OMF names in the location specified by the `DB_CREATE_FILE_DEST` parameter.

To use the `SET NEWNAME` command to specify names for OMF:

1. Set the `DB_CREATE_FILE_DEST` initialization parameter at the auxiliary instance to the desired location.
2. Enclose the `DUPLICATE` command in a `RUN` block and use the `SET NEWNAME` command with the `TO NEW` option for OMF.

***Example 26-6 Duplicating Databases with the SET NEWNAME FOR DATAFILE and SET NEWNAME FOR TABLESPACE Commands***

This example illustrates a script that specifies literal names for data files 1-5. The only Oracle Managed Files in the source database are the data files in the `users` tablespace. Therefore, the `TO NEW` option is specified in the `SET NEWNAME` command for these files.

```md
RUN
{
SET NEWNAME FOR TABLESPACE users TO NEW;
SET NEWNAME FOR DATAFILE 3 TO NEW;
SET NEWNAME FOR DATAFILE 1 TO '/oradata1/system01.dbf';
SET NEWNAME FOR DATAFILE 2 TO '/oradata2/sysaux01.dbf';
SET NEWNAME FOR TEMPFILE 1 TO '/oradatat/temp01';
DUPLICATE TARGET DATABASE TO dupdb
  SKIP TABLESPACE tools
  LOGFILE
    GROUP 1 ('/duplogs/redo01a.log','/duplogs/redo01b.log') SIZE 4M REUSE,
    GROUP 2 ('/duplogs/redo02a.log','/duplogs/redo02b.log') SIZE 4M REUSE;
}
```

***Example 26-7 Using the SET NEWNAME Command to Create Files in an ASM Disk Group***

This example uses the `SET NEWNAME` command to direct individual data files, temp files, or tablespaces to a specified ASM disk group.

```md
RUN
{
SET NEWNAME FOR DATAFILE 1 TO "+DGROUP1";
SET NEWNAME FOR DATAFILE 2 TO "+DGROUP2";
.
.
.
DUPLICATE TARGET DATABASE
TO dupdb
FROM ACTIVE DATABASE
SPFILE SET DB_CREATE_FILE_DEST +DGROUP3;
}
```

**See Also:** Using the SET NEWNAME Command to Name File System Data Files and Temp Files

#### Using the DB\_FILE\_NAME\_CONVERT Parameter to Generate Names for Non-OMF or ASM Data Files

In addition to using the `SET NEWNAME` or `CONFIGURE AUXNAME` commands, you can use the `DB_FILE_NAME_CONVERT` parameter to transform target file names. You can either specify the `DB_FILE_NAME_CONVERT` option in the `DUPLICATE` command or you can set it in the initialization parameter file of the auxiliary instance.

For example, you can change the target file name from the `/oracle/` directory to the `/dup/oracle/` directory. The `DB_FILE_NAME_CONVERT` parameter allows you to specify multiple conversion file name pairs, however, starting with Oracle Database 12c Release 2 (12.2), Oracle recommends that you do not exceed 99 pairs of file name strings. The `DB_FILE_NAME_CONVERT` parameter can also be used to produce names for data files and temp files.

**Restrictions of the DB\_FILE\_NAME\_CONVERT Parameter**

You cannot use the `DB_FILE_NAME_CONVERT` option of the `DUPLICATE` command to control generation of new names for files at the duplicate instance that are in the OMF format at the source database instance.

**See Also:** [*Oracle Database Backup and Recovery Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/bradv&id=RCMRF-GUID-E13D8A02-80F9-49A2-9C31-92DD3A795CE4)

#### Using the LOG\_FILE\_NAME\_CONVERT Parameter to Generate Names for Non-OMF or ASM Log Files

If the `LOG_FILE` clause has been omitted and none of the OMF initialization parameters `DB_CREATE_FILE_DEST`, `DB_CREATE_ONLINE_DEST_n`, or `DB_RECOVERY_FILE_DEST` are specified, then the `LOG_FILE_NAME_CONVERT` parameter can transform target file names. This works in the same way that the `DB_FILE_NAME_CONVERT` parameter does to transform target file names from `log_*` to `duplog_*`.

You can specify multiple conversion file name pairs with this parameter. When you specify the `LOG_FILE_NAME_CONVERT` parameter, RMAN uses the `REUSE` parameter when creating the online redo logs. If an online redo log file exists at the named location and is of the correct size, then it is reused for the duplication process.

**Restrictions of the LOG\_FILE\_NAME\_CONVERT Parameter**

- If you set OMF initialization parameters, do not specify the `LOG_FILE_NAME_CONVERT` parameter.
- The `LOG_FILE_NAME_CONVERT` parameter cannot be specified as a clause in the `DUPLICATE` command, it can only be specified in the initialization parameter of the auxiliary instance.
- You cannot use the `LOG_FILE_NAME_CONVERT` initialization parameter to control generation of new names for files at the duplicate instance that are in the OMF format at the source database instance.

## Making Disk Backups Accessible Without Shared Disk

You can use the shared disk technique to make backups available to the auxiliary instance. When NFS or shared disk is not an option, then the path that stores the backups must exist on *both* the source and destination hosts, unless the `BACKUP LOCATION` option is used for the `DUPLICATE` command without a target or recovery catalog connection.

Assume that you maintain two hosts, `srchost` and `dsthost`. The database on `srchost` is `srcdb`. The RMAN backups of `srcdb` reside in the `/dsk1/bkp` directory on host `srchost`. The directory `/dsk1/bkp` is in use on the destination host, so you intend to store backups in the `/dsk2/dup` directory on the destination host.

To transfer the backups from the source host to the destination host:

1. Create a directory in the source host that has the same name as the directory on the destination host that contains the backups.
	For example, if you intend to store the RMAN backups in the `/dsk2/dup` directory on the destination host, then create the `/dsk2/dup` directory on the source host.
2. On the source host, copy the backups to the directory created in the previous step, and then catalog the backups. You can use either of the following approaches:
	- Connect RMAN to the source database as `TARGET` and use the `BACKUP` command to back up the backups. For example, use the `BACKUP COPY OF DATABASE` command to copy the backups in `/dsk1/bkp` on the source host to `/dsk2/dup` on the source host. In this case, RMAN automatically catalogs the backups in the new location. If you are duplicating a PDB, then use the `PLUGGABLE DATABASE` syntax of the `BACKUP COPY OF` command to copy only the backups of the PDB.
		- Use an operating system utility to copy the backups in the `/dsk1/bkp` directory on the source host to the `/dsk2/dup` directory on the source host. Afterward, connect RMAN to the source database as `TARGET` and use the `CATALOG` command to update the source control file with the location of the manually transferred backups.
3. Manually transfer the backups in the new directory on the source host to the identically named directory on the destination host.
	For example, use FTP to transfer the backups in the `/dsk2/dup` directory on the source host to the `/dsk2/dup` directory on the destination host. The auxiliary channel can search for backups in the `/dsk2/dup` directory on the destination host and restore them.