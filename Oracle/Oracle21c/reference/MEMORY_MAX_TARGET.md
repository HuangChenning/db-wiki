---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/MEMORY_MAX_TARGET.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.212 MEMORY\_MAX\_TARGET

`MEMORY_MAX_TARGET` specifies the maximum value to which a DBA can set the `MEMORY_TARGET` initialization parameter.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `MEMORY_MAX_TARGET = ` `integer` ` [K \| M \| G]` |
| Default value | `0` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `0` to the physical memory size available to the Oracle Database |
| Basic | No |

Note:

On Linux platforms only, Oracle recommends against explicitly setting values for `MEMORY_TARGET` and `MEMORY_MAX_TARGET` in the initialization parameter file at the time of instance startup. Doing so may result in suboptimal small page allocation in the SGA. Furthermore, if the `USE_LARGE_PAGES` parameter is set to `ONLY` and you attempt to set values for `MEMORY_TARGET` and `MEMORY_MAX_TARGET`, the instance will fail to start.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN00207) for more information about managing memory
- " [MEMORY\_TARGET](MEMORY_TARGET.md) "
- " [USE\_LARGE\_PAGES](USE_LARGE_PAGES.md) "