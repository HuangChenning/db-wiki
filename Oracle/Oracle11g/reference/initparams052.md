---
title: DB_CACHE_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams052.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `DB_CACHE_SIZE =` `integer` `[K \| M \| G]` |
| Default value | If `SGA_TARGET` is set: If the parameter is not specified, then the default is `0` (internally determined by the Oracle Database). If the parameter is specified, then the user-specified value indicates a minimum value for the memory pool.  If `SGA_TARGET` is not set, then the default is either 48 MB or 4 MB \* number of CPUs, whichever is greater |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |

`DB_CACHE_SIZE` specifies the size of the `DEFAULT` buffer pool for buffers with the primary block size (the block size defined by the `DB_BLOCK_SIZE` initialization parameter).

The value must be at least `4M * number of cpus` (smaller values are automatically rounded up to this value). A user-specified value larger than this is rounded up to the nearest granule size. A value of zero is illegal because it is needed for the `DEFAULT` memory pool of the primary block size, which is the block size for the `SYSTEM` tablespace.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information on setting this parameter