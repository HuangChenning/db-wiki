---
title: DB_FLASH_CACHE_FILE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams059.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_FLASH_CACHE_FILE =` `filename` `\|` `disk group` |
| Default value | There is no default value. |
| Modifiable | No |
| Basic | No |

`DB_FLASH_CACHE_FILE` filename for the flash memory or disk group representing a collection of flash memory.

Specifying this parameter without also specifying the `DB_FLASH_CACHE_SIZE` initialization parameter is not allowed.

Note:

This initialization parameter is available starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

["DB\_FLASH\_CACHE\_SIZE"](initparams060.md)