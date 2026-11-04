---
title: Configuring the RMAN Environment
book: "Backup and Recovery User's Guide"
doc_id: E10642-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfb.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-users-guide
---

## 5 Configuring the RMAN Environment

This chapter explains the most basic tasks involved in configuring RMAN. This chapter contains the following topics:

See Also:

- [Chapter 6, "Configuring the RMAN Environment: Advanced Topics"](rcmconfa.md) to learn about configuration options not covered in this chapter, including backup compression and encryption
- Appendix C in the [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/web_services.htm#RCMRF90489) for information about configuring RMAN for the Oracle Secure Backup (OSB) Cloud Module.

## Configuring the Environment for RMAN Backups

For most parameters required for backups, RMAN provides sensible defaults that enable you to perform basic backup and recovery. When implementing an RMAN-based backup strategy, you can use RMAN more effectively if you understand the most common configurations.

To simplify ongoing use of RMAN, you can set some persistent configuration settings for each target database. These settings control many aspects of RMAN behavior. For example, you can configure the backup retention policy, default destinations for backups, default backup device type, and so on. You can use the [`SHOW`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2015.htm#RCMRF154) and [`CONFIGURE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) commands to view and change RMAN configurations.

This section explains what an RMAN configuration is and how you can use the `CONFIGURE` command to change RMAN default behavior for your backup and recovery environment. This section also introduces the major settings available to you and their more common values.

Note:

If you plan to back up to tape, refer to "Configuring RMAN to Make Backups to a Media Manager".

This section includes the following topics:

- Showing and Clearing Persistent RMAN Configurations
- Configuring the Default Device for Backups: Disk or SBT
- Configuring the Default Type for Backups: Backup Sets or Copies
- Configuring Channels
- Configuring Control File and Server Parameter File Autobackups

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) for `CONFIGURE` syntax

### Showing and Clearing Persistent RMAN Configurations

You can use the `SHOW` command to display the current value of RMAN configured settings for the target database. You can also view whether these commands are currently set to their default values.

To view or change your CONFIGURE command settings:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. Run the RMAN `SHOW` command.
	For example, run `SHOW ALL` as shown in Example 5-1 (sample output included). The output includes both parameters that you have changed and those that are set to the default. The configuration is displayed as the series of RMAN commands required to re-create the configuration. You can save the output in a text file and use this command file to re-create the configuration on the same or a different database.
	Example 5-1 SHOW ALL Command
	```
	SHOW ALL;
	RMAN configuration parameters for database with db_unique_name PROD1 are:
	CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 3 DAYS;
	CONFIGURE BACKUP OPTIMIZATION ON;
	CONFIGURE DEFAULT DEVICE TYPE TO DISK; # default
	CONFIGURE CONTROLFILE AUTOBACKUP ON;
	CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE SBT_TAPE TO '%F'; # default
	CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK TO '%F'; # default
	CONFIGURE DEVICE TYPE 'SBT_TAPE' PARALLELISM 2 BACKUP TYPE TO COMPRESSED BACKUPSET;
	CONFIGURE DEVICE TYPE DISK PARALLELISM 1 BACKUP TYPE TO BACKUPSET; # default
	CONFIGURE DATAFILE BACKUP COPIES FOR DEVICE TYPE SBT_TAPE TO 1; # default
	CONFIGURE DATAFILE BACKUP COPIES FOR DEVICE TYPE DISK TO 1; # default
	CONFIGURE ARCHIVELOG BACKUP COPIES FOR DEVICE TYPE SBT_TAPE TO 1; # default
	CONFIGURE ARCHIVELOG BACKUP COPIES FOR DEVICE TYPE DISK TO 1; # default
	CONFIGURE CHANNEL DEVICE TYPE 'SBT_TAPE' PARMS 'ENV=(OB_DEVICE=tape1)';
	CONFIGURE MAXSETSIZE TO UNLIMITED; # default
	CONFIGURE ENCRYPTION FOR DATABASE OFF; # default
	CONFIGURE ENCRYPTION ALGORITHM 'AES128'; # default
	CONFIGURE ARCHIVELOG DELETION POLICY TO NONE; # default
	CONFIGURE SNAPSHOT CONTROLFILE NAME TO '/disk1/oracle/dbs/snapcf_ev.f'; # default
	```
	You can also use the `SHOW` command with the name of a particular configuration. For example, you can view the retention policy and default device type as follows:
	```
	SHOW RETENTION POLICY;
	SHOW DEFAULT DEVICE TYPE;
	```
3. Optionally, use the `CONFIGURE ... CLEAR` command to return any configuration to its default value, as shown in the following examples:
	```
	CONFIGURE BACKUP OPTIMIZATION CLEAR;
	CONFIGURE RETENTION POLICY CLEAR;
	CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK CLEAR;
	```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2015.htm#RCMRF154) for `SHOW` syntax

### Configuring the Default Device for Backups: Disk or SBT

Backups for which no destination device type is specified are directed to the configured default device. RMAN is preconfigured to use disk as the default device type. No additional configuration is necessary.

You may need to change the default device type from disk to tape, or change it back from tape to disk. Table 5-1 shows the commands that configure the default device.

Table 5-1 Commands to Configure the Default Device Type

| Command | Explanation |
| --- | --- |
| `CONFIGURE DEFAULT DEVICE TYPE TO DISK` | Specifies that backups should go to disk by default.  If a recovery area is enabled, then the backup location defaults to the [fast recovery area](glossary.md). Otherwise, the backup location defaults to an operating system-specific directory on disk.  When backing up to disk, the logical block size of the database file must be an even multiple of the physical block size of the destination device. For example, a device of type DISK with a block size of 2 kilobytes can only be used as a destination for backups of database files with logical block sizes of 2 KB, 4 KB, 6 KB, and so on. Most disk drives have physical block sizes of 512 bytes, so this limitation rarely affects backup to disk drives. Nevertheless, you can encounter this limitation when backing up to a writable DVD or a device that has a larger physical block size. |
| `CONFIGURE DEFAULT DEVICE TYPE TO sbt` | Specifies that backups should go to tape by default.  "Configuring RMAN to Make Backups to a Media Manager" explains how to set up RMAN for use with a media manager. After RMAN can communicate with the media manager, you can configure RMAN to make backups to tape and specify [SBT](glossary.md) as the default device type. |

You can always override the default device by using the `DEVICE` `TYPE` clause of the [`BACKUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) command, as shown in the following examples:

```
BACKUP DEVICE TYPE sbt DATABASE;
BACKUP DEVICE TYPE DISK DATABASE;
```

To change the configured default device type:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. Run the `SHOW ALL` command to show the currently configured default device.
3. Run the `CONFIGURE DEFAULT DEVICE TYPE` command, specifying either `TO DISK` or `TO sbt`.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) for more details on using the `BACKUP` command with the `DEVICE` `TYPE` clause

### Configuring the Default Type for Backups: Backup Sets or Copies

The [`BACKUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) command can create either backup sets or image copies. For disk, you can configure RMAN to create either backup sets or image copies as its default backup type with the `CONFIGURE DEVICE TYPE DISK BACKUP TYPE TO` command. The default backup type for disk is an uncompressed [backup set](glossary.md).

Note:

Because RMAN can write an [image copy](glossary.md) only to disk, the backup type for tape can only be a backup set.

RMAN can create backup sets using [binary compression](glossary.md). You can configure RMAN to use compressed backup sets by default on a device type by specifying the `COMPRESSED` option in the `BACKUP TYPE TO ... BACKUPSET` clause. To disable compression, use the `CONFIGURE DEVICE TYPE` command with arguments specifying your other desired settings, but omit the `COMPRESSED` keyword.

To configure the default type of backup:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. Configure backup sets or image copies as the default backup type.
	The following examples configure the backup type for disk backups to copies and backup sets:
	```
	CONFIGURE DEVICE TYPE DISK BACKUP TYPE TO COPY; # image copies
	CONFIGURE DEVICE TYPE DISK BACKUP TYPE TO BACKUPSET; # uncompressed
	```
	The following examples configure compression for backup sets:
	```
	CONFIGURE DEVICE TYPE DISK BACKUP TYPE TO COMPRESSED BACKUPSET;
	CONFIGURE DEVICE TYPE sbt BACKUP TYPE TO COMPRESSED BACKUPSET;
	```
	See Also:
	- [Backup Sets](rcmcncpt.md)
	- [Making Compressed Backups](rcmbckba.md)

### Configuring Channels

As explained in ["RMAN Channels"](rcmarchi.md), an RMAN [channel](glossary.md) is a connection to a database server session. RMAN uses channels to perform most tasks.

#### About Channel Configuration

Use the `CONFIGURE` `CHANNEL` command to configure options for disk or [SBT](glossary.md) channels. `CONFIGURE` `CHANNEL` takes the same options used to specify one-time options with the [`ALLOCATE CHANNEL`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta004.htm#RCMRF102) command. You can configure generic channel settings for a device type, that is, a template that is used for any channels created based on configured settings for that device.

Note:

This section explains configuration of disk channels. To learn how to configure channels for tape, see "Configuring SBT Channels for Use with a Media Manager".

If you use `CONFIGURE` `CHANNEL` to specify generic channel settings for a device, any previous settings are discarded, even if the settings are not in conflict. For example, after the second `CONFIGURE` `CHANNEL` command, which specifies only the [`FORMAT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl010.htm#RCMRF195) for configured disk channels, the `MAXPIECESIZE` for the disk channel is returned to its default value:

```
CONFIGURE CHANNEL DEVICE TYPE DISK MAXPIECESIZE 2G;
CONFIGURE CHANNEL DEVICE TYPE DISK FORMAT /tmp/%U;
```

#### Configuring Channels for Disk

By default, RMAN allocates one disk channel for all operations. You may want to specify different options for this channel, for example, a new default location for backups. Example 5-2 configures RMAN to write disk backups to the `/disk1` directory and specifies a nondefault format for the relative file name.

Example 5-2 Configuring a Nondefault Backup Location

```
CONFIGURE CHANNEL DEVICE TYPE DISK FORMAT '/disk1/ora_df%t_s%s_s%p';
```

In Example 5-2, RMAN automatically replaces the format specifier `%t` with a four byte time stamp, `%s` with the backup set number, and `%p` with the backup piece number.

Note:

When you configure an explicit format for disk channels, RMAN does not create backups by default in the [fast recovery area](glossary.md). In this case, you lose the disk space management capabilities of the fast recovery area.

You can also specify an ASM disk location, as shown in Example 5-3:

Example 5-3 Configuring an ASM Disk Location

```
CONFIGURE CHANNEL DEVICE TYPE DISK FORMAT '+dgroup1';
```

See Also:

["Backing Up Database Files with RMAN"](rcmbckba.md) to learn how to make backups

#### Configuring Parallel Channels for Disk and SBT Devices

The number of channels available for a device type when you run a command determines whether RMAN reads or writes in parallel. As a rule, the number of channels used in executing a command should match the number of devices accessed. Thus, for tape backups, allocate one channel for each tape drive. For disk backups, allocate one channel for each physical disk, unless you can optimize the backup for your disk subsystem architecture with multiple channels. Failing to allocate the right number of channels adversely affects RMAN performance during I/O operations.

You can configure [channel parallelism](glossary.md) settings, [binary compression](glossary.md) for backup sets, and other options for an [SBT](glossary.md) device with `CONFIGURE` `DEVICE` `TYPE` `sbt`. You set the configuration for the device type independently of the channel configuration.

Example 5-4 changes the SBT device (sample output included) so that RMAN can back up to a media manager using two tape drives in parallel. Each configured SBT channel backs up approximately half the total data.

Example 5-4 Configuring Parallelism for an SBT Device

```
RMAN> CONFIGURE DEVICE TYPE sbt PARALLELISM 2;

old RMAN configuration parameters:
CONFIGURE DEVICE TYPE 'SBT_TAPE' BACKUP TYPE TO COMPRESSED BACKUPSET PARALLELISM 1;
new RMAN configuration parameters:
CONFIGURE DEVICE TYPE 'SBT_TAPE' PARALLELISM 2 BACKUP TYPE TO COMPRESSED BACKUPSET;
new RMAN configuration parameters are successfully stored
```

Example 5-5 changes the default backup type for the SBT device to an uncompressed backup set (sample output included).

Example 5-5 Configuring the Backup Type for an SBT Device

```
RMAN> CONFIGURE DEVICE TYPE sbt BACKUP TYPE TO BACKUPSET;
 
old RMAN configuration parameters:
CONFIGURE DEVICE TYPE 'SBT_TAPE' PARALLELISM 2 BACKUP TYPE TO COMPRESSED BACKUPSET;
new RMAN configuration parameters:
CONFIGURE DEVICE TYPE 'SBT_TAPE' BACKUP TYPE TO BACKUPSET PARALLELISM 2;
new RMAN configuration parameters are successfully stored
```

The `CONFIGURE DEVICE TYPE` commands used in this example only affect parallelism and backup type and do not affect the values of settings not specified. In Example 5-4, the default backup type of compressed backup set was not changed by changing the parallelism setting. In Example 5-5, the ability to use multiple tape drives in parallel was not affected by changing the default backup type.

See Also:

- ["Specifying Multiple Formats for Disk Backups"](rcmbckba.md) to learn how to make disk backups in parallel
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) for reference material on the `CHANNEL` parameter of the `BACKUP` command
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for information about taking advantage of parallel operations in an Oracle Real Application Clusters (Oracle RAC) configuration

#### Manually Overriding Configured Channels

If you manually allocate a channel during a job, then RMAN disregards any configured channel settings. For example, assume that the default device type is SBT, and you execute the following command:

```
RUN 
{
  ALLOCATE CHANNEL c1 DEVICE TYPE DISK;
  BACKUP TABLESPACE users;
}
```

In this case, RMAN uses only the disk channel that you manually allocated within the [`RUN`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2012.htm#RCMRF151) command, overriding any defaults set by using `CONFIGURE` `DEVICE` `TYPE`, `CONFIGURE` `DEFAULT` `DEVICE`, or `CONFIGURE` `CHANNEL` settings.

See Also:

- ["RMAN Channels"](rcmarchi.md) to learn about configured and allocated channels
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta004.htm#RCMRF102) for `ALLOCATE CHANNEL` syntax
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) for `CONFIGURE` syntax

### Configuring Control File and Server Parameter File Autobackups

As explained in ["Control File and Server Parameter File Autobackups"](rcmcncpt.md), you can configure RMAN to automatically back up the control file and server parameter file. The autobackup occurs whenever a backup record is added. If the database runs in `ARCHIVELOG` mode, then an autobackup is also taken whenever the database structure metadata in the control file changes. A [control file autobackup](glossary.md) enables RMAN to recover the database even if the current control file, recovery catalog, and server parameter file are lost.

Because the file name for the autobackup follows a well-known format, RMAN can search for it without access to a repository and then restore the server parameter file. After you have started the instance with the restored server parameter file, RMAN can restore the control file from an autobackup. After you mount the control file, the RMAN repository is available, and RMAN can restore the data files and find the archived redo logs.

You can enable the autobackup feature by running the following command:

```
CONFIGURE CONTROLFILE AUTOBACKUP ON;
```

You can disable the feature by running the following command:

```
CONFIGURE CONTROLFILE AUTOBACKUP OFF;
```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) for `CONFIGURE` syntax

#### Configuring the Control File Autobackup Format

By default, the format of the autobackup file for all configured devices is the substitution variable `%F` in the [`FORMAT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl010.htm#RCMRF195) clause. This variable format translates into `c-IIIIIIIIII-YYYYMMDD-QQ`, with the placeholders defined as follows:

- `IIIIIIIIII` stands for the DBID.
- `YYYYMMDD` is a time stamp of the day the backup is generated.
- `QQ` is the hexadecimal sequence that starts with `00` and has a maximum of `FF`.

You can change the default format by using the following command, where `deviceSpecifier` is any valid device type, and ' `string` ' must contain the substitution variable `%F` (and no other substitution variables) and is a valid handle for the specified device:

```
CONFIGURE CONTROLFILE AUTOBACKUP FORMAT 
  FOR DEVICE TYPE deviceSpecifier TO 'string';
```

For example, you can run the following command to specify a nondefault file name for the control file autobackup. In the file name, `?` stands for `ORACLE_HOME`.

```
CONFIGURE CONTROLFILE AUTOBACKUP FORMAT 
  FOR DEVICE TYPE DISK TO '?/oradata/cf_%F';
```

The following example configures the autobackup to write to an Automatic Storage Management disk group:

```
CONFIGURE CONTROLFILE AUTOBACKUP FORMAT 
  FOR DEVICE TYPE DISK TO '+dgroup1/%F';
```

Note:

The valid formats for control file autobackups are: `%D`, `%I`, `%M`, `%Y`, `%F`, `%T`, `%d`, and `%n`. If you use formats other than these, you may not be able to restore the control file autobackup.

To clear control file autobackup formats for a device, use the following commands:

```
CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK CLEAR;
CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE sbt CLEAR;
```

If you have set up a [fast recovery area](glossary.md) for the database, then you can direct control file autobackups to the fast recovery area by clearing the control file autobackup format for disk.

Note:

All files in the fast recovery area are maintained by Oracle Database and associated file names are maintained in the Oracle Managed Files (OMF) format.

#### Overriding the Configured Control File Autobackup Format

The [`SET`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2014.htm#RCMRF153) `CONTROLFILE` `AUTOBACKUP` `FORMAT` command, which you can specify either within a [`RUN`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2012.htm#RCMRF151) command or at the RMAN prompt, overrides the configured autobackup format in the current session only. The order of precedence is:

1. `SET CONTROLFILE AUTOBACKUP FORMAT` (within a `RUN` block`)`
2. `SET CONTROLFILE AUTOBACKUP FORMAT` (at `RMAN` prompt)
3. `CONFIGURE CONTROLFILE AUTOBACKUP FORMAT`

The following example shows how the two forms of `SET` `CONTROLFILE` `AUTOBACKUP` `FORMAT` interact:

```
SET CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK TO 'controlfile_%F';
BACKUP AS COPY DATABASE;
RUN
{ 
  SET CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK TO '/tmp/%F.bck'; 
  BACKUP AS BACKUPSET 
    DEVICE TYPE DISK 
    DATABASE;
}
```

The first `SET CONTROLFILE AUTOBACKUP FORMAT` controls the name of the control file autobackup until the RMAN client exits, overriding any configured control file autobackup format. The `SET CONTROFILE AUTOBACKUP FORMAT` in the `RUN` block overrides the `SET CONTROLFILE AUTOBACKUP FORMAT` outside the `RUN` block for the duration of the `RUN` block.

## Configuring RMAN to Make Backups to a Media Manager

On most platforms, to back up to and restore from sequential media such as tape you must integrate a [media manager](glossary.md) with your Oracle database. You can use [Oracle Secure Backup](glossary.md), which supports both database and file system backups to tape, as your media manager. See [Oracle Secure Backup Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OBADM) to learn how to set up RMAN for use specifically with Oracle Secure Backup.

If you do not use Oracle Secure Backup, then you can use a third-party media manager. This section describes the generic steps for configuring RMAN for use with a third-party media manager. The actual steps depend on the media management product that you install and the platform on which you run the database. If you opt to use RMAN with a media manager other than Oracle Secure Backup, then you must obtain all product-specific information from the vendor.

Read the following sections in order when configuring the media manager:

1. Prerequisites for Using a Media Manager with RMAN
2. Determining the Location of the Media Management Library
3. Configuring Media Management Software for RMAN Backups
4. Testing Whether the Media Manager Library Is Integrated Correctly
5. Configuring SBT Channels for Use with a Media Manager
	See Also:
	["Media Management"](rcmarchi.md) for an overview of media management software and its implications for RMAN

### Prerequisites for Using a Media Manager with RMAN

Before you can begin using RMAN with a third-party media manager, you must install the media manager and ensure that RMAN can communicate with it. Refer to the media management vendor's software documentation for instructions.

In general, you should begin by installing and configuring the media management software on the target host or production network. Ensure that you can make non-RMAN backups of operating system files on the target database host. This step makes later troubleshooting much easier by confirming that the basic integration of the media manager with the target host has been successful. Refer to your media management documentation to learn how to back up files to the media manager without using RMAN.

Then, obtain and install the third-party media management module for integration with the database server. This module contains the [media management library](glossary.md) that the Oracle database loads and uses when accessing the media manager. It is generally a third-party product that must be purchased separately. Contact your media management vendor for details.

### Determining the Location of the Media Management Library

Before attempting to use RMAN with a media manager, determine the location of the media management library. When allocating or configuring a [channel](glossary.md) for RMAN to use to communicate with a media manager, you must specify the `SBT_LIBRARY` parameter in an `ALLOCATE CHANNEL` or `CONFIGURE CHANNEL` command. The `SBT_LIBRARY` parameter specifies the path to the library.

The following example shows the channel syntax, where pathname is the absolute file name of the library:

```
CONFIGURE CHANNEL DEVICE TYPE sbt
  PARMS 'SBT_LIBRARY=pathname';
```

When RMAN allocates channels to communicate with a media manager, it attempts to load the library indicated by the `SBT_LIBRARY` parameter.

If you do not provide a value for the `SBT_LIBRARY` parameter in an allocated or preconfigured channel, then RMAN looks in a platform-specific and secured default location.

On Linux and UNIX, the SBT library is loaded from:

```
/opt/oracle/extapi/[32,64]/{SBT}/{VENDOR}/{VERSION}/libobk.so
```

The SBT library file name extension name varies according to platform:

- `.so`, `.sl` on HP-UX,
- `.a` on AIX,

On Windows, the SBT library is loaded from:

```
%SYSTEM_DRIVE%\oracle\extapi\[32,64]\{SBT}\{VENDOR}\{VERSION}\orasbt.dll
```

If RMAN cannot use the secured default location or if you are using Oracle Database 11g or earlier, RMAN loads the SBT library from the location designated by the environment variables `PATH` or `LIBPATH`.

In some cases, your organization may have security or regulatory compliance requirements that prohibit the use of environment variables `PATH` or `LIBPATH` to designate a library directory. To disable this behavior, set the `PARMS` string to SBT\_SECURE=1.

Note:

The default media management library file is not part of the standard database installation. It is present only if you install third-party media management software.

See Also:

Your operating system-specific database documentation and the documentation supplied by your media vendor for instructions on how to achieve media manager integration on your platform

### Configuring Media Management Software for RMAN Backups

After installing the media management software, perform whatever configuration that your vendor requires so that the software can accept RMAN backups. Depending on the type of media management software that you installed, you may have to define media pools, configure users and classes, and so on.

Consult your media management vendor documentation for the appropriate RMAN settings. The `PARMS` parameter sends instructions to the media manager. If `PARMS` values are needed for the [`ALLOCATE CHANNEL`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta004.htm#RCMRF102) or the [`CONFIGURE CHANNEL`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) command, or if a [`FORMAT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl010.htm#RCMRF195) string is recommended for the [`BACKUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) or `CONFIGURE` command, then refer to the vendor documentation for this information.

Example 5-6 shows a `PARMS` setting for Oracle Secure Backup. This `PARMS` settings instructs the media manager to back up to a family of tapes called `datafile_mf`. The `PARMS` settings are always vendor-specific.

Example 5-6 PARMS Setting for Oracle Secure Backup

```
CONFIGURE CHANNEL DEVICE TYPE 'SBT_TAPE'
  PARMS 'ENV=(OB_MEDIA_FAMILY=datafile_mf)';
```

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta004.htm#RCMRF102) for `ALLOCATE` `CHANNEL` syntax
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) for channel control options
- [Oracle Secure Backup Reference](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OBREF8000) for RMAN-specific parameter settings for Oracle Secure Backup

### Testing Whether the Media Manager Library Is Integrated Correctly

After you have confirmed that the database server can load the media management library, test to ensure that RMAN can back up to the media manager.

#### Testing ALLOCATE CHANNEL on the Media Manager

The following steps use the `ALLOCATE CHANNEL` command to perform a basic test of RMAN communication with the media manager.

To test channel allocation on the media manager:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. Run the `ALLOCATE` `CHANNEL` command with the `PARMS` required by your media management software.
	The following `RUN` command shows sample vendor-specific `PARMS` settings:
	```
	RUN
	{
	  ALLOCATE CHANNEL c1 DEVICE TYPE sbt
	    PARMS 'SBT_LIBRARY=/mydir/lib/libobk.so,
	    ENV=(OB_DEVICE=drive1,OB_MEDIA_FAMILY=datafile_mf)';
	}
	```
3. Examine the RMAN output.
	If you do not receive an error message, then the database successfully loaded the media management library. If you receive the `ORA-27211` error, the media management library could not be loaded:
	```
	RMAN-00571: ===========================================================
	RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============
	RMAN-00571: ===========================================================
	RMAN-03009: failure of allocate command on c1 channel at 11/30/2007 13:57:18
	ORA-19554: error allocating device, device type: SBT_TAPE, device name: 
	ORA-27211: Failed to load Media Management Library
	Additional information: 25
	```
	In this case, check the media management installation to ensure that the library is correctly installed, and recheck the value for the `SBT_LIBRARY` parameter as described in "Determining the Location of the Media Management Library".
	If the database cannot locate a media management library in the location specified by the `SBT_LIBRARY` parameter or the default location, then RMAN issues an `ORA-27211` error and exits.

Whenever channel allocation fails, the database writes a trace file to the `trace` subdirectory in the [Automatic Diagnostic Repository (ADR)](glossary.md) home directory. The following shows sample output:

```
SKGFQ OSD: Error in function sbtinit on line 2278
SKGFQ OSD: Look for SBT Trace messages in file /oracle/rdbms/log/sbtio.log
SBT Initialize failed for /oracle/lib/libobk.so
```

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/monitoring.htm#ADMIN005) to learn how to use the Automatic Diagnostic Repository to monitor database operations

#### Testing Backup and Restore Operations on the Media Manager

After testing a channel allocation on the media manager, create and restore a test backup. For example, you can use the command in Example 5-7 (substituting the channel settings required by your media management vendor) to test whether a backup can be created on the media manager. If your database does not use a server parameter file, then back up the current control file instead.

Example 5-7 Backing Up the Server Parameter File to Tape

```
RUN
{
  ALLOCATE CHANNEL c1 DEVICE TYPE sbt
    PARMS 'SBT_LIBRARY=/mydir/lib/libobk.so,
    ENV=(OB_DEVICE=drive1,OB_MEDIA_FAMILY=datafile_mf)';
  BACKUP SPFILE;
  # If your database does not use a server parameter file, use:
  # BACKUP CURRENT CONTROLFILE;
}
```

If the backup succeeds, then attempt to restore the server parameter file as an initialization parameter file. Example 5-8 restores the backup created in Example 5-7 to a temporary directory.

Example 5-8 Restoring the Server Parameter File from Tape

```
RUN
{
  ALLOCATE CHANNEL c1 DEVICE TYPE sbt
    PARMS 'SBT_LIBRARY=/mydir/lib/libobk.so,
    ENV=(OB_DEVICE=drive1,OB_MEDIA_FAMILY=datafile_mf)';
  RESTORE SPFILE TO PFILE '/tmp/test_restore.f';
  # If your database does not use a server parameter file, use:
  # RESTORE CURRENT CONTROLFILE TO '/tmp/test_restore.f';
}
```

If the backup and restore operations succeed, then you are ready to use the media manager with RMAN. Possible failures include the following cases:

- The backup hangs.
	A hanging backup usually indicates that the media manager is waiting to mount a tape. Check if there are any media manager jobs in tape mount request mode and fix the problem. Ensure that the steps in "Configuring RMAN to Make Backups to a Media Manager" are correctly done.
- The backup fails with `ORA-27211: Failed to load Media Management Library`.
	This error indicates that the media management software is not correctly configured. Ensure that the steps in "Configuring RMAN to Make Backups to a Media Manager" are correctly done. Also, ensure that you have the `PARMS` and `FORMAT` strings required by your media management software.

### Configuring SBT Channels for Use with a Media Manager

This section describes how to configure channels for use with a media manager. For an overview of configured channels and how they are used, refer to the section ["Configuring Advanced Channel Options"](rcmconfa.md).

#### About Media Manager Backup Piece Names

A [backup piece](glossary.md) name is determined by the [`FORMAT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl010.htm#RCMRF195) string specified in the `BACKUP` command, `CONFIGURE` `CHANNEL` command, or `ALLOCATE` `CHANNEL` command. The media manager considers the backup piece name as the name of the backup file, so every backup piece must have a unique name in the [media management catalog](glossary.md).

You can use the substitution variables in a `FORMAT` parameter to generate unique backup piece names. For example, `%d` specifies the name of the database, whereas `%t` specifies the backup time stamp. For most purposes, you can use `%U`, in which case RMAN automatically generates a unique file name. The backup piece name `12i1nk47_1_1` is an example. If you do not specify the `FORMAT` parameter, then RMAN automatically generates a unique file name with the `%U` substitution variable.

Your media manager may impose restrictions on file names and sizes. In this case, you may need more control over the naming of backup pieces so that they obey media manager restrictions. For example, some media managers only support a 14-character backup piece name, and some require special `FORMAT` strings. The unique names generated by the `%U` substitution variable do not exceed 14 characters.

Some media managers may have limits on the maximum size of files that they can back up or restore. You must ensure that RMAN does not produce backup sets larger than those limits. To limit backup piece sizes, use the parameter `MAXPIECESIZE`, which you can set in the `CONFIGURE` `CHANNEL` and `ALLOCATE` `CHANNEL` commands.

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl001.htm#RCMRF104) and ["Number and Size of Backup Pieces"](rcmcncpt.md) to learn how to set `MAXPIECESIZE`
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl010.htm#RCMRF195) for the complete list of variables allowable in format strings with the `BACKUP` command
- Your media management documentation to determine the string character limit for the media manager

#### Configuring Automatic SBT Channels

The easiest technique for backing up to a media manager is to configure automatic [SBT](glossary.md) channels. As explained in "Configuring the Default Device for Backups: Disk or SBT", you can use a tape device as your default backup destination.

To configure channels for use with a media manager:

1. Configure a generic SBT channel.
	In the configuration, enter all parameters that you tested "Testing Backup and Restore Operations on the Media Manager". The following example configures vendor-specific channel parameters and sets the default device:
	```
	CONFIGURE CHANNEL DEVICE TYPE sbt 
	  PARMS 'ENV=(OB_RESOURCE_WAIT_TIME=1minute,OB_DEVICE=tape1)';
	```
2. Configure the default device type to SBT, as shown in the following command:
	```
	CONFIGURE DEFAULT DEVICE TYPE TO sbt;
	```
	If you use multiple tape devices, then you must specify the channel parallelism as described in "Configuring Parallel Channels for Disk and SBT Devices". The following configuration enables you to back up to two tape drives in parallel:
	```
	CONFIGURE DEVICE TYPE sbt PARALLELISM 2;
	```
	Optionally, check your channel configuration by running the following command:
	```
	SHOW CHANNEL FOR DEVICE TYPE sbt;
	```
3. Make a test backup to tape.
	The following command backs up the server parameter file to tape:
	```
	BACKUP SPFILE;
	```
4. List your backups to ensure that the test backup went to the media manager:
	```
	LIST BACKUP OF SPFILE;
	```

## Configuring the Fast Recovery Area

As explained in ["Fast Recovery Area"](rcmarchi.md), the [fast recovery area](glossary.md) feature enables you to set up a disk area where the database can create and manage a variety of files related to backup and recovery. Use of the fast recovery area is strongly recommended. Consider configuring a fast recovery area as a first step in implementing a backup strategy.

This section outlines the functions of the fast recovery area, identifies the files stored there, explains the rules for file management, and introduces the most important configuration options. This section contains the following topics:

- Overview of the Fast Recovery Area
- Enabling the Fast Recovery Area
- Disabling the Fast Recovery Area
- Configuring Locations for Control Files and Redo Logs
- Configuring RMAN File Creation in the Fast Recovery Area

See Also:

["Maintaining the Fast Recovery Area"](rcmmaint.md)

### Overview of the Fast Recovery Area

The fast recovery area can contain control files, online redo logs, archived redo logs, flashback logs, and RMAN backups. Files in the recovery area are permanent or transient. Permanent files are active files used by the database instance. All files that are not permanent are transient. In general, Oracle Database eventually deletes transient files after they become obsolete under the [backup retention policy](glossary.md) or have been backed up to tape.

The fast recovery area is an Oracle Database managed space that can be used to hold RMAN disk backups, control file autobackups and archived redo log files. The files placed in this location are maintained by Oracle Database and the generated file names are maintained in Oracle Managed Files (OMF) format.

Table 5-2 describes the files in the recovery area, the classification of each file as permanent or temporary, and how database availability is affected.

Table 5-2 Files in the Fast Recovery Area

| Files | Type | Database Behavior When Fast Recovery Area Is Inaccessible |
| --- | --- | --- |
| Multiplexed copies of the current control file | Permanent | The instance fails if the database cannot write to a multiplexed copy of the control file stored in the fast recovery area. Failure occurs even if accessible multiplexed copies are located outside the recovery area.  See Also: "Configuring Control File Locations" to learn how to configure control files in the recovery area |
| Online redo log files | Permanent | Instance availability is not affected if a mirrored copy of the online redo log exists in an accessible location outside the fast recovery area. Otherwise, the instance fails.  See Also: "Configuring Online Redo Log Locations" to learn how to configure online redo logs in the recovery area |
| Archived redo log files | Transient | Instance availability is not affected if the log is archived to an accessible location outside the fast recovery area. Otherwise, the database eventually halts because it cannot archive the online redo logs.  See Also: "Configuring Archived Redo Log Locations" to learn how to configure archived redo logs in the recovery area |
| Foreign archived redo log files | Transient | Instance availability is not affected.  Note: Foreign archived redo logs are received by a logical standby database for a LogMiner session. Unlike a normal archived log, a [foreign archived redo log](glossary.md) is associated with a different DBID. For this reason, it cannot be backed up or restored on a logical standby database. |
| Image copies of data files and control files | Transient | Instance availability is not affected. |
| Backup pieces | Transient | Instance availability is not affected. |
| Flashback logs | Transient | Instance availability is not affected if guaranteed restore points are not defined. In this case, the database automatically disables Flashback Database, writes a message to the alert log, and continues with database processing. If guaranteed restore points are configured, the instance fails because of interdependencies on the flashback logs.  The [Oracle Flashback Database](glossary.md) feature, which provides a convenient alternative to [database point-in-time recovery (DBPITR)](glossary.md), generates [flashback logs](glossary.md). These logs are transient files and must be stored in the fast recovery area. Unlike other transient files, flashback logs cannot be backed up to other media. If the fast recovery area has insufficient space to store flashback logs and meet other backup retention requirements, then the recovery area may delete flashback logs.  See Also: ["Enabling Flashback Database"](flashdb.md) to learn how to enable flashback logging |

If you are on a Windows platform, then you can use the [Volume Shadow Copy Service (VSS)](glossary.md) with the [Oracle VSS writer](glossary.md). In this case, the fast recovery area automates management of files that are backed up in a VSS snapshot and deletes them as needed.

See Also:

- [Chapter 18, "Performing Flashback and Database Point-in-Time Recovery"](rcmflash.md)
- [Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/win.112/e10845/toc.htm) to learn about making backups in a VSS environment

#### Oracle Managed Files and Automatic Storage Management

The fast recovery area can be used with [Oracle Managed Files (OMF)](glossary.md) and [Automatic Storage Management (ASM)](glossary.md). Because the fast recovery area is built on top of OMF, so it can be stored anywhere that Oracle Managed Files can. You can also use the recovery area with ASM.

Even if you choose not to set up the fast recovery area in ASM storage, you can still use Oracle Managed Files to manage your backup files in an ASM disk group. However, you lose a major benefit of the fast recovery area: the automatic deletion of files no longer needed to meet your recoverability goals as space is needed for more recent backups. Nevertheless, the other automatic features of OMF still function.

When your store backups, using OMF on top of ASM without using a fast recovery area is supported but discouraged. It is awkward to directly manipulate files under ASM.

#### How Oracle Manages Disk Space in the Fast Recovery Area

Space in the fast recovery area is balanced among backups and archived logs that must be kept according to the retention policy, and other files that may be subject to deletion. Oracle Database does not delete eligible files from the fast recovery area until the space must be reclaimed for some other purpose. Files recently moved to tape are often still available on disk for use in recovery. The recovery area can thus serve as a cache for tape. When the fast recovery area is full, Oracle Database automatically deletes eligible files to reclaim space in the recovery area as needed.

### Enabling the Fast Recovery Area

You enable the fast recovery area by setting two initialization parameters. These parameters enable the fast recovery area without having to shut down and restart the database instance.

You set the size of the fast recovery area with the parameter `DB_RECOVERY_FILE_DEST_SIZE` first, and then you set the physical location of the flash recovery files with the parameter `DB_RECOVERY_FILE_DEST`.

Table 5-3 discusses both the mandatory and optional parameters for enabling the fast recovery area.

In an Oracle Real Application Clusters (Oracle RAC) database, all instances must have the same values for these initialization parameters. The location must be on a cluster file system, ASM, or a shared directory.

Table 5-3 Initialization Parameters for the Fast Recovery Area

| Initialization Parameter | Required | Description |
| --- | --- | --- |
| [`DB_RECOVERY_FILE_DEST_SIZE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams066.htm#REFRN10235) | Yes | Specifies the [disk quota](glossary.md), which is maximum storage in bytes of data to be used by the recovery area for this database. You must set this parameter before `DB_RECOVERY_FILE_DEST`.  The `DB_RECOVERY_FILE_DEST_SIZE` setting does not include the following kinds of disk overhead:  - Block 0 or the operating system block header of each Oracle Database file is not included. 	Allow an extra 10% for this data when computing the actual disk usage required for the fast recovery area. - `DB_RECOVERY_FILE_DEST_SIZE` does not indicate the real size occupied on disk when the underlying file system is mirrored, compressed, or affected by overhead not known to Oracle Database. 	For example, if the recovery area is on a two-way mirrored ASM disk group, each file of x bytes occupies 2x bytes on the ASM disk group. In this case, set `DB_RECOVERY_FILE_DEST_SIZE` to no more than half the size of the disks for the ASM disk group. Likewise, when using a three-way mirrored ASM disk group, `DB_RECOVERY_FILE_DEST_SIZE` must be no greater than one third the size of the disks in the disk group, and so on. |
| [`DB_RECOVERY_FILE_DEST`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams065.htm#REFRN10234) | Yes | Specifies the recovery area location, which can be a file system directory or ASM disk group, but not a raw disk. The location must be large enough for the disk quota. |
| DB\_FLASHBACK\_RETENTION\_TARGET | No | Specifies the upper limit (in minutes) on how far back in time the database may be flashed back. This parameter is required only for Flashback Database.  This parameter indirectly determines how much flashback log data is kept in the recovery area. The size of flashback logs generated by the database can vary considerably depending on the database workload. If more blocks are affected by database updates during a given interval, then more disk space is used by the flashback log data generated for that interval. |

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_2014.htm#SQLRF00902) for `ALTER` `SYSTEM` syntax, and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN002) for details on setting and changing database initialization parameters

#### Considerations When Setting the Size of the Fast Recovery Area

The larger the fast recovery area is, the more useful it becomes. Ideally, the fast recovery area should be large enough to contain the files listed in Table 5-2. The recovery area should be able to contain a copy of all data files in the database and the incremental backups used by your chosen backup strategy.

If providing this much space is impractical, then it is best to create an area large enough to keep a backup of the most important tablespaces and all the archived logs not yet on tape. At an absolute minimum, the fast recovery area must be large enough to contain the archived redo logs not yet on tape. If the recovery area has insufficient space to store new flashback logs and meet other backup retention requirements, then to make room, the recovery area may delete older flashback logs.

Formulas for estimating a useful fast recovery area size depend on whether:

- Your database has a small or large number of data blocks that change frequently
- You store backups only on disk, or on disk and tape
- You use a redundancy-based [backup retention policy](glossary.md), or a recovery window-based retention policy
- You plan to use Flashback Database or a [guaranteed restore point](glossary.md) as alternatives to [point-in-time recovery](glossary.md) in response to logical errors

If you plan to enable flashback logging, then the volume of flashback log generation is approximately the same order of magnitude as redo log generation. For example, if you intend to set `DB_FLASHBACK_RETENTION_TARGET` to 24 hours, and if the database generates 20 gigabytes of redo in a day, then a general rule of thumb is to allow 20 GB to 30 GB of disk space for the flashback logs. The same rule applies to guaranteed restore points when flashback logging is enabled. For example, if the database generates 20 GB of redo every day, and if the guaranteed restore point is kept for a day, then plan to allocate 20 to 30 GB.

Suppose that you want to determine the size of a fast recovery area when the backup retention policy is set to `REDUNDANCY 1` and you intend to follow Oracle's suggested strategy of using an [incrementally updated backup](glossary.md). In this example, you use the following formula to estimate the disk quota, where n is the interval in days between incremental updates and y is the delay in applying the foreign archived redo logs on a logical standby database:

```
Disk Quota =
Size of a copy of database +
Size of an incremental backup +
Size of (n+1) days of archived redo logs +
Size of (y+1) days of foreign archived redo logs (for logical standby) +
Size of control file +
Size of an online redo log member * number of log groups +
Size of flashback logs (based on DB_FLASHBACK_RETENTION_TARGET value)
```

#### Considerations When Setting the Location of the Fast Recovery Area

Place the fast recovery area on a separate disk from the [database area](glossary.md), where the database maintains active database files such as data files, control files, and online redo logs. Keeping the fast recovery area on the same disk as the database area exposes you to loss of both your live database files and backups if a media failure occurs.

Oracle recommends that `DB_RECOVERY_FILE_DEST` be set to a different value from `DB_CREATE_FILE_DEST` or any of the `DB_CREATE_ONLINE_LOG_DEST_` `n` initialization parameters. The database writes a warning to the alert log if `DB_RECOVERY_FILE_DEST` equals these parameters.

Multiple databases can have the same value for `DB_RECOVERY_FILE_DEST`, but one of the following must be true:

- No two databases for which the [`DB_UNIQUE_NAME`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams070.htm#REFRN10242) initialization parameters are specified have the same value for `DB_UNIQUE_NAME`.
- For those databases where no `DB_UNIQUE_NAME` is provided, no two databases have the same value for [`DB_NAME`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams064.htm#REFRN10041).

When databases share a single recovery area in this way, the location should be large enough to hold the files for all databases. Add the values for `DB_RECOVERY_FILE_DEST_SIZE` for the databases, then allow for overhead such as mirroring or compression.

#### Setting the Fast Recovery Area Location and Initial Size

Table 5-3 lists the initialization parameters that you must set to enable the fast recovery area. This section explains how to specify a location for the recovery area and set its initial size.

To determine the optimum size for the fast recovery area:

1. If you plan to use flashback logging or guaranteed restore points, then query `V$ARCHIVED_LOG` to determine how much redo the database generates in the time to which you intend to set `DB_FLASHBACK_RETENTION_TARGET`.
2. Set the recovery area size.
	If you plan to use flashback logging or guaranteed restore points, then ensure that the size value obtained from Step 1 is incorporated into the setting. Set the `DB_RECOVERY_FILE_DEST_SIZE` initialization parameter by any of the following means:
	- Shut down the database and set the `DB_RECOVERY_FILE_DEST_SIZE` parameter in the initialization parameter file of the database, as shown in the following example:
		```
		DB_RECOVERY_FILE_DEST_SIZE = 10G
		```
		- Specify the parameter with the SQL statement `ALTER` `SYSTEM` `SET` when the database is open, as shown in the following examples:
		```
		ALTER SYSTEM SET 
		  DB_RECOVERY_FILE_DEST_SIZE = 10G 
		  SCOPE=BOTH SID='*';
		```
		- Use the Database Configuration Assistant to set the size.
3. Set the recovery area location.
	Set the initialization parameters by any of the following means:
	- Set `DB_RECOVERY_FILE_DEST` in the initialization parameter file of the database, as shown in the following example:
		```
		DB_RECOVERY_FILE_DEST = '/u01/oradata/rcv_area'
		```
		- Specify `DB_RECOVERY_FILE_DEST` with the SQL statement `ALTER` `SYSTEM` `SET` when the database is open, as shown in the following example:
		```
		ALTER SYSTEM SET
		  DB_RECOVERY_FILE_DEST = '+disk1' 
		  SCOPE=BOTH SID='*';
		```
		- Use the Database Configuration Assistant to set the location.
	If you do not plan to use flashback logging, then open the database (if it is closed) and do not complete the rest of the steps in this procedure.
4. If flashback logging is enabled, then run the database under a normal workload for the time period specified by `DB_FLASHBACK_RETENTION_TARGET`.
	In this way, the database can generate a representative sample of flashback logs.
5. Query the [`V$FLASHBACK_DATABASE_LOG`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1144.htm#REFRN30300) view as follows:
	```
	SELECT ESTIMATED_FLASHBACK_SIZE 
	FROM   V$FLASHBACK_DATABASE_LOG;
	```
	The result is an estimate of the disk space needed to meet the current flashback retention target, based on the database workload since Flashback Database was enabled.
6. If necessary, adjust the flashback log space requirement based on the actual size of flashback logs generated during the time period specified by `DB_FLASHBACK_RETENTION_TARGET`.

See Also:

["Managing Space for Flashback Logs in the Fast Recovery Area"](rcmmaint.md)

### Disabling the Fast Recovery Area

If you have enabled Flashback Database or use the fast recovery area for archive logs, then take the appropriate steps from those that follow below. Otherwise, skip to Step 3:

1. If Flashback Database is enabled, then disable it before you disable the fast recovery area.
	```
	ALTER DATABASE FLASHBACK OFF;
	```
2. If you are using the fast recovery area for archive logs, then set the initialization parameter `LOG_ARCHIVE_DEST_` n to use a non-fast recovery area location.
	For example, to change the fast recovery area for `LOG_ARCHIVE_DEST_1` to a non-fast recovery area location, use the command `ALTER SYSTEM SET`:
	```
	LOG_ARCHIVE_DEST_1='LOCATION=USE_DB_RECOVERY_FILE_DEST'
	```
	```
	ALTER SYSTEM SET LOG_ARCHIVE_DEST_1='LOCATION=/ORACLE/DBS/';
	```
3. Disable the fast recovery area initialization parameter.
	```
	ALTER SYSTEM SET DB_RECOVERY_FILE_DEST='';
	```

### Configuring Locations for Control Files and Redo Logs

As explained in "Overview of the Fast Recovery Area", the only permanent files are multiplexed copies of the current control file and online redo logs. This section explains how to set locations for these files and the archived logs.

#### Configuring Online Redo Log Locations

The initialization parameters that determine where online redo log files are created are `DB_CREATE_ONLINE_LOG_DEST_` `n`, `DB_RECOVERY_FILE_DEST`, and `DB_CREATE_FILE_DEST`. Details of the effect of combinations of these parameters on online redo log creation can be found in [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5004.htm#SQLRF01204) in the description of the `LOGFILE` clause of the `CREATE` `DATABASE` statement.

The following SQL statements can create online redo logs in the fast recovery area:

- [`CREATE DATABASE`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5004.htm#SQLRF01204)
- [`ALTER DATABASE ADD LOGFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1004.htm#SQLRF00802)
- [`ALTER DATABASE ADD STANDBY LOGFILE`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1004.htm#SQLRF00802)
- [`ALTER DATABASE OPEN RESETLOGS`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1004.htm#SQLRF00802)

The default size of an online log created in the fast recovery area is 100 megabytes. The log member file names are automatically generated by the database.

#### Configuring Control File Locations

The initialization parameters `CONTROL_FILES`, `DB_CREATE_ONLINE_LOG_DEST_` `n`, `DB_RECOVERY_FILE_DEST`, and `DB_CREATE_FILE_DEST` all interact to determine the location where the database control files are created. For a full description of how these parameters interact, see the "Semantics" section of the description of `CREATE CONTROLFILE` in [Oracle Database SQL Language Reference.](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5003.htm#SQLRF01203)

If the database creates an Oracle managed control file, and if the database uses a server parameter file, then the database sets the `CONTROL_FILES` initialization parameter in the server parameter file. If the database uses a client-side initialization parameter file, then you must set the `CONTROL_FILES` initialization parameter manually in the initialization parameter file.

#### Configuring Archived Redo Log Locations

Oracle recommends that you the use fast recovery area as an archiving location because the archived logs are automatically managed by the database. The generated file names for the archived logs in the fast recovery area are for Oracle Managed files and are not determined by the parameter `LOG_ARCHIVE_FORMAT`. Whatever archiving scheme you choose, it is always advisable to create multiple copies of archived redo logs.

You have the following basic options for archiving redo logs, listed from most to least recommended:

1. Enable archiving to the fast recovery area only and use disk mirroring to create the redundancy needed to protect the archived redo logs.
	If `DB_RECOVERY_FILE_DEST` is specified and no `LOG_ARCHIVE_DEST_` `n` is specified, then `LOG_ARCHIVE_DEST_10` is implicitly set to the recovery area. You can override this behavior by setting `LOG_ARCHIVE_DEST_10` to an empty string.
2. Enable archiving to the fast recovery area and set other `LOG_ARCHIVE_DEST_` `n` initialization parameter to locations outside the fast recovery area.
	If a fast recovery area is configured, then you can add the fast recovery area as an archiving destination by setting any `LOG_ARCHIVE_DEST_` `n` parameter to `LOCATION=USE_DB_RECOVERY_FILE_DEST`.
3. Set `LOG_ARCHIVE_DEST_` `n` initialization parameters to archive only to non-fast recovery area locations.

If you use the fast recovery area, then you cannot use the `LOG_ARCHIVE_DEST` and `LOG_ARCHIVE_DUPLEX_DEST` initialization parameters. Using either of these parameters prevents you from starting the instance. Instead, set the `LOG_ARCHIVE_DEST_` `n` parameters. After your database is using `LOG_ARCHIVE_DEST_` `n`, you can configure a recovery area.

Note also that if you enable archiving but do not set any value for `LOG_ARCHIVE_DEST`, `LOG_ARCHIVE_DEST_` `n`, or `DB_RECOVERY_FILE_DEST`, then the redo logs are archived to a default location that is platform-specific. For example, on Solaris the default is `?/dbs`.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams125.htm#REFRN10086) for details on the semantics of the `LOG_ARCHIVE_DEST_` `n` parameters

### Configuring RMAN File Creation in the Fast Recovery Area

This section describes RMAN commands or implicit actions (such as control file autobackups) that can create files in the fast recovery area, and explains how to control whether a command creates files there or in another destination. The commands are:

- [`BACKUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107)
	If you do not specify the [`FORMAT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl010.htm#RCMRF195) clause for disk backups, then RMAN creates backup pieces and image copies in the fast recovery area, with names in Oracle Managed Files name format. If a fast recovery area is enabled, and if you do specify `FORMAT` on `BACKUP` or a channel, then RMAN creates the backup in a platform-specific location rather than in the recovery area.
- Control File Autobackup
	RMAN can create control file autobackups in the fast recovery area. Use the RMAN command [`CONFIGURE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) `CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK CLEAR` to clear any configured format option for the control file autobackup location on disk. RMAN creates control file autobackups in the fast recovery area when no other destination is configured.
- [`RESTORE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2008.htm#RCMRF149) `ARCHIVELOG`
	Explicitly or implicitly set a `LOG_ARCHIVE_DEST_` `n` parameter to `LOCATION=USE_DB_RECOVERY_FILE_DEST`. If you do not specify [`SET`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2014.htm#RCMRF153) `ARCHIVELOG DESTINATION` to override this behavior, then RMAN restores archived redo log files to the fast recovery area.
- [`RECOVER`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2001.htm#RCMRF140) `DATABASE` or `RECOVER TABLESPACE`, `RECOVER ... BLOCK`, and [`FLASHBACK DATABASE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta023.htm#RCMRF194)
	These commands restore archived redo log files from backup for use during media recovery, as required by the command. RMAN restores any redo log files needed during these operations to the fast recovery area and deletes them after they are applied during media recovery.
	To direct the restored archived logs to the fast recovery area, set a `LOG_ARCHIVE_DEST_` `n` parameter to `LOCATION = USE_DB_RECOVERY_FILE_DEST`. Verify that you are not using `SET ARCHIVELOG DESTINATION` to direct restored logs to some other destination.

## Configuring the Backup Retention Policy

As explained in ["Backup Retention Policies"](rcmcncpt.md), the [backup retention policy](glossary.md) specifies which backups must be retained to meet your data recovery requirements. This policy can be based on a [recovery window](glossary.md) or [redundancy](glossary.md). Use the [`CONFIGURE RETENTION POLICY`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) command to specify the retention policy.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) for `CONFIGURE` syntax

### Configuring a Redundancy-Based Retention Policy

The `REDUNDANCY` parameter of the `CONFIGURE` `RETENTION` `POLICY` command specifies how many full or level 0 backups of each data file and control file that RMAN should keep. If the number of full or level 0 backups for a specific data file or control file exceeds the `REDUNDANCY` setting, then RMAN considers the extra backups as obsolete. The default retention policy is `REDUNDANCY 1`.

As you produce more backups, RMAN keeps track of which ones to retain and which are obsolete. RMAN retains all archived logs and incremental backups that are needed to recover the nonobsolete backups.

Assume that you make a full backup of data file 7 on Monday, Tuesday, Wednesday, and Thursday. You now have four full backups of this data file. If `REDUNDANCY` is `2`, then the Monday and Tuesday backups are obsolete. If you make another backup on Friday, then the Wednesday backup of data file 7 becomes obsolete.

Assume a different case in which `REDUNDANCY` is `1`. You run a level 0 database backup at noon on Monday, a level 1 cumulative backup at noon on Tuesday and Wednesday, and a level 0 backup at noon on Thursday. Immediately after each daily backup you run the command `DELETE OBSOLETE`. The Wednesday `DELETE` command does not remove the Tuesday level 1 backup because this backup is not redundant: the Tuesday level 1 backup could be used to recover the Monday level 0 backup to a time between noon on Tuesday and noon on Wednesday. However, the `DELETE` command on Thursday removes the previous level 0 and level 1 backups.

Run the `CONFIGURE` `RETENTION` `POLICY` command at the RMAN prompt, as in the following example:

```
CONFIGURE RETENTION POLICY TO REDUNDANCY 3;
```

See Also:

["Deleting Obsolete RMAN Backups Based on Retention Policies"](rcmmaint.md)

### Configuring a Recovery Window-Based Retention Policy

The `RECOVERY` `WINDOW` parameter of the `CONFIGURE` command specifies the number of days between the current time and the earliest point of recoverability. RMAN does not consider any full or [level 0 incremental backup](glossary.md) as obsolete if it falls within the recovery window. Additionally, RMAN retains all archived logs and level 1 incremental backups that are needed to recover to a random point within the window.

Run the `CONFIGURE` `RETENTION` `POLICY` command at the RMAN prompt. This example ensures that you can recover the database to any point within the last week:

```
CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 7 DAYS;
```

RMAN does not automatically delete backups rendered obsolete by the recovery window. Instead, RMAN shows them as `OBSOLETE` in the `REPORT` `OBSOLETE` output and in `the OBSOLETE` column of `V$BACKUP_FILES`. RMAN deletes obsolete files if you run the `DELETE` `OBSOLETE` command.

See Also:

["Deleting Obsolete RMAN Backups Based on Retention Policies"](rcmmaint.md)

### Disabling the Retention Policy

When you disable the retention policy, RMAN does not consider any backup as obsolete. To disable the retention policy, run this command:

```
CONFIGURE RETENTION POLICY TO NONE;
```

Configuring the retention policy to `NONE` is different from clearing it. Clearing it returns it to its default setting of `REDUNDANCY 1`, whereas `NONE` disables it.

If you disable the retention policy and run [`REPORT OBSOLETE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2006.htm#RCMRF147) or [`DELETE OBSOLETE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta016.htm#RCMRF121) commands without passing a retention policy option to the command, then RMAN issues an error because no retention policy exists to determine which backups are obsolete.

Caution:

If you are using a fast recovery area, then you should not run your database with the retention policy disabled. If files are never considered obsolete, then a file can only be deleted from the fast recovery area if it has been backed up to some other disk location or to a tertiary storage device such as tape. This action is likely to use all of the space in your recovery area, which interferes with the normal operation of your database. See "How Oracle Manages Disk Space in the Fast Recovery Area"

## Backup Optimization and the CONFIGURE command

Run the [`CONFIGURE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) command to enable and disable backup optimization. Backup optimization skips the backup of files in certain circumstances if the identical file or an identical version of the file has been backed up.

### Overview of Backup Optimization

If you enable [backup optimization](glossary.md), then the [`BACKUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) command skips backing up files when the identical file has already been backed up to the specified device type. Table 5-4 describes criteria that RMAN uses to determine whether a file is identical to a file that it backed up.

Table 5-4 Criteria to Determine an Identical File

| Type of File | Criteria to Determine an Identical File |
| --- | --- |
| Data file | The data file must have the same [DBID](glossary.md), [checkpoint](glossary.md) SCN, creation SCN, and `RESETLOGS` SCN and time as a data file in a backup. The data file must be offline-normal, read-only, or closed normally. |
| Archived log | Same DBID, thread, sequence number, and `RESETLOGS` SCN and time |
| Backup set | Same DBID, backup set record ID, and stamp |

If RMAN determines that a file is identical and it has been backed up, then it is a candidate to be skipped. RMAN must do further checking to determine whether to skip the file, however, because both the retention policy and the backup duplexing feature are factors in the algorithm that determines whether RMAN has sufficient backups on the specified device type.

RMAN uses backup optimization when the following conditions are true:

- The `CONFIGURE` `BACKUP` `OPTIMIZATION` `ON` command has been run to enable backup optimization.
- You run `BACKUP` `DATABASE`, `BACKUP` `ARCHIVELOG` with `ALL` or `LIKE` options, or `BACKUP` `BACKUPSET` `ALL`, `BACKUP RECOVERY AREA`, `BACKUP RECOVERY FILES`, or `BACKUP DATAFILECOPY`.
	Note:
	When `TO DESTINATION` is used with `BACKUP RECOVERY AREA` or `BACKUP RECOVERY FILES`, RMAN only skips backups of files that have identical backups in the `TO DESTINATION` location that you provide.
- Only one type of channel is allocated, do not mix disk and [SBT](glossary.md) channels in the same backup command.

Note:

In [backup undo optimization](glossary.md), RMAN excludes undo changes (that are not needed for recovery of a backup) for transactions that have been committed. You can enable and disable backup optimization, but backup undo optimization is built-in behavior.

For example, assume that you have configured backup optimization. These commands back up to tape the database, all archived logs, and all backup sets:

```
BACKUP DEVICE TYPE sbt DATABASE PLUS ARCHIVELOG;
BACKUP DEVICE TYPE sbt BACKUPSET ALL;
```

If none of the backed-up files has changed since the last backup, then RMAN does not back up the files again. RMAN also does not signal an error if it skips all files specified in the command because the files have already been backed up.

You can override optimization at any time by specifying the `FORCE` option on the `BACKUP` command. For example, you can run:

```
BACKUP DATABASE FORCE;
BACKUP ARCHIVELOG ALL FORCE;
```

See Also:

The `CONFIGURE` entry in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) for a complete description of the backup optimization rules

### Effect of Retention Policies on Backup Optimization for SBT Backups

Backup optimization is not always applied when backing up to [SBT](glossary.md) devices. The exceptions to normal backup optimization behavior for recovery window-based and redundancy-based retention policies are described in the following sections.

Note:

Use caution when enabling backup optimization if you use a media manager with its own internal expiration policy. Run the [`CROSSCHECK`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta015.htm#RCMRF119) command periodically to synchronize the RMAN repository with the media manager. Otherwise, RMAN may skip backups due to optimization without recognizing that the media manager has discarded backups stored on tape.

#### Backup Optimization for SBT Backups with Recovery Window Retention Policy

Suppose that backup optimization is enabled, and a recovery window [backup retention policy](glossary.md) is in effect. In this case, when performing SBT backups RMAN always backs up data files whose most recent backup is older than the [recovery window](glossary.md). For example, assume the following scenario:

- Today is February 21.
- The recovery window is 7 days.
- The most recent backup of tablespace `tools` to tape is January 3.
- Tablespace `tools` is read-only.

On February 21, when you issue a command to back up tablespace `tools` to tape, RMAN backs it up even though it did not change after the January 3 backup (because it is read-only). RMAN makes the backup because no backup of the tablespace exists within the 7-day recovery window.

This behavior enables the media manager to expire old tapes. Otherwise, the media manager would be forced to keep the January 3 backup of tablespace `tools` indefinitely. By making a more recent backup of tablespace `tools` on February 21, RMAN enables the media manager to expire the tape containing the January 3 backup.

#### Backup Optimization for SBT Backups With Redundancy Retention Policy

Assume that you configure a retention policy for redundancy. In this case, RMAN only skips backups of offline or read-only data files to SBT when there are `r` + 1 backups of the files, where `r` is set in `CONFIGURE` `RETENTION` `POLICY` `TO` `REDUNDANCY` `r`.

For example, assume that you enable backup optimization and set the following retention policy:

```
CONFIGURE DEFAULT DEVICE TYPE TO sbt;
CONFIGURE BACKUP OPTIMIZATION ON;
CONFIGURE RETENTION POLICY TO REDUNDANCY 2;
```

With these settings, RMAN only skips backups when three identical files are already backed up. Also assume that you have never backed up the `users` tablespace, which is read/write, and that you perform the actions described in Table 5-5 over the course of the week.

Table 5-5 Effect of Redundancy Setting on Backup Optimization

| Day | Action | Result | Redundant Backup |
| --- | --- | --- | --- |
| Monday | Take `users` offline normal. |  |  |
| Tuesday | `BACKUP` `DATABASE` | The `users` tablespace is backed up. |  |
| Wednesday | `BACKUP` `DATABASE` | The `users` tablespace is backed up. |  |
| Thursday | `BACKUP` `DATABASE` | The `users` tablespace is backed up. | Tuesday backup |
| Friday | `BACKUP` `DATABASE` | The `users` tablespace is not backed up. | Tuesday backup |
| Saturday | `BACKUP` `DATABASE` | The `users` tablespace is not backed up. | Tuesday backup |
| Sunday | `DELETE` `OBSOLETE` | The Tuesday backup is deleted. |  |
| Monday | `BACKUP` `DATABASE` | The `users` tablespace is backed up. | Wednesday backup |

The backups on Tuesday, Wednesday, and Thursday back up the offline `users` tablespace to satisfy the condition that three backups must exist (one more than redundancy setting). The Friday and Saturday backups do not back up the `users` tablespace because of backup optimization. The Tuesday backup of `users` is obsolete beginning on Thursday.

On Sunday, you delete all obsolete backups, which removes the Tuesday backup of `users`. The Tuesday backup is obsolete because of the retention policy setting. The whole database backup on Monday then backs up the `users` tablespace to satisfy the condition that three backups must exist (one more than redundancy setting). In this way, you can recycle your tapes over time.

See Also:

"Backup Optimization and the CONFIGURE command"

### Configuring Backup Optimization

By default, backup optimization is configured to `OFF`. You can use the [`SHOW BACKUP OPTIMIZATION`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2015.htm#RCMRF154) command to view the current settings of backup optimization.

To configure backup optimization:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. Run the `SHOW` `BACKUP` `OPTIMIZATION` command to determine whether optimization is currently enabled.
	For example, enter the following command:
	```
	SHOW BACKUP OPTIMIZATION;
	```
	Sample output for `SHOW` `BACKUP` `OPTIMIZATION` follows:
	```
	RMAN configuration parameters for database with db_unique_name PROD1 are:
	CONFIGURE BACKUP OPTIMIZATION OFF;
	```
3. Enable backup optimization by running the following command:
	```
	CONFIGURE BACKUP OPTIMIZATION ON;
	```

See Also:

["Using Backup Optimization to Skip Files"](rcmbckad.md) for examples of how to optimize RMAN backups

## Configuring an Archived Redo Log Deletion Policy

You can use RMAN to create a persistent configuration that governs when archived redo logs are eligible for deletion from disk.

### About Archived Redo Log Deletion Policies

You can use the `CONFIGURE ARCHIVELOG DELETION POLICY` command to specify when archived redo logs are eligible for deletion. This deletion policy applies to all archiving destinations, including the [fast recovery area](glossary.md).

Archived redo logs can be deleted automatically by the database or by user-initiated RMAN commands. Only logs in the fast recovery area can be deleted automatically by the database. For archived redo log files in the fast recovery area, the database retains them as long as possible and automatically deletes eligible logs when additional disk space is required. You can manually delete eligible logs from any location, whether inside or outside the fast recovery area, when you issue [`BACKUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) `... DELETE INPUT` or `DELETE ARCHIVELOG` commands.

#### When the Archived Redo Log Deletion Policy Is Disabled

By default, there is no [archived redo log deletion policy](glossary.md) and this is why the archive redo log policy is set to the `NONE` clause. In this particular case, the fast recovery area considers archived redo log files in the recovery area as eligible for deletion if they have been backed up at least once to disk or SBT or the logs are obsolete according to the backup retention policy. The backup retention policy considers logs obsolete only if the logs are not needed by a guaranteed restore point and the logs are not needed by Oracle Flashback Database. Archived redo logs are needed by Flashback Database if the logs were created later than `SYSDATE-'DB_FLASHBACK_RETENTION_TARGET'`.

See Also:

- The `CONFIGURE ARCHIVELOG DELETION POLICY` entry in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) for detailed information about policy options
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) to learn how to configure an archived log deletion policy in a Data Guard environment

#### When the Archived Redo Log Deletion Policy Is Enabled

You can use the `CONFIGURE ARCHIVELOG DELETION POLICY BACKED UP` `integer` `TIMES TO DEVICE TYPE` command to enable an archived log deletion policy. This configuration specifies that archived logs are eligible for deletion only when the specified number of archived log backups exist on the specified device type.

If the deletion policy is configured with the `BACKED UP` `integer` `TIMES` clause, then a `BACKUP ARCHIVELOG` command copies the logs unless `integer` backups already exist on the specified device type. If `integer` backups of the logs exist, then the `BACKUP ARCHIVELOG` command skips the logs. In this way, the archived log deletion policy functions as a default `NOT BACKED UP` `integer` `TIMES` clause on the `BACKUP ARCHIVELOG` command. You can override the deletion policy by specifying the `FORCE` option on the `BACKUP` command.

The archived log deletion policy also has options specific to a Data Guard environment. For example, if you specify the `APPLIED ON STANDBY` clause, then RMAN can delete logs after they have been applied at all mandatory remote destinations. If you specify `SHIPPED TO STANDBY`, then RMAN can delete logs when they have been transferred to all mandatory standby destinations.

See Also:

- The `CONFIGURE ARCHIVELOG DELETION POLICY` entry in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) for detailed information about policy options
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB04700) to learn how to configure an archived log deletion policy in a Data Guard environment

### Enabling an Archived Redo Log Deletion Policy

This section explains how to configure an archived redo log deletion policy. By default the policy is set to `NONE`.

To enable an archived redo log deletion policy:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. Run the `CONFIGURE ARCHIVELOG DELETION POLICY` command with the desired options.
	The following example specifies that archived redo logs are eligible to be deleted from the fast recovery area and all local archiving destinations when logs have been backed up at least twice to tape:
	```
	CONFIGURE ARCHIVELOG DELETION POLICY
	  TO BACKED UP 2 TIMES TO SBT;
	```

See Also:

- ["Deleting Archived Redo Logs After Backups"](rcmbckba.md)
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) to learn how to manage archived redo logs in a Data Guard environment
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) for a complete explanation of the `CONFIGURE ARCHIVELOG DELETION POLICY` command and the conditions under which archived logs are eligible for deletion

## Configuring RMAN in a Data Guard Environment

If you use RMAN in a Data Guard environment, then you can use the `CONFIGURE` command to register and configure settings for the physical databases in this environment. RMAN uses the `DB_UNIQUE_NAME` initialization parameter to distinguish one database from another. Thus, it is critical that you maintain the uniqueness of the `DB_UNIQUE_NAME` in the Data Guard environment.

RMAN must be connected to a recovery catalog when you create or alter a configuration for a database in the Data Guard environment. If you use the `SET DBID` command to set the DBID in the [RMAN session](glossary.md), then you can configure a standby database even when RMAN is not connected as `TARGET` to a database in the Data Guard environment. You can even create a configuration for a standby database that has not yet been created.

You can use the following forms of the `CONFIGURE` command:

- `CONFIGURE DB_UNIQUE_NAME` defines a connection to a [physical standby database](glossary.md) and implicitly registers the new database.
	New standby databases are also automatically registered when RMAN connects as `TARGET` to a standby database for the first time.
- `CONFIGURE FOR DB_UNIQUE_NAME` configures settings for a database in the Data Guard environment.
	For example, you can configure channels, default devices, and so on for a specified database or for all databases in the environment. You can use `SHOW ALL FOR DB_UNIQUE_NAME` to show the configuration for a specific standby database or `SHOW ALL FOR DB_UNIQUE_NAME ALL` to show configurations for all known databases.

A Data Guard environment involves many considerations that are only relevant for Data Guard. For example, you can configure an [archived redo log deletion policy](glossary.md) based on whether archived logs are transferred to or applied on a standby database.

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB04700) to learn how to configure the RMAN environment for use with a standby database
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) for a complete explanation of the `CONFIGURE ARCHIVELOG DELETION POLICY` command and the conditions under which archived logs are eligible for deletion