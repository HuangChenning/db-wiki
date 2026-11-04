---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INMEMORY_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.158 INMEMORY\_SIZE

`INMEMORY_SIZE` sets the size of the In-Memory Area, which contains the IM Column Store (IM column store) on a database instance.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `INMEMORY_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | 0 to the amount of memory left in the SGA after other allocations |
| Basic | No |
| Oracle RAC | All instances should use the same value. |

The default value is 0, which means that the IM column store is not used.

The database must be restarted after setting this parameter to enable the IM column store.

The minimum size to which this parameter can be set is 100 MB.

Typically this parameter should be set to at least the size needed to accommodate all the tables that will use the IM column store. It can be set higher to allow for growth of those tables or to accommodate other tables that will use the IM column store in the future.

This parameter can also be set per PDB to limit the maximum size of the IM column store for that PDB. Note that the sum of the PDB values do not have to equal the CDB value, and the sum of the PDB values may even be greater than the CDB value.

Unless this parameter is specifically set on a PDB, each PDB inherits the CDB value, which means they can use all of the available IM column store.

The value specified for this parameter counts toward `SGA_TARGET`. For example, if you set `SGA_TARGET` to 10 GB and you set `INMEMORY_SIZE` to 2 GB, then 20% of the `SGA_TARGET` setting is allocated to the In-Memory Area.

Unlike other SGA components such as the buffer cache and shared pool, the In-Memory Area size is not controlled by automatic memory management. The database does not automatically shrink the In-Memory Area when the buffer cache or shared pool requires more memory, or increase the In-Memory Area when it runs out of space. You can only increase the size of the In-Memory Area by manually adjusting the `INMEMORY_SIZE` initialization parameter.

In-Memory Dynamic Scans require the Resource Manager. Therefore, the Resource Manager is automatically enabled when you change the value of `INMEMORY_SIZE` from `0` to a non-zero value. No specific resource plan is required.

Database In-Memory Base Level allows a maximum of 16 GB for the size of the In-Memory area. Therefore, if Database In-Memory Base Level is enabled (the value of the `INMEMORY_FORCE` initialization parameter is set to `BASE_LEVEL`), then the value of `INMEMORY_SIZE` cannot exceed 16 GB for a CDB. In an Oracle RAC environment, the value of `INMEMORY_SIZE` is limited to 16 GB for each instance.

See Also:

- " [INMEMORY\_CLAUSE\_DEFAULT](INMEMORY_CLAUSE_DEFAULT.md) "
- " [INMEMORY\_FORCE](INMEMORY_FORCE.md) "
- " [INMEMORY\_MAX\_POPULATE\_SERVERS](INMEMORY_MAX_POPULATE_SERVERS.md) "
- " [INMEMORY\_QUERY](INMEMORY_QUERY.md) "
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-BFA53515-7643-41E5-A296-654AB4A9F9E7) for an introduction to the IM column store
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-EEA265EE-8FBA-4457-8C3F-315B9EEA2224) for more information about the IM column store
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-6A220D69-66BA-4C50-8FAB-D5004C96B215) for an example of using the `INMEMORY_SIZE` parameter