---
title: DB_BLOCK_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams050.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `8192` |
| Modifiable | No |
| Range of values | `2048` to `32768`, but your operating system may have a narrower range |
| Basic | Yes |
| Oracle RAC | You must set this parameter for every instance, and multiple instances must have the same value. |

Caution:

Set this parameter at the time of database creation. Do not alter it afterward.

`DB_BLOCK_SIZE` specifies (in bytes) the size of Oracle database blocks. Typical values are `4096` and `8192`. The value of this parameter must be a multiple of the physical block size at the device level.

The value for `DB_BLOCK_SIZE` in effect at the time you create the database determines the size of the blocks. The value must remain set to its initial value.

For Real Application Clusters, this parameter affects the maximum value of the `FREELISTS` storage parameter for tables and indexes. Oracle uses one database block for each freelist group. Decision support system (DSS) and data warehouse database environments tend to benefit from larger block size values.

Note:

- 32-bit operating systems support a maximum `DB_BLOCK_SIZE` value of 16384
- 64-bit operating systems support a maximum `DB_BLOCK_SIZE` value of 32768

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information on setting this parameter
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for information on freelist groups
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information on the DSS and data warehouse environments
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for general information on block sizes