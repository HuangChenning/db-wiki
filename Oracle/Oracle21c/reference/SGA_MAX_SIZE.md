---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SGA_MAX_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.331 SGA\_MAX\_SIZE

`SGA_MAX_SIZE` specifies the maximum size of the SGA for the lifetime of the instance.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `SGA_MAX_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | Initial size of SGA at startup, dependent on the sizes of different pools in the SGA, such as buffer cache, shared pool, large pool, and so on. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 0 to operating system-dependent |

On 64-bit platforms and non-Windows 32-bit platforms, when either `MEMORY_TARGET` or `MEMORY_MAX_TARGET` is specified, the default value of `SGA_MAX_SIZE` is set to the larger of the two parameters. This causes more address space to be reserved for expansion of the SGA.

On Windows 32-bit platforms, the default value of `SGA_MAX_SIZE` is the largest of the following values:

- 60% of `MEMORY_TARGET`, if specified
- 60% of `MEMORY_MAX_TARGET`, if specified
- 25% of the total available virtual address space

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA518) for more information about this parameter