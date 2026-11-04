---
title: SGA_MAX_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams235.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `SGA_MAX_SIZE =` `integer` `[K \| M \| G]` |
| Default value | Initial size of SGA at startup, dependent on the sizes of different pools in the SGA, such as buffer cache, shared pool, large pool, and so on. |
| Modifiable | No |
| Range of values | 0 to operating system-dependent |

`SGA_MAX_SIZE` specifies the maximum size of the SGA for the lifetime of the instance.

On 64-bit platforms and non-Windows 32-bit platforms, when either `MEMORY_TARGET` or `MEMORY_MAX_TARGET` is specified, the default value of `SGA_MAX_SIZE` is set to the larger of the two parameters. This causes more address space to be reserved for expansion of the SGA.

On Windows 32-bit platforms, the default value of `SGA_MAX_SIZE` is the largest of the following values:

- 60% of `MEMORY_TARGET`, if specified
- 60% of `MEMORY_MAX_TARGET`, if specified
- 25% of the total available virtual address space