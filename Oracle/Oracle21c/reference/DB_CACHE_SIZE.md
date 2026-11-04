---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_CACHE_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.77 DB\_CACHE\_SIZE

`DB_CACHE_SIZE` specifies the size of the `DEFAULT` buffer pool for buffers with the primary block size (the block size defined by the `DB_BLOCK_SIZE` initialization parameter).

Note:

Oracle recommends against setting this parameter in a PDB. The only shared memory sizing parameter that should be set in a PDB is `SGA_TARGET`, which specifies the maximum SGA that the PDB can use at any time.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `DB_CACHE_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | If `SGA_TARGET` is set: If the parameter is not specified, then the default is `0` (internally determined by the Oracle Database). If the parameter is specified, then the user-specified value indicates a minimum value for the memory pool.  If `SGA_TARGET` is not set, then the default is either 48 MB or 4 MB \* number of CPUs, whichever is greater |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

The value must be at least `4M * number of cpus ` (smaller values are automatically rounded up to this value). A user-specified value larger than this is rounded up to the nearest granule size. A value of zero is invalid because it is needed for the `DEFAULT` memory pool of the primary block size, which is the block size for the `SYSTEM` tablespace.

See Also:

- " [SGA\_TARGET](SGA_TARGET.md) "
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA336) and [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11220) for more information on setting this parameter
- [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=MULTI-GUID-A3459A8B-A36A-44D4-9FCD-75CA0E3D3252) for more information about the initialization parameters that control the memory usage of PDBs