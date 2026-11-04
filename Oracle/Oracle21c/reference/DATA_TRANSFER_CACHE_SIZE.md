---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DATA_TRANSFER_CACHE_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.69 DATA\_TRANSFER\_CACHE\_SIZE

`DATA_TRANSFER_CACHE_SIZE` sets the size of the data transfer cache (in bytes) used to receive data blocks (typically from a primary database in an Oracle Data Guard environment) for consumption by an instance during execution of an `RMAN RECOVER ... NONLOGGED BLOCK` command.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `DATA_TRANSFER_CACHE_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | If `SGA_TARGET` is set, then if `DATA_TRANSFER_CACHE_SIZE` is not specified, the default size of the data transfer cache is 0 (internally determined by Oracle Database). If `SGA_TARGET` is set and `DATA_TRANSFER_CACHE_SIZE` is specified, then the user-specified value indicates the minimum value for the data transfer cache.  If `SGA_TARGET` is not set, the data transfer cache will not be available. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | 0 – 512M, rounded up to the next granule size |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

This initialization parameter needs to be set only for databases that do not use Automatic Memory Management and that use the `RMAN RECOVER ... NONLOGGED BLOCK` command.