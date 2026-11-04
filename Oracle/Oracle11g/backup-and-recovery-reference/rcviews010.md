---
title: RC_BACKUP_CORRUPTION
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews010.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

This view lists corrupt block ranges in data file backups, which may be detected when `BACKUP VALIDATE` is used or the `MAXCORRUPT` parameter is greater than 0. It corresponds to the `V$BACKUP_CORRUPTION` view in the control file. Corruptions are not tolerated in control file and archived redo log backups.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for this database in the recovery catalog. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the incarnation of the target database. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `RECID` | `NUMBER` | The record identifier from `V$BACKUP_CORRUPTION`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `STAMP` | `NUMBER` | The stamp propagated from `V$BACKUP_CORRUPTION`. `RECID` and `STAMP` form a concatenated primary key that uniquely identifies this record in the target database control file. |
| `BS_KEY` | `NUMBER` | The primary key of the backup set to which this record belongs in the recovery catalog. Use this column to join with `RC_BACKUP_SET` or `RC_BACKUP_PIECE`. |
| `SET_STAMP` | `NUMBER` | The `SET_STAMP` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `SET_COUNT` | `NUMBER` | The `SET_COUNT` value from `V$BACKUP_SET`. `SET_STAMP` and `SET_COUNT` form a concatenated key that uniquely identifies the backup set to which this record belongs in the target database control file. |
| `PIECE#` | `NUMBER` | The backup piece that contains this corrupt block. |
| `BDF_KEY` | `NUMBER` | The primary key for the data file backup or copy in the recovery catalog. Use this key to join with `RC_BACKUP_DATAFILE`. If you issue the `LIST` command while RMAN is connected to the recovery catalog, then this value appears in the `KEY` column of the output. |
| `BDF_RECID` | `NUMBER` | The `RECID` value from `V$BACKUP_DATAFILE`. |
| `BDF_STAMP` | `NUMBER` | The `STAMP` value from `V$BACKUP_DATAFILE`. |
| `FILE#` | `NUMBER` | The absolute file number for the data file that contains the corrupt blocks. |
| `CREATION_CHANGE#` | `NUMBER` | The creation SCN of the data file containing the corrupt blocks. |
| `BLOCK#` | `NUMBER` | The block number of the first corrupted block in this range of corrupted blocks. |
| `BLOCKS` | `NUMBER` | The number of corrupted blocks found beginning with `BLOCK#`. |
| `CORRUPTION_CHANGE#` | `NUMBER` | For media corrupt blocks, this value is zero. For logically corrupt blocks, this value is the lowest SCN in the blocks in this corrupt range. |
| `MARKED_CORRUPT` | `VARCHAR2(3)` | `YES` if this corruption was not previously detected by Oracle, or `NO` if Oracle has already discovered this corrupt block and marked it as corrupt in the database. If a corrupt block is encountered in a backup that was not marked corrupt by Oracle, then the backup process does not mark the block as corrupt in the production data file. Thus, this field may be `YES` for the same block in multiple backup sets. |
| `CORRUPTION_TYPE` | `VARCHAR2(9)` | Same as `RC_DATABASE_BLOCK_CORRUPTION.CORRUPTION_TYPE`. |