---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_BLOCK_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.75 DB\_BLOCK\_SIZE

`DB_BLOCK_SIZE` specifies (in bytes) the size of Oracle database blocks.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `8192` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `2048` to `32768`, but your operating system may have a narrower range |
| Basic | Yes |
| Oracle RAC | You must set this parameter for every instance, and multiple instances must have the same value. |

Note:

Set this parameter at the time of database creation. Do not alter it afterward.

Typical values for `DB_BLOCK_SIZE` are `4096` and `8192`. The value of this parameter must be a multiple of the physical block size at the device level.

The value for `DB_BLOCK_SIZE` in effect at the time you create the database determines the size of the blocks. The value must remain set to its initial value.

For Oracle Real Application Clusters (Oracle RAC), this parameter affects the maximum value of the `FREELISTS` storage parameter for tables and indexes. Oracle uses one database block for each freelist group. Decision support system (DSS) and data warehouse database environments tend to benefit from larger block size values.

Note:

64-bit operating systems support a maximum `DB_BLOCK_SIZE` value of 32768

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11106) for information on setting this parameter
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF52316) for information on freelist groups