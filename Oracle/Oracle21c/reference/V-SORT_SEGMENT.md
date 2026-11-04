---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SORT_SEGMENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.44 V$SORT\_SEGMENT

`V$SORT_SEGMENT` displays information about every sort segment in a given instance. The view is only updated when the tablespace is of the `TEMPORARY` type.

| Column | Datatype | Description |
| --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | Name of the tablespace |
| `SEGMENT_FILE` | `NUMBER` | File number of the first extent |
| `SEGMENT_BLOCK` | `NUMBER` | Block number of the first extent |
| `EXTENT_SIZE` | `NUMBER` | Extent size |
| `CURRENT_USERS` | `NUMBER` | Number of active users of the segment |
| `TOTAL_EXTENTS` | `NUMBER` | Total number of extents in the segment |
| `TOTAL_BLOCKS` | `NUMBER` | Total number of blocks in the segment |
| `USED_EXTENTS` | `NUMBER` | Extents allocated to active sorts |
| `USED_BLOCKS` | `NUMBER` | Blocks allocated to active sorts |
| `FREE_EXTENTS` | `NUMBER` | Extents not allocated to any sort |
| `FREE_BLOCKS` | `NUMBER` | Blocks not allocated to any sort |
| `ADDED_EXTENTS` | `NUMBER` | Number of extent allocations |
| `EXTENT_HITS` | `NUMBER` | Number of times an unused extent was found in the pool |
| `FREED_EXTENTS` | `NUMBER` | Number of deallocated extents |
| `FREE_REQUESTS` | `NUMBER` | Number of requests to deallocate |
| `MAX_SIZE` | `NUMBER` | Maximum number of extents ever used |
| `MAX_BLOCKS` | `NUMBER` | Maximum number of blocks ever used |
| `MAX_USED_SIZE` | `NUMBER` | Maximum number of extents used by all sorts |
| `MAX_USED_BLOCKS` | `NUMBER` | Maximum number of blocks used by all sorts |
| `MAX_SORT_SIZE` | `NUMBER` | Maximum number of extents used by an individual sort |
| `MAX_SORT_BLOCKS` | `NUMBER` | Maximum number of blocks used by an individual sort |
| `RELATIVE_FNO` | `NUMBER` | Relative file number of the sort segment header |
| `TS#` | `NUMBER` | Tablespace number |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `IS_LOCAL_TEMP` | `NUMBER` | Indicates whether the sort segment is allocated from a local temporary tablespace (`1`) or not (`0`). |