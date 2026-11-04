---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_DATABASE_BLOCK_CORRUPTION.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view gives information about database blocks that were corrupted after the last backup. It corresponds to the `V$DATABASE_BLOCK_CORRUPTION` view, which is populated in real time with corruption information.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the current incarnation. Use this column to join with `RC_DATABASE_INCARNATION`. |
| `FILE#` | `NUMBER` | The absolute file number of the data file. |
| `BLOCK#` | `NUMBER` | The block number of the first corrupted block in this range of corrupted blocks. |
| `BLOCKS` | `NUMBER` | The number of corrupted blocks found beginning with `BLOCK#`. |
| `CORRUPTION_CHANGE#` | `NUMBER` | For media corrupt blocks, this value is zero. For logically corrupt blocks, this value is the lowest SCN in the blocks in this corrupt range. |
| `CORRUPTION_TYPE` | `VARCHAR2(9)` | The type of block corruption in the data file. Possible values are:  - `ALL ZERO`. The block header on disk contained only zeros. The block may be valid if it was never filled and if it is in an Oracle7 file. The buffer is reformatted to the Oracle8 standard for an empty block. - `FRACTURED`. The block header looks reasonable, but the front and back of the block are different versions. - `CHECKSUM`. The optional check value shows that the block is not self-consistent. It is impossible to determine exactly why the check value fails, but it probably fails because sectors in the middle of the block are from different versions. - `CORRUPT`. The block is wrongly identified or is not a data block (for example, the data block address is missing) - `LOGICAL`. Specifies the range for logically corrupt blocks. - `NOLOGGING. `The block does not have redo log entries (for example, `NOLOGGING` operations on primary database can introduce this type of corruption on a physical standby) |