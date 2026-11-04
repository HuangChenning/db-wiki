---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PGA_AGGREGATE_LIMIT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.281 PGA\_AGGREGATE\_LIMIT

`PGA_AGGREGATE_LIMIT` specifies a limit on the aggregate PGA memory consumed by the instance.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `PGA_AGGREGATE_LIMIT = ` `integer` ` [K \| M \| G]` |
| Default value | If `MEMORY_TARGET` is set, then `PGA_AGGREGATE_LIMIT` defaults to the `MEMORY_MAX_TARGET` value.  If `MEMORY_TARGET` is not set, then `PGA_AGGREGATE_LIMIT` defaults to 200% of `PGA_AGGREGATE_TARGET`.  If `MEMORY_TARGET` is not set, and `PGA_AGGREGATE_TARGET` is explicitly set to 0, then the value of `PGA_AGGREGATE_LIMIT` is set to 90% of the physical memory size minus the total SGA size.  In all cases, the default `PGA_AGGREGATE_LIMIT` is at least 2GB and at least 3MB times the `PROCESSES` parameter (and at least 5MB times the `PROCESSES` parameter for an Oracle RAC instance).  For a PDB, the default value is the same as the CDB's default value. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | Do not attempt to set `PGA_AGGREGATE_LIMIT` below its default value, even in a parameter file (pfile), or instance startup will fail. However, `PGA_AGGREGATE_LIMIT` can be set to 0 either in a parameter file or dynamically after startup. If a value of 0 is specified, it means there is no limit to the aggregate PGA memory consumed by the instance. |
| Basic | No |

Actions Taken When PGA\_AGGREGATE\_LIMIT is Exceeded

Parallel queries will be treated as a unit. First, the sessions that are using the most untunable memory will have their calls terminated. Then, if the total PGA memory usage is still over the limit, the sessions that are using the most untunable memory will be terminated.

SYS processes and background processes other than job queue processes will not be subjected to any of the actions described in this section. Instead, if they are using the most untunable memory, they will periodically write a brief summary of their PGA usage to a trace file.

Note:

This parameter is optional for pluggable databases (PDBs). When this parameter is set for a PDB, it specifies the maximum PGA size for the PDB.

To be able to use Resource Manager in a CDB to control the amount of memory each PDB can use:

- The `NONCDB_COMPATIBLE` initialization parameter must be set to `FALSE` at the CDB level (in the root of the CDB).
- The `MEMORY_TARGET` initialization parameter must not be set at the CDB level.
- You must set the `PGA_AGGREGATE_LIMIT` initialization parameter in a PDB to a value that meets these requirements:
	- Less than or equal to the `PGA_AGGREGATE_LIMIT` value set at the CDB level
		- Greater than or equal to twice the value of `PGA_AGGREGATE_TARGET` set in the PDB
	When you set `PGA_AGGREGATE_LIMIT` in a PDB to a value that does not meet these requirements, you receive an error. If these requirements are violated after the PDB’s parameter is set (for example, if the `PGA_AGGREGATE_LIMIT` value is changed at the CDB level), Oracle will adjust the PDB’s value to meet these requirements.

See Also:

- " [MEMORY\_TARGET](MEMORY_TARGET.md) "
- " [PGA\_AGGREGATE\_TARGET](PGA_AGGREGATE_TARGET.md) "
- [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=MULTI-GUID-A3459A8B-A36A-44D4-9FCD-75CA0E3D3252) for more information about the initialization parameters that control the memory usage of PDBs
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA95346) for more information about this parameter