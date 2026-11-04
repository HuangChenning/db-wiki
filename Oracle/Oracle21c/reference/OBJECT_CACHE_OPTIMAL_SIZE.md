---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OBJECT_CACHE_OPTIMAL_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.233 OBJECT\_CACHE\_OPTIMAL\_SIZE

`OBJECT_CACHE_OPTIMAL_SIZE` specifies (in bytes) the size to which the session object cache is reduced when the size of the cache exceeds the maximum size.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `10240000` (10M) |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM ... DEFERRED` |
| Modifiable in a PDB | Yes |
| Range of values | 10 KB to operating system-dependent maximum |
| Basic | No |

The object cache is a memory block on the client that allows applications to store entire objects and to navigate among them without round trips to the server. On the server, it is used to cache frequently used objects requested as a result of client requests to help in performance.

See Also:

[Pro\*C/C++ Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=LNPCC4321) and [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=LNOCI16983) for information on precompiler use of the object cache