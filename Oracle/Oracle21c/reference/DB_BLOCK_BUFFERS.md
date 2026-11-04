---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_BLOCK_BUFFERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.72 DB\_BLOCK\_BUFFERS

`DB_BLOCK_BUFFERS` specifies the number of database buffers in the buffer cache.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `50` to an operating system-specific maximum |
| Basic | No |
| Oracle RAC | Multiple instances can have different values, and you can change the values as needed. |

Note:

`DB_BLOCK_BUFFERS` cannot be combined with the dynamic `DB_CACHE_SIZE` parameter; combining these parameters in the same parameter file will produce an error.

`DB_BLOCK_BUFFERS` is one of several parameters that contribute to the total memory requirements of the SGA of an instance.

This parameter, together with `DB_BLOCK_SIZE`, determines the total size of the buffer cache. Effective use of the buffer cache can greatly reduce the I/O load on the database. `DB_BLOCK_SIZE` can be specified only when the database is first created, so you use `DB_BLOCK_BUFFERS` to control the size of the buffer cache.

Note:

The `DB_BLOCK_BUFFERS` initialization parameter is deprecated. It is maintained for backward compatibility.

Oracle recommends that you use `DB_CACHE_SIZE` instead.

See Also:

" [DB\_CACHE\_SIZE](DB_CACHE_SIZE.md) "