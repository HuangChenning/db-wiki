---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SHARED_POOL_RESERVED_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.336 SHARED\_POOL\_RESERVED\_SIZE

`SHARED_POOL_RESERVED_SIZE` specifies (in bytes) the shared pool space that is reserved for large contiguous requests for shared pool memory.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `SHARED_POOL_RESERVED_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | 5% of the value of `SHARED_POOL_SIZE` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | Minimum: `5000`  Maximum: half of the value of `SHARED_POOL_SIZE` |
| Basic | No |

You can use this parameter to avoid performance degradation in the shared pool in situations where pool fragmentation forces Oracle to search for and free chunks of unused pool to satisfy the current request.

See Also:

- " [SHARED\_POOL\_SIZE](SHARED_POOL_SIZE.md) "
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA606) for information on sizing the shared pool