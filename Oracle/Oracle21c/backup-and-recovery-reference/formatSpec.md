---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/formatSpec.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

Purpose

Use the `formatSpec` subclause to specify a file name format or an Automatic Storage Management disk group for a backup piece or image copy. If you do not specify a value for the `FORMAT` parameter, then RMAN either creates the backup in the fast recovery area if it is enabled, or in a platform-specific directory (for example, `?/dbs` on UNIX) if a fast recovery area is not enabled. In either case, RMAN uses the variable %U to name the backup.

Tip:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=SQLRF01114) to learn how to create and name Automated Storage Manager disk groups

Usage Notes

Any name that is valid as a sequential file name on the platform is allowed, so long as each backup piece or copy has a unique name. If backing up to disk, then any valid disk file name is allowed, provided it is unique.

You cannot specify an Oracle Managed Files file name as the format for a backup. For example, if `+DISK1/datafile/system.732.609791431` is an OMF file name, then you cannot specify this file name in the `FORMAT` parameter.

Environment variables are not valid in the `FORMAT` parameter.

The entire `format_string` is processed in a port-specific manner by the target instance to derive the final backup piece name. The substitution variables listed in " Semantics " are available in `FORMAT` strings to aid in generating unique file names. The formatting of this information varies by platform.

You can specify up to four `FORMAT` strings. RMAN uses the second, third, and fourth values only when `BACKUP` `COPIES`, `SET` `BACKUP COPIES`, or `CONFIGURE` `... BACKUP COPIES` is in effect. When choosing the format for each backup piece, RMAN uses the first format value for copy 1, the second format value for copy 2, and so on. If the number of format values exceeds the number of copies, then the extra formats are not used. If the number of format values is less than the number of copies, then RMAN reuses the format values, starting with the first one.

Specify `format_string` in any of the following places, listed in order of precedence:

1. The `backupSpec` clause
2. The `BACKUP` command
3. The `ALLOCATE CHANNEL` command
4. The `CONFIGURE` `CHANNEL` command

If it is specified in multiple places, then RMAN searches for the `FORMAT` parameter in the order shown.

Syntax

formatSpec::=

![formatspec](img/formatspec.gif)

> ' format\_string '
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

formatSpec

The following table lists RMAN substitution variables that are valid in format strings.

| Syntax Element | Description |
| --- | --- |
| `%a` | Specifies the activation ID of the database. |
| `%b` | Specifies the file name stripped of directory paths. It is only valid for `SET                     NEWNAME` and backup resetwhen producing image copies It yields errors if used as a format specification for a backup that produces backup pieces. |
| `%c` | Specifies the copy number of the backup piece within a set of duplexed backup pieces. If you did not duplex a backup, then this variable is 1 for backup sets and 0 for proxy copies. If a command is enabled, then the variable shows the copy number. The maximum value for `%c` is 256. |
| `%d` | Specifies the name of the database (see Example 4-23). |
| `%D` | Specifies the current day of the month from the Gregorian calendar in format `DD`. |
| `%e` | Specifies the archived log sequence number. |
| `%f` | Specifies the absolute file number (see Example 4-23). |
| `%F` | Combines the DBID, day, month, year, and sequence into a unique and repeatable generated name. This variable translates into `c-IIIIIIIIII-YYYYMMDD-QQ`, where:  - `IIIIIIIIII` stands for the DBID. The DBID is printed in decimal so that it can be easily associated with the target database. - `YYYYMMDD` is a time stamp in the Gregorian calendar of the day the backup is generated - `QQ` is the sequence in hexadecimal number that starts with 00 and has a maximum of 'FF' (256)  Note: `%F` is valid only in the `CONFIGURE` `CONTROLFILE` `AUTOBACKUP` `FORMAT` command. |
| `%h` | Specifies the archived redo log thread number. |
| `%I` | Specifies the DBID. |
| `%M` | Specifies the month in the Gregorian calendar in format `MM`. |
| `%N` | Specifies the tablespace name. This substitution variable is only valid when backing up data files as image copies. |
| `%n` | Specifies the name of the database, padded on the right with `x` characters to a total length of eight characters. For example, if `prod1` is the database name, then the padded name is `prod1xxx`. |
| `%p` | Specifies the piece number within the backup set. This value starts at `1` for each backup set and is incremented by 1 as each backup piece is created.  Note: If you specify `PROXY`, then the `%p` variable must be included in the `FORMAT` string either explicitly or implicitly within %U. |
| `%r` | Specifies the resetlogs ID. |
| `%s` | Specifies the backup set number. This number is a counter in the control file that is incremented for each backup set. The counter value starts at `1` and is unique for the lifetime of the control file. If you restore a backup control file, then duplicate values can result. Also, `CREATE CONTROLFILE` initializes the counter back to `1`. |
| `%t` | Specifies the backup set time stamp, which is a 4-byte value derived as the number of seconds elapsed since a fixed reference time. You can use a combination of `%s` and `%t` to form a unique name for the backup set. |
| `%T` | Specifies the year, month, and day in the Gregorian calendar in this format: `YYYYMMDD`. |
| `%u` | Specifies an 8-character name constituted by compressed representations of the backup set or image copy number and the time the backup set or image copy was created. |
| `%U` | Specifies a system-generated unique file name (default).  The meaning of `%U` is different for image copies and backup pieces. For a backup piece, `%U` specifies a convenient shorthand for `%u_%p_%c` that guarantees uniqueness in generated backup file names. For an image copy of a data file, `%U` means the following:  `data-D-%d_id-%I_TS-%N_FNO-%f_%u`  For an image copy of an archived redo log, `%U` means the following:  `arch-D_%d-id-%I_S-%e_T-%h_A-%a_%u`  For an image copy of a control file, `%U` means the following:  `cf-D_%d-id-%I_%u` |
| `%Y` | Specifies the year in this format: `YYYY`. |
| `%%` | Specifies the percent (`%`) character. For example, `%%Y` translates to the string `%Y`. |

Example

Example 4-22 Specifying an ASM Disk Group

This example copies the database to ASM disk group `DISK1`:

```
BACKUP AS COPY DATABASE FORMAT '+DISK1';
```

Example 4-23 Specifying a Format for Data File Copies

This example copies two data files with tag `LATESTCOPY` to directory `/disk2`:

```
BACKUP AS COPY
  COPY OF DATAFILE 27, 28
  FROM TAG 'LATESTCOPY' 
  FORMAT '/disk2/Datafile%f_Database%d';
```