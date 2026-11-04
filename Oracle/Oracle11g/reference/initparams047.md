---
title: DB_BLOCK_BUFFERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams047.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | No |
| Range of values | `50` to an operating system-specific maximum |
| Basic | No |
| Oracle RAC | Multiple instances can have different values, and you can change the values as needed. |

Note:

`DB_BLOCK_BUFFERS` cannot be combined with the dynamic `DB_CACHE_SIZE` parameter; combining these parameters in the same parameter file will produce an error.

`DB_BLOCK_BUFFERS` specifies the number of database buffers in the buffer cache. It is one of several parameters that contribute to the total memory requirements of the SGA of an instance.

This parameter, together with `DB_BLOCK_SIZE`, determines the total size of the buffer cache. Effective use of the buffer cache can greatly reduce the I/O load on the database. `DB_BLOCK_SIZE` can be specified only when the database is first created, so you use `DB_BLOCK_BUFFERS` to control the size of the buffer cache.