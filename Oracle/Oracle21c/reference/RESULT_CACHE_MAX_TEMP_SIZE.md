---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESULT_CACHE_MAX_TEMP_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.317 RESULT\_CACHE\_MAX\_TEMP\_SIZE

`RESULT_CACHE_MAX_TEMP_SIZE` specifies the maximum amount of temporary tablespace (in bytes) that can be consumed by the result cache.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `RESULT_CACHE_MAX_TEMP_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | `RESULT_CACHE_MAX_SIZE` \* `10` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `0` to operating system-dependent |
| Basic | No |
| Oracle RAC | You must either set this parameter to `0` on all instances to disable the result cache, or use a nonzero value on all instances. Disabling the result cache on some instances may lead to incorrect results. |

If you attempt to set this parameter to a value that is less than 5% of the size of the SGA, then this parameter will be set to 5% of the size of the SGA. If you attempt to set this parameter to a value that is more than 10% of the current total unused space available for temporary tablespaces in the `SYS` schema, then this parameter will be set to 10% of the current total unused space available for temporary tablespaces in the `SYS` schema.

If the value of this parameter is 0, then the result cache is disabled for the PDB.

Note:

This parameter is available starting with Oracle Database 21c.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA616) for information about tuning the result cache