---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/configuring-rman-client-advanced.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

RMAN configuration tasks include configuring advanced backup compression options.

### 6.1 Configuring Advanced Channel Options

The `CONFIGURE CHANNEL` command is used to configure RMAN channel options.

This section contains the following topics about advanced channel option:

- About Channel Control Options
- Configuring Specific Channel Parameters

See Also:

- [About RMAN Channels](rman-architecture.md) for a conceptual overview of configured and allocated channels
- [Configuring Channels](configuring-rman-client-basic.md) the basics for configuring channels
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF113) for `CONFIGURE` syntax

#### 6.1.1 About Channel Control Options

Whether you allocate channels manually or use automatic channel allocation, you can use channel commands and options to control behavior.

Table 6-1 summarizes the ways in which you can control channel behavior. Unless noted, all channel parameters are supported in both `CONFIGURE CHANNEL` and `ALLOCATE CHANNEL` commands.

Table 6-1 Channel Control Options

| Type of Channel Control | Commands |
| --- | --- |
| Limit I/O bandwidth consumption | Use the `RATE` channel parameter to act as a throttling mechanism for backups. |
| Limit backup sets and pieces | Use the `MAXPIECESIZE` channel parameter to set limits on the size of backup pieces. You can also use the `MAXSETSIZE` parameter on the `BACKUP` and `CONFIGURE` commands to set a limit for the size of backup sets. |
| Vendor-specific instructions | Use the `PARMS` channel parameter to specify vendor-specific information for a [media management software](glossary.md). You can also use the `SEND` command to send vendor-specific commands to a media manager. |
| Channel parallel backup and restore operations | Use `CONFIGURE DEVICE TYPE ... PARALLELISM` for persistent channel parallelism or multiple `ALLOCATE CHANNEL` commands for job-level parallelism. |
| Connection settings for database instances | Specify which instance performs an operation with the `CONNECT` channel parameter. |

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF102) for `ALLOCATE` `CHANNEL` syntax
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF113) for `CONFIGURE` syntax

#### 6.1.2 Configuring Specific Channel Parameters

In addition to configuring parameters that apply to all channels of a particular type, you can also use the `CONFIGURE` command to configure parameters that apply to one specific channel.

Configure specific channels by number when it is necessary to control the parameters set for each channel separately. This technique is necessary in the following situations:

- When running an Oracle Real Application Clusters (Oracle RAC) database in which individual nodes do not have access to the full set of backups. Each channel must be configured with a node-specific connect string so that all backups are accessible by at least one channel.
- When using a media manager that requires different `PARMS` settings on each channel.

To configure specific channel parameters:

- Run the `CONFIGURE CHANNEL` `n` command (where `n` is a positive integer less than 255) to configure a specific channel.
	When manually numbering channels, you must specify one or more channel options (for example, `MAXPIECESIZE` or [`FORMAT`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF195)) for each channel. When you use that specific numbered channel in a backup, the configured settings for that channel are used instead of the configured generic channel settings.

##### 6.1.2.1 Configuring Specific Channels: Examples

Example 6-1 Configuring Channel Parallelism for Disk Devices

This example sends disk backups to two different disks. Configure disk channels as follows:

```
CONFIGURE DEFAULT DEVICE TYPE TO disk;        # backup goes to disk
CONFIGURE DEVICE TYPE disk PARALLELISM 2;     # two channels used in parallel
CONFIGURE CHANNEL 1 DEVICE TYPE DISK FORMAT '/disk1/%U' # 1st channel to disk1 
CONFIGURE CHANNEL 2 DEVICE TYPE DISK FORMAT '/disk2/%U' # 2nd channel to disk2
BACKUP DATABASE; # backup - first channel goes to disk1 and second to disk2
```

Example 6-2 Configuring Channel Parallelism for Tape Devices

This example configures channels to create parallel database backups. You have two tape drives and want each drive to use tapes from a different tape media family. The backup data is divided between the two tape devices. Each configured channel backs up approximately half the total data.

```
CONFIGURE DEFAULT DEVICE TYPE TO sbt;    # backup goes to sbt
CONFIGURE DEVICE TYPE sbt PARALLELISM 2; # two sbt channels allocated by default
# Configure channel 1 to pool named first_pool
CONFIGURE CHANNEL 1 DEVICE TYPE sbt 
  PARMS 'ENV=(OB_MEDIA_FAMILY=first_pool)'; 
# configure channel 2 to pool named second_pool
CONFIGURE CHANNEL 2 DEVICE TYPE sbt 
  PARMS 'ENV=(OB_MEDIA_FAMILY=second_pool)'; 
BACKUP DATABASE; # first stream goes to 'first_pool' and second to 'second_pool'
```

##### 6.1.2.2 Relationship Between CONFIGURE CHANNEL and Parallelism Setting

The `PARALLELISM` setting is not constrained by the number of specifically configured channels.

For example, if you back up to 20 different tape devices, then you can configure 20 different SBT channels, each with a manually assigned number (from 1 to 20) and each with a different set of channel options. In such a situation, you can set `PARALLELISM` to any value up to the number of devices, in this instance 20.

RMAN always numbers parallel channels starting with `1` and ending with the `PARALLELISM` setting. For example, if the default device is SBT and parallelism is set to 3, then RMAN names the channels as follows:

```
ORA_SBT_TAPE_1
ORA_SBT_TAPE_2
ORA_SBT_TAPE_3
```

RMAN always uses the name `ORA_SBT_TAPE_` n even if you configure `DEVICE` `TYPE` `sbt` (not the synonymous `sbt_tape`). RMAN always allocates the number of channels specified in `PARALLELISM`, using specifically configured channels if you have configured them and generic channels if you have not. If you configure specific channels with numbers higher than the parallelism setting, then this setting prevents RMAN from using them.

See Also:

[About RMAN Channels](rman-architecture.md) to learn about channels

### 6.2 Configuring Advanced Backup Options

Backup options enable you to control aspects such as backup size, backup compression, and backup encryption.

" [About Configuring the Environment for RMAN Backups](configuring-rman-client-basic.md) " explains the basics for configuring RMAN to make backups. This section explains more advanced configuration options. This section contains the following topics:

#### 6.2.1 Configuring the Maximum Size of Backup Sets

The `CONFIGURE MAXSETSIZE` command limits the size of backup sets created on a channel. This `CONFIGURE` setting applies to any channel, whether manually allocated or configured, when the `BACKUP` command is used to create backup sets. The default value is given in bytes and is rounded down to the lowest kilobyte value.

In tape backups, it is possible for a [multiplexed backup set](glossary.md) to span multiple tapes, which means that blocks from each data file in the backup set are written to multiple tapes. If one tape of a multivolume backup set fails, then you lose the data on all the tapes rather than just one. If a backup is not a [multisection backup](glossary.md), then a backup set always includes a whole data file rather than a partial data file. You can use `MAXSETSIZE` to specify that each backup set fits on one tape rather than spanning multiple tapes.

The value set by the `CONFIGURE MAXSETSIZE` command is a default for the given channel. You can override the configured `MAXSETSIZE` value by specifying a `MAXSETSIZE` option for an individual `BACKUP` command.

Assume that you issue the following commands at the RMAN prompt:

```
CONFIGURE DEFAULT DEVICE TYPE TO sbt;
CONFIGURE CHANNEL DEVICE TYPE sbt PARMS 'ENV=(OB_MEDIA_FAMILY=first_pool)'; 
CONFIGURE MAXSETSIZE TO 7500K;
BACKUP TABLESPACE users;
BACKUP TABLESPACE tools MAXSETSIZE 5G;
```

The results are as follows:

- The backup of the `users` tablespace uses the configured [SBT](glossary.md) channel and the configured default `MAXSETSIZE` setting of `7500K`.
- The backup of the `tools` tablespace uses the `MAXSETSIZE` setting of `5G` specified in the `BACKUP` command.

See Also:

- [Limiting the Size of Backup Sets with BACKUP... MAXSETSIZE](backing-up-database-advanced.md)
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) for `BACKUP` syntax

#### 6.2.2 Configuring the Maximum Size of Backup Pieces

Backup piece size is an issue when it exceeds the maximum file size permitted by the file system or media management software. You can use the `MAXPIECESIZE` parameter of the `CONFIGURE` `CHANNEL` or `ALLOCATE` `CHANNEL` command to limit the size of backup pieces.

For example, to limit the backup piece size to 2 gigabytes or less, you can configure the automatic `DISK` channel as follows and then run `BACKUP` `DATABASE`:

```
CONFIGURE CHANNEL DEVICE TYPE DISK MAXPIECESIZE 2G;
BACKUP DATABASE;
```

Note:

In version 2.0 of the media management API, media management vendors can specify the maximum size of a backup piece that can be written to their media manager. RMAN respects this limit regardless of the settings that you configure for `MAXPIECESIZE`.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF113) to learn about the `CONFIGURE CHANNEL ... MAXPIECESIZE` command

#### 6.2.3 Configuring Backup Duplexing

Use the `CONFIGURE ... BACKUP COPIES` command to specify how many copies of each backup piece are created on the specified device type for the specified type of file. This type of backup is known as a duplexed backup set.

RMAN can duplex backups to either disk or tape, but cannot duplex backups to tape and disk simultaneously. When backing up to tape, ensure that the number of copies does not exceed the number of available tape devices. The `CONFIGURE` settings for duplexing only affect backups of data files, control files, and archived logs into backup sets, and do not affect image copies.

By default, `CONFIGURE` `...` `BACKUP` `COPIES` is set to `1` for each device type.

The following examples show possible duplexing configurations:

```
# Makes 2 disk copies of each data file and control file backup set
# (autobackups excluded)
CONFIGURE DATAFILE BACKUP COPIES FOR DEVICE TYPE DISK TO 2;
# Makes 3 copies of every archived redo log backup to tape
CONFIGURE ARCHIVELOG BACKUP COPIES FOR DEVICE TYPE sbt TO 3;
```

To return a `BACKUP` `COPIES` configuration to its default value, run the same `CONFIGURE` command with the `CLEAR` option, as in the following example:

```
CONFIGURE DATAFILE BACKUP COPIES FOR DEVICE TYPE sbt CLEAR;
```

Note:

If you do not want to create a persistent copies configuration, then you can specify copies with the `BACKUP` `COPIES` and the [`SET BACKUP COPIES`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF153) commands.

See Also:

- [About Multiple Copies of RMAN Backups](rman-backup-concepts.md) for an overview of duplexed backups
- [Duplexing Backup Sets](backing-up-database-advanced.md) to learn how to create duplexed backups
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) for `BACKUP` syntax
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF113) for `CONFIGURE` syntax
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF153) for `SET` syntax

#### 6.2.4 Configuring Tablespaces for Exclusion from Whole Database Backups

Sometimes you may want to omit a specified tablespace from part of the regular backup schedule. Use the `CONFIGURE` command to configure tablespace exclusion.

Here are some possible scenarios to consider:

- A tablespace is easy to rebuild, so it is more cost-effective to rebuild it than back it up every day.
- A tablespace contains temporary or test data that you do not need to back up.
- A tablespace does not change often and therefore should be backed up on a different schedule from other backups.

You can run [`CONFIGURE EXCLUDE FOR TABLESPACE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF113) to exclude the specified tablespace from the [`BACKUP DATABASE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) command. The exclusion condition applies to any data files that you add to this tablespace in the future.

For example, you can exclude testing tablespaces `cwmlite` and `example` from whole database backups as follows:

```
CONFIGURE EXCLUDE FOR TABLESPACE cwmlite;
CONFIGURE EXCLUDE FOR TABLESPACE example;
```

If you run the following command, then RMAN backs up all tablespaces in the database except `cwmlite` and `example`:

```
BACKUP DATABASE;
```

You can still back up the configured tablespaces by explicitly specifying them in a `BACKUP` command or by specifying the `NOEXCLUDE` option on a `BACKUP` `DATABASE` command. For example, you can enter one of the following commands:

```
BACKUP DATABASE NOEXCLUDE; #backs up database, including cwmlite and example
BACKUP TABLESPACE cwmlite, example;  # backs up only cwmlite and example
```

You can disable the exclusion feature for `cwmlite` and `example` as follows:

```
CONFIGURE EXCLUDE FOR TABLESPACE cwmlite CLEAR;
CONFIGURE EXCLUDE FOR TABLESPACE example CLEAR;
```

RMAN includes these tablespaces in future whole database backups.

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) for `BACKUP` and `CONFIGURE` syntax

#### 6.2.5 Configuring Compression Options

RMAN supports precompression processing and binary compression of backup sets. The `CONFIGURE COMPRESSION ALGORITHM` command enables you to configure compression options.

This following topics contain additional information about compression:

- About RMAN Precompression Block Processing
- About RMAN Supported Compression Levels

##### 6.2.5.1 About RMAN Precompression Block Processing

Better backup compression ratios are achieved by consolidating the free space in each data block, and setting that free space to binary zeroes. This precompression processing stage has the most benefit for data blocks that have been the subject of many deletes and inserts operations. Conversely, it has no effect on data blocks that are still in their initial loaded state.

The `OPTIMIZE FOR LOAD` option controls precompression processing. By specifying the default, `OPTIMIZE FOR LOAD TRUE`, you ensure that RMAN optimizes CPU usage and avoids precompression block processing. By specifying `OPTIMIZE FOR LOAD FALSE`, RMAN uses additional CPU resources to perform precompression block processing.

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF113) for `CONFIGURE` and `SET` syntax

##### 6.2.5.2 About RMAN Supported Compression Levels

Oracle Database provides two categories of compression algorithms: a default compression algorithm and a group of compression algorithms available with the Oracle Advanced Compression option.

The default algorithm is a standard feature of Oracle Database while the Oracle Advanced Compression option is a separately purchased option.

See Also:

- About RMAN Default Compression
- About Oracle Advanced Compression Option

###### 6.2.5.2.1 About RMAN Default Compression

Use the CONFIGURE command to configure the default compression algorithm, which does not require the Oracle Advanced Compression option.

Example 6-3 Configuring Basic Compression for Backup

The following example configures basic compression for RMAN backups..

```
CONFIGURE COMPRESSION ALGORITHM 'BASIC';
```

###### 6.2.5.2.2 About Oracle Advanced Compression Option

If you have enabled the Oracle Advanced Compression option, you can choose from the compression levels listed in the following table.

| Compression Level | Performance Benefits and Trade-Offs |
| --- | --- |
| `HIGH` | Best suited for backups over slower networks where the limiting factor is network speed. |
| `MEDIUM` | Recommended for most environments. Good combination of compression ratios and speed. |
| `LOW` | Least effect on backup throughput. |

The compression ratio generally increases from low to high, with a trade-off of potentially consuming more CPU resources.

Because the performance of the various compression levels depends on the nature of the data in the database, network configuration, system resources and the type of computer system and its capabilities, Oracle cannot document universally applicable performance statistics. Which level is best for your environment depends on how balanced your system is regarding bandwidth into the CPU and the actual speed of the CPU. It is highly recommended that you run tests with the different compression levels on the data in your environment. Choosing a compression level based on your environment, network traffic characteristics (workload), and data set is the only way to ensure that the backup set compression level can satisfy your organization's performance requirements and applicable service level agreements.

Note:

Restoring a compressed backup is performed inline, and does not require decompression.

See Also:

- See [Oracle Database Licensing Information User Manual](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=DBLIC-GUID-AB56CEE3-955E-4E56-8B44-6075E889C283) for more information about the Oracle Advanced Compression option.
- If you are backing up to tape and your tape device performs its own compression, then do not use both RMAN backup set compression and the media manager vendor's compression. See the discussion of tuning RMAN's tape backup performance in [Tuning RMAN Performance](tuning-rman-performance.md).

#### 6.2.6 Configuring Backup Encryption

For improved security, you can configure backup encryption for RMAN backup sets. Encrypted backups cannot be read if they are obtained by unauthorized users.

This section contains the following topics:

- About Backup Encryption
- Configuring RMAN Backup Encryption Modes
- Configuring the Backup Encryption Algorithm

##### 6.2.6.1 About Backup Encryption

The `V$RMAN_ENCRYPTION_ALGORITHMS` view contains a list of encryption algorithms supported by RMAN. If no encryption algorithm is specified, then the default encryption algorithm is 128-bit Advanced Encryption Standard (AES).

RMAN encryption requires the [`COMPATIBLE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=REFRN10019) initialization parameter at a target database to be at least 10.2.0.

The [Oracle Secure Backup](glossary.md) [media management software](glossary.md) is the only supported interface for making encrypted RMAN backups directly to tape. RMAN issues an `ORA-19919` error if you attempt to create encrypted RMAN backups using a media manager other than Oracle Secure Backup.

When you use the [`BACKUP`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) `BACKUPSET` command with encrypted backup sets, the backup sets are backed up in encrypted form. Because `BACKUP BACKUPSET` copies an already-encrypted backup set to disk or tape, no decryption key is needed during `BACKUP BACKUPSET`. The data is never decrypted during any part of the operation. The `BACKUP BACKUPSET` command can neither encrypt nor decrypt backup sets.

Encrypted backups are decrypted automatically during restore and recovery, if the required decryption keys are available. Each backup set gets a separate key. The key is stored in encrypted form in the backup piece. The backup is decrypted with keys obtained by a user-supplied password or the Oracle software keystore.

RMAN Encryption Modes

RMAN offers the following encryption modes:

- Transparent encryption
	This is the default mode and uses the Oracle software keystore. A keystore is a password-protected container used to store a Transparent Data Encryption (TDE) key. In previous releases, this container was referred to as a wallet.
- Password encryption
	This mode uses only password protection. You must provide a password when creating and restoring encrypted backups.
- Dual mode encryption
	This mode requires either the keystore or a password.

Note:

Keystore-based encryption is more secure than password-based encryption because no passwords are involved. Use password-based encryption only when it is absolutely necessary because your backups must be transportable.

###### 6.2.6.1.1 Transparent Encryption of Backups

Transparent encryption can create and restore encrypted backups with no DBA intervention, if the required Oracle key management infrastructure is available.

Transparent encryption is best suited for day-to-day backup operations, where backups are restored to the same database from which they were created. Transparent encryption is the default for RMAN encryption.

When you use transparent encryption, you must first configure an Oracle software keystore for each database. Transparent backup encryption supports both the auto-login software keystore and password-based software keystore. When you use the auto-login software keystore, encrypted backup operations can be performed at any time, because the auto-login keystore is always open. When you use the password-based software keystore, the keystore must be opened before you can perform backup encryption.

Caution:

If you use an auto-login keystore, do not back it up along with your encrypted backup data, because users can read the encrypted backups if they obtain both the backups and the autologin keystore. It is safe to back up the Oracle keystore because that form of the keystore cannot be used without the keystore password.

After the Oracle keystore is configured, encrypted backups can be created and restored with no further DBA intervention. If some columns in the database are encrypted with Transparent Data Encryption (TDE) column encryption, and if those columns are backed up using backup encryption, then those columns are encrypted a second time during the backup. When the backup sets are decrypted during a restore operation, the encrypted columns are returned to their original encrypted form.

Because the Oracle key management infrastructure archives all previous master keys in the Oracle keystore, changing or resetting the current database master key does not affect your ability to restore encrypted backups performed with an older master key. You can reset the database master key at any time. RMAN can restore all encrypted backups that were ever created by this database.

Caution:

If you lose your Oracle keystore, then you are unable to restore any transparently encrypted backups.

Note:

[Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ASOAG600) for information about configuring an Oracle software keystore

###### 6.2.6.1.2 Password Encryption of Backups

Password encryption requires that the DBA provide a password when creating and restoring encrypted backups. Restoring a password-encrypted backup requires the same password that was used to create the backup.

Password encryption is useful for backups that are restored at remote locations, but which must remain secure in transit. Password encryption cannot be persistently configured. You do not need to configure an Oracle keystore if password encryption is used exclusively.

Caution:

If you forget or lose the password that you used to encrypt a password-encrypted backup, then you are unable to restore the backup.

To use password encryption, use the [`SET`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF153) `ENCRYPTION ON IDENTIFIED BY` `password` ` ONLY` command in your RMAN scripts.

###### 6.2.6.1.3 Dual Mode Encryption of Backups

Dual-mode encrypted backups can be restored either transparently or by specifying a password.

Dual-mode encrypted backups are useful when you create backups that are normally restored on-site using the Oracle keystore, but which occasionally must be restored offsite, where the Oracle keystore is not available.

When restoring a dual-mode encrypted backup, you can use either the Oracle keystore or a password for decryption.

Caution:

If you forget or lose the password that you used to encrypt a dual-mode encrypted backup and you also lose your Oracle keystore, then you are unable to restore the backup.

To create dual-mode encrypted backup sets, specify the `SET ENCRYPTION ON IDENTIFIED BY` `password` command in your RMAN scripts.

##### 6.2.6.2 Configuring RMAN Backup Encryption Modes

You can use the `CONFIGURE` command to persistently configure transparent encryption of backups.

You can use the command to specify the following:

- Whether to use transparent encryptions for backups of all database files
- Whether to use transparent encryptions for backups of specific tablespaces
- Which algorithm to use for encrypting backups

You can also use the `SET` `ENCRYPTION` command to perform the following actions:

- Override the encryption settings specified by the [`CONFIGURE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF113) `ENCRYPTION` command. For example, you can use `SET` `ENCRYPTION` `OFF` to create an unencrypted backup, even though a database is configured for encrypted backups.
- Set a password for backup encryption, persisting until the RMAN client exits. Because of the sensitive nature of passwords, RMAN does not permit configuration of passwords that persist across RMAN sessions.

Using or not using persistent configuration settings controls whether archived redo log backups are encrypted. Backup sets containing archived redo log files are encrypted if any of the following are true:

- `SET` `ENCRYPTION` `ON` is in effect when the archive log backup is being created.
- Encryption is configured for backups of the whole database or at least one tablespace.

This behavior ensures that the redo associated with any encrypted backup of a data file is also encrypted.

To configure the environment so that all RMAN backups are encrypted:

1. Set up the Oracle keystore as explained in [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ASOAG600).
2. ```
	CONFIGURE ENCRYPTION FOR DATABASE ON;
	```
	At this stage, all RMAN backup sets created by this database use transparent encryption by default.

You can explicitly override the persistent encryption configuration for an [RMAN session](glossary.md) with the following command:

```
SET ENCRYPTION ON;
```

The encryption setting remains in effect until you issue the `SET` `ENCRYPTION` `OFF` command during an RMAN session, or change the persistent setting again with the following command:

```
CONFIGURE ENCRYPTION FOR DATABASE OFF;
```

##### 6.2.6.3 Configuring the Backup Encryption Algorithm

You can use the `CONFIGURE` command to persistently configure the default algorithm to use for encryption when writing backup sets.

Possible values are listed in `V$RMAN_ENCRYPTION_ALGORITHMS`. The default algorithm is AES 128-bit.

To configure the default backup encryption algorithm:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. Ensure that the target database is mounted or open.
3. Execute the `CONFIGURE ENCRYPTION ALGORITHM` command, specifying a valid value from `V$RMAN_ENCRYPTION_ALGORITHMS.ALGORITHM_NAME`.
	The following example configures the algorithm to AES 256-bit encryption:
	```
	CONFIGURE ENCRYPTION ALGORITHM TO 'AES256';
	```

### 6.3 Configuring Auxiliary Instance Data File Names

You may want to set the names of data files in the auxiliary instance when performing operations such as data file tablespace point-in-time recovery (TSPITR) or data transfer with RMAN. You set these names before starting the TSPITR or database duplication.

The command is as follows, where `datafileSpec` identifies some data file by its original name or data file number, and `filename` is the new path for the specified file:

```
CONFIGURE AUXNAME FOR datafileSpec TO 'filename';
```

For example, you might configure a new auxiliary name for data file `2` as follows:

```
CONFIGURE AUXNAME FOR DATAFILE 2 TO '/newdisk/datafiles/df2.df';
```

As with other settings, the [`CONFIGURE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF113) command setting persists across RMAN sessions until cleared with `CONFIGURE ``...` `CLEAR`, as shown in the following example:

```
CONFIGURE AUXNAME FOR DATAFILE 2 CLEAR;
```

If you are performing TSPITR or running the [`DUPLICATE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF126) command, then by using `CONFIGURE AUXNAME` you can preconfigure the file names for use on the auxiliary database without manually specifying the auxiliary file names during the procedure.

When renaming files with the `DUPLICATE` command, `CONFIGURE AUXNAME` is an alternative to [`SET NEWNAME`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF153) command. The difference is that after you set the `AUXNAME` the first time, you do not need to reset the file name when you issue another `DUPLICATE` command; the `AUXNAME` setting remains in effect until you issue `CONFIGURE AUXNAME` `...` `CLEAR`. In contrast, you must reissue the `SET NEWNAME` command every time you rename files.

See Also:

- [Performing RMAN Tablespace Point-in-Time Recovery (TSPITR)](performing-rman-tspitr.md) for more details on using `CONFIGURE AUXNAME` for TSPITR
- [Duplicating Databases](rman-duplicating-databases.md) for more details on using `CONFIGURE AUXNAME` in performing database duplication

### 6.4 Configuring the Snapshot Control File Location

When RMAN needs a read-consistent version of the control file, it creates a temporary snapshot control file. RMAN needs a snapshot control file when resynchronizing with the recovery catalog or when making a backup of the current control file.

The default location for the snapshot control file is platform-specific and depends on the Oracle home of each target database. For example, the default file name on some Linux platforms is `$ORACLE_HOME/dbs/snapcf_@.f`. If a [fast recovery area](glossary.md) is configured for a target database, then the default location for the snapshot control file is not the fast recovery area.

This section contains the following topics:

- Viewing the Configured Location of the Snapshot Control File
- Setting the Location of the Snapshot Control File

#### 6.4.1 Viewing the Configured Location of the Snapshot Control File

You can see the current snapshot location by running the `SHOW` command.

This example shows a snapshot location that is determined by the default rule:

```
RMAN> SHOW SNAPSHOT CONTROLFILE NAME;
CONFIGURE SNAPSHOT CONTROLFILE NAME TO '/oracle/dbs/snapcf_trgt.f'; # default
```

This example shows a snapshot control file that has a nondefault file name:

```
RMAN> SHOW SNAPSHOT CONTROLFILE NAME;
CONFIGURE SNAPSHOT CONTROLFILE NAME TO '/oracle/oradata/trgt/snap_trgt.ctl';
```

#### 6.4.2 Setting the Location of the Snapshot Control File

Use the `CONFIGURE SNAPSHOT CONTROLFILE NAME TO '` `filepath` `'` command to change the name and path of the snapshot control file. Subsequent snapshot control files that RMAN creates use the specified name and path.

In an Oracle Real Application Clusters (Oracle RAC) environment, the snapshot control file location must be on shared storage—that is, storage that is accessible to all Oracle RAC instances.

For example, start RMAN, connect to the target database, and then enter:

```
CONFIGURE SNAPSHOT CONTROLFILE NAME TO '/oracle/oradata/trgt/snap_trgt.ctl';
```

You can also set the snapshot control file name to a [raw device](glossary.md).

To reset the snapshot control file location to the default, run the `CONFIGURE SNAPSHOT CONTROLFILE NAME CLEAR` command.

See Also:

- [Resynchronizing the Recovery Catalog](managing-recovery-catalog.md)
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RACAD320) for details about handling snapshot control files in Oracle RAC configurations

### 6.5 Configuring RMAN for Use with a Shared Server

RMAN cannot connect to a target database through a shared server dispatcher. RMAN requires a dedicated server process.

If your target database is configured for a shared server, then you must modify your Oracle Net configuration to provide dedicated server processes for RMAN connections.

To ensure that RMAN does not connect to a dispatcher when a target database is configured for a shared server, the net service name used by RMAN must include `(SERVER=DEDICATED)` in the `CONNECT_DATA` attribute of the connect string.

Oracle Net configuration varies greatly from system to system. The following procedure illustrates only one method. This scenario assumes that the following service name in `tnsnames.ora` file connects to a target database using the shared server architecture, where `inst1` is a value of the `SERVICE_NAMES` initialization parameter:

```
inst1_shs =
  (DESCRIPTION=
    (ADDRESS=(PROTOCOL=tcp)(HOST=inst1_host)(port=1521))
    (CONNECT_DATA=(SERVICE_NAME=inst1)(SERVER=shared))
  )
```

Note:

Starting with Oracle Database 19c, customer use of the `SERVICE_NAMES` parameter is deprecated. It can be desupported in a future release. To manage your services, Oracle recommends that you use the `SRVCTL` or `GDSCTL` command line utilities, or the `DBMS_SERVICE` package.

To use RMAN with a shared server:

1. Create a net service name in the `tnsnames.ora` file that connects to the nonshared SID. For example, enter:
	```
	inst1_ded =
	  (DESCRIPTION=
	    (ADDRESS=(PROTOCOL=tcp)(HOST=inst1_host)(port=1521))
	    (CONNECT_DATA=(SERVICE_NAME=inst1)(SERVER=dedicated))
	  )
	```
2. Start SQL\*Plus and then connect using both the shared server and dedicated server service names to confirm the mode of each session.
	For example, connect with `SYSBACKUP` or `SYSDBA` privilege to `inst1_ded` and then execute the following `SELECT` statement (sample output included):
	```
	SQL> SELECT SERVER 
	  2  FROM   V$SESSION 
	  3  WHERE  SID = (SELECT DISTINCT SID FROM V$MYSTAT);
	SERVER   
	---------
	DEDICATED
	1 row selected.
	```
	To connect to a shared server session, connect with `SYSBACKUP` or `SYSDBA` privilege to `inst1_shs` and then execute the following `SELECT` statement (sample output included):
	```
	SQL> SELECT SERVER 
	  2  FROM   V$SESSION 
	  3  WHERE  SID = (SELECT DISTINCT SID FROM V$MYSTAT);
	SERVER   
	---------
	SHARED 
	1 row selected.
	```
3. Start RMAN and connect to the target database using the dedicated service name. Optionally, connect to a recovery catalog.
	See Also:
	Your platform-specific Oracle documentation and the [Oracle Database Net Services Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=NETRF005) for a complete description of Oracle Net connect string syntax

### 6.6 Enabling Lost Write Detection

A data block lost write occurs when an I/O subsystem acknowledges the completion of the block write, but the write did not occur in the persistent storage. On a subsequent block read, the I/O subsystem returns the stale version of the data block, which might be used to update other blocks of the database, thereby corrupting it.

You can set the [`DB_LOST_WRITE_PROTECT`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=REFRN10268) initialization parameter to `TYPICAL` or `FULL` so that a database records buffer cache block reads in the redo log. The default setting is `NONE`. When the parameter is set to `TYPICAL`, the instance logs buffer cache reads for read/write tablespaces in the redo log, but not read-only tablespaces. When set to `FULL`, the instance also records reads for read-only tablespaces. The performance overhead for `TYPICAL` mode is approximately 5 to 10% and potentially higher for `FULL` mode.

Lost write detection is most effective when used with Data Guard. In this case, you set `DB_LOST_WRITE_PROTECT` in both primary and standby databases. When a standby database applies redo during managed recovery, it reads the corresponding blocks and compares the SCNs with the SCNs in the redo log. If the block SCN on the primary database is lower than on the standby database, then it detects a lost write on the primary database and throws an external error (`ORA-752`). If the SCN is higher, it detects a lost write on the standby database and throws an internal error (`ORA-600 [3020]`). In either case, the standby database writes the reason for the failure in the alert log and trace file.

To repair a lost write on a primary database, you must initiate failover to the standby database. To repair a lost write on a standby database, you must re-create the entire standby database or restore a backup of only the affected files.

Enabling lost write detection is also useful when you are not using Data Guard. In this case, you can encounter a lost write in two ways: during normal database operation or during media recovery. In the first case, there is no direct way to detect the error. Indirect symptoms such as inconsistent tables cannot be unambiguously traced to the lost write. If you retained a backup made before the suspected lost write, however, then you can restore this backup to an alternative location and recover it. To diagnose the problem, recover the database or tablespace to the SCN of the stale block read, which then generates the lost write error (`ORA-752`).

If a lost write error is encountered during media recovery, the only response is to open the database with the `RESETLOGS` option. The database is in a consistent state, but all data after the `RESETLOGS` SCN is lost. If you recover a backup made after database creation, you have no guarantee that other stale blocks have not corrupted the database. This possibility exists because the restored backup may have been made after an earlier lost write. To guarantee that no lost writes have corrupted the database, you must perform media recovery from database creation, which is not a practical strategy for most database environments.

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SBYDB00930) to learn how to use a standby database for lost write detection and repair
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=REFRN10268) to learn about the `DB_LOST_WRITE_PROTECT` initialization parameter

### 6.7 Enabling Shadow Lost Write Protection

Shadow lost write protection provides fast detection and immediate response to a data block lost rewrite thereby minimizing data loss and database repair time. A standby database is not mandatory for using shadow lost write protection.

A data block lost write occurs when an I/O subsystem acknowledges the completion of a block write, but the write did not occur in the storage. Subsequent block reads will return the stale version of the data block, which may be used to update other data blocks, thus corrupting data. Shadow lost write protection uses shadow tablespaces to store only SCNs for the tracked data files. When a tracked data block is read from disk, shadow lost write protection detects lost writes by comparing the SCN for the block in the shadow tablespace with the SCN of the most recent write in the block being read.

Shadow lost write protection can be enabled at the database level, PDB level, tablespace level, or data file level. The database compatibility level must be 18.0.0 or higher.

To use shadow lost write protection:

- Create one or more shadow tablespaces for shadow lost write protection using the `CREATE BIGFILE TABLESPACE` command with the `LOST WRITE PROTECTION` clause.
- Enable shadow lost write protection at the required level (database, PDB, tablespace, or data file). Use the `ALTER` command with the `ENABLE LOST WRITE PROTECTION` clause to enable shadow lost write protection.

When shadow lost write protection is enabled, RMAN checks the blocks being read for lost writes. If any lost writes are found, an error is displayed and the backup operation is terminated.

Note:

Shadow lost write protection is not related to lost write protection that is configured using the `DB_LOST_WRITE_PROTECT` initialization parameter.