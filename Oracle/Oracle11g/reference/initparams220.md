---
title: RESULT_CACHE_MAX_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams220.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `RESULT_CACHE_MAX_SIZE =` `integer` `[K \| M \| G]` |
| Default value | Derived from the values of `SHARED_POOL_SIZE`, `SGA_TARGET`, and `MEMORY_TARGET` |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `0` to operating system-dependent |
| Basic | No |
| Oracle RAC | You must either set this parameter to `0` on all instances to disable the result cache, or use a nonzero value on all instances. Disabling the result cache on some instances may lead to incorrect results. |

`RESULT_CACHE_MAX_SIZE` specifies the maximum amount of SGA memory (in bytes) that can be used by the Result Cache. Values of this parameter greater than `0` are rounded up to the next multiple of 32 KB. If the value of this parameter is `0`, then the feature is disabled.