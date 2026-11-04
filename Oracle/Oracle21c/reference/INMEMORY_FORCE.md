---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INMEMORY_FORCE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.154 INMEMORY\_FORCE

`INMEMORY_FORCE` allows you to specify whether objects, such as tables, materialized views, and partitions, that are specified as `INMEMORY` are populated into the In-Memory Column Store (IM column store) or not.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `INMEMORY_FORCE = { DEFAULT \| OFF \| BASE_LEVEL \| CELLMEMORY_LEVEL }` |
| Default value | `DEFAULT` |
| Modifiable | You can use `ALTER` `SYSTEM` to dynamically modify this parameter setting as follows:  - From `DEFAULT` to `OFF` - From `OFF` to `DEFAULT` - From `BASE_LEVEL` to `DEFAULT` - From `CELLMEMORY_LEVEL` to `DEFAULT` - From `CELLMEMORY_LEVEL` to `OFF`  All other modifications of this parameter require you to update the initialization file and restart the instance. |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | All instances should use the same value. |

The following values can be set:

- `DEFAULT`
	The IM column store is populated with objects that are specified as `INMEMORY`.
- `OFF`
	Even if the IM column store is configured on this instance, no objects are populated in memory.
- `BASE_LEVEL`
	Enables Database In-Memory Base Level. The Base Level lets you to experiment with Oracle Database In-Memory features without purchasing the Oracle Database In-Memory option.
	When the Base Level is enabled, the value of the `INMEMORY_SIZE` initialization parameter is limited to 16 GB for a CDB. In an Oracle RAC environment, the value of `INMEMORY_SIZE` is limited to 16 GB for each instance. The compression level for all objects and columns is automatically and transparently set to `QUERY` `LOW`. Automatic In-Memory is disabled, and In-Memory Column Store feature tracking is tracked for "In-Memory Base Level" rather than "In-Memory Column Store." The CellMemory feature is disabled for Oracle Exadata.
- `CELLMEMORY_LEVEL`
	CellMemory is an Exadata feature that allows you to use Exadata Smart Flash Cache to populate data in in-memory columnar format. In older releases of Oracle Database, in order to use the CellMemory feature, you were required to enable the IM column store (by setting `INMEMORY_SIZE` to a value greater than `0`), even if you had no intention of using the IM column store. This incurred the overhead of enabling the IM column store without any benefit. Starting with Oracle Database release 19c, version 19.8, you can use the CellMemory feature without enabling the IM column store by setting `INMEMORY_FORCE=CELLMEMORY_LEVEL` and `INMEMORY_SIZE=0`. With these settings, the IM column store is not enabled and queries can use CellMemory to scan objects.
	Note that if the value of `INMEMORY_SIZE` is greater than `0`, then setting `INMEMORY_FORCE=CELLMEMORY_LEVEL` is equivalent to setting `INMEMORY_FORCE=DEFAULT`. The IM column store is enabled, even if you only use CellMemory.

See Also:

- " [INMEMORY\_CLAUSE\_DEFAULT](INMEMORY_CLAUSE_DEFAULT.md) "
- " [INMEMORY\_MAX\_POPULATE\_SERVERS](INMEMORY_MAX_POPULATE_SERVERS.md) "
- " [INMEMORY\_QUERY](INMEMORY_QUERY.md) "
- " [INMEMORY\_SIZE](INMEMORY_SIZE.md) "
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-BFA53515-7643-41E5-A296-654AB4A9F9E7) for an introduction to the IM column store
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-EEA265EE-8FBA-4457-8C3F-315B9EEA2224) for more information about the IM column store
- [Oracle Database Licensing Information User Manual](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBLIC-GUID-0F9EB85D-4610-4EDF-89C2-4916A0E7AC87) to learn which database offerings support the Database In-Memory Base Level feature