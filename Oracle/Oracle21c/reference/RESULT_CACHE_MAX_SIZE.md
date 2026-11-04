---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESULT_CACHE_MAX_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.315 RESULT\_CACHE\_MAX\_SIZE

`RESULT_CACHE_MAX_SIZE` specifies the maximum amount of SGA memory (in bytes) that can be used by the result cache.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `RESULT_CACHE_MAX_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | Derived from the values of `SHARED_POOL_SIZE`, `SGA_TARGET`, and `MEMORY_TARGET` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to operating system-dependent |
| Basic | No |
| Oracle RAC | You must either set this parameter to `0` on all instances to disable the result cache, or use a nonzero value on all instances. Disabling the result cache on some instances may lead to incorrect results. |

Values of this parameter greater than `0` are rounded up to the next multiple of 32 KB. If the value of this parameter is `0`, then the feature is disabled.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA616) for information about tuning the result cache