---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INMEMORY_TRICKLE_REPOPULATE_SERVERS_PERCENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.159 INMEMORY\_TRICKLE\_REPOPULATE\_SERVERS\_PERCENT

`INMEMORY_TRICKLE_REPOPULATE_SERVERS_PERCENT` limits the maximum number of background populate servers used for In-Memory Column Store (IM column store) repopulation, as trickle repopulation is designed to use only a small percentage of the populate servers.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `0 to 50` |
| Basic | No |
| Oracle RAC | All instances should use the same value. |

The value for this parameter is a percentage of the `INMEMORY_MAX_POPULATE_SERVERS` initialization parameter value.

For example, if this parameter is set to 5 and `INMEMORY_MAX_POPULATE_SERVERS` is set to 10, then on average half of a core is used for trickle repopulation.

The default value of 1 is good in most cases. In some cases, if you want to disable trickle repopulate, this parameter can be set to 0. If you want to keep the system more aggressively up to date (at the expense of more background CPU), you can set the parameter to higher values such as 5 or 10.

A value of greater than 50 is not allowed, so that at least half of the populate servers are available for other (re)populate tasks. On some systems, a value of less than 50 can be problematic, depending on other workload.

This parameter has meaning only if the `INMEMORY_SIZE` parameter is also set to a positive value.