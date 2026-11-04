---
title: SHARED_POOL_RESERVED_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams239.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `SHARED_POOL_RESERVED_SIZE =` `integer` `[K \| M \| G]` |
| Default value | 5% of the value of `SHARED_POOL_SIZE` |
| Modifiable | No |
| Range of values | Minimum: `5000`  Maximum: one half of the value of `SHARED_POOL_SIZE` |

`SHARED_POOL_RESERVED_SIZE` specifies (in bytes) the shared pool space that is reserved for large contiguous requests for shared pool memory.

You can use this parameter to avoid performance degradation in the shared pool in situations where pool fragmentation forces Oracle to search for and free chunks of unused pool to satisfy the current request.

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information on setting this parameter
- ["SHARED\_POOL\_SIZE"](initparams240.md)