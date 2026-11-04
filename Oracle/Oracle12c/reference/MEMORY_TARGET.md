---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/MEMORY_TARGET.html
tags:
  - oracle
  - 12c
  - reference
---

`MEMORY_TARGET` specifies the Oracle systemwide usable memory. The database tunes memory to the `MEMORY_TARGET` value, reducing or enlarging the SGA and PGA as needed.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `MEMORY_TARGET = ` `integer` ` [K \| M \| G]` |
| Default value | `0` (SGA autotuning is disabled for `DEFERRED` mode autotuning requests, but allowed for `IMMEDIATE` mode autotuning requests) |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | 152 MB to `MEMORY_MAX_TARGET` |
| Basic | No |

`MEMORY_TARGET` should be set higher than or equal to the sum of the current sizes of the SGA and PGA.

In a text-based initialization parameter file, if you omit `MEMORY_MAX_TARGET` and include a value for `MEMORY_TARGET`, then the database automatically sets `MEMORY_MAX_TARGET` to the value of `MEMORY_TARGET`. If you omit the line for `MEMORY_TARGET` and include a value for `MEMORY_MAX_TARGET`, the `MEMORY_TARGET` parameter defaults to zero. After startup, you can then dynamically change `MEMORY_TARGET` to a nonzero value, provided that it does not exceed the value of `MEMORY_MAX_TARGET`.

Total memory usage can grow beyond the value of `MEMORY_TARGET`. For example, memory is allocated to PL/SQL tables and varrays regardless of the value of `MEMORY_TARGET` as long as memory is available at the operating system level.

In the Default value field, `IMMEDIATE` mode autotuning requests are necessary to avoid `ORA-04031` errors. The `DEFERRED` and `IMMEDIATE` modes are reflected in the `OPER_MODE` column of the `V$MEMORY_RESIZE_OPS` view.

Note:

The default value of `SGA_MAX_SIZE` depends on the values of `MEMORY_TARGET` and `MEMORY_MAX_TARGET`.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN00207) for more information about managing memory
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN-GUID-A3459A8B-A36A-44D4-9FCD-75CA0E3D3252) for information about the initialization parameters that control the memory usage of PDBs