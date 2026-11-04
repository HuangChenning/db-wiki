---
title: RMAN Backup Concepts
book: "Backup and Recovery User's Guide"
doc_id: E10642-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmcncpt.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-users-guide
---

## 8 RMAN Backup Concepts

This chapter describes the general concepts that you must understand to make any type of RMAN backup. This chapter contains the following topics:

## Consistent and Inconsistent RMAN Backups

The RMAN command for making backups is [`BACKUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107). The RMAN `BACKUP` command supports backing up the following types of files:

- Datafiles and control files
- Server parameter file
- Archived redo logs
- RMAN backups

Although the database depends on other types of files, such as network configuration files, password files, and the contents of the Oracle home, you cannot back up these files with RMAN. Likewise, some features of Oracle Database, such as external tables, may depend upon files other than the datafiles, control files, and redo log. RMAN cannot back up these files. Use some non-RMAN backup solution for any files not in the preceding list.

When you execute the `BACKUP` command in RMAN, the output is always either one or more backup sets or one or more image copies. A [backup set](glossary.md) is an RMAN-specific proprietary format, whereas an [image copy](glossary.md) is a bit-for-bit copy of a file. By default, RMAN creates backup sets.

### Consistent Backups

You can use the [`BACKUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) command to make consistent and inconsistent backups of the database. A [consistent backup](glossary.md) occurs when the database is in a consistent state. A database is in a consistent state after being shut down with the [`SHUTDOWN`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2016.htm#RCMRF155) `NORMAL`, `SHUTDOWN IMMEDIATE`, or `SHUTDOWN TRANSACTIONAL` commands. A consistent shutdown guarantees that all redo has been applied to the datafiles. If you mount the database and make a backup at this point, then you can restore the database backup later and open it without performing media recovery.

### Inconsistent Backups

Any database backup that is not consistent is an [inconsistent backup](glossary.md). A backup made when the database is open is inconsistent, as is a backup made after an instance failure or `SHUTDOWN ABORT` command. When a database is restored from an inconsistent backup, Oracle Database must perform media recovery before the database can be opened, applying any pending changes from the redo logs.

Note:

RMAN does not permit you to make inconsistent backups when the database is in `NOARCHIVELOG` mode. If you employ user-managed backup techniques for a `NOARCHIVELOG` database, then you must not make inconsistent backups of this database.

If the database runs in `ARCHIVELOG` mode, and you back up the archived redo logs and datafiles, inconsistent backups can be the foundation for a sound backup and recovery strategy. Inconsistent backups offer superior availability because you do not have to shut down the database to make backups that fully protect the database.

## Online Backups and Backup Mode

When performing a [user-managed backup](glossary.md) of an online tablespace or database, an operating system utility can back up a data file at the same time that the database writer (DBWR) is updating the file. It is possible for the utility to read a block in a half-updated state, so that the block that is copied to the backup media is updated in its first half, while the second half contains older data. This type of [logical corruption](glossary.md) is known as a [fractured block](glossary.md), that is, a block that is not consistent with an SCN. If this backup must be restored later, and if the block requires recovery, then recovery fails because the block is not usable.

When performing a user-managed online backup, you must place your datafiles into [backup mode](glossary.md) with the [`ALTER DATABASE`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1004.htm#SQLRF00802) or [`ALTER TABLESPACE`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_3002.htm#SQLRF01002) statement with the `BEGIN BACKUP` clause. When a tablespace is in backup mode, the database writes the before image for an entire block to the redo stream before modifying a block. The database also records changes to the block in the online redo log. Backup mode also freezes the [data file checkpoint](glossary.md) until the file is removed from backup mode. Oracle Database performs this safeguard because it cannot guarantee that a third-party backup tool copies the file header before copying the data blocks.

Unlike user-managed tools, RMAN does not require extra logging or backup mode because it knows the format of data blocks. RMAN is guaranteed not to back up fractured blocks. During an RMAN backup, a database server session reads each data block and checks whether it is fractured by comparing the block header and footer. If a block is fractured, then the session rereads the block. If the same fracture is found, then the block is considered permanently corrupt. Also, RMAN does not need to freeze the data file header checkpoint because it knows the order in which the blocks are read, which enables it to capture a known good checkpoint for the file.

See Also:

["Making User-Managed Backups of Online Tablespaces and Data Files"](osbackup.md) to learn how to back up online tablespaces when not using RMAN

## Backup Sets

When you execute the [`BACKUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) command in RMAN, you create one or more backup sets or image copies. By default, RMAN creates backup sets regardless of whether the destination is disk or a media manager.

Note:

Data file backup sets are typically smaller than data file image copies and take less time to write.

This section contains the following topics:

- Backup Sets and Backup Pieces
- Block Compression for Backup Sets
- Binary Compression for Backup Sets
- Backup Undo
- Encryption for Backup Sets
- Filenames for Backup Pieces
- Number and Size of Backup Pieces
- Number and Size of Backup Sets
- Multiplexed Backup Sets
- Proxy Copies

### Backup Sets and Backup Pieces

RMAN can store backup data in a logical structure called a [backup set](glossary.md), which is the smallest unit of an RMAN backup. A backup set contains the data from one or more datafiles, archived redo logs, control files, or server parameter file. Backup sets, which are only created and accessed through RMAN, are the only form in which RMAN can write backups to media managers such as tape drives and tape libraries.

A backup set contains one or more binary files in an RMAN-specific format. Each of these files is known as a [backup piece](glossary.md). A backup set can contain multiple datafiles. For example, you can back up 10 datafiles into a single backup set consisting of a single backup piece. In this case, RMAN creates one backup piece as output. The backup set contains only this backup piece.

If you specify the `SECTION SIZE` parameter on the `BACKUP` command, then RMAN produces a [multisection backup](glossary.md). This is a backup of a single large file, produced by multiple channels in parallel, each of which produces one backup piece. Each backup piece contains one [file section](glossary.md) of the file being backed up.

For non-multisection backups, RMAN only records backup sets in the repository that complete successfully. There is no such thing as a partial backup set. This differs from an unsuccessful multisection backup, where it is possible for RMAN metadata to contain a record for a partial backup set. In the latter case, you must use the `DELETE` command to delete the partial backup set.

Note:

RMAN never considers partial backups as candidates for restore and recovery.

See Also:

[Chapter 9, "Backing Up the Database"](rcmbckba.md)

### Block Compression for Backup Sets

RMAN uses two types of block compression when creating backup sets:

- Unused Block Compression (Supports disk backup and Oracle Secure Backup tape backup)
- Null Block Compression (Supports all backups)

Although it is referred to as block compression, it might be helpful to think of block compression as block skipping. Rather than compressing the data in the blocks, RMAN completely eliminates the blocks from the backup. RMAN reads blocks from a data file and writes them to a backup set. If unused block compression is enabled, RMAN reads only those blocks of the data file in an extent that currently belongs to a database segment. Unused block compression can only be employed when backing up tablespaces whose space is locally managed. When not employing unused block compression, RMAN reads every block of the data file. Before RMAN writes a block to the backup set, it applies the null block test, and if the block has never been used, it does not write that block to the backup set.

#### Unused Block Compression

During [unused block compression](glossary.md), RMAN does not check each block. Instead, RMAN reads the bitmaps that indicate what blocks are currently allocated and then only reads the blocks that are currently allocated.

Unused block compression is turned on automatically when all of the following five conditions are true:

- The `COMPATIBLE` initialization parameter is set to 10.2 or higher.
- There are currently no guaranteed restore points defined for the database.
- The data file is locally managed.
- The data file is being backed up to a backup set as part of a full backup or a level 0 incremental backup.
- The backup set is created on disk, or Oracle Secure Backup is the media manager.

#### Null Block Compression

During null block compression, RMAN checks every block to see if it has ever contained data. Blocks that have never contained data are not backed up. Blocks that have contained data, either currently or in the past, are backed up.

### Binary Compression for Backup Sets

RMAN supports [binary compression](glossary.md) of backup sets. Binary compression is only enabled when you specify `AS COMPRESSED BACKUPSET` in the `BACKUP` command, or one-time with the `CONFIGURE DEVICE TYPE <DISK | SBT> BACKUP TYPE TO COMPRESSED BACKUPSET` command.You have two binary compression options:

- You can use the `BASIC` compression algorithm, which does not require the Advanced Compression Option. This setting offers a compression ratio comparable to `MEDIUM`, at the expense of additional CPU consumption.
- If you have enabled the Oracle Database 11g Release 2 Advanced Compression Option, you can choose from the compression levels outlined in ["Advanced Compression Option"](rcmconfa.md).

See Also:

- ["Configuring Compression Options"](rcmconfa.md)
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) to learn about `BACKUP AS BACKUPSET` and `CONFIGURE COMPRESSION ALGORITHM`

### Backup Undo

In [backup undo optimization](glossary.md), RMAN excludes undo not needed for recovery of a backup, that is, for transactions that have been committed. Backup undo optimization works for level 0 and full disk backups and Oracle Secure Backup (OSB) tape backups. Unlike [backup optimization](glossary.md), backup undo optimization is not configurable.

### Encryption for Backup Sets

RMAN supports [backup encryption](glossary.md) for backup sets. You can use wallet-based transparent encryption, password-based encryption, or both. You can use the [`CONFIGURE ENCRYPTION`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) command to configure persistent transparent encryption. Use the [`SET ENCRYPTION`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2014.htm#RCMRF153) command at the [RMAN session](glossary.md) level to specify password-based encryption.

Note:

Wallet-based encryption is more secure than password-based encryption because no passwords are involved. You should use password-based encryption only when it is absolutely necessary because your backups must be transportable.

To create encrypted backups on disk with RMAN, the database must use the Advanced Security Option. For encrypted RMAN backups directly to tape, the [Oracle Secure Backup](glossary.md) [SBT](glossary.md) is the only supported interface.

See Also:

- ["Configuring Backup Encryption"](rcmconfa.md)
- ["Encrypting RMAN Backups"](rcmbckad.md)

### Filenames for Backup Pieces

You can either let RMAN determine a unique name for backup pieces or use the [`FORMAT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl010.htm#RCMRF195) clause to specify a name. If you do not specify the `FORMAT` parameter, then RMAN automatically generates a unique file name with the `%U` substitution variable in the default backup location.

An example of RMAN generating an SBT backup piece name by `%U` is:

```
2i1nk47_1_1
```

An example of a non- Oracle Managed File (OMF) backup piece on disk is:

```
/backups/TEST/2i1nk47_1_1
```

The `FORMAT` clause supports substitution variables other than `%U` for generating unique file names. For example, you can use `%d` to generate the name of the database, `%I` for the DBID, `%t` for the time stamp, and so on.

You can specify up to four `FORMAT` parameters. If you specify multiple `FORMAT` parameters, then RMAN uses the multiple `FORMAT` parameters only when you specify multiple copies. You can create multiple copies by using the `BACKUP ...` `COPIES`, [`SET BACKUP COPIES`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2014.htm#RCMRF153), or [`CONFIGURE ... BACKUP COPIES`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) commands.

Note:

If you use a media manager, then check your vendor documentation for restrictions on `FORMAT`, such as the size of the name, the naming conventions, and so on.

See Also:

- ["Specifying a Format for RMAN Backups"](rcmbckba.md)
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) for descriptions of the `FORMAT` clause and the substitution variables

### Number and Size of Backup Pieces

By default a backup set contains one backup piece. To restrict the size of each backup piece, specify the `MAXPIECESIZE` option of the [`CONFIGURE CHANNEL`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) or [`ALLOCATE CHANNEL`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta004.htm#RCMRF102) commands. This option limits backup piece size to the specified number of bytes. If the total size of the backup set is greater than the specified backup piece size, then RMAN creates multiple physical pieces to hold the backup set contents.

You can use this option for media managers that cannot manage a backup piece that spans multiple tapes. For example, if a tape can hold 10 GB, but the backup set being created must hold 80 GB of data, then you must instruct RMAN to create backup pieces of 10 GB, small enough to fit on the tapes used with the media manager. In this case, the backup set media consists of eight tapes. Media managers supporting SBT 2.0 can return a value to RMAN indicating the largest supported backup piece size, which RMAN uses in planning backup activities.

If you specify the `SECTION SIZE` parameter on the `BACKUP` command, then RMAN can create a [multisection backup](glossary.md). In this case, a single backup set can contain multiple backup pieces, each containing a [file section](glossary.md). The purpose of multisection backups is to enable multiple channels to back up a large file in parallel.

See Also:

- ["Configuring the Maximum Size of Backup Pieces"](rcmconfa.md)
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta004.htm#RCMRF102) for `ALLOCATE` `CHANNEL` syntax
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) for `CONFIGURE` syntax

### Number and Size of Backup Sets

You use the [`backupSpec`](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=RCMRF204) clause of the `BACKUP` command to specify the objects to be backed up. Each `backupSpec` clause produces at least one backup set.

The total number and size of backup sets depends mostly on an internal RMAN algorithm. However, you can influence RMAN behavior with the `MAXSETSIZE` parameter in the `CONFIGURE` or `BACKUP` command. By limiting the size of the backup set, the parameter indirectly limits the number of files in the set and can possibly force RMAN to create additional backup sets. Also, you can specify `BACKUP ... FILESPERSET` to specify the maximum number of files in each backup set.

See Also:

- ["About Backup Set Size"](rcmbckad.md)
- [Chapter 22, "Tuning RMAN Performance"](rcmtunin.md) to learn about RMAN buffer management
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) to learn the syntax for the `backupSpec` clause

### Multiplexed Backup Sets

When creating backup sets, RMAN can simultaneously read multiple files from disk and then write their blocks into the same backup set. For example, RMAN can read from two datafiles simultaneously, and then combine the blocks from these datafiles into a single backup piece. The combination of blocks from multiple files is called backup [multiplexing](glossary.md). Image copies, by contrast, are never multiplexed.

Note:

If RMAN creates a [multisection backup](glossary.md) of a data file, then the data file is not multiplexed with any other data file or [file section](glossary.md).

As Figure 8-1 illustrates, RMAN can back up three datafiles into a backup set that contains only one backup piece. This backup piece contains the intermingled data blocks of the three input datafiles.

Figure 8-1 Data File Multiplexing

![Figure 8-1 Data File Multiplexing](img/bradv022.gif)

> This illustration depicts data file multiplexing. Three separate datafiles are read by a server session and written in intermingled fashion into a single backup piece as RMAN backs them up.
>
> [Copyright © 2003, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

RMAN multiplexing is determined by several factors. For example, the `FILESPERSET` parameter of the `BACKUP` command determines how many datafiles to put in each backup set. The `MAXOPENFILES` parameter of `ALLOCATE CHANNEL` or `CONFIGURE CHANNEL` defines how many datafiles RMAN can read from simultaneously. The basic multiplexing algorithm is as follows:

- Number of files in each backup set
	This number is the minimum of the `FILESPERSET` setting and the number of files read by each channel. The `FILESPERSET` default is 64.
- The [level of multiplexing](glossary.md)
	This is the number of input files simultaneously read and then written into the same backup piece. The level of multiplexing is the minimum of `MAXOPENFILES` and the number of files in each backup set. The `MAXOPENFILES` default is 8.

Suppose that you back up 12 datafiles with one channel when `FILEPERSET` is set to 4. The level of multiplexing is the lesser of this number and 8. Thus, the channel simultaneously writes blocks from 4 datafiles into each backup piece.

Now suppose that you back up 50 datafiles with one channel. The number of files in each backup set is 50. The level of multiplexing is the lesser of this number and 8. Thus, the channel simultaneously writes blocks from 8 datafiles into each backup piece.

RMAN multiplexing of backup sets is different from [media manager multiplexing](glossary.md). One type of media manager multiplexing occurs when the media manager writes the concurrent output from multiple RMAN channels to a single sequential device. Another type occurs when a backup mixes database files and non-database files on the same tape.

Caution:

Oracle recommends that you never use media manager multiplexing for RMAN backups.

See Also:

- ["Allocation of Input Disk Buffers"](rcmtunin.md) to learn how multiplexing affects allocation of disk buffers during backups
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) for `BACKUP` syntax

### Proxy Copies

During a [proxy copy](glossary.md), RMAN turns over control of the data transfer to a media manager that supports this feature. Proxy copy can only be used with media managers that support it and cannot be used with channels of type `DISK`. The `PROXY` option of the `BACKUP` command specifies that a backup should be a proxy copy.

For each file that you attempt to back up with the `BACKUP` `PROXY` command, RMAN queries the media manager to determine whether it can perform a proxy copy. If the media manager cannot proxy copy the file, then RMAN backs up the file as if the `PROXY` option had not been used. (Use the `PROXY` `ONLY` option to force RMAN to fail if a proxy copy cannot be performed.)

Control files are never backed up with proxy copy. If the `PROXY` option is specified on an operation backing up a control file, then it is silently ignored for the purposes of backing up the control file.

## Image Copies

An [image copy](glossary.md) is an exact copy of a single data file, archived redo log file, or control file. Image copies are not stored in an RMAN-specific format. They are identical to the results of copying a file with operating system commands. RMAN can use image copies during RMAN restore and recover operations, and you can also use image copies with non-RMAN restore and recovery techniques.

### RMAN-Created Image Copies

To create image copies and have them recorded in the RMAN repository, you run the RMAN `BACKUP` `AS` `COPY` command. Alternatively, you can configure the default backup type for disk as image copies. A database server session is used to create the copy. The server session also performs actions such as validating the blocks in the file and recording the image copy in the RMAN repository.

As with backup pieces, [`FORMAT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl010.htm#RCMRF195) variables are used to specify the names of image copies. The default format `%U`, which was explained in "Filenames for Backup Pieces", is defined differently for image copies. The following example shows the name for data file `2` generated by `%U`:

```
/d1/oracle/work/orcva/RDBMS/datafile/o1_mf_sysaux_2qylngm3_.dbf
```

When creating image copies, you can also name the output copies with the `DB_FILE_NAME_CONVERT` parameter of the `BACKUP` command. This parameter works identically to the [`DB_FILE_NAME_CONVERT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams057.htm#REFRN10038) initialization parameter. Pairs of file name prefixes are provided to change the names of the output files. If a file is not converted by any of the pairs, then RMAN uses the `FORMAT` specification: if no `FORMAT` is specified, then RMAN uses the default format `%U`.

Example 8-1 copies the datafiles whose file name is prefixed with `/maindisk/oradata/users` so that they are prefixed with `/backups/users_ts`.

Example 8-1 Specifying Filenames with DB\_FILE\_NAME\_CONVERT

```
BACKUP AS COPY 
  DB_FILE_NAME_CONVERT ('/maindisk/oradata/users',
                        '/backups/users_ts')
  TABLESPACE users;
```

If you run a `RESTORE` command, then by default RMAN restores a data file or control file to its original location by copying an image copy backup to that location. Image copies are chosen over backup sets because of the extra overhead of reading through an entire backup set in search of files to be restored.

If you must restore and recover a current data file, and if you have an image copy available on disk, then you do not need to have RMAN copy the image copy back to its old location. Instead, you can use the image copy in place as a replacement for the data file to be restored. ["Performing Complete Recovery After Switching to a Copy"](rcmcomre.md) explains how to perform this task.

See Also:

- ["Configuring the Default Type for Backups: Backup Sets or Copies"](rcmconfb.md) to learn how to make either backup sets or image copies the default type of RMAN backups
- ["Specifying Backup Set or Copy for an RMAN Backup to Disk"](rcmbckba.md)
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl010.htm#RCMRF195) to learn about the meaning of `%U` for image copies

### User-Managed Image Copies

RMAN can use image copies created by mechanisms outside of RMAN, such as native operating system file copy commands or third-party utilities that leave image copies of files on disk. This type of copy is known as a [user-managed backup](glossary.md) or [operating system backup](glossary.md).

You can use the [`CATALOG`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta008.htm#RCMRF109) command to inspect an existing image copy and enter its metadata into the RMAN repository. However, the `CATALOG` command does not do the following:

- Read all blocks in the data file copy to ensure there are no corruptions
- Guarantee that the image copy was correctly made in [backup mode](glossary.md)

After you catalog these files, you can use them with the [`RESTORE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2008.htm#RCMRF149) or [`SWITCH`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2020.htm#RCMRF159) commands just as you can for RMAN-generated image copies.

Some sites store their datafiles on mirrored disk volumes, which permit the creation of image copies by [breaking a mirror](glossary.md). After you have broken the mirror, you can notify RMAN of the existence of a new user-managed copy, thus making it eligible for a backup. You must notify RMAN when the copy is no longer available by using the [`CHANGE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta009.htm#RCMRF110) `...` `UNCATALOG` command.

See Also:

- [Chapter 28, "Making User-Managed Database Backups"](osbackup.md)
- ["Adding Backup Records to the RMAN Repository"](rcmmaint.md) to learn how to catalog data file and archived log image copies
- ["Making Split Mirror Backups with RMAN"](rcmbckad.md)
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta009.htm#RCMRF110) for `CHANGE` syntax

## Multiple Copies of RMAN Backups

In RMAN, you can make multiple, identical copies of backups in the following ways:

- Duplex backups with the `BACKUP` `... COPIES` command, in which case RMAN creates multiple copies of each backup set
- Back up your files as backup sets or image copies, and then back up the backup sets or image copies with the RMAN `BACKUP` `BACKUPSET` or `BACKUP` `COPY OF` commands

### Duplexed Backup Sets

When backing up datafiles, archived redo log files, server parameter files, and control files into backup pieces, RMAN can create a [duplexed backup set](glossary.md), producing up to four identical copies of each backup piece in the backup set on different backup destinations with one `BACKUP` command. Duplexing is not supported for backup operations that produce image copies.

You can use the `COPIES` parameter in the `CONFIGURE`, `SET`, or `BACKUP` commands to specify duplexing of backup sets when using the `BACKUP` command. RMAN can duplex backups to either disk or tape, but cannot duplex backups to tape and disk simultaneously. When backing up to tape, ensure that the number of copies does not exceed the number of available tape devices.

The `FORMAT` parameter of the `BACKUP` command specifies the destinations for duplexed backups. The following example creates three copies of the backup of data file `7`:

```
BACKUP DEVICE TYPE DISK COPIES 3 DATAFILE 7 
  FORMAT '/disk1/%U','?/oradata/%U','?/%U';
```

RMAN places the first copy of each backup piece in `/disk1`, the second in `?/oradata`, and the third in the Oracle home. RMAN does not produce three backup sets, each with a different unique backup set key. Rather, RMAN produces one backup set with a unique key, and generates three identical copies of each backup piece in the set.

### Backups of Backups

You can use the `BACKUP` command to back up existing backup sets and image copies.

#### Backups of Backup Sets

The RMAN `BACKUP` `BACKUPSET` command backs up backup sets that were created on disk. The command is a useful way to spread backups among multiple media.

If RMAN discovers that one copy of a backup set is corrupted or missing, then it searches for other copies of the same backup set. This behavior is similar to the behavior of RMAN when backing up archived redo logs that exist in multiple archiving destinations.

Example 8-2 shows how you might run the `BACKUP` command weekly as part of the production backup schedule. In this way, you ensure that all your backups exist on both disk and tape.

Example 8-2 Backing Up Backup Sets to Tape

```
BACKUP DEVICE TYPE DISK AS BACKUPSET 
  DATABASE PLUS ARCHIVELOG; 
BACKUP 
  DEVICE TYPE sbt 
  BACKUPSET ALL; # copies backup sets on disk to tape
```

Note:

Backups to `sbt` that use automatic channels require that you first run the `CONFIGURE` `DEVICE` `TYPE` `sbt` command.

You can also use `BACKUP` `BACKUPSET` to manage backup space allocation. Example 8-3 backs up backup sets that were created more than a week ago from disk to tape, and then deletes them from disk.

Example 8-3 Managing Space Allocation

```
BACKUP 
  DEVICE TYPE sbt 
  BACKUPSET COMPLETED BEFORE 'SYSDATE-7' 
  DELETE INPUT;
```

`DELETE` `INPUT` here is equivalent to `DELETE` `ALL` `INPUT`: RMAN deletes all existing copies of the backup set. If you duplexed a backup to four locations, then RMAN deletes all four copies of the pieces in the backup set.

See Also:

["Backing Up RMAN Backups"](rcmbckba.md)

#### Backups of Image Copies

You can use the `BACKUP COPY OF` command to back up existing image copies of database files either as backup sets or as image copies. When using this command, an image copy of every data file specified in the command must exist. If there are multiple copies of a data file, then the latest one is used. If you specify a tablespace or the whole database, then RMAN issues an error if there are datafiles in the database or tablespace for which there are no image copy backups.

## Control File and Server Parameter File Autobackups

Having recent backups of your control file and server parameter file is extremely valuable in many recovery situations. To ensure that you have backups of these files, the database supports control file and server parameter file autobackups. The autobackup occurs independently of any backup of the current control file explicitly requested as part of your `BACKUP` command.

With a [control file autobackup](glossary.md), RMAN can recover the database even if the current control file, recovery catalog, and server parameter file are inaccessible. Because the path used to store the autobackup follows a well-known format, RMAN can search for and restore the server parameter file from that autobackup. After you have started the instance with the restored server parameter file, RMAN can restore the control file from the autobackup. After you mount the control file, use the RMAN repository in the mounted control file to restore the datafiles.

### When RMAN Performs Control File Autobackups

If `CONFIGURE CONTROLFILE AUTOBACKUP` is `ON`, then RMAN automatically backs up the control file and the current server parameter file (if used to start up the database) at the end of a successful `BACKUP` command. If the database runs in `ARCHIVELOG` level, RMAN makes control file autobackups when a structural change to the database affects the contents of the control file.

Note:

Beginning with Oracle Database Release 11g Release 2, RMAN takes only one control file autobackup when multiple structural changes contained in a script (for example, adding tablespaces, altering the state of a tablespace or data file, adding a new online redo log, renaming a file, and so on) have been applied.

### How RMAN Performs Control File Autobackups

The first channel allocated during the backup job creates the autobackup and places it into its own backup set. For autobackups after database structural changes, the server process associated with the structural change makes the backup.

If a server parameter file is in use by the database, then RMAN backs it up in the same backup set as the control file autobackup. After the autobackup completes, the database writes a message containing the complete path of the backup piece and the device type to the alert log located in the [Automatic Diagnostic Repository (ADR)](glossary.md).

Note:

Control file autobackups are never duplexed.

The control file autobackup file name has a default format of `%F` for all device types, so that RMAN can determine the file location and restore it without a repository. You can specify a different format with the `CONFIGURE` `CONTROLFILE` `AUTOBACKUP` `FORMAT` command, but all autobackup formats must include the `%F` variable. If you do not use the default format, then during disaster recovery you must specify the format that was used to generate the autobackups. Otherwise, RMAN cannot restore the autobackup.

See Also:

- ["Configuring Control File and Server Parameter File Autobackups"](rcmconfb.md)
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) for `CONFIGURE` syntax
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) for `BACKUP` syntax
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl010.htm#RCMRF195) to learn about the substitution variable `%F`

## Incremental Backups

By default, RMAN makes full backups. A [full backup](glossary.md) of a data file includes every allocated block in the file being backed up. A full backup of a data file can be an image copy, in which case every data block is backed up. It can also be stored in a backup set, in which case data file blocks not in use may be skipped.

A full backup is the default type of RMAN backup. A full backup has no effect on subsequent incremental backups and is not considered a part of an [incremental backup](glossary.md) strategy. Image copies are always full backups because they include every data block in a data file. A backup set is by default a full backup because it can potentially include every data block in a data file, although [unused block compression](glossary.md) means that blocks never used are excluded and, in some cases, currently unused blocks are excluded (see "Block Compression for Backup Sets").

In contrast to a full backup, an incremental backup copies only those data blocks that have changed since a previous backup. You can use RMAN to create incremental backups of datafiles, tablespaces, or the whole database. A full backup cannot be part of an incremental backup strategy; that is, it cannot be the parent for a subsequent incremental backup.

### Multilevel Incremental Backups

RMAN can create multilevel incremental backups. Each incremental level is denoted by a value of 0 or 1. A [level 0 incremental backup](glossary.md), which is the base for subsequent incremental backups, copies all blocks containing data. You can create a level 0 database backup as backup sets or image copies.

The only difference between a level 0 incremental backup and a full backup is that a full backup is never included in an incremental strategy. Thus, an incremental level 0 backup is a full backup that happens to be the parent of incremental backups whose level is greater than 0.

A level 1 incremental backup can be either of the following types:

- A [differential incremental backup](glossary.md), which backs up all blocks changed after the most recent incremental backup at level 1 or 0
- A [cumulative incremental backup](glossary.md), which backs up all blocks changed after the most recent incremental backup at level 0

Incremental backups are differential by default.

Note:

Cumulative backups are preferable to differential backups when recovery time is more important than disk space, because fewer incremental backups must be applied during recovery.

The size of the backup file depends solely upon the number of blocks modified, the incremental backup level, and the type of incremental backup (differential or cumulative).

#### Differential Incremental Backups

In a differential level 1 backup, RMAN backs up all blocks that have changed since the most recent incremental backup at level 1 (cumulative or differential) or level 0. For example, in a differential level 1 backup, RMAN determines which level 1 backup occurred most recently and backs up all blocks modified after that backup. If no level 1 is available, then RMAN copies all blocks changed since the base level 0 backup.

If no level 0 backup is available in either the current or parent [incarnation](glossary.md), then the behavior varies with the compatibility mode setting. If compatibility is >=10.0.0, RMAN copies all blocks that have been changed since the file was created. Otherwise, RMAN generates a level 0 backup.

Figure 8-2 Differential Incremental Backups

![Figure 8-2 Differential Incremental Backups](img/bradv017.gif)

> This illustration depicts differential incremental backups. In this example, RMAN is shown backing up blocks of data over the course of two weeks. Sunday is shown as having a backup level of 0; Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday are shown as having backup levels of 1. The second week is a repeat of the first. The backups are described in the following text.
  

In the example shown in Figure 8-2, the following activity occurs each week:

- Sunday
	An incremental level 0 backup backs up all blocks that have ever been in use in this database.
- Monday through Saturday
	On each day from Monday through Saturday, a differential incremental level 1 backup backs up all blocks that have changed since the most recent incremental backup at level 1 or 0. The Monday backup copies blocks changed since Sunday level 0 backup, the Tuesday backup copies blocks changed since the Monday level 1 backup, and so forth.

#### Cumulative Incremental Backups

In a cumulative level 1 backup, RMAN backs up all blocks used since the most recent level 0 incremental backup in either the current or parent incarnation. Cumulative incremental backups reduce the work needed for a restore operation by ensuring that you only need one incremental backup from any particular level. Cumulative backups require more space and time than differential backups because they duplicate the work done by previous backups at the same level.

In the example shown in Figure 8-3, the following occurs each week:

- Sunday
	An incremental level 0 backup backs up all blocks that have ever been in use in this database.
- Monday - Saturday
	A cumulative incremental level 1 backup copies all blocks changed since the most recent level 0 backup. Because the most recent level 0 backup was created on Sunday, the level 1 backup on each day Monday through Saturday backs up all blocks changed since the Sunday backup.

See Also:

["Making and Updating Incremental Backups"](rcmbckba.md)

Figure 8-3 Cumulative Incremental Backups

![Figure 8-3 Cumulative Incremental Backups](img/bradv018.gif)

> This illustration depicts cumulative incremental backups. In this example, RMAN is shown backing up blocks of data over the course of two weeks. Sunday is shown as having a backup level of 0; Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday are shown as having backup levels of 1. The second week is a repeat of the first. The backups are described in the following text.
  

### Block Change Tracking

The [block change tracking](glossary.md) feature for incremental backups improves incremental backup performance by recording changed blocks in each data file in a [block change tracking file](glossary.md). This file is a small binary file stored in the [database area](glossary.md). RMAN tracks changed blocks as redo is generated.

If block change tracking is enabled, then RMAN uses the change tracking file to identify changed blocks for incremental backups, thus avoiding the need to scan every block in the data file. RMAN only uses block change tracking when the incremental level is greater than 0, because a [level 0 incremental backup](glossary.md) includes all blocks.

See Also:

["Using Block Change Tracking to Improve Incremental Backup Performance"](rcmbckba.md)

### Incremental Backup Algorithm

The following concepts are essential for understanding the algorithm that RMAN uses to make incremental backups:

- Checkpoint SCN
	Every data file has a [data file checkpoint](glossary.md) SCN, which you can view in `V$DATAFILE.CHECKPOINT_CHANGE#`. All changes with an SCN lower than this SCN are guaranteed to be in the file. When a level 0 incremental backup is restored, the restored data file contains the checkpoint SCN that it had when the level 0 was created. When a level 1 incremental backup is applied to a file, the checkpoint SCN of the file is advanced to the checkpoint SCN that the file had when the incremental level 1 backup was created.
- Incremental start SCN
	This SCN applies only to level 1 incremental backups. All blocks whose SCN is greater than or equal to the incremental start SCN are included in the backup. Blocks whose SCN is lower than the incremental start SCN are not included in the backup. The incremental start SCN is most often the checkpoint SCN of the parent of the level 1 backup.
- Block SCN
	Every data block in a data file records the SCN at which the most recent change was made to the block.

When RMAN makes a level 1 incremental backup of a file, RMAN reads the file, examines the SCN of every block, and backs up blocks whose SCN is greater than or equal to the incremental start SCN for this backup. If the backup is differential, then the incremental start SCN is the checkpoint SCN of the most recent level 1 backup. If the backup is cumulative, then the incremental start SCN is the checkpoint SCN of the most recent level 0 backup.

When block change tracking is enabled, RMAN uses bitmaps to avoid reading blocks that have not changed during the range from incremental start SCN to checkpoint SCN. RMAN still examines every block that is read and uses the SCN in the block to decide which blocks to include in the backup.

One consequence of the incremental backup algorithm is that RMAN applies all blocks containing changed data during recovery, even if the change is to an object created with the `NOLOGGING` option. Thus, if you restore a backup made before `NOLOGGING` changes were made, then incremental backups are the only way to recover these changes.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for more information about `NOLOGGING` mode

### Recovery with Incremental Backups

During [media recovery](glossary.md), RMAN examines the restored files to determine whether it can recover them with an incremental backup. If it has a choice, then RMAN always chooses incremental backups over archived redo logs because applying changes at a block level is faster than applying redo.

RMAN does not need to restore a base incremental backup of a data file to apply incremental backups to the data file during recovery. For example, you can restore data file image copies and recover them with incremental backups.

See Also:

["Selection of Incremental Backups and Archived Redo Logs"](rcmrvcon.md)

## Backup Retention Policies

You can use the [`CONFIGURE RETENTION POLICY`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) command to create a persistent and automatic [backup retention policy](glossary.md). When a backup retention policy is in effect, RMAN considers a backup of datafiles or control files as an [obsolete backup](glossary.md), that is, no longer needed for recovery, according to criteria specified in the `CONFIGURE` command. You can use the [`REPORT OBSOLETE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2006.htm#RCMRF147) command to view obsolete files and the [`DELETE OBSOLETE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta016.htm#RCMRF121) command to delete them.

As you produce backups over time, older backups become obsolete as they are no longer needed to satisfy the retention policy. RMAN can identify the obsolete files for you, but it does not automatically delete them. You must use the `DELETE` `OBSOLETE` command to delete files that are no longer needed to satisfy the retention policy.

If a fast recovery area is configured, then the database automatically deletes files that are either obsolete or backed up to tape when more recovery area space is needed for new files. The disk quota rules are distinct from the retention policy rules, but the database never deletes files in violation of the retention policy to satisfy the disk quota. Refer to ["Responding to a Full Fast Recovery Area"](rcmmaint.md).

A backup is obsolete when `REPORT` `OBSOLETE` or `DELETE` `OBSOLETE` determines, based on the user-defined retention policy, that it is not needed for recovery. A backup is considered an [expired backup](glossary.md) only when RMAN performs a crosscheck and cannot find the file. In short, obsolete means a file is not needed, whereas expired means it is not found.

A backup retention policy applies only to full or level 0 data file and control file backups. For data file copies and proxy copies, if RMAN determines that the copy or proxy copy is not needed, then the copy or proxy copy can be deleted. For data file backup sets, RMAN cannot delete the backup set until all data file backups within the backup set are obsolete.

The retention policy is not responsible for deleting or rendering obsolete archived redo logs and incremental level 1 backups. Rather, these files become obsolete when no full backups exist that need them. Besides affecting full or level 0 data file and control file backups, the retention policy affects archived redo logs and level 1 incremental backups. First, RMAN decides which data file and control file backups are obsolete. Then, RMAN considers as obsolete all archived logs and incremental level 1 backups that are not needed to recover the oldest data file or control file backup that must be retained.

Note:

RMAN cannot implement an automatic retention policy if backups are deleted by non-RMAN techniques, for example, through the media manager's tape retention policy. The media manager should never expire a tape until all RMAN backups on that tape have been removed from the media manager's catalog.

There are two mutually exclusive options for implementing a retention policy: [redundancy](glossary.md) and [recovery window](glossary.md).

### Recovery Window

A recovery window is a period of time that begins with the current time and extends backward in time to the point of recoverability. The point of recoverability is the earliest time for a hypothetical point-in-time recovery, that is, the earliest point to which you can recover following a media failure. For example, if you implement a recovery window of 1 week, then RMAN retains full backups and required incremental backups and archived logs so that the database can be recovered up to 7 days in the past. You implement this retention policy as follows:

```
CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 7 DAYS;
```

This command ensures that for each data file, one backup that is older than the point of recoverability is retained. For example, if the recovery window is `7`, then there must always exist one backup of each data file that satisfies the following condition:

```
SYSDATE - BACKUP CHECKPOINT TIME >= 7
```

All backups older than the most recent backup that satisfied this condition are obsolete.

Assume the retention policy illustrated in Figure 8-4. The retention policy has the following aspects:

- The recovery window is 7 days.
- Database backups are scheduled every two weeks on these days:
	- January 1
		- January 15
		- January 29
		- February 12
- The database runs in `ARCHIVELOG` mode, and archived logs are saved on disk only as long as needed for the retention policy.

Figure 8-4 Recovery Window, Part 1

![Figure 8-4 Recovery Window, Part 1](img/bradv004.gif)

> This illustration depicts part one of a recovery window. There is a timeline beginning at January 1 and proceeding through January 28. Beginning on January 1, a backup is scheduled for every two weeks. Archived logs are saved every seven days, and are numbered Log 100 for January 1, Log 250 on day 7, Log 500 on day 14, Log 750 on day 21, and Log 850 on day 23. A recovery window is shown extending back seven days from day 23 to day 16. The recovery is explained in the following text.
  

As illustrated in Figure 8-4, the current time is January 23 and the point of recoverability is January 16. Hence, the January 14 backup is needed for recovery, and so are the archived logs from log sequence 500 through 850. The logs before 500 and the January 1 backup are obsolete because they are not needed for recovery to a point within the window.

Assume the same scenario a week later, as depicted in Figure 8-5.

Figure 8-5 Recovery Window, Part 2

![Figure 8-5 Recovery Window, Part 2](img/bradv002.gif)

> This illustration depicts part two of a recovery window. There is a timeline beginning at January 1 and proceeding through February 4. Beginning on January 1, a backup is scheduled for every two weeks. Archived logs are saved every seven days, and are numbered Log 100 for January 1, Log 250 on day 7, Log 500 on day 14, Log 750 on day 21, Log 1000 on day 28, and Log 1150 on day 30. A recovery window is shown extending back seven days from day 30 to day 23. The recovery is explained in the following text.
  

In this scenario, the current time is January 30 and the point of recoverability is January 23. Note how the January 14 backup is not obsolete even though a more recent backup (January 28) exists in the recovery window. This situation occurs because restoring the January 28 backup does not enable you to recover to the earliest time in the window, January 23. To ensure recoverability to any point in the window, you must save the January 14 backup and all archived logs from sequence 500 to 1150.

See Also:

["Configuring a Recovery Window-Based Retention Policy"](rcmconfb.md)

### Backup Redundancy

In some cases using a recovery window can complicate disk space planning because the number of backups that must be retained is not constant and depends on the backup schedule. In contrast, a redundancy-based retention policy specifies how many backups of each data file must be retained. For example, you can configure a redundancy of 2 as follows:

```
CONFIGURE RETENTION POLICY TO REDUNDANCY 2;
```

The default retention policy is configured to `REDUNDANCY` `1`.

See Also:

["Configuring a Redundancy-Based Retention Policy"](rcmconfb.md)

### Batch Deletes of Obsolete Backups

You can run the `REPORT` `OBSOLETE` command to determine which backups are currently obsolete according to the retention policy. A companion command, `DELETE` `OBSOLETE`, deletes all files that are obsolete according to the retention policy. You can run `DELETE` `OBSOLETE` periodically to minimize space wasted by storing obsolete backups. For example, you can run `DELETE` `OBSOLETE` in a weekly script.

You can also override the configured retention policy by specifying the `REDUNDANCY` or `RECOVERY` `WINDOW` options on the `REPORT` or `DELETE` commands. Using `DELETE OBSOLETE` with a recovery window shorter than the configured recovery window effectively reduces the window of recoverability. For example, if the configured window is 14 days, but you execute `DELETE OBSOLETE RECOVERY WINDOW OF 7 DAYS`, then you no longer have the ability to recover to a time between 7 and 14 days ago.

See Also:

- [Chapter 11, "Reporting on RMAN Operations"](rcmreprt.md) to learn how to generate reports and delete backups
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta016.htm#RCMRF121) for `DELETE` syntax
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2006.htm#RCMRF147) for `REPORT` syntax

### Backup Retention Policy and Fast Recovery Area Deletion Rules

The RMAN status `OBSOLETE` is always determined in reference to a retention policy. For example, if a database backup is considered `OBSOLETE` in the RMAN repository, it is because it is either not needed for recovery to a point within the recovery window, or it is redundant.

If you configure a [fast recovery area](glossary.md), then the database uses an internal algorithm to select files in the fast recovery area that are no longer needed to meet the configured retention policy. These backups have status `OBSOLETE` and are eligible for deletion to satisfy the [disk quota](glossary.md) rules. The retention policy is never violated when determining which files to delete from the fast recovery area to satisfy the disk quota rules.

There is one important difference between the fast recovery area rules for `OBSOLETE` status and the disk quota rules for deletion eligibility. Assume that archived logs 1000 through 2000, which are on disk, are needed for the current recovery window and so are not obsolete. If you back up these logs to tape, then the retention policy considers the disk logs as required, that is, not obsolete. Nevertheless, the fast recovery area disk quota algorithm considers the logs on disk as eligible for deletion because they have been backed up to tape. The logs on disk do not have `OBSOLETE` status in the repository, but they are eligible for deletion by the fast recovery area.