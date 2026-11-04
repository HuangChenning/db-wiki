---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/toDestSpec.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

Purpose

Use the `toDestSpec` subclause to specify a directory or an Automatic Storage Management disk group for disk backups. If you do not specify a value for the `TO DESTINATION`, then RMAN either creates the backup in the fast recovery area if it is enabled, or in a platform-specific directory (for example, `?/dbs` on UNIX) if a fast recovery area is not enabled. RMAN uses Oracle Managed Files file names when the `TO DESTINATION` parameter is used.

Usage Notes

This subclause can only be used with disk devices and cannot be used with the `FORMAT` option.

If backup optimization is enabled, RMAN only skips backups of files that have identical backups in the location designated by the `TO DESTINATION` field.

You can specify up to four `TO DESTINATION` strings. RMAN uses the second, third, and fourth values only when `BACKUP` `COPIES`, `SET` `BACKUP COPIES`, or `CONFIGURE` `... BACKUP COPIES` is in effect. When choosing the format for each backup piece, RMAN uses the first format value for copy 1, the second format value for copy 2, and so on. If the number of format values exceeds the number of copies, then the extra formats are not used. If the number of format values is less than the number of copies, then RMAN reuses the format values, starting with the first one.

Specify `todest_string` in any of the following places, listed in order of precedence:

1. The `backupSpec` clause
2. The `BACKUP` command
3. The `ALLOCATE CHANNEL` command
4. The `CONFIGURE` `CHANNEL` command

If it is specified in multiple places, then RMAN searches for the `TO DESTINATION` parameter in the order shown.

Syntax

toDestSpec::=

![todestspec](img/todestspec.gif)

> ' toDest\_string '
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Examples

Example 4-38 Specifying an ASM Disk Group

This example copies the database to ASM disk group `DISK1:`

```
BACKUP AS COPY DATABASE TO DESTINATION '+DISK1';
```

Example 4-39 Specifying a Destination for Data File Copies

This example copies two data files with tag `LATESTCOPY` to directory `/disk2`:

```
BACKUP AS COPY
 COPY OF DATAFILE 27, 28
 FROM TAG 'LATESTCOPY'  TO DESTINATION '/disk2';
```

Example 4-40 Specifying a Destination for Recovery Area files

This example copies all recovery area files to `/disk2:`

Because `Backup Recovery Area` has backup optimization enabled by default, RMAN only skips backups of files that previously exist on `/disk2` and not ones that reside in other locations.

Note: This subclause, when used with the `BACKUP RECOVERY AREA`, enables you to designate a disk channel as a location.

```
BACKUP RECOVERY AREA TO DESTINATION '/disk2';
```