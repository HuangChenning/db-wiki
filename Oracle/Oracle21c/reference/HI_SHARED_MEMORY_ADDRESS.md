---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/HI_SHARED_MEMORY_ADDRESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.145 HI\_SHARED\_MEMORY\_ADDRESS

`HI_SHARED_MEMORY_ADDRESS` specifies the starting address at run time of the system global area (SGA).

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |

This parameter is ignored on platforms that specify the SGA's starting address at linktime.

On 64-bit platforms, use `HI_SHARED_MEMORY_ADDRESS` to specify the high-order 32 bits of a 64-bit address. Use `SHARED_MEMORY_ADDRESS` to specify the low-order 32 bits of the address (see " [SHARED\_MEMORY\_ADDRESS](SHARED_MEMORY_ADDRESS.md) "). If both parameters are 0 or unspecified, the SGA address defaults to a platform-specific location.