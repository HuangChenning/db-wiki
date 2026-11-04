---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/HASH_AREA_SIZE.html
tags:
  - oracle
  - 12c
  - reference
---

`HASH_AREA_SIZE` specifies the maximum amount of memory, in bytes, to be used for hash joins.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Derived: 2 \* `SORT_AREA_SIZE` |
| Modifiable | `ALTER SESSION` |
| Modifiable in a PDB | No |
| Range of values | 0 to operating system-dependent |
| Basic | No |

Note:

Oracle does not recommend using the `HASH_AREA_SIZE` parameter unless the instance is configured with the shared server option. Oracle recommends that you enable automatic sizing of SQL working areas by setting `PGA_AGGREGATE_TARGET` instead. `HASH_AREA_SIZE` is retained for backward compatibility.

`HASH_AREA_SIZE` is relevant to parallel execution operations and to the query portion of DML or DDL statements.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT1242) for information on hash joins in general