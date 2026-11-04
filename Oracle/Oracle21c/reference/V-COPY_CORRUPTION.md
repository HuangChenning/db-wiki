---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-COPY_CORRUPTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.144 V$COPY\_CORRUPTION

`V$COPY_CORRUPTION` displays information about data file copy corruptions from the control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Copy corruption record ID |
| `STAMP` | `NUMBER` | Copy corruption record stamp |
| `COPY_RECID` | `NUMBER` | Data file copy record ID |
| `COPY_STAMP` | `NUMBER` | Data file copy record stamp |
| `FILE#` | `NUMBER` | Data file number |
| `BLOCK#` | `NUMBER` | First block of the corrupted range |
| `BLOCKS` | `NUMBER` | Number of contiguous blocks in the corrupted range |
| `CORRUPTION_CHANGE#` | `NUMBER` | Change number at which the logical corruption was detected. Set to `0` to indicate media corruption. |
| `MARKED_CORRUPT` | `VARCHAR2(3)` | (`YES` \| `NO`) If set to `YES` the blocks were not marked corrupted in the data file, but were detected and marked as corrupted while making the data file copy |
| `CORRUPTION_TYPE` | `VARCHAR2(9)` | Type of block corruption in the data file:  - `ALL ZERO` - Block header on disk contained only zeros. The block may be valid if it was never filled and if it is in an Oracle7 file. The buffer will be reformatted to the Oracle8 standard for an empty block. - `FRACTURED` - Block header looks reasonable, but the front and back of the block are different versions. - `CHECKSUM` - optional check value shows that the block is not self-consistent. It is impossible to determine exactly why the check value fails, but it probably fails because sectors in the middle of the block are from different versions. - `CORRUPT` - Block is wrongly identified or is not a data block (for example, the data block address is missing) - `LOGICAL` - Block is logically corrupt - `NOLOGGING` - Block does not have redo log entries (for example, `NOLOGGING` operations on primary database can introduce this type of corruption on a physical standby) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |