---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/MEMORY_MAX_TARGET.html
tags:
  - oracle
  - 12c
  - reference
---

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

See the description of `MEMORY_TARGET` for more information about how the settings of `MEMORY_MAX_TARGET` and `MEMORY_TARGET` affect each other.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN00207) for more information about managing memory