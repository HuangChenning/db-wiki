---
title: "Duplicating a Database: Advanced Topics"
book: "Backup and Recovery User's Guide"
doc_id: E10642-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmdupad.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-users-guide
---

## 25 Duplicating a Database: Advanced Topics

This chapter explains advanced forms of database duplication that are not covered in [Chapter 24, "Duplicating a Database."](rcmdupdb.md)

This chapter contains the following topics:

## Specifying Alternative Names for Duplicate Database Files

["Step 2: Choosing a Strategy for Naming Duplicate Files"](rcmdupdb.md) explains the recommended strategy of using the same names for the duplicate and source database files. In all other cases, you must choose an alternative naming strategy for the duplicate files. The strategy that you use depends on whether the source and duplicate databases use Oracle Managed Files (OMF) or Oracle Automatic Storage Management (ASM).

If the source data files use OMF, then you cannot rename them using `DB_FILE_NAME_CONVERT`. ["Using Non-ASM Storage"](rcmtspit.md) discusses the details and options of OMF-managed data files.

### Specifying Non-OMF or Non-ASM Alternative Names for Duplicate Database Files

This section explains how to specify names for the duplicate files when the following condition is true:

The source and auxiliary hosts either use different directory structures or use the same structure but you want to name the duplicate files differently.

Table 25-1 summarizes the formats available for naming each type of file.

#### Using SET NEWNAME to Name File System Data Files and Temp Files

As shown in Table 25-1, one way to name duplicate data files is to use the `SET NEWNAME` command before executing the `DUPLICATE` command. RMAN supports the following commands, listed in order of precedence:

1. `SET NEWNAME FOR DATAFILE` and `SET NEWNAME FOR TEMPFILE`
2. `SET NEWNAME FOR TABLESPACE`
3. `SET NEWNAME FOR DATABASE`

The order of precedence means that `SET NEWNAME FOR TABLESPACE` specifies names for files not already named by `SET NEWNAME FOR DATAFILE` and `SET NEWNAME FOR TEMPFILE,` whereas `SET NEWNAME FOR DATABASE` specifies names for files not already named by `SET NEWNAME FOR TABLESPACE`, `SET NEWNAME FOR DATAFILE`, or `SET NEWNAME FOR TEMPFILE`.

When using `SET NEWNAME FOR DATAFILE`, you can specify a full path as a literal, as in `/oradata1/system01.dbf`. When using `SET` with `FOR DATABASE` or `FOR TABLESPACE`, however, you must use at least one of the first three substitution variables summarized in Table 25-1 (`%I` and `%N` are optional).

Table 25-1 Substitution Variables for SET NEWNAME

| Variable | Summary |
| --- | --- |
| `%b` | Specifies the file name stripped of directory paths. For example, if a data file is named `/oradata/prod/financial.dbf`, then `%b` results in `financial.dbf`. |
| `%f` | Specifies the absolute file number of the data file for which the new name is generated. For example, if data file `2` is duplicated, then `%f` generates the value `2`. |
| `%I` | Specifies the DBID |
| `%N` | Specifies the tablespace name |
| `%U` | Specifies the following format: `data-D-%d_id-%I_TS-%N_FNO-%f` |

To use SET NEWNAME to specify new file names:

1. Follow Steps 1 through 4 in ["Basic Steps of Database Duplication"](rcmdupdb.md).
2. Within a `RUN` command, issue the `SET NEWNAME` command before issuing `DUPLICATE`.
	Example 25-1 illustrates a script that specifies new names for data files `1` through `5` and temp file `1`. The script does not set a new name for data file `6` because it is in the `TOOLS` tablespace, which is excluded from the duplicate database.
	Example 25-1 Duplicating with SET NEWNAME FOR DATAFILE
	```
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
	      GROUP 1 ('/duplogs/redo01a.log', 
	               '/duplogs/redo01b.log') SIZE 4M REUSE, 
	      GROUP 2 ('/duplogs/redo02a.log', 
	               '/duplogs/redo02b.log') SIZE 4M REUSE;
	}
	```
	Example 25-2 is a variation of Example 25-1 and uses one `SET NEWNAME` command to name all data files in the tablespace `users`. Once the example completes, the file names for tablespace `users` are set to: `/oradata4/users01.dbf` and `/oradata5/users02.dbf`.
	Example 25-2 Duplicating with SET NEWNAME FOR DATAFILE and FOR TABLESPACE
	```
	RUN
	{
	  SET NEWNAME FOR TABLESPACE users TO '/oradata%f/%b';
	  SET NEWNAME FOR DATAFILE 1 TO '/oradata1/system01.dbf'; 
	  SET NEWNAME FOR DATAFILE 2 TO '/oradata2/sysaux01.dbf';
	  SET NEWNAME FOR DATAFILE 3 TO '/oradata3/undotbs01.dbf'; 
	  SET NEWNAME FOR TEMPFILE 1 TO '/oradatat/temp01.dbf'; 
	  DUPLICATE TARGET DATABASE TO dupdb
	    SKIP TABLESPACE tools
	    LOGFILE
	      GROUP 1 ('/duplogs/redo01a.log', 
	               '/duplogs/redo01b.log') SIZE 4M REUSE, 
	      GROUP 2 ('/duplogs/redo02a.log', 
	               '/duplogs/redo02b.log') SIZE 4M REUSE;
	}
	```
	Example 25-3 is a variation of Example 25-1 and uses a single `SET` command to name all data files in the database.
	Example 25-3 Duplicating with SET NEWNAME FOR DATABASE
	```
	RUN
	{
	  SET NEWNAME FOR DATABASE TO '/oradata/%U'; 
	  DUPLICATE TARGET DATABASE TO dupdb
	    SKIP TABLESPACE tools
	    LOGFILE
	      GROUP 1 ('/duplogs/redo01a.log', 
	               '/duplogs/redo01b.log') SIZE 4M REUSE, 
	      GROUP 2 ('/duplogs/redo02a.log', 
	               '/duplogs/redo02b.log') SIZE 4M REUSE;
	}
	```

Assume the following:

- `DBID` is `87650928`
- Database name is `PROD`

Table 25-2 shows the results from Example 25-3.

Table 25-2 Results from Example 25-3 SET NEWNAME DATABASE Command

| Before SET NEWNAME DATABASE | Tablespace Name | Data File File Number | After SET NEWNAME DATABASE TO '/oradata/%U'; |
| --- | --- | --- | --- |
| `.../system01.dbf` | `SYSTEM` | 1 | `/oradata/data-D-PROD_id-87650928_TS-SYSTEM_FNO-1` |
| `.../sysaux01.dbf` | `SYSAUX` | 2 | `/oradata/data-D-PROD_id-87650928_TS-SYSAUX_FNO-2` |
| `.../undotbs01.dbf` | `UNDOTS` | 3 | `/oradata/data-D-PROD_id-87650928_TS-UNDOTS_FNO-3` |
| `.../users01.dbf` | `USERS` | 4 | `/oradata/data-D-PROD_id-87650928_TS-USERS_FNO-4` |
| `.../users02.dbf` | `USERS` | 5 | `/oradata/data-D-PROD_id-87650928_TS-USERS_FNO-5` |
| `.../temp01.dbf` | `TEMP` | 1 | `/oradata/data-D-PROD_id-87650928_TS-TEMP_FNO-1` |

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2014.htm#RCMRF153) for details on substitution variables usable in `SET` `NEWNAME`

#### Using CONFIGURE AUXNAME to Name File System Data Files and OMF/ASM Target Data Files

The `CONFIGURE AUXNAME` command is an alternative to the `SET NEWNAME` command. The difference is that after you configure the auxiliary name the first time, additional `DUPLICATE` commands reuse the configured settings. In contrast, you must reissue the `SET NEWNAME` command every time you execute the `DUPLICATE` command.

To use CONFIGURE AUXNAME to specify names for duplicate data files:

1. Issue a `CONFIGURE AUXNAME` command for each file that you want to name in the duplicate database.
	For example, enter the following commands at the RMAN prompt to specify names for data files `1` through `5`:
	```
	CONFIGURE AUXNAME FOR DATAFILE 1 TO '/oradata1/system01.dbf'; 
	CONFIGURE AUXNAME FOR DATAFILE 2 TO '/oradata2/sysaux01.dbf';
	CONFIGURE AUXNAME FOR DATAFILE 3 TO '/oradata3/undotbs01.dbf';
	CONFIGURE AUXNAME FOR DATAFILE 4 TO '/oradata4/users01.dbf'; 
	CONFIGURE AUXNAME FOR DATAFILE 5 TO '/oradata5/users02.dbf';
	```
2. Issue a `DUPLICATE` command.
	For example, enter the following command at the RMAN prompt:
	```
	SET NEWNAME FOR TEMPFILE 1 TO '/oradatat/temp01.dbf'; 
	DUPLICATE TARGET DATABASE
	  TO dupdb
	  SKIP TABLESPACE tools
	  LOGFILE
	    GROUP 1 ('/duplogs/redo01a.log',
	             '/duplogs/redo01b.log') SIZE 4M REUSE,
	    GROUP 2 ('/duplogs/redo02a.log',
	             '/duplogs/redo02b.log') SIZE 4M REUSE;
	```
	RMAN uses the `CONFIGURE AUXNAME` settings to name data files `1` through `5`.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) for details on using `CONFIGURE` `AUXNAME`

### Specifying OMF or ASM Alternative Names for Duplicate Database Files

The following sections discuss requirements for creating a duplicate database when some or all files of the duplicate database use OMF or ASM.

See Also:

[Oracle Database Storage Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmcon.htm#OSTMG036) for an introduction to ASM and OMF

#### Settings and Restrictions for OMF Initialization Parameters

When creating a duplicate database that uses Oracle Managed Files, you must set initialization parameters in the auxiliary instance. If you use the `SPFILE` clause of `DUPLICATE` to name the files, then you can set initialization parameters in the `SPFILE` clause. Table 25-3 describes the relevant parameters and recommended settings and Table 25-4 lists the restrictions and initialization parameters that should not be set.

See:

[Oracle Database Reference f](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) or more information about these parameters.

Table 25-3 Initialization Parameters for Oracle Managed Files

| Initialization Parameter | Purpose | Recommendation |
| --- | --- | --- |
| [`DB_CREATE_FILE_DEST`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams053.htm#REFRN10034) | Specifies the default location for Oracle managed data files. This location is also the default location for Oracle managed control files and online logs if none of the `DB_CREATE_ONLINE_LOG_DEST` initialization parameters are specified. | Set this parameter to the location for the Oracle Managed Files. Any database files for which no other location is specified are created in `DB_CREATE_FILE_DEST` by `DUPLICATE`. You can override the default for specific files using `SET NEWNAME`, as described in "Using SET NEWNAME to Create OMF or ASM Files". |
| [`DB_CREATE_ONLINE_LOG_DEST_` n](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams054.htm#REFRN10035) | Specifies the default location for Oracle managed control files and online redo logs. If multiple parameters are set, then one control file and one online redo log is created in each location. | Set these parameters (`_1`, `_2`, and so on) only if you want to multiplex the control files and online redo log files in multiple locations. |
| [`DB_RECOVERY_FILE_DEST`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams065.htm#REFRN10234) | Specifies the default location for the fast recovery area. The fast recovery area contains multiplexed copies of current control files and online redo log files. | Set this parameter if you want a multiplexed copy of the control file and online redo log file in the recovery area. |

Table 25-4 Initialization Parameter Restrictions for Oracle Managed Files

| Initialization Parameter | Purpose | Restriction |
| --- | --- | --- |
| [`CONTROL_FILES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams037.htm#REFRN10021) | Specifies one or more names of control files, separated by commas. | Do not set this parameter if you want the duplicate database control files in an OMF format. Oracle recommends that you use a server parameter file at the duplicate database when using control files in an OMF format. |
| [`DB_FILE_NAME_CONVERT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams057.htm#REFRN10038) | Converts the file name of a new data file on the primary database to a file name on the duplicate database. | Do not set this parameter. Omitting this parameter enables the database to generate valid Oracle managed file names for the duplicate data files. |
| [`LOG_FILE_NAME_CONVERT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams137.htm#REFRN10098) | Converts the file name of a new log file on the primary database to the file name of a log file on the standby database. | Do not set this parameter. Omitting this parameter allows the database to generate valid Oracle managed online redo log file names.  To direct duplicate database online redo log files to Oracle managed storage, you can use the `DB_CREATE_FILE_DEST`, `DB_RECOVERY_FILE_DEST`, or `DB_CREATE_ONLINE_LOG_DEST_` `n` initialization parameters to identify an Oracle managed location for the online logs. |

#### Setting Initialization Parameters for ASM

The procedure for creating a duplicate database to an ASM location is similar to the procedure described in "Settings and Restrictions for OMF Initialization Parameters". The difference is that you must identify the initialization parameters that control the location where files are created and set these parameters to an ASM disk group. For example, set `DB_CREATE_FILE_DEST`, `DB_CREATE_ONLINE_DEST_` `n`, and `CONTROL_FILES` to `+DISK1`.

##### Duplicating a Database from a File System to ASM: Example

In this example, you use active database duplication. If the source database uses a server parameter file (or a backup is available), then you can create a temporary initialization parameter file on the destination host and set only the `DB_NAME` parameter.

Assume that the source database `prod` is on `host1` and stores its data files in a non-ASM file system. The control files for `prod` are located in `/oracle/oradata/prod/`. You want to duplicate the source database to database `dupdb` on remote host `host2`. You want to store the duplicate database files in ASM disk group `+DISK1`.

After connecting RMAN to the target, duplicate, and recovery catalog databases, run the RMAN script shown in Example 25-4 to duplicate the database.

Example 25-4 Duplicating from a File System to ASM (Active)

```
DUPLICATE TARGET DATABASE TO dupdb
  FROM ACTIVE DATABASE
  SPFILE 
    PARAMETER_VALUE_CONVERT '/oracle/oradata/prod/', '+DISK1'
    SET DB_CREATE_FILE_DEST +DISK1;
```

When the `DUPLICATE` command completes, the duplicate database is created, with data files, online redo log files, and control files in ASM disk group `+DISK1`.

##### Duplicating a Database from ASM to ASM: Example

In this example, you use active database duplication. If the source database uses a server parameter file (or a backup is available), then you can create a temporary initialization parameter file on the destination host and set only the `DB_NAME` parameter.

Assume that the source database `prod` is on `host1` and stores its data files in ASM disk group `+DISK1`. You want to duplicate the target to database `dupdb` on remote host `host2`. You want to store the data files for `dupdb` in ASM. Specifically, you want to store the data files and control files in disk group `+DISK2`.

In the `DUPLICATE` command, set `PARAMETER_VALUE_CONVERT` to convert all directory locations from `+DISK1` to `+DISK2`. The new file names in `+DISK2` are generated by ASM and do not match the original file names in disk group `+DISK1`.

After connecting to the target, duplicate, and catalog databases, run the RMAN script shown in Example 25-5 to duplicate the database.

Example 25-5 Duplicating from ASM to ASM (Active)

```
DUPLICATE TARGET DATABASE
  TO dupdb
  FROM ACTIVE DATABASE
  SPFILE PARAMETER_VALUE_CONVERT '+DISK1','+DISK2'
     SET DB_RECOVERY_FILE_DEST_SIZE='750G';
```

When the `DUPLICATE` command completes, the duplicate database is created, with data files, online redo logs, and control files in the larger ASM disk group `+DISK2`.

#### Using SET NEWNAME to Create OMF or ASM Files

To name Oracle managed data files, you can use the same `SET NEWNAME` commands described in "Using SET NEWNAME to Name File System Data Files and Temp Files", but with `TO NEW` instead of `TO '` `filename` `'`. RMAN creates the specified data files or temp files with Oracle Managed File names in the location specified by `DB_CREATE_FILE_DEST`.

To use SET NEWNAME to specify names for Oracle Managed Files:

1. Set the `DB_CREATE_FILE_DEST` initialization parameter at the auxiliary instance to the desired location
2. Enclose the `DUPLICATE` command in a `RUN` block and use `SET NEWNAME` with the `TO NEW` option for Oracle Managed Files.
	Example 25-6 illustrates a script that specifies literal names for data files `1` to `5`. The only Oracle Managed Files in the source database are the data files in the `users` tablespace. Therefore, `TO NEW` is specified in the `SET NEWNAME` command for these files.
	Example 25-6 Duplicating with SET NEWNAME FOR DATAFILE and FOR TABLESPACE
	```
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
	      GROUP 1 ('/duplogs/redo01a.log', 
	               '/duplogs/redo01b.log') SIZE 4M REUSE, 
	      GROUP 2 ('/duplogs/redo02a.log', 
	               '/duplogs/redo02b.log') SIZE 4M REUSE;
	}
	```
	As shown in Example 25-7, you can also use `SET` `NEWNAME` to direct individual data files, temp files, or tablespaces to a specified ASM disk group.
	Example 25-7 Using SET NEWNAME to Create Files in an ASM Disk Group
	```
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

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2014.htm#RCMRF153) for details on using `SET` `NEWNAME`

#### Using DB\_FILE\_NAME\_CONVERT to Generate Names for Non-OMF or ASM Data Files

Another technique to generate names besides using `SET NEWNAME` or `CONFIGURE AUXNAME` commands is to use `DB_FILE_NAME_CONVERT` to transform target file names. For example, you can change the target file name from `/oracle/` to `/dup/oracle/`. `DB_FILE_NAME_CONVERT` enables you to specify multiple conversion file name pairs. It can also be used to produce names for data files and temp files.

You can specify `DB_FILE_NAME_CONVERT` in the `DUPLICATE` command or you can set it in the initialization parameter of the auxiliary instance.

##### Restrictions of DB\_FILE\_NAME\_CONVERT:

You cannot use the `DB_FILE_NAME_CONVERT` clause of the `DUPLICATE` command to control generation of new names for files at the duplicate instance that are in the Oracle Managed Files (OMF) format at the source database instance. See [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/toc.htm) for details on this restriction.

#### Using LOG\_FILE\_NAME\_CONVERT to Generate Names for Non-OMF or ASM Log Files

If the `LOG_FILE` clause has been omitted and none of the Oracle Managed Files initialization parameters `DB_CREATE_FILE_DEST`, `DB_CREATE_ONLINE_DEST_n`, or `DB_RECOVERY_FILE_DEST` are specified, then `LOG_FILE_NAME_CONVERT` can transforms target file names. This works in much the same way as the `DB_FILE_NAME_CONVERT` and can transform target file names from `log_*` to `duplog_*`. You can specify multiple conversion file name pairs with this parameter.

When you specify `LOG_FILE_NAME_CONVERT`, RMAN uses the `REUSE` parameter when creating the online redo logs. If an online redo log file already exists at the named location and is of the correct size, then it is reused for the duplicate.

##### Restrictions of LOG\_FILE\_NAME\_CONVERT:

- Do not specify `LOG_FILE_NAME_CONVERT` if you set Oracle Managed Files initialization parameters.
- `LOG_FILE_NAME_CONVERT` cannot be specified as a `DUPLICATE` clause, it can only be specified in the initialization parameter of the auxiliary instance.
- You cannot use the `LOG_FILE_NAME_CONVERT` initialization parameter to control generation of new names for files at the duplicate instance that are in the Oracle Managed Files (OMF) format at the source database instance.

## Making Disk Backups Accessible Without Shared Disk

["Step 3: Making Backups Accessible to the Duplicate Instance"](rcmdupdb.md) recommends using the shared disk technique to make backups available to the auxiliary instance. When NFS or shared disk is not an option, then the path that stores the backups must exist on both the source and destination hosts unless the `BACKUP LOCATION` option is used for the DUPLICATE command without a target or recovery catalog connection.

Assume that you maintain two hosts, `srchost` and `dsthost`. The database on `srchost` is `srcdb`. The RMAN backups of `srcdb` reside in `/dsk1/bkp` on host `srchost`. The directory `/dsk1/bkp` is already in use on the destination host, so you intend to store backups in `/dsk2/dup` on the destination host.

To transfer the backups from the source host to the destination host:

1. Create a new directory in the source host that has the same name as the directory on the destination host that will contain the backups.
	For example, if you intend to store the RMAN backups in `/dsk2/dup` on the destination host, then create `/dsk2/dup` on the source host.
2. On the source host, copy the backups to the directory created in the previous step, and then catalog the backups. You can use either of the following approaches:
	- Connect RMAN to the source database as `TARGET` and use the `BACKUP` command to back up the backups, as explained in ["Backing Up RMAN Backups"](rcmbckba.md). For example, use the `BACKUP COPY OF DATABASE` command to copy the backups in `/dsk1/bkp` on the source host to `/dsk2/dup` on the source host. In this case, RMAN automatically catalogs the backups in the new location.
		- Use an operating system utility to copy the backups in `/dsk1/bkp` on the source host to `/dsk2/dup` on the source host. Afterward, connect RMAN to the source database as `TARGET` and use the `CATALOG` command to update the source control file with the location of the manually transferred backups.
3. Manually transfer the backups in the new directory on the source host to the identically named directory on the destination host.
	For example, use FTP to transfer the backups in `/dsk2/dup` on the source host to `/dsk2/dup` on the destination host.

The auxiliary channel can search for backups in `/dsk2/dup` on the destination host and restore them.

## Duplicating a Database When No Server Parameter File Exists

The procedure in ["Step 5: Creating an Initialization Parameter File and Starting the Auxiliary Instance"](rcmdupdb.md) assumes that you use the `SPFILE` clause of the `DUPLICATE` command. If the source database does not use a server parameter file, then you must set all necessary parameters for the auxiliary instance in a text-based initialization parameter file.

Table 25-5 describes a subset of the possible initialization parameters. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) provides more information about these parameters. See Table 25-1 to learn about options for naming duplicate files.

Table 25-5 Auxiliary Instance Initialization Parameters

| Initialization Parameter | Value | Status |
| --- | --- | --- |
| [`DB_NAME`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams064.htm#REFRN10041) | The same name used in the `DUPLICATE` command. If you are using `DUPLICATE` to create a standby database, then the name must be the same as the primary database.  The `DB_NAME` setting for the duplicate database must be unique among databases in its Oracle home. | Required |
| [`CONTROL_FILES`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams037.htm#REFRN10021) | Control file locations | Required |
| [`DB_BLOCK_SIZE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams050.htm#REFRN10031) | The block size for the duplicate database. This block size must match the block size of the source database. If the source database parameter file contains a value for the `DB_BLOCK_SIZE` initialization parameter, then you must specify the same value for the auxiliary instance. If no `DB_BLOCK_SIZE` is specified in the source database initialization parameter file, however, then do not specify `DB_BLOCK_SIZE` in the auxiliary instance. | Required if this initialization parameter is set in the source database |
| [`DB_FILE_NAME_CONVERT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams057.htm#REFRN10038) | Pairs of strings for converting the names of data files and temp files. You can also specify `DB_FILE_NAME_CONVERT` on the `DUPLICATE` command itself. See "Using DB\_FILE\_NAME\_CONVERT to Generate Names for Non-OMF or ASM Data Files". | Optional |
| [`LOG_FILE_NAME_CONVERT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams137.htm#REFRN10098) | Pairs of strings for naming online redo log files. See "Using LOG\_FILE\_NAME\_CONVERT to Generate Names for Non-OMF or ASM Log Files". | Optional |
| [`DB_CREATE_FILE_DEST`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams053.htm#REFRN10034) | Location for Oracle managed data files. | Optional |
| [`DB_CREATE_ONLINE_LOG_DEST` \_ `n`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams054.htm#REFRN10035) | Location for Oracle managed online redo log files | Optional |
| [`DB_RECOVERY_FILE_DEST`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams065.htm#REFRN10234) | Location for fast recovery area | Optional |
| Oracle Real Application Cluster (Oracle RAC) parameters:  - \<INSTANCESIDn>.`INSTANCE_NAME` - \<INSTANCESIDn>.`INSTANCE_NUMBER` - \<INSTANCESIDn>.`THREAD` - \<INSTANCESIDn>.`UNDO_TABLESPACE` - \<INSTANCESIDn>.`LOCAL_LISTENER` | Set these parameters for each instance of the Oracle RAC database. | Required for Oracle RAC configuration |

To create an initialization parameter file when not planning to use the SPFILE clause:

1. Use an operating system utility to make a copy of the initialization parameter file of the source database in the operating system-specific default location.
2. In the copied initialization parameter file, manually change `DB_NAME` to the name of the duplicate database. If you are using `DUPLICATE` to create a standby database, then the name must be the same as the primary database.
3. If necessary, change other initialization parameters, including the parameters that allow you to connect as `SYSDBA` through Oracle Net, as needed. You must verify that all paths are accessible on the host where the database is being duplicated.
	Example 25-8 shows a sample initialization parameter file.
	Example 25-8 Sample Initialization Parameter File for the Auxiliary Instance
	```
	DB_NAME=dupdb
	CONTROL_FILES=(/dup/oracle/oradata/prod/control01.ctl,
	               /dup/oracle/oradata/prod/control02.ctl)
	DB_FILE_NAME_CONVERT=(/oracle/oradata/prod/,/dup/oracle/oradata/prod/)
	LOG_FILE_NAME_CONVERT=(/oracle/oradata/prod/redo,/dup/oracle/oradata/prod/redo)
	```

## Starting the Auxiliary Instance When No Server Parameter File Exists

["Step 5: Creating an Initialization Parameter File and Starting the Auxiliary Instance"](rcmdupdb.md) assumes that the source database instance uses a server parameter file. This scenario assumes that the source database does not currently use a server parameter file or RMAN cannot restore a backup server parameter file. In this case, you must start the auxiliary instance with a text-based initialization parameter file.

To start the auxiliary instance in preparation for database duplication:

1. Copy the text-based initialization parameter file to the default location on the host containing the SQL\*Plus client.
2. Start SQL\*Plus and connect to the auxiliary instance with `SYSOPER` privileges.
3. Start the auxiliary instance in `NOMOUNT` mode, using the text-based initialization parameter file:
	```
	SQL> STARTUP NOMOUNT
	```
4. Copy the text-based initialization parameter file for the auxiliary instance to the same host as the RMAN client used to perform the duplication. You must specify the location of this text-based initialization parameter file in the `PFILE` clause of the `DUPLICATE` command.

## Duplicating a Subset of the Source Database Tablespaces

It is not always necessary to duplicate all tablespaces of a database. For example, you may plan to generate reports that require only a subset of tablespaces from your source database.

Note:

When excluding tablespaces in backup-based duplication without a target connection or without a target and a recovery catalog connection, RMAN has special prerequisites. See the Prerequisites section of the `DUPLICATE` entry in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta020.htm#RCMRF126) for details.

Table 25-6 explains `DUPLICATE` command options for specifying subsets of tablespaces for the duplicate database.

Table 25-6 Options to Specify Subsets of Tablespaces for the Duplicate Database

| DUPLICATE Options | Explanation |
| --- | --- |
| `SKIP READONLY` | Excludes the data files of read-only tablespaces from the duplicate database |
| `SKIP TABLESPACE` `'tablespace_name ', ...` | Excludes the specified tablespaces from the duplicate database. You cannot exclude the `SYSTEM` and `SYSAUX` tablespaces, tablespaces with `SYS` objects, undo tablespaces, tablespaces with undo segments, tablespaces with materialized views, or tablespaces in such a way that the duplicated tablespaces are not self-contained. |
| `TABLESPACE` `'tablespace_name ', ...` | Automatically includes the `SYSTEM`, `SYSAUX`, and undo tablespaces. The included tablespaces must be self-contained and the resulting skipped tablespaces must not contain `SYS` objects or materialized views. |

To specify a subset of tablespaces for a duplicate database:

1. Ensure that you have completed Steps 1 through 4 in ["Basic Steps of Database Duplication"](rcmdupdb.md).
2. Run the `DUPLICATE` command with one or more of the options in Table 25-6.

Other factors that influence what tablespaces are copied include the `OFFLINE NORMAL` option. When tablespaces are taken offline with the `OFFLINE NORMAL` option before duplication, RMAN does not duplicate the associated data files, and issues `DROP TABLESPACE` statement for these tablespaces on the duplicate database. Therefore, you do not have to specify options to exclude these tablespaces.

Note:

RMAN does duplicate tablespaces that are taken offline with any other option besides `NORMAL` (unless they are named in a `SKIP TABLESPACE` option). Only `OFFLINE NORMAL` tablespaces are skipped automatically. As with online tablespaces, RMAN requires a valid backup for these tablespaces when you use backup-based duplication.

### Excluding Specified Tablespaces

Example 25-9 shows how to skip read-only tablespaces.

Example 25-9 Excluding Read-Only Tablespaces

```
DUPLICATE TARGET DATABASE TO dupdb
  FROM ACTIVE DATABASE
  SKIP READONLY
  NOFILENAMECHECK;
```

Example 25-10 shows how to skip a tablespace named `tools`.

Example 25-10 Excluding Specified Tablespaces

```
DUPLICATE TARGET DATABASE 
  TO dupdb
  FROM ACTIVE DATABASE
  SKIP TABLESPACE tools
  NOFILENAMECHECK;
```

### Including Specified Tablespaces

You can use the `TABLESPACE` option to specify which tablespaces to include in the specified database. Unlike the `SKIP TABLESPACE` option, which specifies which tablespaces to exclude from the duplicate database, this option specifies which tablespaces to include and then skips the remaining tablespaces. The duplicated subset of tablespaces must be self-contained. The resulting set of skipped tablespaces must not have undo segments or materialized views.

Example 25-11 is a variation of [Example 24-1](rcmdupdb.md) except with the `users` tablespace included, which is assumed to be self-contained, and all other tablespaces excluded, except for `SYSTEM` and `SYSAUX` tablespaces and tablespaces with undo segments.

Example 25-11 Including Specified Tablespaces

```
DUPLICATE TARGET DATABASE 
  TO dupdb
  FROM ACTIVE DATABASE
  TABLESPACE users
  NOFILENAMECHECK;
```

Assume that you perform backup-based duplication with a target connection, but no recovery catalog connection. Assume that you want to specify a subset of tablespaces for duplication. If the target database is not open in this scenario, then RMAN has no way to obtain the names of the tablespaces with undo segments. Thus, you must specify the `UNDO TABLESPACE` option for these tablespaces as shown in Example 25-12.

Example 25-12 Including Specified Tablespaces

```
DUPLICATE TARGET DATABASE TO dupdb
  TABLESPACE users
  UNDO TABLESPACE undotbs
  NOFILENAMECHECK;
```