---
title: DB_nK_CACHE_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams046.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `DB_[2 \| 4 \| 8 \| 16 \| 32]K_CACHE_SIZE =` `integer` `[K \| M \| G]` |
| Default value | `0` (additional block size caches are not configured by default) |
| Modifiable | `ALTER SYSTEM` |
| Range of values | Minimum: `0` (values greater than zero are automatically modified to be either the granule size \* number of processor groups, or 4 MB \* number of CPUs, whichever is greater)  Maximum: operating system-dependent |
| Basic | No |

`DB_` `n` `K_CACHE_SIZE` (where `n` = 2, 4, 8, 16, 32) specifies the size of the cache for the `n` `K` buffers. You can set this parameter only when `DB_BLOCK_SIZE` has a value other than `n` `K`. For example, if `DB_BLOCK_SIZE` = `4096`, then it is illegal to specify the parameter `DB_4K_CACHE_SIZE` (because the size for the 4 KB block cache is already specified by `DB_CACHE_SIZE`).

Do not set this parameter to zero if there are any online tablespaces with an `n` `K` block size.

Operating system-specific block size restrictions apply. For example, you cannot set `DB_32K_CACHE_SIZE` if the operating system's maximum block size is less than 32 KB. Also, you cannot set `DB_2K_CACHE_SIZE` if the minimum block size is greater than 2 KB.

See Also:

Your operating system-specific Oracle documentation for more information on block size restrictions