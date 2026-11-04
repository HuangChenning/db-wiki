---
title: OBJECT_CACHE_OPTIMAL_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams161.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `102400` (100K) |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM ... DEFERRED` |
| Range of values | 10 KB to operating system-dependent maximum |

The object cache is a memory block on the client that allows applications to store entire objects and to navigate among them without round trips to the server. `OBJECT_CACHE_OPTIMAL_SIZE` specifies (in bytes) the size to which the session object cache is reduced when the size of the cache exceeds the maximum size.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm), [Pro\*C/C++ Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10825/toc.htm), and [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm) for information on precompiler use of the object cache