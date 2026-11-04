---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SORT_AREA_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.344 SORT\_AREA\_SIZE

`SORT_AREA_SIZE` specifies (in bytes) the maximum amount of memory Oracle will use for a sort.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `65536` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM ... DEFERRED` |
| Modifiable in a PDB | Yes |
| Range of values | Minimum: the value equivalent of six database blocks  Maximum: operating system-dependent |
| Basic | No |

Note:

Oracle does not recommend using the `SORT_AREA_SIZE` parameter unless the instance is configured with the shared server option. Oracle recommends that you enable automatic sizing of SQL working areas by setting `PGA_AGGREGATE_TARGET` instead. `SORT_AREA_SIZE` is retained for backward compatibility.

After the sort is complete, but before the rows are returned, Oracle releases all of the memory allocated for the sort, except the amount specified by the `SORT_AREA_RETAINED_SIZE` parameter. After the last row is returned, Oracle releases the remainder of the memory.

Increasing `SORT_AREA_SIZE` size improves the efficiency of large sorts.

Each sort in a query can consume memory up to the amount specified by `SORT_AREA_SIZE`, and there can be multiple sorts in a query. Also, if a query is executed in parallel, each PX server can consume memory up to the amount specified by `SORT_AREA_SIZE` for each sort it does.

`SORT_AREA_SIZE` is also used for inserts and updates to bitmap indexes. Setting this value appropriately results in a bitmap segment being updated only once for each DML operation, even if more than one row in that segment changes.

Larger values of `SORT_AREA_SIZE` permit more sorts to be performed in memory. If more space is required to complete the sort than will fit into the memory provided, then temporary segments on disk are used to hold the intermediate sort runs.

The default is adequate for most OLTP operations. You might want to adjust this parameter for decision support systems, batch jobs, or large `CREATE INDEX` operations.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT1237) for information on sort areas
- Your operating system-specific Oracle documentation for the default value on your system
- " [SORT\_AREA\_RETAINED\_SIZE](SORT_AREA_RETAINED_SIZE.md) "