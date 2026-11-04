---
title: PGA_AGGREGATE_TARGET
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams193.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `PGA_AGGREGATE_TARGET =` `integer` `[K \| M \| G]` |
| Default value | 10 MB or 20% of the size of the SGA, whichever is greater |
| Modifiable | `ALTER SYSTEM` |
| Range of values | Minimum: 10 MB  Maximum: 4096 GB - 1 |
| Basic | Yes |

`PGA_AGGREGATE_TARGET` specifies the target aggregate PGA memory available to all server processes attached to the instance.

Setting `PGA_AGGREGATE_TARGET` to a nonzero value has the effect of automatically setting the `WORKAREA_SIZE_POLICY` parameter to `AUTO`. This means that SQL working areas used by memory-intensive SQL operators (such as sort, group-by, hash-join, bitmap merge, and bitmap create) will be automatically sized. A nonzero value for this parameter is the default since, unless you specify otherwise, Oracle sets it to 20% of the SGA or 10 MB, whichever is greater.

Setting `PGA_AGGREGATE_TARGET` to 0 automatically sets the `WORKAREA_SIZE_POLICY` parameter to `MANUAL`. This means that SQL workareas are sized using the `*_AREA_SIZE` parameters.

Oracle attempts to keep the amount of private memory below the target specified by this parameter by adapting the size of the work areas to private memory. When increasing the value of this parameter, you indirectly increase the memory allotted to work areas. Consequently, more memory-intensive operations are able to run fully in memory and less will work their way over to disk.

If Automatic Memory Management is enabled (`MEMORY_TARGET` is set to a positive value) and `PGA_AGGREGATE_TARGET` is also set to a positive value, the `PGA_AGGREGATE_TARGET` value acts as the minimum value for the size of the instance PGA.