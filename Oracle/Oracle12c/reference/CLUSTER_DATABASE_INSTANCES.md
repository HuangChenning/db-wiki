---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/CLUSTER_DATABASE_INSTANCES.html
tags:
  - oracle
  - 12c
  - reference
---

`CLUSTER_DATABASE_INSTANCES` is an Oracle RAC parameter that specifies the number of instances that are configured as part of the cluster database.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | If `CLUSTER_DATABASE` is set to `false`, then `1`  If `CLUSTER_DATABASE` is set to `true`, the number of configured Oracle RAC instances |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | Any nonzero value |
| Basic | No |
| Oracle RAC | Multiple instances should have the same value. |

You must set this parameter for every instance. Normally you should set this parameter to the number of instances in your Oracle RAC environment. A proper setting for this parameter can improve memory use.

See Also:

- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TGSQL94713) for more information about parallel execution
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=RACAD1111) for information on Oracle Real Application Clusters