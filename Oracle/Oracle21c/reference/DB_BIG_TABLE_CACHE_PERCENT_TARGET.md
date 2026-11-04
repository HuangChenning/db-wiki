---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_BIG_TABLE_CACHE_PERCENT_TARGET.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.71 DB\_BIG\_TABLE\_CACHE\_PERCENT\_TARGET

`DB_BIG_TABLE_CACHE_PERCENT_TARGET` specifies the cache section target size for automatic big table caching, as a percentage of the buffer cache.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_BIG_TABLE_CACHE_PERCENT_TARGET =` `string` |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | Multiple instances can have different values, but it is recommended to keep the big table cache section size uniform. |

Automatic big table caching enables parallel queries and serial queries to use the buffer cache, which enhances the in-memory query capabilities of Oracle Database. Automatic big table caching is designed primarily to enhance performance for data warehouse workloads, but it also improves performance in mixed workloads.

Starting in Oracle Database 12c Release 1 (12.1.0.2), table scans can use a different algorithm in the following scenarios:

- Parallel queries:
	In single-instance and Oracle Real Application Clusters (Oracle RAC) databases, parallel queries can use the automatic big table cache when the `DB_BIG_TABLE_CACHE_PERCENT_TARGET` initialization parameter is set to a nonzero value, and the `PARALLEL_DEGREE_POLICY` initialization parameter is set to `AUTO` or `ADAPTIVE`.
- Serial queries:
	In a single-instance configuration only, serial queries can use the automatic big table cache when the `DB_BIG_TABLE_CACHE_PERCENT_TARGET` initialization parameter is set to a nonzero value.

When a nonzero value is specified for the `DB_BIG_TABLE_CACHE_PERCENT_TARGET` parameter, the value indicates the percentage of the buffer cache to reserve for the big table cache. The largest value that can be specified with the `DB_BIG_TABLE_CACHE_PERCENT_TARGET` parameter is 90, which reserves 10% of the buffer cache for usage besides table scans.

The default value of this parameter is `0`. Therefore, automatic big table caching is not enabled by default. When automatic big table caching is not enabled, queries might run using the least recently used (LRU) mechanism for cached reads, or might decide to use direct reads for the table scan.

If a large table is about the size of the combined size of the big table cache of all instances, the table will be partitioned and cached or mostly cached on all instances. With in-memory parallel query, this could eliminate most disk reads for queries on the table, or the database could intelligently read from disk only for the portion of the table that does not fit in the big table cache. If the big table cache cannot cache all the tables to be scanned, only the most frequently accessed tables will be cached, and the rest will be read via direct read automatically.

Use these guidelines when setting the parameter:

- If you do not enable automatic degree of parallelism (DOP) in your Oracle RAC environment, do not set this parameter because the big table cache is not used in that situation.
- When setting this parameter, consider the workload mix: how much of the workload is for OLTP; insert, update, and random access; and how much of the workload involves table scans. Because data warehouse workloads often perform large table scans, you may consider giving the big table cache section a higher percentage of buffer cache space for data warehouses.
- This parameter can be dynamically changed if the workload changes. The change could take some time to reach the target (depending on the current workload) because buffer cache memory might be actively used at that time.

Note:

Automatic big table caching uses temperature and object-based algorithms to track medium and big tables. Oracle will cache very small tables, but they will not be tracked by automatic big table caching.

See Also:

- " [PARALLEL\_DEGREE\_POLICY](PARALLEL_DEGREE_POLICY.md) "
- See " [V$BT\_SCAN\_CACHE](V-BT_SCAN_CACHE.md) " and " [V$BT\_SCAN\_OBJ\_TEMPS](V-BT_SCAN_OBJ_TEMPS.md) " for more information about the big table cache
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=VLDBG14145) for more information about this parameter and about automatic big table caching