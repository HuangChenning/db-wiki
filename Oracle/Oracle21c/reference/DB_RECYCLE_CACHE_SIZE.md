---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_RECYCLE_CACHE_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.94 DB\_RECYCLE\_CACHE\_SIZE

`DB_RECYCLE_CACHE_SIZE` specifies the size of the `RECYCLE` buffer pool.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `DB_RECYCLE_CACHE_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | `0` (`DB_RECYCLE_CACHE_SIZE` is not configured by default) |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | Minimum: `0` (values greater than zero are automatically modified to be either the granule size \* number of processor groups, or 4 MB \* number of CPUs, whichever is greater)  Maximum: operating system-dependent |
| Basic | No |

The size of the buffers in the `RECYCLE` pool is the primary block size (the block size defined by the `DB_BLOCK_SIZE` initialization parameter).

See Also:

- " [DB\_KEEP\_CACHE\_SIZE](DB_KEEP_CACHE_SIZE.md) "
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA315) for information on setting these parameters and on using multiple buffer pools