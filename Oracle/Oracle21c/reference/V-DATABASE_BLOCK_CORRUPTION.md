---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DATABASE_BLOCK_CORRUPTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.154 V$DATABASE\_BLOCK\_CORRUPTION

`V$DATABASE_BLOCK_CORRUPTION` displays information about database blocks that were corrupted after the last backup.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | Absolute file number of the data file that contains the corrupt blocks |
| `BLOCK#` | `NUMBER` | Block number of the first corrupt block in the range of corrupted blocks |
| `BLOCKS` | `NUMBER` | Number of corrupted blocks found starting with `BLOCK#` |
| `CORRUPTION_CHANGE#` | `NUMBER` | Change number at which the logical corruption was detected. Set to 0 to indicate media corruption. |
| `CORRUPTION_TYPE` | `VARCHAR2(9)` | Type of block corruption in the data file:  - `ALL ZERO` - Block header on disk contained only zeros. The block may be valid if it was never filled and if it is in an Oracle7 file. The buffer will be reformatted to the Oracle8 standard for an empty block. - `FRACTURED` - Block header looks reasonable, but the front and back of the block are different versions. - `CHECKSUM` - optional check value shows that the block is not self-consistent. It is impossible to determine exactly why the check value fails, but it probably fails because sectors in the middle of the block are from different versions. - `CORRUPT` - Block is wrongly identified or is not a data block (for example, the data block address is missing) - `LOGICAL` - Block is logically corrupt |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$NONLOGGED\_BLOCK](V-NONLOGGED_BLOCK.md) " for information about nonlogged blocks