---
title: PARALLEL_MIN_SERVERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams188.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM` |
| Range of values | 0 to value of `PARALLEL_MAX_SERVERS` |
| Oracle RAC | Multiple instances can have different values. |

Note:

This parameter applies to parallel execution in exclusive mode as well as in a Real Application Clusters environment.

`PARALLEL_MIN_SERVERS` specifies the minimum number of parallel execution processes for the instance. This value is the number of parallel execution processes Oracle creates when the instance is started.

Note:

When the `PROCESSES` initialization parameter is set to a value that is lower than the documented default value for the `PARALLEL_MIN_SERVERS` parameter in the table above, the database sets the default value of `PARALLEL_MIN_SERVERS` to a value that is lower than the documented default value. The lower default value enables the database to start service processes and allows user processes to connect to the database.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information on tuning parallel execution