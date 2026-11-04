---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PGA_AGGREGATE_TARGET.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.282 PGA\_AGGREGATE\_TARGET

`PGA_AGGREGATE_TARGET` specifies the target aggregate PGA memory available to all server processes attached to the instance.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `PGA_AGGREGATE_TARGET = ` `integer` ` [K \| M \| G]` |
| Default value | `10` MB or 20% of the size of the SGA, whichever is greater  For a PDB, the default value is the same as the CDB's default value. |
| Modifiable | `ALTER SYSTEM ` |
| Modifiable in a PDB | Yes |
| Range of values | Minimum: 10 MB  Maximum: 4096 GB - 1 |
| Basic | Yes |

To set a hard limit for aggregate PGA memory, use the `PGA_AGGREGATE_LIMIT` parameter.

Setting `PGA_AGGREGATE_TARGET` to a nonzero value has the effect of automatically setting the `WORKAREA_SIZE_POLICY` parameter to `AUTO`. With this setting, SQL working areas used by memory-intensive SQL operators (such as sort, group-by, hash-join, bitmap merge, and bitmap create) will be automatically sized. A nonzero value for this parameter is the default since, unless you specify otherwise, Oracle sets it to 20% of the SGA or 10 MB, whichever is greater.

Setting `PGA_AGGREGATE_TARGET` to 0 automatically sets the `WORKAREA_SIZE_POLICY` parameter to `MANUAL`. With this setting, SQL working areas are sized using the `*_AREA_SIZE` parameters.

Oracle attempts to keep the amount of private memory below the target specified by this parameter by adapting the size of the working areas to private memory. When increasing the value of this parameter, you indirectly increase the memory allotted to working areas. Consequently, more memory-intensive operations are able to run fully in memory and fewer will work their way over to disk.

If Automatic Memory Management is enabled (`MEMORY_TARGET` is set to a positive value) and `PGA_AGGREGATE_TARGET` is also set to a positive value, the `PGA_AGGREGATE_TARGET` value acts as the minimum value for the size of the instance PGA.

Note:

This parameter is optional for pluggable databases (PDBs). When this parameter is set for a PDB, it specifies the target aggregate PGA size for the PDB.

To be able to use Resource Manager in a CDB to control the amount of memory each PDB can use:

- The `NONCDB_COMPATIBLE` initialization parameter must be set to `FALSE` at the CDB level (in the root of the CDB).
- The `MEMORY_TARGET` initialization parameter must not be set at the CDB level.
- You must set the `PGA_AGGREGATE_TARGET` initialization parameter in a PDB to a value that meets these requirements:
	- Less than or equal to the `PGA_AGGREGATE_TARGET` value set at the CDB level
		- Less than or equal to 50% of the `PGA_AGGREGATE_LIMIT` initialization parameter value set at the CDB level
		- Less than or equal to 50% of the `PGA_AGGREGATE_LIMIT` value set in the PDB
	When you set `PGA_AGGREGATE_TARGET` in a PDB to a value that does not meet these requirements, you receive an error. If these requirements are violated after the PDB’s parameter is set (for example, if the `PGA_AGGREGATE_TARGET` value is changed at the CDB level), Oracle will adjust the PDB’s value to meet these requirements.

See Also:

- " [WORKAREA\_SIZE\_POLICY](WORKAREA_SIZE_POLICY.md) "
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA290) for more information about configuring memory
- " [PGA\_AGGREGATE\_LIMIT](PGA_AGGREGATE_LIMIT.md) "