---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/OBJECT_CACHE_MAX_SIZE_PERCENT.html
tags:
  - oracle
  - 12c
  - reference
---

The object cache is a memory block on the client that allows applications to store entire objects and to navigate among them without round trips to the server. `OBJECT_CACHE_MAX_SIZE_PERCENT` specifies the percentage of the optimal cache size that the session object cache can grow past the optimal size.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `10` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM ... DEFERRED` |
| Modifiable in a PDB | Yes |
| Range of values | 0 to operating system-dependent maximum |
| Basic | No |

The maximum size is equal to the optimal size plus the product of this percentage and the optimal size. When the cache size exceeds this maximum size, the system will attempt to shrink the cache to the optimal size.

See Also:

- " [OBJECT\_CACHE\_OPTIMAL\_SIZE](OBJECT_CACHE_OPTIMAL_SIZE.md) " for a description of the object cache
- [Pro\*C/C++ Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=LNPCC4321) and [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=LNOCI16983) for information on precompiler use of the object cache