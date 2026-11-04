---
title: "V$BUFFER_POOL"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1072.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BUFFER_POOL` displays information about all buffer pools available for the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Buffer pool identifier number |
| `NAME` | `VARCHAR2(20)` | Name of the buffer pool: - `DEFAULT` - `KEEP` - `RECYCLE` 	Note: Currently, `KEEP` and `RECYCLE` pools only exist for the standard block size. All non-standard block size pools are `DEFAULT`. |
| `BLOCK_SIZE` | `NUMBER` | Block size (in bytes) for buffers in this pool. Possible values: the standard block size, the power of 2 non-standard block sizes, `2048`, `4096`, `8192`, `16384`, `32768`. |
| `RESIZE_STATE` | `VARCHAR2(10)` | Current state of the resize operation:  `STATIC` - Not being resized  `ALLOCATING` - Memory is being allocated (can be cancelled by the user)  `ACTIVATING` - New buffers are being created (user cannot cancel)  `SHRINKING` - Buffers are being deleted (can be cancelled by the user) |
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

See Also:

["DB\_BLOCK\_SIZE"](initparams050.md)