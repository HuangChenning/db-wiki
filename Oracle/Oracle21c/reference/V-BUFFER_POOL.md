---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BUFFER_POOL.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.113 V$BUFFER\_POOL

`V$BUFFER_POOL` displays information about all buffer pools available for the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Buffer pool identifier number |
| `NAME` | `VARCHAR2(20)` | Name of the buffer pool:  - `DEFAULT` - `KEEP` - `RECYCLE` 	Note: Currently, `KEEP` and `RECYCLE` pools only exist for the standard block size. All nonstandard block size pools are `DEFAULT`. |
| `BLOCK_SIZE` | `NUMBER` | Block size (in bytes) for buffers in this pool. Possible values: the standard block size, the power of 2 nonstandard block sizes, `2048`, `4096`, `8192`, `16384`, `32768`. |
| `RESIZE_STATE` | `VARCHAR2(10)` | Current state of the resize operation:  `STATIC` - Not being resized  `ALLOCATING` - Memory is being allocated (can be canceled by the user)  `ACTIVATING` - New buffers are being created (user cannot cancel)  `SHRINKING` - Buffers are being deleted (can be canceled by the user) |
| `CURRENT_SIZE` | `NUMBER` | Present size of the sub-cache (in megabytes) |
| `BUFFERS` | `NUMBER` | Current instantaneous number of buffers |
| `TARGET_SIZE` | `NUMBER` | If a resize is in progress (state is not `STATIC`), records new target size (in megabytes). If the pool is `STATIC`, the value in this column is the same as the current size of the pool. |
| `TARGET_BUFFERS` | `NUMBER` | If a resize is in progress, records new target size in terms of buffers. Otherwise, the value in this column is the same as the current number of buffers. |
| `PREV_SIZE` | `NUMBER` | Previous buffer pool size. If the buffer pool has never been resized, the previous size is zero. |
| `PREV_BUFFERS` | `NUMBER` | Previous number of buffers in the buffer pool. Value is zero if the buffer pool has never been resized. |
| `LO_BNUM` | `NUMBER` | Obsolete column |
| `HI_BNUM` | `NUMBER` | Obsolete column |
| `LO_SETID` | `NUMBER` | Obsolete column |
| `HI_SETID` | `NUMBER` | Obsolete column |
| `SET_COUNT` | `NUMBER` | Obsolete column |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [DB\_BLOCK\_SIZE](DB_BLOCK_SIZE.md) "