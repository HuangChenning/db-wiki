---
title: DB_FLASH_CACHE_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams060.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `DB_FLASH_CACHE_SIZE =` `integer` `[K \| M \| G]` |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM` |
| Range of values | Minimum: `0`  Maximum: operating system-dependent |
| Basic | No |

`DB_FLASH_CACHE_SIZE` specifies the size of the Database Smart Flash Cache (flash cache). This parameter may only be specified at instance startup. You can dynamically change this parameter to `0` (disabling the flash cache) after the database is started. You can re-enable flash cache by setting this parameter to the original value when the database was started. Dynamic resizing of `DB_FLASH_CACHE_SIZE` or re-enabling flash cache to a different size is not supported.

Note:

This initialization parameter is available starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

["DB\_FLASH\_CACHE\_FILE"](initparams059.md)