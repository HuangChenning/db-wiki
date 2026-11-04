---
title: Backup and Recovery Reference
book: Oracle AI Database Backup and Recovery Reference
doc_id: E96242-15
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/rcmrf/allocOperandList.html
tags:
  - oracle
  - 19c
  - backup-and-recovery-reference
---

## 4.1 allocOperandList

Purpose

Use the `allocOperandList` subclause to control options on a **channel**, which is a connection between RMAN and a database instance.

Syntax

allocOperandList::=

![allocoperandlist](img/allocoperandlist.gif)

> {CONNECT connectStringSpec | {AUXILIARY FORMAT { formatSpec \[, formatSpec\]... | NEW} | FORMAT formatSpec \[, formatSpec\]... | TO DESTINATION toDestSpec \[, toDestSpec\]...} | MAXOPENFILES integer | MAXPIECESIZE sizeSpec | PARMS ' channel\_parms ' | RATE sizeSpec | SEND ' command '} \[ {CONNECT connectStringSpec | {AUXILIARY FORMAT { formatSpec \[, formatSpec\]... | NEW} | FORMAT formatSpec \[, formatSpec\]... | TO DESTINATION toDestSpec \[, toDestSpec\]...} | MAXOPENFILES integer | MAXPIECESIZE sizeSpec | PARMS ' channel\_parms ' | RATE sizeSpec | SEND ' command '}\]...


([connectStringSpec::=](connectStringSpec.md), [formatSpec::=](formatSpec.md), [sizeSpec::=](sizeSpec.md), [toDestSpec::=](toDestSpec.md))

Semantics

allocOperandList

| Syntax Element | Description |
| --- | --- |
| `CONNECT` `connectStringSpec` | Specifies a connect string to the database instance where RMAN conducts the backup or restore operations. Use this parameter to spread the work across different instances in an Oracle RAC configuration.  If you do not specify this parameter, and if you did not specify the `AUXILIARY` option, then RMAN conducts all operations on the target database instance specified by the command-line `CONNECT` parameter or `CONNECT` command. Typically, do not use the `CONNECT` parameter with the `AUXILIARY` option.  See Also: `connectStringSpec` and `RMAN` |
| `AUXILIARY FORMAT` | Specifies the format of image copies created on an auxiliary instance.  RMAN must be connected to the auxiliary instance with `CONNECT` `AUXILIARY` and have access to auxiliary channels. |
| `formatSpec` | Specifies a pattern for image copy names on an auxiliary instance.  The path must be valid on the auxiliary host.  See Also: `formatSpec` for valid substitution variables |
| `   NEW` | Creates an image copy in the directory specified by the `DB_CREATE_FILE_DEST` initialization parameter of the auxiliary instance.  The image copy name is in an Oracle Managed Files format. |
| `FORMAT` `formatSpec` | Specifies the format to use for the names backup pieces or image copies created on this channel. Example 4-1 illustrates this technique.  The `FORMAT` parameter is useful if you allocate multiple disk channels and want each channel to write to a different directory. The `FORMAT` parameter specified in `CONFIGURE` `CHANNEL` or `ALLOCATE CHANNEL` is semantically equivalent to the `FORMAT` parameter specified in the `BACKUP` command (not the `DATAFILECOPY FORMAT` parameter in [forRecoveryOfSpec](BACKUP.md)). If you specify the `FORMAT` parameter in the `BACKUP` command, then it overrides the `FORMAT` parameter specified in `CONFIGURE CHANNEL` or `ALLOCATE CHANNEL`.  If you do not specify `FORMAT`, then RMAN uses `%U` by default, which guarantees a unique name for the names of the backup files. If the fast recovery area is configured, then RMAN creates the backup files in the default disk location. Otherwise, the default disk location is operating system-specific (for example, `?/dbs` on Solaris).  You can specify up to four `FORMAT` strings. RMAN uses the second, third, and fourth values only when `BACKUP COPIES`, `SET BACKUP COPIES`, or `CONFIGURE ... BACKUP COPIES` is in effect. When choosing which format to use for each backup piece, RMAN uses the first format value for copy 1, the second format value for copy 2, and so forth. If the number of format values exceeds the number of copies, then the extra formats are not used. If the number of format values is less than the number of copies, then RMAN reuses the format values, starting with the first one.  Because the channels correspond to server sessions on the target database, the `FORMAT` string must use the conventions of the target host, not the client host. For example, if the RMAN client runs on a Windows host and the target database runs on a Linux host, then the `FORMAT` string must adhere to the naming conventions of a Linux file system or raw device.  See Also: `formatSpec` for available `FORMAT` parameters |
| `TO DESTINATION` toDestSpec | Specifies the directory where the backup is created. This parameter is valid for disk and not SBT channels. The backup files are created in an Oracle Managed Files (OMF) directory. Backup skips the files only when backups do not exist in the specified `TO DESTINATION`. |
| `MAXOPENFILES` `integer` | Controls the maximum number of input files that a `BACKUP` command can have open at any given time (the default is 8). Use this parameter to prevent "Too many open files" error messages when backing up a large number of files into a single backup set. |
| `MAXPIECESIZE` `sizeSpec` | Specifies the maximum size of each backup piece created on this channel. Example 4-2 illustrates this technique. Specify the size in bytes, kilobytes (`K`), megabytes (`M`), or gigabytes (`G`). The default setting is in bytes and is rounded down into kilobytes. For example, if you set `MAXPIECESIZE` to 5000, RMAN sets the maximum piece size at 4 kilobytes, which is the lower kilobyte boundary of 5000 bytes.  Note: You cannot use `BACKUP ... SECTION SIZE` with `MAXPIECESIZE`. |
| `PARMS` `'` `channel_parms` `'` | Specifies parameters for the `sbt` channel. Example 4-3 illustrates this technique. Do not use this port-specific string if you have specified `DEVICE TYPE DISK`.  You can use the following formats for the channel parameters:  - `'ENV=(``var1=val1``, ``var2=val2``,...)'` 	Specifies one or more environment variables required by the media manager in the server session corresponding to this RMAN client. Because RMAN is a client program, you can use the `ENV` parameter to set server session-specific variables that perform operations on behalf of the RMAN client, for example, `PARMS 'ENV=(OB_DEVICE_1=tape1)'`. 	Note: On Windows, Oracle recommends that you use the `SBT_PARMS` parameter to specify the environment variables, instead of the `ENV` parameter. For example, `PARMS 'SBT_PARMS=(OB_DEVICE_1=tape1)' 'SBT_LIBRARY=lib_name'.` - `'SBT_LIBRARY=` `lib_name` `'` 	In cases where the media management library supports it, (for example, the Oracle Database Cloud Backup for Amazon S3) and on the Windows platform, you must use the `SBT_PARMS` parameter to specify environment variables. In all other scenarios, you use the `ENV` variable. 	Note: On Windows, Oracle recommends that you use the `SBT_PARMS` parameter to specify the environment variables, instead of the `ENV` parameter. For example, `PARMS 'SBT_PARMS=(OB_DEVICE_1=tape1)'                           'SBT_LIBRARY=lib_name'.` 	Specifies which media library is used on this `sbt` channel, for example, `PARMS="SBT_LIBRARY=/oracle/lib/mmv.so"`. The default library is operating system-specific (for example, `libobk.so` on Linux and `ORASBT.DLL` on Windows.  For more information, see these topics in the Backup and Recovery User's Guide. - [Configuring RMAN to Make Backups to a Media Manager](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/rcmrf&id=BRADV-GUID-215D0081-288D-4A90-92C2-1E9CA8AF0CAB) to learn how to integrate media management libraries. - [Backing Up a Database to Cloud Using RMAN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/rcmrf&id=BRADV-GUID-B1EBFA43-F75F-4E2A-BC50-4FD570868332) to learn how to perform cloud backup and restores using RMAN. |
| `RATE` `sizeSpec` | Sets the maximum number of bytes (default), kilobytes (`K`), megabytes (`M`), or gigabytes (`G`) that RMAN reads each second on this channel. This parameter sets an upper limit for bytes read so that RMAN does not consume too much disk bandwidth and degrade performance. |
| `SEND` `'` `command` `'` | Sends a vendor-specific command string to all allocated channels. For example, you could specify an Oracle Secure Backup media family with `SEND 'OB_MEDIA_FAMILY datafile_mf'`.  On Windows, to send command strings to the SBT library, it is recommended that you use the `SEND` option instead of using `ENV` in the `PARAMS` option.  See Also: Your media manager documentation to determine whether this feature is supported and when to use it. |

Note:

Oracle Secure Backup (OSB) 19.1 desupport was announced on May 1, 2026 with premier support end date on September 30, 2027. See My Oracle Support note [PNEWS3035](https://support.oracle.com/support/?documentId=PNEWS3035) for more information. Please refer to [Lifetime Support Policy: Oracle Technology Products](https://www.oracle.com/support/lifetime-support/) for updated support timeframes.

Oracle recommends that database backups to cloud take advantage of Oracle Database Zero Data Loss Cloud Protect, which uses Oracle Zero Data Loss Autonomous Recovery Service in OCI. Cloud Protect offers an efficient incremental forever backup strategy, real-time transaction protection, logically air-gapped immutable backups, and fast, point-in-time recovery.

For customers who require database backups to Amazon S3, Oracle Database Cloud Backup for Amazon S3 may be used. This offering is similar to Oracle Secure Backup Cloud Module in that it is fully integrated with Recovery Manager (RMAN) and enables you to back up your Oracle database to Amazon S3. You can exchange your Oracle Secure Backup license for an Oracle Database Cloud Backup for Amazon S3 license on a 1:1 basis. See [Oracle Database Cloud Backup for Amazon S3](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/rcmrf&id=BRADV-GUID-F187E3A0-EA0E-49DA-B075-4FE7C5846A32) for more information.

toDestSpec

This subclause specifies either a directory or an Automated Storage Management (ASM) disk group for a backup piece or image copy. Refer to [toDestSpec::=](toDestSpec.md) for the syntax diagram.

Examples

Example 4-1 Specifying the Default Location for Disk Backups

This example allocates a disk channel that specifies a nondefault format, and then backs up the database to the nondefault location.

```
RUN
{
  ALLOCATE CHANNEL d1 DEVICE TYPE DISK FORMAT = '/disk1/bkup_%U';
  BACKUP DATABASE;
}
```

Example 4-2 Setting the Maximum Size of a Backup Piece

This example manually allocates an SBT channel, which specifies an Oracle Secure Backup tape drive, and makes a whole database backup. The `MAXPIECESIZE` parameter specifies that no backup piece written to tape can exceed 800 MB.

```
RUN
{
  ALLOCATE CHANNEL c1 DEVICE TYPE sbt 
    PARMS 'SBT_LIBRARY=/usr/local/oracle/backup/lib/libobk.so, ENV=(OB_DEVICE_1=stape1)'
    MAXPIECESIZE 800M;
  BACKUP DATABASE;
}
```

Example 4-3 Setting SBT Channel Parameters

This example configures the default SBT channel to use the Oracle Secure Backup tape drive named `stape1` and makes a database backup with the default channel:

```
CONFIGURE DEFAULT DEVICE TYPE TO sbt;
CONFIGURE CHANNEL DEVICE TYPE sbt PARMS 'ENV=(OB_DEVICE_1=stape1)';
BACKUP DATABASE;
```

Later you decide to back up the database to drive `stape2`. The following examples uses a manually allocated SBT channel to back up the database to `stape2`.

```
RUN
{
  ALLOCATE CHANNEL st2 DEVICE TYPE sbt 
    PARMS 'ENV=(OB_DEVICE_1=stape2)';
  BACKUP DATABASE;
}
```