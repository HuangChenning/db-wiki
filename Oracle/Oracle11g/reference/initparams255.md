---
title: STREAMS_POOL_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams255.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `STREAMS_POOL_SIZE =` `integer` `[K \| M \| G]` |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM` |
| Range of values | Minimum: `0` (values greater than zero are rounded up to the nearest granule size)  Maximum: operating system-dependent |

Oracle's Automatic Shared Memory Management feature manages the size of the Streams pool when the `SGA_TARGET` initialization parameter is set to a nonzero value. If the `STREAMS_POOL_SIZE` initialization parameter also is set to a nonzero value, then Automatic Shared Memory Management uses this value as a minimum for the Streams pool.

If the `STREAMS_POOL_SIZE` initialization parameter is set to a nonzero value, and the `SGA_TARGET` parameter is set to 0 (zero), then the Streams pool size is the value specified by the `STREAMS_POOL_SIZE` parameter, in bytes.

If both the `STREAMS_POOL_SIZE` and the `SGA_TARGET` initialization parameters are set to 0 (zero), then, by default, the first use of Streams in a database transfers an amount of memory equal to 10% of the shared pool from the buffer cache to the Streams pool.