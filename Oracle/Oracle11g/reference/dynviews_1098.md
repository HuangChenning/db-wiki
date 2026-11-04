---
title: "V$DATABASE_BLOCK_CORRUPTION"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1098.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DATABASE_BLOCK_CORRUPTION` displays information about database blocks that were corrupted after the last backup.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | Absolute file number of the datafile that contains the corrupt blocks |
| `BLOCK#` | `NUMBER` | Block number of the first corrupt block in the range of corrupted blocks |
| `BLOCKS` | `NUMBER` | Number of corrupted blocks found starting with `BLOCK#` |
| `CORRUPTION_CHANGE#` | `NUMBER` | Change number at which the logical corruption was detected. Set to 0 to indicate media corruption. |
| `CORRUPTION_TYPE` | `VARCHAR2(9)` | Type of block corruption in the datafile: - `ALL ZERO` - Block header on disk contained only zeros. The block may be valid if it was never filled and if it is in an Oracle7 file. The buffer will be reformatted to the Oracle8 standard for an empty block. - `FRACTURED` - Block header looks reasonable, but the front and back of the block are different versions. - `CHECKSUM` - optional check value shows that the block is not self-consistent. It is impossible to determine exactly why the check value fails, but it probably fails because sectors in the middle of the block are from different versions. - `CORRUPT` - Block is wrongly identified or is not a data block (for example, the data block address is missing) - `LOGICAL` - Block is logically corrupt - `NOLOGGING` - Block does not have redo log entries (for example, `NOLOGGING` operations on primary database can introduce this type of corruption on a physical standby) |