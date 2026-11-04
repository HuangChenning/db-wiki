---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SORT_AREA_RETAINED_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.343 SORT\_AREA\_RETAINED\_SIZE

`SORT_AREA_RETAINED_SIZE` specifies (in bytes) the maximum amount of the user global area (UGA) memory retained after a sort run completes. The retained size controls the size of the read buffer, which Oracle uses to maintain a portion of the sort in memory. This memory is released back to the UGA, not to the operating system, after the last row is fetched from the sort space.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Derived from `SORT_AREA_SIZE` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM ... DEFERRED` |
| Modifiable in a PDB | Yes |
| Range of values | From the value equivalent of two database blocks to the value of `SORT_AREA_SIZE` |
| Basic | No |

Note:

Oracle does not recommend using the `SORT_AREA_RETAINED_SIZE` parameter unless the instance is configured with the shared server option. Oracle recommends that you enable automatic sizing of SQL working areas by setting `PGA_AGGREGATE_TARGET` instead. `SORT_AREA_RETAINED_SIZE` is retained for backward compatibility.

Oracle may allocate multiple sort spaces of this size for each query. Usually, only one or two sorts occur simultaneously, even for complex queries. In some cases, however, additional concurrent sorts are required, and each sort keeps its own memory area. If the shared server is used, allocation is to the SGA until the value in `SORT_AREA_RETAINED_SIZE` is reached. The difference between `SORT_AREA_RETAINED_SIZE` and `SORT_AREA_SIZE` is allocated to the PGA.

Note:

The default value as reflected in the `V$PARAMETER` dynamic performance view is 0. However, if you do not explicitly set this parameter, Oracle actually uses the value of the `SORT_AREA_SIZE` parameter.

See Also:

- " [SORT\_AREA\_SIZE](SORT_AREA_SIZE.md) "
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA610) for information on setting the values of this parameter and the `SORT_AREA_SIZE` parameter to tune sort operations using shared servers