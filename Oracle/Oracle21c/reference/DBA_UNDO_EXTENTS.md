---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_UNDO_EXTENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.79 DBA\_UNDO\_EXTENTS

`DBA_UNDO_EXTENTS` describes the extents comprising the segments in all undo tablespaces in the database.

Note:

The status of the undo space distribution reported by `DBA_UNDO_EXTENTS` is correct for the undo tablespace that is active on the instance on which `DBA_UNDO_EXTENTS` is queried. However, due to the use of in-memory information that is different on each instance, there can be a discrepancy in the status of the undo space distribution of undo tablespaces active on other instances when queried from one instance. This does not affect undo functionality and is only a reporting discrepancy for other instances' undo tablespace space distribution status. As a best practice, query the space distribution for an undo tablespace from the instance on which it is active.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `CHAR(3)` |  | Owner of the undo tablespace |
| `SEGMENT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the undo segment |
| `TABLESPACE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the undo tablespace |
| `EXTENT_ID` | `NUMBER` |  | ID of the extent |
| `FILE_ID` | `NUMBER` | `NOT NULL` | Absolute file number of the data file containing the extent |
| `BLOCK_ID` | `NUMBER` |  | Start block number of the extent |
| `BYTES` | `NUMBER` |  | Size of the extent (in bytes) |
| `BLOCKS` | `NUMBER` |  | Size of the extent (in blocks) |
| `RELATIVE_FNO` | `NUMBER` |  | Relative number of the file containing the segment header |
| `COMMIT_JTIME` | `NUMBER` |  | Commit time of the undo in the extent expressed as Julian time. This column is deprecated, but retained for backward compatibility reasons. |
| `COMMIT_WTIME` | `VARCHAR2(20)` |  | Commit time of the undo in the extent expressed as Wallclock time.This column is deprecated, but retained for backward compatibility reasons. |
| `STATUS` | `VARCHAR2(9)` |  | Transaction Status of the undo in the extent:  - `ACTIVE` - `EXPIRED` - `UNEXPIRED` |