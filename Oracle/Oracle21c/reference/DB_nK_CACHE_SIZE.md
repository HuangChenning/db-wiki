---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_nK_CACHE_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.70 DB\_nK\_CACHE\_SIZE

`DB_` `n` `K_CACHE_SIZE` (where `n` = 2, 4, 8, 16, 32) specifies the size of the cache for the `n` `K` buffers.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `DB_[2 \| 4 \| 8 \| 16 \| 32]K_CACHE_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | `0` (additional block size caches are not configured by default) |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | Minimum: `0` (values greater than zero are automatically modified to be either the granule size \* number of processor groups, or 4 MB \* number of CPUs, whichever is greater)  Maximum: operating system-dependent |
| Basic | No |

You can set this parameter only when `DB_BLOCK_SIZE` has a value other than `n` `K`. For example, if `DB_BLOCK_SIZE` = `4096`, then you cannot specify the parameter `DB_4K_CACHE_SIZE` (because the size for the 4 KB block cache is already specified by `DB_CACHE_SIZE`).

Do not set this parameter to zero if there are any online tablespaces with an `n` `K` block size.

Operating system-specific block size restrictions apply. For example, you cannot set `DB_32K_CACHE_SIZE` if the operating system's maximum block size is less than 32 KB. Also, you cannot set `DB_2K_CACHE_SIZE` if the minimum block size is greater than 2 KB.

See Also:

Your operating system-specific Oracle documentation for more information on block size restrictions