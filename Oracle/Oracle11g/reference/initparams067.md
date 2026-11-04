---
title: DB_RECYCLE_CACHE_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams067.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `DB_RECYCLE_CACHE_SIZE =` `integer` `[K \| M \| G]` |
| Default value | `0` (`DB_RECYCLE_CACHE_SIZE` is not configured by default) |
| Modifiable | `ALTER SYSTEM` |
| Range of values | Minimum: `0` (values greater than zero are automatically modified to be either the granule size \* number of processor groups, or 4 MB \* number of CPUs, whichever is greater)  Maximum: operating system-dependent |
| Basic | No |

`DB_RECYCLE_CACHE_SIZE` specifies the size of the `RECYCLE` buffer pool. The size of the buffers in the `RECYCLE` pool is the primary block size (the block size defined by the `DB_BLOCK_SIZE` initialization parameter).

See Also:

- ["DB\_KEEP\_CACHE\_SIZE"](initparams062.md)
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for information on setting these parameters and on using multiple buffer pools