---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PARALLEL_FORCE_LOCAL.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.268 PARALLEL\_FORCE\_LOCAL

`PARALLEL_FORCE_LOCAL` controls parallel execution in an Oracle RAC environment.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |

By default, the parallel server processes selected to execute a SQL statement can operate on any or all Oracle RAC nodes in the cluster. By setting `PARALLEL_FORCE_LOCAL` to `true`, the parallel server processes are restricted so that they can only operate on the same Oracle RAC node where the query coordinator resides (the node on which the SQL statement was executed).

Note that, regardless of the value of this parameter, parallel server worker processes are spawned across Oracle RAC nodes for queries accessing `GV$` views and CDB\_\* views.

See Also:

[Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=VLDBG1485) for more information about this parameter