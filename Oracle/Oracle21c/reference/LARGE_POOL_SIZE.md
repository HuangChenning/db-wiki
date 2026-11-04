---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LARGE_POOL_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.172 LARGE\_POOL\_SIZE

`LARGE_POOL_SIZE` specifies (in bytes) the size of the large pool allocation heap.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `LARGE_POOL_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | If `SGA_TARGET` is set, but a value is not specified for `LARGE_POOL_SIZE`, then the default is `0` (internally determined by the Oracle database). If `LARGE_POOL_SIZE` is specified, then the user-specified value indicates a minimum value for the memory pool.  If `SGA_TARGET` is not set, then the default is `0`. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | Minimum: the granule size  Maximum: operating system-dependent |
| Basic | No |

The large pool allocation heap is used in shared server systems for session memory, by parallel execution for message buffers, and by backup processes for disk I/O buffers. Parallel execution allocates buffers out of the large pool only when `SGA_TARGET` is set.

You can specify the value of this parameter using a number, optionally followed by K or M to specify kilobytes or megabytes, respectively. If you do not specify K or M, then the number is taken as bytes.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA336) for more information on setting this parameter