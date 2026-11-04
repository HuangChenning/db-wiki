---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DB_FLASH_CACHE_FILE.html
tags:
  - oracle
  - 12c
  - reference
---

`DB_FLASH_CACHE_FILE` specifies file name(s) for the flash memory or disk group representing a collection of flash memory, for use with Database Smart Flash Cache.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_FLASH_CACHE_FILE = ` `filename [,filename]...``  \|  ` `disk group` |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

You can specify up to 16 file names for flash memory devices. For example, if there are three flash raw devices:

```
db_flash_cache_file = /dev/raw/sda, /dev/raw/sdb, /dev/raw/sdc
```

Specifying this parameter without also specifying the `DB_FLASH_CACHE_SIZE` initialization parameter is not allowed.

See Also:

" [DB\_FLASH\_CACHE\_SIZE](DB_FLASH_CACHE_SIZE.md) "