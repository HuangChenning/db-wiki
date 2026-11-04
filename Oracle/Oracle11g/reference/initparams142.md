---
title: MEMORY_MAX_TARGET
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams142.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `MEMORY_MAX_TARGET =` `integer` `[K \| M \| G]` |
| Default value | `0` |
| Modifiable | No |
| Range of values | `0` to the physical memory size available to the Oracle Database |
| Basic | No |

`MEMORY_MAX_TARGET` specifies the maximum value to which a DBA can set the `MEMORY_TARGET` initialization parameter. See the description of `MEMORY_TARGET` for more information about how the settings of `MEMORY_MAX_TARGET` and `MEMORY_TARGET` affect each other.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/memory.htm#ADMIN00207) for more information about managing memory