---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_FLASH_CACHE_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.85 DB\_FLASH\_CACHE\_SIZE

`DB_FLASH_CACHE_SIZE` specifies the size of the Database Smart Flash Cache (flash cache). This parameter may only be specified at instance startup.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `DB_FLASH_CACHE_SIZE =` `integer` `[K \| M \| G \| T] [,` `integer` `[K \| M \| G \| T]]...` |
| Default value | 0 |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | 0 to (`DB_BLOCK_SIZE` \* 256 MB)  - If `DB_BLOCK_SIZE` = 2 KB, then 0 to 512 GB - If `DB_BLOCK_SIZE` = 4 KB, then 0 to 1 TB - If `DB_BLOCK_SIZE` = 8 KB, then 0 to 2 TB - If `DB_BLOCK_SIZE` = 16 KB, then 0 to 4 TB - If `DB_BLOCK_SIZE` = 32 KB, then 0 to 8 TB |
| Basic | No |

You can specify up to 16 file sizes, for each of the flash memory devices specified with `DB_FLASH_CACHE_FILE`. For example, if there are three flash raw devices, you can specify the sizes of each device as follows:

```
db_flash_cache_file = /dev/raw/sda, /dev/raw/sdb, /dev/raw/sdc
db_flash_cache_size = 32G, 32G, 64G
```

If your flash cache consists of one flash cache device, you can dynamically change this parameter to `0` for that flash cache device (disabling the flash cache) after the database is started. You can then reenable the flash cache by setting this parameter for the device back to the original value when the database was started. Dynamic resizing of `DB_FLASH_CACHE_SIZE` or reenabling flash cache to a different size is not supported.

If your flash cache includes multiple flash cache devices, you can dynamically change the parameter to `0` for a particular flash cache device (turning it off) after the database is started. You can then reenable that flash cache device by setting this parameter for the device back to the original value it had when the database was started (turning it back on).

For example, to turn off the `/dev/raw/sdb` flash cache device:

```
db_flash_cache_file = /dev/raw/sda, /dev/raw/sdb, /dev/raw/sdc
db_flash_cache_size = 32G, 0, 64G
```

And, to turn the `/dev/raw/sdb` flash cache device back on again:

```
db_flash_cache_file = /dev/raw/sda, /dev/raw/sdb, /dev/raw/sdc
db_flash_cache_size = 32G, 32G, 64G
```

See Also:

" [DB\_FLASH\_CACHE\_FILE](DB_FLASH_CACHE_FILE.md) "