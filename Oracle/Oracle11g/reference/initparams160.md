---
title: OBJECT_CACHE_MAX_SIZE_PERCENT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams160.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | 10 |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM ... DEFERRED` |
| Range of values | 0 to operating system-dependent maximum |

The object cache is a memory block on the client that allows applications to store entire objects and to navigate among them without round trips to the server. `OBJECT_CACHE_MAX_SIZE_PERCENT` specifies the percentage of the optimal cache size that the session object cache can grow past the optimal size. The maximum size is equal to the optimal size plus the product of this percentage and the optimal size. When the cache size exceeds this maximum size, the system will attempt to shrink the cache to the optimal size.

See Also:

- ["OBJECT\_CACHE\_OPTIMAL\_SIZE"](initparams161.md) for a description of the object cache
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm), [Pro\*C/C++ Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10825/toc.htm), and [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm) for information on precompiler use of the object cache