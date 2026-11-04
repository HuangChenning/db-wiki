---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PARALLEL_MIN_SERVERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.273 PARALLEL\_MIN\_SERVERS

These processes will be kept active to service parallel statements.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `CPU_COUNT * PARALLEL_THREADS_PER_CPU * 2` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | Default value to the value of `PARALLEL_MAX_SERVERS` |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

Note:

This parameter applies to parallel execution in exclusive mode as well as in an Oracle Real Application Clusters environment.

Note:

When the `PROCESSES` initialization parameter is set to a value that is lower than the documented default value for the `PARALLEL_MIN_SERVERS` parameter in the table above, the database sets the default value of `PARALLEL_MIN_SERVERS` to a value that is lower than the documented default value. The lower default value enables the database to start service processes and allows user processes to connect to the database.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11187) for more information about parallel execution servers